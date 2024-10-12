from flask import Flask, render_template, send_from_directory,request, Response
from flask import jsonify
import os
import requests

app = Flask(__name__)



@app.route('/')
def renderHome():
    return render_template("home.html")

@app.route("/hybridFarm")
def renderAboutHybridFarm():
    return render_template("hybridFarm.html", companyName="Stealth")

@app.route("/hybridFarm/PlayhybridFarm")
def playHybridFarm():
    return render_template("index.html")



if __name__ == "__main__":
    #print ("the name is The MAIN")
    #app.run(host='0.0.0.0',debug=True)  #for running within a private network
    app.run(host='0.0.0.0',debug=True)
