from couchdb import Server

# Go to http://localhost:5984/_utils to create the database.

def create(dbname, username, password, type='user'):
    db = Server()[dbname]
    db.create({'type': type, 'username': username, 'password': password})
