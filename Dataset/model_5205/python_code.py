from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class FaultyUMLmodel_C:

    def __init__(self, u: int):
        self.u = u
        
    @property
    def u(self) -> int:
        return self.__u

    @u.setter
    def u(self, u: int):
        self.__u = u

class FaultyUMLmodel_B:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

class FaultyUMLmodel_A:

    def __init__(self, v: int, w: bool):
        self.v = v
        self.w = w
        
    @property
    def w(self) -> bool:
        return self.__w

    @w.setter
    def w(self, w: bool):
        self.__w = w

    @property
    def v(self) -> int:
        return self.__v

    @v.setter
    def v(self, v: int):
        self.__v = v

class FaultyUMLmodel_D:

    def __init__(self, z: bool):
        self.z = z
        
    @property
    def z(self) -> bool:
        return self.__z

    @z.setter
    def z(self, z: bool):
        self.__z = z
