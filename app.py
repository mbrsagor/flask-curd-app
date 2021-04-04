from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    completed = db.Column(db.Boolean)

@app.route('/')
def index():
    todo_list = Todo.query.all()
    # print(todo_list)
    return render_template('base.html', todo_list=todo_list)

@app.route('/add')
def add_todo():
    title = request.get("title")
    todo_instance = Todo(title=title, completed=False)
    db.session.add(todo_instance)
    db.session.commit()

if __name__ == '__main__':
    db.create_all()

    # todo_instance = Todo(title="New todo title", completed=True)
    # db.session.add(todo_instance)
    # db.session.commit()

    app.run(debug=True)


# CBS
# Circle
