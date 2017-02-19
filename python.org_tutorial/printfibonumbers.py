#!/bb/bin/bbpy64

default_limit = 100;

def fib(n):
    a = 1;
    b = 1;
    while b < n:
        print b;
        a,b = b,a+b;
    
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        N = int(sys.argv[1]);
        print 'Printing fibonacci numbers less than ' + str(N);
    else:
        N = default_limit;
        print 'No limit specified, using' + str(N) + ' as the limit';

    fib(N);



    


