#define class-integer
class integer (object):
    def __init__(self, number, check):
        self.number = number
        self.check = check
    def display(self):
        print self.check + str(self.number)
        #if self.check == "negative":
        #    print self.number*-1
        #else:
        #   print self.number
        #print self.check
class negativeinteger (integer):
    def __init__ (self, number):
        super(negativeinteger, self).__init__(number, "negative")
    def display(self):
        integer.display(self)
        print "this is an object of the Negativeinteger class"

if __name__=="__main__":
    d = raw_input("give me a number:")
    m = raw_input("give me another number:")
    for x in [x,y]:
        x.display()