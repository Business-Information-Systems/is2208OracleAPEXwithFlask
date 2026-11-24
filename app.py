from flask import Flask, render_template, request, flash
from studentDao import StudentDao
app = Flask(__name__)

#Secret key needed to prevent cross site request forgeries (CSRF).
app.config['SECRET_KEY'] = '7aef297a334740e8fbbe092f0e1581e1967c05d3f8f7fba8'

#Creating a StudentDao() object authenticates us with Oracle APEX
#and generates a token. Tokens last for an hour before expiring.
studentDao = StudentDao()

#We use a single web page to do everything. No redirects needed.
@app.route('/', methods = ('GET', 'POST'))
def read_or_create():
    if request.method == 'POST':
        name = request.form['name']
        if not name:
            flash('Name is required!')
        else:
            studentDao.add_student(name)
    #Read all students from Oracle APEX every time the page is loaded.
    return render_template("index.html",items=studentDao.get_students())

if __name__ == '__main__':
    app.run()
