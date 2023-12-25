import queue
import random
import time


def generate_request(q):
    request_id = random.randint(1, 999)
    request = f"Запит ID: {request_id}"
    q.put(request)
    print(f"Створено: {request}")


def process_request(q):
    if not q.empty():
        request = q.get()
        print(f"Обробка: {request}")
    else:
        print("Запит порожній")


def main_loop():
    request_queue = queue.Queue()
    try:
        while True:
            generate_request(request_queue)
            process_request(request_queue)
            time.sleep(2)
    except KeyboardInterrupt:
        print(" Програма зупинена користувачем")


if __name__ == "__main__":
    main_loop()
