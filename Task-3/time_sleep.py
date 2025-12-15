import time

def sync_task(task_name, delay):
    print(f"{task_name} started")
    time.sleep(delay)
    print(f"{task_name} finished after {delay} seconds")

start_time = time.time()

sync_task("Task 1", 2)
sync_task("Task 2", 3)
sync_task("Task 3", 4)

end_time = time.time()

print(f"\nTotal execution time (SYNC): {end_time - start_time:.2f} seconds")