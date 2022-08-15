from ... import db



class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary=True)
    name = db.Column(db.String(255))
    author = db.Column(db.String(255))
    price = db.Column(db.Integer)
