# Fibonacci numbers module

def fib_print(n): # print fibonacci series up to n
    a,b = 0,1;
    while b < n:
        print b;
        a,b = b, a+b;

def fib_return(n):
    result = [];
    a, b = 0, 1;
    while b < n:
        result.append(b);
        a, b = b, a+b;
    return result;
        
