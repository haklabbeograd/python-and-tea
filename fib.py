
c = 0
def fib(n):
    #print 'fib:', n, c
    global c
    c += 1
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

lst = []
for i in range(3, 20):
    c = 0
    fib(i)
    print i, 'treba', c
    lst.append(c)

print float(lst[-2])/lst[-3]

