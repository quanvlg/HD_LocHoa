# Hàm làm sạch dữ liệu dựa trên nguyên tắc đã thảo luận
def clean_data(data):
    # Danh sách để lưu kết quả sau khi làm sạch
    result = []

    # Biến để theo dõi số thứ tự lớn nhất đã được giữ lại
    max_order = -float('inf')

    # Lặp qua các cặp ngày - số thứ tự trong dữ liệu
    for day, order in data:
        # Nếu số thứ tự lớn hơn số thứ tự lớn nhất đã giữ lại, giữ lại cặp này
        if order > max_order:
            result.append((day, order))
            max_order = order  # Cập nhật số thứ tự lớn nhất đã được giữ lại

    return result


# Dữ liệu đầu vào
data = [
    (1, 10), (2, 20), (3, 12), (4, 13), (5, 14), (6, 2), (7, 5), (8, 6),
    (9, 7), (10, 8), (11, 1), (12, 15), (13, 3), (14, 4), (15, 16), (16, 17),
    (17, 18), (18, 19), (19, 11), (20, 21), (21, 9)
]

# Làm sạch dữ liệu
cleaned_data = clean_data(data)

# In kết quả
print("Kết quả sau khi làm sạch dữ liệu:")
for day, order in cleaned_data:
    print(f"Ngày: {day}, Số thứ tự: {order}")


import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv('duongdan_file.csv')

# Chuyển đổi thành danh sách các cặp (Ngày, Số thứ tự)
data = list(zip(df['Ngày'], df['Số thứ tự']))

# Làm sạch dữ liệu
cleaned_data = clean_data(data)

# In kết quả
for day, order in cleaned_data:
    print(f"Ngày: {day}, Số thứ tự: {order}")
