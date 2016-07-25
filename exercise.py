import pg

# Connect to the PostgreSQL database
db = pg.DB(dbname='exercise_db')

tech_name = raw_input('enter tech name:')
# tech_id = raw_input('enter tech id:')
# 1
query = db.query('select * from tech')
print query # shows you the data

#2
db.insert('tech', name= tech_name)

#3
db.update('tech', {'id': 1, 'name': 'Java'})

#4
db.delete('tech', {'id': 22})














# named_result = query.namedresult()
# for project in named_result:
#     print "Project: %s" % (project.name)
# db.insert()

# db.insert('project', name='Anthony')

# db.update('project', {'id':14, 'name':'Anthonys' })
