import os
from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

class MongoRepository(object):
 def __init__(self):
   mongo_url = os.environ.get('MONGO_URL')
   self.db = MongoClient(mongo_url).kudos

 def find_all(self, selector):
   return self.db.kudos.find(selector)
 
 def find(self, selector):
   return self.db.kudos.find_one(selector)
 
 def create(self, kudo):
   return self.db.kudos.insert_one(kudo)

 def update(self, selector, kudo):
   return self.db.kudos.replace_one(selector, kudo).modified_count
 
 def delete(self, selector):
   return self.db.kudos.delete_one(selector).deleted_count