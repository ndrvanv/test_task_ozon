import logging

def parse_order(order):
    try:
        return {
            'order_id': order['order_id'],
            'status': order['status'],
            'date': order['date'],
            'amount': order['amount'],
            'customer_region': order['customer']['region']
        }
    except KeyError as e:
        logging.error(f"Ошибка при парсинге заказа {order.get('order_id')}: отсутствует поле {e}")
        return None