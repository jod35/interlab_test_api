from labtest import db
from datetime import datetime

#the user table in our database
class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    public_id=db.Column(db.String(255),nullable=False)
    labname=db.Column(db.String(255),nullable=False)
    labrep=db.Column(db.String(255),nullable=False)
    email=db.Column(db.String(255),nullable=False)
    pasword=db.Column(db.String(255),nullable=False)
    image=db.Column(db.String(255))
    accredited=db.Column(db.Boolean())
    requests=db.relationship('Request',backref='provider',lazy=True)
    payments=db.relationship('Payments',backref='payer',lazy=True)
    def __repr__(self):
        return '{}'.format(self.labname)
    

class Sample(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    sample_id = db.Column(db.String(255),nullable=False)
    test_type=db.Column(db.String(255),nullable=False)

    def __repr__(self):
        return '{}'.format(self.sample_id)


class Request(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    sample_id=db.Column(db.String(255),nullable=False)
    provider=db.Column(db.Integer(),db.ForeignKey('user.id'))
    test_sample=db.Column(db.Integer(),db.ForeignKey('sample.id'))
    request_time=db.Column(db.DateTime(),default=datetime.utcnow)
    paid_for=db.Column(db.Boolean(),default=False)
    # payment_info=db.relationship('Payment',backref='request',lazy=True)
    requestor=db.Column(db.Integer(),db.ForeignKey('user.id'))

    def __repr__(self):
        return 'sample {}'.format(self.id)

class Payment(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    sample_id=db.Column(db.Integer(),db.ForeignKey('sample.id'))
    request_id=db.Column(db.Integer(),db.ForeignKey('request.id'))
    user_id=db.Column(db.Integer(),db.ForeignKey('user.id'))
    payment_amount=db.Column(db.Integer())
    def __repr__(self):
        return 'Payment {}'.format(self.id)
