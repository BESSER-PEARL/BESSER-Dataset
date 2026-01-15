from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CallConcurrencyFeature(Enum):
    sequential = "sequential"
    guarded = "guarded"
    concurrent = "concurrent"


############################################
# Definition of Classes
############################################

class DurationInterval:

    pass
class TimeInterval:

    pass
class IntervalConstraint:

    pass
class CommonBehavior_SimpleTime_DurationConstraint(IntervalConstraint):

    def __init__(self, firstEvent: bool, CommonBehavior_SimpleTime_DurationConstraint: "DurationInterval" = None):
        self.firstEvent = firstEvent
        self.CommonBehavior_SimpleTime_DurationConstraint = CommonBehavior_SimpleTime_DurationConstraint
        
    @property
    def firstEvent(self) -> bool:
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: bool):
        self.__firstEvent = firstEvent

    @property
    def CommonBehavior_SimpleTime_DurationConstraint(self):
        return self.__CommonBehavior_SimpleTime_DurationConstraint

    @CommonBehavior_SimpleTime_DurationConstraint.setter
    def CommonBehavior_SimpleTime_DurationConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CommonBehavior_SimpleTime_DurationConstraint__CommonBehavior_SimpleTime_DurationConstraint", None)
        self.__CommonBehavior_SimpleTime_DurationConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DurationInterval"):
                opp_val = getattr(old_value, "DurationInterval", None)
                if opp_val == self:
                    setattr(old_value, "DurationInterval", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DurationInterval"):
                opp_val = getattr(value, "DurationInterval", None)
                setattr(value, "DurationInterval", self)

class CommonBehavior_SimpleTime_TimeConstraint(IntervalConstraint):

    def __init__(self, firstEvent: bool, CommonBehavior_SimpleTime_TimeConstraint: "TimeInterval" = None):
        self.firstEvent = firstEvent
        self.CommonBehavior_SimpleTime_TimeConstraint = CommonBehavior_SimpleTime_TimeConstraint
        
    @property
    def firstEvent(self) -> bool:
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: bool):
        self.__firstEvent = firstEvent

    @property
    def CommonBehavior_SimpleTime_TimeConstraint(self):
        return self.__CommonBehavior_SimpleTime_TimeConstraint

    @CommonBehavior_SimpleTime_TimeConstraint.setter
    def CommonBehavior_SimpleTime_TimeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CommonBehavior_SimpleTime_TimeConstraint__CommonBehavior_SimpleTime_TimeConstraint", None)
        self.__CommonBehavior_SimpleTime_TimeConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TimeInterval"):
                opp_val = getattr(old_value, "TimeInterval", None)
                if opp_val == self:
                    setattr(old_value, "TimeInterval", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TimeInterval"):
                opp_val = getattr(value, "TimeInterval", None)
                setattr(value, "TimeInterval", self)

class Duration:

    pass
class Interval:

    pass
class CommonBehavior_SimpleTime_DurationInterval(Interval):

    pass
class CommonBehavior_SimpleTime_TimeInterval(Interval):

    pass
class Observation:

    pass
class CommonBehavior_SimpleTime_DurationObservation(Observation):

    def __init__(self, firstEvent: bool, CommonBehavior_SimpleTime_DurationObservation: set["NamedElement"] = None, Observation47: "CommonBehavior_SimpleTime_Duration", Observation: "CommonBehavior_SimpleTime_TimeExpression"):
        self.firstEvent = firstEvent
        self.CommonBehavior_SimpleTime_DurationObservation = CommonBehavior_SimpleTime_DurationObservation if CommonBehavior_SimpleTime_DurationObservation is not None else set()
        
    @property
    def firstEvent(self) -> bool:
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: bool):
        self.__firstEvent = firstEvent

    @property
    def CommonBehavior_SimpleTime_DurationObservation(self):
        return self.__CommonBehavior_SimpleTime_DurationObservation

    @CommonBehavior_SimpleTime_DurationObservation.setter
    def CommonBehavior_SimpleTime_DurationObservation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CommonBehavior_SimpleTime_DurationObservation__CommonBehavior_SimpleTime_DurationObservation", None)
        self.__CommonBehavior_SimpleTime_DurationObservation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NamedElement42"):
                    opp_val = getattr(item, "NamedElement42", None)
                    
                    if opp_val == self:
                        setattr(item, "NamedElement42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NamedElement42"):
                    opp_val = getattr(item, "NamedElement42", None)
                    
                    setattr(item, "NamedElement42", self)
                    

class CommonBehavior_SimpleTime_TimeObservation(Observation):

    def __init__(self, firstEvent: bool, CommonBehavior_SimpleTime_TimeObservation: "NamedElement" = None, Observation47: "CommonBehavior_SimpleTime_Duration", Observation: "CommonBehavior_SimpleTime_TimeExpression"):
        self.firstEvent = firstEvent
        self.CommonBehavior_SimpleTime_TimeObservation = CommonBehavior_SimpleTime_TimeObservation
        
    @property
    def firstEvent(self) -> bool:
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: bool):
        self.__firstEvent = firstEvent

    @property
    def CommonBehavior_SimpleTime_TimeObservation(self):
        return self.__CommonBehavior_SimpleTime_TimeObservation

    @CommonBehavior_SimpleTime_TimeObservation.setter
    def CommonBehavior_SimpleTime_TimeObservation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CommonBehavior_SimpleTime_TimeObservation__CommonBehavior_SimpleTime_TimeObservation", None)
        self.__CommonBehavior_SimpleTime_TimeObservation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NamedElement"):
                opp_val = getattr(old_value, "NamedElement", None)
                if opp_val == self:
                    setattr(old_value, "NamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NamedElement"):
                opp_val = getattr(value, "NamedElement", None)
                setattr(value, "NamedElement", self)

class ValueSpecification:

    pass
class CommonBehavior_SimpleTime_Duration(ValueSpecification):

    pass
class CommonBehavior_SimpleTime_Interval(ValueSpecification):

    pass
class CommonBehavior_Communications_Operation:

    pass
class CommonBehavior_SimpleTime_TimeExpression(ValueSpecification):

    pass
class TimeExpression:

    pass
class CommonBehavior_SimpleTime_TimeEvent:

    def __init__(self, isRelative: bool, CommonBehavior_SimpleTime_TimeEvent: "TimeExpression" = None):
        self.isRelative = isRelative
        self.CommonBehavior_SimpleTime_TimeEvent = CommonBehavior_SimpleTime_TimeEvent
        
    @property
    def isRelative(self) -> bool:
        return self.__isRelative

    @isRelative.setter
    def isRelative(self, isRelative: bool):
        self.__isRelative = isRelative

    @property
    def CommonBehavior_SimpleTime_TimeEvent(self):
        return self.__CommonBehavior_SimpleTime_TimeEvent

    @CommonBehavior_SimpleTime_TimeEvent.setter
    def CommonBehavior_SimpleTime_TimeEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CommonBehavior_SimpleTime_TimeEvent__CommonBehavior_SimpleTime_TimeEvent", None)
        self.__CommonBehavior_SimpleTime_TimeEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TimeExpression"):
                opp_val = getattr(old_value, "TimeExpression", None)
                if opp_val == self:
                    setattr(old_value, "TimeExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TimeExpression"):
                opp_val = getattr(value, "TimeExpression", None)
                setattr(value, "TimeExpression", self)

class CommonBehavior_Communications_ValueSpecification(ABC):

    pass
class CommonBehavior_Communications_PackageableElement(ABC):

    pass
class Event:

    pass
class CommonBehavior_Communications_ChangeEvent(Event):

    pass
class Operation:

    pass
class MessageEvent:

    pass
class CommonBehavior_Communications_SignalEvent(MessageEvent):

    pass
class CommonBehavior_Communications_CallEvent(MessageEvent):

    pass
class CommonBehavior_Communications_AnyReceiveEvent(MessageEvent):

    pass
class CommonBehavior_Communications_MessageEvent(Event):

    pass
class PackageableElement:

    pass
class CommonBehavior_SimpleTime_Observation(PackageableElement):

    pass
class CommonBehavior_Communications_Event(PackageableElement):

    pass
class Signal:

    pass
class CommonBehavior_Communications_Property:

    pass
class NamedElement:

    pass
class CommonBehavior_Communications_Trigger(NamedElement):

    pass
class CommonBehavior_Communications_NamedElement(ABC):

    pass
class CommonBehavior_BasicBehavior_Parameter:

    pass
class Property:

    pass
class CommonBehavior_BasicBehavior_Constraint:

    pass
class CommonBehavior_BasicBehavior_OpaqueExpression:

    pass
class Constraint:

    pass
class CommonBehavior_SimpleTime_IntervalConstraint(Constraint):

    pass
class CommonBehavior_BasicBehavior_BehavioralFeature(ABC):

    def __init__(self, concurrency: str, 19: set["Behavior"] = None):
        self.concurrency = concurrency
        self.19 = 19 if 19 is not None else set()
        
    @property
    def concurrency(self) -> str:
        return self.__concurrency

    @concurrency.setter
    def concurrency(self, concurrency: str):
        self.__concurrency = concurrency

    @property
    def 19(self):
        return self.__19

    @19.setter
    def 19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CommonBehavior_BasicBehavior_BehavioralFeature__19", None)
        self.__19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "20"):
                    opp_val = getattr(item, "20", None)
                    
                    if opp_val == self:
                        setattr(item, "20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "20"):
                    opp_val = getattr(item, "20", None)
                    
                    setattr(item, "20", self)
                    

class OpaqueBehavior:

    pass
class CommonBehavior_BasicBehavior_FunctionBehavior(OpaqueBehavior):

    pass
class CommonBehavior_BasicBehavior_RedefinableElement(ABC):

    pass
class Reception:

    pass
class Parameter:

    pass
class BehavioralFeature:

    pass
class CommonBehavior_Communications_Reception(BehavioralFeature):

    pass
class BehavioredClassifier:

    pass
class Class:

    pass
class CommonBehavior_BasicBehavior_Behavior(Class):

    def __init__(self, isReentrant: bool, CommonBehavior_BasicBehavior_Behavior: "BehavioredClassifier" = None, CommonBehavior_BasicBehavior_Behavior7: set["Behavior"] = None, : "BehavioralFeature" = None, CommonBehavior_BasicBehavior_Behavior16: set["Constraint"] = None, CommonBehavior_BasicBehavior_Behavior12: set["Parameter"] = None, CommonBehavior_BasicBehavior_Behavior14: set["Constraint"] = None):
        self.isReentrant = isReentrant
        self.CommonBehavior_BasicBehavior_Behavior = CommonBehavior_BasicBehavior_Behavior
        self.CommonBehavior_BasicBehavior_Behavior7 = CommonBehavior_BasicBehavior_Behavior7 if CommonBehavior_BasicBehavior_Behavior7 is not None else set()
        self. = 
        self.CommonBehavior_BasicBehavior_Behavior16 = CommonBehavior_BasicBehavior_Behavior16 if CommonBehavior_BasicBehavior_Behavior16 is not None else set()
        self.CommonBehavior_BasicBehavior_Behavior12 = CommonBehavior_BasicBehavior_Behavior12 if CommonBehavior_BasicBehavior_Behavior12 is not None else set()
        self.CommonBehavior_BasicBehavior_Behavior14 = CommonBehavior_BasicBehavior_Behavior14 if CommonBehavior_BasicBehavior_Behavior14 is not None else set()
        
    @property
    def isReentrant(self) -> bool:
        return self.__isReentrant

    @isReentrant.setter
    def isReentrant(self, isReentrant: bool):
        self.__isReentrant = isReentrant

    @property
    def CommonBehavior_BasicBehavior_Behavior12(self):
        return self.__CommonBehavior_BasicBehavior_Behavior12

    @CommonBehavior_BasicBehavior_Behavior12.setter
    def CommonBehavior_BasicBehavior_Behavior12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CommonBehavior_BasicBehavior_Behavior__CommonBehavior_BasicBehavior_Behavior12", None)
        self.__CommonBehavior_BasicBehavior_Behavior12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CommonBehavior_BasicBehavior_Behavior__", None)
        self.__ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "10"):
                opp_val = getattr(old_value, "10", None)
                if opp_val == self:
                    setattr(old_value, "10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "10"):
                opp_val = getattr(value, "10", None)
                setattr(value, "10", self)

    @property
    def CommonBehavior_BasicBehavior_Behavior14(self):
        return self.__CommonBehavior_BasicBehavior_Behavior14

    @CommonBehavior_BasicBehavior_Behavior14.setter
    def CommonBehavior_BasicBehavior_Behavior14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CommonBehavior_BasicBehavior_Behavior__CommonBehavior_BasicBehavior_Behavior14", None)
        self.__CommonBehavior_BasicBehavior_Behavior14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    setattr(item, "Constraint", self)
                    

    @property
    def CommonBehavior_BasicBehavior_Behavior(self):
        return self.__CommonBehavior_BasicBehavior_Behavior

    @CommonBehavior_BasicBehavior_Behavior.setter
    def CommonBehavior_BasicBehavior_Behavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CommonBehavior_BasicBehavior_Behavior__CommonBehavior_BasicBehavior_Behavior", None)
        self.__CommonBehavior_BasicBehavior_Behavior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BehavioredClassifier"):
                opp_val = getattr(old_value, "BehavioredClassifier", None)
                if opp_val == self:
                    setattr(old_value, "BehavioredClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BehavioredClassifier"):
                opp_val = getattr(value, "BehavioredClassifier", None)
                setattr(value, "BehavioredClassifier", self)

    @property
    def CommonBehavior_BasicBehavior_Behavior7(self):
        return self.__CommonBehavior_BasicBehavior_Behavior7

    @CommonBehavior_BasicBehavior_Behavior7.setter
    def CommonBehavior_BasicBehavior_Behavior7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CommonBehavior_BasicBehavior_Behavior__CommonBehavior_BasicBehavior_Behavior7", None)
        self.__CommonBehavior_BasicBehavior_Behavior7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Behavior8"):
                    opp_val = getattr(item, "Behavior8", None)
                    
                    if opp_val == self:
                        setattr(item, "Behavior8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Behavior8"):
                    opp_val = getattr(item, "Behavior8", None)
                    
                    setattr(item, "Behavior8", self)
                    

    @property
    def CommonBehavior_BasicBehavior_Behavior16(self):
        return self.__CommonBehavior_BasicBehavior_Behavior16

    @CommonBehavior_BasicBehavior_Behavior16.setter
    def CommonBehavior_BasicBehavior_Behavior16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CommonBehavior_BasicBehavior_Behavior__CommonBehavior_BasicBehavior_Behavior16", None)
        self.__CommonBehavior_BasicBehavior_Behavior16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint17"):
                    opp_val = getattr(item, "Constraint17", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint17"):
                    opp_val = getattr(item, "Constraint17", None)
                    
                    setattr(item, "Constraint17", self)
                    

class Classifier:

    pass
class CommonBehavior_Communications_Signal(Classifier):

    pass
class CommonBehavior_Communications_Interface(Classifier):

    pass
class CommonBehavior_BasicBehavior_BehavioredClassifier(Classifier):

    pass
class BasicBehavior_BehavioredClassifier:

    pass
class BasicBehavior_Classifier:

    pass
class CommonBehavior_BasicBehavior_Class(BasicBehavior_BehavioredClassifier, BasicBehavior_Classifier):

    pass
class RedefinableElement:

    pass
class CommonBehavior_BasicBehavior_Classifier(RedefinableElement):

    pass
class Behavior:

    pass
class CommonBehavior_BasicBehavior_OpaqueBehavior(Behavior):

    def __init__(self, body: str, language: str, Behavior25: "CommonBehavior_BasicBehavior_OpaqueExpression", Behavior: "CommonBehavior_BasicBehavior_BehavioredClassifier", Behavior8: "CommonBehavior_BasicBehavior_Behavior", Behavior3: "CommonBehavior_BasicBehavior_BehavioredClassifier", 20: "CommonBehavior_BasicBehavior_BehavioralFeature"):
        self.body = body
        self.language = language
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body
