import sqlite3
import logging

DB_PATH = 'db/orders.db'

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    logging.info("Инициализация базы данных")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            status TEXT,
            date TEXT,
            amount REAL,
            customer_region TEXT
        )
    ''')
    conn.commit()
    conn.close()
    logging.info("База данных инициализирована")

def order_exists(order_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM orders WHERE order_id = ?", (order_id,))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists

def insert_order(order):
    if order_exists(order['order_id']):
        logging.info(f"Заказ {order['order_id']} уже существует, пропускаем")
        return

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO orders (order_id, status, date, amount, customer_region)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            order['order_id'],
            order['status'],
            order['date'],
            order['amount'],
            order['customer_region']
        ))
        conn.commit()
        logging.info(f"Заказ {order['order_id']} успешно добавлен")
    except Exception as e:
        logging.error(f"Ошибка при вставке заказа {order['order_id']}: {e}")
    finally:
        conn.close()