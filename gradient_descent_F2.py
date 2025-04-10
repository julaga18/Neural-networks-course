import random


def F(x):
    x1, x2 = x[0], x[1]
    f =  3*x1**4 + 4*x1**3 - 12*x1**2 + 12*x2**2 - 24*x2
    return f

def DF_x(x):
    x1, x2 = x[0], x[1]
    df1 = 12*x1**3 + 12*x1**2 - 24*x1
    df2 = 24*x2 - 24
    return [df1,df2]

def random_x(N):
    x_old = []
    for _ in range(2):
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
    x_old = [2.0, 10.0]
    print(f'Punkt startowy {x_old}')
    return gradient_descent(c, epsilon, x_old)



if __name__ == "__main__": 
    print("Losowy punkt startowy:")
    gradient_descent_random(0.001, 0.0001, 3)

    print("Wybrany punkt startowy:")
    gradient_descent_choosen(0.001, 0.0001)
    

   

