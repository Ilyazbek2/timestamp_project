from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/timestamp/<int:ts>")
def get_time(ts: int):
    """Return readable date for given timestamp."""
    dt = datetime.fromtimestamp(ts)
    return dt.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
