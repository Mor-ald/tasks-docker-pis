import mongo
from datetime import datetime

from flask import Flask

connection = mongo.connect('mongo-swarm', 27017, 'mongodbuser', 'your_mongodb_root_password')
database = mongo.use(connection, '1')
collection = mongo.pick_collection(database, '1')
  
app = Flask(__name__)

def get_hit_count():
  db_table = mongo.find_document(collection, {})
  if (db_table and 'count' in db_table):
    mongo.update_document(collection, { '_id': db_table['_id'] }, { 'count': int(db_table['count']) + 1 , 'time': datetime.now() })
    return db_table['count'] + 1
  else:
    mongo.insert_document(collection, { 'count': 1 , 'time': datetime.now() })
    return 1

@app.route('/')
def hello():
  count = get_hit_count()
  return 'Counter: {} .\n'.format(count)
