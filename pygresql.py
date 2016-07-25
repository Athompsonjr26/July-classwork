

#    ___         ___          __    ____  __
#   / _ \_   _  / _ \_ __ ___/ _\  /___ \/ /
#  / /_)/ | | |/ /_\/ '__/ _ \ \  //  / / /
# / ___/| |_| / /_\\| | |  __/\ \/ \_/ / /___
# \/     \__, \____/|_|  \___\__/\___,_\____/
#        |___/


import pg

# Connect to the PostgreSQL database
db = pg.DB(dbname='github')










# Make a query
query = db.query('select * from coder')












# If you need a multi-line query
query = db.query('''
    select
        *
    from
        projects
    where
        stars is not NULL
    order by
        stars desc
    limit
        10
''')













# 3 ways to get the result of the query

# 1. Get a list of tuples
>>> tupled_result = query.getresult()
[(1, 'Matthew Brimmer', 'mbrimmer1@gmail.com'), (2, 'David Pham', 'dpham@gmail.com')]












# 2. Get a list of dictionaries
>>> dictionaried_result = query.dictresult()
[{'id': 1, 'name': 'Matthew Brimmer', 'email': 'mbrimmer1@gmail.com'}, {'id': 2, 'name': 'David Pham', 'email': 'dpham@gmail.com'}]












# 3. Get a list of named-tuples, which are basically objects with attributes
>>> named_result = query.namedresult()
[Row(id=1, name='Matthew Brimmer', email='mbrimmer1@gmail.com'), Row(id=2, name='David Pham', email='dpham@gmail.com')












# TOBYS RECOMMENDATION
# --------------------
# I recommend query.namedresult() because it's most convinient (especially in an HTML template later) to access the individual columns of the query result: by using the dot notation like coder.name or coder.email. For example:

named_result = query.namedresult()
for coder in named_result:
    print "Coder: %s, Email: %s", (coder.name, coder.email)

















# The API for inserting data is

db.insert(TABLE_NAME, COLUMN1=VALUE1, COLUMN2=VALUE2)

# For example:

db.insert('coder', name='Anthony', email='anthony@gmail.com')














# The API for updating data is

db.update(table_name, dictionary)

# The dictionary needs to contain
# 1. the primary key of the object to be updated
# 2. the columns to be updated in that row

# Example:

db.update('coder', {'id': 1, 'name': 'Matt'})

# The above code will update the user with id = 1 and update his name to 'Matt'
