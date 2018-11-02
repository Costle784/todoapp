from app import db
from sqlalchemy.sql import func

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    content = db.Column(db.String(200)) 
    complete = db.Column(db.Boolean, default=False) 
    created = db.Column(db.DateTime(timezone=True), server_default=func.now())