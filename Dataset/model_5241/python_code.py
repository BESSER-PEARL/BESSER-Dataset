from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Color(Enum):
    RED = "RED"
    BLUE = "BLUE"


############################################
# Definition of Classes
############################################

class genericsGoCrazy_OtherClass:

    pass
class Car:

    pass
class genericsGoCrazy_SubCar(Car):

    pass
class genericsGoCrazy_Comp:

    pass
class genericsGoCrazy_MySubClass:

    pass
class genericsGoCrazy_Car:

    def __init__(self, name: str, fullName: str, doors: str, color: str, genericsGoCrazy_Car: "genericsGoCrazy_Car" = None, genericsGoCrazy_Car0: "genericsGoCrazy_Car" = None):
        self.name = name
        self.fullName = fullName
        self.doors = doors
        self.color = color
        self.genericsGoCrazy_Car = genericsGoCrazy_Car
        self.genericsGoCrazy_Car0 = genericsGoCrazy_Car0
        
    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def doors(self) -> str:
        return self.__doors

    @doors.setter
    def doors(self, doors: str):
        self.__doors = doors

    @property
    def genericsGoCrazy_Car0(self):
        return self.__genericsGoCrazy_Car0

    @genericsGoCrazy_Car0.setter
    def genericsGoCrazy_Car0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericsGoCrazy_Car__genericsGoCrazy_Car0", None)
        self.__genericsGoCrazy_Car0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "genericsGoCrazy_Car"):
                opp_val = getattr(old_value, "genericsGoCrazy_Car", None)
                if opp_val == self:
                    setattr(old_value, "genericsGoCrazy_Car", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "genericsGoCrazy_Car"):
                opp_val = getattr(value, "genericsGoCrazy_Car", None)
                setattr(value, "genericsGoCrazy_Car", self)

    @property
    def genericsGoCrazy_Car(self):
        return self.__genericsGoCrazy_Car

    @genericsGoCrazy_Car.setter
    def genericsGoCrazy_Car(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericsGoCrazy_Car__genericsGoCrazy_Car", None)
        self.__genericsGoCrazy_Car = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "genericsGoCrazy_Car0"):
                opp_val = getattr(old_value, "genericsGoCrazy_Car0", None)
                if opp_val == self:
                    setattr(old_value, "genericsGoCrazy_Car0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "genericsGoCrazy_Car0"):
                opp_val = getattr(value, "genericsGoCrazy_Car0", None)
                setattr(value, "genericsGoCrazy_Car0", self)

    def foo(self, a: int):
        # TODO: Implement foo method
        pass

    def enhancedFoo(self, aT: str, aInt: int):
        # TODO: Implement enhancedFoo method
        pass

    def superFoo(self, key: str):
        # TODO: Implement superFoo method
        pass

class genericsGoCrazy_MyClass:

    def __init__(self, a1: str, a2: str, a3: str, theEObject: str, aMap: str):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.theEObject = theEObject
        self.aMap = aMap
        
    @property
    def aMap(self) -> str:
        return self.__aMap

    @aMap.setter
    def aMap(self, aMap: str):
        self.__aMap = aMap

    @property
    def a2(self) -> str:
        return self.__a2

    @a2.setter
    def a2(self, a2: str):
        self.__a2 = a2

    @property
    def a3(self) -> str:
        return self.__a3

    @a3.setter
    def a3(self, a3: str):
        self.__a3 = a3

    @property
    def theEObject(self) -> str:
        return self.__theEObject

    @theEObject.setter
    def theEObject(self, theEObject: str):
        self.__theEObject = theEObject

    @property
    def a1(self) -> str:
        return self.__a1

    @a1.setter
    def a1(self, a1: str):
        self.__a1 = a1

    def bar(self, aF: str, aT: str, ts: str):
        # TODO: Implement bar method
        pass
