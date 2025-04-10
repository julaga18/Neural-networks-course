import numpy as np
import random

def f(x, beta):
    return 1 / (1 + np.exp(-beta * x))

def df(x, beta):
    return (beta * np.exp(-beta * x)) / (1 + np.exp(-beta * x))**2

def dE(s, x, z, beta):
    grad = np.zeros_like(s)
    for p in range(4):
        s_xp = 0
        for i in range(3):
            s_xp += s[i] * x[p,i]
        yp = f(s_xp, beta)
        grad += (yp - z[p]) * df(np.dot(s, x[p]), beta) * x[p]
    return grad

def gradient_descent(c, epsilon, beta, N):
    
    s_old = np.array([random.uniform(-N, N) for _ in range(3)])

    x = np.array([[0, 0, 1], 
                  [0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]])
    
    z = np.array([0, 0, 0, 1])
    t = 0

    print(f"Początkowe wartości wag: {s_old}")
    print(f"Początkowe wartości y(p): {np.round([f(sum(s_old[i] * x[p, i] for i in range(3)), beta) for p in range(4)],4)}")

    while True:
        gradient = dE(s_old, x, z, beta)
        s_new = s_old - c * gradient
        
        if np.max(np.abs(s_new - s_old)) < epsilon:
            break
        
        s_old = s_new
        t += 1

    print(f"Liczba iteracji: {t}")
    print(f"Końcowe wartości wag: {s_new}")
    print(f"Końcowe wartości y(p): {np.round([f(sum(s_old[i] * x[p, i] for i in range(3)), beta) for p in range(4)],4)}")
    
    return s_new

if __name__ == "__main__":
    c =  1.0 #0.1
    epsilon = 0.001
    beta = 2.0
    N = 2
    gradient_descent(c, epsilon, beta, N)
