import json
import logging
from database import init_db, insert_order
from utils import parse_order

# Настройка логирования с правильной кодировкой UTF-8
logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'  # Добавляем правильную кодировку
)

def load_json_data(file_path):
    logging.info(f"Начало загрузки данных из файла {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        logging.info("Данные успешно загружены из JSON")
        return data
    except Exception as e:
        logging.error(f"Ошибка при загрузке JSON: {e}")
        raise

def main():
    logging.info("Запуск скрипта загрузки заказов")
    init_db()

    orders = load_json_data('data/ozon_orders.json')

    for order in orders:
        parsed_order = parse_order(order)
        if parsed_order:
            insert_order(parsed_order)

    logging.info("Завершение работы скрипта")

if __name__ == "__main__":
    main()