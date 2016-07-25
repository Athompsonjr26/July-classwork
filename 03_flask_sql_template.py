# Now we also need the render_template function
from flask import Flask, render_template
import pg

db = pg.DB(dbname='github')

app = Flask('MyApp')

@app.route('/')
def projects():
    # Query the database
    query = db.query('''
        select * from project
        order by stars desc limit 10
    ''')
    # use the template to build up HTML to be sent
    # to the browser
    return render_template(
        'top10.html',
        title='Top 10 Projects',
        projects=query.namedresult())

# Start the server if this file is run as a script on the command line
if __name__ == '__main__':
    # run the server in debug mode, which will automatically
    # restart the server for you on save
    app.run(debug=True)
