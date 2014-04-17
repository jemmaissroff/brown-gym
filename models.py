from google.appengine.ext import db

class Running(db.Model):
    running = db.StringProperty(required = True)
    time = db.DateTimeProperty(auto_now_add = True)