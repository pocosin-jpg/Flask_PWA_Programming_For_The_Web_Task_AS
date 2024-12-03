from flask import Flask
from flask import render_template
from flask import request
import database_manager as dbHandler

app = Flask(__name__)


@app.route("/index.html", methods=["GET"])
@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("/index.html", content=dbHandler.listExtension())


@app.route("/add.html", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        dob = request.form["dob"]
        dbHandler.insertStudent(firstname, lastname, dob)
        return render_template("/add.html", message="Thank you for adding a student.")
    else:
        return render_template("/add.html")


@app.route("/students.html", methods=["POST", "GET"])
def students():
    if request.method == "POST":
        id = request.form["id"]
        dbHandler.deleteStudent(id)
    return render_template("/students.html", studentList=dbHandler.listStudents())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
