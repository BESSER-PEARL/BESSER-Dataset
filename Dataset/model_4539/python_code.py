from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class House2_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Action:

    pass
class House2_ValueAction(Action):

    def __init__(self, switchToValue: float):
        self.switchToValue = switchToValue
        
    @property
    def switchToValue(self) -> float:
        return self.__switchToValue

    @switchToValue.setter
    def switchToValue(self, switchToValue: float):
        self.__switchToValue = switchToValue

class House2_BooleanAction(Action):

    def __init__(self, switchTo: bool):
        self.switchTo = switchTo
        
    @property
    def switchTo(self) -> bool:
        return self.__switchTo

    @switchTo.setter
    def switchTo(self, switchTo: bool):
        self.__switchTo = switchTo

class Condition:

    pass
class House2_GreaterThanCondition(Condition):

    def __init__(self, threshold: float):
        self.threshold = threshold
        
    @property
    def threshold(self) -> float:
        return self.__threshold

    @threshold.setter
    def threshold(self, threshold: float):
        self.__threshold = threshold

class House2_EqualCondition(Condition):

    def __init__(self, boolcond: bool, valuecond: float):
        self.boolcond = boolcond
        self.valuecond = valuecond
        
    @property
    def boolcond(self) -> bool:
        return self.__boolcond

    @boolcond.setter
    def boolcond(self, boolcond: bool):
        self.__boolcond = boolcond

    @property
    def valuecond(self) -> float:
        return self.__valuecond

    @valuecond.setter
    def valuecond(self, valuecond: float):
        self.__valuecond = valuecond

class House2_LessThanCondition(Condition):

    def __init__(self, threshold: float):
        self.threshold = threshold
        
    @property
    def threshold(self) -> float:
        return self.__threshold

    @threshold.setter
    def threshold(self, threshold: float):
        self.__threshold = threshold

class House2_Action(ABC):

    pass
class House2_Condition(ABC):

    pass
class Actor:

    pass
class House2_RollerBlind(Actor):

    def __init__(self, isUp: bool):
        self.isUp = isUp
        
    @property
    def isUp(self) -> bool:
        return self.__isUp

    @isUp.setter
    def isUp(self, isUp: bool):
        self.__isUp = isUp

class House2_Lamp(Actor):

    def __init__(self, isOn: bool):
        self.isOn = isOn
        
    @property
    def isOn(self) -> bool:
        return self.__isOn

    @isOn.setter
    def isOn(self, isOn: bool):
        self.__isOn = isOn

class House2_Boiler(Actor):

    def __init__(self, isOn: bool):
        self.isOn = isOn
        
    @property
    def isOn(self) -> bool:
        return self.__isOn

    @isOn.setter
    def isOn(self, isOn: bool):
        self.__isOn = isOn

class Sensor:

    pass
class House2_RainSensor(Sensor):

    def __init__(self, active: bool):
        self.active = active
        
    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

class House2_TwilightSwitch(Sensor):

    def __init__(self, active: bool):
        self.active = active
        
    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

class House2_TemperatureSensor(Sensor):

    def __init__(self, temp: float):
        self.temp = temp
        
    @property
    def temp(self) -> float:
        return self.__temp

    @temp.setter
    def temp(self, temp: float):
        self.__temp = temp

class NamedElement:

    pass
class House2_Element(NamedElement):

    pass
class House2_Actor(NamedElement):

    pass
class House2_Sensor(NamedElement):

    pass
class House2_Container(NamedElement):

    pass
class House2_ControlRule:

    pass
class Element:

    pass
class Container:

    pass
class House2_Room(Container):

    pass
class House2_House(Container, Element):

    pass