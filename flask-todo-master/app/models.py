from app import db
from datetime import datetime

class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mytodolist = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, mytodolist):
        self.mytodolist = mytodolist

    def __repr__(self):
        return '[%s,%s]' % (self.id, self.mytodolist)
    
    
