# Now we also need the request object
# Also using redirect
from flask import Flask, render_template, request, redirect
import pg

db = pg.DB(dbname='github')

app = Flask('MyFormApp')

@app.route('/')
def form():
    # Render the form.html template
    return render_template(
        'form.html',
        title='Enter new project')

# This URL receives the form submit and processes it
@app.route('/submit_form', methods=['POST'])
def submit_form():
    project_name = request.form['project_name']
    project_description = request.form['project_description']
    db.insert('project', name=project_name, description=project_description)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
