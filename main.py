from flask import Flask, render_template

app = Flask(__name__)

app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

app.route("/add<int:a><int:b>", methods=["POST"])
def add(a, b):
    return {"message":"sum of {a} and {b} is :{a + b}"}


if __name__ == "__main__":
    app.run(debug=True)
