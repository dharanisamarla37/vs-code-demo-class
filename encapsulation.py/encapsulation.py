# encapsulation using single class
class display():
    __a = 5 # private
    _b = 5 #public
    print(__a)
    print(_b)
    
    
class display():
    def __init__(self,a,b):#this is method
        self.__a=a
        self._b=b
class demo(display):#inherit from upper class
    def output(self):
        print(self._b )
d=demo(10,20)
d.output()