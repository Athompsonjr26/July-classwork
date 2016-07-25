# the Flask class from the flask module
from flask import Flask
import pg

db = pg.DB(dbname='github')

app = Flask('MyApp')

@app.route('/')
def projects():
    # Query the database
    query = db.query('''
        select * from project
        where stars is not NULL
        order by stars desc limit 10
    ''')
    # built up the HTML for a list of projects and send it back
    # to the browser
    html = '<ul>'
    for project in query.namedresult():
        html += '<li>%s - %d stars</li>' % (project.name, project.stars)
    html += '</ul>'
    return html

# Start the server if this file is run as a script on the command line
if __name__ == '__main__':
    # run the server in debug mode, which will automatically
    # restart the server for you on save
    app.run(debug=True)
