from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return chat()


def chat():
    x = open("chat.txt","r")
    return x.read()


if __name__ == "__main__":
    app.run()
