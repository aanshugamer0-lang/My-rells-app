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
        password = request.form['password']
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            error = 'गलत पासवर्ड या यूज़रनेम!'
    return f'''
    <body style="background:#121212;color:white;font-family:sans-serif;text-align:center;padding-top:100px;">
        <h2>🔐 Secure Video App Login</h2>
        <form method="post">
            <input type="text" name="username" placeholder="Username" required style="padding:10px;margin:5px;"><br>
            <input type="password" name="password" placeholder="Password" required style="padding:10px;margin:5px;"><br>
            <button type="submit" style="padding:10px 20px;background:#0095f6;color:white;border:none;cursor:pointer;">Login</button>
        </form>
        <p style="color:red;">{{error if error else ""}}</p>
    </body>
    '''

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
          
