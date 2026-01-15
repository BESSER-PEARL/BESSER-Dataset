from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ChoreographyLoopType(Enum):
    None = "None"
    Standard = "Standard"
    MultiInstanceSequential = "MultiInstanceSequential"
    MultiInstanceParallel = "MultiInstanceParallel"
class AssociationDirection(Enum):
    None = "None"
    One = "One"
    Both = "Both"
class ItemKind(Enum):
    Physical = "Physical"
    Information = "Information"
class EventBasedGatewayType(Enum):
    Parallel = "Parallel"
    Exclusive = "Exclusive"
class GatewayDirection(Enum):
    Unspecified = "Unspecified"
    Converging = "Converging"
    Diverging = "Diverging"
    Mixed = "Mixed"
class AdHocOrdering(Enum):
    Parallel = "Parallel"
    Sequential = "Sequential"
class RelationshipDirection(Enum):
    None = "None"
    Forward = "Forward"
    Backward = "Backward"
    Both = "Both"
class MultiInstanceBehavior(Enum):
    None = "None"
    One = "One"
    All = "All"
    Complex = "Complex"
class ProcessType(Enum):
    None = "None"
    Public = "Public"
    Private = "Private"


############################################
# Definition of Classes
############################################

class bpmn2_BPMNDiagram:

    pass
class SubProcess:

    pass
class bpmn2_Transaction(SubProcess):

    def __init__(self, protocol: str, method: str):
        self.protocol = protocol
        self.method = method
        
    @property
    def protocol(self) -> str:
        return self.__protocol

    @protocol.setter
    def protocol(self, protocol: str):
        self.__protocol = protocol

    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

class bpmn2_AdHocSubProcess(SubProcess):

    def __init__(self, ordering: str, cancelRemainingInstances: bool, bpmn2_AdHocSubProcess: "bpmn2_Expression" = None):
        self.ordering = ordering
        self.cancelRemainingInstances = cancelRemainingInstances
        self.bpmn2_AdHocSubProcess = bpmn2_AdHocSubProcess
        
    @property
    def cancelRemainingInstances(self) -> bool:
        return self.__cancelRemainingInstances

    @cancelRemainingInstances.setter
    def cancelRemainingInstances(self, cancelRemainingInstances: bool):
        self.__cancelRemainingInstances = cancelRemainingInstances

    @property
    def ordering(self) -> str:
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering

    @property
    def bpmn2_AdHocSubProcess(self):
        return self.__bpmn2_AdHocSubProcess

    @bpmn2_AdHocSubProcess.setter
    def bpmn2_AdHocSubProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_AdHocSubProcess__bpmn2_AdHocSubProcess", None)
        self.__bpmn2_AdHocSubProcess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Expression471"):
                opp_val = getattr(old_value, "bpmn2_Expression471", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Expression471", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Expression471"):
                opp_val = getattr(value, "bpmn2_Expression471", None)
                setattr(value, "bpmn2_Expression471", self)

class LoopCharacteristics:

    pass
class bpmn2_StandardLoopCharacteristics(LoopCharacteristics):

    def __init__(self, testBefore: bool, bpmn2_StandardLoopCharacteristics: "bpmn2_Expression" = None, bpmn2_StandardLoopCharacteristics456: "bpmn2_Expression" = None):
        self.testBefore = testBefore
        self.bpmn2_StandardLoopCharacteristics = bpmn2_StandardLoopCharacteristics
        self.bpmn2_StandardLoopCharacteristics456 = bpmn2_StandardLoopCharacteristics456
        
    @property
    def testBefore(self) -> bool:
        return self.__testBefore

    @testBefore.setter
    def testBefore(self, testBefore: bool):
        self.__testBefore = testBefore

    @property
    def bpmn2_StandardLoopCharacteristics456(self):
        return self.__bpmn2_StandardLoopCharacteristics456

    @bpmn2_StandardLoopCharacteristics456.setter
    def bpmn2_StandardLoopCharacteristics456(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_StandardLoopCharacteristics__bpmn2_StandardLoopCharacteristics456", None)
        self.__bpmn2_StandardLoopCharacteristics456 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Expression457"):
                opp_val = getattr(old_value, "bpmn2_Expression457", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Expression457", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Expression457"):
                opp_val = getattr(value, "bpmn2_Expression457", None)
                setattr(value, "bpmn2_Expression457", self)

    @property
    def bpmn2_StandardLoopCharacteristics(self):
        return self.__bpmn2_StandardLoopCharacteristics

    @bpmn2_StandardLoopCharacteristics.setter
    def bpmn2_StandardLoopCharacteristics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_StandardLoopCharacteristics__bpmn2_StandardLoopCharacteristics", None)
        self.__bpmn2_StandardLoopCharacteristics = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Expression454"):
                opp_val = getattr(old_value, "bpmn2_Expression454", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Expression454", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Expression454"):
                opp_val = getattr(value, "bpmn2_Expression454", None)
                setattr(value, "bpmn2_Expression454", self)

class bpmn2_MultiInstanceLoopCharacteristics(LoopCharacteristics):

    def __init__(self, isSequential: bool, behavior: str, bpmn2_MultiInstanceLoopCharacteristics: "bpmn2_Expression" = None, bpmn2_MultiInstanceLoopCharacteristics426: "bpmn2_ItemAwareElement" = None, bpmn2_MultiInstanceLoopCharacteristics429: "bpmn2_ItemAwareElement" = None, bpmn2_MultiInstanceLoopCharacteristics432: "bpmn2_DataInput" = None, bpmn2_MultiInstanceLoopCharacteristics435: "bpmn2_DataOutput" = None, bpmn2_MultiInstanceLoopCharacteristics438: "bpmn2_Expression" = None, bpmn2_MultiInstanceLoopCharacteristics441: set["bpmn2_ComplexBehaviorDefinition"] = None, bpmn2_MultiInstanceLoopCharacteristics443: "bpmn2_EventDefinition" = None, bpmn2_MultiInstanceLoopCharacteristics446: "bpmn2_EventDefinition" = None):
        self.isSequential = isSequential
        self.behavior = behavior
        self.bpmn2_MultiInstanceLoopCharacteristics = bpmn2_MultiInstanceLoopCharacteristics
        self.bpmn2_MultiInstanceLoopCharacteristics426 = bpmn2_MultiInstanceLoopCharacteristics426
        self.bpmn2_MultiInstanceLoopCharacteristics429 = bpmn2_MultiInstanceLoopCharacteristics429
        self.bpmn2_MultiInstanceLoopCharacteristics432 = bpmn2_MultiInstanceLoopCharacteristics432
        self.bpmn2_MultiInstanceLoopCharacteristics435 = bpmn2_MultiInstanceLoopCharacteristics435
        self.bpmn2_MultiInstanceLoopCharacteristics438 = bpmn2_MultiInstanceLoopCharacteristics438
        self.bpmn2_MultiInstanceLoopCharacteristics441 = bpmn2_MultiInstanceLoopCharacteristics441 if bpmn2_MultiInstanceLoopCharacteristics441 is not None else set()
        self.bpmn2_MultiInstanceLoopCharacteristics443 = bpmn2_MultiInstanceLoopCharacteristics443
        self.bpmn2_MultiInstanceLoopCharacteristics446 = bpmn2_MultiInstanceLoopCharacteristics446
        
    @property
    def behavior(self) -> str:
        return self.__behavior

    @behavior.setter
    def behavior(self, behavior: str):
        self.__behavior = behavior

    @property
    def isSequential(self) -> bool:
        return self.__isSequential

    @isSequential.setter
    def isSequential(self, isSequential: bool):
        self.__isSequential = isSequential

    @property
    def bpmn2_MultiInstanceLoopCharacteristics438(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics438

    @bpmn2_MultiInstanceLoopCharacteristics438.setter
    def bpmn2_MultiInstanceLoopCharacteristics438(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics438", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics438 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Expression439"):
                opp_val = getattr(old_value, "bpmn2_Expression439", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Expression439", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Expression439"):
                opp_val = getattr(value, "bpmn2_Expression439", None)
                setattr(value, "bpmn2_Expression439", self)

    @property
    def bpmn2_MultiInstanceLoopCharacteristics426(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics426

    @bpmn2_MultiInstanceLoopCharacteristics426.setter
    def bpmn2_MultiInstanceLoopCharacteristics426(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics426", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics426 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemAwareElement427"):
                opp_val = getattr(old_value, "bpmn2_ItemAwareElement427", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemAwareElement427", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemAwareElement427"):
                opp_val = getattr(value, "bpmn2_ItemAwareElement427", None)
                setattr(value, "bpmn2_ItemAwareElement427", self)

    @property
    def bpmn2_MultiInstanceLoopCharacteristics446(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics446

    @bpmn2_MultiInstanceLoopCharacteristics446.setter
    def bpmn2_MultiInstanceLoopCharacteristics446(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics446", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics446 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_EventDefinition447"):
                opp_val = getattr(old_value, "bpmn2_EventDefinition447", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_EventDefinition447", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_EventDefinition447"):
                opp_val = getattr(value, "bpmn2_EventDefinition447", None)
                setattr(value, "bpmn2_EventDefinition447", self)

    @property
    def bpmn2_MultiInstanceLoopCharacteristics(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics

    @bpmn2_MultiInstanceLoopCharacteristics.setter
    def bpmn2_MultiInstanceLoopCharacteristics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Expression424"):
                opp_val = getattr(old_value, "bpmn2_Expression424", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Expression424", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Expression424"):
                opp_val = getattr(value, "bpmn2_Expression424", None)
                setattr(value, "bpmn2_Expression424", self)

    @property
    def bpmn2_MultiInstanceLoopCharacteristics435(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics435

    @bpmn2_MultiInstanceLoopCharacteristics435.setter
    def bpmn2_MultiInstanceLoopCharacteristics435(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics435", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics435 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DataOutput436"):
                opp_val = getattr(old_value, "bpmn2_DataOutput436", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_DataOutput436", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DataOutput436"):
                opp_val = getattr(value, "bpmn2_DataOutput436", None)
                setattr(value, "bpmn2_DataOutput436", self)

    @property
    def bpmn2_MultiInstanceLoopCharacteristics443(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics443

    @bpmn2_MultiInstanceLoopCharacteristics443.setter
    def bpmn2_MultiInstanceLoopCharacteristics443(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics443", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics443 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_EventDefinition444"):
                opp_val = getattr(old_value, "bpmn2_EventDefinition444", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_EventDefinition444", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_EventDefinition444"):
                opp_val = getattr(value, "bpmn2_EventDefinition444", None)
                setattr(value, "bpmn2_EventDefinition444", self)

    @property
    def bpmn2_MultiInstanceLoopCharacteristics432(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics432

    @bpmn2_MultiInstanceLoopCharacteristics432.setter
    def bpmn2_MultiInstanceLoopCharacteristics432(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics432", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics432 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DataInput433"):
                opp_val = getattr(old_value, "bpmn2_DataInput433", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_DataInput433", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DataInput433"):
                opp_val = getattr(value, "bpmn2_DataInput433", None)
                setattr(value, "bpmn2_DataInput433", self)

    @property
    def bpmn2_MultiInstanceLoopCharacteristics441(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics441

    @bpmn2_MultiInstanceLoopCharacteristics441.setter
    def bpmn2_MultiInstanceLoopCharacteristics441(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics441", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics441 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_ComplexBehaviorDefinition"):
                    opp_val = getattr(item, "bpmn2_ComplexBehaviorDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_ComplexBehaviorDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_ComplexBehaviorDefinition"):
                    opp_val = getattr(item, "bpmn2_ComplexBehaviorDefinition", None)
                    
                    setattr(item, "bpmn2_ComplexBehaviorDefinition", self)
                    

    @property
    def bpmn2_MultiInstanceLoopCharacteristics429(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics429

    @bpmn2_MultiInstanceLoopCharacteristics429.setter
    def bpmn2_MultiInstanceLoopCharacteristics429(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics429", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics429 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemAwareElement430"):
                opp_val = getattr(old_value, "bpmn2_ItemAwareElement430", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemAwareElement430", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemAwareElement430"):
                opp_val = getattr(value, "bpmn2_ItemAwareElement430", None)
                setattr(value, "bpmn2_ItemAwareElement430", self)

class Artifact:

    pass
class bpmn2_Association(Artifact):

    def __init__(self, associationDirection: str, bpmn2_Association: "bpmn2_BaseElement" = None, bpmn2_Association415: "bpmn2_BaseElement" = None):
        self.associationDirection = associationDirection
        self.bpmn2_Association = bpmn2_Association
        self.bpmn2_Association415 = bpmn2_Association415
        
    @property
    def associationDirection(self) -> str:
        return self.__associationDirection

    @associationDirection.setter
    def associationDirection(self, associationDirection: str):
        self.__associationDirection = associationDirection

    @property
    def bpmn2_Association(self):
        return self.__bpmn2_Association

    @bpmn2_Association.setter
    def bpmn2_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Association__bpmn2_Association", None)
        self.__bpmn2_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_BaseElement413"):
                opp_val = getattr(old_value, "bpmn2_BaseElement413", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_BaseElement413", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_BaseElement413"):
                opp_val = getattr(value, "bpmn2_BaseElement413", None)
                setattr(value, "bpmn2_BaseElement413", self)

    @property
    def bpmn2_Association415(self):
        return self.__bpmn2_Association415

    @bpmn2_Association415.setter
    def bpmn2_Association415(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Association__bpmn2_Association415", None)
        self.__bpmn2_Association415 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_BaseElement416"):
                opp_val = getattr(old_value, "bpmn2_BaseElement416", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_BaseElement416", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_BaseElement416"):
                opp_val = getattr(value, "bpmn2_BaseElement416", None)
                setattr(value, "bpmn2_BaseElement416", self)

class bpmn2_Group(Artifact):

    pass
class bpmn2_TextAnnotation(Artifact):

    def __init__(self, text: str, textFormat: str):
        self.text = text
        self.textFormat = textFormat
        
    @property
    def textFormat(self) -> str:
        return self.__textFormat

    @textFormat.setter
    def textFormat(self, textFormat: str):
        self.__textFormat = textFormat

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class Choreography:

    pass
class bpmn2_GlobalChoreographyTask(Choreography):

    pass
class ChoreographyActivity:

    pass
class bpmn2_ChoreographyTask(ChoreographyActivity):

    pass
class bpmn2_CallChoreography(ChoreographyActivity):

    pass
class ConversationNode:

    pass
class bpmn2_Conversation(ConversationNode):

    pass
class bpmn2_SubConversation(ConversationNode):

    pass
class bpmn2_CallConversation(ConversationNode):

    pass
class EventDefinition:

    pass
class bpmn2_SignalEventDefinition(EventDefinition):

    pass
class bpmn2_CancelEventDefinition(EventDefinition):

    pass
class bpmn2_ConditionalEventDefinition(EventDefinition):

    pass
class bpmn2_MessageEventDefinition(EventDefinition):

    pass
class bpmn2_LinkEventDefinition(EventDefinition):

    def __init__(self, name: str, LinkEventDefinition: "bpmn2_LinkEventDefinition" = None, source: "bpmn2_LinkEventDefinition" = None, LinkEventDefinition367: "bpmn2_LinkEventDefinition" = None, target: set["bpmn2_LinkEventDefinition"] = None):
        self.name = name
        self.LinkEventDefinition = LinkEventDefinition
        self.source = source
        self.LinkEventDefinition367 = LinkEventDefinition367
        self.target = target if target is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def LinkEventDefinition367(self):
        return self.__LinkEventDefinition367

    @LinkEventDefinition367.setter
    def LinkEventDefinition367(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_LinkEventDefinition__LinkEventDefinition367", None)
        self.__LinkEventDefinition367 = value
        
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
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_LinkEventDefinition__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LinkEventDefinition367"):
                    opp_val = getattr(item, "LinkEventDefinition367", None)
                    
                    if opp_val == self:
                        setattr(item, "LinkEventDefinition367", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LinkEventDefinition367"):
                    opp_val = getattr(item, "LinkEventDefinition367", None)
                    
                    setattr(item, "LinkEventDefinition367", self)
                    

    @property
    def LinkEventDefinition(self):
        return self.__LinkEventDefinition

    @LinkEventDefinition.setter
    def LinkEventDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_LinkEventDefinition__LinkEventDefinition", None)
        self.__LinkEventDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if opp_val == self:
                    setattr(old_value, "source", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                setattr(value, "source", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_LinkEventDefinition__source", None)
        self.__source = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LinkEventDefinition"):
                opp_val = getattr(old_value, "LinkEventDefinition", None)
                if opp_val == self:
                    setattr(old_value, "LinkEventDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LinkEventDefinition"):
                opp_val = getattr(value, "LinkEventDefinition", None)
                setattr(value, "LinkEventDefinition", self)

class bpmn2_TimerEventDefinition(EventDefinition):

    pass
class bpmn2_CompensateEventDefinition(EventDefinition):

    def __init__(self, waitForCompletion: bool, bpmn2_CompensateEventDefinition: "bpmn2_Activity" = None):
        self.waitForCompletion = waitForCompletion
        self.bpmn2_CompensateEventDefinition = bpmn2_CompensateEventDefinition
        
    @property
    def waitForCompletion(self) -> bool:
        return self.__waitForCompletion

    @waitForCompletion.setter
    def waitForCompletion(self, waitForCompletion: bool):
        self.__waitForCompletion = waitForCompletion

    @property
    def bpmn2_CompensateEventDefinition(self):
        return self.__bpmn2_CompensateEventDefinition

    @bpmn2_CompensateEventDefinition.setter
    def bpmn2_CompensateEventDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CompensateEventDefinition__bpmn2_CompensateEventDefinition", None)
        self.__bpmn2_CompensateEventDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Activity354"):
                opp_val = getattr(old_value, "bpmn2_Activity354", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Activity354", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Activity354"):
                opp_val = getattr(value, "bpmn2_Activity354", None)
                setattr(value, "bpmn2_Activity354", self)

class bpmn2_Escalation:

    def __init__(self, name: str, escalationCode: str, id: str, bpmn2_Escalation: "bpmn2_EscalationEventDefinition" = None, bpmn2_Escalation351: "bpmn2_ItemDefinition" = None):
        self.name = name
        self.escalationCode = escalationCode
        self.id = id
        self.bpmn2_Escalation = bpmn2_Escalation
        self.bpmn2_Escalation351 = bpmn2_Escalation351
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def escalationCode(self) -> str:
        return self.__escalationCode

    @escalationCode.setter
    def escalationCode(self, escalationCode: str):
        self.__escalationCode = escalationCode

    @property
    def bpmn2_Escalation(self):
        return self.__bpmn2_Escalation

    @bpmn2_Escalation.setter
    def bpmn2_Escalation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Escalation__bpmn2_Escalation", None)
        self.__bpmn2_Escalation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_EscalationEventDefinition"):
                opp_val = getattr(old_value, "bpmn2_EscalationEventDefinition", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_EscalationEventDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_EscalationEventDefinition"):
                opp_val = getattr(value, "bpmn2_EscalationEventDefinition", None)
                setattr(value, "bpmn2_EscalationEventDefinition", self)

    @property
    def bpmn2_Escalation351(self):
        return self.__bpmn2_Escalation351

    @bpmn2_Escalation351.setter
    def bpmn2_Escalation351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Escalation__bpmn2_Escalation351", None)
        self.__bpmn2_Escalation351 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemDefinition352"):
                opp_val = getattr(old_value, "bpmn2_ItemDefinition352", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemDefinition352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemDefinition352"):
                opp_val = getattr(value, "bpmn2_ItemDefinition352", None)
                setattr(value, "bpmn2_ItemDefinition352", self)

class bpmn2_EscalationEventDefinition(EventDefinition):

    pass
class bpmn2_TerminateEventDefinition(EventDefinition):

    pass
class bpmn2_ErrorEventDefinition(EventDefinition):

    pass
class ThrowEvent:

    pass
class bpmn2_EndEvent(ThrowEvent):

    pass
class bpmn2_ImplicitThrowEvent(ThrowEvent):

    pass
class bpmn2_IntermediateThrowEvent(ThrowEvent):

    pass
class bpmn2_Extension:

    def __init__(self, mustUnderstand: bool, id: str, bpmn2_Extension: "bpmn2_ExtensionDefinition" = None, bpmn2_Extension476: "bpmn2_Definitions" = None):
        self.mustUnderstand = mustUnderstand
        self.id = id
        self.bpmn2_Extension = bpmn2_Extension
        self.bpmn2_Extension476 = bpmn2_Extension476
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def mustUnderstand(self) -> bool:
        return self.__mustUnderstand

    @mustUnderstand.setter
    def mustUnderstand(self, mustUnderstand: bool):
        self.__mustUnderstand = mustUnderstand

    @property
    def bpmn2_Extension476(self):
        return self.__bpmn2_Extension476

    @bpmn2_Extension476.setter
    def bpmn2_Extension476(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Extension__bpmn2_Extension476", None)
        self.__bpmn2_Extension476 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Definitions475"):
                opp_val = getattr(old_value, "bpmn2_Definitions475", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Definitions475"):
                opp_val = getattr(value, "bpmn2_Definitions475", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Definitions475", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Extension(self):
        return self.__bpmn2_Extension

    @bpmn2_Extension.setter
    def bpmn2_Extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Extension__bpmn2_Extension", None)
        self.__bpmn2_Extension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ExtensionDefinition332"):
                opp_val = getattr(old_value, "bpmn2_ExtensionDefinition332", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ExtensionDefinition332", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ExtensionDefinition332"):
                opp_val = getattr(value, "bpmn2_ExtensionDefinition332", None)
                setattr(value, "bpmn2_ExtensionDefinition332", self)

class Gateway:

    pass
class bpmn2_ExclusiveGateway(Gateway):

    pass
class bpmn2_ParallelGateway(Gateway):

    pass
class bpmn2_InclusiveGateway(Gateway):

    pass
class bpmn2_ComplexGateway(Gateway):

    pass
class bpmn2_EventBasedGateway(Gateway):

    def __init__(self, instantiate: bool, eventGatewayType: str):
        self.instantiate = instantiate
        self.eventGatewayType = eventGatewayType
        
    @property
    def eventGatewayType(self) -> str:
        return self.__eventGatewayType

    @eventGatewayType.setter
    def eventGatewayType(self, eventGatewayType: str):
        self.__eventGatewayType = eventGatewayType

    @property
    def instantiate(self) -> bool:
        return self.__instantiate

    @instantiate.setter
    def instantiate(self, instantiate: bool):
        self.__instantiate = instantiate

class HumanPerformer:

    pass
class bpmn2_PotentialOwner(HumanPerformer):

    pass
class Performer:

    pass
class bpmn2_HumanPerformer(Performer):

    pass
class DataAssociation:

    pass
class bpmn2_DataInputAssociation(DataAssociation):

    pass
class bpmn2_DataOutputAssociation(DataAssociation):

    pass
class Event:

    pass
class bpmn2_ThrowEvent(Event):

    pass
class bpmn2_CatchEvent(Event):

    def __init__(self, parallelMultiple: bool, bpmn2_CatchEvent: "bpmn2_OutputSet" = None, bpmn2_CatchEvent286: set["bpmn2_EventDefinition"] = None, bpmn2_CatchEvent288: set["bpmn2_DataOutputAssociation"] = None, bpmn2_CatchEvent291: set["bpmn2_DataOutput"] = None, bpmn2_CatchEvent294: set["bpmn2_EventDefinition"] = None):
        self.parallelMultiple = parallelMultiple
        self.bpmn2_CatchEvent = bpmn2_CatchEvent
        self.bpmn2_CatchEvent286 = bpmn2_CatchEvent286 if bpmn2_CatchEvent286 is not None else set()
        self.bpmn2_CatchEvent288 = bpmn2_CatchEvent288 if bpmn2_CatchEvent288 is not None else set()
        self.bpmn2_CatchEvent291 = bpmn2_CatchEvent291 if bpmn2_CatchEvent291 is not None else set()
        self.bpmn2_CatchEvent294 = bpmn2_CatchEvent294 if bpmn2_CatchEvent294 is not None else set()
        
    @property
    def parallelMultiple(self) -> bool:
        return self.__parallelMultiple

    @parallelMultiple.setter
    def parallelMultiple(self, parallelMultiple: bool):
        self.__parallelMultiple = parallelMultiple

    @property
    def bpmn2_CatchEvent294(self):
        return self.__bpmn2_CatchEvent294

    @bpmn2_CatchEvent294.setter
    def bpmn2_CatchEvent294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CatchEvent__bpmn2_CatchEvent294", None)
        self.__bpmn2_CatchEvent294 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_EventDefinition295"):
                    opp_val = getattr(item, "bpmn2_EventDefinition295", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_EventDefinition295", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_EventDefinition295"):
                    opp_val = getattr(item, "bpmn2_EventDefinition295", None)
                    
                    setattr(item, "bpmn2_EventDefinition295", self)
                    

    @property
    def bpmn2_CatchEvent286(self):
        return self.__bpmn2_CatchEvent286

    @bpmn2_CatchEvent286.setter
    def bpmn2_CatchEvent286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CatchEvent__bpmn2_CatchEvent286", None)
        self.__bpmn2_CatchEvent286 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_EventDefinition"):
                    opp_val = getattr(item, "bpmn2_EventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_EventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_EventDefinition"):
                    opp_val = getattr(item, "bpmn2_EventDefinition", None)
                    
                    setattr(item, "bpmn2_EventDefinition", self)
                    

    @property
    def bpmn2_CatchEvent(self):
        return self.__bpmn2_CatchEvent

    @bpmn2_CatchEvent.setter
    def bpmn2_CatchEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CatchEvent__bpmn2_CatchEvent", None)
        self.__bpmn2_CatchEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_OutputSet284"):
                opp_val = getattr(old_value, "bpmn2_OutputSet284", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_OutputSet284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_OutputSet284"):
                opp_val = getattr(value, "bpmn2_OutputSet284", None)
                setattr(value, "bpmn2_OutputSet284", self)

    @property
    def bpmn2_CatchEvent291(self):
        return self.__bpmn2_CatchEvent291

    @bpmn2_CatchEvent291.setter
    def bpmn2_CatchEvent291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CatchEvent__bpmn2_CatchEvent291", None)
        self.__bpmn2_CatchEvent291 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_DataOutput292"):
                    opp_val = getattr(item, "bpmn2_DataOutput292", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_DataOutput292", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_DataOutput292"):
                    opp_val = getattr(item, "bpmn2_DataOutput292", None)
                    
                    setattr(item, "bpmn2_DataOutput292", self)
                    

    @property
    def bpmn2_CatchEvent288(self):
        return self.__bpmn2_CatchEvent288

    @bpmn2_CatchEvent288.setter
    def bpmn2_CatchEvent288(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CatchEvent__bpmn2_CatchEvent288", None)
        self.__bpmn2_CatchEvent288 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_DataOutputAssociation289"):
                    opp_val = getattr(item, "bpmn2_DataOutputAssociation289", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_DataOutputAssociation289", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_DataOutputAssociation289"):
                    opp_val = getattr(item, "bpmn2_DataOutputAssociation289", None)
                    
                    setattr(item, "bpmn2_DataOutputAssociation289", self)
                    

class CatchEvent:

    pass
class bpmn2_StartEvent(CatchEvent):

    def __init__(self, isInterrupting: bool):
        self.isInterrupting = isInterrupting
        
    @property
    def isInterrupting(self) -> bool:
        return self.__isInterrupting

    @isInterrupting.setter
    def isInterrupting(self, isInterrupting: bool):
        self.__isInterrupting = isInterrupting

class bpmn2_IntermediateCatchEvent(CatchEvent):

    pass
class bpmn2_BoundaryEvent(CatchEvent):

    def __init__(self, cancelActivity: bool, boundaryEventRefs: "bpmn2_Activity" = None, BoundaryEvent: "bpmn2_Activity" = None):
        self.cancelActivity = cancelActivity
        self.boundaryEventRefs = boundaryEventRefs
        self.BoundaryEvent = BoundaryEvent
        
    @property
    def cancelActivity(self) -> bool:
        return self.__cancelActivity

    @cancelActivity.setter
    def cancelActivity(self, cancelActivity: bool):
        self.__cancelActivity = cancelActivity

    @property
    def BoundaryEvent(self):
        return self.__BoundaryEvent

    @BoundaryEvent.setter
    def BoundaryEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BoundaryEvent__BoundaryEvent", None)
        self.__BoundaryEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attachedToRef"):
                opp_val = getattr(old_value, "attachedToRef", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attachedToRef"):
                opp_val = getattr(value, "attachedToRef", None)
                if opp_val is None:
                    setattr(value, "attachedToRef", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def boundaryEventRefs(self):
        return self.__boundaryEventRefs

    @boundaryEventRefs.setter
    def boundaryEventRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BoundaryEvent__boundaryEventRefs", None)
        self.__boundaryEventRefs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Activity"):
                opp_val = getattr(old_value, "Activity", None)
                if opp_val == self:
                    setattr(old_value, "Activity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Activity"):
                opp_val = getattr(value, "Activity", None)
                setattr(value, "Activity", self)

class Expression:

    pass
class bpmn2_FormalExpression(Expression):

    def __init__(self, language: str, bpmn2_FormalExpression248: "bpmn2_EObject" = None, bpmn2_FormalExpression251: "bpmn2_ItemDefinition" = None, bpmn2_FormalExpression260: "bpmn2_CorrelationPropertyBinding" = None, bpmn2_FormalExpression: "bpmn2_CorrelationPropertyRetrievalExpression" = None, bpmn2_FormalExpression299: "bpmn2_DataAssociation" = None, bpmn2_FormalExpression450: "bpmn2_ComplexBehaviorDefinition" = None):
        self.language = language
        self.bpmn2_FormalExpression248 = bpmn2_FormalExpression248
        self.bpmn2_FormalExpression251 = bpmn2_FormalExpression251
        self.bpmn2_FormalExpression260 = bpmn2_FormalExpression260
        self.bpmn2_FormalExpression = bpmn2_FormalExpression
        self.bpmn2_FormalExpression299 = bpmn2_FormalExpression299
        self.bpmn2_FormalExpression450 = bpmn2_FormalExpression450
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def bpmn2_FormalExpression299(self):
        return self.__bpmn2_FormalExpression299

    @bpmn2_FormalExpression299.setter
    def bpmn2_FormalExpression299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FormalExpression__bpmn2_FormalExpression299", None)
        self.__bpmn2_FormalExpression299 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DataAssociation"):
                opp_val = getattr(old_value, "bpmn2_DataAssociation", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_DataAssociation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DataAssociation"):
                opp_val = getattr(value, "bpmn2_DataAssociation", None)
                setattr(value, "bpmn2_DataAssociation", self)

    @property
    def bpmn2_FormalExpression248(self):
        return self.__bpmn2_FormalExpression248

    @bpmn2_FormalExpression248.setter
    def bpmn2_FormalExpression248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FormalExpression__bpmn2_FormalExpression248", None)
        self.__bpmn2_FormalExpression248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_EObject249"):
                opp_val = getattr(old_value, "bpmn2_EObject249", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_EObject249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_EObject249"):
                opp_val = getattr(value, "bpmn2_EObject249", None)
                setattr(value, "bpmn2_EObject249", self)

    @property
    def bpmn2_FormalExpression251(self):
        return self.__bpmn2_FormalExpression251

    @bpmn2_FormalExpression251.setter
    def bpmn2_FormalExpression251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FormalExpression__bpmn2_FormalExpression251", None)
        self.__bpmn2_FormalExpression251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemDefinition252"):
                opp_val = getattr(old_value, "bpmn2_ItemDefinition252", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemDefinition252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemDefinition252"):
                opp_val = getattr(value, "bpmn2_ItemDefinition252", None)
                setattr(value, "bpmn2_ItemDefinition252", self)

    @property
    def bpmn2_FormalExpression260(self):
        return self.__bpmn2_FormalExpression260

    @bpmn2_FormalExpression260.setter
    def bpmn2_FormalExpression260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FormalExpression__bpmn2_FormalExpression260", None)
        self.__bpmn2_FormalExpression260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CorrelationPropertyBinding259"):
                opp_val = getattr(old_value, "bpmn2_CorrelationPropertyBinding259", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_CorrelationPropertyBinding259", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CorrelationPropertyBinding259"):
                opp_val = getattr(value, "bpmn2_CorrelationPropertyBinding259", None)
                setattr(value, "bpmn2_CorrelationPropertyBinding259", self)

    @property
    def bpmn2_FormalExpression450(self):
        return self.__bpmn2_FormalExpression450

    @bpmn2_FormalExpression450.setter
    def bpmn2_FormalExpression450(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FormalExpression__bpmn2_FormalExpression450", None)
        self.__bpmn2_FormalExpression450 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ComplexBehaviorDefinition449"):
                opp_val = getattr(old_value, "bpmn2_ComplexBehaviorDefinition449", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ComplexBehaviorDefinition449", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ComplexBehaviorDefinition449"):
                opp_val = getattr(value, "bpmn2_ComplexBehaviorDefinition449", None)
                setattr(value, "bpmn2_ComplexBehaviorDefinition449", self)

    @property
    def bpmn2_FormalExpression(self):
        return self.__bpmn2_FormalExpression

    @bpmn2_FormalExpression.setter
    def bpmn2_FormalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FormalExpression__bpmn2_FormalExpression", None)
        self.__bpmn2_FormalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CorrelationPropertyRetrievalExpression243"):
                opp_val = getattr(old_value, "bpmn2_CorrelationPropertyRetrievalExpression243", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_CorrelationPropertyRetrievalExpression243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CorrelationPropertyRetrievalExpression243"):
                opp_val = getattr(value, "bpmn2_CorrelationPropertyRetrievalExpression243", None)
                setattr(value, "bpmn2_CorrelationPropertyRetrievalExpression243", self)

class FlowNode:

    pass
class bpmn2_ChoreographyActivity(FlowNode):

    def __init__(self, loopType: str, bpmn2_ChoreographyActivity: set["bpmn2_Participant"] = None, bpmn2_ChoreographyActivity395: "bpmn2_Participant" = None, bpmn2_ChoreographyActivity398: set["bpmn2_CorrelationKey"] = None):
        self.loopType = loopType
        self.bpmn2_ChoreographyActivity = bpmn2_ChoreographyActivity if bpmn2_ChoreographyActivity is not None else set()
        self.bpmn2_ChoreographyActivity395 = bpmn2_ChoreographyActivity395
        self.bpmn2_ChoreographyActivity398 = bpmn2_ChoreographyActivity398 if bpmn2_ChoreographyActivity398 is not None else set()
        
    @property
    def loopType(self) -> str:
        return self.__loopType

    @loopType.setter
    def loopType(self, loopType: str):
        self.__loopType = loopType

    @property
    def bpmn2_ChoreographyActivity395(self):
        return self.__bpmn2_ChoreographyActivity395

    @bpmn2_ChoreographyActivity395.setter
    def bpmn2_ChoreographyActivity395(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ChoreographyActivity__bpmn2_ChoreographyActivity395", None)
        self.__bpmn2_ChoreographyActivity395 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Participant396"):
                opp_val = getattr(old_value, "bpmn2_Participant396", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Participant396", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Participant396"):
                opp_val = getattr(value, "bpmn2_Participant396", None)
                setattr(value, "bpmn2_Participant396", self)

    @property
    def bpmn2_ChoreographyActivity398(self):
        return self.__bpmn2_ChoreographyActivity398

    @bpmn2_ChoreographyActivity398.setter
    def bpmn2_ChoreographyActivity398(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ChoreographyActivity__bpmn2_ChoreographyActivity398", None)
        self.__bpmn2_ChoreographyActivity398 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_CorrelationKey399"):
                    opp_val = getattr(item, "bpmn2_CorrelationKey399", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_CorrelationKey399", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_CorrelationKey399"):
                    opp_val = getattr(item, "bpmn2_CorrelationKey399", None)
                    
                    setattr(item, "bpmn2_CorrelationKey399", self)
                    

    @property
    def bpmn2_ChoreographyActivity(self):
        return self.__bpmn2_ChoreographyActivity

    @bpmn2_ChoreographyActivity.setter
    def bpmn2_ChoreographyActivity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ChoreographyActivity__bpmn2_ChoreographyActivity", None)
        self.__bpmn2_ChoreographyActivity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Participant393"):
                    opp_val = getattr(item, "bpmn2_Participant393", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Participant393", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Participant393"):
                    opp_val = getattr(item, "bpmn2_Participant393", None)
                    
                    setattr(item, "bpmn2_Participant393", self)
                    

class bpmn2_Gateway(FlowNode):

    def __init__(self, gatewayDirection: str):
        self.gatewayDirection = gatewayDirection
        
    @property
    def gatewayDirection(self) -> str:
        return self.__gatewayDirection

    @gatewayDirection.setter
    def gatewayDirection(self, gatewayDirection: str):
        self.__gatewayDirection = gatewayDirection

class bpmn2_Activity(FlowNode):

    def __init__(self, isForCompensation: bool, startQuantity: int, completionQuantity: int, bpmn2_Activity: "bpmn2_LoopCharacteristics" = None, bpmn2_Activity266: set["bpmn2_ResourceRole"] = None, bpmn2_Activity269: "bpmn2_SequenceFlow" = None, bpmn2_Activity272: set["bpmn2_Property"] = None, bpmn2_Activity281: set["bpmn2_DataOutputAssociation"] = None, Activity: "bpmn2_BoundaryEvent" = None, bpmn2_Activity275: "bpmn2_InputOutputSpecification" = None, attachedToRef: set["bpmn2_BoundaryEvent"] = None, bpmn2_Activity279: set["bpmn2_DataInputAssociation"] = None, bpmn2_Activity354: "bpmn2_CompensateEventDefinition" = None):
        self.isForCompensation = isForCompensation
        self.startQuantity = startQuantity
        self.completionQuantity = completionQuantity
        self.bpmn2_Activity = bpmn2_Activity
        self.bpmn2_Activity266 = bpmn2_Activity266 if bpmn2_Activity266 is not None else set()
        self.bpmn2_Activity269 = bpmn2_Activity269
        self.bpmn2_Activity272 = bpmn2_Activity272 if bpmn2_Activity272 is not None else set()
        self.bpmn2_Activity281 = bpmn2_Activity281 if bpmn2_Activity281 is not None else set()
        self.Activity = Activity
        self.bpmn2_Activity275 = bpmn2_Activity275
        self.attachedToRef = attachedToRef if attachedToRef is not None else set()
        self.bpmn2_Activity279 = bpmn2_Activity279 if bpmn2_Activity279 is not None else set()
        self.bpmn2_Activity354 = bpmn2_Activity354
        
    @property
    def startQuantity(self) -> int:
        return self.__startQuantity

    @startQuantity.setter
    def startQuantity(self, startQuantity: int):
        self.__startQuantity = startQuantity

    @property
    def completionQuantity(self) -> int:
        return self.__completionQuantity

    @completionQuantity.setter
    def completionQuantity(self, completionQuantity: int):
        self.__completionQuantity = completionQuantity

    @property
    def isForCompensation(self) -> bool:
        return self.__isForCompensation

    @isForCompensation.setter
    def isForCompensation(self, isForCompensation: bool):
        self.__isForCompensation = isForCompensation

    @property
    def bpmn2_Activity275(self):
        return self.__bpmn2_Activity275

    @bpmn2_Activity275.setter
    def bpmn2_Activity275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity275", None)
        self.__bpmn2_Activity275 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_InputOutputSpecification276"):
                opp_val = getattr(old_value, "bpmn2_InputOutputSpecification276", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_InputOutputSpecification276", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_InputOutputSpecification276"):
                opp_val = getattr(value, "bpmn2_InputOutputSpecification276", None)
                setattr(value, "bpmn2_InputOutputSpecification276", self)

    @property
    def attachedToRef(self):
        return self.__attachedToRef

    @attachedToRef.setter
    def attachedToRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__attachedToRef", None)
        self.__attachedToRef = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BoundaryEvent"):
                    opp_val = getattr(item, "BoundaryEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "BoundaryEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BoundaryEvent"):
                    opp_val = getattr(item, "BoundaryEvent", None)
                    
                    setattr(item, "BoundaryEvent", self)
                    

    @property
    def bpmn2_Activity279(self):
        return self.__bpmn2_Activity279

    @bpmn2_Activity279.setter
    def bpmn2_Activity279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity279", None)
        self.__bpmn2_Activity279 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_DataInputAssociation"):
                    opp_val = getattr(item, "bpmn2_DataInputAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_DataInputAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_DataInputAssociation"):
                    opp_val = getattr(item, "bpmn2_DataInputAssociation", None)
                    
                    setattr(item, "bpmn2_DataInputAssociation", self)
                    

    @property
    def bpmn2_Activity269(self):
        return self.__bpmn2_Activity269

    @bpmn2_Activity269.setter
    def bpmn2_Activity269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity269", None)
        self.__bpmn2_Activity269 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_SequenceFlow270"):
                opp_val = getattr(old_value, "bpmn2_SequenceFlow270", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_SequenceFlow270", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_SequenceFlow270"):
                opp_val = getattr(value, "bpmn2_SequenceFlow270", None)
                setattr(value, "bpmn2_SequenceFlow270", self)

    @property
    def bpmn2_Activity266(self):
        return self.__bpmn2_Activity266

    @bpmn2_Activity266.setter
    def bpmn2_Activity266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity266", None)
        self.__bpmn2_Activity266 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_ResourceRole267"):
                    opp_val = getattr(item, "bpmn2_ResourceRole267", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_ResourceRole267", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_ResourceRole267"):
                    opp_val = getattr(item, "bpmn2_ResourceRole267", None)
                    
                    setattr(item, "bpmn2_ResourceRole267", self)
                    

    @property
    def Activity(self):
        return self.__Activity

    @Activity.setter
    def Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__Activity", None)
        self.__Activity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boundaryEventRefs"):
                opp_val = getattr(old_value, "boundaryEventRefs", None)
                if opp_val == self:
                    setattr(old_value, "boundaryEventRefs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boundaryEventRefs"):
                opp_val = getattr(value, "boundaryEventRefs", None)
                setattr(value, "boundaryEventRefs", self)

    @property
    def bpmn2_Activity354(self):
        return self.__bpmn2_Activity354

    @bpmn2_Activity354.setter
    def bpmn2_Activity354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity354", None)
        self.__bpmn2_Activity354 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CompensateEventDefinition"):
                opp_val = getattr(old_value, "bpmn2_CompensateEventDefinition", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_CompensateEventDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CompensateEventDefinition"):
                opp_val = getattr(value, "bpmn2_CompensateEventDefinition", None)
                setattr(value, "bpmn2_CompensateEventDefinition", self)

    @property
    def bpmn2_Activity(self):
        return self.__bpmn2_Activity

    @bpmn2_Activity.setter
    def bpmn2_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity", None)
        self.__bpmn2_Activity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_LoopCharacteristics"):
                opp_val = getattr(old_value, "bpmn2_LoopCharacteristics", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_LoopCharacteristics", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_LoopCharacteristics"):
                opp_val = getattr(value, "bpmn2_LoopCharacteristics", None)
                setattr(value, "bpmn2_LoopCharacteristics", self)

    @property
    def bpmn2_Activity281(self):
        return self.__bpmn2_Activity281

    @bpmn2_Activity281.setter
    def bpmn2_Activity281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity281", None)
        self.__bpmn2_Activity281 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_DataOutputAssociation"):
                    opp_val = getattr(item, "bpmn2_DataOutputAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_DataOutputAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_DataOutputAssociation"):
                    opp_val = getattr(item, "bpmn2_DataOutputAssociation", None)
                    
                    setattr(item, "bpmn2_DataOutputAssociation", self)
                    

    @property
    def bpmn2_Activity272(self):
        return self.__bpmn2_Activity272

    @bpmn2_Activity272.setter
    def bpmn2_Activity272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity272", None)
        self.__bpmn2_Activity272 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Property273"):
                    opp_val = getattr(item, "bpmn2_Property273", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Property273", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Property273"):
                    opp_val = getattr(item, "bpmn2_Property273", None)
                    
                    setattr(item, "bpmn2_Property273", self)
                    

class Activity:

    pass
class bpmn2_CallActivity(Activity):

    pass
class Task:

    pass
class bpmn2_BusinessRuleTask(Task):

    def __init__(self, implementation: str):
        self.implementation = implementation
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

class bpmn2_ReceiveTask(Task):

    def __init__(self, implementation: str, instantiate: bool, bpmn2_ReceiveTask: "bpmn2_Operation" = None, bpmn2_ReceiveTask468: "bpmn2_Message" = None):
        self.implementation = implementation
        self.instantiate = instantiate
        self.bpmn2_ReceiveTask = bpmn2_ReceiveTask
        self.bpmn2_ReceiveTask468 = bpmn2_ReceiveTask468
        
    @property
    def instantiate(self) -> bool:
        return self.__instantiate

    @instantiate.setter
    def instantiate(self, instantiate: bool):
        self.__instantiate = instantiate

    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def bpmn2_ReceiveTask(self):
        return self.__bpmn2_ReceiveTask

    @bpmn2_ReceiveTask.setter
    def bpmn2_ReceiveTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ReceiveTask__bpmn2_ReceiveTask", None)
        self.__bpmn2_ReceiveTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Operation466"):
                opp_val = getattr(old_value, "bpmn2_Operation466", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Operation466", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Operation466"):
                opp_val = getattr(value, "bpmn2_Operation466", None)
                setattr(value, "bpmn2_Operation466", self)

    @property
    def bpmn2_ReceiveTask468(self):
        return self.__bpmn2_ReceiveTask468

    @bpmn2_ReceiveTask468.setter
    def bpmn2_ReceiveTask468(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ReceiveTask__bpmn2_ReceiveTask468", None)
        self.__bpmn2_ReceiveTask468 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Message469"):
                opp_val = getattr(old_value, "bpmn2_Message469", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Message469", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Message469"):
                opp_val = getattr(value, "bpmn2_Message469", None)
                setattr(value, "bpmn2_Message469", self)

class bpmn2_ServiceTask(Task):

    def __init__(self, implementation: str, bpmn2_ServiceTask: "bpmn2_Operation" = None):
        self.implementation = implementation
        self.bpmn2_ServiceTask = bpmn2_ServiceTask
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def bpmn2_ServiceTask(self):
        return self.__bpmn2_ServiceTask

    @bpmn2_ServiceTask.setter
    def bpmn2_ServiceTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ServiceTask__bpmn2_ServiceTask", None)
        self.__bpmn2_ServiceTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Operation420"):
                opp_val = getattr(old_value, "bpmn2_Operation420", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Operation420", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Operation420"):
                opp_val = getattr(value, "bpmn2_Operation420", None)
                setattr(value, "bpmn2_Operation420", self)

class bpmn2_ScriptTask(Task):

    def __init__(self, scriptFormat: str, script: str):
        self.scriptFormat = scriptFormat
        self.script = script
        
    @property
    def script(self) -> str:
        return self.__script

    @script.setter
    def script(self, script: str):
        self.__script = script

    @property
    def scriptFormat(self) -> str:
        return self.__scriptFormat

    @scriptFormat.setter
    def scriptFormat(self, scriptFormat: str):
        self.__scriptFormat = scriptFormat

class bpmn2_UserTask(Task):

    def __init__(self, implementation: str, bpmn2_UserTask: set["bpmn2_Rendering"] = None):
        self.implementation = implementation
        self.bpmn2_UserTask = bpmn2_UserTask if bpmn2_UserTask is not None else set()
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def bpmn2_UserTask(self):
        return self.__bpmn2_UserTask

    @bpmn2_UserTask.setter
    def bpmn2_UserTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_UserTask__bpmn2_UserTask", None)
        self.__bpmn2_UserTask = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Rendering"):
                    opp_val = getattr(item, "bpmn2_Rendering", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Rendering", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Rendering"):
                    opp_val = getattr(item, "bpmn2_Rendering", None)
                    
                    setattr(item, "bpmn2_Rendering", self)
                    

class bpmn2_SendTask(Task):

    def __init__(self, implementation: str, bpmn2_SendTask: "bpmn2_Operation" = None, bpmn2_SendTask463: "bpmn2_Message" = None):
        self.implementation = implementation
        self.bpmn2_SendTask = bpmn2_SendTask
        self.bpmn2_SendTask463 = bpmn2_SendTask463
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def bpmn2_SendTask463(self):
        return self.__bpmn2_SendTask463

    @bpmn2_SendTask463.setter
    def bpmn2_SendTask463(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SendTask__bpmn2_SendTask463", None)
        self.__bpmn2_SendTask463 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Message464"):
                opp_val = getattr(old_value, "bpmn2_Message464", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Message464", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Message464"):
                opp_val = getattr(value, "bpmn2_Message464", None)
                setattr(value, "bpmn2_Message464", self)

    @property
    def bpmn2_SendTask(self):
        return self.__bpmn2_SendTask

    @bpmn2_SendTask.setter
    def bpmn2_SendTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SendTask__bpmn2_SendTask", None)
        self.__bpmn2_SendTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Operation461"):
                opp_val = getattr(old_value, "bpmn2_Operation461", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Operation461", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Operation461"):
                opp_val = getattr(value, "bpmn2_Operation461", None)
                setattr(value, "bpmn2_Operation461", self)

class bpmn2_ManualTask(Task):

    pass
class GlobalTask:

    pass
class bpmn2_GlobalBusinessRuleTask(GlobalTask):

    def __init__(self, implementation: str):
        self.implementation = implementation
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

class bpmn2_GlobalScriptTask(GlobalTask):

    def __init__(self, scriptLanguage: str, script: str):
        self.scriptLanguage = scriptLanguage
        self.script = script
        
    @property
    def script(self) -> str:
        return self.__script

    @script.setter
    def script(self, script: str):
        self.__script = script

    @property
    def scriptLanguage(self) -> str:
        return self.__scriptLanguage

    @scriptLanguage.setter
    def scriptLanguage(self, scriptLanguage: str):
        self.__scriptLanguage = scriptLanguage

class bpmn2_GlobalUserTask(GlobalTask):

    def __init__(self, implementation: str, bpmn2_GlobalUserTask: set["bpmn2_Rendering"] = None):
        self.implementation = implementation
        self.bpmn2_GlobalUserTask = bpmn2_GlobalUserTask if bpmn2_GlobalUserTask is not None else set()
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def bpmn2_GlobalUserTask(self):
        return self.__bpmn2_GlobalUserTask

    @bpmn2_GlobalUserTask.setter
    def bpmn2_GlobalUserTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_GlobalUserTask__bpmn2_GlobalUserTask", None)
        self.__bpmn2_GlobalUserTask = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Rendering316"):
                    opp_val = getattr(item, "bpmn2_Rendering316", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Rendering316", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Rendering316"):
                    opp_val = getattr(item, "bpmn2_Rendering316", None)
                    
                    setattr(item, "bpmn2_Rendering316", self)
                    

class bpmn2_GlobalManualTask(GlobalTask):

    pass
class bpmn2_InteractionNode(ABC):

    pass
class bpmn2_ParticipantMultiplicity:

    def __init__(self, minimum: int, maximum: int, id: str, bpmn2_ParticipantMultiplicity: "bpmn2_Participant" = None):
        self.minimum = minimum
        self.maximum = maximum
        self.id = id
        self.bpmn2_ParticipantMultiplicity = bpmn2_ParticipantMultiplicity
        
    @property
    def maximum(self) -> int:
        return self.__maximum

    @maximum.setter
    def maximum(self, maximum: int):
        self.__maximum = maximum

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def minimum(self) -> int:
        return self.__minimum

    @minimum.setter
    def minimum(self, minimum: int):
        self.__minimum = minimum

    @property
    def bpmn2_ParticipantMultiplicity(self):
        return self.__bpmn2_ParticipantMultiplicity

    @bpmn2_ParticipantMultiplicity.setter
    def bpmn2_ParticipantMultiplicity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ParticipantMultiplicity__bpmn2_ParticipantMultiplicity", None)
        self.__bpmn2_ParticipantMultiplicity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Participant192"):
                opp_val = getattr(old_value, "bpmn2_Participant192", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Participant192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Participant192"):
                opp_val = getattr(value, "bpmn2_Participant192", None)
                setattr(value, "bpmn2_Participant192", self)

class InteractionNode:

    pass
class bpmn2_Event(FlowNode, InteractionNode):

    pass
class bpmn2_Task(Activity, InteractionNode):

    pass
class Collaboration:

    pass
class bpmn2_GlobalConversation(Collaboration):

    pass
class FlowElement:

    pass
class bpmn2_SequenceFlow(FlowElement):

    def __init__(self, isImmediate: bool, SequenceFlow: "bpmn2_FlowNode" = None, SequenceFlow153: "bpmn2_FlowNode" = None, bpmn2_SequenceFlow: "bpmn2_Expression" = None, incoming: "bpmn2_FlowNode" = None, outgoing: "bpmn2_FlowNode" = None, bpmn2_SequenceFlow270: "bpmn2_Activity" = None, bpmn2_SequenceFlow321: "bpmn2_ComplexGateway" = None, bpmn2_SequenceFlow323: "bpmn2_ExclusiveGateway" = None, bpmn2_SequenceFlow325: "bpmn2_InclusiveGateway" = None):
        self.isImmediate = isImmediate
        self.SequenceFlow = SequenceFlow
        self.SequenceFlow153 = SequenceFlow153
        self.bpmn2_SequenceFlow = bpmn2_SequenceFlow
        self.incoming = incoming
        self.outgoing = outgoing
        self.bpmn2_SequenceFlow270 = bpmn2_SequenceFlow270
        self.bpmn2_SequenceFlow321 = bpmn2_SequenceFlow321
        self.bpmn2_SequenceFlow323 = bpmn2_SequenceFlow323
        self.bpmn2_SequenceFlow325 = bpmn2_SequenceFlow325
        
    @property
    def isImmediate(self) -> bool:
        return self.__isImmediate

    @isImmediate.setter
    def isImmediate(self, isImmediate: bool):
        self.__isImmediate = isImmediate

    @property
    def bpmn2_SequenceFlow321(self):
        return self.__bpmn2_SequenceFlow321

    @bpmn2_SequenceFlow321.setter
    def bpmn2_SequenceFlow321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SequenceFlow__bpmn2_SequenceFlow321", None)
        self.__bpmn2_SequenceFlow321 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ComplexGateway320"):
                opp_val = getattr(old_value, "bpmn2_ComplexGateway320", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ComplexGateway320", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ComplexGateway320"):
                opp_val = getattr(value, "bpmn2_ComplexGateway320", None)
                setattr(value, "bpmn2_ComplexGateway320", self)

    @property
    def SequenceFlow(self):
        return self.__SequenceFlow

    @SequenceFlow.setter
    def SequenceFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SequenceFlow__SequenceFlow", None)
        self.__SequenceFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceRef"):
                opp_val = getattr(old_value, "sourceRef", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceRef"):
                opp_val = getattr(value, "sourceRef", None)
                if opp_val is None:
                    setattr(value, "sourceRef", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SequenceFlow__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FlowNode160"):
                opp_val = getattr(old_value, "FlowNode160", None)
                if opp_val == self:
                    setattr(old_value, "FlowNode160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowNode160"):
                opp_val = getattr(value, "FlowNode160", None)
                setattr(value, "FlowNode160", self)

    @property
    def bpmn2_SequenceFlow323(self):
        return self.__bpmn2_SequenceFlow323

    @bpmn2_SequenceFlow323.setter
    def bpmn2_SequenceFlow323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SequenceFlow__bpmn2_SequenceFlow323", None)
        self.__bpmn2_SequenceFlow323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ExclusiveGateway"):
                opp_val = getattr(old_value, "bpmn2_ExclusiveGateway", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ExclusiveGateway", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ExclusiveGateway"):
                opp_val = getattr(value, "bpmn2_ExclusiveGateway", None)
                setattr(value, "bpmn2_ExclusiveGateway", self)

    @property
    def bpmn2_SequenceFlow325(self):
        return self.__bpmn2_SequenceFlow325

    @bpmn2_SequenceFlow325.setter
    def bpmn2_SequenceFlow325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SequenceFlow__bpmn2_SequenceFlow325", None)
        self.__bpmn2_SequenceFlow325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_InclusiveGateway"):
                opp_val = getattr(old_value, "bpmn2_InclusiveGateway", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_InclusiveGateway", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_InclusiveGateway"):
                opp_val = getattr(value, "bpmn2_InclusiveGateway", None)
                setattr(value, "bpmn2_InclusiveGateway", self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SequenceFlow__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FlowNode158"):
                opp_val = getattr(old_value, "FlowNode158", None)
                if opp_val == self:
                    setattr(old_value, "FlowNode158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowNode158"):
                opp_val = getattr(value, "FlowNode158", None)
                setattr(value, "FlowNode158", self)

    @property
    def bpmn2_SequenceFlow(self):
        return self.__bpmn2_SequenceFlow

    @bpmn2_SequenceFlow.setter
    def bpmn2_SequenceFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SequenceFlow__bpmn2_SequenceFlow", None)
        self.__bpmn2_SequenceFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Expression156"):
                opp_val = getattr(old_value, "bpmn2_Expression156", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Expression156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Expression156"):
                opp_val = getattr(value, "bpmn2_Expression156", None)
                setattr(value, "bpmn2_Expression156", self)

    @property
    def SequenceFlow153(self):
        return self.__SequenceFlow153

    @SequenceFlow153.setter
    def SequenceFlow153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SequenceFlow__SequenceFlow153", None)
        self.__SequenceFlow153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targetRef"):
                opp_val = getattr(old_value, "targetRef", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targetRef"):
                opp_val = getattr(value, "targetRef", None)
                if opp_val is None:
                    setattr(value, "targetRef", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_SequenceFlow270(self):
        return self.__bpmn2_SequenceFlow270

    @bpmn2_SequenceFlow270.setter
    def bpmn2_SequenceFlow270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SequenceFlow__bpmn2_SequenceFlow270", None)
        self.__bpmn2_SequenceFlow270 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Activity269"):
                opp_val = getattr(old_value, "bpmn2_Activity269", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Activity269", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Activity269"):
                opp_val = getattr(value, "bpmn2_Activity269", None)
                setattr(value, "bpmn2_Activity269", self)

class bpmn2_FlowNode(FlowElement):

    pass
class FlowElementsContainer:

    pass
class bpmn2_Choreography(Collaboration, FlowElementsContainer):

    pass
class bpmn2_SubProcess(Activity, FlowElementsContainer):

    def __init__(self, triggeredByEvent: bool, bpmn2_SubProcess: set["bpmn2_Artifact"] = None):
        self.triggeredByEvent = triggeredByEvent
        self.bpmn2_SubProcess = bpmn2_SubProcess if bpmn2_SubProcess is not None else set()
        
    @property
    def triggeredByEvent(self) -> bool:
        return self.__triggeredByEvent

    @triggeredByEvent.setter
    def triggeredByEvent(self, triggeredByEvent: bool):
        self.__triggeredByEvent = triggeredByEvent

    @property
    def bpmn2_SubProcess(self):
        return self.__bpmn2_SubProcess

    @bpmn2_SubProcess.setter
    def bpmn2_SubProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SubProcess__bpmn2_SubProcess", None)
        self.__bpmn2_SubProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Artifact422"):
                    opp_val = getattr(item, "bpmn2_Artifact422", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Artifact422", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Artifact422"):
                    opp_val = getattr(item, "bpmn2_Artifact422", None)
                    
                    setattr(item, "bpmn2_Artifact422", self)
                    

class bpmn2_SubChoreography(ChoreographyActivity, FlowElementsContainer):

    pass
class ResourceRole:

    pass
class bpmn2_Performer(ResourceRole):

    pass
class bpmn2_ResourceAssignmentExpression:

    def __init__(self, id: str, bpmn2_ResourceAssignmentExpression: "bpmn2_ResourceRole" = None, bpmn2_ResourceAssignmentExpression109: "bpmn2_Expression" = None):
        self.id = id
        self.bpmn2_ResourceAssignmentExpression = bpmn2_ResourceAssignmentExpression
        self.bpmn2_ResourceAssignmentExpression109 = bpmn2_ResourceAssignmentExpression109
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def bpmn2_ResourceAssignmentExpression109(self):
        return self.__bpmn2_ResourceAssignmentExpression109

    @bpmn2_ResourceAssignmentExpression109.setter
    def bpmn2_ResourceAssignmentExpression109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ResourceAssignmentExpression__bpmn2_ResourceAssignmentExpression109", None)
        self.__bpmn2_ResourceAssignmentExpression109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Expression110"):
                opp_val = getattr(old_value, "bpmn2_Expression110", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Expression110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Expression110"):
                opp_val = getattr(value, "bpmn2_Expression110", None)
                setattr(value, "bpmn2_Expression110", self)

    @property
    def bpmn2_ResourceAssignmentExpression(self):
        return self.__bpmn2_ResourceAssignmentExpression

    @bpmn2_ResourceAssignmentExpression.setter
    def bpmn2_ResourceAssignmentExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ResourceAssignmentExpression__bpmn2_ResourceAssignmentExpression", None)
        self.__bpmn2_ResourceAssignmentExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ResourceRole97"):
                opp_val = getattr(old_value, "bpmn2_ResourceRole97", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ResourceRole97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ResourceRole97"):
                opp_val = getattr(value, "bpmn2_ResourceRole97", None)
                setattr(value, "bpmn2_ResourceRole97", self)

class bpmn2_ResourceParameterBinding:

    def __init__(self, id: str, bpmn2_ResourceParameterBinding: "bpmn2_ResourceRole" = None, bpmn2_ResourceParameterBinding104: "bpmn2_Expression" = None, bpmn2_ResourceParameterBinding106: "bpmn2_ResourceParameter" = None):
        self.id = id
        self.bpmn2_ResourceParameterBinding = bpmn2_ResourceParameterBinding
        self.bpmn2_ResourceParameterBinding104 = bpmn2_ResourceParameterBinding104
        self.bpmn2_ResourceParameterBinding106 = bpmn2_ResourceParameterBinding106
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def bpmn2_ResourceParameterBinding(self):
        return self.__bpmn2_ResourceParameterBinding

    @bpmn2_ResourceParameterBinding.setter
    def bpmn2_ResourceParameterBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ResourceParameterBinding__bpmn2_ResourceParameterBinding", None)
        self.__bpmn2_ResourceParameterBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ResourceRole95"):
                opp_val = getattr(old_value, "bpmn2_ResourceRole95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ResourceRole95"):
                opp_val = getattr(value, "bpmn2_ResourceRole95", None)
                if opp_val is None:
                    setattr(value, "bpmn2_ResourceRole95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_ResourceParameterBinding104(self):
        return self.__bpmn2_ResourceParameterBinding104

    @bpmn2_ResourceParameterBinding104.setter
    def bpmn2_ResourceParameterBinding104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ResourceParameterBinding__bpmn2_ResourceParameterBinding104", None)
        self.__bpmn2_ResourceParameterBinding104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Expression"):
                opp_val = getattr(old_value, "bpmn2_Expression", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Expression"):
                opp_val = getattr(value, "bpmn2_Expression", None)
                setattr(value, "bpmn2_Expression", self)

    @property
    def bpmn2_ResourceParameterBinding106(self):
        return self.__bpmn2_ResourceParameterBinding106

    @bpmn2_ResourceParameterBinding106.setter
    def bpmn2_ResourceParameterBinding106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ResourceParameterBinding__bpmn2_ResourceParameterBinding106", None)
        self.__bpmn2_ResourceParameterBinding106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ResourceParameter107"):
                opp_val = getattr(old_value, "bpmn2_ResourceParameter107", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ResourceParameter107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ResourceParameter107"):
                opp_val = getattr(value, "bpmn2_ResourceParameter107", None)
                setattr(value, "bpmn2_ResourceParameter107", self)

class bpmn2_InputOutputBinding:

    def __init__(self, id: str, bpmn2_InputOutputBinding: "bpmn2_CallableElement" = None, bpmn2_InputOutputBinding84: "bpmn2_InputSet" = None, bpmn2_InputOutputBinding87: "bpmn2_OutputSet" = None, bpmn2_InputOutputBinding90: "bpmn2_Operation" = None):
        self.id = id
        self.bpmn2_InputOutputBinding = bpmn2_InputOutputBinding
        self.bpmn2_InputOutputBinding84 = bpmn2_InputOutputBinding84
        self.bpmn2_InputOutputBinding87 = bpmn2_InputOutputBinding87
        self.bpmn2_InputOutputBinding90 = bpmn2_InputOutputBinding90
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def bpmn2_InputOutputBinding87(self):
        return self.__bpmn2_InputOutputBinding87

    @bpmn2_InputOutputBinding87.setter
    def bpmn2_InputOutputBinding87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_InputOutputBinding__bpmn2_InputOutputBinding87", None)
        self.__bpmn2_InputOutputBinding87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_OutputSet88"):
                opp_val = getattr(old_value, "bpmn2_OutputSet88", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_OutputSet88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_OutputSet88"):
                opp_val = getattr(value, "bpmn2_OutputSet88", None)
                setattr(value, "bpmn2_OutputSet88", self)

    @property
    def bpmn2_InputOutputBinding84(self):
        return self.__bpmn2_InputOutputBinding84

    @bpmn2_InputOutputBinding84.setter
    def bpmn2_InputOutputBinding84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_InputOutputBinding__bpmn2_InputOutputBinding84", None)
        self.__bpmn2_InputOutputBinding84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_InputSet85"):
                opp_val = getattr(old_value, "bpmn2_InputSet85", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_InputSet85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_InputSet85"):
                opp_val = getattr(value, "bpmn2_InputSet85", None)
                setattr(value, "bpmn2_InputSet85", self)

    @property
    def bpmn2_InputOutputBinding90(self):
        return self.__bpmn2_InputOutputBinding90

    @bpmn2_InputOutputBinding90.setter
    def bpmn2_InputOutputBinding90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_InputOutputBinding__bpmn2_InputOutputBinding90", None)
        self.__bpmn2_InputOutputBinding90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Operation91"):
                opp_val = getattr(old_value, "bpmn2_Operation91", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Operation91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Operation91"):
                opp_val = getattr(value, "bpmn2_Operation91", None)
                setattr(value, "bpmn2_Operation91", self)

    @property
    def bpmn2_InputOutputBinding(self):
        return self.__bpmn2_InputOutputBinding

    @bpmn2_InputOutputBinding.setter
    def bpmn2_InputOutputBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_InputOutputBinding__bpmn2_InputOutputBinding", None)
        self.__bpmn2_InputOutputBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CallableElement44"):
                opp_val = getattr(old_value, "bpmn2_CallableElement44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CallableElement44"):
                opp_val = getattr(value, "bpmn2_CallableElement44", None)
                if opp_val is None:
                    setattr(value, "bpmn2_CallableElement44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ItemAwareElement:

    pass
class bpmn2_Property(ItemAwareElement):

    def __init__(self, name: str, bpmn2_Property: "bpmn2_Process" = None, bpmn2_Property273: "bpmn2_Activity" = None, bpmn2_Property297: "bpmn2_Event" = None):
        self.name = name
        self.bpmn2_Property = bpmn2_Property
        self.bpmn2_Property273 = bpmn2_Property273
        self.bpmn2_Property297 = bpmn2_Property297
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_Property297(self):
        return self.__bpmn2_Property297

    @bpmn2_Property297.setter
    def bpmn2_Property297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Property__bpmn2_Property297", None)
        self.__bpmn2_Property297 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Event"):
                opp_val = getattr(old_value, "bpmn2_Event", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Event"):
                opp_val = getattr(value, "bpmn2_Event", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Event", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Property273(self):
        return self.__bpmn2_Property273

    @bpmn2_Property273.setter
    def bpmn2_Property273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Property__bpmn2_Property273", None)
        self.__bpmn2_Property273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Activity272"):
                opp_val = getattr(old_value, "bpmn2_Activity272", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Activity272"):
                opp_val = getattr(value, "bpmn2_Activity272", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Activity272", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Property(self):
        return self.__bpmn2_Property

    @bpmn2_Property.setter
    def bpmn2_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Property__bpmn2_Property", None)
        self.__bpmn2_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Process115"):
                opp_val = getattr(old_value, "bpmn2_Process115", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Process115"):
                opp_val = getattr(value, "bpmn2_Process115", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Process115", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_DataObject(ItemAwareElement, FlowElement):

    def __init__(self, isCollection: bool, bpmn2_DataObject: "bpmn2_DataObjectReference" = None):
        self.isCollection = isCollection
        self.bpmn2_DataObject = bpmn2_DataObject
        
    @property
    def isCollection(self) -> bool:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: bool):
        self.__isCollection = isCollection

    @property
    def bpmn2_DataObject(self):
        return self.__bpmn2_DataObject

    @bpmn2_DataObject.setter
    def bpmn2_DataObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataObject__bpmn2_DataObject", None)
        self.__bpmn2_DataObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DataObjectReference"):
                opp_val = getattr(old_value, "bpmn2_DataObjectReference", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_DataObjectReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DataObjectReference"):
                opp_val = getattr(value, "bpmn2_DataObjectReference", None)
                setattr(value, "bpmn2_DataObjectReference", self)

class bpmn2_DataInput(ItemAwareElement):

    def __init__(self, name: str, isCollection: bool, DataInput: "bpmn2_InputSet" = None, DataInput55: "bpmn2_InputSet" = None, DataInput57: "bpmn2_InputSet" = None, optionalInputRefs: set["bpmn2_InputSet"] = None, whileExecutingInputRefs: set["bpmn2_InputSet"] = None, dataInputRefs: set["bpmn2_InputSet"] = None, bpmn2_DataInput: "bpmn2_InputOutputSpecification" = None, bpmn2_DataInput343: "bpmn2_ThrowEvent" = None, bpmn2_DataInput433: "bpmn2_MultiInstanceLoopCharacteristics" = None):
        self.name = name
        self.isCollection = isCollection
        self.DataInput = DataInput
        self.DataInput55 = DataInput55
        self.DataInput57 = DataInput57
        self.optionalInputRefs = optionalInputRefs if optionalInputRefs is not None else set()
        self.whileExecutingInputRefs = whileExecutingInputRefs if whileExecutingInputRefs is not None else set()
        self.dataInputRefs = dataInputRefs if dataInputRefs is not None else set()
        self.bpmn2_DataInput = bpmn2_DataInput
        self.bpmn2_DataInput343 = bpmn2_DataInput343
        self.bpmn2_DataInput433 = bpmn2_DataInput433
        
    @property
    def isCollection(self) -> bool:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: bool):
        self.__isCollection = isCollection

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def DataInput(self):
        return self.__DataInput

    @DataInput.setter
    def DataInput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataInput__DataInput", None)
        self.__DataInput = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inputSetRefs"):
                opp_val = getattr(old_value, "inputSetRefs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inputSetRefs"):
                opp_val = getattr(value, "inputSetRefs", None)
                if opp_val is None:
                    setattr(value, "inputSetRefs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DataInput55(self):
        return self.__DataInput55

    @DataInput55.setter
    def DataInput55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataInput__DataInput55", None)
        self.__DataInput55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inputSetWithOptional"):
                opp_val = getattr(old_value, "inputSetWithOptional", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inputSetWithOptional"):
                opp_val = getattr(value, "inputSetWithOptional", None)
                if opp_val is None:
                    setattr(value, "inputSetWithOptional", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataInputRefs(self):
        return self.__dataInputRefs

    @dataInputRefs.setter
    def dataInputRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataInput__dataInputRefs", None)
        self.__dataInputRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputSet64"):
                    opp_val = getattr(item, "InputSet64", None)
                    
                    if opp_val == self:
                        setattr(item, "InputSet64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputSet64"):
                    opp_val = getattr(item, "InputSet64", None)
                    
                    setattr(item, "InputSet64", self)
                    

    @property
    def bpmn2_DataInput(self):
        return self.__bpmn2_DataInput

    @bpmn2_DataInput.setter
    def bpmn2_DataInput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataInput__bpmn2_DataInput", None)
        self.__bpmn2_DataInput = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_InputOutputSpecification50"):
                opp_val = getattr(old_value, "bpmn2_InputOutputSpecification50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_InputOutputSpecification50"):
                opp_val = getattr(value, "bpmn2_InputOutputSpecification50", None)
                if opp_val is None:
                    setattr(value, "bpmn2_InputOutputSpecification50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DataInput57(self):
        return self.__DataInput57

    @DataInput57.setter
    def DataInput57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataInput__DataInput57", None)
        self.__DataInput57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inputSetWithWhileExecuting"):
                opp_val = getattr(old_value, "inputSetWithWhileExecuting", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inputSetWithWhileExecuting"):
                opp_val = getattr(value, "inputSetWithWhileExecuting", None)
                if opp_val is None:
                    setattr(value, "inputSetWithWhileExecuting", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_DataInput343(self):
        return self.__bpmn2_DataInput343

    @bpmn2_DataInput343.setter
    def bpmn2_DataInput343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataInput__bpmn2_DataInput343", None)
        self.__bpmn2_DataInput343 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ThrowEvent342"):
                opp_val = getattr(old_value, "bpmn2_ThrowEvent342", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ThrowEvent342"):
                opp_val = getattr(value, "bpmn2_ThrowEvent342", None)
                if opp_val is None:
                    setattr(value, "bpmn2_ThrowEvent342", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def optionalInputRefs(self):
        return self.__optionalInputRefs

    @optionalInputRefs.setter
    def optionalInputRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataInput__optionalInputRefs", None)
        self.__optionalInputRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputSet"):
                    opp_val = getattr(item, "InputSet", None)
                    
                    if opp_val == self:
                        setattr(item, "InputSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputSet"):
                    opp_val = getattr(item, "InputSet", None)
                    
                    setattr(item, "InputSet", self)
                    

    @property
    def whileExecutingInputRefs(self):
        return self.__whileExecutingInputRefs

    @whileExecutingInputRefs.setter
    def whileExecutingInputRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataInput__whileExecutingInputRefs", None)
        self.__whileExecutingInputRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputSet62"):
                    opp_val = getattr(item, "InputSet62", None)
                    
                    if opp_val == self:
                        setattr(item, "InputSet62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputSet62"):
                    opp_val = getattr(item, "InputSet62", None)
                    
                    setattr(item, "InputSet62", self)
                    

    @property
    def bpmn2_DataInput433(self):
        return self.__bpmn2_DataInput433

    @bpmn2_DataInput433.setter
    def bpmn2_DataInput433(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataInput__bpmn2_DataInput433", None)
        self.__bpmn2_DataInput433 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_MultiInstanceLoopCharacteristics432"):
                opp_val = getattr(old_value, "bpmn2_MultiInstanceLoopCharacteristics432", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_MultiInstanceLoopCharacteristics432", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_MultiInstanceLoopCharacteristics432"):
                opp_val = getattr(value, "bpmn2_MultiInstanceLoopCharacteristics432", None)
                setattr(value, "bpmn2_MultiInstanceLoopCharacteristics432", self)

class bpmn2_DataObjectReference(ItemAwareElement, FlowElement):

    pass
class bpmn2_DataStoreReference(ItemAwareElement, FlowElement):

    pass
class bpmn2_DataOutput(ItemAwareElement):

    def __init__(self, name: str, isCollection: bool, bpmn2_DataOutput: "bpmn2_InputOutputSpecification" = None, DataOutput: "bpmn2_OutputSet" = None, DataOutput71: "bpmn2_OutputSet" = None, optionalOutputRefs: set["bpmn2_OutputSet"] = None, whileExecutingOutputRefs: set["bpmn2_OutputSet"] = None, dataOutputRefs: set["bpmn2_OutputSet"] = None, DataOutput73: "bpmn2_OutputSet" = None, bpmn2_DataOutput292: "bpmn2_CatchEvent" = None, bpmn2_DataOutput436: "bpmn2_MultiInstanceLoopCharacteristics" = None):
        self.name = name
        self.isCollection = isCollection
        self.bpmn2_DataOutput = bpmn2_DataOutput
        self.DataOutput = DataOutput
        self.DataOutput71 = DataOutput71
        self.optionalOutputRefs = optionalOutputRefs if optionalOutputRefs is not None else set()
        self.whileExecutingOutputRefs = whileExecutingOutputRefs if whileExecutingOutputRefs is not None else set()
        self.dataOutputRefs = dataOutputRefs if dataOutputRefs is not None else set()
        self.DataOutput73 = DataOutput73
        self.bpmn2_DataOutput292 = bpmn2_DataOutput292
        self.bpmn2_DataOutput436 = bpmn2_DataOutput436
        
    @property
    def isCollection(self) -> bool:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: bool):
        self.__isCollection = isCollection

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def whileExecutingOutputRefs(self):
        return self.__whileExecutingOutputRefs

    @whileExecutingOutputRefs.setter
    def whileExecutingOutputRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataOutput__whileExecutingOutputRefs", None)
        self.__whileExecutingOutputRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputSet80"):
                    opp_val = getattr(item, "OutputSet80", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputSet80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputSet80"):
                    opp_val = getattr(item, "OutputSet80", None)
                    
                    setattr(item, "OutputSet80", self)
                    

    @property
    def bpmn2_DataOutput(self):
        return self.__bpmn2_DataOutput

    @bpmn2_DataOutput.setter
    def bpmn2_DataOutput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataOutput__bpmn2_DataOutput", None)
        self.__bpmn2_DataOutput = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_InputOutputSpecification52"):
                opp_val = getattr(old_value, "bpmn2_InputOutputSpecification52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_InputOutputSpecification52"):
                opp_val = getattr(value, "bpmn2_InputOutputSpecification52", None)
                if opp_val is None:
                    setattr(value, "bpmn2_InputOutputSpecification52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_DataOutput436(self):
        return self.__bpmn2_DataOutput436

    @bpmn2_DataOutput436.setter
    def bpmn2_DataOutput436(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataOutput__bpmn2_DataOutput436", None)
        self.__bpmn2_DataOutput436 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_MultiInstanceLoopCharacteristics435"):
                opp_val = getattr(old_value, "bpmn2_MultiInstanceLoopCharacteristics435", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_MultiInstanceLoopCharacteristics435", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_MultiInstanceLoopCharacteristics435"):
                opp_val = getattr(value, "bpmn2_MultiInstanceLoopCharacteristics435", None)
                setattr(value, "bpmn2_MultiInstanceLoopCharacteristics435", self)

    @property
    def DataOutput73(self):
        return self.__DataOutput73

    @DataOutput73.setter
    def DataOutput73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataOutput__DataOutput73", None)
        self.__DataOutput73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outputSetWithWhileExecuting"):
                opp_val = getattr(old_value, "outputSetWithWhileExecuting", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outputSetWithWhileExecuting"):
                opp_val = getattr(value, "outputSetWithWhileExecuting", None)
                if opp_val is None:
                    setattr(value, "outputSetWithWhileExecuting", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_DataOutput292(self):
        return self.__bpmn2_DataOutput292

    @bpmn2_DataOutput292.setter
    def bpmn2_DataOutput292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataOutput__bpmn2_DataOutput292", None)
        self.__bpmn2_DataOutput292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CatchEvent291"):
                opp_val = getattr(old_value, "bpmn2_CatchEvent291", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CatchEvent291"):
                opp_val = getattr(value, "bpmn2_CatchEvent291", None)
                if opp_val is None:
                    setattr(value, "bpmn2_CatchEvent291", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def optionalOutputRefs(self):
        return self.__optionalOutputRefs

    @optionalOutputRefs.setter
    def optionalOutputRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataOutput__optionalOutputRefs", None)
        self.__optionalOutputRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputSet78"):
                    opp_val = getattr(item, "OutputSet78", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputSet78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputSet78"):
                    opp_val = getattr(item, "OutputSet78", None)
                    
                    setattr(item, "OutputSet78", self)
                    

    @property
    def dataOutputRefs(self):
        return self.__dataOutputRefs

    @dataOutputRefs.setter
    def dataOutputRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataOutput__dataOutputRefs", None)
        self.__dataOutputRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputSet82"):
                    opp_val = getattr(item, "OutputSet82", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputSet82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputSet82"):
                    opp_val = getattr(item, "OutputSet82", None)
                    
                    setattr(item, "OutputSet82", self)
                    

    @property
    def DataOutput(self):
        return self.__DataOutput

    @DataOutput.setter
    def DataOutput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataOutput__DataOutput", None)
        self.__DataOutput = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outputSetRefs"):
                opp_val = getattr(old_value, "outputSetRefs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outputSetRefs"):
                opp_val = getattr(value, "outputSetRefs", None)
                if opp_val is None:
                    setattr(value, "outputSetRefs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DataOutput71(self):
        return self.__DataOutput71

    @DataOutput71.setter
    def DataOutput71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataOutput__DataOutput71", None)
        self.__DataOutput71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outputSetWithOptional"):
                opp_val = getattr(old_value, "outputSetWithOptional", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outputSetWithOptional"):
                opp_val = getattr(value, "outputSetWithOptional", None)
                if opp_val is None:
                    setattr(value, "outputSetWithOptional", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CallableElement:

    pass
class bpmn2_Process(FlowElementsContainer, CallableElement):

    def __init__(self, processType: str, isClosed: bool, isExecutable: bool, bpmn2_Process: "bpmn2_Auditing" = None, bpmn2_Process113: "bpmn2_Monitoring" = None, bpmn2_Process115: set["bpmn2_Property"] = None, bpmn2_Process118: "bpmn2_Process" = None, bpmn2_Process116: set["bpmn2_Process"] = None, bpmn2_Process120: "bpmn2_Collaboration" = None, bpmn2_Process122: set["bpmn2_ResourceRole"] = None, bpmn2_Process125: set["bpmn2_Artifact"] = None, bpmn2_Process127: set["bpmn2_CorrelationSubscription"] = None, bpmn2_Process197: "bpmn2_Participant" = None):
        self.processType = processType
        self.isClosed = isClosed
        self.isExecutable = isExecutable
        self.bpmn2_Process = bpmn2_Process
        self.bpmn2_Process113 = bpmn2_Process113
        self.bpmn2_Process115 = bpmn2_Process115 if bpmn2_Process115 is not None else set()
        self.bpmn2_Process118 = bpmn2_Process118
        self.bpmn2_Process116 = bpmn2_Process116 if bpmn2_Process116 is not None else set()
        self.bpmn2_Process120 = bpmn2_Process120
        self.bpmn2_Process122 = bpmn2_Process122 if bpmn2_Process122 is not None else set()
        self.bpmn2_Process125 = bpmn2_Process125 if bpmn2_Process125 is not None else set()
        self.bpmn2_Process127 = bpmn2_Process127 if bpmn2_Process127 is not None else set()
        self.bpmn2_Process197 = bpmn2_Process197
        
    @property
    def processType(self) -> str:
        return self.__processType

    @processType.setter
    def processType(self, processType: str):
        self.__processType = processType

    @property
    def isExecutable(self) -> bool:
        return self.__isExecutable

    @isExecutable.setter
    def isExecutable(self, isExecutable: bool):
        self.__isExecutable = isExecutable

    @property
    def isClosed(self) -> bool:
        return self.__isClosed

    @isClosed.setter
    def isClosed(self, isClosed: bool):
        self.__isClosed = isClosed

    @property
    def bpmn2_Process(self):
        return self.__bpmn2_Process

    @bpmn2_Process.setter
    def bpmn2_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process", None)
        self.__bpmn2_Process = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Auditing"):
                opp_val = getattr(old_value, "bpmn2_Auditing", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Auditing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Auditing"):
                opp_val = getattr(value, "bpmn2_Auditing", None)
                setattr(value, "bpmn2_Auditing", self)

    @property
    def bpmn2_Process197(self):
        return self.__bpmn2_Process197

    @bpmn2_Process197.setter
    def bpmn2_Process197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process197", None)
        self.__bpmn2_Process197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Participant196"):
                opp_val = getattr(old_value, "bpmn2_Participant196", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Participant196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Participant196"):
                opp_val = getattr(value, "bpmn2_Participant196", None)
                setattr(value, "bpmn2_Participant196", self)

    @property
    def bpmn2_Process115(self):
        return self.__bpmn2_Process115

    @bpmn2_Process115.setter
    def bpmn2_Process115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process115", None)
        self.__bpmn2_Process115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Property"):
                    opp_val = getattr(item, "bpmn2_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Property"):
                    opp_val = getattr(item, "bpmn2_Property", None)
                    
                    setattr(item, "bpmn2_Property", self)
                    

    @property
    def bpmn2_Process113(self):
        return self.__bpmn2_Process113

    @bpmn2_Process113.setter
    def bpmn2_Process113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process113", None)
        self.__bpmn2_Process113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Monitoring"):
                opp_val = getattr(old_value, "bpmn2_Monitoring", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Monitoring", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Monitoring"):
                opp_val = getattr(value, "bpmn2_Monitoring", None)
                setattr(value, "bpmn2_Monitoring", self)

    @property
    def bpmn2_Process127(self):
        return self.__bpmn2_Process127

    @bpmn2_Process127.setter
    def bpmn2_Process127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process127", None)
        self.__bpmn2_Process127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_CorrelationSubscription"):
                    opp_val = getattr(item, "bpmn2_CorrelationSubscription", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_CorrelationSubscription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_CorrelationSubscription"):
                    opp_val = getattr(item, "bpmn2_CorrelationSubscription", None)
                    
                    setattr(item, "bpmn2_CorrelationSubscription", self)
                    

    @property
    def bpmn2_Process116(self):
        return self.__bpmn2_Process116

    @bpmn2_Process116.setter
    def bpmn2_Process116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process116", None)
        self.__bpmn2_Process116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Process118"):
                    opp_val = getattr(item, "bpmn2_Process118", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Process118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Process118"):
                    opp_val = getattr(item, "bpmn2_Process118", None)
                    
                    setattr(item, "bpmn2_Process118", self)
                    

    @property
    def bpmn2_Process125(self):
        return self.__bpmn2_Process125

    @bpmn2_Process125.setter
    def bpmn2_Process125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process125", None)
        self.__bpmn2_Process125 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Artifact"):
                    opp_val = getattr(item, "bpmn2_Artifact", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Artifact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Artifact"):
                    opp_val = getattr(item, "bpmn2_Artifact", None)
                    
                    setattr(item, "bpmn2_Artifact", self)
                    

    @property
    def bpmn2_Process118(self):
        return self.__bpmn2_Process118

    @bpmn2_Process118.setter
    def bpmn2_Process118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process118", None)
        self.__bpmn2_Process118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Process116"):
                opp_val = getattr(old_value, "bpmn2_Process116", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Process116"):
                opp_val = getattr(value, "bpmn2_Process116", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Process116", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Process122(self):
        return self.__bpmn2_Process122

    @bpmn2_Process122.setter
    def bpmn2_Process122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process122", None)
        self.__bpmn2_Process122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_ResourceRole123"):
                    opp_val = getattr(item, "bpmn2_ResourceRole123", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_ResourceRole123", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_ResourceRole123"):
                    opp_val = getattr(item, "bpmn2_ResourceRole123", None)
                    
                    setattr(item, "bpmn2_ResourceRole123", self)
                    

    @property
    def bpmn2_Process120(self):
        return self.__bpmn2_Process120

    @bpmn2_Process120.setter
    def bpmn2_Process120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process120", None)
        self.__bpmn2_Process120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Collaboration"):
                opp_val = getattr(old_value, "bpmn2_Collaboration", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Collaboration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Collaboration"):
                opp_val = getattr(value, "bpmn2_Collaboration", None)
                setattr(value, "bpmn2_Collaboration", self)

class bpmn2_GlobalTask(CallableElement):

    pass
class bpmn2_Import:

    def __init__(self, importType: str, location: str, namespace: str, id: str, bpmn2_Import: "bpmn2_ItemDefinition" = None, bpmn2_Import473: "bpmn2_Definitions" = None):
        self.importType = importType
        self.location = location
        self.namespace = namespace
        self.id = id
        self.bpmn2_Import = bpmn2_Import
        self.bpmn2_Import473 = bpmn2_Import473
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def importType(self) -> str:
        return self.__importType

    @importType.setter
    def importType(self, importType: str):
        self.__importType = importType

    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def bpmn2_Import473(self):
        return self.__bpmn2_Import473

    @bpmn2_Import473.setter
    def bpmn2_Import473(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Import__bpmn2_Import473", None)
        self.__bpmn2_Import473 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Definitions"):
                opp_val = getattr(old_value, "bpmn2_Definitions", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Definitions"):
                opp_val = getattr(value, "bpmn2_Definitions", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Definitions", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Import(self):
        return self.__bpmn2_Import

    @bpmn2_Import.setter
    def bpmn2_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Import__bpmn2_Import", None)
        self.__bpmn2_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemDefinition34"):
                opp_val = getattr(old_value, "bpmn2_ItemDefinition34", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemDefinition34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemDefinition34"):
                opp_val = getattr(value, "bpmn2_ItemDefinition34", None)
                setattr(value, "bpmn2_ItemDefinition34", self)

class RootElement:

    pass
class bpmn2_Message(RootElement):

    def __init__(self, name: str, bpmn2_Message29: "bpmn2_ItemDefinition" = None, bpmn2_Message: "bpmn2_Operation" = None, bpmn2_Message22: "bpmn2_Operation" = None, bpmn2_Message219: "bpmn2_MessageFlow" = None, bpmn2_Message246: "bpmn2_CorrelationPropertyRetrievalExpression" = None, bpmn2_Message369: "bpmn2_MessageEventDefinition" = None, bpmn2_Message464: "bpmn2_SendTask" = None, bpmn2_Message469: "bpmn2_ReceiveTask" = None):
        self.name = name
        self.bpmn2_Message29 = bpmn2_Message29
        self.bpmn2_Message = bpmn2_Message
        self.bpmn2_Message22 = bpmn2_Message22
        self.bpmn2_Message219 = bpmn2_Message219
        self.bpmn2_Message246 = bpmn2_Message246
        self.bpmn2_Message369 = bpmn2_Message369
        self.bpmn2_Message464 = bpmn2_Message464
        self.bpmn2_Message469 = bpmn2_Message469
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_Message469(self):
        return self.__bpmn2_Message469

    @bpmn2_Message469.setter
    def bpmn2_Message469(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Message__bpmn2_Message469", None)
        self.__bpmn2_Message469 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ReceiveTask468"):
                opp_val = getattr(old_value, "bpmn2_ReceiveTask468", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ReceiveTask468", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ReceiveTask468"):
                opp_val = getattr(value, "bpmn2_ReceiveTask468", None)
                setattr(value, "bpmn2_ReceiveTask468", self)

    @property
    def bpmn2_Message369(self):
        return self.__bpmn2_Message369

    @bpmn2_Message369.setter
    def bpmn2_Message369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Message__bpmn2_Message369", None)
        self.__bpmn2_Message369 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_MessageEventDefinition"):
                opp_val = getattr(old_value, "bpmn2_MessageEventDefinition", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_MessageEventDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_MessageEventDefinition"):
                opp_val = getattr(value, "bpmn2_MessageEventDefinition", None)
                setattr(value, "bpmn2_MessageEventDefinition", self)

    @property
    def bpmn2_Message219(self):
        return self.__bpmn2_Message219

    @bpmn2_Message219.setter
    def bpmn2_Message219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Message__bpmn2_Message219", None)
        self.__bpmn2_Message219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_MessageFlow218"):
                opp_val = getattr(old_value, "bpmn2_MessageFlow218", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_MessageFlow218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_MessageFlow218"):
                opp_val = getattr(value, "bpmn2_MessageFlow218", None)
                setattr(value, "bpmn2_MessageFlow218", self)

    @property
    def bpmn2_Message(self):
        return self.__bpmn2_Message

    @bpmn2_Message.setter
    def bpmn2_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Message__bpmn2_Message", None)
        self.__bpmn2_Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Operation19"):
                opp_val = getattr(old_value, "bpmn2_Operation19", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Operation19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Operation19"):
                opp_val = getattr(value, "bpmn2_Operation19", None)
                setattr(value, "bpmn2_Operation19", self)

    @property
    def bpmn2_Message29(self):
        return self.__bpmn2_Message29

    @bpmn2_Message29.setter
    def bpmn2_Message29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Message__bpmn2_Message29", None)
        self.__bpmn2_Message29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemDefinition"):
                opp_val = getattr(old_value, "bpmn2_ItemDefinition", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemDefinition"):
                opp_val = getattr(value, "bpmn2_ItemDefinition", None)
                setattr(value, "bpmn2_ItemDefinition", self)

    @property
    def bpmn2_Message22(self):
        return self.__bpmn2_Message22

    @bpmn2_Message22.setter
    def bpmn2_Message22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Message__bpmn2_Message22", None)
        self.__bpmn2_Message22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Operation21"):
                opp_val = getattr(old_value, "bpmn2_Operation21", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Operation21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Operation21"):
                opp_val = getattr(value, "bpmn2_Operation21", None)
                setattr(value, "bpmn2_Operation21", self)

    @property
    def bpmn2_Message246(self):
        return self.__bpmn2_Message246

    @bpmn2_Message246.setter
    def bpmn2_Message246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Message__bpmn2_Message246", None)
        self.__bpmn2_Message246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CorrelationPropertyRetrievalExpression245"):
                opp_val = getattr(old_value, "bpmn2_CorrelationPropertyRetrievalExpression245", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_CorrelationPropertyRetrievalExpression245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CorrelationPropertyRetrievalExpression245"):
                opp_val = getattr(value, "bpmn2_CorrelationPropertyRetrievalExpression245", None)
                setattr(value, "bpmn2_CorrelationPropertyRetrievalExpression245", self)

    @property
    def bpmn2_Message464(self):
        return self.__bpmn2_Message464

    @bpmn2_Message464.setter
    def bpmn2_Message464(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Message__bpmn2_Message464", None)
        self.__bpmn2_Message464 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_SendTask463"):
                opp_val = getattr(old_value, "bpmn2_SendTask463", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_SendTask463", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_SendTask463"):
                opp_val = getattr(value, "bpmn2_SendTask463", None)
                setattr(value, "bpmn2_SendTask463", self)

class bpmn2_EndPoint(RootElement):

    pass
class bpmn2_CallableElement(RootElement):

    def __init__(self, name: str, bpmn2_CallableElement: "bpmn2_InputOutputSpecification" = None, bpmn2_CallableElement41: set["bpmn2_Interface"] = None, bpmn2_CallableElement44: set["bpmn2_InputOutputBinding"] = None, bpmn2_CallableElement459: "bpmn2_CallActivity" = None):
        self.name = name
        self.bpmn2_CallableElement = bpmn2_CallableElement
        self.bpmn2_CallableElement41 = bpmn2_CallableElement41 if bpmn2_CallableElement41 is not None else set()
        self.bpmn2_CallableElement44 = bpmn2_CallableElement44 if bpmn2_CallableElement44 is not None else set()
        self.bpmn2_CallableElement459 = bpmn2_CallableElement459
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_CallableElement41(self):
        return self.__bpmn2_CallableElement41

    @bpmn2_CallableElement41.setter
    def bpmn2_CallableElement41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CallableElement__bpmn2_CallableElement41", None)
        self.__bpmn2_CallableElement41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Interface42"):
                    opp_val = getattr(item, "bpmn2_Interface42", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Interface42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Interface42"):
                    opp_val = getattr(item, "bpmn2_Interface42", None)
                    
                    setattr(item, "bpmn2_Interface42", self)
                    

    @property
    def bpmn2_CallableElement459(self):
        return self.__bpmn2_CallableElement459

    @bpmn2_CallableElement459.setter
    def bpmn2_CallableElement459(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CallableElement__bpmn2_CallableElement459", None)
        self.__bpmn2_CallableElement459 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CallActivity"):
                opp_val = getattr(old_value, "bpmn2_CallActivity", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_CallActivity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CallActivity"):
                opp_val = getattr(value, "bpmn2_CallActivity", None)
                setattr(value, "bpmn2_CallActivity", self)

    @property
    def bpmn2_CallableElement44(self):
        return self.__bpmn2_CallableElement44

    @bpmn2_CallableElement44.setter
    def bpmn2_CallableElement44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CallableElement__bpmn2_CallableElement44", None)
        self.__bpmn2_CallableElement44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_InputOutputBinding"):
                    opp_val = getattr(item, "bpmn2_InputOutputBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_InputOutputBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_InputOutputBinding"):
                    opp_val = getattr(item, "bpmn2_InputOutputBinding", None)
                    
                    setattr(item, "bpmn2_InputOutputBinding", self)
                    

    @property
    def bpmn2_CallableElement(self):
        return self.__bpmn2_CallableElement

    @bpmn2_CallableElement.setter
    def bpmn2_CallableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CallableElement__bpmn2_CallableElement", None)
        self.__bpmn2_CallableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_InputOutputSpecification"):
                opp_val = getattr(old_value, "bpmn2_InputOutputSpecification", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_InputOutputSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_InputOutputSpecification"):
                opp_val = getattr(value, "bpmn2_InputOutputSpecification", None)
                setattr(value, "bpmn2_InputOutputSpecification", self)

class bpmn2_Category(RootElement):

    def __init__(self, name: str, bpmn2_Category: set["bpmn2_CategoryValue"] = None):
        self.name = name
        self.bpmn2_Category = bpmn2_Category if bpmn2_Category is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_Category(self):
        return self.__bpmn2_Category

    @bpmn2_Category.setter
    def bpmn2_Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Category__bpmn2_Category", None)
        self.__bpmn2_Category = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_CategoryValue418"):
                    opp_val = getattr(item, "bpmn2_CategoryValue418", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_CategoryValue418", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_CategoryValue418"):
                    opp_val = getattr(item, "bpmn2_CategoryValue418", None)
                    
                    setattr(item, "bpmn2_CategoryValue418", self)
                    

class bpmn2_PartnerEntity(RootElement):

    def __init__(self, name: str, bpmn2_PartnerEntity: set["bpmn2_Participant"] = None):
        self.name = name
        self.bpmn2_PartnerEntity = bpmn2_PartnerEntity if bpmn2_PartnerEntity is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_PartnerEntity(self):
        return self.__bpmn2_PartnerEntity

    @bpmn2_PartnerEntity.setter
    def bpmn2_PartnerEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_PartnerEntity__bpmn2_PartnerEntity", None)
        self.__bpmn2_PartnerEntity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Participant389"):
                    opp_val = getattr(item, "bpmn2_Participant389", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Participant389", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Participant389"):
                    opp_val = getattr(item, "bpmn2_Participant389", None)
                    
                    setattr(item, "bpmn2_Participant389", self)
                    

class bpmn2_PartnerRole(RootElement):

    def __init__(self, name: str, bpmn2_PartnerRole: set["bpmn2_Participant"] = None):
        self.name = name
        self.bpmn2_PartnerRole = bpmn2_PartnerRole if bpmn2_PartnerRole is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_PartnerRole(self):
        return self.__bpmn2_PartnerRole

    @bpmn2_PartnerRole.setter
    def bpmn2_PartnerRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_PartnerRole__bpmn2_PartnerRole", None)
        self.__bpmn2_PartnerRole = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Participant391"):
                    opp_val = getattr(item, "bpmn2_Participant391", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Participant391", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Participant391"):
                    opp_val = getattr(item, "bpmn2_Participant391", None)
                    
                    setattr(item, "bpmn2_Participant391", self)
                    

class bpmn2_Error(RootElement):

    def __init__(self, name: str, errorCode: str, bpmn2_Error36: "bpmn2_ItemDefinition" = None, bpmn2_Error: "bpmn2_Operation" = None, bpmn2_Error348: "bpmn2_ErrorEventDefinition" = None):
        self.name = name
        self.errorCode = errorCode
        self.bpmn2_Error36 = bpmn2_Error36
        self.bpmn2_Error = bpmn2_Error
        self.bpmn2_Error348 = bpmn2_Error348
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def errorCode(self) -> str:
        return self.__errorCode

    @errorCode.setter
    def errorCode(self, errorCode: str):
        self.__errorCode = errorCode

    @property
    def bpmn2_Error(self):
        return self.__bpmn2_Error

    @bpmn2_Error.setter
    def bpmn2_Error(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Error__bpmn2_Error", None)
        self.__bpmn2_Error = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Operation24"):
                opp_val = getattr(old_value, "bpmn2_Operation24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Operation24"):
                opp_val = getattr(value, "bpmn2_Operation24", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Operation24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Error36(self):
        return self.__bpmn2_Error36

    @bpmn2_Error36.setter
    def bpmn2_Error36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Error__bpmn2_Error36", None)
        self.__bpmn2_Error36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemDefinition37"):
                opp_val = getattr(old_value, "bpmn2_ItemDefinition37", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemDefinition37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemDefinition37"):
                opp_val = getattr(value, "bpmn2_ItemDefinition37", None)
                setattr(value, "bpmn2_ItemDefinition37", self)

    @property
    def bpmn2_Error348(self):
        return self.__bpmn2_Error348

    @bpmn2_Error348.setter
    def bpmn2_Error348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Error__bpmn2_Error348", None)
        self.__bpmn2_Error348 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ErrorEventDefinition"):
                opp_val = getattr(old_value, "bpmn2_ErrorEventDefinition", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ErrorEventDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ErrorEventDefinition"):
                opp_val = getattr(value, "bpmn2_ErrorEventDefinition", None)
                setattr(value, "bpmn2_ErrorEventDefinition", self)

class bpmn2_EventDefinition(RootElement):

    pass
class bpmn2_CorrelationProperty(RootElement):

    def __init__(self, name: str, bpmn2_CorrelationProperty: "bpmn2_CorrelationKey" = None, bpmn2_CorrelationProperty263: "bpmn2_CorrelationPropertyBinding" = None, bpmn2_CorrelationProperty238: set["bpmn2_CorrelationPropertyRetrievalExpression"] = None, bpmn2_CorrelationProperty240: "bpmn2_ItemDefinition" = None):
        self.name = name
        self.bpmn2_CorrelationProperty = bpmn2_CorrelationProperty
        self.bpmn2_CorrelationProperty263 = bpmn2_CorrelationProperty263
        self.bpmn2_CorrelationProperty238 = bpmn2_CorrelationProperty238 if bpmn2_CorrelationProperty238 is not None else set()
        self.bpmn2_CorrelationProperty240 = bpmn2_CorrelationProperty240
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_CorrelationProperty(self):
        return self.__bpmn2_CorrelationProperty

    @bpmn2_CorrelationProperty.setter
    def bpmn2_CorrelationProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CorrelationProperty__bpmn2_CorrelationProperty", None)
        self.__bpmn2_CorrelationProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CorrelationKey236"):
                opp_val = getattr(old_value, "bpmn2_CorrelationKey236", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CorrelationKey236"):
                opp_val = getattr(value, "bpmn2_CorrelationKey236", None)
                if opp_val is None:
                    setattr(value, "bpmn2_CorrelationKey236", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_CorrelationProperty263(self):
        return self.__bpmn2_CorrelationProperty263

    @bpmn2_CorrelationProperty263.setter
    def bpmn2_CorrelationProperty263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CorrelationProperty__bpmn2_CorrelationProperty263", None)
        self.__bpmn2_CorrelationProperty263 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CorrelationPropertyBinding262"):
                opp_val = getattr(old_value, "bpmn2_CorrelationPropertyBinding262", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_CorrelationPropertyBinding262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CorrelationPropertyBinding262"):
                opp_val = getattr(value, "bpmn2_CorrelationPropertyBinding262", None)
                setattr(value, "bpmn2_CorrelationPropertyBinding262", self)

    @property
    def bpmn2_CorrelationProperty240(self):
        return self.__bpmn2_CorrelationProperty240

    @bpmn2_CorrelationProperty240.setter
    def bpmn2_CorrelationProperty240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CorrelationProperty__bpmn2_CorrelationProperty240", None)
        self.__bpmn2_CorrelationProperty240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemDefinition241"):
                opp_val = getattr(old_value, "bpmn2_ItemDefinition241", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemDefinition241", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemDefinition241"):
                opp_val = getattr(value, "bpmn2_ItemDefinition241", None)
                setattr(value, "bpmn2_ItemDefinition241", self)

    @property
    def bpmn2_CorrelationProperty238(self):
        return self.__bpmn2_CorrelationProperty238

    @bpmn2_CorrelationProperty238.setter
    def bpmn2_CorrelationProperty238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CorrelationProperty__bpmn2_CorrelationProperty238", None)
        self.__bpmn2_CorrelationProperty238 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_CorrelationPropertyRetrievalExpression"):
                    opp_val = getattr(item, "bpmn2_CorrelationPropertyRetrievalExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_CorrelationPropertyRetrievalExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_CorrelationPropertyRetrievalExpression"):
                    opp_val = getattr(item, "bpmn2_CorrelationPropertyRetrievalExpression", None)
                    
                    setattr(item, "bpmn2_CorrelationPropertyRetrievalExpression", self)
                    

class bpmn2_Resource(RootElement):

    def __init__(self, name: str, bpmn2_Resource: "bpmn2_ResourceRole" = None, bpmn2_Resource99: set["bpmn2_ResourceParameter"] = None):
        self.name = name
        self.bpmn2_Resource = bpmn2_Resource
        self.bpmn2_Resource99 = bpmn2_Resource99 if bpmn2_Resource99 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_Resource(self):
        return self.__bpmn2_Resource

    @bpmn2_Resource.setter
    def bpmn2_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Resource__bpmn2_Resource", None)
        self.__bpmn2_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ResourceRole93"):
                opp_val = getattr(old_value, "bpmn2_ResourceRole93", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ResourceRole93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ResourceRole93"):
                opp_val = getattr(value, "bpmn2_ResourceRole93", None)
                setattr(value, "bpmn2_ResourceRole93", self)

    @property
    def bpmn2_Resource99(self):
        return self.__bpmn2_Resource99

    @bpmn2_Resource99.setter
    def bpmn2_Resource99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Resource__bpmn2_Resource99", None)
        self.__bpmn2_Resource99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_ResourceParameter"):
                    opp_val = getattr(item, "bpmn2_ResourceParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_ResourceParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_ResourceParameter"):
                    opp_val = getattr(item, "bpmn2_ResourceParameter", None)
                    
                    setattr(item, "bpmn2_ResourceParameter", self)
                    

class bpmn2_Collaboration(RootElement):

    def __init__(self, name: str, isClosed: bool, bpmn2_Collaboration: "bpmn2_Process" = None, bpmn2_Collaboration167: set["bpmn2_ParticipantAssociation"] = None, bpmn2_Collaboration169: set["bpmn2_MessageFlowAssociation"] = None, bpmn2_Collaboration171: "bpmn2_ConversationAssociation" = None, bpmn2_Collaboration173: set["bpmn2_Participant"] = None, bpmn2_Collaboration175: set["bpmn2_MessageFlow"] = None, bpmn2_Collaboration177: set["bpmn2_CorrelationKey"] = None, bpmn2_Collaboration179: set["bpmn2_ConversationNode"] = None, bpmn2_Collaboration181: set["bpmn2_ConversationLink"] = None, bpmn2_Collaboration162: set["bpmn2_Choreography"] = None, bpmn2_Collaboration164: set["bpmn2_Artifact"] = None, bpmn2_Collaboration382: "bpmn2_CallConversation" = None):
        self.name = name
        self.isClosed = isClosed
        self.bpmn2_Collaboration = bpmn2_Collaboration
        self.bpmn2_Collaboration167 = bpmn2_Collaboration167 if bpmn2_Collaboration167 is not None else set()
        self.bpmn2_Collaboration169 = bpmn2_Collaboration169 if bpmn2_Collaboration169 is not None else set()
        self.bpmn2_Collaboration171 = bpmn2_Collaboration171
        self.bpmn2_Collaboration173 = bpmn2_Collaboration173 if bpmn2_Collaboration173 is not None else set()
        self.bpmn2_Collaboration175 = bpmn2_Collaboration175 if bpmn2_Collaboration175 is not None else set()
        self.bpmn2_Collaboration177 = bpmn2_Collaboration177 if bpmn2_Collaboration177 is not None else set()
        self.bpmn2_Collaboration179 = bpmn2_Collaboration179 if bpmn2_Collaboration179 is not None else set()
        self.bpmn2_Collaboration181 = bpmn2_Collaboration181 if bpmn2_Collaboration181 is not None else set()
        self.bpmn2_Collaboration162 = bpmn2_Collaboration162 if bpmn2_Collaboration162 is not None else set()
        self.bpmn2_Collaboration164 = bpmn2_Collaboration164 if bpmn2_Collaboration164 is not None else set()
        self.bpmn2_Collaboration382 = bpmn2_Collaboration382
        
    @property
    def isClosed(self) -> bool:
        return self.__isClosed

    @isClosed.setter
    def isClosed(self, isClosed: bool):
        self.__isClosed = isClosed

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_Collaboration(self):
        return self.__bpmn2_Collaboration

    @bpmn2_Collaboration.setter
    def bpmn2_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration", None)
        self.__bpmn2_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Process120"):
                opp_val = getattr(old_value, "bpmn2_Process120", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Process120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Process120"):
                opp_val = getattr(value, "bpmn2_Process120", None)
                setattr(value, "bpmn2_Process120", self)

    @property
    def bpmn2_Collaboration382(self):
        return self.__bpmn2_Collaboration382

    @bpmn2_Collaboration382.setter
    def bpmn2_Collaboration382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration382", None)
        self.__bpmn2_Collaboration382 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CallConversation"):
                opp_val = getattr(old_value, "bpmn2_CallConversation", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_CallConversation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CallConversation"):
                opp_val = getattr(value, "bpmn2_CallConversation", None)
                setattr(value, "bpmn2_CallConversation", self)

    @property
    def bpmn2_Collaboration162(self):
        return self.__bpmn2_Collaboration162

    @bpmn2_Collaboration162.setter
    def bpmn2_Collaboration162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration162", None)
        self.__bpmn2_Collaboration162 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Choreography"):
                    opp_val = getattr(item, "bpmn2_Choreography", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Choreography", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Choreography"):
                    opp_val = getattr(item, "bpmn2_Choreography", None)
                    
                    setattr(item, "bpmn2_Choreography", self)
                    

    @property
    def bpmn2_Collaboration169(self):
        return self.__bpmn2_Collaboration169

    @bpmn2_Collaboration169.setter
    def bpmn2_Collaboration169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration169", None)
        self.__bpmn2_Collaboration169 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_MessageFlowAssociation"):
                    opp_val = getattr(item, "bpmn2_MessageFlowAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_MessageFlowAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_MessageFlowAssociation"):
                    opp_val = getattr(item, "bpmn2_MessageFlowAssociation", None)
                    
                    setattr(item, "bpmn2_MessageFlowAssociation", self)
                    

    @property
    def bpmn2_Collaboration173(self):
        return self.__bpmn2_Collaboration173

    @bpmn2_Collaboration173.setter
    def bpmn2_Collaboration173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration173", None)
        self.__bpmn2_Collaboration173 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Participant"):
                    opp_val = getattr(item, "bpmn2_Participant", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Participant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Participant"):
                    opp_val = getattr(item, "bpmn2_Participant", None)
                    
                    setattr(item, "bpmn2_Participant", self)
                    

    @property
    def bpmn2_Collaboration167(self):
        return self.__bpmn2_Collaboration167

    @bpmn2_Collaboration167.setter
    def bpmn2_Collaboration167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration167", None)
        self.__bpmn2_Collaboration167 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_ParticipantAssociation"):
                    opp_val = getattr(item, "bpmn2_ParticipantAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_ParticipantAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_ParticipantAssociation"):
                    opp_val = getattr(item, "bpmn2_ParticipantAssociation", None)
                    
                    setattr(item, "bpmn2_ParticipantAssociation", self)
                    

    @property
    def bpmn2_Collaboration175(self):
        return self.__bpmn2_Collaboration175

    @bpmn2_Collaboration175.setter
    def bpmn2_Collaboration175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration175", None)
        self.__bpmn2_Collaboration175 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_MessageFlow"):
                    opp_val = getattr(item, "bpmn2_MessageFlow", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_MessageFlow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_MessageFlow"):
                    opp_val = getattr(item, "bpmn2_MessageFlow", None)
                    
                    setattr(item, "bpmn2_MessageFlow", self)
                    

    @property
    def bpmn2_Collaboration181(self):
        return self.__bpmn2_Collaboration181

    @bpmn2_Collaboration181.setter
    def bpmn2_Collaboration181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration181", None)
        self.__bpmn2_Collaboration181 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_ConversationLink"):
                    opp_val = getattr(item, "bpmn2_ConversationLink", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_ConversationLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_ConversationLink"):
                    opp_val = getattr(item, "bpmn2_ConversationLink", None)
                    
                    setattr(item, "bpmn2_ConversationLink", self)
                    

    @property
    def bpmn2_Collaboration164(self):
        return self.__bpmn2_Collaboration164

    @bpmn2_Collaboration164.setter
    def bpmn2_Collaboration164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration164", None)
        self.__bpmn2_Collaboration164 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Artifact165"):
                    opp_val = getattr(item, "bpmn2_Artifact165", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Artifact165", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Artifact165"):
                    opp_val = getattr(item, "bpmn2_Artifact165", None)
                    
                    setattr(item, "bpmn2_Artifact165", self)
                    

    @property
    def bpmn2_Collaboration179(self):
        return self.__bpmn2_Collaboration179

    @bpmn2_Collaboration179.setter
    def bpmn2_Collaboration179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration179", None)
        self.__bpmn2_Collaboration179 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_ConversationNode"):
                    opp_val = getattr(item, "bpmn2_ConversationNode", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_ConversationNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_ConversationNode"):
                    opp_val = getattr(item, "bpmn2_ConversationNode", None)
                    
                    setattr(item, "bpmn2_ConversationNode", self)
                    

    @property
    def bpmn2_Collaboration177(self):
        return self.__bpmn2_Collaboration177

    @bpmn2_Collaboration177.setter
    def bpmn2_Collaboration177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration177", None)
        self.__bpmn2_Collaboration177 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_CorrelationKey"):
                    opp_val = getattr(item, "bpmn2_CorrelationKey", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_CorrelationKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_CorrelationKey"):
                    opp_val = getattr(item, "bpmn2_CorrelationKey", None)
                    
                    setattr(item, "bpmn2_CorrelationKey", self)
                    

    @property
    def bpmn2_Collaboration171(self):
        return self.__bpmn2_Collaboration171

    @bpmn2_Collaboration171.setter
    def bpmn2_Collaboration171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration171", None)
        self.__bpmn2_Collaboration171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ConversationAssociation"):
                opp_val = getattr(old_value, "bpmn2_ConversationAssociation", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ConversationAssociation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ConversationAssociation"):
                opp_val = getattr(value, "bpmn2_ConversationAssociation", None)
                setattr(value, "bpmn2_ConversationAssociation", self)

class bpmn2_Signal(RootElement):

    def __init__(self, name: str, bpmn2_Signal377: "bpmn2_ItemDefinition" = None, bpmn2_Signal: "bpmn2_SignalEventDefinition" = None):
        self.name = name
        self.bpmn2_Signal377 = bpmn2_Signal377
        self.bpmn2_Signal = bpmn2_Signal
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_Signal377(self):
        return self.__bpmn2_Signal377

    @bpmn2_Signal377.setter
    def bpmn2_Signal377(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Signal__bpmn2_Signal377", None)
        self.__bpmn2_Signal377 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemDefinition378"):
                opp_val = getattr(old_value, "bpmn2_ItemDefinition378", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemDefinition378", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemDefinition378"):
                opp_val = getattr(value, "bpmn2_ItemDefinition378", None)
                setattr(value, "bpmn2_ItemDefinition378", self)

    @property
    def bpmn2_Signal(self):
        return self.__bpmn2_Signal

    @bpmn2_Signal.setter
    def bpmn2_Signal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Signal__bpmn2_Signal", None)
        self.__bpmn2_Signal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_SignalEventDefinition"):
                opp_val = getattr(old_value, "bpmn2_SignalEventDefinition", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_SignalEventDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_SignalEventDefinition"):
                opp_val = getattr(value, "bpmn2_SignalEventDefinition", None)
                setattr(value, "bpmn2_SignalEventDefinition", self)

class bpmn2_ItemDefinition(RootElement):

    def __init__(self, itemKind: str, isCollection: bool, bpmn2_ItemDefinition: "bpmn2_Message" = None, bpmn2_ItemDefinition31: "bpmn2_EObject" = None, bpmn2_ItemDefinition34: "bpmn2_Import" = None, bpmn2_ItemDefinition37: "bpmn2_Error" = None, bpmn2_ItemDefinition66: "bpmn2_ItemAwareElement" = None, bpmn2_ItemDefinition102: "bpmn2_ResourceParameter" = None, bpmn2_ItemDefinition252: "bpmn2_FormalExpression" = None, bpmn2_ItemDefinition241: "bpmn2_CorrelationProperty" = None, bpmn2_ItemDefinition352: "bpmn2_Escalation" = None, bpmn2_ItemDefinition378: "bpmn2_Signal" = None):
        self.itemKind = itemKind
        self.isCollection = isCollection
        self.bpmn2_ItemDefinition = bpmn2_ItemDefinition
        self.bpmn2_ItemDefinition31 = bpmn2_ItemDefinition31
        self.bpmn2_ItemDefinition34 = bpmn2_ItemDefinition34
        self.bpmn2_ItemDefinition37 = bpmn2_ItemDefinition37
        self.bpmn2_ItemDefinition66 = bpmn2_ItemDefinition66
        self.bpmn2_ItemDefinition102 = bpmn2_ItemDefinition102
        self.bpmn2_ItemDefinition252 = bpmn2_ItemDefinition252
        self.bpmn2_ItemDefinition241 = bpmn2_ItemDefinition241
        self.bpmn2_ItemDefinition352 = bpmn2_ItemDefinition352
        self.bpmn2_ItemDefinition378 = bpmn2_ItemDefinition378
        
    @property
    def itemKind(self) -> str:
        return self.__itemKind

    @itemKind.setter
    def itemKind(self, itemKind: str):
        self.__itemKind = itemKind

    @property
    def isCollection(self) -> bool:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: bool):
        self.__isCollection = isCollection

    @property
    def bpmn2_ItemDefinition34(self):
        return self.__bpmn2_ItemDefinition34

    @bpmn2_ItemDefinition34.setter
    def bpmn2_ItemDefinition34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition34", None)
        self.__bpmn2_ItemDefinition34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Import"):
                opp_val = getattr(old_value, "bpmn2_Import", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Import", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Import"):
                opp_val = getattr(value, "bpmn2_Import", None)
                setattr(value, "bpmn2_Import", self)

    @property
    def bpmn2_ItemDefinition352(self):
        return self.__bpmn2_ItemDefinition352

    @bpmn2_ItemDefinition352.setter
    def bpmn2_ItemDefinition352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition352", None)
        self.__bpmn2_ItemDefinition352 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Escalation351"):
                opp_val = getattr(old_value, "bpmn2_Escalation351", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Escalation351", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Escalation351"):
                opp_val = getattr(value, "bpmn2_Escalation351", None)
                setattr(value, "bpmn2_Escalation351", self)

    @property
    def bpmn2_ItemDefinition37(self):
        return self.__bpmn2_ItemDefinition37

    @bpmn2_ItemDefinition37.setter
    def bpmn2_ItemDefinition37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition37", None)
        self.__bpmn2_ItemDefinition37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Error36"):
                opp_val = getattr(old_value, "bpmn2_Error36", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Error36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Error36"):
                opp_val = getattr(value, "bpmn2_Error36", None)
                setattr(value, "bpmn2_Error36", self)

    @property
    def bpmn2_ItemDefinition252(self):
        return self.__bpmn2_ItemDefinition252

    @bpmn2_ItemDefinition252.setter
    def bpmn2_ItemDefinition252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition252", None)
        self.__bpmn2_ItemDefinition252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_FormalExpression251"):
                opp_val = getattr(old_value, "bpmn2_FormalExpression251", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_FormalExpression251", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_FormalExpression251"):
                opp_val = getattr(value, "bpmn2_FormalExpression251", None)
                setattr(value, "bpmn2_FormalExpression251", self)

    @property
    def bpmn2_ItemDefinition(self):
        return self.__bpmn2_ItemDefinition

    @bpmn2_ItemDefinition.setter
    def bpmn2_ItemDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition", None)
        self.__bpmn2_ItemDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Message29"):
                opp_val = getattr(old_value, "bpmn2_Message29", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Message29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Message29"):
                opp_val = getattr(value, "bpmn2_Message29", None)
                setattr(value, "bpmn2_Message29", self)

    @property
    def bpmn2_ItemDefinition378(self):
        return self.__bpmn2_ItemDefinition378

    @bpmn2_ItemDefinition378.setter
    def bpmn2_ItemDefinition378(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition378", None)
        self.__bpmn2_ItemDefinition378 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Signal377"):
                opp_val = getattr(old_value, "bpmn2_Signal377", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Signal377", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Signal377"):
                opp_val = getattr(value, "bpmn2_Signal377", None)
                setattr(value, "bpmn2_Signal377", self)

    @property
    def bpmn2_ItemDefinition31(self):
        return self.__bpmn2_ItemDefinition31

    @bpmn2_ItemDefinition31.setter
    def bpmn2_ItemDefinition31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition31", None)
        self.__bpmn2_ItemDefinition31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_EObject32"):
                opp_val = getattr(old_value, "bpmn2_EObject32", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_EObject32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_EObject32"):
                opp_val = getattr(value, "bpmn2_EObject32", None)
                setattr(value, "bpmn2_EObject32", self)

    @property
    def bpmn2_ItemDefinition66(self):
        return self.__bpmn2_ItemDefinition66

    @bpmn2_ItemDefinition66.setter
    def bpmn2_ItemDefinition66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition66", None)
        self.__bpmn2_ItemDefinition66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemAwareElement"):
                opp_val = getattr(old_value, "bpmn2_ItemAwareElement", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemAwareElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemAwareElement"):
                opp_val = getattr(value, "bpmn2_ItemAwareElement", None)
                setattr(value, "bpmn2_ItemAwareElement", self)

    @property
    def bpmn2_ItemDefinition241(self):
        return self.__bpmn2_ItemDefinition241

    @bpmn2_ItemDefinition241.setter
    def bpmn2_ItemDefinition241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition241", None)
        self.__bpmn2_ItemDefinition241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CorrelationProperty240"):
                opp_val = getattr(old_value, "bpmn2_CorrelationProperty240", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_CorrelationProperty240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CorrelationProperty240"):
                opp_val = getattr(value, "bpmn2_CorrelationProperty240", None)
                setattr(value, "bpmn2_CorrelationProperty240", self)

    @property
    def bpmn2_ItemDefinition102(self):
        return self.__bpmn2_ItemDefinition102

    @bpmn2_ItemDefinition102.setter
    def bpmn2_ItemDefinition102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition102", None)
        self.__bpmn2_ItemDefinition102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ResourceParameter101"):
                opp_val = getattr(old_value, "bpmn2_ResourceParameter101", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ResourceParameter101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ResourceParameter101"):
                opp_val = getattr(value, "bpmn2_ResourceParameter101", None)
                setattr(value, "bpmn2_ResourceParameter101", self)

class bpmn2_DataStore(ItemAwareElement, RootElement):

    def __init__(self, name: str, capacity: int, isUnlimited: bool, bpmn2_DataStore: "bpmn2_DataStoreReference" = None):
        self.name = name
        self.capacity = capacity
        self.isUnlimited = isUnlimited
        self.bpmn2_DataStore = bpmn2_DataStore
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isUnlimited(self) -> bool:
        return self.__isUnlimited

    @isUnlimited.setter
    def isUnlimited(self, isUnlimited: bool):
        self.__isUnlimited = isUnlimited

    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    @property
    def bpmn2_DataStore(self):
        return self.__bpmn2_DataStore

    @bpmn2_DataStore.setter
    def bpmn2_DataStore(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataStore__bpmn2_DataStore", None)
        self.__bpmn2_DataStore = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DataStoreReference"):
                opp_val = getattr(old_value, "bpmn2_DataStoreReference", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_DataStoreReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DataStoreReference"):
                opp_val = getattr(value, "bpmn2_DataStoreReference", None)
                setattr(value, "bpmn2_DataStoreReference", self)

class bpmn2_Interface(RootElement):

    def __init__(self, name: str, bpmn2_Interface: set["bpmn2_Operation"] = None, bpmn2_Interface2: "bpmn2_EObject" = None, bpmn2_Interface42: "bpmn2_CallableElement" = None, bpmn2_Interface190: "bpmn2_Participant" = None):
        self.name = name
        self.bpmn2_Interface = bpmn2_Interface if bpmn2_Interface is not None else set()
        self.bpmn2_Interface2 = bpmn2_Interface2
        self.bpmn2_Interface42 = bpmn2_Interface42
        self.bpmn2_Interface190 = bpmn2_Interface190
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_Interface190(self):
        return self.__bpmn2_Interface190

    @bpmn2_Interface190.setter
    def bpmn2_Interface190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Interface__bpmn2_Interface190", None)
        self.__bpmn2_Interface190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Participant189"):
                opp_val = getattr(old_value, "bpmn2_Participant189", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Participant189"):
                opp_val = getattr(value, "bpmn2_Participant189", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Participant189", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Interface2(self):
        return self.__bpmn2_Interface2

    @bpmn2_Interface2.setter
    def bpmn2_Interface2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Interface__bpmn2_Interface2", None)
        self.__bpmn2_Interface2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_EObject"):
                opp_val = getattr(old_value, "bpmn2_EObject", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_EObject"):
                opp_val = getattr(value, "bpmn2_EObject", None)
                setattr(value, "bpmn2_EObject", self)

    @property
    def bpmn2_Interface42(self):
        return self.__bpmn2_Interface42

    @bpmn2_Interface42.setter
    def bpmn2_Interface42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Interface__bpmn2_Interface42", None)
        self.__bpmn2_Interface42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CallableElement41"):
                opp_val = getattr(old_value, "bpmn2_CallableElement41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CallableElement41"):
                opp_val = getattr(value, "bpmn2_CallableElement41", None)
                if opp_val is None:
                    setattr(value, "bpmn2_CallableElement41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Interface(self):
        return self.__bpmn2_Interface

    @bpmn2_Interface.setter
    def bpmn2_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Interface__bpmn2_Interface", None)
        self.__bpmn2_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Operation"):
                    opp_val = getattr(item, "bpmn2_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Operation"):
                    opp_val = getattr(item, "bpmn2_Operation", None)
                    
                    setattr(item, "bpmn2_Operation", self)
                    

class bpmn2_ExtensionAttributeDefinition:

    def __init__(self, name: str, type: str, isReference: bool, id: str, ExtensionAttributeDefinition: "bpmn2_ExtensionDefinition" = None, extensionAttributeDefinitions: "bpmn2_ExtensionDefinition" = None, bpmn2_ExtensionAttributeDefinition: "bpmn2_ExtensionAttributeValue" = None):
        self.name = name
        self.type = type
        self.isReference = isReference
        self.id = id
        self.ExtensionAttributeDefinition = ExtensionAttributeDefinition
        self.extensionAttributeDefinitions = extensionAttributeDefinitions
        self.bpmn2_ExtensionAttributeDefinition = bpmn2_ExtensionAttributeDefinition
        
    @property
    def isReference(self) -> bool:
        return self.__isReference

    @isReference.setter
    def isReference(self, isReference: bool):
        self.__isReference = isReference

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def extensionAttributeDefinitions(self):
        return self.__extensionAttributeDefinitions

    @extensionAttributeDefinitions.setter
    def extensionAttributeDefinitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ExtensionAttributeDefinition__extensionAttributeDefinitions", None)
        self.__extensionAttributeDefinitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExtensionDefinition"):
                opp_val = getattr(old_value, "ExtensionDefinition", None)
                if opp_val == self:
                    setattr(old_value, "ExtensionDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExtensionDefinition"):
                opp_val = getattr(value, "ExtensionDefinition", None)
                setattr(value, "ExtensionDefinition", self)

    @property
    def ExtensionAttributeDefinition(self):
        return self.__ExtensionAttributeDefinition

    @ExtensionAttributeDefinition.setter
    def ExtensionAttributeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ExtensionAttributeDefinition__ExtensionAttributeDefinition", None)
        self.__ExtensionAttributeDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extensionDefinition"):
                opp_val = getattr(old_value, "extensionDefinition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extensionDefinition"):
                opp_val = getattr(value, "extensionDefinition", None)
                if opp_val is None:
                    setattr(value, "extensionDefinition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_ExtensionAttributeDefinition(self):
        return self.__bpmn2_ExtensionAttributeDefinition

    @bpmn2_ExtensionAttributeDefinition.setter
    def bpmn2_ExtensionAttributeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ExtensionAttributeDefinition__bpmn2_ExtensionAttributeDefinition", None)
        self.__bpmn2_ExtensionAttributeDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ExtensionAttributeValue17"):
                opp_val = getattr(old_value, "bpmn2_ExtensionAttributeValue17", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ExtensionAttributeValue17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ExtensionAttributeValue17"):
                opp_val = getattr(value, "bpmn2_ExtensionAttributeValue17", None)
                setattr(value, "bpmn2_ExtensionAttributeValue17", self)

class bpmn2_ExtensionAttributeValue:

    def __init__(self, id: str, bpmn2_ExtensionAttributeValue: "bpmn2_BaseElement" = None, bpmn2_ExtensionAttributeValue11: "bpmn2_EObject" = None, bpmn2_ExtensionAttributeValue14: "bpmn2_EObject" = None, bpmn2_ExtensionAttributeValue17: "bpmn2_ExtensionAttributeDefinition" = None):
        self.id = id
        self.bpmn2_ExtensionAttributeValue = bpmn2_ExtensionAttributeValue
        self.bpmn2_ExtensionAttributeValue11 = bpmn2_ExtensionAttributeValue11
        self.bpmn2_ExtensionAttributeValue14 = bpmn2_ExtensionAttributeValue14
        self.bpmn2_ExtensionAttributeValue17 = bpmn2_ExtensionAttributeValue17
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def bpmn2_ExtensionAttributeValue14(self):
        return self.__bpmn2_ExtensionAttributeValue14

    @bpmn2_ExtensionAttributeValue14.setter
    def bpmn2_ExtensionAttributeValue14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ExtensionAttributeValue__bpmn2_ExtensionAttributeValue14", None)
        self.__bpmn2_ExtensionAttributeValue14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_EObject15"):
                opp_val = getattr(old_value, "bpmn2_EObject15", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_EObject15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_EObject15"):
                opp_val = getattr(value, "bpmn2_EObject15", None)
                setattr(value, "bpmn2_EObject15", self)

    @property
    def bpmn2_ExtensionAttributeValue(self):
        return self.__bpmn2_ExtensionAttributeValue

    @bpmn2_ExtensionAttributeValue.setter
    def bpmn2_ExtensionAttributeValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ExtensionAttributeValue__bpmn2_ExtensionAttributeValue", None)
        self.__bpmn2_ExtensionAttributeValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_BaseElement5"):
                opp_val = getattr(old_value, "bpmn2_BaseElement5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_BaseElement5"):
                opp_val = getattr(value, "bpmn2_BaseElement5", None)
                if opp_val is None:
                    setattr(value, "bpmn2_BaseElement5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_ExtensionAttributeValue11(self):
        return self.__bpmn2_ExtensionAttributeValue11

    @bpmn2_ExtensionAttributeValue11.setter
    def bpmn2_ExtensionAttributeValue11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ExtensionAttributeValue__bpmn2_ExtensionAttributeValue11", None)
        self.__bpmn2_ExtensionAttributeValue11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_EObject12"):
                opp_val = getattr(old_value, "bpmn2_EObject12", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_EObject12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_EObject12"):
                opp_val = getattr(value, "bpmn2_EObject12", None)
                setattr(value, "bpmn2_EObject12", self)

    @property
    def bpmn2_ExtensionAttributeValue17(self):
        return self.__bpmn2_ExtensionAttributeValue17

    @bpmn2_ExtensionAttributeValue17.setter
    def bpmn2_ExtensionAttributeValue17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ExtensionAttributeValue__bpmn2_ExtensionAttributeValue17", None)
        self.__bpmn2_ExtensionAttributeValue17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ExtensionAttributeDefinition"):
                opp_val = getattr(old_value, "bpmn2_ExtensionAttributeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ExtensionAttributeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ExtensionAttributeDefinition"):
                opp_val = getattr(value, "bpmn2_ExtensionAttributeDefinition", None)
                setattr(value, "bpmn2_ExtensionAttributeDefinition", self)

class bpmn2_ExtensionDefinition:

    def __init__(self, name: str, id: str, bpmn2_ExtensionDefinition: "bpmn2_BaseElement" = None, extensionDefinition: set["bpmn2_ExtensionAttributeDefinition"] = None, ExtensionDefinition: "bpmn2_ExtensionAttributeDefinition" = None, bpmn2_ExtensionDefinition332: "bpmn2_Extension" = None):
        self.name = name
        self.id = id
        self.bpmn2_ExtensionDefinition = bpmn2_ExtensionDefinition
        self.extensionDefinition = extensionDefinition if extensionDefinition is not None else set()
        self.ExtensionDefinition = ExtensionDefinition
        self.bpmn2_ExtensionDefinition332 = bpmn2_ExtensionDefinition332
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def extensionDefinition(self):
        return self.__extensionDefinition

    @extensionDefinition.setter
    def extensionDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ExtensionDefinition__extensionDefinition", None)
        self.__extensionDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExtensionAttributeDefinition"):
                    opp_val = getattr(item, "ExtensionAttributeDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "ExtensionAttributeDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExtensionAttributeDefinition"):
                    opp_val = getattr(item, "ExtensionAttributeDefinition", None)
                    
                    setattr(item, "ExtensionAttributeDefinition", self)
                    

    @property
    def bpmn2_ExtensionDefinition(self):
        return self.__bpmn2_ExtensionDefinition

    @bpmn2_ExtensionDefinition.setter
    def bpmn2_ExtensionDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ExtensionDefinition__bpmn2_ExtensionDefinition", None)
        self.__bpmn2_ExtensionDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_BaseElement"):
                opp_val = getattr(old_value, "bpmn2_BaseElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_BaseElement"):
                opp_val = getattr(value, "bpmn2_BaseElement", None)
                if opp_val is None:
                    setattr(value, "bpmn2_BaseElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_ExtensionDefinition332(self):
        return self.__bpmn2_ExtensionDefinition332

    @bpmn2_ExtensionDefinition332.setter
    def bpmn2_ExtensionDefinition332(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ExtensionDefinition__bpmn2_ExtensionDefinition332", None)
        self.__bpmn2_ExtensionDefinition332 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Extension"):
                opp_val = getattr(old_value, "bpmn2_Extension", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Extension", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Extension"):
                opp_val = getattr(value, "bpmn2_Extension", None)
                setattr(value, "bpmn2_Extension", self)

    @property
    def ExtensionDefinition(self):
        return self.__ExtensionDefinition

    @ExtensionDefinition.setter
    def ExtensionDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ExtensionDefinition__ExtensionDefinition", None)
        self.__ExtensionDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extensionAttributeDefinitions"):
                opp_val = getattr(old_value, "extensionAttributeDefinitions", None)
                if opp_val == self:
                    setattr(old_value, "extensionAttributeDefinitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extensionAttributeDefinitions"):
                opp_val = getattr(value, "extensionAttributeDefinitions", None)
                setattr(value, "extensionAttributeDefinitions", self)

class bpmn2_BaseElement(ABC):

    def __init__(self, id: str, bpmn2_BaseElement: set["bpmn2_ExtensionDefinition"] = None, bpmn2_BaseElement5: set["bpmn2_ExtensionAttributeValue"] = None, bpmn2_BaseElement7: set["bpmn2_Documentation"] = None, bpmn2_BaseElement146: "bpmn2_Lane" = None, bpmn2_BaseElement150: "bpmn2_Lane" = None, bpmn2_BaseElement413: "bpmn2_Association" = None, bpmn2_BaseElement416: "bpmn2_Association" = None):
        self.id = id
        self.bpmn2_BaseElement = bpmn2_BaseElement if bpmn2_BaseElement is not None else set()
        self.bpmn2_BaseElement5 = bpmn2_BaseElement5 if bpmn2_BaseElement5 is not None else set()
        self.bpmn2_BaseElement7 = bpmn2_BaseElement7 if bpmn2_BaseElement7 is not None else set()
        self.bpmn2_BaseElement146 = bpmn2_BaseElement146
        self.bpmn2_BaseElement150 = bpmn2_BaseElement150
        self.bpmn2_BaseElement413 = bpmn2_BaseElement413
        self.bpmn2_BaseElement416 = bpmn2_BaseElement416
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def bpmn2_BaseElement7(self):
        return self.__bpmn2_BaseElement7

    @bpmn2_BaseElement7.setter
    def bpmn2_BaseElement7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BaseElement__bpmn2_BaseElement7", None)
        self.__bpmn2_BaseElement7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Documentation"):
                    opp_val = getattr(item, "bpmn2_Documentation", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Documentation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Documentation"):
                    opp_val = getattr(item, "bpmn2_Documentation", None)
                    
                    setattr(item, "bpmn2_Documentation", self)
                    

    @property
    def bpmn2_BaseElement150(self):
        return self.__bpmn2_BaseElement150

    @bpmn2_BaseElement150.setter
    def bpmn2_BaseElement150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BaseElement__bpmn2_BaseElement150", None)
        self.__bpmn2_BaseElement150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Lane149"):
                opp_val = getattr(old_value, "bpmn2_Lane149", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Lane149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Lane149"):
                opp_val = getattr(value, "bpmn2_Lane149", None)
                setattr(value, "bpmn2_Lane149", self)

    @property
    def bpmn2_BaseElement(self):
        return self.__bpmn2_BaseElement

    @bpmn2_BaseElement.setter
    def bpmn2_BaseElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BaseElement__bpmn2_BaseElement", None)
        self.__bpmn2_BaseElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_ExtensionDefinition"):
                    opp_val = getattr(item, "bpmn2_ExtensionDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_ExtensionDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_ExtensionDefinition"):
                    opp_val = getattr(item, "bpmn2_ExtensionDefinition", None)
                    
                    setattr(item, "bpmn2_ExtensionDefinition", self)
                    

    @property
    def bpmn2_BaseElement416(self):
        return self.__bpmn2_BaseElement416

    @bpmn2_BaseElement416.setter
    def bpmn2_BaseElement416(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BaseElement__bpmn2_BaseElement416", None)
        self.__bpmn2_BaseElement416 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Association415"):
                opp_val = getattr(old_value, "bpmn2_Association415", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Association415", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Association415"):
                opp_val = getattr(value, "bpmn2_Association415", None)
                setattr(value, "bpmn2_Association415", self)

    @property
    def bpmn2_BaseElement146(self):
        return self.__bpmn2_BaseElement146

    @bpmn2_BaseElement146.setter
    def bpmn2_BaseElement146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BaseElement__bpmn2_BaseElement146", None)
        self.__bpmn2_BaseElement146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Lane145"):
                opp_val = getattr(old_value, "bpmn2_Lane145", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Lane145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Lane145"):
                opp_val = getattr(value, "bpmn2_Lane145", None)
                setattr(value, "bpmn2_Lane145", self)

    @property
    def bpmn2_BaseElement413(self):
        return self.__bpmn2_BaseElement413

    @bpmn2_BaseElement413.setter
    def bpmn2_BaseElement413(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BaseElement__bpmn2_BaseElement413", None)
        self.__bpmn2_BaseElement413 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Association"):
                opp_val = getattr(old_value, "bpmn2_Association", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Association"):
                opp_val = getattr(value, "bpmn2_Association", None)
                setattr(value, "bpmn2_Association", self)

    @property
    def bpmn2_BaseElement5(self):
        return self.__bpmn2_BaseElement5

    @bpmn2_BaseElement5.setter
    def bpmn2_BaseElement5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BaseElement__bpmn2_BaseElement5", None)
        self.__bpmn2_BaseElement5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_ExtensionAttributeValue"):
                    opp_val = getattr(item, "bpmn2_ExtensionAttributeValue", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_ExtensionAttributeValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_ExtensionAttributeValue"):
                    opp_val = getattr(item, "bpmn2_ExtensionAttributeValue", None)
                    
                    setattr(item, "bpmn2_ExtensionAttributeValue", self)
                    

class BaseElement:

    pass
class bpmn2_Assignment(BaseElement):

    pass
class bpmn2_DataState(BaseElement):

    def __init__(self, name: str, bpmn2_DataState: "bpmn2_ItemAwareElement" = None):
        self.name = name
        self.bpmn2_DataState = bpmn2_DataState
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_DataState(self):
        return self.__bpmn2_DataState

    @bpmn2_DataState.setter
    def bpmn2_DataState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataState__bpmn2_DataState", None)
        self.__bpmn2_DataState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemAwareElement68"):
                opp_val = getattr(old_value, "bpmn2_ItemAwareElement68", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemAwareElement68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemAwareElement68"):
                opp_val = getattr(value, "bpmn2_ItemAwareElement68", None)
                setattr(value, "bpmn2_ItemAwareElement68", self)

class bpmn2_CorrelationKey(BaseElement):

    def __init__(self, name: str, bpmn2_CorrelationKey: "bpmn2_Collaboration" = None, bpmn2_CorrelationKey234: "bpmn2_ConversationNode" = None, bpmn2_CorrelationKey236: set["bpmn2_CorrelationProperty"] = None, bpmn2_CorrelationKey255: "bpmn2_CorrelationSubscription" = None, bpmn2_CorrelationKey399: "bpmn2_ChoreographyActivity" = None):
        self.name = name
        self.bpmn2_CorrelationKey = bpmn2_CorrelationKey
        self.bpmn2_CorrelationKey234 = bpmn2_CorrelationKey234
        self.bpmn2_CorrelationKey236 = bpmn2_CorrelationKey236 if bpmn2_CorrelationKey236 is not None else set()
        self.bpmn2_CorrelationKey255 = bpmn2_CorrelationKey255
        self.bpmn2_CorrelationKey399 = bpmn2_CorrelationKey399
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_CorrelationKey(self):
        return self.__bpmn2_CorrelationKey

    @bpmn2_CorrelationKey.setter
    def bpmn2_CorrelationKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CorrelationKey__bpmn2_CorrelationKey", None)
        self.__bpmn2_CorrelationKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Collaboration177"):
                opp_val = getattr(old_value, "bpmn2_Collaboration177", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Collaboration177"):
                opp_val = getattr(value, "bpmn2_Collaboration177", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Collaboration177", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_CorrelationKey399(self):
        return self.__bpmn2_CorrelationKey399

    @bpmn2_CorrelationKey399.setter
    def bpmn2_CorrelationKey399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CorrelationKey__bpmn2_CorrelationKey399", None)
        self.__bpmn2_CorrelationKey399 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ChoreographyActivity398"):
                opp_val = getattr(old_value, "bpmn2_ChoreographyActivity398", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ChoreographyActivity398"):
                opp_val = getattr(value, "bpmn2_ChoreographyActivity398", None)
                if opp_val is None:
                    setattr(value, "bpmn2_ChoreographyActivity398", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_CorrelationKey236(self):
        return self.__bpmn2_CorrelationKey236

    @bpmn2_CorrelationKey236.setter
    def bpmn2_CorrelationKey236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CorrelationKey__bpmn2_CorrelationKey236", None)
        self.__bpmn2_CorrelationKey236 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_CorrelationProperty"):
                    opp_val = getattr(item, "bpmn2_CorrelationProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_CorrelationProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_CorrelationProperty"):
                    opp_val = getattr(item, "bpmn2_CorrelationProperty", None)
                    
                    setattr(item, "bpmn2_CorrelationProperty", self)
                    

    @property
    def bpmn2_CorrelationKey255(self):
        return self.__bpmn2_CorrelationKey255

    @bpmn2_CorrelationKey255.setter
    def bpmn2_CorrelationKey255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CorrelationKey__bpmn2_CorrelationKey255", None)
        self.__bpmn2_CorrelationKey255 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CorrelationSubscription254"):
                opp_val = getattr(old_value, "bpmn2_CorrelationSubscription254", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_CorrelationSubscription254", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CorrelationSubscription254"):
                opp_val = getattr(value, "bpmn2_CorrelationSubscription254", None)
                setattr(value, "bpmn2_CorrelationSubscription254", self)

    @property
    def bpmn2_CorrelationKey234(self):
        return self.__bpmn2_CorrelationKey234

    @bpmn2_CorrelationKey234.setter
    def bpmn2_CorrelationKey234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CorrelationKey__bpmn2_CorrelationKey234", None)
        self.__bpmn2_CorrelationKey234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ConversationNode233"):
                opp_val = getattr(old_value, "bpmn2_ConversationNode233", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ConversationNode233"):
                opp_val = getattr(value, "bpmn2_ConversationNode233", None)
                if opp_val is None:
                    setattr(value, "bpmn2_ConversationNode233", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_Artifact(BaseElement):

    pass
class bpmn2_Monitoring(BaseElement):

    pass
class bpmn2_LoopCharacteristics(BaseElement):

    pass
class bpmn2_FlowElement(BaseElement):

    def __init__(self, name: str, categorizedFlowElements: set["bpmn2_CategoryValue"] = None, FlowElement: "bpmn2_CategoryValue" = None, bpmn2_FlowElement: "bpmn2_FlowElementsContainer" = None, bpmn2_FlowElement132: "bpmn2_Auditing" = None, bpmn2_FlowElement135: "bpmn2_Monitoring" = None):
        self.name = name
        self.categorizedFlowElements = categorizedFlowElements if categorizedFlowElements is not None else set()
        self.FlowElement = FlowElement
        self.bpmn2_FlowElement = bpmn2_FlowElement
        self.bpmn2_FlowElement132 = bpmn2_FlowElement132
        self.bpmn2_FlowElement135 = bpmn2_FlowElement135
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_FlowElement132(self):
        return self.__bpmn2_FlowElement132

    @bpmn2_FlowElement132.setter
    def bpmn2_FlowElement132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FlowElement__bpmn2_FlowElement132", None)
        self.__bpmn2_FlowElement132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Auditing133"):
                opp_val = getattr(old_value, "bpmn2_Auditing133", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Auditing133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Auditing133"):
                opp_val = getattr(value, "bpmn2_Auditing133", None)
                setattr(value, "bpmn2_Auditing133", self)

    @property
    def bpmn2_FlowElement(self):
        return self.__bpmn2_FlowElement

    @bpmn2_FlowElement.setter
    def bpmn2_FlowElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FlowElement__bpmn2_FlowElement", None)
        self.__bpmn2_FlowElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_FlowElementsContainer"):
                opp_val = getattr(old_value, "bpmn2_FlowElementsContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_FlowElementsContainer"):
                opp_val = getattr(value, "bpmn2_FlowElementsContainer", None)
                if opp_val is None:
                    setattr(value, "bpmn2_FlowElementsContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def categorizedFlowElements(self):
        return self.__categorizedFlowElements

    @categorizedFlowElements.setter
    def categorizedFlowElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FlowElement__categorizedFlowElements", None)
        self.__categorizedFlowElements = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CategoryValue"):
                    opp_val = getattr(item, "CategoryValue", None)
                    
                    if opp_val == self:
                        setattr(item, "CategoryValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CategoryValue"):
                    opp_val = getattr(item, "CategoryValue", None)
                    
                    setattr(item, "CategoryValue", self)
                    

    @property
    def FlowElement(self):
        return self.__FlowElement

    @FlowElement.setter
    def FlowElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FlowElement__FlowElement", None)
        self.__FlowElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "categoryValueRef"):
                opp_val = getattr(old_value, "categoryValueRef", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "categoryValueRef"):
                opp_val = getattr(value, "categoryValueRef", None)
                if opp_val is None:
                    setattr(value, "categoryValueRef", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_FlowElement135(self):
        return self.__bpmn2_FlowElement135

    @bpmn2_FlowElement135.setter
    def bpmn2_FlowElement135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FlowElement__bpmn2_FlowElement135", None)
        self.__bpmn2_FlowElement135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Monitoring136"):
                opp_val = getattr(old_value, "bpmn2_Monitoring136", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Monitoring136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Monitoring136"):
                opp_val = getattr(value, "bpmn2_Monitoring136", None)
                setattr(value, "bpmn2_Monitoring136", self)

class bpmn2_Auditing(BaseElement):

    pass
class bpmn2_Relationship(BaseElement):

    def __init__(self, type: str, direction: str, bpmn2_Relationship: set["bpmn2_EObject"] = None, bpmn2_Relationship329: set["bpmn2_EObject"] = None, bpmn2_Relationship479: "bpmn2_Definitions" = None):
        self.type = type
        self.direction = direction
        self.bpmn2_Relationship = bpmn2_Relationship if bpmn2_Relationship is not None else set()
        self.bpmn2_Relationship329 = bpmn2_Relationship329 if bpmn2_Relationship329 is not None else set()
        self.bpmn2_Relationship479 = bpmn2_Relationship479
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def bpmn2_Relationship(self):
        return self.__bpmn2_Relationship

    @bpmn2_Relationship.setter
    def bpmn2_Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Relationship__bpmn2_Relationship", None)
        self.__bpmn2_Relationship = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_EObject327"):
                    opp_val = getattr(item, "bpmn2_EObject327", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_EObject327", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_EObject327"):
                    opp_val = getattr(item, "bpmn2_EObject327", None)
                    
                    setattr(item, "bpmn2_EObject327", self)
                    

    @property
    def bpmn2_Relationship479(self):
        return self.__bpmn2_Relationship479

    @bpmn2_Relationship479.setter
    def bpmn2_Relationship479(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Relationship__bpmn2_Relationship479", None)
        self.__bpmn2_Relationship479 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Definitions478"):
                opp_val = getattr(old_value, "bpmn2_Definitions478", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Definitions478"):
                opp_val = getattr(value, "bpmn2_Definitions478", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Definitions478", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Relationship329(self):
        return self.__bpmn2_Relationship329

    @bpmn2_Relationship329.setter
    def bpmn2_Relationship329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Relationship__bpmn2_Relationship329", None)
        self.__bpmn2_Relationship329 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_EObject330"):
                    opp_val = getattr(item, "bpmn2_EObject330", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_EObject330", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_EObject330"):
                    opp_val = getattr(item, "bpmn2_EObject330", None)
                    
                    setattr(item, "bpmn2_EObject330", self)
                    

class bpmn2_Rendering(BaseElement):

    pass
class bpmn2_ConversationNode(BaseElement, InteractionNode):

    def __init__(self, name: str, bpmn2_ConversationNode: "bpmn2_Collaboration" = None, bpmn2_ConversationNode222: "bpmn2_ConversationAssociation" = None, bpmn2_ConversationNode225: "bpmn2_ConversationAssociation" = None, bpmn2_ConversationNode227: set["bpmn2_Participant"] = None, bpmn2_ConversationNode230: set["bpmn2_MessageFlow"] = None, bpmn2_ConversationNode233: set["bpmn2_CorrelationKey"] = None, bpmn2_ConversationNode387: "bpmn2_SubConversation" = None):
        self.name = name
        self.bpmn2_ConversationNode = bpmn2_ConversationNode
        self.bpmn2_ConversationNode222 = bpmn2_ConversationNode222
        self.bpmn2_ConversationNode225 = bpmn2_ConversationNode225
        self.bpmn2_ConversationNode227 = bpmn2_ConversationNode227 if bpmn2_ConversationNode227 is not None else set()
        self.bpmn2_ConversationNode230 = bpmn2_ConversationNode230 if bpmn2_ConversationNode230 is not None else set()
        self.bpmn2_ConversationNode233 = bpmn2_ConversationNode233 if bpmn2_ConversationNode233 is not None else set()
        self.bpmn2_ConversationNode387 = bpmn2_ConversationNode387
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_ConversationNode233(self):
        return self.__bpmn2_ConversationNode233

    @bpmn2_ConversationNode233.setter
    def bpmn2_ConversationNode233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ConversationNode__bpmn2_ConversationNode233", None)
        self.__bpmn2_ConversationNode233 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_CorrelationKey234"):
                    opp_val = getattr(item, "bpmn2_CorrelationKey234", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_CorrelationKey234", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_CorrelationKey234"):
                    opp_val = getattr(item, "bpmn2_CorrelationKey234", None)
                    
                    setattr(item, "bpmn2_CorrelationKey234", self)
                    

    @property
    def bpmn2_ConversationNode225(self):
        return self.__bpmn2_ConversationNode225

    @bpmn2_ConversationNode225.setter
    def bpmn2_ConversationNode225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ConversationNode__bpmn2_ConversationNode225", None)
        self.__bpmn2_ConversationNode225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ConversationAssociation224"):
                opp_val = getattr(old_value, "bpmn2_ConversationAssociation224", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ConversationAssociation224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ConversationAssociation224"):
                opp_val = getattr(value, "bpmn2_ConversationAssociation224", None)
                setattr(value, "bpmn2_ConversationAssociation224", self)

    @property
    def bpmn2_ConversationNode222(self):
        return self.__bpmn2_ConversationNode222

    @bpmn2_ConversationNode222.setter
    def bpmn2_ConversationNode222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ConversationNode__bpmn2_ConversationNode222", None)
        self.__bpmn2_ConversationNode222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ConversationAssociation221"):
                opp_val = getattr(old_value, "bpmn2_ConversationAssociation221", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ConversationAssociation221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ConversationAssociation221"):
                opp_val = getattr(value, "bpmn2_ConversationAssociation221", None)
                setattr(value, "bpmn2_ConversationAssociation221", self)

    @property
    def bpmn2_ConversationNode387(self):
        return self.__bpmn2_ConversationNode387

    @bpmn2_ConversationNode387.setter
    def bpmn2_ConversationNode387(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ConversationNode__bpmn2_ConversationNode387", None)
        self.__bpmn2_ConversationNode387 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_SubConversation"):
                opp_val = getattr(old_value, "bpmn2_SubConversation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_SubConversation"):
                opp_val = getattr(value, "bpmn2_SubConversation", None)
                if opp_val is None:
                    setattr(value, "bpmn2_SubConversation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_ConversationNode227(self):
        return self.__bpmn2_ConversationNode227

    @bpmn2_ConversationNode227.setter
    def bpmn2_ConversationNode227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ConversationNode__bpmn2_ConversationNode227", None)
        self.__bpmn2_ConversationNode227 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Participant228"):
                    opp_val = getattr(item, "bpmn2_Participant228", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Participant228", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Participant228"):
                    opp_val = getattr(item, "bpmn2_Participant228", None)
                    
                    setattr(item, "bpmn2_Participant228", self)
                    

    @property
    def bpmn2_ConversationNode230(self):
        return self.__bpmn2_ConversationNode230

    @bpmn2_ConversationNode230.setter
    def bpmn2_ConversationNode230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ConversationNode__bpmn2_ConversationNode230", None)
        self.__bpmn2_ConversationNode230 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_MessageFlow231"):
                    opp_val = getattr(item, "bpmn2_MessageFlow231", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_MessageFlow231", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_MessageFlow231"):
                    opp_val = getattr(item, "bpmn2_MessageFlow231", None)
                    
                    setattr(item, "bpmn2_MessageFlow231", self)
                    

    @property
    def bpmn2_ConversationNode(self):
        return self.__bpmn2_ConversationNode

    @bpmn2_ConversationNode.setter
    def bpmn2_ConversationNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ConversationNode__bpmn2_ConversationNode", None)
        self.__bpmn2_ConversationNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Collaboration179"):
                opp_val = getattr(old_value, "bpmn2_Collaboration179", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Collaboration179"):
                opp_val = getattr(value, "bpmn2_Collaboration179", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Collaboration179", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_InputSet(BaseElement):

    def __init__(self, name: str, inputSetRefs: set["bpmn2_DataInput"] = None, inputSetWithOptional: set["bpmn2_DataInput"] = None, inputSetWithWhileExecuting: set["bpmn2_DataInput"] = None, inputSetRefs59: set["bpmn2_OutputSet"] = None, InputSet: "bpmn2_DataInput" = None, InputSet62: "bpmn2_DataInput" = None, InputSet64: "bpmn2_DataInput" = None, bpmn2_InputSet: "bpmn2_InputOutputSpecification" = None, bpmn2_InputSet85: "bpmn2_InputOutputBinding" = None, InputSet76: "bpmn2_OutputSet" = None, bpmn2_InputSet334: "bpmn2_ThrowEvent" = None):
        self.name = name
        self.inputSetRefs = inputSetRefs if inputSetRefs is not None else set()
        self.inputSetWithOptional = inputSetWithOptional if inputSetWithOptional is not None else set()
        self.inputSetWithWhileExecuting = inputSetWithWhileExecuting if inputSetWithWhileExecuting is not None else set()
        self.inputSetRefs59 = inputSetRefs59 if inputSetRefs59 is not None else set()
        self.InputSet = InputSet
        self.InputSet62 = InputSet62
        self.InputSet64 = InputSet64
        self.bpmn2_InputSet = bpmn2_InputSet
        self.bpmn2_InputSet85 = bpmn2_InputSet85
        self.InputSet76 = InputSet76
        self.bpmn2_InputSet334 = bpmn2_InputSet334
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_InputSet85(self):
        return self.__bpmn2_InputSet85

    @bpmn2_InputSet85.setter
    def bpmn2_InputSet85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_InputSet__bpmn2_InputSet85", None)
        self.__bpmn2_InputSet85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_InputOutputBinding84"):
                opp_val = getattr(old_value, "bpmn2_InputOutputBinding84", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_InputOutputBinding84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_InputOutputBinding84"):
                opp_val = getattr(value, "bpmn2_InputOutputBinding84", None)
                setattr(value, "bpmn2_InputOutputBinding84", self)

    @property
    def InputSet76(self):
        return self.__InputSet76

    @InputSet76.setter
    def InputSet76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_InputSet__InputSet76", None)
        self.__InputSet76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outputSetRefs75"):
                opp_val = getattr(old_value, "outputSetRefs75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outputSetRefs75"):
                opp_val = getattr(value, "outputSetRefs75", None)
                if opp_val is None:
                    setattr(value, "outputSetRefs75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inputSetWithOptional(self):
        return self.__inputSetWithOptional

    @inputSetWithOptional.setter
    def inputSetWithOptional(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_InputSet__inputSetWithOptional", None)
        self.__inputSetWithOptional = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataInput55"):
                    opp_val = getattr(item, "DataInput55", None)
                    
                    if opp_val == self:
                        setattr(item, "DataInput55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataInput55"):
                    opp_val = getattr(item, "DataInput55", None)
                    
                    setattr(item, "DataInput55", self)
                    

    @property
    def bpmn2_InputSet(self):
        return self.__bpmn2_InputSet

    @bpmn2_InputSet.setter
    def bpmn2_InputSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_InputSet__bpmn2_InputSet", None)
        self.__bpmn2_InputSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_InputOutputSpecification46"):
                opp_val = getattr(old_value, "bpmn2_InputOutputSpecification46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_InputOutputSpecification46"):
                opp_val = getattr(value, "bpmn2_InputOutputSpecification46", None)
                if opp_val is None:
                    setattr(value, "bpmn2_InputOutputSpecification46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inputSetRefs59(self):
        return self.__inputSetRefs59

    @inputSetRefs59.setter
    def inputSetRefs59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_InputSet__inputSetRefs59", None)
        self.__inputSetRefs59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputSet"):
                    opp_val = getattr(item, "OutputSet", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputSet"):
                    opp_val = getattr(item, "OutputSet", None)
                    
                    setattr(item, "OutputSet", self)
                    

    @property
    def InputSet62(self):
        return self.__InputSet62

    @InputSet62.setter
    def InputSet62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_InputSet__InputSet62", None)
        self.__InputSet62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileExecutingInputRefs"):
                opp_val = getattr(old_value, "whileExecutingInputRefs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileExecutingInputRefs"):
                opp_val = getattr(value, "whileExecutingInputRefs", None)
                if opp_val is None:
                    setattr(value, "whileExecutingInputRefs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def InputSet(self):
        return self.__InputSet

    @InputSet.setter
    def InputSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_InputSet__InputSet", None)
        self.__InputSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optionalInputRefs"):
                opp_val = getattr(old_value, "optionalInputRefs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optionalInputRefs"):
                opp_val = getattr(value, "optionalInputRefs", None)
                if opp_val is None:
                    setattr(value, "optionalInputRefs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inputSetRefs(self):
        return self.__inputSetRefs

    @inputSetRefs.setter
    def inputSetRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_InputSet__inputSetRefs", None)
        self.__inputSetRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataInput"):
                    opp_val = getattr(item, "DataInput", None)
                    
                    if opp_val == self:
                        setattr(item, "DataInput", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataInput"):
                    opp_val = getattr(item, "DataInput", None)
                    
                    setattr(item, "DataInput", self)
                    

    @property
    def bpmn2_InputSet334(self):
        return self.__bpmn2_InputSet334

    @bpmn2_InputSet334.setter
    def bpmn2_InputSet334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_InputSet__bpmn2_InputSet334", None)
        self.__bpmn2_InputSet334 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ThrowEvent"):
                opp_val = getattr(old_value, "bpmn2_ThrowEvent", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ThrowEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ThrowEvent"):
                opp_val = getattr(value, "bpmn2_ThrowEvent", None)
                setattr(value, "bpmn2_ThrowEvent", self)

    @property
    def inputSetWithWhileExecuting(self):
        return self.__inputSetWithWhileExecuting

    @inputSetWithWhileExecuting.setter
    def inputSetWithWhileExecuting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_InputSet__inputSetWithWhileExecuting", None)
        self.__inputSetWithWhileExecuting = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataInput57"):
                    opp_val = getattr(item, "DataInput57", None)
                    
                    if opp_val == self:
                        setattr(item, "DataInput57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataInput57"):
                    opp_val = getattr(item, "DataInput57", None)
                    
                    setattr(item, "DataInput57", self)
                    

    @property
    def InputSet64(self):
        return self.__InputSet64

    @InputSet64.setter
    def InputSet64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_InputSet__InputSet64", None)
        self.__InputSet64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataInputRefs"):
                opp_val = getattr(old_value, "dataInputRefs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataInputRefs"):
                opp_val = getattr(value, "dataInputRefs", None)
                if opp_val is None:
                    setattr(value, "dataInputRefs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_ConversationAssociation(BaseElement):

    pass
class bpmn2_LaneSet(BaseElement):

    def __init__(self, name: str, bpmn2_LaneSet140: set["bpmn2_Lane"] = None, bpmn2_LaneSet143: "bpmn2_Lane" = None, bpmn2_LaneSet: "bpmn2_FlowElementsContainer" = None):
        self.name = name
        self.bpmn2_LaneSet140 = bpmn2_LaneSet140 if bpmn2_LaneSet140 is not None else set()
        self.bpmn2_LaneSet143 = bpmn2_LaneSet143
        self.bpmn2_LaneSet = bpmn2_LaneSet
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_LaneSet140(self):
        return self.__bpmn2_LaneSet140

    @bpmn2_LaneSet140.setter
    def bpmn2_LaneSet140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_LaneSet__bpmn2_LaneSet140", None)
        self.__bpmn2_LaneSet140 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Lane"):
                    opp_val = getattr(item, "bpmn2_Lane", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Lane", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Lane"):
                    opp_val = getattr(item, "bpmn2_Lane", None)
                    
                    setattr(item, "bpmn2_Lane", self)
                    

    @property
    def bpmn2_LaneSet(self):
        return self.__bpmn2_LaneSet

    @bpmn2_LaneSet.setter
    def bpmn2_LaneSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_LaneSet__bpmn2_LaneSet", None)
        self.__bpmn2_LaneSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_FlowElementsContainer130"):
                opp_val = getattr(old_value, "bpmn2_FlowElementsContainer130", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_FlowElementsContainer130"):
                opp_val = getattr(value, "bpmn2_FlowElementsContainer130", None)
                if opp_val is None:
                    setattr(value, "bpmn2_FlowElementsContainer130", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_LaneSet143(self):
        return self.__bpmn2_LaneSet143

    @bpmn2_LaneSet143.setter
    def bpmn2_LaneSet143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_LaneSet__bpmn2_LaneSet143", None)
        self.__bpmn2_LaneSet143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Lane142"):
                opp_val = getattr(old_value, "bpmn2_Lane142", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Lane142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Lane142"):
                opp_val = getattr(value, "bpmn2_Lane142", None)
                setattr(value, "bpmn2_Lane142", self)

class bpmn2_Documentation(BaseElement):

    def __init__(self, text: str, textFormat: str, bpmn2_Documentation: "bpmn2_BaseElement" = None):
        self.text = text
        self.textFormat = textFormat
        self.bpmn2_Documentation = bpmn2_Documentation
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def textFormat(self) -> str:
        return self.__textFormat

    @textFormat.setter
    def textFormat(self, textFormat: str):
        self.__textFormat = textFormat

    @property
    def bpmn2_Documentation(self):
        return self.__bpmn2_Documentation

    @bpmn2_Documentation.setter
    def bpmn2_Documentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Documentation__bpmn2_Documentation", None)
        self.__bpmn2_Documentation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_BaseElement7"):
                opp_val = getattr(old_value, "bpmn2_BaseElement7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_BaseElement7"):
                opp_val = getattr(value, "bpmn2_BaseElement7", None)
                if opp_val is None:
                    setattr(value, "bpmn2_BaseElement7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_Expression(BaseElement):

    pass
class bpmn2_InputOutputSpecification(BaseElement):

    pass
class bpmn2_CorrelationPropertyRetrievalExpression(BaseElement):

    pass
class bpmn2_ParticipantAssociation(BaseElement):

    pass
class bpmn2_CorrelationSubscription(BaseElement):

    pass
class bpmn2_ResourceRole(BaseElement):

    def __init__(self, name: str, bpmn2_ResourceRole: "bpmn2_GlobalTask" = None, bpmn2_ResourceRole93: "bpmn2_Resource" = None, bpmn2_ResourceRole95: set["bpmn2_ResourceParameterBinding"] = None, bpmn2_ResourceRole97: "bpmn2_ResourceAssignmentExpression" = None, bpmn2_ResourceRole123: "bpmn2_Process" = None, bpmn2_ResourceRole267: "bpmn2_Activity" = None):
        self.name = name
        self.bpmn2_ResourceRole = bpmn2_ResourceRole
        self.bpmn2_ResourceRole93 = bpmn2_ResourceRole93
        self.bpmn2_ResourceRole95 = bpmn2_ResourceRole95 if bpmn2_ResourceRole95 is not None else set()
        self.bpmn2_ResourceRole97 = bpmn2_ResourceRole97
        self.bpmn2_ResourceRole123 = bpmn2_ResourceRole123
        self.bpmn2_ResourceRole267 = bpmn2_ResourceRole267
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_ResourceRole123(self):
        return self.__bpmn2_ResourceRole123

    @bpmn2_ResourceRole123.setter
    def bpmn2_ResourceRole123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ResourceRole__bpmn2_ResourceRole123", None)
        self.__bpmn2_ResourceRole123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Process122"):
                opp_val = getattr(old_value, "bpmn2_Process122", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Process122"):
                opp_val = getattr(value, "bpmn2_Process122", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Process122", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_ResourceRole93(self):
        return self.__bpmn2_ResourceRole93

    @bpmn2_ResourceRole93.setter
    def bpmn2_ResourceRole93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ResourceRole__bpmn2_ResourceRole93", None)
        self.__bpmn2_ResourceRole93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Resource"):
                opp_val = getattr(old_value, "bpmn2_Resource", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Resource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Resource"):
                opp_val = getattr(value, "bpmn2_Resource", None)
                setattr(value, "bpmn2_Resource", self)

    @property
    def bpmn2_ResourceRole267(self):
        return self.__bpmn2_ResourceRole267

    @bpmn2_ResourceRole267.setter
    def bpmn2_ResourceRole267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ResourceRole__bpmn2_ResourceRole267", None)
        self.__bpmn2_ResourceRole267 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Activity266"):
                opp_val = getattr(old_value, "bpmn2_Activity266", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Activity266"):
                opp_val = getattr(value, "bpmn2_Activity266", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Activity266", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_ResourceRole95(self):
        return self.__bpmn2_ResourceRole95

    @bpmn2_ResourceRole95.setter
    def bpmn2_ResourceRole95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ResourceRole__bpmn2_ResourceRole95", None)
        self.__bpmn2_ResourceRole95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_ResourceParameterBinding"):
                    opp_val = getattr(item, "bpmn2_ResourceParameterBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_ResourceParameterBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_ResourceParameterBinding"):
                    opp_val = getattr(item, "bpmn2_ResourceParameterBinding", None)
                    
                    setattr(item, "bpmn2_ResourceParameterBinding", self)
                    

    @property
    def bpmn2_ResourceRole97(self):
        return self.__bpmn2_ResourceRole97

    @bpmn2_ResourceRole97.setter
    def bpmn2_ResourceRole97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ResourceRole__bpmn2_ResourceRole97", None)
        self.__bpmn2_ResourceRole97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ResourceAssignmentExpression"):
                opp_val = getattr(old_value, "bpmn2_ResourceAssignmentExpression", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ResourceAssignmentExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ResourceAssignmentExpression"):
                opp_val = getattr(value, "bpmn2_ResourceAssignmentExpression", None)
                setattr(value, "bpmn2_ResourceAssignmentExpression", self)

    @property
    def bpmn2_ResourceRole(self):
        return self.__bpmn2_ResourceRole

    @bpmn2_ResourceRole.setter
    def bpmn2_ResourceRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ResourceRole__bpmn2_ResourceRole", None)
        self.__bpmn2_ResourceRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_GlobalTask"):
                opp_val = getattr(old_value, "bpmn2_GlobalTask", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_GlobalTask"):
                opp_val = getattr(value, "bpmn2_GlobalTask", None)
                if opp_val is None:
                    setattr(value, "bpmn2_GlobalTask", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_Definitions(BaseElement):

    def __init__(self, exporter: str, exporterVersion: str, name: str, targetNamespace: str, expressionLanguage: str, typeLanguage: str, bpmn2_Definitions475: set["bpmn2_Extension"] = None, bpmn2_Definitions478: set["bpmn2_Relationship"] = None, bpmn2_Definitions481: set["bpmn2_RootElement"] = None, bpmn2_Definitions483: set["bpmn2_BPMNDiagram"] = None, bpmn2_Definitions: set["bpmn2_Import"] = None):
        self.exporter = exporter
        self.exporterVersion = exporterVersion
        self.name = name
        self.targetNamespace = targetNamespace
        self.expressionLanguage = expressionLanguage
        self.typeLanguage = typeLanguage
        self.bpmn2_Definitions475 = bpmn2_Definitions475 if bpmn2_Definitions475 is not None else set()
        self.bpmn2_Definitions478 = bpmn2_Definitions478 if bpmn2_Definitions478 is not None else set()
        self.bpmn2_Definitions481 = bpmn2_Definitions481 if bpmn2_Definitions481 is not None else set()
        self.bpmn2_Definitions483 = bpmn2_Definitions483 if bpmn2_Definitions483 is not None else set()
        self.bpmn2_Definitions = bpmn2_Definitions if bpmn2_Definitions is not None else set()
        
    @property
    def exporter(self) -> str:
        return self.__exporter

    @exporter.setter
    def exporter(self, exporter: str):
        self.__exporter = exporter

    @property
    def expressionLanguage(self) -> str:
        return self.__expressionLanguage

    @expressionLanguage.setter
    def expressionLanguage(self, expressionLanguage: str):
        self.__expressionLanguage = expressionLanguage

    @property
    def exporterVersion(self) -> str:
        return self.__exporterVersion

    @exporterVersion.setter
    def exporterVersion(self, exporterVersion: str):
        self.__exporterVersion = exporterVersion

    @property
    def typeLanguage(self) -> str:
        return self.__typeLanguage

    @typeLanguage.setter
    def typeLanguage(self, typeLanguage: str):
        self.__typeLanguage = typeLanguage

    @property
    def targetNamespace(self) -> str:
        return self.__targetNamespace

    @targetNamespace.setter
    def targetNamespace(self, targetNamespace: str):
        self.__targetNamespace = targetNamespace

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_Definitions481(self):
        return self.__bpmn2_Definitions481

    @bpmn2_Definitions481.setter
    def bpmn2_Definitions481(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Definitions__bpmn2_Definitions481", None)
        self.__bpmn2_Definitions481 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_RootElement"):
                    opp_val = getattr(item, "bpmn2_RootElement", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_RootElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_RootElement"):
                    opp_val = getattr(item, "bpmn2_RootElement", None)
                    
                    setattr(item, "bpmn2_RootElement", self)
                    

    @property
    def bpmn2_Definitions(self):
        return self.__bpmn2_Definitions

    @bpmn2_Definitions.setter
    def bpmn2_Definitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Definitions__bpmn2_Definitions", None)
        self.__bpmn2_Definitions = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Import473"):
                    opp_val = getattr(item, "bpmn2_Import473", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Import473", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Import473"):
                    opp_val = getattr(item, "bpmn2_Import473", None)
                    
                    setattr(item, "bpmn2_Import473", self)
                    

    @property
    def bpmn2_Definitions478(self):
        return self.__bpmn2_Definitions478

    @bpmn2_Definitions478.setter
    def bpmn2_Definitions478(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Definitions__bpmn2_Definitions478", None)
        self.__bpmn2_Definitions478 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Relationship479"):
                    opp_val = getattr(item, "bpmn2_Relationship479", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Relationship479", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Relationship479"):
                    opp_val = getattr(item, "bpmn2_Relationship479", None)
                    
                    setattr(item, "bpmn2_Relationship479", self)
                    

    @property
    def bpmn2_Definitions483(self):
        return self.__bpmn2_Definitions483

    @bpmn2_Definitions483.setter
    def bpmn2_Definitions483(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Definitions__bpmn2_Definitions483", None)
        self.__bpmn2_Definitions483 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_BPMNDiagram"):
                    opp_val = getattr(item, "bpmn2_BPMNDiagram", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_BPMNDiagram", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_BPMNDiagram"):
                    opp_val = getattr(item, "bpmn2_BPMNDiagram", None)
                    
                    setattr(item, "bpmn2_BPMNDiagram", self)
                    

    @property
    def bpmn2_Definitions475(self):
        return self.__bpmn2_Definitions475

    @bpmn2_Definitions475.setter
    def bpmn2_Definitions475(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Definitions__bpmn2_Definitions475", None)
        self.__bpmn2_Definitions475 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Extension476"):
                    opp_val = getattr(item, "bpmn2_Extension476", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Extension476", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Extension476"):
                    opp_val = getattr(item, "bpmn2_Extension476", None)
                    
                    setattr(item, "bpmn2_Extension476", self)
                    

class bpmn2_CorrelationPropertyBinding(BaseElement):

    pass
class bpmn2_MessageFlowAssociation(BaseElement):

    pass
class bpmn2_FlowElementsContainer(BaseElement):

    pass
class bpmn2_CategoryValue(BaseElement):

    def __init__(self, value: str, CategoryValue: "bpmn2_FlowElement" = None, categoryValueRef: set["bpmn2_FlowElement"] = None, bpmn2_CategoryValue: "bpmn2_Group" = None, bpmn2_CategoryValue418: "bpmn2_Category" = None):
        self.value = value
        self.CategoryValue = CategoryValue
        self.categoryValueRef = categoryValueRef if categoryValueRef is not None else set()
        self.bpmn2_CategoryValue = bpmn2_CategoryValue
        self.bpmn2_CategoryValue418 = bpmn2_CategoryValue418
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def categoryValueRef(self):
        return self.__categoryValueRef

    @categoryValueRef.setter
    def categoryValueRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CategoryValue__categoryValueRef", None)
        self.__categoryValueRef = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FlowElement"):
                    opp_val = getattr(item, "FlowElement", None)
                    
                    if opp_val == self:
                        setattr(item, "FlowElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FlowElement"):
                    opp_val = getattr(item, "FlowElement", None)
                    
                    setattr(item, "FlowElement", self)
                    

    @property
    def bpmn2_CategoryValue418(self):
        return self.__bpmn2_CategoryValue418

    @bpmn2_CategoryValue418.setter
    def bpmn2_CategoryValue418(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CategoryValue__bpmn2_CategoryValue418", None)
        self.__bpmn2_CategoryValue418 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Category"):
                opp_val = getattr(old_value, "bpmn2_Category", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Category"):
                opp_val = getattr(value, "bpmn2_Category", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Category", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_CategoryValue(self):
        return self.__bpmn2_CategoryValue

    @bpmn2_CategoryValue.setter
    def bpmn2_CategoryValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CategoryValue__bpmn2_CategoryValue", None)
        self.__bpmn2_CategoryValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Group"):
                opp_val = getattr(old_value, "bpmn2_Group", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Group", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Group"):
                opp_val = getattr(value, "bpmn2_Group", None)
                setattr(value, "bpmn2_Group", self)

    @property
    def CategoryValue(self):
        return self.__CategoryValue

    @CategoryValue.setter
    def CategoryValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CategoryValue__CategoryValue", None)
        self.__CategoryValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "categorizedFlowElements"):
                opp_val = getattr(old_value, "categorizedFlowElements", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "categorizedFlowElements"):
                opp_val = getattr(value, "categorizedFlowElements", None)
                if opp_val is None:
                    setattr(value, "categorizedFlowElements", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_Operation(BaseElement):

    def __init__(self, name: str, bpmn2_Operation: "bpmn2_Interface" = None, bpmn2_Operation26: "bpmn2_EObject" = None, bpmn2_Operation19: "bpmn2_Message" = None, bpmn2_Operation21: "bpmn2_Message" = None, bpmn2_Operation24: set["bpmn2_Error"] = None, bpmn2_Operation91: "bpmn2_InputOutputBinding" = None, bpmn2_Operation372: "bpmn2_MessageEventDefinition" = None, bpmn2_Operation420: "bpmn2_ServiceTask" = None, bpmn2_Operation461: "bpmn2_SendTask" = None, bpmn2_Operation466: "bpmn2_ReceiveTask" = None):
        self.name = name
        self.bpmn2_Operation = bpmn2_Operation
        self.bpmn2_Operation26 = bpmn2_Operation26
        self.bpmn2_Operation19 = bpmn2_Operation19
        self.bpmn2_Operation21 = bpmn2_Operation21
        self.bpmn2_Operation24 = bpmn2_Operation24 if bpmn2_Operation24 is not None else set()
        self.bpmn2_Operation91 = bpmn2_Operation91
        self.bpmn2_Operation372 = bpmn2_Operation372
        self.bpmn2_Operation420 = bpmn2_Operation420
        self.bpmn2_Operation461 = bpmn2_Operation461
        self.bpmn2_Operation466 = bpmn2_Operation466
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_Operation19(self):
        return self.__bpmn2_Operation19

    @bpmn2_Operation19.setter
    def bpmn2_Operation19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Operation__bpmn2_Operation19", None)
        self.__bpmn2_Operation19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Message"):
                opp_val = getattr(old_value, "bpmn2_Message", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Message", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Message"):
                opp_val = getattr(value, "bpmn2_Message", None)
                setattr(value, "bpmn2_Message", self)

    @property
    def bpmn2_Operation91(self):
        return self.__bpmn2_Operation91

    @bpmn2_Operation91.setter
    def bpmn2_Operation91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Operation__bpmn2_Operation91", None)
        self.__bpmn2_Operation91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_InputOutputBinding90"):
                opp_val = getattr(old_value, "bpmn2_InputOutputBinding90", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_InputOutputBinding90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_InputOutputBinding90"):
                opp_val = getattr(value, "bpmn2_InputOutputBinding90", None)
                setattr(value, "bpmn2_InputOutputBinding90", self)

    @property
    def bpmn2_Operation466(self):
        return self.__bpmn2_Operation466

    @bpmn2_Operation466.setter
    def bpmn2_Operation466(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Operation__bpmn2_Operation466", None)
        self.__bpmn2_Operation466 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ReceiveTask"):
                opp_val = getattr(old_value, "bpmn2_ReceiveTask", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ReceiveTask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ReceiveTask"):
                opp_val = getattr(value, "bpmn2_ReceiveTask", None)
                setattr(value, "bpmn2_ReceiveTask", self)

    @property
    def bpmn2_Operation372(self):
        return self.__bpmn2_Operation372

    @bpmn2_Operation372.setter
    def bpmn2_Operation372(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Operation__bpmn2_Operation372", None)
        self.__bpmn2_Operation372 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_MessageEventDefinition371"):
                opp_val = getattr(old_value, "bpmn2_MessageEventDefinition371", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_MessageEventDefinition371", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_MessageEventDefinition371"):
                opp_val = getattr(value, "bpmn2_MessageEventDefinition371", None)
                setattr(value, "bpmn2_MessageEventDefinition371", self)

    @property
    def bpmn2_Operation420(self):
        return self.__bpmn2_Operation420

    @bpmn2_Operation420.setter
    def bpmn2_Operation420(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Operation__bpmn2_Operation420", None)
        self.__bpmn2_Operation420 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ServiceTask"):
                opp_val = getattr(old_value, "bpmn2_ServiceTask", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ServiceTask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ServiceTask"):
                opp_val = getattr(value, "bpmn2_ServiceTask", None)
                setattr(value, "bpmn2_ServiceTask", self)

    @property
    def bpmn2_Operation(self):
        return self.__bpmn2_Operation

    @bpmn2_Operation.setter
    def bpmn2_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Operation__bpmn2_Operation", None)
        self.__bpmn2_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Interface"):
                opp_val = getattr(old_value, "bpmn2_Interface", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Interface"):
                opp_val = getattr(value, "bpmn2_Interface", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Interface", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Operation24(self):
        return self.__bpmn2_Operation24

    @bpmn2_Operation24.setter
    def bpmn2_Operation24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Operation__bpmn2_Operation24", None)
        self.__bpmn2_Operation24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Error"):
                    opp_val = getattr(item, "bpmn2_Error", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Error", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Error"):
                    opp_val = getattr(item, "bpmn2_Error", None)
                    
                    setattr(item, "bpmn2_Error", self)
                    

    @property
    def bpmn2_Operation461(self):
        return self.__bpmn2_Operation461

    @bpmn2_Operation461.setter
    def bpmn2_Operation461(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Operation__bpmn2_Operation461", None)
        self.__bpmn2_Operation461 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_SendTask"):
                opp_val = getattr(old_value, "bpmn2_SendTask", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_SendTask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_SendTask"):
                opp_val = getattr(value, "bpmn2_SendTask", None)
                setattr(value, "bpmn2_SendTask", self)

    @property
    def bpmn2_Operation26(self):
        return self.__bpmn2_Operation26

    @bpmn2_Operation26.setter
    def bpmn2_Operation26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Operation__bpmn2_Operation26", None)
        self.__bpmn2_Operation26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_EObject27"):
                opp_val = getattr(old_value, "bpmn2_EObject27", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_EObject27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_EObject27"):
                opp_val = getattr(value, "bpmn2_EObject27", None)
                setattr(value, "bpmn2_EObject27", self)

    @property
    def bpmn2_Operation21(self):
        return self.__bpmn2_Operation21

    @bpmn2_Operation21.setter
    def bpmn2_Operation21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Operation__bpmn2_Operation21", None)
        self.__bpmn2_Operation21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Message22"):
                opp_val = getattr(old_value, "bpmn2_Message22", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Message22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Message22"):
                opp_val = getattr(value, "bpmn2_Message22", None)
                setattr(value, "bpmn2_Message22", self)

class bpmn2_DataAssociation(BaseElement):

    pass
class bpmn2_ConversationLink(BaseElement):

    def __init__(self, name: str, bpmn2_ConversationLink: "bpmn2_Collaboration" = None, ConversationLink: "bpmn2_InteractionNode" = None, ConversationLink202: "bpmn2_InteractionNode" = None, outgoingConversationLinks: "bpmn2_InteractionNode" = None, incomingConversationLinks: "bpmn2_InteractionNode" = None):
        self.name = name
        self.bpmn2_ConversationLink = bpmn2_ConversationLink
        self.ConversationLink = ConversationLink
        self.ConversationLink202 = ConversationLink202
        self.outgoingConversationLinks = outgoingConversationLinks
        self.incomingConversationLinks = incomingConversationLinks
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ConversationLink(self):
        return self.__ConversationLink

    @ConversationLink.setter
    def ConversationLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ConversationLink__ConversationLink", None)
        self.__ConversationLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targetRef199"):
                opp_val = getattr(old_value, "targetRef199", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targetRef199"):
                opp_val = getattr(value, "targetRef199", None)
                if opp_val is None:
                    setattr(value, "targetRef199", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoingConversationLinks(self):
        return self.__outgoingConversationLinks

    @outgoingConversationLinks.setter
    def outgoingConversationLinks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ConversationLink__outgoingConversationLinks", None)
        self.__outgoingConversationLinks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InteractionNode"):
                opp_val = getattr(old_value, "InteractionNode", None)
                if opp_val == self:
                    setattr(old_value, "InteractionNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InteractionNode"):
                opp_val = getattr(value, "InteractionNode", None)
                setattr(value, "InteractionNode", self)

    @property
    def incomingConversationLinks(self):
        return self.__incomingConversationLinks

    @incomingConversationLinks.setter
    def incomingConversationLinks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ConversationLink__incomingConversationLinks", None)
        self.__incomingConversationLinks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InteractionNode205"):
                opp_val = getattr(old_value, "InteractionNode205", None)
                if opp_val == self:
                    setattr(old_value, "InteractionNode205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InteractionNode205"):
                opp_val = getattr(value, "InteractionNode205", None)
                setattr(value, "InteractionNode205", self)

    @property
    def bpmn2_ConversationLink(self):
        return self.__bpmn2_ConversationLink

    @bpmn2_ConversationLink.setter
    def bpmn2_ConversationLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ConversationLink__bpmn2_ConversationLink", None)
        self.__bpmn2_ConversationLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Collaboration181"):
                opp_val = getattr(old_value, "bpmn2_Collaboration181", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Collaboration181"):
                opp_val = getattr(value, "bpmn2_Collaboration181", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Collaboration181", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ConversationLink202(self):
        return self.__ConversationLink202

    @ConversationLink202.setter
    def ConversationLink202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ConversationLink__ConversationLink202", None)
        self.__ConversationLink202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceRef201"):
                opp_val = getattr(old_value, "sourceRef201", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceRef201"):
                opp_val = getattr(value, "sourceRef201", None)
                if opp_val is None:
                    setattr(value, "sourceRef201", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_Participant(BaseElement, InteractionNode):

    def __init__(self, name: str, bpmn2_Participant: "bpmn2_Collaboration" = None, bpmn2_Participant184: "bpmn2_ParticipantAssociation" = None, bpmn2_Participant187: "bpmn2_ParticipantAssociation" = None, bpmn2_Participant189: set["bpmn2_Interface"] = None, bpmn2_Participant192: "bpmn2_ParticipantMultiplicity" = None, bpmn2_Participant194: set["bpmn2_EndPoint"] = None, bpmn2_Participant196: "bpmn2_Process" = None, bpmn2_Participant228: "bpmn2_ConversationNode" = None, bpmn2_Participant389: "bpmn2_PartnerEntity" = None, bpmn2_Participant391: "bpmn2_PartnerRole" = None, bpmn2_Participant393: "bpmn2_ChoreographyActivity" = None, bpmn2_Participant396: "bpmn2_ChoreographyActivity" = None, bpmn2_Participant410: "bpmn2_GlobalChoreographyTask" = None):
        self.name = name
        self.bpmn2_Participant = bpmn2_Participant
        self.bpmn2_Participant184 = bpmn2_Participant184
        self.bpmn2_Participant187 = bpmn2_Participant187
        self.bpmn2_Participant189 = bpmn2_Participant189 if bpmn2_Participant189 is not None else set()
        self.bpmn2_Participant192 = bpmn2_Participant192
        self.bpmn2_Participant194 = bpmn2_Participant194 if bpmn2_Participant194 is not None else set()
        self.bpmn2_Participant196 = bpmn2_Participant196
        self.bpmn2_Participant228 = bpmn2_Participant228
        self.bpmn2_Participant389 = bpmn2_Participant389
        self.bpmn2_Participant391 = bpmn2_Participant391
        self.bpmn2_Participant393 = bpmn2_Participant393
        self.bpmn2_Participant396 = bpmn2_Participant396
        self.bpmn2_Participant410 = bpmn2_Participant410
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_Participant196(self):
        return self.__bpmn2_Participant196

    @bpmn2_Participant196.setter
    def bpmn2_Participant196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant196", None)
        self.__bpmn2_Participant196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Process197"):
                opp_val = getattr(old_value, "bpmn2_Process197", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Process197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Process197"):
                opp_val = getattr(value, "bpmn2_Process197", None)
                setattr(value, "bpmn2_Process197", self)

    @property
    def bpmn2_Participant391(self):
        return self.__bpmn2_Participant391

    @bpmn2_Participant391.setter
    def bpmn2_Participant391(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant391", None)
        self.__bpmn2_Participant391 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_PartnerRole"):
                opp_val = getattr(old_value, "bpmn2_PartnerRole", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_PartnerRole"):
                opp_val = getattr(value, "bpmn2_PartnerRole", None)
                if opp_val is None:
                    setattr(value, "bpmn2_PartnerRole", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Participant396(self):
        return self.__bpmn2_Participant396

    @bpmn2_Participant396.setter
    def bpmn2_Participant396(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant396", None)
        self.__bpmn2_Participant396 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ChoreographyActivity395"):
                opp_val = getattr(old_value, "bpmn2_ChoreographyActivity395", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ChoreographyActivity395", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ChoreographyActivity395"):
                opp_val = getattr(value, "bpmn2_ChoreographyActivity395", None)
                setattr(value, "bpmn2_ChoreographyActivity395", self)

    @property
    def bpmn2_Participant189(self):
        return self.__bpmn2_Participant189

    @bpmn2_Participant189.setter
    def bpmn2_Participant189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant189", None)
        self.__bpmn2_Participant189 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Interface190"):
                    opp_val = getattr(item, "bpmn2_Interface190", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Interface190", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Interface190"):
                    opp_val = getattr(item, "bpmn2_Interface190", None)
                    
                    setattr(item, "bpmn2_Interface190", self)
                    

    @property
    def bpmn2_Participant187(self):
        return self.__bpmn2_Participant187

    @bpmn2_Participant187.setter
    def bpmn2_Participant187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant187", None)
        self.__bpmn2_Participant187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ParticipantAssociation186"):
                opp_val = getattr(old_value, "bpmn2_ParticipantAssociation186", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ParticipantAssociation186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ParticipantAssociation186"):
                opp_val = getattr(value, "bpmn2_ParticipantAssociation186", None)
                setattr(value, "bpmn2_ParticipantAssociation186", self)

    @property
    def bpmn2_Participant194(self):
        return self.__bpmn2_Participant194

    @bpmn2_Participant194.setter
    def bpmn2_Participant194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant194", None)
        self.__bpmn2_Participant194 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_EndPoint"):
                    opp_val = getattr(item, "bpmn2_EndPoint", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_EndPoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_EndPoint"):
                    opp_val = getattr(item, "bpmn2_EndPoint", None)
                    
                    setattr(item, "bpmn2_EndPoint", self)
                    

    @property
    def bpmn2_Participant192(self):
        return self.__bpmn2_Participant192

    @bpmn2_Participant192.setter
    def bpmn2_Participant192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant192", None)
        self.__bpmn2_Participant192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ParticipantMultiplicity"):
                opp_val = getattr(old_value, "bpmn2_ParticipantMultiplicity", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ParticipantMultiplicity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ParticipantMultiplicity"):
                opp_val = getattr(value, "bpmn2_ParticipantMultiplicity", None)
                setattr(value, "bpmn2_ParticipantMultiplicity", self)

    @property
    def bpmn2_Participant389(self):
        return self.__bpmn2_Participant389

    @bpmn2_Participant389.setter
    def bpmn2_Participant389(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant389", None)
        self.__bpmn2_Participant389 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_PartnerEntity"):
                opp_val = getattr(old_value, "bpmn2_PartnerEntity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_PartnerEntity"):
                opp_val = getattr(value, "bpmn2_PartnerEntity", None)
                if opp_val is None:
                    setattr(value, "bpmn2_PartnerEntity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Participant(self):
        return self.__bpmn2_Participant

    @bpmn2_Participant.setter
    def bpmn2_Participant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant", None)
        self.__bpmn2_Participant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Collaboration173"):
                opp_val = getattr(old_value, "bpmn2_Collaboration173", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Collaboration173"):
                opp_val = getattr(value, "bpmn2_Collaboration173", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Collaboration173", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Participant410(self):
        return self.__bpmn2_Participant410

    @bpmn2_Participant410.setter
    def bpmn2_Participant410(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant410", None)
        self.__bpmn2_Participant410 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_GlobalChoreographyTask"):
                opp_val = getattr(old_value, "bpmn2_GlobalChoreographyTask", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_GlobalChoreographyTask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_GlobalChoreographyTask"):
                opp_val = getattr(value, "bpmn2_GlobalChoreographyTask", None)
                setattr(value, "bpmn2_GlobalChoreographyTask", self)

    @property
    def bpmn2_Participant393(self):
        return self.__bpmn2_Participant393

    @bpmn2_Participant393.setter
    def bpmn2_Participant393(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant393", None)
        self.__bpmn2_Participant393 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ChoreographyActivity"):
                opp_val = getattr(old_value, "bpmn2_ChoreographyActivity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ChoreographyActivity"):
                opp_val = getattr(value, "bpmn2_ChoreographyActivity", None)
                if opp_val is None:
                    setattr(value, "bpmn2_ChoreographyActivity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Participant184(self):
        return self.__bpmn2_Participant184

    @bpmn2_Participant184.setter
    def bpmn2_Participant184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant184", None)
        self.__bpmn2_Participant184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ParticipantAssociation183"):
                opp_val = getattr(old_value, "bpmn2_ParticipantAssociation183", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ParticipantAssociation183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ParticipantAssociation183"):
                opp_val = getattr(value, "bpmn2_ParticipantAssociation183", None)
                setattr(value, "bpmn2_ParticipantAssociation183", self)

    @property
    def bpmn2_Participant228(self):
        return self.__bpmn2_Participant228

    @bpmn2_Participant228.setter
    def bpmn2_Participant228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant228", None)
        self.__bpmn2_Participant228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ConversationNode227"):
                opp_val = getattr(old_value, "bpmn2_ConversationNode227", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ConversationNode227"):
                opp_val = getattr(value, "bpmn2_ConversationNode227", None)
                if opp_val is None:
                    setattr(value, "bpmn2_ConversationNode227", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_ResourceParameter(BaseElement):

    def __init__(self, name: str, isRequired: bool, bpmn2_ResourceParameter107: "bpmn2_ResourceParameterBinding" = None, bpmn2_ResourceParameter: "bpmn2_Resource" = None, bpmn2_ResourceParameter101: "bpmn2_ItemDefinition" = None):
        self.name = name
        self.isRequired = isRequired
        self.bpmn2_ResourceParameter107 = bpmn2_ResourceParameter107
        self.bpmn2_ResourceParameter = bpmn2_ResourceParameter
        self.bpmn2_ResourceParameter101 = bpmn2_ResourceParameter101
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isRequired(self) -> bool:
        return self.__isRequired

    @isRequired.setter
    def isRequired(self, isRequired: bool):
        self.__isRequired = isRequired

    @property
    def bpmn2_ResourceParameter(self):
        return self.__bpmn2_ResourceParameter

    @bpmn2_ResourceParameter.setter
    def bpmn2_ResourceParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ResourceParameter__bpmn2_ResourceParameter", None)
        self.__bpmn2_ResourceParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Resource99"):
                opp_val = getattr(old_value, "bpmn2_Resource99", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Resource99"):
                opp_val = getattr(value, "bpmn2_Resource99", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Resource99", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_ResourceParameter107(self):
        return self.__bpmn2_ResourceParameter107

    @bpmn2_ResourceParameter107.setter
    def bpmn2_ResourceParameter107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ResourceParameter__bpmn2_ResourceParameter107", None)
        self.__bpmn2_ResourceParameter107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ResourceParameterBinding106"):
                opp_val = getattr(old_value, "bpmn2_ResourceParameterBinding106", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ResourceParameterBinding106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ResourceParameterBinding106"):
                opp_val = getattr(value, "bpmn2_ResourceParameterBinding106", None)
                setattr(value, "bpmn2_ResourceParameterBinding106", self)

    @property
    def bpmn2_ResourceParameter101(self):
        return self.__bpmn2_ResourceParameter101

    @bpmn2_ResourceParameter101.setter
    def bpmn2_ResourceParameter101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ResourceParameter__bpmn2_ResourceParameter101", None)
        self.__bpmn2_ResourceParameter101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemDefinition102"):
                opp_val = getattr(old_value, "bpmn2_ItemDefinition102", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemDefinition102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemDefinition102"):
                opp_val = getattr(value, "bpmn2_ItemDefinition102", None)
                setattr(value, "bpmn2_ItemDefinition102", self)

class bpmn2_ComplexBehaviorDefinition(BaseElement):

    pass
class bpmn2_OutputSet(BaseElement):

    def __init__(self, name: str, OutputSet: "bpmn2_InputSet" = None, outputSetRefs: set["bpmn2_DataOutput"] = None, outputSetWithOptional: set["bpmn2_DataOutput"] = None, bpmn2_OutputSet: "bpmn2_InputOutputSpecification" = None, OutputSet78: "bpmn2_DataOutput" = None, OutputSet80: "bpmn2_DataOutput" = None, OutputSet82: "bpmn2_DataOutput" = None, bpmn2_OutputSet88: "bpmn2_InputOutputBinding" = None, outputSetWithWhileExecuting: set["bpmn2_DataOutput"] = None, outputSetRefs75: set["bpmn2_InputSet"] = None, bpmn2_OutputSet284: "bpmn2_CatchEvent" = None):
        self.name = name
        self.OutputSet = OutputSet
        self.outputSetRefs = outputSetRefs if outputSetRefs is not None else set()
        self.outputSetWithOptional = outputSetWithOptional if outputSetWithOptional is not None else set()
        self.bpmn2_OutputSet = bpmn2_OutputSet
        self.OutputSet78 = OutputSet78
        self.OutputSet80 = OutputSet80
        self.OutputSet82 = OutputSet82
        self.bpmn2_OutputSet88 = bpmn2_OutputSet88
        self.outputSetWithWhileExecuting = outputSetWithWhileExecuting if outputSetWithWhileExecuting is not None else set()
        self.outputSetRefs75 = outputSetRefs75 if outputSetRefs75 is not None else set()
        self.bpmn2_OutputSet284 = bpmn2_OutputSet284
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_OutputSet284(self):
        return self.__bpmn2_OutputSet284

    @bpmn2_OutputSet284.setter
    def bpmn2_OutputSet284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_OutputSet__bpmn2_OutputSet284", None)
        self.__bpmn2_OutputSet284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CatchEvent"):
                opp_val = getattr(old_value, "bpmn2_CatchEvent", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_CatchEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CatchEvent"):
                opp_val = getattr(value, "bpmn2_CatchEvent", None)
                setattr(value, "bpmn2_CatchEvent", self)

    @property
    def bpmn2_OutputSet(self):
        return self.__bpmn2_OutputSet

    @bpmn2_OutputSet.setter
    def bpmn2_OutputSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_OutputSet__bpmn2_OutputSet", None)
        self.__bpmn2_OutputSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_InputOutputSpecification48"):
                opp_val = getattr(old_value, "bpmn2_InputOutputSpecification48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_InputOutputSpecification48"):
                opp_val = getattr(value, "bpmn2_InputOutputSpecification48", None)
                if opp_val is None:
                    setattr(value, "bpmn2_InputOutputSpecification48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outputSetWithOptional(self):
        return self.__outputSetWithOptional

    @outputSetWithOptional.setter
    def outputSetWithOptional(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_OutputSet__outputSetWithOptional", None)
        self.__outputSetWithOptional = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataOutput71"):
                    opp_val = getattr(item, "DataOutput71", None)
                    
                    if opp_val == self:
                        setattr(item, "DataOutput71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataOutput71"):
                    opp_val = getattr(item, "DataOutput71", None)
                    
                    setattr(item, "DataOutput71", self)
                    

    @property
    def OutputSet80(self):
        return self.__OutputSet80

    @OutputSet80.setter
    def OutputSet80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_OutputSet__OutputSet80", None)
        self.__OutputSet80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileExecutingOutputRefs"):
                opp_val = getattr(old_value, "whileExecutingOutputRefs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileExecutingOutputRefs"):
                opp_val = getattr(value, "whileExecutingOutputRefs", None)
                if opp_val is None:
                    setattr(value, "whileExecutingOutputRefs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OutputSet(self):
        return self.__OutputSet

    @OutputSet.setter
    def OutputSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_OutputSet__OutputSet", None)
        self.__OutputSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inputSetRefs59"):
                opp_val = getattr(old_value, "inputSetRefs59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inputSetRefs59"):
                opp_val = getattr(value, "inputSetRefs59", None)
                if opp_val is None:
                    setattr(value, "inputSetRefs59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outputSetRefs75(self):
        return self.__outputSetRefs75

    @outputSetRefs75.setter
    def outputSetRefs75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_OutputSet__outputSetRefs75", None)
        self.__outputSetRefs75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputSet76"):
                    opp_val = getattr(item, "InputSet76", None)
                    
                    if opp_val == self:
                        setattr(item, "InputSet76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputSet76"):
                    opp_val = getattr(item, "InputSet76", None)
                    
                    setattr(item, "InputSet76", self)
                    

    @property
    def outputSetWithWhileExecuting(self):
        return self.__outputSetWithWhileExecuting

    @outputSetWithWhileExecuting.setter
    def outputSetWithWhileExecuting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_OutputSet__outputSetWithWhileExecuting", None)
        self.__outputSetWithWhileExecuting = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataOutput73"):
                    opp_val = getattr(item, "DataOutput73", None)
                    
                    if opp_val == self:
                        setattr(item, "DataOutput73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataOutput73"):
                    opp_val = getattr(item, "DataOutput73", None)
                    
                    setattr(item, "DataOutput73", self)
                    

    @property
    def OutputSet78(self):
        return self.__OutputSet78

    @OutputSet78.setter
    def OutputSet78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_OutputSet__OutputSet78", None)
        self.__OutputSet78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "optionalOutputRefs"):
                opp_val = getattr(old_value, "optionalOutputRefs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "optionalOutputRefs"):
                opp_val = getattr(value, "optionalOutputRefs", None)
                if opp_val is None:
                    setattr(value, "optionalOutputRefs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outputSetRefs(self):
        return self.__outputSetRefs

    @outputSetRefs.setter
    def outputSetRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_OutputSet__outputSetRefs", None)
        self.__outputSetRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataOutput"):
                    opp_val = getattr(item, "DataOutput", None)
                    
                    if opp_val == self:
                        setattr(item, "DataOutput", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataOutput"):
                    opp_val = getattr(item, "DataOutput", None)
                    
                    setattr(item, "DataOutput", self)
                    

    @property
    def OutputSet82(self):
        return self.__OutputSet82

    @OutputSet82.setter
    def OutputSet82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_OutputSet__OutputSet82", None)
        self.__OutputSet82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataOutputRefs"):
                opp_val = getattr(old_value, "dataOutputRefs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataOutputRefs"):
                opp_val = getattr(value, "dataOutputRefs", None)
                if opp_val is None:
                    setattr(value, "dataOutputRefs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_OutputSet88(self):
        return self.__bpmn2_OutputSet88

    @bpmn2_OutputSet88.setter
    def bpmn2_OutputSet88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_OutputSet__bpmn2_OutputSet88", None)
        self.__bpmn2_OutputSet88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_InputOutputBinding87"):
                opp_val = getattr(old_value, "bpmn2_InputOutputBinding87", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_InputOutputBinding87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_InputOutputBinding87"):
                opp_val = getattr(value, "bpmn2_InputOutputBinding87", None)
                setattr(value, "bpmn2_InputOutputBinding87", self)

class bpmn2_Lane(BaseElement):

    def __init__(self, name: str, bpmn2_Lane: "bpmn2_LaneSet" = None, bpmn2_Lane142: "bpmn2_LaneSet" = None, bpmn2_Lane145: "bpmn2_BaseElement" = None, lanes: set["bpmn2_FlowNode"] = None, bpmn2_Lane149: "bpmn2_BaseElement" = None, Lane: "bpmn2_FlowNode" = None):
        self.name = name
        self.bpmn2_Lane = bpmn2_Lane
        self.bpmn2_Lane142 = bpmn2_Lane142
        self.bpmn2_Lane145 = bpmn2_Lane145
        self.lanes = lanes if lanes is not None else set()
        self.bpmn2_Lane149 = bpmn2_Lane149
        self.Lane = Lane
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_Lane(self):
        return self.__bpmn2_Lane

    @bpmn2_Lane.setter
    def bpmn2_Lane(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Lane__bpmn2_Lane", None)
        self.__bpmn2_Lane = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_LaneSet140"):
                opp_val = getattr(old_value, "bpmn2_LaneSet140", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_LaneSet140"):
                opp_val = getattr(value, "bpmn2_LaneSet140", None)
                if opp_val is None:
                    setattr(value, "bpmn2_LaneSet140", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Lane142(self):
        return self.__bpmn2_Lane142

    @bpmn2_Lane142.setter
    def bpmn2_Lane142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Lane__bpmn2_Lane142", None)
        self.__bpmn2_Lane142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_LaneSet143"):
                opp_val = getattr(old_value, "bpmn2_LaneSet143", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_LaneSet143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_LaneSet143"):
                opp_val = getattr(value, "bpmn2_LaneSet143", None)
                setattr(value, "bpmn2_LaneSet143", self)

    @property
    def bpmn2_Lane145(self):
        return self.__bpmn2_Lane145

    @bpmn2_Lane145.setter
    def bpmn2_Lane145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Lane__bpmn2_Lane145", None)
        self.__bpmn2_Lane145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_BaseElement146"):
                opp_val = getattr(old_value, "bpmn2_BaseElement146", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_BaseElement146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_BaseElement146"):
                opp_val = getattr(value, "bpmn2_BaseElement146", None)
                setattr(value, "bpmn2_BaseElement146", self)

    @property
    def bpmn2_Lane149(self):
        return self.__bpmn2_Lane149

    @bpmn2_Lane149.setter
    def bpmn2_Lane149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Lane__bpmn2_Lane149", None)
        self.__bpmn2_Lane149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_BaseElement150"):
                opp_val = getattr(old_value, "bpmn2_BaseElement150", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_BaseElement150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_BaseElement150"):
                opp_val = getattr(value, "bpmn2_BaseElement150", None)
                setattr(value, "bpmn2_BaseElement150", self)

    @property
    def Lane(self):
        return self.__Lane

    @Lane.setter
    def Lane(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Lane__Lane", None)
        self.__Lane = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flowNodeRefs"):
                opp_val = getattr(old_value, "flowNodeRefs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flowNodeRefs"):
                opp_val = getattr(value, "flowNodeRefs", None)
                if opp_val is None:
                    setattr(value, "flowNodeRefs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lanes(self):
        return self.__lanes

    @lanes.setter
    def lanes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Lane__lanes", None)
        self.__lanes = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FlowNode"):
                    opp_val = getattr(item, "FlowNode", None)
                    
                    if opp_val == self:
                        setattr(item, "FlowNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FlowNode"):
                    opp_val = getattr(item, "FlowNode", None)
                    
                    setattr(item, "FlowNode", self)
                    

class bpmn2_ItemAwareElement(BaseElement):

    pass
class bpmn2_MessageFlow(BaseElement):

    def __init__(self, name: str, bpmn2_MessageFlow: "bpmn2_Collaboration" = None, bpmn2_MessageFlow208: "bpmn2_MessageFlowAssociation" = None, bpmn2_MessageFlow211: "bpmn2_MessageFlowAssociation" = None, bpmn2_MessageFlow213: "bpmn2_InteractionNode" = None, bpmn2_MessageFlow215: "bpmn2_InteractionNode" = None, bpmn2_MessageFlow218: "bpmn2_Message" = None, bpmn2_MessageFlow231: "bpmn2_ConversationNode" = None, bpmn2_MessageFlow408: "bpmn2_ChoreographyTask" = None):
        self.name = name
        self.bpmn2_MessageFlow = bpmn2_MessageFlow
        self.bpmn2_MessageFlow208 = bpmn2_MessageFlow208
        self.bpmn2_MessageFlow211 = bpmn2_MessageFlow211
        self.bpmn2_MessageFlow213 = bpmn2_MessageFlow213
        self.bpmn2_MessageFlow215 = bpmn2_MessageFlow215
        self.bpmn2_MessageFlow218 = bpmn2_MessageFlow218
        self.bpmn2_MessageFlow231 = bpmn2_MessageFlow231
        self.bpmn2_MessageFlow408 = bpmn2_MessageFlow408
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_MessageFlow213(self):
        return self.__bpmn2_MessageFlow213

    @bpmn2_MessageFlow213.setter
    def bpmn2_MessageFlow213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MessageFlow__bpmn2_MessageFlow213", None)
        self.__bpmn2_MessageFlow213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_InteractionNode"):
                opp_val = getattr(old_value, "bpmn2_InteractionNode", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_InteractionNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_InteractionNode"):
                opp_val = getattr(value, "bpmn2_InteractionNode", None)
                setattr(value, "bpmn2_InteractionNode", self)

    @property
    def bpmn2_MessageFlow408(self):
        return self.__bpmn2_MessageFlow408

    @bpmn2_MessageFlow408.setter
    def bpmn2_MessageFlow408(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MessageFlow__bpmn2_MessageFlow408", None)
        self.__bpmn2_MessageFlow408 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ChoreographyTask"):
                opp_val = getattr(old_value, "bpmn2_ChoreographyTask", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ChoreographyTask"):
                opp_val = getattr(value, "bpmn2_ChoreographyTask", None)
                if opp_val is None:
                    setattr(value, "bpmn2_ChoreographyTask", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_MessageFlow218(self):
        return self.__bpmn2_MessageFlow218

    @bpmn2_MessageFlow218.setter
    def bpmn2_MessageFlow218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MessageFlow__bpmn2_MessageFlow218", None)
        self.__bpmn2_MessageFlow218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Message219"):
                opp_val = getattr(old_value, "bpmn2_Message219", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Message219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Message219"):
                opp_val = getattr(value, "bpmn2_Message219", None)
                setattr(value, "bpmn2_Message219", self)

    @property
    def bpmn2_MessageFlow215(self):
        return self.__bpmn2_MessageFlow215

    @bpmn2_MessageFlow215.setter
    def bpmn2_MessageFlow215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MessageFlow__bpmn2_MessageFlow215", None)
        self.__bpmn2_MessageFlow215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_InteractionNode216"):
                opp_val = getattr(old_value, "bpmn2_InteractionNode216", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_InteractionNode216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_InteractionNode216"):
                opp_val = getattr(value, "bpmn2_InteractionNode216", None)
                setattr(value, "bpmn2_InteractionNode216", self)

    @property
    def bpmn2_MessageFlow(self):
        return self.__bpmn2_MessageFlow

    @bpmn2_MessageFlow.setter
    def bpmn2_MessageFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MessageFlow__bpmn2_MessageFlow", None)
        self.__bpmn2_MessageFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Collaboration175"):
                opp_val = getattr(old_value, "bpmn2_Collaboration175", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Collaboration175"):
                opp_val = getattr(value, "bpmn2_Collaboration175", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Collaboration175", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_MessageFlow211(self):
        return self.__bpmn2_MessageFlow211

    @bpmn2_MessageFlow211.setter
    def bpmn2_MessageFlow211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MessageFlow__bpmn2_MessageFlow211", None)
        self.__bpmn2_MessageFlow211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_MessageFlowAssociation210"):
                opp_val = getattr(old_value, "bpmn2_MessageFlowAssociation210", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_MessageFlowAssociation210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_MessageFlowAssociation210"):
                opp_val = getattr(value, "bpmn2_MessageFlowAssociation210", None)
                setattr(value, "bpmn2_MessageFlowAssociation210", self)

    @property
    def bpmn2_MessageFlow231(self):
        return self.__bpmn2_MessageFlow231

    @bpmn2_MessageFlow231.setter
    def bpmn2_MessageFlow231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MessageFlow__bpmn2_MessageFlow231", None)
        self.__bpmn2_MessageFlow231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ConversationNode230"):
                opp_val = getattr(old_value, "bpmn2_ConversationNode230", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ConversationNode230"):
                opp_val = getattr(value, "bpmn2_ConversationNode230", None)
                if opp_val is None:
                    setattr(value, "bpmn2_ConversationNode230", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_MessageFlow208(self):
        return self.__bpmn2_MessageFlow208

    @bpmn2_MessageFlow208.setter
    def bpmn2_MessageFlow208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MessageFlow__bpmn2_MessageFlow208", None)
        self.__bpmn2_MessageFlow208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_MessageFlowAssociation207"):
                opp_val = getattr(old_value, "bpmn2_MessageFlowAssociation207", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_MessageFlowAssociation207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_MessageFlowAssociation207"):
                opp_val = getattr(value, "bpmn2_MessageFlowAssociation207", None)
                setattr(value, "bpmn2_MessageFlowAssociation207", self)

class bpmn2_RootElement(BaseElement):

    pass
class bpmn2_EObject:

    pass