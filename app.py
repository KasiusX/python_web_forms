from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == '123':
            return 'logged in'
        else:
            return 'Access denied'

        return 'username: ' + username + ' password ' + password
    else:
        return render_template('login.html')


@app.route('/name', methods=['GET','POST'])
def name():
    name = ''
    if request.method == 'POST':
        name = request.form['name']

    return render_template('name.html',name=name)