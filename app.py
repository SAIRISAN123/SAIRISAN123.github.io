from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def renderHome():
    return render_template("home.html")


if __name__ == "__main__":
    #print ("the name is The MAIN")
    #app.run(host='0.0.0.0',debug=True)  #for running within a private network
    app.run(host='0.0.0.0',debug=True)
