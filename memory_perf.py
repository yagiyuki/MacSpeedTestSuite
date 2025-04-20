import time

def memory_performance_test(size_in_mb):
    num_elements = size_in_mb * 1024 * 1024 // 8  # int型のサイズを考慮
    test_array = list(range(num_elements))
    start_time = time.time()
    test_array2 = test_array.copy()
    end_time = time.time()
    return end_time - start_time

mem_test_size = 500  # 例: 500MB
memory_performance = memory_performance_test(mem_test_size)
print(f"メモリパフォーマンス測定（サイズ={mem_test_size}MB）: {memory_performance} 秒")

