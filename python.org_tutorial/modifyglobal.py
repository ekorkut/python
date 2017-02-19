#!/bb/bin/bbpy64

GLOBALVAR = 4

print "First:" + str(GLOBALVAR)

def modify():
    GLOBALVAR = 5

print "Second:" + str(GLOBALVAR)
