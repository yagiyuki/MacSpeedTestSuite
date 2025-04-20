import os
import time

# ファイル書き込み速度の測定
def write_speed_test(file_name, file_size):
    start_time = time.time()
    with open(file_name, "wb") as f:
        f.write(os.urandom(file_size))
    end_time = time.time()
    return end_time - start_time

# ファイル読み込み速度の測定
def read_speed_test(file_name):
    start_time = time.time()
    with open(file_name, "rb") as f:
        data = f.read()
    end_time = time.time()
    return end_time - start_time

file_name = "test_file"
file_size = 100 * 1024 * 1024  # 例: 100MB

write_time = write_speed_test(file_name, file_size)
print(f"書き込み時間: {write_time} 秒")

read_time = read_speed_test(file_name)
print(f"読み込み時間: {read_time} 秒")

os.remove(file_name)  # ファイルの削除
