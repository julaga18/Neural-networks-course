import random


def F(x):
    x1, x2, x3 = x[0], x[1], x[2]
    f =  2*x1**2 + 2*x2**2 + x3**2 - 2*x1*x2 - 2*x2*x3 - 2*x1 + 3
    return f


def DF_x(x):
    x1, x2, x3 = x[0], x[1], x[2]
    df1 = 4*x1 - 2*x2 - 2
    df2 = 4*x2- 2*x1 - 2*x3
    df3 = 2*x3 - 2*x2
    return [df1,df2,df3]


def random_x(N):
    x_old = []
    for _ in range(3):
        x = (random.random() - 0.5) * 2 * N
        x_old.append(x)
    return x_old


def gradient_descent(c, epsilon, x_old):
    x_new = x_old[:]
    df_x = DF_x(x_old)
    for i in range(len(x_old)):
        x_new[i] = x_old[i] - c * df_x[i]

    while max(abs(x_new[i] - x_old[i]) for i in range(len(x_old))) > epsilon:
        x_old = x_new[:]
        df_x = DF_x(x_old)
        for i in range(len(x_old)):
            x_new[i] = x_old[i] - c * df_x[i]

    print(f"Minimum w punkcie: {x_new}, wartość F: {F(x_new)}")
    return F(x_new)


def gradient_descent_random(c, epsilon, N):
    x_old = random_x(N)
    print(f'Punkt startowy {x_old}')
    return gradient_descent(c, epsilon, x_old)


def gradient_descent_choosen(c, epsilon):
    x_old = [2.0, 10.0, 1.0]
    print(f'Punkt startowy {x_old}')
    return gradient_descent(c, epsilon, x_old)


if __name__ == "__main__": 
    print("Losowy x_old:")
    gradient_descent_random(0.001, 0.0001, 10)

    print("Wybrany x_old:")
    gradient_descent_choosen(0.001, 0.0001)
