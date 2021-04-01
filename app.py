from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

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
    app.run()
