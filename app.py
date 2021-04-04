from flask import Flask, redirect, render_template, url_for, request

from models import Todo

app = Flask(__name__)

# Todo create, and list route
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        todo_content = request.form['content']
        todo_instance = Todo(content=todo_content)

        try:
            db.session.add(todo_instance)
            db.session.commit()
            return redirect('/')

        except:
            return "There was an error creating."
            
    else:
        todo_obj = Todo.query.order_by(Todo.date).all()
        return render_template('index.html')

@app.route('/me/<user>')
def me(user):
    return render_template('me.html', name= user)

@app.route('/about')
def about():
    return "I'm Sagor from Dhaka, Bangladesh"

@app.route('/hello/<name>')
def sayHello(name):
    return f"Hello {name}!"

@app.route('/task/<int:taskId>')
def taskList(taskId):
    return f"Task id {taskId}"

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return f"Hello {guest}"

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))


# run the project on local dev server
if __name__ == '__main__':
    app.run(debug=True)
