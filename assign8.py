class A:
    c = 0
    _b = 0
    __a = 0
    def __init__(self,c,_b,__a):
        self.c = c
        self._b = _b
        self.__a = __a
    def display_A(self):
        print("Inside of Class A!")
        print("Value of A",self.__a)
        print("Value of B",self._b)
        print("Value of C",self.c)

class B(A):
    def display_B(self):
        print("Inside of Class B!")
        try:
            print("Value of A",self.__a)
        except NameError:
            print("Private Variable is getting asscced out of its class!")
        except Exception:
            print("Private variable invalid accessing Error Raised!!")
        print("Value of B",self._b)
        print("Value of C",self.c)

b = B(1,2,3)
b.display_A()
b.display_B()
