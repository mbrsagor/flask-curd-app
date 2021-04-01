from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/about')
def about():
    return "I'm Sagor from Dhaka, Bangladesh"


if __name__ == '__main__':
    app.run()
