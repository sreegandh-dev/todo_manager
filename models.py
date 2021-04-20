from forms import db
from datetime import datetime


# declared 5 variables which make up as the major component for a task
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    details = db.Column(db.String(1000), nullable=False)
    complete = db.Column(db.Boolean)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Task %r>' % self.id
