from flask import Flask, render_template, request, redirect, url_for
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


@app.route("/add", methods=["POST"])
def add_todo():
    title = request.form.get("title")
    todo_instance = Todo(title=title, completed=False)
    db.session.add(todo_instance)
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/update/<int:todo_id>")
def update_todo(todo_id):
    todo_instance = Todo.query.filter(id=todo_id).first()
    todo_instance.completed = not todo_instance.completed
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()

    # todo_instance = Todo(title="New todo title", completed=True)
    # db.session.add(todo_instance)
    # db.session.commit()

    app.run(debug=True)
