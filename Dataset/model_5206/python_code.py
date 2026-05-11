from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class FaultyUMLmodel_D:

    def __init__(self, z: bool):
        self.z = z
        
        pass
    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, z: bool):
        self.__z = z


class FaultyUMLmodel_C:

    def __init__(self, u: int):
        self.u = u
        
        pass
    @property
    def u(self):
        return self.__u

    @u.setter
    def u(self, u: int):
        self.__u = u


class FaultyUMLmodel_B:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y


class FaultyUMLmodel_A:

    def __init__(self, v: int, w: bool):
        self.v = v
        self.w = w
        
        pass
    @property
    def w(self):
        return self.__w

    @w.setter
    def w(self, w: bool):
        self.__w = w


    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v: int):
        self.__v = v

