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
        return render_template(
            "/add.html", message="Thank you for adding a student."
        )  # noqa: E501
    else:
        return render_template("/add.html")


@app.route("/students.html", methods=["POST", "GET"])
def students():
    if request.method == "POST":
        id = request.form["id"]
        dbHandler.deleteStudent(id)
    return render_template(
        "/students.html", studentList=dbHandler.listStudents()
    )  # noqa: E501


@app.route("/marks.html", methods=["POST", "GET"])
def studentMarks():
    if request.method == "POST":
        id = request.form["id"]
        dbHandler.deleteStudentMark(id)
    return render_template(
        "/marks.html", studentMarksList=dbHandler.listStudentMarks()
    )  # noqa: E501


@app.route("/addMark.html", methods=["POST", "GET"])
def addMark():
    if request.method == "POST":
        StudentId = request.form["StudentId"]
        Subject = request.form["Subject"]
        Mark = request.form["Mark"]
        dbHandler.insertStudentMark(StudentId, Subject, Mark)
        return render_template(
            "/addMark.html", message="Thank you for adding a student's mark."
        )  # noqa: E501
    else:
        return render_template("/addMark.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
