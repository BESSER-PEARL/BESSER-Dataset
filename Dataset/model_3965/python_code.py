from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ExecutionSpecification:

    pass
class MessageEnd:

    pass
class OccurrenceSpecification:

    pass
class behavior_ExecutionOccurrenceSpecification(OccurrenceSpecification):

    pass
class behavior_MessageOccurrenceSpecification(MessageEnd, OccurrenceSpecification):

    pass
class Message:

    pass
class behavior_AlternativeMessage(Message):

    pass
class behavior_OptionalMessage(Message):

    pass
class RedefinableElement:

    pass
class Event:

    pass
class behavior_ExecutionEvent(Event):

    pass
class behavior_CreatEvent(Event):

    pass
class InteractionFragment:

    pass
class behavior_ExecutionSpecification(InteractionFragment):

    pass
class behavior_OccurrenceSpecification(InteractionFragment):

    pass
class Behavior:

    pass
class behavior_BehaviorExecutionSpecification(ExecutionSpecification):

    pass
class behavior_DestructionEvent(Event):

    pass
class behavior_Interaction(Behavior, InteractionFragment):

    pass
class behavior_Element(ABC):

    pass
class BehavioredClassifier:

    pass
class behavior_Object(BehavioredClassifier):

    pass
class behavior_Class(BehavioredClassifier):

    pass
class Object:

    pass
class behavior_Actor(Object):

    pass
class behavior_Feature(RedefinableElement):

    def __init__(self, isStatic: bool, Feature: "behavior_Classifier" = None, feature: set["behavior_Classifier"] = None):
        self.isStatic = isStatic
        self.Feature = Feature
        self.feature = feature if feature is not None else set()
        
    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Feature__Feature", None)
        self.__Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuringClassifier"):
                opp_val = getattr(old_value, "featuringClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuringClassifier"):
                opp_val = getattr(value, "featuringClassifier", None)
                if opp_val is None:
                    setattr(value, "featuringClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Feature__feature", None)
        self.__feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Classifier"):
                    opp_val = getattr(item, "Classifier", None)
                    
                    if opp_val == self:
                        setattr(item, "Classifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Classifier"):
                    opp_val = getattr(item, "Classifier", None)
                    
                    setattr(item, "Classifier", self)
                    

class Namespace:

    pass
class behavior_Classifier(Namespace):

    def __init__(self, isAbstract: bool, behavior_Classifier: set["behavior_NamedElement"] = None, behavior_Classifier16: "behavior_Classifier" = None, behavior_Classifier14: set["behavior_Classifier"] = None, behavior_Classifier19: "behavior_Classifier" = None, behavior_Classifier17: set["behavior_Classifier"] = None, featuringClassifier: set["behavior_Feature"] = None, behavior_Classifier22: "behavior_Class" = None, behavior_Classifier24: "behavior_RedefinableElement" = None, Classifier: "behavior_Feature" = None):
        self.isAbstract = isAbstract
        self.behavior_Classifier = behavior_Classifier if behavior_Classifier is not None else set()
        self.behavior_Classifier16 = behavior_Classifier16
        self.behavior_Classifier14 = behavior_Classifier14 if behavior_Classifier14 is not None else set()
        self.behavior_Classifier19 = behavior_Classifier19
        self.behavior_Classifier17 = behavior_Classifier17 if behavior_Classifier17 is not None else set()
        self.featuringClassifier = featuringClassifier if featuringClassifier is not None else set()
        self.behavior_Classifier22 = behavior_Classifier22
        self.behavior_Classifier24 = behavior_Classifier24
        self.Classifier = Classifier
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def behavior_Classifier(self):
        return self.__behavior_Classifier

    @behavior_Classifier.setter
    def behavior_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Classifier__behavior_Classifier", None)
        self.__behavior_Classifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behavior_NamedElement"):
                    opp_val = getattr(item, "behavior_NamedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "behavior_NamedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behavior_NamedElement"):
                    opp_val = getattr(item, "behavior_NamedElement", None)
                    
                    setattr(item, "behavior_NamedElement", self)
                    

    @property
    def behavior_Classifier19(self):
        return self.__behavior_Classifier19

    @behavior_Classifier19.setter
    def behavior_Classifier19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Classifier__behavior_Classifier19", None)
        self.__behavior_Classifier19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Classifier17"):
                opp_val = getattr(old_value, "behavior_Classifier17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Classifier17"):
                opp_val = getattr(value, "behavior_Classifier17", None)
                if opp_val is None:
                    setattr(value, "behavior_Classifier17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behavior_Classifier22(self):
        return self.__behavior_Classifier22

    @behavior_Classifier22.setter
    def behavior_Classifier22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Classifier__behavior_Classifier22", None)
        self.__behavior_Classifier22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Class"):
                opp_val = getattr(old_value, "behavior_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Class"):
                opp_val = getattr(value, "behavior_Class", None)
                if opp_val is None:
                    setattr(value, "behavior_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behavior_Classifier17(self):
        return self.__behavior_Classifier17

    @behavior_Classifier17.setter
    def behavior_Classifier17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Classifier__behavior_Classifier17", None)
        self.__behavior_Classifier17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behavior_Classifier19"):
                    opp_val = getattr(item, "behavior_Classifier19", None)
                    
                    if opp_val == self:
                        setattr(item, "behavior_Classifier19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behavior_Classifier19"):
                    opp_val = getattr(item, "behavior_Classifier19", None)
                    
                    setattr(item, "behavior_Classifier19", self)
                    

    @property
    def behavior_Classifier24(self):
        return self.__behavior_Classifier24

    @behavior_Classifier24.setter
    def behavior_Classifier24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Classifier__behavior_Classifier24", None)
        self.__behavior_Classifier24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_RedefinableElement"):
                opp_val = getattr(old_value, "behavior_RedefinableElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_RedefinableElement"):
                opp_val = getattr(value, "behavior_RedefinableElement", None)
                if opp_val is None:
                    setattr(value, "behavior_RedefinableElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behavior_Classifier16(self):
        return self.__behavior_Classifier16

    @behavior_Classifier16.setter
    def behavior_Classifier16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Classifier__behavior_Classifier16", None)
        self.__behavior_Classifier16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Classifier14"):
                opp_val = getattr(old_value, "behavior_Classifier14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Classifier14"):
                opp_val = getattr(value, "behavior_Classifier14", None)
                if opp_val is None:
                    setattr(value, "behavior_Classifier14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featuringClassifier(self):
        return self.__featuringClassifier

    @featuringClassifier.setter
    def featuringClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Classifier__featuringClassifier", None)
        self.__featuringClassifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    setattr(item, "Feature", self)
                    

    @property
    def behavior_Classifier14(self):
        return self.__behavior_Classifier14

    @behavior_Classifier14.setter
    def behavior_Classifier14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Classifier__behavior_Classifier14", None)
        self.__behavior_Classifier14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behavior_Classifier16"):
                    opp_val = getattr(item, "behavior_Classifier16", None)
                    
                    if opp_val == self:
                        setattr(item, "behavior_Classifier16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behavior_Classifier16"):
                    opp_val = getattr(item, "behavior_Classifier16", None)
                    
                    setattr(item, "behavior_Classifier16", self)
                    

    @property
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Classifier__Classifier", None)
        self.__Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature"):
                opp_val = getattr(old_value, "feature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature"):
                opp_val = getattr(value, "feature", None)
                if opp_val is None:
                    setattr(value, "feature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Classifier:

    pass
class behavior_BehavioredClassifier(Classifier):

    pass
class Class:

    pass
class Element:

    pass
class behavior_Comment(Element):

    def __init__(self, body: str, behavior_Comment: "behavior_Element" = None, behavior_Comment65: set["behavior_Element"] = None):
        self.body = body
        self.behavior_Comment = behavior_Comment
        self.behavior_Comment65 = behavior_Comment65 if behavior_Comment65 is not None else set()
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def behavior_Comment(self):
        return self.__behavior_Comment

    @behavior_Comment.setter
    def behavior_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Comment__behavior_Comment", None)
        self.__behavior_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Element"):
                opp_val = getattr(old_value, "behavior_Element", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Element"):
                opp_val = getattr(value, "behavior_Element", None)
                if opp_val is None:
                    setattr(value, "behavior_Element", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behavior_Comment65(self):
        return self.__behavior_Comment65

    @behavior_Comment65.setter
    def behavior_Comment65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Comment__behavior_Comment65", None)
        self.__behavior_Comment65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behavior_Element66"):
                    opp_val = getattr(item, "behavior_Element66", None)
                    
                    if opp_val == self:
                        setattr(item, "behavior_Element66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behavior_Element66"):
                    opp_val = getattr(item, "behavior_Element66", None)
                    
                    setattr(item, "behavior_Element66", self)
                    

class behavior_NamedElement(Element):

    def __init__(self, name: str, Archpoint: bool, behavior_NamedElement: "behavior_Classifier" = None):
        self.name = name
        self.Archpoint = Archpoint
        self.behavior_NamedElement = behavior_NamedElement
        
    @property
    def Archpoint(self) -> bool:
        return self.__Archpoint

    @Archpoint.setter
    def Archpoint(self, Archpoint: bool):
        self.__Archpoint = Archpoint

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def behavior_NamedElement(self):
        return self.__behavior_NamedElement

    @behavior_NamedElement.setter
    def behavior_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_NamedElement__behavior_NamedElement", None)
        self.__behavior_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Classifier"):
                opp_val = getattr(old_value, "behavior_Classifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Classifier"):
                opp_val = getattr(value, "behavior_Classifier", None)
                if opp_val is None:
                    setattr(value, "behavior_Classifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BehavioralFeature:

    pass
class behavior_Operation(BehavioralFeature):

    pass
class behavior_Behavior(Class):

    pass
class NamedElement:

    pass
class behavior_Lifeline(NamedElement):

    pass
class behavior_InteractionFragment(NamedElement):

    pass
class behavior_GeneralOrdering(NamedElement):

    pass
class behavior_Message(NamedElement):

    def __init__(self, MessageOrder: int, Message: "behavior_Interaction" = None, message: "behavior_Interaction" = None, behavior_Message: "behavior_MessageEnd" = None, behavior_Message38: "behavior_MessageEnd" = None, behavior_Message41: "behavior_Connector" = None, behavior_Message77: "behavior_MessageEnd" = None, behavior_Message92: "behavior_AlternativeMessage" = None):
        self.MessageOrder = MessageOrder
        self.Message = Message
        self.message = message
        self.behavior_Message = behavior_Message
        self.behavior_Message38 = behavior_Message38
        self.behavior_Message41 = behavior_Message41
        self.behavior_Message77 = behavior_Message77
        self.behavior_Message92 = behavior_Message92
        
    @property
    def MessageOrder(self) -> int:
        return self.__MessageOrder

    @MessageOrder.setter
    def MessageOrder(self, MessageOrder: int):
        self.__MessageOrder = MessageOrder

    @property
    def behavior_Message41(self):
        return self.__behavior_Message41

    @behavior_Message41.setter
    def behavior_Message41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Message__behavior_Message41", None)
        self.__behavior_Message41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Connector"):
                opp_val = getattr(old_value, "behavior_Connector", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Connector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Connector"):
                opp_val = getattr(value, "behavior_Connector", None)
                setattr(value, "behavior_Connector", self)

    @property
    def behavior_Message(self):
        return self.__behavior_Message

    @behavior_Message.setter
    def behavior_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Message__behavior_Message", None)
        self.__behavior_Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_MessageEnd"):
                opp_val = getattr(old_value, "behavior_MessageEnd", None)
                if opp_val == self:
                    setattr(old_value, "behavior_MessageEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_MessageEnd"):
                opp_val = getattr(value, "behavior_MessageEnd", None)
                setattr(value, "behavior_MessageEnd", self)

    @property
    def behavior_Message77(self):
        return self.__behavior_Message77

    @behavior_Message77.setter
    def behavior_Message77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Message__behavior_Message77", None)
        self.__behavior_Message77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_MessageEnd76"):
                opp_val = getattr(old_value, "behavior_MessageEnd76", None)
                if opp_val == self:
                    setattr(old_value, "behavior_MessageEnd76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_MessageEnd76"):
                opp_val = getattr(value, "behavior_MessageEnd76", None)
                setattr(value, "behavior_MessageEnd76", self)

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Message__message", None)
        self.__message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Interaction"):
                opp_val = getattr(old_value, "Interaction", None)
                if opp_val == self:
                    setattr(old_value, "Interaction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Interaction"):
                opp_val = getattr(value, "Interaction", None)
                setattr(value, "Interaction", self)

    @property
    def Message(self):
        return self.__Message

    @Message.setter
    def Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Message__Message", None)
        self.__Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interaction58"):
                opp_val = getattr(old_value, "interaction58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interaction58"):
                opp_val = getattr(value, "interaction58", None)
                if opp_val is None:
                    setattr(value, "interaction58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behavior_Message38(self):
        return self.__behavior_Message38

    @behavior_Message38.setter
    def behavior_Message38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Message__behavior_Message38", None)
        self.__behavior_Message38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_MessageEnd39"):
                opp_val = getattr(old_value, "behavior_MessageEnd39", None)
                if opp_val == self:
                    setattr(old_value, "behavior_MessageEnd39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_MessageEnd39"):
                opp_val = getattr(value, "behavior_MessageEnd39", None)
                setattr(value, "behavior_MessageEnd39", self)

    @property
    def behavior_Message92(self):
        return self.__behavior_Message92

    @behavior_Message92.setter
    def behavior_Message92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Message__behavior_Message92", None)
        self.__behavior_Message92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_AlternativeMessage"):
                opp_val = getattr(old_value, "behavior_AlternativeMessage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_AlternativeMessage"):
                opp_val = getattr(value, "behavior_AlternativeMessage", None)
                if opp_val is None:
                    setattr(value, "behavior_AlternativeMessage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class behavior_Event(NamedElement):

    pass
class behavior_MessageEnd(NamedElement):

    pass
class behavior_Namespace(NamedElement):

    pass
class behavior_RedefinableElement(NamedElement):

    pass
class Feature:

    pass
class behavior_Connector(Feature):

    pass
class behavior_BehavioralFeature(NamedElement, Feature):

    pass