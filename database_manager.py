import sqlite3 as sql


def listExtension():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM extension").fetchall()
    con.close()
    return data


def insertStudent(firstname, lastname, dob):
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO Students (firstname, lastname, dob) VALUES (?,?,?)",
        (firstname, lastname, dob),
    )
    con.commit()
    con.close()


def listStudents():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM Students").fetchall()
    con.close()
    return data


def deleteStudent(id):
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    print(id)
    cur.execute("DELETE FROM Students WHERE id=?", (id,))
    con.commit()
    con.close()


def listStudentMarks():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM StudentMarks").fetchall()
    con.close()
    return data


def insertStudentMark(StudentId, Subject, Mark):
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO StudentMarks (StudentId, Subject, Mark) VALUES (?,?,?)",
        (StudentId, Subject, Mark),
    )
    con.commit()
    con.close()


def deleteStudentMark(id):
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    print(id)
    cur.execute("DELETE FROM StudentMarks WHERE id=?", (id,))
    con.commit()
    con.close()
