from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from datetime import timedelta
import os, datetime


app = Flask(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(seconds=30)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session.permanent = True
        session['username'] = 'admin'
        session['time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        session['logged_in'] = True
        return "logged in as " + session['username'] + " " + session['time']
    else:
        flash('wrong password!')
        return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0')