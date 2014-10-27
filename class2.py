class Foo:
    def method1(self):
        print "Calling method1."
    def method2(self): 
        print "Calling method2."
    
def call_method(foo, num): 
    f = getattr(foo, "method%d" % num) 
    f()

foo = Foo()
call_method(foo, 2)
