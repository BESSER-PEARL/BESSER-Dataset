from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class use_registered_classes_C:

    pass
class use_registered_classes_B:

    pass
class use_registered_classes_A:

    def __init__(self, x: int, y: str, z: str):
        self.x = x
        self.y = y
        self.z = z
        
        pass
    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, z: str):
        self.__z = z


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

