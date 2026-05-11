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

class TimeInterval:

    pass
class IntervalConstraint:

    pass
class CommonBehavior_SimpleTime_DurationConstraint(IntervalConstraint):

    def __init__(self, firstEvent: bool, CommonBehavior_SimpleTime_DurationConstraint: "DurationInterval" = None):
        self.firstEvent = firstEvent
        self.CommonBehavior_SimpleTime_DurationConstraint = CommonBehavior_SimpleTime_DurationConstraint
        
        pass
    @property
    def firstEvent(self):
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
        
        pass
    @property
    def firstEvent(self):
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
class DurationInterval:

    pass
class TimeExpression:

    pass
class CommonBehavior_SimpleTime_TimeEvent:

    def __init__(self, isRelative: bool, CommonBehavior_SimpleTime_TimeEvent: "TimeExpression" = None):
        self.isRelative = isRelative
        self.CommonBehavior_SimpleTime_TimeEvent = CommonBehavior_SimpleTime_TimeEvent
        
        pass
    @property
    def isRelative(self):
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
class ValueSpecification:

    pass
class CommonBehavior_SimpleTime_Duration(ValueSpecification):

    pass
class CommonBehavior_SimpleTime_Interval(ValueSpecification):

    pass
class CommonBehavior_SimpleTime_TimeExpression(ValueSpecification):

    pass
class CommonBehavior_Communications_Operation:

    pass
class Operation:

    pass
class MessageEvent:

    pass
class CommonBehavior_Communications_CallEvent(MessageEvent):

    pass
class CommonBehavior_Communications_SignalEvent(MessageEvent):

    pass
class CommonBehavior_Communications_AnyReceiveEvent(MessageEvent):

    pass
class PackageableElement:

    pass
class CommonBehavior_Communications_Event(PackageableElement):

    pass
class CommonBehavior_Communications_PackageableElement(ABC):

    pass
class Event:

    pass
class CommonBehavior_Communications_ChangeEvent(Event):

    pass
class CommonBehavior_Communications_MessageEvent(Event):

    pass
class NamedElement:

    pass
class CommonBehavior_Communications_Trigger(NamedElement):

    pass
class CommonBehavior_Communications_NamedElement(ABC):

    pass
class CommonBehavior_SimpleTime_Observation(PackageableElement):

    pass
class Observation:

    pass
class CommonBehavior_SimpleTime_DurationObservation(Observation):

    def __init__(self, firstEvent: bool, CommonBehavior_SimpleTime_DurationObservation: set["NamedElement"] = None, Observation45: "CommonBehavior_SimpleTime_Duration" = None, Observation: "CommonBehavior_SimpleTime_TimeExpression" = None):
        self.firstEvent = firstEvent
        self.CommonBehavior_SimpleTime_DurationObservation = CommonBehavior_SimpleTime_DurationObservation if CommonBehavior_SimpleTime_DurationObservation is not None else set()
        
        pass
    @property
    def firstEvent(self):
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
                if hasattr(item, "NamedElement40"):
                    opp_val = getattr(item, "NamedElement40", None)
                    
                    if opp_val == self:
                        setattr(item, "NamedElement40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NamedElement40"):
                    opp_val = getattr(item, "NamedElement40", None)
                    
                    setattr(item, "NamedElement40", self)
                    

class CommonBehavior_SimpleTime_TimeObservation(Observation):

    def __init__(self, firstEvent: bool, CommonBehavior_SimpleTime_TimeObservation: "NamedElement" = None, Observation45: "CommonBehavior_SimpleTime_Duration" = None, Observation: "CommonBehavior_SimpleTime_TimeExpression" = None):
        self.firstEvent = firstEvent
        self.CommonBehavior_SimpleTime_TimeObservation = CommonBehavior_SimpleTime_TimeObservation
        
        pass
    @property
    def firstEvent(self):
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

class CommonBehavior_Communications_Property:

    pass
class Property:

    pass
class CommonBehavior_BasicBehavior_Constraint:

    pass
class CommonBehavior_BasicBehavior_OpaqueExpression:

    pass
class CommonBehavior_BasicBehavior_Parameter:

    pass
class Signal:

    pass
class CommonBehavior_BasicBehavior_RedefinableElement(ABC):

    pass
class Constraint:

    pass
class CommonBehavior_SimpleTime_IntervalConstraint(Constraint):

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

    def __init__(self, isReentrant: bool, CommonBehavior_BasicBehavior_Behavior: "BehavioredClassifier" = None, CommonBehavior_BasicBehavior_Behavior7: set["Behavior"] = None, method: "BehavioralFeature" = None, CommonBehavior_BasicBehavior_Behavior11: set["Parameter"] = None, CommonBehavior_BasicBehavior_Behavior13: set["Constraint"] = None, CommonBehavior_BasicBehavior_Behavior15: set["Constraint"] = None):
        self.isReentrant = isReentrant
        self.CommonBehavior_BasicBehavior_Behavior = CommonBehavior_BasicBehavior_Behavior
        self.CommonBehavior_BasicBehavior_Behavior7 = CommonBehavior_BasicBehavior_Behavior7 if CommonBehavior_BasicBehavior_Behavior7 is not None else set()
        self.method = method
        self.CommonBehavior_BasicBehavior_Behavior11 = CommonBehavior_BasicBehavior_Behavior11 if CommonBehavior_BasicBehavior_Behavior11 is not None else set()
        self.CommonBehavior_BasicBehavior_Behavior13 = CommonBehavior_BasicBehavior_Behavior13 if CommonBehavior_BasicBehavior_Behavior13 is not None else set()
        self.CommonBehavior_BasicBehavior_Behavior15 = CommonBehavior_BasicBehavior_Behavior15 if CommonBehavior_BasicBehavior_Behavior15 is not None else set()
        
        pass
    @property
    def isReentrant(self):
        return self.__isReentrant

    @isReentrant.setter
    def isReentrant(self, isReentrant: bool):
        self.__isReentrant = isReentrant


    @property
    def CommonBehavior_BasicBehavior_Behavior13(self):
        return self.__CommonBehavior_BasicBehavior_Behavior13

    @CommonBehavior_BasicBehavior_Behavior13.setter
    def CommonBehavior_BasicBehavior_Behavior13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CommonBehavior_BasicBehavior_Behavior__CommonBehavior_BasicBehavior_Behavior13", None)
        self.__CommonBehavior_BasicBehavior_Behavior13 = value if value is not None else set()
        
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
    def CommonBehavior_BasicBehavior_Behavior15(self):
        return self.__CommonBehavior_BasicBehavior_Behavior15

    @CommonBehavior_BasicBehavior_Behavior15.setter
    def CommonBehavior_BasicBehavior_Behavior15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CommonBehavior_BasicBehavior_Behavior__CommonBehavior_BasicBehavior_Behavior15", None)
        self.__CommonBehavior_BasicBehavior_Behavior15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint16"):
                    opp_val = getattr(item, "Constraint16", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint16"):
                    opp_val = getattr(item, "Constraint16", None)
                    
                    setattr(item, "Constraint16", self)
                    

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
    def CommonBehavior_BasicBehavior_Behavior11(self):
        return self.__CommonBehavior_BasicBehavior_Behavior11

    @CommonBehavior_BasicBehavior_Behavior11.setter
    def CommonBehavior_BasicBehavior_Behavior11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CommonBehavior_BasicBehavior_Behavior__CommonBehavior_BasicBehavior_Behavior11", None)
        self.__CommonBehavior_BasicBehavior_Behavior11 = value if value is not None else set()
        
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
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CommonBehavior_BasicBehavior_Behavior__method", None)
        self.__method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BehavioralFeature"):
                opp_val = getattr(old_value, "BehavioralFeature", None)
                if opp_val == self:
                    setattr(old_value, "BehavioralFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BehavioralFeature"):
                opp_val = getattr(value, "BehavioralFeature", None)
                setattr(value, "BehavioralFeature", self)

class Reception:

    pass
class BasicBehavior_BehavioredClassifier:

    pass
class BasicBehavior_Classifier:

    pass
class CommonBehavior_BasicBehavior_Class(BasicBehavior_Classifier, BasicBehavior_BehavioredClassifier):

    pass
class RedefinableElement:

    pass
class CommonBehavior_BasicBehavior_Classifier(RedefinableElement):

    pass
class Behavior:

    pass
class CommonBehavior_BasicBehavior_OpaqueBehavior(Behavior):

    def __init__(self, language: str, body: str, Behavior: "CommonBehavior_BasicBehavior_BehavioredClassifier" = None, Behavior18: "CommonBehavior_BasicBehavior_BehavioralFeature" = None, Behavior8: "CommonBehavior_BasicBehavior_Behavior" = None, Behavior3: "CommonBehavior_BasicBehavior_BehavioredClassifier" = None, Behavior23: "CommonBehavior_BasicBehavior_OpaqueExpression" = None):
        self.language = language
        self.body = body
        
        pass
    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


class CommonBehavior_BasicBehavior_BehavioralFeature(ABC):

    def __init__(self, concurrency: str, specification: set["Behavior"] = None):
        self.concurrency = concurrency
        self.specification = specification if specification is not None else set()
        
        pass
    @property
    def concurrency(self):
        return self.__concurrency

    @concurrency.setter
    def concurrency(self, concurrency: str):
        self.__concurrency = concurrency


    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CommonBehavior_BasicBehavior_BehavioralFeature__specification", None)
        self.__specification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Behavior18"):
                    opp_val = getattr(item, "Behavior18", None)
                    
                    if opp_val == self:
                        setattr(item, "Behavior18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Behavior18"):
                    opp_val = getattr(item, "Behavior18", None)
                    
                    setattr(item, "Behavior18", self)
                    

class OpaqueBehavior:

    pass
class CommonBehavior_BasicBehavior_FunctionBehavior(OpaqueBehavior):

    pass
class Classifier:

    pass
class CommonBehavior_Communications_Interface(Classifier):

    pass
class CommonBehavior_Communications_Signal(Classifier):

    pass
class CommonBehavior_BasicBehavior_BehavioredClassifier(Classifier):

    pass