from models import db, Orders

class OrdersRepository:
    @staticmethod
    def find_all():
        return Orders.query.all()
    
    @staticmethod
    def find_by_id(orderId):
        return Orders.query.get(orderId)
    
    @staticmethod
    def save(order: Orders):
        db.session.add(order)
        db.session.commit()

        return order
    
    @staticmethod
    def update(order: Orders):
        target: Orders = Orders.query.get(order.id)

        if not target:
            return None
        
        target.orderName = order.orderName
        target.price = order.price
        target.isDiscounted = order.isDiscounted

        db.session.commit()
        return target
    
    @staticmethod
    def delete(orderId):
        target = Orders.query.get(orderId)

        if not target:
            return None
        
        db.session.delete(target)
        db.session.commit()
        
        return target
    
    @staticmethod
    def total_bill():
        orders = Orders.query.all()
        total = sum(float(order.price) for order in orders)
        return total
    
    @staticmethod
    def discounted_bill():
        orders = Orders.query.all()
        total = 0
        for order in orders:
            if order.isDiscounted:
                total += float(order.price) * 0.95  # Apply 5% discount
            else:
                total += float(order.price)
        return total
