from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Direction(Enum):
    pass

############################################
# Definition of Classes
############################################










class ElevatorControl:

    pass


class ElevatorComponent(ABC):

    def __init__(self, direction: Direction):
        self.direction = direction
        
        pass
    @property
    def direction(self):
        return self.__direction
    @direction.setter
    def direction(self, direction: Direction):
        self.__direction = direction



class Button:

    def __init__(self, floor: int, pressed: bool, elevatorControl2: "ElevatorControl" = None):
        self.floor = floor
        self.pressed = pressed
        self.elevatorControl2 = elevatorControl2
        
        pass
    @property
    def floor(self):
        return self.__floor
    @floor.setter
    def floor(self, floor: int):
        self.__floor = floor

    @property
    def pressed(self):
        return self.__pressed
    @pressed.setter
    def pressed(self, pressed: bool):
        self.__pressed = pressed

    @property
    def elevatorControl2(self):
        return self.__elevatorControl2
    @elevatorControl2.setter
    def elevatorControl2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Button__elevatorControl2", None)
        self.__elevatorControl2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "button3"):
                opp_val = getattr(old_value, "button3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "button3"):
                opp_val = getattr(value, "button3", None)
                if opp_val is None:
                    setattr(value, "button3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Elevator:

    def __init__(self, number: int, currentFloor: int, destinationFloor: int, elevatorControl0: "ElevatorControl" = None):
        self.number = number
        self.currentFloor = currentFloor
        self.destinationFloor = destinationFloor
        self.elevatorControl0 = elevatorControl0
        
        pass
    @property
    def destinationFloor(self):
        return self.__destinationFloor
    @destinationFloor.setter
    def destinationFloor(self, destinationFloor: int):
        self.__destinationFloor = destinationFloor

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def currentFloor(self):
        return self.__currentFloor
    @currentFloor.setter
    def currentFloor(self, currentFloor: int):
        self.__currentFloor = currentFloor

    @property
    def elevatorControl0(self):
        return self.__elevatorControl0
    @elevatorControl0.setter
    def elevatorControl0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elevator__elevatorControl0", None)
        self.__elevatorControl0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevator1"):
                opp_val = getattr(old_value, "elevator1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevator1"):
                opp_val = getattr(value, "elevator1", None)
                if opp_val is None:
                    setattr(value, "elevator1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

