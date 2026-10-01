import numpy as np

def grad(x):
    return 2 * x

def cost(x):
    return x**2 - 2

def myGD1(x0, eta):
    x = [x0]
    for it in range(100):
        x_new = x[-1] - eta * grad(x[-1])
        if abs(grad(x_new)) < 1e-3:
            break
        x.append(x_new)
    return (x, it)

# x0 = 5, learning rate = 0.1
x_sol, iters = myGD1(5, 0.1)
print(f"Nghiem x = {x_sol[-1]:.6f}, Gia tri cuc tieu f(x) = {cost(x_sol[-1]):.6f} sau {iters} vong lap")