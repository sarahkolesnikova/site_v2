from flask import Flask
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/research')
def research():
    return render_template('research1.html')

@app.route('/act')
def act():
    return render_template('act.html')

@app.route('/tls')
def tls():
    return render_template('tls.html')

@app.route('/team')
def team():
    return render_template('team.html', page_title='Our Team')

@app.route('/publications')
def publications():
    return render_template('publications.html', page_title='Publications')

@app.route('/awards')
def awards():
    return render_template('awards.html', page_title='Awards')

@app.route('/join-us')
def join_us():
    return render_template('join_us.html', page_title='Join Us')

if __name__ == '__main__':
    app.run()