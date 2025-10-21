# Timestamp Logger (Multithreaded)

This project demonstrates how to use multithreading and network requests in Python to log timestamps with corresponding dates.

## Features
- Runs 10 threads, each active for 20 seconds.
- Each thread logs one entry per second.
- Data requested from Flask server (`server.py`).
- Logs are written to `logs.txt`, sorted by timestamp.

## How to Run

### 1. Run the server:
```bash
python server.py

