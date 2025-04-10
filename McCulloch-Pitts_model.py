
def f(x):
    if x >= 0:
        return 1
    elif x < 0:
        return 0


def dot_product(u,w):
    u.append(1.0)
    product = 0
    for i in range(len(u)):
        product += u[i] * w[i] 
    return product


def NOT(u):
    w = [-2.0, 1.0]
    product = dot_product(u,w)
    result = f(product)
    return result


def AND(u):
    w = [2.0, 2.0, -3.0]
    product = dot_product(u,w)
    result = f(product)
    return result


def NAND(u):
    w = [-0.25, -0.5, 0.7]
    product = dot_product(u,w)
    result = f(product)
    return result


def OR(u):
    w = [2.0, 3.0, -1.0]
    product = dot_product(u,w)
    result = f(product)
    return result


print("NOT gate")
print(NOT([0.0]))
print(NOT([1.0]))

print("AND gate")
print(AND([0.0,0.0]))
print(AND([1.0,0.0]))
print(AND([0.0,1.0]))
print(AND([1.0,1.0]))

print("NAND gate")
print(NAND([0.0,0.0]))
print(NAND([1.0,0.0]))
print(NAND([0.0,1.0]))
print(NAND([1.0,1.0]))

print("OR gate")
print(OR([0.0,0.0]))
print(OR([1.0,0.0]))
print(OR([0.0,1.0]))
print(OR([1.0,1.0]))
    


   
