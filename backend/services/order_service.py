from repositories.order_repository import OrdersRepository
from models import Orders

class OrderService:
    @staticmethod
    def get_all_orders():
        return OrdersRepository.find_all()
    
    @staticmethod
    def get_order_by_id(order_id):
        return OrdersRepository.find_by_id(order_id)
    
    @staticmethod
    def create_order(order_data):
        # Convert discounted to boolean, handling empty strings
        discounted = order_data.get('discounted', False)
        if discounted == '' or discounted is None:
            discounted = False
        
        order = Orders(
            orderName=order_data.get('orderName'),
            price=order_data.get('price'),
            isDiscounted=bool(discounted)
        )
        return OrdersRepository.save(order)
    
    @staticmethod
    def update_order(order_id, order_data):
        existing_order = OrdersRepository.find_by_id(order_id)
        
        if not existing_order:
            return None
        
        existing_order.orderName = order_data.get('orderName', existing_order.orderName)
        existing_order.price = order_data.get('price', existing_order.price)
        existing_order.isDiscounted = order_data.get('discounted', existing_order.isDiscounted)
        
        return OrdersRepository.update(existing_order)
    
    @staticmethod
    def delete_order(order_id):
        return OrdersRepository.delete(order_id)
    
    @staticmethod
    def get_total_bill():
        return OrdersRepository.total_bill()
    
    @staticmethod
    def get_discounted_bill():
        return OrdersRepository.discounted_bill()
