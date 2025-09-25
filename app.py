from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "これはホームページです！"

@app.route("/hello")
def hello():
    return "こんにちは、Render！"

@app.route("/about")
def about():
    return "これはAboutページです！"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
