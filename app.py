import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    registration_number = db.Column(db.String(80), unique=False, nullable=True, primary_key=False)
    name = db.Column(db.String(80), unique=False, nullable=True, primary_key=False)
    email = db.Column(db.String(80), unique=False, nullable=True, primary_key=False)
    date_of_birth = db.Column(db.String(80), unique=False, nullable=True, primary_key=False)
    hometown = db.Column(db.String(80), unique=False, nullable=True, primary_key=False)
    score = db.Column(db.Float, unique=False, nullable=True, primary_key=False)

    def __repr__(self):
        return "[id: {}, registration_number: {}, name: {}, email: {}, date_of_birth: {}, hometown: {}, score: {} ]".format(self.id, self.registration_number, self.name, self.email, self.date_of_birth, self.hometown, self.score)

@app.route("/", methods=["GET", "POST"])
def home():
    students = None
    if request.form:
        try:
            score = request.form.get("score")
            if score == '' :
                score = 0
            student = Student(
                registration_number=request.form.get("registration_number"), 
                name=request.form.get("name"),
                email=request.form.get("email"),
                date_of_birth=request.form.get("date_of_birth"),
                hometown=request.form.get("hometown"),
                score= score
            )
            db.session.add(student)
            db.session.commit()
        except Exception as e:
            print("Failed to add student")
            print(e)
    students = Student.query.all()
    return render_template("home.html", students=students)


@app.route("/update", methods=["POST"])
def update():
    try:
        id = request.form.get("id")
        name = request.form.get("name")
        registration_number = request.form.get("registration_number")
        email = request.form.get("email")
        date_of_birth = request.form.get("date_of_birth")
        hometown = request.form.get("hometown")
        score = request.form.get("score")

        student = Student.query.filter_by(id=id).first()
        student.name = name
        student.registration_number = registration_number
        student.email = email
        student.date_of_birth = date_of_birth
        student.hometown = hometown
        student.score = score
        db.session.commit()
    except Exception as e:
        print("Couldn't update student title")
        print(e)
    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete():
    id = request.form.get("id")
    student = Student.query.filter_by(id=id).first()
    db.session.delete(student)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    db.create_all()
    app.run(host='127.0.0.1', port=8087, debug=True)
