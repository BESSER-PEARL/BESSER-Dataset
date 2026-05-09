from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SpeedUnit(Enum):
    Hz = "Hz"
    Mhz = "Mhz"
    GHz = "GHz"
    MIPS = "MIPS"
class PinNature(Enum):
    Digital = "Digital"
    Analog = "Analog"
    Mixed = "Mixed"
class TimerOp(Enum):
    initializeTimer = "initializeTimer"
class WordSize(Enum):
    wd_8bits = "wd_8bits"
    wd_16bits = "wd_16bits"
    wd_24bits = "wd_24bits"
    wd_32bits = "wd_32bits"
    wd_48bits = "wd_48bits"
    wd_64bits = "wd_64bits"
class MemoryUnit(Enum):
    Mo = "Mo"
    Go = "Go"
    Ko = "Ko"
class OperationName(Enum):
    digitalPinRead = "digitalPinRead"
    digitalPinWrite = "digitalPinWrite"
    analogPinRead = "analogPinRead"
    analogPinWrite = "analogPinWrite"
    pinConfigMode = "pinConfigMode"
class RegType(Enum):
    accumulator = "accumulator"
    general = "general"
    PCounter = "PCounter"
    Stack = "Stack"
    CCR = "CCR"
    ICR = "ICR"
    IR = "IR"
class PinModes(Enum):
    Input = "Input"
    Output = "Output"


############################################
# Definition of Classes
############################################

class EEPROM:

    pass
class ROM:

    pass
class MicrocontrollerModeling_EEPROM(ROM):

    pass
class Memory:

    pass
class MicrocontrollerModeling_PinMode:

    def __init__(self, name: str, value: str, MicrocontrollerModeling_PinMode: "MicrocontrollerModeling_CLanguage" = None):
        self.name = name
        self.value = value
        self.MicrocontrollerModeling_PinMode = MicrocontrollerModeling_PinMode
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def MicrocontrollerModeling_PinMode(self):
        return self.__MicrocontrollerModeling_PinMode

    @MicrocontrollerModeling_PinMode.setter
    def MicrocontrollerModeling_PinMode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_PinMode__MicrocontrollerModeling_PinMode", None)
        self.__MicrocontrollerModeling_PinMode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MicrocontrollerModeling_CLanguage18"):
                opp_val = getattr(old_value, "MicrocontrollerModeling_CLanguage18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MicrocontrollerModeling_CLanguage18"):
                opp_val = getattr(value, "MicrocontrollerModeling_CLanguage18", None)
                if opp_val is None:
                    setattr(value, "MicrocontrollerModeling_CLanguage18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MicrocontrollerModeling_Library:

    def __init__(self, name: str, MicrocontrollerModeling_Library: "MicrocontrollerModeling_CLanguage" = None):
        self.name = name
        self.MicrocontrollerModeling_Library = MicrocontrollerModeling_Library
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def MicrocontrollerModeling_Library(self):
        return self.__MicrocontrollerModeling_Library

    @MicrocontrollerModeling_Library.setter
    def MicrocontrollerModeling_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_Library__MicrocontrollerModeling_Library", None)
        self.__MicrocontrollerModeling_Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MicrocontrollerModeling_CLanguage14"):
                opp_val = getattr(old_value, "MicrocontrollerModeling_CLanguage14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MicrocontrollerModeling_CLanguage14"):
                opp_val = getattr(value, "MicrocontrollerModeling_CLanguage14", None)
                if opp_val is None:
                    setattr(value, "MicrocontrollerModeling_CLanguage14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MicrocontrollerModeling_Register:

    def __init__(self, type: str, name: str, MicrocontrollerModeling_Register: "MicrocontrollerModeling_Microcontroller" = None):
        self.type = type
        self.name = name
        self.MicrocontrollerModeling_Register = MicrocontrollerModeling_Register
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def MicrocontrollerModeling_Register(self):
        return self.__MicrocontrollerModeling_Register

    @MicrocontrollerModeling_Register.setter
    def MicrocontrollerModeling_Register(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_Register__MicrocontrollerModeling_Register", None)
        self.__MicrocontrollerModeling_Register = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MicrocontrollerModeling_Microcontroller12"):
                opp_val = getattr(old_value, "MicrocontrollerModeling_Microcontroller12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MicrocontrollerModeling_Microcontroller12"):
                opp_val = getattr(value, "MicrocontrollerModeling_Microcontroller12", None)
                if opp_val is None:
                    setattr(value, "MicrocontrollerModeling_Microcontroller12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MicrocontrollerModeling_RAM(Memory):

    pass
class MicrocontrollerModeling_Flash(EEPROM):

    pass
class MicrocontrollerModeling_Memory(ABC):

    def __init__(self, unit: str, size: int):
        self.unit = unit
        self.size = size
        
        pass
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size


    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


class Function:

    pass
class MicrocontrollerModeling_TimerConfig(Function):

    def __init__(self, name: str, period: int, MicrocontrollerModeling_TimerConfig: "MicrocontrollerModeling_CLanguage" = None):
        self.name = name
        self.period = period
        self.MicrocontrollerModeling_TimerConfig = MicrocontrollerModeling_TimerConfig
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def period(self):
        return self.__period

    @period.setter
    def period(self, period: int):
        self.__period = period


    @property
    def MicrocontrollerModeling_TimerConfig(self):
        return self.__MicrocontrollerModeling_TimerConfig

    @MicrocontrollerModeling_TimerConfig.setter
    def MicrocontrollerModeling_TimerConfig(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_TimerConfig__MicrocontrollerModeling_TimerConfig", None)
        self.__MicrocontrollerModeling_TimerConfig = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MicrocontrollerModeling_CLanguage16"):
                opp_val = getattr(old_value, "MicrocontrollerModeling_CLanguage16", None)
                if opp_val == self:
                    setattr(old_value, "MicrocontrollerModeling_CLanguage16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MicrocontrollerModeling_CLanguage16"):
                opp_val = getattr(value, "MicrocontrollerModeling_CLanguage16", None)
                setattr(value, "MicrocontrollerModeling_CLanguage16", self)

class MicrocontrollerModeling_Instruction:

    def __init__(self, value: str, MicrocontrollerModeling_Instruction: "MicrocontrollerModeling_Function" = None):
        self.value = value
        self.MicrocontrollerModeling_Instruction = MicrocontrollerModeling_Instruction
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def MicrocontrollerModeling_Instruction(self):
        return self.__MicrocontrollerModeling_Instruction

    @MicrocontrollerModeling_Instruction.setter
    def MicrocontrollerModeling_Instruction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_Instruction__MicrocontrollerModeling_Instruction", None)
        self.__MicrocontrollerModeling_Instruction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MicrocontrollerModeling_Function23"):
                opp_val = getattr(old_value, "MicrocontrollerModeling_Function23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MicrocontrollerModeling_Function23"):
                opp_val = getattr(value, "MicrocontrollerModeling_Function23", None)
                if opp_val is None:
                    setattr(value, "MicrocontrollerModeling_Function23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MicrocontrollerModeling_Parameter:

    def __init__(self, name: str, type: str, MicrocontrollerModeling_Parameter: "MicrocontrollerModeling_Function" = None):
        self.name = name
        self.type = type
        self.MicrocontrollerModeling_Parameter = MicrocontrollerModeling_Parameter
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def MicrocontrollerModeling_Parameter(self):
        return self.__MicrocontrollerModeling_Parameter

    @MicrocontrollerModeling_Parameter.setter
    def MicrocontrollerModeling_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_Parameter__MicrocontrollerModeling_Parameter", None)
        self.__MicrocontrollerModeling_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MicrocontrollerModeling_Function"):
                opp_val = getattr(old_value, "MicrocontrollerModeling_Function", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MicrocontrollerModeling_Function"):
                opp_val = getattr(value, "MicrocontrollerModeling_Function", None)
                if opp_val is None:
                    setattr(value, "MicrocontrollerModeling_Function", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MicrocontrollerModeling_Function:

    def __init__(self, type: str, MicrocontrollerModeling_Function: set["MicrocontrollerModeling_Parameter"] = None, MicrocontrollerModeling_Function23: set["MicrocontrollerModeling_Instruction"] = None):
        self.type = type
        self.MicrocontrollerModeling_Function = MicrocontrollerModeling_Function if MicrocontrollerModeling_Function is not None else set()
        self.MicrocontrollerModeling_Function23 = MicrocontrollerModeling_Function23 if MicrocontrollerModeling_Function23 is not None else set()
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def MicrocontrollerModeling_Function23(self):
        return self.__MicrocontrollerModeling_Function23

    @MicrocontrollerModeling_Function23.setter
    def MicrocontrollerModeling_Function23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_Function__MicrocontrollerModeling_Function23", None)
        self.__MicrocontrollerModeling_Function23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MicrocontrollerModeling_Instruction"):
                    opp_val = getattr(item, "MicrocontrollerModeling_Instruction", None)
                    
                    if opp_val == self:
                        setattr(item, "MicrocontrollerModeling_Instruction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MicrocontrollerModeling_Instruction"):
                    opp_val = getattr(item, "MicrocontrollerModeling_Instruction", None)
                    
                    setattr(item, "MicrocontrollerModeling_Instruction", self)
                    

    @property
    def MicrocontrollerModeling_Function(self):
        return self.__MicrocontrollerModeling_Function

    @MicrocontrollerModeling_Function.setter
    def MicrocontrollerModeling_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_Function__MicrocontrollerModeling_Function", None)
        self.__MicrocontrollerModeling_Function = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MicrocontrollerModeling_Parameter"):
                    opp_val = getattr(item, "MicrocontrollerModeling_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "MicrocontrollerModeling_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MicrocontrollerModeling_Parameter"):
                    opp_val = getattr(item, "MicrocontrollerModeling_Parameter", None)
                    
                    setattr(item, "MicrocontrollerModeling_Parameter", self)
                    

class MicrocontrollerModeling_PinOperation(Function):

    def __init__(self, name: str, MicrocontrollerModeling_PinOperation: "MicrocontrollerModeling_CLanguage" = None):
        self.name = name
        self.MicrocontrollerModeling_PinOperation = MicrocontrollerModeling_PinOperation
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def MicrocontrollerModeling_PinOperation(self):
        return self.__MicrocontrollerModeling_PinOperation

    @MicrocontrollerModeling_PinOperation.setter
    def MicrocontrollerModeling_PinOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_PinOperation__MicrocontrollerModeling_PinOperation", None)
        self.__MicrocontrollerModeling_PinOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MicrocontrollerModeling_CLanguage20"):
                opp_val = getattr(old_value, "MicrocontrollerModeling_CLanguage20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MicrocontrollerModeling_CLanguage20"):
                opp_val = getattr(value, "MicrocontrollerModeling_CLanguage20", None)
                if opp_val is None:
                    setattr(value, "MicrocontrollerModeling_CLanguage20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MicrocontrollerModeling_ROM(Memory):

    pass
class MicrocontrollerModeling_Processor:

    def __init__(self, unit: str, speed: int, MicrocontrollerModeling_Processor: "MicrocontrollerModeling_Microcontroller" = None):
        self.unit = unit
        self.speed = speed
        self.MicrocontrollerModeling_Processor = MicrocontrollerModeling_Processor
        
        pass
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed


    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


    @property
    def MicrocontrollerModeling_Processor(self):
        return self.__MicrocontrollerModeling_Processor

    @MicrocontrollerModeling_Processor.setter
    def MicrocontrollerModeling_Processor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_Processor__MicrocontrollerModeling_Processor", None)
        self.__MicrocontrollerModeling_Processor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MicrocontrollerModeling_Microcontroller4"):
                opp_val = getattr(old_value, "MicrocontrollerModeling_Microcontroller4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MicrocontrollerModeling_Microcontroller4"):
                opp_val = getattr(value, "MicrocontrollerModeling_Microcontroller4", None)
                if opp_val is None:
                    setattr(value, "MicrocontrollerModeling_Microcontroller4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MicrocontrollerModeling_CLanguage:

    def __init__(self, hasMain: bool, filesExtension: str, name: str, MicrocontrollerModeling_CLanguage18: set["MicrocontrollerModeling_PinMode"] = None, MicrocontrollerModeling_CLanguage: "MicrocontrollerModeling_Microcontroller" = None, MicrocontrollerModeling_CLanguage20: set["MicrocontrollerModeling_PinOperation"] = None, MicrocontrollerModeling_CLanguage14: set["MicrocontrollerModeling_Library"] = None, MicrocontrollerModeling_CLanguage16: "MicrocontrollerModeling_TimerConfig" = None):
        self.hasMain = hasMain
        self.filesExtension = filesExtension
        self.name = name
        self.MicrocontrollerModeling_CLanguage18 = MicrocontrollerModeling_CLanguage18 if MicrocontrollerModeling_CLanguage18 is not None else set()
        self.MicrocontrollerModeling_CLanguage = MicrocontrollerModeling_CLanguage
        self.MicrocontrollerModeling_CLanguage20 = MicrocontrollerModeling_CLanguage20 if MicrocontrollerModeling_CLanguage20 is not None else set()
        self.MicrocontrollerModeling_CLanguage14 = MicrocontrollerModeling_CLanguage14 if MicrocontrollerModeling_CLanguage14 is not None else set()
        self.MicrocontrollerModeling_CLanguage16 = MicrocontrollerModeling_CLanguage16
        
        pass
    @property
    def hasMain(self):
        return self.__hasMain

    @hasMain.setter
    def hasMain(self, hasMain: bool):
        self.__hasMain = hasMain


    @property
    def filesExtension(self):
        return self.__filesExtension

    @filesExtension.setter
    def filesExtension(self, filesExtension: str):
        self.__filesExtension = filesExtension


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def MicrocontrollerModeling_CLanguage18(self):
        return self.__MicrocontrollerModeling_CLanguage18

    @MicrocontrollerModeling_CLanguage18.setter
    def MicrocontrollerModeling_CLanguage18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_CLanguage__MicrocontrollerModeling_CLanguage18", None)
        self.__MicrocontrollerModeling_CLanguage18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MicrocontrollerModeling_PinMode"):
                    opp_val = getattr(item, "MicrocontrollerModeling_PinMode", None)
                    
                    if opp_val == self:
                        setattr(item, "MicrocontrollerModeling_PinMode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MicrocontrollerModeling_PinMode"):
                    opp_val = getattr(item, "MicrocontrollerModeling_PinMode", None)
                    
                    setattr(item, "MicrocontrollerModeling_PinMode", self)
                    

    @property
    def MicrocontrollerModeling_CLanguage(self):
        return self.__MicrocontrollerModeling_CLanguage

    @MicrocontrollerModeling_CLanguage.setter
    def MicrocontrollerModeling_CLanguage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_CLanguage__MicrocontrollerModeling_CLanguage", None)
        self.__MicrocontrollerModeling_CLanguage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MicrocontrollerModeling_Microcontroller2"):
                opp_val = getattr(old_value, "MicrocontrollerModeling_Microcontroller2", None)
                if opp_val == self:
                    setattr(old_value, "MicrocontrollerModeling_Microcontroller2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MicrocontrollerModeling_Microcontroller2"):
                opp_val = getattr(value, "MicrocontrollerModeling_Microcontroller2", None)
                setattr(value, "MicrocontrollerModeling_Microcontroller2", self)

    @property
    def MicrocontrollerModeling_CLanguage20(self):
        return self.__MicrocontrollerModeling_CLanguage20

    @MicrocontrollerModeling_CLanguage20.setter
    def MicrocontrollerModeling_CLanguage20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_CLanguage__MicrocontrollerModeling_CLanguage20", None)
        self.__MicrocontrollerModeling_CLanguage20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MicrocontrollerModeling_PinOperation"):
                    opp_val = getattr(item, "MicrocontrollerModeling_PinOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "MicrocontrollerModeling_PinOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MicrocontrollerModeling_PinOperation"):
                    opp_val = getattr(item, "MicrocontrollerModeling_PinOperation", None)
                    
                    setattr(item, "MicrocontrollerModeling_PinOperation", self)
                    

    @property
    def MicrocontrollerModeling_CLanguage14(self):
        return self.__MicrocontrollerModeling_CLanguage14

    @MicrocontrollerModeling_CLanguage14.setter
    def MicrocontrollerModeling_CLanguage14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_CLanguage__MicrocontrollerModeling_CLanguage14", None)
        self.__MicrocontrollerModeling_CLanguage14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MicrocontrollerModeling_Library"):
                    opp_val = getattr(item, "MicrocontrollerModeling_Library", None)
                    
                    if opp_val == self:
                        setattr(item, "MicrocontrollerModeling_Library", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MicrocontrollerModeling_Library"):
                    opp_val = getattr(item, "MicrocontrollerModeling_Library", None)
                    
                    setattr(item, "MicrocontrollerModeling_Library", self)
                    

    @property
    def MicrocontrollerModeling_CLanguage16(self):
        return self.__MicrocontrollerModeling_CLanguage16

    @MicrocontrollerModeling_CLanguage16.setter
    def MicrocontrollerModeling_CLanguage16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_CLanguage__MicrocontrollerModeling_CLanguage16", None)
        self.__MicrocontrollerModeling_CLanguage16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MicrocontrollerModeling_TimerConfig"):
                opp_val = getattr(old_value, "MicrocontrollerModeling_TimerConfig", None)
                if opp_val == self:
                    setattr(old_value, "MicrocontrollerModeling_TimerConfig", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MicrocontrollerModeling_TimerConfig"):
                opp_val = getattr(value, "MicrocontrollerModeling_TimerConfig", None)
                setattr(value, "MicrocontrollerModeling_TimerConfig", self)

class MicrocontrollerModeling_Pin:

    def __init__(self, name: str, nature: str, number: int, MicrocontrollerModeling_Pin: "MicrocontrollerModeling_Microcontroller" = None):
        self.name = name
        self.nature = nature
        self.number = number
        self.MicrocontrollerModeling_Pin = MicrocontrollerModeling_Pin
        
        pass
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number


    @property
    def nature(self):
        return self.__nature

    @nature.setter
    def nature(self, nature: str):
        self.__nature = nature


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def MicrocontrollerModeling_Pin(self):
        return self.__MicrocontrollerModeling_Pin

    @MicrocontrollerModeling_Pin.setter
    def MicrocontrollerModeling_Pin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_Pin__MicrocontrollerModeling_Pin", None)
        self.__MicrocontrollerModeling_Pin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MicrocontrollerModeling_Microcontroller"):
                opp_val = getattr(old_value, "MicrocontrollerModeling_Microcontroller", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MicrocontrollerModeling_Microcontroller"):
                opp_val = getattr(value, "MicrocontrollerModeling_Microcontroller", None)
                if opp_val is None:
                    setattr(value, "MicrocontrollerModeling_Microcontroller", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MicrocontrollerModeling_Microcontroller:

    def __init__(self, name: str, family: str, manufacturer: str, wordMemory: str, MicrocontrollerModeling_Microcontroller: set["MicrocontrollerModeling_Pin"] = None, MicrocontrollerModeling_Microcontroller2: "MicrocontrollerModeling_CLanguage" = None, MicrocontrollerModeling_Microcontroller4: set["MicrocontrollerModeling_Processor"] = None, MicrocontrollerModeling_Microcontroller6: "MicrocontrollerModeling_ROM" = None, MicrocontrollerModeling_Microcontroller8: "MicrocontrollerModeling_Flash" = None, MicrocontrollerModeling_Microcontroller10: "MicrocontrollerModeling_RAM" = None, MicrocontrollerModeling_Microcontroller12: set["MicrocontrollerModeling_Register"] = None):
        self.name = name
        self.family = family
        self.manufacturer = manufacturer
        self.wordMemory = wordMemory
        self.MicrocontrollerModeling_Microcontroller = MicrocontrollerModeling_Microcontroller if MicrocontrollerModeling_Microcontroller is not None else set()
        self.MicrocontrollerModeling_Microcontroller2 = MicrocontrollerModeling_Microcontroller2
        self.MicrocontrollerModeling_Microcontroller4 = MicrocontrollerModeling_Microcontroller4 if MicrocontrollerModeling_Microcontroller4 is not None else set()
        self.MicrocontrollerModeling_Microcontroller6 = MicrocontrollerModeling_Microcontroller6
        self.MicrocontrollerModeling_Microcontroller8 = MicrocontrollerModeling_Microcontroller8
        self.MicrocontrollerModeling_Microcontroller10 = MicrocontrollerModeling_Microcontroller10
        self.MicrocontrollerModeling_Microcontroller12 = MicrocontrollerModeling_Microcontroller12 if MicrocontrollerModeling_Microcontroller12 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def wordMemory(self):
        return self.__wordMemory

    @wordMemory.setter
    def wordMemory(self, wordMemory: str):
        self.__wordMemory = wordMemory


    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, family: str):
        self.__family = family


    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer: str):
        self.__manufacturer = manufacturer


    @property
    def MicrocontrollerModeling_Microcontroller12(self):
        return self.__MicrocontrollerModeling_Microcontroller12

    @MicrocontrollerModeling_Microcontroller12.setter
    def MicrocontrollerModeling_Microcontroller12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_Microcontroller__MicrocontrollerModeling_Microcontroller12", None)
        self.__MicrocontrollerModeling_Microcontroller12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MicrocontrollerModeling_Register"):
                    opp_val = getattr(item, "MicrocontrollerModeling_Register", None)
                    
                    if opp_val == self:
                        setattr(item, "MicrocontrollerModeling_Register", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MicrocontrollerModeling_Register"):
                    opp_val = getattr(item, "MicrocontrollerModeling_Register", None)
                    
                    setattr(item, "MicrocontrollerModeling_Register", self)
                    

    @property
    def MicrocontrollerModeling_Microcontroller4(self):
        return self.__MicrocontrollerModeling_Microcontroller4

    @MicrocontrollerModeling_Microcontroller4.setter
    def MicrocontrollerModeling_Microcontroller4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_Microcontroller__MicrocontrollerModeling_Microcontroller4", None)
        self.__MicrocontrollerModeling_Microcontroller4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MicrocontrollerModeling_Processor"):
                    opp_val = getattr(item, "MicrocontrollerModeling_Processor", None)
                    
                    if opp_val == self:
                        setattr(item, "MicrocontrollerModeling_Processor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MicrocontrollerModeling_Processor"):
                    opp_val = getattr(item, "MicrocontrollerModeling_Processor", None)
                    
                    setattr(item, "MicrocontrollerModeling_Processor", self)
                    

    @property
    def MicrocontrollerModeling_Microcontroller8(self):
        return self.__MicrocontrollerModeling_Microcontroller8

    @MicrocontrollerModeling_Microcontroller8.setter
    def MicrocontrollerModeling_Microcontroller8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_Microcontroller__MicrocontrollerModeling_Microcontroller8", None)
        self.__MicrocontrollerModeling_Microcontroller8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MicrocontrollerModeling_Flash"):
                opp_val = getattr(old_value, "MicrocontrollerModeling_Flash", None)
                if opp_val == self:
                    setattr(old_value, "MicrocontrollerModeling_Flash", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MicrocontrollerModeling_Flash"):
                opp_val = getattr(value, "MicrocontrollerModeling_Flash", None)
                setattr(value, "MicrocontrollerModeling_Flash", self)

    @property
    def MicrocontrollerModeling_Microcontroller(self):
        return self.__MicrocontrollerModeling_Microcontroller

    @MicrocontrollerModeling_Microcontroller.setter
    def MicrocontrollerModeling_Microcontroller(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_Microcontroller__MicrocontrollerModeling_Microcontroller", None)
        self.__MicrocontrollerModeling_Microcontroller = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MicrocontrollerModeling_Pin"):
                    opp_val = getattr(item, "MicrocontrollerModeling_Pin", None)
                    
                    if opp_val == self:
                        setattr(item, "MicrocontrollerModeling_Pin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MicrocontrollerModeling_Pin"):
                    opp_val = getattr(item, "MicrocontrollerModeling_Pin", None)
                    
                    setattr(item, "MicrocontrollerModeling_Pin", self)
                    

    @property
    def MicrocontrollerModeling_Microcontroller2(self):
        return self.__MicrocontrollerModeling_Microcontroller2

    @MicrocontrollerModeling_Microcontroller2.setter
    def MicrocontrollerModeling_Microcontroller2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_Microcontroller__MicrocontrollerModeling_Microcontroller2", None)
        self.__MicrocontrollerModeling_Microcontroller2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MicrocontrollerModeling_CLanguage"):
                opp_val = getattr(old_value, "MicrocontrollerModeling_CLanguage", None)
                if opp_val == self:
                    setattr(old_value, "MicrocontrollerModeling_CLanguage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MicrocontrollerModeling_CLanguage"):
                opp_val = getattr(value, "MicrocontrollerModeling_CLanguage", None)
                setattr(value, "MicrocontrollerModeling_CLanguage", self)

    @property
    def MicrocontrollerModeling_Microcontroller10(self):
        return self.__MicrocontrollerModeling_Microcontroller10

    @MicrocontrollerModeling_Microcontroller10.setter
    def MicrocontrollerModeling_Microcontroller10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_Microcontroller__MicrocontrollerModeling_Microcontroller10", None)
        self.__MicrocontrollerModeling_Microcontroller10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MicrocontrollerModeling_RAM"):
                opp_val = getattr(old_value, "MicrocontrollerModeling_RAM", None)
                if opp_val == self:
                    setattr(old_value, "MicrocontrollerModeling_RAM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MicrocontrollerModeling_RAM"):
                opp_val = getattr(value, "MicrocontrollerModeling_RAM", None)
                setattr(value, "MicrocontrollerModeling_RAM", self)

    @property
    def MicrocontrollerModeling_Microcontroller6(self):
        return self.__MicrocontrollerModeling_Microcontroller6

    @MicrocontrollerModeling_Microcontroller6.setter
    def MicrocontrollerModeling_Microcontroller6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MicrocontrollerModeling_Microcontroller__MicrocontrollerModeling_Microcontroller6", None)
        self.__MicrocontrollerModeling_Microcontroller6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MicrocontrollerModeling_ROM"):
                opp_val = getattr(old_value, "MicrocontrollerModeling_ROM", None)
                if opp_val == self:
                    setattr(old_value, "MicrocontrollerModeling_ROM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MicrocontrollerModeling_ROM"):
                opp_val = getattr(value, "MicrocontrollerModeling_ROM", None)
                setattr(value, "MicrocontrollerModeling_ROM", self)
