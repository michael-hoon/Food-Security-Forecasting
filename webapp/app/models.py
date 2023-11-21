from app import db
from app import login
from datetime import datetime 

class Variables(db.Model):
    __tablename__ = 'variables'
    id = db.Column(db.Integer, primary_key=True)
    population = db.Column(db.Float)
    infant_mortality = db.Column(db.Float)
    hdi = db.Column(db.Float)
    gini_index = db.Column(db.Float)
    temperature = db.Column(db.Float)
	    
    def __repr__(self):
        return f'<Question>'
