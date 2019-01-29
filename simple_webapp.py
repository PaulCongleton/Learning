from flask import Flask, session

from checker import check_logged_in

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello from simple webapp.  '

@app.route('/page1')
@check_logged_in
def page1() -> str:
    return 'this is page 1.  '

@app.route('/page2')
@check_logged_in
def page2() -> str:
    return 'this is page 2.  '

@app.route('/page3')
@check_logged_in
def page3() -> str:
    return 'this is page 3.  '

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in. '

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are no longer logged in.  '

app.secret_key = 'YouWillNeverGuess'

if __name__ == '__main__':
    app.run(debug  = True)