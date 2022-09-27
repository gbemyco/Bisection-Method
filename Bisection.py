def f(x):
    return x**3-x**2-1

def bisection(a,b,n):
    i = 1
    condition = True
    while condition:
        x =(a+b)/2
        if f(x)<0:
            a=x
        else:
            b=x
        print('iteration = ',i, 'x = ',x, 'f(x) = ', f(x))
        if i == n:
            condition = False
        else:
            condition = True
            i = i + 1
    print('Required root is : ', x)

a = input ('First approximation root : ')
b = input ('Second approximation root : ')
n = input ('No. of iteration : ')
a = float(a)
b = float(b)
n = int(n)

if f(a)*f(b)>0:
    print('Given approximate root do not bracket the root.')
    print('Try again with different values.')
else:
    bisection(a,b,n)

    