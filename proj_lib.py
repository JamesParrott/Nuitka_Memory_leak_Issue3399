class _Int:
    pass

class MyClass:

    def __init__(self, x):
        self.x = x
        self.i = _Int() # this attribute of the user declared class _Int instance is just to show another 2 left object causing increasing memory consumption each time it runs

def operation_with_match(x): # it produces memory leaks in case of x is an instance of any user declared class
    match x:
        case MyClass(): # case statement can be anything, e.g. case 1: return x
            return x.x
    return x

def operation_with_if(x): # it doesn't produce any memory leak whatsoever
    if isinstance(x, MyClass):
        return x.x
    return x