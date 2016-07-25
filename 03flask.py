from flask import Flask

db = pg.DB(dbname='exercise_db')

app = Flask('MyApp')

@app.route('/')
def projects():

    query = db.query('''
        select * from project
    ''')

    return render_template(
        'top10.html',
        title='Top Projects',
        projects=query.namedresult())

if __name__ == '__main__':

    app.run(debug=True)
