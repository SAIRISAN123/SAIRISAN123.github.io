from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        "title": "Software Engineer",
        "salary": "Rs. 1,000,000",
        "location": "Mountain View, CA",
        "description": "Work with a team of engineers to build software products for Google."
    },
    {
        "title": "Network Engineer",
        "salary": "Rs. 800,000",
        "location": "Menlo Park, CA",
        "description": "Lead a team of engineers to build network for Facebook"
    },
    {
        "title": "Data Scientist",
        "salary": "Rs. 1,200,000",
        "location": "San Francisco, CA",
        "description": "Analyze data to discover insights about Twitter users."
    }
]

@app.route("/")
def renderHome():
    return render_template("home.html", jobs=JOBS, companyName="Stealth")


if __name__ == "__main__":
    #print ("the name is The MAIN")
    #app.run(host='0.0.0.0',debug=True)  #for running within a private network
    app.run(host='0.0.0.0',debug=True)
