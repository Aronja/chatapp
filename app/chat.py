from flask import Flask, request, render_template, redirect #What is request doing
app = Flask(__name__)

@app.route("/read")
def reading():
    return chat()

@app.route("/")
def layout():
    return render_template('layout.html')

@app.route("/write")
def writing():
    name = request.args["name"]
    chatwrite(name)
    chatwrite(": ")
    msg = request.args["msg"]
    chatwrite(msg)
    chatwrite("\n")
    return redirect ("/")

@app.route("/test")
def testing():
    test = request.args["test"]
    performtesting(test)
    performtesting("\n")
    return redirect ("/testread")
    # msg = request.args["test"]
    # chatwrite(msg)
    # chatwrite("\n")
    # return redirect ("/")

@app.route("/testread")
def readingtest():
    return testread()


def chat():
    x = open("chat.txt","r")
    return x.read() # this is a function that is used for files
def chatwrite(msg):
    x = open("chat.txt","a")
    return x.write(msg)
def performtesting(test):
    y = open ("test.txt","a")
    return y.write(test)
def testread():
    y = open ("test.txt","r")
    return y.read()


if __name__ == "__main__":
    app.run()


#curl can be used for testing roots without a browser
#curl http://127.0.0.1:5000/test?test=funktioniertdas
#curl http://127.0.0.1:5000/read
#curl http://127.0.0.1:5000/read | grep hi
#curl https://atom.io/packages/comment | grep -i keyboard
