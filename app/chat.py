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



def chat():
    x = open("chat.txt","r")
    return x.read() # this is a function that is used for files
def chatwrite(msg):
    x = open("chat.txt","a")
    return x.write(msg)


if __name__ == "__main__":
    app.run()

#curl can be used for testing roots without a browser
#curl http://127.0.0.1:5000/write?msg=funktioniertdas
#curl http://127.0.0.1:5000/read
#curl http://127.0.0.1:5000/read | grep hi
#curl https://atom.io/packages/comment | grep -i keyboard
