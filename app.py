from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    response = requests.get('http://127.0.0.1:8000/users') 
    users = response.json()
    return render_template('users.html', users=users)

@app.route('/comments')
def comments():
    response = requests.get('http://127.0.0.1:8000/comments') 
    comments = response.json()
    return render_template('comments.html', comments=comments)

@app.route('/posts')
def posts():
    response = requests.get('http://127.0.0.1:8000/posts') 
    posts = response.json()
    return render_template('posts.html', posts=posts)

@app.route('/todos')
def todos():
    response = requests.get('http://127.0.0.1:8000/todos') 
    todos = response.json()
    return render_template('todos.html', todos=todos)
if __name__ == '__main__':
    app.run(debug=True)