w = [1, 2, -10]
x = [3, 4, 1]
y_thuc_te = -1

# Tính w^T x
wTx = sum(w_i * x_i for w_i, x_i in zip(w, x))

# Perceptron: w^T x >= 0 thì dự đoán +1, ngược lại dự đoán -1
y_du_doan = 1 if wTx >= 0 else -1

phan_lop_sai = y_du_doan != y_thuc_te

print("w^T x =", wTx)
print("Nhãn dự đoán =", y_du_doan)
print("Điểm dữ liệu bị phân lớp sai:", phan_lop_sai)