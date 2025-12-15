import time
import asyncio

def sync_task(task_name, delay):
    print(f"{task_name} started (SYNC)")
    time.sleep(delay)
    print(f"{task_name} finished after {delay} seconds (SYNC)")


async def async_task(task_name, delay):
    print(f"{task_name} started (ASYNC)")
    await asyncio.sleep(delay)
    print(f"{task_name} finished after {delay} seconds (ASYNC)")


def run_sync():
    print("Running synchronous tasks\n")

    start_time = time.time()

    sync_task("Task 1", 2)
    sync_task("Task 2", 3)
    sync_task("Task 3", 4)

    end_time = time.time()
    print(f"Total execution time (SYNC): {end_time - start_time:.2f} seconds")


async def run_async():
    print("Running asynchronous tasks\n")

    start_time = time.time()

    await asyncio.gather(
        async_task("Task 1", 2),
        async_task("Task 2", 3),
        async_task("Task 3", 4)
    )

    end_time = time.time()
    print(f"Total execution time (ASYNC): {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    run_sync()
    asyncio.run(run_async())