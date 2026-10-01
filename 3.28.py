import numpy as np

# Khởi tạo dữ liệu
w = np.array([-2, 1, 0])
x = np.array([2, 3, 1])
y = 1

# Bước 1: Tính w^T x
wx = np.dot(w, x)

print("Giá trị w^T x ban đầu =", wx)

# Hàm Perceptron
if wx > 0:
    y_pred = 1
else:
    y_pred = 0

print("Nhãn dự đoán =", y_pred)
print("Nhãn thực tế  =", y)

# Kiểm tra phân lớp đúng hay sai
if y_pred != y:
    print("=> Mẫu bị phân lớp SAI")

    # Bước 2: Cập nhật Perceptron
    w = w + y * x

    print("w sau khi cập nhật =", w)

else:
    print("=> Mẫu được phân lớp ĐÚNG")

# Bước 3: Tính lại w^T x
wx_new = np.dot(w, x)

print("Giá trị w^T x sau cập nhật =", wx_new)