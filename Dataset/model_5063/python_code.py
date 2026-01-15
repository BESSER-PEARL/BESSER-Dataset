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
class ItemKind(Enum):
    Physical = "Physical"
    Information = "Information"
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
class ChoreographyLoopType(Enum):
    None = "None"
    Standard = "Standard"
    MultiInstanceSequential = "MultiInstanceSequential"
    MultiInstanceParallel = "MultiInstanceParallel"
class EventBasedGatewayType(Enum):
    Parallel = "Parallel"
    Exclusive = "Exclusive"


############################################
# Definition of Classes
############################################

class HumanPerformer:

    pass
class ResourceRole:

    pass
class LoopCharacteristics:

    pass
class Performer:

    pass
class CallableElement:

    pass
class Choreography:

    pass
class GlobalTask:

    pass
class Expression:

    pass
class bpmn2_ExtensionAttributeDefinition:

    def __init__(self, name: str, type: str, isReference: bool, extensionAttributeDefinitions: "bpmn2_ExtensionDefinition" = None, bpmn2_ExtensionAttributeDefinition: "bpmn2_ExtensionAttributeValue" = None, ExtensionAttributeDefinition: "bpmn2_ExtensionDefinition" = None):
        self.name = name
        self.type = type
        self.isReference = isReference
        self.extensionAttributeDefinitions = extensionAttributeDefinitions
        self.bpmn2_ExtensionAttributeDefinition = bpmn2_ExtensionAttributeDefinition
        self.ExtensionAttributeDefinition = ExtensionAttributeDefinition
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

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
    def bpmn2_ExtensionAttributeDefinition(self):
        return self.__bpmn2_ExtensionAttributeDefinition

    @bpmn2_ExtensionAttributeDefinition.setter
    def bpmn2_ExtensionAttributeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ExtensionAttributeDefinition__bpmn2_ExtensionAttributeDefinition", None)
        self.__bpmn2_ExtensionAttributeDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ExtensionAttributeValue564"):
                opp_val = getattr(old_value, "bpmn2_ExtensionAttributeValue564", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ExtensionAttributeValue564", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ExtensionAttributeValue564"):
                opp_val = getattr(value, "bpmn2_ExtensionAttributeValue564", None)
                setattr(value, "bpmn2_ExtensionAttributeValue564", self)

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

class ThrowEvent:

    pass
class bpmn2_BPMNDiagram:

    pass
class FlowElement:

    pass
class DataAssociation:

    pass
class bpmn2_Document:

    pass
class ItemAwareElement:

    pass
class InteractionNode:

    pass
class bpmn2_InteractionNode:

    pass
class Gateway:

    pass
class Event:

    pass
class EventDefinition:

    pass
class RootElement:

    pass
class FlowElementsContainer:

    pass
class Collaboration:

    pass
class bpmn2_ExtensionDefinition:

    def __init__(self, name: str, bpmn2_ExtensionDefinition: "bpmn2_BaseElement" = None, ExtensionDefinition: "bpmn2_ExtensionAttributeDefinition" = None, bpmn2_ExtensionDefinition558: "bpmn2_Extension" = None, extensionDefinition: set["bpmn2_ExtensionAttributeDefinition"] = None):
        self.name = name
        self.bpmn2_ExtensionDefinition = bpmn2_ExtensionDefinition
        self.ExtensionDefinition = ExtensionDefinition
        self.bpmn2_ExtensionDefinition558 = bpmn2_ExtensionDefinition558
        self.extensionDefinition = extensionDefinition if extensionDefinition is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def bpmn2_ExtensionDefinition(self):
        return self.__bpmn2_ExtensionDefinition

    @bpmn2_ExtensionDefinition.setter
    def bpmn2_ExtensionDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ExtensionDefinition__bpmn2_ExtensionDefinition", None)
        self.__bpmn2_ExtensionDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_BaseElement339"):
                opp_val = getattr(old_value, "bpmn2_BaseElement339", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_BaseElement339"):
                opp_val = getattr(value, "bpmn2_BaseElement339", None)
                if opp_val is None:
                    setattr(value, "bpmn2_BaseElement339", set([self]))
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
                    

    @property
    def bpmn2_ExtensionDefinition558(self):
        return self.__bpmn2_ExtensionDefinition558

    @bpmn2_ExtensionDefinition558.setter
    def bpmn2_ExtensionDefinition558(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ExtensionDefinition__bpmn2_ExtensionDefinition558", None)
        self.__bpmn2_ExtensionDefinition558 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Extension557"):
                opp_val = getattr(old_value, "bpmn2_Extension557", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Extension557", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Extension557"):
                opp_val = getattr(value, "bpmn2_Extension557", None)
                setattr(value, "bpmn2_Extension557", self)

class Artifact:

    pass
class BaseElement:

    pass
class bpmn2_FlowElementsContainer(BaseElement):

    pass
class bpmn2_ItemAwareElement(BaseElement):

    pass
class ConversationNode:

    pass
class ChoreographyActivity:

    pass
class Activity:

    pass
class Task:

    pass
class CatchEvent:

    pass
class bpmn2_OrganisationalUnit:

    pass
class bpmn2_Criterion:

    pass
class bpmn2_Competency:

    pass
class SubProcess:

    pass
class bpmn2_Role:

    pass
class bpmn2_Position:

    pass
class bpmn2_TimerEventDefinition(EventDefinition):

    pass
class bpmn2_ThrowEvent(Event):

    pass
class bpmn2_TextAnnotation(Artifact):

    def __init__(self, text: str, textFormat: str, bpmn2_TextAnnotation: "bpmn2_DocumentRoot" = None):
        self.text = text
        self.textFormat = textFormat
        self.bpmn2_TextAnnotation = bpmn2_TextAnnotation
        
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
    def bpmn2_TextAnnotation(self):
        return self.__bpmn2_TextAnnotation

    @bpmn2_TextAnnotation.setter
    def bpmn2_TextAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_TextAnnotation__bpmn2_TextAnnotation", None)
        self.__bpmn2_TextAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DocumentRoot267"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot267", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot267"):
                opp_val = getattr(value, "bpmn2_DocumentRoot267", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot267", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_TerminateEventDefinition(EventDefinition):

    pass
class FlowNode:

    pass
class bpmn2_UserTask(Task):

    def __init__(self, implementation: str, bpmn2_UserTask: "bpmn2_DocumentRoot" = None, bpmn2_UserTask907: set["bpmn2_Rendering"] = None):
        self.implementation = implementation
        self.bpmn2_UserTask = bpmn2_UserTask
        self.bpmn2_UserTask907 = bpmn2_UserTask907 if bpmn2_UserTask907 is not None else set()
        
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
        self.__bpmn2_UserTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DocumentRoot275"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot275", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot275"):
                opp_val = getattr(value, "bpmn2_DocumentRoot275", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot275", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_UserTask907(self):
        return self.__bpmn2_UserTask907

    @bpmn2_UserTask907.setter
    def bpmn2_UserTask907(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_UserTask__bpmn2_UserTask907", None)
        self.__bpmn2_UserTask907 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Rendering908"):
                    opp_val = getattr(item, "bpmn2_Rendering908", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Rendering908", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Rendering908"):
                    opp_val = getattr(item, "bpmn2_Rendering908", None)
                    
                    setattr(item, "bpmn2_Rendering908", self)
                    

class bpmn2_Transaction(SubProcess):

    def __init__(self, protocol: str, method: str, bpmn2_Transaction: "bpmn2_DocumentRoot" = None):
        self.protocol = protocol
        self.method = method
        self.bpmn2_Transaction = bpmn2_Transaction
        
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

    @property
    def bpmn2_Transaction(self):
        return self.__bpmn2_Transaction

    @bpmn2_Transaction.setter
    def bpmn2_Transaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Transaction__bpmn2_Transaction", None)
        self.__bpmn2_Transaction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DocumentRoot273"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot273", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot273"):
                opp_val = getattr(value, "bpmn2_DocumentRoot273", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot273", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_SubChoreography(FlowElementsContainer, ChoreographyActivity):

    pass
class bpmn2_StartEvent(CatchEvent):

    def __init__(self, isInterrupting: bool, bpmn2_StartEvent: "bpmn2_DocumentRoot" = None):
        self.isInterrupting = isInterrupting
        self.bpmn2_StartEvent = bpmn2_StartEvent
        
    @property
    def isInterrupting(self) -> bool:
        return self.__isInterrupting

    @isInterrupting.setter
    def isInterrupting(self, isInterrupting: bool):
        self.__isInterrupting = isInterrupting

    @property
    def bpmn2_StartEvent(self):
        return self.__bpmn2_StartEvent

    @bpmn2_StartEvent.setter
    def bpmn2_StartEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_StartEvent__bpmn2_StartEvent", None)
        self.__bpmn2_StartEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DocumentRoot252"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot252", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot252"):
                opp_val = getattr(value, "bpmn2_DocumentRoot252", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot252", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_StandardLoopCharacteristics(LoopCharacteristics):

    def __init__(self, loopMaximum: str, testBefore: bool, bpmn2_StandardLoopCharacteristics: "bpmn2_DocumentRoot" = None, bpmn2_StandardLoopCharacteristics866: "bpmn2_Expression" = None):
        self.loopMaximum = loopMaximum
        self.testBefore = testBefore
        self.bpmn2_StandardLoopCharacteristics = bpmn2_StandardLoopCharacteristics
        self.bpmn2_StandardLoopCharacteristics866 = bpmn2_StandardLoopCharacteristics866
        
    @property
    def loopMaximum(self) -> str:
        return self.__loopMaximum

    @loopMaximum.setter
    def loopMaximum(self, loopMaximum: str):
        self.__loopMaximum = loopMaximum

    @property
    def testBefore(self) -> bool:
        return self.__testBefore

    @testBefore.setter
    def testBefore(self, testBefore: bool):
        self.__testBefore = testBefore

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
            if hasattr(old_value, "bpmn2_DocumentRoot250"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot250", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot250"):
                opp_val = getattr(value, "bpmn2_DocumentRoot250", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot250", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_StandardLoopCharacteristics866(self):
        return self.__bpmn2_StandardLoopCharacteristics866

    @bpmn2_StandardLoopCharacteristics866.setter
    def bpmn2_StandardLoopCharacteristics866(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_StandardLoopCharacteristics__bpmn2_StandardLoopCharacteristics866", None)
        self.__bpmn2_StandardLoopCharacteristics866 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Expression867"):
                opp_val = getattr(old_value, "bpmn2_Expression867", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Expression867", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Expression867"):
                opp_val = getattr(value, "bpmn2_Expression867", None)
                setattr(value, "bpmn2_Expression867", self)

class bpmn2_SignalEventDefinition(EventDefinition):

    pass
class bpmn2_Signal(RootElement):

    pass
class bpmn2_ServiceTask(Task):

    def __init__(self, implementation: str, bpmn2_ServiceTask: "bpmn2_DocumentRoot" = None, bpmn2_ServiceTask857: "bpmn2_Operation" = None):
        self.implementation = implementation
        self.bpmn2_ServiceTask = bpmn2_ServiceTask
        self.bpmn2_ServiceTask857 = bpmn2_ServiceTask857
        
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
            if hasattr(old_value, "bpmn2_DocumentRoot244"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot244", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot244"):
                opp_val = getattr(value, "bpmn2_DocumentRoot244", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot244", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_ServiceTask857(self):
        return self.__bpmn2_ServiceTask857

    @bpmn2_ServiceTask857.setter
    def bpmn2_ServiceTask857(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ServiceTask__bpmn2_ServiceTask857", None)
        self.__bpmn2_ServiceTask857 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Operation858"):
                opp_val = getattr(old_value, "bpmn2_Operation858", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Operation858", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Operation858"):
                opp_val = getattr(value, "bpmn2_Operation858", None)
                setattr(value, "bpmn2_Operation858", self)

class bpmn2_Task(Activity, InteractionNode):

    pass
class bpmn2_SubProcess(FlowElementsContainer, Activity):

    def __init__(self, triggeredByEvent: bool, bpmn2_SubProcess: "bpmn2_DocumentRoot" = None, bpmn2_SubProcess875: set["bpmn2_Artifact"] = None, bpmn2_SubProcess878: set["bpmn2_Process"] = None):
        self.triggeredByEvent = triggeredByEvent
        self.bpmn2_SubProcess = bpmn2_SubProcess
        self.bpmn2_SubProcess875 = bpmn2_SubProcess875 if bpmn2_SubProcess875 is not None else set()
        self.bpmn2_SubProcess878 = bpmn2_SubProcess878 if bpmn2_SubProcess878 is not None else set()
        
    @property
    def triggeredByEvent(self) -> bool:
        return self.__triggeredByEvent

    @triggeredByEvent.setter
    def triggeredByEvent(self, triggeredByEvent: bool):
        self.__triggeredByEvent = triggeredByEvent

    @property
    def bpmn2_SubProcess875(self):
        return self.__bpmn2_SubProcess875

    @bpmn2_SubProcess875.setter
    def bpmn2_SubProcess875(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SubProcess__bpmn2_SubProcess875", None)
        self.__bpmn2_SubProcess875 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Artifact876"):
                    opp_val = getattr(item, "bpmn2_Artifact876", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Artifact876", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Artifact876"):
                    opp_val = getattr(item, "bpmn2_Artifact876", None)
                    
                    setattr(item, "bpmn2_Artifact876", self)
                    

    @property
    def bpmn2_SubProcess878(self):
        return self.__bpmn2_SubProcess878

    @bpmn2_SubProcess878.setter
    def bpmn2_SubProcess878(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SubProcess__bpmn2_SubProcess878", None)
        self.__bpmn2_SubProcess878 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Process879"):
                    opp_val = getattr(item, "bpmn2_Process879", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Process879", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Process879"):
                    opp_val = getattr(item, "bpmn2_Process879", None)
                    
                    setattr(item, "bpmn2_Process879", self)
                    

    @property
    def bpmn2_SubProcess(self):
        return self.__bpmn2_SubProcess

    @bpmn2_SubProcess.setter
    def bpmn2_SubProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SubProcess__bpmn2_SubProcess", None)
        self.__bpmn2_SubProcess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DocumentRoot258"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot258", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot258"):
                opp_val = getattr(value, "bpmn2_DocumentRoot258", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot258", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_SubConversation(ConversationNode):

    pass
class bpmn2_ResourceParameterBinding(BaseElement):

    pass
class bpmn2_ResourceParameter(BaseElement):

    def __init__(self, isRequired: bool, bpmn2_ResourceParameter: "bpmn2_DocumentRoot" = None, bpmn2_ResourceParameter833: "bpmn2_ResourceParameterBinding" = None, bpmn2_ResourceParameter821: "bpmn2_Resource" = None, bpmn2_ResourceParameter826: "bpmn2_ItemDefinition" = None):
        self.isRequired = isRequired
        self.bpmn2_ResourceParameter = bpmn2_ResourceParameter
        self.bpmn2_ResourceParameter833 = bpmn2_ResourceParameter833
        self.bpmn2_ResourceParameter821 = bpmn2_ResourceParameter821
        self.bpmn2_ResourceParameter826 = bpmn2_ResourceParameter826
        
    @property
    def isRequired(self) -> bool:
        return self.__isRequired

    @isRequired.setter
    def isRequired(self, isRequired: bool):
        self.__isRequired = isRequired

    @property
    def bpmn2_ResourceParameter821(self):
        return self.__bpmn2_ResourceParameter821

    @bpmn2_ResourceParameter821.setter
    def bpmn2_ResourceParameter821(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ResourceParameter__bpmn2_ResourceParameter821", None)
        self.__bpmn2_ResourceParameter821 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Resource820"):
                opp_val = getattr(old_value, "bpmn2_Resource820", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Resource820"):
                opp_val = getattr(value, "bpmn2_Resource820", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Resource820", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_ResourceParameter826(self):
        return self.__bpmn2_ResourceParameter826

    @bpmn2_ResourceParameter826.setter
    def bpmn2_ResourceParameter826(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ResourceParameter__bpmn2_ResourceParameter826", None)
        self.__bpmn2_ResourceParameter826 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemDefinition827"):
                opp_val = getattr(old_value, "bpmn2_ItemDefinition827", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemDefinition827", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemDefinition827"):
                opp_val = getattr(value, "bpmn2_ItemDefinition827", None)
                setattr(value, "bpmn2_ItemDefinition827", self)

    @property
    def bpmn2_ResourceParameter833(self):
        return self.__bpmn2_ResourceParameter833

    @bpmn2_ResourceParameter833.setter
    def bpmn2_ResourceParameter833(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ResourceParameter__bpmn2_ResourceParameter833", None)
        self.__bpmn2_ResourceParameter833 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ResourceParameterBinding832"):
                opp_val = getattr(old_value, "bpmn2_ResourceParameterBinding832", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ResourceParameterBinding832", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ResourceParameterBinding832"):
                opp_val = getattr(value, "bpmn2_ResourceParameterBinding832", None)
                setattr(value, "bpmn2_ResourceParameterBinding832", self)

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
            if hasattr(old_value, "bpmn2_DocumentRoot232"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot232", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot232"):
                opp_val = getattr(value, "bpmn2_DocumentRoot232", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot232", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_ResourceAssignmentExpression(BaseElement):

    pass
class bpmn2_Resource(RootElement):

    pass
class bpmn2_Rendering(BaseElement):

    pass
class bpmn2_SequenceFlow(FlowElement):

    def __init__(self, isImmediate: bool, bpmn2_SequenceFlow: "bpmn2_DocumentRoot" = None, bpmn2_SequenceFlow297: "bpmn2_Activity" = None, bpmn2_SequenceFlow442: "bpmn2_ComplexGateway" = None, bpmn2_SequenceFlow555: "bpmn2_ExclusiveGateway" = None, SequenceFlow: "bpmn2_FlowNode" = None, SequenceFlow583: "bpmn2_FlowNode" = None, bpmn2_SequenceFlow601: "bpmn2_InclusiveGateway" = None, bpmn2_SequenceFlow850: "bpmn2_Expression" = None, outgoing: "bpmn2_FlowNode" = None, incoming: "bpmn2_FlowNode" = None):
        self.isImmediate = isImmediate
        self.bpmn2_SequenceFlow = bpmn2_SequenceFlow
        self.bpmn2_SequenceFlow297 = bpmn2_SequenceFlow297
        self.bpmn2_SequenceFlow442 = bpmn2_SequenceFlow442
        self.bpmn2_SequenceFlow555 = bpmn2_SequenceFlow555
        self.SequenceFlow = SequenceFlow
        self.SequenceFlow583 = SequenceFlow583
        self.bpmn2_SequenceFlow601 = bpmn2_SequenceFlow601
        self.bpmn2_SequenceFlow850 = bpmn2_SequenceFlow850
        self.outgoing = outgoing
        self.incoming = incoming
        
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
            if hasattr(old_value, "FlowNode855"):
                opp_val = getattr(old_value, "FlowNode855", None)
                if opp_val == self:
                    setattr(old_value, "FlowNode855", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowNode855"):
                opp_val = getattr(value, "FlowNode855", None)
                setattr(value, "FlowNode855", self)

    @property
    def bpmn2_SequenceFlow850(self):
        return self.__bpmn2_SequenceFlow850

    @bpmn2_SequenceFlow850.setter
    def bpmn2_SequenceFlow850(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SequenceFlow__bpmn2_SequenceFlow850", None)
        self.__bpmn2_SequenceFlow850 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Expression851"):
                opp_val = getattr(old_value, "bpmn2_Expression851", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Expression851", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Expression851"):
                opp_val = getattr(value, "bpmn2_Expression851", None)
                setattr(value, "bpmn2_Expression851", self)

    @property
    def bpmn2_SequenceFlow297(self):
        return self.__bpmn2_SequenceFlow297

    @bpmn2_SequenceFlow297.setter
    def bpmn2_SequenceFlow297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SequenceFlow__bpmn2_SequenceFlow297", None)
        self.__bpmn2_SequenceFlow297 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Activity296"):
                opp_val = getattr(old_value, "bpmn2_Activity296", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Activity296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Activity296"):
                opp_val = getattr(value, "bpmn2_Activity296", None)
                setattr(value, "bpmn2_Activity296", self)

    @property
    def bpmn2_SequenceFlow601(self):
        return self.__bpmn2_SequenceFlow601

    @bpmn2_SequenceFlow601.setter
    def bpmn2_SequenceFlow601(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SequenceFlow__bpmn2_SequenceFlow601", None)
        self.__bpmn2_SequenceFlow601 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_InclusiveGateway600"):
                opp_val = getattr(old_value, "bpmn2_InclusiveGateway600", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_InclusiveGateway600", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_InclusiveGateway600"):
                opp_val = getattr(value, "bpmn2_InclusiveGateway600", None)
                setattr(value, "bpmn2_InclusiveGateway600", self)

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
            if hasattr(old_value, "FlowNode853"):
                opp_val = getattr(old_value, "FlowNode853", None)
                if opp_val == self:
                    setattr(old_value, "FlowNode853", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowNode853"):
                opp_val = getattr(value, "FlowNode853", None)
                setattr(value, "FlowNode853", self)

    @property
    def SequenceFlow583(self):
        return self.__SequenceFlow583

    @SequenceFlow583.setter
    def SequenceFlow583(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SequenceFlow__SequenceFlow583", None)
        self.__SequenceFlow583 = value
        
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
    def bpmn2_SequenceFlow442(self):
        return self.__bpmn2_SequenceFlow442

    @bpmn2_SequenceFlow442.setter
    def bpmn2_SequenceFlow442(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SequenceFlow__bpmn2_SequenceFlow442", None)
        self.__bpmn2_SequenceFlow442 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ComplexGateway441"):
                opp_val = getattr(old_value, "bpmn2_ComplexGateway441", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ComplexGateway441", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ComplexGateway441"):
                opp_val = getattr(value, "bpmn2_ComplexGateway441", None)
                setattr(value, "bpmn2_ComplexGateway441", self)

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
            if hasattr(old_value, "bpmn2_DocumentRoot242"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot242", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot242"):
                opp_val = getattr(value, "bpmn2_DocumentRoot242", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot242", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_SequenceFlow555(self):
        return self.__bpmn2_SequenceFlow555

    @bpmn2_SequenceFlow555.setter
    def bpmn2_SequenceFlow555(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SequenceFlow__bpmn2_SequenceFlow555", None)
        self.__bpmn2_SequenceFlow555 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ExclusiveGateway554"):
                opp_val = getattr(old_value, "bpmn2_ExclusiveGateway554", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ExclusiveGateway554", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ExclusiveGateway554"):
                opp_val = getattr(value, "bpmn2_ExclusiveGateway554", None)
                setattr(value, "bpmn2_ExclusiveGateway554", self)

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

class bpmn2_SendTask(Task):

    def __init__(self, implementation: str, bpmn2_SendTask: "bpmn2_DocumentRoot" = None, bpmn2_SendTask844: "bpmn2_Message" = None, bpmn2_SendTask847: "bpmn2_Operation" = None):
        self.implementation = implementation
        self.bpmn2_SendTask = bpmn2_SendTask
        self.bpmn2_SendTask844 = bpmn2_SendTask844
        self.bpmn2_SendTask847 = bpmn2_SendTask847
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def bpmn2_SendTask844(self):
        return self.__bpmn2_SendTask844

    @bpmn2_SendTask844.setter
    def bpmn2_SendTask844(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SendTask__bpmn2_SendTask844", None)
        self.__bpmn2_SendTask844 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Message845"):
                opp_val = getattr(old_value, "bpmn2_Message845", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Message845", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Message845"):
                opp_val = getattr(value, "bpmn2_Message845", None)
                setattr(value, "bpmn2_Message845", self)

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
            if hasattr(old_value, "bpmn2_DocumentRoot240"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot240", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot240"):
                opp_val = getattr(value, "bpmn2_DocumentRoot240", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot240", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_SendTask847(self):
        return self.__bpmn2_SendTask847

    @bpmn2_SendTask847.setter
    def bpmn2_SendTask847(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_SendTask__bpmn2_SendTask847", None)
        self.__bpmn2_SendTask847 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Operation848"):
                opp_val = getattr(old_value, "bpmn2_Operation848", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Operation848", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Operation848"):
                opp_val = getattr(value, "bpmn2_Operation848", None)
                setattr(value, "bpmn2_Operation848", self)

class bpmn2_ScriptTask(Task):

    def __init__(self, script: str, scriptFormat: str, bpmn2_ScriptTask: "bpmn2_DocumentRoot" = None):
        self.script = script
        self.scriptFormat = scriptFormat
        self.bpmn2_ScriptTask = bpmn2_ScriptTask
        
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

    @property
    def bpmn2_ScriptTask(self):
        return self.__bpmn2_ScriptTask

    @bpmn2_ScriptTask.setter
    def bpmn2_ScriptTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ScriptTask__bpmn2_ScriptTask", None)
        self.__bpmn2_ScriptTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DocumentRoot238"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot238", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot238"):
                opp_val = getattr(value, "bpmn2_DocumentRoot238", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot238", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_EObject:

    pass
class bpmn2_PotentialOwner(HumanPerformer):

    pass
class bpmn2_PartnerRole(RootElement):

    pass
class bpmn2_PartnerEntity(RootElement):

    pass
class bpmn2_ParticipantMultiplicity(BaseElement):

    def __init__(self, maximum: int, minimum: int, bpmn2_ParticipantMultiplicity: "bpmn2_DocumentRoot" = None, bpmn2_ParticipantMultiplicity767: "bpmn2_Participant" = None):
        self.maximum = maximum
        self.minimum = minimum
        self.bpmn2_ParticipantMultiplicity = bpmn2_ParticipantMultiplicity
        self.bpmn2_ParticipantMultiplicity767 = bpmn2_ParticipantMultiplicity767
        
    @property
    def maximum(self) -> int:
        return self.__maximum

    @maximum.setter
    def maximum(self, maximum: int):
        self.__maximum = maximum

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
            if hasattr(old_value, "bpmn2_DocumentRoot210"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot210", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot210"):
                opp_val = getattr(value, "bpmn2_DocumentRoot210", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot210", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_ParticipantMultiplicity767(self):
        return self.__bpmn2_ParticipantMultiplicity767

    @bpmn2_ParticipantMultiplicity767.setter
    def bpmn2_ParticipantMultiplicity767(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ParticipantMultiplicity__bpmn2_ParticipantMultiplicity767", None)
        self.__bpmn2_ParticipantMultiplicity767 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Participant766"):
                opp_val = getattr(old_value, "bpmn2_Participant766", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Participant766", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Participant766"):
                opp_val = getattr(value, "bpmn2_Participant766", None)
                setattr(value, "bpmn2_Participant766", self)

class bpmn2_ParticipantAssociation(BaseElement):

    pass
class bpmn2_Participant(BaseElement, InteractionNode):

    pass
class bpmn2_ParallelGateway(Gateway):

    pass
class bpmn2_Relationship(BaseElement):

    def __init__(self, direction: str, type: str, bpmn2_Relationship: "bpmn2_DocumentRoot" = None, bpmn2_Relationship537: "bpmn2_Definitions" = None, bpmn2_Relationship814: set["bpmn2_EObject"] = None, bpmn2_Relationship817: set["bpmn2_EObject"] = None):
        self.direction = direction
        self.type = type
        self.bpmn2_Relationship = bpmn2_Relationship
        self.bpmn2_Relationship537 = bpmn2_Relationship537
        self.bpmn2_Relationship814 = bpmn2_Relationship814 if bpmn2_Relationship814 is not None else set()
        self.bpmn2_Relationship817 = bpmn2_Relationship817 if bpmn2_Relationship817 is not None else set()
        
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
        self.__bpmn2_Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DocumentRoot224"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot224", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot224"):
                opp_val = getattr(value, "bpmn2_DocumentRoot224", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot224", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Relationship537(self):
        return self.__bpmn2_Relationship537

    @bpmn2_Relationship537.setter
    def bpmn2_Relationship537(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Relationship__bpmn2_Relationship537", None)
        self.__bpmn2_Relationship537 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Definitions536"):
                opp_val = getattr(old_value, "bpmn2_Definitions536", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Definitions536"):
                opp_val = getattr(value, "bpmn2_Definitions536", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Definitions536", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Relationship817(self):
        return self.__bpmn2_Relationship817

    @bpmn2_Relationship817.setter
    def bpmn2_Relationship817(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Relationship__bpmn2_Relationship817", None)
        self.__bpmn2_Relationship817 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_EObject818"):
                    opp_val = getattr(item, "bpmn2_EObject818", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_EObject818", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_EObject818"):
                    opp_val = getattr(item, "bpmn2_EObject818", None)
                    
                    setattr(item, "bpmn2_EObject818", self)
                    

    @property
    def bpmn2_Relationship814(self):
        return self.__bpmn2_Relationship814

    @bpmn2_Relationship814.setter
    def bpmn2_Relationship814(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Relationship__bpmn2_Relationship814", None)
        self.__bpmn2_Relationship814 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_EObject815"):
                    opp_val = getattr(item, "bpmn2_EObject815", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_EObject815", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_EObject815"):
                    opp_val = getattr(item, "bpmn2_EObject815", None)
                    
                    setattr(item, "bpmn2_EObject815", self)
                    

class bpmn2_ReceiveTask(Task):

    def __init__(self, implementation: str, instantiate: bool, bpmn2_ReceiveTask: "bpmn2_DocumentRoot" = None, bpmn2_ReceiveTask808: "bpmn2_Message" = None, bpmn2_ReceiveTask811: "bpmn2_Operation" = None):
        self.implementation = implementation
        self.instantiate = instantiate
        self.bpmn2_ReceiveTask = bpmn2_ReceiveTask
        self.bpmn2_ReceiveTask808 = bpmn2_ReceiveTask808
        self.bpmn2_ReceiveTask811 = bpmn2_ReceiveTask811
        
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
    def bpmn2_ReceiveTask808(self):
        return self.__bpmn2_ReceiveTask808

    @bpmn2_ReceiveTask808.setter
    def bpmn2_ReceiveTask808(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ReceiveTask__bpmn2_ReceiveTask808", None)
        self.__bpmn2_ReceiveTask808 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Message809"):
                opp_val = getattr(old_value, "bpmn2_Message809", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Message809", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Message809"):
                opp_val = getattr(value, "bpmn2_Message809", None)
                setattr(value, "bpmn2_Message809", self)

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
            if hasattr(old_value, "bpmn2_DocumentRoot222"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot222", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot222"):
                opp_val = getattr(value, "bpmn2_DocumentRoot222", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot222", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_ReceiveTask811(self):
        return self.__bpmn2_ReceiveTask811

    @bpmn2_ReceiveTask811.setter
    def bpmn2_ReceiveTask811(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ReceiveTask__bpmn2_ReceiveTask811", None)
        self.__bpmn2_ReceiveTask811 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Operation812"):
                opp_val = getattr(old_value, "bpmn2_Operation812", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Operation812", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Operation812"):
                opp_val = getattr(value, "bpmn2_Operation812", None)
                setattr(value, "bpmn2_Operation812", self)

class bpmn2_Property(ItemAwareElement):

    pass
class bpmn2_Process(FlowElementsContainer, CallableElement):

    def __init__(self, isClosed: bool, isExecutable: bool, processType: str, bpmn2_Process: "bpmn2_DocumentRoot" = None, bpmn2_Process770: "bpmn2_Participant" = None, bpmn2_Process784: "bpmn2_Auditing" = None, bpmn2_Process787: "bpmn2_Monitoring" = None, bpmn2_Process790: set["bpmn2_Property"] = None, bpmn2_Process793: set["bpmn2_Artifact"] = None, bpmn2_Process796: set["bpmn2_ResourceRole"] = None, bpmn2_Process799: set["bpmn2_CorrelationSubscription"] = None, bpmn2_Process803: "bpmn2_Process" = None, bpmn2_Process801: set["bpmn2_Process"] = None, bpmn2_Process805: "bpmn2_Collaboration" = None, bpmn2_Process879: "bpmn2_SubProcess" = None):
        self.isClosed = isClosed
        self.isExecutable = isExecutable
        self.processType = processType
        self.bpmn2_Process = bpmn2_Process
        self.bpmn2_Process770 = bpmn2_Process770
        self.bpmn2_Process784 = bpmn2_Process784
        self.bpmn2_Process787 = bpmn2_Process787
        self.bpmn2_Process790 = bpmn2_Process790 if bpmn2_Process790 is not None else set()
        self.bpmn2_Process793 = bpmn2_Process793 if bpmn2_Process793 is not None else set()
        self.bpmn2_Process796 = bpmn2_Process796 if bpmn2_Process796 is not None else set()
        self.bpmn2_Process799 = bpmn2_Process799 if bpmn2_Process799 is not None else set()
        self.bpmn2_Process803 = bpmn2_Process803
        self.bpmn2_Process801 = bpmn2_Process801 if bpmn2_Process801 is not None else set()
        self.bpmn2_Process805 = bpmn2_Process805
        self.bpmn2_Process879 = bpmn2_Process879
        
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
    def bpmn2_Process803(self):
        return self.__bpmn2_Process803

    @bpmn2_Process803.setter
    def bpmn2_Process803(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process803", None)
        self.__bpmn2_Process803 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Process801"):
                opp_val = getattr(old_value, "bpmn2_Process801", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Process801"):
                opp_val = getattr(value, "bpmn2_Process801", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Process801", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Process796(self):
        return self.__bpmn2_Process796

    @bpmn2_Process796.setter
    def bpmn2_Process796(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process796", None)
        self.__bpmn2_Process796 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_ResourceRole797"):
                    opp_val = getattr(item, "bpmn2_ResourceRole797", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_ResourceRole797", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_ResourceRole797"):
                    opp_val = getattr(item, "bpmn2_ResourceRole797", None)
                    
                    setattr(item, "bpmn2_ResourceRole797", self)
                    

    @property
    def bpmn2_Process793(self):
        return self.__bpmn2_Process793

    @bpmn2_Process793.setter
    def bpmn2_Process793(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process793", None)
        self.__bpmn2_Process793 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Artifact794"):
                    opp_val = getattr(item, "bpmn2_Artifact794", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Artifact794", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Artifact794"):
                    opp_val = getattr(item, "bpmn2_Artifact794", None)
                    
                    setattr(item, "bpmn2_Artifact794", self)
                    

    @property
    def bpmn2_Process805(self):
        return self.__bpmn2_Process805

    @bpmn2_Process805.setter
    def bpmn2_Process805(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process805", None)
        self.__bpmn2_Process805 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Collaboration806"):
                opp_val = getattr(old_value, "bpmn2_Collaboration806", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Collaboration806", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Collaboration806"):
                opp_val = getattr(value, "bpmn2_Collaboration806", None)
                setattr(value, "bpmn2_Collaboration806", self)

    @property
    def bpmn2_Process799(self):
        return self.__bpmn2_Process799

    @bpmn2_Process799.setter
    def bpmn2_Process799(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process799", None)
        self.__bpmn2_Process799 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_CorrelationSubscription800"):
                    opp_val = getattr(item, "bpmn2_CorrelationSubscription800", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_CorrelationSubscription800", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_CorrelationSubscription800"):
                    opp_val = getattr(item, "bpmn2_CorrelationSubscription800", None)
                    
                    setattr(item, "bpmn2_CorrelationSubscription800", self)
                    

    @property
    def bpmn2_Process790(self):
        return self.__bpmn2_Process790

    @bpmn2_Process790.setter
    def bpmn2_Process790(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process790", None)
        self.__bpmn2_Process790 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Property791"):
                    opp_val = getattr(item, "bpmn2_Property791", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Property791", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Property791"):
                    opp_val = getattr(item, "bpmn2_Property791", None)
                    
                    setattr(item, "bpmn2_Property791", self)
                    

    @property
    def bpmn2_Process879(self):
        return self.__bpmn2_Process879

    @bpmn2_Process879.setter
    def bpmn2_Process879(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process879", None)
        self.__bpmn2_Process879 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_SubProcess878"):
                opp_val = getattr(old_value, "bpmn2_SubProcess878", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_SubProcess878"):
                opp_val = getattr(value, "bpmn2_SubProcess878", None)
                if opp_val is None:
                    setattr(value, "bpmn2_SubProcess878", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Process787(self):
        return self.__bpmn2_Process787

    @bpmn2_Process787.setter
    def bpmn2_Process787(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process787", None)
        self.__bpmn2_Process787 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Monitoring788"):
                opp_val = getattr(old_value, "bpmn2_Monitoring788", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Monitoring788", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Monitoring788"):
                opp_val = getattr(value, "bpmn2_Monitoring788", None)
                setattr(value, "bpmn2_Monitoring788", self)

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
            if hasattr(old_value, "bpmn2_DocumentRoot218"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot218", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot218"):
                opp_val = getattr(value, "bpmn2_DocumentRoot218", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot218", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Process770(self):
        return self.__bpmn2_Process770

    @bpmn2_Process770.setter
    def bpmn2_Process770(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process770", None)
        self.__bpmn2_Process770 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Participant769"):
                opp_val = getattr(old_value, "bpmn2_Participant769", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Participant769", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Participant769"):
                opp_val = getattr(value, "bpmn2_Participant769", None)
                setattr(value, "bpmn2_Participant769", self)

    @property
    def bpmn2_Process784(self):
        return self.__bpmn2_Process784

    @bpmn2_Process784.setter
    def bpmn2_Process784(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process784", None)
        self.__bpmn2_Process784 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Auditing785"):
                opp_val = getattr(old_value, "bpmn2_Auditing785", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Auditing785", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Auditing785"):
                opp_val = getattr(value, "bpmn2_Auditing785", None)
                setattr(value, "bpmn2_Auditing785", self)

    @property
    def bpmn2_Process801(self):
        return self.__bpmn2_Process801

    @bpmn2_Process801.setter
    def bpmn2_Process801(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Process__bpmn2_Process801", None)
        self.__bpmn2_Process801 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Process803"):
                    opp_val = getattr(item, "bpmn2_Process803", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Process803", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Process803"):
                    opp_val = getattr(item, "bpmn2_Process803", None)
                    
                    setattr(item, "bpmn2_Process803", self)
                    

class bpmn2_MessageFlowAssociation(BaseElement):

    pass
class bpmn2_MessageFlow(BaseElement):

    pass
class bpmn2_MessageEventDefinition(EventDefinition):

    pass
class bpmn2_Message(RootElement):

    pass
class bpmn2_ManualTask(Task):

    pass
class bpmn2_LoopCharacteristics(BaseElement):

    pass
class bpmn2_LinkEventDefinition(EventDefinition):

    pass
class bpmn2_OutputSet(BaseElement):

    pass
class bpmn2_Operation(BaseElement):

    pass
class bpmn2_MultiInstanceLoopCharacteristics(LoopCharacteristics):

    def __init__(self, behavior: str, isSequential: bool, bpmn2_MultiInstanceLoopCharacteristics: "bpmn2_DocumentRoot" = None, bpmn2_MultiInstanceLoopCharacteristics713: "bpmn2_Expression" = None, bpmn2_MultiInstanceLoopCharacteristics716: "bpmn2_ItemAwareElement" = None, bpmn2_MultiInstanceLoopCharacteristics719: "bpmn2_ItemAwareElement" = None, bpmn2_MultiInstanceLoopCharacteristics722: "bpmn2_DataInput" = None, bpmn2_MultiInstanceLoopCharacteristics725: "bpmn2_DataOutput" = None, bpmn2_MultiInstanceLoopCharacteristics728: set["bpmn2_ComplexBehaviorDefinition"] = None, bpmn2_MultiInstanceLoopCharacteristics731: "bpmn2_Expression" = None, bpmn2_MultiInstanceLoopCharacteristics734: "bpmn2_EventDefinition" = None, bpmn2_MultiInstanceLoopCharacteristics737: "bpmn2_EventDefinition" = None):
        self.behavior = behavior
        self.isSequential = isSequential
        self.bpmn2_MultiInstanceLoopCharacteristics = bpmn2_MultiInstanceLoopCharacteristics
        self.bpmn2_MultiInstanceLoopCharacteristics713 = bpmn2_MultiInstanceLoopCharacteristics713
        self.bpmn2_MultiInstanceLoopCharacteristics716 = bpmn2_MultiInstanceLoopCharacteristics716
        self.bpmn2_MultiInstanceLoopCharacteristics719 = bpmn2_MultiInstanceLoopCharacteristics719
        self.bpmn2_MultiInstanceLoopCharacteristics722 = bpmn2_MultiInstanceLoopCharacteristics722
        self.bpmn2_MultiInstanceLoopCharacteristics725 = bpmn2_MultiInstanceLoopCharacteristics725
        self.bpmn2_MultiInstanceLoopCharacteristics728 = bpmn2_MultiInstanceLoopCharacteristics728 if bpmn2_MultiInstanceLoopCharacteristics728 is not None else set()
        self.bpmn2_MultiInstanceLoopCharacteristics731 = bpmn2_MultiInstanceLoopCharacteristics731
        self.bpmn2_MultiInstanceLoopCharacteristics734 = bpmn2_MultiInstanceLoopCharacteristics734
        self.bpmn2_MultiInstanceLoopCharacteristics737 = bpmn2_MultiInstanceLoopCharacteristics737
        
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
    def bpmn2_MultiInstanceLoopCharacteristics734(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics734

    @bpmn2_MultiInstanceLoopCharacteristics734.setter
    def bpmn2_MultiInstanceLoopCharacteristics734(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics734", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics734 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_EventDefinition735"):
                opp_val = getattr(old_value, "bpmn2_EventDefinition735", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_EventDefinition735", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_EventDefinition735"):
                opp_val = getattr(value, "bpmn2_EventDefinition735", None)
                setattr(value, "bpmn2_EventDefinition735", self)

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
            if hasattr(old_value, "bpmn2_DocumentRoot198"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot198", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot198"):
                opp_val = getattr(value, "bpmn2_DocumentRoot198", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot198", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_MultiInstanceLoopCharacteristics737(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics737

    @bpmn2_MultiInstanceLoopCharacteristics737.setter
    def bpmn2_MultiInstanceLoopCharacteristics737(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics737", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics737 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_EventDefinition738"):
                opp_val = getattr(old_value, "bpmn2_EventDefinition738", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_EventDefinition738", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_EventDefinition738"):
                opp_val = getattr(value, "bpmn2_EventDefinition738", None)
                setattr(value, "bpmn2_EventDefinition738", self)

    @property
    def bpmn2_MultiInstanceLoopCharacteristics716(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics716

    @bpmn2_MultiInstanceLoopCharacteristics716.setter
    def bpmn2_MultiInstanceLoopCharacteristics716(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics716", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics716 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemAwareElement717"):
                opp_val = getattr(old_value, "bpmn2_ItemAwareElement717", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemAwareElement717", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemAwareElement717"):
                opp_val = getattr(value, "bpmn2_ItemAwareElement717", None)
                setattr(value, "bpmn2_ItemAwareElement717", self)

    @property
    def bpmn2_MultiInstanceLoopCharacteristics722(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics722

    @bpmn2_MultiInstanceLoopCharacteristics722.setter
    def bpmn2_MultiInstanceLoopCharacteristics722(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics722", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics722 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DataInput723"):
                opp_val = getattr(old_value, "bpmn2_DataInput723", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_DataInput723", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DataInput723"):
                opp_val = getattr(value, "bpmn2_DataInput723", None)
                setattr(value, "bpmn2_DataInput723", self)

    @property
    def bpmn2_MultiInstanceLoopCharacteristics713(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics713

    @bpmn2_MultiInstanceLoopCharacteristics713.setter
    def bpmn2_MultiInstanceLoopCharacteristics713(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics713", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics713 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Expression714"):
                opp_val = getattr(old_value, "bpmn2_Expression714", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Expression714", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Expression714"):
                opp_val = getattr(value, "bpmn2_Expression714", None)
                setattr(value, "bpmn2_Expression714", self)

    @property
    def bpmn2_MultiInstanceLoopCharacteristics719(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics719

    @bpmn2_MultiInstanceLoopCharacteristics719.setter
    def bpmn2_MultiInstanceLoopCharacteristics719(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics719", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics719 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemAwareElement720"):
                opp_val = getattr(old_value, "bpmn2_ItemAwareElement720", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemAwareElement720", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemAwareElement720"):
                opp_val = getattr(value, "bpmn2_ItemAwareElement720", None)
                setattr(value, "bpmn2_ItemAwareElement720", self)

    @property
    def bpmn2_MultiInstanceLoopCharacteristics731(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics731

    @bpmn2_MultiInstanceLoopCharacteristics731.setter
    def bpmn2_MultiInstanceLoopCharacteristics731(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics731", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics731 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Expression732"):
                opp_val = getattr(old_value, "bpmn2_Expression732", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Expression732", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Expression732"):
                opp_val = getattr(value, "bpmn2_Expression732", None)
                setattr(value, "bpmn2_Expression732", self)

    @property
    def bpmn2_MultiInstanceLoopCharacteristics728(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics728

    @bpmn2_MultiInstanceLoopCharacteristics728.setter
    def bpmn2_MultiInstanceLoopCharacteristics728(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics728", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics728 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_ComplexBehaviorDefinition729"):
                    opp_val = getattr(item, "bpmn2_ComplexBehaviorDefinition729", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_ComplexBehaviorDefinition729", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_ComplexBehaviorDefinition729"):
                    opp_val = getattr(item, "bpmn2_ComplexBehaviorDefinition729", None)
                    
                    setattr(item, "bpmn2_ComplexBehaviorDefinition729", self)
                    

    @property
    def bpmn2_MultiInstanceLoopCharacteristics725(self):
        return self.__bpmn2_MultiInstanceLoopCharacteristics725

    @bpmn2_MultiInstanceLoopCharacteristics725.setter
    def bpmn2_MultiInstanceLoopCharacteristics725(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_MultiInstanceLoopCharacteristics__bpmn2_MultiInstanceLoopCharacteristics725", None)
        self.__bpmn2_MultiInstanceLoopCharacteristics725 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DataOutput726"):
                opp_val = getattr(old_value, "bpmn2_DataOutput726", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_DataOutput726", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DataOutput726"):
                opp_val = getattr(value, "bpmn2_DataOutput726", None)
                setattr(value, "bpmn2_DataOutput726", self)

class bpmn2_InputOutputBinding(BaseElement):

    pass
class bpmn2_Monitoring(BaseElement):

    pass
class bpmn2_IntermediateThrowEvent(ThrowEvent):

    pass
class bpmn2_IntermediateCatchEvent(CatchEvent):

    pass
class bpmn2_Interface(RootElement):

    pass
class bpmn2_LaneSet(BaseElement, InteractionNode):

    pass
class bpmn2_Lane(BaseElement, InteractionNode):

    pass
class bpmn2_ItemDefinition(RootElement):

    def __init__(self, isCollection: bool, itemKind: str, bpmn2_ItemDefinition: "bpmn2_DocumentRoot" = None, bpmn2_ItemDefinition474: "bpmn2_CorrelationProperty" = None, bpmn2_ItemDefinition546: "bpmn2_Escalation" = None, bpmn2_ItemDefinition540: "bpmn2_Error" = None, bpmn2_ItemDefinition586: "bpmn2_FormalExpression" = None, bpmn2_ItemDefinition648: "bpmn2_ItemAwareElement" = None, bpmn2_ItemDefinition650: "bpmn2_Import" = None, bpmn2_ItemDefinition653: "bpmn2_EObject" = None, bpmn2_ItemDefinition690: "bpmn2_Message" = None, bpmn2_ItemDefinition827: "bpmn2_ResourceParameter" = None, bpmn2_ItemDefinition861: "bpmn2_Signal" = None):
        self.isCollection = isCollection
        self.itemKind = itemKind
        self.bpmn2_ItemDefinition = bpmn2_ItemDefinition
        self.bpmn2_ItemDefinition474 = bpmn2_ItemDefinition474
        self.bpmn2_ItemDefinition546 = bpmn2_ItemDefinition546
        self.bpmn2_ItemDefinition540 = bpmn2_ItemDefinition540
        self.bpmn2_ItemDefinition586 = bpmn2_ItemDefinition586
        self.bpmn2_ItemDefinition648 = bpmn2_ItemDefinition648
        self.bpmn2_ItemDefinition650 = bpmn2_ItemDefinition650
        self.bpmn2_ItemDefinition653 = bpmn2_ItemDefinition653
        self.bpmn2_ItemDefinition690 = bpmn2_ItemDefinition690
        self.bpmn2_ItemDefinition827 = bpmn2_ItemDefinition827
        self.bpmn2_ItemDefinition861 = bpmn2_ItemDefinition861
        
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
    def bpmn2_ItemDefinition650(self):
        return self.__bpmn2_ItemDefinition650

    @bpmn2_ItemDefinition650.setter
    def bpmn2_ItemDefinition650(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition650", None)
        self.__bpmn2_ItemDefinition650 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Import651"):
                opp_val = getattr(old_value, "bpmn2_Import651", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Import651", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Import651"):
                opp_val = getattr(value, "bpmn2_Import651", None)
                setattr(value, "bpmn2_Import651", self)

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
            if hasattr(old_value, "bpmn2_DocumentRoot176"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot176", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot176"):
                opp_val = getattr(value, "bpmn2_DocumentRoot176", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot176", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_ItemDefinition586(self):
        return self.__bpmn2_ItemDefinition586

    @bpmn2_ItemDefinition586.setter
    def bpmn2_ItemDefinition586(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition586", None)
        self.__bpmn2_ItemDefinition586 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_FormalExpression585"):
                opp_val = getattr(old_value, "bpmn2_FormalExpression585", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_FormalExpression585", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_FormalExpression585"):
                opp_val = getattr(value, "bpmn2_FormalExpression585", None)
                setattr(value, "bpmn2_FormalExpression585", self)

    @property
    def bpmn2_ItemDefinition861(self):
        return self.__bpmn2_ItemDefinition861

    @bpmn2_ItemDefinition861.setter
    def bpmn2_ItemDefinition861(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition861", None)
        self.__bpmn2_ItemDefinition861 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Signal860"):
                opp_val = getattr(old_value, "bpmn2_Signal860", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Signal860", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Signal860"):
                opp_val = getattr(value, "bpmn2_Signal860", None)
                setattr(value, "bpmn2_Signal860", self)

    @property
    def bpmn2_ItemDefinition474(self):
        return self.__bpmn2_ItemDefinition474

    @bpmn2_ItemDefinition474.setter
    def bpmn2_ItemDefinition474(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition474", None)
        self.__bpmn2_ItemDefinition474 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CorrelationProperty473"):
                opp_val = getattr(old_value, "bpmn2_CorrelationProperty473", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_CorrelationProperty473", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CorrelationProperty473"):
                opp_val = getattr(value, "bpmn2_CorrelationProperty473", None)
                setattr(value, "bpmn2_CorrelationProperty473", self)

    @property
    def bpmn2_ItemDefinition648(self):
        return self.__bpmn2_ItemDefinition648

    @bpmn2_ItemDefinition648.setter
    def bpmn2_ItemDefinition648(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition648", None)
        self.__bpmn2_ItemDefinition648 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemAwareElement647"):
                opp_val = getattr(old_value, "bpmn2_ItemAwareElement647", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemAwareElement647", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemAwareElement647"):
                opp_val = getattr(value, "bpmn2_ItemAwareElement647", None)
                setattr(value, "bpmn2_ItemAwareElement647", self)

    @property
    def bpmn2_ItemDefinition653(self):
        return self.__bpmn2_ItemDefinition653

    @bpmn2_ItemDefinition653.setter
    def bpmn2_ItemDefinition653(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition653", None)
        self.__bpmn2_ItemDefinition653 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_EObject654"):
                opp_val = getattr(old_value, "bpmn2_EObject654", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_EObject654", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_EObject654"):
                opp_val = getattr(value, "bpmn2_EObject654", None)
                setattr(value, "bpmn2_EObject654", self)

    @property
    def bpmn2_ItemDefinition546(self):
        return self.__bpmn2_ItemDefinition546

    @bpmn2_ItemDefinition546.setter
    def bpmn2_ItemDefinition546(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition546", None)
        self.__bpmn2_ItemDefinition546 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Escalation545"):
                opp_val = getattr(old_value, "bpmn2_Escalation545", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Escalation545", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Escalation545"):
                opp_val = getattr(value, "bpmn2_Escalation545", None)
                setattr(value, "bpmn2_Escalation545", self)

    @property
    def bpmn2_ItemDefinition827(self):
        return self.__bpmn2_ItemDefinition827

    @bpmn2_ItemDefinition827.setter
    def bpmn2_ItemDefinition827(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition827", None)
        self.__bpmn2_ItemDefinition827 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ResourceParameter826"):
                opp_val = getattr(old_value, "bpmn2_ResourceParameter826", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ResourceParameter826", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ResourceParameter826"):
                opp_val = getattr(value, "bpmn2_ResourceParameter826", None)
                setattr(value, "bpmn2_ResourceParameter826", self)

    @property
    def bpmn2_ItemDefinition540(self):
        return self.__bpmn2_ItemDefinition540

    @bpmn2_ItemDefinition540.setter
    def bpmn2_ItemDefinition540(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition540", None)
        self.__bpmn2_ItemDefinition540 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Error539"):
                opp_val = getattr(old_value, "bpmn2_Error539", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Error539", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Error539"):
                opp_val = getattr(value, "bpmn2_Error539", None)
                setattr(value, "bpmn2_Error539", self)

    @property
    def bpmn2_ItemDefinition690(self):
        return self.__bpmn2_ItemDefinition690

    @bpmn2_ItemDefinition690.setter
    def bpmn2_ItemDefinition690(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ItemDefinition__bpmn2_ItemDefinition690", None)
        self.__bpmn2_ItemDefinition690 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Message689"):
                opp_val = getattr(old_value, "bpmn2_Message689", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Message689", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Message689"):
                opp_val = getattr(value, "bpmn2_Message689", None)
                setattr(value, "bpmn2_Message689", self)

class bpmn2_InputOutputSpecification(BaseElement):

    pass
class bpmn2_Performer(ResourceRole):

    pass
class bpmn2_HumanPerformer(Performer):

    pass
class bpmn2_Group(Artifact):

    pass
class bpmn2_GlobalUserTask(GlobalTask):

    def __init__(self, implementation: str, bpmn2_GlobalUserTask: "bpmn2_DocumentRoot" = None, bpmn2_GlobalUserTask594: set["bpmn2_Rendering"] = None):
        self.implementation = implementation
        self.bpmn2_GlobalUserTask = bpmn2_GlobalUserTask
        self.bpmn2_GlobalUserTask594 = bpmn2_GlobalUserTask594 if bpmn2_GlobalUserTask594 is not None else set()
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def bpmn2_GlobalUserTask594(self):
        return self.__bpmn2_GlobalUserTask594

    @bpmn2_GlobalUserTask594.setter
    def bpmn2_GlobalUserTask594(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_GlobalUserTask__bpmn2_GlobalUserTask594", None)
        self.__bpmn2_GlobalUserTask594 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Rendering595"):
                    opp_val = getattr(item, "bpmn2_Rendering595", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Rendering595", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Rendering595"):
                    opp_val = getattr(item, "bpmn2_Rendering595", None)
                    
                    setattr(item, "bpmn2_Rendering595", self)
                    

    @property
    def bpmn2_GlobalUserTask(self):
        return self.__bpmn2_GlobalUserTask

    @bpmn2_GlobalUserTask.setter
    def bpmn2_GlobalUserTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_GlobalUserTask__bpmn2_GlobalUserTask", None)
        self.__bpmn2_GlobalUserTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DocumentRoot148"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot148", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot148"):
                opp_val = getattr(value, "bpmn2_DocumentRoot148", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot148", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_GlobalTask(CallableElement):

    pass
class bpmn2_GlobalScriptTask(GlobalTask):

    def __init__(self, script: str, scriptLanguage: str, bpmn2_GlobalScriptTask: "bpmn2_DocumentRoot" = None):
        self.script = script
        self.scriptLanguage = scriptLanguage
        self.bpmn2_GlobalScriptTask = bpmn2_GlobalScriptTask
        
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

    @property
    def bpmn2_GlobalScriptTask(self):
        return self.__bpmn2_GlobalScriptTask

    @bpmn2_GlobalScriptTask.setter
    def bpmn2_GlobalScriptTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_GlobalScriptTask__bpmn2_GlobalScriptTask", None)
        self.__bpmn2_GlobalScriptTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DocumentRoot144"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot144", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot144"):
                opp_val = getattr(value, "bpmn2_DocumentRoot144", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot144", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_GlobalManualTask(GlobalTask):

    pass
class bpmn2_InputSet(BaseElement):

    pass
class bpmn2_InclusiveGateway(Gateway):

    pass
class bpmn2_Import:

    def __init__(self, importType: str, location: str, namespace: str, bpmn2_Import: "bpmn2_DocumentRoot" = None, bpmn2_Import526: "bpmn2_Definitions" = None, bpmn2_Import651: "bpmn2_ItemDefinition" = None):
        self.importType = importType
        self.location = location
        self.namespace = namespace
        self.bpmn2_Import = bpmn2_Import
        self.bpmn2_Import526 = bpmn2_Import526
        self.bpmn2_Import651 = bpmn2_Import651
        
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
    def bpmn2_Import526(self):
        return self.__bpmn2_Import526

    @bpmn2_Import526.setter
    def bpmn2_Import526(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Import__bpmn2_Import526", None)
        self.__bpmn2_Import526 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Definitions525"):
                opp_val = getattr(old_value, "bpmn2_Definitions525", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Definitions525"):
                opp_val = getattr(value, "bpmn2_Definitions525", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Definitions525", set([self]))
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
            if hasattr(old_value, "bpmn2_DocumentRoot160"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot160", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot160"):
                opp_val = getattr(value, "bpmn2_DocumentRoot160", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot160", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Import651(self):
        return self.__bpmn2_Import651

    @bpmn2_Import651.setter
    def bpmn2_Import651(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Import__bpmn2_Import651", None)
        self.__bpmn2_Import651 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemDefinition650"):
                opp_val = getattr(old_value, "bpmn2_ItemDefinition650", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemDefinition650", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemDefinition650"):
                opp_val = getattr(value, "bpmn2_ItemDefinition650", None)
                setattr(value, "bpmn2_ItemDefinition650", self)

class bpmn2_ImplicitThrowEvent(ThrowEvent):

    pass
class bpmn2_ResourceRole(BaseElement):

    pass
class bpmn2_FlowNode(FlowElement):

    pass
class bpmn2_ExtensionAttributeValue:

    def __init__(self, value: str, bpmn2_ExtensionAttributeValue: "bpmn2_DocumentRoot" = None, bpmn2_ExtensionAttributeValue334: "bpmn2_BaseElement" = None, bpmn2_ExtensionAttributeValue561: "bpmn2_EObject" = None, bpmn2_ExtensionAttributeValue564: "bpmn2_ExtensionAttributeDefinition" = None):
        self.value = value
        self.bpmn2_ExtensionAttributeValue = bpmn2_ExtensionAttributeValue
        self.bpmn2_ExtensionAttributeValue334 = bpmn2_ExtensionAttributeValue334
        self.bpmn2_ExtensionAttributeValue561 = bpmn2_ExtensionAttributeValue561
        self.bpmn2_ExtensionAttributeValue564 = bpmn2_ExtensionAttributeValue564
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def bpmn2_ExtensionAttributeValue564(self):
        return self.__bpmn2_ExtensionAttributeValue564

    @bpmn2_ExtensionAttributeValue564.setter
    def bpmn2_ExtensionAttributeValue564(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ExtensionAttributeValue__bpmn2_ExtensionAttributeValue564", None)
        self.__bpmn2_ExtensionAttributeValue564 = value
        
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
            if hasattr(old_value, "bpmn2_DocumentRoot128"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot128", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot128"):
                opp_val = getattr(value, "bpmn2_DocumentRoot128", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot128", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_ExtensionAttributeValue334(self):
        return self.__bpmn2_ExtensionAttributeValue334

    @bpmn2_ExtensionAttributeValue334.setter
    def bpmn2_ExtensionAttributeValue334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ExtensionAttributeValue__bpmn2_ExtensionAttributeValue334", None)
        self.__bpmn2_ExtensionAttributeValue334 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_BaseElement333"):
                opp_val = getattr(old_value, "bpmn2_BaseElement333", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_BaseElement333"):
                opp_val = getattr(value, "bpmn2_BaseElement333", None)
                if opp_val is None:
                    setattr(value, "bpmn2_BaseElement333", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_ExtensionAttributeValue561(self):
        return self.__bpmn2_ExtensionAttributeValue561

    @bpmn2_ExtensionAttributeValue561.setter
    def bpmn2_ExtensionAttributeValue561(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ExtensionAttributeValue__bpmn2_ExtensionAttributeValue561", None)
        self.__bpmn2_ExtensionAttributeValue561 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_EObject562"):
                opp_val = getattr(old_value, "bpmn2_EObject562", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_EObject562", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_EObject562"):
                opp_val = getattr(value, "bpmn2_EObject562", None)
                setattr(value, "bpmn2_EObject562", self)

class bpmn2_Extension:

    def __init__(self, mustUnderstand: bool, xsdDefinition: str, bpmn2_Extension: "bpmn2_DocumentRoot" = None, bpmn2_Extension529: "bpmn2_Definitions" = None, bpmn2_Extension557: "bpmn2_ExtensionDefinition" = None):
        self.mustUnderstand = mustUnderstand
        self.xsdDefinition = xsdDefinition
        self.bpmn2_Extension = bpmn2_Extension
        self.bpmn2_Extension529 = bpmn2_Extension529
        self.bpmn2_Extension557 = bpmn2_Extension557
        
    @property
    def mustUnderstand(self) -> bool:
        return self.__mustUnderstand

    @mustUnderstand.setter
    def mustUnderstand(self, mustUnderstand: bool):
        self.__mustUnderstand = mustUnderstand

    @property
    def xsdDefinition(self) -> str:
        return self.__xsdDefinition

    @xsdDefinition.setter
    def xsdDefinition(self, xsdDefinition: str):
        self.__xsdDefinition = xsdDefinition

    @property
    def bpmn2_Extension529(self):
        return self.__bpmn2_Extension529

    @bpmn2_Extension529.setter
    def bpmn2_Extension529(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Extension__bpmn2_Extension529", None)
        self.__bpmn2_Extension529 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Definitions528"):
                opp_val = getattr(old_value, "bpmn2_Definitions528", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Definitions528"):
                opp_val = getattr(value, "bpmn2_Definitions528", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Definitions528", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Extension557(self):
        return self.__bpmn2_Extension557

    @bpmn2_Extension557.setter
    def bpmn2_Extension557(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Extension__bpmn2_Extension557", None)
        self.__bpmn2_Extension557 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ExtensionDefinition558"):
                opp_val = getattr(old_value, "bpmn2_ExtensionDefinition558", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ExtensionDefinition558", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ExtensionDefinition558"):
                opp_val = getattr(value, "bpmn2_ExtensionDefinition558", None)
                setattr(value, "bpmn2_ExtensionDefinition558", self)

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
            if hasattr(old_value, "bpmn2_DocumentRoot126"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot126", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot126"):
                opp_val = getattr(value, "bpmn2_DocumentRoot126", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot126", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_Expression(BaseElement):

    pass
class bpmn2_ExclusiveGateway(Gateway):

    pass
class bpmn2_EventBasedGateway(Gateway):

    def __init__(self, eventGatewayType: str, instantiate: bool, bpmn2_EventBasedGateway: "bpmn2_DocumentRoot" = None):
        self.eventGatewayType = eventGatewayType
        self.instantiate = instantiate
        self.bpmn2_EventBasedGateway = bpmn2_EventBasedGateway
        
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

    @property
    def bpmn2_EventBasedGateway(self):
        return self.__bpmn2_EventBasedGateway

    @bpmn2_EventBasedGateway.setter
    def bpmn2_EventBasedGateway(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_EventBasedGateway__bpmn2_EventBasedGateway", None)
        self.__bpmn2_EventBasedGateway = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DocumentRoot120"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot120", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot120"):
                opp_val = getattr(value, "bpmn2_DocumentRoot120", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot120", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_GlobalConversation(Collaboration):

    pass
class bpmn2_GlobalChoreographyTask(Choreography):

    pass
class bpmn2_GlobalBusinessRuleTask(GlobalTask):

    def __init__(self, implementation: str, bpmn2_GlobalBusinessRuleTask: "bpmn2_DocumentRoot" = None):
        self.implementation = implementation
        self.bpmn2_GlobalBusinessRuleTask = bpmn2_GlobalBusinessRuleTask
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def bpmn2_GlobalBusinessRuleTask(self):
        return self.__bpmn2_GlobalBusinessRuleTask

    @bpmn2_GlobalBusinessRuleTask.setter
    def bpmn2_GlobalBusinessRuleTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_GlobalBusinessRuleTask__bpmn2_GlobalBusinessRuleTask", None)
        self.__bpmn2_GlobalBusinessRuleTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DocumentRoot136"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot136", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot136"):
                opp_val = getattr(value, "bpmn2_DocumentRoot136", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot136", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_Gateway(FlowNode):

    def __init__(self, gatewayDirection: str, bpmn2_Gateway: "bpmn2_DocumentRoot" = None):
        self.gatewayDirection = gatewayDirection
        self.bpmn2_Gateway = bpmn2_Gateway
        
    @property
    def gatewayDirection(self) -> str:
        return self.__gatewayDirection

    @gatewayDirection.setter
    def gatewayDirection(self, gatewayDirection: str):
        self.__gatewayDirection = gatewayDirection

    @property
    def bpmn2_Gateway(self):
        return self.__bpmn2_Gateway

    @bpmn2_Gateway.setter
    def bpmn2_Gateway(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Gateway__bpmn2_Gateway", None)
        self.__bpmn2_Gateway = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DocumentRoot134"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot134", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot134"):
                opp_val = getattr(value, "bpmn2_DocumentRoot134", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot134", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_FormalExpression(Expression):

    def __init__(self, mixed: str, body: str, language: str, bpmn2_FormalExpression: "bpmn2_DocumentRoot" = None, bpmn2_FormalExpression433: "bpmn2_ComplexBehaviorDefinition" = None, bpmn2_FormalExpression500: "bpmn2_DataAssociation" = None, bpmn2_FormalExpression477: "bpmn2_CorrelationPropertyBinding" = None, bpmn2_FormalExpression483: "bpmn2_CorrelationPropertyRetrievalExpression" = None, bpmn2_FormalExpression585: "bpmn2_ItemDefinition" = None):
        self.mixed = mixed
        self.body = body
        self.language = language
        self.bpmn2_FormalExpression = bpmn2_FormalExpression
        self.bpmn2_FormalExpression433 = bpmn2_FormalExpression433
        self.bpmn2_FormalExpression500 = bpmn2_FormalExpression500
        self.bpmn2_FormalExpression477 = bpmn2_FormalExpression477
        self.bpmn2_FormalExpression483 = bpmn2_FormalExpression483
        self.bpmn2_FormalExpression585 = bpmn2_FormalExpression585
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

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
            if hasattr(old_value, "bpmn2_DocumentRoot132"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot132", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot132"):
                opp_val = getattr(value, "bpmn2_DocumentRoot132", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot132", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_FormalExpression477(self):
        return self.__bpmn2_FormalExpression477

    @bpmn2_FormalExpression477.setter
    def bpmn2_FormalExpression477(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FormalExpression__bpmn2_FormalExpression477", None)
        self.__bpmn2_FormalExpression477 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CorrelationPropertyBinding476"):
                opp_val = getattr(old_value, "bpmn2_CorrelationPropertyBinding476", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_CorrelationPropertyBinding476", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CorrelationPropertyBinding476"):
                opp_val = getattr(value, "bpmn2_CorrelationPropertyBinding476", None)
                setattr(value, "bpmn2_CorrelationPropertyBinding476", self)

    @property
    def bpmn2_FormalExpression500(self):
        return self.__bpmn2_FormalExpression500

    @bpmn2_FormalExpression500.setter
    def bpmn2_FormalExpression500(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FormalExpression__bpmn2_FormalExpression500", None)
        self.__bpmn2_FormalExpression500 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DataAssociation499"):
                opp_val = getattr(old_value, "bpmn2_DataAssociation499", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_DataAssociation499", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DataAssociation499"):
                opp_val = getattr(value, "bpmn2_DataAssociation499", None)
                setattr(value, "bpmn2_DataAssociation499", self)

    @property
    def bpmn2_FormalExpression585(self):
        return self.__bpmn2_FormalExpression585

    @bpmn2_FormalExpression585.setter
    def bpmn2_FormalExpression585(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FormalExpression__bpmn2_FormalExpression585", None)
        self.__bpmn2_FormalExpression585 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemDefinition586"):
                opp_val = getattr(old_value, "bpmn2_ItemDefinition586", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemDefinition586", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemDefinition586"):
                opp_val = getattr(value, "bpmn2_ItemDefinition586", None)
                setattr(value, "bpmn2_ItemDefinition586", self)

    @property
    def bpmn2_FormalExpression433(self):
        return self.__bpmn2_FormalExpression433

    @bpmn2_FormalExpression433.setter
    def bpmn2_FormalExpression433(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FormalExpression__bpmn2_FormalExpression433", None)
        self.__bpmn2_FormalExpression433 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ComplexBehaviorDefinition432"):
                opp_val = getattr(old_value, "bpmn2_ComplexBehaviorDefinition432", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ComplexBehaviorDefinition432", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ComplexBehaviorDefinition432"):
                opp_val = getattr(value, "bpmn2_ComplexBehaviorDefinition432", None)
                setattr(value, "bpmn2_ComplexBehaviorDefinition432", self)

    @property
    def bpmn2_FormalExpression483(self):
        return self.__bpmn2_FormalExpression483

    @bpmn2_FormalExpression483.setter
    def bpmn2_FormalExpression483(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_FormalExpression__bpmn2_FormalExpression483", None)
        self.__bpmn2_FormalExpression483 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CorrelationPropertyRetrievalExpression482"):
                opp_val = getattr(old_value, "bpmn2_CorrelationPropertyRetrievalExpression482", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_CorrelationPropertyRetrievalExpression482", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CorrelationPropertyRetrievalExpression482"):
                opp_val = getattr(value, "bpmn2_CorrelationPropertyRetrievalExpression482", None)
                setattr(value, "bpmn2_CorrelationPropertyRetrievalExpression482", self)

class bpmn2_EndPoint(RootElement):

    pass
class bpmn2_EndEvent(ThrowEvent):

    pass
class bpmn2_Documentation(BaseElement):

    def __init__(self, mixed: str, text: str, textFormat: str, bpmn2_Documentation: "bpmn2_DocumentRoot" = None, bpmn2_Documentation337: "bpmn2_BaseElement" = None):
        self.mixed = mixed
        self.text = text
        self.textFormat = textFormat
        self.bpmn2_Documentation = bpmn2_Documentation
        self.bpmn2_Documentation337 = bpmn2_Documentation337
        
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
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

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
            if hasattr(old_value, "bpmn2_DocumentRoot104"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot104"):
                opp_val = getattr(value, "bpmn2_DocumentRoot104", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Documentation337(self):
        return self.__bpmn2_Documentation337

    @bpmn2_Documentation337.setter
    def bpmn2_Documentation337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Documentation__bpmn2_Documentation337", None)
        self.__bpmn2_Documentation337 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_BaseElement336"):
                opp_val = getattr(old_value, "bpmn2_BaseElement336", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_BaseElement336"):
                opp_val = getattr(value, "bpmn2_BaseElement336", None)
                if opp_val is None:
                    setattr(value, "bpmn2_BaseElement336", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_Definitions(BaseElement):

    def __init__(self, exporter: str, exporterVersion: str, expressionLanguage: str, targetNamespace: str, typeLanguage: str, bpmn2_Definitions: "bpmn2_DocumentRoot" = None, bpmn2_Definitions525: set["bpmn2_Import"] = None, bpmn2_Definitions528: set["bpmn2_Extension"] = None, bpmn2_Definitions531: set["bpmn2_RootElement"] = None, bpmn2_Definitions534: set["bpmn2_BPMNDiagram"] = None, bpmn2_Definitions536: set["bpmn2_Relationship"] = None):
        self.exporter = exporter
        self.exporterVersion = exporterVersion
        self.expressionLanguage = expressionLanguage
        self.targetNamespace = targetNamespace
        self.typeLanguage = typeLanguage
        self.bpmn2_Definitions = bpmn2_Definitions
        self.bpmn2_Definitions525 = bpmn2_Definitions525 if bpmn2_Definitions525 is not None else set()
        self.bpmn2_Definitions528 = bpmn2_Definitions528 if bpmn2_Definitions528 is not None else set()
        self.bpmn2_Definitions531 = bpmn2_Definitions531 if bpmn2_Definitions531 is not None else set()
        self.bpmn2_Definitions534 = bpmn2_Definitions534 if bpmn2_Definitions534 is not None else set()
        self.bpmn2_Definitions536 = bpmn2_Definitions536 if bpmn2_Definitions536 is not None else set()
        
    @property
    def targetNamespace(self) -> str:
        return self.__targetNamespace

    @targetNamespace.setter
    def targetNamespace(self, targetNamespace: str):
        self.__targetNamespace = targetNamespace

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
    def expressionLanguage(self) -> str:
        return self.__expressionLanguage

    @expressionLanguage.setter
    def expressionLanguage(self, expressionLanguage: str):
        self.__expressionLanguage = expressionLanguage

    @property
    def exporter(self) -> str:
        return self.__exporter

    @exporter.setter
    def exporter(self, exporter: str):
        self.__exporter = exporter

    @property
    def bpmn2_Definitions525(self):
        return self.__bpmn2_Definitions525

    @bpmn2_Definitions525.setter
    def bpmn2_Definitions525(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Definitions__bpmn2_Definitions525", None)
        self.__bpmn2_Definitions525 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Import526"):
                    opp_val = getattr(item, "bpmn2_Import526", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Import526", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Import526"):
                    opp_val = getattr(item, "bpmn2_Import526", None)
                    
                    setattr(item, "bpmn2_Import526", self)
                    

    @property
    def bpmn2_Definitions536(self):
        return self.__bpmn2_Definitions536

    @bpmn2_Definitions536.setter
    def bpmn2_Definitions536(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Definitions__bpmn2_Definitions536", None)
        self.__bpmn2_Definitions536 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Relationship537"):
                    opp_val = getattr(item, "bpmn2_Relationship537", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Relationship537", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Relationship537"):
                    opp_val = getattr(item, "bpmn2_Relationship537", None)
                    
                    setattr(item, "bpmn2_Relationship537", self)
                    

    @property
    def bpmn2_Definitions531(self):
        return self.__bpmn2_Definitions531

    @bpmn2_Definitions531.setter
    def bpmn2_Definitions531(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Definitions__bpmn2_Definitions531", None)
        self.__bpmn2_Definitions531 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_RootElement532"):
                    opp_val = getattr(item, "bpmn2_RootElement532", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_RootElement532", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_RootElement532"):
                    opp_val = getattr(item, "bpmn2_RootElement532", None)
                    
                    setattr(item, "bpmn2_RootElement532", self)
                    

    @property
    def bpmn2_Definitions534(self):
        return self.__bpmn2_Definitions534

    @bpmn2_Definitions534.setter
    def bpmn2_Definitions534(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Definitions__bpmn2_Definitions534", None)
        self.__bpmn2_Definitions534 = value if value is not None else set()
        
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
    def bpmn2_Definitions528(self):
        return self.__bpmn2_Definitions528

    @bpmn2_Definitions528.setter
    def bpmn2_Definitions528(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Definitions__bpmn2_Definitions528", None)
        self.__bpmn2_Definitions528 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Extension529"):
                    opp_val = getattr(item, "bpmn2_Extension529", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Extension529", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Extension529"):
                    opp_val = getattr(item, "bpmn2_Extension529", None)
                    
                    setattr(item, "bpmn2_Extension529", self)
                    

    @property
    def bpmn2_Definitions(self):
        return self.__bpmn2_Definitions

    @bpmn2_Definitions.setter
    def bpmn2_Definitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Definitions__bpmn2_Definitions", None)
        self.__bpmn2_Definitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DocumentRoot102"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot102"):
                opp_val = getattr(value, "bpmn2_DocumentRoot102", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_DataStoreReference(FlowElement, ItemAwareElement):

    pass
class bpmn2_DataStore(RootElement, ItemAwareElement):

    def __init__(self, capacity: int, isUnlimited: bool, bpmn2_DataStore: "bpmn2_DocumentRoot" = None, bpmn2_DataStore523: "bpmn2_DataStoreReference" = None):
        self.capacity = capacity
        self.isUnlimited = isUnlimited
        self.bpmn2_DataStore = bpmn2_DataStore
        self.bpmn2_DataStore523 = bpmn2_DataStore523
        
    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    @property
    def isUnlimited(self) -> bool:
        return self.__isUnlimited

    @isUnlimited.setter
    def isUnlimited(self, isUnlimited: bool):
        self.__isUnlimited = isUnlimited

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
            if hasattr(old_value, "bpmn2_DocumentRoot98"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot98", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot98"):
                opp_val = getattr(value, "bpmn2_DocumentRoot98", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot98", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_DataStore523(self):
        return self.__bpmn2_DataStore523

    @bpmn2_DataStore523.setter
    def bpmn2_DataStore523(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataStore__bpmn2_DataStore523", None)
        self.__bpmn2_DataStore523 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DataStoreReference522"):
                opp_val = getattr(old_value, "bpmn2_DataStoreReference522", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_DataStoreReference522", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DataStoreReference522"):
                opp_val = getattr(value, "bpmn2_DataStoreReference522", None)
                setattr(value, "bpmn2_DataStoreReference522", self)

class bpmn2_DataState(BaseElement):

    pass
class bpmn2_DataOutputAssociation(DataAssociation):

    pass
class bpmn2_Event(FlowNode, InteractionNode):

    pass
class bpmn2_EscalationEventDefinition(EventDefinition):

    pass
class bpmn2_Escalation(RootElement):

    def __init__(self, escalationCode: str, bpmn2_Escalation: "bpmn2_DocumentRoot" = None, bpmn2_Escalation545: "bpmn2_ItemDefinition" = None, bpmn2_Escalation549: "bpmn2_EscalationEventDefinition" = None):
        self.escalationCode = escalationCode
        self.bpmn2_Escalation = bpmn2_Escalation
        self.bpmn2_Escalation545 = bpmn2_Escalation545
        self.bpmn2_Escalation549 = bpmn2_Escalation549
        
    @property
    def escalationCode(self) -> str:
        return self.__escalationCode

    @escalationCode.setter
    def escalationCode(self, escalationCode: str):
        self.__escalationCode = escalationCode

    @property
    def bpmn2_Escalation545(self):
        return self.__bpmn2_Escalation545

    @bpmn2_Escalation545.setter
    def bpmn2_Escalation545(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Escalation__bpmn2_Escalation545", None)
        self.__bpmn2_Escalation545 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemDefinition546"):
                opp_val = getattr(old_value, "bpmn2_ItemDefinition546", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemDefinition546", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemDefinition546"):
                opp_val = getattr(value, "bpmn2_ItemDefinition546", None)
                setattr(value, "bpmn2_ItemDefinition546", self)

    @property
    def bpmn2_Escalation549(self):
        return self.__bpmn2_Escalation549

    @bpmn2_Escalation549.setter
    def bpmn2_Escalation549(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Escalation__bpmn2_Escalation549", None)
        self.__bpmn2_Escalation549 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_EscalationEventDefinition548"):
                opp_val = getattr(old_value, "bpmn2_EscalationEventDefinition548", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_EscalationEventDefinition548", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_EscalationEventDefinition548"):
                opp_val = getattr(value, "bpmn2_EscalationEventDefinition548", None)
                setattr(value, "bpmn2_EscalationEventDefinition548", self)

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
            if hasattr(old_value, "bpmn2_DocumentRoot114"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot114"):
                opp_val = getattr(value, "bpmn2_DocumentRoot114", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_ErrorEventDefinition(EventDefinition):

    pass
class bpmn2_Error(RootElement):

    def __init__(self, errorCode: str, bpmn2_Error: "bpmn2_DocumentRoot" = None, bpmn2_Error539: "bpmn2_ItemDefinition" = None, bpmn2_Error543: "bpmn2_ErrorEventDefinition" = None, bpmn2_Error747: "bpmn2_Operation" = None):
        self.errorCode = errorCode
        self.bpmn2_Error = bpmn2_Error
        self.bpmn2_Error539 = bpmn2_Error539
        self.bpmn2_Error543 = bpmn2_Error543
        self.bpmn2_Error747 = bpmn2_Error747
        
    @property
    def errorCode(self) -> str:
        return self.__errorCode

    @errorCode.setter
    def errorCode(self, errorCode: str):
        self.__errorCode = errorCode

    @property
    def bpmn2_Error747(self):
        return self.__bpmn2_Error747

    @bpmn2_Error747.setter
    def bpmn2_Error747(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Error__bpmn2_Error747", None)
        self.__bpmn2_Error747 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Operation746"):
                opp_val = getattr(old_value, "bpmn2_Operation746", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Operation746"):
                opp_val = getattr(value, "bpmn2_Operation746", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Operation746", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Error539(self):
        return self.__bpmn2_Error539

    @bpmn2_Error539.setter
    def bpmn2_Error539(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Error__bpmn2_Error539", None)
        self.__bpmn2_Error539 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ItemDefinition540"):
                opp_val = getattr(old_value, "bpmn2_ItemDefinition540", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ItemDefinition540", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ItemDefinition540"):
                opp_val = getattr(value, "bpmn2_ItemDefinition540", None)
                setattr(value, "bpmn2_ItemDefinition540", self)

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
            if hasattr(old_value, "bpmn2_DocumentRoot110"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot110", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot110"):
                opp_val = getattr(value, "bpmn2_DocumentRoot110", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot110", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Error543(self):
        return self.__bpmn2_Error543

    @bpmn2_Error543.setter
    def bpmn2_Error543(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Error__bpmn2_Error543", None)
        self.__bpmn2_Error543 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ErrorEventDefinition542"):
                opp_val = getattr(old_value, "bpmn2_ErrorEventDefinition542", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_ErrorEventDefinition542", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ErrorEventDefinition542"):
                opp_val = getattr(value, "bpmn2_ErrorEventDefinition542", None)
                setattr(value, "bpmn2_ErrorEventDefinition542", self)

class bpmn2_ChoreographyActivity(FlowNode):

    def __init__(self, loopType: str, bpmn2_ChoreographyActivity: "bpmn2_DocumentRoot" = None, bpmn2_ChoreographyActivity387: set["bpmn2_Participant"] = None, bpmn2_ChoreographyActivity390: set["bpmn2_CorrelationKey"] = None, bpmn2_ChoreographyActivity393: "bpmn2_Participant" = None):
        self.loopType = loopType
        self.bpmn2_ChoreographyActivity = bpmn2_ChoreographyActivity
        self.bpmn2_ChoreographyActivity387 = bpmn2_ChoreographyActivity387 if bpmn2_ChoreographyActivity387 is not None else set()
        self.bpmn2_ChoreographyActivity390 = bpmn2_ChoreographyActivity390 if bpmn2_ChoreographyActivity390 is not None else set()
        self.bpmn2_ChoreographyActivity393 = bpmn2_ChoreographyActivity393
        
    @property
    def loopType(self) -> str:
        return self.__loopType

    @loopType.setter
    def loopType(self, loopType: str):
        self.__loopType = loopType

    @property
    def bpmn2_ChoreographyActivity393(self):
        return self.__bpmn2_ChoreographyActivity393

    @bpmn2_ChoreographyActivity393.setter
    def bpmn2_ChoreographyActivity393(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ChoreographyActivity__bpmn2_ChoreographyActivity393", None)
        self.__bpmn2_ChoreographyActivity393 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Participant394"):
                opp_val = getattr(old_value, "bpmn2_Participant394", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Participant394", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Participant394"):
                opp_val = getattr(value, "bpmn2_Participant394", None)
                setattr(value, "bpmn2_Participant394", self)

    @property
    def bpmn2_ChoreographyActivity(self):
        return self.__bpmn2_ChoreographyActivity

    @bpmn2_ChoreographyActivity.setter
    def bpmn2_ChoreographyActivity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ChoreographyActivity__bpmn2_ChoreographyActivity", None)
        self.__bpmn2_ChoreographyActivity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DocumentRoot54"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot54"):
                opp_val = getattr(value, "bpmn2_DocumentRoot54", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_ChoreographyActivity387(self):
        return self.__bpmn2_ChoreographyActivity387

    @bpmn2_ChoreographyActivity387.setter
    def bpmn2_ChoreographyActivity387(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ChoreographyActivity__bpmn2_ChoreographyActivity387", None)
        self.__bpmn2_ChoreographyActivity387 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Participant388"):
                    opp_val = getattr(item, "bpmn2_Participant388", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Participant388", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Participant388"):
                    opp_val = getattr(item, "bpmn2_Participant388", None)
                    
                    setattr(item, "bpmn2_Participant388", self)
                    

    @property
    def bpmn2_ChoreographyActivity390(self):
        return self.__bpmn2_ChoreographyActivity390

    @bpmn2_ChoreographyActivity390.setter
    def bpmn2_ChoreographyActivity390(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_ChoreographyActivity__bpmn2_ChoreographyActivity390", None)
        self.__bpmn2_ChoreographyActivity390 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_CorrelationKey391"):
                    opp_val = getattr(item, "bpmn2_CorrelationKey391", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_CorrelationKey391", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_CorrelationKey391"):
                    opp_val = getattr(item, "bpmn2_CorrelationKey391", None)
                    
                    setattr(item, "bpmn2_CorrelationKey391", self)
                    

class bpmn2_DataInput(ItemAwareElement):

    def __init__(self, isCollection: bool, bpmn2_DataInput: "bpmn2_DocumentRoot" = None, optionalInputRefs: set["bpmn2_InputSet"] = None, whileExecutingInputRefs: set["bpmn2_InputSet"] = None, dataInputRefs: set["bpmn2_InputSet"] = None, documentAndKnowledge: set["bpmn2_Document"] = None, bpmn2_DataInput613: "bpmn2_InputOutputSpecification" = None, DataInput: "bpmn2_InputSet" = None, DataInput625: "bpmn2_InputSet" = None, DataInput627: "bpmn2_InputSet" = None, bpmn2_DataInput723: "bpmn2_MultiInstanceLoopCharacteristics" = None, bpmn2_DataInput884: "bpmn2_ThrowEvent" = None):
        self.isCollection = isCollection
        self.bpmn2_DataInput = bpmn2_DataInput
        self.optionalInputRefs = optionalInputRefs if optionalInputRefs is not None else set()
        self.whileExecutingInputRefs = whileExecutingInputRefs if whileExecutingInputRefs is not None else set()
        self.dataInputRefs = dataInputRefs if dataInputRefs is not None else set()
        self.documentAndKnowledge = documentAndKnowledge if documentAndKnowledge is not None else set()
        self.bpmn2_DataInput613 = bpmn2_DataInput613
        self.DataInput = DataInput
        self.DataInput625 = DataInput625
        self.DataInput627 = DataInput627
        self.bpmn2_DataInput723 = bpmn2_DataInput723
        self.bpmn2_DataInput884 = bpmn2_DataInput884
        
    @property
    def isCollection(self) -> bool:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: bool):
        self.__isCollection = isCollection

    @property
    def bpmn2_DataInput723(self):
        return self.__bpmn2_DataInput723

    @bpmn2_DataInput723.setter
    def bpmn2_DataInput723(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataInput__bpmn2_DataInput723", None)
        self.__bpmn2_DataInput723 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_MultiInstanceLoopCharacteristics722"):
                opp_val = getattr(old_value, "bpmn2_MultiInstanceLoopCharacteristics722", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_MultiInstanceLoopCharacteristics722", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_MultiInstanceLoopCharacteristics722"):
                opp_val = getattr(value, "bpmn2_MultiInstanceLoopCharacteristics722", None)
                setattr(value, "bpmn2_MultiInstanceLoopCharacteristics722", self)

    @property
    def DataInput627(self):
        return self.__DataInput627

    @DataInput627.setter
    def DataInput627(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataInput__DataInput627", None)
        self.__DataInput627 = value
        
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
    def documentAndKnowledge(self):
        return self.__documentAndKnowledge

    @documentAndKnowledge.setter
    def documentAndKnowledge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataInput__documentAndKnowledge", None)
        self.__documentAndKnowledge = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, ".."):
                    opp_val = getattr(item, "..", None)
                    
                    if opp_val == self:
                        setattr(item, "..", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, ".."):
                    opp_val = getattr(item, "..", None)
                    
                    setattr(item, "..", self)
                    

    @property
    def DataInput625(self):
        return self.__DataInput625

    @DataInput625.setter
    def DataInput625(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataInput__DataInput625", None)
        self.__DataInput625 = value
        
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
                if hasattr(item, "InputSet508"):
                    opp_val = getattr(item, "InputSet508", None)
                    
                    if opp_val == self:
                        setattr(item, "InputSet508", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputSet508"):
                    opp_val = getattr(item, "InputSet508", None)
                    
                    setattr(item, "InputSet508", self)
                    

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
    def bpmn2_DataInput(self):
        return self.__bpmn2_DataInput

    @bpmn2_DataInput.setter
    def bpmn2_DataInput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataInput__bpmn2_DataInput", None)
        self.__bpmn2_DataInput = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DocumentRoot84"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot84", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot84"):
                opp_val = getattr(value, "bpmn2_DocumentRoot84", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot84", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_DataInput613(self):
        return self.__bpmn2_DataInput613

    @bpmn2_DataInput613.setter
    def bpmn2_DataInput613(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataInput__bpmn2_DataInput613", None)
        self.__bpmn2_DataInput613 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_InputOutputSpecification612"):
                opp_val = getattr(old_value, "bpmn2_InputOutputSpecification612", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_InputOutputSpecification612"):
                opp_val = getattr(value, "bpmn2_InputOutputSpecification612", None)
                if opp_val is None:
                    setattr(value, "bpmn2_InputOutputSpecification612", set([self]))
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
                if hasattr(item, "InputSet506"):
                    opp_val = getattr(item, "InputSet506", None)
                    
                    if opp_val == self:
                        setattr(item, "InputSet506", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputSet506"):
                    opp_val = getattr(item, "InputSet506", None)
                    
                    setattr(item, "InputSet506", self)
                    

    @property
    def bpmn2_DataInput884(self):
        return self.__bpmn2_DataInput884

    @bpmn2_DataInput884.setter
    def bpmn2_DataInput884(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataInput__bpmn2_DataInput884", None)
        self.__bpmn2_DataInput884 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_ThrowEvent883"):
                opp_val = getattr(old_value, "bpmn2_ThrowEvent883", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_ThrowEvent883"):
                opp_val = getattr(value, "bpmn2_ThrowEvent883", None)
                if opp_val is None:
                    setattr(value, "bpmn2_ThrowEvent883", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_Collaboration(RootElement):

    def __init__(self, isClosed: bool, bpmn2_Collaboration: "bpmn2_DocumentRoot" = None, bpmn2_Collaboration355: "bpmn2_CallConversation" = None, bpmn2_Collaboration423: set["bpmn2_Choreography"] = None, bpmn2_Collaboration426: set["bpmn2_ConversationLink"] = None, bpmn2_Collaboration399: set["bpmn2_Participant"] = None, bpmn2_Collaboration402: set["bpmn2_MessageFlow"] = None, bpmn2_Collaboration405: set["bpmn2_Artifact"] = None, bpmn2_Collaboration408: set["bpmn2_ConversationNode"] = None, bpmn2_Collaboration411: set["bpmn2_ConversationAssociation"] = None, bpmn2_Collaboration414: set["bpmn2_ParticipantAssociation"] = None, bpmn2_Collaboration417: set["bpmn2_MessageFlowAssociation"] = None, bpmn2_Collaboration420: set["bpmn2_CorrelationKey"] = None, bpmn2_Collaboration806: "bpmn2_Process" = None):
        self.isClosed = isClosed
        self.bpmn2_Collaboration = bpmn2_Collaboration
        self.bpmn2_Collaboration355 = bpmn2_Collaboration355
        self.bpmn2_Collaboration423 = bpmn2_Collaboration423 if bpmn2_Collaboration423 is not None else set()
        self.bpmn2_Collaboration426 = bpmn2_Collaboration426 if bpmn2_Collaboration426 is not None else set()
        self.bpmn2_Collaboration399 = bpmn2_Collaboration399 if bpmn2_Collaboration399 is not None else set()
        self.bpmn2_Collaboration402 = bpmn2_Collaboration402 if bpmn2_Collaboration402 is not None else set()
        self.bpmn2_Collaboration405 = bpmn2_Collaboration405 if bpmn2_Collaboration405 is not None else set()
        self.bpmn2_Collaboration408 = bpmn2_Collaboration408 if bpmn2_Collaboration408 is not None else set()
        self.bpmn2_Collaboration411 = bpmn2_Collaboration411 if bpmn2_Collaboration411 is not None else set()
        self.bpmn2_Collaboration414 = bpmn2_Collaboration414 if bpmn2_Collaboration414 is not None else set()
        self.bpmn2_Collaboration417 = bpmn2_Collaboration417 if bpmn2_Collaboration417 is not None else set()
        self.bpmn2_Collaboration420 = bpmn2_Collaboration420 if bpmn2_Collaboration420 is not None else set()
        self.bpmn2_Collaboration806 = bpmn2_Collaboration806
        
    @property
    def isClosed(self) -> bool:
        return self.__isClosed

    @isClosed.setter
    def isClosed(self, isClosed: bool):
        self.__isClosed = isClosed

    @property
    def bpmn2_Collaboration426(self):
        return self.__bpmn2_Collaboration426

    @bpmn2_Collaboration426.setter
    def bpmn2_Collaboration426(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration426", None)
        self.__bpmn2_Collaboration426 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_ConversationLink427"):
                    opp_val = getattr(item, "bpmn2_ConversationLink427", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_ConversationLink427", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_ConversationLink427"):
                    opp_val = getattr(item, "bpmn2_ConversationLink427", None)
                    
                    setattr(item, "bpmn2_ConversationLink427", self)
                    

    @property
    def bpmn2_Collaboration417(self):
        return self.__bpmn2_Collaboration417

    @bpmn2_Collaboration417.setter
    def bpmn2_Collaboration417(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration417", None)
        self.__bpmn2_Collaboration417 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_MessageFlowAssociation418"):
                    opp_val = getattr(item, "bpmn2_MessageFlowAssociation418", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_MessageFlowAssociation418", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_MessageFlowAssociation418"):
                    opp_val = getattr(item, "bpmn2_MessageFlowAssociation418", None)
                    
                    setattr(item, "bpmn2_MessageFlowAssociation418", self)
                    

    @property
    def bpmn2_Collaboration402(self):
        return self.__bpmn2_Collaboration402

    @bpmn2_Collaboration402.setter
    def bpmn2_Collaboration402(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration402", None)
        self.__bpmn2_Collaboration402 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_MessageFlow403"):
                    opp_val = getattr(item, "bpmn2_MessageFlow403", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_MessageFlow403", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_MessageFlow403"):
                    opp_val = getattr(item, "bpmn2_MessageFlow403", None)
                    
                    setattr(item, "bpmn2_MessageFlow403", self)
                    

    @property
    def bpmn2_Collaboration411(self):
        return self.__bpmn2_Collaboration411

    @bpmn2_Collaboration411.setter
    def bpmn2_Collaboration411(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration411", None)
        self.__bpmn2_Collaboration411 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_ConversationAssociation412"):
                    opp_val = getattr(item, "bpmn2_ConversationAssociation412", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_ConversationAssociation412", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_ConversationAssociation412"):
                    opp_val = getattr(item, "bpmn2_ConversationAssociation412", None)
                    
                    setattr(item, "bpmn2_ConversationAssociation412", self)
                    

    @property
    def bpmn2_Collaboration420(self):
        return self.__bpmn2_Collaboration420

    @bpmn2_Collaboration420.setter
    def bpmn2_Collaboration420(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration420", None)
        self.__bpmn2_Collaboration420 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_CorrelationKey421"):
                    opp_val = getattr(item, "bpmn2_CorrelationKey421", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_CorrelationKey421", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_CorrelationKey421"):
                    opp_val = getattr(item, "bpmn2_CorrelationKey421", None)
                    
                    setattr(item, "bpmn2_CorrelationKey421", self)
                    

    @property
    def bpmn2_Collaboration806(self):
        return self.__bpmn2_Collaboration806

    @bpmn2_Collaboration806.setter
    def bpmn2_Collaboration806(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration806", None)
        self.__bpmn2_Collaboration806 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Process805"):
                opp_val = getattr(old_value, "bpmn2_Process805", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Process805", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Process805"):
                opp_val = getattr(value, "bpmn2_Process805", None)
                setattr(value, "bpmn2_Process805", self)

    @property
    def bpmn2_Collaboration399(self):
        return self.__bpmn2_Collaboration399

    @bpmn2_Collaboration399.setter
    def bpmn2_Collaboration399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration399", None)
        self.__bpmn2_Collaboration399 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Participant400"):
                    opp_val = getattr(item, "bpmn2_Participant400", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Participant400", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Participant400"):
                    opp_val = getattr(item, "bpmn2_Participant400", None)
                    
                    setattr(item, "bpmn2_Participant400", self)
                    

    @property
    def bpmn2_Collaboration355(self):
        return self.__bpmn2_Collaboration355

    @bpmn2_Collaboration355.setter
    def bpmn2_Collaboration355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration355", None)
        self.__bpmn2_Collaboration355 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CallConversation354"):
                opp_val = getattr(old_value, "bpmn2_CallConversation354", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_CallConversation354", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CallConversation354"):
                opp_val = getattr(value, "bpmn2_CallConversation354", None)
                setattr(value, "bpmn2_CallConversation354", self)

    @property
    def bpmn2_Collaboration405(self):
        return self.__bpmn2_Collaboration405

    @bpmn2_Collaboration405.setter
    def bpmn2_Collaboration405(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration405", None)
        self.__bpmn2_Collaboration405 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Artifact406"):
                    opp_val = getattr(item, "bpmn2_Artifact406", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Artifact406", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Artifact406"):
                    opp_val = getattr(item, "bpmn2_Artifact406", None)
                    
                    setattr(item, "bpmn2_Artifact406", self)
                    

    @property
    def bpmn2_Collaboration423(self):
        return self.__bpmn2_Collaboration423

    @bpmn2_Collaboration423.setter
    def bpmn2_Collaboration423(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration423", None)
        self.__bpmn2_Collaboration423 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Choreography424"):
                    opp_val = getattr(item, "bpmn2_Choreography424", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Choreography424", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Choreography424"):
                    opp_val = getattr(item, "bpmn2_Choreography424", None)
                    
                    setattr(item, "bpmn2_Choreography424", self)
                    

    @property
    def bpmn2_Collaboration408(self):
        return self.__bpmn2_Collaboration408

    @bpmn2_Collaboration408.setter
    def bpmn2_Collaboration408(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration408", None)
        self.__bpmn2_Collaboration408 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_ConversationNode409"):
                    opp_val = getattr(item, "bpmn2_ConversationNode409", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_ConversationNode409", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_ConversationNode409"):
                    opp_val = getattr(item, "bpmn2_ConversationNode409", None)
                    
                    setattr(item, "bpmn2_ConversationNode409", self)
                    

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
            if hasattr(old_value, "bpmn2_DocumentRoot52"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot52"):
                opp_val = getattr(value, "bpmn2_DocumentRoot52", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Collaboration414(self):
        return self.__bpmn2_Collaboration414

    @bpmn2_Collaboration414.setter
    def bpmn2_Collaboration414(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Collaboration__bpmn2_Collaboration414", None)
        self.__bpmn2_Collaboration414 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_ParticipantAssociation415"):
                    opp_val = getattr(item, "bpmn2_ParticipantAssociation415", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_ParticipantAssociation415", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_ParticipantAssociation415"):
                    opp_val = getattr(item, "bpmn2_ParticipantAssociation415", None)
                    
                    setattr(item, "bpmn2_ParticipantAssociation415", self)
                    

class bpmn2_DataAssociation(BaseElement):

    pass
class bpmn2_Choreography(FlowElementsContainer, Collaboration):

    pass
class bpmn2_CorrelationSubscription(BaseElement):

    pass
class bpmn2_CategoryValue(BaseElement):

    def __init__(self, value: str, bpmn2_CategoryValue: "bpmn2_DocumentRoot" = None, bpmn2_CategoryValue382: "bpmn2_Category" = None, bpmn2_CategoryValue384: set["bpmn2_FlowElement"] = None, bpmn2_CategoryValue574: "bpmn2_FlowElement" = None, bpmn2_CategoryValue598: "bpmn2_Group" = None):
        self.value = value
        self.bpmn2_CategoryValue = bpmn2_CategoryValue
        self.bpmn2_CategoryValue382 = bpmn2_CategoryValue382
        self.bpmn2_CategoryValue384 = bpmn2_CategoryValue384 if bpmn2_CategoryValue384 is not None else set()
        self.bpmn2_CategoryValue574 = bpmn2_CategoryValue574
        self.bpmn2_CategoryValue598 = bpmn2_CategoryValue598
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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
            if hasattr(old_value, "bpmn2_DocumentRoot48"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot48"):
                opp_val = getattr(value, "bpmn2_DocumentRoot48", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_CategoryValue384(self):
        return self.__bpmn2_CategoryValue384

    @bpmn2_CategoryValue384.setter
    def bpmn2_CategoryValue384(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CategoryValue__bpmn2_CategoryValue384", None)
        self.__bpmn2_CategoryValue384 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_FlowElement385"):
                    opp_val = getattr(item, "bpmn2_FlowElement385", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_FlowElement385", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_FlowElement385"):
                    opp_val = getattr(item, "bpmn2_FlowElement385", None)
                    
                    setattr(item, "bpmn2_FlowElement385", self)
                    

    @property
    def bpmn2_CategoryValue382(self):
        return self.__bpmn2_CategoryValue382

    @bpmn2_CategoryValue382.setter
    def bpmn2_CategoryValue382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CategoryValue__bpmn2_CategoryValue382", None)
        self.__bpmn2_CategoryValue382 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Category381"):
                opp_val = getattr(old_value, "bpmn2_Category381", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Category381"):
                opp_val = getattr(value, "bpmn2_Category381", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Category381", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_CategoryValue574(self):
        return self.__bpmn2_CategoryValue574

    @bpmn2_CategoryValue574.setter
    def bpmn2_CategoryValue574(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CategoryValue__bpmn2_CategoryValue574", None)
        self.__bpmn2_CategoryValue574 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_FlowElement573"):
                opp_val = getattr(old_value, "bpmn2_FlowElement573", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_FlowElement573"):
                opp_val = getattr(value, "bpmn2_FlowElement573", None)
                if opp_val is None:
                    setattr(value, "bpmn2_FlowElement573", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_CategoryValue598(self):
        return self.__bpmn2_CategoryValue598

    @bpmn2_CategoryValue598.setter
    def bpmn2_CategoryValue598(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CategoryValue__bpmn2_CategoryValue598", None)
        self.__bpmn2_CategoryValue598 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Group597"):
                opp_val = getattr(old_value, "bpmn2_Group597", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Group597", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Group597"):
                opp_val = getattr(value, "bpmn2_Group597", None)
                setattr(value, "bpmn2_Group597", self)

class bpmn2_Category(RootElement):

    pass
class bpmn2_CorrelationPropertyRetrievalExpression(BaseElement):

    pass
class bpmn2_CatchEvent(Event):

    def __init__(self, parallelMultiple: bool, bpmn2_CatchEvent: "bpmn2_DocumentRoot" = None, bpmn2_CatchEvent366: set["bpmn2_DataOutput"] = None, bpmn2_CatchEvent369: set["bpmn2_DataOutputAssociation"] = None, bpmn2_CatchEvent372: "bpmn2_OutputSet" = None, bpmn2_CatchEvent375: set["bpmn2_EventDefinition"] = None, bpmn2_CatchEvent378: set["bpmn2_EventDefinition"] = None):
        self.parallelMultiple = parallelMultiple
        self.bpmn2_CatchEvent = bpmn2_CatchEvent
        self.bpmn2_CatchEvent366 = bpmn2_CatchEvent366 if bpmn2_CatchEvent366 is not None else set()
        self.bpmn2_CatchEvent369 = bpmn2_CatchEvent369 if bpmn2_CatchEvent369 is not None else set()
        self.bpmn2_CatchEvent372 = bpmn2_CatchEvent372
        self.bpmn2_CatchEvent375 = bpmn2_CatchEvent375 if bpmn2_CatchEvent375 is not None else set()
        self.bpmn2_CatchEvent378 = bpmn2_CatchEvent378 if bpmn2_CatchEvent378 is not None else set()
        
    @property
    def parallelMultiple(self) -> bool:
        return self.__parallelMultiple

    @parallelMultiple.setter
    def parallelMultiple(self, parallelMultiple: bool):
        self.__parallelMultiple = parallelMultiple

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
            if hasattr(old_value, "bpmn2_DocumentRoot44"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot44"):
                opp_val = getattr(value, "bpmn2_DocumentRoot44", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_CatchEvent372(self):
        return self.__bpmn2_CatchEvent372

    @bpmn2_CatchEvent372.setter
    def bpmn2_CatchEvent372(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CatchEvent__bpmn2_CatchEvent372", None)
        self.__bpmn2_CatchEvent372 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_OutputSet373"):
                opp_val = getattr(old_value, "bpmn2_OutputSet373", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_OutputSet373", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_OutputSet373"):
                opp_val = getattr(value, "bpmn2_OutputSet373", None)
                setattr(value, "bpmn2_OutputSet373", self)

    @property
    def bpmn2_CatchEvent375(self):
        return self.__bpmn2_CatchEvent375

    @bpmn2_CatchEvent375.setter
    def bpmn2_CatchEvent375(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CatchEvent__bpmn2_CatchEvent375", None)
        self.__bpmn2_CatchEvent375 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_EventDefinition376"):
                    opp_val = getattr(item, "bpmn2_EventDefinition376", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_EventDefinition376", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_EventDefinition376"):
                    opp_val = getattr(item, "bpmn2_EventDefinition376", None)
                    
                    setattr(item, "bpmn2_EventDefinition376", self)
                    

    @property
    def bpmn2_CatchEvent369(self):
        return self.__bpmn2_CatchEvent369

    @bpmn2_CatchEvent369.setter
    def bpmn2_CatchEvent369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CatchEvent__bpmn2_CatchEvent369", None)
        self.__bpmn2_CatchEvent369 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_DataOutputAssociation370"):
                    opp_val = getattr(item, "bpmn2_DataOutputAssociation370", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_DataOutputAssociation370", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_DataOutputAssociation370"):
                    opp_val = getattr(item, "bpmn2_DataOutputAssociation370", None)
                    
                    setattr(item, "bpmn2_DataOutputAssociation370", self)
                    

    @property
    def bpmn2_CatchEvent378(self):
        return self.__bpmn2_CatchEvent378

    @bpmn2_CatchEvent378.setter
    def bpmn2_CatchEvent378(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CatchEvent__bpmn2_CatchEvent378", None)
        self.__bpmn2_CatchEvent378 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_EventDefinition379"):
                    opp_val = getattr(item, "bpmn2_EventDefinition379", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_EventDefinition379", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_EventDefinition379"):
                    opp_val = getattr(item, "bpmn2_EventDefinition379", None)
                    
                    setattr(item, "bpmn2_EventDefinition379", self)
                    

    @property
    def bpmn2_CatchEvent366(self):
        return self.__bpmn2_CatchEvent366

    @bpmn2_CatchEvent366.setter
    def bpmn2_CatchEvent366(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CatchEvent__bpmn2_CatchEvent366", None)
        self.__bpmn2_CatchEvent366 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_DataOutput367"):
                    opp_val = getattr(item, "bpmn2_DataOutput367", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_DataOutput367", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_DataOutput367"):
                    opp_val = getattr(item, "bpmn2_DataOutput367", None)
                    
                    setattr(item, "bpmn2_DataOutput367", self)
                    

class bpmn2_CorrelationPropertyBinding(BaseElement):

    pass
class bpmn2_CorrelationProperty(RootElement):

    pass
class bpmn2_CorrelationKey(BaseElement):

    pass
class bpmn2_ConversationLink(BaseElement):

    pass
class bpmn2_ConversationAssociation(BaseElement):

    pass
class bpmn2_Conversation(ConversationNode):

    pass
class bpmn2_ConditionalEventDefinition(EventDefinition):

    pass
class bpmn2_ComplexGateway(Gateway):

    pass
class bpmn2_DataOutput(ItemAwareElement):

    def __init__(self, isCollection: bool, bpmn2_DataOutput: "bpmn2_DocumentRoot" = None, bpmn2_DataOutput367: "bpmn2_CatchEvent" = None, documentAndKnowledge519: set["bpmn2_Document"] = None, optionalOutputRefs: set["bpmn2_OutputSet"] = None, whileExecutingOutputRefs: set["bpmn2_OutputSet"] = None, dataOutputRefs: set["bpmn2_OutputSet"] = None, bpmn2_DataOutput616: "bpmn2_InputOutputSpecification" = None, DataOutput: "bpmn2_OutputSet" = None, DataOutput753: "bpmn2_OutputSet" = None, DataOutput755: "bpmn2_OutputSet" = None, bpmn2_DataOutput726: "bpmn2_MultiInstanceLoopCharacteristics" = None):
        self.isCollection = isCollection
        self.bpmn2_DataOutput = bpmn2_DataOutput
        self.bpmn2_DataOutput367 = bpmn2_DataOutput367
        self.documentAndKnowledge519 = documentAndKnowledge519 if documentAndKnowledge519 is not None else set()
        self.optionalOutputRefs = optionalOutputRefs if optionalOutputRefs is not None else set()
        self.whileExecutingOutputRefs = whileExecutingOutputRefs if whileExecutingOutputRefs is not None else set()
        self.dataOutputRefs = dataOutputRefs if dataOutputRefs is not None else set()
        self.bpmn2_DataOutput616 = bpmn2_DataOutput616
        self.DataOutput = DataOutput
        self.DataOutput753 = DataOutput753
        self.DataOutput755 = DataOutput755
        self.bpmn2_DataOutput726 = bpmn2_DataOutput726
        
    @property
    def isCollection(self) -> bool:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: bool):
        self.__isCollection = isCollection

    @property
    def DataOutput755(self):
        return self.__DataOutput755

    @DataOutput755.setter
    def DataOutput755(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataOutput__DataOutput755", None)
        self.__DataOutput755 = value
        
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
                if hasattr(item, "OutputSet517"):
                    opp_val = getattr(item, "OutputSet517", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputSet517", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputSet517"):
                    opp_val = getattr(item, "OutputSet517", None)
                    
                    setattr(item, "OutputSet517", self)
                    

    @property
    def documentAndKnowledge519(self):
        return self.__documentAndKnowledge519

    @documentAndKnowledge519.setter
    def documentAndKnowledge519(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataOutput__documentAndKnowledge519", None)
        self.__documentAndKnowledge519 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "..520"):
                    opp_val = getattr(item, "..520", None)
                    
                    if opp_val == self:
                        setattr(item, "..520", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "..520"):
                    opp_val = getattr(item, "..520", None)
                    
                    setattr(item, "..520", self)
                    

    @property
    def bpmn2_DataOutput367(self):
        return self.__bpmn2_DataOutput367

    @bpmn2_DataOutput367.setter
    def bpmn2_DataOutput367(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataOutput__bpmn2_DataOutput367", None)
        self.__bpmn2_DataOutput367 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CatchEvent366"):
                opp_val = getattr(old_value, "bpmn2_CatchEvent366", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CatchEvent366"):
                opp_val = getattr(value, "bpmn2_CatchEvent366", None)
                if opp_val is None:
                    setattr(value, "bpmn2_CatchEvent366", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DataOutput753(self):
        return self.__DataOutput753

    @DataOutput753.setter
    def DataOutput753(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataOutput__DataOutput753", None)
        self.__DataOutput753 = value
        
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
    def bpmn2_DataOutput616(self):
        return self.__bpmn2_DataOutput616

    @bpmn2_DataOutput616.setter
    def bpmn2_DataOutput616(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataOutput__bpmn2_DataOutput616", None)
        self.__bpmn2_DataOutput616 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_InputOutputSpecification615"):
                opp_val = getattr(old_value, "bpmn2_InputOutputSpecification615", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_InputOutputSpecification615"):
                opp_val = getattr(value, "bpmn2_InputOutputSpecification615", None)
                if opp_val is None:
                    setattr(value, "bpmn2_InputOutputSpecification615", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_DataOutput726(self):
        return self.__bpmn2_DataOutput726

    @bpmn2_DataOutput726.setter
    def bpmn2_DataOutput726(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataOutput__bpmn2_DataOutput726", None)
        self.__bpmn2_DataOutput726 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_MultiInstanceLoopCharacteristics725"):
                opp_val = getattr(old_value, "bpmn2_MultiInstanceLoopCharacteristics725", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_MultiInstanceLoopCharacteristics725", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_MultiInstanceLoopCharacteristics725"):
                opp_val = getattr(value, "bpmn2_MultiInstanceLoopCharacteristics725", None)
                setattr(value, "bpmn2_MultiInstanceLoopCharacteristics725", self)

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
                if hasattr(item, "OutputSet515"):
                    opp_val = getattr(item, "OutputSet515", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputSet515", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputSet515"):
                    opp_val = getattr(item, "OutputSet515", None)
                    
                    setattr(item, "OutputSet515", self)
                    

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
            if hasattr(old_value, "bpmn2_DocumentRoot92"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot92"):
                opp_val = getattr(value, "bpmn2_DocumentRoot92", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                    

class bpmn2_ComplexBehaviorDefinition(BaseElement):

    pass
class bpmn2_DataObjectReference(FlowElement, ItemAwareElement):

    pass
class bpmn2_CompensateEventDefinition(EventDefinition):

    def __init__(self, waitForCompletion: bool, bpmn2_CompensateEventDefinition: "bpmn2_DocumentRoot" = None, bpmn2_CompensateEventDefinition429: "bpmn2_Activity" = None):
        self.waitForCompletion = waitForCompletion
        self.bpmn2_CompensateEventDefinition = bpmn2_CompensateEventDefinition
        self.bpmn2_CompensateEventDefinition429 = bpmn2_CompensateEventDefinition429
        
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
            if hasattr(old_value, "bpmn2_DocumentRoot58"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot58"):
                opp_val = getattr(value, "bpmn2_DocumentRoot58", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_CompensateEventDefinition429(self):
        return self.__bpmn2_CompensateEventDefinition429

    @bpmn2_CompensateEventDefinition429.setter
    def bpmn2_CompensateEventDefinition429(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_CompensateEventDefinition__bpmn2_CompensateEventDefinition429", None)
        self.__bpmn2_CompensateEventDefinition429 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Activity430"):
                opp_val = getattr(old_value, "bpmn2_Activity430", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Activity430", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Activity430"):
                opp_val = getattr(value, "bpmn2_Activity430", None)
                setattr(value, "bpmn2_Activity430", self)

class bpmn2_DataObject(FlowElement, ItemAwareElement):

    def __init__(self, isCollection: bool, bpmn2_DataObject: "bpmn2_DocumentRoot" = None, bpmn2_DataObject512: "bpmn2_DataObjectReference" = None):
        self.isCollection = isCollection
        self.bpmn2_DataObject = bpmn2_DataObject
        self.bpmn2_DataObject512 = bpmn2_DataObject512
        
    @property
    def isCollection(self) -> bool:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: bool):
        self.__isCollection = isCollection

    @property
    def bpmn2_DataObject512(self):
        return self.__bpmn2_DataObject512

    @bpmn2_DataObject512.setter
    def bpmn2_DataObject512(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DataObject__bpmn2_DataObject512", None)
        self.__bpmn2_DataObject512 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DataObjectReference511"):
                opp_val = getattr(old_value, "bpmn2_DataObjectReference511", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_DataObjectReference511", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DataObjectReference511"):
                opp_val = getattr(value, "bpmn2_DataObjectReference511", None)
                setattr(value, "bpmn2_DataObjectReference511", self)

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
            if hasattr(old_value, "bpmn2_DocumentRoot88"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot88"):
                opp_val = getattr(value, "bpmn2_DocumentRoot88", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_ChoreographyTask(ChoreographyActivity):

    pass
class bpmn2_DataInputAssociation(DataAssociation):

    pass
class bpmn2_BaseElement:

    def __init__(self, description: str, id: str, anyAttribute: str, name: str, bpmn2_BaseElement22: "bpmn2_DocumentRoot" = None, bpmn2_BaseElement: "bpmn2_DocumentRoot" = None, bpmn2_BaseElement328: "bpmn2_Association" = None, bpmn2_BaseElement331: "bpmn2_Association" = None, bpmn2_BaseElement333: set["bpmn2_ExtensionAttributeValue"] = None, bpmn2_BaseElement336: set["bpmn2_Documentation"] = None, bpmn2_BaseElement339: set["bpmn2_ExtensionDefinition"] = None, bpmn2_BaseElement664: "bpmn2_Lane" = None, bpmn2_BaseElement657: "bpmn2_Lane" = None):
        self.description = description
        self.id = id
        self.anyAttribute = anyAttribute
        self.name = name
        self.bpmn2_BaseElement22 = bpmn2_BaseElement22
        self.bpmn2_BaseElement = bpmn2_BaseElement
        self.bpmn2_BaseElement328 = bpmn2_BaseElement328
        self.bpmn2_BaseElement331 = bpmn2_BaseElement331
        self.bpmn2_BaseElement333 = bpmn2_BaseElement333 if bpmn2_BaseElement333 is not None else set()
        self.bpmn2_BaseElement336 = bpmn2_BaseElement336 if bpmn2_BaseElement336 is not None else set()
        self.bpmn2_BaseElement339 = bpmn2_BaseElement339 if bpmn2_BaseElement339 is not None else set()
        self.bpmn2_BaseElement664 = bpmn2_BaseElement664
        self.bpmn2_BaseElement657 = bpmn2_BaseElement657
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

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
    def bpmn2_BaseElement664(self):
        return self.__bpmn2_BaseElement664

    @bpmn2_BaseElement664.setter
    def bpmn2_BaseElement664(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BaseElement__bpmn2_BaseElement664", None)
        self.__bpmn2_BaseElement664 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Lane663"):
                opp_val = getattr(old_value, "bpmn2_Lane663", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Lane663", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Lane663"):
                opp_val = getattr(value, "bpmn2_Lane663", None)
                setattr(value, "bpmn2_Lane663", self)

    @property
    def bpmn2_BaseElement336(self):
        return self.__bpmn2_BaseElement336

    @bpmn2_BaseElement336.setter
    def bpmn2_BaseElement336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BaseElement__bpmn2_BaseElement336", None)
        self.__bpmn2_BaseElement336 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Documentation337"):
                    opp_val = getattr(item, "bpmn2_Documentation337", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Documentation337", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Documentation337"):
                    opp_val = getattr(item, "bpmn2_Documentation337", None)
                    
                    setattr(item, "bpmn2_Documentation337", self)
                    

    @property
    def bpmn2_BaseElement(self):
        return self.__bpmn2_BaseElement

    @bpmn2_BaseElement.setter
    def bpmn2_BaseElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BaseElement__bpmn2_BaseElement", None)
        self.__bpmn2_BaseElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DocumentRoot19"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot19"):
                opp_val = getattr(value, "bpmn2_DocumentRoot19", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_BaseElement333(self):
        return self.__bpmn2_BaseElement333

    @bpmn2_BaseElement333.setter
    def bpmn2_BaseElement333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BaseElement__bpmn2_BaseElement333", None)
        self.__bpmn2_BaseElement333 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_ExtensionAttributeValue334"):
                    opp_val = getattr(item, "bpmn2_ExtensionAttributeValue334", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_ExtensionAttributeValue334", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_ExtensionAttributeValue334"):
                    opp_val = getattr(item, "bpmn2_ExtensionAttributeValue334", None)
                    
                    setattr(item, "bpmn2_ExtensionAttributeValue334", self)
                    

    @property
    def bpmn2_BaseElement22(self):
        return self.__bpmn2_BaseElement22

    @bpmn2_BaseElement22.setter
    def bpmn2_BaseElement22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BaseElement__bpmn2_BaseElement22", None)
        self.__bpmn2_BaseElement22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DocumentRoot21"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot21"):
                opp_val = getattr(value, "bpmn2_DocumentRoot21", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_BaseElement328(self):
        return self.__bpmn2_BaseElement328

    @bpmn2_BaseElement328.setter
    def bpmn2_BaseElement328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BaseElement__bpmn2_BaseElement328", None)
        self.__bpmn2_BaseElement328 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Association327"):
                opp_val = getattr(old_value, "bpmn2_Association327", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Association327", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Association327"):
                opp_val = getattr(value, "bpmn2_Association327", None)
                setattr(value, "bpmn2_Association327", self)

    @property
    def bpmn2_BaseElement657(self):
        return self.__bpmn2_BaseElement657

    @bpmn2_BaseElement657.setter
    def bpmn2_BaseElement657(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BaseElement__bpmn2_BaseElement657", None)
        self.__bpmn2_BaseElement657 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Lane656"):
                opp_val = getattr(old_value, "bpmn2_Lane656", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Lane656"):
                opp_val = getattr(value, "bpmn2_Lane656", None)
                if opp_val is None:
                    setattr(value, "bpmn2_Lane656", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_BaseElement339(self):
        return self.__bpmn2_BaseElement339

    @bpmn2_BaseElement339.setter
    def bpmn2_BaseElement339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BaseElement__bpmn2_BaseElement339", None)
        self.__bpmn2_BaseElement339 = value if value is not None else set()
        
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
    def bpmn2_BaseElement331(self):
        return self.__bpmn2_BaseElement331

    @bpmn2_BaseElement331.setter
    def bpmn2_BaseElement331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BaseElement__bpmn2_BaseElement331", None)
        self.__bpmn2_BaseElement331 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Association330"):
                opp_val = getattr(old_value, "bpmn2_Association330", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Association330", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Association330"):
                opp_val = getattr(value, "bpmn2_Association330", None)
                setattr(value, "bpmn2_Association330", self)

class bpmn2_Auditing(BaseElement):

    pass
class bpmn2_Association(Artifact):

    def __init__(self, associationDirection: str, bpmn2_Association: "bpmn2_DocumentRoot" = None, bpmn2_Association327: "bpmn2_BaseElement" = None, bpmn2_Association330: "bpmn2_BaseElement" = None):
        self.associationDirection = associationDirection
        self.bpmn2_Association = bpmn2_Association
        self.bpmn2_Association327 = bpmn2_Association327
        self.bpmn2_Association330 = bpmn2_Association330
        
    @property
    def associationDirection(self) -> str:
        return self.__associationDirection

    @associationDirection.setter
    def associationDirection(self, associationDirection: str):
        self.__associationDirection = associationDirection

    @property
    def bpmn2_Association327(self):
        return self.__bpmn2_Association327

    @bpmn2_Association327.setter
    def bpmn2_Association327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Association__bpmn2_Association327", None)
        self.__bpmn2_Association327 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_BaseElement328"):
                opp_val = getattr(old_value, "bpmn2_BaseElement328", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_BaseElement328", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_BaseElement328"):
                opp_val = getattr(value, "bpmn2_BaseElement328", None)
                setattr(value, "bpmn2_BaseElement328", self)

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
            if hasattr(old_value, "bpmn2_DocumentRoot15"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot15"):
                opp_val = getattr(value, "bpmn2_DocumentRoot15", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Association330(self):
        return self.__bpmn2_Association330

    @bpmn2_Association330.setter
    def bpmn2_Association330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Association__bpmn2_Association330", None)
        self.__bpmn2_Association330 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_BaseElement331"):
                opp_val = getattr(old_value, "bpmn2_BaseElement331", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_BaseElement331", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_BaseElement331"):
                opp_val = getattr(value, "bpmn2_BaseElement331", None)
                setattr(value, "bpmn2_BaseElement331", self)

class bpmn2_RootElement(BaseElement):

    pass
class bpmn2_EventDefinition(RootElement):

    pass
class bpmn2_CancelEventDefinition(EventDefinition):

    pass
class bpmn2_ConversationNode(BaseElement, InteractionNode):

    pass
class bpmn2_CallConversation(ConversationNode):

    pass
class bpmn2_CallChoreography(ChoreographyActivity):

    pass
class bpmn2_CallActivity(Activity):

    pass
class bpmn2_CallableElement(RootElement):

    pass
class bpmn2_BusinessRuleTask(Task):

    def __init__(self, implementation: str, bpmn2_BusinessRuleTask: "bpmn2_DocumentRoot" = None):
        self.implementation = implementation
        self.bpmn2_BusinessRuleTask = bpmn2_BusinessRuleTask
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def bpmn2_BusinessRuleTask(self):
        return self.__bpmn2_BusinessRuleTask

    @bpmn2_BusinessRuleTask.setter
    def bpmn2_BusinessRuleTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BusinessRuleTask__bpmn2_BusinessRuleTask", None)
        self.__bpmn2_BusinessRuleTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DocumentRoot26"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot26"):
                opp_val = getattr(value, "bpmn2_DocumentRoot26", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_BoundaryEvent(CatchEvent):

    def __init__(self, cancelActivity: bool, bpmn2_BoundaryEvent: "bpmn2_DocumentRoot" = None, BoundaryEvent: "bpmn2_Activity" = None, boundaryEventRefs: "bpmn2_Activity" = None):
        self.cancelActivity = cancelActivity
        self.bpmn2_BoundaryEvent = bpmn2_BoundaryEvent
        self.BoundaryEvent = BoundaryEvent
        self.boundaryEventRefs = boundaryEventRefs
        
    @property
    def cancelActivity(self) -> bool:
        return self.__cancelActivity

    @cancelActivity.setter
    def cancelActivity(self, cancelActivity: bool):
        self.__cancelActivity = cancelActivity

    @property
    def bpmn2_BoundaryEvent(self):
        return self.__bpmn2_BoundaryEvent

    @bpmn2_BoundaryEvent.setter
    def bpmn2_BoundaryEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_BoundaryEvent__bpmn2_BoundaryEvent", None)
        self.__bpmn2_BoundaryEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DocumentRoot24"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot24"):
                opp_val = getattr(value, "bpmn2_DocumentRoot24", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot24", set([self]))
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

class bpmn2_Assignment(BaseElement):

    pass
class bpmn2_Artifact(BaseElement):

    pass
class bpmn2_FlowElement(BaseElement):

    pass
class bpmn2_AdHocSubProcess(SubProcess):

    def __init__(self, cancelRemainingInstances: bool, ordering: str, bpmn2_AdHocSubProcess: "bpmn2_DocumentRoot" = None, bpmn2_AdHocSubProcess318: "bpmn2_Expression" = None):
        self.cancelRemainingInstances = cancelRemainingInstances
        self.ordering = ordering
        self.bpmn2_AdHocSubProcess = bpmn2_AdHocSubProcess
        self.bpmn2_AdHocSubProcess318 = bpmn2_AdHocSubProcess318
        
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
    def bpmn2_AdHocSubProcess318(self):
        return self.__bpmn2_AdHocSubProcess318

    @bpmn2_AdHocSubProcess318.setter
    def bpmn2_AdHocSubProcess318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_AdHocSubProcess__bpmn2_AdHocSubProcess318", None)
        self.__bpmn2_AdHocSubProcess318 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_Expression319"):
                opp_val = getattr(old_value, "bpmn2_Expression319", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_Expression319", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_Expression319"):
                opp_val = getattr(value, "bpmn2_Expression319", None)
                setattr(value, "bpmn2_Expression319", self)

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
            if hasattr(old_value, "bpmn2_DocumentRoot7"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot7"):
                opp_val = getattr(value, "bpmn2_DocumentRoot7", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn2_Activity(FlowNode):

    def __init__(self, completionQuantity: int, isForCompensation: bool, startQuantity: int, bpmn2_Activity: "bpmn2_DocumentRoot" = None, bpmn2_Activity277: "bpmn2_InputOutputSpecification" = None, attachedToRef: set["bpmn2_BoundaryEvent"] = None, bpmn2_Activity308: set["bpmn2_Performer"] = None, bpmn2_Activity311: set["bpmn2_Position"] = None, bpmn2_Activity313: set["bpmn2_Role"] = None, bpmn2_Activity315: set["bpmn2_Competency"] = None, bpmn2_Activity281: set["bpmn2_Property"] = None, bpmn2_Activity284: set["bpmn2_DataInputAssociation"] = None, bpmn2_Activity287: set["bpmn2_DataOutputAssociation"] = None, bpmn2_Activity290: set["bpmn2_ResourceRole"] = None, bpmn2_Activity293: "bpmn2_LoopCharacteristics" = None, bpmn2_Activity296: "bpmn2_SequenceFlow" = None, bpmn2_Activity299: set["bpmn2_Competency"] = None, bpmn2_Activity301: set["bpmn2_Criterion"] = None, bpmn2_Activity303: set["bpmn2_OrganisationalUnit"] = None, bpmn2_Activity305: set["bpmn2_OrganisationalUnit"] = None, Activity: "bpmn2_BoundaryEvent" = None, bpmn2_Activity430: "bpmn2_CompensateEventDefinition" = None):
        self.completionQuantity = completionQuantity
        self.isForCompensation = isForCompensation
        self.startQuantity = startQuantity
        self.bpmn2_Activity = bpmn2_Activity
        self.bpmn2_Activity277 = bpmn2_Activity277
        self.attachedToRef = attachedToRef if attachedToRef is not None else set()
        self.bpmn2_Activity308 = bpmn2_Activity308 if bpmn2_Activity308 is not None else set()
        self.bpmn2_Activity311 = bpmn2_Activity311 if bpmn2_Activity311 is not None else set()
        self.bpmn2_Activity313 = bpmn2_Activity313 if bpmn2_Activity313 is not None else set()
        self.bpmn2_Activity315 = bpmn2_Activity315 if bpmn2_Activity315 is not None else set()
        self.bpmn2_Activity281 = bpmn2_Activity281 if bpmn2_Activity281 is not None else set()
        self.bpmn2_Activity284 = bpmn2_Activity284 if bpmn2_Activity284 is not None else set()
        self.bpmn2_Activity287 = bpmn2_Activity287 if bpmn2_Activity287 is not None else set()
        self.bpmn2_Activity290 = bpmn2_Activity290 if bpmn2_Activity290 is not None else set()
        self.bpmn2_Activity293 = bpmn2_Activity293
        self.bpmn2_Activity296 = bpmn2_Activity296
        self.bpmn2_Activity299 = bpmn2_Activity299 if bpmn2_Activity299 is not None else set()
        self.bpmn2_Activity301 = bpmn2_Activity301 if bpmn2_Activity301 is not None else set()
        self.bpmn2_Activity303 = bpmn2_Activity303 if bpmn2_Activity303 is not None else set()
        self.bpmn2_Activity305 = bpmn2_Activity305 if bpmn2_Activity305 is not None else set()
        self.Activity = Activity
        self.bpmn2_Activity430 = bpmn2_Activity430
        
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
    def completionQuantity(self) -> int:
        return self.__completionQuantity

    @completionQuantity.setter
    def completionQuantity(self, completionQuantity: int):
        self.__completionQuantity = completionQuantity

    @property
    def bpmn2_Activity430(self):
        return self.__bpmn2_Activity430

    @bpmn2_Activity430.setter
    def bpmn2_Activity430(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity430", None)
        self.__bpmn2_Activity430 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_CompensateEventDefinition429"):
                opp_val = getattr(old_value, "bpmn2_CompensateEventDefinition429", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_CompensateEventDefinition429", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_CompensateEventDefinition429"):
                opp_val = getattr(value, "bpmn2_CompensateEventDefinition429", None)
                setattr(value, "bpmn2_CompensateEventDefinition429", self)

    @property
    def bpmn2_Activity313(self):
        return self.__bpmn2_Activity313

    @bpmn2_Activity313.setter
    def bpmn2_Activity313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity313", None)
        self.__bpmn2_Activity313 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Role"):
                    opp_val = getattr(item, "bpmn2_Role", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Role", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Role"):
                    opp_val = getattr(item, "bpmn2_Role", None)
                    
                    setattr(item, "bpmn2_Role", self)
                    

    @property
    def bpmn2_Activity277(self):
        return self.__bpmn2_Activity277

    @bpmn2_Activity277.setter
    def bpmn2_Activity277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity277", None)
        self.__bpmn2_Activity277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_InputOutputSpecification278"):
                opp_val = getattr(old_value, "bpmn2_InputOutputSpecification278", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_InputOutputSpecification278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_InputOutputSpecification278"):
                opp_val = getattr(value, "bpmn2_InputOutputSpecification278", None)
                setattr(value, "bpmn2_InputOutputSpecification278", self)

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
                if hasattr(item, "bpmn2_Property282"):
                    opp_val = getattr(item, "bpmn2_Property282", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Property282", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Property282"):
                    opp_val = getattr(item, "bpmn2_Property282", None)
                    
                    setattr(item, "bpmn2_Property282", self)
                    

    @property
    def bpmn2_Activity287(self):
        return self.__bpmn2_Activity287

    @bpmn2_Activity287.setter
    def bpmn2_Activity287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity287", None)
        self.__bpmn2_Activity287 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_DataOutputAssociation288"):
                    opp_val = getattr(item, "bpmn2_DataOutputAssociation288", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_DataOutputAssociation288", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_DataOutputAssociation288"):
                    opp_val = getattr(item, "bpmn2_DataOutputAssociation288", None)
                    
                    setattr(item, "bpmn2_DataOutputAssociation288", self)
                    

    @property
    def bpmn2_Activity311(self):
        return self.__bpmn2_Activity311

    @bpmn2_Activity311.setter
    def bpmn2_Activity311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity311", None)
        self.__bpmn2_Activity311 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Position"):
                    opp_val = getattr(item, "bpmn2_Position", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Position", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Position"):
                    opp_val = getattr(item, "bpmn2_Position", None)
                    
                    setattr(item, "bpmn2_Position", self)
                    

    @property
    def bpmn2_Activity305(self):
        return self.__bpmn2_Activity305

    @bpmn2_Activity305.setter
    def bpmn2_Activity305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity305", None)
        self.__bpmn2_Activity305 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_OrganisationalUnit306"):
                    opp_val = getattr(item, "bpmn2_OrganisationalUnit306", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_OrganisationalUnit306", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_OrganisationalUnit306"):
                    opp_val = getattr(item, "bpmn2_OrganisationalUnit306", None)
                    
                    setattr(item, "bpmn2_OrganisationalUnit306", self)
                    

    @property
    def bpmn2_Activity296(self):
        return self.__bpmn2_Activity296

    @bpmn2_Activity296.setter
    def bpmn2_Activity296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity296", None)
        self.__bpmn2_Activity296 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_SequenceFlow297"):
                opp_val = getattr(old_value, "bpmn2_SequenceFlow297", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_SequenceFlow297", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_SequenceFlow297"):
                opp_val = getattr(value, "bpmn2_SequenceFlow297", None)
                setattr(value, "bpmn2_SequenceFlow297", self)

    @property
    def bpmn2_Activity308(self):
        return self.__bpmn2_Activity308

    @bpmn2_Activity308.setter
    def bpmn2_Activity308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity308", None)
        self.__bpmn2_Activity308 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Performer309"):
                    opp_val = getattr(item, "bpmn2_Performer309", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Performer309", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Performer309"):
                    opp_val = getattr(item, "bpmn2_Performer309", None)
                    
                    setattr(item, "bpmn2_Performer309", self)
                    

    @property
    def bpmn2_Activity299(self):
        return self.__bpmn2_Activity299

    @bpmn2_Activity299.setter
    def bpmn2_Activity299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity299", None)
        self.__bpmn2_Activity299 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Competency"):
                    opp_val = getattr(item, "bpmn2_Competency", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Competency", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Competency"):
                    opp_val = getattr(item, "bpmn2_Competency", None)
                    
                    setattr(item, "bpmn2_Competency", self)
                    

    @property
    def bpmn2_Activity303(self):
        return self.__bpmn2_Activity303

    @bpmn2_Activity303.setter
    def bpmn2_Activity303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity303", None)
        self.__bpmn2_Activity303 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_OrganisationalUnit"):
                    opp_val = getattr(item, "bpmn2_OrganisationalUnit", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_OrganisationalUnit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_OrganisationalUnit"):
                    opp_val = getattr(item, "bpmn2_OrganisationalUnit", None)
                    
                    setattr(item, "bpmn2_OrganisationalUnit", self)
                    

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
                if hasattr(item, "bpmn2_DataInputAssociation285"):
                    opp_val = getattr(item, "bpmn2_DataInputAssociation285", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_DataInputAssociation285", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_DataInputAssociation285"):
                    opp_val = getattr(item, "bpmn2_DataInputAssociation285", None)
                    
                    setattr(item, "bpmn2_DataInputAssociation285", self)
                    

    @property
    def bpmn2_Activity290(self):
        return self.__bpmn2_Activity290

    @bpmn2_Activity290.setter
    def bpmn2_Activity290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity290", None)
        self.__bpmn2_Activity290 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_ResourceRole291"):
                    opp_val = getattr(item, "bpmn2_ResourceRole291", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_ResourceRole291", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_ResourceRole291"):
                    opp_val = getattr(item, "bpmn2_ResourceRole291", None)
                    
                    setattr(item, "bpmn2_ResourceRole291", self)
                    

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
    def bpmn2_Activity301(self):
        return self.__bpmn2_Activity301

    @bpmn2_Activity301.setter
    def bpmn2_Activity301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity301", None)
        self.__bpmn2_Activity301 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Criterion"):
                    opp_val = getattr(item, "bpmn2_Criterion", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Criterion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Criterion"):
                    opp_val = getattr(item, "bpmn2_Criterion", None)
                    
                    setattr(item, "bpmn2_Criterion", self)
                    

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
    def bpmn2_Activity(self):
        return self.__bpmn2_Activity

    @bpmn2_Activity.setter
    def bpmn2_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity", None)
        self.__bpmn2_Activity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_DocumentRoot5"):
                opp_val = getattr(old_value, "bpmn2_DocumentRoot5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_DocumentRoot5"):
                opp_val = getattr(value, "bpmn2_DocumentRoot5", None)
                if opp_val is None:
                    setattr(value, "bpmn2_DocumentRoot5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bpmn2_Activity293(self):
        return self.__bpmn2_Activity293

    @bpmn2_Activity293.setter
    def bpmn2_Activity293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity293", None)
        self.__bpmn2_Activity293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bpmn2_LoopCharacteristics294"):
                opp_val = getattr(old_value, "bpmn2_LoopCharacteristics294", None)
                if opp_val == self:
                    setattr(old_value, "bpmn2_LoopCharacteristics294", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bpmn2_LoopCharacteristics294"):
                opp_val = getattr(value, "bpmn2_LoopCharacteristics294", None)
                setattr(value, "bpmn2_LoopCharacteristics294", self)

    @property
    def bpmn2_Activity315(self):
        return self.__bpmn2_Activity315

    @bpmn2_Activity315.setter
    def bpmn2_Activity315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_Activity__bpmn2_Activity315", None)
        self.__bpmn2_Activity315 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_Competency316"):
                    opp_val = getattr(item, "bpmn2_Competency316", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_Competency316", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_Competency316"):
                    opp_val = getattr(item, "bpmn2_Competency316", None)
                    
                    setattr(item, "bpmn2_Competency316", self)
                    

class bpmn2_EStringToStringMapEntry:

    pass
class bpmn2_DocumentRoot:

    pass