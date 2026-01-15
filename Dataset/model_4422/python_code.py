from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BoardType(Enum):
    RaspberryPi = "RaspberryPi"
    Arduino = "Arduino"
    BeagleBoard = "BeagleBoard"


############################################
# Definition of Classes
############################################

class iot_IotActivity(ABC):

    pass
class iot_Sketch:

    pass
class iot_Board:

    def __init__(self, name: str, type: str, iot_Board8: set["iot_HWComp"] = None, iot_Board: "iot_System" = None):
        self.name = name
        self.type = type
        self.iot_Board8 = iot_Board8 if iot_Board8 is not None else set()
        self.iot_Board = iot_Board
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iot_Board8(self):
        return self.__iot_Board8

    @iot_Board8.setter
    def iot_Board8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Board__iot_Board8", None)
        self.__iot_Board8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot_HWComp9"):
                    opp_val = getattr(item, "iot_HWComp9", None)
                    
                    if opp_val == self:
                        setattr(item, "iot_HWComp9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot_HWComp9"):
                    opp_val = getattr(item, "iot_HWComp9", None)
                    
                    setattr(item, "iot_HWComp9", self)
                    

    @property
    def iot_Board(self):
        return self.__iot_Board

    @iot_Board.setter
    def iot_Board(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Board__iot_Board", None)
        self.__iot_Board = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_System4"):
                opp_val = getattr(old_value, "iot_System4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_System4"):
                opp_val = getattr(value, "iot_System4", None)
                if opp_val is None:
                    setattr(value, "iot_System4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iot_System:

    def __init__(self, name: str, iot_System: set["iot_HWComp"] = None, iot_System4: set["iot_Board"] = None, iot_System6: "iot_Sketch" = None):
        self.name = name
        self.iot_System = iot_System if iot_System is not None else set()
        self.iot_System4 = iot_System4 if iot_System4 is not None else set()
        self.iot_System6 = iot_System6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iot_System6(self):
        return self.__iot_System6

    @iot_System6.setter
    def iot_System6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_System__iot_System6", None)
        self.__iot_System6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Sketch"):
                opp_val = getattr(old_value, "iot_Sketch", None)
                if opp_val == self:
                    setattr(old_value, "iot_Sketch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Sketch"):
                opp_val = getattr(value, "iot_Sketch", None)
                setattr(value, "iot_Sketch", self)

    @property
    def iot_System(self):
        return self.__iot_System

    @iot_System.setter
    def iot_System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_System__iot_System", None)
        self.__iot_System = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot_HWComp2"):
                    opp_val = getattr(item, "iot_HWComp2", None)
                    
                    if opp_val == self:
                        setattr(item, "iot_HWComp2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot_HWComp2"):
                    opp_val = getattr(item, "iot_HWComp2", None)
                    
                    setattr(item, "iot_HWComp2", self)
                    

    @property
    def iot_System4(self):
        return self.__iot_System4

    @iot_System4.setter
    def iot_System4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_System__iot_System4", None)
        self.__iot_System4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot_Board"):
                    opp_val = getattr(item, "iot_Board", None)
                    
                    if opp_val == self:
                        setattr(item, "iot_Board", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot_Board"):
                    opp_val = getattr(item, "iot_Board", None)
                    
                    setattr(item, "iot_Board", self)
                    

class HWComp:

    pass
class iot_Actuator(HWComp):

    pass
class iot_Sensor(HWComp):

    pass
class iot_HWComp(ABC):

    def __init__(self, name: str, iot_HWComp9: "iot_Board" = None, iot_HWComp: set["iot_IotOperationDef"] = None, iot_HWComp2: "iot_System" = None):
        self.name = name
        self.iot_HWComp9 = iot_HWComp9
        self.iot_HWComp = iot_HWComp if iot_HWComp is not None else set()
        self.iot_HWComp2 = iot_HWComp2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iot_HWComp2(self):
        return self.__iot_HWComp2

    @iot_HWComp2.setter
    def iot_HWComp2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_HWComp__iot_HWComp2", None)
        self.__iot_HWComp2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_System"):
                opp_val = getattr(old_value, "iot_System", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_System"):
                opp_val = getattr(value, "iot_System", None)
                if opp_val is None:
                    setattr(value, "iot_System", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot_HWComp9(self):
        return self.__iot_HWComp9

    @iot_HWComp9.setter
    def iot_HWComp9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_HWComp__iot_HWComp9", None)
        self.__iot_HWComp9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Board8"):
                opp_val = getattr(old_value, "iot_Board8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Board8"):
                opp_val = getattr(value, "iot_Board8", None)
                if opp_val is None:
                    setattr(value, "iot_Board8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot_HWComp(self):
        return self.__iot_HWComp

    @iot_HWComp.setter
    def iot_HWComp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_HWComp__iot_HWComp", None)
        self.__iot_HWComp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot_IotOperationDef"):
                    opp_val = getattr(item, "iot_IotOperationDef", None)
                    
                    if opp_val == self:
                        setattr(item, "iot_IotOperationDef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot_IotOperationDef"):
                    opp_val = getattr(item, "iot_IotOperationDef", None)
                    
                    setattr(item, "iot_IotOperationDef", self)
                    

class iot_IotOperationDef(ABC):

    pass