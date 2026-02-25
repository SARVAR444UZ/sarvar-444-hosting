from flask import Flask
import os

app = Flask(__name__)

@app.get("/")
def index():
    # Bu kod sening index.html faylingni o'qib internetga chiqaradi
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
