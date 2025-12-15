import asyncio
import time

async def async_task(task_name, delay):
    print(f"{task_name} started")
    await asyncio.sleep(delay)
    print(f"{task_name} finished after {delay} seconds")

async def main():
    start_time = time.time()

    await asyncio.gather(
        async_task("Task 1", 3),
        async_task("Task 2", 2),
        async_task("Task 3", 1)
    )

    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")

asyncio.run(main())