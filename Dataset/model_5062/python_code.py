from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class MultiInstanceBehavior(Enum):
    None = "None"
    One = "One"
    All = "All"
    Complex = "Complex"
class ItemKind(Enum):
    Physical = "Physical"
    Information = "Information"
class AdHocOrdering(Enum):
    Parallel = "Parallel"
    Sequential = "Sequential"
class RelationshipDirection(Enum):
    None = "None"
    Forward = "Forward"
    Backward = "Backward"
    Both = "Both"
class EventBasedGatewayType(Enum):
    Parallel = "Parallel"
    Exclusive = "Exclusive"
class GatewayDirection(Enum):
    Unspecified = "Unspecified"
    Converging = "Converging"
    Diverging = "Diverging"
    Mixed = "Mixed"
class AssociationDirection(Enum):
    None = "None"
    One = "One"
    Both = "Both"
class ChoreographyLoopType(Enum):
    None = "None"
    Standard = "Standard"
    MultiInstanceSequential = "MultiInstanceSequential"
    MultiInstanceParallel = "MultiInstanceParallel"
class ProcessType(Enum):
    None = "None"
    Public = "Public"
    Private = "Private"


############################################
# Definition of Classes
############################################

class EObject:

    pass
class BPMN2Model_BPMNBase(EObject):

    pass
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
class ThrowEvent:

    pass
class FlowElement:

    pass
class DataAssociation:

    pass
class ItemAwareElement:

    pass
class InteractionNode:

    pass
class Gateway:

    pass
class FlowElementsContainer:

    pass
class Collaboration:

    pass
class Event:

    pass
class EventDefinition:

    pass
class RootElement:

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
class Artifact:

    pass
class BaseElement:

    pass
class BPMN2Model_FlowElementsContainer(BaseElement):

    pass
class BPMN2Model_ItemAwareElement(BaseElement):

    pass
class SubProcess:

    pass
class FlowNode:

    pass
class BPMN2Model_UserTask(Task):

    def __init__(self, implementation: str, BPMN2Model_UserTask: "BPMN2Model_DocumentRoot" = None, BPMN2Model_UserTask865: set["BPMN2Model_Rendering"] = None):
        self.implementation = implementation
        self.BPMN2Model_UserTask = BPMN2Model_UserTask
        self.BPMN2Model_UserTask865 = BPMN2Model_UserTask865 if BPMN2Model_UserTask865 is not None else set()
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def BPMN2Model_UserTask(self):
        return self.__BPMN2Model_UserTask

    @BPMN2Model_UserTask.setter
    def BPMN2Model_UserTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_UserTask__BPMN2Model_UserTask", None)
        self.__BPMN2Model_UserTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot275"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot275", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot275"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot275", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot275", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_UserTask865(self):
        return self.__BPMN2Model_UserTask865

    @BPMN2Model_UserTask865.setter
    def BPMN2Model_UserTask865(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_UserTask__BPMN2Model_UserTask865", None)
        self.__BPMN2Model_UserTask865 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Rendering866"):
                    opp_val = getattr(item, "BPMN2Model_Rendering866", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Rendering866", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Rendering866"):
                    opp_val = getattr(item, "BPMN2Model_Rendering866", None)
                    
                    setattr(item, "BPMN2Model_Rendering866", self)
                    

class BPMN2Model_Transaction(SubProcess):

    def __init__(self, protocol: str, method: str, BPMN2Model_Transaction: "BPMN2Model_DocumentRoot" = None):
        self.protocol = protocol
        self.method = method
        self.BPMN2Model_Transaction = BPMN2Model_Transaction
        
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

    @property
    def BPMN2Model_Transaction(self):
        return self.__BPMN2Model_Transaction

    @BPMN2Model_Transaction.setter
    def BPMN2Model_Transaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Transaction__BPMN2Model_Transaction", None)
        self.__BPMN2Model_Transaction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot273"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot273", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot273"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot273", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot273", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_TimerEventDefinition(EventDefinition):

    pass
class BPMN2Model_ThrowEvent(Event):

    pass
class BPMN2Model_TextAnnotation(Artifact):

    def __init__(self, text: str, textFormat: str, BPMN2Model_TextAnnotation: "BPMN2Model_DocumentRoot" = None):
        self.text = text
        self.textFormat = textFormat
        self.BPMN2Model_TextAnnotation = BPMN2Model_TextAnnotation
        
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
    def BPMN2Model_TextAnnotation(self):
        return self.__BPMN2Model_TextAnnotation

    @BPMN2Model_TextAnnotation.setter
    def BPMN2Model_TextAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_TextAnnotation__BPMN2Model_TextAnnotation", None)
        self.__BPMN2Model_TextAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot267"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot267", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot267"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot267", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot267", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_TerminateEventDefinition(EventDefinition):

    pass
class BPMN2Model_Task(Activity, InteractionNode):

    pass
class BPMN2Model_SubProcess(Activity, FlowElementsContainer):

    def __init__(self, triggeredByEvent: bool, BPMN2Model_SubProcess: "BPMN2Model_DocumentRoot" = None, BPMN2Model_SubProcess838: set["BPMN2Model_Artifact"] = None):
        self.triggeredByEvent = triggeredByEvent
        self.BPMN2Model_SubProcess = BPMN2Model_SubProcess
        self.BPMN2Model_SubProcess838 = BPMN2Model_SubProcess838 if BPMN2Model_SubProcess838 is not None else set()
        
    @property
    def triggeredByEvent(self) -> bool:
        return self.__triggeredByEvent

    @triggeredByEvent.setter
    def triggeredByEvent(self, triggeredByEvent: bool):
        self.__triggeredByEvent = triggeredByEvent

    @property
    def BPMN2Model_SubProcess(self):
        return self.__BPMN2Model_SubProcess

    @BPMN2Model_SubProcess.setter
    def BPMN2Model_SubProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_SubProcess__BPMN2Model_SubProcess", None)
        self.__BPMN2Model_SubProcess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot258"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot258", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot258"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot258", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot258", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_SubProcess838(self):
        return self.__BPMN2Model_SubProcess838

    @BPMN2Model_SubProcess838.setter
    def BPMN2Model_SubProcess838(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_SubProcess__BPMN2Model_SubProcess838", None)
        self.__BPMN2Model_SubProcess838 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Artifact839"):
                    opp_val = getattr(item, "BPMN2Model_Artifact839", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Artifact839", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Artifact839"):
                    opp_val = getattr(item, "BPMN2Model_Artifact839", None)
                    
                    setattr(item, "BPMN2Model_Artifact839", self)
                    

class BPMN2Model_SubConversation(ConversationNode):

    pass
class BPMN2Model_SubChoreography(FlowElementsContainer, ChoreographyActivity):

    pass
class BPMN2Model_ResourceParameter(BaseElement):

    def __init__(self, isRequired: bool, name: str, BPMN2Model_ResourceParameter: "BPMN2Model_DocumentRoot" = None, BPMN2Model_ResourceParameter781: "BPMN2Model_Resource" = None, BPMN2Model_ResourceParameter786: "BPMN2Model_ItemDefinition" = None, BPMN2Model_ResourceParameter793: "BPMN2Model_ResourceParameterBinding" = None):
        self.isRequired = isRequired
        self.name = name
        self.BPMN2Model_ResourceParameter = BPMN2Model_ResourceParameter
        self.BPMN2Model_ResourceParameter781 = BPMN2Model_ResourceParameter781
        self.BPMN2Model_ResourceParameter786 = BPMN2Model_ResourceParameter786
        self.BPMN2Model_ResourceParameter793 = BPMN2Model_ResourceParameter793
        
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
    def BPMN2Model_ResourceParameter786(self):
        return self.__BPMN2Model_ResourceParameter786

    @BPMN2Model_ResourceParameter786.setter
    def BPMN2Model_ResourceParameter786(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ResourceParameter__BPMN2Model_ResourceParameter786", None)
        self.__BPMN2Model_ResourceParameter786 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ItemDefinition787"):
                opp_val = getattr(old_value, "BPMN2Model_ItemDefinition787", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ItemDefinition787", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ItemDefinition787"):
                opp_val = getattr(value, "BPMN2Model_ItemDefinition787", None)
                setattr(value, "BPMN2Model_ItemDefinition787", self)

    @property
    def BPMN2Model_ResourceParameter(self):
        return self.__BPMN2Model_ResourceParameter

    @BPMN2Model_ResourceParameter.setter
    def BPMN2Model_ResourceParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ResourceParameter__BPMN2Model_ResourceParameter", None)
        self.__BPMN2Model_ResourceParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot232"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot232", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot232"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot232", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot232", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_ResourceParameter793(self):
        return self.__BPMN2Model_ResourceParameter793

    @BPMN2Model_ResourceParameter793.setter
    def BPMN2Model_ResourceParameter793(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ResourceParameter__BPMN2Model_ResourceParameter793", None)
        self.__BPMN2Model_ResourceParameter793 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ResourceParameterBinding792"):
                opp_val = getattr(old_value, "BPMN2Model_ResourceParameterBinding792", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ResourceParameterBinding792", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ResourceParameterBinding792"):
                opp_val = getattr(value, "BPMN2Model_ResourceParameterBinding792", None)
                setattr(value, "BPMN2Model_ResourceParameterBinding792", self)

    @property
    def BPMN2Model_ResourceParameter781(self):
        return self.__BPMN2Model_ResourceParameter781

    @BPMN2Model_ResourceParameter781.setter
    def BPMN2Model_ResourceParameter781(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ResourceParameter__BPMN2Model_ResourceParameter781", None)
        self.__BPMN2Model_ResourceParameter781 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Resource780"):
                opp_val = getattr(old_value, "BPMN2Model_Resource780", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Resource780"):
                opp_val = getattr(value, "BPMN2Model_Resource780", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_Resource780", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_StartEvent(CatchEvent):

    def __init__(self, isInterrupting: bool, BPMN2Model_StartEvent: "BPMN2Model_DocumentRoot" = None):
        self.isInterrupting = isInterrupting
        self.BPMN2Model_StartEvent = BPMN2Model_StartEvent
        
    @property
    def isInterrupting(self) -> bool:
        return self.__isInterrupting

    @isInterrupting.setter
    def isInterrupting(self, isInterrupting: bool):
        self.__isInterrupting = isInterrupting

    @property
    def BPMN2Model_StartEvent(self):
        return self.__BPMN2Model_StartEvent

    @BPMN2Model_StartEvent.setter
    def BPMN2Model_StartEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_StartEvent__BPMN2Model_StartEvent", None)
        self.__BPMN2Model_StartEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot252"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot252", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot252"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot252", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot252", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_StandardLoopCharacteristics(LoopCharacteristics):

    def __init__(self, testBefore: bool, BPMN2Model_StandardLoopCharacteristics: "BPMN2Model_DocumentRoot" = None, BPMN2Model_StandardLoopCharacteristics826: "BPMN2Model_Expression" = None, BPMN2Model_StandardLoopCharacteristics829: "BPMN2Model_Expression" = None):
        self.testBefore = testBefore
        self.BPMN2Model_StandardLoopCharacteristics = BPMN2Model_StandardLoopCharacteristics
        self.BPMN2Model_StandardLoopCharacteristics826 = BPMN2Model_StandardLoopCharacteristics826
        self.BPMN2Model_StandardLoopCharacteristics829 = BPMN2Model_StandardLoopCharacteristics829
        
    @property
    def testBefore(self) -> bool:
        return self.__testBefore

    @testBefore.setter
    def testBefore(self, testBefore: bool):
        self.__testBefore = testBefore

    @property
    def BPMN2Model_StandardLoopCharacteristics826(self):
        return self.__BPMN2Model_StandardLoopCharacteristics826

    @BPMN2Model_StandardLoopCharacteristics826.setter
    def BPMN2Model_StandardLoopCharacteristics826(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_StandardLoopCharacteristics__BPMN2Model_StandardLoopCharacteristics826", None)
        self.__BPMN2Model_StandardLoopCharacteristics826 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Expression827"):
                opp_val = getattr(old_value, "BPMN2Model_Expression827", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Expression827", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Expression827"):
                opp_val = getattr(value, "BPMN2Model_Expression827", None)
                setattr(value, "BPMN2Model_Expression827", self)

    @property
    def BPMN2Model_StandardLoopCharacteristics(self):
        return self.__BPMN2Model_StandardLoopCharacteristics

    @BPMN2Model_StandardLoopCharacteristics.setter
    def BPMN2Model_StandardLoopCharacteristics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_StandardLoopCharacteristics__BPMN2Model_StandardLoopCharacteristics", None)
        self.__BPMN2Model_StandardLoopCharacteristics = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot250"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot250", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot250"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot250", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot250", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_StandardLoopCharacteristics829(self):
        return self.__BPMN2Model_StandardLoopCharacteristics829

    @BPMN2Model_StandardLoopCharacteristics829.setter
    def BPMN2Model_StandardLoopCharacteristics829(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_StandardLoopCharacteristics__BPMN2Model_StandardLoopCharacteristics829", None)
        self.__BPMN2Model_StandardLoopCharacteristics829 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Expression830"):
                opp_val = getattr(old_value, "BPMN2Model_Expression830", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Expression830", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Expression830"):
                opp_val = getattr(value, "BPMN2Model_Expression830", None)
                setattr(value, "BPMN2Model_Expression830", self)

class BPMN2Model_SignalEventDefinition(EventDefinition):

    pass
class BPMN2Model_Signal(RootElement):

    def __init__(self, name: str, BPMN2Model_Signal: "BPMN2Model_DocumentRoot" = None, BPMN2Model_Signal820: "BPMN2Model_ItemDefinition" = None, BPMN2Model_Signal824: "BPMN2Model_SignalEventDefinition" = None):
        self.name = name
        self.BPMN2Model_Signal = BPMN2Model_Signal
        self.BPMN2Model_Signal820 = BPMN2Model_Signal820
        self.BPMN2Model_Signal824 = BPMN2Model_Signal824
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_Signal824(self):
        return self.__BPMN2Model_Signal824

    @BPMN2Model_Signal824.setter
    def BPMN2Model_Signal824(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Signal__BPMN2Model_Signal824", None)
        self.__BPMN2Model_Signal824 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_SignalEventDefinition823"):
                opp_val = getattr(old_value, "BPMN2Model_SignalEventDefinition823", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_SignalEventDefinition823", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_SignalEventDefinition823"):
                opp_val = getattr(value, "BPMN2Model_SignalEventDefinition823", None)
                setattr(value, "BPMN2Model_SignalEventDefinition823", self)

    @property
    def BPMN2Model_Signal820(self):
        return self.__BPMN2Model_Signal820

    @BPMN2Model_Signal820.setter
    def BPMN2Model_Signal820(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Signal__BPMN2Model_Signal820", None)
        self.__BPMN2Model_Signal820 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ItemDefinition821"):
                opp_val = getattr(old_value, "BPMN2Model_ItemDefinition821", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ItemDefinition821", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ItemDefinition821"):
                opp_val = getattr(value, "BPMN2Model_ItemDefinition821", None)
                setattr(value, "BPMN2Model_ItemDefinition821", self)

    @property
    def BPMN2Model_Signal(self):
        return self.__BPMN2Model_Signal

    @BPMN2Model_Signal.setter
    def BPMN2Model_Signal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Signal__BPMN2Model_Signal", None)
        self.__BPMN2Model_Signal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot246"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot246", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot246"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot246", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot246", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_ServiceTask(Task):

    def __init__(self, implementation: str, BPMN2Model_ServiceTask: "BPMN2Model_DocumentRoot" = None, BPMN2Model_ServiceTask817: "BPMN2Model_Operation" = None):
        self.implementation = implementation
        self.BPMN2Model_ServiceTask = BPMN2Model_ServiceTask
        self.BPMN2Model_ServiceTask817 = BPMN2Model_ServiceTask817
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def BPMN2Model_ServiceTask817(self):
        return self.__BPMN2Model_ServiceTask817

    @BPMN2Model_ServiceTask817.setter
    def BPMN2Model_ServiceTask817(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ServiceTask__BPMN2Model_ServiceTask817", None)
        self.__BPMN2Model_ServiceTask817 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Operation818"):
                opp_val = getattr(old_value, "BPMN2Model_Operation818", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Operation818", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Operation818"):
                opp_val = getattr(value, "BPMN2Model_Operation818", None)
                setattr(value, "BPMN2Model_Operation818", self)

    @property
    def BPMN2Model_ServiceTask(self):
        return self.__BPMN2Model_ServiceTask

    @BPMN2Model_ServiceTask.setter
    def BPMN2Model_ServiceTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ServiceTask__BPMN2Model_ServiceTask", None)
        self.__BPMN2Model_ServiceTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot244"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot244", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot244"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot244", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot244", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_SequenceFlow(FlowElement):

    def __init__(self, isImmediate: bool, BPMN2Model_SequenceFlow: "BPMN2Model_DocumentRoot" = None, BPMN2Model_SequenceFlow297: "BPMN2Model_Activity" = None, BPMN2Model_SequenceFlow423: "BPMN2Model_ComplexGateway" = None, BPMN2Model_SequenceFlow530: "BPMN2Model_ExclusiveGateway" = None, SequenceFlow: "BPMN2Model_FlowNode" = None, SequenceFlow558: "BPMN2Model_FlowNode" = None, BPMN2Model_SequenceFlow576: "BPMN2Model_InclusiveGateway" = None, BPMN2Model_SequenceFlow810: "BPMN2Model_Expression" = None, outgoing: "BPMN2Model_FlowNode" = None, incoming: "BPMN2Model_FlowNode" = None):
        self.isImmediate = isImmediate
        self.BPMN2Model_SequenceFlow = BPMN2Model_SequenceFlow
        self.BPMN2Model_SequenceFlow297 = BPMN2Model_SequenceFlow297
        self.BPMN2Model_SequenceFlow423 = BPMN2Model_SequenceFlow423
        self.BPMN2Model_SequenceFlow530 = BPMN2Model_SequenceFlow530
        self.SequenceFlow = SequenceFlow
        self.SequenceFlow558 = SequenceFlow558
        self.BPMN2Model_SequenceFlow576 = BPMN2Model_SequenceFlow576
        self.BPMN2Model_SequenceFlow810 = BPMN2Model_SequenceFlow810
        self.outgoing = outgoing
        self.incoming = incoming
        
    @property
    def isImmediate(self) -> bool:
        return self.__isImmediate

    @isImmediate.setter
    def isImmediate(self, isImmediate: bool):
        self.__isImmediate = isImmediate

    @property
    def SequenceFlow558(self):
        return self.__SequenceFlow558

    @SequenceFlow558.setter
    def SequenceFlow558(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_SequenceFlow__SequenceFlow558", None)
        self.__SequenceFlow558 = value
        
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
    def BPMN2Model_SequenceFlow576(self):
        return self.__BPMN2Model_SequenceFlow576

    @BPMN2Model_SequenceFlow576.setter
    def BPMN2Model_SequenceFlow576(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_SequenceFlow__BPMN2Model_SequenceFlow576", None)
        self.__BPMN2Model_SequenceFlow576 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_InclusiveGateway575"):
                opp_val = getattr(old_value, "BPMN2Model_InclusiveGateway575", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_InclusiveGateway575", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_InclusiveGateway575"):
                opp_val = getattr(value, "BPMN2Model_InclusiveGateway575", None)
                setattr(value, "BPMN2Model_InclusiveGateway575", self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_SequenceFlow__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FlowNode815"):
                opp_val = getattr(old_value, "FlowNode815", None)
                if opp_val == self:
                    setattr(old_value, "FlowNode815", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowNode815"):
                opp_val = getattr(value, "FlowNode815", None)
                setattr(value, "FlowNode815", self)

    @property
    def BPMN2Model_SequenceFlow423(self):
        return self.__BPMN2Model_SequenceFlow423

    @BPMN2Model_SequenceFlow423.setter
    def BPMN2Model_SequenceFlow423(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_SequenceFlow__BPMN2Model_SequenceFlow423", None)
        self.__BPMN2Model_SequenceFlow423 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ComplexGateway422"):
                opp_val = getattr(old_value, "BPMN2Model_ComplexGateway422", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ComplexGateway422", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ComplexGateway422"):
                opp_val = getattr(value, "BPMN2Model_ComplexGateway422", None)
                setattr(value, "BPMN2Model_ComplexGateway422", self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_SequenceFlow__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FlowNode813"):
                opp_val = getattr(old_value, "FlowNode813", None)
                if opp_val == self:
                    setattr(old_value, "FlowNode813", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowNode813"):
                opp_val = getattr(value, "FlowNode813", None)
                setattr(value, "FlowNode813", self)

    @property
    def BPMN2Model_SequenceFlow530(self):
        return self.__BPMN2Model_SequenceFlow530

    @BPMN2Model_SequenceFlow530.setter
    def BPMN2Model_SequenceFlow530(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_SequenceFlow__BPMN2Model_SequenceFlow530", None)
        self.__BPMN2Model_SequenceFlow530 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ExclusiveGateway529"):
                opp_val = getattr(old_value, "BPMN2Model_ExclusiveGateway529", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ExclusiveGateway529", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ExclusiveGateway529"):
                opp_val = getattr(value, "BPMN2Model_ExclusiveGateway529", None)
                setattr(value, "BPMN2Model_ExclusiveGateway529", self)

    @property
    def BPMN2Model_SequenceFlow(self):
        return self.__BPMN2Model_SequenceFlow

    @BPMN2Model_SequenceFlow.setter
    def BPMN2Model_SequenceFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_SequenceFlow__BPMN2Model_SequenceFlow", None)
        self.__BPMN2Model_SequenceFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot242"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot242", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot242"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot242", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot242", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_SequenceFlow297(self):
        return self.__BPMN2Model_SequenceFlow297

    @BPMN2Model_SequenceFlow297.setter
    def BPMN2Model_SequenceFlow297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_SequenceFlow__BPMN2Model_SequenceFlow297", None)
        self.__BPMN2Model_SequenceFlow297 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Activity296"):
                opp_val = getattr(old_value, "BPMN2Model_Activity296", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Activity296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Activity296"):
                opp_val = getattr(value, "BPMN2Model_Activity296", None)
                setattr(value, "BPMN2Model_Activity296", self)

    @property
    def SequenceFlow(self):
        return self.__SequenceFlow

    @SequenceFlow.setter
    def SequenceFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_SequenceFlow__SequenceFlow", None)
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

    @property
    def BPMN2Model_SequenceFlow810(self):
        return self.__BPMN2Model_SequenceFlow810

    @BPMN2Model_SequenceFlow810.setter
    def BPMN2Model_SequenceFlow810(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_SequenceFlow__BPMN2Model_SequenceFlow810", None)
        self.__BPMN2Model_SequenceFlow810 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Expression811"):
                opp_val = getattr(old_value, "BPMN2Model_Expression811", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Expression811", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Expression811"):
                opp_val = getattr(value, "BPMN2Model_Expression811", None)
                setattr(value, "BPMN2Model_Expression811", self)

class BPMN2Model_SendTask(Task):

    def __init__(self, implementation: str, BPMN2Model_SendTask: "BPMN2Model_DocumentRoot" = None, BPMN2Model_SendTask804: "BPMN2Model_Message" = None, BPMN2Model_SendTask807: "BPMN2Model_Operation" = None):
        self.implementation = implementation
        self.BPMN2Model_SendTask = BPMN2Model_SendTask
        self.BPMN2Model_SendTask804 = BPMN2Model_SendTask804
        self.BPMN2Model_SendTask807 = BPMN2Model_SendTask807
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def BPMN2Model_SendTask804(self):
        return self.__BPMN2Model_SendTask804

    @BPMN2Model_SendTask804.setter
    def BPMN2Model_SendTask804(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_SendTask__BPMN2Model_SendTask804", None)
        self.__BPMN2Model_SendTask804 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Message805"):
                opp_val = getattr(old_value, "BPMN2Model_Message805", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Message805", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Message805"):
                opp_val = getattr(value, "BPMN2Model_Message805", None)
                setattr(value, "BPMN2Model_Message805", self)

    @property
    def BPMN2Model_SendTask(self):
        return self.__BPMN2Model_SendTask

    @BPMN2Model_SendTask.setter
    def BPMN2Model_SendTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_SendTask__BPMN2Model_SendTask", None)
        self.__BPMN2Model_SendTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot240"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot240", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot240"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot240", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot240", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_SendTask807(self):
        return self.__BPMN2Model_SendTask807

    @BPMN2Model_SendTask807.setter
    def BPMN2Model_SendTask807(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_SendTask__BPMN2Model_SendTask807", None)
        self.__BPMN2Model_SendTask807 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Operation808"):
                opp_val = getattr(old_value, "BPMN2Model_Operation808", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Operation808", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Operation808"):
                opp_val = getattr(value, "BPMN2Model_Operation808", None)
                setattr(value, "BPMN2Model_Operation808", self)

class BPMN2Model_ScriptTask(Task):

    def __init__(self, script: str, scriptFormat: str, BPMN2Model_ScriptTask: "BPMN2Model_DocumentRoot" = None):
        self.script = script
        self.scriptFormat = scriptFormat
        self.BPMN2Model_ScriptTask = BPMN2Model_ScriptTask
        
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
    def BPMN2Model_ScriptTask(self):
        return self.__BPMN2Model_ScriptTask

    @BPMN2Model_ScriptTask.setter
    def BPMN2Model_ScriptTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ScriptTask__BPMN2Model_ScriptTask", None)
        self.__BPMN2Model_ScriptTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot238"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot238", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot238"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot238", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot238", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_EObject:

    pass
class BPMN2Model_Resource(RootElement):

    def __init__(self, name: str, BPMN2Model_Resource: "BPMN2Model_DocumentRoot" = None, BPMN2Model_Resource780: set["BPMN2Model_ResourceParameter"] = None, BPMN2Model_Resource796: "BPMN2Model_ResourceRole" = None):
        self.name = name
        self.BPMN2Model_Resource = BPMN2Model_Resource
        self.BPMN2Model_Resource780 = BPMN2Model_Resource780 if BPMN2Model_Resource780 is not None else set()
        self.BPMN2Model_Resource796 = BPMN2Model_Resource796
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_Resource780(self):
        return self.__BPMN2Model_Resource780

    @BPMN2Model_Resource780.setter
    def BPMN2Model_Resource780(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Resource__BPMN2Model_Resource780", None)
        self.__BPMN2Model_Resource780 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ResourceParameter781"):
                    opp_val = getattr(item, "BPMN2Model_ResourceParameter781", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ResourceParameter781", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ResourceParameter781"):
                    opp_val = getattr(item, "BPMN2Model_ResourceParameter781", None)
                    
                    setattr(item, "BPMN2Model_ResourceParameter781", self)
                    

    @property
    def BPMN2Model_Resource796(self):
        return self.__BPMN2Model_Resource796

    @BPMN2Model_Resource796.setter
    def BPMN2Model_Resource796(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Resource__BPMN2Model_Resource796", None)
        self.__BPMN2Model_Resource796 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ResourceRole795"):
                opp_val = getattr(old_value, "BPMN2Model_ResourceRole795", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ResourceRole795", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ResourceRole795"):
                opp_val = getattr(value, "BPMN2Model_ResourceRole795", None)
                setattr(value, "BPMN2Model_ResourceRole795", self)

    @property
    def BPMN2Model_Resource(self):
        return self.__BPMN2Model_Resource

    @BPMN2Model_Resource.setter
    def BPMN2Model_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Resource__BPMN2Model_Resource", None)
        self.__BPMN2Model_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot228"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot228", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot228"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot228", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot228", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_Rendering(BaseElement):

    pass
class BPMN2Model_Relationship(BaseElement):

    def __init__(self, direction: str, type: str, BPMN2Model_Relationship: "BPMN2Model_DocumentRoot" = None, BPMN2Model_Relationship512: "BPMN2Model_Definitions" = None, BPMN2Model_Relationship774: set["BPMN2Model_EObject"] = None, BPMN2Model_Relationship777: set["BPMN2Model_EObject"] = None):
        self.direction = direction
        self.type = type
        self.BPMN2Model_Relationship = BPMN2Model_Relationship
        self.BPMN2Model_Relationship512 = BPMN2Model_Relationship512
        self.BPMN2Model_Relationship774 = BPMN2Model_Relationship774 if BPMN2Model_Relationship774 is not None else set()
        self.BPMN2Model_Relationship777 = BPMN2Model_Relationship777 if BPMN2Model_Relationship777 is not None else set()
        
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
    def BPMN2Model_Relationship512(self):
        return self.__BPMN2Model_Relationship512

    @BPMN2Model_Relationship512.setter
    def BPMN2Model_Relationship512(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Relationship__BPMN2Model_Relationship512", None)
        self.__BPMN2Model_Relationship512 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Definitions511"):
                opp_val = getattr(old_value, "BPMN2Model_Definitions511", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Definitions511"):
                opp_val = getattr(value, "BPMN2Model_Definitions511", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_Definitions511", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Relationship777(self):
        return self.__BPMN2Model_Relationship777

    @BPMN2Model_Relationship777.setter
    def BPMN2Model_Relationship777(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Relationship__BPMN2Model_Relationship777", None)
        self.__BPMN2Model_Relationship777 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_EObject778"):
                    opp_val = getattr(item, "BPMN2Model_EObject778", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_EObject778", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_EObject778"):
                    opp_val = getattr(item, "BPMN2Model_EObject778", None)
                    
                    setattr(item, "BPMN2Model_EObject778", self)
                    

    @property
    def BPMN2Model_Relationship774(self):
        return self.__BPMN2Model_Relationship774

    @BPMN2Model_Relationship774.setter
    def BPMN2Model_Relationship774(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Relationship__BPMN2Model_Relationship774", None)
        self.__BPMN2Model_Relationship774 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_EObject775"):
                    opp_val = getattr(item, "BPMN2Model_EObject775", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_EObject775", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_EObject775"):
                    opp_val = getattr(item, "BPMN2Model_EObject775", None)
                    
                    setattr(item, "BPMN2Model_EObject775", self)
                    

    @property
    def BPMN2Model_Relationship(self):
        return self.__BPMN2Model_Relationship

    @BPMN2Model_Relationship.setter
    def BPMN2Model_Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Relationship__BPMN2Model_Relationship", None)
        self.__BPMN2Model_Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot224"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot224", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot224"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot224", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot224", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_ReceiveTask(Task):

    def __init__(self, implementation: str, instantiate: bool, BPMN2Model_ReceiveTask: "BPMN2Model_DocumentRoot" = None, BPMN2Model_ReceiveTask768: "BPMN2Model_Message" = None, BPMN2Model_ReceiveTask771: "BPMN2Model_Operation" = None):
        self.implementation = implementation
        self.instantiate = instantiate
        self.BPMN2Model_ReceiveTask = BPMN2Model_ReceiveTask
        self.BPMN2Model_ReceiveTask768 = BPMN2Model_ReceiveTask768
        self.BPMN2Model_ReceiveTask771 = BPMN2Model_ReceiveTask771
        
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
    def BPMN2Model_ReceiveTask(self):
        return self.__BPMN2Model_ReceiveTask

    @BPMN2Model_ReceiveTask.setter
    def BPMN2Model_ReceiveTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ReceiveTask__BPMN2Model_ReceiveTask", None)
        self.__BPMN2Model_ReceiveTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot222"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot222", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot222"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot222", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot222", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_ReceiveTask768(self):
        return self.__BPMN2Model_ReceiveTask768

    @BPMN2Model_ReceiveTask768.setter
    def BPMN2Model_ReceiveTask768(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ReceiveTask__BPMN2Model_ReceiveTask768", None)
        self.__BPMN2Model_ReceiveTask768 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Message769"):
                opp_val = getattr(old_value, "BPMN2Model_Message769", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Message769", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Message769"):
                opp_val = getattr(value, "BPMN2Model_Message769", None)
                setattr(value, "BPMN2Model_Message769", self)

    @property
    def BPMN2Model_ReceiveTask771(self):
        return self.__BPMN2Model_ReceiveTask771

    @BPMN2Model_ReceiveTask771.setter
    def BPMN2Model_ReceiveTask771(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ReceiveTask__BPMN2Model_ReceiveTask771", None)
        self.__BPMN2Model_ReceiveTask771 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Operation772"):
                opp_val = getattr(old_value, "BPMN2Model_Operation772", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Operation772", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Operation772"):
                opp_val = getattr(value, "BPMN2Model_Operation772", None)
                setattr(value, "BPMN2Model_Operation772", self)

class BPMN2Model_Property(ItemAwareElement):

    def __init__(self, name: str, BPMN2Model_Property: "BPMN2Model_DocumentRoot" = None, BPMN2Model_Property282: "BPMN2Model_Activity" = None, BPMN2Model_Property527: "BPMN2Model_Event" = None, BPMN2Model_Property751: "BPMN2Model_Process" = None):
        self.name = name
        self.BPMN2Model_Property = BPMN2Model_Property
        self.BPMN2Model_Property282 = BPMN2Model_Property282
        self.BPMN2Model_Property527 = BPMN2Model_Property527
        self.BPMN2Model_Property751 = BPMN2Model_Property751
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_Property751(self):
        return self.__BPMN2Model_Property751

    @BPMN2Model_Property751.setter
    def BPMN2Model_Property751(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Property__BPMN2Model_Property751", None)
        self.__BPMN2Model_Property751 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Process750"):
                opp_val = getattr(old_value, "BPMN2Model_Process750", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Process750"):
                opp_val = getattr(value, "BPMN2Model_Process750", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_Process750", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Property527(self):
        return self.__BPMN2Model_Property527

    @BPMN2Model_Property527.setter
    def BPMN2Model_Property527(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Property__BPMN2Model_Property527", None)
        self.__BPMN2Model_Property527 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Event526"):
                opp_val = getattr(old_value, "BPMN2Model_Event526", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Event526"):
                opp_val = getattr(value, "BPMN2Model_Event526", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_Event526", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Property(self):
        return self.__BPMN2Model_Property

    @BPMN2Model_Property.setter
    def BPMN2Model_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Property__BPMN2Model_Property", None)
        self.__BPMN2Model_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot220"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot220", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot220"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot220", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot220", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Property282(self):
        return self.__BPMN2Model_Property282

    @BPMN2Model_Property282.setter
    def BPMN2Model_Property282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Property__BPMN2Model_Property282", None)
        self.__BPMN2Model_Property282 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Activity281"):
                opp_val = getattr(old_value, "BPMN2Model_Activity281", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Activity281"):
                opp_val = getattr(value, "BPMN2Model_Activity281", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_Activity281", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_Process(FlowElementsContainer, CallableElement):

    def __init__(self, isClosed: bool, isExecutable: bool, processType: str, BPMN2Model_Process: "BPMN2Model_DocumentRoot" = None, BPMN2Model_Process730: "BPMN2Model_Participant" = None, BPMN2Model_Process744: "BPMN2Model_Auditing" = None, BPMN2Model_Process747: "BPMN2Model_Monitoring" = None, BPMN2Model_Process750: set["BPMN2Model_Property"] = None, BPMN2Model_Process753: set["BPMN2Model_Artifact"] = None, BPMN2Model_Process756: set["BPMN2Model_ResourceRole"] = None, BPMN2Model_Process759: set["BPMN2Model_CorrelationSubscription"] = None, BPMN2Model_Process763: "BPMN2Model_Process" = None, BPMN2Model_Process761: set["BPMN2Model_Process"] = None, BPMN2Model_Process765: "BPMN2Model_Collaboration" = None):
        self.isClosed = isClosed
        self.isExecutable = isExecutable
        self.processType = processType
        self.BPMN2Model_Process = BPMN2Model_Process
        self.BPMN2Model_Process730 = BPMN2Model_Process730
        self.BPMN2Model_Process744 = BPMN2Model_Process744
        self.BPMN2Model_Process747 = BPMN2Model_Process747
        self.BPMN2Model_Process750 = BPMN2Model_Process750 if BPMN2Model_Process750 is not None else set()
        self.BPMN2Model_Process753 = BPMN2Model_Process753 if BPMN2Model_Process753 is not None else set()
        self.BPMN2Model_Process756 = BPMN2Model_Process756 if BPMN2Model_Process756 is not None else set()
        self.BPMN2Model_Process759 = BPMN2Model_Process759 if BPMN2Model_Process759 is not None else set()
        self.BPMN2Model_Process763 = BPMN2Model_Process763
        self.BPMN2Model_Process761 = BPMN2Model_Process761 if BPMN2Model_Process761 is not None else set()
        self.BPMN2Model_Process765 = BPMN2Model_Process765
        
    @property
    def isExecutable(self) -> bool:
        return self.__isExecutable

    @isExecutable.setter
    def isExecutable(self, isExecutable: bool):
        self.__isExecutable = isExecutable

    @property
    def processType(self) -> str:
        return self.__processType

    @processType.setter
    def processType(self, processType: str):
        self.__processType = processType

    @property
    def isClosed(self) -> bool:
        return self.__isClosed

    @isClosed.setter
    def isClosed(self, isClosed: bool):
        self.__isClosed = isClosed

    @property
    def BPMN2Model_Process759(self):
        return self.__BPMN2Model_Process759

    @BPMN2Model_Process759.setter
    def BPMN2Model_Process759(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Process__BPMN2Model_Process759", None)
        self.__BPMN2Model_Process759 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_CorrelationSubscription760"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationSubscription760", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_CorrelationSubscription760", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_CorrelationSubscription760"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationSubscription760", None)
                    
                    setattr(item, "BPMN2Model_CorrelationSubscription760", self)
                    

    @property
    def BPMN2Model_Process747(self):
        return self.__BPMN2Model_Process747

    @BPMN2Model_Process747.setter
    def BPMN2Model_Process747(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Process__BPMN2Model_Process747", None)
        self.__BPMN2Model_Process747 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Monitoring748"):
                opp_val = getattr(old_value, "BPMN2Model_Monitoring748", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Monitoring748", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Monitoring748"):
                opp_val = getattr(value, "BPMN2Model_Monitoring748", None)
                setattr(value, "BPMN2Model_Monitoring748", self)

    @property
    def BPMN2Model_Process761(self):
        return self.__BPMN2Model_Process761

    @BPMN2Model_Process761.setter
    def BPMN2Model_Process761(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Process__BPMN2Model_Process761", None)
        self.__BPMN2Model_Process761 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Process763"):
                    opp_val = getattr(item, "BPMN2Model_Process763", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Process763", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Process763"):
                    opp_val = getattr(item, "BPMN2Model_Process763", None)
                    
                    setattr(item, "BPMN2Model_Process763", self)
                    

    @property
    def BPMN2Model_Process753(self):
        return self.__BPMN2Model_Process753

    @BPMN2Model_Process753.setter
    def BPMN2Model_Process753(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Process__BPMN2Model_Process753", None)
        self.__BPMN2Model_Process753 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Artifact754"):
                    opp_val = getattr(item, "BPMN2Model_Artifact754", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Artifact754", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Artifact754"):
                    opp_val = getattr(item, "BPMN2Model_Artifact754", None)
                    
                    setattr(item, "BPMN2Model_Artifact754", self)
                    

    @property
    def BPMN2Model_Process765(self):
        return self.__BPMN2Model_Process765

    @BPMN2Model_Process765.setter
    def BPMN2Model_Process765(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Process__BPMN2Model_Process765", None)
        self.__BPMN2Model_Process765 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Collaboration766"):
                opp_val = getattr(old_value, "BPMN2Model_Collaboration766", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Collaboration766", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Collaboration766"):
                opp_val = getattr(value, "BPMN2Model_Collaboration766", None)
                setattr(value, "BPMN2Model_Collaboration766", self)

    @property
    def BPMN2Model_Process(self):
        return self.__BPMN2Model_Process

    @BPMN2Model_Process.setter
    def BPMN2Model_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Process__BPMN2Model_Process", None)
        self.__BPMN2Model_Process = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot218"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot218", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot218"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot218", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot218", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Process744(self):
        return self.__BPMN2Model_Process744

    @BPMN2Model_Process744.setter
    def BPMN2Model_Process744(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Process__BPMN2Model_Process744", None)
        self.__BPMN2Model_Process744 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Auditing745"):
                opp_val = getattr(old_value, "BPMN2Model_Auditing745", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Auditing745", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Auditing745"):
                opp_val = getattr(value, "BPMN2Model_Auditing745", None)
                setattr(value, "BPMN2Model_Auditing745", self)

    @property
    def BPMN2Model_Process756(self):
        return self.__BPMN2Model_Process756

    @BPMN2Model_Process756.setter
    def BPMN2Model_Process756(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Process__BPMN2Model_Process756", None)
        self.__BPMN2Model_Process756 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ResourceRole757"):
                    opp_val = getattr(item, "BPMN2Model_ResourceRole757", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ResourceRole757", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ResourceRole757"):
                    opp_val = getattr(item, "BPMN2Model_ResourceRole757", None)
                    
                    setattr(item, "BPMN2Model_ResourceRole757", self)
                    

    @property
    def BPMN2Model_Process763(self):
        return self.__BPMN2Model_Process763

    @BPMN2Model_Process763.setter
    def BPMN2Model_Process763(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Process__BPMN2Model_Process763", None)
        self.__BPMN2Model_Process763 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Process761"):
                opp_val = getattr(old_value, "BPMN2Model_Process761", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Process761"):
                opp_val = getattr(value, "BPMN2Model_Process761", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_Process761", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Process750(self):
        return self.__BPMN2Model_Process750

    @BPMN2Model_Process750.setter
    def BPMN2Model_Process750(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Process__BPMN2Model_Process750", None)
        self.__BPMN2Model_Process750 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Property751"):
                    opp_val = getattr(item, "BPMN2Model_Property751", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Property751", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Property751"):
                    opp_val = getattr(item, "BPMN2Model_Property751", None)
                    
                    setattr(item, "BPMN2Model_Property751", self)
                    

    @property
    def BPMN2Model_Process730(self):
        return self.__BPMN2Model_Process730

    @BPMN2Model_Process730.setter
    def BPMN2Model_Process730(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Process__BPMN2Model_Process730", None)
        self.__BPMN2Model_Process730 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Participant729"):
                opp_val = getattr(old_value, "BPMN2Model_Participant729", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Participant729", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Participant729"):
                opp_val = getattr(value, "BPMN2Model_Participant729", None)
                setattr(value, "BPMN2Model_Participant729", self)

class BPMN2Model_PotentialOwner(HumanPerformer):

    pass
class BPMN2Model_PartnerRole(RootElement):

    def __init__(self, name: str, BPMN2Model_PartnerRole: "BPMN2Model_DocumentRoot" = None, BPMN2Model_PartnerRole741: set["BPMN2Model_Participant"] = None):
        self.name = name
        self.BPMN2Model_PartnerRole = BPMN2Model_PartnerRole
        self.BPMN2Model_PartnerRole741 = BPMN2Model_PartnerRole741 if BPMN2Model_PartnerRole741 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_PartnerRole741(self):
        return self.__BPMN2Model_PartnerRole741

    @BPMN2Model_PartnerRole741.setter
    def BPMN2Model_PartnerRole741(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_PartnerRole__BPMN2Model_PartnerRole741", None)
        self.__BPMN2Model_PartnerRole741 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Participant742"):
                    opp_val = getattr(item, "BPMN2Model_Participant742", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Participant742", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Participant742"):
                    opp_val = getattr(item, "BPMN2Model_Participant742", None)
                    
                    setattr(item, "BPMN2Model_Participant742", self)
                    

    @property
    def BPMN2Model_PartnerRole(self):
        return self.__BPMN2Model_PartnerRole

    @BPMN2Model_PartnerRole.setter
    def BPMN2Model_PartnerRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_PartnerRole__BPMN2Model_PartnerRole", None)
        self.__BPMN2Model_PartnerRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot214"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot214", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot214"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot214", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot214", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_PartnerEntity(RootElement):

    def __init__(self, name: str, BPMN2Model_PartnerEntity: "BPMN2Model_DocumentRoot" = None, BPMN2Model_PartnerEntity738: set["BPMN2Model_Participant"] = None):
        self.name = name
        self.BPMN2Model_PartnerEntity = BPMN2Model_PartnerEntity
        self.BPMN2Model_PartnerEntity738 = BPMN2Model_PartnerEntity738 if BPMN2Model_PartnerEntity738 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_PartnerEntity(self):
        return self.__BPMN2Model_PartnerEntity

    @BPMN2Model_PartnerEntity.setter
    def BPMN2Model_PartnerEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_PartnerEntity__BPMN2Model_PartnerEntity", None)
        self.__BPMN2Model_PartnerEntity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot212"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot212", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot212"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot212", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot212", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_PartnerEntity738(self):
        return self.__BPMN2Model_PartnerEntity738

    @BPMN2Model_PartnerEntity738.setter
    def BPMN2Model_PartnerEntity738(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_PartnerEntity__BPMN2Model_PartnerEntity738", None)
        self.__BPMN2Model_PartnerEntity738 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Participant739"):
                    opp_val = getattr(item, "BPMN2Model_Participant739", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Participant739", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Participant739"):
                    opp_val = getattr(item, "BPMN2Model_Participant739", None)
                    
                    setattr(item, "BPMN2Model_Participant739", self)
                    

class BPMN2Model_ParticipantAssociation(BaseElement):

    pass
class BPMN2Model_Participant(InteractionNode, BaseElement):

    def __init__(self, name: str, BPMN2Model_Participant: "BPMN2Model_DocumentRoot" = None, BPMN2Model_Participant369: "BPMN2Model_ChoreographyActivity" = None, BPMN2Model_Participant375: "BPMN2Model_ChoreographyActivity" = None, BPMN2Model_Participant381: "BPMN2Model_Collaboration" = None, BPMN2Model_Participant440: "BPMN2Model_ConversationNode" = None, BPMN2Model_Participant564: "BPMN2Model_GlobalChoreographyTask" = None, BPMN2Model_Participant720: set["BPMN2Model_Interface"] = None, BPMN2Model_Participant723: set["BPMN2Model_EndPoint"] = None, BPMN2Model_Participant726: "BPMN2Model_ParticipantMultiplicity" = None, BPMN2Model_Participant729: "BPMN2Model_Process" = None, BPMN2Model_Participant733: "BPMN2Model_ParticipantAssociation" = None, BPMN2Model_Participant736: "BPMN2Model_ParticipantAssociation" = None, BPMN2Model_Participant739: "BPMN2Model_PartnerEntity" = None, BPMN2Model_Participant742: "BPMN2Model_PartnerRole" = None):
        self.name = name
        self.BPMN2Model_Participant = BPMN2Model_Participant
        self.BPMN2Model_Participant369 = BPMN2Model_Participant369
        self.BPMN2Model_Participant375 = BPMN2Model_Participant375
        self.BPMN2Model_Participant381 = BPMN2Model_Participant381
        self.BPMN2Model_Participant440 = BPMN2Model_Participant440
        self.BPMN2Model_Participant564 = BPMN2Model_Participant564
        self.BPMN2Model_Participant720 = BPMN2Model_Participant720 if BPMN2Model_Participant720 is not None else set()
        self.BPMN2Model_Participant723 = BPMN2Model_Participant723 if BPMN2Model_Participant723 is not None else set()
        self.BPMN2Model_Participant726 = BPMN2Model_Participant726
        self.BPMN2Model_Participant729 = BPMN2Model_Participant729
        self.BPMN2Model_Participant733 = BPMN2Model_Participant733
        self.BPMN2Model_Participant736 = BPMN2Model_Participant736
        self.BPMN2Model_Participant739 = BPMN2Model_Participant739
        self.BPMN2Model_Participant742 = BPMN2Model_Participant742
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_Participant369(self):
        return self.__BPMN2Model_Participant369

    @BPMN2Model_Participant369.setter
    def BPMN2Model_Participant369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Participant__BPMN2Model_Participant369", None)
        self.__BPMN2Model_Participant369 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ChoreographyActivity368"):
                opp_val = getattr(old_value, "BPMN2Model_ChoreographyActivity368", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ChoreographyActivity368"):
                opp_val = getattr(value, "BPMN2Model_ChoreographyActivity368", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_ChoreographyActivity368", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Participant729(self):
        return self.__BPMN2Model_Participant729

    @BPMN2Model_Participant729.setter
    def BPMN2Model_Participant729(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Participant__BPMN2Model_Participant729", None)
        self.__BPMN2Model_Participant729 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Process730"):
                opp_val = getattr(old_value, "BPMN2Model_Process730", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Process730", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Process730"):
                opp_val = getattr(value, "BPMN2Model_Process730", None)
                setattr(value, "BPMN2Model_Process730", self)

    @property
    def BPMN2Model_Participant742(self):
        return self.__BPMN2Model_Participant742

    @BPMN2Model_Participant742.setter
    def BPMN2Model_Participant742(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Participant__BPMN2Model_Participant742", None)
        self.__BPMN2Model_Participant742 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_PartnerRole741"):
                opp_val = getattr(old_value, "BPMN2Model_PartnerRole741", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_PartnerRole741"):
                opp_val = getattr(value, "BPMN2Model_PartnerRole741", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_PartnerRole741", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Participant440(self):
        return self.__BPMN2Model_Participant440

    @BPMN2Model_Participant440.setter
    def BPMN2Model_Participant440(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Participant__BPMN2Model_Participant440", None)
        self.__BPMN2Model_Participant440 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ConversationNode439"):
                opp_val = getattr(old_value, "BPMN2Model_ConversationNode439", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ConversationNode439"):
                opp_val = getattr(value, "BPMN2Model_ConversationNode439", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_ConversationNode439", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Participant739(self):
        return self.__BPMN2Model_Participant739

    @BPMN2Model_Participant739.setter
    def BPMN2Model_Participant739(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Participant__BPMN2Model_Participant739", None)
        self.__BPMN2Model_Participant739 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_PartnerEntity738"):
                opp_val = getattr(old_value, "BPMN2Model_PartnerEntity738", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_PartnerEntity738"):
                opp_val = getattr(value, "BPMN2Model_PartnerEntity738", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_PartnerEntity738", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Participant564(self):
        return self.__BPMN2Model_Participant564

    @BPMN2Model_Participant564.setter
    def BPMN2Model_Participant564(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Participant__BPMN2Model_Participant564", None)
        self.__BPMN2Model_Participant564 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_GlobalChoreographyTask563"):
                opp_val = getattr(old_value, "BPMN2Model_GlobalChoreographyTask563", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_GlobalChoreographyTask563", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_GlobalChoreographyTask563"):
                opp_val = getattr(value, "BPMN2Model_GlobalChoreographyTask563", None)
                setattr(value, "BPMN2Model_GlobalChoreographyTask563", self)

    @property
    def BPMN2Model_Participant720(self):
        return self.__BPMN2Model_Participant720

    @BPMN2Model_Participant720.setter
    def BPMN2Model_Participant720(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Participant__BPMN2Model_Participant720", None)
        self.__BPMN2Model_Participant720 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Interface721"):
                    opp_val = getattr(item, "BPMN2Model_Interface721", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Interface721", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Interface721"):
                    opp_val = getattr(item, "BPMN2Model_Interface721", None)
                    
                    setattr(item, "BPMN2Model_Interface721", self)
                    

    @property
    def BPMN2Model_Participant723(self):
        return self.__BPMN2Model_Participant723

    @BPMN2Model_Participant723.setter
    def BPMN2Model_Participant723(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Participant__BPMN2Model_Participant723", None)
        self.__BPMN2Model_Participant723 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_EndPoint724"):
                    opp_val = getattr(item, "BPMN2Model_EndPoint724", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_EndPoint724", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_EndPoint724"):
                    opp_val = getattr(item, "BPMN2Model_EndPoint724", None)
                    
                    setattr(item, "BPMN2Model_EndPoint724", self)
                    

    @property
    def BPMN2Model_Participant736(self):
        return self.__BPMN2Model_Participant736

    @BPMN2Model_Participant736.setter
    def BPMN2Model_Participant736(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Participant__BPMN2Model_Participant736", None)
        self.__BPMN2Model_Participant736 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ParticipantAssociation735"):
                opp_val = getattr(old_value, "BPMN2Model_ParticipantAssociation735", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ParticipantAssociation735", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ParticipantAssociation735"):
                opp_val = getattr(value, "BPMN2Model_ParticipantAssociation735", None)
                setattr(value, "BPMN2Model_ParticipantAssociation735", self)

    @property
    def BPMN2Model_Participant375(self):
        return self.__BPMN2Model_Participant375

    @BPMN2Model_Participant375.setter
    def BPMN2Model_Participant375(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Participant__BPMN2Model_Participant375", None)
        self.__BPMN2Model_Participant375 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ChoreographyActivity374"):
                opp_val = getattr(old_value, "BPMN2Model_ChoreographyActivity374", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ChoreographyActivity374", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ChoreographyActivity374"):
                opp_val = getattr(value, "BPMN2Model_ChoreographyActivity374", None)
                setattr(value, "BPMN2Model_ChoreographyActivity374", self)

    @property
    def BPMN2Model_Participant733(self):
        return self.__BPMN2Model_Participant733

    @BPMN2Model_Participant733.setter
    def BPMN2Model_Participant733(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Participant__BPMN2Model_Participant733", None)
        self.__BPMN2Model_Participant733 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ParticipantAssociation732"):
                opp_val = getattr(old_value, "BPMN2Model_ParticipantAssociation732", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ParticipantAssociation732", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ParticipantAssociation732"):
                opp_val = getattr(value, "BPMN2Model_ParticipantAssociation732", None)
                setattr(value, "BPMN2Model_ParticipantAssociation732", self)

    @property
    def BPMN2Model_Participant(self):
        return self.__BPMN2Model_Participant

    @BPMN2Model_Participant.setter
    def BPMN2Model_Participant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Participant__BPMN2Model_Participant", None)
        self.__BPMN2Model_Participant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot206"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot206", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot206"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot206", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot206", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Participant726(self):
        return self.__BPMN2Model_Participant726

    @BPMN2Model_Participant726.setter
    def BPMN2Model_Participant726(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Participant__BPMN2Model_Participant726", None)
        self.__BPMN2Model_Participant726 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ParticipantMultiplicity727"):
                opp_val = getattr(old_value, "BPMN2Model_ParticipantMultiplicity727", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ParticipantMultiplicity727", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ParticipantMultiplicity727"):
                opp_val = getattr(value, "BPMN2Model_ParticipantMultiplicity727", None)
                setattr(value, "BPMN2Model_ParticipantMultiplicity727", self)

    @property
    def BPMN2Model_Participant381(self):
        return self.__BPMN2Model_Participant381

    @BPMN2Model_Participant381.setter
    def BPMN2Model_Participant381(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Participant__BPMN2Model_Participant381", None)
        self.__BPMN2Model_Participant381 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Collaboration380"):
                opp_val = getattr(old_value, "BPMN2Model_Collaboration380", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Collaboration380"):
                opp_val = getattr(value, "BPMN2Model_Collaboration380", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_Collaboration380", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_ParallelGateway(Gateway):

    pass
class BPMN2Model_OutputSet(BaseElement):

    def __init__(self, name: str, BPMN2Model_OutputSet: "BPMN2Model_DocumentRoot" = None, BPMN2Model_OutputSet354: "BPMN2Model_CatchEvent" = None, OutputSet: "BPMN2Model_DataOutput" = None, OutputSet495: "BPMN2Model_DataOutput" = None, OutputSet497: "BPMN2Model_DataOutput" = None, BPMN2Model_OutputSet585: "BPMN2Model_InputOutputBinding" = None, BPMN2Model_OutputSet597: "BPMN2Model_InputOutputSpecification" = None, OutputSet605: "BPMN2Model_InputSet" = None, outputSetRefs: set["BPMN2Model_DataOutput"] = None, outputSetWithOptional: set["BPMN2Model_DataOutput"] = None, outputSetWithWhileExecuting: set["BPMN2Model_DataOutput"] = None, outputSetRefs717: set["BPMN2Model_InputSet"] = None):
        self.name = name
        self.BPMN2Model_OutputSet = BPMN2Model_OutputSet
        self.BPMN2Model_OutputSet354 = BPMN2Model_OutputSet354
        self.OutputSet = OutputSet
        self.OutputSet495 = OutputSet495
        self.OutputSet497 = OutputSet497
        self.BPMN2Model_OutputSet585 = BPMN2Model_OutputSet585
        self.BPMN2Model_OutputSet597 = BPMN2Model_OutputSet597
        self.OutputSet605 = OutputSet605
        self.outputSetRefs = outputSetRefs if outputSetRefs is not None else set()
        self.outputSetWithOptional = outputSetWithOptional if outputSetWithOptional is not None else set()
        self.outputSetWithWhileExecuting = outputSetWithWhileExecuting if outputSetWithWhileExecuting is not None else set()
        self.outputSetRefs717 = outputSetRefs717 if outputSetRefs717 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OutputSet495(self):
        return self.__OutputSet495

    @OutputSet495.setter
    def OutputSet495(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_OutputSet__OutputSet495", None)
        self.__OutputSet495 = value
        
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
    def OutputSet497(self):
        return self.__OutputSet497

    @OutputSet497.setter
    def OutputSet497(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_OutputSet__OutputSet497", None)
        self.__OutputSet497 = value
        
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
    def BPMN2Model_OutputSet(self):
        return self.__BPMN2Model_OutputSet

    @BPMN2Model_OutputSet.setter
    def BPMN2Model_OutputSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_OutputSet__BPMN2Model_OutputSet", None)
        self.__BPMN2Model_OutputSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot202"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot202", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot202"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot202", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot202", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outputSetRefs(self):
        return self.__outputSetRefs

    @outputSetRefs.setter
    def outputSetRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_OutputSet__outputSetRefs", None)
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
        old_value = getattr(self, f"_BPMN2Model_OutputSet__outputSetWithWhileExecuting", None)
        self.__outputSetWithWhileExecuting = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataOutput715"):
                    opp_val = getattr(item, "DataOutput715", None)
                    
                    if opp_val == self:
                        setattr(item, "DataOutput715", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataOutput715"):
                    opp_val = getattr(item, "DataOutput715", None)
                    
                    setattr(item, "DataOutput715", self)
                    

    @property
    def outputSetWithOptional(self):
        return self.__outputSetWithOptional

    @outputSetWithOptional.setter
    def outputSetWithOptional(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_OutputSet__outputSetWithOptional", None)
        self.__outputSetWithOptional = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataOutput713"):
                    opp_val = getattr(item, "DataOutput713", None)
                    
                    if opp_val == self:
                        setattr(item, "DataOutput713", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataOutput713"):
                    opp_val = getattr(item, "DataOutput713", None)
                    
                    setattr(item, "DataOutput713", self)
                    

    @property
    def BPMN2Model_OutputSet585(self):
        return self.__BPMN2Model_OutputSet585

    @BPMN2Model_OutputSet585.setter
    def BPMN2Model_OutputSet585(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_OutputSet__BPMN2Model_OutputSet585", None)
        self.__BPMN2Model_OutputSet585 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_InputOutputBinding584"):
                opp_val = getattr(old_value, "BPMN2Model_InputOutputBinding584", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_InputOutputBinding584", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_InputOutputBinding584"):
                opp_val = getattr(value, "BPMN2Model_InputOutputBinding584", None)
                setattr(value, "BPMN2Model_InputOutputBinding584", self)

    @property
    def BPMN2Model_OutputSet354(self):
        return self.__BPMN2Model_OutputSet354

    @BPMN2Model_OutputSet354.setter
    def BPMN2Model_OutputSet354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_OutputSet__BPMN2Model_OutputSet354", None)
        self.__BPMN2Model_OutputSet354 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_CatchEvent353"):
                opp_val = getattr(old_value, "BPMN2Model_CatchEvent353", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_CatchEvent353", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_CatchEvent353"):
                opp_val = getattr(value, "BPMN2Model_CatchEvent353", None)
                setattr(value, "BPMN2Model_CatchEvent353", self)

    @property
    def outputSetRefs717(self):
        return self.__outputSetRefs717

    @outputSetRefs717.setter
    def outputSetRefs717(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_OutputSet__outputSetRefs717", None)
        self.__outputSetRefs717 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputSet718"):
                    opp_val = getattr(item, "InputSet718", None)
                    
                    if opp_val == self:
                        setattr(item, "InputSet718", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputSet718"):
                    opp_val = getattr(item, "InputSet718", None)
                    
                    setattr(item, "InputSet718", self)
                    

    @property
    def BPMN2Model_OutputSet597(self):
        return self.__BPMN2Model_OutputSet597

    @BPMN2Model_OutputSet597.setter
    def BPMN2Model_OutputSet597(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_OutputSet__BPMN2Model_OutputSet597", None)
        self.__BPMN2Model_OutputSet597 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_InputOutputSpecification596"):
                opp_val = getattr(old_value, "BPMN2Model_InputOutputSpecification596", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_InputOutputSpecification596"):
                opp_val = getattr(value, "BPMN2Model_InputOutputSpecification596", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_InputOutputSpecification596", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OutputSet(self):
        return self.__OutputSet

    @OutputSet.setter
    def OutputSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_OutputSet__OutputSet", None)
        self.__OutputSet = value
        
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
    def OutputSet605(self):
        return self.__OutputSet605

    @OutputSet605.setter
    def OutputSet605(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_OutputSet__OutputSet605", None)
        self.__OutputSet605 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inputSetRefs604"):
                opp_val = getattr(old_value, "inputSetRefs604", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inputSetRefs604"):
                opp_val = getattr(value, "inputSetRefs604", None)
                if opp_val is None:
                    setattr(value, "inputSetRefs604", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_Operation(BaseElement):

    def __init__(self, name: str, BPMN2Model_Operation: "BPMN2Model_DocumentRoot" = None, BPMN2Model_Operation582: "BPMN2Model_InputOutputBinding" = None, BPMN2Model_Operation614: "BPMN2Model_Interface" = None, BPMN2Model_Operation653: "BPMN2Model_MessageEventDefinition" = None, BPMN2Model_Operation700: "BPMN2Model_Message" = None, BPMN2Model_Operation703: "BPMN2Model_Message" = None, BPMN2Model_Operation706: set["BPMN2Model_Error"] = None, BPMN2Model_Operation709: "BPMN2Model_EObject" = None, BPMN2Model_Operation772: "BPMN2Model_ReceiveTask" = None, BPMN2Model_Operation808: "BPMN2Model_SendTask" = None, BPMN2Model_Operation818: "BPMN2Model_ServiceTask" = None):
        self.name = name
        self.BPMN2Model_Operation = BPMN2Model_Operation
        self.BPMN2Model_Operation582 = BPMN2Model_Operation582
        self.BPMN2Model_Operation614 = BPMN2Model_Operation614
        self.BPMN2Model_Operation653 = BPMN2Model_Operation653
        self.BPMN2Model_Operation700 = BPMN2Model_Operation700
        self.BPMN2Model_Operation703 = BPMN2Model_Operation703
        self.BPMN2Model_Operation706 = BPMN2Model_Operation706 if BPMN2Model_Operation706 is not None else set()
        self.BPMN2Model_Operation709 = BPMN2Model_Operation709
        self.BPMN2Model_Operation772 = BPMN2Model_Operation772
        self.BPMN2Model_Operation808 = BPMN2Model_Operation808
        self.BPMN2Model_Operation818 = BPMN2Model_Operation818
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_Operation709(self):
        return self.__BPMN2Model_Operation709

    @BPMN2Model_Operation709.setter
    def BPMN2Model_Operation709(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Operation__BPMN2Model_Operation709", None)
        self.__BPMN2Model_Operation709 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_EObject710"):
                opp_val = getattr(old_value, "BPMN2Model_EObject710", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_EObject710", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_EObject710"):
                opp_val = getattr(value, "BPMN2Model_EObject710", None)
                setattr(value, "BPMN2Model_EObject710", self)

    @property
    def BPMN2Model_Operation818(self):
        return self.__BPMN2Model_Operation818

    @BPMN2Model_Operation818.setter
    def BPMN2Model_Operation818(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Operation__BPMN2Model_Operation818", None)
        self.__BPMN2Model_Operation818 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ServiceTask817"):
                opp_val = getattr(old_value, "BPMN2Model_ServiceTask817", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ServiceTask817", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ServiceTask817"):
                opp_val = getattr(value, "BPMN2Model_ServiceTask817", None)
                setattr(value, "BPMN2Model_ServiceTask817", self)

    @property
    def BPMN2Model_Operation582(self):
        return self.__BPMN2Model_Operation582

    @BPMN2Model_Operation582.setter
    def BPMN2Model_Operation582(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Operation__BPMN2Model_Operation582", None)
        self.__BPMN2Model_Operation582 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_InputOutputBinding581"):
                opp_val = getattr(old_value, "BPMN2Model_InputOutputBinding581", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_InputOutputBinding581", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_InputOutputBinding581"):
                opp_val = getattr(value, "BPMN2Model_InputOutputBinding581", None)
                setattr(value, "BPMN2Model_InputOutputBinding581", self)

    @property
    def BPMN2Model_Operation700(self):
        return self.__BPMN2Model_Operation700

    @BPMN2Model_Operation700.setter
    def BPMN2Model_Operation700(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Operation__BPMN2Model_Operation700", None)
        self.__BPMN2Model_Operation700 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Message701"):
                opp_val = getattr(old_value, "BPMN2Model_Message701", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Message701", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Message701"):
                opp_val = getattr(value, "BPMN2Model_Message701", None)
                setattr(value, "BPMN2Model_Message701", self)

    @property
    def BPMN2Model_Operation706(self):
        return self.__BPMN2Model_Operation706

    @BPMN2Model_Operation706.setter
    def BPMN2Model_Operation706(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Operation__BPMN2Model_Operation706", None)
        self.__BPMN2Model_Operation706 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Error707"):
                    opp_val = getattr(item, "BPMN2Model_Error707", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Error707", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Error707"):
                    opp_val = getattr(item, "BPMN2Model_Error707", None)
                    
                    setattr(item, "BPMN2Model_Error707", self)
                    

    @property
    def BPMN2Model_Operation808(self):
        return self.__BPMN2Model_Operation808

    @BPMN2Model_Operation808.setter
    def BPMN2Model_Operation808(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Operation__BPMN2Model_Operation808", None)
        self.__BPMN2Model_Operation808 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_SendTask807"):
                opp_val = getattr(old_value, "BPMN2Model_SendTask807", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_SendTask807", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_SendTask807"):
                opp_val = getattr(value, "BPMN2Model_SendTask807", None)
                setattr(value, "BPMN2Model_SendTask807", self)

    @property
    def BPMN2Model_Operation772(self):
        return self.__BPMN2Model_Operation772

    @BPMN2Model_Operation772.setter
    def BPMN2Model_Operation772(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Operation__BPMN2Model_Operation772", None)
        self.__BPMN2Model_Operation772 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ReceiveTask771"):
                opp_val = getattr(old_value, "BPMN2Model_ReceiveTask771", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ReceiveTask771", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ReceiveTask771"):
                opp_val = getattr(value, "BPMN2Model_ReceiveTask771", None)
                setattr(value, "BPMN2Model_ReceiveTask771", self)

    @property
    def BPMN2Model_Operation703(self):
        return self.__BPMN2Model_Operation703

    @BPMN2Model_Operation703.setter
    def BPMN2Model_Operation703(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Operation__BPMN2Model_Operation703", None)
        self.__BPMN2Model_Operation703 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Message704"):
                opp_val = getattr(old_value, "BPMN2Model_Message704", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Message704", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Message704"):
                opp_val = getattr(value, "BPMN2Model_Message704", None)
                setattr(value, "BPMN2Model_Message704", self)

    @property
    def BPMN2Model_Operation(self):
        return self.__BPMN2Model_Operation

    @BPMN2Model_Operation.setter
    def BPMN2Model_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Operation__BPMN2Model_Operation", None)
        self.__BPMN2Model_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot200"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot200", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot200"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot200", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot200", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Operation653(self):
        return self.__BPMN2Model_Operation653

    @BPMN2Model_Operation653.setter
    def BPMN2Model_Operation653(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Operation__BPMN2Model_Operation653", None)
        self.__BPMN2Model_Operation653 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_MessageEventDefinition652"):
                opp_val = getattr(old_value, "BPMN2Model_MessageEventDefinition652", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_MessageEventDefinition652", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_MessageEventDefinition652"):
                opp_val = getattr(value, "BPMN2Model_MessageEventDefinition652", None)
                setattr(value, "BPMN2Model_MessageEventDefinition652", self)

    @property
    def BPMN2Model_Operation614(self):
        return self.__BPMN2Model_Operation614

    @BPMN2Model_Operation614.setter
    def BPMN2Model_Operation614(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Operation__BPMN2Model_Operation614", None)
        self.__BPMN2Model_Operation614 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Interface613"):
                opp_val = getattr(old_value, "BPMN2Model_Interface613", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Interface613"):
                opp_val = getattr(value, "BPMN2Model_Interface613", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_Interface613", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_MultiInstanceLoopCharacteristics(LoopCharacteristics):

    def __init__(self, behavior: str, isSequential: bool, BPMN2Model_MultiInstanceLoopCharacteristics: "BPMN2Model_DocumentRoot" = None, BPMN2Model_MultiInstanceLoopCharacteristics673: "BPMN2Model_Expression" = None, BPMN2Model_MultiInstanceLoopCharacteristics676: "BPMN2Model_ItemAwareElement" = None, BPMN2Model_MultiInstanceLoopCharacteristics679: "BPMN2Model_ItemAwareElement" = None, BPMN2Model_MultiInstanceLoopCharacteristics682: "BPMN2Model_DataInput" = None, BPMN2Model_MultiInstanceLoopCharacteristics685: "BPMN2Model_DataOutput" = None, BPMN2Model_MultiInstanceLoopCharacteristics688: set["BPMN2Model_ComplexBehaviorDefinition"] = None, BPMN2Model_MultiInstanceLoopCharacteristics691: "BPMN2Model_Expression" = None, BPMN2Model_MultiInstanceLoopCharacteristics694: "BPMN2Model_EventDefinition" = None, BPMN2Model_MultiInstanceLoopCharacteristics697: "BPMN2Model_EventDefinition" = None):
        self.behavior = behavior
        self.isSequential = isSequential
        self.BPMN2Model_MultiInstanceLoopCharacteristics = BPMN2Model_MultiInstanceLoopCharacteristics
        self.BPMN2Model_MultiInstanceLoopCharacteristics673 = BPMN2Model_MultiInstanceLoopCharacteristics673
        self.BPMN2Model_MultiInstanceLoopCharacteristics676 = BPMN2Model_MultiInstanceLoopCharacteristics676
        self.BPMN2Model_MultiInstanceLoopCharacteristics679 = BPMN2Model_MultiInstanceLoopCharacteristics679
        self.BPMN2Model_MultiInstanceLoopCharacteristics682 = BPMN2Model_MultiInstanceLoopCharacteristics682
        self.BPMN2Model_MultiInstanceLoopCharacteristics685 = BPMN2Model_MultiInstanceLoopCharacteristics685
        self.BPMN2Model_MultiInstanceLoopCharacteristics688 = BPMN2Model_MultiInstanceLoopCharacteristics688 if BPMN2Model_MultiInstanceLoopCharacteristics688 is not None else set()
        self.BPMN2Model_MultiInstanceLoopCharacteristics691 = BPMN2Model_MultiInstanceLoopCharacteristics691
        self.BPMN2Model_MultiInstanceLoopCharacteristics694 = BPMN2Model_MultiInstanceLoopCharacteristics694
        self.BPMN2Model_MultiInstanceLoopCharacteristics697 = BPMN2Model_MultiInstanceLoopCharacteristics697
        
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
    def BPMN2Model_MultiInstanceLoopCharacteristics694(self):
        return self.__BPMN2Model_MultiInstanceLoopCharacteristics694

    @BPMN2Model_MultiInstanceLoopCharacteristics694.setter
    def BPMN2Model_MultiInstanceLoopCharacteristics694(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_MultiInstanceLoopCharacteristics__BPMN2Model_MultiInstanceLoopCharacteristics694", None)
        self.__BPMN2Model_MultiInstanceLoopCharacteristics694 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_EventDefinition695"):
                opp_val = getattr(old_value, "BPMN2Model_EventDefinition695", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_EventDefinition695", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_EventDefinition695"):
                opp_val = getattr(value, "BPMN2Model_EventDefinition695", None)
                setattr(value, "BPMN2Model_EventDefinition695", self)

    @property
    def BPMN2Model_MultiInstanceLoopCharacteristics697(self):
        return self.__BPMN2Model_MultiInstanceLoopCharacteristics697

    @BPMN2Model_MultiInstanceLoopCharacteristics697.setter
    def BPMN2Model_MultiInstanceLoopCharacteristics697(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_MultiInstanceLoopCharacteristics__BPMN2Model_MultiInstanceLoopCharacteristics697", None)
        self.__BPMN2Model_MultiInstanceLoopCharacteristics697 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_EventDefinition698"):
                opp_val = getattr(old_value, "BPMN2Model_EventDefinition698", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_EventDefinition698", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_EventDefinition698"):
                opp_val = getattr(value, "BPMN2Model_EventDefinition698", None)
                setattr(value, "BPMN2Model_EventDefinition698", self)

    @property
    def BPMN2Model_MultiInstanceLoopCharacteristics688(self):
        return self.__BPMN2Model_MultiInstanceLoopCharacteristics688

    @BPMN2Model_MultiInstanceLoopCharacteristics688.setter
    def BPMN2Model_MultiInstanceLoopCharacteristics688(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_MultiInstanceLoopCharacteristics__BPMN2Model_MultiInstanceLoopCharacteristics688", None)
        self.__BPMN2Model_MultiInstanceLoopCharacteristics688 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ComplexBehaviorDefinition689"):
                    opp_val = getattr(item, "BPMN2Model_ComplexBehaviorDefinition689", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ComplexBehaviorDefinition689", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ComplexBehaviorDefinition689"):
                    opp_val = getattr(item, "BPMN2Model_ComplexBehaviorDefinition689", None)
                    
                    setattr(item, "BPMN2Model_ComplexBehaviorDefinition689", self)
                    

    @property
    def BPMN2Model_MultiInstanceLoopCharacteristics(self):
        return self.__BPMN2Model_MultiInstanceLoopCharacteristics

    @BPMN2Model_MultiInstanceLoopCharacteristics.setter
    def BPMN2Model_MultiInstanceLoopCharacteristics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_MultiInstanceLoopCharacteristics__BPMN2Model_MultiInstanceLoopCharacteristics", None)
        self.__BPMN2Model_MultiInstanceLoopCharacteristics = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot198"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot198", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot198"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot198", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot198", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_MultiInstanceLoopCharacteristics691(self):
        return self.__BPMN2Model_MultiInstanceLoopCharacteristics691

    @BPMN2Model_MultiInstanceLoopCharacteristics691.setter
    def BPMN2Model_MultiInstanceLoopCharacteristics691(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_MultiInstanceLoopCharacteristics__BPMN2Model_MultiInstanceLoopCharacteristics691", None)
        self.__BPMN2Model_MultiInstanceLoopCharacteristics691 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Expression692"):
                opp_val = getattr(old_value, "BPMN2Model_Expression692", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Expression692", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Expression692"):
                opp_val = getattr(value, "BPMN2Model_Expression692", None)
                setattr(value, "BPMN2Model_Expression692", self)

    @property
    def BPMN2Model_MultiInstanceLoopCharacteristics676(self):
        return self.__BPMN2Model_MultiInstanceLoopCharacteristics676

    @BPMN2Model_MultiInstanceLoopCharacteristics676.setter
    def BPMN2Model_MultiInstanceLoopCharacteristics676(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_MultiInstanceLoopCharacteristics__BPMN2Model_MultiInstanceLoopCharacteristics676", None)
        self.__BPMN2Model_MultiInstanceLoopCharacteristics676 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ItemAwareElement677"):
                opp_val = getattr(old_value, "BPMN2Model_ItemAwareElement677", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ItemAwareElement677", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ItemAwareElement677"):
                opp_val = getattr(value, "BPMN2Model_ItemAwareElement677", None)
                setattr(value, "BPMN2Model_ItemAwareElement677", self)

    @property
    def BPMN2Model_MultiInstanceLoopCharacteristics682(self):
        return self.__BPMN2Model_MultiInstanceLoopCharacteristics682

    @BPMN2Model_MultiInstanceLoopCharacteristics682.setter
    def BPMN2Model_MultiInstanceLoopCharacteristics682(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_MultiInstanceLoopCharacteristics__BPMN2Model_MultiInstanceLoopCharacteristics682", None)
        self.__BPMN2Model_MultiInstanceLoopCharacteristics682 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DataInput683"):
                opp_val = getattr(old_value, "BPMN2Model_DataInput683", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_DataInput683", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DataInput683"):
                opp_val = getattr(value, "BPMN2Model_DataInput683", None)
                setattr(value, "BPMN2Model_DataInput683", self)

    @property
    def BPMN2Model_MultiInstanceLoopCharacteristics685(self):
        return self.__BPMN2Model_MultiInstanceLoopCharacteristics685

    @BPMN2Model_MultiInstanceLoopCharacteristics685.setter
    def BPMN2Model_MultiInstanceLoopCharacteristics685(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_MultiInstanceLoopCharacteristics__BPMN2Model_MultiInstanceLoopCharacteristics685", None)
        self.__BPMN2Model_MultiInstanceLoopCharacteristics685 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DataOutput686"):
                opp_val = getattr(old_value, "BPMN2Model_DataOutput686", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_DataOutput686", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DataOutput686"):
                opp_val = getattr(value, "BPMN2Model_DataOutput686", None)
                setattr(value, "BPMN2Model_DataOutput686", self)

    @property
    def BPMN2Model_MultiInstanceLoopCharacteristics679(self):
        return self.__BPMN2Model_MultiInstanceLoopCharacteristics679

    @BPMN2Model_MultiInstanceLoopCharacteristics679.setter
    def BPMN2Model_MultiInstanceLoopCharacteristics679(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_MultiInstanceLoopCharacteristics__BPMN2Model_MultiInstanceLoopCharacteristics679", None)
        self.__BPMN2Model_MultiInstanceLoopCharacteristics679 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ItemAwareElement680"):
                opp_val = getattr(old_value, "BPMN2Model_ItemAwareElement680", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ItemAwareElement680", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ItemAwareElement680"):
                opp_val = getattr(value, "BPMN2Model_ItemAwareElement680", None)
                setattr(value, "BPMN2Model_ItemAwareElement680", self)

    @property
    def BPMN2Model_MultiInstanceLoopCharacteristics673(self):
        return self.__BPMN2Model_MultiInstanceLoopCharacteristics673

    @BPMN2Model_MultiInstanceLoopCharacteristics673.setter
    def BPMN2Model_MultiInstanceLoopCharacteristics673(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_MultiInstanceLoopCharacteristics__BPMN2Model_MultiInstanceLoopCharacteristics673", None)
        self.__BPMN2Model_MultiInstanceLoopCharacteristics673 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Expression674"):
                opp_val = getattr(old_value, "BPMN2Model_Expression674", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Expression674", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Expression674"):
                opp_val = getattr(value, "BPMN2Model_Expression674", None)
                setattr(value, "BPMN2Model_Expression674", self)

class BPMN2Model_Monitoring(BaseElement):

    pass
class BPMN2Model_MessageFlowAssociation(BaseElement):

    pass
class BPMN2Model_MessageFlow(BaseElement):

    def __init__(self, name: str, BPMN2Model_MessageFlow: "BPMN2Model_DocumentRoot" = None, BPMN2Model_MessageFlow378: "BPMN2Model_ChoreographyTask" = None, BPMN2Model_MessageFlow384: "BPMN2Model_Collaboration" = None, BPMN2Model_MessageFlow443: "BPMN2Model_ConversationNode" = None, BPMN2Model_MessageFlow658: "BPMN2Model_Message" = None, BPMN2Model_MessageFlow661: "BPMN2Model_InteractionNode" = None, BPMN2Model_MessageFlow664: "BPMN2Model_InteractionNode" = None, BPMN2Model_MessageFlow668: "BPMN2Model_MessageFlowAssociation" = None, BPMN2Model_MessageFlow671: "BPMN2Model_MessageFlowAssociation" = None):
        self.name = name
        self.BPMN2Model_MessageFlow = BPMN2Model_MessageFlow
        self.BPMN2Model_MessageFlow378 = BPMN2Model_MessageFlow378
        self.BPMN2Model_MessageFlow384 = BPMN2Model_MessageFlow384
        self.BPMN2Model_MessageFlow443 = BPMN2Model_MessageFlow443
        self.BPMN2Model_MessageFlow658 = BPMN2Model_MessageFlow658
        self.BPMN2Model_MessageFlow661 = BPMN2Model_MessageFlow661
        self.BPMN2Model_MessageFlow664 = BPMN2Model_MessageFlow664
        self.BPMN2Model_MessageFlow668 = BPMN2Model_MessageFlow668
        self.BPMN2Model_MessageFlow671 = BPMN2Model_MessageFlow671
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_MessageFlow(self):
        return self.__BPMN2Model_MessageFlow

    @BPMN2Model_MessageFlow.setter
    def BPMN2Model_MessageFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_MessageFlow__BPMN2Model_MessageFlow", None)
        self.__BPMN2Model_MessageFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot192"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot192", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot192"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot192", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot192", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_MessageFlow671(self):
        return self.__BPMN2Model_MessageFlow671

    @BPMN2Model_MessageFlow671.setter
    def BPMN2Model_MessageFlow671(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_MessageFlow__BPMN2Model_MessageFlow671", None)
        self.__BPMN2Model_MessageFlow671 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_MessageFlowAssociation670"):
                opp_val = getattr(old_value, "BPMN2Model_MessageFlowAssociation670", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_MessageFlowAssociation670", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_MessageFlowAssociation670"):
                opp_val = getattr(value, "BPMN2Model_MessageFlowAssociation670", None)
                setattr(value, "BPMN2Model_MessageFlowAssociation670", self)

    @property
    def BPMN2Model_MessageFlow664(self):
        return self.__BPMN2Model_MessageFlow664

    @BPMN2Model_MessageFlow664.setter
    def BPMN2Model_MessageFlow664(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_MessageFlow__BPMN2Model_MessageFlow664", None)
        self.__BPMN2Model_MessageFlow664 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_InteractionNode665"):
                opp_val = getattr(old_value, "BPMN2Model_InteractionNode665", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_InteractionNode665", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_InteractionNode665"):
                opp_val = getattr(value, "BPMN2Model_InteractionNode665", None)
                setattr(value, "BPMN2Model_InteractionNode665", self)

    @property
    def BPMN2Model_MessageFlow384(self):
        return self.__BPMN2Model_MessageFlow384

    @BPMN2Model_MessageFlow384.setter
    def BPMN2Model_MessageFlow384(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_MessageFlow__BPMN2Model_MessageFlow384", None)
        self.__BPMN2Model_MessageFlow384 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Collaboration383"):
                opp_val = getattr(old_value, "BPMN2Model_Collaboration383", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Collaboration383"):
                opp_val = getattr(value, "BPMN2Model_Collaboration383", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_Collaboration383", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_MessageFlow378(self):
        return self.__BPMN2Model_MessageFlow378

    @BPMN2Model_MessageFlow378.setter
    def BPMN2Model_MessageFlow378(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_MessageFlow__BPMN2Model_MessageFlow378", None)
        self.__BPMN2Model_MessageFlow378 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ChoreographyTask377"):
                opp_val = getattr(old_value, "BPMN2Model_ChoreographyTask377", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ChoreographyTask377"):
                opp_val = getattr(value, "BPMN2Model_ChoreographyTask377", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_ChoreographyTask377", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_MessageFlow658(self):
        return self.__BPMN2Model_MessageFlow658

    @BPMN2Model_MessageFlow658.setter
    def BPMN2Model_MessageFlow658(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_MessageFlow__BPMN2Model_MessageFlow658", None)
        self.__BPMN2Model_MessageFlow658 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Message659"):
                opp_val = getattr(old_value, "BPMN2Model_Message659", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Message659", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Message659"):
                opp_val = getattr(value, "BPMN2Model_Message659", None)
                setattr(value, "BPMN2Model_Message659", self)

    @property
    def BPMN2Model_MessageFlow661(self):
        return self.__BPMN2Model_MessageFlow661

    @BPMN2Model_MessageFlow661.setter
    def BPMN2Model_MessageFlow661(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_MessageFlow__BPMN2Model_MessageFlow661", None)
        self.__BPMN2Model_MessageFlow661 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_InteractionNode662"):
                opp_val = getattr(old_value, "BPMN2Model_InteractionNode662", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_InteractionNode662", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_InteractionNode662"):
                opp_val = getattr(value, "BPMN2Model_InteractionNode662", None)
                setattr(value, "BPMN2Model_InteractionNode662", self)

    @property
    def BPMN2Model_MessageFlow668(self):
        return self.__BPMN2Model_MessageFlow668

    @BPMN2Model_MessageFlow668.setter
    def BPMN2Model_MessageFlow668(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_MessageFlow__BPMN2Model_MessageFlow668", None)
        self.__BPMN2Model_MessageFlow668 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_MessageFlowAssociation667"):
                opp_val = getattr(old_value, "BPMN2Model_MessageFlowAssociation667", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_MessageFlowAssociation667", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_MessageFlowAssociation667"):
                opp_val = getattr(value, "BPMN2Model_MessageFlowAssociation667", None)
                setattr(value, "BPMN2Model_MessageFlowAssociation667", self)

    @property
    def BPMN2Model_MessageFlow443(self):
        return self.__BPMN2Model_MessageFlow443

    @BPMN2Model_MessageFlow443.setter
    def BPMN2Model_MessageFlow443(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_MessageFlow__BPMN2Model_MessageFlow443", None)
        self.__BPMN2Model_MessageFlow443 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ConversationNode442"):
                opp_val = getattr(old_value, "BPMN2Model_ConversationNode442", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ConversationNode442"):
                opp_val = getattr(value, "BPMN2Model_ConversationNode442", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_ConversationNode442", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_MessageEventDefinition(EventDefinition):

    pass
class BPMN2Model_Message(RootElement):

    def __init__(self, name: str, BPMN2Model_Message: "BPMN2Model_DocumentRoot" = None, BPMN2Model_Message467: "BPMN2Model_CorrelationPropertyRetrievalExpression" = None, BPMN2Model_Message649: "BPMN2Model_ItemDefinition" = None, BPMN2Model_Message656: "BPMN2Model_MessageEventDefinition" = None, BPMN2Model_Message659: "BPMN2Model_MessageFlow" = None, BPMN2Model_Message701: "BPMN2Model_Operation" = None, BPMN2Model_Message704: "BPMN2Model_Operation" = None, BPMN2Model_Message769: "BPMN2Model_ReceiveTask" = None, BPMN2Model_Message805: "BPMN2Model_SendTask" = None):
        self.name = name
        self.BPMN2Model_Message = BPMN2Model_Message
        self.BPMN2Model_Message467 = BPMN2Model_Message467
        self.BPMN2Model_Message649 = BPMN2Model_Message649
        self.BPMN2Model_Message656 = BPMN2Model_Message656
        self.BPMN2Model_Message659 = BPMN2Model_Message659
        self.BPMN2Model_Message701 = BPMN2Model_Message701
        self.BPMN2Model_Message704 = BPMN2Model_Message704
        self.BPMN2Model_Message769 = BPMN2Model_Message769
        self.BPMN2Model_Message805 = BPMN2Model_Message805
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_Message656(self):
        return self.__BPMN2Model_Message656

    @BPMN2Model_Message656.setter
    def BPMN2Model_Message656(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Message__BPMN2Model_Message656", None)
        self.__BPMN2Model_Message656 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_MessageEventDefinition655"):
                opp_val = getattr(old_value, "BPMN2Model_MessageEventDefinition655", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_MessageEventDefinition655", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_MessageEventDefinition655"):
                opp_val = getattr(value, "BPMN2Model_MessageEventDefinition655", None)
                setattr(value, "BPMN2Model_MessageEventDefinition655", self)

    @property
    def BPMN2Model_Message(self):
        return self.__BPMN2Model_Message

    @BPMN2Model_Message.setter
    def BPMN2Model_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Message__BPMN2Model_Message", None)
        self.__BPMN2Model_Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot188"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot188", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot188"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot188", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot188", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Message649(self):
        return self.__BPMN2Model_Message649

    @BPMN2Model_Message649.setter
    def BPMN2Model_Message649(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Message__BPMN2Model_Message649", None)
        self.__BPMN2Model_Message649 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ItemDefinition650"):
                opp_val = getattr(old_value, "BPMN2Model_ItemDefinition650", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ItemDefinition650", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ItemDefinition650"):
                opp_val = getattr(value, "BPMN2Model_ItemDefinition650", None)
                setattr(value, "BPMN2Model_ItemDefinition650", self)

    @property
    def BPMN2Model_Message467(self):
        return self.__BPMN2Model_Message467

    @BPMN2Model_Message467.setter
    def BPMN2Model_Message467(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Message__BPMN2Model_Message467", None)
        self.__BPMN2Model_Message467 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_CorrelationPropertyRetrievalExpression466"):
                opp_val = getattr(old_value, "BPMN2Model_CorrelationPropertyRetrievalExpression466", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_CorrelationPropertyRetrievalExpression466", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_CorrelationPropertyRetrievalExpression466"):
                opp_val = getattr(value, "BPMN2Model_CorrelationPropertyRetrievalExpression466", None)
                setattr(value, "BPMN2Model_CorrelationPropertyRetrievalExpression466", self)

    @property
    def BPMN2Model_Message704(self):
        return self.__BPMN2Model_Message704

    @BPMN2Model_Message704.setter
    def BPMN2Model_Message704(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Message__BPMN2Model_Message704", None)
        self.__BPMN2Model_Message704 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Operation703"):
                opp_val = getattr(old_value, "BPMN2Model_Operation703", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Operation703", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Operation703"):
                opp_val = getattr(value, "BPMN2Model_Operation703", None)
                setattr(value, "BPMN2Model_Operation703", self)

    @property
    def BPMN2Model_Message659(self):
        return self.__BPMN2Model_Message659

    @BPMN2Model_Message659.setter
    def BPMN2Model_Message659(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Message__BPMN2Model_Message659", None)
        self.__BPMN2Model_Message659 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_MessageFlow658"):
                opp_val = getattr(old_value, "BPMN2Model_MessageFlow658", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_MessageFlow658", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_MessageFlow658"):
                opp_val = getattr(value, "BPMN2Model_MessageFlow658", None)
                setattr(value, "BPMN2Model_MessageFlow658", self)

    @property
    def BPMN2Model_Message805(self):
        return self.__BPMN2Model_Message805

    @BPMN2Model_Message805.setter
    def BPMN2Model_Message805(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Message__BPMN2Model_Message805", None)
        self.__BPMN2Model_Message805 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_SendTask804"):
                opp_val = getattr(old_value, "BPMN2Model_SendTask804", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_SendTask804", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_SendTask804"):
                opp_val = getattr(value, "BPMN2Model_SendTask804", None)
                setattr(value, "BPMN2Model_SendTask804", self)

    @property
    def BPMN2Model_Message701(self):
        return self.__BPMN2Model_Message701

    @BPMN2Model_Message701.setter
    def BPMN2Model_Message701(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Message__BPMN2Model_Message701", None)
        self.__BPMN2Model_Message701 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Operation700"):
                opp_val = getattr(old_value, "BPMN2Model_Operation700", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Operation700", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Operation700"):
                opp_val = getattr(value, "BPMN2Model_Operation700", None)
                setattr(value, "BPMN2Model_Operation700", self)

    @property
    def BPMN2Model_Message769(self):
        return self.__BPMN2Model_Message769

    @BPMN2Model_Message769.setter
    def BPMN2Model_Message769(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Message__BPMN2Model_Message769", None)
        self.__BPMN2Model_Message769 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ReceiveTask768"):
                opp_val = getattr(old_value, "BPMN2Model_ReceiveTask768", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ReceiveTask768", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ReceiveTask768"):
                opp_val = getattr(value, "BPMN2Model_ReceiveTask768", None)
                setattr(value, "BPMN2Model_ReceiveTask768", self)

class BPMN2Model_Interface(RootElement):

    def __init__(self, name: str, BPMN2Model_Interface: "BPMN2Model_DocumentRoot" = None, BPMN2Model_Interface339: "BPMN2Model_CallableElement" = None, BPMN2Model_Interface613: set["BPMN2Model_Operation"] = None, BPMN2Model_Interface616: "BPMN2Model_EObject" = None, BPMN2Model_Interface721: "BPMN2Model_Participant" = None):
        self.name = name
        self.BPMN2Model_Interface = BPMN2Model_Interface
        self.BPMN2Model_Interface339 = BPMN2Model_Interface339
        self.BPMN2Model_Interface613 = BPMN2Model_Interface613 if BPMN2Model_Interface613 is not None else set()
        self.BPMN2Model_Interface616 = BPMN2Model_Interface616
        self.BPMN2Model_Interface721 = BPMN2Model_Interface721
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_Interface339(self):
        return self.__BPMN2Model_Interface339

    @BPMN2Model_Interface339.setter
    def BPMN2Model_Interface339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Interface__BPMN2Model_Interface339", None)
        self.__BPMN2Model_Interface339 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_CallableElement338"):
                opp_val = getattr(old_value, "BPMN2Model_CallableElement338", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_CallableElement338"):
                opp_val = getattr(value, "BPMN2Model_CallableElement338", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_CallableElement338", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Interface(self):
        return self.__BPMN2Model_Interface

    @BPMN2Model_Interface.setter
    def BPMN2Model_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Interface__BPMN2Model_Interface", None)
        self.__BPMN2Model_Interface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot166"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot166", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot166"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot166", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot166", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Interface721(self):
        return self.__BPMN2Model_Interface721

    @BPMN2Model_Interface721.setter
    def BPMN2Model_Interface721(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Interface__BPMN2Model_Interface721", None)
        self.__BPMN2Model_Interface721 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Participant720"):
                opp_val = getattr(old_value, "BPMN2Model_Participant720", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Participant720"):
                opp_val = getattr(value, "BPMN2Model_Participant720", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_Participant720", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Interface613(self):
        return self.__BPMN2Model_Interface613

    @BPMN2Model_Interface613.setter
    def BPMN2Model_Interface613(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Interface__BPMN2Model_Interface613", None)
        self.__BPMN2Model_Interface613 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Operation614"):
                    opp_val = getattr(item, "BPMN2Model_Operation614", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Operation614", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Operation614"):
                    opp_val = getattr(item, "BPMN2Model_Operation614", None)
                    
                    setattr(item, "BPMN2Model_Operation614", self)
                    

    @property
    def BPMN2Model_Interface616(self):
        return self.__BPMN2Model_Interface616

    @BPMN2Model_Interface616.setter
    def BPMN2Model_Interface616(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Interface__BPMN2Model_Interface616", None)
        self.__BPMN2Model_Interface616 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_EObject617"):
                opp_val = getattr(old_value, "BPMN2Model_EObject617", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_EObject617", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_EObject617"):
                opp_val = getattr(value, "BPMN2Model_EObject617", None)
                setattr(value, "BPMN2Model_EObject617", self)

class BPMN2Model_ManualTask(Task):

    pass
class BPMN2Model_LoopCharacteristics(BaseElement):

    pass
class BPMN2Model_LinkEventDefinition(EventDefinition):

    def __init__(self, name: str, BPMN2Model_LinkEventDefinition: "BPMN2Model_DocumentRoot" = None, LinkEventDefinition: "BPMN2Model_LinkEventDefinition" = None, target: set["BPMN2Model_LinkEventDefinition"] = None, LinkEventDefinition647: "BPMN2Model_LinkEventDefinition" = None, source: "BPMN2Model_LinkEventDefinition" = None):
        self.name = name
        self.BPMN2Model_LinkEventDefinition = BPMN2Model_LinkEventDefinition
        self.LinkEventDefinition = LinkEventDefinition
        self.target = target if target is not None else set()
        self.LinkEventDefinition647 = LinkEventDefinition647
        self.source = source
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def LinkEventDefinition(self):
        return self.__LinkEventDefinition

    @LinkEventDefinition.setter
    def LinkEventDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_LinkEventDefinition__LinkEventDefinition", None)
        self.__LinkEventDefinition = value
        
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
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_LinkEventDefinition__source", None)
        self.__source = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LinkEventDefinition647"):
                opp_val = getattr(old_value, "LinkEventDefinition647", None)
                if opp_val == self:
                    setattr(old_value, "LinkEventDefinition647", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LinkEventDefinition647"):
                opp_val = getattr(value, "LinkEventDefinition647", None)
                setattr(value, "LinkEventDefinition647", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_LinkEventDefinition__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LinkEventDefinition"):
                    opp_val = getattr(item, "LinkEventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "LinkEventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LinkEventDefinition"):
                    opp_val = getattr(item, "LinkEventDefinition", None)
                    
                    setattr(item, "LinkEventDefinition", self)
                    

    @property
    def BPMN2Model_LinkEventDefinition(self):
        return self.__BPMN2Model_LinkEventDefinition

    @BPMN2Model_LinkEventDefinition.setter
    def BPMN2Model_LinkEventDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_LinkEventDefinition__BPMN2Model_LinkEventDefinition", None)
        self.__BPMN2Model_LinkEventDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot182"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot182", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot182"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot182", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot182", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def LinkEventDefinition647(self):
        return self.__LinkEventDefinition647

    @LinkEventDefinition647.setter
    def LinkEventDefinition647(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_LinkEventDefinition__LinkEventDefinition647", None)
        self.__LinkEventDefinition647 = value
        
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

class BPMN2Model_LaneSet(BaseElement):

    def __init__(self, name: str, BPMN2Model_LaneSet: "BPMN2Model_DocumentRoot" = None, BPMN2Model_LaneSet551: "BPMN2Model_FlowElementsContainer" = None, BPMN2Model_LaneSet636: "BPMN2Model_Lane" = None, BPMN2Model_LaneSet641: set["BPMN2Model_Lane"] = None):
        self.name = name
        self.BPMN2Model_LaneSet = BPMN2Model_LaneSet
        self.BPMN2Model_LaneSet551 = BPMN2Model_LaneSet551
        self.BPMN2Model_LaneSet636 = BPMN2Model_LaneSet636
        self.BPMN2Model_LaneSet641 = BPMN2Model_LaneSet641 if BPMN2Model_LaneSet641 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_LaneSet551(self):
        return self.__BPMN2Model_LaneSet551

    @BPMN2Model_LaneSet551.setter
    def BPMN2Model_LaneSet551(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_LaneSet__BPMN2Model_LaneSet551", None)
        self.__BPMN2Model_LaneSet551 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_FlowElementsContainer"):
                opp_val = getattr(old_value, "BPMN2Model_FlowElementsContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_FlowElementsContainer"):
                opp_val = getattr(value, "BPMN2Model_FlowElementsContainer", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_FlowElementsContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_LaneSet(self):
        return self.__BPMN2Model_LaneSet

    @BPMN2Model_LaneSet.setter
    def BPMN2Model_LaneSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_LaneSet__BPMN2Model_LaneSet", None)
        self.__BPMN2Model_LaneSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot180"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot180", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot180"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot180", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot180", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_LaneSet636(self):
        return self.__BPMN2Model_LaneSet636

    @BPMN2Model_LaneSet636.setter
    def BPMN2Model_LaneSet636(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_LaneSet__BPMN2Model_LaneSet636", None)
        self.__BPMN2Model_LaneSet636 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Lane635"):
                opp_val = getattr(old_value, "BPMN2Model_Lane635", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Lane635", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Lane635"):
                opp_val = getattr(value, "BPMN2Model_Lane635", None)
                setattr(value, "BPMN2Model_Lane635", self)

    @property
    def BPMN2Model_LaneSet641(self):
        return self.__BPMN2Model_LaneSet641

    @BPMN2Model_LaneSet641.setter
    def BPMN2Model_LaneSet641(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_LaneSet__BPMN2Model_LaneSet641", None)
        self.__BPMN2Model_LaneSet641 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Lane642"):
                    opp_val = getattr(item, "BPMN2Model_Lane642", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Lane642", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Lane642"):
                    opp_val = getattr(item, "BPMN2Model_Lane642", None)
                    
                    setattr(item, "BPMN2Model_Lane642", self)
                    

class BPMN2Model_Lane(BaseElement):

    def __init__(self, name: str, BPMN2Model_Lane: "BPMN2Model_DocumentRoot" = None, Lane: "BPMN2Model_FlowNode" = None, BPMN2Model_Lane631: "BPMN2Model_BaseElement" = None, lanes: set["BPMN2Model_FlowNode"] = None, BPMN2Model_Lane635: "BPMN2Model_LaneSet" = None, BPMN2Model_Lane638: "BPMN2Model_BaseElement" = None, BPMN2Model_Lane642: "BPMN2Model_LaneSet" = None):
        self.name = name
        self.BPMN2Model_Lane = BPMN2Model_Lane
        self.Lane = Lane
        self.BPMN2Model_Lane631 = BPMN2Model_Lane631
        self.lanes = lanes if lanes is not None else set()
        self.BPMN2Model_Lane635 = BPMN2Model_Lane635
        self.BPMN2Model_Lane638 = BPMN2Model_Lane638
        self.BPMN2Model_Lane642 = BPMN2Model_Lane642
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_Lane631(self):
        return self.__BPMN2Model_Lane631

    @BPMN2Model_Lane631.setter
    def BPMN2Model_Lane631(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Lane__BPMN2Model_Lane631", None)
        self.__BPMN2Model_Lane631 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_BaseElement632"):
                opp_val = getattr(old_value, "BPMN2Model_BaseElement632", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_BaseElement632", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_BaseElement632"):
                opp_val = getattr(value, "BPMN2Model_BaseElement632", None)
                setattr(value, "BPMN2Model_BaseElement632", self)

    @property
    def Lane(self):
        return self.__Lane

    @Lane.setter
    def Lane(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Lane__Lane", None)
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
    def BPMN2Model_Lane638(self):
        return self.__BPMN2Model_Lane638

    @BPMN2Model_Lane638.setter
    def BPMN2Model_Lane638(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Lane__BPMN2Model_Lane638", None)
        self.__BPMN2Model_Lane638 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_BaseElement639"):
                opp_val = getattr(old_value, "BPMN2Model_BaseElement639", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_BaseElement639", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_BaseElement639"):
                opp_val = getattr(value, "BPMN2Model_BaseElement639", None)
                setattr(value, "BPMN2Model_BaseElement639", self)

    @property
    def BPMN2Model_Lane635(self):
        return self.__BPMN2Model_Lane635

    @BPMN2Model_Lane635.setter
    def BPMN2Model_Lane635(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Lane__BPMN2Model_Lane635", None)
        self.__BPMN2Model_Lane635 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_LaneSet636"):
                opp_val = getattr(old_value, "BPMN2Model_LaneSet636", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_LaneSet636", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_LaneSet636"):
                opp_val = getattr(value, "BPMN2Model_LaneSet636", None)
                setattr(value, "BPMN2Model_LaneSet636", self)

    @property
    def BPMN2Model_Lane642(self):
        return self.__BPMN2Model_Lane642

    @BPMN2Model_Lane642.setter
    def BPMN2Model_Lane642(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Lane__BPMN2Model_Lane642", None)
        self.__BPMN2Model_Lane642 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_LaneSet641"):
                opp_val = getattr(old_value, "BPMN2Model_LaneSet641", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_LaneSet641"):
                opp_val = getattr(value, "BPMN2Model_LaneSet641", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_LaneSet641", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lanes(self):
        return self.__lanes

    @lanes.setter
    def lanes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Lane__lanes", None)
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
    def BPMN2Model_Lane(self):
        return self.__BPMN2Model_Lane

    @BPMN2Model_Lane.setter
    def BPMN2Model_Lane(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Lane__BPMN2Model_Lane", None)
        self.__BPMN2Model_Lane = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot178"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot178", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot178"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot178", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot178", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_ItemDefinition(RootElement):

    def __init__(self, isCollection: bool, itemKind: str, BPMN2Model_ItemDefinition: "BPMN2Model_DocumentRoot" = None, BPMN2Model_ItemDefinition455: "BPMN2Model_CorrelationProperty" = None, BPMN2Model_ItemDefinition515: "BPMN2Model_Error" = None, BPMN2Model_ItemDefinition521: "BPMN2Model_Escalation" = None, BPMN2Model_ItemDefinition561: "BPMN2Model_FormalExpression" = None, BPMN2Model_ItemDefinition623: "BPMN2Model_ItemAwareElement" = None, BPMN2Model_ItemDefinition625: "BPMN2Model_Import" = None, BPMN2Model_ItemDefinition628: "BPMN2Model_EObject" = None, BPMN2Model_ItemDefinition650: "BPMN2Model_Message" = None, BPMN2Model_ItemDefinition787: "BPMN2Model_ResourceParameter" = None, BPMN2Model_ItemDefinition821: "BPMN2Model_Signal" = None):
        self.isCollection = isCollection
        self.itemKind = itemKind
        self.BPMN2Model_ItemDefinition = BPMN2Model_ItemDefinition
        self.BPMN2Model_ItemDefinition455 = BPMN2Model_ItemDefinition455
        self.BPMN2Model_ItemDefinition515 = BPMN2Model_ItemDefinition515
        self.BPMN2Model_ItemDefinition521 = BPMN2Model_ItemDefinition521
        self.BPMN2Model_ItemDefinition561 = BPMN2Model_ItemDefinition561
        self.BPMN2Model_ItemDefinition623 = BPMN2Model_ItemDefinition623
        self.BPMN2Model_ItemDefinition625 = BPMN2Model_ItemDefinition625
        self.BPMN2Model_ItemDefinition628 = BPMN2Model_ItemDefinition628
        self.BPMN2Model_ItemDefinition650 = BPMN2Model_ItemDefinition650
        self.BPMN2Model_ItemDefinition787 = BPMN2Model_ItemDefinition787
        self.BPMN2Model_ItemDefinition821 = BPMN2Model_ItemDefinition821
        
    @property
    def isCollection(self) -> bool:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: bool):
        self.__isCollection = isCollection

    @property
    def itemKind(self) -> str:
        return self.__itemKind

    @itemKind.setter
    def itemKind(self, itemKind: str):
        self.__itemKind = itemKind

    @property
    def BPMN2Model_ItemDefinition625(self):
        return self.__BPMN2Model_ItemDefinition625

    @BPMN2Model_ItemDefinition625.setter
    def BPMN2Model_ItemDefinition625(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ItemDefinition__BPMN2Model_ItemDefinition625", None)
        self.__BPMN2Model_ItemDefinition625 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Import626"):
                opp_val = getattr(old_value, "BPMN2Model_Import626", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Import626", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Import626"):
                opp_val = getattr(value, "BPMN2Model_Import626", None)
                setattr(value, "BPMN2Model_Import626", self)

    @property
    def BPMN2Model_ItemDefinition628(self):
        return self.__BPMN2Model_ItemDefinition628

    @BPMN2Model_ItemDefinition628.setter
    def BPMN2Model_ItemDefinition628(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ItemDefinition__BPMN2Model_ItemDefinition628", None)
        self.__BPMN2Model_ItemDefinition628 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_EObject629"):
                opp_val = getattr(old_value, "BPMN2Model_EObject629", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_EObject629", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_EObject629"):
                opp_val = getattr(value, "BPMN2Model_EObject629", None)
                setattr(value, "BPMN2Model_EObject629", self)

    @property
    def BPMN2Model_ItemDefinition623(self):
        return self.__BPMN2Model_ItemDefinition623

    @BPMN2Model_ItemDefinition623.setter
    def BPMN2Model_ItemDefinition623(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ItemDefinition__BPMN2Model_ItemDefinition623", None)
        self.__BPMN2Model_ItemDefinition623 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ItemAwareElement622"):
                opp_val = getattr(old_value, "BPMN2Model_ItemAwareElement622", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ItemAwareElement622", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ItemAwareElement622"):
                opp_val = getattr(value, "BPMN2Model_ItemAwareElement622", None)
                setattr(value, "BPMN2Model_ItemAwareElement622", self)

    @property
    def BPMN2Model_ItemDefinition515(self):
        return self.__BPMN2Model_ItemDefinition515

    @BPMN2Model_ItemDefinition515.setter
    def BPMN2Model_ItemDefinition515(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ItemDefinition__BPMN2Model_ItemDefinition515", None)
        self.__BPMN2Model_ItemDefinition515 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Error514"):
                opp_val = getattr(old_value, "BPMN2Model_Error514", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Error514", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Error514"):
                opp_val = getattr(value, "BPMN2Model_Error514", None)
                setattr(value, "BPMN2Model_Error514", self)

    @property
    def BPMN2Model_ItemDefinition455(self):
        return self.__BPMN2Model_ItemDefinition455

    @BPMN2Model_ItemDefinition455.setter
    def BPMN2Model_ItemDefinition455(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ItemDefinition__BPMN2Model_ItemDefinition455", None)
        self.__BPMN2Model_ItemDefinition455 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_CorrelationProperty454"):
                opp_val = getattr(old_value, "BPMN2Model_CorrelationProperty454", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_CorrelationProperty454", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_CorrelationProperty454"):
                opp_val = getattr(value, "BPMN2Model_CorrelationProperty454", None)
                setattr(value, "BPMN2Model_CorrelationProperty454", self)

    @property
    def BPMN2Model_ItemDefinition(self):
        return self.__BPMN2Model_ItemDefinition

    @BPMN2Model_ItemDefinition.setter
    def BPMN2Model_ItemDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ItemDefinition__BPMN2Model_ItemDefinition", None)
        self.__BPMN2Model_ItemDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot176"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot176", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot176"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot176", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot176", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_ItemDefinition561(self):
        return self.__BPMN2Model_ItemDefinition561

    @BPMN2Model_ItemDefinition561.setter
    def BPMN2Model_ItemDefinition561(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ItemDefinition__BPMN2Model_ItemDefinition561", None)
        self.__BPMN2Model_ItemDefinition561 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_FormalExpression560"):
                opp_val = getattr(old_value, "BPMN2Model_FormalExpression560", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_FormalExpression560", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_FormalExpression560"):
                opp_val = getattr(value, "BPMN2Model_FormalExpression560", None)
                setattr(value, "BPMN2Model_FormalExpression560", self)

    @property
    def BPMN2Model_ItemDefinition821(self):
        return self.__BPMN2Model_ItemDefinition821

    @BPMN2Model_ItemDefinition821.setter
    def BPMN2Model_ItemDefinition821(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ItemDefinition__BPMN2Model_ItemDefinition821", None)
        self.__BPMN2Model_ItemDefinition821 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Signal820"):
                opp_val = getattr(old_value, "BPMN2Model_Signal820", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Signal820", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Signal820"):
                opp_val = getattr(value, "BPMN2Model_Signal820", None)
                setattr(value, "BPMN2Model_Signal820", self)

    @property
    def BPMN2Model_ItemDefinition521(self):
        return self.__BPMN2Model_ItemDefinition521

    @BPMN2Model_ItemDefinition521.setter
    def BPMN2Model_ItemDefinition521(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ItemDefinition__BPMN2Model_ItemDefinition521", None)
        self.__BPMN2Model_ItemDefinition521 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Escalation520"):
                opp_val = getattr(old_value, "BPMN2Model_Escalation520", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Escalation520", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Escalation520"):
                opp_val = getattr(value, "BPMN2Model_Escalation520", None)
                setattr(value, "BPMN2Model_Escalation520", self)

    @property
    def BPMN2Model_ItemDefinition787(self):
        return self.__BPMN2Model_ItemDefinition787

    @BPMN2Model_ItemDefinition787.setter
    def BPMN2Model_ItemDefinition787(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ItemDefinition__BPMN2Model_ItemDefinition787", None)
        self.__BPMN2Model_ItemDefinition787 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ResourceParameter786"):
                opp_val = getattr(old_value, "BPMN2Model_ResourceParameter786", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ResourceParameter786", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ResourceParameter786"):
                opp_val = getattr(value, "BPMN2Model_ResourceParameter786", None)
                setattr(value, "BPMN2Model_ResourceParameter786", self)

    @property
    def BPMN2Model_ItemDefinition650(self):
        return self.__BPMN2Model_ItemDefinition650

    @BPMN2Model_ItemDefinition650.setter
    def BPMN2Model_ItemDefinition650(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ItemDefinition__BPMN2Model_ItemDefinition650", None)
        self.__BPMN2Model_ItemDefinition650 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Message649"):
                opp_val = getattr(old_value, "BPMN2Model_Message649", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Message649", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Message649"):
                opp_val = getattr(value, "BPMN2Model_Message649", None)
                setattr(value, "BPMN2Model_Message649", self)

class BPMN2Model_InputOutputSpecification(BaseElement):

    pass
class BPMN2Model_IntermediateThrowEvent(ThrowEvent):

    pass
class BPMN2Model_IntermediateCatchEvent(CatchEvent):

    pass
class BPMN2Model_InputSet(BaseElement):

    def __init__(self, name: str, BPMN2Model_InputSet: "BPMN2Model_DocumentRoot" = None, InputSet: "BPMN2Model_DataInput" = None, InputSet487: "BPMN2Model_DataInput" = None, InputSet489: "BPMN2Model_DataInput" = None, BPMN2Model_InputSet579: "BPMN2Model_InputOutputBinding" = None, BPMN2Model_InputSet594: "BPMN2Model_InputOutputSpecification" = None, inputSetRefs: set["BPMN2Model_DataInput"] = None, inputSetWithOptional: set["BPMN2Model_DataInput"] = None, inputSetWithWhileExecuting: set["BPMN2Model_DataInput"] = None, inputSetRefs604: set["BPMN2Model_OutputSet"] = None, InputSet718: "BPMN2Model_OutputSet" = None, BPMN2Model_InputSet848: "BPMN2Model_ThrowEvent" = None):
        self.name = name
        self.BPMN2Model_InputSet = BPMN2Model_InputSet
        self.InputSet = InputSet
        self.InputSet487 = InputSet487
        self.InputSet489 = InputSet489
        self.BPMN2Model_InputSet579 = BPMN2Model_InputSet579
        self.BPMN2Model_InputSet594 = BPMN2Model_InputSet594
        self.inputSetRefs = inputSetRefs if inputSetRefs is not None else set()
        self.inputSetWithOptional = inputSetWithOptional if inputSetWithOptional is not None else set()
        self.inputSetWithWhileExecuting = inputSetWithWhileExecuting if inputSetWithWhileExecuting is not None else set()
        self.inputSetRefs604 = inputSetRefs604 if inputSetRefs604 is not None else set()
        self.InputSet718 = InputSet718
        self.BPMN2Model_InputSet848 = BPMN2Model_InputSet848
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_InputSet(self):
        return self.__BPMN2Model_InputSet

    @BPMN2Model_InputSet.setter
    def BPMN2Model_InputSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_InputSet__BPMN2Model_InputSet", None)
        self.__BPMN2Model_InputSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot164"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot164", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot164"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot164", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot164", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def InputSet489(self):
        return self.__InputSet489

    @InputSet489.setter
    def InputSet489(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_InputSet__InputSet489", None)
        self.__InputSet489 = value
        
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
    def inputSetWithWhileExecuting(self):
        return self.__inputSetWithWhileExecuting

    @inputSetWithWhileExecuting.setter
    def inputSetWithWhileExecuting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_InputSet__inputSetWithWhileExecuting", None)
        self.__inputSetWithWhileExecuting = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataInput602"):
                    opp_val = getattr(item, "DataInput602", None)
                    
                    if opp_val == self:
                        setattr(item, "DataInput602", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataInput602"):
                    opp_val = getattr(item, "DataInput602", None)
                    
                    setattr(item, "DataInput602", self)
                    

    @property
    def InputSet718(self):
        return self.__InputSet718

    @InputSet718.setter
    def InputSet718(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_InputSet__InputSet718", None)
        self.__InputSet718 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outputSetRefs717"):
                opp_val = getattr(old_value, "outputSetRefs717", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outputSetRefs717"):
                opp_val = getattr(value, "outputSetRefs717", None)
                if opp_val is None:
                    setattr(value, "outputSetRefs717", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inputSetWithOptional(self):
        return self.__inputSetWithOptional

    @inputSetWithOptional.setter
    def inputSetWithOptional(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_InputSet__inputSetWithOptional", None)
        self.__inputSetWithOptional = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataInput600"):
                    opp_val = getattr(item, "DataInput600", None)
                    
                    if opp_val == self:
                        setattr(item, "DataInput600", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataInput600"):
                    opp_val = getattr(item, "DataInput600", None)
                    
                    setattr(item, "DataInput600", self)
                    

    @property
    def InputSet487(self):
        return self.__InputSet487

    @InputSet487.setter
    def InputSet487(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_InputSet__InputSet487", None)
        self.__InputSet487 = value
        
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
    def BPMN2Model_InputSet594(self):
        return self.__BPMN2Model_InputSet594

    @BPMN2Model_InputSet594.setter
    def BPMN2Model_InputSet594(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_InputSet__BPMN2Model_InputSet594", None)
        self.__BPMN2Model_InputSet594 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_InputOutputSpecification593"):
                opp_val = getattr(old_value, "BPMN2Model_InputOutputSpecification593", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_InputOutputSpecification593"):
                opp_val = getattr(value, "BPMN2Model_InputOutputSpecification593", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_InputOutputSpecification593", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_InputSet848(self):
        return self.__BPMN2Model_InputSet848

    @BPMN2Model_InputSet848.setter
    def BPMN2Model_InputSet848(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_InputSet__BPMN2Model_InputSet848", None)
        self.__BPMN2Model_InputSet848 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ThrowEvent847"):
                opp_val = getattr(old_value, "BPMN2Model_ThrowEvent847", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ThrowEvent847", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ThrowEvent847"):
                opp_val = getattr(value, "BPMN2Model_ThrowEvent847", None)
                setattr(value, "BPMN2Model_ThrowEvent847", self)

    @property
    def inputSetRefs(self):
        return self.__inputSetRefs

    @inputSetRefs.setter
    def inputSetRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_InputSet__inputSetRefs", None)
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
    def BPMN2Model_InputSet579(self):
        return self.__BPMN2Model_InputSet579

    @BPMN2Model_InputSet579.setter
    def BPMN2Model_InputSet579(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_InputSet__BPMN2Model_InputSet579", None)
        self.__BPMN2Model_InputSet579 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_InputOutputBinding578"):
                opp_val = getattr(old_value, "BPMN2Model_InputOutputBinding578", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_InputOutputBinding578", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_InputOutputBinding578"):
                opp_val = getattr(value, "BPMN2Model_InputOutputBinding578", None)
                setattr(value, "BPMN2Model_InputOutputBinding578", self)

    @property
    def inputSetRefs604(self):
        return self.__inputSetRefs604

    @inputSetRefs604.setter
    def inputSetRefs604(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_InputSet__inputSetRefs604", None)
        self.__inputSetRefs604 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputSet605"):
                    opp_val = getattr(item, "OutputSet605", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputSet605", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputSet605"):
                    opp_val = getattr(item, "OutputSet605", None)
                    
                    setattr(item, "OutputSet605", self)
                    

    @property
    def InputSet(self):
        return self.__InputSet

    @InputSet.setter
    def InputSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_InputSet__InputSet", None)
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

class BPMN2Model_InclusiveGateway(Gateway):

    pass
class BPMN2Model_ImplicitThrowEvent(ThrowEvent):

    pass
class BPMN2Model_ResourceRole(BaseElement):

    def __init__(self, name: str, BPMN2Model_ResourceRole: "BPMN2Model_DocumentRoot" = None, BPMN2Model_ResourceRole291: "BPMN2Model_Activity" = None, BPMN2Model_ResourceRole567: "BPMN2Model_GlobalTask" = None, BPMN2Model_ResourceRole757: "BPMN2Model_Process" = None, BPMN2Model_ResourceRole795: "BPMN2Model_Resource" = None, BPMN2Model_ResourceRole798: set["BPMN2Model_ResourceParameterBinding"] = None, BPMN2Model_ResourceRole801: "BPMN2Model_ResourceAssignmentExpression" = None):
        self.name = name
        self.BPMN2Model_ResourceRole = BPMN2Model_ResourceRole
        self.BPMN2Model_ResourceRole291 = BPMN2Model_ResourceRole291
        self.BPMN2Model_ResourceRole567 = BPMN2Model_ResourceRole567
        self.BPMN2Model_ResourceRole757 = BPMN2Model_ResourceRole757
        self.BPMN2Model_ResourceRole795 = BPMN2Model_ResourceRole795
        self.BPMN2Model_ResourceRole798 = BPMN2Model_ResourceRole798 if BPMN2Model_ResourceRole798 is not None else set()
        self.BPMN2Model_ResourceRole801 = BPMN2Model_ResourceRole801
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_ResourceRole795(self):
        return self.__BPMN2Model_ResourceRole795

    @BPMN2Model_ResourceRole795.setter
    def BPMN2Model_ResourceRole795(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ResourceRole__BPMN2Model_ResourceRole795", None)
        self.__BPMN2Model_ResourceRole795 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Resource796"):
                opp_val = getattr(old_value, "BPMN2Model_Resource796", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Resource796", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Resource796"):
                opp_val = getattr(value, "BPMN2Model_Resource796", None)
                setattr(value, "BPMN2Model_Resource796", self)

    @property
    def BPMN2Model_ResourceRole801(self):
        return self.__BPMN2Model_ResourceRole801

    @BPMN2Model_ResourceRole801.setter
    def BPMN2Model_ResourceRole801(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ResourceRole__BPMN2Model_ResourceRole801", None)
        self.__BPMN2Model_ResourceRole801 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ResourceAssignmentExpression802"):
                opp_val = getattr(old_value, "BPMN2Model_ResourceAssignmentExpression802", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ResourceAssignmentExpression802", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ResourceAssignmentExpression802"):
                opp_val = getattr(value, "BPMN2Model_ResourceAssignmentExpression802", None)
                setattr(value, "BPMN2Model_ResourceAssignmentExpression802", self)

    @property
    def BPMN2Model_ResourceRole(self):
        return self.__BPMN2Model_ResourceRole

    @BPMN2Model_ResourceRole.setter
    def BPMN2Model_ResourceRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ResourceRole__BPMN2Model_ResourceRole", None)
        self.__BPMN2Model_ResourceRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot156"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot156", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot156"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot156", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot156", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_ResourceRole291(self):
        return self.__BPMN2Model_ResourceRole291

    @BPMN2Model_ResourceRole291.setter
    def BPMN2Model_ResourceRole291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ResourceRole__BPMN2Model_ResourceRole291", None)
        self.__BPMN2Model_ResourceRole291 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Activity290"):
                opp_val = getattr(old_value, "BPMN2Model_Activity290", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Activity290"):
                opp_val = getattr(value, "BPMN2Model_Activity290", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_Activity290", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_ResourceRole757(self):
        return self.__BPMN2Model_ResourceRole757

    @BPMN2Model_ResourceRole757.setter
    def BPMN2Model_ResourceRole757(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ResourceRole__BPMN2Model_ResourceRole757", None)
        self.__BPMN2Model_ResourceRole757 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Process756"):
                opp_val = getattr(old_value, "BPMN2Model_Process756", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Process756"):
                opp_val = getattr(value, "BPMN2Model_Process756", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_Process756", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_ResourceRole567(self):
        return self.__BPMN2Model_ResourceRole567

    @BPMN2Model_ResourceRole567.setter
    def BPMN2Model_ResourceRole567(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ResourceRole__BPMN2Model_ResourceRole567", None)
        self.__BPMN2Model_ResourceRole567 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_GlobalTask566"):
                opp_val = getattr(old_value, "BPMN2Model_GlobalTask566", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_GlobalTask566"):
                opp_val = getattr(value, "BPMN2Model_GlobalTask566", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_GlobalTask566", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_ResourceRole798(self):
        return self.__BPMN2Model_ResourceRole798

    @BPMN2Model_ResourceRole798.setter
    def BPMN2Model_ResourceRole798(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ResourceRole__BPMN2Model_ResourceRole798", None)
        self.__BPMN2Model_ResourceRole798 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ResourceParameterBinding799"):
                    opp_val = getattr(item, "BPMN2Model_ResourceParameterBinding799", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ResourceParameterBinding799", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ResourceParameterBinding799"):
                    opp_val = getattr(item, "BPMN2Model_ResourceParameterBinding799", None)
                    
                    setattr(item, "BPMN2Model_ResourceParameterBinding799", self)
                    

class BPMN2Model_Performer(ResourceRole):

    pass
class BPMN2Model_HumanPerformer(Performer):

    pass
class BPMN2Model_Group(Artifact):

    pass
class BPMN2Model_GlobalUserTask(GlobalTask):

    def __init__(self, implementation: str, BPMN2Model_GlobalUserTask: "BPMN2Model_DocumentRoot" = None, BPMN2Model_GlobalUserTask569: set["BPMN2Model_Rendering"] = None):
        self.implementation = implementation
        self.BPMN2Model_GlobalUserTask = BPMN2Model_GlobalUserTask
        self.BPMN2Model_GlobalUserTask569 = BPMN2Model_GlobalUserTask569 if BPMN2Model_GlobalUserTask569 is not None else set()
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def BPMN2Model_GlobalUserTask(self):
        return self.__BPMN2Model_GlobalUserTask

    @BPMN2Model_GlobalUserTask.setter
    def BPMN2Model_GlobalUserTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_GlobalUserTask__BPMN2Model_GlobalUserTask", None)
        self.__BPMN2Model_GlobalUserTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot148"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot148", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot148"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot148", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot148", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_GlobalUserTask569(self):
        return self.__BPMN2Model_GlobalUserTask569

    @BPMN2Model_GlobalUserTask569.setter
    def BPMN2Model_GlobalUserTask569(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_GlobalUserTask__BPMN2Model_GlobalUserTask569", None)
        self.__BPMN2Model_GlobalUserTask569 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Rendering570"):
                    opp_val = getattr(item, "BPMN2Model_Rendering570", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Rendering570", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Rendering570"):
                    opp_val = getattr(item, "BPMN2Model_Rendering570", None)
                    
                    setattr(item, "BPMN2Model_Rendering570", self)
                    

class BPMN2Model_GlobalTask(CallableElement):

    pass
class BPMN2Model_GlobalScriptTask(GlobalTask):

    def __init__(self, script: str, scriptLanguage: str, BPMN2Model_GlobalScriptTask: "BPMN2Model_DocumentRoot" = None):
        self.script = script
        self.scriptLanguage = scriptLanguage
        self.BPMN2Model_GlobalScriptTask = BPMN2Model_GlobalScriptTask
        
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
    def BPMN2Model_GlobalScriptTask(self):
        return self.__BPMN2Model_GlobalScriptTask

    @BPMN2Model_GlobalScriptTask.setter
    def BPMN2Model_GlobalScriptTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_GlobalScriptTask__BPMN2Model_GlobalScriptTask", None)
        self.__BPMN2Model_GlobalScriptTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot144"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot144", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot144"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot144", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot144", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_GlobalManualTask(GlobalTask):

    pass
class BPMN2Model_GlobalConversation(Collaboration):

    pass
class BPMN2Model_GlobalChoreographyTask(Choreography):

    pass
class BPMN2Model_GlobalBusinessRuleTask(GlobalTask):

    def __init__(self, implementation: str, BPMN2Model_GlobalBusinessRuleTask: "BPMN2Model_DocumentRoot" = None):
        self.implementation = implementation
        self.BPMN2Model_GlobalBusinessRuleTask = BPMN2Model_GlobalBusinessRuleTask
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def BPMN2Model_GlobalBusinessRuleTask(self):
        return self.__BPMN2Model_GlobalBusinessRuleTask

    @BPMN2Model_GlobalBusinessRuleTask.setter
    def BPMN2Model_GlobalBusinessRuleTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_GlobalBusinessRuleTask__BPMN2Model_GlobalBusinessRuleTask", None)
        self.__BPMN2Model_GlobalBusinessRuleTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot136"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot136", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot136"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot136", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot136", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_Gateway(FlowNode):

    def __init__(self, gatewayDirection: str, BPMN2Model_Gateway: "BPMN2Model_DocumentRoot" = None):
        self.gatewayDirection = gatewayDirection
        self.BPMN2Model_Gateway = BPMN2Model_Gateway
        
    @property
    def gatewayDirection(self) -> str:
        return self.__gatewayDirection

    @gatewayDirection.setter
    def gatewayDirection(self, gatewayDirection: str):
        self.__gatewayDirection = gatewayDirection

    @property
    def BPMN2Model_Gateway(self):
        return self.__BPMN2Model_Gateway

    @BPMN2Model_Gateway.setter
    def BPMN2Model_Gateway(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Gateway__BPMN2Model_Gateway", None)
        self.__BPMN2Model_Gateway = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot134"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot134", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot134"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot134", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot134", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_FormalExpression(Expression):

    def __init__(self, mixed: str, body: str, language: str, BPMN2Model_FormalExpression: "BPMN2Model_DocumentRoot" = None, BPMN2Model_FormalExpression414: "BPMN2Model_ComplexBehaviorDefinition" = None, BPMN2Model_FormalExpression458: "BPMN2Model_CorrelationPropertyBinding" = None, BPMN2Model_FormalExpression464: "BPMN2Model_CorrelationPropertyRetrievalExpression" = None, BPMN2Model_FormalExpression481: "BPMN2Model_DataAssociation" = None, BPMN2Model_FormalExpression560: "BPMN2Model_ItemDefinition" = None):
        self.mixed = mixed
        self.body = body
        self.language = language
        self.BPMN2Model_FormalExpression = BPMN2Model_FormalExpression
        self.BPMN2Model_FormalExpression414 = BPMN2Model_FormalExpression414
        self.BPMN2Model_FormalExpression458 = BPMN2Model_FormalExpression458
        self.BPMN2Model_FormalExpression464 = BPMN2Model_FormalExpression464
        self.BPMN2Model_FormalExpression481 = BPMN2Model_FormalExpression481
        self.BPMN2Model_FormalExpression560 = BPMN2Model_FormalExpression560
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

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

    @property
    def BPMN2Model_FormalExpression464(self):
        return self.__BPMN2Model_FormalExpression464

    @BPMN2Model_FormalExpression464.setter
    def BPMN2Model_FormalExpression464(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_FormalExpression__BPMN2Model_FormalExpression464", None)
        self.__BPMN2Model_FormalExpression464 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_CorrelationPropertyRetrievalExpression463"):
                opp_val = getattr(old_value, "BPMN2Model_CorrelationPropertyRetrievalExpression463", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_CorrelationPropertyRetrievalExpression463", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_CorrelationPropertyRetrievalExpression463"):
                opp_val = getattr(value, "BPMN2Model_CorrelationPropertyRetrievalExpression463", None)
                setattr(value, "BPMN2Model_CorrelationPropertyRetrievalExpression463", self)

    @property
    def BPMN2Model_FormalExpression560(self):
        return self.__BPMN2Model_FormalExpression560

    @BPMN2Model_FormalExpression560.setter
    def BPMN2Model_FormalExpression560(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_FormalExpression__BPMN2Model_FormalExpression560", None)
        self.__BPMN2Model_FormalExpression560 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ItemDefinition561"):
                opp_val = getattr(old_value, "BPMN2Model_ItemDefinition561", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ItemDefinition561", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ItemDefinition561"):
                opp_val = getattr(value, "BPMN2Model_ItemDefinition561", None)
                setattr(value, "BPMN2Model_ItemDefinition561", self)

    @property
    def BPMN2Model_FormalExpression414(self):
        return self.__BPMN2Model_FormalExpression414

    @BPMN2Model_FormalExpression414.setter
    def BPMN2Model_FormalExpression414(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_FormalExpression__BPMN2Model_FormalExpression414", None)
        self.__BPMN2Model_FormalExpression414 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ComplexBehaviorDefinition413"):
                opp_val = getattr(old_value, "BPMN2Model_ComplexBehaviorDefinition413", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ComplexBehaviorDefinition413", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ComplexBehaviorDefinition413"):
                opp_val = getattr(value, "BPMN2Model_ComplexBehaviorDefinition413", None)
                setattr(value, "BPMN2Model_ComplexBehaviorDefinition413", self)

    @property
    def BPMN2Model_FormalExpression481(self):
        return self.__BPMN2Model_FormalExpression481

    @BPMN2Model_FormalExpression481.setter
    def BPMN2Model_FormalExpression481(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_FormalExpression__BPMN2Model_FormalExpression481", None)
        self.__BPMN2Model_FormalExpression481 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DataAssociation480"):
                opp_val = getattr(old_value, "BPMN2Model_DataAssociation480", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_DataAssociation480", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DataAssociation480"):
                opp_val = getattr(value, "BPMN2Model_DataAssociation480", None)
                setattr(value, "BPMN2Model_DataAssociation480", self)

    @property
    def BPMN2Model_FormalExpression(self):
        return self.__BPMN2Model_FormalExpression

    @BPMN2Model_FormalExpression.setter
    def BPMN2Model_FormalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_FormalExpression__BPMN2Model_FormalExpression", None)
        self.__BPMN2Model_FormalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot132"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot132", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot132"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot132", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot132", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_FormalExpression458(self):
        return self.__BPMN2Model_FormalExpression458

    @BPMN2Model_FormalExpression458.setter
    def BPMN2Model_FormalExpression458(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_FormalExpression__BPMN2Model_FormalExpression458", None)
        self.__BPMN2Model_FormalExpression458 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_CorrelationPropertyBinding457"):
                opp_val = getattr(old_value, "BPMN2Model_CorrelationPropertyBinding457", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_CorrelationPropertyBinding457", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_CorrelationPropertyBinding457"):
                opp_val = getattr(value, "BPMN2Model_CorrelationPropertyBinding457", None)
                setattr(value, "BPMN2Model_CorrelationPropertyBinding457", self)

class BPMN2Model_FlowNode(FlowElement):

    pass
class BPMN2Model_Expression(BaseElement):

    pass
class BPMN2Model_ExclusiveGateway(Gateway):

    pass
class BPMN2Model_EventBasedGateway(Gateway):

    def __init__(self, eventGatewayType: str, instantiate: bool, BPMN2Model_EventBasedGateway: "BPMN2Model_DocumentRoot" = None):
        self.eventGatewayType = eventGatewayType
        self.instantiate = instantiate
        self.BPMN2Model_EventBasedGateway = BPMN2Model_EventBasedGateway
        
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

    @property
    def BPMN2Model_EventBasedGateway(self):
        return self.__BPMN2Model_EventBasedGateway

    @BPMN2Model_EventBasedGateway.setter
    def BPMN2Model_EventBasedGateway(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_EventBasedGateway__BPMN2Model_EventBasedGateway", None)
        self.__BPMN2Model_EventBasedGateway = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot120"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot120", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot120"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot120", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot120", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_Event(InteractionNode, FlowNode):

    pass
class BPMN2Model_EscalationEventDefinition(EventDefinition):

    pass
class BPMN2Model_ErrorEventDefinition(EventDefinition):

    pass
class BPMN2Model_Error(RootElement):

    def __init__(self, errorCode: str, name: str, BPMN2Model_Error: "BPMN2Model_DocumentRoot" = None, BPMN2Model_Error514: "BPMN2Model_ItemDefinition" = None, BPMN2Model_Error518: "BPMN2Model_ErrorEventDefinition" = None, BPMN2Model_Error707: "BPMN2Model_Operation" = None):
        self.errorCode = errorCode
        self.name = name
        self.BPMN2Model_Error = BPMN2Model_Error
        self.BPMN2Model_Error514 = BPMN2Model_Error514
        self.BPMN2Model_Error518 = BPMN2Model_Error518
        self.BPMN2Model_Error707 = BPMN2Model_Error707
        
    @property
    def errorCode(self) -> str:
        return self.__errorCode

    @errorCode.setter
    def errorCode(self, errorCode: str):
        self.__errorCode = errorCode

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_Error(self):
        return self.__BPMN2Model_Error

    @BPMN2Model_Error.setter
    def BPMN2Model_Error(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Error__BPMN2Model_Error", None)
        self.__BPMN2Model_Error = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot110"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot110", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot110"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot110", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot110", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Error518(self):
        return self.__BPMN2Model_Error518

    @BPMN2Model_Error518.setter
    def BPMN2Model_Error518(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Error__BPMN2Model_Error518", None)
        self.__BPMN2Model_Error518 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ErrorEventDefinition517"):
                opp_val = getattr(old_value, "BPMN2Model_ErrorEventDefinition517", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ErrorEventDefinition517", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ErrorEventDefinition517"):
                opp_val = getattr(value, "BPMN2Model_ErrorEventDefinition517", None)
                setattr(value, "BPMN2Model_ErrorEventDefinition517", self)

    @property
    def BPMN2Model_Error514(self):
        return self.__BPMN2Model_Error514

    @BPMN2Model_Error514.setter
    def BPMN2Model_Error514(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Error__BPMN2Model_Error514", None)
        self.__BPMN2Model_Error514 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ItemDefinition515"):
                opp_val = getattr(old_value, "BPMN2Model_ItemDefinition515", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ItemDefinition515", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ItemDefinition515"):
                opp_val = getattr(value, "BPMN2Model_ItemDefinition515", None)
                setattr(value, "BPMN2Model_ItemDefinition515", self)

    @property
    def BPMN2Model_Error707(self):
        return self.__BPMN2Model_Error707

    @BPMN2Model_Error707.setter
    def BPMN2Model_Error707(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Error__BPMN2Model_Error707", None)
        self.__BPMN2Model_Error707 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Operation706"):
                opp_val = getattr(old_value, "BPMN2Model_Operation706", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Operation706"):
                opp_val = getattr(value, "BPMN2Model_Operation706", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_Operation706", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_EndPoint(RootElement):

    pass
class BPMN2Model_EndEvent(ThrowEvent):

    pass
class BPMN2Model_Documentation(BaseElement):

    def __init__(self, mixed: str, text: str, textFormat: str, BPMN2Model_Documentation: "BPMN2Model_DocumentRoot" = None, BPMN2Model_Documentation318: "BPMN2Model_BaseElement" = None):
        self.mixed = mixed
        self.text = text
        self.textFormat = textFormat
        self.BPMN2Model_Documentation = BPMN2Model_Documentation
        self.BPMN2Model_Documentation318 = BPMN2Model_Documentation318
        
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
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def BPMN2Model_Documentation(self):
        return self.__BPMN2Model_Documentation

    @BPMN2Model_Documentation.setter
    def BPMN2Model_Documentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Documentation__BPMN2Model_Documentation", None)
        self.__BPMN2Model_Documentation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot104"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot104"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot104", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Documentation318(self):
        return self.__BPMN2Model_Documentation318

    @BPMN2Model_Documentation318.setter
    def BPMN2Model_Documentation318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Documentation__BPMN2Model_Documentation318", None)
        self.__BPMN2Model_Documentation318 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_BaseElement317"):
                opp_val = getattr(old_value, "BPMN2Model_BaseElement317", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_BaseElement317"):
                opp_val = getattr(value, "BPMN2Model_BaseElement317", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_BaseElement317", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_Definitions(BaseElement):

    def __init__(self, exporter: str, exporterVersion: str, expressionLanguage: str, name: str, targetNamespace: str, typeLanguage: str, BPMN2Model_Definitions: "BPMN2Model_DocumentRoot" = None, BPMN2Model_Definitions502: set["BPMN2Model_Import"] = None, BPMN2Model_Definitions505: set["BPMN2Model_Extension"] = None, BPMN2Model_Definitions508: set["BPMN2Model_RootElement"] = None, BPMN2Model_Definitions511: set["BPMN2Model_Relationship"] = None):
        self.exporter = exporter
        self.exporterVersion = exporterVersion
        self.expressionLanguage = expressionLanguage
        self.name = name
        self.targetNamespace = targetNamespace
        self.typeLanguage = typeLanguage
        self.BPMN2Model_Definitions = BPMN2Model_Definitions
        self.BPMN2Model_Definitions502 = BPMN2Model_Definitions502 if BPMN2Model_Definitions502 is not None else set()
        self.BPMN2Model_Definitions505 = BPMN2Model_Definitions505 if BPMN2Model_Definitions505 is not None else set()
        self.BPMN2Model_Definitions508 = BPMN2Model_Definitions508 if BPMN2Model_Definitions508 is not None else set()
        self.BPMN2Model_Definitions511 = BPMN2Model_Definitions511 if BPMN2Model_Definitions511 is not None else set()
        
    @property
    def targetNamespace(self) -> str:
        return self.__targetNamespace

    @targetNamespace.setter
    def targetNamespace(self, targetNamespace: str):
        self.__targetNamespace = targetNamespace

    @property
    def exporter(self) -> str:
        return self.__exporter

    @exporter.setter
    def exporter(self, exporter: str):
        self.__exporter = exporter

    @property
    def exporterVersion(self) -> str:
        return self.__exporterVersion

    @exporterVersion.setter
    def exporterVersion(self, exporterVersion: str):
        self.__exporterVersion = exporterVersion

    @property
    def expressionLanguage(self) -> str:
        return self.__expressionLanguage

    @expressionLanguage.setter
    def expressionLanguage(self, expressionLanguage: str):
        self.__expressionLanguage = expressionLanguage

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def typeLanguage(self) -> str:
        return self.__typeLanguage

    @typeLanguage.setter
    def typeLanguage(self, typeLanguage: str):
        self.__typeLanguage = typeLanguage

    @property
    def BPMN2Model_Definitions508(self):
        return self.__BPMN2Model_Definitions508

    @BPMN2Model_Definitions508.setter
    def BPMN2Model_Definitions508(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Definitions__BPMN2Model_Definitions508", None)
        self.__BPMN2Model_Definitions508 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_RootElement509"):
                    opp_val = getattr(item, "BPMN2Model_RootElement509", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_RootElement509", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_RootElement509"):
                    opp_val = getattr(item, "BPMN2Model_RootElement509", None)
                    
                    setattr(item, "BPMN2Model_RootElement509", self)
                    

    @property
    def BPMN2Model_Definitions511(self):
        return self.__BPMN2Model_Definitions511

    @BPMN2Model_Definitions511.setter
    def BPMN2Model_Definitions511(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Definitions__BPMN2Model_Definitions511", None)
        self.__BPMN2Model_Definitions511 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Relationship512"):
                    opp_val = getattr(item, "BPMN2Model_Relationship512", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Relationship512", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Relationship512"):
                    opp_val = getattr(item, "BPMN2Model_Relationship512", None)
                    
                    setattr(item, "BPMN2Model_Relationship512", self)
                    

    @property
    def BPMN2Model_Definitions(self):
        return self.__BPMN2Model_Definitions

    @BPMN2Model_Definitions.setter
    def BPMN2Model_Definitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Definitions__BPMN2Model_Definitions", None)
        self.__BPMN2Model_Definitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot102"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot102"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot102", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Definitions505(self):
        return self.__BPMN2Model_Definitions505

    @BPMN2Model_Definitions505.setter
    def BPMN2Model_Definitions505(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Definitions__BPMN2Model_Definitions505", None)
        self.__BPMN2Model_Definitions505 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Extension506"):
                    opp_val = getattr(item, "BPMN2Model_Extension506", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Extension506", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Extension506"):
                    opp_val = getattr(item, "BPMN2Model_Extension506", None)
                    
                    setattr(item, "BPMN2Model_Extension506", self)
                    

    @property
    def BPMN2Model_Definitions502(self):
        return self.__BPMN2Model_Definitions502

    @BPMN2Model_Definitions502.setter
    def BPMN2Model_Definitions502(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Definitions__BPMN2Model_Definitions502", None)
        self.__BPMN2Model_Definitions502 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Import503"):
                    opp_val = getattr(item, "BPMN2Model_Import503", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Import503", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Import503"):
                    opp_val = getattr(item, "BPMN2Model_Import503", None)
                    
                    setattr(item, "BPMN2Model_Import503", self)
                    

class BPMN2Model_DataStoreReference(ItemAwareElement, FlowElement):

    pass
class BPMN2Model_ConversationAssociation(BaseElement):

    pass
class BPMN2Model_DataStore(RootElement, ItemAwareElement):

    def __init__(self, capacity: int, isUnlimited: bool, name: str, BPMN2Model_DataStore: "BPMN2Model_DocumentRoot" = None, BPMN2Model_DataStore500: "BPMN2Model_DataStoreReference" = None):
        self.capacity = capacity
        self.isUnlimited = isUnlimited
        self.name = name
        self.BPMN2Model_DataStore = BPMN2Model_DataStore
        self.BPMN2Model_DataStore500 = BPMN2Model_DataStore500
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def BPMN2Model_DataStore500(self):
        return self.__BPMN2Model_DataStore500

    @BPMN2Model_DataStore500.setter
    def BPMN2Model_DataStore500(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataStore__BPMN2Model_DataStore500", None)
        self.__BPMN2Model_DataStore500 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DataStoreReference499"):
                opp_val = getattr(old_value, "BPMN2Model_DataStoreReference499", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_DataStoreReference499", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DataStoreReference499"):
                opp_val = getattr(value, "BPMN2Model_DataStoreReference499", None)
                setattr(value, "BPMN2Model_DataStoreReference499", self)

    @property
    def BPMN2Model_DataStore(self):
        return self.__BPMN2Model_DataStore

    @BPMN2Model_DataStore.setter
    def BPMN2Model_DataStore(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataStore__BPMN2Model_DataStore", None)
        self.__BPMN2Model_DataStore = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot98"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot98", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot98"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot98", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot98", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_DataState(BaseElement):

    def __init__(self, name: str, BPMN2Model_DataState: "BPMN2Model_DocumentRoot" = None, BPMN2Model_DataState620: "BPMN2Model_ItemAwareElement" = None):
        self.name = name
        self.BPMN2Model_DataState = BPMN2Model_DataState
        self.BPMN2Model_DataState620 = BPMN2Model_DataState620
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_DataState(self):
        return self.__BPMN2Model_DataState

    @BPMN2Model_DataState.setter
    def BPMN2Model_DataState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataState__BPMN2Model_DataState", None)
        self.__BPMN2Model_DataState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot96"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot96", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot96"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot96", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot96", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_DataState620(self):
        return self.__BPMN2Model_DataState620

    @BPMN2Model_DataState620.setter
    def BPMN2Model_DataState620(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataState__BPMN2Model_DataState620", None)
        self.__BPMN2Model_DataState620 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ItemAwareElement619"):
                opp_val = getattr(old_value, "BPMN2Model_ItemAwareElement619", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ItemAwareElement619", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ItemAwareElement619"):
                opp_val = getattr(value, "BPMN2Model_ItemAwareElement619", None)
                setattr(value, "BPMN2Model_ItemAwareElement619", self)

class BPMN2Model_DataOutputAssociation(DataAssociation):

    pass
class BPMN2Model_DataOutput(ItemAwareElement):

    def __init__(self, isCollection: bool, name: str, BPMN2Model_DataOutput: "BPMN2Model_DocumentRoot" = None, BPMN2Model_DataOutput348: "BPMN2Model_CatchEvent" = None, optionalOutputRefs: set["BPMN2Model_OutputSet"] = None, whileExecutingOutputRefs: set["BPMN2Model_OutputSet"] = None, dataOutputRefs: set["BPMN2Model_OutputSet"] = None, BPMN2Model_DataOutput591: "BPMN2Model_InputOutputSpecification" = None, BPMN2Model_DataOutput686: "BPMN2Model_MultiInstanceLoopCharacteristics" = None, DataOutput: "BPMN2Model_OutputSet" = None, DataOutput713: "BPMN2Model_OutputSet" = None, DataOutput715: "BPMN2Model_OutputSet" = None):
        self.isCollection = isCollection
        self.name = name
        self.BPMN2Model_DataOutput = BPMN2Model_DataOutput
        self.BPMN2Model_DataOutput348 = BPMN2Model_DataOutput348
        self.optionalOutputRefs = optionalOutputRefs if optionalOutputRefs is not None else set()
        self.whileExecutingOutputRefs = whileExecutingOutputRefs if whileExecutingOutputRefs is not None else set()
        self.dataOutputRefs = dataOutputRefs if dataOutputRefs is not None else set()
        self.BPMN2Model_DataOutput591 = BPMN2Model_DataOutput591
        self.BPMN2Model_DataOutput686 = BPMN2Model_DataOutput686
        self.DataOutput = DataOutput
        self.DataOutput713 = DataOutput713
        self.DataOutput715 = DataOutput715
        
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
    def DataOutput713(self):
        return self.__DataOutput713

    @DataOutput713.setter
    def DataOutput713(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataOutput__DataOutput713", None)
        self.__DataOutput713 = value
        
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
    def DataOutput(self):
        return self.__DataOutput

    @DataOutput.setter
    def DataOutput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataOutput__DataOutput", None)
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
    def dataOutputRefs(self):
        return self.__dataOutputRefs

    @dataOutputRefs.setter
    def dataOutputRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataOutput__dataOutputRefs", None)
        self.__dataOutputRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputSet497"):
                    opp_val = getattr(item, "OutputSet497", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputSet497", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputSet497"):
                    opp_val = getattr(item, "OutputSet497", None)
                    
                    setattr(item, "OutputSet497", self)
                    

    @property
    def DataOutput715(self):
        return self.__DataOutput715

    @DataOutput715.setter
    def DataOutput715(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataOutput__DataOutput715", None)
        self.__DataOutput715 = value
        
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
    def BPMN2Model_DataOutput591(self):
        return self.__BPMN2Model_DataOutput591

    @BPMN2Model_DataOutput591.setter
    def BPMN2Model_DataOutput591(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataOutput__BPMN2Model_DataOutput591", None)
        self.__BPMN2Model_DataOutput591 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_InputOutputSpecification590"):
                opp_val = getattr(old_value, "BPMN2Model_InputOutputSpecification590", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_InputOutputSpecification590"):
                opp_val = getattr(value, "BPMN2Model_InputOutputSpecification590", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_InputOutputSpecification590", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_DataOutput686(self):
        return self.__BPMN2Model_DataOutput686

    @BPMN2Model_DataOutput686.setter
    def BPMN2Model_DataOutput686(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataOutput__BPMN2Model_DataOutput686", None)
        self.__BPMN2Model_DataOutput686 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_MultiInstanceLoopCharacteristics685"):
                opp_val = getattr(old_value, "BPMN2Model_MultiInstanceLoopCharacteristics685", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_MultiInstanceLoopCharacteristics685", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_MultiInstanceLoopCharacteristics685"):
                opp_val = getattr(value, "BPMN2Model_MultiInstanceLoopCharacteristics685", None)
                setattr(value, "BPMN2Model_MultiInstanceLoopCharacteristics685", self)

    @property
    def optionalOutputRefs(self):
        return self.__optionalOutputRefs

    @optionalOutputRefs.setter
    def optionalOutputRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataOutput__optionalOutputRefs", None)
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
                    

    @property
    def BPMN2Model_DataOutput348(self):
        return self.__BPMN2Model_DataOutput348

    @BPMN2Model_DataOutput348.setter
    def BPMN2Model_DataOutput348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataOutput__BPMN2Model_DataOutput348", None)
        self.__BPMN2Model_DataOutput348 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_CatchEvent347"):
                opp_val = getattr(old_value, "BPMN2Model_CatchEvent347", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_CatchEvent347"):
                opp_val = getattr(value, "BPMN2Model_CatchEvent347", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_CatchEvent347", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_DataOutput(self):
        return self.__BPMN2Model_DataOutput

    @BPMN2Model_DataOutput.setter
    def BPMN2Model_DataOutput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataOutput__BPMN2Model_DataOutput", None)
        self.__BPMN2Model_DataOutput = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot92"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot92"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot92", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def whileExecutingOutputRefs(self):
        return self.__whileExecutingOutputRefs

    @whileExecutingOutputRefs.setter
    def whileExecutingOutputRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataOutput__whileExecutingOutputRefs", None)
        self.__whileExecutingOutputRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputSet495"):
                    opp_val = getattr(item, "OutputSet495", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputSet495", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputSet495"):
                    opp_val = getattr(item, "OutputSet495", None)
                    
                    setattr(item, "OutputSet495", self)
                    

class BPMN2Model_DataObjectReference(ItemAwareElement, FlowElement):

    pass
class BPMN2Model_DataObject(FlowElement, ItemAwareElement):

    def __init__(self, isCollection: bool, BPMN2Model_DataObject: "BPMN2Model_DocumentRoot" = None, BPMN2Model_DataObject492: "BPMN2Model_DataObjectReference" = None):
        self.isCollection = isCollection
        self.BPMN2Model_DataObject = BPMN2Model_DataObject
        self.BPMN2Model_DataObject492 = BPMN2Model_DataObject492
        
    @property
    def isCollection(self) -> bool:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: bool):
        self.__isCollection = isCollection

    @property
    def BPMN2Model_DataObject(self):
        return self.__BPMN2Model_DataObject

    @BPMN2Model_DataObject.setter
    def BPMN2Model_DataObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataObject__BPMN2Model_DataObject", None)
        self.__BPMN2Model_DataObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot88"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot88"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot88", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_DataObject492(self):
        return self.__BPMN2Model_DataObject492

    @BPMN2Model_DataObject492.setter
    def BPMN2Model_DataObject492(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataObject__BPMN2Model_DataObject492", None)
        self.__BPMN2Model_DataObject492 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DataObjectReference491"):
                opp_val = getattr(old_value, "BPMN2Model_DataObjectReference491", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_DataObjectReference491", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DataObjectReference491"):
                opp_val = getattr(value, "BPMN2Model_DataObjectReference491", None)
                setattr(value, "BPMN2Model_DataObjectReference491", self)

class BPMN2Model_DataInputAssociation(DataAssociation):

    pass
class BPMN2Model_DataInput(ItemAwareElement):

    def __init__(self, isCollection: bool, name: str, BPMN2Model_DataInput: "BPMN2Model_DocumentRoot" = None, optionalInputRefs: set["BPMN2Model_InputSet"] = None, whileExecutingInputRefs: set["BPMN2Model_InputSet"] = None, dataInputRefs: set["BPMN2Model_InputSet"] = None, BPMN2Model_DataInput588: "BPMN2Model_InputOutputSpecification" = None, DataInput: "BPMN2Model_InputSet" = None, DataInput600: "BPMN2Model_InputSet" = None, DataInput602: "BPMN2Model_InputSet" = None, BPMN2Model_DataInput683: "BPMN2Model_MultiInstanceLoopCharacteristics" = None, BPMN2Model_DataInput842: "BPMN2Model_ThrowEvent" = None):
        self.isCollection = isCollection
        self.name = name
        self.BPMN2Model_DataInput = BPMN2Model_DataInput
        self.optionalInputRefs = optionalInputRefs if optionalInputRefs is not None else set()
        self.whileExecutingInputRefs = whileExecutingInputRefs if whileExecutingInputRefs is not None else set()
        self.dataInputRefs = dataInputRefs if dataInputRefs is not None else set()
        self.BPMN2Model_DataInput588 = BPMN2Model_DataInput588
        self.DataInput = DataInput
        self.DataInput600 = DataInput600
        self.DataInput602 = DataInput602
        self.BPMN2Model_DataInput683 = BPMN2Model_DataInput683
        self.BPMN2Model_DataInput842 = BPMN2Model_DataInput842
        
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
    def BPMN2Model_DataInput(self):
        return self.__BPMN2Model_DataInput

    @BPMN2Model_DataInput.setter
    def BPMN2Model_DataInput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataInput__BPMN2Model_DataInput", None)
        self.__BPMN2Model_DataInput = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot84"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot84", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot84"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot84", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot84", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_DataInput588(self):
        return self.__BPMN2Model_DataInput588

    @BPMN2Model_DataInput588.setter
    def BPMN2Model_DataInput588(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataInput__BPMN2Model_DataInput588", None)
        self.__BPMN2Model_DataInput588 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_InputOutputSpecification587"):
                opp_val = getattr(old_value, "BPMN2Model_InputOutputSpecification587", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_InputOutputSpecification587"):
                opp_val = getattr(value, "BPMN2Model_InputOutputSpecification587", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_InputOutputSpecification587", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DataInput602(self):
        return self.__DataInput602

    @DataInput602.setter
    def DataInput602(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataInput__DataInput602", None)
        self.__DataInput602 = value
        
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
    def whileExecutingInputRefs(self):
        return self.__whileExecutingInputRefs

    @whileExecutingInputRefs.setter
    def whileExecutingInputRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataInput__whileExecutingInputRefs", None)
        self.__whileExecutingInputRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputSet487"):
                    opp_val = getattr(item, "InputSet487", None)
                    
                    if opp_val == self:
                        setattr(item, "InputSet487", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputSet487"):
                    opp_val = getattr(item, "InputSet487", None)
                    
                    setattr(item, "InputSet487", self)
                    

    @property
    def DataInput600(self):
        return self.__DataInput600

    @DataInput600.setter
    def DataInput600(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataInput__DataInput600", None)
        self.__DataInput600 = value
        
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
    def optionalInputRefs(self):
        return self.__optionalInputRefs

    @optionalInputRefs.setter
    def optionalInputRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataInput__optionalInputRefs", None)
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
    def BPMN2Model_DataInput683(self):
        return self.__BPMN2Model_DataInput683

    @BPMN2Model_DataInput683.setter
    def BPMN2Model_DataInput683(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataInput__BPMN2Model_DataInput683", None)
        self.__BPMN2Model_DataInput683 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_MultiInstanceLoopCharacteristics682"):
                opp_val = getattr(old_value, "BPMN2Model_MultiInstanceLoopCharacteristics682", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_MultiInstanceLoopCharacteristics682", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_MultiInstanceLoopCharacteristics682"):
                opp_val = getattr(value, "BPMN2Model_MultiInstanceLoopCharacteristics682", None)
                setattr(value, "BPMN2Model_MultiInstanceLoopCharacteristics682", self)

    @property
    def BPMN2Model_DataInput842(self):
        return self.__BPMN2Model_DataInput842

    @BPMN2Model_DataInput842.setter
    def BPMN2Model_DataInput842(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataInput__BPMN2Model_DataInput842", None)
        self.__BPMN2Model_DataInput842 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ThrowEvent841"):
                opp_val = getattr(old_value, "BPMN2Model_ThrowEvent841", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ThrowEvent841"):
                opp_val = getattr(value, "BPMN2Model_ThrowEvent841", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_ThrowEvent841", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataInputRefs(self):
        return self.__dataInputRefs

    @dataInputRefs.setter
    def dataInputRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataInput__dataInputRefs", None)
        self.__dataInputRefs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputSet489"):
                    opp_val = getattr(item, "InputSet489", None)
                    
                    if opp_val == self:
                        setattr(item, "InputSet489", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputSet489"):
                    opp_val = getattr(item, "InputSet489", None)
                    
                    setattr(item, "InputSet489", self)
                    

    @property
    def DataInput(self):
        return self.__DataInput

    @DataInput.setter
    def DataInput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DataInput__DataInput", None)
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

class BPMN2Model_DataAssociation(BaseElement):

    pass
class BPMN2Model_CorrelationSubscription(BaseElement):

    pass
class BPMN2Model_CorrelationPropertyRetrievalExpression(BaseElement):

    pass
class BPMN2Model_CorrelationPropertyBinding(BaseElement):

    pass
class BPMN2Model_CorrelationProperty(RootElement):

    def __init__(self, name: str, BPMN2Model_CorrelationProperty: "BPMN2Model_DocumentRoot" = None, BPMN2Model_CorrelationProperty449: "BPMN2Model_CorrelationKey" = None, BPMN2Model_CorrelationProperty451: set["BPMN2Model_CorrelationPropertyRetrievalExpression"] = None, BPMN2Model_CorrelationProperty454: "BPMN2Model_ItemDefinition" = None, BPMN2Model_CorrelationProperty461: "BPMN2Model_CorrelationPropertyBinding" = None):
        self.name = name
        self.BPMN2Model_CorrelationProperty = BPMN2Model_CorrelationProperty
        self.BPMN2Model_CorrelationProperty449 = BPMN2Model_CorrelationProperty449
        self.BPMN2Model_CorrelationProperty451 = BPMN2Model_CorrelationProperty451 if BPMN2Model_CorrelationProperty451 is not None else set()
        self.BPMN2Model_CorrelationProperty454 = BPMN2Model_CorrelationProperty454
        self.BPMN2Model_CorrelationProperty461 = BPMN2Model_CorrelationProperty461
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_CorrelationProperty451(self):
        return self.__BPMN2Model_CorrelationProperty451

    @BPMN2Model_CorrelationProperty451.setter
    def BPMN2Model_CorrelationProperty451(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CorrelationProperty__BPMN2Model_CorrelationProperty451", None)
        self.__BPMN2Model_CorrelationProperty451 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_CorrelationPropertyRetrievalExpression452"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationPropertyRetrievalExpression452", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_CorrelationPropertyRetrievalExpression452", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_CorrelationPropertyRetrievalExpression452"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationPropertyRetrievalExpression452", None)
                    
                    setattr(item, "BPMN2Model_CorrelationPropertyRetrievalExpression452", self)
                    

    @property
    def BPMN2Model_CorrelationProperty461(self):
        return self.__BPMN2Model_CorrelationProperty461

    @BPMN2Model_CorrelationProperty461.setter
    def BPMN2Model_CorrelationProperty461(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CorrelationProperty__BPMN2Model_CorrelationProperty461", None)
        self.__BPMN2Model_CorrelationProperty461 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_CorrelationPropertyBinding460"):
                opp_val = getattr(old_value, "BPMN2Model_CorrelationPropertyBinding460", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_CorrelationPropertyBinding460", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_CorrelationPropertyBinding460"):
                opp_val = getattr(value, "BPMN2Model_CorrelationPropertyBinding460", None)
                setattr(value, "BPMN2Model_CorrelationPropertyBinding460", self)

    @property
    def BPMN2Model_CorrelationProperty454(self):
        return self.__BPMN2Model_CorrelationProperty454

    @BPMN2Model_CorrelationProperty454.setter
    def BPMN2Model_CorrelationProperty454(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CorrelationProperty__BPMN2Model_CorrelationProperty454", None)
        self.__BPMN2Model_CorrelationProperty454 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ItemDefinition455"):
                opp_val = getattr(old_value, "BPMN2Model_ItemDefinition455", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ItemDefinition455", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ItemDefinition455"):
                opp_val = getattr(value, "BPMN2Model_ItemDefinition455", None)
                setattr(value, "BPMN2Model_ItemDefinition455", self)

    @property
    def BPMN2Model_CorrelationProperty(self):
        return self.__BPMN2Model_CorrelationProperty

    @BPMN2Model_CorrelationProperty.setter
    def BPMN2Model_CorrelationProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CorrelationProperty__BPMN2Model_CorrelationProperty", None)
        self.__BPMN2Model_CorrelationProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot74"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot74"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot74", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_CorrelationProperty449(self):
        return self.__BPMN2Model_CorrelationProperty449

    @BPMN2Model_CorrelationProperty449.setter
    def BPMN2Model_CorrelationProperty449(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CorrelationProperty__BPMN2Model_CorrelationProperty449", None)
        self.__BPMN2Model_CorrelationProperty449 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_CorrelationKey448"):
                opp_val = getattr(old_value, "BPMN2Model_CorrelationKey448", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_CorrelationKey448"):
                opp_val = getattr(value, "BPMN2Model_CorrelationKey448", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_CorrelationKey448", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_CorrelationKey(BaseElement):

    def __init__(self, name: str, BPMN2Model_CorrelationKey: "BPMN2Model_DocumentRoot" = None, BPMN2Model_CorrelationKey372: "BPMN2Model_ChoreographyActivity" = None, BPMN2Model_CorrelationKey402: "BPMN2Model_Collaboration" = None, BPMN2Model_CorrelationKey446: "BPMN2Model_ConversationNode" = None, BPMN2Model_CorrelationKey448: set["BPMN2Model_CorrelationProperty"] = None, BPMN2Model_CorrelationKey473: "BPMN2Model_CorrelationSubscription" = None):
        self.name = name
        self.BPMN2Model_CorrelationKey = BPMN2Model_CorrelationKey
        self.BPMN2Model_CorrelationKey372 = BPMN2Model_CorrelationKey372
        self.BPMN2Model_CorrelationKey402 = BPMN2Model_CorrelationKey402
        self.BPMN2Model_CorrelationKey446 = BPMN2Model_CorrelationKey446
        self.BPMN2Model_CorrelationKey448 = BPMN2Model_CorrelationKey448 if BPMN2Model_CorrelationKey448 is not None else set()
        self.BPMN2Model_CorrelationKey473 = BPMN2Model_CorrelationKey473
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_CorrelationKey402(self):
        return self.__BPMN2Model_CorrelationKey402

    @BPMN2Model_CorrelationKey402.setter
    def BPMN2Model_CorrelationKey402(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CorrelationKey__BPMN2Model_CorrelationKey402", None)
        self.__BPMN2Model_CorrelationKey402 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Collaboration401"):
                opp_val = getattr(old_value, "BPMN2Model_Collaboration401", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Collaboration401"):
                opp_val = getattr(value, "BPMN2Model_Collaboration401", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_Collaboration401", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_CorrelationKey446(self):
        return self.__BPMN2Model_CorrelationKey446

    @BPMN2Model_CorrelationKey446.setter
    def BPMN2Model_CorrelationKey446(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CorrelationKey__BPMN2Model_CorrelationKey446", None)
        self.__BPMN2Model_CorrelationKey446 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ConversationNode445"):
                opp_val = getattr(old_value, "BPMN2Model_ConversationNode445", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ConversationNode445"):
                opp_val = getattr(value, "BPMN2Model_ConversationNode445", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_ConversationNode445", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_CorrelationKey372(self):
        return self.__BPMN2Model_CorrelationKey372

    @BPMN2Model_CorrelationKey372.setter
    def BPMN2Model_CorrelationKey372(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CorrelationKey__BPMN2Model_CorrelationKey372", None)
        self.__BPMN2Model_CorrelationKey372 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ChoreographyActivity371"):
                opp_val = getattr(old_value, "BPMN2Model_ChoreographyActivity371", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ChoreographyActivity371"):
                opp_val = getattr(value, "BPMN2Model_ChoreographyActivity371", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_ChoreographyActivity371", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_CorrelationKey(self):
        return self.__BPMN2Model_CorrelationKey

    @BPMN2Model_CorrelationKey.setter
    def BPMN2Model_CorrelationKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CorrelationKey__BPMN2Model_CorrelationKey", None)
        self.__BPMN2Model_CorrelationKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot72"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot72", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot72"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot72", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot72", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_CorrelationKey473(self):
        return self.__BPMN2Model_CorrelationKey473

    @BPMN2Model_CorrelationKey473.setter
    def BPMN2Model_CorrelationKey473(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CorrelationKey__BPMN2Model_CorrelationKey473", None)
        self.__BPMN2Model_CorrelationKey473 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_CorrelationSubscription472"):
                opp_val = getattr(old_value, "BPMN2Model_CorrelationSubscription472", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_CorrelationSubscription472", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_CorrelationSubscription472"):
                opp_val = getattr(value, "BPMN2Model_CorrelationSubscription472", None)
                setattr(value, "BPMN2Model_CorrelationSubscription472", self)

    @property
    def BPMN2Model_CorrelationKey448(self):
        return self.__BPMN2Model_CorrelationKey448

    @BPMN2Model_CorrelationKey448.setter
    def BPMN2Model_CorrelationKey448(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CorrelationKey__BPMN2Model_CorrelationKey448", None)
        self.__BPMN2Model_CorrelationKey448 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_CorrelationProperty449"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationProperty449", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_CorrelationProperty449", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_CorrelationProperty449"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationProperty449", None)
                    
                    setattr(item, "BPMN2Model_CorrelationProperty449", self)
                    

class BPMN2Model_ConversationLink(BaseElement):

    def __init__(self, name: str, BPMN2Model_ConversationLink: "BPMN2Model_DocumentRoot" = None, BPMN2Model_ConversationLink408: "BPMN2Model_Collaboration" = None, BPMN2Model_ConversationLink434: "BPMN2Model_InteractionNode" = None, BPMN2Model_ConversationLink436: "BPMN2Model_InteractionNode" = None, BPMN2Model_ConversationLink608: "BPMN2Model_InteractionNode" = None, BPMN2Model_ConversationLink611: "BPMN2Model_InteractionNode" = None):
        self.name = name
        self.BPMN2Model_ConversationLink = BPMN2Model_ConversationLink
        self.BPMN2Model_ConversationLink408 = BPMN2Model_ConversationLink408
        self.BPMN2Model_ConversationLink434 = BPMN2Model_ConversationLink434
        self.BPMN2Model_ConversationLink436 = BPMN2Model_ConversationLink436
        self.BPMN2Model_ConversationLink608 = BPMN2Model_ConversationLink608
        self.BPMN2Model_ConversationLink611 = BPMN2Model_ConversationLink611
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_ConversationLink408(self):
        return self.__BPMN2Model_ConversationLink408

    @BPMN2Model_ConversationLink408.setter
    def BPMN2Model_ConversationLink408(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ConversationLink__BPMN2Model_ConversationLink408", None)
        self.__BPMN2Model_ConversationLink408 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Collaboration407"):
                opp_val = getattr(old_value, "BPMN2Model_Collaboration407", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Collaboration407"):
                opp_val = getattr(value, "BPMN2Model_Collaboration407", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_Collaboration407", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_ConversationLink436(self):
        return self.__BPMN2Model_ConversationLink436

    @BPMN2Model_ConversationLink436.setter
    def BPMN2Model_ConversationLink436(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ConversationLink__BPMN2Model_ConversationLink436", None)
        self.__BPMN2Model_ConversationLink436 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_InteractionNode437"):
                opp_val = getattr(old_value, "BPMN2Model_InteractionNode437", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_InteractionNode437", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_InteractionNode437"):
                opp_val = getattr(value, "BPMN2Model_InteractionNode437", None)
                setattr(value, "BPMN2Model_InteractionNode437", self)

    @property
    def BPMN2Model_ConversationLink608(self):
        return self.__BPMN2Model_ConversationLink608

    @BPMN2Model_ConversationLink608.setter
    def BPMN2Model_ConversationLink608(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ConversationLink__BPMN2Model_ConversationLink608", None)
        self.__BPMN2Model_ConversationLink608 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_InteractionNode607"):
                opp_val = getattr(old_value, "BPMN2Model_InteractionNode607", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_InteractionNode607"):
                opp_val = getattr(value, "BPMN2Model_InteractionNode607", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_InteractionNode607", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_ConversationLink(self):
        return self.__BPMN2Model_ConversationLink

    @BPMN2Model_ConversationLink.setter
    def BPMN2Model_ConversationLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ConversationLink__BPMN2Model_ConversationLink", None)
        self.__BPMN2Model_ConversationLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot70"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot70"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot70", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_ConversationLink434(self):
        return self.__BPMN2Model_ConversationLink434

    @BPMN2Model_ConversationLink434.setter
    def BPMN2Model_ConversationLink434(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ConversationLink__BPMN2Model_ConversationLink434", None)
        self.__BPMN2Model_ConversationLink434 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_InteractionNode"):
                opp_val = getattr(old_value, "BPMN2Model_InteractionNode", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_InteractionNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_InteractionNode"):
                opp_val = getattr(value, "BPMN2Model_InteractionNode", None)
                setattr(value, "BPMN2Model_InteractionNode", self)

    @property
    def BPMN2Model_ConversationLink611(self):
        return self.__BPMN2Model_ConversationLink611

    @BPMN2Model_ConversationLink611.setter
    def BPMN2Model_ConversationLink611(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ConversationLink__BPMN2Model_ConversationLink611", None)
        self.__BPMN2Model_ConversationLink611 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_InteractionNode610"):
                opp_val = getattr(old_value, "BPMN2Model_InteractionNode610", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_InteractionNode610"):
                opp_val = getattr(value, "BPMN2Model_InteractionNode610", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_InteractionNode610", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_Conversation(ConversationNode):

    pass
class BPMN2Model_ConditionalEventDefinition(EventDefinition):

    pass
class BPMN2Model_ComplexGateway(Gateway):

    pass
class BPMN2Model_ComplexBehaviorDefinition(BaseElement):

    pass
class BPMN2Model_CompensateEventDefinition(EventDefinition):

    def __init__(self, waitForCompletion: bool, BPMN2Model_CompensateEventDefinition: "BPMN2Model_DocumentRoot" = None, BPMN2Model_CompensateEventDefinition410: "BPMN2Model_Activity" = None):
        self.waitForCompletion = waitForCompletion
        self.BPMN2Model_CompensateEventDefinition = BPMN2Model_CompensateEventDefinition
        self.BPMN2Model_CompensateEventDefinition410 = BPMN2Model_CompensateEventDefinition410
        
    @property
    def waitForCompletion(self) -> bool:
        return self.__waitForCompletion

    @waitForCompletion.setter
    def waitForCompletion(self, waitForCompletion: bool):
        self.__waitForCompletion = waitForCompletion

    @property
    def BPMN2Model_CompensateEventDefinition410(self):
        return self.__BPMN2Model_CompensateEventDefinition410

    @BPMN2Model_CompensateEventDefinition410.setter
    def BPMN2Model_CompensateEventDefinition410(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CompensateEventDefinition__BPMN2Model_CompensateEventDefinition410", None)
        self.__BPMN2Model_CompensateEventDefinition410 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Activity411"):
                opp_val = getattr(old_value, "BPMN2Model_Activity411", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Activity411", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Activity411"):
                opp_val = getattr(value, "BPMN2Model_Activity411", None)
                setattr(value, "BPMN2Model_Activity411", self)

    @property
    def BPMN2Model_CompensateEventDefinition(self):
        return self.__BPMN2Model_CompensateEventDefinition

    @BPMN2Model_CompensateEventDefinition.setter
    def BPMN2Model_CompensateEventDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CompensateEventDefinition__BPMN2Model_CompensateEventDefinition", None)
        self.__BPMN2Model_CompensateEventDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot58"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot58"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot58", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_ChoreographyTask(ChoreographyActivity):

    pass
class BPMN2Model_ChoreographyActivity(FlowNode):

    def __init__(self, loopType: str, BPMN2Model_ChoreographyActivity: "BPMN2Model_DocumentRoot" = None, BPMN2Model_ChoreographyActivity368: set["BPMN2Model_Participant"] = None, BPMN2Model_ChoreographyActivity371: set["BPMN2Model_CorrelationKey"] = None, BPMN2Model_ChoreographyActivity374: "BPMN2Model_Participant" = None):
        self.loopType = loopType
        self.BPMN2Model_ChoreographyActivity = BPMN2Model_ChoreographyActivity
        self.BPMN2Model_ChoreographyActivity368 = BPMN2Model_ChoreographyActivity368 if BPMN2Model_ChoreographyActivity368 is not None else set()
        self.BPMN2Model_ChoreographyActivity371 = BPMN2Model_ChoreographyActivity371 if BPMN2Model_ChoreographyActivity371 is not None else set()
        self.BPMN2Model_ChoreographyActivity374 = BPMN2Model_ChoreographyActivity374
        
    @property
    def loopType(self) -> str:
        return self.__loopType

    @loopType.setter
    def loopType(self, loopType: str):
        self.__loopType = loopType

    @property
    def BPMN2Model_ChoreographyActivity371(self):
        return self.__BPMN2Model_ChoreographyActivity371

    @BPMN2Model_ChoreographyActivity371.setter
    def BPMN2Model_ChoreographyActivity371(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ChoreographyActivity__BPMN2Model_ChoreographyActivity371", None)
        self.__BPMN2Model_ChoreographyActivity371 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_CorrelationKey372"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationKey372", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_CorrelationKey372", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_CorrelationKey372"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationKey372", None)
                    
                    setattr(item, "BPMN2Model_CorrelationKey372", self)
                    

    @property
    def BPMN2Model_ChoreographyActivity368(self):
        return self.__BPMN2Model_ChoreographyActivity368

    @BPMN2Model_ChoreographyActivity368.setter
    def BPMN2Model_ChoreographyActivity368(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ChoreographyActivity__BPMN2Model_ChoreographyActivity368", None)
        self.__BPMN2Model_ChoreographyActivity368 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Participant369"):
                    opp_val = getattr(item, "BPMN2Model_Participant369", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Participant369", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Participant369"):
                    opp_val = getattr(item, "BPMN2Model_Participant369", None)
                    
                    setattr(item, "BPMN2Model_Participant369", self)
                    

    @property
    def BPMN2Model_ChoreographyActivity374(self):
        return self.__BPMN2Model_ChoreographyActivity374

    @BPMN2Model_ChoreographyActivity374.setter
    def BPMN2Model_ChoreographyActivity374(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ChoreographyActivity__BPMN2Model_ChoreographyActivity374", None)
        self.__BPMN2Model_ChoreographyActivity374 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Participant375"):
                opp_val = getattr(old_value, "BPMN2Model_Participant375", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Participant375", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Participant375"):
                opp_val = getattr(value, "BPMN2Model_Participant375", None)
                setattr(value, "BPMN2Model_Participant375", self)

    @property
    def BPMN2Model_ChoreographyActivity(self):
        return self.__BPMN2Model_ChoreographyActivity

    @BPMN2Model_ChoreographyActivity.setter
    def BPMN2Model_ChoreographyActivity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ChoreographyActivity__BPMN2Model_ChoreographyActivity", None)
        self.__BPMN2Model_ChoreographyActivity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot54"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot54"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot54", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_Collaboration(RootElement):

    def __init__(self, isClosed: bool, name: str, BPMN2Model_Collaboration: "BPMN2Model_DocumentRoot" = None, BPMN2Model_Collaboration336: "BPMN2Model_CallConversation" = None, BPMN2Model_Collaboration380: set["BPMN2Model_Participant"] = None, BPMN2Model_Collaboration383: set["BPMN2Model_MessageFlow"] = None, BPMN2Model_Collaboration386: set["BPMN2Model_Artifact"] = None, BPMN2Model_Collaboration389: set["BPMN2Model_ConversationNode"] = None, BPMN2Model_Collaboration392: "BPMN2Model_ConversationAssociation" = None, BPMN2Model_Collaboration395: set["BPMN2Model_ParticipantAssociation"] = None, BPMN2Model_Collaboration398: set["BPMN2Model_MessageFlowAssociation"] = None, BPMN2Model_Collaboration401: set["BPMN2Model_CorrelationKey"] = None, BPMN2Model_Collaboration404: set["BPMN2Model_Choreography"] = None, BPMN2Model_Collaboration407: set["BPMN2Model_ConversationLink"] = None, BPMN2Model_Collaboration766: "BPMN2Model_Process" = None):
        self.isClosed = isClosed
        self.name = name
        self.BPMN2Model_Collaboration = BPMN2Model_Collaboration
        self.BPMN2Model_Collaboration336 = BPMN2Model_Collaboration336
        self.BPMN2Model_Collaboration380 = BPMN2Model_Collaboration380 if BPMN2Model_Collaboration380 is not None else set()
        self.BPMN2Model_Collaboration383 = BPMN2Model_Collaboration383 if BPMN2Model_Collaboration383 is not None else set()
        self.BPMN2Model_Collaboration386 = BPMN2Model_Collaboration386 if BPMN2Model_Collaboration386 is not None else set()
        self.BPMN2Model_Collaboration389 = BPMN2Model_Collaboration389 if BPMN2Model_Collaboration389 is not None else set()
        self.BPMN2Model_Collaboration392 = BPMN2Model_Collaboration392
        self.BPMN2Model_Collaboration395 = BPMN2Model_Collaboration395 if BPMN2Model_Collaboration395 is not None else set()
        self.BPMN2Model_Collaboration398 = BPMN2Model_Collaboration398 if BPMN2Model_Collaboration398 is not None else set()
        self.BPMN2Model_Collaboration401 = BPMN2Model_Collaboration401 if BPMN2Model_Collaboration401 is not None else set()
        self.BPMN2Model_Collaboration404 = BPMN2Model_Collaboration404 if BPMN2Model_Collaboration404 is not None else set()
        self.BPMN2Model_Collaboration407 = BPMN2Model_Collaboration407 if BPMN2Model_Collaboration407 is not None else set()
        self.BPMN2Model_Collaboration766 = BPMN2Model_Collaboration766
        
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
    def BPMN2Model_Collaboration392(self):
        return self.__BPMN2Model_Collaboration392

    @BPMN2Model_Collaboration392.setter
    def BPMN2Model_Collaboration392(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Collaboration__BPMN2Model_Collaboration392", None)
        self.__BPMN2Model_Collaboration392 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ConversationAssociation393"):
                opp_val = getattr(old_value, "BPMN2Model_ConversationAssociation393", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ConversationAssociation393", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ConversationAssociation393"):
                opp_val = getattr(value, "BPMN2Model_ConversationAssociation393", None)
                setattr(value, "BPMN2Model_ConversationAssociation393", self)

    @property
    def BPMN2Model_Collaboration395(self):
        return self.__BPMN2Model_Collaboration395

    @BPMN2Model_Collaboration395.setter
    def BPMN2Model_Collaboration395(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Collaboration__BPMN2Model_Collaboration395", None)
        self.__BPMN2Model_Collaboration395 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ParticipantAssociation396"):
                    opp_val = getattr(item, "BPMN2Model_ParticipantAssociation396", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ParticipantAssociation396", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ParticipantAssociation396"):
                    opp_val = getattr(item, "BPMN2Model_ParticipantAssociation396", None)
                    
                    setattr(item, "BPMN2Model_ParticipantAssociation396", self)
                    

    @property
    def BPMN2Model_Collaboration766(self):
        return self.__BPMN2Model_Collaboration766

    @BPMN2Model_Collaboration766.setter
    def BPMN2Model_Collaboration766(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Collaboration__BPMN2Model_Collaboration766", None)
        self.__BPMN2Model_Collaboration766 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Process765"):
                opp_val = getattr(old_value, "BPMN2Model_Process765", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Process765", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Process765"):
                opp_val = getattr(value, "BPMN2Model_Process765", None)
                setattr(value, "BPMN2Model_Process765", self)

    @property
    def BPMN2Model_Collaboration398(self):
        return self.__BPMN2Model_Collaboration398

    @BPMN2Model_Collaboration398.setter
    def BPMN2Model_Collaboration398(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Collaboration__BPMN2Model_Collaboration398", None)
        self.__BPMN2Model_Collaboration398 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_MessageFlowAssociation399"):
                    opp_val = getattr(item, "BPMN2Model_MessageFlowAssociation399", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_MessageFlowAssociation399", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_MessageFlowAssociation399"):
                    opp_val = getattr(item, "BPMN2Model_MessageFlowAssociation399", None)
                    
                    setattr(item, "BPMN2Model_MessageFlowAssociation399", self)
                    

    @property
    def BPMN2Model_Collaboration407(self):
        return self.__BPMN2Model_Collaboration407

    @BPMN2Model_Collaboration407.setter
    def BPMN2Model_Collaboration407(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Collaboration__BPMN2Model_Collaboration407", None)
        self.__BPMN2Model_Collaboration407 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ConversationLink408"):
                    opp_val = getattr(item, "BPMN2Model_ConversationLink408", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ConversationLink408", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ConversationLink408"):
                    opp_val = getattr(item, "BPMN2Model_ConversationLink408", None)
                    
                    setattr(item, "BPMN2Model_ConversationLink408", self)
                    

    @property
    def BPMN2Model_Collaboration336(self):
        return self.__BPMN2Model_Collaboration336

    @BPMN2Model_Collaboration336.setter
    def BPMN2Model_Collaboration336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Collaboration__BPMN2Model_Collaboration336", None)
        self.__BPMN2Model_Collaboration336 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_CallConversation335"):
                opp_val = getattr(old_value, "BPMN2Model_CallConversation335", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_CallConversation335", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_CallConversation335"):
                opp_val = getattr(value, "BPMN2Model_CallConversation335", None)
                setattr(value, "BPMN2Model_CallConversation335", self)

    @property
    def BPMN2Model_Collaboration401(self):
        return self.__BPMN2Model_Collaboration401

    @BPMN2Model_Collaboration401.setter
    def BPMN2Model_Collaboration401(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Collaboration__BPMN2Model_Collaboration401", None)
        self.__BPMN2Model_Collaboration401 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_CorrelationKey402"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationKey402", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_CorrelationKey402", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_CorrelationKey402"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationKey402", None)
                    
                    setattr(item, "BPMN2Model_CorrelationKey402", self)
                    

    @property
    def BPMN2Model_Collaboration389(self):
        return self.__BPMN2Model_Collaboration389

    @BPMN2Model_Collaboration389.setter
    def BPMN2Model_Collaboration389(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Collaboration__BPMN2Model_Collaboration389", None)
        self.__BPMN2Model_Collaboration389 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ConversationNode390"):
                    opp_val = getattr(item, "BPMN2Model_ConversationNode390", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ConversationNode390", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ConversationNode390"):
                    opp_val = getattr(item, "BPMN2Model_ConversationNode390", None)
                    
                    setattr(item, "BPMN2Model_ConversationNode390", self)
                    

    @property
    def BPMN2Model_Collaboration383(self):
        return self.__BPMN2Model_Collaboration383

    @BPMN2Model_Collaboration383.setter
    def BPMN2Model_Collaboration383(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Collaboration__BPMN2Model_Collaboration383", None)
        self.__BPMN2Model_Collaboration383 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_MessageFlow384"):
                    opp_val = getattr(item, "BPMN2Model_MessageFlow384", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_MessageFlow384", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_MessageFlow384"):
                    opp_val = getattr(item, "BPMN2Model_MessageFlow384", None)
                    
                    setattr(item, "BPMN2Model_MessageFlow384", self)
                    

    @property
    def BPMN2Model_Collaboration386(self):
        return self.__BPMN2Model_Collaboration386

    @BPMN2Model_Collaboration386.setter
    def BPMN2Model_Collaboration386(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Collaboration__BPMN2Model_Collaboration386", None)
        self.__BPMN2Model_Collaboration386 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Artifact387"):
                    opp_val = getattr(item, "BPMN2Model_Artifact387", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Artifact387", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Artifact387"):
                    opp_val = getattr(item, "BPMN2Model_Artifact387", None)
                    
                    setattr(item, "BPMN2Model_Artifact387", self)
                    

    @property
    def BPMN2Model_Collaboration(self):
        return self.__BPMN2Model_Collaboration

    @BPMN2Model_Collaboration.setter
    def BPMN2Model_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Collaboration__BPMN2Model_Collaboration", None)
        self.__BPMN2Model_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot52"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot52"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot52", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Collaboration380(self):
        return self.__BPMN2Model_Collaboration380

    @BPMN2Model_Collaboration380.setter
    def BPMN2Model_Collaboration380(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Collaboration__BPMN2Model_Collaboration380", None)
        self.__BPMN2Model_Collaboration380 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Participant381"):
                    opp_val = getattr(item, "BPMN2Model_Participant381", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Participant381", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Participant381"):
                    opp_val = getattr(item, "BPMN2Model_Participant381", None)
                    
                    setattr(item, "BPMN2Model_Participant381", self)
                    

    @property
    def BPMN2Model_Collaboration404(self):
        return self.__BPMN2Model_Collaboration404

    @BPMN2Model_Collaboration404.setter
    def BPMN2Model_Collaboration404(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Collaboration__BPMN2Model_Collaboration404", None)
        self.__BPMN2Model_Collaboration404 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Choreography405"):
                    opp_val = getattr(item, "BPMN2Model_Choreography405", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Choreography405", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Choreography405"):
                    opp_val = getattr(item, "BPMN2Model_Choreography405", None)
                    
                    setattr(item, "BPMN2Model_Choreography405", self)
                    

class BPMN2Model_Choreography(Collaboration, FlowElementsContainer):

    pass
class BPMN2Model_CategoryValue(BaseElement):

    def __init__(self, value: str, BPMN2Model_CategoryValue: "BPMN2Model_DocumentRoot" = None, BPMN2Model_CategoryValue363: "BPMN2Model_Category" = None, BPMN2Model_CategoryValue365: set["BPMN2Model_FlowElement"] = None, BPMN2Model_CategoryValue549: "BPMN2Model_FlowElement" = None, BPMN2Model_CategoryValue573: "BPMN2Model_Group" = None):
        self.value = value
        self.BPMN2Model_CategoryValue = BPMN2Model_CategoryValue
        self.BPMN2Model_CategoryValue363 = BPMN2Model_CategoryValue363
        self.BPMN2Model_CategoryValue365 = BPMN2Model_CategoryValue365 if BPMN2Model_CategoryValue365 is not None else set()
        self.BPMN2Model_CategoryValue549 = BPMN2Model_CategoryValue549
        self.BPMN2Model_CategoryValue573 = BPMN2Model_CategoryValue573
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def BPMN2Model_CategoryValue549(self):
        return self.__BPMN2Model_CategoryValue549

    @BPMN2Model_CategoryValue549.setter
    def BPMN2Model_CategoryValue549(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CategoryValue__BPMN2Model_CategoryValue549", None)
        self.__BPMN2Model_CategoryValue549 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_FlowElement548"):
                opp_val = getattr(old_value, "BPMN2Model_FlowElement548", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_FlowElement548"):
                opp_val = getattr(value, "BPMN2Model_FlowElement548", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_FlowElement548", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_CategoryValue363(self):
        return self.__BPMN2Model_CategoryValue363

    @BPMN2Model_CategoryValue363.setter
    def BPMN2Model_CategoryValue363(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CategoryValue__BPMN2Model_CategoryValue363", None)
        self.__BPMN2Model_CategoryValue363 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Category362"):
                opp_val = getattr(old_value, "BPMN2Model_Category362", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Category362"):
                opp_val = getattr(value, "BPMN2Model_Category362", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_Category362", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_CategoryValue365(self):
        return self.__BPMN2Model_CategoryValue365

    @BPMN2Model_CategoryValue365.setter
    def BPMN2Model_CategoryValue365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CategoryValue__BPMN2Model_CategoryValue365", None)
        self.__BPMN2Model_CategoryValue365 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_FlowElement366"):
                    opp_val = getattr(item, "BPMN2Model_FlowElement366", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_FlowElement366", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_FlowElement366"):
                    opp_val = getattr(item, "BPMN2Model_FlowElement366", None)
                    
                    setattr(item, "BPMN2Model_FlowElement366", self)
                    

    @property
    def BPMN2Model_CategoryValue(self):
        return self.__BPMN2Model_CategoryValue

    @BPMN2Model_CategoryValue.setter
    def BPMN2Model_CategoryValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CategoryValue__BPMN2Model_CategoryValue", None)
        self.__BPMN2Model_CategoryValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot48"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot48"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot48", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_CategoryValue573(self):
        return self.__BPMN2Model_CategoryValue573

    @BPMN2Model_CategoryValue573.setter
    def BPMN2Model_CategoryValue573(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CategoryValue__BPMN2Model_CategoryValue573", None)
        self.__BPMN2Model_CategoryValue573 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Group572"):
                opp_val = getattr(old_value, "BPMN2Model_Group572", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Group572", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Group572"):
                opp_val = getattr(value, "BPMN2Model_Group572", None)
                setattr(value, "BPMN2Model_Group572", self)

class BPMN2Model_Category(RootElement):

    def __init__(self, name: str, BPMN2Model_Category: "BPMN2Model_DocumentRoot" = None, BPMN2Model_Category362: set["BPMN2Model_CategoryValue"] = None):
        self.name = name
        self.BPMN2Model_Category = BPMN2Model_Category
        self.BPMN2Model_Category362 = BPMN2Model_Category362 if BPMN2Model_Category362 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_Category362(self):
        return self.__BPMN2Model_Category362

    @BPMN2Model_Category362.setter
    def BPMN2Model_Category362(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Category__BPMN2Model_Category362", None)
        self.__BPMN2Model_Category362 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_CategoryValue363"):
                    opp_val = getattr(item, "BPMN2Model_CategoryValue363", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_CategoryValue363", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_CategoryValue363"):
                    opp_val = getattr(item, "BPMN2Model_CategoryValue363", None)
                    
                    setattr(item, "BPMN2Model_CategoryValue363", self)
                    

    @property
    def BPMN2Model_Category(self):
        return self.__BPMN2Model_Category

    @BPMN2Model_Category.setter
    def BPMN2Model_Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Category__BPMN2Model_Category", None)
        self.__BPMN2Model_Category = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot46"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot46"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot46", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_CatchEvent(Event):

    def __init__(self, parallelMultiple: bool, BPMN2Model_CatchEvent: "BPMN2Model_DocumentRoot" = None, BPMN2Model_CatchEvent347: set["BPMN2Model_DataOutput"] = None, BPMN2Model_CatchEvent350: set["BPMN2Model_DataOutputAssociation"] = None, BPMN2Model_CatchEvent353: "BPMN2Model_OutputSet" = None, BPMN2Model_CatchEvent356: set["BPMN2Model_EventDefinition"] = None, BPMN2Model_CatchEvent359: set["BPMN2Model_EventDefinition"] = None):
        self.parallelMultiple = parallelMultiple
        self.BPMN2Model_CatchEvent = BPMN2Model_CatchEvent
        self.BPMN2Model_CatchEvent347 = BPMN2Model_CatchEvent347 if BPMN2Model_CatchEvent347 is not None else set()
        self.BPMN2Model_CatchEvent350 = BPMN2Model_CatchEvent350 if BPMN2Model_CatchEvent350 is not None else set()
        self.BPMN2Model_CatchEvent353 = BPMN2Model_CatchEvent353
        self.BPMN2Model_CatchEvent356 = BPMN2Model_CatchEvent356 if BPMN2Model_CatchEvent356 is not None else set()
        self.BPMN2Model_CatchEvent359 = BPMN2Model_CatchEvent359 if BPMN2Model_CatchEvent359 is not None else set()
        
    @property
    def parallelMultiple(self) -> bool:
        return self.__parallelMultiple

    @parallelMultiple.setter
    def parallelMultiple(self, parallelMultiple: bool):
        self.__parallelMultiple = parallelMultiple

    @property
    def BPMN2Model_CatchEvent359(self):
        return self.__BPMN2Model_CatchEvent359

    @BPMN2Model_CatchEvent359.setter
    def BPMN2Model_CatchEvent359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CatchEvent__BPMN2Model_CatchEvent359", None)
        self.__BPMN2Model_CatchEvent359 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_EventDefinition360"):
                    opp_val = getattr(item, "BPMN2Model_EventDefinition360", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_EventDefinition360", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_EventDefinition360"):
                    opp_val = getattr(item, "BPMN2Model_EventDefinition360", None)
                    
                    setattr(item, "BPMN2Model_EventDefinition360", self)
                    

    @property
    def BPMN2Model_CatchEvent356(self):
        return self.__BPMN2Model_CatchEvent356

    @BPMN2Model_CatchEvent356.setter
    def BPMN2Model_CatchEvent356(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CatchEvent__BPMN2Model_CatchEvent356", None)
        self.__BPMN2Model_CatchEvent356 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_EventDefinition357"):
                    opp_val = getattr(item, "BPMN2Model_EventDefinition357", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_EventDefinition357", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_EventDefinition357"):
                    opp_val = getattr(item, "BPMN2Model_EventDefinition357", None)
                    
                    setattr(item, "BPMN2Model_EventDefinition357", self)
                    

    @property
    def BPMN2Model_CatchEvent353(self):
        return self.__BPMN2Model_CatchEvent353

    @BPMN2Model_CatchEvent353.setter
    def BPMN2Model_CatchEvent353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CatchEvent__BPMN2Model_CatchEvent353", None)
        self.__BPMN2Model_CatchEvent353 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_OutputSet354"):
                opp_val = getattr(old_value, "BPMN2Model_OutputSet354", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_OutputSet354", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_OutputSet354"):
                opp_val = getattr(value, "BPMN2Model_OutputSet354", None)
                setattr(value, "BPMN2Model_OutputSet354", self)

    @property
    def BPMN2Model_CatchEvent347(self):
        return self.__BPMN2Model_CatchEvent347

    @BPMN2Model_CatchEvent347.setter
    def BPMN2Model_CatchEvent347(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CatchEvent__BPMN2Model_CatchEvent347", None)
        self.__BPMN2Model_CatchEvent347 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_DataOutput348"):
                    opp_val = getattr(item, "BPMN2Model_DataOutput348", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_DataOutput348", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_DataOutput348"):
                    opp_val = getattr(item, "BPMN2Model_DataOutput348", None)
                    
                    setattr(item, "BPMN2Model_DataOutput348", self)
                    

    @property
    def BPMN2Model_CatchEvent350(self):
        return self.__BPMN2Model_CatchEvent350

    @BPMN2Model_CatchEvent350.setter
    def BPMN2Model_CatchEvent350(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CatchEvent__BPMN2Model_CatchEvent350", None)
        self.__BPMN2Model_CatchEvent350 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_DataOutputAssociation351"):
                    opp_val = getattr(item, "BPMN2Model_DataOutputAssociation351", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_DataOutputAssociation351", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_DataOutputAssociation351"):
                    opp_val = getattr(item, "BPMN2Model_DataOutputAssociation351", None)
                    
                    setattr(item, "BPMN2Model_DataOutputAssociation351", self)
                    

    @property
    def BPMN2Model_CatchEvent(self):
        return self.__BPMN2Model_CatchEvent

    @BPMN2Model_CatchEvent.setter
    def BPMN2Model_CatchEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CatchEvent__BPMN2Model_CatchEvent", None)
        self.__BPMN2Model_CatchEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot44"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot44"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot44", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_RootElement(BaseElement):

    pass
class BPMN2Model_EventDefinition(RootElement):

    pass
class BPMN2Model_CancelEventDefinition(EventDefinition):

    pass
class BPMN2Model_ConversationNode(BaseElement, InteractionNode):

    def __init__(self, name: str, BPMN2Model_ConversationNode: "BPMN2Model_DocumentRoot" = None, BPMN2Model_ConversationNode390: "BPMN2Model_Collaboration" = None, BPMN2Model_ConversationNode429: "BPMN2Model_ConversationAssociation" = None, BPMN2Model_ConversationNode432: "BPMN2Model_ConversationAssociation" = None, BPMN2Model_ConversationNode439: set["BPMN2Model_Participant"] = None, BPMN2Model_ConversationNode442: set["BPMN2Model_MessageFlow"] = None, BPMN2Model_ConversationNode445: set["BPMN2Model_CorrelationKey"] = None, BPMN2Model_ConversationNode836: "BPMN2Model_SubConversation" = None):
        self.name = name
        self.BPMN2Model_ConversationNode = BPMN2Model_ConversationNode
        self.BPMN2Model_ConversationNode390 = BPMN2Model_ConversationNode390
        self.BPMN2Model_ConversationNode429 = BPMN2Model_ConversationNode429
        self.BPMN2Model_ConversationNode432 = BPMN2Model_ConversationNode432
        self.BPMN2Model_ConversationNode439 = BPMN2Model_ConversationNode439 if BPMN2Model_ConversationNode439 is not None else set()
        self.BPMN2Model_ConversationNode442 = BPMN2Model_ConversationNode442 if BPMN2Model_ConversationNode442 is not None else set()
        self.BPMN2Model_ConversationNode445 = BPMN2Model_ConversationNode445 if BPMN2Model_ConversationNode445 is not None else set()
        self.BPMN2Model_ConversationNode836 = BPMN2Model_ConversationNode836
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_ConversationNode445(self):
        return self.__BPMN2Model_ConversationNode445

    @BPMN2Model_ConversationNode445.setter
    def BPMN2Model_ConversationNode445(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ConversationNode__BPMN2Model_ConversationNode445", None)
        self.__BPMN2Model_ConversationNode445 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_CorrelationKey446"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationKey446", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_CorrelationKey446", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_CorrelationKey446"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationKey446", None)
                    
                    setattr(item, "BPMN2Model_CorrelationKey446", self)
                    

    @property
    def BPMN2Model_ConversationNode439(self):
        return self.__BPMN2Model_ConversationNode439

    @BPMN2Model_ConversationNode439.setter
    def BPMN2Model_ConversationNode439(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ConversationNode__BPMN2Model_ConversationNode439", None)
        self.__BPMN2Model_ConversationNode439 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Participant440"):
                    opp_val = getattr(item, "BPMN2Model_Participant440", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Participant440", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Participant440"):
                    opp_val = getattr(item, "BPMN2Model_Participant440", None)
                    
                    setattr(item, "BPMN2Model_Participant440", self)
                    

    @property
    def BPMN2Model_ConversationNode836(self):
        return self.__BPMN2Model_ConversationNode836

    @BPMN2Model_ConversationNode836.setter
    def BPMN2Model_ConversationNode836(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ConversationNode__BPMN2Model_ConversationNode836", None)
        self.__BPMN2Model_ConversationNode836 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_SubConversation835"):
                opp_val = getattr(old_value, "BPMN2Model_SubConversation835", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_SubConversation835"):
                opp_val = getattr(value, "BPMN2Model_SubConversation835", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_SubConversation835", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_ConversationNode390(self):
        return self.__BPMN2Model_ConversationNode390

    @BPMN2Model_ConversationNode390.setter
    def BPMN2Model_ConversationNode390(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ConversationNode__BPMN2Model_ConversationNode390", None)
        self.__BPMN2Model_ConversationNode390 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Collaboration389"):
                opp_val = getattr(old_value, "BPMN2Model_Collaboration389", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Collaboration389"):
                opp_val = getattr(value, "BPMN2Model_Collaboration389", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_Collaboration389", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_ConversationNode442(self):
        return self.__BPMN2Model_ConversationNode442

    @BPMN2Model_ConversationNode442.setter
    def BPMN2Model_ConversationNode442(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ConversationNode__BPMN2Model_ConversationNode442", None)
        self.__BPMN2Model_ConversationNode442 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_MessageFlow443"):
                    opp_val = getattr(item, "BPMN2Model_MessageFlow443", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_MessageFlow443", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_MessageFlow443"):
                    opp_val = getattr(item, "BPMN2Model_MessageFlow443", None)
                    
                    setattr(item, "BPMN2Model_MessageFlow443", self)
                    

    @property
    def BPMN2Model_ConversationNode429(self):
        return self.__BPMN2Model_ConversationNode429

    @BPMN2Model_ConversationNode429.setter
    def BPMN2Model_ConversationNode429(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ConversationNode__BPMN2Model_ConversationNode429", None)
        self.__BPMN2Model_ConversationNode429 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ConversationAssociation428"):
                opp_val = getattr(old_value, "BPMN2Model_ConversationAssociation428", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ConversationAssociation428", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ConversationAssociation428"):
                opp_val = getattr(value, "BPMN2Model_ConversationAssociation428", None)
                setattr(value, "BPMN2Model_ConversationAssociation428", self)

    @property
    def BPMN2Model_ConversationNode432(self):
        return self.__BPMN2Model_ConversationNode432

    @BPMN2Model_ConversationNode432.setter
    def BPMN2Model_ConversationNode432(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ConversationNode__BPMN2Model_ConversationNode432", None)
        self.__BPMN2Model_ConversationNode432 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ConversationAssociation431"):
                opp_val = getattr(old_value, "BPMN2Model_ConversationAssociation431", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ConversationAssociation431", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ConversationAssociation431"):
                opp_val = getattr(value, "BPMN2Model_ConversationAssociation431", None)
                setattr(value, "BPMN2Model_ConversationAssociation431", self)

    @property
    def BPMN2Model_ConversationNode(self):
        return self.__BPMN2Model_ConversationNode

    @BPMN2Model_ConversationNode.setter
    def BPMN2Model_ConversationNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ConversationNode__BPMN2Model_ConversationNode", None)
        self.__BPMN2Model_ConversationNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot36"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot36"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot36", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_CallConversation(ConversationNode):

    pass
class BPMN2Model_CallChoreography(ChoreographyActivity):

    pass
class BPMN2Model_CallActivity(Activity):

    pass
class BPMN2Model_CallableElement(RootElement):

    def __init__(self, name: str, BPMN2Model_CallableElement: "BPMN2Model_DocumentRoot" = None, BPMN2Model_CallableElement324: "BPMN2Model_CallActivity" = None, BPMN2Model_CallableElement338: set["BPMN2Model_Interface"] = None, BPMN2Model_CallableElement341: "BPMN2Model_InputOutputSpecification" = None, BPMN2Model_CallableElement344: set["BPMN2Model_InputOutputBinding"] = None):
        self.name = name
        self.BPMN2Model_CallableElement = BPMN2Model_CallableElement
        self.BPMN2Model_CallableElement324 = BPMN2Model_CallableElement324
        self.BPMN2Model_CallableElement338 = BPMN2Model_CallableElement338 if BPMN2Model_CallableElement338 is not None else set()
        self.BPMN2Model_CallableElement341 = BPMN2Model_CallableElement341
        self.BPMN2Model_CallableElement344 = BPMN2Model_CallableElement344 if BPMN2Model_CallableElement344 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_CallableElement338(self):
        return self.__BPMN2Model_CallableElement338

    @BPMN2Model_CallableElement338.setter
    def BPMN2Model_CallableElement338(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CallableElement__BPMN2Model_CallableElement338", None)
        self.__BPMN2Model_CallableElement338 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Interface339"):
                    opp_val = getattr(item, "BPMN2Model_Interface339", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Interface339", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Interface339"):
                    opp_val = getattr(item, "BPMN2Model_Interface339", None)
                    
                    setattr(item, "BPMN2Model_Interface339", self)
                    

    @property
    def BPMN2Model_CallableElement341(self):
        return self.__BPMN2Model_CallableElement341

    @BPMN2Model_CallableElement341.setter
    def BPMN2Model_CallableElement341(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CallableElement__BPMN2Model_CallableElement341", None)
        self.__BPMN2Model_CallableElement341 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_InputOutputSpecification342"):
                opp_val = getattr(old_value, "BPMN2Model_InputOutputSpecification342", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_InputOutputSpecification342", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_InputOutputSpecification342"):
                opp_val = getattr(value, "BPMN2Model_InputOutputSpecification342", None)
                setattr(value, "BPMN2Model_InputOutputSpecification342", self)

    @property
    def BPMN2Model_CallableElement344(self):
        return self.__BPMN2Model_CallableElement344

    @BPMN2Model_CallableElement344.setter
    def BPMN2Model_CallableElement344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CallableElement__BPMN2Model_CallableElement344", None)
        self.__BPMN2Model_CallableElement344 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_InputOutputBinding345"):
                    opp_val = getattr(item, "BPMN2Model_InputOutputBinding345", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_InputOutputBinding345", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_InputOutputBinding345"):
                    opp_val = getattr(item, "BPMN2Model_InputOutputBinding345", None)
                    
                    setattr(item, "BPMN2Model_InputOutputBinding345", self)
                    

    @property
    def BPMN2Model_CallableElement324(self):
        return self.__BPMN2Model_CallableElement324

    @BPMN2Model_CallableElement324.setter
    def BPMN2Model_CallableElement324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CallableElement__BPMN2Model_CallableElement324", None)
        self.__BPMN2Model_CallableElement324 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_CallActivity323"):
                opp_val = getattr(old_value, "BPMN2Model_CallActivity323", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_CallActivity323", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_CallActivity323"):
                opp_val = getattr(value, "BPMN2Model_CallActivity323", None)
                setattr(value, "BPMN2Model_CallActivity323", self)

    @property
    def BPMN2Model_CallableElement(self):
        return self.__BPMN2Model_CallableElement

    @BPMN2Model_CallableElement.setter
    def BPMN2Model_CallableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_CallableElement__BPMN2Model_CallableElement", None)
        self.__BPMN2Model_CallableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot28"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot28"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot28", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_BusinessRuleTask(Task):

    def __init__(self, implementation: str, BPMN2Model_BusinessRuleTask: "BPMN2Model_DocumentRoot" = None):
        self.implementation = implementation
        self.BPMN2Model_BusinessRuleTask = BPMN2Model_BusinessRuleTask
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def BPMN2Model_BusinessRuleTask(self):
        return self.__BPMN2Model_BusinessRuleTask

    @BPMN2Model_BusinessRuleTask.setter
    def BPMN2Model_BusinessRuleTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_BusinessRuleTask__BPMN2Model_BusinessRuleTask", None)
        self.__BPMN2Model_BusinessRuleTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot26"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot26"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot26", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_BoundaryEvent(CatchEvent):

    def __init__(self, cancelActivity: bool, BPMN2Model_BoundaryEvent: "BPMN2Model_DocumentRoot" = None, BoundaryEvent: "BPMN2Model_Activity" = None, boundaryEventRefs: "BPMN2Model_Activity" = None):
        self.cancelActivity = cancelActivity
        self.BPMN2Model_BoundaryEvent = BPMN2Model_BoundaryEvent
        self.BoundaryEvent = BoundaryEvent
        self.boundaryEventRefs = boundaryEventRefs
        
    @property
    def cancelActivity(self) -> bool:
        return self.__cancelActivity

    @cancelActivity.setter
    def cancelActivity(self, cancelActivity: bool):
        self.__cancelActivity = cancelActivity

    @property
    def BPMN2Model_BoundaryEvent(self):
        return self.__BPMN2Model_BoundaryEvent

    @BPMN2Model_BoundaryEvent.setter
    def BPMN2Model_BoundaryEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_BoundaryEvent__BPMN2Model_BoundaryEvent", None)
        self.__BPMN2Model_BoundaryEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot24"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot24"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot24", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def boundaryEventRefs(self):
        return self.__boundaryEventRefs

    @boundaryEventRefs.setter
    def boundaryEventRefs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_BoundaryEvent__boundaryEventRefs", None)
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
        old_value = getattr(self, f"_BPMN2Model_BoundaryEvent__BoundaryEvent", None)
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

class BPMN2Model_Auditing(BaseElement):

    pass
class BPMN2Model_Association(Artifact):

    def __init__(self, associationDirection: str, BPMN2Model_Association: "BPMN2Model_DocumentRoot" = None, BPMN2Model_Association308: "BPMN2Model_BaseElement" = None, BPMN2Model_Association311: "BPMN2Model_BaseElement" = None):
        self.associationDirection = associationDirection
        self.BPMN2Model_Association = BPMN2Model_Association
        self.BPMN2Model_Association308 = BPMN2Model_Association308
        self.BPMN2Model_Association311 = BPMN2Model_Association311
        
    @property
    def associationDirection(self) -> str:
        return self.__associationDirection

    @associationDirection.setter
    def associationDirection(self, associationDirection: str):
        self.__associationDirection = associationDirection

    @property
    def BPMN2Model_Association(self):
        return self.__BPMN2Model_Association

    @BPMN2Model_Association.setter
    def BPMN2Model_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Association__BPMN2Model_Association", None)
        self.__BPMN2Model_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot15"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot15"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot15", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Association308(self):
        return self.__BPMN2Model_Association308

    @BPMN2Model_Association308.setter
    def BPMN2Model_Association308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Association__BPMN2Model_Association308", None)
        self.__BPMN2Model_Association308 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_BaseElement309"):
                opp_val = getattr(old_value, "BPMN2Model_BaseElement309", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_BaseElement309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_BaseElement309"):
                opp_val = getattr(value, "BPMN2Model_BaseElement309", None)
                setattr(value, "BPMN2Model_BaseElement309", self)

    @property
    def BPMN2Model_Association311(self):
        return self.__BPMN2Model_Association311

    @BPMN2Model_Association311.setter
    def BPMN2Model_Association311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Association__BPMN2Model_Association311", None)
        self.__BPMN2Model_Association311 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_BaseElement312"):
                opp_val = getattr(old_value, "BPMN2Model_BaseElement312", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_BaseElement312", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_BaseElement312"):
                opp_val = getattr(value, "BPMN2Model_BaseElement312", None)
                setattr(value, "BPMN2Model_BaseElement312", self)

class BPMN2Model_Assignment(BaseElement):

    pass
class BPMN2Model_Artifact(BaseElement):

    pass
class BPMN2Model_FlowElement(BaseElement):

    def __init__(self, name: str, BPMN2Model_FlowElement: "BPMN2Model_DocumentRoot" = None, BPMN2Model_FlowElement366: "BPMN2Model_CategoryValue" = None, BPMN2Model_FlowElement542: "BPMN2Model_Auditing" = None, BPMN2Model_FlowElement545: "BPMN2Model_Monitoring" = None, BPMN2Model_FlowElement548: set["BPMN2Model_CategoryValue"] = None, BPMN2Model_FlowElement554: "BPMN2Model_FlowElementsContainer" = None):
        self.name = name
        self.BPMN2Model_FlowElement = BPMN2Model_FlowElement
        self.BPMN2Model_FlowElement366 = BPMN2Model_FlowElement366
        self.BPMN2Model_FlowElement542 = BPMN2Model_FlowElement542
        self.BPMN2Model_FlowElement545 = BPMN2Model_FlowElement545
        self.BPMN2Model_FlowElement548 = BPMN2Model_FlowElement548 if BPMN2Model_FlowElement548 is not None else set()
        self.BPMN2Model_FlowElement554 = BPMN2Model_FlowElement554
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_FlowElement542(self):
        return self.__BPMN2Model_FlowElement542

    @BPMN2Model_FlowElement542.setter
    def BPMN2Model_FlowElement542(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_FlowElement__BPMN2Model_FlowElement542", None)
        self.__BPMN2Model_FlowElement542 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Auditing543"):
                opp_val = getattr(old_value, "BPMN2Model_Auditing543", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Auditing543", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Auditing543"):
                opp_val = getattr(value, "BPMN2Model_Auditing543", None)
                setattr(value, "BPMN2Model_Auditing543", self)

    @property
    def BPMN2Model_FlowElement545(self):
        return self.__BPMN2Model_FlowElement545

    @BPMN2Model_FlowElement545.setter
    def BPMN2Model_FlowElement545(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_FlowElement__BPMN2Model_FlowElement545", None)
        self.__BPMN2Model_FlowElement545 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Monitoring546"):
                opp_val = getattr(old_value, "BPMN2Model_Monitoring546", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Monitoring546", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Monitoring546"):
                opp_val = getattr(value, "BPMN2Model_Monitoring546", None)
                setattr(value, "BPMN2Model_Monitoring546", self)

    @property
    def BPMN2Model_FlowElement366(self):
        return self.__BPMN2Model_FlowElement366

    @BPMN2Model_FlowElement366.setter
    def BPMN2Model_FlowElement366(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_FlowElement__BPMN2Model_FlowElement366", None)
        self.__BPMN2Model_FlowElement366 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_CategoryValue365"):
                opp_val = getattr(old_value, "BPMN2Model_CategoryValue365", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_CategoryValue365"):
                opp_val = getattr(value, "BPMN2Model_CategoryValue365", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_CategoryValue365", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_FlowElement554(self):
        return self.__BPMN2Model_FlowElement554

    @BPMN2Model_FlowElement554.setter
    def BPMN2Model_FlowElement554(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_FlowElement__BPMN2Model_FlowElement554", None)
        self.__BPMN2Model_FlowElement554 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_FlowElementsContainer553"):
                opp_val = getattr(old_value, "BPMN2Model_FlowElementsContainer553", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_FlowElementsContainer553"):
                opp_val = getattr(value, "BPMN2Model_FlowElementsContainer553", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_FlowElementsContainer553", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_FlowElement(self):
        return self.__BPMN2Model_FlowElement

    @BPMN2Model_FlowElement.setter
    def BPMN2Model_FlowElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_FlowElement__BPMN2Model_FlowElement", None)
        self.__BPMN2Model_FlowElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot9"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot9"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot9", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_FlowElement548(self):
        return self.__BPMN2Model_FlowElement548

    @BPMN2Model_FlowElement548.setter
    def BPMN2Model_FlowElement548(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_FlowElement__BPMN2Model_FlowElement548", None)
        self.__BPMN2Model_FlowElement548 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_CategoryValue549"):
                    opp_val = getattr(item, "BPMN2Model_CategoryValue549", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_CategoryValue549", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_CategoryValue549"):
                    opp_val = getattr(item, "BPMN2Model_CategoryValue549", None)
                    
                    setattr(item, "BPMN2Model_CategoryValue549", self)
                    

class BPMN2Model_AdHocSubProcess(SubProcess):

    def __init__(self, cancelRemainingInstances: bool, ordering: str, BPMN2Model_AdHocSubProcess: "BPMN2Model_DocumentRoot" = None, BPMN2Model_AdHocSubProcess299: "BPMN2Model_Expression" = None):
        self.cancelRemainingInstances = cancelRemainingInstances
        self.ordering = ordering
        self.BPMN2Model_AdHocSubProcess = BPMN2Model_AdHocSubProcess
        self.BPMN2Model_AdHocSubProcess299 = BPMN2Model_AdHocSubProcess299
        
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
    def BPMN2Model_AdHocSubProcess(self):
        return self.__BPMN2Model_AdHocSubProcess

    @BPMN2Model_AdHocSubProcess.setter
    def BPMN2Model_AdHocSubProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_AdHocSubProcess__BPMN2Model_AdHocSubProcess", None)
        self.__BPMN2Model_AdHocSubProcess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot7"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot7"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot7", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_AdHocSubProcess299(self):
        return self.__BPMN2Model_AdHocSubProcess299

    @BPMN2Model_AdHocSubProcess299.setter
    def BPMN2Model_AdHocSubProcess299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_AdHocSubProcess__BPMN2Model_AdHocSubProcess299", None)
        self.__BPMN2Model_AdHocSubProcess299 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Expression300"):
                opp_val = getattr(old_value, "BPMN2Model_Expression300", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Expression300", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Expression300"):
                opp_val = getattr(value, "BPMN2Model_Expression300", None)
                setattr(value, "BPMN2Model_Expression300", self)

class BPMN2Model_Activity(FlowNode):

    def __init__(self, completionQuantity: int, isForCompensation: bool, startQuantity: int, BPMN2Model_Activity: "BPMN2Model_DocumentRoot" = None, BPMN2Model_Activity277: "BPMN2Model_InputOutputSpecification" = None, attachedToRef: set["BPMN2Model_BoundaryEvent"] = None, BPMN2Model_Activity281: set["BPMN2Model_Property"] = None, BPMN2Model_Activity284: set["BPMN2Model_DataInputAssociation"] = None, BPMN2Model_Activity287: set["BPMN2Model_DataOutputAssociation"] = None, BPMN2Model_Activity290: set["BPMN2Model_ResourceRole"] = None, BPMN2Model_Activity293: "BPMN2Model_LoopCharacteristics" = None, BPMN2Model_Activity296: "BPMN2Model_SequenceFlow" = None, Activity: "BPMN2Model_BoundaryEvent" = None, BPMN2Model_Activity411: "BPMN2Model_CompensateEventDefinition" = None):
        self.completionQuantity = completionQuantity
        self.isForCompensation = isForCompensation
        self.startQuantity = startQuantity
        self.BPMN2Model_Activity = BPMN2Model_Activity
        self.BPMN2Model_Activity277 = BPMN2Model_Activity277
        self.attachedToRef = attachedToRef if attachedToRef is not None else set()
        self.BPMN2Model_Activity281 = BPMN2Model_Activity281 if BPMN2Model_Activity281 is not None else set()
        self.BPMN2Model_Activity284 = BPMN2Model_Activity284 if BPMN2Model_Activity284 is not None else set()
        self.BPMN2Model_Activity287 = BPMN2Model_Activity287 if BPMN2Model_Activity287 is not None else set()
        self.BPMN2Model_Activity290 = BPMN2Model_Activity290 if BPMN2Model_Activity290 is not None else set()
        self.BPMN2Model_Activity293 = BPMN2Model_Activity293
        self.BPMN2Model_Activity296 = BPMN2Model_Activity296
        self.Activity = Activity
        self.BPMN2Model_Activity411 = BPMN2Model_Activity411
        
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
    def BPMN2Model_Activity281(self):
        return self.__BPMN2Model_Activity281

    @BPMN2Model_Activity281.setter
    def BPMN2Model_Activity281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Activity__BPMN2Model_Activity281", None)
        self.__BPMN2Model_Activity281 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Property282"):
                    opp_val = getattr(item, "BPMN2Model_Property282", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Property282", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Property282"):
                    opp_val = getattr(item, "BPMN2Model_Property282", None)
                    
                    setattr(item, "BPMN2Model_Property282", self)
                    

    @property
    def BPMN2Model_Activity287(self):
        return self.__BPMN2Model_Activity287

    @BPMN2Model_Activity287.setter
    def BPMN2Model_Activity287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Activity__BPMN2Model_Activity287", None)
        self.__BPMN2Model_Activity287 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_DataOutputAssociation288"):
                    opp_val = getattr(item, "BPMN2Model_DataOutputAssociation288", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_DataOutputAssociation288", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_DataOutputAssociation288"):
                    opp_val = getattr(item, "BPMN2Model_DataOutputAssociation288", None)
                    
                    setattr(item, "BPMN2Model_DataOutputAssociation288", self)
                    

    @property
    def attachedToRef(self):
        return self.__attachedToRef

    @attachedToRef.setter
    def attachedToRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Activity__attachedToRef", None)
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
    def BPMN2Model_Activity411(self):
        return self.__BPMN2Model_Activity411

    @BPMN2Model_Activity411.setter
    def BPMN2Model_Activity411(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Activity__BPMN2Model_Activity411", None)
        self.__BPMN2Model_Activity411 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_CompensateEventDefinition410"):
                opp_val = getattr(old_value, "BPMN2Model_CompensateEventDefinition410", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_CompensateEventDefinition410", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_CompensateEventDefinition410"):
                opp_val = getattr(value, "BPMN2Model_CompensateEventDefinition410", None)
                setattr(value, "BPMN2Model_CompensateEventDefinition410", self)

    @property
    def BPMN2Model_Activity296(self):
        return self.__BPMN2Model_Activity296

    @BPMN2Model_Activity296.setter
    def BPMN2Model_Activity296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Activity__BPMN2Model_Activity296", None)
        self.__BPMN2Model_Activity296 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_SequenceFlow297"):
                opp_val = getattr(old_value, "BPMN2Model_SequenceFlow297", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_SequenceFlow297", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_SequenceFlow297"):
                opp_val = getattr(value, "BPMN2Model_SequenceFlow297", None)
                setattr(value, "BPMN2Model_SequenceFlow297", self)

    @property
    def BPMN2Model_Activity(self):
        return self.__BPMN2Model_Activity

    @BPMN2Model_Activity.setter
    def BPMN2Model_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Activity__BPMN2Model_Activity", None)
        self.__BPMN2Model_Activity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot5"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot5"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot5", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Activity(self):
        return self.__Activity

    @Activity.setter
    def Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Activity__Activity", None)
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
    def BPMN2Model_Activity284(self):
        return self.__BPMN2Model_Activity284

    @BPMN2Model_Activity284.setter
    def BPMN2Model_Activity284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Activity__BPMN2Model_Activity284", None)
        self.__BPMN2Model_Activity284 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_DataInputAssociation285"):
                    opp_val = getattr(item, "BPMN2Model_DataInputAssociation285", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_DataInputAssociation285", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_DataInputAssociation285"):
                    opp_val = getattr(item, "BPMN2Model_DataInputAssociation285", None)
                    
                    setattr(item, "BPMN2Model_DataInputAssociation285", self)
                    

    @property
    def BPMN2Model_Activity290(self):
        return self.__BPMN2Model_Activity290

    @BPMN2Model_Activity290.setter
    def BPMN2Model_Activity290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Activity__BPMN2Model_Activity290", None)
        self.__BPMN2Model_Activity290 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ResourceRole291"):
                    opp_val = getattr(item, "BPMN2Model_ResourceRole291", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ResourceRole291", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ResourceRole291"):
                    opp_val = getattr(item, "BPMN2Model_ResourceRole291", None)
                    
                    setattr(item, "BPMN2Model_ResourceRole291", self)
                    

    @property
    def BPMN2Model_Activity277(self):
        return self.__BPMN2Model_Activity277

    @BPMN2Model_Activity277.setter
    def BPMN2Model_Activity277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Activity__BPMN2Model_Activity277", None)
        self.__BPMN2Model_Activity277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_InputOutputSpecification278"):
                opp_val = getattr(old_value, "BPMN2Model_InputOutputSpecification278", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_InputOutputSpecification278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_InputOutputSpecification278"):
                opp_val = getattr(value, "BPMN2Model_InputOutputSpecification278", None)
                setattr(value, "BPMN2Model_InputOutputSpecification278", self)

    @property
    def BPMN2Model_Activity293(self):
        return self.__BPMN2Model_Activity293

    @BPMN2Model_Activity293.setter
    def BPMN2Model_Activity293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Activity__BPMN2Model_Activity293", None)
        self.__BPMN2Model_Activity293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_LoopCharacteristics294"):
                opp_val = getattr(old_value, "BPMN2Model_LoopCharacteristics294", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_LoopCharacteristics294", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_LoopCharacteristics294"):
                opp_val = getattr(value, "BPMN2Model_LoopCharacteristics294", None)
                setattr(value, "BPMN2Model_LoopCharacteristics294", self)

class BPMN2Model_EStringToStringMapEntry:

    pass
class BPMNBase:

    pass
class BPMN2Model_Import(BPMNBase):

    def __init__(self, importType: str, location: str, namespace: str, BPMN2Model_Import: "BPMN2Model_DocumentRoot" = None, BPMN2Model_Import503: "BPMN2Model_Definitions" = None, BPMN2Model_Import626: "BPMN2Model_ItemDefinition" = None):
        self.importType = importType
        self.location = location
        self.namespace = namespace
        self.BPMN2Model_Import = BPMN2Model_Import
        self.BPMN2Model_Import503 = BPMN2Model_Import503
        self.BPMN2Model_Import626 = BPMN2Model_Import626
        
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
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def BPMN2Model_Import503(self):
        return self.__BPMN2Model_Import503

    @BPMN2Model_Import503.setter
    def BPMN2Model_Import503(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Import__BPMN2Model_Import503", None)
        self.__BPMN2Model_Import503 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Definitions502"):
                opp_val = getattr(old_value, "BPMN2Model_Definitions502", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Definitions502"):
                opp_val = getattr(value, "BPMN2Model_Definitions502", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_Definitions502", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Import(self):
        return self.__BPMN2Model_Import

    @BPMN2Model_Import.setter
    def BPMN2Model_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Import__BPMN2Model_Import", None)
        self.__BPMN2Model_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot160"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot160", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot160"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot160", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot160", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Import626(self):
        return self.__BPMN2Model_Import626

    @BPMN2Model_Import626.setter
    def BPMN2Model_Import626(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Import__BPMN2Model_Import626", None)
        self.__BPMN2Model_Import626 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ItemDefinition625"):
                opp_val = getattr(old_value, "BPMN2Model_ItemDefinition625", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ItemDefinition625", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ItemDefinition625"):
                opp_val = getattr(value, "BPMN2Model_ItemDefinition625", None)
                setattr(value, "BPMN2Model_ItemDefinition625", self)

class BPMN2Model_ResourceParameterBinding(BPMNBase):

    pass
class BPMN2Model_Extension(BPMNBase):

    def __init__(self, mustUnderstand: bool, xsdDefinition: str, BPMN2Model_Extension: "BPMN2Model_DocumentRoot" = None, BPMN2Model_Extension506: "BPMN2Model_Definitions" = None, BPMN2Model_Extension532: "BPMN2Model_ExtensionDefinition" = None):
        self.mustUnderstand = mustUnderstand
        self.xsdDefinition = xsdDefinition
        self.BPMN2Model_Extension = BPMN2Model_Extension
        self.BPMN2Model_Extension506 = BPMN2Model_Extension506
        self.BPMN2Model_Extension532 = BPMN2Model_Extension532
        
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
    def BPMN2Model_Extension506(self):
        return self.__BPMN2Model_Extension506

    @BPMN2Model_Extension506.setter
    def BPMN2Model_Extension506(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Extension__BPMN2Model_Extension506", None)
        self.__BPMN2Model_Extension506 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Definitions505"):
                opp_val = getattr(old_value, "BPMN2Model_Definitions505", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Definitions505"):
                opp_val = getattr(value, "BPMN2Model_Definitions505", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_Definitions505", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Extension(self):
        return self.__BPMN2Model_Extension

    @BPMN2Model_Extension.setter
    def BPMN2Model_Extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Extension__BPMN2Model_Extension", None)
        self.__BPMN2Model_Extension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot126"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot126", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot126"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot126", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot126", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_Extension532(self):
        return self.__BPMN2Model_Extension532

    @BPMN2Model_Extension532.setter
    def BPMN2Model_Extension532(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Extension__BPMN2Model_Extension532", None)
        self.__BPMN2Model_Extension532 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ExtensionDefinition533"):
                opp_val = getattr(old_value, "BPMN2Model_ExtensionDefinition533", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ExtensionDefinition533", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ExtensionDefinition533"):
                opp_val = getattr(value, "BPMN2Model_ExtensionDefinition533", None)
                setattr(value, "BPMN2Model_ExtensionDefinition533", self)

class BPMN2Model_ExtensionDefinition(BPMNBase):

    def __init__(self, name: str, BPMN2Model_ExtensionDefinition: "BPMN2Model_BaseElement" = None, BPMN2Model_ExtensionDefinition533: "BPMN2Model_Extension" = None, ExtensionDefinition: "BPMN2Model_ExtensionAttributeDefinition" = None, extensionDefinition: set["BPMN2Model_ExtensionAttributeDefinition"] = None):
        self.name = name
        self.BPMN2Model_ExtensionDefinition = BPMN2Model_ExtensionDefinition
        self.BPMN2Model_ExtensionDefinition533 = BPMN2Model_ExtensionDefinition533
        self.ExtensionDefinition = ExtensionDefinition
        self.extensionDefinition = extensionDefinition if extensionDefinition is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_ExtensionDefinition(self):
        return self.__BPMN2Model_ExtensionDefinition

    @BPMN2Model_ExtensionDefinition.setter
    def BPMN2Model_ExtensionDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ExtensionDefinition__BPMN2Model_ExtensionDefinition", None)
        self.__BPMN2Model_ExtensionDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_BaseElement320"):
                opp_val = getattr(old_value, "BPMN2Model_BaseElement320", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_BaseElement320"):
                opp_val = getattr(value, "BPMN2Model_BaseElement320", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_BaseElement320", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_ExtensionDefinition533(self):
        return self.__BPMN2Model_ExtensionDefinition533

    @BPMN2Model_ExtensionDefinition533.setter
    def BPMN2Model_ExtensionDefinition533(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ExtensionDefinition__BPMN2Model_ExtensionDefinition533", None)
        self.__BPMN2Model_ExtensionDefinition533 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Extension532"):
                opp_val = getattr(old_value, "BPMN2Model_Extension532", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Extension532", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Extension532"):
                opp_val = getattr(value, "BPMN2Model_Extension532", None)
                setattr(value, "BPMN2Model_Extension532", self)

    @property
    def ExtensionDefinition(self):
        return self.__ExtensionDefinition

    @ExtensionDefinition.setter
    def ExtensionDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ExtensionDefinition__ExtensionDefinition", None)
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
    def extensionDefinition(self):
        return self.__extensionDefinition

    @extensionDefinition.setter
    def extensionDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ExtensionDefinition__extensionDefinition", None)
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
                    

class BPMN2Model_ExtensionAttributeValue(BPMNBase):

    def __init__(self, value: str, BPMN2Model_ExtensionAttributeValue: "BPMN2Model_DocumentRoot" = None, BPMN2Model_ExtensionAttributeValue315: "BPMN2Model_BaseElement" = None, BPMN2Model_ExtensionAttributeValue536: "BPMN2Model_EObject" = None, BPMN2Model_ExtensionAttributeValue539: "BPMN2Model_ExtensionAttributeDefinition" = None):
        self.value = value
        self.BPMN2Model_ExtensionAttributeValue = BPMN2Model_ExtensionAttributeValue
        self.BPMN2Model_ExtensionAttributeValue315 = BPMN2Model_ExtensionAttributeValue315
        self.BPMN2Model_ExtensionAttributeValue536 = BPMN2Model_ExtensionAttributeValue536
        self.BPMN2Model_ExtensionAttributeValue539 = BPMN2Model_ExtensionAttributeValue539
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def BPMN2Model_ExtensionAttributeValue315(self):
        return self.__BPMN2Model_ExtensionAttributeValue315

    @BPMN2Model_ExtensionAttributeValue315.setter
    def BPMN2Model_ExtensionAttributeValue315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ExtensionAttributeValue__BPMN2Model_ExtensionAttributeValue315", None)
        self.__BPMN2Model_ExtensionAttributeValue315 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_BaseElement314"):
                opp_val = getattr(old_value, "BPMN2Model_BaseElement314", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_BaseElement314"):
                opp_val = getattr(value, "BPMN2Model_BaseElement314", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_BaseElement314", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_ExtensionAttributeValue539(self):
        return self.__BPMN2Model_ExtensionAttributeValue539

    @BPMN2Model_ExtensionAttributeValue539.setter
    def BPMN2Model_ExtensionAttributeValue539(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ExtensionAttributeValue__BPMN2Model_ExtensionAttributeValue539", None)
        self.__BPMN2Model_ExtensionAttributeValue539 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ExtensionAttributeDefinition"):
                opp_val = getattr(old_value, "BPMN2Model_ExtensionAttributeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ExtensionAttributeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ExtensionAttributeDefinition"):
                opp_val = getattr(value, "BPMN2Model_ExtensionAttributeDefinition", None)
                setattr(value, "BPMN2Model_ExtensionAttributeDefinition", self)

    @property
    def BPMN2Model_ExtensionAttributeValue(self):
        return self.__BPMN2Model_ExtensionAttributeValue

    @BPMN2Model_ExtensionAttributeValue.setter
    def BPMN2Model_ExtensionAttributeValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ExtensionAttributeValue__BPMN2Model_ExtensionAttributeValue", None)
        self.__BPMN2Model_ExtensionAttributeValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot128"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot128", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot128"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot128", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot128", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_ExtensionAttributeValue536(self):
        return self.__BPMN2Model_ExtensionAttributeValue536

    @BPMN2Model_ExtensionAttributeValue536.setter
    def BPMN2Model_ExtensionAttributeValue536(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ExtensionAttributeValue__BPMN2Model_ExtensionAttributeValue536", None)
        self.__BPMN2Model_ExtensionAttributeValue536 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_EObject537"):
                opp_val = getattr(old_value, "BPMN2Model_EObject537", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_EObject537", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_EObject537"):
                opp_val = getattr(value, "BPMN2Model_EObject537", None)
                setattr(value, "BPMN2Model_EObject537", self)

class BPMN2Model_ParticipantMultiplicity(BPMNBase):

    def __init__(self, maximum: int, minimum: int, BPMN2Model_ParticipantMultiplicity: "BPMN2Model_DocumentRoot" = None, BPMN2Model_ParticipantMultiplicity727: "BPMN2Model_Participant" = None):
        self.maximum = maximum
        self.minimum = minimum
        self.BPMN2Model_ParticipantMultiplicity = BPMN2Model_ParticipantMultiplicity
        self.BPMN2Model_ParticipantMultiplicity727 = BPMN2Model_ParticipantMultiplicity727
        
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
    def BPMN2Model_ParticipantMultiplicity727(self):
        return self.__BPMN2Model_ParticipantMultiplicity727

    @BPMN2Model_ParticipantMultiplicity727.setter
    def BPMN2Model_ParticipantMultiplicity727(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ParticipantMultiplicity__BPMN2Model_ParticipantMultiplicity727", None)
        self.__BPMN2Model_ParticipantMultiplicity727 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Participant726"):
                opp_val = getattr(old_value, "BPMN2Model_Participant726", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Participant726", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Participant726"):
                opp_val = getattr(value, "BPMN2Model_Participant726", None)
                setattr(value, "BPMN2Model_Participant726", self)

    @property
    def BPMN2Model_ParticipantMultiplicity(self):
        return self.__BPMN2Model_ParticipantMultiplicity

    @BPMN2Model_ParticipantMultiplicity.setter
    def BPMN2Model_ParticipantMultiplicity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ParticipantMultiplicity__BPMN2Model_ParticipantMultiplicity", None)
        self.__BPMN2Model_ParticipantMultiplicity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot210"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot210", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot210"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot210", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot210", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_Escalation(BPMNBase):

    def __init__(self, escalationCode: str, name: str, BPMN2Model_Escalation: "BPMN2Model_DocumentRoot" = None, BPMN2Model_Escalation520: "BPMN2Model_ItemDefinition" = None, BPMN2Model_Escalation524: "BPMN2Model_EscalationEventDefinition" = None):
        self.escalationCode = escalationCode
        self.name = name
        self.BPMN2Model_Escalation = BPMN2Model_Escalation
        self.BPMN2Model_Escalation520 = BPMN2Model_Escalation520
        self.BPMN2Model_Escalation524 = BPMN2Model_Escalation524
        
    @property
    def escalationCode(self) -> str:
        return self.__escalationCode

    @escalationCode.setter
    def escalationCode(self, escalationCode: str):
        self.__escalationCode = escalationCode

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def BPMN2Model_Escalation520(self):
        return self.__BPMN2Model_Escalation520

    @BPMN2Model_Escalation520.setter
    def BPMN2Model_Escalation520(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Escalation__BPMN2Model_Escalation520", None)
        self.__BPMN2Model_Escalation520 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ItemDefinition521"):
                opp_val = getattr(old_value, "BPMN2Model_ItemDefinition521", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ItemDefinition521", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ItemDefinition521"):
                opp_val = getattr(value, "BPMN2Model_ItemDefinition521", None)
                setattr(value, "BPMN2Model_ItemDefinition521", self)

    @property
    def BPMN2Model_Escalation524(self):
        return self.__BPMN2Model_Escalation524

    @BPMN2Model_Escalation524.setter
    def BPMN2Model_Escalation524(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Escalation__BPMN2Model_Escalation524", None)
        self.__BPMN2Model_Escalation524 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_EscalationEventDefinition523"):
                opp_val = getattr(old_value, "BPMN2Model_EscalationEventDefinition523", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_EscalationEventDefinition523", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_EscalationEventDefinition523"):
                opp_val = getattr(value, "BPMN2Model_EscalationEventDefinition523", None)
                setattr(value, "BPMN2Model_EscalationEventDefinition523", self)

    @property
    def BPMN2Model_Escalation(self):
        return self.__BPMN2Model_Escalation

    @BPMN2Model_Escalation.setter
    def BPMN2Model_Escalation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_Escalation__BPMN2Model_Escalation", None)
        self.__BPMN2Model_Escalation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot114"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot114"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot114", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BPMN2Model_BaseElement(BPMNBase):

    def __init__(self, id: str, anyAttribute: str, BPMN2Model_BaseElement: "BPMN2Model_DocumentRoot" = None, BPMN2Model_BaseElement22: "BPMN2Model_DocumentRoot" = None, BPMN2Model_BaseElement309: "BPMN2Model_Association" = None, BPMN2Model_BaseElement312: "BPMN2Model_Association" = None, BPMN2Model_BaseElement314: set["BPMN2Model_ExtensionAttributeValue"] = None, BPMN2Model_BaseElement317: set["BPMN2Model_Documentation"] = None, BPMN2Model_BaseElement320: set["BPMN2Model_ExtensionDefinition"] = None, BPMN2Model_BaseElement632: "BPMN2Model_Lane" = None, BPMN2Model_BaseElement639: "BPMN2Model_Lane" = None):
        self.id = id
        self.anyAttribute = anyAttribute
        self.BPMN2Model_BaseElement = BPMN2Model_BaseElement
        self.BPMN2Model_BaseElement22 = BPMN2Model_BaseElement22
        self.BPMN2Model_BaseElement309 = BPMN2Model_BaseElement309
        self.BPMN2Model_BaseElement312 = BPMN2Model_BaseElement312
        self.BPMN2Model_BaseElement314 = BPMN2Model_BaseElement314 if BPMN2Model_BaseElement314 is not None else set()
        self.BPMN2Model_BaseElement317 = BPMN2Model_BaseElement317 if BPMN2Model_BaseElement317 is not None else set()
        self.BPMN2Model_BaseElement320 = BPMN2Model_BaseElement320 if BPMN2Model_BaseElement320 is not None else set()
        self.BPMN2Model_BaseElement632 = BPMN2Model_BaseElement632
        self.BPMN2Model_BaseElement639 = BPMN2Model_BaseElement639
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def BPMN2Model_BaseElement317(self):
        return self.__BPMN2Model_BaseElement317

    @BPMN2Model_BaseElement317.setter
    def BPMN2Model_BaseElement317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_BaseElement__BPMN2Model_BaseElement317", None)
        self.__BPMN2Model_BaseElement317 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Documentation318"):
                    opp_val = getattr(item, "BPMN2Model_Documentation318", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Documentation318", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Documentation318"):
                    opp_val = getattr(item, "BPMN2Model_Documentation318", None)
                    
                    setattr(item, "BPMN2Model_Documentation318", self)
                    

    @property
    def BPMN2Model_BaseElement312(self):
        return self.__BPMN2Model_BaseElement312

    @BPMN2Model_BaseElement312.setter
    def BPMN2Model_BaseElement312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_BaseElement__BPMN2Model_BaseElement312", None)
        self.__BPMN2Model_BaseElement312 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Association311"):
                opp_val = getattr(old_value, "BPMN2Model_Association311", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Association311", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Association311"):
                opp_val = getattr(value, "BPMN2Model_Association311", None)
                setattr(value, "BPMN2Model_Association311", self)

    @property
    def BPMN2Model_BaseElement22(self):
        return self.__BPMN2Model_BaseElement22

    @BPMN2Model_BaseElement22.setter
    def BPMN2Model_BaseElement22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_BaseElement__BPMN2Model_BaseElement22", None)
        self.__BPMN2Model_BaseElement22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot21"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot21"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot21", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_BaseElement314(self):
        return self.__BPMN2Model_BaseElement314

    @BPMN2Model_BaseElement314.setter
    def BPMN2Model_BaseElement314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_BaseElement__BPMN2Model_BaseElement314", None)
        self.__BPMN2Model_BaseElement314 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ExtensionAttributeValue315"):
                    opp_val = getattr(item, "BPMN2Model_ExtensionAttributeValue315", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ExtensionAttributeValue315", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ExtensionAttributeValue315"):
                    opp_val = getattr(item, "BPMN2Model_ExtensionAttributeValue315", None)
                    
                    setattr(item, "BPMN2Model_ExtensionAttributeValue315", self)
                    

    @property
    def BPMN2Model_BaseElement309(self):
        return self.__BPMN2Model_BaseElement309

    @BPMN2Model_BaseElement309.setter
    def BPMN2Model_BaseElement309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_BaseElement__BPMN2Model_BaseElement309", None)
        self.__BPMN2Model_BaseElement309 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Association308"):
                opp_val = getattr(old_value, "BPMN2Model_Association308", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Association308", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Association308"):
                opp_val = getattr(value, "BPMN2Model_Association308", None)
                setattr(value, "BPMN2Model_Association308", self)

    @property
    def BPMN2Model_BaseElement(self):
        return self.__BPMN2Model_BaseElement

    @BPMN2Model_BaseElement.setter
    def BPMN2Model_BaseElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_BaseElement__BPMN2Model_BaseElement", None)
        self.__BPMN2Model_BaseElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_DocumentRoot19"):
                opp_val = getattr(old_value, "BPMN2Model_DocumentRoot19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_DocumentRoot19"):
                opp_val = getattr(value, "BPMN2Model_DocumentRoot19", None)
                if opp_val is None:
                    setattr(value, "BPMN2Model_DocumentRoot19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BPMN2Model_BaseElement320(self):
        return self.__BPMN2Model_BaseElement320

    @BPMN2Model_BaseElement320.setter
    def BPMN2Model_BaseElement320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_BaseElement__BPMN2Model_BaseElement320", None)
        self.__BPMN2Model_BaseElement320 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ExtensionDefinition"):
                    opp_val = getattr(item, "BPMN2Model_ExtensionDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ExtensionDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ExtensionDefinition"):
                    opp_val = getattr(item, "BPMN2Model_ExtensionDefinition", None)
                    
                    setattr(item, "BPMN2Model_ExtensionDefinition", self)
                    

    @property
    def BPMN2Model_BaseElement632(self):
        return self.__BPMN2Model_BaseElement632

    @BPMN2Model_BaseElement632.setter
    def BPMN2Model_BaseElement632(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_BaseElement__BPMN2Model_BaseElement632", None)
        self.__BPMN2Model_BaseElement632 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Lane631"):
                opp_val = getattr(old_value, "BPMN2Model_Lane631", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Lane631", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Lane631"):
                opp_val = getattr(value, "BPMN2Model_Lane631", None)
                setattr(value, "BPMN2Model_Lane631", self)

    @property
    def BPMN2Model_BaseElement639(self):
        return self.__BPMN2Model_BaseElement639

    @BPMN2Model_BaseElement639.setter
    def BPMN2Model_BaseElement639(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_BaseElement__BPMN2Model_BaseElement639", None)
        self.__BPMN2Model_BaseElement639 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_Lane638"):
                opp_val = getattr(old_value, "BPMN2Model_Lane638", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_Lane638", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_Lane638"):
                opp_val = getattr(value, "BPMN2Model_Lane638", None)
                setattr(value, "BPMN2Model_Lane638", self)

class BPMN2Model_InputOutputBinding(BPMNBase):

    pass
class BPMN2Model_ResourceAssignmentExpression(BPMNBase):

    pass
class BPMN2Model_ExtensionAttributeDefinition(BPMNBase):

    def __init__(self, name: str, type: str, isReference: bool, extensionAttributeDefinitions: "BPMN2Model_ExtensionDefinition" = None, BPMN2Model_ExtensionAttributeDefinition: "BPMN2Model_ExtensionAttributeValue" = None, ExtensionAttributeDefinition: "BPMN2Model_ExtensionDefinition" = None):
        self.name = name
        self.type = type
        self.isReference = isReference
        self.extensionAttributeDefinitions = extensionAttributeDefinitions
        self.BPMN2Model_ExtensionAttributeDefinition = BPMN2Model_ExtensionAttributeDefinition
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
    def BPMN2Model_ExtensionAttributeDefinition(self):
        return self.__BPMN2Model_ExtensionAttributeDefinition

    @BPMN2Model_ExtensionAttributeDefinition.setter
    def BPMN2Model_ExtensionAttributeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ExtensionAttributeDefinition__BPMN2Model_ExtensionAttributeDefinition", None)
        self.__BPMN2Model_ExtensionAttributeDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMN2Model_ExtensionAttributeValue539"):
                opp_val = getattr(old_value, "BPMN2Model_ExtensionAttributeValue539", None)
                if opp_val == self:
                    setattr(old_value, "BPMN2Model_ExtensionAttributeValue539", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMN2Model_ExtensionAttributeValue539"):
                opp_val = getattr(value, "BPMN2Model_ExtensionAttributeValue539", None)
                setattr(value, "BPMN2Model_ExtensionAttributeValue539", self)

    @property
    def extensionAttributeDefinitions(self):
        return self.__extensionAttributeDefinitions

    @extensionAttributeDefinitions.setter
    def extensionAttributeDefinitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_ExtensionAttributeDefinition__extensionAttributeDefinitions", None)
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
        old_value = getattr(self, f"_BPMN2Model_ExtensionAttributeDefinition__ExtensionAttributeDefinition", None)
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

class BPMN2Model_InteractionNode(BPMNBase):

    pass
class BPMN2Model_DocumentRoot(BPMNBase):

    def __init__(self, mixed: str, BPMN2Model_DocumentRoot2: set["BPMN2Model_EStringToStringMapEntry"] = None, BPMN2Model_DocumentRoot5: set["BPMN2Model_Activity"] = None, BPMN2Model_DocumentRoot7: set["BPMN2Model_AdHocSubProcess"] = None, BPMN2Model_DocumentRoot9: set["BPMN2Model_FlowElement"] = None, BPMN2Model_DocumentRoot11: set["BPMN2Model_Artifact"] = None, BPMN2Model_DocumentRoot13: set["BPMN2Model_Assignment"] = None, BPMN2Model_DocumentRoot15: set["BPMN2Model_Association"] = None, BPMN2Model_DocumentRoot17: set["BPMN2Model_Auditing"] = None, BPMN2Model_DocumentRoot19: set["BPMN2Model_BaseElement"] = None, BPMN2Model_DocumentRoot21: set["BPMN2Model_BaseElement"] = None, BPMN2Model_DocumentRoot24: set["BPMN2Model_BoundaryEvent"] = None, BPMN2Model_DocumentRoot26: set["BPMN2Model_BusinessRuleTask"] = None, BPMN2Model_DocumentRoot28: set["BPMN2Model_CallableElement"] = None, BPMN2Model_DocumentRoot30: set["BPMN2Model_CallActivity"] = None, BPMN2Model_DocumentRoot32: set["BPMN2Model_CallChoreography"] = None, BPMN2Model_DocumentRoot34: set["BPMN2Model_CallConversation"] = None, BPMN2Model_DocumentRoot: set["BPMN2Model_EStringToStringMapEntry"] = None, BPMN2Model_DocumentRoot38: set["BPMN2Model_CancelEventDefinition"] = None, BPMN2Model_DocumentRoot40: set["BPMN2Model_EventDefinition"] = None, BPMN2Model_DocumentRoot42: set["BPMN2Model_RootElement"] = None, BPMN2Model_DocumentRoot44: set["BPMN2Model_CatchEvent"] = None, BPMN2Model_DocumentRoot46: set["BPMN2Model_Category"] = None, BPMN2Model_DocumentRoot48: set["BPMN2Model_CategoryValue"] = None, BPMN2Model_DocumentRoot50: set["BPMN2Model_Choreography"] = None, BPMN2Model_DocumentRoot52: set["BPMN2Model_Collaboration"] = None, BPMN2Model_DocumentRoot54: set["BPMN2Model_ChoreographyActivity"] = None, BPMN2Model_DocumentRoot56: set["BPMN2Model_ChoreographyTask"] = None, BPMN2Model_DocumentRoot58: set["BPMN2Model_CompensateEventDefinition"] = None, BPMN2Model_DocumentRoot60: set["BPMN2Model_ComplexBehaviorDefinition"] = None, BPMN2Model_DocumentRoot62: set["BPMN2Model_ComplexGateway"] = None, BPMN2Model_DocumentRoot64: set["BPMN2Model_ConditionalEventDefinition"] = None, BPMN2Model_DocumentRoot66: set["BPMN2Model_Conversation"] = None, BPMN2Model_DocumentRoot36: set["BPMN2Model_ConversationNode"] = None, BPMN2Model_DocumentRoot68: set["BPMN2Model_ConversationAssociation"] = None, BPMN2Model_DocumentRoot70: set["BPMN2Model_ConversationLink"] = None, BPMN2Model_DocumentRoot72: set["BPMN2Model_CorrelationKey"] = None, BPMN2Model_DocumentRoot74: set["BPMN2Model_CorrelationProperty"] = None, BPMN2Model_DocumentRoot76: set["BPMN2Model_CorrelationPropertyBinding"] = None, BPMN2Model_DocumentRoot78: set["BPMN2Model_CorrelationPropertyRetrievalExpression"] = None, BPMN2Model_DocumentRoot80: set["BPMN2Model_CorrelationSubscription"] = None, BPMN2Model_DocumentRoot82: set["BPMN2Model_DataAssociation"] = None, BPMN2Model_DocumentRoot84: set["BPMN2Model_DataInput"] = None, BPMN2Model_DocumentRoot86: set["BPMN2Model_DataInputAssociation"] = None, BPMN2Model_DocumentRoot88: set["BPMN2Model_DataObject"] = None, BPMN2Model_DocumentRoot90: set["BPMN2Model_DataObjectReference"] = None, BPMN2Model_DocumentRoot92: set["BPMN2Model_DataOutput"] = None, BPMN2Model_DocumentRoot94: set["BPMN2Model_DataOutputAssociation"] = None, BPMN2Model_DocumentRoot96: set["BPMN2Model_DataState"] = None, BPMN2Model_DocumentRoot100: set["BPMN2Model_DataStoreReference"] = None, BPMN2Model_DocumentRoot102: set["BPMN2Model_Definitions"] = None, BPMN2Model_DocumentRoot104: set["BPMN2Model_Documentation"] = None, BPMN2Model_DocumentRoot106: set["BPMN2Model_EndEvent"] = None, BPMN2Model_DocumentRoot108: set["BPMN2Model_EndPoint"] = None, BPMN2Model_DocumentRoot110: set["BPMN2Model_Error"] = None, BPMN2Model_DocumentRoot112: set["BPMN2Model_ErrorEventDefinition"] = None, BPMN2Model_DocumentRoot114: set["BPMN2Model_Escalation"] = None, BPMN2Model_DocumentRoot116: set["BPMN2Model_EscalationEventDefinition"] = None, BPMN2Model_DocumentRoot118: set["BPMN2Model_Event"] = None, BPMN2Model_DocumentRoot120: set["BPMN2Model_EventBasedGateway"] = None, BPMN2Model_DocumentRoot122: set["BPMN2Model_ExclusiveGateway"] = None, BPMN2Model_DocumentRoot124: set["BPMN2Model_Expression"] = None, BPMN2Model_DocumentRoot126: set["BPMN2Model_Extension"] = None, BPMN2Model_DocumentRoot98: set["BPMN2Model_DataStore"] = None, BPMN2Model_DocumentRoot128: set["BPMN2Model_ExtensionAttributeValue"] = None, BPMN2Model_DocumentRoot130: set["BPMN2Model_FlowNode"] = None, BPMN2Model_DocumentRoot132: set["BPMN2Model_FormalExpression"] = None, BPMN2Model_DocumentRoot134: set["BPMN2Model_Gateway"] = None, BPMN2Model_DocumentRoot136: set["BPMN2Model_GlobalBusinessRuleTask"] = None, BPMN2Model_DocumentRoot138: set["BPMN2Model_GlobalChoreographyTask"] = None, BPMN2Model_DocumentRoot140: set["BPMN2Model_GlobalConversation"] = None, BPMN2Model_DocumentRoot142: set["BPMN2Model_GlobalManualTask"] = None, BPMN2Model_DocumentRoot144: set["BPMN2Model_GlobalScriptTask"] = None, BPMN2Model_DocumentRoot146: set["BPMN2Model_GlobalTask"] = None, BPMN2Model_DocumentRoot148: set["BPMN2Model_GlobalUserTask"] = None, BPMN2Model_DocumentRoot150: set["BPMN2Model_Group"] = None, BPMN2Model_DocumentRoot152: set["BPMN2Model_HumanPerformer"] = None, BPMN2Model_DocumentRoot154: set["BPMN2Model_Performer"] = None, BPMN2Model_DocumentRoot156: set["BPMN2Model_ResourceRole"] = None, BPMN2Model_DocumentRoot158: set["BPMN2Model_ImplicitThrowEvent"] = None, BPMN2Model_DocumentRoot160: set["BPMN2Model_Import"] = None, BPMN2Model_DocumentRoot162: set["BPMN2Model_InclusiveGateway"] = None, BPMN2Model_DocumentRoot164: set["BPMN2Model_InputSet"] = None, BPMN2Model_DocumentRoot166: set["BPMN2Model_Interface"] = None, BPMN2Model_DocumentRoot168: set["BPMN2Model_IntermediateCatchEvent"] = None, BPMN2Model_DocumentRoot170: set["BPMN2Model_IntermediateThrowEvent"] = None, BPMN2Model_DocumentRoot172: set["BPMN2Model_InputOutputBinding"] = None, BPMN2Model_DocumentRoot174: set["BPMN2Model_InputOutputSpecification"] = None, BPMN2Model_DocumentRoot176: set["BPMN2Model_ItemDefinition"] = None, BPMN2Model_DocumentRoot178: set["BPMN2Model_Lane"] = None, BPMN2Model_DocumentRoot180: set["BPMN2Model_LaneSet"] = None, BPMN2Model_DocumentRoot182: set["BPMN2Model_LinkEventDefinition"] = None, BPMN2Model_DocumentRoot184: set["BPMN2Model_LoopCharacteristics"] = None, BPMN2Model_DocumentRoot186: set["BPMN2Model_ManualTask"] = None, BPMN2Model_DocumentRoot188: set["BPMN2Model_Message"] = None, BPMN2Model_DocumentRoot190: set["BPMN2Model_MessageEventDefinition"] = None, BPMN2Model_DocumentRoot192: set["BPMN2Model_MessageFlow"] = None, BPMN2Model_DocumentRoot194: set["BPMN2Model_MessageFlowAssociation"] = None, BPMN2Model_DocumentRoot196: set["BPMN2Model_Monitoring"] = None, BPMN2Model_DocumentRoot198: set["BPMN2Model_MultiInstanceLoopCharacteristics"] = None, BPMN2Model_DocumentRoot200: set["BPMN2Model_Operation"] = None, BPMN2Model_DocumentRoot202: set["BPMN2Model_OutputSet"] = None, BPMN2Model_DocumentRoot204: set["BPMN2Model_ParallelGateway"] = None, BPMN2Model_DocumentRoot206: set["BPMN2Model_Participant"] = None, BPMN2Model_DocumentRoot208: set["BPMN2Model_ParticipantAssociation"] = None, BPMN2Model_DocumentRoot212: set["BPMN2Model_PartnerEntity"] = None, BPMN2Model_DocumentRoot214: set["BPMN2Model_PartnerRole"] = None, BPMN2Model_DocumentRoot216: set["BPMN2Model_PotentialOwner"] = None, BPMN2Model_DocumentRoot218: set["BPMN2Model_Process"] = None, BPMN2Model_DocumentRoot220: set["BPMN2Model_Property"] = None, BPMN2Model_DocumentRoot222: set["BPMN2Model_ReceiveTask"] = None, BPMN2Model_DocumentRoot224: set["BPMN2Model_Relationship"] = None, BPMN2Model_DocumentRoot226: set["BPMN2Model_Rendering"] = None, BPMN2Model_DocumentRoot228: set["BPMN2Model_Resource"] = None, BPMN2Model_DocumentRoot230: set["BPMN2Model_ResourceAssignmentExpression"] = None, BPMN2Model_DocumentRoot210: set["BPMN2Model_ParticipantMultiplicity"] = None, BPMN2Model_DocumentRoot232: set["BPMN2Model_ResourceParameter"] = None, BPMN2Model_DocumentRoot234: set["BPMN2Model_ResourceParameterBinding"] = None, BPMN2Model_DocumentRoot236: set["BPMN2Model_EObject"] = None, BPMN2Model_DocumentRoot238: set["BPMN2Model_ScriptTask"] = None, BPMN2Model_DocumentRoot240: set["BPMN2Model_SendTask"] = None, BPMN2Model_DocumentRoot242: set["BPMN2Model_SequenceFlow"] = None, BPMN2Model_DocumentRoot244: set["BPMN2Model_ServiceTask"] = None, BPMN2Model_DocumentRoot246: set["BPMN2Model_Signal"] = None, BPMN2Model_DocumentRoot248: set["BPMN2Model_SignalEventDefinition"] = None, BPMN2Model_DocumentRoot250: set["BPMN2Model_StandardLoopCharacteristics"] = None, BPMN2Model_DocumentRoot252: set["BPMN2Model_StartEvent"] = None, BPMN2Model_DocumentRoot254: set["BPMN2Model_SubChoreography"] = None, BPMN2Model_DocumentRoot256: set["BPMN2Model_SubConversation"] = None, BPMN2Model_DocumentRoot258: set["BPMN2Model_SubProcess"] = None, BPMN2Model_DocumentRoot260: set["BPMN2Model_Task"] = None, BPMN2Model_DocumentRoot262: set["BPMN2Model_TerminateEventDefinition"] = None, BPMN2Model_DocumentRoot264: set["BPMN2Model_EObject"] = None, BPMN2Model_DocumentRoot267: set["BPMN2Model_TextAnnotation"] = None, BPMN2Model_DocumentRoot269: set["BPMN2Model_ThrowEvent"] = None, BPMN2Model_DocumentRoot271: set["BPMN2Model_TimerEventDefinition"] = None, BPMN2Model_DocumentRoot273: set["BPMN2Model_Transaction"] = None, BPMN2Model_DocumentRoot275: set["BPMN2Model_UserTask"] = None):
        self.mixed = mixed
        self.BPMN2Model_DocumentRoot2 = BPMN2Model_DocumentRoot2 if BPMN2Model_DocumentRoot2 is not None else set()
        self.BPMN2Model_DocumentRoot5 = BPMN2Model_DocumentRoot5 if BPMN2Model_DocumentRoot5 is not None else set()
        self.BPMN2Model_DocumentRoot7 = BPMN2Model_DocumentRoot7 if BPMN2Model_DocumentRoot7 is not None else set()
        self.BPMN2Model_DocumentRoot9 = BPMN2Model_DocumentRoot9 if BPMN2Model_DocumentRoot9 is not None else set()
        self.BPMN2Model_DocumentRoot11 = BPMN2Model_DocumentRoot11 if BPMN2Model_DocumentRoot11 is not None else set()
        self.BPMN2Model_DocumentRoot13 = BPMN2Model_DocumentRoot13 if BPMN2Model_DocumentRoot13 is not None else set()
        self.BPMN2Model_DocumentRoot15 = BPMN2Model_DocumentRoot15 if BPMN2Model_DocumentRoot15 is not None else set()
        self.BPMN2Model_DocumentRoot17 = BPMN2Model_DocumentRoot17 if BPMN2Model_DocumentRoot17 is not None else set()
        self.BPMN2Model_DocumentRoot19 = BPMN2Model_DocumentRoot19 if BPMN2Model_DocumentRoot19 is not None else set()
        self.BPMN2Model_DocumentRoot21 = BPMN2Model_DocumentRoot21 if BPMN2Model_DocumentRoot21 is not None else set()
        self.BPMN2Model_DocumentRoot24 = BPMN2Model_DocumentRoot24 if BPMN2Model_DocumentRoot24 is not None else set()
        self.BPMN2Model_DocumentRoot26 = BPMN2Model_DocumentRoot26 if BPMN2Model_DocumentRoot26 is not None else set()
        self.BPMN2Model_DocumentRoot28 = BPMN2Model_DocumentRoot28 if BPMN2Model_DocumentRoot28 is not None else set()
        self.BPMN2Model_DocumentRoot30 = BPMN2Model_DocumentRoot30 if BPMN2Model_DocumentRoot30 is not None else set()
        self.BPMN2Model_DocumentRoot32 = BPMN2Model_DocumentRoot32 if BPMN2Model_DocumentRoot32 is not None else set()
        self.BPMN2Model_DocumentRoot34 = BPMN2Model_DocumentRoot34 if BPMN2Model_DocumentRoot34 is not None else set()
        self.BPMN2Model_DocumentRoot = BPMN2Model_DocumentRoot if BPMN2Model_DocumentRoot is not None else set()
        self.BPMN2Model_DocumentRoot38 = BPMN2Model_DocumentRoot38 if BPMN2Model_DocumentRoot38 is not None else set()
        self.BPMN2Model_DocumentRoot40 = BPMN2Model_DocumentRoot40 if BPMN2Model_DocumentRoot40 is not None else set()
        self.BPMN2Model_DocumentRoot42 = BPMN2Model_DocumentRoot42 if BPMN2Model_DocumentRoot42 is not None else set()
        self.BPMN2Model_DocumentRoot44 = BPMN2Model_DocumentRoot44 if BPMN2Model_DocumentRoot44 is not None else set()
        self.BPMN2Model_DocumentRoot46 = BPMN2Model_DocumentRoot46 if BPMN2Model_DocumentRoot46 is not None else set()
        self.BPMN2Model_DocumentRoot48 = BPMN2Model_DocumentRoot48 if BPMN2Model_DocumentRoot48 is not None else set()
        self.BPMN2Model_DocumentRoot50 = BPMN2Model_DocumentRoot50 if BPMN2Model_DocumentRoot50 is not None else set()
        self.BPMN2Model_DocumentRoot52 = BPMN2Model_DocumentRoot52 if BPMN2Model_DocumentRoot52 is not None else set()
        self.BPMN2Model_DocumentRoot54 = BPMN2Model_DocumentRoot54 if BPMN2Model_DocumentRoot54 is not None else set()
        self.BPMN2Model_DocumentRoot56 = BPMN2Model_DocumentRoot56 if BPMN2Model_DocumentRoot56 is not None else set()
        self.BPMN2Model_DocumentRoot58 = BPMN2Model_DocumentRoot58 if BPMN2Model_DocumentRoot58 is not None else set()
        self.BPMN2Model_DocumentRoot60 = BPMN2Model_DocumentRoot60 if BPMN2Model_DocumentRoot60 is not None else set()
        self.BPMN2Model_DocumentRoot62 = BPMN2Model_DocumentRoot62 if BPMN2Model_DocumentRoot62 is not None else set()
        self.BPMN2Model_DocumentRoot64 = BPMN2Model_DocumentRoot64 if BPMN2Model_DocumentRoot64 is not None else set()
        self.BPMN2Model_DocumentRoot66 = BPMN2Model_DocumentRoot66 if BPMN2Model_DocumentRoot66 is not None else set()
        self.BPMN2Model_DocumentRoot36 = BPMN2Model_DocumentRoot36 if BPMN2Model_DocumentRoot36 is not None else set()
        self.BPMN2Model_DocumentRoot68 = BPMN2Model_DocumentRoot68 if BPMN2Model_DocumentRoot68 is not None else set()
        self.BPMN2Model_DocumentRoot70 = BPMN2Model_DocumentRoot70 if BPMN2Model_DocumentRoot70 is not None else set()
        self.BPMN2Model_DocumentRoot72 = BPMN2Model_DocumentRoot72 if BPMN2Model_DocumentRoot72 is not None else set()
        self.BPMN2Model_DocumentRoot74 = BPMN2Model_DocumentRoot74 if BPMN2Model_DocumentRoot74 is not None else set()
        self.BPMN2Model_DocumentRoot76 = BPMN2Model_DocumentRoot76 if BPMN2Model_DocumentRoot76 is not None else set()
        self.BPMN2Model_DocumentRoot78 = BPMN2Model_DocumentRoot78 if BPMN2Model_DocumentRoot78 is not None else set()
        self.BPMN2Model_DocumentRoot80 = BPMN2Model_DocumentRoot80 if BPMN2Model_DocumentRoot80 is not None else set()
        self.BPMN2Model_DocumentRoot82 = BPMN2Model_DocumentRoot82 if BPMN2Model_DocumentRoot82 is not None else set()
        self.BPMN2Model_DocumentRoot84 = BPMN2Model_DocumentRoot84 if BPMN2Model_DocumentRoot84 is not None else set()
        self.BPMN2Model_DocumentRoot86 = BPMN2Model_DocumentRoot86 if BPMN2Model_DocumentRoot86 is not None else set()
        self.BPMN2Model_DocumentRoot88 = BPMN2Model_DocumentRoot88 if BPMN2Model_DocumentRoot88 is not None else set()
        self.BPMN2Model_DocumentRoot90 = BPMN2Model_DocumentRoot90 if BPMN2Model_DocumentRoot90 is not None else set()
        self.BPMN2Model_DocumentRoot92 = BPMN2Model_DocumentRoot92 if BPMN2Model_DocumentRoot92 is not None else set()
        self.BPMN2Model_DocumentRoot94 = BPMN2Model_DocumentRoot94 if BPMN2Model_DocumentRoot94 is not None else set()
        self.BPMN2Model_DocumentRoot96 = BPMN2Model_DocumentRoot96 if BPMN2Model_DocumentRoot96 is not None else set()
        self.BPMN2Model_DocumentRoot100 = BPMN2Model_DocumentRoot100 if BPMN2Model_DocumentRoot100 is not None else set()
        self.BPMN2Model_DocumentRoot102 = BPMN2Model_DocumentRoot102 if BPMN2Model_DocumentRoot102 is not None else set()
        self.BPMN2Model_DocumentRoot104 = BPMN2Model_DocumentRoot104 if BPMN2Model_DocumentRoot104 is not None else set()
        self.BPMN2Model_DocumentRoot106 = BPMN2Model_DocumentRoot106 if BPMN2Model_DocumentRoot106 is not None else set()
        self.BPMN2Model_DocumentRoot108 = BPMN2Model_DocumentRoot108 if BPMN2Model_DocumentRoot108 is not None else set()
        self.BPMN2Model_DocumentRoot110 = BPMN2Model_DocumentRoot110 if BPMN2Model_DocumentRoot110 is not None else set()
        self.BPMN2Model_DocumentRoot112 = BPMN2Model_DocumentRoot112 if BPMN2Model_DocumentRoot112 is not None else set()
        self.BPMN2Model_DocumentRoot114 = BPMN2Model_DocumentRoot114 if BPMN2Model_DocumentRoot114 is not None else set()
        self.BPMN2Model_DocumentRoot116 = BPMN2Model_DocumentRoot116 if BPMN2Model_DocumentRoot116 is not None else set()
        self.BPMN2Model_DocumentRoot118 = BPMN2Model_DocumentRoot118 if BPMN2Model_DocumentRoot118 is not None else set()
        self.BPMN2Model_DocumentRoot120 = BPMN2Model_DocumentRoot120 if BPMN2Model_DocumentRoot120 is not None else set()
        self.BPMN2Model_DocumentRoot122 = BPMN2Model_DocumentRoot122 if BPMN2Model_DocumentRoot122 is not None else set()
        self.BPMN2Model_DocumentRoot124 = BPMN2Model_DocumentRoot124 if BPMN2Model_DocumentRoot124 is not None else set()
        self.BPMN2Model_DocumentRoot126 = BPMN2Model_DocumentRoot126 if BPMN2Model_DocumentRoot126 is not None else set()
        self.BPMN2Model_DocumentRoot98 = BPMN2Model_DocumentRoot98 if BPMN2Model_DocumentRoot98 is not None else set()
        self.BPMN2Model_DocumentRoot128 = BPMN2Model_DocumentRoot128 if BPMN2Model_DocumentRoot128 is not None else set()
        self.BPMN2Model_DocumentRoot130 = BPMN2Model_DocumentRoot130 if BPMN2Model_DocumentRoot130 is not None else set()
        self.BPMN2Model_DocumentRoot132 = BPMN2Model_DocumentRoot132 if BPMN2Model_DocumentRoot132 is not None else set()
        self.BPMN2Model_DocumentRoot134 = BPMN2Model_DocumentRoot134 if BPMN2Model_DocumentRoot134 is not None else set()
        self.BPMN2Model_DocumentRoot136 = BPMN2Model_DocumentRoot136 if BPMN2Model_DocumentRoot136 is not None else set()
        self.BPMN2Model_DocumentRoot138 = BPMN2Model_DocumentRoot138 if BPMN2Model_DocumentRoot138 is not None else set()
        self.BPMN2Model_DocumentRoot140 = BPMN2Model_DocumentRoot140 if BPMN2Model_DocumentRoot140 is not None else set()
        self.BPMN2Model_DocumentRoot142 = BPMN2Model_DocumentRoot142 if BPMN2Model_DocumentRoot142 is not None else set()
        self.BPMN2Model_DocumentRoot144 = BPMN2Model_DocumentRoot144 if BPMN2Model_DocumentRoot144 is not None else set()
        self.BPMN2Model_DocumentRoot146 = BPMN2Model_DocumentRoot146 if BPMN2Model_DocumentRoot146 is not None else set()
        self.BPMN2Model_DocumentRoot148 = BPMN2Model_DocumentRoot148 if BPMN2Model_DocumentRoot148 is not None else set()
        self.BPMN2Model_DocumentRoot150 = BPMN2Model_DocumentRoot150 if BPMN2Model_DocumentRoot150 is not None else set()
        self.BPMN2Model_DocumentRoot152 = BPMN2Model_DocumentRoot152 if BPMN2Model_DocumentRoot152 is not None else set()
        self.BPMN2Model_DocumentRoot154 = BPMN2Model_DocumentRoot154 if BPMN2Model_DocumentRoot154 is not None else set()
        self.BPMN2Model_DocumentRoot156 = BPMN2Model_DocumentRoot156 if BPMN2Model_DocumentRoot156 is not None else set()
        self.BPMN2Model_DocumentRoot158 = BPMN2Model_DocumentRoot158 if BPMN2Model_DocumentRoot158 is not None else set()
        self.BPMN2Model_DocumentRoot160 = BPMN2Model_DocumentRoot160 if BPMN2Model_DocumentRoot160 is not None else set()
        self.BPMN2Model_DocumentRoot162 = BPMN2Model_DocumentRoot162 if BPMN2Model_DocumentRoot162 is not None else set()
        self.BPMN2Model_DocumentRoot164 = BPMN2Model_DocumentRoot164 if BPMN2Model_DocumentRoot164 is not None else set()
        self.BPMN2Model_DocumentRoot166 = BPMN2Model_DocumentRoot166 if BPMN2Model_DocumentRoot166 is not None else set()
        self.BPMN2Model_DocumentRoot168 = BPMN2Model_DocumentRoot168 if BPMN2Model_DocumentRoot168 is not None else set()
        self.BPMN2Model_DocumentRoot170 = BPMN2Model_DocumentRoot170 if BPMN2Model_DocumentRoot170 is not None else set()
        self.BPMN2Model_DocumentRoot172 = BPMN2Model_DocumentRoot172 if BPMN2Model_DocumentRoot172 is not None else set()
        self.BPMN2Model_DocumentRoot174 = BPMN2Model_DocumentRoot174 if BPMN2Model_DocumentRoot174 is not None else set()
        self.BPMN2Model_DocumentRoot176 = BPMN2Model_DocumentRoot176 if BPMN2Model_DocumentRoot176 is not None else set()
        self.BPMN2Model_DocumentRoot178 = BPMN2Model_DocumentRoot178 if BPMN2Model_DocumentRoot178 is not None else set()
        self.BPMN2Model_DocumentRoot180 = BPMN2Model_DocumentRoot180 if BPMN2Model_DocumentRoot180 is not None else set()
        self.BPMN2Model_DocumentRoot182 = BPMN2Model_DocumentRoot182 if BPMN2Model_DocumentRoot182 is not None else set()
        self.BPMN2Model_DocumentRoot184 = BPMN2Model_DocumentRoot184 if BPMN2Model_DocumentRoot184 is not None else set()
        self.BPMN2Model_DocumentRoot186 = BPMN2Model_DocumentRoot186 if BPMN2Model_DocumentRoot186 is not None else set()
        self.BPMN2Model_DocumentRoot188 = BPMN2Model_DocumentRoot188 if BPMN2Model_DocumentRoot188 is not None else set()
        self.BPMN2Model_DocumentRoot190 = BPMN2Model_DocumentRoot190 if BPMN2Model_DocumentRoot190 is not None else set()
        self.BPMN2Model_DocumentRoot192 = BPMN2Model_DocumentRoot192 if BPMN2Model_DocumentRoot192 is not None else set()
        self.BPMN2Model_DocumentRoot194 = BPMN2Model_DocumentRoot194 if BPMN2Model_DocumentRoot194 is not None else set()
        self.BPMN2Model_DocumentRoot196 = BPMN2Model_DocumentRoot196 if BPMN2Model_DocumentRoot196 is not None else set()
        self.BPMN2Model_DocumentRoot198 = BPMN2Model_DocumentRoot198 if BPMN2Model_DocumentRoot198 is not None else set()
        self.BPMN2Model_DocumentRoot200 = BPMN2Model_DocumentRoot200 if BPMN2Model_DocumentRoot200 is not None else set()
        self.BPMN2Model_DocumentRoot202 = BPMN2Model_DocumentRoot202 if BPMN2Model_DocumentRoot202 is not None else set()
        self.BPMN2Model_DocumentRoot204 = BPMN2Model_DocumentRoot204 if BPMN2Model_DocumentRoot204 is not None else set()
        self.BPMN2Model_DocumentRoot206 = BPMN2Model_DocumentRoot206 if BPMN2Model_DocumentRoot206 is not None else set()
        self.BPMN2Model_DocumentRoot208 = BPMN2Model_DocumentRoot208 if BPMN2Model_DocumentRoot208 is not None else set()
        self.BPMN2Model_DocumentRoot212 = BPMN2Model_DocumentRoot212 if BPMN2Model_DocumentRoot212 is not None else set()
        self.BPMN2Model_DocumentRoot214 = BPMN2Model_DocumentRoot214 if BPMN2Model_DocumentRoot214 is not None else set()
        self.BPMN2Model_DocumentRoot216 = BPMN2Model_DocumentRoot216 if BPMN2Model_DocumentRoot216 is not None else set()
        self.BPMN2Model_DocumentRoot218 = BPMN2Model_DocumentRoot218 if BPMN2Model_DocumentRoot218 is not None else set()
        self.BPMN2Model_DocumentRoot220 = BPMN2Model_DocumentRoot220 if BPMN2Model_DocumentRoot220 is not None else set()
        self.BPMN2Model_DocumentRoot222 = BPMN2Model_DocumentRoot222 if BPMN2Model_DocumentRoot222 is not None else set()
        self.BPMN2Model_DocumentRoot224 = BPMN2Model_DocumentRoot224 if BPMN2Model_DocumentRoot224 is not None else set()
        self.BPMN2Model_DocumentRoot226 = BPMN2Model_DocumentRoot226 if BPMN2Model_DocumentRoot226 is not None else set()
        self.BPMN2Model_DocumentRoot228 = BPMN2Model_DocumentRoot228 if BPMN2Model_DocumentRoot228 is not None else set()
        self.BPMN2Model_DocumentRoot230 = BPMN2Model_DocumentRoot230 if BPMN2Model_DocumentRoot230 is not None else set()
        self.BPMN2Model_DocumentRoot210 = BPMN2Model_DocumentRoot210 if BPMN2Model_DocumentRoot210 is not None else set()
        self.BPMN2Model_DocumentRoot232 = BPMN2Model_DocumentRoot232 if BPMN2Model_DocumentRoot232 is not None else set()
        self.BPMN2Model_DocumentRoot234 = BPMN2Model_DocumentRoot234 if BPMN2Model_DocumentRoot234 is not None else set()
        self.BPMN2Model_DocumentRoot236 = BPMN2Model_DocumentRoot236 if BPMN2Model_DocumentRoot236 is not None else set()
        self.BPMN2Model_DocumentRoot238 = BPMN2Model_DocumentRoot238 if BPMN2Model_DocumentRoot238 is not None else set()
        self.BPMN2Model_DocumentRoot240 = BPMN2Model_DocumentRoot240 if BPMN2Model_DocumentRoot240 is not None else set()
        self.BPMN2Model_DocumentRoot242 = BPMN2Model_DocumentRoot242 if BPMN2Model_DocumentRoot242 is not None else set()
        self.BPMN2Model_DocumentRoot244 = BPMN2Model_DocumentRoot244 if BPMN2Model_DocumentRoot244 is not None else set()
        self.BPMN2Model_DocumentRoot246 = BPMN2Model_DocumentRoot246 if BPMN2Model_DocumentRoot246 is not None else set()
        self.BPMN2Model_DocumentRoot248 = BPMN2Model_DocumentRoot248 if BPMN2Model_DocumentRoot248 is not None else set()
        self.BPMN2Model_DocumentRoot250 = BPMN2Model_DocumentRoot250 if BPMN2Model_DocumentRoot250 is not None else set()
        self.BPMN2Model_DocumentRoot252 = BPMN2Model_DocumentRoot252 if BPMN2Model_DocumentRoot252 is not None else set()
        self.BPMN2Model_DocumentRoot254 = BPMN2Model_DocumentRoot254 if BPMN2Model_DocumentRoot254 is not None else set()
        self.BPMN2Model_DocumentRoot256 = BPMN2Model_DocumentRoot256 if BPMN2Model_DocumentRoot256 is not None else set()
        self.BPMN2Model_DocumentRoot258 = BPMN2Model_DocumentRoot258 if BPMN2Model_DocumentRoot258 is not None else set()
        self.BPMN2Model_DocumentRoot260 = BPMN2Model_DocumentRoot260 if BPMN2Model_DocumentRoot260 is not None else set()
        self.BPMN2Model_DocumentRoot262 = BPMN2Model_DocumentRoot262 if BPMN2Model_DocumentRoot262 is not None else set()
        self.BPMN2Model_DocumentRoot264 = BPMN2Model_DocumentRoot264 if BPMN2Model_DocumentRoot264 is not None else set()
        self.BPMN2Model_DocumentRoot267 = BPMN2Model_DocumentRoot267 if BPMN2Model_DocumentRoot267 is not None else set()
        self.BPMN2Model_DocumentRoot269 = BPMN2Model_DocumentRoot269 if BPMN2Model_DocumentRoot269 is not None else set()
        self.BPMN2Model_DocumentRoot271 = BPMN2Model_DocumentRoot271 if BPMN2Model_DocumentRoot271 is not None else set()
        self.BPMN2Model_DocumentRoot273 = BPMN2Model_DocumentRoot273 if BPMN2Model_DocumentRoot273 is not None else set()
        self.BPMN2Model_DocumentRoot275 = BPMN2Model_DocumentRoot275 if BPMN2Model_DocumentRoot275 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def BPMN2Model_DocumentRoot212(self):
        return self.__BPMN2Model_DocumentRoot212

    @BPMN2Model_DocumentRoot212.setter
    def BPMN2Model_DocumentRoot212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot212", None)
        self.__BPMN2Model_DocumentRoot212 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_PartnerEntity"):
                    opp_val = getattr(item, "BPMN2Model_PartnerEntity", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_PartnerEntity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_PartnerEntity"):
                    opp_val = getattr(item, "BPMN2Model_PartnerEntity", None)
                    
                    setattr(item, "BPMN2Model_PartnerEntity", self)
                    

    @property
    def BPMN2Model_DocumentRoot206(self):
        return self.__BPMN2Model_DocumentRoot206

    @BPMN2Model_DocumentRoot206.setter
    def BPMN2Model_DocumentRoot206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot206", None)
        self.__BPMN2Model_DocumentRoot206 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Participant"):
                    opp_val = getattr(item, "BPMN2Model_Participant", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Participant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Participant"):
                    opp_val = getattr(item, "BPMN2Model_Participant", None)
                    
                    setattr(item, "BPMN2Model_Participant", self)
                    

    @property
    def BPMN2Model_DocumentRoot244(self):
        return self.__BPMN2Model_DocumentRoot244

    @BPMN2Model_DocumentRoot244.setter
    def BPMN2Model_DocumentRoot244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot244", None)
        self.__BPMN2Model_DocumentRoot244 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ServiceTask"):
                    opp_val = getattr(item, "BPMN2Model_ServiceTask", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ServiceTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ServiceTask"):
                    opp_val = getattr(item, "BPMN2Model_ServiceTask", None)
                    
                    setattr(item, "BPMN2Model_ServiceTask", self)
                    

    @property
    def BPMN2Model_DocumentRoot168(self):
        return self.__BPMN2Model_DocumentRoot168

    @BPMN2Model_DocumentRoot168.setter
    def BPMN2Model_DocumentRoot168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot168", None)
        self.__BPMN2Model_DocumentRoot168 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_IntermediateCatchEvent"):
                    opp_val = getattr(item, "BPMN2Model_IntermediateCatchEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_IntermediateCatchEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_IntermediateCatchEvent"):
                    opp_val = getattr(item, "BPMN2Model_IntermediateCatchEvent", None)
                    
                    setattr(item, "BPMN2Model_IntermediateCatchEvent", self)
                    

    @property
    def BPMN2Model_DocumentRoot108(self):
        return self.__BPMN2Model_DocumentRoot108

    @BPMN2Model_DocumentRoot108.setter
    def BPMN2Model_DocumentRoot108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot108", None)
        self.__BPMN2Model_DocumentRoot108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_EndPoint"):
                    opp_val = getattr(item, "BPMN2Model_EndPoint", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_EndPoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_EndPoint"):
                    opp_val = getattr(item, "BPMN2Model_EndPoint", None)
                    
                    setattr(item, "BPMN2Model_EndPoint", self)
                    

    @property
    def BPMN2Model_DocumentRoot120(self):
        return self.__BPMN2Model_DocumentRoot120

    @BPMN2Model_DocumentRoot120.setter
    def BPMN2Model_DocumentRoot120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot120", None)
        self.__BPMN2Model_DocumentRoot120 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_EventBasedGateway"):
                    opp_val = getattr(item, "BPMN2Model_EventBasedGateway", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_EventBasedGateway", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_EventBasedGateway"):
                    opp_val = getattr(item, "BPMN2Model_EventBasedGateway", None)
                    
                    setattr(item, "BPMN2Model_EventBasedGateway", self)
                    

    @property
    def BPMN2Model_DocumentRoot234(self):
        return self.__BPMN2Model_DocumentRoot234

    @BPMN2Model_DocumentRoot234.setter
    def BPMN2Model_DocumentRoot234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot234", None)
        self.__BPMN2Model_DocumentRoot234 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ResourceParameterBinding"):
                    opp_val = getattr(item, "BPMN2Model_ResourceParameterBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ResourceParameterBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ResourceParameterBinding"):
                    opp_val = getattr(item, "BPMN2Model_ResourceParameterBinding", None)
                    
                    setattr(item, "BPMN2Model_ResourceParameterBinding", self)
                    

    @property
    def BPMN2Model_DocumentRoot230(self):
        return self.__BPMN2Model_DocumentRoot230

    @BPMN2Model_DocumentRoot230.setter
    def BPMN2Model_DocumentRoot230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot230", None)
        self.__BPMN2Model_DocumentRoot230 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ResourceAssignmentExpression"):
                    opp_val = getattr(item, "BPMN2Model_ResourceAssignmentExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ResourceAssignmentExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ResourceAssignmentExpression"):
                    opp_val = getattr(item, "BPMN2Model_ResourceAssignmentExpression", None)
                    
                    setattr(item, "BPMN2Model_ResourceAssignmentExpression", self)
                    

    @property
    def BPMN2Model_DocumentRoot214(self):
        return self.__BPMN2Model_DocumentRoot214

    @BPMN2Model_DocumentRoot214.setter
    def BPMN2Model_DocumentRoot214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot214", None)
        self.__BPMN2Model_DocumentRoot214 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_PartnerRole"):
                    opp_val = getattr(item, "BPMN2Model_PartnerRole", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_PartnerRole", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_PartnerRole"):
                    opp_val = getattr(item, "BPMN2Model_PartnerRole", None)
                    
                    setattr(item, "BPMN2Model_PartnerRole", self)
                    

    @property
    def BPMN2Model_DocumentRoot94(self):
        return self.__BPMN2Model_DocumentRoot94

    @BPMN2Model_DocumentRoot94.setter
    def BPMN2Model_DocumentRoot94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot94", None)
        self.__BPMN2Model_DocumentRoot94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_DataOutputAssociation"):
                    opp_val = getattr(item, "BPMN2Model_DataOutputAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_DataOutputAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_DataOutputAssociation"):
                    opp_val = getattr(item, "BPMN2Model_DataOutputAssociation", None)
                    
                    setattr(item, "BPMN2Model_DataOutputAssociation", self)
                    

    @property
    def BPMN2Model_DocumentRoot148(self):
        return self.__BPMN2Model_DocumentRoot148

    @BPMN2Model_DocumentRoot148.setter
    def BPMN2Model_DocumentRoot148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot148", None)
        self.__BPMN2Model_DocumentRoot148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_GlobalUserTask"):
                    opp_val = getattr(item, "BPMN2Model_GlobalUserTask", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_GlobalUserTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_GlobalUserTask"):
                    opp_val = getattr(item, "BPMN2Model_GlobalUserTask", None)
                    
                    setattr(item, "BPMN2Model_GlobalUserTask", self)
                    

    @property
    def BPMN2Model_DocumentRoot50(self):
        return self.__BPMN2Model_DocumentRoot50

    @BPMN2Model_DocumentRoot50.setter
    def BPMN2Model_DocumentRoot50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot50", None)
        self.__BPMN2Model_DocumentRoot50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Choreography"):
                    opp_val = getattr(item, "BPMN2Model_Choreography", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Choreography", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Choreography"):
                    opp_val = getattr(item, "BPMN2Model_Choreography", None)
                    
                    setattr(item, "BPMN2Model_Choreography", self)
                    

    @property
    def BPMN2Model_DocumentRoot192(self):
        return self.__BPMN2Model_DocumentRoot192

    @BPMN2Model_DocumentRoot192.setter
    def BPMN2Model_DocumentRoot192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot192", None)
        self.__BPMN2Model_DocumentRoot192 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_MessageFlow"):
                    opp_val = getattr(item, "BPMN2Model_MessageFlow", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_MessageFlow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_MessageFlow"):
                    opp_val = getattr(item, "BPMN2Model_MessageFlow", None)
                    
                    setattr(item, "BPMN2Model_MessageFlow", self)
                    

    @property
    def BPMN2Model_DocumentRoot142(self):
        return self.__BPMN2Model_DocumentRoot142

    @BPMN2Model_DocumentRoot142.setter
    def BPMN2Model_DocumentRoot142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot142", None)
        self.__BPMN2Model_DocumentRoot142 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_GlobalManualTask"):
                    opp_val = getattr(item, "BPMN2Model_GlobalManualTask", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_GlobalManualTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_GlobalManualTask"):
                    opp_val = getattr(item, "BPMN2Model_GlobalManualTask", None)
                    
                    setattr(item, "BPMN2Model_GlobalManualTask", self)
                    

    @property
    def BPMN2Model_DocumentRoot172(self):
        return self.__BPMN2Model_DocumentRoot172

    @BPMN2Model_DocumentRoot172.setter
    def BPMN2Model_DocumentRoot172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot172", None)
        self.__BPMN2Model_DocumentRoot172 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_InputOutputBinding"):
                    opp_val = getattr(item, "BPMN2Model_InputOutputBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_InputOutputBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_InputOutputBinding"):
                    opp_val = getattr(item, "BPMN2Model_InputOutputBinding", None)
                    
                    setattr(item, "BPMN2Model_InputOutputBinding", self)
                    

    @property
    def BPMN2Model_DocumentRoot156(self):
        return self.__BPMN2Model_DocumentRoot156

    @BPMN2Model_DocumentRoot156.setter
    def BPMN2Model_DocumentRoot156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot156", None)
        self.__BPMN2Model_DocumentRoot156 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ResourceRole"):
                    opp_val = getattr(item, "BPMN2Model_ResourceRole", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ResourceRole", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ResourceRole"):
                    opp_val = getattr(item, "BPMN2Model_ResourceRole", None)
                    
                    setattr(item, "BPMN2Model_ResourceRole", self)
                    

    @property
    def BPMN2Model_DocumentRoot80(self):
        return self.__BPMN2Model_DocumentRoot80

    @BPMN2Model_DocumentRoot80.setter
    def BPMN2Model_DocumentRoot80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot80", None)
        self.__BPMN2Model_DocumentRoot80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_CorrelationSubscription"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationSubscription", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_CorrelationSubscription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_CorrelationSubscription"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationSubscription", None)
                    
                    setattr(item, "BPMN2Model_CorrelationSubscription", self)
                    

    @property
    def BPMN2Model_DocumentRoot264(self):
        return self.__BPMN2Model_DocumentRoot264

    @BPMN2Model_DocumentRoot264.setter
    def BPMN2Model_DocumentRoot264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot264", None)
        self.__BPMN2Model_DocumentRoot264 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_EObject265"):
                    opp_val = getattr(item, "BPMN2Model_EObject265", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_EObject265", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_EObject265"):
                    opp_val = getattr(item, "BPMN2Model_EObject265", None)
                    
                    setattr(item, "BPMN2Model_EObject265", self)
                    

    @property
    def BPMN2Model_DocumentRoot226(self):
        return self.__BPMN2Model_DocumentRoot226

    @BPMN2Model_DocumentRoot226.setter
    def BPMN2Model_DocumentRoot226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot226", None)
        self.__BPMN2Model_DocumentRoot226 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Rendering"):
                    opp_val = getattr(item, "BPMN2Model_Rendering", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Rendering", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Rendering"):
                    opp_val = getattr(item, "BPMN2Model_Rendering", None)
                    
                    setattr(item, "BPMN2Model_Rendering", self)
                    

    @property
    def BPMN2Model_DocumentRoot248(self):
        return self.__BPMN2Model_DocumentRoot248

    @BPMN2Model_DocumentRoot248.setter
    def BPMN2Model_DocumentRoot248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot248", None)
        self.__BPMN2Model_DocumentRoot248 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_SignalEventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_SignalEventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_SignalEventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_SignalEventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_SignalEventDefinition", None)
                    
                    setattr(item, "BPMN2Model_SignalEventDefinition", self)
                    

    @property
    def BPMN2Model_DocumentRoot106(self):
        return self.__BPMN2Model_DocumentRoot106

    @BPMN2Model_DocumentRoot106.setter
    def BPMN2Model_DocumentRoot106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot106", None)
        self.__BPMN2Model_DocumentRoot106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_EndEvent"):
                    opp_val = getattr(item, "BPMN2Model_EndEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_EndEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_EndEvent"):
                    opp_val = getattr(item, "BPMN2Model_EndEvent", None)
                    
                    setattr(item, "BPMN2Model_EndEvent", self)
                    

    @property
    def BPMN2Model_DocumentRoot96(self):
        return self.__BPMN2Model_DocumentRoot96

    @BPMN2Model_DocumentRoot96.setter
    def BPMN2Model_DocumentRoot96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot96", None)
        self.__BPMN2Model_DocumentRoot96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_DataState"):
                    opp_val = getattr(item, "BPMN2Model_DataState", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_DataState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_DataState"):
                    opp_val = getattr(item, "BPMN2Model_DataState", None)
                    
                    setattr(item, "BPMN2Model_DataState", self)
                    

    @property
    def BPMN2Model_DocumentRoot166(self):
        return self.__BPMN2Model_DocumentRoot166

    @BPMN2Model_DocumentRoot166.setter
    def BPMN2Model_DocumentRoot166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot166", None)
        self.__BPMN2Model_DocumentRoot166 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Interface"):
                    opp_val = getattr(item, "BPMN2Model_Interface", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Interface", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Interface"):
                    opp_val = getattr(item, "BPMN2Model_Interface", None)
                    
                    setattr(item, "BPMN2Model_Interface", self)
                    

    @property
    def BPMN2Model_DocumentRoot110(self):
        return self.__BPMN2Model_DocumentRoot110

    @BPMN2Model_DocumentRoot110.setter
    def BPMN2Model_DocumentRoot110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot110", None)
        self.__BPMN2Model_DocumentRoot110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Error"):
                    opp_val = getattr(item, "BPMN2Model_Error", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Error", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Error"):
                    opp_val = getattr(item, "BPMN2Model_Error", None)
                    
                    setattr(item, "BPMN2Model_Error", self)
                    

    @property
    def BPMN2Model_DocumentRoot208(self):
        return self.__BPMN2Model_DocumentRoot208

    @BPMN2Model_DocumentRoot208.setter
    def BPMN2Model_DocumentRoot208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot208", None)
        self.__BPMN2Model_DocumentRoot208 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ParticipantAssociation"):
                    opp_val = getattr(item, "BPMN2Model_ParticipantAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ParticipantAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ParticipantAssociation"):
                    opp_val = getattr(item, "BPMN2Model_ParticipantAssociation", None)
                    
                    setattr(item, "BPMN2Model_ParticipantAssociation", self)
                    

    @property
    def BPMN2Model_DocumentRoot38(self):
        return self.__BPMN2Model_DocumentRoot38

    @BPMN2Model_DocumentRoot38.setter
    def BPMN2Model_DocumentRoot38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot38", None)
        self.__BPMN2Model_DocumentRoot38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_CancelEventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_CancelEventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_CancelEventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_CancelEventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_CancelEventDefinition", None)
                    
                    setattr(item, "BPMN2Model_CancelEventDefinition", self)
                    

    @property
    def BPMN2Model_DocumentRoot232(self):
        return self.__BPMN2Model_DocumentRoot232

    @BPMN2Model_DocumentRoot232.setter
    def BPMN2Model_DocumentRoot232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot232", None)
        self.__BPMN2Model_DocumentRoot232 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ResourceParameter"):
                    opp_val = getattr(item, "BPMN2Model_ResourceParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ResourceParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ResourceParameter"):
                    opp_val = getattr(item, "BPMN2Model_ResourceParameter", None)
                    
                    setattr(item, "BPMN2Model_ResourceParameter", self)
                    

    @property
    def BPMN2Model_DocumentRoot122(self):
        return self.__BPMN2Model_DocumentRoot122

    @BPMN2Model_DocumentRoot122.setter
    def BPMN2Model_DocumentRoot122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot122", None)
        self.__BPMN2Model_DocumentRoot122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ExclusiveGateway"):
                    opp_val = getattr(item, "BPMN2Model_ExclusiveGateway", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ExclusiveGateway", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ExclusiveGateway"):
                    opp_val = getattr(item, "BPMN2Model_ExclusiveGateway", None)
                    
                    setattr(item, "BPMN2Model_ExclusiveGateway", self)
                    

    @property
    def BPMN2Model_DocumentRoot138(self):
        return self.__BPMN2Model_DocumentRoot138

    @BPMN2Model_DocumentRoot138.setter
    def BPMN2Model_DocumentRoot138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot138", None)
        self.__BPMN2Model_DocumentRoot138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_GlobalChoreographyTask"):
                    opp_val = getattr(item, "BPMN2Model_GlobalChoreographyTask", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_GlobalChoreographyTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_GlobalChoreographyTask"):
                    opp_val = getattr(item, "BPMN2Model_GlobalChoreographyTask", None)
                    
                    setattr(item, "BPMN2Model_GlobalChoreographyTask", self)
                    

    @property
    def BPMN2Model_DocumentRoot72(self):
        return self.__BPMN2Model_DocumentRoot72

    @BPMN2Model_DocumentRoot72.setter
    def BPMN2Model_DocumentRoot72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot72", None)
        self.__BPMN2Model_DocumentRoot72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_CorrelationKey"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationKey", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_CorrelationKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_CorrelationKey"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationKey", None)
                    
                    setattr(item, "BPMN2Model_CorrelationKey", self)
                    

    @property
    def BPMN2Model_DocumentRoot68(self):
        return self.__BPMN2Model_DocumentRoot68

    @BPMN2Model_DocumentRoot68.setter
    def BPMN2Model_DocumentRoot68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot68", None)
        self.__BPMN2Model_DocumentRoot68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ConversationAssociation"):
                    opp_val = getattr(item, "BPMN2Model_ConversationAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ConversationAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ConversationAssociation"):
                    opp_val = getattr(item, "BPMN2Model_ConversationAssociation", None)
                    
                    setattr(item, "BPMN2Model_ConversationAssociation", self)
                    

    @property
    def BPMN2Model_DocumentRoot162(self):
        return self.__BPMN2Model_DocumentRoot162

    @BPMN2Model_DocumentRoot162.setter
    def BPMN2Model_DocumentRoot162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot162", None)
        self.__BPMN2Model_DocumentRoot162 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_InclusiveGateway"):
                    opp_val = getattr(item, "BPMN2Model_InclusiveGateway", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_InclusiveGateway", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_InclusiveGateway"):
                    opp_val = getattr(item, "BPMN2Model_InclusiveGateway", None)
                    
                    setattr(item, "BPMN2Model_InclusiveGateway", self)
                    

    @property
    def BPMN2Model_DocumentRoot216(self):
        return self.__BPMN2Model_DocumentRoot216

    @BPMN2Model_DocumentRoot216.setter
    def BPMN2Model_DocumentRoot216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot216", None)
        self.__BPMN2Model_DocumentRoot216 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_PotentialOwner"):
                    opp_val = getattr(item, "BPMN2Model_PotentialOwner", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_PotentialOwner", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_PotentialOwner"):
                    opp_val = getattr(item, "BPMN2Model_PotentialOwner", None)
                    
                    setattr(item, "BPMN2Model_PotentialOwner", self)
                    

    @property
    def BPMN2Model_DocumentRoot48(self):
        return self.__BPMN2Model_DocumentRoot48

    @BPMN2Model_DocumentRoot48.setter
    def BPMN2Model_DocumentRoot48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot48", None)
        self.__BPMN2Model_DocumentRoot48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_CategoryValue"):
                    opp_val = getattr(item, "BPMN2Model_CategoryValue", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_CategoryValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_CategoryValue"):
                    opp_val = getattr(item, "BPMN2Model_CategoryValue", None)
                    
                    setattr(item, "BPMN2Model_CategoryValue", self)
                    

    @property
    def BPMN2Model_DocumentRoot269(self):
        return self.__BPMN2Model_DocumentRoot269

    @BPMN2Model_DocumentRoot269.setter
    def BPMN2Model_DocumentRoot269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot269", None)
        self.__BPMN2Model_DocumentRoot269 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ThrowEvent"):
                    opp_val = getattr(item, "BPMN2Model_ThrowEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ThrowEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ThrowEvent"):
                    opp_val = getattr(item, "BPMN2Model_ThrowEvent", None)
                    
                    setattr(item, "BPMN2Model_ThrowEvent", self)
                    

    @property
    def BPMN2Model_DocumentRoot210(self):
        return self.__BPMN2Model_DocumentRoot210

    @BPMN2Model_DocumentRoot210.setter
    def BPMN2Model_DocumentRoot210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot210", None)
        self.__BPMN2Model_DocumentRoot210 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ParticipantMultiplicity"):
                    opp_val = getattr(item, "BPMN2Model_ParticipantMultiplicity", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ParticipantMultiplicity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ParticipantMultiplicity"):
                    opp_val = getattr(item, "BPMN2Model_ParticipantMultiplicity", None)
                    
                    setattr(item, "BPMN2Model_ParticipantMultiplicity", self)
                    

    @property
    def BPMN2Model_DocumentRoot(self):
        return self.__BPMN2Model_DocumentRoot

    @BPMN2Model_DocumentRoot.setter
    def BPMN2Model_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot", None)
        self.__BPMN2Model_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_EStringToStringMapEntry"):
                    opp_val = getattr(item, "BPMN2Model_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_EStringToStringMapEntry"):
                    opp_val = getattr(item, "BPMN2Model_EStringToStringMapEntry", None)
                    
                    setattr(item, "BPMN2Model_EStringToStringMapEntry", self)
                    

    @property
    def BPMN2Model_DocumentRoot154(self):
        return self.__BPMN2Model_DocumentRoot154

    @BPMN2Model_DocumentRoot154.setter
    def BPMN2Model_DocumentRoot154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot154", None)
        self.__BPMN2Model_DocumentRoot154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Performer"):
                    opp_val = getattr(item, "BPMN2Model_Performer", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Performer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Performer"):
                    opp_val = getattr(item, "BPMN2Model_Performer", None)
                    
                    setattr(item, "BPMN2Model_Performer", self)
                    

    @property
    def BPMN2Model_DocumentRoot262(self):
        return self.__BPMN2Model_DocumentRoot262

    @BPMN2Model_DocumentRoot262.setter
    def BPMN2Model_DocumentRoot262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot262", None)
        self.__BPMN2Model_DocumentRoot262 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_TerminateEventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_TerminateEventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_TerminateEventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_TerminateEventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_TerminateEventDefinition", None)
                    
                    setattr(item, "BPMN2Model_TerminateEventDefinition", self)
                    

    @property
    def BPMN2Model_DocumentRoot150(self):
        return self.__BPMN2Model_DocumentRoot150

    @BPMN2Model_DocumentRoot150.setter
    def BPMN2Model_DocumentRoot150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot150", None)
        self.__BPMN2Model_DocumentRoot150 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Group"):
                    opp_val = getattr(item, "BPMN2Model_Group", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Group", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Group"):
                    opp_val = getattr(item, "BPMN2Model_Group", None)
                    
                    setattr(item, "BPMN2Model_Group", self)
                    

    @property
    def BPMN2Model_DocumentRoot7(self):
        return self.__BPMN2Model_DocumentRoot7

    @BPMN2Model_DocumentRoot7.setter
    def BPMN2Model_DocumentRoot7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot7", None)
        self.__BPMN2Model_DocumentRoot7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_AdHocSubProcess"):
                    opp_val = getattr(item, "BPMN2Model_AdHocSubProcess", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_AdHocSubProcess", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_AdHocSubProcess"):
                    opp_val = getattr(item, "BPMN2Model_AdHocSubProcess", None)
                    
                    setattr(item, "BPMN2Model_AdHocSubProcess", self)
                    

    @property
    def BPMN2Model_DocumentRoot26(self):
        return self.__BPMN2Model_DocumentRoot26

    @BPMN2Model_DocumentRoot26.setter
    def BPMN2Model_DocumentRoot26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot26", None)
        self.__BPMN2Model_DocumentRoot26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_BusinessRuleTask"):
                    opp_val = getattr(item, "BPMN2Model_BusinessRuleTask", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_BusinessRuleTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_BusinessRuleTask"):
                    opp_val = getattr(item, "BPMN2Model_BusinessRuleTask", None)
                    
                    setattr(item, "BPMN2Model_BusinessRuleTask", self)
                    

    @property
    def BPMN2Model_DocumentRoot76(self):
        return self.__BPMN2Model_DocumentRoot76

    @BPMN2Model_DocumentRoot76.setter
    def BPMN2Model_DocumentRoot76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot76", None)
        self.__BPMN2Model_DocumentRoot76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_CorrelationPropertyBinding"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationPropertyBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_CorrelationPropertyBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_CorrelationPropertyBinding"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationPropertyBinding", None)
                    
                    setattr(item, "BPMN2Model_CorrelationPropertyBinding", self)
                    

    @property
    def BPMN2Model_DocumentRoot188(self):
        return self.__BPMN2Model_DocumentRoot188

    @BPMN2Model_DocumentRoot188.setter
    def BPMN2Model_DocumentRoot188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot188", None)
        self.__BPMN2Model_DocumentRoot188 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Message"):
                    opp_val = getattr(item, "BPMN2Model_Message", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Message", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Message"):
                    opp_val = getattr(item, "BPMN2Model_Message", None)
                    
                    setattr(item, "BPMN2Model_Message", self)
                    

    @property
    def BPMN2Model_DocumentRoot160(self):
        return self.__BPMN2Model_DocumentRoot160

    @BPMN2Model_DocumentRoot160.setter
    def BPMN2Model_DocumentRoot160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot160", None)
        self.__BPMN2Model_DocumentRoot160 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Import"):
                    opp_val = getattr(item, "BPMN2Model_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Import"):
                    opp_val = getattr(item, "BPMN2Model_Import", None)
                    
                    setattr(item, "BPMN2Model_Import", self)
                    

    @property
    def BPMN2Model_DocumentRoot30(self):
        return self.__BPMN2Model_DocumentRoot30

    @BPMN2Model_DocumentRoot30.setter
    def BPMN2Model_DocumentRoot30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot30", None)
        self.__BPMN2Model_DocumentRoot30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_CallActivity"):
                    opp_val = getattr(item, "BPMN2Model_CallActivity", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_CallActivity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_CallActivity"):
                    opp_val = getattr(item, "BPMN2Model_CallActivity", None)
                    
                    setattr(item, "BPMN2Model_CallActivity", self)
                    

    @property
    def BPMN2Model_DocumentRoot124(self):
        return self.__BPMN2Model_DocumentRoot124

    @BPMN2Model_DocumentRoot124.setter
    def BPMN2Model_DocumentRoot124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot124", None)
        self.__BPMN2Model_DocumentRoot124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Expression"):
                    opp_val = getattr(item, "BPMN2Model_Expression", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Expression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Expression"):
                    opp_val = getattr(item, "BPMN2Model_Expression", None)
                    
                    setattr(item, "BPMN2Model_Expression", self)
                    

    @property
    def BPMN2Model_DocumentRoot224(self):
        return self.__BPMN2Model_DocumentRoot224

    @BPMN2Model_DocumentRoot224.setter
    def BPMN2Model_DocumentRoot224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot224", None)
        self.__BPMN2Model_DocumentRoot224 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Relationship"):
                    opp_val = getattr(item, "BPMN2Model_Relationship", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Relationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Relationship"):
                    opp_val = getattr(item, "BPMN2Model_Relationship", None)
                    
                    setattr(item, "BPMN2Model_Relationship", self)
                    

    @property
    def BPMN2Model_DocumentRoot267(self):
        return self.__BPMN2Model_DocumentRoot267

    @BPMN2Model_DocumentRoot267.setter
    def BPMN2Model_DocumentRoot267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot267", None)
        self.__BPMN2Model_DocumentRoot267 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_TextAnnotation"):
                    opp_val = getattr(item, "BPMN2Model_TextAnnotation", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_TextAnnotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_TextAnnotation"):
                    opp_val = getattr(item, "BPMN2Model_TextAnnotation", None)
                    
                    setattr(item, "BPMN2Model_TextAnnotation", self)
                    

    @property
    def BPMN2Model_DocumentRoot90(self):
        return self.__BPMN2Model_DocumentRoot90

    @BPMN2Model_DocumentRoot90.setter
    def BPMN2Model_DocumentRoot90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot90", None)
        self.__BPMN2Model_DocumentRoot90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_DataObjectReference"):
                    opp_val = getattr(item, "BPMN2Model_DataObjectReference", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_DataObjectReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_DataObjectReference"):
                    opp_val = getattr(item, "BPMN2Model_DataObjectReference", None)
                    
                    setattr(item, "BPMN2Model_DataObjectReference", self)
                    

    @property
    def BPMN2Model_DocumentRoot92(self):
        return self.__BPMN2Model_DocumentRoot92

    @BPMN2Model_DocumentRoot92.setter
    def BPMN2Model_DocumentRoot92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot92", None)
        self.__BPMN2Model_DocumentRoot92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_DataOutput"):
                    opp_val = getattr(item, "BPMN2Model_DataOutput", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_DataOutput", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_DataOutput"):
                    opp_val = getattr(item, "BPMN2Model_DataOutput", None)
                    
                    setattr(item, "BPMN2Model_DataOutput", self)
                    

    @property
    def BPMN2Model_DocumentRoot202(self):
        return self.__BPMN2Model_DocumentRoot202

    @BPMN2Model_DocumentRoot202.setter
    def BPMN2Model_DocumentRoot202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot202", None)
        self.__BPMN2Model_DocumentRoot202 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_OutputSet"):
                    opp_val = getattr(item, "BPMN2Model_OutputSet", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_OutputSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_OutputSet"):
                    opp_val = getattr(item, "BPMN2Model_OutputSet", None)
                    
                    setattr(item, "BPMN2Model_OutputSet", self)
                    

    @property
    def BPMN2Model_DocumentRoot52(self):
        return self.__BPMN2Model_DocumentRoot52

    @BPMN2Model_DocumentRoot52.setter
    def BPMN2Model_DocumentRoot52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot52", None)
        self.__BPMN2Model_DocumentRoot52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Collaboration"):
                    opp_val = getattr(item, "BPMN2Model_Collaboration", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Collaboration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Collaboration"):
                    opp_val = getattr(item, "BPMN2Model_Collaboration", None)
                    
                    setattr(item, "BPMN2Model_Collaboration", self)
                    

    @property
    def BPMN2Model_DocumentRoot152(self):
        return self.__BPMN2Model_DocumentRoot152

    @BPMN2Model_DocumentRoot152.setter
    def BPMN2Model_DocumentRoot152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot152", None)
        self.__BPMN2Model_DocumentRoot152 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_HumanPerformer"):
                    opp_val = getattr(item, "BPMN2Model_HumanPerformer", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_HumanPerformer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_HumanPerformer"):
                    opp_val = getattr(item, "BPMN2Model_HumanPerformer", None)
                    
                    setattr(item, "BPMN2Model_HumanPerformer", self)
                    

    @property
    def BPMN2Model_DocumentRoot82(self):
        return self.__BPMN2Model_DocumentRoot82

    @BPMN2Model_DocumentRoot82.setter
    def BPMN2Model_DocumentRoot82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot82", None)
        self.__BPMN2Model_DocumentRoot82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_DataAssociation"):
                    opp_val = getattr(item, "BPMN2Model_DataAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_DataAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_DataAssociation"):
                    opp_val = getattr(item, "BPMN2Model_DataAssociation", None)
                    
                    setattr(item, "BPMN2Model_DataAssociation", self)
                    

    @property
    def BPMN2Model_DocumentRoot240(self):
        return self.__BPMN2Model_DocumentRoot240

    @BPMN2Model_DocumentRoot240.setter
    def BPMN2Model_DocumentRoot240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot240", None)
        self.__BPMN2Model_DocumentRoot240 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_SendTask"):
                    opp_val = getattr(item, "BPMN2Model_SendTask", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_SendTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_SendTask"):
                    opp_val = getattr(item, "BPMN2Model_SendTask", None)
                    
                    setattr(item, "BPMN2Model_SendTask", self)
                    

    @property
    def BPMN2Model_DocumentRoot5(self):
        return self.__BPMN2Model_DocumentRoot5

    @BPMN2Model_DocumentRoot5.setter
    def BPMN2Model_DocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot5", None)
        self.__BPMN2Model_DocumentRoot5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Activity"):
                    opp_val = getattr(item, "BPMN2Model_Activity", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Activity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Activity"):
                    opp_val = getattr(item, "BPMN2Model_Activity", None)
                    
                    setattr(item, "BPMN2Model_Activity", self)
                    

    @property
    def BPMN2Model_DocumentRoot200(self):
        return self.__BPMN2Model_DocumentRoot200

    @BPMN2Model_DocumentRoot200.setter
    def BPMN2Model_DocumentRoot200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot200", None)
        self.__BPMN2Model_DocumentRoot200 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Operation"):
                    opp_val = getattr(item, "BPMN2Model_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Operation"):
                    opp_val = getattr(item, "BPMN2Model_Operation", None)
                    
                    setattr(item, "BPMN2Model_Operation", self)
                    

    @property
    def BPMN2Model_DocumentRoot184(self):
        return self.__BPMN2Model_DocumentRoot184

    @BPMN2Model_DocumentRoot184.setter
    def BPMN2Model_DocumentRoot184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot184", None)
        self.__BPMN2Model_DocumentRoot184 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_LoopCharacteristics"):
                    opp_val = getattr(item, "BPMN2Model_LoopCharacteristics", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_LoopCharacteristics", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_LoopCharacteristics"):
                    opp_val = getattr(item, "BPMN2Model_LoopCharacteristics", None)
                    
                    setattr(item, "BPMN2Model_LoopCharacteristics", self)
                    

    @property
    def BPMN2Model_DocumentRoot218(self):
        return self.__BPMN2Model_DocumentRoot218

    @BPMN2Model_DocumentRoot218.setter
    def BPMN2Model_DocumentRoot218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot218", None)
        self.__BPMN2Model_DocumentRoot218 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Process"):
                    opp_val = getattr(item, "BPMN2Model_Process", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Process", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Process"):
                    opp_val = getattr(item, "BPMN2Model_Process", None)
                    
                    setattr(item, "BPMN2Model_Process", self)
                    

    @property
    def BPMN2Model_DocumentRoot250(self):
        return self.__BPMN2Model_DocumentRoot250

    @BPMN2Model_DocumentRoot250.setter
    def BPMN2Model_DocumentRoot250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot250", None)
        self.__BPMN2Model_DocumentRoot250 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_StandardLoopCharacteristics"):
                    opp_val = getattr(item, "BPMN2Model_StandardLoopCharacteristics", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_StandardLoopCharacteristics", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_StandardLoopCharacteristics"):
                    opp_val = getattr(item, "BPMN2Model_StandardLoopCharacteristics", None)
                    
                    setattr(item, "BPMN2Model_StandardLoopCharacteristics", self)
                    

    @property
    def BPMN2Model_DocumentRoot78(self):
        return self.__BPMN2Model_DocumentRoot78

    @BPMN2Model_DocumentRoot78.setter
    def BPMN2Model_DocumentRoot78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot78", None)
        self.__BPMN2Model_DocumentRoot78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_CorrelationPropertyRetrievalExpression"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationPropertyRetrievalExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_CorrelationPropertyRetrievalExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_CorrelationPropertyRetrievalExpression"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationPropertyRetrievalExpression", None)
                    
                    setattr(item, "BPMN2Model_CorrelationPropertyRetrievalExpression", self)
                    

    @property
    def BPMN2Model_DocumentRoot126(self):
        return self.__BPMN2Model_DocumentRoot126

    @BPMN2Model_DocumentRoot126.setter
    def BPMN2Model_DocumentRoot126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot126", None)
        self.__BPMN2Model_DocumentRoot126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Extension"):
                    opp_val = getattr(item, "BPMN2Model_Extension", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Extension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Extension"):
                    opp_val = getattr(item, "BPMN2Model_Extension", None)
                    
                    setattr(item, "BPMN2Model_Extension", self)
                    

    @property
    def BPMN2Model_DocumentRoot54(self):
        return self.__BPMN2Model_DocumentRoot54

    @BPMN2Model_DocumentRoot54.setter
    def BPMN2Model_DocumentRoot54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot54", None)
        self.__BPMN2Model_DocumentRoot54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ChoreographyActivity"):
                    opp_val = getattr(item, "BPMN2Model_ChoreographyActivity", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ChoreographyActivity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ChoreographyActivity"):
                    opp_val = getattr(item, "BPMN2Model_ChoreographyActivity", None)
                    
                    setattr(item, "BPMN2Model_ChoreographyActivity", self)
                    

    @property
    def BPMN2Model_DocumentRoot58(self):
        return self.__BPMN2Model_DocumentRoot58

    @BPMN2Model_DocumentRoot58.setter
    def BPMN2Model_DocumentRoot58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot58", None)
        self.__BPMN2Model_DocumentRoot58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_CompensateEventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_CompensateEventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_CompensateEventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_CompensateEventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_CompensateEventDefinition", None)
                    
                    setattr(item, "BPMN2Model_CompensateEventDefinition", self)
                    

    @property
    def BPMN2Model_DocumentRoot36(self):
        return self.__BPMN2Model_DocumentRoot36

    @BPMN2Model_DocumentRoot36.setter
    def BPMN2Model_DocumentRoot36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot36", None)
        self.__BPMN2Model_DocumentRoot36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ConversationNode"):
                    opp_val = getattr(item, "BPMN2Model_ConversationNode", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ConversationNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ConversationNode"):
                    opp_val = getattr(item, "BPMN2Model_ConversationNode", None)
                    
                    setattr(item, "BPMN2Model_ConversationNode", self)
                    

    @property
    def BPMN2Model_DocumentRoot32(self):
        return self.__BPMN2Model_DocumentRoot32

    @BPMN2Model_DocumentRoot32.setter
    def BPMN2Model_DocumentRoot32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot32", None)
        self.__BPMN2Model_DocumentRoot32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_CallChoreography"):
                    opp_val = getattr(item, "BPMN2Model_CallChoreography", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_CallChoreography", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_CallChoreography"):
                    opp_val = getattr(item, "BPMN2Model_CallChoreography", None)
                    
                    setattr(item, "BPMN2Model_CallChoreography", self)
                    

    @property
    def BPMN2Model_DocumentRoot180(self):
        return self.__BPMN2Model_DocumentRoot180

    @BPMN2Model_DocumentRoot180.setter
    def BPMN2Model_DocumentRoot180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot180", None)
        self.__BPMN2Model_DocumentRoot180 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_LaneSet"):
                    opp_val = getattr(item, "BPMN2Model_LaneSet", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_LaneSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_LaneSet"):
                    opp_val = getattr(item, "BPMN2Model_LaneSet", None)
                    
                    setattr(item, "BPMN2Model_LaneSet", self)
                    

    @property
    def BPMN2Model_DocumentRoot158(self):
        return self.__BPMN2Model_DocumentRoot158

    @BPMN2Model_DocumentRoot158.setter
    def BPMN2Model_DocumentRoot158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot158", None)
        self.__BPMN2Model_DocumentRoot158 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ImplicitThrowEvent"):
                    opp_val = getattr(item, "BPMN2Model_ImplicitThrowEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ImplicitThrowEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ImplicitThrowEvent"):
                    opp_val = getattr(item, "BPMN2Model_ImplicitThrowEvent", None)
                    
                    setattr(item, "BPMN2Model_ImplicitThrowEvent", self)
                    

    @property
    def BPMN2Model_DocumentRoot252(self):
        return self.__BPMN2Model_DocumentRoot252

    @BPMN2Model_DocumentRoot252.setter
    def BPMN2Model_DocumentRoot252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot252", None)
        self.__BPMN2Model_DocumentRoot252 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_StartEvent"):
                    opp_val = getattr(item, "BPMN2Model_StartEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_StartEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_StartEvent"):
                    opp_val = getattr(item, "BPMN2Model_StartEvent", None)
                    
                    setattr(item, "BPMN2Model_StartEvent", self)
                    

    @property
    def BPMN2Model_DocumentRoot246(self):
        return self.__BPMN2Model_DocumentRoot246

    @BPMN2Model_DocumentRoot246.setter
    def BPMN2Model_DocumentRoot246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot246", None)
        self.__BPMN2Model_DocumentRoot246 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Signal"):
                    opp_val = getattr(item, "BPMN2Model_Signal", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Signal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Signal"):
                    opp_val = getattr(item, "BPMN2Model_Signal", None)
                    
                    setattr(item, "BPMN2Model_Signal", self)
                    

    @property
    def BPMN2Model_DocumentRoot21(self):
        return self.__BPMN2Model_DocumentRoot21

    @BPMN2Model_DocumentRoot21.setter
    def BPMN2Model_DocumentRoot21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot21", None)
        self.__BPMN2Model_DocumentRoot21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_BaseElement22"):
                    opp_val = getattr(item, "BPMN2Model_BaseElement22", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_BaseElement22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_BaseElement22"):
                    opp_val = getattr(item, "BPMN2Model_BaseElement22", None)
                    
                    setattr(item, "BPMN2Model_BaseElement22", self)
                    

    @property
    def BPMN2Model_DocumentRoot114(self):
        return self.__BPMN2Model_DocumentRoot114

    @BPMN2Model_DocumentRoot114.setter
    def BPMN2Model_DocumentRoot114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot114", None)
        self.__BPMN2Model_DocumentRoot114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Escalation"):
                    opp_val = getattr(item, "BPMN2Model_Escalation", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Escalation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Escalation"):
                    opp_val = getattr(item, "BPMN2Model_Escalation", None)
                    
                    setattr(item, "BPMN2Model_Escalation", self)
                    

    @property
    def BPMN2Model_DocumentRoot242(self):
        return self.__BPMN2Model_DocumentRoot242

    @BPMN2Model_DocumentRoot242.setter
    def BPMN2Model_DocumentRoot242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot242", None)
        self.__BPMN2Model_DocumentRoot242 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_SequenceFlow"):
                    opp_val = getattr(item, "BPMN2Model_SequenceFlow", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_SequenceFlow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_SequenceFlow"):
                    opp_val = getattr(item, "BPMN2Model_SequenceFlow", None)
                    
                    setattr(item, "BPMN2Model_SequenceFlow", self)
                    

    @property
    def BPMN2Model_DocumentRoot74(self):
        return self.__BPMN2Model_DocumentRoot74

    @BPMN2Model_DocumentRoot74.setter
    def BPMN2Model_DocumentRoot74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot74", None)
        self.__BPMN2Model_DocumentRoot74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_CorrelationProperty"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_CorrelationProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_CorrelationProperty"):
                    opp_val = getattr(item, "BPMN2Model_CorrelationProperty", None)
                    
                    setattr(item, "BPMN2Model_CorrelationProperty", self)
                    

    @property
    def BPMN2Model_DocumentRoot198(self):
        return self.__BPMN2Model_DocumentRoot198

    @BPMN2Model_DocumentRoot198.setter
    def BPMN2Model_DocumentRoot198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot198", None)
        self.__BPMN2Model_DocumentRoot198 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_MultiInstanceLoopCharacteristics"):
                    opp_val = getattr(item, "BPMN2Model_MultiInstanceLoopCharacteristics", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_MultiInstanceLoopCharacteristics", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_MultiInstanceLoopCharacteristics"):
                    opp_val = getattr(item, "BPMN2Model_MultiInstanceLoopCharacteristics", None)
                    
                    setattr(item, "BPMN2Model_MultiInstanceLoopCharacteristics", self)
                    

    @property
    def BPMN2Model_DocumentRoot70(self):
        return self.__BPMN2Model_DocumentRoot70

    @BPMN2Model_DocumentRoot70.setter
    def BPMN2Model_DocumentRoot70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot70", None)
        self.__BPMN2Model_DocumentRoot70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ConversationLink"):
                    opp_val = getattr(item, "BPMN2Model_ConversationLink", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ConversationLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ConversationLink"):
                    opp_val = getattr(item, "BPMN2Model_ConversationLink", None)
                    
                    setattr(item, "BPMN2Model_ConversationLink", self)
                    

    @property
    def BPMN2Model_DocumentRoot66(self):
        return self.__BPMN2Model_DocumentRoot66

    @BPMN2Model_DocumentRoot66.setter
    def BPMN2Model_DocumentRoot66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot66", None)
        self.__BPMN2Model_DocumentRoot66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Conversation"):
                    opp_val = getattr(item, "BPMN2Model_Conversation", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Conversation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Conversation"):
                    opp_val = getattr(item, "BPMN2Model_Conversation", None)
                    
                    setattr(item, "BPMN2Model_Conversation", self)
                    

    @property
    def BPMN2Model_DocumentRoot178(self):
        return self.__BPMN2Model_DocumentRoot178

    @BPMN2Model_DocumentRoot178.setter
    def BPMN2Model_DocumentRoot178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot178", None)
        self.__BPMN2Model_DocumentRoot178 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Lane"):
                    opp_val = getattr(item, "BPMN2Model_Lane", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Lane", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Lane"):
                    opp_val = getattr(item, "BPMN2Model_Lane", None)
                    
                    setattr(item, "BPMN2Model_Lane", self)
                    

    @property
    def BPMN2Model_DocumentRoot271(self):
        return self.__BPMN2Model_DocumentRoot271

    @BPMN2Model_DocumentRoot271.setter
    def BPMN2Model_DocumentRoot271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot271", None)
        self.__BPMN2Model_DocumentRoot271 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_TimerEventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_TimerEventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_TimerEventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_TimerEventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_TimerEventDefinition", None)
                    
                    setattr(item, "BPMN2Model_TimerEventDefinition", self)
                    

    @property
    def BPMN2Model_DocumentRoot170(self):
        return self.__BPMN2Model_DocumentRoot170

    @BPMN2Model_DocumentRoot170.setter
    def BPMN2Model_DocumentRoot170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot170", None)
        self.__BPMN2Model_DocumentRoot170 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_IntermediateThrowEvent"):
                    opp_val = getattr(item, "BPMN2Model_IntermediateThrowEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_IntermediateThrowEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_IntermediateThrowEvent"):
                    opp_val = getattr(item, "BPMN2Model_IntermediateThrowEvent", None)
                    
                    setattr(item, "BPMN2Model_IntermediateThrowEvent", self)
                    

    @property
    def BPMN2Model_DocumentRoot220(self):
        return self.__BPMN2Model_DocumentRoot220

    @BPMN2Model_DocumentRoot220.setter
    def BPMN2Model_DocumentRoot220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot220", None)
        self.__BPMN2Model_DocumentRoot220 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Property"):
                    opp_val = getattr(item, "BPMN2Model_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Property"):
                    opp_val = getattr(item, "BPMN2Model_Property", None)
                    
                    setattr(item, "BPMN2Model_Property", self)
                    

    @property
    def BPMN2Model_DocumentRoot34(self):
        return self.__BPMN2Model_DocumentRoot34

    @BPMN2Model_DocumentRoot34.setter
    def BPMN2Model_DocumentRoot34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot34", None)
        self.__BPMN2Model_DocumentRoot34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_CallConversation"):
                    opp_val = getattr(item, "BPMN2Model_CallConversation", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_CallConversation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_CallConversation"):
                    opp_val = getattr(item, "BPMN2Model_CallConversation", None)
                    
                    setattr(item, "BPMN2Model_CallConversation", self)
                    

    @property
    def BPMN2Model_DocumentRoot112(self):
        return self.__BPMN2Model_DocumentRoot112

    @BPMN2Model_DocumentRoot112.setter
    def BPMN2Model_DocumentRoot112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot112", None)
        self.__BPMN2Model_DocumentRoot112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ErrorEventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_ErrorEventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ErrorEventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ErrorEventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_ErrorEventDefinition", None)
                    
                    setattr(item, "BPMN2Model_ErrorEventDefinition", self)
                    

    @property
    def BPMN2Model_DocumentRoot236(self):
        return self.__BPMN2Model_DocumentRoot236

    @BPMN2Model_DocumentRoot236.setter
    def BPMN2Model_DocumentRoot236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot236", None)
        self.__BPMN2Model_DocumentRoot236 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_EObject"):
                    opp_val = getattr(item, "BPMN2Model_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_EObject"):
                    opp_val = getattr(item, "BPMN2Model_EObject", None)
                    
                    setattr(item, "BPMN2Model_EObject", self)
                    

    @property
    def BPMN2Model_DocumentRoot196(self):
        return self.__BPMN2Model_DocumentRoot196

    @BPMN2Model_DocumentRoot196.setter
    def BPMN2Model_DocumentRoot196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot196", None)
        self.__BPMN2Model_DocumentRoot196 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Monitoring"):
                    opp_val = getattr(item, "BPMN2Model_Monitoring", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Monitoring", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Monitoring"):
                    opp_val = getattr(item, "BPMN2Model_Monitoring", None)
                    
                    setattr(item, "BPMN2Model_Monitoring", self)
                    

    @property
    def BPMN2Model_DocumentRoot24(self):
        return self.__BPMN2Model_DocumentRoot24

    @BPMN2Model_DocumentRoot24.setter
    def BPMN2Model_DocumentRoot24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot24", None)
        self.__BPMN2Model_DocumentRoot24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_BoundaryEvent"):
                    opp_val = getattr(item, "BPMN2Model_BoundaryEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_BoundaryEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_BoundaryEvent"):
                    opp_val = getattr(item, "BPMN2Model_BoundaryEvent", None)
                    
                    setattr(item, "BPMN2Model_BoundaryEvent", self)
                    

    @property
    def BPMN2Model_DocumentRoot28(self):
        return self.__BPMN2Model_DocumentRoot28

    @BPMN2Model_DocumentRoot28.setter
    def BPMN2Model_DocumentRoot28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot28", None)
        self.__BPMN2Model_DocumentRoot28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_CallableElement"):
                    opp_val = getattr(item, "BPMN2Model_CallableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_CallableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_CallableElement"):
                    opp_val = getattr(item, "BPMN2Model_CallableElement", None)
                    
                    setattr(item, "BPMN2Model_CallableElement", self)
                    

    @property
    def BPMN2Model_DocumentRoot134(self):
        return self.__BPMN2Model_DocumentRoot134

    @BPMN2Model_DocumentRoot134.setter
    def BPMN2Model_DocumentRoot134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot134", None)
        self.__BPMN2Model_DocumentRoot134 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Gateway"):
                    opp_val = getattr(item, "BPMN2Model_Gateway", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Gateway", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Gateway"):
                    opp_val = getattr(item, "BPMN2Model_Gateway", None)
                    
                    setattr(item, "BPMN2Model_Gateway", self)
                    

    @property
    def BPMN2Model_DocumentRoot146(self):
        return self.__BPMN2Model_DocumentRoot146

    @BPMN2Model_DocumentRoot146.setter
    def BPMN2Model_DocumentRoot146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot146", None)
        self.__BPMN2Model_DocumentRoot146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_GlobalTask"):
                    opp_val = getattr(item, "BPMN2Model_GlobalTask", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_GlobalTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_GlobalTask"):
                    opp_val = getattr(item, "BPMN2Model_GlobalTask", None)
                    
                    setattr(item, "BPMN2Model_GlobalTask", self)
                    

    @property
    def BPMN2Model_DocumentRoot100(self):
        return self.__BPMN2Model_DocumentRoot100

    @BPMN2Model_DocumentRoot100.setter
    def BPMN2Model_DocumentRoot100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot100", None)
        self.__BPMN2Model_DocumentRoot100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_DataStoreReference"):
                    opp_val = getattr(item, "BPMN2Model_DataStoreReference", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_DataStoreReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_DataStoreReference"):
                    opp_val = getattr(item, "BPMN2Model_DataStoreReference", None)
                    
                    setattr(item, "BPMN2Model_DataStoreReference", self)
                    

    @property
    def BPMN2Model_DocumentRoot62(self):
        return self.__BPMN2Model_DocumentRoot62

    @BPMN2Model_DocumentRoot62.setter
    def BPMN2Model_DocumentRoot62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot62", None)
        self.__BPMN2Model_DocumentRoot62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ComplexGateway"):
                    opp_val = getattr(item, "BPMN2Model_ComplexGateway", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ComplexGateway", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ComplexGateway"):
                    opp_val = getattr(item, "BPMN2Model_ComplexGateway", None)
                    
                    setattr(item, "BPMN2Model_ComplexGateway", self)
                    

    @property
    def BPMN2Model_DocumentRoot256(self):
        return self.__BPMN2Model_DocumentRoot256

    @BPMN2Model_DocumentRoot256.setter
    def BPMN2Model_DocumentRoot256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot256", None)
        self.__BPMN2Model_DocumentRoot256 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_SubConversation"):
                    opp_val = getattr(item, "BPMN2Model_SubConversation", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_SubConversation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_SubConversation"):
                    opp_val = getattr(item, "BPMN2Model_SubConversation", None)
                    
                    setattr(item, "BPMN2Model_SubConversation", self)
                    

    @property
    def BPMN2Model_DocumentRoot42(self):
        return self.__BPMN2Model_DocumentRoot42

    @BPMN2Model_DocumentRoot42.setter
    def BPMN2Model_DocumentRoot42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot42", None)
        self.__BPMN2Model_DocumentRoot42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_RootElement"):
                    opp_val = getattr(item, "BPMN2Model_RootElement", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_RootElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_RootElement"):
                    opp_val = getattr(item, "BPMN2Model_RootElement", None)
                    
                    setattr(item, "BPMN2Model_RootElement", self)
                    

    @property
    def BPMN2Model_DocumentRoot118(self):
        return self.__BPMN2Model_DocumentRoot118

    @BPMN2Model_DocumentRoot118.setter
    def BPMN2Model_DocumentRoot118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot118", None)
        self.__BPMN2Model_DocumentRoot118 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Event"):
                    opp_val = getattr(item, "BPMN2Model_Event", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Event"):
                    opp_val = getattr(item, "BPMN2Model_Event", None)
                    
                    setattr(item, "BPMN2Model_Event", self)
                    

    @property
    def BPMN2Model_DocumentRoot238(self):
        return self.__BPMN2Model_DocumentRoot238

    @BPMN2Model_DocumentRoot238.setter
    def BPMN2Model_DocumentRoot238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot238", None)
        self.__BPMN2Model_DocumentRoot238 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ScriptTask"):
                    opp_val = getattr(item, "BPMN2Model_ScriptTask", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ScriptTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ScriptTask"):
                    opp_val = getattr(item, "BPMN2Model_ScriptTask", None)
                    
                    setattr(item, "BPMN2Model_ScriptTask", self)
                    

    @property
    def BPMN2Model_DocumentRoot9(self):
        return self.__BPMN2Model_DocumentRoot9

    @BPMN2Model_DocumentRoot9.setter
    def BPMN2Model_DocumentRoot9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot9", None)
        self.__BPMN2Model_DocumentRoot9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_FlowElement"):
                    opp_val = getattr(item, "BPMN2Model_FlowElement", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_FlowElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_FlowElement"):
                    opp_val = getattr(item, "BPMN2Model_FlowElement", None)
                    
                    setattr(item, "BPMN2Model_FlowElement", self)
                    

    @property
    def BPMN2Model_DocumentRoot174(self):
        return self.__BPMN2Model_DocumentRoot174

    @BPMN2Model_DocumentRoot174.setter
    def BPMN2Model_DocumentRoot174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot174", None)
        self.__BPMN2Model_DocumentRoot174 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_InputOutputSpecification"):
                    opp_val = getattr(item, "BPMN2Model_InputOutputSpecification", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_InputOutputSpecification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_InputOutputSpecification"):
                    opp_val = getattr(item, "BPMN2Model_InputOutputSpecification", None)
                    
                    setattr(item, "BPMN2Model_InputOutputSpecification", self)
                    

    @property
    def BPMN2Model_DocumentRoot13(self):
        return self.__BPMN2Model_DocumentRoot13

    @BPMN2Model_DocumentRoot13.setter
    def BPMN2Model_DocumentRoot13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot13", None)
        self.__BPMN2Model_DocumentRoot13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Assignment"):
                    opp_val = getattr(item, "BPMN2Model_Assignment", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Assignment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Assignment"):
                    opp_val = getattr(item, "BPMN2Model_Assignment", None)
                    
                    setattr(item, "BPMN2Model_Assignment", self)
                    

    @property
    def BPMN2Model_DocumentRoot104(self):
        return self.__BPMN2Model_DocumentRoot104

    @BPMN2Model_DocumentRoot104.setter
    def BPMN2Model_DocumentRoot104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot104", None)
        self.__BPMN2Model_DocumentRoot104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Documentation"):
                    opp_val = getattr(item, "BPMN2Model_Documentation", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Documentation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Documentation"):
                    opp_val = getattr(item, "BPMN2Model_Documentation", None)
                    
                    setattr(item, "BPMN2Model_Documentation", self)
                    

    @property
    def BPMN2Model_DocumentRoot144(self):
        return self.__BPMN2Model_DocumentRoot144

    @BPMN2Model_DocumentRoot144.setter
    def BPMN2Model_DocumentRoot144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot144", None)
        self.__BPMN2Model_DocumentRoot144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_GlobalScriptTask"):
                    opp_val = getattr(item, "BPMN2Model_GlobalScriptTask", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_GlobalScriptTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_GlobalScriptTask"):
                    opp_val = getattr(item, "BPMN2Model_GlobalScriptTask", None)
                    
                    setattr(item, "BPMN2Model_GlobalScriptTask", self)
                    

    @property
    def BPMN2Model_DocumentRoot164(self):
        return self.__BPMN2Model_DocumentRoot164

    @BPMN2Model_DocumentRoot164.setter
    def BPMN2Model_DocumentRoot164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot164", None)
        self.__BPMN2Model_DocumentRoot164 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_InputSet"):
                    opp_val = getattr(item, "BPMN2Model_InputSet", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_InputSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_InputSet"):
                    opp_val = getattr(item, "BPMN2Model_InputSet", None)
                    
                    setattr(item, "BPMN2Model_InputSet", self)
                    

    @property
    def BPMN2Model_DocumentRoot190(self):
        return self.__BPMN2Model_DocumentRoot190

    @BPMN2Model_DocumentRoot190.setter
    def BPMN2Model_DocumentRoot190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot190", None)
        self.__BPMN2Model_DocumentRoot190 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_MessageEventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_MessageEventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_MessageEventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_MessageEventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_MessageEventDefinition", None)
                    
                    setattr(item, "BPMN2Model_MessageEventDefinition", self)
                    

    @property
    def BPMN2Model_DocumentRoot182(self):
        return self.__BPMN2Model_DocumentRoot182

    @BPMN2Model_DocumentRoot182.setter
    def BPMN2Model_DocumentRoot182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot182", None)
        self.__BPMN2Model_DocumentRoot182 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_LinkEventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_LinkEventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_LinkEventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_LinkEventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_LinkEventDefinition", None)
                    
                    setattr(item, "BPMN2Model_LinkEventDefinition", self)
                    

    @property
    def BPMN2Model_DocumentRoot98(self):
        return self.__BPMN2Model_DocumentRoot98

    @BPMN2Model_DocumentRoot98.setter
    def BPMN2Model_DocumentRoot98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot98", None)
        self.__BPMN2Model_DocumentRoot98 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_DataStore"):
                    opp_val = getattr(item, "BPMN2Model_DataStore", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_DataStore", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_DataStore"):
                    opp_val = getattr(item, "BPMN2Model_DataStore", None)
                    
                    setattr(item, "BPMN2Model_DataStore", self)
                    

    @property
    def BPMN2Model_DocumentRoot260(self):
        return self.__BPMN2Model_DocumentRoot260

    @BPMN2Model_DocumentRoot260.setter
    def BPMN2Model_DocumentRoot260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot260", None)
        self.__BPMN2Model_DocumentRoot260 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Task"):
                    opp_val = getattr(item, "BPMN2Model_Task", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Task", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Task"):
                    opp_val = getattr(item, "BPMN2Model_Task", None)
                    
                    setattr(item, "BPMN2Model_Task", self)
                    

    @property
    def BPMN2Model_DocumentRoot88(self):
        return self.__BPMN2Model_DocumentRoot88

    @BPMN2Model_DocumentRoot88.setter
    def BPMN2Model_DocumentRoot88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot88", None)
        self.__BPMN2Model_DocumentRoot88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_DataObject"):
                    opp_val = getattr(item, "BPMN2Model_DataObject", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_DataObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_DataObject"):
                    opp_val = getattr(item, "BPMN2Model_DataObject", None)
                    
                    setattr(item, "BPMN2Model_DataObject", self)
                    

    @property
    def BPMN2Model_DocumentRoot258(self):
        return self.__BPMN2Model_DocumentRoot258

    @BPMN2Model_DocumentRoot258.setter
    def BPMN2Model_DocumentRoot258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot258", None)
        self.__BPMN2Model_DocumentRoot258 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_SubProcess"):
                    opp_val = getattr(item, "BPMN2Model_SubProcess", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_SubProcess", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_SubProcess"):
                    opp_val = getattr(item, "BPMN2Model_SubProcess", None)
                    
                    setattr(item, "BPMN2Model_SubProcess", self)
                    

    @property
    def BPMN2Model_DocumentRoot102(self):
        return self.__BPMN2Model_DocumentRoot102

    @BPMN2Model_DocumentRoot102.setter
    def BPMN2Model_DocumentRoot102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot102", None)
        self.__BPMN2Model_DocumentRoot102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Definitions"):
                    opp_val = getattr(item, "BPMN2Model_Definitions", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Definitions", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Definitions"):
                    opp_val = getattr(item, "BPMN2Model_Definitions", None)
                    
                    setattr(item, "BPMN2Model_Definitions", self)
                    

    @property
    def BPMN2Model_DocumentRoot40(self):
        return self.__BPMN2Model_DocumentRoot40

    @BPMN2Model_DocumentRoot40.setter
    def BPMN2Model_DocumentRoot40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot40", None)
        self.__BPMN2Model_DocumentRoot40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_EventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_EventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_EventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_EventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_EventDefinition", None)
                    
                    setattr(item, "BPMN2Model_EventDefinition", self)
                    

    @property
    def BPMN2Model_DocumentRoot176(self):
        return self.__BPMN2Model_DocumentRoot176

    @BPMN2Model_DocumentRoot176.setter
    def BPMN2Model_DocumentRoot176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot176", None)
        self.__BPMN2Model_DocumentRoot176 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ItemDefinition"):
                    opp_val = getattr(item, "BPMN2Model_ItemDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ItemDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ItemDefinition"):
                    opp_val = getattr(item, "BPMN2Model_ItemDefinition", None)
                    
                    setattr(item, "BPMN2Model_ItemDefinition", self)
                    

    @property
    def BPMN2Model_DocumentRoot222(self):
        return self.__BPMN2Model_DocumentRoot222

    @BPMN2Model_DocumentRoot222.setter
    def BPMN2Model_DocumentRoot222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot222", None)
        self.__BPMN2Model_DocumentRoot222 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ReceiveTask"):
                    opp_val = getattr(item, "BPMN2Model_ReceiveTask", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ReceiveTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ReceiveTask"):
                    opp_val = getattr(item, "BPMN2Model_ReceiveTask", None)
                    
                    setattr(item, "BPMN2Model_ReceiveTask", self)
                    

    @property
    def BPMN2Model_DocumentRoot46(self):
        return self.__BPMN2Model_DocumentRoot46

    @BPMN2Model_DocumentRoot46.setter
    def BPMN2Model_DocumentRoot46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot46", None)
        self.__BPMN2Model_DocumentRoot46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Category"):
                    opp_val = getattr(item, "BPMN2Model_Category", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Category", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Category"):
                    opp_val = getattr(item, "BPMN2Model_Category", None)
                    
                    setattr(item, "BPMN2Model_Category", self)
                    

    @property
    def BPMN2Model_DocumentRoot204(self):
        return self.__BPMN2Model_DocumentRoot204

    @BPMN2Model_DocumentRoot204.setter
    def BPMN2Model_DocumentRoot204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot204", None)
        self.__BPMN2Model_DocumentRoot204 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ParallelGateway"):
                    opp_val = getattr(item, "BPMN2Model_ParallelGateway", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ParallelGateway", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ParallelGateway"):
                    opp_val = getattr(item, "BPMN2Model_ParallelGateway", None)
                    
                    setattr(item, "BPMN2Model_ParallelGateway", self)
                    

    @property
    def BPMN2Model_DocumentRoot116(self):
        return self.__BPMN2Model_DocumentRoot116

    @BPMN2Model_DocumentRoot116.setter
    def BPMN2Model_DocumentRoot116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot116", None)
        self.__BPMN2Model_DocumentRoot116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_EscalationEventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_EscalationEventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_EscalationEventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_EscalationEventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_EscalationEventDefinition", None)
                    
                    setattr(item, "BPMN2Model_EscalationEventDefinition", self)
                    

    @property
    def BPMN2Model_DocumentRoot136(self):
        return self.__BPMN2Model_DocumentRoot136

    @BPMN2Model_DocumentRoot136.setter
    def BPMN2Model_DocumentRoot136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot136", None)
        self.__BPMN2Model_DocumentRoot136 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_GlobalBusinessRuleTask"):
                    opp_val = getattr(item, "BPMN2Model_GlobalBusinessRuleTask", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_GlobalBusinessRuleTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_GlobalBusinessRuleTask"):
                    opp_val = getattr(item, "BPMN2Model_GlobalBusinessRuleTask", None)
                    
                    setattr(item, "BPMN2Model_GlobalBusinessRuleTask", self)
                    

    @property
    def BPMN2Model_DocumentRoot15(self):
        return self.__BPMN2Model_DocumentRoot15

    @BPMN2Model_DocumentRoot15.setter
    def BPMN2Model_DocumentRoot15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot15", None)
        self.__BPMN2Model_DocumentRoot15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Association"):
                    opp_val = getattr(item, "BPMN2Model_Association", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Association", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Association"):
                    opp_val = getattr(item, "BPMN2Model_Association", None)
                    
                    setattr(item, "BPMN2Model_Association", self)
                    

    @property
    def BPMN2Model_DocumentRoot84(self):
        return self.__BPMN2Model_DocumentRoot84

    @BPMN2Model_DocumentRoot84.setter
    def BPMN2Model_DocumentRoot84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot84", None)
        self.__BPMN2Model_DocumentRoot84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_DataInput"):
                    opp_val = getattr(item, "BPMN2Model_DataInput", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_DataInput", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_DataInput"):
                    opp_val = getattr(item, "BPMN2Model_DataInput", None)
                    
                    setattr(item, "BPMN2Model_DataInput", self)
                    

    @property
    def BPMN2Model_DocumentRoot275(self):
        return self.__BPMN2Model_DocumentRoot275

    @BPMN2Model_DocumentRoot275.setter
    def BPMN2Model_DocumentRoot275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot275", None)
        self.__BPMN2Model_DocumentRoot275 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_UserTask"):
                    opp_val = getattr(item, "BPMN2Model_UserTask", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_UserTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_UserTask"):
                    opp_val = getattr(item, "BPMN2Model_UserTask", None)
                    
                    setattr(item, "BPMN2Model_UserTask", self)
                    

    @property
    def BPMN2Model_DocumentRoot273(self):
        return self.__BPMN2Model_DocumentRoot273

    @BPMN2Model_DocumentRoot273.setter
    def BPMN2Model_DocumentRoot273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot273", None)
        self.__BPMN2Model_DocumentRoot273 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Transaction"):
                    opp_val = getattr(item, "BPMN2Model_Transaction", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Transaction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Transaction"):
                    opp_val = getattr(item, "BPMN2Model_Transaction", None)
                    
                    setattr(item, "BPMN2Model_Transaction", self)
                    

    @property
    def BPMN2Model_DocumentRoot86(self):
        return self.__BPMN2Model_DocumentRoot86

    @BPMN2Model_DocumentRoot86.setter
    def BPMN2Model_DocumentRoot86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot86", None)
        self.__BPMN2Model_DocumentRoot86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_DataInputAssociation"):
                    opp_val = getattr(item, "BPMN2Model_DataInputAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_DataInputAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_DataInputAssociation"):
                    opp_val = getattr(item, "BPMN2Model_DataInputAssociation", None)
                    
                    setattr(item, "BPMN2Model_DataInputAssociation", self)
                    

    @property
    def BPMN2Model_DocumentRoot17(self):
        return self.__BPMN2Model_DocumentRoot17

    @BPMN2Model_DocumentRoot17.setter
    def BPMN2Model_DocumentRoot17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot17", None)
        self.__BPMN2Model_DocumentRoot17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Auditing"):
                    opp_val = getattr(item, "BPMN2Model_Auditing", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Auditing", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Auditing"):
                    opp_val = getattr(item, "BPMN2Model_Auditing", None)
                    
                    setattr(item, "BPMN2Model_Auditing", self)
                    

    @property
    def BPMN2Model_DocumentRoot254(self):
        return self.__BPMN2Model_DocumentRoot254

    @BPMN2Model_DocumentRoot254.setter
    def BPMN2Model_DocumentRoot254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot254", None)
        self.__BPMN2Model_DocumentRoot254 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_SubChoreography"):
                    opp_val = getattr(item, "BPMN2Model_SubChoreography", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_SubChoreography", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_SubChoreography"):
                    opp_val = getattr(item, "BPMN2Model_SubChoreography", None)
                    
                    setattr(item, "BPMN2Model_SubChoreography", self)
                    

    @property
    def BPMN2Model_DocumentRoot128(self):
        return self.__BPMN2Model_DocumentRoot128

    @BPMN2Model_DocumentRoot128.setter
    def BPMN2Model_DocumentRoot128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot128", None)
        self.__BPMN2Model_DocumentRoot128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ExtensionAttributeValue"):
                    opp_val = getattr(item, "BPMN2Model_ExtensionAttributeValue", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ExtensionAttributeValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ExtensionAttributeValue"):
                    opp_val = getattr(item, "BPMN2Model_ExtensionAttributeValue", None)
                    
                    setattr(item, "BPMN2Model_ExtensionAttributeValue", self)
                    

    @property
    def BPMN2Model_DocumentRoot132(self):
        return self.__BPMN2Model_DocumentRoot132

    @BPMN2Model_DocumentRoot132.setter
    def BPMN2Model_DocumentRoot132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot132", None)
        self.__BPMN2Model_DocumentRoot132 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_FormalExpression"):
                    opp_val = getattr(item, "BPMN2Model_FormalExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_FormalExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_FormalExpression"):
                    opp_val = getattr(item, "BPMN2Model_FormalExpression", None)
                    
                    setattr(item, "BPMN2Model_FormalExpression", self)
                    

    @property
    def BPMN2Model_DocumentRoot228(self):
        return self.__BPMN2Model_DocumentRoot228

    @BPMN2Model_DocumentRoot228.setter
    def BPMN2Model_DocumentRoot228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot228", None)
        self.__BPMN2Model_DocumentRoot228 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Resource"):
                    opp_val = getattr(item, "BPMN2Model_Resource", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Resource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Resource"):
                    opp_val = getattr(item, "BPMN2Model_Resource", None)
                    
                    setattr(item, "BPMN2Model_Resource", self)
                    

    @property
    def BPMN2Model_DocumentRoot11(self):
        return self.__BPMN2Model_DocumentRoot11

    @BPMN2Model_DocumentRoot11.setter
    def BPMN2Model_DocumentRoot11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot11", None)
        self.__BPMN2Model_DocumentRoot11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_Artifact"):
                    opp_val = getattr(item, "BPMN2Model_Artifact", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_Artifact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_Artifact"):
                    opp_val = getattr(item, "BPMN2Model_Artifact", None)
                    
                    setattr(item, "BPMN2Model_Artifact", self)
                    

    @property
    def BPMN2Model_DocumentRoot130(self):
        return self.__BPMN2Model_DocumentRoot130

    @BPMN2Model_DocumentRoot130.setter
    def BPMN2Model_DocumentRoot130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot130", None)
        self.__BPMN2Model_DocumentRoot130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_FlowNode"):
                    opp_val = getattr(item, "BPMN2Model_FlowNode", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_FlowNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_FlowNode"):
                    opp_val = getattr(item, "BPMN2Model_FlowNode", None)
                    
                    setattr(item, "BPMN2Model_FlowNode", self)
                    

    @property
    def BPMN2Model_DocumentRoot44(self):
        return self.__BPMN2Model_DocumentRoot44

    @BPMN2Model_DocumentRoot44.setter
    def BPMN2Model_DocumentRoot44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot44", None)
        self.__BPMN2Model_DocumentRoot44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_CatchEvent"):
                    opp_val = getattr(item, "BPMN2Model_CatchEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_CatchEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_CatchEvent"):
                    opp_val = getattr(item, "BPMN2Model_CatchEvent", None)
                    
                    setattr(item, "BPMN2Model_CatchEvent", self)
                    

    @property
    def BPMN2Model_DocumentRoot56(self):
        return self.__BPMN2Model_DocumentRoot56

    @BPMN2Model_DocumentRoot56.setter
    def BPMN2Model_DocumentRoot56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot56", None)
        self.__BPMN2Model_DocumentRoot56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ChoreographyTask"):
                    opp_val = getattr(item, "BPMN2Model_ChoreographyTask", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ChoreographyTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ChoreographyTask"):
                    opp_val = getattr(item, "BPMN2Model_ChoreographyTask", None)
                    
                    setattr(item, "BPMN2Model_ChoreographyTask", self)
                    

    @property
    def BPMN2Model_DocumentRoot194(self):
        return self.__BPMN2Model_DocumentRoot194

    @BPMN2Model_DocumentRoot194.setter
    def BPMN2Model_DocumentRoot194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot194", None)
        self.__BPMN2Model_DocumentRoot194 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_MessageFlowAssociation"):
                    opp_val = getattr(item, "BPMN2Model_MessageFlowAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_MessageFlowAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_MessageFlowAssociation"):
                    opp_val = getattr(item, "BPMN2Model_MessageFlowAssociation", None)
                    
                    setattr(item, "BPMN2Model_MessageFlowAssociation", self)
                    

    @property
    def BPMN2Model_DocumentRoot140(self):
        return self.__BPMN2Model_DocumentRoot140

    @BPMN2Model_DocumentRoot140.setter
    def BPMN2Model_DocumentRoot140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot140", None)
        self.__BPMN2Model_DocumentRoot140 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_GlobalConversation"):
                    opp_val = getattr(item, "BPMN2Model_GlobalConversation", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_GlobalConversation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_GlobalConversation"):
                    opp_val = getattr(item, "BPMN2Model_GlobalConversation", None)
                    
                    setattr(item, "BPMN2Model_GlobalConversation", self)
                    

    @property
    def BPMN2Model_DocumentRoot64(self):
        return self.__BPMN2Model_DocumentRoot64

    @BPMN2Model_DocumentRoot64.setter
    def BPMN2Model_DocumentRoot64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot64", None)
        self.__BPMN2Model_DocumentRoot64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ConditionalEventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_ConditionalEventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ConditionalEventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ConditionalEventDefinition"):
                    opp_val = getattr(item, "BPMN2Model_ConditionalEventDefinition", None)
                    
                    setattr(item, "BPMN2Model_ConditionalEventDefinition", self)
                    

    @property
    def BPMN2Model_DocumentRoot19(self):
        return self.__BPMN2Model_DocumentRoot19

    @BPMN2Model_DocumentRoot19.setter
    def BPMN2Model_DocumentRoot19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot19", None)
        self.__BPMN2Model_DocumentRoot19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_BaseElement"):
                    opp_val = getattr(item, "BPMN2Model_BaseElement", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_BaseElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_BaseElement"):
                    opp_val = getattr(item, "BPMN2Model_BaseElement", None)
                    
                    setattr(item, "BPMN2Model_BaseElement", self)
                    

    @property
    def BPMN2Model_DocumentRoot60(self):
        return self.__BPMN2Model_DocumentRoot60

    @BPMN2Model_DocumentRoot60.setter
    def BPMN2Model_DocumentRoot60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot60", None)
        self.__BPMN2Model_DocumentRoot60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ComplexBehaviorDefinition"):
                    opp_val = getattr(item, "BPMN2Model_ComplexBehaviorDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ComplexBehaviorDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ComplexBehaviorDefinition"):
                    opp_val = getattr(item, "BPMN2Model_ComplexBehaviorDefinition", None)
                    
                    setattr(item, "BPMN2Model_ComplexBehaviorDefinition", self)
                    

    @property
    def BPMN2Model_DocumentRoot2(self):
        return self.__BPMN2Model_DocumentRoot2

    @BPMN2Model_DocumentRoot2.setter
    def BPMN2Model_DocumentRoot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot2", None)
        self.__BPMN2Model_DocumentRoot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "BPMN2Model_EStringToStringMapEntry3", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_EStringToStringMapEntry3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "BPMN2Model_EStringToStringMapEntry3", None)
                    
                    setattr(item, "BPMN2Model_EStringToStringMapEntry3", self)
                    

    @property
    def BPMN2Model_DocumentRoot186(self):
        return self.__BPMN2Model_DocumentRoot186

    @BPMN2Model_DocumentRoot186.setter
    def BPMN2Model_DocumentRoot186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BPMN2Model_DocumentRoot__BPMN2Model_DocumentRoot186", None)
        self.__BPMN2Model_DocumentRoot186 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BPMN2Model_ManualTask"):
                    opp_val = getattr(item, "BPMN2Model_ManualTask", None)
                    
                    if opp_val == self:
                        setattr(item, "BPMN2Model_ManualTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BPMN2Model_ManualTask"):
                    opp_val = getattr(item, "BPMN2Model_ManualTask", None)
                    
                    setattr(item, "BPMN2Model_ManualTask", self)
                    
