import threading
import time

# Example Thread without Lock
def write_to_file(filename, content):
    print(f"thread: {threading.current_thread().name}: start writing file: {filename}")
    time.sleep(1)
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Thread {threading.current_thread().name} completely writend file: {filename}")

def multi_thread():
    file_list = {
        "file1.txt": "content of file 1",
        "file2.txt": "content of file 2",
        "file3.txt": "content of file 3",
    }

    threads = []
    start_time = time.time()

    for filename, content in file_list.items():
        thread = threading.Thread(target=write_to_file, args=(filename, content), name=filename)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()

    print(f"completed task during {end_time-start_time:.2f}")

# Example about Thread with Lock to share data between all threads -> avoid GIL Python

lock = threading.Lock()
shared_thread_results ={}

def process_data(thread_id, data_content):
    time.sleep(1)
    result = f"process of {data_content}"
    with lock:
        print(f"Luồng {thread_id}: Đã có khóa, đang ghi vào shared_thread_results.")
        shared_thread_results[thread_id] = result
def shared_multi_thread():
    tasks = {
        "id 1": "Data_a",
        "id 2": "Data_b",
        "id 3": "Data_c"
    }
    threads = []
    for thread_id, data_content in tasks.items():
        thread = threading.Thread(target=process_data, args=(thread_id, data_content), name=thread_id)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print(f"result of shared data {shared_thread_results}")


if __name__ == "__main__":
    # multi_thread()
    shared_multi_thread()