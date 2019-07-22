from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("template.html", msg="Hello, World!!!!!!!!!!")

if __name__ == "__main__":
    app.run(debug=True)
