import couchdb
couch = couchdb.Server('http://localhost5984/')
couchdb = 'gh'
db = couch[couchdb]
for id in db:
	db.delete(db[id])
