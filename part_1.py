import queue
import random
import time

queue = queue.Queue()
request_id = 1


def generate_request():
    global request_id
    request = f"Заявка ID: {request_id}"
    queue.put(request)
    print(f"Створили нову заявку: ID {request}")
    request_id += 1


def process_request():
    if queue.empty():
        print("Запит відсутній")

    request = queue.get()
    print(f"Виконання: {request}")


def main():
    print(f"Створити чергу заявок: ")

    while True:
        command = input("Введіть команду: ").strip()

        if command == "q":
            break
        elif command == "new":
            generate_request()
        elif command == "process":
            process_request()
        else:
            print("Команда не вірна.")


if __name__ == "__main__":
    main()
