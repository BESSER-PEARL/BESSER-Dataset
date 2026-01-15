from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Datatype(Enum):
    int8 = "int8"
    int16 = "int16"
    int32 = "int32"
    int64 = "int64"
    float32 = "float32"
    float64 = "float64"
    string = "string"
    msg = "msg"


############################################
# Definition of Classes
############################################

class rosmodel_Field:

    def __init__(self, name: str, type: str, rosmodel_Field: "rosmodel_Message" = None, rosmodel_Field39: "rosmodel_ServiceType" = None, rosmodel_Field42: "rosmodel_ServiceType" = None, rosmodel_Field51: "rosmodel_ActionMessage" = None, rosmodel_Field54: "rosmodel_ActionMessage" = None, rosmodel_Field57: "rosmodel_ActionMessage" = None):
        self.name = name
        self.type = type
        self.rosmodel_Field = rosmodel_Field
        self.rosmodel_Field39 = rosmodel_Field39
        self.rosmodel_Field42 = rosmodel_Field42
        self.rosmodel_Field51 = rosmodel_Field51
        self.rosmodel_Field54 = rosmodel_Field54
        self.rosmodel_Field57 = rosmodel_Field57
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def rosmodel_Field51(self):
        return self.__rosmodel_Field51

    @rosmodel_Field51.setter
    def rosmodel_Field51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Field__rosmodel_Field51", None)
        self.__rosmodel_Field51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_ActionMessage50"):
                opp_val = getattr(old_value, "rosmodel_ActionMessage50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_ActionMessage50"):
                opp_val = getattr(value, "rosmodel_ActionMessage50", None)
                if opp_val is None:
                    setattr(value, "rosmodel_ActionMessage50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rosmodel_Field54(self):
        return self.__rosmodel_Field54

    @rosmodel_Field54.setter
    def rosmodel_Field54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Field__rosmodel_Field54", None)
        self.__rosmodel_Field54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_ActionMessage53"):
                opp_val = getattr(old_value, "rosmodel_ActionMessage53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_ActionMessage53"):
                opp_val = getattr(value, "rosmodel_ActionMessage53", None)
                if opp_val is None:
                    setattr(value, "rosmodel_ActionMessage53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rosmodel_Field(self):
        return self.__rosmodel_Field

    @rosmodel_Field.setter
    def rosmodel_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Field__rosmodel_Field", None)
        self.__rosmodel_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Message36"):
                opp_val = getattr(old_value, "rosmodel_Message36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Message36"):
                opp_val = getattr(value, "rosmodel_Message36", None)
                if opp_val is None:
                    setattr(value, "rosmodel_Message36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rosmodel_Field57(self):
        return self.__rosmodel_Field57

    @rosmodel_Field57.setter
    def rosmodel_Field57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Field__rosmodel_Field57", None)
        self.__rosmodel_Field57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_ActionMessage56"):
                opp_val = getattr(old_value, "rosmodel_ActionMessage56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_ActionMessage56"):
                opp_val = getattr(value, "rosmodel_ActionMessage56", None)
                if opp_val is None:
                    setattr(value, "rosmodel_ActionMessage56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rosmodel_Field42(self):
        return self.__rosmodel_Field42

    @rosmodel_Field42.setter
    def rosmodel_Field42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Field__rosmodel_Field42", None)
        self.__rosmodel_Field42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_ServiceType41"):
                opp_val = getattr(old_value, "rosmodel_ServiceType41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_ServiceType41"):
                opp_val = getattr(value, "rosmodel_ServiceType41", None)
                if opp_val is None:
                    setattr(value, "rosmodel_ServiceType41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rosmodel_Field39(self):
        return self.__rosmodel_Field39

    @rosmodel_Field39.setter
    def rosmodel_Field39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Field__rosmodel_Field39", None)
        self.__rosmodel_Field39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_ServiceType38"):
                opp_val = getattr(old_value, "rosmodel_ServiceType38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_ServiceType38"):
                opp_val = getattr(value, "rosmodel_ServiceType38", None)
                if opp_val is None:
                    setattr(value, "rosmodel_ServiceType38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rosmodel_Event:

    def __init__(self, name: str, rosmodel_Event: "rosmodel_Node" = None, rosmodel_Event81: "rosmodel_State" = None, rosmodel_Event95: "rosmodel_Transition" = None):
        self.name = name
        self.rosmodel_Event = rosmodel_Event
        self.rosmodel_Event81 = rosmodel_Event81
        self.rosmodel_Event95 = rosmodel_Event95
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rosmodel_Event95(self):
        return self.__rosmodel_Event95

    @rosmodel_Event95.setter
    def rosmodel_Event95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Event__rosmodel_Event95", None)
        self.__rosmodel_Event95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Transition96"):
                opp_val = getattr(old_value, "rosmodel_Transition96", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_Transition96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Transition96"):
                opp_val = getattr(value, "rosmodel_Transition96", None)
                setattr(value, "rosmodel_Transition96", self)

    @property
    def rosmodel_Event(self):
        return self.__rosmodel_Event

    @rosmodel_Event.setter
    def rosmodel_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Event__rosmodel_Event", None)
        self.__rosmodel_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Node28"):
                opp_val = getattr(old_value, "rosmodel_Node28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Node28"):
                opp_val = getattr(value, "rosmodel_Node28", None)
                if opp_val is None:
                    setattr(value, "rosmodel_Node28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rosmodel_Event81(self):
        return self.__rosmodel_Event81

    @rosmodel_Event81.setter
    def rosmodel_Event81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Event__rosmodel_Event81", None)
        self.__rosmodel_Event81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_State80"):
                opp_val = getattr(old_value, "rosmodel_State80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_State80"):
                opp_val = getattr(value, "rosmodel_State80", None)
                if opp_val is None:
                    setattr(value, "rosmodel_State80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rosmodel_Action:

    def __init__(self, name: str, rosmodel_Action: "rosmodel_Node" = None, rosmodel_Action72: "rosmodel_State" = None, rosmodel_Action75: "rosmodel_State" = None, rosmodel_Action78: "rosmodel_State" = None, rosmodel_Action90: "rosmodel_Transition" = None, rosmodel_Action93: "rosmodel_Transition" = None):
        self.name = name
        self.rosmodel_Action = rosmodel_Action
        self.rosmodel_Action72 = rosmodel_Action72
        self.rosmodel_Action75 = rosmodel_Action75
        self.rosmodel_Action78 = rosmodel_Action78
        self.rosmodel_Action90 = rosmodel_Action90
        self.rosmodel_Action93 = rosmodel_Action93
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rosmodel_Action90(self):
        return self.__rosmodel_Action90

    @rosmodel_Action90.setter
    def rosmodel_Action90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Action__rosmodel_Action90", None)
        self.__rosmodel_Action90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Transition89"):
                opp_val = getattr(old_value, "rosmodel_Transition89", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_Transition89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Transition89"):
                opp_val = getattr(value, "rosmodel_Transition89", None)
                setattr(value, "rosmodel_Transition89", self)

    @property
    def rosmodel_Action75(self):
        return self.__rosmodel_Action75

    @rosmodel_Action75.setter
    def rosmodel_Action75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Action__rosmodel_Action75", None)
        self.__rosmodel_Action75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_State74"):
                opp_val = getattr(old_value, "rosmodel_State74", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_State74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_State74"):
                opp_val = getattr(value, "rosmodel_State74", None)
                setattr(value, "rosmodel_State74", self)

    @property
    def rosmodel_Action78(self):
        return self.__rosmodel_Action78

    @rosmodel_Action78.setter
    def rosmodel_Action78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Action__rosmodel_Action78", None)
        self.__rosmodel_Action78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_State77"):
                opp_val = getattr(old_value, "rosmodel_State77", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_State77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_State77"):
                opp_val = getattr(value, "rosmodel_State77", None)
                setattr(value, "rosmodel_State77", self)

    @property
    def rosmodel_Action93(self):
        return self.__rosmodel_Action93

    @rosmodel_Action93.setter
    def rosmodel_Action93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Action__rosmodel_Action93", None)
        self.__rosmodel_Action93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Transition92"):
                opp_val = getattr(old_value, "rosmodel_Transition92", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_Transition92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Transition92"):
                opp_val = getattr(value, "rosmodel_Transition92", None)
                setattr(value, "rosmodel_Transition92", self)

    @property
    def rosmodel_Action(self):
        return self.__rosmodel_Action

    @rosmodel_Action.setter
    def rosmodel_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Action__rosmodel_Action", None)
        self.__rosmodel_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Node26"):
                opp_val = getattr(old_value, "rosmodel_Node26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Node26"):
                opp_val = getattr(value, "rosmodel_Node26", None)
                if opp_val is None:
                    setattr(value, "rosmodel_Node26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rosmodel_Action72(self):
        return self.__rosmodel_Action72

    @rosmodel_Action72.setter
    def rosmodel_Action72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Action__rosmodel_Action72", None)
        self.__rosmodel_Action72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_State71"):
                opp_val = getattr(old_value, "rosmodel_State71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_State71"):
                opp_val = getattr(value, "rosmodel_State71", None)
                if opp_val is None:
                    setattr(value, "rosmodel_State71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rosmodel_Transition:

    def __init__(self, name: str, rosmodel_Transition: "rosmodel_Node" = None, rosmodel_Transition66: "rosmodel_State" = None, rosmodel_Transition83: "rosmodel_State" = None, rosmodel_Transition86: "rosmodel_State" = None, rosmodel_Transition89: "rosmodel_Action" = None, rosmodel_Transition92: "rosmodel_Action" = None, rosmodel_Transition96: "rosmodel_Event" = None):
        self.name = name
        self.rosmodel_Transition = rosmodel_Transition
        self.rosmodel_Transition66 = rosmodel_Transition66
        self.rosmodel_Transition83 = rosmodel_Transition83
        self.rosmodel_Transition86 = rosmodel_Transition86
        self.rosmodel_Transition89 = rosmodel_Transition89
        self.rosmodel_Transition92 = rosmodel_Transition92
        self.rosmodel_Transition96 = rosmodel_Transition96
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rosmodel_Transition83(self):
        return self.__rosmodel_Transition83

    @rosmodel_Transition83.setter
    def rosmodel_Transition83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Transition__rosmodel_Transition83", None)
        self.__rosmodel_Transition83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_State84"):
                opp_val = getattr(old_value, "rosmodel_State84", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_State84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_State84"):
                opp_val = getattr(value, "rosmodel_State84", None)
                setattr(value, "rosmodel_State84", self)

    @property
    def rosmodel_Transition66(self):
        return self.__rosmodel_Transition66

    @rosmodel_Transition66.setter
    def rosmodel_Transition66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Transition__rosmodel_Transition66", None)
        self.__rosmodel_Transition66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_State65"):
                opp_val = getattr(old_value, "rosmodel_State65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_State65"):
                opp_val = getattr(value, "rosmodel_State65", None)
                if opp_val is None:
                    setattr(value, "rosmodel_State65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rosmodel_Transition(self):
        return self.__rosmodel_Transition

    @rosmodel_Transition.setter
    def rosmodel_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Transition__rosmodel_Transition", None)
        self.__rosmodel_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Node24"):
                opp_val = getattr(old_value, "rosmodel_Node24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Node24"):
                opp_val = getattr(value, "rosmodel_Node24", None)
                if opp_val is None:
                    setattr(value, "rosmodel_Node24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rosmodel_Transition92(self):
        return self.__rosmodel_Transition92

    @rosmodel_Transition92.setter
    def rosmodel_Transition92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Transition__rosmodel_Transition92", None)
        self.__rosmodel_Transition92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Action93"):
                opp_val = getattr(old_value, "rosmodel_Action93", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_Action93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Action93"):
                opp_val = getattr(value, "rosmodel_Action93", None)
                setattr(value, "rosmodel_Action93", self)

    @property
    def rosmodel_Transition96(self):
        return self.__rosmodel_Transition96

    @rosmodel_Transition96.setter
    def rosmodel_Transition96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Transition__rosmodel_Transition96", None)
        self.__rosmodel_Transition96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Event95"):
                opp_val = getattr(old_value, "rosmodel_Event95", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_Event95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Event95"):
                opp_val = getattr(value, "rosmodel_Event95", None)
                setattr(value, "rosmodel_Event95", self)

    @property
    def rosmodel_Transition89(self):
        return self.__rosmodel_Transition89

    @rosmodel_Transition89.setter
    def rosmodel_Transition89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Transition__rosmodel_Transition89", None)
        self.__rosmodel_Transition89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Action90"):
                opp_val = getattr(old_value, "rosmodel_Action90", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_Action90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Action90"):
                opp_val = getattr(value, "rosmodel_Action90", None)
                setattr(value, "rosmodel_Action90", self)

    @property
    def rosmodel_Transition86(self):
        return self.__rosmodel_Transition86

    @rosmodel_Transition86.setter
    def rosmodel_Transition86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Transition__rosmodel_Transition86", None)
        self.__rosmodel_Transition86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_State87"):
                opp_val = getattr(old_value, "rosmodel_State87", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_State87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_State87"):
                opp_val = getattr(value, "rosmodel_State87", None)
                setattr(value, "rosmodel_State87", self)

class rosmodel_State:

    def __init__(self, name: str, rosmodel_State: "rosmodel_Node" = None, rosmodel_State65: set["rosmodel_Transition"] = None, rosmodel_State69: "rosmodel_State" = None, rosmodel_State67: set["rosmodel_State"] = None, rosmodel_State71: set["rosmodel_Action"] = None, rosmodel_State74: "rosmodel_Action" = None, rosmodel_State77: "rosmodel_Action" = None, rosmodel_State80: set["rosmodel_Event"] = None, rosmodel_State84: "rosmodel_Transition" = None, rosmodel_State87: "rosmodel_Transition" = None):
        self.name = name
        self.rosmodel_State = rosmodel_State
        self.rosmodel_State65 = rosmodel_State65 if rosmodel_State65 is not None else set()
        self.rosmodel_State69 = rosmodel_State69
        self.rosmodel_State67 = rosmodel_State67 if rosmodel_State67 is not None else set()
        self.rosmodel_State71 = rosmodel_State71 if rosmodel_State71 is not None else set()
        self.rosmodel_State74 = rosmodel_State74
        self.rosmodel_State77 = rosmodel_State77
        self.rosmodel_State80 = rosmodel_State80 if rosmodel_State80 is not None else set()
        self.rosmodel_State84 = rosmodel_State84
        self.rosmodel_State87 = rosmodel_State87
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rosmodel_State67(self):
        return self.__rosmodel_State67

    @rosmodel_State67.setter
    def rosmodel_State67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_State__rosmodel_State67", None)
        self.__rosmodel_State67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_State69"):
                    opp_val = getattr(item, "rosmodel_State69", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_State69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_State69"):
                    opp_val = getattr(item, "rosmodel_State69", None)
                    
                    setattr(item, "rosmodel_State69", self)
                    

    @property
    def rosmodel_State77(self):
        return self.__rosmodel_State77

    @rosmodel_State77.setter
    def rosmodel_State77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_State__rosmodel_State77", None)
        self.__rosmodel_State77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Action78"):
                opp_val = getattr(old_value, "rosmodel_Action78", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_Action78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Action78"):
                opp_val = getattr(value, "rosmodel_Action78", None)
                setattr(value, "rosmodel_Action78", self)

    @property
    def rosmodel_State80(self):
        return self.__rosmodel_State80

    @rosmodel_State80.setter
    def rosmodel_State80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_State__rosmodel_State80", None)
        self.__rosmodel_State80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_Event81"):
                    opp_val = getattr(item, "rosmodel_Event81", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_Event81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_Event81"):
                    opp_val = getattr(item, "rosmodel_Event81", None)
                    
                    setattr(item, "rosmodel_Event81", self)
                    

    @property
    def rosmodel_State65(self):
        return self.__rosmodel_State65

    @rosmodel_State65.setter
    def rosmodel_State65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_State__rosmodel_State65", None)
        self.__rosmodel_State65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_Transition66"):
                    opp_val = getattr(item, "rosmodel_Transition66", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_Transition66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_Transition66"):
                    opp_val = getattr(item, "rosmodel_Transition66", None)
                    
                    setattr(item, "rosmodel_Transition66", self)
                    

    @property
    def rosmodel_State69(self):
        return self.__rosmodel_State69

    @rosmodel_State69.setter
    def rosmodel_State69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_State__rosmodel_State69", None)
        self.__rosmodel_State69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_State67"):
                opp_val = getattr(old_value, "rosmodel_State67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_State67"):
                opp_val = getattr(value, "rosmodel_State67", None)
                if opp_val is None:
                    setattr(value, "rosmodel_State67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rosmodel_State84(self):
        return self.__rosmodel_State84

    @rosmodel_State84.setter
    def rosmodel_State84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_State__rosmodel_State84", None)
        self.__rosmodel_State84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Transition83"):
                opp_val = getattr(old_value, "rosmodel_Transition83", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_Transition83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Transition83"):
                opp_val = getattr(value, "rosmodel_Transition83", None)
                setattr(value, "rosmodel_Transition83", self)

    @property
    def rosmodel_State71(self):
        return self.__rosmodel_State71

    @rosmodel_State71.setter
    def rosmodel_State71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_State__rosmodel_State71", None)
        self.__rosmodel_State71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_Action72"):
                    opp_val = getattr(item, "rosmodel_Action72", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_Action72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_Action72"):
                    opp_val = getattr(item, "rosmodel_Action72", None)
                    
                    setattr(item, "rosmodel_Action72", self)
                    

    @property
    def rosmodel_State87(self):
        return self.__rosmodel_State87

    @rosmodel_State87.setter
    def rosmodel_State87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_State__rosmodel_State87", None)
        self.__rosmodel_State87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Transition86"):
                opp_val = getattr(old_value, "rosmodel_Transition86", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_Transition86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Transition86"):
                opp_val = getattr(value, "rosmodel_Transition86", None)
                setattr(value, "rosmodel_Transition86", self)

    @property
    def rosmodel_State74(self):
        return self.__rosmodel_State74

    @rosmodel_State74.setter
    def rosmodel_State74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_State__rosmodel_State74", None)
        self.__rosmodel_State74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Action75"):
                opp_val = getattr(old_value, "rosmodel_Action75", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_Action75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Action75"):
                opp_val = getattr(value, "rosmodel_Action75", None)
                setattr(value, "rosmodel_Action75", self)

    @property
    def rosmodel_State(self):
        return self.__rosmodel_State

    @rosmodel_State.setter
    def rosmodel_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_State__rosmodel_State", None)
        self.__rosmodel_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Node22"):
                opp_val = getattr(old_value, "rosmodel_Node22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Node22"):
                opp_val = getattr(value, "rosmodel_Node22", None)
                if opp_val is None:
                    setattr(value, "rosmodel_Node22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rosmodel_ActionServer:

    def __init__(self, name: str, rosmodel_ActionServer: "rosmodel_Node" = None, rosmodel_ActionServer59: "rosmodel_ActionMessage" = None):
        self.name = name
        self.rosmodel_ActionServer = rosmodel_ActionServer
        self.rosmodel_ActionServer59 = rosmodel_ActionServer59
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rosmodel_ActionServer59(self):
        return self.__rosmodel_ActionServer59

    @rosmodel_ActionServer59.setter
    def rosmodel_ActionServer59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_ActionServer__rosmodel_ActionServer59", None)
        self.__rosmodel_ActionServer59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_ActionMessage60"):
                opp_val = getattr(old_value, "rosmodel_ActionMessage60", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_ActionMessage60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_ActionMessage60"):
                opp_val = getattr(value, "rosmodel_ActionMessage60", None)
                setattr(value, "rosmodel_ActionMessage60", self)

    @property
    def rosmodel_ActionServer(self):
        return self.__rosmodel_ActionServer

    @rosmodel_ActionServer.setter
    def rosmodel_ActionServer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_ActionServer__rosmodel_ActionServer", None)
        self.__rosmodel_ActionServer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Node20"):
                opp_val = getattr(old_value, "rosmodel_Node20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Node20"):
                opp_val = getattr(value, "rosmodel_Node20", None)
                if opp_val is None:
                    setattr(value, "rosmodel_Node20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rosmodel_ActionClient:

    def __init__(self, name: str, rosmodel_ActionClient: "rosmodel_Node" = None, rosmodel_ActionClient62: "rosmodel_ActionMessage" = None):
        self.name = name
        self.rosmodel_ActionClient = rosmodel_ActionClient
        self.rosmodel_ActionClient62 = rosmodel_ActionClient62
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rosmodel_ActionClient(self):
        return self.__rosmodel_ActionClient

    @rosmodel_ActionClient.setter
    def rosmodel_ActionClient(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_ActionClient__rosmodel_ActionClient", None)
        self.__rosmodel_ActionClient = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Node18"):
                opp_val = getattr(old_value, "rosmodel_Node18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Node18"):
                opp_val = getattr(value, "rosmodel_Node18", None)
                if opp_val is None:
                    setattr(value, "rosmodel_Node18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rosmodel_ActionClient62(self):
        return self.__rosmodel_ActionClient62

    @rosmodel_ActionClient62.setter
    def rosmodel_ActionClient62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_ActionClient__rosmodel_ActionClient62", None)
        self.__rosmodel_ActionClient62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_ActionMessage63"):
                opp_val = getattr(old_value, "rosmodel_ActionMessage63", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_ActionMessage63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_ActionMessage63"):
                opp_val = getattr(value, "rosmodel_ActionMessage63", None)
                setattr(value, "rosmodel_ActionMessage63", self)

class rosmodel_ServiceServer:

    def __init__(self, name: str, rosmodel_ServiceServer: "rosmodel_Node" = None, rosmodel_ServiceServer44: "rosmodel_ServiceType" = None):
        self.name = name
        self.rosmodel_ServiceServer = rosmodel_ServiceServer
        self.rosmodel_ServiceServer44 = rosmodel_ServiceServer44
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rosmodel_ServiceServer(self):
        return self.__rosmodel_ServiceServer

    @rosmodel_ServiceServer.setter
    def rosmodel_ServiceServer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_ServiceServer__rosmodel_ServiceServer", None)
        self.__rosmodel_ServiceServer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Node16"):
                opp_val = getattr(old_value, "rosmodel_Node16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Node16"):
                opp_val = getattr(value, "rosmodel_Node16", None)
                if opp_val is None:
                    setattr(value, "rosmodel_Node16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rosmodel_ServiceServer44(self):
        return self.__rosmodel_ServiceServer44

    @rosmodel_ServiceServer44.setter
    def rosmodel_ServiceServer44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_ServiceServer__rosmodel_ServiceServer44", None)
        self.__rosmodel_ServiceServer44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_ServiceType45"):
                opp_val = getattr(old_value, "rosmodel_ServiceType45", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_ServiceType45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_ServiceType45"):
                opp_val = getattr(value, "rosmodel_ServiceType45", None)
                setattr(value, "rosmodel_ServiceType45", self)

class rosmodel_ServiceClient:

    def __init__(self, name: str, rosmodel_ServiceClient: "rosmodel_Node" = None, rosmodel_ServiceClient47: "rosmodel_ServiceType" = None):
        self.name = name
        self.rosmodel_ServiceClient = rosmodel_ServiceClient
        self.rosmodel_ServiceClient47 = rosmodel_ServiceClient47
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rosmodel_ServiceClient47(self):
        return self.__rosmodel_ServiceClient47

    @rosmodel_ServiceClient47.setter
    def rosmodel_ServiceClient47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_ServiceClient__rosmodel_ServiceClient47", None)
        self.__rosmodel_ServiceClient47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_ServiceType48"):
                opp_val = getattr(old_value, "rosmodel_ServiceType48", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_ServiceType48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_ServiceType48"):
                opp_val = getattr(value, "rosmodel_ServiceType48", None)
                setattr(value, "rosmodel_ServiceType48", self)

    @property
    def rosmodel_ServiceClient(self):
        return self.__rosmodel_ServiceClient

    @rosmodel_ServiceClient.setter
    def rosmodel_ServiceClient(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_ServiceClient__rosmodel_ServiceClient", None)
        self.__rosmodel_ServiceClient = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Node14"):
                opp_val = getattr(old_value, "rosmodel_Node14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Node14"):
                opp_val = getattr(value, "rosmodel_Node14", None)
                if opp_val is None:
                    setattr(value, "rosmodel_Node14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rosmodel_Subscriber:

    def __init__(self, name: str, queue_size: int, msg: str, rosmodel_Subscriber: "rosmodel_Node" = None, rosmodel_Subscriber33: "rosmodel_Topic" = None):
        self.name = name
        self.queue_size = queue_size
        self.msg = msg
        self.rosmodel_Subscriber = rosmodel_Subscriber
        self.rosmodel_Subscriber33 = rosmodel_Subscriber33
        
    @property
    def queue_size(self) -> int:
        return self.__queue_size

    @queue_size.setter
    def queue_size(self, queue_size: int):
        self.__queue_size = queue_size

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def msg(self) -> str:
        return self.__msg

    @msg.setter
    def msg(self, msg: str):
        self.__msg = msg

    @property
    def rosmodel_Subscriber33(self):
        return self.__rosmodel_Subscriber33

    @rosmodel_Subscriber33.setter
    def rosmodel_Subscriber33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Subscriber__rosmodel_Subscriber33", None)
        self.__rosmodel_Subscriber33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Topic34"):
                opp_val = getattr(old_value, "rosmodel_Topic34", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_Topic34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Topic34"):
                opp_val = getattr(value, "rosmodel_Topic34", None)
                setattr(value, "rosmodel_Topic34", self)

    @property
    def rosmodel_Subscriber(self):
        return self.__rosmodel_Subscriber

    @rosmodel_Subscriber.setter
    def rosmodel_Subscriber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Subscriber__rosmodel_Subscriber", None)
        self.__rosmodel_Subscriber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Node12"):
                opp_val = getattr(old_value, "rosmodel_Node12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Node12"):
                opp_val = getattr(value, "rosmodel_Node12", None)
                if opp_val is None:
                    setattr(value, "rosmodel_Node12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rosmodel_Publisher:

    def __init__(self, name: str, queue_size: int, msg: str, rosmodel_Publisher: "rosmodel_Node" = None, rosmodel_Publisher30: "rosmodel_Topic" = None):
        self.name = name
        self.queue_size = queue_size
        self.msg = msg
        self.rosmodel_Publisher = rosmodel_Publisher
        self.rosmodel_Publisher30 = rosmodel_Publisher30
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def msg(self) -> str:
        return self.__msg

    @msg.setter
    def msg(self, msg: str):
        self.__msg = msg

    @property
    def queue_size(self) -> int:
        return self.__queue_size

    @queue_size.setter
    def queue_size(self, queue_size: int):
        self.__queue_size = queue_size

    @property
    def rosmodel_Publisher(self):
        return self.__rosmodel_Publisher

    @rosmodel_Publisher.setter
    def rosmodel_Publisher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Publisher__rosmodel_Publisher", None)
        self.__rosmodel_Publisher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Node10"):
                opp_val = getattr(old_value, "rosmodel_Node10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Node10"):
                opp_val = getattr(value, "rosmodel_Node10", None)
                if opp_val is None:
                    setattr(value, "rosmodel_Node10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rosmodel_Publisher30(self):
        return self.__rosmodel_Publisher30

    @rosmodel_Publisher30.setter
    def rosmodel_Publisher30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Publisher__rosmodel_Publisher30", None)
        self.__rosmodel_Publisher30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Topic31"):
                opp_val = getattr(old_value, "rosmodel_Topic31", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_Topic31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Topic31"):
                opp_val = getattr(value, "rosmodel_Topic31", None)
                setattr(value, "rosmodel_Topic31", self)

class rosmodel_ActionMessage:

    def __init__(self, name: str, rosmodel_ActionMessage: "rosmodel_Package" = None, rosmodel_ActionMessage50: set["rosmodel_Field"] = None, rosmodel_ActionMessage53: set["rosmodel_Field"] = None, rosmodel_ActionMessage56: set["rosmodel_Field"] = None, rosmodel_ActionMessage60: "rosmodel_ActionServer" = None, rosmodel_ActionMessage63: "rosmodel_ActionClient" = None):
        self.name = name
        self.rosmodel_ActionMessage = rosmodel_ActionMessage
        self.rosmodel_ActionMessage50 = rosmodel_ActionMessage50 if rosmodel_ActionMessage50 is not None else set()
        self.rosmodel_ActionMessage53 = rosmodel_ActionMessage53 if rosmodel_ActionMessage53 is not None else set()
        self.rosmodel_ActionMessage56 = rosmodel_ActionMessage56 if rosmodel_ActionMessage56 is not None else set()
        self.rosmodel_ActionMessage60 = rosmodel_ActionMessage60
        self.rosmodel_ActionMessage63 = rosmodel_ActionMessage63
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rosmodel_ActionMessage(self):
        return self.__rosmodel_ActionMessage

    @rosmodel_ActionMessage.setter
    def rosmodel_ActionMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_ActionMessage__rosmodel_ActionMessage", None)
        self.__rosmodel_ActionMessage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Package8"):
                opp_val = getattr(old_value, "rosmodel_Package8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Package8"):
                opp_val = getattr(value, "rosmodel_Package8", None)
                if opp_val is None:
                    setattr(value, "rosmodel_Package8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rosmodel_ActionMessage63(self):
        return self.__rosmodel_ActionMessage63

    @rosmodel_ActionMessage63.setter
    def rosmodel_ActionMessage63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_ActionMessage__rosmodel_ActionMessage63", None)
        self.__rosmodel_ActionMessage63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_ActionClient62"):
                opp_val = getattr(old_value, "rosmodel_ActionClient62", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_ActionClient62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_ActionClient62"):
                opp_val = getattr(value, "rosmodel_ActionClient62", None)
                setattr(value, "rosmodel_ActionClient62", self)

    @property
    def rosmodel_ActionMessage50(self):
        return self.__rosmodel_ActionMessage50

    @rosmodel_ActionMessage50.setter
    def rosmodel_ActionMessage50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_ActionMessage__rosmodel_ActionMessage50", None)
        self.__rosmodel_ActionMessage50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_Field51"):
                    opp_val = getattr(item, "rosmodel_Field51", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_Field51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_Field51"):
                    opp_val = getattr(item, "rosmodel_Field51", None)
                    
                    setattr(item, "rosmodel_Field51", self)
                    

    @property
    def rosmodel_ActionMessage53(self):
        return self.__rosmodel_ActionMessage53

    @rosmodel_ActionMessage53.setter
    def rosmodel_ActionMessage53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_ActionMessage__rosmodel_ActionMessage53", None)
        self.__rosmodel_ActionMessage53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_Field54"):
                    opp_val = getattr(item, "rosmodel_Field54", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_Field54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_Field54"):
                    opp_val = getattr(item, "rosmodel_Field54", None)
                    
                    setattr(item, "rosmodel_Field54", self)
                    

    @property
    def rosmodel_ActionMessage56(self):
        return self.__rosmodel_ActionMessage56

    @rosmodel_ActionMessage56.setter
    def rosmodel_ActionMessage56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_ActionMessage__rosmodel_ActionMessage56", None)
        self.__rosmodel_ActionMessage56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_Field57"):
                    opp_val = getattr(item, "rosmodel_Field57", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_Field57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_Field57"):
                    opp_val = getattr(item, "rosmodel_Field57", None)
                    
                    setattr(item, "rosmodel_Field57", self)
                    

    @property
    def rosmodel_ActionMessage60(self):
        return self.__rosmodel_ActionMessage60

    @rosmodel_ActionMessage60.setter
    def rosmodel_ActionMessage60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_ActionMessage__rosmodel_ActionMessage60", None)
        self.__rosmodel_ActionMessage60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_ActionServer59"):
                opp_val = getattr(old_value, "rosmodel_ActionServer59", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_ActionServer59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_ActionServer59"):
                opp_val = getattr(value, "rosmodel_ActionServer59", None)
                setattr(value, "rosmodel_ActionServer59", self)

class rosmodel_ServiceType:

    def __init__(self, name: str, rosmodel_ServiceType: "rosmodel_Package" = None, rosmodel_ServiceType38: set["rosmodel_Field"] = None, rosmodel_ServiceType41: set["rosmodel_Field"] = None, rosmodel_ServiceType45: "rosmodel_ServiceServer" = None, rosmodel_ServiceType48: "rosmodel_ServiceClient" = None):
        self.name = name
        self.rosmodel_ServiceType = rosmodel_ServiceType
        self.rosmodel_ServiceType38 = rosmodel_ServiceType38 if rosmodel_ServiceType38 is not None else set()
        self.rosmodel_ServiceType41 = rosmodel_ServiceType41 if rosmodel_ServiceType41 is not None else set()
        self.rosmodel_ServiceType45 = rosmodel_ServiceType45
        self.rosmodel_ServiceType48 = rosmodel_ServiceType48
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rosmodel_ServiceType48(self):
        return self.__rosmodel_ServiceType48

    @rosmodel_ServiceType48.setter
    def rosmodel_ServiceType48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_ServiceType__rosmodel_ServiceType48", None)
        self.__rosmodel_ServiceType48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_ServiceClient47"):
                opp_val = getattr(old_value, "rosmodel_ServiceClient47", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_ServiceClient47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_ServiceClient47"):
                opp_val = getattr(value, "rosmodel_ServiceClient47", None)
                setattr(value, "rosmodel_ServiceClient47", self)

    @property
    def rosmodel_ServiceType38(self):
        return self.__rosmodel_ServiceType38

    @rosmodel_ServiceType38.setter
    def rosmodel_ServiceType38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_ServiceType__rosmodel_ServiceType38", None)
        self.__rosmodel_ServiceType38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_Field39"):
                    opp_val = getattr(item, "rosmodel_Field39", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_Field39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_Field39"):
                    opp_val = getattr(item, "rosmodel_Field39", None)
                    
                    setattr(item, "rosmodel_Field39", self)
                    

    @property
    def rosmodel_ServiceType(self):
        return self.__rosmodel_ServiceType

    @rosmodel_ServiceType.setter
    def rosmodel_ServiceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_ServiceType__rosmodel_ServiceType", None)
        self.__rosmodel_ServiceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Package6"):
                opp_val = getattr(old_value, "rosmodel_Package6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Package6"):
                opp_val = getattr(value, "rosmodel_Package6", None)
                if opp_val is None:
                    setattr(value, "rosmodel_Package6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rosmodel_ServiceType45(self):
        return self.__rosmodel_ServiceType45

    @rosmodel_ServiceType45.setter
    def rosmodel_ServiceType45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_ServiceType__rosmodel_ServiceType45", None)
        self.__rosmodel_ServiceType45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_ServiceServer44"):
                opp_val = getattr(old_value, "rosmodel_ServiceServer44", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_ServiceServer44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_ServiceServer44"):
                opp_val = getattr(value, "rosmodel_ServiceServer44", None)
                setattr(value, "rosmodel_ServiceServer44", self)

    @property
    def rosmodel_ServiceType41(self):
        return self.__rosmodel_ServiceType41

    @rosmodel_ServiceType41.setter
    def rosmodel_ServiceType41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_ServiceType__rosmodel_ServiceType41", None)
        self.__rosmodel_ServiceType41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_Field42"):
                    opp_val = getattr(item, "rosmodel_Field42", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_Field42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_Field42"):
                    opp_val = getattr(item, "rosmodel_Field42", None)
                    
                    setattr(item, "rosmodel_Field42", self)
                    

class rosmodel_Message:

    def __init__(self, name: str, rosmodel_Message: "rosmodel_Package" = None, rosmodel_Message36: set["rosmodel_Field"] = None):
        self.name = name
        self.rosmodel_Message = rosmodel_Message
        self.rosmodel_Message36 = rosmodel_Message36 if rosmodel_Message36 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rosmodel_Message(self):
        return self.__rosmodel_Message

    @rosmodel_Message.setter
    def rosmodel_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Message__rosmodel_Message", None)
        self.__rosmodel_Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Package4"):
                opp_val = getattr(old_value, "rosmodel_Package4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Package4"):
                opp_val = getattr(value, "rosmodel_Package4", None)
                if opp_val is None:
                    setattr(value, "rosmodel_Package4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rosmodel_Message36(self):
        return self.__rosmodel_Message36

    @rosmodel_Message36.setter
    def rosmodel_Message36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Message__rosmodel_Message36", None)
        self.__rosmodel_Message36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_Field"):
                    opp_val = getattr(item, "rosmodel_Field", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_Field", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_Field"):
                    opp_val = getattr(item, "rosmodel_Field", None)
                    
                    setattr(item, "rosmodel_Field", self)
                    

class rosmodel_Topic:

    def __init__(self, name: str, rosmodel_Topic: "rosmodel_Package" = None, rosmodel_Topic31: "rosmodel_Publisher" = None, rosmodel_Topic34: "rosmodel_Subscriber" = None):
        self.name = name
        self.rosmodel_Topic = rosmodel_Topic
        self.rosmodel_Topic31 = rosmodel_Topic31
        self.rosmodel_Topic34 = rosmodel_Topic34
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rosmodel_Topic31(self):
        return self.__rosmodel_Topic31

    @rosmodel_Topic31.setter
    def rosmodel_Topic31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Topic__rosmodel_Topic31", None)
        self.__rosmodel_Topic31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Publisher30"):
                opp_val = getattr(old_value, "rosmodel_Publisher30", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_Publisher30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Publisher30"):
                opp_val = getattr(value, "rosmodel_Publisher30", None)
                setattr(value, "rosmodel_Publisher30", self)

    @property
    def rosmodel_Topic(self):
        return self.__rosmodel_Topic

    @rosmodel_Topic.setter
    def rosmodel_Topic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Topic__rosmodel_Topic", None)
        self.__rosmodel_Topic = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Package2"):
                opp_val = getattr(old_value, "rosmodel_Package2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Package2"):
                opp_val = getattr(value, "rosmodel_Package2", None)
                if opp_val is None:
                    setattr(value, "rosmodel_Package2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rosmodel_Topic34(self):
        return self.__rosmodel_Topic34

    @rosmodel_Topic34.setter
    def rosmodel_Topic34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Topic__rosmodel_Topic34", None)
        self.__rosmodel_Topic34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Subscriber33"):
                opp_val = getattr(old_value, "rosmodel_Subscriber33", None)
                if opp_val == self:
                    setattr(old_value, "rosmodel_Subscriber33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Subscriber33"):
                opp_val = getattr(value, "rosmodel_Subscriber33", None)
                setattr(value, "rosmodel_Subscriber33", self)

class rosmodel_Node:

    def __init__(self, name: str, frequency: float, rosmodel_Node: "rosmodel_Package" = None, rosmodel_Node10: set["rosmodel_Publisher"] = None, rosmodel_Node12: set["rosmodel_Subscriber"] = None, rosmodel_Node14: set["rosmodel_ServiceClient"] = None, rosmodel_Node16: set["rosmodel_ServiceServer"] = None, rosmodel_Node18: set["rosmodel_ActionClient"] = None, rosmodel_Node20: set["rosmodel_ActionServer"] = None, rosmodel_Node22: set["rosmodel_State"] = None, rosmodel_Node24: set["rosmodel_Transition"] = None, rosmodel_Node26: set["rosmodel_Action"] = None, rosmodel_Node28: set["rosmodel_Event"] = None):
        self.name = name
        self.frequency = frequency
        self.rosmodel_Node = rosmodel_Node
        self.rosmodel_Node10 = rosmodel_Node10 if rosmodel_Node10 is not None else set()
        self.rosmodel_Node12 = rosmodel_Node12 if rosmodel_Node12 is not None else set()
        self.rosmodel_Node14 = rosmodel_Node14 if rosmodel_Node14 is not None else set()
        self.rosmodel_Node16 = rosmodel_Node16 if rosmodel_Node16 is not None else set()
        self.rosmodel_Node18 = rosmodel_Node18 if rosmodel_Node18 is not None else set()
        self.rosmodel_Node20 = rosmodel_Node20 if rosmodel_Node20 is not None else set()
        self.rosmodel_Node22 = rosmodel_Node22 if rosmodel_Node22 is not None else set()
        self.rosmodel_Node24 = rosmodel_Node24 if rosmodel_Node24 is not None else set()
        self.rosmodel_Node26 = rosmodel_Node26 if rosmodel_Node26 is not None else set()
        self.rosmodel_Node28 = rosmodel_Node28 if rosmodel_Node28 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def frequency(self) -> float:
        return self.__frequency

    @frequency.setter
    def frequency(self, frequency: float):
        self.__frequency = frequency

    @property
    def rosmodel_Node28(self):
        return self.__rosmodel_Node28

    @rosmodel_Node28.setter
    def rosmodel_Node28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Node__rosmodel_Node28", None)
        self.__rosmodel_Node28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_Event"):
                    opp_val = getattr(item, "rosmodel_Event", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_Event"):
                    opp_val = getattr(item, "rosmodel_Event", None)
                    
                    setattr(item, "rosmodel_Event", self)
                    

    @property
    def rosmodel_Node10(self):
        return self.__rosmodel_Node10

    @rosmodel_Node10.setter
    def rosmodel_Node10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Node__rosmodel_Node10", None)
        self.__rosmodel_Node10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_Publisher"):
                    opp_val = getattr(item, "rosmodel_Publisher", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_Publisher", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_Publisher"):
                    opp_val = getattr(item, "rosmodel_Publisher", None)
                    
                    setattr(item, "rosmodel_Publisher", self)
                    

    @property
    def rosmodel_Node24(self):
        return self.__rosmodel_Node24

    @rosmodel_Node24.setter
    def rosmodel_Node24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Node__rosmodel_Node24", None)
        self.__rosmodel_Node24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_Transition"):
                    opp_val = getattr(item, "rosmodel_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_Transition"):
                    opp_val = getattr(item, "rosmodel_Transition", None)
                    
                    setattr(item, "rosmodel_Transition", self)
                    

    @property
    def rosmodel_Node12(self):
        return self.__rosmodel_Node12

    @rosmodel_Node12.setter
    def rosmodel_Node12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Node__rosmodel_Node12", None)
        self.__rosmodel_Node12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_Subscriber"):
                    opp_val = getattr(item, "rosmodel_Subscriber", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_Subscriber", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_Subscriber"):
                    opp_val = getattr(item, "rosmodel_Subscriber", None)
                    
                    setattr(item, "rosmodel_Subscriber", self)
                    

    @property
    def rosmodel_Node20(self):
        return self.__rosmodel_Node20

    @rosmodel_Node20.setter
    def rosmodel_Node20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Node__rosmodel_Node20", None)
        self.__rosmodel_Node20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_ActionServer"):
                    opp_val = getattr(item, "rosmodel_ActionServer", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_ActionServer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_ActionServer"):
                    opp_val = getattr(item, "rosmodel_ActionServer", None)
                    
                    setattr(item, "rosmodel_ActionServer", self)
                    

    @property
    def rosmodel_Node26(self):
        return self.__rosmodel_Node26

    @rosmodel_Node26.setter
    def rosmodel_Node26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Node__rosmodel_Node26", None)
        self.__rosmodel_Node26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_Action"):
                    opp_val = getattr(item, "rosmodel_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_Action"):
                    opp_val = getattr(item, "rosmodel_Action", None)
                    
                    setattr(item, "rosmodel_Action", self)
                    

    @property
    def rosmodel_Node16(self):
        return self.__rosmodel_Node16

    @rosmodel_Node16.setter
    def rosmodel_Node16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Node__rosmodel_Node16", None)
        self.__rosmodel_Node16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_ServiceServer"):
                    opp_val = getattr(item, "rosmodel_ServiceServer", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_ServiceServer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_ServiceServer"):
                    opp_val = getattr(item, "rosmodel_ServiceServer", None)
                    
                    setattr(item, "rosmodel_ServiceServer", self)
                    

    @property
    def rosmodel_Node(self):
        return self.__rosmodel_Node

    @rosmodel_Node.setter
    def rosmodel_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Node__rosmodel_Node", None)
        self.__rosmodel_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rosmodel_Package"):
                opp_val = getattr(old_value, "rosmodel_Package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rosmodel_Package"):
                opp_val = getattr(value, "rosmodel_Package", None)
                if opp_val is None:
                    setattr(value, "rosmodel_Package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rosmodel_Node18(self):
        return self.__rosmodel_Node18

    @rosmodel_Node18.setter
    def rosmodel_Node18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Node__rosmodel_Node18", None)
        self.__rosmodel_Node18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_ActionClient"):
                    opp_val = getattr(item, "rosmodel_ActionClient", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_ActionClient", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_ActionClient"):
                    opp_val = getattr(item, "rosmodel_ActionClient", None)
                    
                    setattr(item, "rosmodel_ActionClient", self)
                    

    @property
    def rosmodel_Node22(self):
        return self.__rosmodel_Node22

    @rosmodel_Node22.setter
    def rosmodel_Node22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Node__rosmodel_Node22", None)
        self.__rosmodel_Node22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_State"):
                    opp_val = getattr(item, "rosmodel_State", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_State"):
                    opp_val = getattr(item, "rosmodel_State", None)
                    
                    setattr(item, "rosmodel_State", self)
                    

    @property
    def rosmodel_Node14(self):
        return self.__rosmodel_Node14

    @rosmodel_Node14.setter
    def rosmodel_Node14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Node__rosmodel_Node14", None)
        self.__rosmodel_Node14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_ServiceClient"):
                    opp_val = getattr(item, "rosmodel_ServiceClient", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_ServiceClient", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_ServiceClient"):
                    opp_val = getattr(item, "rosmodel_ServiceClient", None)
                    
                    setattr(item, "rosmodel_ServiceClient", self)
                    

class rosmodel_Package:

    def __init__(self, name: str, author: str, author_email: str, description: str, depends: str, rosmodel_Package: set["rosmodel_Node"] = None, rosmodel_Package2: set["rosmodel_Topic"] = None, rosmodel_Package4: set["rosmodel_Message"] = None, rosmodel_Package6: set["rosmodel_ServiceType"] = None, rosmodel_Package8: set["rosmodel_ActionMessage"] = None):
        self.name = name
        self.author = author
        self.author_email = author_email
        self.description = description
        self.depends = depends
        self.rosmodel_Package = rosmodel_Package if rosmodel_Package is not None else set()
        self.rosmodel_Package2 = rosmodel_Package2 if rosmodel_Package2 is not None else set()
        self.rosmodel_Package4 = rosmodel_Package4 if rosmodel_Package4 is not None else set()
        self.rosmodel_Package6 = rosmodel_Package6 if rosmodel_Package6 is not None else set()
        self.rosmodel_Package8 = rosmodel_Package8 if rosmodel_Package8 is not None else set()
        
    @property
    def author_email(self) -> str:
        return self.__author_email

    @author_email.setter
    def author_email(self, author_email: str):
        self.__author_email = author_email

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def depends(self) -> str:
        return self.__depends

    @depends.setter
    def depends(self, depends: str):
        self.__depends = depends

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def rosmodel_Package(self):
        return self.__rosmodel_Package

    @rosmodel_Package.setter
    def rosmodel_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Package__rosmodel_Package", None)
        self.__rosmodel_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_Node"):
                    opp_val = getattr(item, "rosmodel_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_Node"):
                    opp_val = getattr(item, "rosmodel_Node", None)
                    
                    setattr(item, "rosmodel_Node", self)
                    

    @property
    def rosmodel_Package2(self):
        return self.__rosmodel_Package2

    @rosmodel_Package2.setter
    def rosmodel_Package2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Package__rosmodel_Package2", None)
        self.__rosmodel_Package2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_Topic"):
                    opp_val = getattr(item, "rosmodel_Topic", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_Topic", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_Topic"):
                    opp_val = getattr(item, "rosmodel_Topic", None)
                    
                    setattr(item, "rosmodel_Topic", self)
                    

    @property
    def rosmodel_Package4(self):
        return self.__rosmodel_Package4

    @rosmodel_Package4.setter
    def rosmodel_Package4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Package__rosmodel_Package4", None)
        self.__rosmodel_Package4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_Message"):
                    opp_val = getattr(item, "rosmodel_Message", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_Message", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_Message"):
                    opp_val = getattr(item, "rosmodel_Message", None)
                    
                    setattr(item, "rosmodel_Message", self)
                    

    @property
    def rosmodel_Package6(self):
        return self.__rosmodel_Package6

    @rosmodel_Package6.setter
    def rosmodel_Package6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Package__rosmodel_Package6", None)
        self.__rosmodel_Package6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_ServiceType"):
                    opp_val = getattr(item, "rosmodel_ServiceType", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_ServiceType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_ServiceType"):
                    opp_val = getattr(item, "rosmodel_ServiceType", None)
                    
                    setattr(item, "rosmodel_ServiceType", self)
                    

    @property
    def rosmodel_Package8(self):
        return self.__rosmodel_Package8

    @rosmodel_Package8.setter
    def rosmodel_Package8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rosmodel_Package__rosmodel_Package8", None)
        self.__rosmodel_Package8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rosmodel_ActionMessage"):
                    opp_val = getattr(item, "rosmodel_ActionMessage", None)
                    
                    if opp_val == self:
                        setattr(item, "rosmodel_ActionMessage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rosmodel_ActionMessage"):
                    opp_val = getattr(item, "rosmodel_ActionMessage", None)
                    
                    setattr(item, "rosmodel_ActionMessage", self)
                    
