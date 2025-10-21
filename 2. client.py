import threading
import time
import requests
from queue import Queue

LOG_FILE = "logs.txt"
URL = "http://127.0.0.1:8080/timestamp/"
q = Queue()
lock = threading.Lock()

def log_writer():
    """Thread that writes log entries from the queue into a file."""
    with open(LOG_FILE, "w") as f:
        while True:
            item = q.get()
            if item is None:  # Stop signal
                break
            with lock:
                f.write(f"{item[0]} {item[1]}\n")
                f.flush()
            q.task_done()

def worker(thread_id: int):
    """Each thread logs one entry per second for 20 seconds."""
    start = time.time()
    while time.time() - start < 20:
        ts = int(time.time())
        try:
            r = requests.get(f"{URL}{ts}")
            if r.ok:
                q.put((ts, r.text.strip()))
                print(f"[Thread-{thread_id}] Logged {ts} {r.text.strip()}")
        except Exception as e:
            print(f"[Thread-{thread_id}] Error: {e}")
        time.sleep(1)

def main():
    writer = threading.Thread(target=log_writer)
    writer.start()

    threads = []
    for i in range(10):
        t = threading.Thread(target=worker, args=(i + 1,))
        t.start()
        threads.append(t)
        time.sleep(1)

    for t in threads:
        t.join()

    q.put(None)
    writer.join()
    print("✅ All threads finished. Logs written to logs.txt")

if __name__ == "__main__":
    main()
