#!/opt/bb/bin/bbpy
import pdb

def myfun(x):
    pdb.set_trace()
    y = x + 1
    return y



print myfun(3)
