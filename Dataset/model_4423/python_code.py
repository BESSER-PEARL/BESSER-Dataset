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

class iot2_Sketch:

    pass
class iot2_Board:

    def __init__(self, name: str, type: str, iot2_Board: "iot2_System" = None, iot2_Board6: set["iot2_HWComponent"] = None):
        self.name = name
        self.type = type
        self.iot2_Board = iot2_Board
        self.iot2_Board6 = iot2_Board6 if iot2_Board6 is not None else set()
        
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
    def iot2_Board(self):
        return self.__iot2_Board

    @iot2_Board.setter
    def iot2_Board(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Board__iot2_Board", None)
        self.__iot2_Board = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_System2"):
                opp_val = getattr(old_value, "iot2_System2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_System2"):
                opp_val = getattr(value, "iot2_System2", None)
                if opp_val is None:
                    setattr(value, "iot2_System2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Board6(self):
        return self.__iot2_Board6

    @iot2_Board6.setter
    def iot2_Board6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Board__iot2_Board6", None)
        self.__iot2_Board6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_HWComponent7"):
                    opp_val = getattr(item, "iot2_HWComponent7", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_HWComponent7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_HWComponent7"):
                    opp_val = getattr(item, "iot2_HWComponent7", None)
                    
                    setattr(item, "iot2_HWComponent7", self)
                    

class iot2_HWComponent(ABC):

    def __init__(self, name: str, iot2_HWComponent11: set["iot2_OperationDef"] = None, iot2_HWComponent: "iot2_System" = None, iot2_HWComponent7: "iot2_Board" = None):
        self.name = name
        self.iot2_HWComponent11 = iot2_HWComponent11 if iot2_HWComponent11 is not None else set()
        self.iot2_HWComponent = iot2_HWComponent
        self.iot2_HWComponent7 = iot2_HWComponent7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iot2_HWComponent7(self):
        return self.__iot2_HWComponent7

    @iot2_HWComponent7.setter
    def iot2_HWComponent7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_HWComponent__iot2_HWComponent7", None)
        self.__iot2_HWComponent7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Board6"):
                opp_val = getattr(old_value, "iot2_Board6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Board6"):
                opp_val = getattr(value, "iot2_Board6", None)
                if opp_val is None:
                    setattr(value, "iot2_Board6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_HWComponent11(self):
        return self.__iot2_HWComponent11

    @iot2_HWComponent11.setter
    def iot2_HWComponent11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_HWComponent__iot2_HWComponent11", None)
        self.__iot2_HWComponent11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_OperationDef"):
                    opp_val = getattr(item, "iot2_OperationDef", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_OperationDef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_OperationDef"):
                    opp_val = getattr(item, "iot2_OperationDef", None)
                    
                    setattr(item, "iot2_OperationDef", self)
                    

    @property
    def iot2_HWComponent(self):
        return self.__iot2_HWComponent

    @iot2_HWComponent.setter
    def iot2_HWComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_HWComponent__iot2_HWComponent", None)
        self.__iot2_HWComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_System"):
                opp_val = getattr(old_value, "iot2_System", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_System"):
                opp_val = getattr(value, "iot2_System", None)
                if opp_val is None:
                    setattr(value, "iot2_System", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class HWComponent:

    pass
class iot2_Actuator(HWComponent):

    pass
class iot2_Sensor(HWComponent):

    pass
class iot2_OperationDef:

    pass
class iot2_Activity:

    pass
class iot2_System:

    def __init__(self, name: str, iot2_System: set["iot2_HWComponent"] = None, iot2_System2: set["iot2_Board"] = None, iot2_System4: "iot2_Sketch" = None):
        self.name = name
        self.iot2_System = iot2_System if iot2_System is not None else set()
        self.iot2_System2 = iot2_System2 if iot2_System2 is not None else set()
        self.iot2_System4 = iot2_System4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iot2_System(self):
        return self.__iot2_System

    @iot2_System.setter
    def iot2_System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_System__iot2_System", None)
        self.__iot2_System = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_HWComponent"):
                    opp_val = getattr(item, "iot2_HWComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_HWComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_HWComponent"):
                    opp_val = getattr(item, "iot2_HWComponent", None)
                    
                    setattr(item, "iot2_HWComponent", self)
                    

    @property
    def iot2_System2(self):
        return self.__iot2_System2

    @iot2_System2.setter
    def iot2_System2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_System__iot2_System2", None)
        self.__iot2_System2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Board"):
                    opp_val = getattr(item, "iot2_Board", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Board", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Board"):
                    opp_val = getattr(item, "iot2_Board", None)
                    
                    setattr(item, "iot2_Board", self)
                    

    @property
    def iot2_System4(self):
        return self.__iot2_System4

    @iot2_System4.setter
    def iot2_System4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_System__iot2_System4", None)
        self.__iot2_System4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Sketch"):
                opp_val = getattr(old_value, "iot2_Sketch", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Sketch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Sketch"):
                opp_val = getattr(value, "iot2_Sketch", None)
                setattr(value, "iot2_Sketch", self)
