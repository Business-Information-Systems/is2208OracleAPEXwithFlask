from flask import Flask, render_template
from studentDao import StudentDao
app = Flask(__name__)
studentDao = StudentDao()

@app.route('/')
def hello_world():  # put application's code here
    students = studentDao.get_students()
    return render_template("index.html",items=students)

if __name__ == '__main__':
    app.run()
