from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class VariableAction:

    pass
class Actions_StructuredActions_ReadVariableAction(VariableAction):

    pass
class Actions_StructuredActions_Variable:

    pass
class Actions_StructuredActions_ClearVariableAction(VariableAction):

    pass
class WriteVariableAction:

    pass
class Actions_StructuredActions_RemoveVariableValueAction(WriteVariableAction):

    pass
class Actions_StructuredActions_AddVariableValueAction(WriteVariableAction):

    pass
class Actions_StructuredActions_WriteVariableAction(VariableAction):

    pass
class Variable:

    pass
class CreateLinkAction:

    pass
class Actions_CompleteActions_CreateLinkObjectAction(CreateLinkAction):

    pass
class Actions_CompleteActions_ReadlsClassifiedObjectAction:

    pass
class Actions_CompleteActions_Trigger:

    pass
class AcceptEventAction:

    pass
class Actions_CompleteActions_AcceptCallAction(AcceptEventAction):

    pass
class WriteLinkAction:

    pass
class Actions_IntermediateActions_CreateLinkAction(WriteLinkAction):

    pass
class Trigger:

    pass
class Actions_IntermediateActions_DestroyLinkAction(WriteLinkAction):

    pass
class Actions_IntermediateActions_Element(ABC):

    pass
class LinkAction:

    pass
class Actions_IntermediateActions_WriteLinkAction(LinkAction):

    pass
class Actions_IntermediateActions_ReadLinkAction(LinkAction):

    pass
class Actions_IntermediateActions_Property:

    pass
class QualifierValue:

    pass
class Property:

    pass
class Element:

    pass
class Actions_CompleteActions_QualifierValue(Element):

    pass
class Actions_IntermediateActions_LinkEndData(Element):

    pass
class LinkEndData:

    pass
class Actions_IntermediateActions_LinkEndDestructionData(LinkEndData):

    def __init__(self, isDestroyDuplicates: bool, Actions_IntermediateActions_LinkEndDestructionData: "InputPin" = None, LinkEndData: "Actions_IntermediateActions_LinkAction"):
        self.isDestroyDuplicates = isDestroyDuplicates
        self.Actions_IntermediateActions_LinkEndDestructionData = Actions_IntermediateActions_LinkEndDestructionData
        
    @property
    def isDestroyDuplicates(self) -> bool:
        return self.__isDestroyDuplicates

    @isDestroyDuplicates.setter
    def isDestroyDuplicates(self, isDestroyDuplicates: bool):
        self.__isDestroyDuplicates = isDestroyDuplicates

    @property
    def Actions_IntermediateActions_LinkEndDestructionData(self):
        return self.__Actions_IntermediateActions_LinkEndDestructionData

    @Actions_IntermediateActions_LinkEndDestructionData.setter
    def Actions_IntermediateActions_LinkEndDestructionData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Actions_IntermediateActions_LinkEndDestructionData__Actions_IntermediateActions_LinkEndDestructionData", None)
        self.__Actions_IntermediateActions_LinkEndDestructionData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InputPin85"):
                opp_val = getattr(old_value, "InputPin85", None)
                if opp_val == self:
                    setattr(old_value, "InputPin85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InputPin85"):
                opp_val = getattr(value, "InputPin85", None)
                setattr(value, "InputPin85", self)

class Actions_IntermediateActions_LinkEndCreationData(LinkEndData):

    def __init__(self, isReplaceAll: bool, Actions_IntermediateActions_LinkEndCreationData: "InputPin" = None, LinkEndData: "Actions_IntermediateActions_LinkAction"):
        self.isReplaceAll = isReplaceAll
        self.Actions_IntermediateActions_LinkEndCreationData = Actions_IntermediateActions_LinkEndCreationData
        
    @property
    def isReplaceAll(self) -> bool:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: bool):
        self.__isReplaceAll = isReplaceAll

    @property
    def Actions_IntermediateActions_LinkEndCreationData(self):
        return self.__Actions_IntermediateActions_LinkEndCreationData

    @Actions_IntermediateActions_LinkEndCreationData.setter
    def Actions_IntermediateActions_LinkEndCreationData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Actions_IntermediateActions_LinkEndCreationData__Actions_IntermediateActions_LinkEndCreationData", None)
        self.__Actions_IntermediateActions_LinkEndCreationData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InputPin83"):
                opp_val = getattr(old_value, "InputPin83", None)
                if opp_val == self:
                    setattr(old_value, "InputPin83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InputPin83"):
                opp_val = getattr(value, "InputPin83", None)
                setattr(value, "InputPin83", self)

class StructuralFeature:

    pass
class WriteStructuralFeatureAction:

    pass
class Actions_IntermediateActions_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class Actions_IntermediateActions_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class StructuralFeatureAction:

    pass
class Actions_IntermediateActions_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class Actions_IntermediateActions_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class Actions_IntermediateActions_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class Actions_IntermediateActions_StructuralFeature(ABC):

    pass
class Actions_BasicActions_Operation:

    pass
class Actions_BasicActions_Signal:

    pass
class Signal:

    pass
class ValueSpecification:

    pass
class Operation:

    pass
class Actions_BasicActions_CallOperationAction:

    pass
class Actions_BasicActions_Behavior(ABC):

    pass
class Behavior:

    pass
class CallAction:

    pass
class Actions_CompleteActions_StartObjectBehaviorAction(CallAction):

    pass
class Actions_BasicActions_CallBehaviorAction(CallAction):

    pass
class InvocationAction:

    pass
class Actions_IntermediateActions_BroadcastSignalAction(InvocationAction):

    pass
class Actions_IntermediateActions_SendObjectAction(InvocationAction):

    pass
class Actions_BasicActions_SendSignalAction(InvocationAction):

    pass
class Actions_BasicActions_CallAction(InvocationAction):

    def __init__(self, isSynchronous: bool, Actions_BasicActions_CallAction: set["OutputPin"] = None):
        self.isSynchronous = isSynchronous
        self.Actions_BasicActions_CallAction = Actions_BasicActions_CallAction if Actions_BasicActions_CallAction is not None else set()
        
    @property
    def isSynchronous(self) -> bool:
        return self.__isSynchronous

    @isSynchronous.setter
    def isSynchronous(self, isSynchronous: bool):
        self.__isSynchronous = isSynchronous

    @property
    def Actions_BasicActions_CallAction(self):
        return self.__Actions_BasicActions_CallAction

    @Actions_BasicActions_CallAction.setter
    def Actions_BasicActions_CallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Actions_BasicActions_CallAction__Actions_BasicActions_CallAction", None)
        self.__Actions_BasicActions_CallAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputPin14"):
                    opp_val = getattr(item, "OutputPin14", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputPin14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputPin14"):
                    opp_val = getattr(item, "OutputPin14", None)
                    
                    setattr(item, "OutputPin14", self)
                    

class Actions_BasicActions_ValueSpecification(ABC):

    pass
class Actions_BasicActions_NamedElement(ABC):

    pass
class OutputPin:

    pass
class Actions_BasicActions_TypedElement(ABC):

    pass
class Actions_BasicActions_MultiplicityElement(ABC):

    pass
class BasicActions_MultiplicityElement:

    pass
class BasicActions_TypedElement:

    pass
class Actions_BasicActions_Pin(BasicActions_TypedElement, BasicActions_MultiplicityElement):

    pass
class Pin:

    pass
class Actions_BasicActions_OutputPin(Pin):

    pass
class Actions_BasicActions_InputPin(Pin):

    pass
class Action:

    pass
class Actions_IntermediateActions_LinkAction(Action):

    pass
class Actions_IntermediateActions_CreateObjectAction(Action):

    pass
class Actions_IntermediateActions_ReadSelfAction(Action):

    pass
class Actions_CompleteActions_ReadLinkObjectEndAction(Action):

    pass
class Actions_CompleteActions_ReadExtendAction(Action):

    pass
class Actions_StructuredActions_RaiseExceptionAction(Action):

    pass
class Actions_CompleteActions_AcceptEventAction(Action):

    def __init__(self, isUnmarshall: bool, Actions_CompleteActions_AcceptEventAction: set["OutputPin"] = None, Actions_CompleteActions_AcceptEventAction104: set["Trigger"] = None, Action: "Actions_StructuredActions_ActionInputPin"):
        self.isUnmarshall = isUnmarshall
        self.Actions_CompleteActions_AcceptEventAction = Actions_CompleteActions_AcceptEventAction if Actions_CompleteActions_AcceptEventAction is not None else set()
        self.Actions_CompleteActions_AcceptEventAction104 = Actions_CompleteActions_AcceptEventAction104 if Actions_CompleteActions_AcceptEventAction104 is not None else set()
        
    @property
    def isUnmarshall(self) -> bool:
        return self.__isUnmarshall

    @isUnmarshall.setter
    def isUnmarshall(self, isUnmarshall: bool):
        self.__isUnmarshall = isUnmarshall

    @property
    def Actions_CompleteActions_AcceptEventAction(self):
        return self.__Actions_CompleteActions_AcceptEventAction

    @Actions_CompleteActions_AcceptEventAction.setter
    def Actions_CompleteActions_AcceptEventAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Actions_CompleteActions_AcceptEventAction__Actions_CompleteActions_AcceptEventAction", None)
        self.__Actions_CompleteActions_AcceptEventAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputPin102"):
                    opp_val = getattr(item, "OutputPin102", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputPin102", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputPin102"):
                    opp_val = getattr(item, "OutputPin102", None)
                    
                    setattr(item, "OutputPin102", self)
                    

    @property
    def Actions_CompleteActions_AcceptEventAction104(self):
        return self.__Actions_CompleteActions_AcceptEventAction104

    @Actions_CompleteActions_AcceptEventAction104.setter
    def Actions_CompleteActions_AcceptEventAction104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Actions_CompleteActions_AcceptEventAction__Actions_CompleteActions_AcceptEventAction104", None)
        self.__Actions_CompleteActions_AcceptEventAction104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Trigger105"):
                    opp_val = getattr(item, "Trigger105", None)
                    
                    if opp_val == self:
                        setattr(item, "Trigger105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trigger105"):
                    opp_val = getattr(item, "Trigger105", None)
                    
                    setattr(item, "Trigger105", self)
                    

class Actions_CompleteActions_StartClassifierBehaviorAction(Action):

    pass
class Actions_IntermediateActions_StructuralFeatureAction(Action):

    pass
class Actions_IntermediateActions_ValueSpecificationAction(Action):

    pass
class Actions_StructuredActions_VariableAction(Action):

    pass
class Actions_IntermediateActions_TestIdentityAction(Action):

    pass
class Actions_CompleteActions_UnmarshallAction(Action):

    pass
class Actions_BasicActions_InvocationAction(Action):

    pass
class Actions_CompleteActions_ReduceAction(Action):

    def __init__(self, isOrdered: bool, Actions_CompleteActions_ReduceAction: "OutputPin" = None, Actions_CompleteActions_ReduceAction156: "InputPin" = None, Actions_CompleteActions_ReduceAction159: "Behavior" = None, Action: "Actions_StructuredActions_ActionInputPin"):
        self.isOrdered = isOrdered
        self.Actions_CompleteActions_ReduceAction = Actions_CompleteActions_ReduceAction
        self.Actions_CompleteActions_ReduceAction156 = Actions_CompleteActions_ReduceAction156
        self.Actions_CompleteActions_ReduceAction159 = Actions_CompleteActions_ReduceAction159
        
    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def Actions_CompleteActions_ReduceAction(self):
        return self.__Actions_CompleteActions_ReduceAction

    @Actions_CompleteActions_ReduceAction.setter
    def Actions_CompleteActions_ReduceAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Actions_CompleteActions_ReduceAction__Actions_CompleteActions_ReduceAction", None)
        self.__Actions_CompleteActions_ReduceAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OutputPin154"):
                opp_val = getattr(old_value, "OutputPin154", None)
                if opp_val == self:
                    setattr(old_value, "OutputPin154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OutputPin154"):
                opp_val = getattr(value, "OutputPin154", None)
                setattr(value, "OutputPin154", self)

    @property
    def Actions_CompleteActions_ReduceAction159(self):
        return self.__Actions_CompleteActions_ReduceAction159

    @Actions_CompleteActions_ReduceAction159.setter
    def Actions_CompleteActions_ReduceAction159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Actions_CompleteActions_ReduceAction__Actions_CompleteActions_ReduceAction159", None)
        self.__Actions_CompleteActions_ReduceAction159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behavior160"):
                opp_val = getattr(old_value, "Behavior160", None)
                if opp_val == self:
                    setattr(old_value, "Behavior160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behavior160"):
                opp_val = getattr(value, "Behavior160", None)
                setattr(value, "Behavior160", self)

    @property
    def Actions_CompleteActions_ReduceAction156(self):
        return self.__Actions_CompleteActions_ReduceAction156

    @Actions_CompleteActions_ReduceAction156.setter
    def Actions_CompleteActions_ReduceAction156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Actions_CompleteActions_ReduceAction__Actions_CompleteActions_ReduceAction156", None)
        self.__Actions_CompleteActions_ReduceAction156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InputPin157"):
                opp_val = getattr(old_value, "InputPin157", None)
                if opp_val == self:
                    setattr(old_value, "InputPin157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InputPin157"):
                opp_val = getattr(value, "InputPin157", None)
                setattr(value, "InputPin157", self)

class Actions_IntermediateActions_DestroyObjectAction(Action):

    pass
class Actions_CompleteActions_ReplyAction(Action):

    pass
class Actions_CompleteActions_ReadLinkObjectEndQualifierAction(Action):

    pass
class Actions_CompleteActions_ReclassifyObjectAction(Action):

    def __init__(self, isReplaceAll: bool, Actions_CompleteActions_ReclassifyObjectAction: "InputPin" = None, Actions_CompleteActions_ReclassifyObjectAction116: set["Classifier"] = None, Actions_CompleteActions_ReclassifyObjectAction119: set["Classifier"] = None, Action: "Actions_StructuredActions_ActionInputPin"):
        self.isReplaceAll = isReplaceAll
        self.Actions_CompleteActions_ReclassifyObjectAction = Actions_CompleteActions_ReclassifyObjectAction
        self.Actions_CompleteActions_ReclassifyObjectAction116 = Actions_CompleteActions_ReclassifyObjectAction116 if Actions_CompleteActions_ReclassifyObjectAction116 is not None else set()
        self.Actions_CompleteActions_ReclassifyObjectAction119 = Actions_CompleteActions_ReclassifyObjectAction119 if Actions_CompleteActions_ReclassifyObjectAction119 is not None else set()
        
    @property
    def isReplaceAll(self) -> bool:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: bool):
        self.__isReplaceAll = isReplaceAll

    @property
    def Actions_CompleteActions_ReclassifyObjectAction119(self):
        return self.__Actions_CompleteActions_ReclassifyObjectAction119

    @Actions_CompleteActions_ReclassifyObjectAction119.setter
    def Actions_CompleteActions_ReclassifyObjectAction119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Actions_CompleteActions_ReclassifyObjectAction__Actions_CompleteActions_ReclassifyObjectAction119", None)
        self.__Actions_CompleteActions_ReclassifyObjectAction119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Classifier120"):
                    opp_val = getattr(item, "Classifier120", None)
                    
                    if opp_val == self:
                        setattr(item, "Classifier120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Classifier120"):
                    opp_val = getattr(item, "Classifier120", None)
                    
                    setattr(item, "Classifier120", self)
                    

    @property
    def Actions_CompleteActions_ReclassifyObjectAction116(self):
        return self.__Actions_CompleteActions_ReclassifyObjectAction116

    @Actions_CompleteActions_ReclassifyObjectAction116.setter
    def Actions_CompleteActions_ReclassifyObjectAction116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Actions_CompleteActions_ReclassifyObjectAction__Actions_CompleteActions_ReclassifyObjectAction116", None)
        self.__Actions_CompleteActions_ReclassifyObjectAction116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Classifier117"):
                    opp_val = getattr(item, "Classifier117", None)
                    
                    if opp_val == self:
                        setattr(item, "Classifier117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Classifier117"):
                    opp_val = getattr(item, "Classifier117", None)
                    
                    setattr(item, "Classifier117", self)
                    

    @property
    def Actions_CompleteActions_ReclassifyObjectAction(self):
        return self.__Actions_CompleteActions_ReclassifyObjectAction

    @Actions_CompleteActions_ReclassifyObjectAction.setter
    def Actions_CompleteActions_ReclassifyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Actions_CompleteActions_ReclassifyObjectAction__Actions_CompleteActions_ReclassifyObjectAction", None)
        self.__Actions_CompleteActions_ReclassifyObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InputPin114"):
                opp_val = getattr(old_value, "InputPin114", None)
                if opp_val == self:
                    setattr(old_value, "InputPin114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InputPin114"):
                opp_val = getattr(value, "InputPin114", None)
                setattr(value, "InputPin114", self)

class Actions_BasicActions_OpaqueAction(Action):

    def __init__(self, body: str, language: str, Actions_BasicActions_OpaqueAction: set["InputPin"] = None, Actions_BasicActions_OpaqueAction8: set["OutputPin"] = None, Action: "Actions_StructuredActions_ActionInputPin"):
        self.body = body
        self.language = language
        self.Actions_BasicActions_OpaqueAction = Actions_BasicActions_OpaqueAction if Actions_BasicActions_OpaqueAction is not None else set()
        self.Actions_BasicActions_OpaqueAction8 = Actions_BasicActions_OpaqueAction8 if Actions_BasicActions_OpaqueAction8 is not None else set()
        
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
    def Actions_BasicActions_OpaqueAction8(self):
        return self.__Actions_BasicActions_OpaqueAction8

    @Actions_BasicActions_OpaqueAction8.setter
    def Actions_BasicActions_OpaqueAction8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Actions_BasicActions_OpaqueAction__Actions_BasicActions_OpaqueAction8", None)
        self.__Actions_BasicActions_OpaqueAction8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputPin9"):
                    opp_val = getattr(item, "OutputPin9", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputPin9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputPin9"):
                    opp_val = getattr(item, "OutputPin9", None)
                    
                    setattr(item, "OutputPin9", self)
                    

    @property
    def Actions_BasicActions_OpaqueAction(self):
        return self.__Actions_BasicActions_OpaqueAction

    @Actions_BasicActions_OpaqueAction.setter
    def Actions_BasicActions_OpaqueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Actions_BasicActions_OpaqueAction__Actions_BasicActions_OpaqueAction", None)
        self.__Actions_BasicActions_OpaqueAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputPin6"):
                    opp_val = getattr(item, "InputPin6", None)
                    
                    if opp_val == self:
                        setattr(item, "InputPin6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputPin6"):
                    opp_val = getattr(item, "InputPin6", None)
                    
                    setattr(item, "InputPin6", self)
                    

class Actions_BasicActions_Classifier(ABC):

    pass
class InputPin:

    pass
class Actions_BasicActions_ValuePin(InputPin):

    pass
class Actions_StructuredActions_ActionInputPin(InputPin):

    pass
class Classifier:

    pass
class NamedElement:

    pass
class Actions_BasicActions_Action(NamedElement):

    pass