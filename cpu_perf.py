import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def measure_time(n):
    start_time = time.time()
    fibonacci(n)
    end_time = time.time()
    return end_time - start_time

# nの異なる値に対する実行時間を測定
n_values = list(range(5, 36, 5))
times = []

for n in n_values:
    elapsed_time = measure_time(n)
    times.append(elapsed_time)
    print(f"n={n}, {elapsed_time}秒")

