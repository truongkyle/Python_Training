import multiprocessing
import time

# Sharing data with Queue()
def process_data(worker_id, value, result_queue):
    print(f"Process {multiprocessing.current_process().name}: start to work with key {worker_id}")
    processed_value = value * 10
    result_queue.put((worker_id, processed_value))
    print(f"Process {multiprocessing.current_process().name}: Sent the result to Queue")

def multiprocessing_data():
    q = multiprocessing.Queue()
    tasks = [
        ('a', 1),
        ('b', 2),
        ('c', 3)
    ]

    processes = []
    for key, value in tasks:
        process = multiprocessing.Process(target=process_data, args=(key, value, q), name=key)
        processes.append(process)
        process.start()

    for p in processes:
        p.join()
    final_results = {}
    while not q.empty():
        key, value = q.get()
        final_results[key] = value
    print(f"final result collected from queue: {final_results}")

if __name__ == "__main__":
    multiprocessing_data()