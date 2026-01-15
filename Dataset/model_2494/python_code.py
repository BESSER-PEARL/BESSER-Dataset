from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsm_State:

    def __init__(self, d: float, f: float, foo: str, i: int, b: bool, c: str, l: str):
        self.d = d
        self.f = f
        self.foo = foo
        self.i = i
        self.b = b
        self.c = c
        self.l = l
        
    @property
    def b(self) -> bool:
        return self.__b

    @b.setter
    def b(self, b: bool):
        self.__b = b

    @property
    def c(self) -> str:
        return self.__c

    @c.setter
    def c(self, c: str):
        self.__c = c

    @property
    def l(self) -> str:
        return self.__l

    @l.setter
    def l(self, l: str):
        self.__l = l

    @property
    def foo(self) -> str:
        return self.__foo

    @foo.setter
    def foo(self, foo: str):
        self.__foo = foo

    @property
    def i(self) -> int:
        return self.__i

    @i.setter
    def i(self, i: int):
        self.__i = i

    @property
    def d(self) -> float:
        return self.__d

    @d.setter
    def d(self, d: float):
        self.__d = d

    @property
    def f(self) -> float:
        return self.__f

    @f.setter
    def f(self, f: float):
        self.__f = f
