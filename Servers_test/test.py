import asyncio
import time
import matplotlib.pyplot as plt

async def client_task(host, port):
    try:
        reader, writer = await asyncio.open_connection(host, port)
        message = "Hello, Server!"
        writer.write(message.encode())
        await writer.drain()
        start_time = time.time()
        data = await reader.read(1024)
        end_time = time.time()
        writer.close()
        await writer.wait_closed()
        return end_time - start_time  # Время в пути сообщения
    except Exception as e:
        return None  # При ошибке возвращаем None

async def run_clients(num_clients):
    host = 'povt-cluster.tstu.tver.ru'
    port = 44322
    tasks = [client_task(host, port) for _ in range(num_clients)]
    start_time = time.time()
    response_times = await asyncio.gather(*tasks)
    end_time = time.time()
    total_duration = end_time - start_time

    response_times = [t for t in response_times if t is not None]
    failed_requests = num_clients - len(response_times)

    if response_times:
        max_time = max(response_times)
        min_time = min(response_times)
        avg_time = sum(response_times) / len(response_times)
        print(f"Максимальное время отклика: {max_time:.10f}s")
        print(f"Минимальное время отклика: {min_time:.10f}s")
        print(f"Среднее время отклика: {avg_time:.10f}s")
        print(f"Общая продолжительность: {total_duration:.10f}s")
        print(f"Обслуженные запросы: {len(response_times)}")
        print(f"Необслуженные запросы: {failed_requests}")

        # График времени ответа
        plt.figure(figsize=(10, 5))
        plt.hist(response_times, bins=50, color='blue', alpha=0.7)
        plt.title("Распределение времени отклика")
        plt.xlabel("Время отклика (s)")
        plt.ylabel("Частота")
        plt.grid(True)
        plt.show()
    else:
        print("Время отклика не зафиксировано, возможно, из-за проблем с подключением.")

asyncio.run(run_clients(10000))
