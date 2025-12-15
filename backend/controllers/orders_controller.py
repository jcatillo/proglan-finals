from flask import Blueprint, request, jsonify
from services import OrderService

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/add-order', methods=['POST'])
def add_order():
    order = request.get_json()

    if not order or not order.get('orderName') or not order.get('price'):
        return jsonify({'success': False, 'message': 'Please enter all required fields'}), 400
    
    entity = OrderService.create_order(order)

    return jsonify({'success': True, 'message': 'Order Successfully added', 'data' : entity.to_dict()}), 201

@order_bp.route('/orders', methods=['GET'])
def get_all_orders():
    orders = OrderService.get_all_orders()
    orders_data = [order.to_dict() for order in orders]

    return jsonify({'message': 'Orders successfully fetched', 'data': orders_data}), 200

@order_bp.route('/total-bill', methods=['GET'])
def get_total_bill():
    total = OrderService.get_total_bill()
    discount = OrderService.get_discounted_bill()

    return jsonify({
        'message': 'Bill successfully fetched',
        'data': {
            'regularBillTotal': total,
            'discountedBillTotal': discount
        }
    }), 200


@order_bp.route('/update/<int:id>', methods=['PUT'])
def update_order(id):
    order_data = request.get_json()

    if not order_data:
        return jsonify({'success': False, 'message': 'No updatable fields found in the request'}), 400
    
    updated = OrderService.update_order(id, order_data)

    if not updated:
        return jsonify({'success': False, 'message': f'Order {id} not found'}), 404
    
    return jsonify({'success': True, 'message': f'Order {id} Updated', 'data': updated.to_dict()}), 200

@order_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = OrderService.get_order_by_id(id)

    if not order:
        return jsonify({'success': False, 'message': 'Order Id {id} not found'}), 404
    
    deleted = OrderService.delete_order(id)
    
    return jsonify({'success': True, 'message': f'Order ID: {id} deleted', 'data': deleted.to_dict()}), 200

    return jsonify({'message': 'Order ID: {id} deleted', 'data': deleted.to_dict()}), 204