from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

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


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))



# API
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
api.add_resource(HelloWorld, '/api/todo')


if __name__ == '__main__':
    db.create_all()

    # todo_instance = Todo(title="New todo title", completed=True)
    # db.session.add(todo_instance)
    # db.session.commit()

    app.run(debug=True)
