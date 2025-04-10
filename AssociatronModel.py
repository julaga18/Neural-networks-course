
def calculate_W(u1, u2):
    w = [[0 for col in range(25)] for row in range(25)]
    for i in range(25):
        for j in range(25):
            w[i][j] = (u1[i] * u1[j] + u2[i] * u2[j]) / 25
    return w


def sgn(x):
    for i in range(25):
        if x[i] < 0:
            x[i] = -1
        else:
            x[i] = 1
    return x


def calculate_output(w, u):
    output = []
    for i in range(25):
        x = 0
        for j in range(25):
            x += w[i][j] * u[j]
        output.append(x)
    return sgn(output)


def show_output(u):
    counter = 0
    for i in range(25):
        if u[i] == -1:
            print('- ', end='')
            counter += 1
        elif u[i] == 1:
            print('* ', end='')
            counter += 1
        if counter%5 == 0:
            print()
    print('\n')


def Asoc(u1, u2, u1_prime, u2_prime):
    w = calculate_W(u1, u2)

    u1_output = calculate_output(w, u1)
    u2_output = calculate_output(w, u2)
    u1_prime_output = calculate_output(w, u1_prime)
    u2_prime_output = calculate_output(w, u2_prime)

    print('u1_output')
    show_output(u1_output)
    print('u2_output')
    show_output(u2_output)
    print('u1_prime_output')
    show_output(u1_prime_output)
    print('u2_prime_output')
    show_output(u2_prime_output)


u1 = [-1, -1, -1, -1, -1,
      -1, 1, 1, 1, -1,
      -1, 1, -1, 1, -1,
      -1, 1, 1, 1, -1,
      -1, -1, -1, -1, -1]


u2 = [-1, -1, -1, -1, -1,
      -1, 1, 1, -1, -1,
      -1, -1, 1, -1, -1,
      -1, -1, 1, -1, -1,
      -1, -1, -1, -1, -1]


u1_prime = [-1, 1, 1, 1, -1,
            -1, 1, -1, 1, -1,
            -1, 1, -1, 1, -1,
            -1, 1, 1, 1, -1,
            -1, -1, -1, -1, -1]


u2_prime = [-1, -1, 1, -1, -1,
            -1, -1, 1, -1, -1,
            -1, -1, 1, -1, -1,
            -1, -1, 1, -1, -1,
            -1, -1, -1, -1, -1]

Asoc(u1, u2, u1_prime, u2_prime)

