
from flask import Flask, session, request, render_template, redirect

import pg

db = pg.DB(dbname='restaurants_db')

app = Flask('MyApp')

@app.route('/')
def home():

    if 'name' in session:

        return render_template('session-hello.html', name=session['name'])
    else:
        return render_template('session-get-name.html')

@app.route('/submit_name', methods=['POST'])
def submit_name():

    session['name'] = request.form['name']
    return redirect('/')

def get_name():
    session['name'] = request.form['name']
    return redirect('/')

@app.route('/clear_name')
def clear_name():

    del session['name']
    return redirect('/')


app.secret_key = 'CSF686CCF85C6FRTCHQDBJDXHBHC1G478C86GCFTDCR'

if __name__ == '__main__':
    app.run(debug=True)
