from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Direction(Enum):
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"
class DigitalPinNumber(Enum):
    D0 = "D0"
    D1 = "D1"
    D2 = "D2"
    D4 = "D4"
    D5 = "D5"


############################################
# Definition of Classes
############################################

class Function:

    pass
class arduino_Write(Function):

    def __init__(self, name: str, arduino_Write: "arduino_DigitalPin" = None):
        self.name = name
        self.arduino_Write = arduino_Write
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arduino_Write(self):
        return self.__arduino_Write

    @arduino_Write.setter
    def arduino_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Write__arduino_Write", None)
        self.__arduino_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_DigitalPin"):
                opp_val = getattr(old_value, "arduino_DigitalPin", None)
                if opp_val == self:
                    setattr(old_value, "arduino_DigitalPin", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_DigitalPin"):
                opp_val = getattr(value, "arduino_DigitalPin", None)
                setattr(value, "arduino_DigitalPin", self)

class arduino_Instruction(ABC):

    pass
class Instruction:

    pass
class arduino_Function(Instruction):

    pass
class Pin:

    pass
class arduino_DigitalPin(Pin):

    def __init__(self, number: str, arduino_DigitalPin12: "arduino_Read" = None, arduino_DigitalPin15: "arduino_Setup" = None, arduino_DigitalPin: "arduino_Write" = None):
        self.number = number
        self.arduino_DigitalPin12 = arduino_DigitalPin12
        self.arduino_DigitalPin15 = arduino_DigitalPin15
        self.arduino_DigitalPin = arduino_DigitalPin
        
    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def arduino_DigitalPin15(self):
        return self.__arduino_DigitalPin15

    @arduino_DigitalPin15.setter
    def arduino_DigitalPin15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_DigitalPin__arduino_DigitalPin15", None)
        self.__arduino_DigitalPin15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Setup14"):
                opp_val = getattr(old_value, "arduino_Setup14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Setup14"):
                opp_val = getattr(value, "arduino_Setup14", None)
                if opp_val is None:
                    setattr(value, "arduino_Setup14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduino_DigitalPin(self):
        return self.__arduino_DigitalPin

    @arduino_DigitalPin.setter
    def arduino_DigitalPin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_DigitalPin__arduino_DigitalPin", None)
        self.__arduino_DigitalPin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Write"):
                opp_val = getattr(old_value, "arduino_Write", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Write", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Write"):
                opp_val = getattr(value, "arduino_Write", None)
                setattr(value, "arduino_Write", self)

    @property
    def arduino_DigitalPin12(self):
        return self.__arduino_DigitalPin12

    @arduino_DigitalPin12.setter
    def arduino_DigitalPin12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_DigitalPin__arduino_DigitalPin12", None)
        self.__arduino_DigitalPin12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Read"):
                opp_val = getattr(old_value, "arduino_Read", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Read", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Read"):
                opp_val = getattr(value, "arduino_Read", None)
                setattr(value, "arduino_Read", self)

class arduino_Pin(ABC):

    def __init__(self, Direction: str, name: str):
        self.Direction = Direction
        self.name = name
        
    @property
    def Direction(self) -> str:
        return self.__Direction

    @Direction.setter
    def Direction(self, Direction: str):
        self.__Direction = Direction

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class arduino_Read(Function):

    def __init__(self, returnValue: str, name: str, arduino_Read: "arduino_DigitalPin" = None):
        self.returnValue = returnValue
        self.name = name
        self.arduino_Read = arduino_Read
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def returnValue(self) -> str:
        return self.__returnValue

    @returnValue.setter
    def returnValue(self, returnValue: str):
        self.__returnValue = returnValue

    @property
    def arduino_Read(self):
        return self.__arduino_Read

    @arduino_Read.setter
    def arduino_Read(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Read__arduino_Read", None)
        self.__arduino_Read = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_DigitalPin12"):
                opp_val = getattr(old_value, "arduino_DigitalPin12", None)
                if opp_val == self:
                    setattr(old_value, "arduino_DigitalPin12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_DigitalPin12"):
                opp_val = getattr(value, "arduino_DigitalPin12", None)
                setattr(value, "arduino_DigitalPin12", self)

class arduino_Loop:

    def __init__(self, name: str, arduino_Loop: "arduino_Sketch" = None, arduino_Loop17: set["arduino_Instruction"] = None):
        self.name = name
        self.arduino_Loop = arduino_Loop
        self.arduino_Loop17 = arduino_Loop17 if arduino_Loop17 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arduino_Loop17(self):
        return self.__arduino_Loop17

    @arduino_Loop17.setter
    def arduino_Loop17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Loop__arduino_Loop17", None)
        self.__arduino_Loop17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_Instruction18"):
                    opp_val = getattr(item, "arduino_Instruction18", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_Instruction18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_Instruction18"):
                    opp_val = getattr(item, "arduino_Instruction18", None)
                    
                    setattr(item, "arduino_Instruction18", self)
                    

    @property
    def arduino_Loop(self):
        return self.__arduino_Loop

    @arduino_Loop.setter
    def arduino_Loop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Loop__arduino_Loop", None)
        self.__arduino_Loop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Sketch4"):
                opp_val = getattr(old_value, "arduino_Sketch4", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Sketch4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Sketch4"):
                opp_val = getattr(value, "arduino_Sketch4", None)
                setattr(value, "arduino_Sketch4", self)

class arduino_Setup:

    def __init__(self, name: str, arduino_Setup: "arduino_Sketch" = None, arduino_Setup14: set["arduino_DigitalPin"] = None):
        self.name = name
        self.arduino_Setup = arduino_Setup
        self.arduino_Setup14 = arduino_Setup14 if arduino_Setup14 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arduino_Setup(self):
        return self.__arduino_Setup

    @arduino_Setup.setter
    def arduino_Setup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Setup__arduino_Setup", None)
        self.__arduino_Setup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Sketch2"):
                opp_val = getattr(old_value, "arduino_Sketch2", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Sketch2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Sketch2"):
                opp_val = getattr(value, "arduino_Sketch2", None)
                setattr(value, "arduino_Sketch2", self)

    @property
    def arduino_Setup14(self):
        return self.__arduino_Setup14

    @arduino_Setup14.setter
    def arduino_Setup14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Setup__arduino_Setup14", None)
        self.__arduino_Setup14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_DigitalPin15"):
                    opp_val = getattr(item, "arduino_DigitalPin15", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_DigitalPin15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_DigitalPin15"):
                    opp_val = getattr(item, "arduino_DigitalPin15", None)
                    
                    setattr(item, "arduino_DigitalPin15", self)
                    

class arduino_Sketch:

    def __init__(self, name: str, arduino_Sketch: "arduino_Project" = None, arduino_Sketch2: "arduino_Setup" = None, arduino_Sketch4: "arduino_Loop" = None, arduino_Sketch6: set["arduino_Instruction"] = None):
        self.name = name
        self.arduino_Sketch = arduino_Sketch
        self.arduino_Sketch2 = arduino_Sketch2
        self.arduino_Sketch4 = arduino_Sketch4
        self.arduino_Sketch6 = arduino_Sketch6 if arduino_Sketch6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arduino_Sketch(self):
        return self.__arduino_Sketch

    @arduino_Sketch.setter
    def arduino_Sketch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sketch__arduino_Sketch", None)
        self.__arduino_Sketch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Project"):
                opp_val = getattr(old_value, "arduino_Project", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Project", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Project"):
                opp_val = getattr(value, "arduino_Project", None)
                setattr(value, "arduino_Project", self)

    @property
    def arduino_Sketch4(self):
        return self.__arduino_Sketch4

    @arduino_Sketch4.setter
    def arduino_Sketch4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sketch__arduino_Sketch4", None)
        self.__arduino_Sketch4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Loop"):
                opp_val = getattr(old_value, "arduino_Loop", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Loop", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Loop"):
                opp_val = getattr(value, "arduino_Loop", None)
                setattr(value, "arduino_Loop", self)

    @property
    def arduino_Sketch6(self):
        return self.__arduino_Sketch6

    @arduino_Sketch6.setter
    def arduino_Sketch6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sketch__arduino_Sketch6", None)
        self.__arduino_Sketch6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_Instruction"):
                    opp_val = getattr(item, "arduino_Instruction", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_Instruction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_Instruction"):
                    opp_val = getattr(item, "arduino_Instruction", None)
                    
                    setattr(item, "arduino_Instruction", self)
                    

    @property
    def arduino_Sketch2(self):
        return self.__arduino_Sketch2

    @arduino_Sketch2.setter
    def arduino_Sketch2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sketch__arduino_Sketch2", None)
        self.__arduino_Sketch2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Setup"):
                opp_val = getattr(old_value, "arduino_Setup", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Setup", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Setup"):
                opp_val = getattr(value, "arduino_Setup", None)
                setattr(value, "arduino_Setup", self)

class arduino_Project:

    def __init__(self, name: str, arduino_Project: "arduino_Sketch" = None):
        self.name = name
        self.arduino_Project = arduino_Project
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arduino_Project(self):
        return self.__arduino_Project

    @arduino_Project.setter
    def arduino_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Project__arduino_Project", None)
        self.__arduino_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Sketch"):
                opp_val = getattr(old_value, "arduino_Sketch", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Sketch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Sketch"):
                opp_val = getattr(value, "arduino_Sketch", None)
                setattr(value, "arduino_Sketch", self)
