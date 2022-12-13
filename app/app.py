import mongo
from datetime import datetime

from flask import Flask
from flask import request

connection = mongo.connect('mongo', 27017, 'mongodbuser', 'your_mongodb_root_password')
database = mongo.use(connection, '1')
collection = mongo.pick_collection(database, '1')
  
app = Flask(__name__)

def get_hit_count():
  dbTable = mongo.find_document(collection, {})
  if (dbTable and 'count' in dbTable):
    mongo.update_document(collection, { '_id': dbTable['_id'] }, { 'count': int(dbTable['count']) + 1 , 'time': datetime.now(), 'User-Agent': request.headers.get('User-Agent') })
    return dbTable
  else:
    mongo.insert_document(collection, { 'count': 1 , 'time': datetime.now(), 'User-Agent': request.headers.get('User-Agent') })
    return { 'count': 0 , 'time': datetime.now(), 'User-Agent': request.headers.get('User-Agent') }

# print response 
@app.route('/')
def hello():
  res = get_hit_count()
  return 'Counter: {} \n'.format(res['count']) + ' || ' + 'Time: {} .\n'.format(res['time']) + ' || ' + 'User: {} .\n'.format(res['User-Agent'])

# delete data in mongodb
@app.route('/delete')
def delete():
  mongo.delete_document(collection, {})
  return 'delete all data'
