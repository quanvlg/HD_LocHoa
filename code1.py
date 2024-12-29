def filter_increasing_pairs(data):
    """
    Lọc các cặp (ngày, số thứ tự) để giữ lại danh sách dài nhất có thứ tự tăng dần.

    Args:
        data (list of tuples): Danh sách các cặp (ngày, số thứ tự).

    Returns:
        list of tuples: Danh sách các cặp (ngày, số thứ tự) thỏa mãn điều kiện tăng dần.
    """
    n = len(data)
    dp = [1] * n  # dp[i] lưu độ dài dãy tăng dài nhất kết thúc tại i
    prev = [-1] * n  # Lưu chỉ số phần tử trước đó trong dãy

    # Tìm dãy tăng dài nhất
    for i in range(1, n):
        for j in range(i):
            if data[j][0] < data[i][0] and data[j][1] < data[i][1]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

    # Truy ngược để tìm dãy tăng
    max_index = dp.index(max(dp))
    result = []
    while max_index != -1:
        result.append(data[max_index])
        max_index = prev[max_index]

    return result[::-1]  # Đảo ngược kết quả


# Dữ liệu ví dụ
data = [
    (1, 18), (2, 19), (3, 29), (4, 13), (5, 14), (6, 21),
    (7, 9), (8, 22), (9, 7), (10, 8), (11, 1), (12, 15),
    (13, 3), (14, 12), (15, 16), (16, 17), (17, 5), (18, 11),
    (19, 20), (20, 26), (21, 27), (22, 28), (23, 23), (24, 24),
    (25, 25), (26, 2), (27, 10), (28, 6), (29, 4), (30, 30)
]

# Lọc danh sách theo nguyên tắc tăng dần
filtered_data = filter_increasing_pairs(data)
print("Danh sách hợp lệ:", filtered_data)
