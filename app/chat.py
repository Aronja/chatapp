from flask import Flask, request, render_template #What is request doing
app = Flask(__name__)

@app.route("/read")
def reading():
    return chat()

@app.route("/")
def layout():
    return render_template('layout.html')

@app.route("/write")
def writing():
    msg = request.args["msg"]
    chatwrite(msg)
    chatwrite("\n")
    return "I wrote a message"


def chat():
    x = open("chat.txt","r")
    return x.read()
def chatwrite(msg):
    x = open("chat.txt","a")
    return x.write("<p>" + msg + "</p>")


if __name__ == "__main__":
    app.run()
