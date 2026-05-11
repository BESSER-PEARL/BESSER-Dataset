from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsm_State:

    def __init__(self, foo: str, i: int, b: bool, c: str, l: str, d: float, f: float):
        self.foo = foo
        self.i = i
        self.b = b
        self.c = c
        self.l = l
        self.d = d
        self.f = f
        
        pass
    @property
    def d(self):
        return self.__d

    @d.setter
    def d(self, d: float):
        self.__d = d


    @property
    def foo(self):
        return self.__foo

    @foo.setter
    def foo(self, foo: str):
        self.__foo = foo


    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c: str):
        self.__c = c


    @property
    def f(self):
        return self.__f

    @f.setter
    def f(self, f: float):
        self.__f = f


    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b: bool):
        self.__b = b


    @property
    def l(self):
        return self.__l

    @l.setter
    def l(self, l: str):
        self.__l = l


    @property
    def i(self):
        return self.__i

    @i.setter
    def i(self, i: int):
        self.__i = i

