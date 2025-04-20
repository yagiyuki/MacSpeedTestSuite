import threading
import time

# シンプルなタスク
def simple_task(thread_id, results):
    start_time = time.time()
    total = 0
    for i in range(10000000):
        total += i
    end_time = time.time()
    results[thread_id] = end_time - start_time

# マルチスレッドでのタスク実行と時間測定
def run_multithreaded_tasks(thread_count):
    threads = []
    results = [0] * thread_count

    for i in range(thread_count):
        thread = threading.Thread(target=simple_task, args=(i, results))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return results

# スレッド数の設定
thread_count = 4

# テスト実行
execution_times = run_multithreaded_tasks(thread_count)
for i, time_taken in enumerate(execution_times):
    print(f"スレッド {i} の実行時間: {time_taken} 秒")

