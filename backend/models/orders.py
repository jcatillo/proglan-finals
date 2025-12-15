from models import db

class Orders(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    orderName = db.Column(db.String(255), nullable=False)
    price = db.Column(db.DECIMAL(10, 2), nullable=False)
    isDiscounted = db.Column(db.Boolean, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'orderName': self.orderName,
            'price': float(self.price),
            'isDiscounted': self.isDiscounted
        }