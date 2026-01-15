from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ardurobotml_Region:

    def __init__(self, name: str, ardurobotml_Region45: "ardurobotml_RegionContainer" = None, ardurobotml_Region: set["ardurobotml_State"] = None):
        self.name = name
        self.ardurobotml_Region45 = ardurobotml_Region45
        self.ardurobotml_Region = ardurobotml_Region if ardurobotml_Region is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ardurobotml_Region45(self):
        return self.__ardurobotml_Region45

    @ardurobotml_Region45.setter
    def ardurobotml_Region45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_Region__ardurobotml_Region45", None)
        self.__ardurobotml_Region45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardurobotml_RegionContainer"):
                opp_val = getattr(old_value, "ardurobotml_RegionContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardurobotml_RegionContainer"):
                opp_val = getattr(value, "ardurobotml_RegionContainer", None)
                if opp_val is None:
                    setattr(value, "ardurobotml_RegionContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ardurobotml_Region(self):
        return self.__ardurobotml_Region

    @ardurobotml_Region.setter
    def ardurobotml_Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_Region__ardurobotml_Region", None)
        self.__ardurobotml_Region = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ardurobotml_State43"):
                    opp_val = getattr(item, "ardurobotml_State43", None)
                    
                    if opp_val == self:
                        setattr(item, "ardurobotml_State43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ardurobotml_State43"):
                    opp_val = getattr(item, "ardurobotml_State43", None)
                    
                    setattr(item, "ardurobotml_State43", self)
                    

class ardurobotml_Condition(ABC):

    pass
class Action:

    pass
class ardurobotml_StopAction(Action):

    pass
class ardurobotml_TurningRightAction(Action):

    def __init__(self, duration: int, startTick: int, speed: int):
        self.duration = duration
        self.startTick = startTick
        self.speed = speed
        
    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def startTick(self) -> int:
        return self.__startTick

    @startTick.setter
    def startTick(self, startTick: int):
        self.__startTick = startTick

class ardurobotml_MoveBackardAction(Action):

    def __init__(self, duration: int, startTick: int, speed: int):
        self.duration = duration
        self.startTick = startTick
        self.speed = speed
        
    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def startTick(self) -> int:
        return self.__startTick

    @startTick.setter
    def startTick(self, startTick: int):
        self.__startTick = startTick

class ardurobotml_MoveForwardAndTurningLeftAction(Action):

    def __init__(self, duration: int, startTick: int, diff: int, speed: int):
        self.duration = duration
        self.startTick = startTick
        self.diff = diff
        self.speed = speed
        
    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed

    @property
    def startTick(self) -> int:
        return self.__startTick

    @startTick.setter
    def startTick(self, startTick: int):
        self.__startTick = startTick

    @property
    def diff(self) -> int:
        return self.__diff

    @diff.setter
    def diff(self, diff: int):
        self.__diff = diff

class ardurobotml_MoveBackardAndTurningLeftAction(Action):

    def __init__(self, duration: int, startTick: int, diff: int, speed: int):
        self.duration = duration
        self.startTick = startTick
        self.diff = diff
        self.speed = speed
        
    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed

    @property
    def startTick(self) -> int:
        return self.__startTick

    @startTick.setter
    def startTick(self, startTick: int):
        self.__startTick = startTick

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def diff(self) -> int:
        return self.__diff

    @diff.setter
    def diff(self, diff: int):
        self.__diff = diff

class ardurobotml_MoveForwardAndTurningRightAction(Action):

    def __init__(self, startTick: int, diff: int, speed: int, duration: int):
        self.startTick = startTick
        self.diff = diff
        self.speed = speed
        self.duration = duration
        
    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def startTick(self) -> int:
        return self.__startTick

    @startTick.setter
    def startTick(self, startTick: int):
        self.__startTick = startTick

    @property
    def diff(self) -> int:
        return self.__diff

    @diff.setter
    def diff(self, diff: int):
        self.__diff = diff

class ardurobotml_SCANCollisionAction(Action):

    pass
class ardurobotml_EmergencyStopAction(Action):

    def __init__(self):
        
    def begin(self):
        # TODO: Implement begin method
        pass

class ardurobotml_AcceleratetAction(Action):

    def __init__(self, ratio: int, startTick: int):
        self.ratio = ratio
        self.startTick = startTick
        
    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def startTick(self) -> int:
        return self.__startTick

    @startTick.setter
    def startTick(self, startTick: int):
        self.__startTick = startTick

class ardurobotml_TurningLeftAction(Action):

    def __init__(self, duration: int, startTick: int, speed: int):
        self.duration = duration
        self.startTick = startTick
        self.speed = speed
        
    @property
    def startTick(self) -> int:
        return self.__startTick

    @startTick.setter
    def startTick(self, startTick: int):
        self.__startTick = startTick

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

class ardurobotml_MoveForwardAction(Action):

    def __init__(self, duration: int, startTick: int, speed: int):
        self.duration = duration
        self.startTick = startTick
        self.speed = speed
        
    @property
    def startTick(self) -> int:
        return self.__startTick

    @startTick.setter
    def startTick(self, startTick: int):
        self.__startTick = startTick

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

class ardurobotml_MoveBackardAndTurningRightAction(Action):

    def __init__(self, duration: int, startTick: int, diff: int, speed: int):
        self.duration = duration
        self.startTick = startTick
        self.diff = diff
        self.speed = speed
        
    @property
    def diff(self) -> int:
        return self.__diff

    @diff.setter
    def diff(self, diff: int):
        self.__diff = diff

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def startTick(self) -> int:
        return self.__startTick

    @startTick.setter
    def startTick(self, startTick: int):
        self.__startTick = startTick

class ardurobotml_DeceleratetAction(Action):

    def __init__(self, ratio: int, startTick: int):
        self.ratio = ratio
        self.startTick = startTick
        
    @property
    def startTick(self) -> int:
        return self.__startTick

    @startTick.setter
    def startTick(self, startTick: int):
        self.__startTick = startTick

    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

class ardurobotml_ActionSequence(Action):

    pass
class Condition:

    pass
class ardurobotml_CollisionSensorCondition(Condition):

    pass
class ardurobotml_SystemPropertyCondition(Condition):

    def __init__(self, expectedAttributeValue: bool):
        self.expectedAttributeValue = expectedAttributeValue
        
    @property
    def expectedAttributeValue(self) -> bool:
        return self.__expectedAttributeValue

    @expectedAttributeValue.setter
    def expectedAttributeValue(self, expectedAttributeValue: bool):
        self.__expectedAttributeValue = expectedAttributeValue

class ardurobotml_AllActionFinishedCondition(Condition):

    pass
class Guard:

    pass
class ardurobotml_EventGuard(Guard):

    pass
class ardurobotml_EvaluateGuard(Guard):

    pass
class ardurobotml_TemporalGuard(Guard):

    def __init__(self, afterDuration: int, ardurobotml_TemporalGuard: "ardurobotml_FSMClock" = None):
        self.afterDuration = afterDuration
        self.ardurobotml_TemporalGuard = ardurobotml_TemporalGuard
        
    @property
    def afterDuration(self) -> int:
        return self.__afterDuration

    @afterDuration.setter
    def afterDuration(self, afterDuration: int):
        self.__afterDuration = afterDuration

    @property
    def ardurobotml_TemporalGuard(self):
        return self.__ardurobotml_TemporalGuard

    @ardurobotml_TemporalGuard.setter
    def ardurobotml_TemporalGuard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_TemporalGuard__ardurobotml_TemporalGuard", None)
        self.__ardurobotml_TemporalGuard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardurobotml_FSMClock35"):
                opp_val = getattr(old_value, "ardurobotml_FSMClock35", None)
                if opp_val == self:
                    setattr(old_value, "ardurobotml_FSMClock35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardurobotml_FSMClock35"):
                opp_val = getattr(value, "ardurobotml_FSMClock35", None)
                setattr(value, "ardurobotml_FSMClock35", self)

class ardurobotml_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class ardurobotml_Transition(NamedElement):

    def __init__(self, outgoingTransitions: "ardurobotml_State" = None, incomingTransitions: "ardurobotml_State" = None, ardurobotml_Transition30: "ardurobotml_Guard" = None, ardurobotml_Transition32: set["ardurobotml_FSMEvent"] = None, ardurobotml_Transition: "ardurobotml_TFSM" = None, Transition: "ardurobotml_State" = None, Transition21: "ardurobotml_State" = None, ardurobotml_Transition40: "ardurobotml_FSMEvent" = None):
        self.outgoingTransitions = outgoingTransitions
        self.incomingTransitions = incomingTransitions
        self.ardurobotml_Transition30 = ardurobotml_Transition30
        self.ardurobotml_Transition32 = ardurobotml_Transition32 if ardurobotml_Transition32 is not None else set()
        self.ardurobotml_Transition = ardurobotml_Transition
        self.Transition = Transition
        self.Transition21 = Transition21
        self.ardurobotml_Transition40 = ardurobotml_Transition40
        
    @property
    def ardurobotml_Transition32(self):
        return self.__ardurobotml_Transition32

    @ardurobotml_Transition32.setter
    def ardurobotml_Transition32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_Transition__ardurobotml_Transition32", None)
        self.__ardurobotml_Transition32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ardurobotml_FSMEvent33"):
                    opp_val = getattr(item, "ardurobotml_FSMEvent33", None)
                    
                    if opp_val == self:
                        setattr(item, "ardurobotml_FSMEvent33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ardurobotml_FSMEvent33"):
                    opp_val = getattr(item, "ardurobotml_FSMEvent33", None)
                    
                    setattr(item, "ardurobotml_FSMEvent33", self)
                    

    @property
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_Transition__incomingTransitions", None)
        self.__incomingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State28"):
                opp_val = getattr(old_value, "State28", None)
                if opp_val == self:
                    setattr(old_value, "State28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State28"):
                opp_val = getattr(value, "State28", None)
                setattr(value, "State28", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_Transition__outgoingTransitions", None)
        self.__outgoingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State26"):
                opp_val = getattr(old_value, "State26", None)
                if opp_val == self:
                    setattr(old_value, "State26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State26"):
                opp_val = getattr(value, "State26", None)
                setattr(value, "State26", self)

    @property
    def ardurobotml_Transition(self):
        return self.__ardurobotml_Transition

    @ardurobotml_Transition.setter
    def ardurobotml_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_Transition__ardurobotml_Transition", None)
        self.__ardurobotml_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardurobotml_TFSM14"):
                opp_val = getattr(old_value, "ardurobotml_TFSM14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardurobotml_TFSM14"):
                opp_val = getattr(value, "ardurobotml_TFSM14", None)
                if opp_val is None:
                    setattr(value, "ardurobotml_TFSM14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition21(self):
        return self.__Transition21

    @Transition21.setter
    def Transition21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_Transition__Transition21", None)
        self.__Transition21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ardurobotml_Transition30(self):
        return self.__ardurobotml_Transition30

    @ardurobotml_Transition30.setter
    def ardurobotml_Transition30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_Transition__ardurobotml_Transition30", None)
        self.__ardurobotml_Transition30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardurobotml_Guard"):
                opp_val = getattr(old_value, "ardurobotml_Guard", None)
                if opp_val == self:
                    setattr(old_value, "ardurobotml_Guard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardurobotml_Guard"):
                opp_val = getattr(value, "ardurobotml_Guard", None)
                setattr(value, "ardurobotml_Guard", self)

    @property
    def ardurobotml_Transition40(self):
        return self.__ardurobotml_Transition40

    @ardurobotml_Transition40.setter
    def ardurobotml_Transition40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_Transition__ardurobotml_Transition40", None)
        self.__ardurobotml_Transition40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardurobotml_FSMEvent39"):
                opp_val = getattr(old_value, "ardurobotml_FSMEvent39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardurobotml_FSMEvent39"):
                opp_val = getattr(value, "ardurobotml_FSMEvent39", None)
                if opp_val is None:
                    setattr(value, "ardurobotml_FSMEvent39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def fire(self) -> str:
        # TODO: Implement fire method
        pass

class ardurobotml_RegionContainer(NamedElement):

    pass
class ardurobotml_Guard(NamedElement):

    pass
class ardurobotml_Action(NamedElement):

    def __init__(self, ardurobotml_Action: "ardurobotml_State" = None, ardurobotml_Action47: "ardurobotml_ActionSequence" = None):
        self.ardurobotml_Action = ardurobotml_Action
        self.ardurobotml_Action47 = ardurobotml_Action47
        
    @property
    def ardurobotml_Action47(self):
        return self.__ardurobotml_Action47

    @ardurobotml_Action47.setter
    def ardurobotml_Action47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_Action__ardurobotml_Action47", None)
        self.__ardurobotml_Action47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardurobotml_ActionSequence"):
                opp_val = getattr(old_value, "ardurobotml_ActionSequence", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardurobotml_ActionSequence"):
                opp_val = getattr(value, "ardurobotml_ActionSequence", None)
                if opp_val is None:
                    setattr(value, "ardurobotml_ActionSequence", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ardurobotml_Action(self):
        return self.__ardurobotml_Action

    @ardurobotml_Action.setter
    def ardurobotml_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_Action__ardurobotml_Action", None)
        self.__ardurobotml_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardurobotml_State23"):
                opp_val = getattr(old_value, "ardurobotml_State23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardurobotml_State23"):
                opp_val = getattr(value, "ardurobotml_State23", None)
                if opp_val is None:
                    setattr(value, "ardurobotml_State23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def end(self):
        # TODO: Implement end method
        pass

    def begin(self):
        # TODO: Implement begin method
        pass

class ardurobotml_TimedSystem(NamedElement):

    pass
class RegionContainer:

    pass
class ardurobotml_TFSM(RegionContainer):

    def __init__(self, ardurobotml_TFSM6: "ardurobotml_State" = None, ardurobotml_TFSM8: set["ardurobotml_FSMEvent"] = None, ardurobotml_TFSM11: "ardurobotml_FSMClock" = None, ardurobotml_TFSM: "ardurobotml_TimedSystem" = None, ardurobotml_TFSM14: set["ardurobotml_Transition"] = None, ardurobotml_TFSM16: "ardurobotml_State" = None, owningFSM: set["ardurobotml_State"] = None, TFSM: "ardurobotml_State" = None):
        self.ardurobotml_TFSM6 = ardurobotml_TFSM6
        self.ardurobotml_TFSM8 = ardurobotml_TFSM8 if ardurobotml_TFSM8 is not None else set()
        self.ardurobotml_TFSM11 = ardurobotml_TFSM11
        self.ardurobotml_TFSM = ardurobotml_TFSM
        self.ardurobotml_TFSM14 = ardurobotml_TFSM14 if ardurobotml_TFSM14 is not None else set()
        self.ardurobotml_TFSM16 = ardurobotml_TFSM16
        self.owningFSM = owningFSM if owningFSM is not None else set()
        self.TFSM = TFSM
        
    @property
    def ardurobotml_TFSM11(self):
        return self.__ardurobotml_TFSM11

    @ardurobotml_TFSM11.setter
    def ardurobotml_TFSM11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_TFSM__ardurobotml_TFSM11", None)
        self.__ardurobotml_TFSM11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardurobotml_FSMClock12"):
                opp_val = getattr(old_value, "ardurobotml_FSMClock12", None)
                if opp_val == self:
                    setattr(old_value, "ardurobotml_FSMClock12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardurobotml_FSMClock12"):
                opp_val = getattr(value, "ardurobotml_FSMClock12", None)
                setattr(value, "ardurobotml_FSMClock12", self)

    @property
    def owningFSM(self):
        return self.__owningFSM

    @owningFSM.setter
    def owningFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_TFSM__owningFSM", None)
        self.__owningFSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    if opp_val == self:
                        setattr(item, "State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    setattr(item, "State", self)
                    

    @property
    def ardurobotml_TFSM8(self):
        return self.__ardurobotml_TFSM8

    @ardurobotml_TFSM8.setter
    def ardurobotml_TFSM8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_TFSM__ardurobotml_TFSM8", None)
        self.__ardurobotml_TFSM8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ardurobotml_FSMEvent9"):
                    opp_val = getattr(item, "ardurobotml_FSMEvent9", None)
                    
                    if opp_val == self:
                        setattr(item, "ardurobotml_FSMEvent9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ardurobotml_FSMEvent9"):
                    opp_val = getattr(item, "ardurobotml_FSMEvent9", None)
                    
                    setattr(item, "ardurobotml_FSMEvent9", self)
                    

    @property
    def ardurobotml_TFSM6(self):
        return self.__ardurobotml_TFSM6

    @ardurobotml_TFSM6.setter
    def ardurobotml_TFSM6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_TFSM__ardurobotml_TFSM6", None)
        self.__ardurobotml_TFSM6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardurobotml_State"):
                opp_val = getattr(old_value, "ardurobotml_State", None)
                if opp_val == self:
                    setattr(old_value, "ardurobotml_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardurobotml_State"):
                opp_val = getattr(value, "ardurobotml_State", None)
                setattr(value, "ardurobotml_State", self)

    @property
    def ardurobotml_TFSM(self):
        return self.__ardurobotml_TFSM

    @ardurobotml_TFSM.setter
    def ardurobotml_TFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_TFSM__ardurobotml_TFSM", None)
        self.__ardurobotml_TFSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardurobotml_TimedSystem"):
                opp_val = getattr(old_value, "ardurobotml_TimedSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardurobotml_TimedSystem"):
                opp_val = getattr(value, "ardurobotml_TimedSystem", None)
                if opp_val is None:
                    setattr(value, "ardurobotml_TimedSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ardurobotml_TFSM16(self):
        return self.__ardurobotml_TFSM16

    @ardurobotml_TFSM16.setter
    def ardurobotml_TFSM16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_TFSM__ardurobotml_TFSM16", None)
        self.__ardurobotml_TFSM16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardurobotml_State17"):
                opp_val = getattr(old_value, "ardurobotml_State17", None)
                if opp_val == self:
                    setattr(old_value, "ardurobotml_State17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardurobotml_State17"):
                opp_val = getattr(value, "ardurobotml_State17", None)
                setattr(value, "ardurobotml_State17", self)

    @property
    def TFSM(self):
        return self.__TFSM

    @TFSM.setter
    def TFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_TFSM__TFSM", None)
        self.__TFSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedStates"):
                opp_val = getattr(old_value, "ownedStates", None)
                if opp_val == self:
                    setattr(old_value, "ownedStates", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedStates"):
                opp_val = getattr(value, "ownedStates", None)
                setattr(value, "ownedStates", self)

    @property
    def ardurobotml_TFSM14(self):
        return self.__ardurobotml_TFSM14

    @ardurobotml_TFSM14.setter
    def ardurobotml_TFSM14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_TFSM__ardurobotml_TFSM14", None)
        self.__ardurobotml_TFSM14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ardurobotml_Transition"):
                    opp_val = getattr(item, "ardurobotml_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "ardurobotml_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ardurobotml_Transition"):
                    opp_val = getattr(item, "ardurobotml_Transition", None)
                    
                    setattr(item, "ardurobotml_Transition", self)
                    

    def initialize(self) -> str:
        # TODO: Implement initialize method
        pass

class ardurobotml_State(RegionContainer):

    def __init__(self, ardurobotml_State: "ardurobotml_TFSM" = None, State26: "ardurobotml_Transition" = None, State28: "ardurobotml_Transition" = None, ardurobotml_State17: "ardurobotml_TFSM" = None, State: "ardurobotml_TFSM" = None, source: set["ardurobotml_Transition"] = None, target: set["ardurobotml_Transition"] = None, ardurobotml_State23: set["ardurobotml_Action"] = None, ownedStates: "ardurobotml_TFSM" = None, ardurobotml_State43: "ardurobotml_Region" = None):
        self.ardurobotml_State = ardurobotml_State
        self.State26 = State26
        self.State28 = State28
        self.ardurobotml_State17 = ardurobotml_State17
        self.State = State
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.ardurobotml_State23 = ardurobotml_State23 if ardurobotml_State23 is not None else set()
        self.ownedStates = ownedStates
        self.ardurobotml_State43 = ardurobotml_State43
        
    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_State__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_State__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition21"):
                    opp_val = getattr(item, "Transition21", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition21"):
                    opp_val = getattr(item, "Transition21", None)
                    
                    setattr(item, "Transition21", self)
                    

    @property
    def ardurobotml_State17(self):
        return self.__ardurobotml_State17

    @ardurobotml_State17.setter
    def ardurobotml_State17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_State__ardurobotml_State17", None)
        self.__ardurobotml_State17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardurobotml_TFSM16"):
                opp_val = getattr(old_value, "ardurobotml_TFSM16", None)
                if opp_val == self:
                    setattr(old_value, "ardurobotml_TFSM16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardurobotml_TFSM16"):
                opp_val = getattr(value, "ardurobotml_TFSM16", None)
                setattr(value, "ardurobotml_TFSM16", self)

    @property
    def ardurobotml_State43(self):
        return self.__ardurobotml_State43

    @ardurobotml_State43.setter
    def ardurobotml_State43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_State__ardurobotml_State43", None)
        self.__ardurobotml_State43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardurobotml_Region"):
                opp_val = getattr(old_value, "ardurobotml_Region", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardurobotml_Region"):
                opp_val = getattr(value, "ardurobotml_Region", None)
                if opp_val is None:
                    setattr(value, "ardurobotml_Region", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedStates(self):
        return self.__ownedStates

    @ownedStates.setter
    def ownedStates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_State__ownedStates", None)
        self.__ownedStates = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TFSM"):
                opp_val = getattr(old_value, "TFSM", None)
                if opp_val == self:
                    setattr(old_value, "TFSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TFSM"):
                opp_val = getattr(value, "TFSM", None)
                setattr(value, "TFSM", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningFSM"):
                opp_val = getattr(old_value, "owningFSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningFSM"):
                opp_val = getattr(value, "owningFSM", None)
                if opp_val is None:
                    setattr(value, "owningFSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State26(self):
        return self.__State26

    @State26.setter
    def State26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_State__State26", None)
        self.__State26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingTransitions"):
                opp_val = getattr(old_value, "outgoingTransitions", None)
                if opp_val == self:
                    setattr(old_value, "outgoingTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingTransitions"):
                opp_val = getattr(value, "outgoingTransitions", None)
                setattr(value, "outgoingTransitions", self)

    @property
    def State28(self):
        return self.__State28

    @State28.setter
    def State28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_State__State28", None)
        self.__State28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingTransitions"):
                opp_val = getattr(old_value, "incomingTransitions", None)
                if opp_val == self:
                    setattr(old_value, "incomingTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingTransitions"):
                opp_val = getattr(value, "incomingTransitions", None)
                setattr(value, "incomingTransitions", self)

    @property
    def ardurobotml_State(self):
        return self.__ardurobotml_State

    @ardurobotml_State.setter
    def ardurobotml_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_State__ardurobotml_State", None)
        self.__ardurobotml_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardurobotml_TFSM6"):
                opp_val = getattr(old_value, "ardurobotml_TFSM6", None)
                if opp_val == self:
                    setattr(old_value, "ardurobotml_TFSM6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardurobotml_TFSM6"):
                opp_val = getattr(value, "ardurobotml_TFSM6", None)
                setattr(value, "ardurobotml_TFSM6", self)

    @property
    def ardurobotml_State23(self):
        return self.__ardurobotml_State23

    @ardurobotml_State23.setter
    def ardurobotml_State23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_State__ardurobotml_State23", None)
        self.__ardurobotml_State23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ardurobotml_Action"):
                    opp_val = getattr(item, "ardurobotml_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "ardurobotml_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ardurobotml_Action"):
                    opp_val = getattr(item, "ardurobotml_Action", None)
                    
                    setattr(item, "ardurobotml_Action", self)
                    

    def onLeave(self) -> str:
        # TODO: Implement onLeave method
        pass

    def onEnter(self) -> str:
        # TODO: Implement onEnter method
        pass

class ardurobotml_FSMEvent(NamedElement):

    pass
class ardurobotml_FSMClock(NamedElement):

    def __init__(self, value: int, ardurobotml_FSMClock: "ardurobotml_TimedSystem" = None, ardurobotml_FSMClock12: "ardurobotml_TFSM" = None, ardurobotml_FSMClock35: "ardurobotml_TemporalGuard" = None):
        self.value = value
        self.ardurobotml_FSMClock = ardurobotml_FSMClock
        self.ardurobotml_FSMClock12 = ardurobotml_FSMClock12
        self.ardurobotml_FSMClock35 = ardurobotml_FSMClock35
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def ardurobotml_FSMClock(self):
        return self.__ardurobotml_FSMClock

    @ardurobotml_FSMClock.setter
    def ardurobotml_FSMClock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_FSMClock__ardurobotml_FSMClock", None)
        self.__ardurobotml_FSMClock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardurobotml_TimedSystem2"):
                opp_val = getattr(old_value, "ardurobotml_TimedSystem2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardurobotml_TimedSystem2"):
                opp_val = getattr(value, "ardurobotml_TimedSystem2", None)
                if opp_val is None:
                    setattr(value, "ardurobotml_TimedSystem2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ardurobotml_FSMClock35(self):
        return self.__ardurobotml_FSMClock35

    @ardurobotml_FSMClock35.setter
    def ardurobotml_FSMClock35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_FSMClock__ardurobotml_FSMClock35", None)
        self.__ardurobotml_FSMClock35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardurobotml_TemporalGuard"):
                opp_val = getattr(old_value, "ardurobotml_TemporalGuard", None)
                if opp_val == self:
                    setattr(old_value, "ardurobotml_TemporalGuard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardurobotml_TemporalGuard"):
                opp_val = getattr(value, "ardurobotml_TemporalGuard", None)
                setattr(value, "ardurobotml_TemporalGuard", self)

    @property
    def ardurobotml_FSMClock12(self):
        return self.__ardurobotml_FSMClock12

    @ardurobotml_FSMClock12.setter
    def ardurobotml_FSMClock12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardurobotml_FSMClock__ardurobotml_FSMClock12", None)
        self.__ardurobotml_FSMClock12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardurobotml_TFSM11"):
                opp_val = getattr(old_value, "ardurobotml_TFSM11", None)
                if opp_val == self:
                    setattr(old_value, "ardurobotml_TFSM11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardurobotml_TFSM11"):
                opp_val = getattr(value, "ardurobotml_TFSM11", None)
                setattr(value, "ardurobotml_TFSM11", self)

    def ticks(self):
        # TODO: Implement ticks method
        pass
