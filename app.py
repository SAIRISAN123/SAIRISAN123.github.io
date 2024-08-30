from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hi This is Sai!!!!</p>"


if __name__ == "__main__":
    #print ("the name is The MAIN")
    #app.run(host='0.0.0.0',debug=True)  #for running within a private network
    app.run(debug=True)
