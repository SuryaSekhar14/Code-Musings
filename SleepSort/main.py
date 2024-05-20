import threading
import time

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
out = []

def sleep_sort(arr):
    def output(value):
        time.sleep(value)
        out.append(value)

    threads = []
    for value in arr:
        thread = threading.Thread(target=output, args=(value,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return out

print(sleep_sort(arr))
