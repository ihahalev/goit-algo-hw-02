from queue import Queue
import random

# Створити чергу заявок
queue = Queue()
start_data = {'id': 0}

def generate_request():
    data = random.randint(1, 100)
    start_data['id'] += 1
    req = {'request': start_data['id'], 'data': data}
    queue.put(req)

def process_request():
    if not queue.empty():
        req = queue.get()
        print(f"Обробка заявок {req['request']} з даними {req['data']}")
    else:
        print("Черга заявок порожня")

if __name__ == "__main__":
    start_data['id'] = 0
    while True:
        generate_request()
        process_request()
        user_input = input("Type any char to exit:\n")
        if (user_input):
            break