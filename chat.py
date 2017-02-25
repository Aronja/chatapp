from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def reading():
    return chat()

@app.route("/write")
def writing():
    msg = request.args["msg"]
    return chatwrite(msg)


def chat():
    x = open("chat.txt","r")
    return x.read()
def chatwrite(msg):
    x = open("chat.txt","a")
    return x.write(msg)

if __name__ == "__main__":
    app.run()
