class MyError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)



while True:
    try:
        x = int(raw_input("Please enter a number:"));
        break;
    except ValueError as inst:
        print "Oops, That was no valid number due to:"
        print inst
        print "Please try again...."

print "You entered " + str(x) + "."


raise MyError(x)


        
