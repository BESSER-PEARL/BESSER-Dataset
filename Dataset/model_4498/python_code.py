from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CompOps(Enum):
    GREATER = "GREATER"
    GREATEROREQUAL = "GREATEROREQUAL"
    EQUAL = "EQUAL"
    LESSOREQUAL = "LESSOREQUAL"
    LESS = "LESS"
    NOTEQUAL = "NOTEQUAL"
class Weekdays(Enum):
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


############################################
# Definition of Classes
############################################

class Expression:

    pass
class PolicyEngine_Constant(Expression):

    pass
class PolicyEngine_RoomUsage(Expression):

    pass
class PolicyEngine_ResetExpression(Expression):

    pass
class PolicyEngine_TimeExpression(Expression):

    def __init__(self, TimeBound: int, PolicyEngine_TimeExpression: "PolicyEngine_Timer" = None):
        self.TimeBound = TimeBound
        self.PolicyEngine_TimeExpression = PolicyEngine_TimeExpression
        
    @property
    def TimeBound(self) -> int:
        return self.__TimeBound

    @TimeBound.setter
    def TimeBound(self, TimeBound: int):
        self.__TimeBound = TimeBound

    @property
    def PolicyEngine_TimeExpression(self):
        return self.__PolicyEngine_TimeExpression

    @PolicyEngine_TimeExpression.setter
    def PolicyEngine_TimeExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PolicyEngine_TimeExpression__PolicyEngine_TimeExpression", None)
        self.__PolicyEngine_TimeExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PolicyEngine_Timer103"):
                opp_val = getattr(old_value, "PolicyEngine_Timer103", None)
                if opp_val == self:
                    setattr(old_value, "PolicyEngine_Timer103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PolicyEngine_Timer103"):
                opp_val = getattr(value, "PolicyEngine_Timer103", None)
                setattr(value, "PolicyEngine_Timer103", self)

class PolicyEngine_RoomActuators(Expression):

    pass
class PolicyEngine_UnaryOp(Expression):

    def __init__(self, operator: str, PolicyEngine_UnaryOp: "PolicyEngine_Expression" = None):
        self.operator = operator
        self.PolicyEngine_UnaryOp = PolicyEngine_UnaryOp
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def PolicyEngine_UnaryOp(self):
        return self.__PolicyEngine_UnaryOp

    @PolicyEngine_UnaryOp.setter
    def PolicyEngine_UnaryOp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PolicyEngine_UnaryOp__PolicyEngine_UnaryOp", None)
        self.__PolicyEngine_UnaryOp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PolicyEngine_Expression120"):
                opp_val = getattr(old_value, "PolicyEngine_Expression120", None)
                if opp_val == self:
                    setattr(old_value, "PolicyEngine_Expression120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PolicyEngine_Expression120"):
                opp_val = getattr(value, "PolicyEngine_Expression120", None)
                setattr(value, "PolicyEngine_Expression120", self)

class PolicyEngine_BinaryOps(Expression):

    def __init__(self, operator: str, PolicyEngine_BinaryOps: "PolicyEngine_Expression" = None, PolicyEngine_BinaryOps117: "PolicyEngine_Expression" = None):
        self.operator = operator
        self.PolicyEngine_BinaryOps = PolicyEngine_BinaryOps
        self.PolicyEngine_BinaryOps117 = PolicyEngine_BinaryOps117
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def PolicyEngine_BinaryOps(self):
        return self.__PolicyEngine_BinaryOps

    @PolicyEngine_BinaryOps.setter
    def PolicyEngine_BinaryOps(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PolicyEngine_BinaryOps__PolicyEngine_BinaryOps", None)
        self.__PolicyEngine_BinaryOps = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PolicyEngine_Expression115"):
                opp_val = getattr(old_value, "PolicyEngine_Expression115", None)
                if opp_val == self:
                    setattr(old_value, "PolicyEngine_Expression115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PolicyEngine_Expression115"):
                opp_val = getattr(value, "PolicyEngine_Expression115", None)
                setattr(value, "PolicyEngine_Expression115", self)

    @property
    def PolicyEngine_BinaryOps117(self):
        return self.__PolicyEngine_BinaryOps117

    @PolicyEngine_BinaryOps117.setter
    def PolicyEngine_BinaryOps117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PolicyEngine_BinaryOps__PolicyEngine_BinaryOps117", None)
        self.__PolicyEngine_BinaryOps117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PolicyEngine_Expression118"):
                opp_val = getattr(old_value, "PolicyEngine_Expression118", None)
                if opp_val == self:
                    setattr(old_value, "PolicyEngine_Expression118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PolicyEngine_Expression118"):
                opp_val = getattr(value, "PolicyEngine_Expression118", None)
                setattr(value, "PolicyEngine_Expression118", self)

class PolicyEngine_If:

    pass
class PolicyEngine_Time:

    def __init__(self, hours: str, minutes: str, PolicyEngine_Time: "PolicyEngine_Schedule" = None, PolicyEngine_Time89: "PolicyEngine_Schedule" = None):
        self.hours = hours
        self.minutes = minutes
        self.PolicyEngine_Time = PolicyEngine_Time
        self.PolicyEngine_Time89 = PolicyEngine_Time89
        
    @property
    def minutes(self) -> str:
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes: str):
        self.__minutes = minutes

    @property
    def hours(self) -> str:
        return self.__hours

    @hours.setter
    def hours(self, hours: str):
        self.__hours = hours

    @property
    def PolicyEngine_Time(self):
        return self.__PolicyEngine_Time

    @PolicyEngine_Time.setter
    def PolicyEngine_Time(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PolicyEngine_Time__PolicyEngine_Time", None)
        self.__PolicyEngine_Time = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PolicyEngine_Schedule86"):
                opp_val = getattr(old_value, "PolicyEngine_Schedule86", None)
                if opp_val == self:
                    setattr(old_value, "PolicyEngine_Schedule86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PolicyEngine_Schedule86"):
                opp_val = getattr(value, "PolicyEngine_Schedule86", None)
                setattr(value, "PolicyEngine_Schedule86", self)

    @property
    def PolicyEngine_Time89(self):
        return self.__PolicyEngine_Time89

    @PolicyEngine_Time89.setter
    def PolicyEngine_Time89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PolicyEngine_Time__PolicyEngine_Time89", None)
        self.__PolicyEngine_Time89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PolicyEngine_Schedule88"):
                opp_val = getattr(old_value, "PolicyEngine_Schedule88", None)
                if opp_val == self:
                    setattr(old_value, "PolicyEngine_Schedule88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PolicyEngine_Schedule88"):
                opp_val = getattr(value, "PolicyEngine_Schedule88", None)
                setattr(value, "PolicyEngine_Schedule88", self)

class PolicyEngine_Expression(ABC):

    pass
class PolicyEngine_HasActuators:

    pass
class PolicyEngine_HasSensors:

    pass
class PolicyEngine_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class HasActuators:

    pass
class PolicyEngine_HasIntegerValue:

    def __init__(self, valueState: int):
        self.valueState = valueState
        
    @property
    def valueState(self) -> int:
        return self.__valueState

    @valueState.setter
    def valueState(self, valueState: int):
        self.__valueState = valueState

class Sensor:

    pass
class PolicyEngine_TouchSensor(Sensor):

    pass
class PolicyEngine_CO2Sensor(Sensor):

    pass
class PolicyEngine_PressureSensor(Sensor):

    pass
class PolicyEngine_LightSensor(Sensor):

    pass
class PolicyEngine_InfraredLightSensor(Sensor):

    pass
class PolicyEngine_HumiditySensor(Sensor):

    pass
class PolicyEngine_SmokeSensor(Sensor):

    pass
class PolicyEngine_TemperatureSensor(Sensor):

    pass
class PolicyEngine_MotionSensor(Sensor):

    pass
class HasSensors:

    pass
class HasIntegerValue:

    pass
class PolicyEngine_Actuator(HasIntegerValue):

    pass
class PolicyEngine_Sensor(HasIntegerValue):

    pass
class Actuator:

    pass
class PolicyEngine_AudioAlarmActuator(Actuator):

    pass
class PolicyEngine_HumidifierActuator(Actuator):

    pass
class PolicyEngine_DoorActuator(Actuator):

    pass
class PolicyEngine_RadiatorActuator(Actuator):

    pass
class PolicyEngine_WindowActuator(Actuator):

    pass
class PolicyEngine_LightSwitchActuator(Actuator):

    pass
class PolicyEngine_MeetingScheduleSystem:

    pass
class PolicyEngine_CalendarSystem:

    pass
class PolicyEngine_AccessControl:

    pass
class PolicyEngine_CTS:

    pass
class NamedElement:

    pass
class PolicyEngine_SensorComponent(NamedElement, HasSensors):

    pass
class PolicyEngine_ActuatorComponent(NamedElement, HasActuators):

    pass
class PolicyEngine_State(NamedElement):

    def __init__(self, valueState: bool, PolicyEngine_State: "PolicyEngine_Model" = None, PolicyEngine_State84: "PolicyEngine_Expression" = None, PolicyEngine_State73: "PolicyEngine_Policy" = None, PolicyEngine_State82: "PolicyEngine_Policy" = None, PolicyEngine_State113: "PolicyEngine_RoomUsage" = None):
        self.valueState = valueState
        self.PolicyEngine_State = PolicyEngine_State
        self.PolicyEngine_State84 = PolicyEngine_State84
        self.PolicyEngine_State73 = PolicyEngine_State73
        self.PolicyEngine_State82 = PolicyEngine_State82
        self.PolicyEngine_State113 = PolicyEngine_State113
        
    @property
    def valueState(self) -> bool:
        return self.__valueState

    @valueState.setter
    def valueState(self, valueState: bool):
        self.__valueState = valueState

    @property
    def PolicyEngine_State113(self):
        return self.__PolicyEngine_State113

    @PolicyEngine_State113.setter
    def PolicyEngine_State113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PolicyEngine_State__PolicyEngine_State113", None)
        self.__PolicyEngine_State113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PolicyEngine_RoomUsage112"):
                opp_val = getattr(old_value, "PolicyEngine_RoomUsage112", None)
                if opp_val == self:
                    setattr(old_value, "PolicyEngine_RoomUsage112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PolicyEngine_RoomUsage112"):
                opp_val = getattr(value, "PolicyEngine_RoomUsage112", None)
                setattr(value, "PolicyEngine_RoomUsage112", self)

    @property
    def PolicyEngine_State(self):
        return self.__PolicyEngine_State

    @PolicyEngine_State.setter
    def PolicyEngine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PolicyEngine_State__PolicyEngine_State", None)
        self.__PolicyEngine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PolicyEngine_Model18"):
                opp_val = getattr(old_value, "PolicyEngine_Model18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PolicyEngine_Model18"):
                opp_val = getattr(value, "PolicyEngine_Model18", None)
                if opp_val is None:
                    setattr(value, "PolicyEngine_Model18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PolicyEngine_State73(self):
        return self.__PolicyEngine_State73

    @PolicyEngine_State73.setter
    def PolicyEngine_State73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PolicyEngine_State__PolicyEngine_State73", None)
        self.__PolicyEngine_State73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PolicyEngine_Policy72"):
                opp_val = getattr(old_value, "PolicyEngine_Policy72", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PolicyEngine_Policy72"):
                opp_val = getattr(value, "PolicyEngine_Policy72", None)
                if opp_val is None:
                    setattr(value, "PolicyEngine_Policy72", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PolicyEngine_State82(self):
        return self.__PolicyEngine_State82

    @PolicyEngine_State82.setter
    def PolicyEngine_State82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PolicyEngine_State__PolicyEngine_State82", None)
        self.__PolicyEngine_State82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PolicyEngine_Policy81"):
                opp_val = getattr(old_value, "PolicyEngine_Policy81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PolicyEngine_Policy81"):
                opp_val = getattr(value, "PolicyEngine_Policy81", None)
                if opp_val is None:
                    setattr(value, "PolicyEngine_Policy81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PolicyEngine_State84(self):
        return self.__PolicyEngine_State84

    @PolicyEngine_State84.setter
    def PolicyEngine_State84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PolicyEngine_State__PolicyEngine_State84", None)
        self.__PolicyEngine_State84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PolicyEngine_Expression"):
                opp_val = getattr(old_value, "PolicyEngine_Expression", None)
                if opp_val == self:
                    setattr(old_value, "PolicyEngine_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PolicyEngine_Expression"):
                opp_val = getattr(value, "PolicyEngine_Expression", None)
                setattr(value, "PolicyEngine_Expression", self)

class PolicyEngine_Timer(NamedElement):

    pass
class PolicyEngine_Id(Expression, NamedElement):

    pass
class PolicyEngine_Policy(NamedElement):

    pass
class PolicyEngine_Floor(NamedElement):

    pass
class PolicyEngine_Schedule(NamedElement):

    def __init__(self, weekdays: str, PolicyEngine_Schedule: "PolicyEngine_Model" = None, PolicyEngine_Schedule53: "PolicyEngine_Room" = None, PolicyEngine_Schedule86: "PolicyEngine_Time" = None, PolicyEngine_Schedule88: "PolicyEngine_Time" = None, PolicyEngine_Schedule76: "PolicyEngine_Policy" = None):
        self.weekdays = weekdays
        self.PolicyEngine_Schedule = PolicyEngine_Schedule
        self.PolicyEngine_Schedule53 = PolicyEngine_Schedule53
        self.PolicyEngine_Schedule86 = PolicyEngine_Schedule86
        self.PolicyEngine_Schedule88 = PolicyEngine_Schedule88
        self.PolicyEngine_Schedule76 = PolicyEngine_Schedule76
        
    @property
    def weekdays(self) -> str:
        return self.__weekdays

    @weekdays.setter
    def weekdays(self, weekdays: str):
        self.__weekdays = weekdays

    @property
    def PolicyEngine_Schedule86(self):
        return self.__PolicyEngine_Schedule86

    @PolicyEngine_Schedule86.setter
    def PolicyEngine_Schedule86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PolicyEngine_Schedule__PolicyEngine_Schedule86", None)
        self.__PolicyEngine_Schedule86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PolicyEngine_Time"):
                opp_val = getattr(old_value, "PolicyEngine_Time", None)
                if opp_val == self:
                    setattr(old_value, "PolicyEngine_Time", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PolicyEngine_Time"):
                opp_val = getattr(value, "PolicyEngine_Time", None)
                setattr(value, "PolicyEngine_Time", self)

    @property
    def PolicyEngine_Schedule88(self):
        return self.__PolicyEngine_Schedule88

    @PolicyEngine_Schedule88.setter
    def PolicyEngine_Schedule88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PolicyEngine_Schedule__PolicyEngine_Schedule88", None)
        self.__PolicyEngine_Schedule88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PolicyEngine_Time89"):
                opp_val = getattr(old_value, "PolicyEngine_Time89", None)
                if opp_val == self:
                    setattr(old_value, "PolicyEngine_Time89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PolicyEngine_Time89"):
                opp_val = getattr(value, "PolicyEngine_Time89", None)
                setattr(value, "PolicyEngine_Time89", self)

    @property
    def PolicyEngine_Schedule53(self):
        return self.__PolicyEngine_Schedule53

    @PolicyEngine_Schedule53.setter
    def PolicyEngine_Schedule53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PolicyEngine_Schedule__PolicyEngine_Schedule53", None)
        self.__PolicyEngine_Schedule53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PolicyEngine_Room52"):
                opp_val = getattr(old_value, "PolicyEngine_Room52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PolicyEngine_Room52"):
                opp_val = getattr(value, "PolicyEngine_Room52", None)
                if opp_val is None:
                    setattr(value, "PolicyEngine_Room52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PolicyEngine_Schedule(self):
        return self.__PolicyEngine_Schedule

    @PolicyEngine_Schedule.setter
    def PolicyEngine_Schedule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PolicyEngine_Schedule__PolicyEngine_Schedule", None)
        self.__PolicyEngine_Schedule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PolicyEngine_Model23"):
                opp_val = getattr(old_value, "PolicyEngine_Model23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PolicyEngine_Model23"):
                opp_val = getattr(value, "PolicyEngine_Model23", None)
                if opp_val is None:
                    setattr(value, "PolicyEngine_Model23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PolicyEngine_Schedule76(self):
        return self.__PolicyEngine_Schedule76

    @PolicyEngine_Schedule76.setter
    def PolicyEngine_Schedule76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PolicyEngine_Schedule__PolicyEngine_Schedule76", None)
        self.__PolicyEngine_Schedule76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PolicyEngine_Policy75"):
                opp_val = getattr(old_value, "PolicyEngine_Policy75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PolicyEngine_Policy75"):
                opp_val = getattr(value, "PolicyEngine_Policy75", None)
                if opp_val is None:
                    setattr(value, "PolicyEngine_Policy75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PolicyEngine_Room(NamedElement):

    pass
class PolicyEngine_Model(NamedElement):

    pass
class PolicyEngine_Building(NamedElement):

    pass