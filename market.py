from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!!</h1>'

@app.route('/about/<username>')
def about_page(username):
    return f'<h1>Hello Welcome to {username}\'s About Page</h1>'

if __name__ == '__main__':
    app.run(debug=True)

