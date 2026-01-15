from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Operator(Enum):
    lesser = "lesser"
    leq = "leq"
    greater = "greater"
    geq = "geq"
    equal = "equal"
    neq = "neq"
class Protocol(Enum):
    ip = "ip"
    zwave = "zwave"
    zigbee = "zigbee"
    mqtt = "mqtt"
    dds = "dds"
class Unit(Enum):
    hour = "hour"
    min = "min"
    sec = "sec"
    milli = "milli"
class DefaultType(Enum):
    Void = "Void"
    Integer = "Integer"
    Real = "Real"
    String = "String"
    Boolean = "Boolean"


############################################
# Definition of Classes
############################################

class Value:

    pass
class iotdsl_IntConstant(Value):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class iotdsl_StringConstant(Value):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class iotdsl_BoolConstant(Value):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class iotdsl_Delay:

    def __init__(self, time: int, unit: str, iotdsl_Delay: "iotdsl_WithinExpression" = None):
        self.time = time
        self.unit = unit
        self.iotdsl_Delay = iotdsl_Delay
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def iotdsl_Delay(self):
        return self.__iotdsl_Delay

    @iotdsl_Delay.setter
    def iotdsl_Delay(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Delay__iotdsl_Delay", None)
        self.__iotdsl_Delay = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_WithinExpression"):
                opp_val = getattr(old_value, "iotdsl_WithinExpression", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_WithinExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_WithinExpression"):
                opp_val = getattr(value, "iotdsl_WithinExpression", None)
                setattr(value, "iotdsl_WithinExpression", self)

class iotdsl_Reaction:

    pass
class TimingExpression:

    pass
class iotdsl_AfterExpression(TimingExpression):

    pass
class iotdsl_WithinExpression(TimingExpression):

    pass
class iotdsl_Attribute:

    def __init__(self, name: str, iotdsl_Attribute: "iotdsl_EventOccurrence" = None, iotdsl_Attribute42: "iotdsl_Reaction" = None):
        self.name = name
        self.iotdsl_Attribute = iotdsl_Attribute
        self.iotdsl_Attribute42 = iotdsl_Attribute42
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iotdsl_Attribute(self):
        return self.__iotdsl_Attribute

    @iotdsl_Attribute.setter
    def iotdsl_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Attribute__iotdsl_Attribute", None)
        self.__iotdsl_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_EventOccurrence31"):
                opp_val = getattr(old_value, "iotdsl_EventOccurrence31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_EventOccurrence31"):
                opp_val = getattr(value, "iotdsl_EventOccurrence31", None)
                if opp_val is None:
                    setattr(value, "iotdsl_EventOccurrence31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iotdsl_Attribute42(self):
        return self.__iotdsl_Attribute42

    @iotdsl_Attribute42.setter
    def iotdsl_Attribute42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Attribute__iotdsl_Attribute42", None)
        self.__iotdsl_Attribute42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Reaction41"):
                opp_val = getattr(old_value, "iotdsl_Reaction41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Reaction41"):
                opp_val = getattr(value, "iotdsl_Reaction41", None)
                if opp_val is None:
                    setattr(value, "iotdsl_Reaction41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Expression:

    pass
class iotdsl_AndExpression(Expression):

    pass
class iotdsl_NotExpression(Expression):

    pass
class iotdsl_EventOccurrence(Expression):

    def __init__(self, operator: str, iotdsl_EventOccurrence: "iotdsl_NotExpression" = None, iotdsl_EventOccurrence26: "iotdsl_NodeInstance" = None, iotdsl_EventOccurrence29: "iotdsl_Sensing" = None, iotdsl_EventOccurrence31: set["iotdsl_Attribute"] = None, iotdsl_EventOccurrence33: "iotdsl_Value" = None):
        self.operator = operator
        self.iotdsl_EventOccurrence = iotdsl_EventOccurrence
        self.iotdsl_EventOccurrence26 = iotdsl_EventOccurrence26
        self.iotdsl_EventOccurrence29 = iotdsl_EventOccurrence29
        self.iotdsl_EventOccurrence31 = iotdsl_EventOccurrence31 if iotdsl_EventOccurrence31 is not None else set()
        self.iotdsl_EventOccurrence33 = iotdsl_EventOccurrence33
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def iotdsl_EventOccurrence29(self):
        return self.__iotdsl_EventOccurrence29

    @iotdsl_EventOccurrence29.setter
    def iotdsl_EventOccurrence29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_EventOccurrence__iotdsl_EventOccurrence29", None)
        self.__iotdsl_EventOccurrence29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Sensing"):
                opp_val = getattr(old_value, "iotdsl_Sensing", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_Sensing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Sensing"):
                opp_val = getattr(value, "iotdsl_Sensing", None)
                setattr(value, "iotdsl_Sensing", self)

    @property
    def iotdsl_EventOccurrence26(self):
        return self.__iotdsl_EventOccurrence26

    @iotdsl_EventOccurrence26.setter
    def iotdsl_EventOccurrence26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_EventOccurrence__iotdsl_EventOccurrence26", None)
        self.__iotdsl_EventOccurrence26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_NodeInstance27"):
                opp_val = getattr(old_value, "iotdsl_NodeInstance27", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_NodeInstance27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_NodeInstance27"):
                opp_val = getattr(value, "iotdsl_NodeInstance27", None)
                setattr(value, "iotdsl_NodeInstance27", self)

    @property
    def iotdsl_EventOccurrence33(self):
        return self.__iotdsl_EventOccurrence33

    @iotdsl_EventOccurrence33.setter
    def iotdsl_EventOccurrence33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_EventOccurrence__iotdsl_EventOccurrence33", None)
        self.__iotdsl_EventOccurrence33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Value34"):
                opp_val = getattr(old_value, "iotdsl_Value34", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_Value34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Value34"):
                opp_val = getattr(value, "iotdsl_Value34", None)
                setattr(value, "iotdsl_Value34", self)

    @property
    def iotdsl_EventOccurrence(self):
        return self.__iotdsl_EventOccurrence

    @iotdsl_EventOccurrence.setter
    def iotdsl_EventOccurrence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_EventOccurrence__iotdsl_EventOccurrence", None)
        self.__iotdsl_EventOccurrence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_NotExpression"):
                opp_val = getattr(old_value, "iotdsl_NotExpression", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_NotExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_NotExpression"):
                opp_val = getattr(value, "iotdsl_NotExpression", None)
                setattr(value, "iotdsl_NotExpression", self)

    @property
    def iotdsl_EventOccurrence31(self):
        return self.__iotdsl_EventOccurrence31

    @iotdsl_EventOccurrence31.setter
    def iotdsl_EventOccurrence31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_EventOccurrence__iotdsl_EventOccurrence31", None)
        self.__iotdsl_EventOccurrence31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iotdsl_Attribute"):
                    opp_val = getattr(item, "iotdsl_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "iotdsl_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iotdsl_Attribute"):
                    opp_val = getattr(item, "iotdsl_Attribute", None)
                    
                    setattr(item, "iotdsl_Attribute", self)
                    

class iotdsl_TimingExpression(Expression):

    pass
class iotdsl_Feature(ABC):

    def __init__(self, name: str, iotdsl_Feature: "iotdsl_Device" = None):
        self.name = name
        self.iotdsl_Feature = iotdsl_Feature
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iotdsl_Feature(self):
        return self.__iotdsl_Feature

    @iotdsl_Feature.setter
    def iotdsl_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Feature__iotdsl_Feature", None)
        self.__iotdsl_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Device"):
                opp_val = getattr(old_value, "iotdsl_Device", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Device"):
                opp_val = getattr(value, "iotdsl_Device", None)
                if opp_val is None:
                    setattr(value, "iotdsl_Device", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Node:

    pass
class iotdsl_Gateway(Node):

    pass
class iotdsl_Device(Node):

    pass
class iotdsl_Expression(ABC):

    pass
class iotdsl_CommunicationPath:

    def __init__(self, protocol: str, iotdsl_CommunicationPath: "iotdsl_Configuration" = None, iotdsl_CommunicationPath16: "iotdsl_NodeInstance" = None, iotdsl_CommunicationPath19: "iotdsl_NodeInstance" = None):
        self.protocol = protocol
        self.iotdsl_CommunicationPath = iotdsl_CommunicationPath
        self.iotdsl_CommunicationPath16 = iotdsl_CommunicationPath16
        self.iotdsl_CommunicationPath19 = iotdsl_CommunicationPath19
        
    @property
    def protocol(self) -> str:
        return self.__protocol

    @protocol.setter
    def protocol(self, protocol: str):
        self.__protocol = protocol

    @property
    def iotdsl_CommunicationPath16(self):
        return self.__iotdsl_CommunicationPath16

    @iotdsl_CommunicationPath16.setter
    def iotdsl_CommunicationPath16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_CommunicationPath__iotdsl_CommunicationPath16", None)
        self.__iotdsl_CommunicationPath16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_NodeInstance17"):
                opp_val = getattr(old_value, "iotdsl_NodeInstance17", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_NodeInstance17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_NodeInstance17"):
                opp_val = getattr(value, "iotdsl_NodeInstance17", None)
                setattr(value, "iotdsl_NodeInstance17", self)

    @property
    def iotdsl_CommunicationPath(self):
        return self.__iotdsl_CommunicationPath

    @iotdsl_CommunicationPath.setter
    def iotdsl_CommunicationPath(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_CommunicationPath__iotdsl_CommunicationPath", None)
        self.__iotdsl_CommunicationPath = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Configuration11"):
                opp_val = getattr(old_value, "iotdsl_Configuration11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Configuration11"):
                opp_val = getattr(value, "iotdsl_Configuration11", None)
                if opp_val is None:
                    setattr(value, "iotdsl_Configuration11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iotdsl_CommunicationPath19(self):
        return self.__iotdsl_CommunicationPath19

    @iotdsl_CommunicationPath19.setter
    def iotdsl_CommunicationPath19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_CommunicationPath__iotdsl_CommunicationPath19", None)
        self.__iotdsl_CommunicationPath19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_NodeInstance20"):
                opp_val = getattr(old_value, "iotdsl_NodeInstance20", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_NodeInstance20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_NodeInstance20"):
                opp_val = getattr(value, "iotdsl_NodeInstance20", None)
                setattr(value, "iotdsl_NodeInstance20", self)

class iotdsl_NodeInstance:

    def __init__(self, name: str, iotdsl_NodeInstance: "iotdsl_Configuration" = None, iotdsl_NodeInstance13: "iotdsl_Type" = None, iotdsl_NodeInstance17: "iotdsl_CommunicationPath" = None, iotdsl_NodeInstance20: "iotdsl_CommunicationPath" = None, iotdsl_NodeInstance27: "iotdsl_EventOccurrence" = None, iotdsl_NodeInstance37: "iotdsl_Reaction" = None):
        self.name = name
        self.iotdsl_NodeInstance = iotdsl_NodeInstance
        self.iotdsl_NodeInstance13 = iotdsl_NodeInstance13
        self.iotdsl_NodeInstance17 = iotdsl_NodeInstance17
        self.iotdsl_NodeInstance20 = iotdsl_NodeInstance20
        self.iotdsl_NodeInstance27 = iotdsl_NodeInstance27
        self.iotdsl_NodeInstance37 = iotdsl_NodeInstance37
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iotdsl_NodeInstance13(self):
        return self.__iotdsl_NodeInstance13

    @iotdsl_NodeInstance13.setter
    def iotdsl_NodeInstance13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_NodeInstance__iotdsl_NodeInstance13", None)
        self.__iotdsl_NodeInstance13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Type14"):
                opp_val = getattr(old_value, "iotdsl_Type14", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_Type14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Type14"):
                opp_val = getattr(value, "iotdsl_Type14", None)
                setattr(value, "iotdsl_Type14", self)

    @property
    def iotdsl_NodeInstance37(self):
        return self.__iotdsl_NodeInstance37

    @iotdsl_NodeInstance37.setter
    def iotdsl_NodeInstance37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_NodeInstance__iotdsl_NodeInstance37", None)
        self.__iotdsl_NodeInstance37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Reaction36"):
                opp_val = getattr(old_value, "iotdsl_Reaction36", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_Reaction36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Reaction36"):
                opp_val = getattr(value, "iotdsl_Reaction36", None)
                setattr(value, "iotdsl_Reaction36", self)

    @property
    def iotdsl_NodeInstance(self):
        return self.__iotdsl_NodeInstance

    @iotdsl_NodeInstance.setter
    def iotdsl_NodeInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_NodeInstance__iotdsl_NodeInstance", None)
        self.__iotdsl_NodeInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Configuration"):
                opp_val = getattr(old_value, "iotdsl_Configuration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Configuration"):
                opp_val = getattr(value, "iotdsl_Configuration", None)
                if opp_val is None:
                    setattr(value, "iotdsl_Configuration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iotdsl_NodeInstance20(self):
        return self.__iotdsl_NodeInstance20

    @iotdsl_NodeInstance20.setter
    def iotdsl_NodeInstance20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_NodeInstance__iotdsl_NodeInstance20", None)
        self.__iotdsl_NodeInstance20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_CommunicationPath19"):
                opp_val = getattr(old_value, "iotdsl_CommunicationPath19", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_CommunicationPath19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_CommunicationPath19"):
                opp_val = getattr(value, "iotdsl_CommunicationPath19", None)
                setattr(value, "iotdsl_CommunicationPath19", self)

    @property
    def iotdsl_NodeInstance27(self):
        return self.__iotdsl_NodeInstance27

    @iotdsl_NodeInstance27.setter
    def iotdsl_NodeInstance27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_NodeInstance__iotdsl_NodeInstance27", None)
        self.__iotdsl_NodeInstance27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_EventOccurrence26"):
                opp_val = getattr(old_value, "iotdsl_EventOccurrence26", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_EventOccurrence26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_EventOccurrence26"):
                opp_val = getattr(value, "iotdsl_EventOccurrence26", None)
                setattr(value, "iotdsl_EventOccurrence26", self)

    @property
    def iotdsl_NodeInstance17(self):
        return self.__iotdsl_NodeInstance17

    @iotdsl_NodeInstance17.setter
    def iotdsl_NodeInstance17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_NodeInstance__iotdsl_NodeInstance17", None)
        self.__iotdsl_NodeInstance17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_CommunicationPath16"):
                opp_val = getattr(old_value, "iotdsl_CommunicationPath16", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_CommunicationPath16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_CommunicationPath16"):
                opp_val = getattr(value, "iotdsl_CommunicationPath16", None)
                setattr(value, "iotdsl_CommunicationPath16", self)

class Capability:

    pass
class iotdsl_Sensing(Capability):

    pass
class iotdsl_Actuating(Capability):

    pass
class iotdsl_Parameter:

    def __init__(self, name: str, iotdsl_Parameter: "iotdsl_Capability" = None, iotdsl_Parameter8: "iotdsl_Type" = None):
        self.name = name
        self.iotdsl_Parameter = iotdsl_Parameter
        self.iotdsl_Parameter8 = iotdsl_Parameter8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iotdsl_Parameter(self):
        return self.__iotdsl_Parameter

    @iotdsl_Parameter.setter
    def iotdsl_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Parameter__iotdsl_Parameter", None)
        self.__iotdsl_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Capability"):
                opp_val = getattr(old_value, "iotdsl_Capability", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Capability"):
                opp_val = getattr(value, "iotdsl_Capability", None)
                if opp_val is None:
                    setattr(value, "iotdsl_Capability", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iotdsl_Parameter8(self):
        return self.__iotdsl_Parameter8

    @iotdsl_Parameter8.setter
    def iotdsl_Parameter8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Parameter__iotdsl_Parameter8", None)
        self.__iotdsl_Parameter8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Type"):
                opp_val = getattr(old_value, "iotdsl_Type", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Type"):
                opp_val = getattr(value, "iotdsl_Type", None)
                setattr(value, "iotdsl_Type", self)

class iotdsl_Value:

    pass
class Feature:

    pass
class iotdsl_Capability(Feature):

    pass
class iotdsl_Property(Feature):

    pass
class iotdsl_EnumLiteral:

    def __init__(self, name: str, iotdsl_EnumLiteral: "iotdsl_Enumeration" = None):
        self.name = name
        self.iotdsl_EnumLiteral = iotdsl_EnumLiteral
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iotdsl_EnumLiteral(self):
        return self.__iotdsl_EnumLiteral

    @iotdsl_EnumLiteral.setter
    def iotdsl_EnumLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_EnumLiteral__iotdsl_EnumLiteral", None)
        self.__iotdsl_EnumLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Enumeration"):
                opp_val = getattr(old_value, "iotdsl_Enumeration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Enumeration"):
                opp_val = getattr(value, "iotdsl_Enumeration", None)
                if opp_val is None:
                    setattr(value, "iotdsl_Enumeration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DeclaredType:

    pass
class iotdsl_Node(DeclaredType):

    pass
class iotdsl_Enumeration(DeclaredType):

    pass
class Type:

    pass
class iotdsl_DeclaredType(Type):

    pass
class iotdsl_PrimitiveType(Type):

    pass
class Content:

    pass
class iotdsl_Configuration(Content):

    def __init__(self, confname: str, iotdsl_Configuration: set["iotdsl_NodeInstance"] = None, iotdsl_Configuration11: set["iotdsl_CommunicationPath"] = None):
        self.confname = confname
        self.iotdsl_Configuration = iotdsl_Configuration if iotdsl_Configuration is not None else set()
        self.iotdsl_Configuration11 = iotdsl_Configuration11 if iotdsl_Configuration11 is not None else set()
        
    @property
    def confname(self) -> str:
        return self.__confname

    @confname.setter
    def confname(self, confname: str):
        self.__confname = confname

    @property
    def iotdsl_Configuration11(self):
        return self.__iotdsl_Configuration11

    @iotdsl_Configuration11.setter
    def iotdsl_Configuration11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Configuration__iotdsl_Configuration11", None)
        self.__iotdsl_Configuration11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iotdsl_CommunicationPath"):
                    opp_val = getattr(item, "iotdsl_CommunicationPath", None)
                    
                    if opp_val == self:
                        setattr(item, "iotdsl_CommunicationPath", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iotdsl_CommunicationPath"):
                    opp_val = getattr(item, "iotdsl_CommunicationPath", None)
                    
                    setattr(item, "iotdsl_CommunicationPath", self)
                    

    @property
    def iotdsl_Configuration(self):
        return self.__iotdsl_Configuration

    @iotdsl_Configuration.setter
    def iotdsl_Configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Configuration__iotdsl_Configuration", None)
        self.__iotdsl_Configuration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iotdsl_NodeInstance"):
                    opp_val = getattr(item, "iotdsl_NodeInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "iotdsl_NodeInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iotdsl_NodeInstance"):
                    opp_val = getattr(item, "iotdsl_NodeInstance", None)
                    
                    setattr(item, "iotdsl_NodeInstance", self)
                    

class iotdsl_Rule(Content):

    def __init__(self, name: str, iotdsl_Rule: "iotdsl_Expression" = None, iotdsl_Rule23: set["iotdsl_Reaction"] = None):
        self.name = name
        self.iotdsl_Rule = iotdsl_Rule
        self.iotdsl_Rule23 = iotdsl_Rule23 if iotdsl_Rule23 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iotdsl_Rule(self):
        return self.__iotdsl_Rule

    @iotdsl_Rule.setter
    def iotdsl_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Rule__iotdsl_Rule", None)
        self.__iotdsl_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Expression"):
                opp_val = getattr(old_value, "iotdsl_Expression", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Expression"):
                opp_val = getattr(value, "iotdsl_Expression", None)
                setattr(value, "iotdsl_Expression", self)

    @property
    def iotdsl_Rule23(self):
        return self.__iotdsl_Rule23

    @iotdsl_Rule23.setter
    def iotdsl_Rule23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Rule__iotdsl_Rule23", None)
        self.__iotdsl_Rule23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iotdsl_Reaction"):
                    opp_val = getattr(item, "iotdsl_Reaction", None)
                    
                    if opp_val == self:
                        setattr(item, "iotdsl_Reaction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iotdsl_Reaction"):
                    opp_val = getattr(item, "iotdsl_Reaction", None)
                    
                    setattr(item, "iotdsl_Reaction", self)
                    

class iotdsl_Type(Content):

    def __init__(self, name: str, iotdsl_Type: "iotdsl_Parameter" = None, iotdsl_Type14: "iotdsl_NodeInstance" = None):
        self.name = name
        self.iotdsl_Type = iotdsl_Type
        self.iotdsl_Type14 = iotdsl_Type14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iotdsl_Type14(self):
        return self.__iotdsl_Type14

    @iotdsl_Type14.setter
    def iotdsl_Type14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Type__iotdsl_Type14", None)
        self.__iotdsl_Type14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_NodeInstance13"):
                opp_val = getattr(old_value, "iotdsl_NodeInstance13", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_NodeInstance13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_NodeInstance13"):
                opp_val = getattr(value, "iotdsl_NodeInstance13", None)
                setattr(value, "iotdsl_NodeInstance13", self)

    @property
    def iotdsl_Type(self):
        return self.__iotdsl_Type

    @iotdsl_Type.setter
    def iotdsl_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Type__iotdsl_Type", None)
        self.__iotdsl_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Parameter8"):
                opp_val = getattr(old_value, "iotdsl_Parameter8", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_Parameter8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Parameter8"):
                opp_val = getattr(value, "iotdsl_Parameter8", None)
                setattr(value, "iotdsl_Parameter8", self)

class iotdsl_Content(ABC):

    pass
class iotdsl_Import:

    def __init__(self, importedNamespace: str, iotdsl_Import: "iotdsl_IotModel" = None):
        self.importedNamespace = importedNamespace
        self.iotdsl_Import = iotdsl_Import
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def iotdsl_Import(self):
        return self.__iotdsl_Import

    @iotdsl_Import.setter
    def iotdsl_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Import__iotdsl_Import", None)
        self.__iotdsl_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_IotModel"):
                opp_val = getattr(old_value, "iotdsl_IotModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_IotModel"):
                opp_val = getattr(value, "iotdsl_IotModel", None)
                if opp_val is None:
                    setattr(value, "iotdsl_IotModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iotdsl_IotModel:

    def __init__(self, name: str, iotdsl_IotModel: set["iotdsl_Import"] = None, iotdsl_IotModel2: set["iotdsl_Content"] = None):
        self.name = name
        self.iotdsl_IotModel = iotdsl_IotModel if iotdsl_IotModel is not None else set()
        self.iotdsl_IotModel2 = iotdsl_IotModel2 if iotdsl_IotModel2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iotdsl_IotModel(self):
        return self.__iotdsl_IotModel

    @iotdsl_IotModel.setter
    def iotdsl_IotModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_IotModel__iotdsl_IotModel", None)
        self.__iotdsl_IotModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iotdsl_Import"):
                    opp_val = getattr(item, "iotdsl_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "iotdsl_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iotdsl_Import"):
                    opp_val = getattr(item, "iotdsl_Import", None)
                    
                    setattr(item, "iotdsl_Import", self)
                    

    @property
    def iotdsl_IotModel2(self):
        return self.__iotdsl_IotModel2

    @iotdsl_IotModel2.setter
    def iotdsl_IotModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_IotModel__iotdsl_IotModel2", None)
        self.__iotdsl_IotModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iotdsl_Content"):
                    opp_val = getattr(item, "iotdsl_Content", None)
                    
                    if opp_val == self:
                        setattr(item, "iotdsl_Content", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iotdsl_Content"):
                    opp_val = getattr(item, "iotdsl_Content", None)
                    
                    setattr(item, "iotdsl_Content", self)
                    
