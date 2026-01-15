from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AssociationDirection(Enum):
    None = "None"
    One = "One"
    Both = "Both"
class RelationshipDirection(Enum):
    None = "None"
    Forward = "Forward"
    Backward = "Backward"
    Both = "Both"
class ItemKind(Enum):
    Physical = "Physical"
    Information = "Information"
class MultiInstanceBehavior(Enum):
    None = "None"
    One = "One"
    All = "All"
    Complex = "Complex"
class EventBasedGatewayType(Enum):
    Parallel = "Parallel"
    Exclusive = "Exclusive"
class ProcessType(Enum):
    None = "None"
    Public = "Public"
    Private = "Private"
class AdHocOrdering(Enum):
    Parallel = "Parallel"
    Sequential = "Sequential"
class GatewayDirection(Enum):
    Unspecified = "Unspecified"
    Converging = "Converging"
    Diverging = "Diverging"
    Mixed = "Mixed"
class ChoreographyLoopType(Enum):
    None = "None"
    Standard = "Standard"
    MultiInstanceSequential = "MultiInstanceSequential"
    MultiInstanceParallel = "MultiInstanceParallel"


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
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

    @property
    def protocol(self) -> str:
        return self.__protocol

    @protocol.setter
    def protocol(self, protocol: str):
        self.__protocol = protocol

class bpmn2_AdHocSubProcess(SubProcess):

    def __init__(self, ordering: str, cancelRemainingInstances: bool, bpmn2_AdHocSubProcess: "bpmn2_Expression" = None):
        self.ordering = ordering
        self.cancelRemainingInstances = cancelRemainingInstances
        self.bpmn2_AdHocSubProcess = bpmn2_AdHocSubProcess
        
    @property
    def ordering(self) -> str:
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering

    @property
    def cancelRemainingInstances(self) -> bool:
        return self.__cancelRemainingInstances

    @cancelRemainingInstances.setter
    def cancelRemainingInstances(self, cancelRemainingInstances: bool):
        self.__cancelRemainingInstances = cancelRemainingInstances

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
            if hasattr(old_value, "bpmn2_Expression476"):
                opp_val = getattr(old_value, "bpmn2_Expression476", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Expression476", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Expression476"):
                opp_val = getattr(value, "bpmn2_Expression476", None)
                setattr(value, "bpmn2_Expression476", self)

class LoopCharacteristics:

    pass
class bpmn2_StandardLoopCharacteristics(LoopCharacteristics):

    def __init__(self, testBefore: bool, bpmn2_StandardLoopCharacteristics: "bpmn2_Expression" = None, bpmn2_StandardLoopCharacteristics461: "bpmn2_Expression" = None):
        self.testBefore = testBefore
        self.bpmn2_StandardLoopCharacteristics = bpmn2_StandardLoopCharacteristics
        self.bpmn2_StandardLoopCharacteristics461 = bpmn2_StandardLoopCharacteristics461
        
    @property
    def testBefore(self) -> bool:
        return self.__testBefore

    @testBefore.setter
    def testBefore(self, testBefore: bool):
        self.__testBefore = testBefore

    @property
    def bpmn2_StandardLoopCharacteristics461(self):
        return self.__bpmn2_StandardLoopCharacteristics461

    @bpmn2_StandardLoopCharacteristics461.setter
    def bpmn2_StandardLoopCharacteristics461(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_StandardLoopCharacteristics__bpmn2_StandardLoopCharacteristics461", None)
        self.__bpmn2_StandardLoopCharacteristics461 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Expression462"):
                opp_val = getattr(old_value, "bpmn2_Expression462", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Expression462", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Expression462"):
                opp_val = getattr(value, "bpmn2_Expression462", None)
                setattr(value, "bpmn2_Expression462", self)

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
            if hasattr(old_value, "bpmn2_Expression459"):
                opp_val = getattr(old_value, "bpmn2_Expression459", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Expression459", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Expression459"):
                opp_val = getattr(value, "bpmn2_Expression459", None)
                setattr(value, "bpmn2_Expression459", self)

class bpmn2_MultiInstanceLoopCharacteristics(LoopCharacteristics):

    def __init__(self, isSequential: bool, behavior: str, bpmn2_MultiInstanceLoopCharacteristics: "bpmn2_Expression" = None, bpmn2_MultiInstanceLoopCharacteristics431: "bpmn2_ItemAwareElement" = None, bpmn2_MultiInstanceLoopCharacteristics434: "bpmn2_ItemAwareElement" = None, bpmn2_MultiInstanceLoopCharacteristics437: "bpmn2_DataInput" = None, bpmn2_MultiInstanceLoopCharacteristics440: "bpmn2_DataOutput" = None, bpmn2_MultiInstanceLoopCharacteristics443: "bpmn2_Expression" = None, bpmn2_MultiInstanceLoopCharacteristics446: set["bpmn2_ComplexBehaviorDefinition"] = None, bpmn2_MultiInstanceLoopCharacteristics448: "bpmn2_EventDefinition" = None, bpmn2_MultiInstanceLoopCharacteristics451: "bpmn2_EventDefinition" = None):
        self.isSequential = isSequential
        self.behavior = behavior
        self.bpmn2_MultiInstanceLoopCharacteristics = bpmn2_MultiInstanceLoopCharacteristics
        self.bpmn2_MultiInstanceLoopCharacteristics431 = bpmn2_MultiInstanceLoopCharacteristics431
        self.bpmn2_MultiInstanceLoopCharacteristics434 = bpmn2_MultiInstanceLoopCharacteristics434
        self.bpmn2_MultiInstanceLoopCharacteristics437 = bpmn2_MultiInstanceLoopCharacteristics437
        self.bpmn2_MultiInstanceLoopCharacteristics440 = bpmn2_MultiInstanceLoopCharacteristics440
        self.bpmn2_MultiInstanceLoopCharacteristics443 = bpmn2_MultiInstanceLoopCharacteristics443
        self.bpmn2_MultiInstanceLoopCharacteristics446 = bpmn2_MultiInstanceLoopCharacteristics446 if bpmn2_MultiInstanceLoopCharacteristics446 is not None else set()
        self.bpmn2_MultiInstanceLoopCharacteristics448 = bpmn2_MultiInstanceLoopCharacteristics448
        self.bpmn2_MultiInstanceLoopCharacteristics451 = bpmn2_MultiInstanceLoopCharacteristics451
        
    @property
    def isSequential(self) -> bool:
        return self.__isSequential

    @isSequential.setter
    def isSequential(self, isSequential: bool):
        self.__isSequential = isSequential

    @property
    def behavior(self) -> str:
        return self.__behavior

    @behavior.setter
    def behavior(self, behavior: str):
        self.__behavior = behavior

    @property
    def bpmn2_MultiInstanceLoopCharacteristics448(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics448

    @bpmn2_MultiInstanceLoopCharacteristics448.setter
    def bpmn2_MultiInstanceLoopCharacteristics448(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics448", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics448 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_EventDefinition449"):
                opp_val = getattr(old_value, "bpmn2_EventDefinition449", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_EventDefinition449", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_EventDefinition449"):
                opp_val = getattr(value, "bpmn2_EventDefinition449", None)
                setattr(value, "bpmn2_EventDefinition449", self)

    @property
    def bpmn2_MultiInstanceLoopCharacteristics437(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics437

    @bpmn2_MultiInstanceLoopCharacteristics437.setter
    def bpmn2_MultiInstanceLoopCharacteristics437(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics437", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics437 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DataInput438"):
                opp_val = getattr(old_value, "bpmn2_DataInput438", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_DataInput438", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DataInput438"):
                opp_val = getattr(value, "bpmn2_DataInput438", None)
                setattr(value, "bpmn2_DataInput438", self)

    @property
    def bpmn2_MultiInstanceLoopCharacteristics451(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics451

    @bpmn2_MultiInstanceLoopCharacteristics451.setter
    def bpmn2_MultiInstanceLoopCharacteristics451(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics451", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics451 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_EventDefinition452"):
                opp_val = getattr(old_value, "bpmn2_EventDefinition452", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_EventDefinition452", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_EventDefinition452"):
                opp_val = getattr(value, "bpmn2_EventDefinition452", None)
                setattr(value, "bpmn2_EventDefinition452", self)

    @property
    def bpmn2_MultiInstanceLoopCharacteristics446(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics446

    @bpmn2_MultiInstanceLoopCharacteristics446.setter
    def bpmn2_MultiInstanceLoopCharacteristics446(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics446", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics446 = value if value is not None else set()
        
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
    def bpmn2_MultiInstanceLoopCharacteristics443(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics443

    @bpmn2_MultiInstanceLoopCharacteristics443.setter
    def bpmn2_MultiInstanceLoopCharacteristics443(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics443", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics443 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Expression444"):
                opp_val = getattr(old_value, "bpmn2_Expression444", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Expression444", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Expression444"):
                opp_val = getattr(value, "bpmn2_Expression444", None)
                setattr(value, "bpmn2_Expression444", self)

    @property
    def bpmn2_MultiInstanceLoopCharacteristics440(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics440

    @bpmn2_MultiInstanceLoopCharacteristics440.setter
    def bpmn2_MultiInstanceLoopCharacteristics440(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics440", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics440 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DataOutput441"):
                opp_val = getattr(old_value, "bpmn2_DataOutput441", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_DataOutput441", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DataOutput441"):
                opp_val = getattr(value, "bpmn2_DataOutput441", None)
                setattr(value, "bpmn2_DataOutput441", self)

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
            if hasattr(old_value, "bpmn2_Expression429"):
                opp_val = getattr(old_value, "bpmn2_Expression429", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Expression429", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Expression429"):
                opp_val = getattr(value, "bpmn2_Expression429", None)
                setattr(value, "bpmn2_Expression429", self)

    @property
    def bpmn2_MultiInstanceLoopCharacteristics434(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics434

    @bpmn2_MultiInstanceLoopCharacteristics434.setter
    def bpmn2_MultiInstanceLoopCharacteristics434(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics434", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics434 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemAwareElement435"):
                opp_val = getattr(old_value, "bpmn2_ItemAwareElement435", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemAwareElement435", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemAwareElement435"):
                opp_val = getattr(value, "bpmn2_ItemAwareElement435", None)
                setattr(value, "bpmn2_ItemAwareElement435", self)

    @property
    def bpmn2_MultiInstanceLoopCharacteristics431(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics431

    @bpmn2_MultiInstanceLoopCharacteristics431.setter
    def bpmn2_MultiInstanceLoopCharacteristics431(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics431", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics431 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemAwareElement432"):
                opp_val = getattr(old_value, "bpmn2_ItemAwareElement432", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemAwareElement432", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemAwareElement432"):
                opp_val = getattr(value, "bpmn2_ItemAwareElement432", None)
                setattr(value, "bpmn2_ItemAwareElement432", self)

class ChoreographyActivity:

    pass
class Artifact:

    pass
class bpmn2_Group(Artifact):

    pass
class bpmn2_Association(Artifact):

    def __init__(self, associationDirection: str, bpmn2_Association: "bpmn2_BaseElement" = None, bpmn2_Association420: "bpmn2_BaseElement" = None):
        self.associationDirection = associationDirection
        self.bpmn2_Association = bpmn2_Association
        self.bpmn2_Association420 = bpmn2_Association420
        
    @property
    def associationDirection(self) -> str:
        return self.__associationDirection

    @associationDirection.setter
    def associationDirection(self, associationDirection: str):
        self.__associationDirection = associationDirection

    @property
    def bpmn2_Association420(self):
        return self.__bpmn2_Association420

    @bpmn2_Association420.setter
    def bpmn2_Association420(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Association__bpmn2_Association420", None)
        self.__bpmn2_Association420 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_BaseElement421"):
                opp_val = getattr(old_value, "bpmn2_BaseElement421", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_BaseElement421", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_BaseElement421"):
                opp_val = getattr(value, "bpmn2_BaseElement421", None)
                setattr(value, "bpmn2_BaseElement421", self)

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
            if hasattr(old_value, "bpmn2_BaseElement418"):
                opp_val = getattr(old_value, "bpmn2_BaseElement418", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_BaseElement418", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_BaseElement418"):
                opp_val = getattr(value, "bpmn2_BaseElement418", None)
                setattr(value, "bpmn2_BaseElement418", self)

class bpmn2_TextAnnotation(Artifact):

    def __init__(self, text: str, textFormat: str):
        self.text = text
        self.textFormat = textFormat
        
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

class Choreography:

    pass
class bpmn2_GlobalChoreographyTask(Choreography):

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
class bpmn2_Escalation:

    def __init__(self, name: str, escalationCode: str, id: str, bpmn2_Escalation: "bpmn2_EscalationEventDefinition" = None, bpmn2_Escalation356: "bpmn2_ItemDefinition" = None):
        self.name = name
        self.escalationCode = escalationCode
        self.id = id
        self.bpmn2_Escalation = bpmn2_Escalation
        self.bpmn2_Escalation356 = bpmn2_Escalation356
        
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
    def bpmn2_Escalation356(self):
        return self.__bpmn2_Escalation356

    @bpmn2_Escalation356.setter
    def bpmn2_Escalation356(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Escalation__bpmn2_Escalation356", None)
        self.__bpmn2_Escalation356 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemDefinition357"):
                opp_val = getattr(old_value, "bpmn2_ItemDefinition357", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemDefinition357", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemDefinition357"):
                opp_val = getattr(value, "bpmn2_ItemDefinition357", None)
                setattr(value, "bpmn2_ItemDefinition357", self)

class EventDefinition:

    pass
class bpmn2_LinkEventDefinition(EventDefinition):

    def __init__(self, name: str, LinkEventDefinition: "bpmn2_LinkEventDefinition" = None, source: "bpmn2_LinkEventDefinition" = None, LinkEventDefinition372: "bpmn2_LinkEventDefinition" = None, target: set["bpmn2_LinkEventDefinition"] = None):
        self.name = name
        self.LinkEventDefinition = LinkEventDefinition
        self.source = source
        self.LinkEventDefinition372 = LinkEventDefinition372
        self.target = target if target is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                if hasattr(item, "LinkEventDefinition372"):
                    opp_val = getattr(item, "LinkEventDefinition372", None)
                    
                    if opp_val == self:
                        setattr(item, "LinkEventDefinition372", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LinkEventDefinition372"):
                    opp_val = getattr(item, "LinkEventDefinition372", None)
                    
                    setattr(item, "LinkEventDefinition372", self)
                    

    @property
    def LinkEventDefinition372(self):
        return self.__LinkEventDefinition372

    @LinkEventDefinition372.setter
    def LinkEventDefinition372(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_LinkEventDefinition__LinkEventDefinition372", None)
        self.__LinkEventDefinition372 = value
        
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

class bpmn2_EscalationEventDefinition(EventDefinition):

    pass
class bpmn2_SignalEventDefinition(EventDefinition):

    pass
class bpmn2_ErrorEventDefinition(EventDefinition):

    pass
class bpmn2_MessageEventDefinition(EventDefinition):

    pass
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
            if hasattr(old_value, "bpmn2_Activity359"):
                opp_val = getattr(old_value, "bpmn2_Activity359", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Activity359", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Activity359"):
                opp_val = getattr(value, "bpmn2_Activity359", None)
                setattr(value, "bpmn2_Activity359", self)

class bpmn2_TerminateEventDefinition(EventDefinition):

    pass
class bpmn2_ConditionalEventDefinition(EventDefinition):

    pass
class bpmn2_CancelEventDefinition(EventDefinition):

    pass
class ThrowEvent:

    pass
class bpmn2_ImplicitThrowEvent(ThrowEvent):

    pass
class bpmn2_EndEvent(ThrowEvent):

    pass
class bpmn2_IntermediateThrowEvent(ThrowEvent):

    pass
class bpmn2_Extension:

    def __init__(self, mustUnderstand: bool, id: str, bpmn2_Extension: "bpmn2_ExtensionDefinition" = None, bpmn2_Extension481: "bpmn2_Definitions" = None):
        self.mustUnderstand = mustUnderstand
        self.id = id
        self.bpmn2_Extension = bpmn2_Extension
        self.bpmn2_Extension481 = bpmn2_Extension481
        
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
    def bpmn2_Extension(self):
        return self.__bpmn2_Extension

    @bpmn2_Extension.setter
    def bpmn2_Extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Extension__bpmn2_Extension", None)
        self.__bpmn2_Extension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ExtensionDefinition337"):
                opp_val = getattr(old_value, "bpmn2_ExtensionDefinition337", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ExtensionDefinition337", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ExtensionDefinition337"):
                opp_val = getattr(value, "bpmn2_ExtensionDefinition337", None)
                setattr(value, "bpmn2_ExtensionDefinition337", self)

    @property
    def bpmn2_Extension481(self):
        return self.__bpmn2_Extension481

    @bpmn2_Extension481.setter
    def bpmn2_Extension481(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Extension__bpmn2_Extension481", None)
        self.__bpmn2_Extension481 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Definitions480"):
                opp_val = getattr(old_value, "bpmn2_Definitions480", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Definitions480"):
                opp_val = getattr(value, "bpmn2_Definitions480", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Definitions480", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class HumanPerformer:

    pass
class bpmn2_PotentialOwner(HumanPerformer):

    pass
class Gateway:

    pass
class bpmn2_ParallelGateway(Gateway):

    pass
class bpmn2_ExclusiveGateway(Gateway):

    pass
class bpmn2_ComplexGateway(Gateway):

    pass
class bpmn2_InclusiveGateway(Gateway):

    pass
class bpmn2_EventBasedGateway(Gateway):

    def __init__(self, instantiate: bool, eventGatewayType: str):
        self.instantiate = instantiate
        self.eventGatewayType = eventGatewayType
        
    @property
    def instantiate(self) -> bool:
        return self.__instantiate

    @instantiate.setter
    def instantiate(self, instantiate: bool):
        self.__instantiate = instantiate

    @property
    def eventGatewayType(self) -> str:
        return self.__eventGatewayType

    @eventGatewayType.setter
    def eventGatewayType(self, eventGatewayType: str):
        self.__eventGatewayType = eventGatewayType

class CatchEvent:

    pass
class bpmn2_IntermediateCatchEvent(CatchEvent):

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

class Performer:

    pass
class bpmn2_HumanPerformer(Performer):

    pass
class DataAssociation:

    pass
class Event:

    pass
class bpmn2_ThrowEvent(Event):

    pass
class bpmn2_CatchEvent(Event):

    def __init__(self, parallelMultiple: bool, bpmn2_CatchEvent: "bpmn2_OutputSet" = None, bpmn2_CatchEvent291: set["bpmn2_EventDefinition"] = None, bpmn2_CatchEvent293: set["bpmn2_DataOutputAssociation"] = None, bpmn2_CatchEvent296: set["bpmn2_DataOutput"] = None, bpmn2_CatchEvent299: set["bpmn2_EventDefinition"] = None):
        self.parallelMultiple = parallelMultiple
        self.bpmn2_CatchEvent = bpmn2_CatchEvent
        self.bpmn2_CatchEvent291 = bpmn2_CatchEvent291 if bpmn2_CatchEvent291 is not None else set()
        self.bpmn2_CatchEvent293 = bpmn2_CatchEvent293 if bpmn2_CatchEvent293 is not None else set()
        self.bpmn2_CatchEvent296 = bpmn2_CatchEvent296 if bpmn2_CatchEvent296 is not None else set()
        self.bpmn2_CatchEvent299 = bpmn2_CatchEvent299 if bpmn2_CatchEvent299 is not None else set()
        
    @property
    def parallelMultiple(self) -> bool:
        return self.__parallelMultiple

    @parallelMultiple.setter
    def parallelMultiple(self, parallelMultiple: bool):
        self.__parallelMultiple = parallelMultiple

    @property
    def bpmn2_CatchEvent293(self):
        return self.__bpmn2_CatchEvent293

    @bpmn2_CatchEvent293.setter
    def bpmn2_CatchEvent293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CatchEvent__bpmn2_CatchEvent293", None)
        self.__bpmn2_CatchEvent293 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_DataOutputAssociation294"):
                    opp_val = getattr(item, "bpmn2_DataOutputAssociation294", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_DataOutputAssociation294", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_DataOutputAssociation294"):
                    opp_val = getattr(item, "bpmn2_DataOutputAssociation294", None)
                    
                    setattr(item, "bpmn2_DataOutputAssociation294", self)
                    

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
            if hasattr(old_value, "bpmn2_OutputSet289"):
                opp_val = getattr(old_value, "bpmn2_OutputSet289", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_OutputSet289", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_OutputSet289"):
                opp_val = getattr(value, "bpmn2_OutputSet289", None)
                setattr(value, "bpmn2_OutputSet289", self)

    @property
    def bpmn2_CatchEvent299(self):
        return self.__bpmn2_CatchEvent299

    @bpmn2_CatchEvent299.setter
    def bpmn2_CatchEvent299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CatchEvent__bpmn2_CatchEvent299", None)
        self.__bpmn2_CatchEvent299 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_EventDefinition300"):
                    opp_val = getattr(item, "bpmn2_EventDefinition300", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_EventDefinition300", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_EventDefinition300"):
                    opp_val = getattr(item, "bpmn2_EventDefinition300", None)
                    
                    setattr(item, "bpmn2_EventDefinition300", self)
                    

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
    def bpmn2_CatchEvent296(self):
        return self.__bpmn2_CatchEvent296

    @bpmn2_CatchEvent296.setter
    def bpmn2_CatchEvent296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CatchEvent__bpmn2_CatchEvent296", None)
        self.__bpmn2_CatchEvent296 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_DataOutput297"):
                    opp_val = getattr(item, "bpmn2_DataOutput297", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_DataOutput297", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_DataOutput297"):
                    opp_val = getattr(item, "bpmn2_DataOutput297", None)
                    
                    setattr(item, "bpmn2_DataOutput297", self)
                    

class bpmn2_DataOutputAssociation(DataAssociation):

    pass
class bpmn2_DataInputAssociation(DataAssociation):

    pass
class bpmn2_BoundaryEvent(CatchEvent):

    def __init__(self, cancelActivity: bool, BoundaryEvent: "bpmn2_Activity" = None, boundaryEventRefs: "bpmn2_Activity" = None):
        self.cancelActivity = cancelActivity
        self.BoundaryEvent = BoundaryEvent
        self.boundaryEventRefs = boundaryEventRefs
        
    @property
    def cancelActivity(self) -> bool:
        return self.__cancelActivity

    @cancelActivity.setter
    def cancelActivity(self, cancelActivity: bool):
        self.__cancelActivity = cancelActivity

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

class FlowNode:

    pass
class bpmn2_ChoreographyActivity(FlowNode):

    def __init__(self, loopType: str, bpmn2_ChoreographyActivity: set["bpmn2_Participant"] = None, bpmn2_ChoreographyActivity400: "bpmn2_Participant" = None, bpmn2_ChoreographyActivity403: set["bpmn2_CorrelationKey"] = None):
        self.loopType = loopType
        self.bpmn2_ChoreographyActivity = bpmn2_ChoreographyActivity if bpmn2_ChoreographyActivity is not None else set()
        self.bpmn2_ChoreographyActivity400 = bpmn2_ChoreographyActivity400
        self.bpmn2_ChoreographyActivity403 = bpmn2_ChoreographyActivity403 if bpmn2_ChoreographyActivity403 is not None else set()
        
    @property
    def loopType(self) -> str:
        return self.__loopType

    @loopType.setter
    def loopType(self, loopType: str):
        self.__loopType = loopType

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
                if hasattr(item, "bpmn2_Participant398"):
                    opp_val = getattr(item, "bpmn2_Participant398", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Participant398", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Participant398"):
                    opp_val = getattr(item, "bpmn2_Participant398", None)
                    
                    setattr(item, "bpmn2_Participant398", self)
                    

    @property
    def bpmn2_ChoreographyActivity400(self):
        return self.__bpmn2_ChoreographyActivity400

    @bpmn2_ChoreographyActivity400.setter
    def bpmn2_ChoreographyActivity400(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ChoreographyActivity__bpmn2_ChoreographyActivity400", None)
        self.__bpmn2_ChoreographyActivity400 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Participant401"):
                opp_val = getattr(old_value, "bpmn2_Participant401", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Participant401", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Participant401"):
                opp_val = getattr(value, "bpmn2_Participant401", None)
                setattr(value, "bpmn2_Participant401", self)

    @property
    def bpmn2_ChoreographyActivity403(self):
        return self.__bpmn2_ChoreographyActivity403

    @bpmn2_ChoreographyActivity403.setter
    def bpmn2_ChoreographyActivity403(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ChoreographyActivity__bpmn2_ChoreographyActivity403", None)
        self.__bpmn2_ChoreographyActivity403 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_CorrelationKey404"):
                    opp_val = getattr(item, "bpmn2_CorrelationKey404", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_CorrelationKey404", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_CorrelationKey404"):
                    opp_val = getattr(item, "bpmn2_CorrelationKey404", None)
                    
                    setattr(item, "bpmn2_CorrelationKey404", self)
                    

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

    def __init__(self, isForCompensation: bool, startQuantity: int, completionQuantity: int, bpmn2_Activity: "bpmn2_LoopCharacteristics" = None, bpmn2_Activity271: set["bpmn2_ResourceRole"] = None, bpmn2_Activity274: "bpmn2_SequenceFlow" = None, bpmn2_Activity277: set["bpmn2_Property"] = None, bpmn2_Activity280: "bpmn2_InputOutputSpecification" = None, attachedToRef: set["bpmn2_BoundaryEvent"] = None, bpmn2_Activity284: set["bpmn2_DataInputAssociation"] = None, bpmn2_Activity286: set["bpmn2_DataOutputAssociation"] = None, Activity: "bpmn2_BoundaryEvent" = None, bpmn2_Activity359: "bpmn2_CompensateEventDefinition" = None):
        self.isForCompensation = isForCompensation
        self.startQuantity = startQuantity
        self.completionQuantity = completionQuantity
        self.bpmn2_Activity = bpmn2_Activity
        self.bpmn2_Activity271 = bpmn2_Activity271 if bpmn2_Activity271 is not None else set()
        self.bpmn2_Activity274 = bpmn2_Activity274
        self.bpmn2_Activity277 = bpmn2_Activity277 if bpmn2_Activity277 is not None else set()
        self.bpmn2_Activity280 = bpmn2_Activity280
        self.attachedToRef = attachedToRef if attachedToRef is not None else set()
        self.bpmn2_Activity284 = bpmn2_Activity284 if bpmn2_Activity284 is not None else set()
        self.bpmn2_Activity286 = bpmn2_Activity286 if bpmn2_Activity286 is not None else set()
        self.Activity = Activity
        self.bpmn2_Activity359 = bpmn2_Activity359
        
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
    def startQuantity(self) -> int:
        return self.__startQuantity

    @startQuantity.setter
    def startQuantity(self, startQuantity: int):
        self.__startQuantity = startQuantity

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
    def bpmn2_Activity359(self):
        return self.__bpmn2_Activity359

    @bpmn2_Activity359.setter
    def bpmn2_Activity359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity359", None)
        self.__bpmn2_Activity359 = value
        
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
    def bpmn2_Activity271(self):
        return self.__bpmn2_Activity271

    @bpmn2_Activity271.setter
    def bpmn2_Activity271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity271", None)
        self.__bpmn2_Activity271 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_ResourceRole272"):
                    opp_val = getattr(item, "bpmn2_ResourceRole272", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_ResourceRole272", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_ResourceRole272"):
                    opp_val = getattr(item, "bpmn2_ResourceRole272", None)
                    
                    setattr(item, "bpmn2_ResourceRole272", self)
                    

    @property
    def bpmn2_Activity286(self):
        return self.__bpmn2_Activity286

    @bpmn2_Activity286.setter
    def bpmn2_Activity286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity286", None)
        self.__bpmn2_Activity286 = value if value is not None else set()
        
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
    def bpmn2_Activity284(self):
        return self.__bpmn2_Activity284

    @bpmn2_Activity284.setter
    def bpmn2_Activity284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity284", None)
        self.__bpmn2_Activity284 = value if value is not None else set()
        
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
    def bpmn2_Activity274(self):
        return self.__bpmn2_Activity274

    @bpmn2_Activity274.setter
    def bpmn2_Activity274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity274", None)
        self.__bpmn2_Activity274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_SequenceFlow275"):
                opp_val = getattr(old_value, "bpmn2_SequenceFlow275", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_SequenceFlow275", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_SequenceFlow275"):
                opp_val = getattr(value, "bpmn2_SequenceFlow275", None)
                setattr(value, "bpmn2_SequenceFlow275", self)

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
    def bpmn2_Activity277(self):
        return self.__bpmn2_Activity277

    @bpmn2_Activity277.setter
    def bpmn2_Activity277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity277", None)
        self.__bpmn2_Activity277 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Property278"):
                    opp_val = getattr(item, "bpmn2_Property278", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Property278", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Property278"):
                    opp_val = getattr(item, "bpmn2_Property278", None)
                    
                    setattr(item, "bpmn2_Property278", self)
                    

    @property
    def bpmn2_Activity280(self):
        return self.__bpmn2_Activity280

    @bpmn2_Activity280.setter
    def bpmn2_Activity280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity280", None)
        self.__bpmn2_Activity280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_InputOutputSpecification281"):
                opp_val = getattr(old_value, "bpmn2_InputOutputSpecification281", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_InputOutputSpecification281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_InputOutputSpecification281"):
                opp_val = getattr(value, "bpmn2_InputOutputSpecification281", None)
                setattr(value, "bpmn2_InputOutputSpecification281", self)

class Activity:

    pass
class bpmn2_CallActivity(Activity):

    pass
class Task:

    pass
class bpmn2_SendTask(Task):

    def __init__(self, implementation: str, bpmn2_SendTask: "bpmn2_Operation" = None, bpmn2_SendTask468: "bpmn2_Message" = None):
        self.implementation = implementation
        self.bpmn2_SendTask = bpmn2_SendTask
        self.bpmn2_SendTask468 = bpmn2_SendTask468
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def bpmn2_SendTask468(self):
        return self.__bpmn2_SendTask468

    @bpmn2_SendTask468.setter
    def bpmn2_SendTask468(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SendTask__bpmn2_SendTask468", None)
        self.__bpmn2_SendTask468 = value
        
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
            if hasattr(old_value, "bpmn2_Operation466"):
                opp_val = getattr(old_value, "bpmn2_Operation466", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Operation466", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Operation466"):
                opp_val = getattr(value, "bpmn2_Operation466", None)
                setattr(value, "bpmn2_Operation466", self)

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
                    

class bpmn2_ReceiveTask(Task):

    def __init__(self, implementation: str, instantiate: bool, bpmn2_ReceiveTask: "bpmn2_Operation" = None, bpmn2_ReceiveTask473: "bpmn2_Message" = None):
        self.implementation = implementation
        self.instantiate = instantiate
        self.bpmn2_ReceiveTask = bpmn2_ReceiveTask
        self.bpmn2_ReceiveTask473 = bpmn2_ReceiveTask473
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def instantiate(self) -> bool:
        return self.__instantiate

    @instantiate.setter
    def instantiate(self, instantiate: bool):
        self.__instantiate = instantiate

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
            if hasattr(old_value, "bpmn2_Operation471"):
                opp_val = getattr(old_value, "bpmn2_Operation471", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Operation471", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Operation471"):
                opp_val = getattr(value, "bpmn2_Operation471", None)
                setattr(value, "bpmn2_Operation471", self)

    @property
    def bpmn2_ReceiveTask473(self):
        return self.__bpmn2_ReceiveTask473

    @bpmn2_ReceiveTask473.setter
    def bpmn2_ReceiveTask473(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ReceiveTask__bpmn2_ReceiveTask473", None)
        self.__bpmn2_ReceiveTask473 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Message474"):
                opp_val = getattr(old_value, "bpmn2_Message474", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Message474", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Message474"):
                opp_val = getattr(value, "bpmn2_Message474", None)
                setattr(value, "bpmn2_Message474", self)

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
            if hasattr(old_value, "bpmn2_Operation425"):
                opp_val = getattr(old_value, "bpmn2_Operation425", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Operation425", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Operation425"):
                opp_val = getattr(value, "bpmn2_Operation425", None)
                setattr(value, "bpmn2_Operation425", self)

class bpmn2_BusinessRuleTask(Task):

    def __init__(self, implementation: str):
        self.implementation = implementation
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

class bpmn2_ManualTask(Task):

    pass
class GlobalTask:

    pass
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
                if hasattr(item, "bpmn2_Rendering321"):
                    opp_val = getattr(item, "bpmn2_Rendering321", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Rendering321", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Rendering321"):
                    opp_val = getattr(item, "bpmn2_Rendering321", None)
                    
                    setattr(item, "bpmn2_Rendering321", self)
                    

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
    def scriptLanguage(self) -> str:
        return self.__scriptLanguage

    @scriptLanguage.setter
    def scriptLanguage(self, scriptLanguage: str):
        self.__scriptLanguage = scriptLanguage

    @property
    def script(self) -> str:
        return self.__script

    @script.setter
    def script(self, script: str):
        self.__script = script

class bpmn2_GlobalManualTask(GlobalTask):

    pass
class Expression:

    pass
class bpmn2_FormalExpression(Expression):

    def __init__(self, language: str, bpmn2_FormalExpression: "bpmn2_CorrelationPropertyRetrievalExpression" = None, bpmn2_FormalExpression253: "bpmn2_EObject" = None, bpmn2_FormalExpression265: "bpmn2_CorrelationPropertyBinding" = None, bpmn2_FormalExpression256: "bpmn2_ItemDefinition" = None, bpmn2_FormalExpression304: "bpmn2_DataAssociation" = None, bpmn2_FormalExpression455: "bpmn2_ComplexBehaviorDefinition" = None):
        self.language = language
        self.bpmn2_FormalExpression = bpmn2_FormalExpression
        self.bpmn2_FormalExpression253 = bpmn2_FormalExpression253
        self.bpmn2_FormalExpression265 = bpmn2_FormalExpression265
        self.bpmn2_FormalExpression256 = bpmn2_FormalExpression256
        self.bpmn2_FormalExpression304 = bpmn2_FormalExpression304
        self.bpmn2_FormalExpression455 = bpmn2_FormalExpression455
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def bpmn2_FormalExpression256(self):
        return self.__bpmn2_FormalExpression256

    @bpmn2_FormalExpression256.setter
    def bpmn2_FormalExpression256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FormalExpression__bpmn2_FormalExpression256", None)
        self.__bpmn2_FormalExpression256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemDefinition257"):
                opp_val = getattr(old_value, "bpmn2_ItemDefinition257", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemDefinition257", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemDefinition257"):
                opp_val = getattr(value, "bpmn2_ItemDefinition257", None)
                setattr(value, "bpmn2_ItemDefinition257", self)

    @property
    def bpmn2_FormalExpression265(self):
        return self.__bpmn2_FormalExpression265

    @bpmn2_FormalExpression265.setter
    def bpmn2_FormalExpression265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FormalExpression__bpmn2_FormalExpression265", None)
        self.__bpmn2_FormalExpression265 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CorrelationPropertyBinding264"):
                opp_val = getattr(old_value, "bpmn2_CorrelationPropertyBinding264", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_CorrelationPropertyBinding264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CorrelationPropertyBinding264"):
                opp_val = getattr(value, "bpmn2_CorrelationPropertyBinding264", None)
                setattr(value, "bpmn2_CorrelationPropertyBinding264", self)

    @property
    def bpmn2_FormalExpression304(self):
        return self.__bpmn2_FormalExpression304

    @bpmn2_FormalExpression304.setter
    def bpmn2_FormalExpression304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FormalExpression__bpmn2_FormalExpression304", None)
        self.__bpmn2_FormalExpression304 = value
        
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
    def bpmn2_FormalExpression455(self):
        return self.__bpmn2_FormalExpression455

    @bpmn2_FormalExpression455.setter
    def bpmn2_FormalExpression455(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FormalExpression__bpmn2_FormalExpression455", None)
        self.__bpmn2_FormalExpression455 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ComplexBehaviorDefinition454"):
                opp_val = getattr(old_value, "bpmn2_ComplexBehaviorDefinition454", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ComplexBehaviorDefinition454", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ComplexBehaviorDefinition454"):
                opp_val = getattr(value, "bpmn2_ComplexBehaviorDefinition454", None)
                setattr(value, "bpmn2_ComplexBehaviorDefinition454", self)

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
            if hasattr(old_value, "bpmn2_CorrelationPropertyRetrievalExpression248"):
                opp_val = getattr(old_value, "bpmn2_CorrelationPropertyRetrievalExpression248", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_CorrelationPropertyRetrievalExpression248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CorrelationPropertyRetrievalExpression248"):
                opp_val = getattr(value, "bpmn2_CorrelationPropertyRetrievalExpression248", None)
                setattr(value, "bpmn2_CorrelationPropertyRetrievalExpression248", self)

    @property
    def bpmn2_FormalExpression253(self):
        return self.__bpmn2_FormalExpression253

    @bpmn2_FormalExpression253.setter
    def bpmn2_FormalExpression253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FormalExpression__bpmn2_FormalExpression253", None)
        self.__bpmn2_FormalExpression253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_EObject254"):
                opp_val = getattr(old_value, "bpmn2_EObject254", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_EObject254", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_EObject254"):
                opp_val = getattr(value, "bpmn2_EObject254", None)
                setattr(value, "bpmn2_EObject254", self)

class bpmn2_InteractionNode(ABC):

    pass
class bpmn2_ParticipantMultiplicity:

    def __init__(self, minimum: int, maximum: int, id: str, bpmn2_ParticipantMultiplicity: "bpmn2_Participant" = None):
        self.minimum = minimum
        self.maximum = maximum
        self.id = id
        self.bpmn2_ParticipantMultiplicity = bpmn2_ParticipantMultiplicity
        
    @property
    def minimum(self) -> int:
        return self.__minimum

    @minimum.setter
    def minimum(self, minimum: int):
        self.__minimum = minimum

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
    def bpmn2_ParticipantMultiplicity(self):
        return self.__bpmn2_ParticipantMultiplicity

    @bpmn2_ParticipantMultiplicity.setter
    def bpmn2_ParticipantMultiplicity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ParticipantMultiplicity__bpmn2_ParticipantMultiplicity", None)
        self.__bpmn2_ParticipantMultiplicity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Participant197"):
                opp_val = getattr(old_value, "bpmn2_Participant197", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Participant197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Participant197"):
                opp_val = getattr(value, "bpmn2_Participant197", None)
                setattr(value, "bpmn2_Participant197", self)

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

    def __init__(self, isImmediate: bool, SequenceFlow: "bpmn2_FlowNode" = None, SequenceFlow158: "bpmn2_FlowNode" = None, bpmn2_SequenceFlow: "bpmn2_Expression" = None, incoming: "bpmn2_FlowNode" = None, outgoing: "bpmn2_FlowNode" = None, bpmn2_SequenceFlow275: "bpmn2_Activity" = None, bpmn2_SequenceFlow326: "bpmn2_ComplexGateway" = None, bpmn2_SequenceFlow328: "bpmn2_ExclusiveGateway" = None, bpmn2_SequenceFlow330: "bpmn2_InclusiveGateway" = None):
        self.isImmediate = isImmediate
        self.SequenceFlow = SequenceFlow
        self.SequenceFlow158 = SequenceFlow158
        self.bpmn2_SequenceFlow = bpmn2_SequenceFlow
        self.incoming = incoming
        self.outgoing = outgoing
        self.bpmn2_SequenceFlow275 = bpmn2_SequenceFlow275
        self.bpmn2_SequenceFlow326 = bpmn2_SequenceFlow326
        self.bpmn2_SequenceFlow328 = bpmn2_SequenceFlow328
        self.bpmn2_SequenceFlow330 = bpmn2_SequenceFlow330
        
    @property
    def isImmediate(self) -> bool:
        return self.__isImmediate

    @isImmediate.setter
    def isImmediate(self, isImmediate: bool):
        self.__isImmediate = isImmediate

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
            if hasattr(old_value, "FlowNode163"):
                opp_val = getattr(old_value, "FlowNode163", None)
                if opp_val == self:
                    setattr(old_value, "FlowNode163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowNode163"):
                opp_val = getattr(value, "FlowNode163", None)
                setattr(value, "FlowNode163", self)

    @property
    def bpmn2_SequenceFlow275(self):
        return self.__bpmn2_SequenceFlow275

    @bpmn2_SequenceFlow275.setter
    def bpmn2_SequenceFlow275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SequenceFlow__bpmn2_SequenceFlow275", None)
        self.__bpmn2_SequenceFlow275 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Activity274"):
                opp_val = getattr(old_value, "bpmn2_Activity274", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Activity274", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Activity274"):
                opp_val = getattr(value, "bpmn2_Activity274", None)
                setattr(value, "bpmn2_Activity274", self)

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
            if hasattr(old_value, "bpmn2_Expression161"):
                opp_val = getattr(old_value, "bpmn2_Expression161", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Expression161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Expression161"):
                opp_val = getattr(value, "bpmn2_Expression161", None)
                setattr(value, "bpmn2_Expression161", self)

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
            if hasattr(old_value, "FlowNode165"):
                opp_val = getattr(old_value, "FlowNode165", None)
                if opp_val == self:
                    setattr(old_value, "FlowNode165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowNode165"):
                opp_val = getattr(value, "FlowNode165", None)
                setattr(value, "FlowNode165", self)

    @property
    def bpmn2_SequenceFlow330(self):
        return self.__bpmn2_SequenceFlow330

    @bpmn2_SequenceFlow330.setter
    def bpmn2_SequenceFlow330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SequenceFlow__bpmn2_SequenceFlow330", None)
        self.__bpmn2_SequenceFlow330 = value
        
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
    def SequenceFlow158(self):
        return self.__SequenceFlow158

    @SequenceFlow158.setter
    def SequenceFlow158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SequenceFlow__SequenceFlow158", None)
        self.__SequenceFlow158 = value
        
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
    def bpmn2_SequenceFlow326(self):
        return self.__bpmn2_SequenceFlow326

    @bpmn2_SequenceFlow326.setter
    def bpmn2_SequenceFlow326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SequenceFlow__bpmn2_SequenceFlow326", None)
        self.__bpmn2_SequenceFlow326 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ComplexGateway325"):
                opp_val = getattr(old_value, "bpmn2_ComplexGateway325", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ComplexGateway325", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ComplexGateway325"):
                opp_val = getattr(value, "bpmn2_ComplexGateway325", None)
                setattr(value, "bpmn2_ComplexGateway325", self)

    @property
    def bpmn2_SequenceFlow328(self):
        return self.__bpmn2_SequenceFlow328

    @bpmn2_SequenceFlow328.setter
    def bpmn2_SequenceFlow328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SequenceFlow__bpmn2_SequenceFlow328", None)
        self.__bpmn2_SequenceFlow328 = value
        
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

class bpmn2_FlowNode(FlowElement):

    pass
class FlowElementsContainer:

    pass
class bpmn2_SubProcess(FlowElementsContainer, Activity):

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
                if hasattr(item, "bpmn2_Artifact427"):
                    opp_val = getattr(item, "bpmn2_Artifact427", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Artifact427", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Artifact427"):
                    opp_val = getattr(item, "bpmn2_Artifact427", None)
                    
                    setattr(item, "bpmn2_Artifact427", self)
                    

class bpmn2_SubChoreography(FlowElementsContainer, ChoreographyActivity):

    pass
class bpmn2_Choreography(FlowElementsContainer, Collaboration):

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

class ItemAwareElement:

    pass
class bpmn2_Property(ItemAwareElement):

    def __init__(self, name: str, bpmn2_Property: "bpmn2_Process" = None, bpmn2_Property278: "bpmn2_Activity" = None, bpmn2_Property302: "bpmn2_Event" = None):
        self.name = name
        self.bpmn2_Property = bpmn2_Property
        self.bpmn2_Property278 = bpmn2_Property278
        self.bpmn2_Property302 = bpmn2_Property302
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_Property302(self):
        return self.__bpmn2_Property302

    @bpmn2_Property302.setter
    def bpmn2_Property302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Property__bpmn2_Property302", None)
        self.__bpmn2_Property302 = value
        
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
    def bpmn2_Property278(self):
        return self.__bpmn2_Property278

    @bpmn2_Property278.setter
    def bpmn2_Property278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Property__bpmn2_Property278", None)
        self.__bpmn2_Property278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Activity277"):
                opp_val = getattr(old_value, "bpmn2_Activity277", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Activity277"):
                opp_val = getattr(value, "bpmn2_Activity277", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Activity277", set([self]))
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

class bpmn2_DataStoreReference(FlowElement, ItemAwareElement):

    pass
class bpmn2_DataObjectReference(FlowElement, ItemAwareElement):

    pass
class bpmn2_DataObject(FlowElement, ItemAwareElement):

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

class bpmn2_DataOutput(ItemAwareElement):

    def __init__(self, name: str, isCollection: bool, DataOutput: "bpmn2_OutputSet" = None, DataOutput71: "bpmn2_OutputSet" = None, DataOutput73: "bpmn2_OutputSet" = None, bpmn2_DataOutput: "bpmn2_InputOutputSpecification" = None, optionalOutputRefs: set["bpmn2_OutputSet"] = None, whileExecutingOutputRefs: set["bpmn2_OutputSet"] = None, dataOutputRefs: set["bpmn2_OutputSet"] = None, bpmn2_DataOutput297: "bpmn2_CatchEvent" = None, bpmn2_DataOutput441: "bpmn2_MultiInstanceLoopCharacteristics" = None):
        self.name = name
        self.isCollection = isCollection
        self.DataOutput = DataOutput
        self.DataOutput71 = DataOutput71
        self.DataOutput73 = DataOutput73
        self.bpmn2_DataOutput = bpmn2_DataOutput
        self.optionalOutputRefs = optionalOutputRefs if optionalOutputRefs is not None else set()
        self.whileExecutingOutputRefs = whileExecutingOutputRefs if whileExecutingOutputRefs is not None else set()
        self.dataOutputRefs = dataOutputRefs if dataOutputRefs is not None else set()
        self.bpmn2_DataOutput297 = bpmn2_DataOutput297
        self.bpmn2_DataOutput441 = bpmn2_DataOutput441
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isCollection(self) -> bool:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: bool):
        self.__isCollection = isCollection

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
    def bpmn2_DataOutput297(self):
        return self.__bpmn2_DataOutput297

    @bpmn2_DataOutput297.setter
    def bpmn2_DataOutput297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataOutput__bpmn2_DataOutput297", None)
        self.__bpmn2_DataOutput297 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CatchEvent296"):
                opp_val = getattr(old_value, "bpmn2_CatchEvent296", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CatchEvent296"):
                opp_val = getattr(value, "bpmn2_CatchEvent296", None)
                if opp_val is None:
                    setattr(value, "bpmn2_CatchEvent296", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def bpmn2_DataOutput441(self):
        return self.__bpmn2_DataOutput441

    @bpmn2_DataOutput441.setter
    def bpmn2_DataOutput441(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataOutput__bpmn2_DataOutput441", None)
        self.__bpmn2_DataOutput441 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_MultiInstanceLoopCharacteristics440"):
                opp_val = getattr(old_value, "bpmn2_MultiInstanceLoopCharacteristics440", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_MultiInstanceLoopCharacteristics440", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_MultiInstanceLoopCharacteristics440"):
                opp_val = getattr(value, "bpmn2_MultiInstanceLoopCharacteristics440", None)
                setattr(value, "bpmn2_MultiInstanceLoopCharacteristics440", self)

class bpmn2_DataInput(ItemAwareElement):

    def __init__(self, name: str, isCollection: bool, optionalInputRefs: set["bpmn2_InputSet"] = None, whileExecutingInputRefs: set["bpmn2_InputSet"] = None, dataInputRefs: set["bpmn2_InputSet"] = None, bpmn2_DataInput: "bpmn2_InputOutputSpecification" = None, DataInput: "bpmn2_InputSet" = None, DataInput55: "bpmn2_InputSet" = None, DataInput57: "bpmn2_InputSet" = None, bpmn2_DataInput348: "bpmn2_ThrowEvent" = None, bpmn2_DataInput438: "bpmn2_MultiInstanceLoopCharacteristics" = None):
        self.name = name
        self.isCollection = isCollection
        self.optionalInputRefs = optionalInputRefs if optionalInputRefs is not None else set()
        self.whileExecutingInputRefs = whileExecutingInputRefs if whileExecutingInputRefs is not None else set()
        self.dataInputRefs = dataInputRefs if dataInputRefs is not None else set()
        self.bpmn2_DataInput = bpmn2_DataInput
        self.DataInput = DataInput
        self.DataInput55 = DataInput55
        self.DataInput57 = DataInput57
        self.bpmn2_DataInput348 = bpmn2_DataInput348
        self.bpmn2_DataInput438 = bpmn2_DataInput438
        
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
    def bpmn2_DataInput348(self):
        return self.__bpmn2_DataInput348

    @bpmn2_DataInput348.setter
    def bpmn2_DataInput348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataInput__bpmn2_DataInput348", None)
        self.__bpmn2_DataInput348 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ThrowEvent347"):
                opp_val = getattr(old_value, "bpmn2_ThrowEvent347", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ThrowEvent347"):
                opp_val = getattr(value, "bpmn2_ThrowEvent347", None)
                if opp_val is None:
                    setattr(value, "bpmn2_ThrowEvent347", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_DataInput438(self):
        return self.__bpmn2_DataInput438

    @bpmn2_DataInput438.setter
    def bpmn2_DataInput438(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataInput__bpmn2_DataInput438", None)
        self.__bpmn2_DataInput438 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_MultiInstanceLoopCharacteristics437"):
                opp_val = getattr(old_value, "bpmn2_MultiInstanceLoopCharacteristics437", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_MultiInstanceLoopCharacteristics437", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_MultiInstanceLoopCharacteristics437"):
                opp_val = getattr(value, "bpmn2_MultiInstanceLoopCharacteristics437", None)
                setattr(value, "bpmn2_MultiInstanceLoopCharacteristics437", self)

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

class CallableElement:

    pass
class bpmn2_Process(CallableElement, FlowElementsContainer):

    def __init__(self, isExecutable: bool, processType: str, isClosed: bool, bpmn2_Process113: "bpmn2_Monitoring" = None, bpmn2_Process115: set["bpmn2_Property"] = None, bpmn2_Process118: "bpmn2_Process" = None, bpmn2_Process116: set["bpmn2_Process"] = None, bpmn2_Process120: "bpmn2_Collaboration" = None, bpmn2_Process122: set["bpmn2_ResourceRole"] = None, bpmn2_Process125: set["bpmn2_Artifact"] = None, bpmn2_Process127: set["bpmn2_CorrelationSubscription"] = None, Process: "bpmn2_Process" = None, decomposes: set["bpmn2_Process"] = None, Process132: "bpmn2_Process" = None, decomposedBy: "bpmn2_Process" = None, bpmn2_Process: "bpmn2_Auditing" = None, bpmn2_Process202: "bpmn2_Participant" = None):
        self.isExecutable = isExecutable
        self.processType = processType
        self.isClosed = isClosed
        self.bpmn2_Process113 = bpmn2_Process113
        self.bpmn2_Process115 = bpmn2_Process115 if bpmn2_Process115 is not None else set()
        self.bpmn2_Process118 = bpmn2_Process118
        self.bpmn2_Process116 = bpmn2_Process116 if bpmn2_Process116 is not None else set()
        self.bpmn2_Process120 = bpmn2_Process120
        self.bpmn2_Process122 = bpmn2_Process122 if bpmn2_Process122 is not None else set()
        self.bpmn2_Process125 = bpmn2_Process125 if bpmn2_Process125 is not None else set()
        self.bpmn2_Process127 = bpmn2_Process127 if bpmn2_Process127 is not None else set()
        self.Process = Process
        self.decomposes = decomposes if decomposes is not None else set()
        self.Process132 = Process132
        self.decomposedBy = decomposedBy
        self.bpmn2_Process = bpmn2_Process
        self.bpmn2_Process202 = bpmn2_Process202
        
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
    def processType(self) -> str:
        return self.__processType

    @processType.setter
    def processType(self, processType: str):
        self.__processType = processType

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
    def decomposes(self):
        return self.__decomposes

    @decomposes.setter
    def decomposes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__decomposes", None)
        self.__decomposes = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Process"):
                    opp_val = getattr(item, "Process", None)
                    
                    if opp_val == self:
                        setattr(item, "Process", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Process"):
                    opp_val = getattr(item, "Process", None)
                    
                    setattr(item, "Process", self)
                    

    @property
    def decomposedBy(self):
        return self.__decomposedBy

    @decomposedBy.setter
    def decomposedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__decomposedBy", None)
        self.__decomposedBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Process132"):
                opp_val = getattr(old_value, "Process132", None)
                if opp_val == self:
                    setattr(old_value, "Process132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Process132"):
                opp_val = getattr(value, "Process132", None)
                setattr(value, "Process132", self)

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
    def Process(self):
        return self.__Process

    @Process.setter
    def Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__Process", None)
        self.__Process = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decomposes"):
                opp_val = getattr(old_value, "decomposes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decomposes"):
                opp_val = getattr(value, "decomposes", None)
                if opp_val is None:
                    setattr(value, "decomposes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Process202(self):
        return self.__bpmn2_Process202

    @bpmn2_Process202.setter
    def bpmn2_Process202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process202", None)
        self.__bpmn2_Process202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Participant201"):
                opp_val = getattr(old_value, "bpmn2_Participant201", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Participant201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Participant201"):
                opp_val = getattr(value, "bpmn2_Participant201", None)
                setattr(value, "bpmn2_Participant201", self)

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
    def Process132(self):
        return self.__Process132

    @Process132.setter
    def Process132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__Process132", None)
        self.__Process132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decomposedBy"):
                opp_val = getattr(old_value, "decomposedBy", None)
                if opp_val == self:
                    setattr(old_value, "decomposedBy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decomposedBy"):
                opp_val = getattr(value, "decomposedBy", None)
                setattr(value, "decomposedBy", self)

class bpmn2_GlobalTask(CallableElement):

    pass
class bpmn2_Import:

    def __init__(self, importType: str, location: str, namespace: str, id: str, bpmn2_Import: "bpmn2_ItemDefinition" = None, bpmn2_Import478: "bpmn2_Definitions" = None):
        self.importType = importType
        self.location = location
        self.namespace = namespace
        self.id = id
        self.bpmn2_Import = bpmn2_Import
        self.bpmn2_Import478 = bpmn2_Import478
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

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
    def importType(self) -> str:
        return self.__importType

    @importType.setter
    def importType(self, importType: str):
        self.__importType = importType

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

    @property
    def bpmn2_Import478(self):
        return self.__bpmn2_Import478

    @bpmn2_Import478.setter
    def bpmn2_Import478(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Import__bpmn2_Import478", None)
        self.__bpmn2_Import478 = value
        
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

class bpmn2_ExtensionAttributeDefinition:

    def __init__(self, id: str, name: str, type: str, isReference: bool, bpmn2_ExtensionAttributeDefinition: "bpmn2_ExtensionAttributeValue" = None, ExtensionAttributeDefinition: "bpmn2_ExtensionDefinition" = None, extensionAttributeDefinitions: "bpmn2_ExtensionDefinition" = None):
        self.id = id
        self.name = name
        self.type = type
        self.isReference = isReference
        self.bpmn2_ExtensionAttributeDefinition = bpmn2_ExtensionAttributeDefinition
        self.ExtensionAttributeDefinition = ExtensionAttributeDefinition
        self.extensionAttributeDefinitions = extensionAttributeDefinitions
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def isReference(self) -> bool:
        return self.__isReference

    @isReference.setter
    def isReference(self, isReference: bool):
        self.__isReference = isReference

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

class bpmn2_ExtensionAttributeValue:

    def __init__(self, id: str, bpmn2_ExtensionAttributeValue11: "bpmn2_EObject" = None, bpmn2_ExtensionAttributeValue14: "bpmn2_EObject" = None, bpmn2_ExtensionAttributeValue17: "bpmn2_ExtensionAttributeDefinition" = None, bpmn2_ExtensionAttributeValue: "bpmn2_BaseElement" = None):
        self.id = id
        self.bpmn2_ExtensionAttributeValue11 = bpmn2_ExtensionAttributeValue11
        self.bpmn2_ExtensionAttributeValue14 = bpmn2_ExtensionAttributeValue14
        self.bpmn2_ExtensionAttributeValue17 = bpmn2_ExtensionAttributeValue17
        self.bpmn2_ExtensionAttributeValue = bpmn2_ExtensionAttributeValue
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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

class bpmn2_ExtensionDefinition:

    def __init__(self, name: str, id: str, bpmn2_ExtensionDefinition: "bpmn2_BaseElement" = None, extensionDefinition: set["bpmn2_ExtensionAttributeDefinition"] = None, ExtensionDefinition: "bpmn2_ExtensionAttributeDefinition" = None, bpmn2_ExtensionDefinition337: "bpmn2_Extension" = None):
        self.name = name
        self.id = id
        self.bpmn2_ExtensionDefinition = bpmn2_ExtensionDefinition
        self.extensionDefinition = extensionDefinition if extensionDefinition is not None else set()
        self.ExtensionDefinition = ExtensionDefinition
        self.bpmn2_ExtensionDefinition337 = bpmn2_ExtensionDefinition337
        
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

    @property
    def bpmn2_ExtensionDefinition337(self):
        return self.__bpmn2_ExtensionDefinition337

    @bpmn2_ExtensionDefinition337.setter
    def bpmn2_ExtensionDefinition337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ExtensionDefinition__bpmn2_ExtensionDefinition337", None)
        self.__bpmn2_ExtensionDefinition337 = value
        
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
                    

class bpmn2_BaseElement(ABC):

    def __init__(self, id: str, description: str, bpmn2_BaseElement: set["bpmn2_ExtensionDefinition"] = None, bpmn2_BaseElement5: set["bpmn2_ExtensionAttributeValue"] = None, bpmn2_BaseElement7: set["bpmn2_Documentation"] = None, bpmn2_BaseElement151: "bpmn2_Lane" = None, bpmn2_BaseElement155: "bpmn2_Lane" = None, bpmn2_BaseElement418: "bpmn2_Association" = None, bpmn2_BaseElement421: "bpmn2_Association" = None):
        self.id = id
        self.description = description
        self.bpmn2_BaseElement = bpmn2_BaseElement if bpmn2_BaseElement is not None else set()
        self.bpmn2_BaseElement5 = bpmn2_BaseElement5 if bpmn2_BaseElement5 is not None else set()
        self.bpmn2_BaseElement7 = bpmn2_BaseElement7 if bpmn2_BaseElement7 is not None else set()
        self.bpmn2_BaseElement151 = bpmn2_BaseElement151
        self.bpmn2_BaseElement155 = bpmn2_BaseElement155
        self.bpmn2_BaseElement418 = bpmn2_BaseElement418
        self.bpmn2_BaseElement421 = bpmn2_BaseElement421
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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
                    

    @property
    def bpmn2_BaseElement151(self):
        return self.__bpmn2_BaseElement151

    @bpmn2_BaseElement151.setter
    def bpmn2_BaseElement151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BaseElement__bpmn2_BaseElement151", None)
        self.__bpmn2_BaseElement151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Lane150"):
                opp_val = getattr(old_value, "bpmn2_Lane150", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Lane150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Lane150"):
                opp_val = getattr(value, "bpmn2_Lane150", None)
                setattr(value, "bpmn2_Lane150", self)

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
    def bpmn2_BaseElement421(self):
        return self.__bpmn2_BaseElement421

    @bpmn2_BaseElement421.setter
    def bpmn2_BaseElement421(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BaseElement__bpmn2_BaseElement421", None)
        self.__bpmn2_BaseElement421 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Association420"):
                opp_val = getattr(old_value, "bpmn2_Association420", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Association420", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Association420"):
                opp_val = getattr(value, "bpmn2_Association420", None)
                setattr(value, "bpmn2_Association420", self)

    @property
    def bpmn2_BaseElement418(self):
        return self.__bpmn2_BaseElement418

    @bpmn2_BaseElement418.setter
    def bpmn2_BaseElement418(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BaseElement__bpmn2_BaseElement418", None)
        self.__bpmn2_BaseElement418 = value
        
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
    def bpmn2_BaseElement155(self):
        return self.__bpmn2_BaseElement155

    @bpmn2_BaseElement155.setter
    def bpmn2_BaseElement155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BaseElement__bpmn2_BaseElement155", None)
        self.__bpmn2_BaseElement155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Lane154"):
                opp_val = getattr(old_value, "bpmn2_Lane154", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Lane154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Lane154"):
                opp_val = getattr(value, "bpmn2_Lane154", None)
                setattr(value, "bpmn2_Lane154", self)

class BaseElement:

    pass
class bpmn2_InputOutputSpecification(BaseElement):

    pass
class bpmn2_CategoryValue(BaseElement):

    def __init__(self, value: str, CategoryValue: "bpmn2_FlowElement" = None, categoryValueRef: set["bpmn2_FlowElement"] = None, bpmn2_CategoryValue: "bpmn2_Group" = None, bpmn2_CategoryValue423: "bpmn2_Category" = None):
        self.value = value
        self.CategoryValue = CategoryValue
        self.categoryValueRef = categoryValueRef if categoryValueRef is not None else set()
        self.bpmn2_CategoryValue = bpmn2_CategoryValue
        self.bpmn2_CategoryValue423 = bpmn2_CategoryValue423
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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
    def bpmn2_CategoryValue423(self):
        return self.__bpmn2_CategoryValue423

    @bpmn2_CategoryValue423.setter
    def bpmn2_CategoryValue423(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CategoryValue__bpmn2_CategoryValue423", None)
        self.__bpmn2_CategoryValue423 = value
        
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

class bpmn2_ConversationNode(BaseElement, InteractionNode):

    def __init__(self, name: str, bpmn2_ConversationNode: "bpmn2_Collaboration" = None, bpmn2_ConversationNode227: "bpmn2_ConversationAssociation" = None, bpmn2_ConversationNode230: "bpmn2_ConversationAssociation" = None, bpmn2_ConversationNode232: set["bpmn2_Participant"] = None, bpmn2_ConversationNode235: set["bpmn2_MessageFlow"] = None, bpmn2_ConversationNode238: set["bpmn2_CorrelationKey"] = None, bpmn2_ConversationNode392: "bpmn2_SubConversation" = None):
        self.name = name
        self.bpmn2_ConversationNode = bpmn2_ConversationNode
        self.bpmn2_ConversationNode227 = bpmn2_ConversationNode227
        self.bpmn2_ConversationNode230 = bpmn2_ConversationNode230
        self.bpmn2_ConversationNode232 = bpmn2_ConversationNode232 if bpmn2_ConversationNode232 is not None else set()
        self.bpmn2_ConversationNode235 = bpmn2_ConversationNode235 if bpmn2_ConversationNode235 is not None else set()
        self.bpmn2_ConversationNode238 = bpmn2_ConversationNode238 if bpmn2_ConversationNode238 is not None else set()
        self.bpmn2_ConversationNode392 = bpmn2_ConversationNode392
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_ConversationNode238(self):
        return self.__bpmn2_ConversationNode238

    @bpmn2_ConversationNode238.setter
    def bpmn2_ConversationNode238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ConversationNode__bpmn2_ConversationNode238", None)
        self.__bpmn2_ConversationNode238 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_CorrelationKey239"):
                    opp_val = getattr(item, "bpmn2_CorrelationKey239", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_CorrelationKey239", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_CorrelationKey239"):
                    opp_val = getattr(item, "bpmn2_CorrelationKey239", None)
                    
                    setattr(item, "bpmn2_CorrelationKey239", self)
                    

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
            if hasattr(old_value, "bpmn2_Collaboration184"):
                opp_val = getattr(old_value, "bpmn2_Collaboration184", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Collaboration184"):
                opp_val = getattr(value, "bpmn2_Collaboration184", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Collaboration184", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_ConversationNode232(self):
        return self.__bpmn2_ConversationNode232

    @bpmn2_ConversationNode232.setter
    def bpmn2_ConversationNode232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ConversationNode__bpmn2_ConversationNode232", None)
        self.__bpmn2_ConversationNode232 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Participant233"):
                    opp_val = getattr(item, "bpmn2_Participant233", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Participant233", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Participant233"):
                    opp_val = getattr(item, "bpmn2_Participant233", None)
                    
                    setattr(item, "bpmn2_Participant233", self)
                    

    @property
    def bpmn2_ConversationNode227(self):
        return self.__bpmn2_ConversationNode227

    @bpmn2_ConversationNode227.setter
    def bpmn2_ConversationNode227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ConversationNode__bpmn2_ConversationNode227", None)
        self.__bpmn2_ConversationNode227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ConversationAssociation226"):
                opp_val = getattr(old_value, "bpmn2_ConversationAssociation226", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ConversationAssociation226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ConversationAssociation226"):
                opp_val = getattr(value, "bpmn2_ConversationAssociation226", None)
                setattr(value, "bpmn2_ConversationAssociation226", self)

    @property
    def bpmn2_ConversationNode392(self):
        return self.__bpmn2_ConversationNode392

    @bpmn2_ConversationNode392.setter
    def bpmn2_ConversationNode392(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ConversationNode__bpmn2_ConversationNode392", None)
        self.__bpmn2_ConversationNode392 = value
        
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
    def bpmn2_ConversationNode230(self):
        return self.__bpmn2_ConversationNode230

    @bpmn2_ConversationNode230.setter
    def bpmn2_ConversationNode230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ConversationNode__bpmn2_ConversationNode230", None)
        self.__bpmn2_ConversationNode230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ConversationAssociation229"):
                opp_val = getattr(old_value, "bpmn2_ConversationAssociation229", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ConversationAssociation229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ConversationAssociation229"):
                opp_val = getattr(value, "bpmn2_ConversationAssociation229", None)
                setattr(value, "bpmn2_ConversationAssociation229", self)

    @property
    def bpmn2_ConversationNode235(self):
        return self.__bpmn2_ConversationNode235

    @bpmn2_ConversationNode235.setter
    def bpmn2_ConversationNode235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ConversationNode__bpmn2_ConversationNode235", None)
        self.__bpmn2_ConversationNode235 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_MessageFlow236"):
                    opp_val = getattr(item, "bpmn2_MessageFlow236", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_MessageFlow236", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_MessageFlow236"):
                    opp_val = getattr(item, "bpmn2_MessageFlow236", None)
                    
                    setattr(item, "bpmn2_MessageFlow236", self)
                    

class bpmn2_InputSet(BaseElement):

    def __init__(self, name: str, bpmn2_InputSet: "bpmn2_InputOutputSpecification" = None, InputSet: "bpmn2_DataInput" = None, InputSet62: "bpmn2_DataInput" = None, InputSet64: "bpmn2_DataInput" = None, InputSet76: "bpmn2_OutputSet" = None, inputSetRefs: set["bpmn2_DataInput"] = None, inputSetWithOptional: set["bpmn2_DataInput"] = None, inputSetWithWhileExecuting: set["bpmn2_DataInput"] = None, inputSetRefs59: set["bpmn2_OutputSet"] = None, bpmn2_InputSet85: "bpmn2_InputOutputBinding" = None, bpmn2_InputSet339: "bpmn2_ThrowEvent" = None):
        self.name = name
        self.bpmn2_InputSet = bpmn2_InputSet
        self.InputSet = InputSet
        self.InputSet62 = InputSet62
        self.InputSet64 = InputSet64
        self.InputSet76 = InputSet76
        self.inputSetRefs = inputSetRefs if inputSetRefs is not None else set()
        self.inputSetWithOptional = inputSetWithOptional if inputSetWithOptional is not None else set()
        self.inputSetWithWhileExecuting = inputSetWithWhileExecuting if inputSetWithWhileExecuting is not None else set()
        self.inputSetRefs59 = inputSetRefs59 if inputSetRefs59 is not None else set()
        self.bpmn2_InputSet85 = bpmn2_InputSet85
        self.bpmn2_InputSet339 = bpmn2_InputSet339
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def bpmn2_InputSet339(self):
        return self.__bpmn2_InputSet339

    @bpmn2_InputSet339.setter
    def bpmn2_InputSet339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_InputSet__bpmn2_InputSet339", None)
        self.__bpmn2_InputSet339 = value
        
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

class bpmn2_Auditing(BaseElement):

    pass
class bpmn2_FlowElement(BaseElement):

    def __init__(self, name: str, bpmn2_FlowElement: "bpmn2_FlowElementsContainer" = None, bpmn2_FlowElement137: "bpmn2_Auditing" = None, bpmn2_FlowElement140: "bpmn2_Monitoring" = None, categorizedFlowElements: set["bpmn2_CategoryValue"] = None, FlowElement: "bpmn2_CategoryValue" = None):
        self.name = name
        self.bpmn2_FlowElement = bpmn2_FlowElement
        self.bpmn2_FlowElement137 = bpmn2_FlowElement137
        self.bpmn2_FlowElement140 = bpmn2_FlowElement140
        self.categorizedFlowElements = categorizedFlowElements if categorizedFlowElements is not None else set()
        self.FlowElement = FlowElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_FlowElement140(self):
        return self.__bpmn2_FlowElement140

    @bpmn2_FlowElement140.setter
    def bpmn2_FlowElement140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FlowElement__bpmn2_FlowElement140", None)
        self.__bpmn2_FlowElement140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Monitoring141"):
                opp_val = getattr(old_value, "bpmn2_Monitoring141", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Monitoring141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Monitoring141"):
                opp_val = getattr(value, "bpmn2_Monitoring141", None)
                setattr(value, "bpmn2_Monitoring141", self)

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
    def bpmn2_FlowElement137(self):
        return self.__bpmn2_FlowElement137

    @bpmn2_FlowElement137.setter
    def bpmn2_FlowElement137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FlowElement__bpmn2_FlowElement137", None)
        self.__bpmn2_FlowElement137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Auditing138"):
                opp_val = getattr(old_value, "bpmn2_Auditing138", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Auditing138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Auditing138"):
                opp_val = getattr(value, "bpmn2_Auditing138", None)
                setattr(value, "bpmn2_Auditing138", self)

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

class bpmn2_ComplexBehaviorDefinition(BaseElement):

    pass
class bpmn2_CorrelationSubscription(BaseElement):

    pass
class bpmn2_Lane(BaseElement):

    def __init__(self, name: str, bpmn2_Lane: "bpmn2_LaneSet" = None, bpmn2_Lane147: "bpmn2_LaneSet" = None, bpmn2_Lane150: "bpmn2_BaseElement" = None, lanes: set["bpmn2_FlowNode"] = None, bpmn2_Lane154: "bpmn2_BaseElement" = None, Lane: "bpmn2_FlowNode" = None):
        self.name = name
        self.bpmn2_Lane = bpmn2_Lane
        self.bpmn2_Lane147 = bpmn2_Lane147
        self.bpmn2_Lane150 = bpmn2_Lane150
        self.lanes = lanes if lanes is not None else set()
        self.bpmn2_Lane154 = bpmn2_Lane154
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
            if hasattr(old_value, "bpmn2_LaneSet145"):
                opp_val = getattr(old_value, "bpmn2_LaneSet145", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_LaneSet145"):
                opp_val = getattr(value, "bpmn2_LaneSet145", None)
                if opp_val is None:
                    setattr(value, "bpmn2_LaneSet145", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def bpmn2_Lane150(self):
        return self.__bpmn2_Lane150

    @bpmn2_Lane150.setter
    def bpmn2_Lane150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Lane__bpmn2_Lane150", None)
        self.__bpmn2_Lane150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_BaseElement151"):
                opp_val = getattr(old_value, "bpmn2_BaseElement151", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_BaseElement151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_BaseElement151"):
                opp_val = getattr(value, "bpmn2_BaseElement151", None)
                setattr(value, "bpmn2_BaseElement151", self)

    @property
    def bpmn2_Lane147(self):
        return self.__bpmn2_Lane147

    @bpmn2_Lane147.setter
    def bpmn2_Lane147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Lane__bpmn2_Lane147", None)
        self.__bpmn2_Lane147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_LaneSet148"):
                opp_val = getattr(old_value, "bpmn2_LaneSet148", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_LaneSet148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_LaneSet148"):
                opp_val = getattr(value, "bpmn2_LaneSet148", None)
                setattr(value, "bpmn2_LaneSet148", self)

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
                    

    @property
    def bpmn2_Lane154(self):
        return self.__bpmn2_Lane154

    @bpmn2_Lane154.setter
    def bpmn2_Lane154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Lane__bpmn2_Lane154", None)
        self.__bpmn2_Lane154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_BaseElement155"):
                opp_val = getattr(old_value, "bpmn2_BaseElement155", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_BaseElement155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_BaseElement155"):
                opp_val = getattr(value, "bpmn2_BaseElement155", None)
                setattr(value, "bpmn2_BaseElement155", self)

class bpmn2_ConversationAssociation(BaseElement):

    pass
class bpmn2_MessageFlow(BaseElement):

    def __init__(self, name: str, bpmn2_MessageFlow213: "bpmn2_MessageFlowAssociation" = None, bpmn2_MessageFlow: "bpmn2_Collaboration" = None, bpmn2_MessageFlow218: "bpmn2_InteractionNode" = None, bpmn2_MessageFlow220: "bpmn2_InteractionNode" = None, bpmn2_MessageFlow223: "bpmn2_Message" = None, bpmn2_MessageFlow236: "bpmn2_ConversationNode" = None, bpmn2_MessageFlow216: "bpmn2_MessageFlowAssociation" = None, bpmn2_MessageFlow413: "bpmn2_ChoreographyTask" = None):
        self.name = name
        self.bpmn2_MessageFlow213 = bpmn2_MessageFlow213
        self.bpmn2_MessageFlow = bpmn2_MessageFlow
        self.bpmn2_MessageFlow218 = bpmn2_MessageFlow218
        self.bpmn2_MessageFlow220 = bpmn2_MessageFlow220
        self.bpmn2_MessageFlow223 = bpmn2_MessageFlow223
        self.bpmn2_MessageFlow236 = bpmn2_MessageFlow236
        self.bpmn2_MessageFlow216 = bpmn2_MessageFlow216
        self.bpmn2_MessageFlow413 = bpmn2_MessageFlow413
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_MessageFlow413(self):
        return self.__bpmn2_MessageFlow413

    @bpmn2_MessageFlow413.setter
    def bpmn2_MessageFlow413(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MessageFlow__bpmn2_MessageFlow413", None)
        self.__bpmn2_MessageFlow413 = value
        
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
    def bpmn2_MessageFlow220(self):
        return self.__bpmn2_MessageFlow220

    @bpmn2_MessageFlow220.setter
    def bpmn2_MessageFlow220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MessageFlow__bpmn2_MessageFlow220", None)
        self.__bpmn2_MessageFlow220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_InteractionNode221"):
                opp_val = getattr(old_value, "bpmn2_InteractionNode221", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_InteractionNode221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_InteractionNode221"):
                opp_val = getattr(value, "bpmn2_InteractionNode221", None)
                setattr(value, "bpmn2_InteractionNode221", self)

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
    def bpmn2_MessageFlow(self):
        return self.__bpmn2_MessageFlow

    @bpmn2_MessageFlow.setter
    def bpmn2_MessageFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MessageFlow__bpmn2_MessageFlow", None)
        self.__bpmn2_MessageFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Collaboration180"):
                opp_val = getattr(old_value, "bpmn2_Collaboration180", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Collaboration180"):
                opp_val = getattr(value, "bpmn2_Collaboration180", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Collaboration180", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_MessageFlow223(self):
        return self.__bpmn2_MessageFlow223

    @bpmn2_MessageFlow223.setter
    def bpmn2_MessageFlow223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MessageFlow__bpmn2_MessageFlow223", None)
        self.__bpmn2_MessageFlow223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Message224"):
                opp_val = getattr(old_value, "bpmn2_Message224", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Message224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Message224"):
                opp_val = getattr(value, "bpmn2_Message224", None)
                setattr(value, "bpmn2_Message224", self)

    @property
    def bpmn2_MessageFlow216(self):
        return self.__bpmn2_MessageFlow216

    @bpmn2_MessageFlow216.setter
    def bpmn2_MessageFlow216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MessageFlow__bpmn2_MessageFlow216", None)
        self.__bpmn2_MessageFlow216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_MessageFlowAssociation215"):
                opp_val = getattr(old_value, "bpmn2_MessageFlowAssociation215", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_MessageFlowAssociation215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_MessageFlowAssociation215"):
                opp_val = getattr(value, "bpmn2_MessageFlowAssociation215", None)
                setattr(value, "bpmn2_MessageFlowAssociation215", self)

    @property
    def bpmn2_MessageFlow236(self):
        return self.__bpmn2_MessageFlow236

    @bpmn2_MessageFlow236.setter
    def bpmn2_MessageFlow236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MessageFlow__bpmn2_MessageFlow236", None)
        self.__bpmn2_MessageFlow236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ConversationNode235"):
                opp_val = getattr(old_value, "bpmn2_ConversationNode235", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ConversationNode235"):
                opp_val = getattr(value, "bpmn2_ConversationNode235", None)
                if opp_val is None:
                    setattr(value, "bpmn2_ConversationNode235", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "bpmn2_MessageFlowAssociation212"):
                opp_val = getattr(old_value, "bpmn2_MessageFlowAssociation212", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_MessageFlowAssociation212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_MessageFlowAssociation212"):
                opp_val = getattr(value, "bpmn2_MessageFlowAssociation212", None)
                setattr(value, "bpmn2_MessageFlowAssociation212", self)

class bpmn2_Expression(BaseElement):

    pass
class bpmn2_Relationship(BaseElement):

    def __init__(self, type: str, direction: str, bpmn2_Relationship: set["bpmn2_EObject"] = None, bpmn2_Relationship334: set["bpmn2_EObject"] = None, bpmn2_Relationship484: "bpmn2_Definitions" = None):
        self.type = type
        self.direction = direction
        self.bpmn2_Relationship = bpmn2_Relationship if bpmn2_Relationship is not None else set()
        self.bpmn2_Relationship334 = bpmn2_Relationship334 if bpmn2_Relationship334 is not None else set()
        self.bpmn2_Relationship484 = bpmn2_Relationship484
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

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
                if hasattr(item, "bpmn2_EObject332"):
                    opp_val = getattr(item, "bpmn2_EObject332", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_EObject332", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_EObject332"):
                    opp_val = getattr(item, "bpmn2_EObject332", None)
                    
                    setattr(item, "bpmn2_EObject332", self)
                    

    @property
    def bpmn2_Relationship484(self):
        return self.__bpmn2_Relationship484

    @bpmn2_Relationship484.setter
    def bpmn2_Relationship484(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Relationship__bpmn2_Relationship484", None)
        self.__bpmn2_Relationship484 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Definitions483"):
                opp_val = getattr(old_value, "bpmn2_Definitions483", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Definitions483"):
                opp_val = getattr(value, "bpmn2_Definitions483", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Definitions483", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Relationship334(self):
        return self.__bpmn2_Relationship334

    @bpmn2_Relationship334.setter
    def bpmn2_Relationship334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Relationship__bpmn2_Relationship334", None)
        self.__bpmn2_Relationship334 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_EObject335"):
                    opp_val = getattr(item, "bpmn2_EObject335", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_EObject335", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_EObject335"):
                    opp_val = getattr(item, "bpmn2_EObject335", None)
                    
                    setattr(item, "bpmn2_EObject335", self)
                    

class bpmn2_CorrelationPropertyRetrievalExpression(BaseElement):

    pass
class bpmn2_ResourceRole(BaseElement):

    def __init__(self, name: str, bpmn2_ResourceRole: "bpmn2_GlobalTask" = None, bpmn2_ResourceRole93: "bpmn2_Resource" = None, bpmn2_ResourceRole95: set["bpmn2_ResourceParameterBinding"] = None, bpmn2_ResourceRole97: "bpmn2_ResourceAssignmentExpression" = None, bpmn2_ResourceRole123: "bpmn2_Process" = None, bpmn2_ResourceRole272: "bpmn2_Activity" = None):
        self.name = name
        self.bpmn2_ResourceRole = bpmn2_ResourceRole
        self.bpmn2_ResourceRole93 = bpmn2_ResourceRole93
        self.bpmn2_ResourceRole95 = bpmn2_ResourceRole95 if bpmn2_ResourceRole95 is not None else set()
        self.bpmn2_ResourceRole97 = bpmn2_ResourceRole97
        self.bpmn2_ResourceRole123 = bpmn2_ResourceRole123
        self.bpmn2_ResourceRole272 = bpmn2_ResourceRole272
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

    @property
    def bpmn2_ResourceRole272(self):
        return self.__bpmn2_ResourceRole272

    @bpmn2_ResourceRole272.setter
    def bpmn2_ResourceRole272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ResourceRole__bpmn2_ResourceRole272", None)
        self.__bpmn2_ResourceRole272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Activity271"):
                opp_val = getattr(old_value, "bpmn2_Activity271", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Activity271"):
                opp_val = getattr(value, "bpmn2_Activity271", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Activity271", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_Documentation(BaseElement):

    def __init__(self, text: str, textFormat: str, bpmn2_Documentation: "bpmn2_BaseElement" = None):
        self.text = text
        self.textFormat = textFormat
        self.bpmn2_Documentation = bpmn2_Documentation
        
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

class bpmn2_OutputSet(BaseElement):

    def __init__(self, name: str, bpmn2_OutputSet: "bpmn2_InputOutputSpecification" = None, outputSetRefs: set["bpmn2_DataOutput"] = None, outputSetWithOptional: set["bpmn2_DataOutput"] = None, outputSetWithWhileExecuting: set["bpmn2_DataOutput"] = None, outputSetRefs75: set["bpmn2_InputSet"] = None, OutputSet78: "bpmn2_DataOutput" = None, OutputSet: "bpmn2_InputSet" = None, bpmn2_OutputSet88: "bpmn2_InputOutputBinding" = None, OutputSet80: "bpmn2_DataOutput" = None, OutputSet82: "bpmn2_DataOutput" = None, bpmn2_OutputSet289: "bpmn2_CatchEvent" = None):
        self.name = name
        self.bpmn2_OutputSet = bpmn2_OutputSet
        self.outputSetRefs = outputSetRefs if outputSetRefs is not None else set()
        self.outputSetWithOptional = outputSetWithOptional if outputSetWithOptional is not None else set()
        self.outputSetWithWhileExecuting = outputSetWithWhileExecuting if outputSetWithWhileExecuting is not None else set()
        self.outputSetRefs75 = outputSetRefs75 if outputSetRefs75 is not None else set()
        self.OutputSet78 = OutputSet78
        self.OutputSet = OutputSet
        self.bpmn2_OutputSet88 = bpmn2_OutputSet88
        self.OutputSet80 = OutputSet80
        self.OutputSet82 = OutputSet82
        self.bpmn2_OutputSet289 = bpmn2_OutputSet289
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def bpmn2_OutputSet289(self):
        return self.__bpmn2_OutputSet289

    @bpmn2_OutputSet289.setter
    def bpmn2_OutputSet289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_OutputSet__bpmn2_OutputSet289", None)
        self.__bpmn2_OutputSet289 = value
        
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

class bpmn2_Artifact(BaseElement):

    pass
class bpmn2_Monitoring(BaseElement):

    pass
class bpmn2_ConversationLink(BaseElement):

    def __init__(self, name: str, bpmn2_ConversationLink: "bpmn2_Collaboration" = None, ConversationLink: "bpmn2_InteractionNode" = None, ConversationLink207: "bpmn2_InteractionNode" = None, outgoingConversationLinks: "bpmn2_InteractionNode" = None, incomingConversationLinks: "bpmn2_InteractionNode" = None):
        self.name = name
        self.bpmn2_ConversationLink = bpmn2_ConversationLink
        self.ConversationLink = ConversationLink
        self.ConversationLink207 = ConversationLink207
        self.outgoingConversationLinks = outgoingConversationLinks
        self.incomingConversationLinks = incomingConversationLinks
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "InteractionNode210"):
                opp_val = getattr(old_value, "InteractionNode210", None)
                if opp_val == self:
                    setattr(old_value, "InteractionNode210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InteractionNode210"):
                opp_val = getattr(value, "InteractionNode210", None)
                setattr(value, "InteractionNode210", self)

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
            if hasattr(old_value, "targetRef204"):
                opp_val = getattr(old_value, "targetRef204", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targetRef204"):
                opp_val = getattr(value, "targetRef204", None)
                if opp_val is None:
                    setattr(value, "targetRef204", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ConversationLink207(self):
        return self.__ConversationLink207

    @ConversationLink207.setter
    def ConversationLink207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ConversationLink__ConversationLink207", None)
        self.__ConversationLink207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceRef206"):
                opp_val = getattr(old_value, "sourceRef206", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceRef206"):
                opp_val = getattr(value, "sourceRef206", None)
                if opp_val is None:
                    setattr(value, "sourceRef206", set([self]))
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
    def bpmn2_ConversationLink(self):
        return self.__bpmn2_ConversationLink

    @bpmn2_ConversationLink.setter
    def bpmn2_ConversationLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ConversationLink__bpmn2_ConversationLink", None)
        self.__bpmn2_ConversationLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Collaboration186"):
                opp_val = getattr(old_value, "bpmn2_Collaboration186", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Collaboration186"):
                opp_val = getattr(value, "bpmn2_Collaboration186", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Collaboration186", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_MessageFlowAssociation(BaseElement):

    pass
class bpmn2_Assignment(BaseElement):

    pass
class bpmn2_LoopCharacteristics(BaseElement):

    pass
class bpmn2_LaneSet(BaseElement):

    def __init__(self, name: str, bpmn2_LaneSet: "bpmn2_FlowElementsContainer" = None, bpmn2_LaneSet145: set["bpmn2_Lane"] = None, bpmn2_LaneSet148: "bpmn2_Lane" = None):
        self.name = name
        self.bpmn2_LaneSet = bpmn2_LaneSet
        self.bpmn2_LaneSet145 = bpmn2_LaneSet145 if bpmn2_LaneSet145 is not None else set()
        self.bpmn2_LaneSet148 = bpmn2_LaneSet148
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_LaneSet145(self):
        return self.__bpmn2_LaneSet145

    @bpmn2_LaneSet145.setter
    def bpmn2_LaneSet145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_LaneSet__bpmn2_LaneSet145", None)
        self.__bpmn2_LaneSet145 = value if value is not None else set()
        
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
            if hasattr(old_value, "bpmn2_FlowElementsContainer135"):
                opp_val = getattr(old_value, "bpmn2_FlowElementsContainer135", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_FlowElementsContainer135"):
                opp_val = getattr(value, "bpmn2_FlowElementsContainer135", None)
                if opp_val is None:
                    setattr(value, "bpmn2_FlowElementsContainer135", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_LaneSet148(self):
        return self.__bpmn2_LaneSet148

    @bpmn2_LaneSet148.setter
    def bpmn2_LaneSet148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_LaneSet__bpmn2_LaneSet148", None)
        self.__bpmn2_LaneSet148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Lane147"):
                opp_val = getattr(old_value, "bpmn2_Lane147", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Lane147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Lane147"):
                opp_val = getattr(value, "bpmn2_Lane147", None)
                setattr(value, "bpmn2_Lane147", self)

class bpmn2_ItemAwareElement(BaseElement):

    pass
class bpmn2_ParticipantAssociation(BaseElement):

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

class bpmn2_Definitions(BaseElement):

    def __init__(self, name: str, targetNamespace: str, expressionLanguage: str, typeLanguage: str, exporter: str, exporterVersion: str, bpmn2_Definitions: set["bpmn2_Import"] = None, bpmn2_Definitions480: set["bpmn2_Extension"] = None, bpmn2_Definitions483: set["bpmn2_Relationship"] = None, bpmn2_Definitions488: set["bpmn2_BPMNDiagram"] = None, bpmn2_Definitions486: set["bpmn2_RootElement"] = None):
        self.name = name
        self.targetNamespace = targetNamespace
        self.expressionLanguage = expressionLanguage
        self.typeLanguage = typeLanguage
        self.exporter = exporter
        self.exporterVersion = exporterVersion
        self.bpmn2_Definitions = bpmn2_Definitions if bpmn2_Definitions is not None else set()
        self.bpmn2_Definitions480 = bpmn2_Definitions480 if bpmn2_Definitions480 is not None else set()
        self.bpmn2_Definitions483 = bpmn2_Definitions483 if bpmn2_Definitions483 is not None else set()
        self.bpmn2_Definitions488 = bpmn2_Definitions488 if bpmn2_Definitions488 is not None else set()
        self.bpmn2_Definitions486 = bpmn2_Definitions486 if bpmn2_Definitions486 is not None else set()
        
    @property
    def expressionLanguage(self) -> str:
        return self.__expressionLanguage

    @expressionLanguage.setter
    def expressionLanguage(self, expressionLanguage: str):
        self.__expressionLanguage = expressionLanguage

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
    def exporter(self) -> str:
        return self.__exporter

    @exporter.setter
    def exporter(self, exporter: str):
        self.__exporter = exporter

    @property
    def typeLanguage(self) -> str:
        return self.__typeLanguage

    @typeLanguage.setter
    def typeLanguage(self, typeLanguage: str):
        self.__typeLanguage = typeLanguage

    @property
    def exporterVersion(self) -> str:
        return self.__exporterVersion

    @exporterVersion.setter
    def exporterVersion(self, exporterVersion: str):
        self.__exporterVersion = exporterVersion

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
                if hasattr(item, "bpmn2_Relationship484"):
                    opp_val = getattr(item, "bpmn2_Relationship484", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Relationship484", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Relationship484"):
                    opp_val = getattr(item, "bpmn2_Relationship484", None)
                    
                    setattr(item, "bpmn2_Relationship484", self)
                    

    @property
    def bpmn2_Definitions480(self):
        return self.__bpmn2_Definitions480

    @bpmn2_Definitions480.setter
    def bpmn2_Definitions480(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Definitions__bpmn2_Definitions480", None)
        self.__bpmn2_Definitions480 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Extension481"):
                    opp_val = getattr(item, "bpmn2_Extension481", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Extension481", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Extension481"):
                    opp_val = getattr(item, "bpmn2_Extension481", None)
                    
                    setattr(item, "bpmn2_Extension481", self)
                    

    @property
    def bpmn2_Definitions486(self):
        return self.__bpmn2_Definitions486

    @bpmn2_Definitions486.setter
    def bpmn2_Definitions486(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Definitions__bpmn2_Definitions486", None)
        self.__bpmn2_Definitions486 = value if value is not None else set()
        
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
                if hasattr(item, "bpmn2_Import478"):
                    opp_val = getattr(item, "bpmn2_Import478", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Import478", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Import478"):
                    opp_val = getattr(item, "bpmn2_Import478", None)
                    
                    setattr(item, "bpmn2_Import478", self)
                    

    @property
    def bpmn2_Definitions488(self):
        return self.__bpmn2_Definitions488

    @bpmn2_Definitions488.setter
    def bpmn2_Definitions488(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Definitions__bpmn2_Definitions488", None)
        self.__bpmn2_Definitions488 = value if value is not None else set()
        
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
                    

class bpmn2_CorrelationKey(BaseElement):

    def __init__(self, name: str, bpmn2_CorrelationKey: "bpmn2_Collaboration" = None, bpmn2_CorrelationKey239: "bpmn2_ConversationNode" = None, bpmn2_CorrelationKey241: set["bpmn2_CorrelationProperty"] = None, bpmn2_CorrelationKey260: "bpmn2_CorrelationSubscription" = None, bpmn2_CorrelationKey404: "bpmn2_ChoreographyActivity" = None):
        self.name = name
        self.bpmn2_CorrelationKey = bpmn2_CorrelationKey
        self.bpmn2_CorrelationKey239 = bpmn2_CorrelationKey239
        self.bpmn2_CorrelationKey241 = bpmn2_CorrelationKey241 if bpmn2_CorrelationKey241 is not None else set()
        self.bpmn2_CorrelationKey260 = bpmn2_CorrelationKey260
        self.bpmn2_CorrelationKey404 = bpmn2_CorrelationKey404
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_CorrelationKey260(self):
        return self.__bpmn2_CorrelationKey260

    @bpmn2_CorrelationKey260.setter
    def bpmn2_CorrelationKey260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CorrelationKey__bpmn2_CorrelationKey260", None)
        self.__bpmn2_CorrelationKey260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CorrelationSubscription259"):
                opp_val = getattr(old_value, "bpmn2_CorrelationSubscription259", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_CorrelationSubscription259", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CorrelationSubscription259"):
                opp_val = getattr(value, "bpmn2_CorrelationSubscription259", None)
                setattr(value, "bpmn2_CorrelationSubscription259", self)

    @property
    def bpmn2_CorrelationKey241(self):
        return self.__bpmn2_CorrelationKey241

    @bpmn2_CorrelationKey241.setter
    def bpmn2_CorrelationKey241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CorrelationKey__bpmn2_CorrelationKey241", None)
        self.__bpmn2_CorrelationKey241 = value if value is not None else set()
        
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
    def bpmn2_CorrelationKey239(self):
        return self.__bpmn2_CorrelationKey239

    @bpmn2_CorrelationKey239.setter
    def bpmn2_CorrelationKey239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CorrelationKey__bpmn2_CorrelationKey239", None)
        self.__bpmn2_CorrelationKey239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ConversationNode238"):
                opp_val = getattr(old_value, "bpmn2_ConversationNode238", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ConversationNode238"):
                opp_val = getattr(value, "bpmn2_ConversationNode238", None)
                if opp_val is None:
                    setattr(value, "bpmn2_ConversationNode238", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_CorrelationKey404(self):
        return self.__bpmn2_CorrelationKey404

    @bpmn2_CorrelationKey404.setter
    def bpmn2_CorrelationKey404(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CorrelationKey__bpmn2_CorrelationKey404", None)
        self.__bpmn2_CorrelationKey404 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ChoreographyActivity403"):
                opp_val = getattr(old_value, "bpmn2_ChoreographyActivity403", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ChoreographyActivity403"):
                opp_val = getattr(value, "bpmn2_ChoreographyActivity403", None)
                if opp_val is None:
                    setattr(value, "bpmn2_ChoreographyActivity403", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "bpmn2_Collaboration182"):
                opp_val = getattr(old_value, "bpmn2_Collaboration182", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Collaboration182"):
                opp_val = getattr(value, "bpmn2_Collaboration182", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Collaboration182", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_ResourceParameter(BaseElement):

    def __init__(self, name: str, isRequired: bool, bpmn2_ResourceParameter: "bpmn2_Resource" = None, bpmn2_ResourceParameter101: "bpmn2_ItemDefinition" = None, bpmn2_ResourceParameter107: "bpmn2_ResourceParameterBinding" = None):
        self.name = name
        self.isRequired = isRequired
        self.bpmn2_ResourceParameter = bpmn2_ResourceParameter
        self.bpmn2_ResourceParameter101 = bpmn2_ResourceParameter101
        self.bpmn2_ResourceParameter107 = bpmn2_ResourceParameter107
        
    @property
    def isRequired(self) -> bool:
        return self.__isRequired

    @isRequired.setter
    def isRequired(self, isRequired: bool):
        self.__isRequired = isRequired

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

class bpmn2_Participant(BaseElement, InteractionNode):

    def __init__(self, name: str, bpmn2_Participant189: "bpmn2_ParticipantAssociation" = None, bpmn2_Participant192: "bpmn2_ParticipantAssociation" = None, bpmn2_Participant194: set["bpmn2_Interface"] = None, bpmn2_Participant197: "bpmn2_ParticipantMultiplicity" = None, bpmn2_Participant199: set["bpmn2_EndPoint"] = None, bpmn2_Participant201: "bpmn2_Process" = None, bpmn2_Participant: "bpmn2_Collaboration" = None, bpmn2_Participant233: "bpmn2_ConversationNode" = None, bpmn2_Participant394: "bpmn2_PartnerEntity" = None, bpmn2_Participant396: "bpmn2_PartnerRole" = None, bpmn2_Participant398: "bpmn2_ChoreographyActivity" = None, bpmn2_Participant401: "bpmn2_ChoreographyActivity" = None, bpmn2_Participant415: "bpmn2_GlobalChoreographyTask" = None):
        self.name = name
        self.bpmn2_Participant189 = bpmn2_Participant189
        self.bpmn2_Participant192 = bpmn2_Participant192
        self.bpmn2_Participant194 = bpmn2_Participant194 if bpmn2_Participant194 is not None else set()
        self.bpmn2_Participant197 = bpmn2_Participant197
        self.bpmn2_Participant199 = bpmn2_Participant199 if bpmn2_Participant199 is not None else set()
        self.bpmn2_Participant201 = bpmn2_Participant201
        self.bpmn2_Participant = bpmn2_Participant
        self.bpmn2_Participant233 = bpmn2_Participant233
        self.bpmn2_Participant394 = bpmn2_Participant394
        self.bpmn2_Participant396 = bpmn2_Participant396
        self.bpmn2_Participant398 = bpmn2_Participant398
        self.bpmn2_Participant401 = bpmn2_Participant401
        self.bpmn2_Participant415 = bpmn2_Participant415
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_Participant401(self):
        return self.__bpmn2_Participant401

    @bpmn2_Participant401.setter
    def bpmn2_Participant401(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant401", None)
        self.__bpmn2_Participant401 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ChoreographyActivity400"):
                opp_val = getattr(old_value, "bpmn2_ChoreographyActivity400", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ChoreographyActivity400", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ChoreographyActivity400"):
                opp_val = getattr(value, "bpmn2_ChoreographyActivity400", None)
                setattr(value, "bpmn2_ChoreographyActivity400", self)

    @property
    def bpmn2_Participant394(self):
        return self.__bpmn2_Participant394

    @bpmn2_Participant394.setter
    def bpmn2_Participant394(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant394", None)
        self.__bpmn2_Participant394 = value
        
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
    def bpmn2_Participant398(self):
        return self.__bpmn2_Participant398

    @bpmn2_Participant398.setter
    def bpmn2_Participant398(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant398", None)
        self.__bpmn2_Participant398 = value
        
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
    def bpmn2_Participant189(self):
        return self.__bpmn2_Participant189

    @bpmn2_Participant189.setter
    def bpmn2_Participant189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant189", None)
        self.__bpmn2_Participant189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ParticipantAssociation188"):
                opp_val = getattr(old_value, "bpmn2_ParticipantAssociation188", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ParticipantAssociation188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ParticipantAssociation188"):
                opp_val = getattr(value, "bpmn2_ParticipantAssociation188", None)
                setattr(value, "bpmn2_ParticipantAssociation188", self)

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
            if hasattr(old_value, "bpmn2_ParticipantAssociation191"):
                opp_val = getattr(old_value, "bpmn2_ParticipantAssociation191", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ParticipantAssociation191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ParticipantAssociation191"):
                opp_val = getattr(value, "bpmn2_ParticipantAssociation191", None)
                setattr(value, "bpmn2_ParticipantAssociation191", self)

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
                if hasattr(item, "bpmn2_Interface195"):
                    opp_val = getattr(item, "bpmn2_Interface195", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Interface195", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Interface195"):
                    opp_val = getattr(item, "bpmn2_Interface195", None)
                    
                    setattr(item, "bpmn2_Interface195", self)
                    

    @property
    def bpmn2_Participant201(self):
        return self.__bpmn2_Participant201

    @bpmn2_Participant201.setter
    def bpmn2_Participant201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant201", None)
        self.__bpmn2_Participant201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Process202"):
                opp_val = getattr(old_value, "bpmn2_Process202", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Process202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Process202"):
                opp_val = getattr(value, "bpmn2_Process202", None)
                setattr(value, "bpmn2_Process202", self)

    @property
    def bpmn2_Participant233(self):
        return self.__bpmn2_Participant233

    @bpmn2_Participant233.setter
    def bpmn2_Participant233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant233", None)
        self.__bpmn2_Participant233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ConversationNode232"):
                opp_val = getattr(old_value, "bpmn2_ConversationNode232", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ConversationNode232"):
                opp_val = getattr(value, "bpmn2_ConversationNode232", None)
                if opp_val is None:
                    setattr(value, "bpmn2_ConversationNode232", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Participant199(self):
        return self.__bpmn2_Participant199

    @bpmn2_Participant199.setter
    def bpmn2_Participant199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant199", None)
        self.__bpmn2_Participant199 = value if value is not None else set()
        
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
    def bpmn2_Participant(self):
        return self.__bpmn2_Participant

    @bpmn2_Participant.setter
    def bpmn2_Participant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant", None)
        self.__bpmn2_Participant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Collaboration178"):
                opp_val = getattr(old_value, "bpmn2_Collaboration178", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Collaboration178"):
                opp_val = getattr(value, "bpmn2_Collaboration178", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Collaboration178", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Participant197(self):
        return self.__bpmn2_Participant197

    @bpmn2_Participant197.setter
    def bpmn2_Participant197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant197", None)
        self.__bpmn2_Participant197 = value
        
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
    def bpmn2_Participant396(self):
        return self.__bpmn2_Participant396

    @bpmn2_Participant396.setter
    def bpmn2_Participant396(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant396", None)
        self.__bpmn2_Participant396 = value
        
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
    def bpmn2_Participant415(self):
        return self.__bpmn2_Participant415

    @bpmn2_Participant415.setter
    def bpmn2_Participant415(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Participant__bpmn2_Participant415", None)
        self.__bpmn2_Participant415 = value
        
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

class bpmn2_Rendering(BaseElement):

    pass
class bpmn2_FlowElementsContainer(BaseElement):

    pass
class bpmn2_CorrelationPropertyBinding(BaseElement):

    pass
class bpmn2_DataAssociation(BaseElement):

    pass
class bpmn2_RootElement(BaseElement):

    pass
class bpmn2_EObject:

    pass
class bpmn2_Operation(BaseElement):

    def __init__(self, name: str, bpmn2_Operation: "bpmn2_Interface" = None, bpmn2_Operation19: "bpmn2_Message" = None, bpmn2_Operation21: "bpmn2_Message" = None, bpmn2_Operation24: set["bpmn2_Error"] = None, bpmn2_Operation26: "bpmn2_EObject" = None, bpmn2_Operation91: "bpmn2_InputOutputBinding" = None, bpmn2_Operation377: "bpmn2_MessageEventDefinition" = None, bpmn2_Operation425: "bpmn2_ServiceTask" = None, bpmn2_Operation466: "bpmn2_SendTask" = None, bpmn2_Operation471: "bpmn2_ReceiveTask" = None):
        self.name = name
        self.bpmn2_Operation = bpmn2_Operation
        self.bpmn2_Operation19 = bpmn2_Operation19
        self.bpmn2_Operation21 = bpmn2_Operation21
        self.bpmn2_Operation24 = bpmn2_Operation24 if bpmn2_Operation24 is not None else set()
        self.bpmn2_Operation26 = bpmn2_Operation26
        self.bpmn2_Operation91 = bpmn2_Operation91
        self.bpmn2_Operation377 = bpmn2_Operation377
        self.bpmn2_Operation425 = bpmn2_Operation425
        self.bpmn2_Operation466 = bpmn2_Operation466
        self.bpmn2_Operation471 = bpmn2_Operation471
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def bpmn2_Operation377(self):
        return self.__bpmn2_Operation377

    @bpmn2_Operation377.setter
    def bpmn2_Operation377(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Operation__bpmn2_Operation377", None)
        self.__bpmn2_Operation377 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_MessageEventDefinition376"):
                opp_val = getattr(old_value, "bpmn2_MessageEventDefinition376", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_MessageEventDefinition376", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_MessageEventDefinition376"):
                opp_val = getattr(value, "bpmn2_MessageEventDefinition376", None)
                setattr(value, "bpmn2_MessageEventDefinition376", self)

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
    def bpmn2_Operation425(self):
        return self.__bpmn2_Operation425

    @bpmn2_Operation425.setter
    def bpmn2_Operation425(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Operation__bpmn2_Operation425", None)
        self.__bpmn2_Operation425 = value
        
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
    def bpmn2_Operation471(self):
        return self.__bpmn2_Operation471

    @bpmn2_Operation471.setter
    def bpmn2_Operation471(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Operation__bpmn2_Operation471", None)
        self.__bpmn2_Operation471 = value
        
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

class RootElement:

    pass
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
                if hasattr(item, "bpmn2_CategoryValue423"):
                    opp_val = getattr(item, "bpmn2_CategoryValue423", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_CategoryValue423", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_CategoryValue423"):
                    opp_val = getattr(item, "bpmn2_CategoryValue423", None)
                    
                    setattr(item, "bpmn2_CategoryValue423", self)
                    

class bpmn2_Signal(RootElement):

    def __init__(self, name: str, bpmn2_Signal: "bpmn2_SignalEventDefinition" = None, bpmn2_Signal382: "bpmn2_ItemDefinition" = None):
        self.name = name
        self.bpmn2_Signal = bpmn2_Signal
        self.bpmn2_Signal382 = bpmn2_Signal382
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

    @property
    def bpmn2_Signal382(self):
        return self.__bpmn2_Signal382

    @bpmn2_Signal382.setter
    def bpmn2_Signal382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Signal__bpmn2_Signal382", None)
        self.__bpmn2_Signal382 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemDefinition383"):
                opp_val = getattr(old_value, "bpmn2_ItemDefinition383", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemDefinition383", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemDefinition383"):
                opp_val = getattr(value, "bpmn2_ItemDefinition383", None)
                setattr(value, "bpmn2_ItemDefinition383", self)

class bpmn2_EndPoint(RootElement):

    pass
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
                if hasattr(item, "bpmn2_Participant396"):
                    opp_val = getattr(item, "bpmn2_Participant396", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Participant396", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Participant396"):
                    opp_val = getattr(item, "bpmn2_Participant396", None)
                    
                    setattr(item, "bpmn2_Participant396", self)
                    

class bpmn2_CallableElement(RootElement):

    def __init__(self, name: str, bpmn2_CallableElement: "bpmn2_InputOutputSpecification" = None, bpmn2_CallableElement41: set["bpmn2_Interface"] = None, bpmn2_CallableElement44: set["bpmn2_InputOutputBinding"] = None, bpmn2_CallableElement464: "bpmn2_CallActivity" = None):
        self.name = name
        self.bpmn2_CallableElement = bpmn2_CallableElement
        self.bpmn2_CallableElement41 = bpmn2_CallableElement41 if bpmn2_CallableElement41 is not None else set()
        self.bpmn2_CallableElement44 = bpmn2_CallableElement44 if bpmn2_CallableElement44 is not None else set()
        self.bpmn2_CallableElement464 = bpmn2_CallableElement464
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_CallableElement464(self):
        return self.__bpmn2_CallableElement464

    @bpmn2_CallableElement464.setter
    def bpmn2_CallableElement464(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CallableElement__bpmn2_CallableElement464", None)
        self.__bpmn2_CallableElement464 = value
        
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
                    

class bpmn2_CorrelationProperty(RootElement):

    def __init__(self, name: str, bpmn2_CorrelationProperty: "bpmn2_CorrelationKey" = None, bpmn2_CorrelationProperty243: set["bpmn2_CorrelationPropertyRetrievalExpression"] = None, bpmn2_CorrelationProperty245: "bpmn2_ItemDefinition" = None, bpmn2_CorrelationProperty268: "bpmn2_CorrelationPropertyBinding" = None):
        self.name = name
        self.bpmn2_CorrelationProperty = bpmn2_CorrelationProperty
        self.bpmn2_CorrelationProperty243 = bpmn2_CorrelationProperty243 if bpmn2_CorrelationProperty243 is not None else set()
        self.bpmn2_CorrelationProperty245 = bpmn2_CorrelationProperty245
        self.bpmn2_CorrelationProperty268 = bpmn2_CorrelationProperty268
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bpmn2_CorrelationProperty245(self):
        return self.__bpmn2_CorrelationProperty245

    @bpmn2_CorrelationProperty245.setter
    def bpmn2_CorrelationProperty245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CorrelationProperty__bpmn2_CorrelationProperty245", None)
        self.__bpmn2_CorrelationProperty245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemDefinition246"):
                opp_val = getattr(old_value, "bpmn2_ItemDefinition246", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemDefinition246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemDefinition246"):
                opp_val = getattr(value, "bpmn2_ItemDefinition246", None)
                setattr(value, "bpmn2_ItemDefinition246", self)

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
            if hasattr(old_value, "bpmn2_CorrelationKey241"):
                opp_val = getattr(old_value, "bpmn2_CorrelationKey241", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CorrelationKey241"):
                opp_val = getattr(value, "bpmn2_CorrelationKey241", None)
                if opp_val is None:
                    setattr(value, "bpmn2_CorrelationKey241", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_CorrelationProperty243(self):
        return self.__bpmn2_CorrelationProperty243

    @bpmn2_CorrelationProperty243.setter
    def bpmn2_CorrelationProperty243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CorrelationProperty__bpmn2_CorrelationProperty243", None)
        self.__bpmn2_CorrelationProperty243 = value if value is not None else set()
        
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
                    

    @property
    def bpmn2_CorrelationProperty268(self):
        return self.__bpmn2_CorrelationProperty268

    @bpmn2_CorrelationProperty268.setter
    def bpmn2_CorrelationProperty268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CorrelationProperty__bpmn2_CorrelationProperty268", None)
        self.__bpmn2_CorrelationProperty268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CorrelationPropertyBinding267"):
                opp_val = getattr(old_value, "bpmn2_CorrelationPropertyBinding267", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_CorrelationPropertyBinding267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CorrelationPropertyBinding267"):
                opp_val = getattr(value, "bpmn2_CorrelationPropertyBinding267", None)
                setattr(value, "bpmn2_CorrelationPropertyBinding267", self)

class bpmn2_DataStore(RootElement, ItemAwareElement):

    def __init__(self, capacity: int, isUnlimited: bool, name: str, bpmn2_DataStore: "bpmn2_DataStoreReference" = None):
        self.capacity = capacity
        self.isUnlimited = isUnlimited
        self.name = name
        self.bpmn2_DataStore = bpmn2_DataStore
        
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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

class bpmn2_Error(RootElement):

    def __init__(self, name: str, errorCode: str, bpmn2_Error: "bpmn2_Operation" = None, bpmn2_Error36: "bpmn2_ItemDefinition" = None, bpmn2_Error353: "bpmn2_ErrorEventDefinition" = None):
        self.name = name
        self.errorCode = errorCode
        self.bpmn2_Error = bpmn2_Error
        self.bpmn2_Error36 = bpmn2_Error36
        self.bpmn2_Error353 = bpmn2_Error353
        
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
    def bpmn2_Error353(self):
        return self.__bpmn2_Error353

    @bpmn2_Error353.setter
    def bpmn2_Error353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Error__bpmn2_Error353", None)
        self.__bpmn2_Error353 = value
        
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
class bpmn2_Collaboration(RootElement):

    def __init__(self, name: str, isClosed: bool, bpmn2_Collaboration: "bpmn2_Process" = None, bpmn2_Collaboration167: set["bpmn2_Choreography"] = None, bpmn2_Collaboration169: set["bpmn2_Artifact"] = None, bpmn2_Collaboration172: set["bpmn2_ParticipantAssociation"] = None, bpmn2_Collaboration174: set["bpmn2_MessageFlowAssociation"] = None, bpmn2_Collaboration176: "bpmn2_ConversationAssociation" = None, bpmn2_Collaboration182: set["bpmn2_CorrelationKey"] = None, bpmn2_Collaboration184: set["bpmn2_ConversationNode"] = None, bpmn2_Collaboration186: set["bpmn2_ConversationLink"] = None, bpmn2_Collaboration178: set["bpmn2_Participant"] = None, bpmn2_Collaboration180: set["bpmn2_MessageFlow"] = None, bpmn2_Collaboration387: "bpmn2_CallConversation" = None):
        self.name = name
        self.isClosed = isClosed
        self.bpmn2_Collaboration = bpmn2_Collaboration
        self.bpmn2_Collaboration167 = bpmn2_Collaboration167 if bpmn2_Collaboration167 is not None else set()
        self.bpmn2_Collaboration169 = bpmn2_Collaboration169 if bpmn2_Collaboration169 is not None else set()
        self.bpmn2_Collaboration172 = bpmn2_Collaboration172 if bpmn2_Collaboration172 is not None else set()
        self.bpmn2_Collaboration174 = bpmn2_Collaboration174 if bpmn2_Collaboration174 is not None else set()
        self.bpmn2_Collaboration176 = bpmn2_Collaboration176
        self.bpmn2_Collaboration182 = bpmn2_Collaboration182 if bpmn2_Collaboration182 is not None else set()
        self.bpmn2_Collaboration184 = bpmn2_Collaboration184 if bpmn2_Collaboration184 is not None else set()
        self.bpmn2_Collaboration186 = bpmn2_Collaboration186 if bpmn2_Collaboration186 is not None else set()
        self.bpmn2_Collaboration178 = bpmn2_Collaboration178 if bpmn2_Collaboration178 is not None else set()
        self.bpmn2_Collaboration180 = bpmn2_Collaboration180 if bpmn2_Collaboration180 is not None else set()
        self.bpmn2_Collaboration387 = bpmn2_Collaboration387
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isClosed(self) -> bool:
        return self.__isClosed

    @isClosed.setter
    def isClosed(self, isClosed: bool):
        self.__isClosed = isClosed

    @property
    def bpmn2_Collaboration182(self):
        return self.__bpmn2_Collaboration182

    @bpmn2_Collaboration182.setter
    def bpmn2_Collaboration182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration182", None)
        self.__bpmn2_Collaboration182 = value if value is not None else set()
        
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
    def bpmn2_Collaboration176(self):
        return self.__bpmn2_Collaboration176

    @bpmn2_Collaboration176.setter
    def bpmn2_Collaboration176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration176", None)
        self.__bpmn2_Collaboration176 = value
        
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

    @property
    def bpmn2_Collaboration180(self):
        return self.__bpmn2_Collaboration180

    @bpmn2_Collaboration180.setter
    def bpmn2_Collaboration180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration180", None)
        self.__bpmn2_Collaboration180 = value if value is not None else set()
        
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
    def bpmn2_Collaboration387(self):
        return self.__bpmn2_Collaboration387

    @bpmn2_Collaboration387.setter
    def bpmn2_Collaboration387(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration387", None)
        self.__bpmn2_Collaboration387 = value
        
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
    def bpmn2_Collaboration172(self):
        return self.__bpmn2_Collaboration172

    @bpmn2_Collaboration172.setter
    def bpmn2_Collaboration172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration172", None)
        self.__bpmn2_Collaboration172 = value if value is not None else set()
        
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
    def bpmn2_Collaboration174(self):
        return self.__bpmn2_Collaboration174

    @bpmn2_Collaboration174.setter
    def bpmn2_Collaboration174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration174", None)
        self.__bpmn2_Collaboration174 = value if value is not None else set()
        
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
                if hasattr(item, "bpmn2_Artifact170"):
                    opp_val = getattr(item, "bpmn2_Artifact170", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Artifact170", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Artifact170"):
                    opp_val = getattr(item, "bpmn2_Artifact170", None)
                    
                    setattr(item, "bpmn2_Artifact170", self)
                    

    @property
    def bpmn2_Collaboration178(self):
        return self.__bpmn2_Collaboration178

    @bpmn2_Collaboration178.setter
    def bpmn2_Collaboration178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration178", None)
        self.__bpmn2_Collaboration178 = value if value is not None else set()
        
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
    def bpmn2_Collaboration184(self):
        return self.__bpmn2_Collaboration184

    @bpmn2_Collaboration184.setter
    def bpmn2_Collaboration184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration184", None)
        self.__bpmn2_Collaboration184 = value if value is not None else set()
        
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
    def bpmn2_Collaboration186(self):
        return self.__bpmn2_Collaboration186

    @bpmn2_Collaboration186.setter
    def bpmn2_Collaboration186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration186", None)
        self.__bpmn2_Collaboration186 = value if value is not None else set()
        
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
                    

class bpmn2_ItemDefinition(RootElement):

    def __init__(self, itemKind: str, isCollection: bool, bpmn2_ItemDefinition: "bpmn2_Message" = None, bpmn2_ItemDefinition31: "bpmn2_EObject" = None, bpmn2_ItemDefinition34: "bpmn2_Import" = None, bpmn2_ItemDefinition37: "bpmn2_Error" = None, bpmn2_ItemDefinition66: "bpmn2_ItemAwareElement" = None, bpmn2_ItemDefinition102: "bpmn2_ResourceParameter" = None, bpmn2_ItemDefinition246: "bpmn2_CorrelationProperty" = None, bpmn2_ItemDefinition257: "bpmn2_FormalExpression" = None, bpmn2_ItemDefinition357: "bpmn2_Escalation" = None, bpmn2_ItemDefinition383: "bpmn2_Signal" = None):
        self.itemKind = itemKind
        self.isCollection = isCollection
        self.bpmn2_ItemDefinition = bpmn2_ItemDefinition
        self.bpmn2_ItemDefinition31 = bpmn2_ItemDefinition31
        self.bpmn2_ItemDefinition34 = bpmn2_ItemDefinition34
        self.bpmn2_ItemDefinition37 = bpmn2_ItemDefinition37
        self.bpmn2_ItemDefinition66 = bpmn2_ItemDefinition66
        self.bpmn2_ItemDefinition102 = bpmn2_ItemDefinition102
        self.bpmn2_ItemDefinition246 = bpmn2_ItemDefinition246
        self.bpmn2_ItemDefinition257 = bpmn2_ItemDefinition257
        self.bpmn2_ItemDefinition357 = bpmn2_ItemDefinition357
        self.bpmn2_ItemDefinition383 = bpmn2_ItemDefinition383
        
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

    @property
    def bpmn2_ItemDefinition246(self):
        return self.__bpmn2_ItemDefinition246

    @bpmn2_ItemDefinition246.setter
    def bpmn2_ItemDefinition246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition246", None)
        self.__bpmn2_ItemDefinition246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CorrelationProperty245"):
                opp_val = getattr(old_value, "bpmn2_CorrelationProperty245", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_CorrelationProperty245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CorrelationProperty245"):
                opp_val = getattr(value, "bpmn2_CorrelationProperty245", None)
                setattr(value, "bpmn2_CorrelationProperty245", self)

    @property
    def bpmn2_ItemDefinition357(self):
        return self.__bpmn2_ItemDefinition357

    @bpmn2_ItemDefinition357.setter
    def bpmn2_ItemDefinition357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition357", None)
        self.__bpmn2_ItemDefinition357 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Escalation356"):
                opp_val = getattr(old_value, "bpmn2_Escalation356", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Escalation356", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Escalation356"):
                opp_val = getattr(value, "bpmn2_Escalation356", None)
                setattr(value, "bpmn2_Escalation356", self)

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
    def bpmn2_ItemDefinition257(self):
        return self.__bpmn2_ItemDefinition257

    @bpmn2_ItemDefinition257.setter
    def bpmn2_ItemDefinition257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition257", None)
        self.__bpmn2_ItemDefinition257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_FormalExpression256"):
                opp_val = getattr(old_value, "bpmn2_FormalExpression256", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_FormalExpression256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_FormalExpression256"):
                opp_val = getattr(value, "bpmn2_FormalExpression256", None)
                setattr(value, "bpmn2_FormalExpression256", self)

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
    def bpmn2_ItemDefinition383(self):
        return self.__bpmn2_ItemDefinition383

    @bpmn2_ItemDefinition383.setter
    def bpmn2_ItemDefinition383(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition383", None)
        self.__bpmn2_ItemDefinition383 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Signal382"):
                opp_val = getattr(old_value, "bpmn2_Signal382", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Signal382", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Signal382"):
                opp_val = getattr(value, "bpmn2_Signal382", None)
                setattr(value, "bpmn2_Signal382", self)

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
                if hasattr(item, "bpmn2_Participant394"):
                    opp_val = getattr(item, "bpmn2_Participant394", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Participant394", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Participant394"):
                    opp_val = getattr(item, "bpmn2_Participant394", None)
                    
                    setattr(item, "bpmn2_Participant394", self)
                    

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

class bpmn2_Interface(RootElement):

    def __init__(self, name: str, bpmn2_Interface: set["bpmn2_Operation"] = None, bpmn2_Interface2: "bpmn2_EObject" = None, bpmn2_Interface42: "bpmn2_CallableElement" = None, bpmn2_Interface195: "bpmn2_Participant" = None):
        self.name = name
        self.bpmn2_Interface = bpmn2_Interface if bpmn2_Interface is not None else set()
        self.bpmn2_Interface2 = bpmn2_Interface2
        self.bpmn2_Interface42 = bpmn2_Interface42
        self.bpmn2_Interface195 = bpmn2_Interface195
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def bpmn2_Interface195(self):
        return self.__bpmn2_Interface195

    @bpmn2_Interface195.setter
    def bpmn2_Interface195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Interface__bpmn2_Interface195", None)
        self.__bpmn2_Interface195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Participant194"):
                opp_val = getattr(old_value, "bpmn2_Participant194", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Participant194"):
                opp_val = getattr(value, "bpmn2_Participant194", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Participant194", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_Message(RootElement):

    def __init__(self, name: str, bpmn2_Message: "bpmn2_Operation" = None, bpmn2_Message22: "bpmn2_Operation" = None, bpmn2_Message29: "bpmn2_ItemDefinition" = None, bpmn2_Message224: "bpmn2_MessageFlow" = None, bpmn2_Message251: "bpmn2_CorrelationPropertyRetrievalExpression" = None, bpmn2_Message374: "bpmn2_MessageEventDefinition" = None, bpmn2_Message469: "bpmn2_SendTask" = None, bpmn2_Message474: "bpmn2_ReceiveTask" = None):
        self.name = name
        self.bpmn2_Message = bpmn2_Message
        self.bpmn2_Message22 = bpmn2_Message22
        self.bpmn2_Message29 = bpmn2_Message29
        self.bpmn2_Message224 = bpmn2_Message224
        self.bpmn2_Message251 = bpmn2_Message251
        self.bpmn2_Message374 = bpmn2_Message374
        self.bpmn2_Message469 = bpmn2_Message469
        self.bpmn2_Message474 = bpmn2_Message474
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def bpmn2_Message469(self):
        return self.__bpmn2_Message469

    @bpmn2_Message469.setter
    def bpmn2_Message469(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Message__bpmn2_Message469", None)
        self.__bpmn2_Message469 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_SendTask468"):
                opp_val = getattr(old_value, "bpmn2_SendTask468", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_SendTask468", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_SendTask468"):
                opp_val = getattr(value, "bpmn2_SendTask468", None)
                setattr(value, "bpmn2_SendTask468", self)

    @property
    def bpmn2_Message474(self):
        return self.__bpmn2_Message474

    @bpmn2_Message474.setter
    def bpmn2_Message474(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Message__bpmn2_Message474", None)
        self.__bpmn2_Message474 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ReceiveTask473"):
                opp_val = getattr(old_value, "bpmn2_ReceiveTask473", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ReceiveTask473", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ReceiveTask473"):
                opp_val = getattr(value, "bpmn2_ReceiveTask473", None)
                setattr(value, "bpmn2_ReceiveTask473", self)

    @property
    def bpmn2_Message224(self):
        return self.__bpmn2_Message224

    @bpmn2_Message224.setter
    def bpmn2_Message224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Message__bpmn2_Message224", None)
        self.__bpmn2_Message224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_MessageFlow223"):
                opp_val = getattr(old_value, "bpmn2_MessageFlow223", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_MessageFlow223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_MessageFlow223"):
                opp_val = getattr(value, "bpmn2_MessageFlow223", None)
                setattr(value, "bpmn2_MessageFlow223", self)

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
    def bpmn2_Message251(self):
        return self.__bpmn2_Message251

    @bpmn2_Message251.setter
    def bpmn2_Message251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Message__bpmn2_Message251", None)
        self.__bpmn2_Message251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CorrelationPropertyRetrievalExpression250"):
                opp_val = getattr(old_value, "bpmn2_CorrelationPropertyRetrievalExpression250", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_CorrelationPropertyRetrievalExpression250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CorrelationPropertyRetrievalExpression250"):
                opp_val = getattr(value, "bpmn2_CorrelationPropertyRetrievalExpression250", None)
                setattr(value, "bpmn2_CorrelationPropertyRetrievalExpression250", self)

    @property
    def bpmn2_Message374(self):
        return self.__bpmn2_Message374

    @bpmn2_Message374.setter
    def bpmn2_Message374(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Message__bpmn2_Message374", None)
        self.__bpmn2_Message374 = value
        
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
