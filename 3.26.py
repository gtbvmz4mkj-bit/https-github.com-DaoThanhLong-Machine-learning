def f(x):
    return x**2 - 4 * x + 5


def dao_ham_f(x):
    return 2 * x - 4


learning_rate = 0.2
x = 5.0
so_buoc = 4

print("f'(x) = 2x - 4")
print(f"Bước 0: x = {x:.4f}, f(x) = {f(x):.6f}")

for buoc in range(1, so_buoc + 1):
    x = x - learning_rate * dao_ham_f(x)
    print(f"Bước {buoc}: x = {x:.4f}, f(x) = {f(x):.6f}")

print("\nNhận xét: x tiến dần đến 2 và f(x) tiến dần đến giá trị nhỏ nhất 1.")