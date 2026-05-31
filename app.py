from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'super_secret_secure_key_123'

USER_CREDENTIALS = {
    "admin": "mysecretpassword"
}

@app.route('/')
def home():
    if 'logged_in' in session:
        return render_template('reels.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.
