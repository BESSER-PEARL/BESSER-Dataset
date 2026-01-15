from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ExpansionKind(Enum):
    parallel = "parallel"
    iterative = "iterative"
    stream = "stream"
class CallConcurrencyKind(Enum):
    sequential = "sequential"
class ParameterDirectionKind(Enum):
    in = "in"
    out = "out"
    inout = "inout"
    return = "return"


############################################
# Definition of Classes
############################################

class BasicBehaviors_ParameterValue:

    pass
class xmof_BasicBehaviors_ParameterValueDefinition:

    pass
class Kernel_Value:

    pass
class xmof_BasicBehaviors_ParameterValue:

    pass
class xmof_LociL1_SemanticVisitor(ABC):

    pass
class Kernel_xmof_EObject:

    pass
class SemanticVisitor:

    pass
class xmof_Kernel_Value(SemanticVisitor):

    pass
class Kernel_xmof_EEnum:

    pass
class PrimitiveValue:

    pass
class xmof_Kernel_BooleanValue(PrimitiveValue):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class xmof_Kernel_IntegerValue(PrimitiveValue):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class xmof_Kernel_StringValue(PrimitiveValue):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Kernel_PrimitiveType:

    pass
class Value:

    pass
class xmof_Kernel_ObjectValue(Value):

    pass
class xmof_Kernel_PrimitiveValue(Value):

    pass
class xmof_Kernel_EnumerationValue(Value):

    pass
class Pin:

    pass
class xmof_BasicActions_OutputPin(Pin):

    pass
class xmof_BasicActions_InputPin(Pin):

    pass
class BasicActions_xmof_EClassifier:

    pass
class ExecutableNode:

    pass
class xmof_BasicActions_Action(ExecutableNode):

    def __init__(self, locallyReentrant: bool, xmof_BasicActions_Action: set["BasicActions_OutputPin"] = None, xmof_BasicActions_Action225: "BasicActions_xmof_EClassifier" = None, xmof_BasicActions_Action227: set["BasicActions_InputPin"] = None):
        self.locallyReentrant = locallyReentrant
        self.xmof_BasicActions_Action = xmof_BasicActions_Action if xmof_BasicActions_Action is not None else set()
        self.xmof_BasicActions_Action225 = xmof_BasicActions_Action225
        self.xmof_BasicActions_Action227 = xmof_BasicActions_Action227 if xmof_BasicActions_Action227 is not None else set()
        
    @property
    def locallyReentrant(self) -> bool:
        return self.__locallyReentrant

    @locallyReentrant.setter
    def locallyReentrant(self, locallyReentrant: bool):
        self.__locallyReentrant = locallyReentrant

    @property
    def xmof_BasicActions_Action(self):
        return self.__xmof_BasicActions_Action

    @xmof_BasicActions_Action.setter
    def xmof_BasicActions_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_BasicActions_Action__xmof_BasicActions_Action", None)
        self.__xmof_BasicActions_Action = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin223"):
                    opp_val = getattr(item, "BasicActions_OutputPin223", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin223", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin223"):
                    opp_val = getattr(item, "BasicActions_OutputPin223", None)
                    
                    setattr(item, "BasicActions_OutputPin223", self)
                    

    @property
    def xmof_BasicActions_Action225(self):
        return self.__xmof_BasicActions_Action225

    @xmof_BasicActions_Action225.setter
    def xmof_BasicActions_Action225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_BasicActions_Action__xmof_BasicActions_Action225", None)
        self.__xmof_BasicActions_Action225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_xmof_EClassifier"):
                opp_val = getattr(old_value, "BasicActions_xmof_EClassifier", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_xmof_EClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_xmof_EClassifier"):
                opp_val = getattr(value, "BasicActions_xmof_EClassifier", None)
                setattr(value, "BasicActions_xmof_EClassifier", self)

    @property
    def xmof_BasicActions_Action227(self):
        return self.__xmof_BasicActions_Action227

    @xmof_BasicActions_Action227.setter
    def xmof_BasicActions_Action227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_BasicActions_Action__xmof_BasicActions_Action227", None)
        self.__xmof_BasicActions_Action227 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_InputPin228"):
                    opp_val = getattr(item, "BasicActions_InputPin228", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_InputPin228", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_InputPin228"):
                    opp_val = getattr(item, "BasicActions_InputPin228", None)
                    
                    setattr(item, "BasicActions_InputPin228", self)
                    

class Communications_Trigger:

    pass
class InvocationAction:

    pass
class xmof_BasicActions_SendSignalAction(InvocationAction):

    pass
class xmof_BasicActions_CallAction(InvocationAction):

    def __init__(self, synchronous: bool, xmof_BasicActions_CallAction: set["BasicActions_OutputPin"] = None):
        self.synchronous = synchronous
        self.xmof_BasicActions_CallAction = xmof_BasicActions_CallAction if xmof_BasicActions_CallAction is not None else set()
        
    @property
    def synchronous(self) -> bool:
        return self.__synchronous

    @synchronous.setter
    def synchronous(self, synchronous: bool):
        self.__synchronous = synchronous

    @property
    def xmof_BasicActions_CallAction(self):
        return self.__xmof_BasicActions_CallAction

    @xmof_BasicActions_CallAction.setter
    def xmof_BasicActions_CallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_BasicActions_CallAction__xmof_BasicActions_CallAction", None)
        self.__xmof_BasicActions_CallAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin230"):
                    opp_val = getattr(item, "BasicActions_OutputPin230", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin230", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin230"):
                    opp_val = getattr(item, "BasicActions_OutputPin230", None)
                    
                    setattr(item, "BasicActions_OutputPin230", self)
                    

class IntermediateActivities_ObjectNode:

    pass
class CompleteActions_xmof_EClassifier:

    pass
class CallAction:

    pass
class xmof_BasicActions_CallBehaviorAction(CallAction):

    pass
class xmof_BasicActions_CallOperationAction(CallAction):

    pass
class xmof_CompleteActions_StartObjectBehaviorAction(CallAction):

    pass
class WriteLinkAction:

    pass
class xmof_IntermediateActions_CreateLinkAction(WriteLinkAction):

    pass
class xmof_IntermediateActions_DestroyLinkAction(WriteLinkAction):

    pass
class IntermediateActions_xmof_EClassifier:

    pass
class LinkEndData:

    pass
class xmof_IntermediateActions_LinkEndDestructionData(LinkEndData):

    def __init__(self, destroyDuplicates: bool, xmof_IntermediateActions_LinkEndDestructionData: "BasicActions_InputPin" = None):
        self.destroyDuplicates = destroyDuplicates
        self.xmof_IntermediateActions_LinkEndDestructionData = xmof_IntermediateActions_LinkEndDestructionData
        
    @property
    def destroyDuplicates(self) -> bool:
        return self.__destroyDuplicates

    @destroyDuplicates.setter
    def destroyDuplicates(self, destroyDuplicates: bool):
        self.__destroyDuplicates = destroyDuplicates

    @property
    def xmof_IntermediateActions_LinkEndDestructionData(self):
        return self.__xmof_IntermediateActions_LinkEndDestructionData

    @xmof_IntermediateActions_LinkEndDestructionData.setter
    def xmof_IntermediateActions_LinkEndDestructionData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_IntermediateActions_LinkEndDestructionData__xmof_IntermediateActions_LinkEndDestructionData", None)
        self.__xmof_IntermediateActions_LinkEndDestructionData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin170"):
                opp_val = getattr(old_value, "BasicActions_InputPin170", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin170"):
                opp_val = getattr(value, "BasicActions_InputPin170", None)
                setattr(value, "BasicActions_InputPin170", self)

class xmof_IntermediateActions_LinkEndCreationData(LinkEndData):

    def __init__(self, replaceAll: bool, xmof_IntermediateActions_LinkEndCreationData: "BasicActions_InputPin" = None):
        self.replaceAll = replaceAll
        self.xmof_IntermediateActions_LinkEndCreationData = xmof_IntermediateActions_LinkEndCreationData
        
    @property
    def replaceAll(self) -> bool:
        return self.__replaceAll

    @replaceAll.setter
    def replaceAll(self, replaceAll: bool):
        self.__replaceAll = replaceAll

    @property
    def xmof_IntermediateActions_LinkEndCreationData(self):
        return self.__xmof_IntermediateActions_LinkEndCreationData

    @xmof_IntermediateActions_LinkEndCreationData.setter
    def xmof_IntermediateActions_LinkEndCreationData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_IntermediateActions_LinkEndCreationData__xmof_IntermediateActions_LinkEndCreationData", None)
        self.__xmof_IntermediateActions_LinkEndCreationData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin168"):
                opp_val = getattr(old_value, "BasicActions_InputPin168", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin168"):
                opp_val = getattr(value, "BasicActions_InputPin168", None)
                setattr(value, "BasicActions_InputPin168", self)

class StructuralFeatureAction:

    pass
class xmof_IntermediateActions_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class xmof_IntermediateActions_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class xmof_IntermediateActions_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class IntermediateActions_xmof_EReference:

    pass
class WriteStructuralFeatureAction:

    pass
class xmof_IntermediateActions_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    def __init__(self, replaceAll: bool, xmof_IntermediateActions_AddStructuralFeatureValueAction: "BasicActions_InputPin" = None):
        self.replaceAll = replaceAll
        self.xmof_IntermediateActions_AddStructuralFeatureValueAction = xmof_IntermediateActions_AddStructuralFeatureValueAction
        
    @property
    def replaceAll(self) -> bool:
        return self.__replaceAll

    @replaceAll.setter
    def replaceAll(self, replaceAll: bool):
        self.__replaceAll = replaceAll

    @property
    def xmof_IntermediateActions_AddStructuralFeatureValueAction(self):
        return self.__xmof_IntermediateActions_AddStructuralFeatureValueAction

    @xmof_IntermediateActions_AddStructuralFeatureValueAction.setter
    def xmof_IntermediateActions_AddStructuralFeatureValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_IntermediateActions_AddStructuralFeatureValueAction__xmof_IntermediateActions_AddStructuralFeatureValueAction", None)
        self.__xmof_IntermediateActions_AddStructuralFeatureValueAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin185"):
                opp_val = getattr(old_value, "BasicActions_InputPin185", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin185"):
                opp_val = getattr(value, "BasicActions_InputPin185", None)
                setattr(value, "BasicActions_InputPin185", self)

class xmof_IntermediateActions_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    def __init__(self, removeDuplicates: bool, xmof_IntermediateActions_RemoveStructuralFeatureValueAction: "BasicActions_InputPin" = None):
        self.removeDuplicates = removeDuplicates
        self.xmof_IntermediateActions_RemoveStructuralFeatureValueAction = xmof_IntermediateActions_RemoveStructuralFeatureValueAction
        
    @property
    def removeDuplicates(self) -> bool:
        return self.__removeDuplicates

    @removeDuplicates.setter
    def removeDuplicates(self, removeDuplicates: bool):
        self.__removeDuplicates = removeDuplicates

    @property
    def xmof_IntermediateActions_RemoveStructuralFeatureValueAction(self):
        return self.__xmof_IntermediateActions_RemoveStructuralFeatureValueAction

    @xmof_IntermediateActions_RemoveStructuralFeatureValueAction.setter
    def xmof_IntermediateActions_RemoveStructuralFeatureValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_IntermediateActions_RemoveStructuralFeatureValueAction__xmof_IntermediateActions_RemoveStructuralFeatureValueAction", None)
        self.__xmof_IntermediateActions_RemoveStructuralFeatureValueAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin160"):
                opp_val = getattr(old_value, "BasicActions_InputPin160", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin160"):
                opp_val = getattr(value, "BasicActions_InputPin160", None)
                setattr(value, "BasicActions_InputPin160", self)

class IntermediateActions_xmof_EStructuralFeature:

    pass
class IntermediateActions_LinkEndData:

    pass
class LinkAction:

    pass
class xmof_IntermediateActions_ReadLinkAction(LinkAction):

    pass
class xmof_IntermediateActions_WriteLinkAction(LinkAction):

    pass
class ExtraStructuredActivities_ExpansionNode:

    pass
class ExtraStructuredActivities_ExpansionRegion:

    pass
class Action:

    pass
class xmof_BasicActions_InvocationAction(Action):

    pass
class xmof_CompleteActions_ReadExtentAction(Action):

    pass
class xmof_IntermediateActions_TestIdentityAction(Action):

    pass
class xmof_CompleteActions_AcceptEventAction(Action):

    def __init__(self, unmarshall: bool, xmof_CompleteActions_AcceptEventAction: set["BasicActions_OutputPin"] = None, xmof_CompleteActions_AcceptEventAction221: set["Communications_Trigger"] = None):
        self.unmarshall = unmarshall
        self.xmof_CompleteActions_AcceptEventAction = xmof_CompleteActions_AcceptEventAction if xmof_CompleteActions_AcceptEventAction is not None else set()
        self.xmof_CompleteActions_AcceptEventAction221 = xmof_CompleteActions_AcceptEventAction221 if xmof_CompleteActions_AcceptEventAction221 is not None else set()
        
    @property
    def unmarshall(self) -> bool:
        return self.__unmarshall

    @unmarshall.setter
    def unmarshall(self, unmarshall: bool):
        self.__unmarshall = unmarshall

    @property
    def xmof_CompleteActions_AcceptEventAction(self):
        return self.__xmof_CompleteActions_AcceptEventAction

    @xmof_CompleteActions_AcceptEventAction.setter
    def xmof_CompleteActions_AcceptEventAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_AcceptEventAction__xmof_CompleteActions_AcceptEventAction", None)
        self.__xmof_CompleteActions_AcceptEventAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin219"):
                    opp_val = getattr(item, "BasicActions_OutputPin219", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin219", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin219"):
                    opp_val = getattr(item, "BasicActions_OutputPin219", None)
                    
                    setattr(item, "BasicActions_OutputPin219", self)
                    

    @property
    def xmof_CompleteActions_AcceptEventAction221(self):
        return self.__xmof_CompleteActions_AcceptEventAction221

    @xmof_CompleteActions_AcceptEventAction221.setter
    def xmof_CompleteActions_AcceptEventAction221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_AcceptEventAction__xmof_CompleteActions_AcceptEventAction221", None)
        self.__xmof_CompleteActions_AcceptEventAction221 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Communications_Trigger"):
                    opp_val = getattr(item, "Communications_Trigger", None)
                    
                    if opp_val == self:
                        setattr(item, "Communications_Trigger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Communications_Trigger"):
                    opp_val = getattr(item, "Communications_Trigger", None)
                    
                    setattr(item, "Communications_Trigger", self)
                    

class xmof_CompleteActions_ReduceAction(Action):

    def __init__(self, ordered: bool, xmof_CompleteActions_ReduceAction: "BasicBehaviors_Behavior" = None, xmof_CompleteActions_ReduceAction196: "BasicActions_InputPin" = None, xmof_CompleteActions_ReduceAction193: "BasicActions_OutputPin" = None):
        self.ordered = ordered
        self.xmof_CompleteActions_ReduceAction = xmof_CompleteActions_ReduceAction
        self.xmof_CompleteActions_ReduceAction196 = xmof_CompleteActions_ReduceAction196
        self.xmof_CompleteActions_ReduceAction193 = xmof_CompleteActions_ReduceAction193
        
    @property
    def ordered(self) -> bool:
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered

    @property
    def xmof_CompleteActions_ReduceAction(self):
        return self.__xmof_CompleteActions_ReduceAction

    @xmof_CompleteActions_ReduceAction.setter
    def xmof_CompleteActions_ReduceAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReduceAction__xmof_CompleteActions_ReduceAction", None)
        self.__xmof_CompleteActions_ReduceAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicBehaviors_Behavior191"):
                opp_val = getattr(old_value, "BasicBehaviors_Behavior191", None)
                if opp_val == self:
                    setattr(old_value, "BasicBehaviors_Behavior191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicBehaviors_Behavior191"):
                opp_val = getattr(value, "BasicBehaviors_Behavior191", None)
                setattr(value, "BasicBehaviors_Behavior191", self)

    @property
    def xmof_CompleteActions_ReduceAction193(self):
        return self.__xmof_CompleteActions_ReduceAction193

    @xmof_CompleteActions_ReduceAction193.setter
    def xmof_CompleteActions_ReduceAction193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReduceAction__xmof_CompleteActions_ReduceAction193", None)
        self.__xmof_CompleteActions_ReduceAction193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_OutputPin194"):
                opp_val = getattr(old_value, "BasicActions_OutputPin194", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_OutputPin194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_OutputPin194"):
                opp_val = getattr(value, "BasicActions_OutputPin194", None)
                setattr(value, "BasicActions_OutputPin194", self)

    @property
    def xmof_CompleteActions_ReduceAction196(self):
        return self.__xmof_CompleteActions_ReduceAction196

    @xmof_CompleteActions_ReduceAction196.setter
    def xmof_CompleteActions_ReduceAction196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReduceAction__xmof_CompleteActions_ReduceAction196", None)
        self.__xmof_CompleteActions_ReduceAction196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin197"):
                opp_val = getattr(old_value, "BasicActions_InputPin197", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin197"):
                opp_val = getattr(value, "BasicActions_InputPin197", None)
                setattr(value, "BasicActions_InputPin197", self)

class xmof_IntermediateActions_ClearAssociationAction(Action):

    pass
class xmof_CompleteActions_ReclassifyObjectAction(Action):

    def __init__(self, replaceAll: bool, xmof_CompleteActions_ReclassifyObjectAction: set["CompleteActions_xmof_EClassifier"] = None, xmof_CompleteActions_ReclassifyObjectAction216: set["CompleteActions_xmof_EClassifier"] = None, xmof_CompleteActions_ReclassifyObjectAction213: "BasicActions_InputPin" = None):
        self.replaceAll = replaceAll
        self.xmof_CompleteActions_ReclassifyObjectAction = xmof_CompleteActions_ReclassifyObjectAction if xmof_CompleteActions_ReclassifyObjectAction is not None else set()
        self.xmof_CompleteActions_ReclassifyObjectAction216 = xmof_CompleteActions_ReclassifyObjectAction216 if xmof_CompleteActions_ReclassifyObjectAction216 is not None else set()
        self.xmof_CompleteActions_ReclassifyObjectAction213 = xmof_CompleteActions_ReclassifyObjectAction213
        
    @property
    def replaceAll(self) -> bool:
        return self.__replaceAll

    @replaceAll.setter
    def replaceAll(self, replaceAll: bool):
        self.__replaceAll = replaceAll

    @property
    def xmof_CompleteActions_ReclassifyObjectAction216(self):
        return self.__xmof_CompleteActions_ReclassifyObjectAction216

    @xmof_CompleteActions_ReclassifyObjectAction216.setter
    def xmof_CompleteActions_ReclassifyObjectAction216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReclassifyObjectAction__xmof_CompleteActions_ReclassifyObjectAction216", None)
        self.__xmof_CompleteActions_ReclassifyObjectAction216 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteActions_xmof_EClassifier217"):
                    opp_val = getattr(item, "CompleteActions_xmof_EClassifier217", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteActions_xmof_EClassifier217", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteActions_xmof_EClassifier217"):
                    opp_val = getattr(item, "CompleteActions_xmof_EClassifier217", None)
                    
                    setattr(item, "CompleteActions_xmof_EClassifier217", self)
                    

    @property
    def xmof_CompleteActions_ReclassifyObjectAction(self):
        return self.__xmof_CompleteActions_ReclassifyObjectAction

    @xmof_CompleteActions_ReclassifyObjectAction.setter
    def xmof_CompleteActions_ReclassifyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReclassifyObjectAction__xmof_CompleteActions_ReclassifyObjectAction", None)
        self.__xmof_CompleteActions_ReclassifyObjectAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteActions_xmof_EClassifier211"):
                    opp_val = getattr(item, "CompleteActions_xmof_EClassifier211", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteActions_xmof_EClassifier211", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteActions_xmof_EClassifier211"):
                    opp_val = getattr(item, "CompleteActions_xmof_EClassifier211", None)
                    
                    setattr(item, "CompleteActions_xmof_EClassifier211", self)
                    

    @property
    def xmof_CompleteActions_ReclassifyObjectAction213(self):
        return self.__xmof_CompleteActions_ReclassifyObjectAction213

    @xmof_CompleteActions_ReclassifyObjectAction213.setter
    def xmof_CompleteActions_ReclassifyObjectAction213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReclassifyObjectAction__xmof_CompleteActions_ReclassifyObjectAction213", None)
        self.__xmof_CompleteActions_ReclassifyObjectAction213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin214"):
                opp_val = getattr(old_value, "BasicActions_InputPin214", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin214"):
                opp_val = getattr(value, "BasicActions_InputPin214", None)
                setattr(value, "BasicActions_InputPin214", self)

class xmof_IntermediateActions_LinkAction(Action):

    pass
class xmof_IntermediateActions_ValueSpecificationAction(Action):

    pass
class xmof_CompleteActions_StartClassifierBehaviorAction(Action):

    pass
class xmof_CompleteActions_ReadIsClassifiedObjectAction(Action):

    def __init__(self, direct: bool, xmof_CompleteActions_ReadIsClassifiedObjectAction: "CompleteActions_xmof_EClassifier" = None, xmof_CompleteActions_ReadIsClassifiedObjectAction205: "BasicActions_OutputPin" = None, xmof_CompleteActions_ReadIsClassifiedObjectAction208: "BasicActions_InputPin" = None):
        self.direct = direct
        self.xmof_CompleteActions_ReadIsClassifiedObjectAction = xmof_CompleteActions_ReadIsClassifiedObjectAction
        self.xmof_CompleteActions_ReadIsClassifiedObjectAction205 = xmof_CompleteActions_ReadIsClassifiedObjectAction205
        self.xmof_CompleteActions_ReadIsClassifiedObjectAction208 = xmof_CompleteActions_ReadIsClassifiedObjectAction208
        
    @property
    def direct(self) -> bool:
        return self.__direct

    @direct.setter
    def direct(self, direct: bool):
        self.__direct = direct

    @property
    def xmof_CompleteActions_ReadIsClassifiedObjectAction205(self):
        return self.__xmof_CompleteActions_ReadIsClassifiedObjectAction205

    @xmof_CompleteActions_ReadIsClassifiedObjectAction205.setter
    def xmof_CompleteActions_ReadIsClassifiedObjectAction205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReadIsClassifiedObjectAction__xmof_CompleteActions_ReadIsClassifiedObjectAction205", None)
        self.__xmof_CompleteActions_ReadIsClassifiedObjectAction205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_OutputPin206"):
                opp_val = getattr(old_value, "BasicActions_OutputPin206", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_OutputPin206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_OutputPin206"):
                opp_val = getattr(value, "BasicActions_OutputPin206", None)
                setattr(value, "BasicActions_OutputPin206", self)

    @property
    def xmof_CompleteActions_ReadIsClassifiedObjectAction208(self):
        return self.__xmof_CompleteActions_ReadIsClassifiedObjectAction208

    @xmof_CompleteActions_ReadIsClassifiedObjectAction208.setter
    def xmof_CompleteActions_ReadIsClassifiedObjectAction208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReadIsClassifiedObjectAction__xmof_CompleteActions_ReadIsClassifiedObjectAction208", None)
        self.__xmof_CompleteActions_ReadIsClassifiedObjectAction208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin209"):
                opp_val = getattr(old_value, "BasicActions_InputPin209", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin209"):
                opp_val = getattr(value, "BasicActions_InputPin209", None)
                setattr(value, "BasicActions_InputPin209", self)

    @property
    def xmof_CompleteActions_ReadIsClassifiedObjectAction(self):
        return self.__xmof_CompleteActions_ReadIsClassifiedObjectAction

    @xmof_CompleteActions_ReadIsClassifiedObjectAction.setter
    def xmof_CompleteActions_ReadIsClassifiedObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReadIsClassifiedObjectAction__xmof_CompleteActions_ReadIsClassifiedObjectAction", None)
        self.__xmof_CompleteActions_ReadIsClassifiedObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteActions_xmof_EClassifier203"):
                opp_val = getattr(old_value, "CompleteActions_xmof_EClassifier203", None)
                if opp_val == self:
                    setattr(old_value, "CompleteActions_xmof_EClassifier203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteActions_xmof_EClassifier203"):
                opp_val = getattr(value, "CompleteActions_xmof_EClassifier203", None)
                setattr(value, "CompleteActions_xmof_EClassifier203", self)

class xmof_IntermediateActions_CreateObjectAction(Action):

    pass
class xmof_IntermediateActions_DestroyObjectAction(Action):

    def __init__(self, destroyLinks: bool, destroyOwnedObjects: bool, xmof_IntermediateActions_DestroyObjectAction: "BasicActions_InputPin" = None):
        self.destroyLinks = destroyLinks
        self.destroyOwnedObjects = destroyOwnedObjects
        self.xmof_IntermediateActions_DestroyObjectAction = xmof_IntermediateActions_DestroyObjectAction
        
    @property
    def destroyLinks(self) -> bool:
        return self.__destroyLinks

    @destroyLinks.setter
    def destroyLinks(self, destroyLinks: bool):
        self.__destroyLinks = destroyLinks

    @property
    def destroyOwnedObjects(self) -> bool:
        return self.__destroyOwnedObjects

    @destroyOwnedObjects.setter
    def destroyOwnedObjects(self, destroyOwnedObjects: bool):
        self.__destroyOwnedObjects = destroyOwnedObjects

    @property
    def xmof_IntermediateActions_DestroyObjectAction(self):
        return self.__xmof_IntermediateActions_DestroyObjectAction

    @xmof_IntermediateActions_DestroyObjectAction.setter
    def xmof_IntermediateActions_DestroyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_IntermediateActions_DestroyObjectAction__xmof_IntermediateActions_DestroyObjectAction", None)
        self.__xmof_IntermediateActions_DestroyObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin183"):
                opp_val = getattr(old_value, "BasicActions_InputPin183", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin183"):
                opp_val = getattr(value, "BasicActions_InputPin183", None)
                setattr(value, "BasicActions_InputPin183", self)

class xmof_IntermediateActions_StructuralFeatureAction(Action):

    pass
class xmof_IntermediateActions_ReadSelfAction(Action):

    pass
class xmof_CompleteStructuredActivities_StructuredActivityNode(Action):

    def __init__(self, mustIsolate: bool, Activities107: set["IntermediateActivities_ActivityNode"] = None, Activities110: set["IntermediateActivities_ActivityEdge"] = None, xmof_CompleteStructuredActivities_StructuredActivityNode: set["BasicActions_OutputPin"] = None, xmof_CompleteStructuredActivities_StructuredActivityNode115: set["BasicActions_InputPin"] = None):
        self.mustIsolate = mustIsolate
        self.Activities107 = Activities107 if Activities107 is not None else set()
        self.Activities110 = Activities110 if Activities110 is not None else set()
        self.xmof_CompleteStructuredActivities_StructuredActivityNode = xmof_CompleteStructuredActivities_StructuredActivityNode if xmof_CompleteStructuredActivities_StructuredActivityNode is not None else set()
        self.xmof_CompleteStructuredActivities_StructuredActivityNode115 = xmof_CompleteStructuredActivities_StructuredActivityNode115 if xmof_CompleteStructuredActivities_StructuredActivityNode115 is not None else set()
        
    @property
    def mustIsolate(self) -> bool:
        return self.__mustIsolate

    @mustIsolate.setter
    def mustIsolate(self, mustIsolate: bool):
        self.__mustIsolate = mustIsolate

    @property
    def xmof_CompleteStructuredActivities_StructuredActivityNode(self):
        return self.__xmof_CompleteStructuredActivities_StructuredActivityNode

    @xmof_CompleteStructuredActivities_StructuredActivityNode.setter
    def xmof_CompleteStructuredActivities_StructuredActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_StructuredActivityNode__xmof_CompleteStructuredActivities_StructuredActivityNode", None)
        self.__xmof_CompleteStructuredActivities_StructuredActivityNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin113"):
                    opp_val = getattr(item, "BasicActions_OutputPin113", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin113"):
                    opp_val = getattr(item, "BasicActions_OutputPin113", None)
                    
                    setattr(item, "BasicActions_OutputPin113", self)
                    

    @property
    def Activities110(self):
        return self.__Activities110

    @Activities110.setter
    def Activities110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_StructuredActivityNode__Activities110", None)
        self.__Activities110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax111"):
                    opp_val = getattr(item, "Syntax111", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax111"):
                    opp_val = getattr(item, "Syntax111", None)
                    
                    setattr(item, "Syntax111", self)
                    

    @property
    def xmof_CompleteStructuredActivities_StructuredActivityNode115(self):
        return self.__xmof_CompleteStructuredActivities_StructuredActivityNode115

    @xmof_CompleteStructuredActivities_StructuredActivityNode115.setter
    def xmof_CompleteStructuredActivities_StructuredActivityNode115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_StructuredActivityNode__xmof_CompleteStructuredActivities_StructuredActivityNode115", None)
        self.__xmof_CompleteStructuredActivities_StructuredActivityNode115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_InputPin116"):
                    opp_val = getattr(item, "BasicActions_InputPin116", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_InputPin116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_InputPin116"):
                    opp_val = getattr(item, "BasicActions_InputPin116", None)
                    
                    setattr(item, "BasicActions_InputPin116", self)
                    

    @property
    def Activities107(self):
        return self.__Activities107

    @Activities107.setter
    def Activities107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_StructuredActivityNode__Activities107", None)
        self.__Activities107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax108"):
                    opp_val = getattr(item, "Syntax108", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax108"):
                    opp_val = getattr(item, "Syntax108", None)
                    
                    setattr(item, "Syntax108", self)
                    

class CompleteStructuredActivities_Clause:

    pass
class BasicActions_InputPin:

    pass
class CompleteStructuredActivities_ExecutableNode:

    pass
class BasicActions_OutputPin:

    pass
class StructuredActivityNode:

    pass
class xmof_ExtraStructuredActivities_ExpansionRegion(StructuredActivityNode):

    def __init__(self, mode: str, Activities127: set["ExtraStructuredActivities_ExpansionNode"] = None, Activities124: set["ExtraStructuredActivities_ExpansionNode"] = None):
        self.mode = mode
        self.Activities127 = Activities127 if Activities127 is not None else set()
        self.Activities124 = Activities124 if Activities124 is not None else set()
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def Activities127(self):
        return self.__Activities127

    @Activities127.setter
    def Activities127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_ExtraStructuredActivities_ExpansionRegion__Activities127", None)
        self.__Activities127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax128"):
                    opp_val = getattr(item, "Syntax128", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax128", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax128"):
                    opp_val = getattr(item, "Syntax128", None)
                    
                    setattr(item, "Syntax128", self)
                    

    @property
    def Activities124(self):
        return self.__Activities124

    @Activities124.setter
    def Activities124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_ExtraStructuredActivities_ExpansionRegion__Activities124", None)
        self.__Activities124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax125"):
                    opp_val = getattr(item, "Syntax125", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax125"):
                    opp_val = getattr(item, "Syntax125", None)
                    
                    setattr(item, "Syntax125", self)
                    

class xmof_CompleteStructuredActivities_ConditionalNode(StructuredActivityNode):

    def __init__(self, assured: bool, determinate: bool, xmof_CompleteStructuredActivities_ConditionalNode: set["CompleteStructuredActivities_Clause"] = None, xmof_CompleteStructuredActivities_ConditionalNode104: set["BasicActions_OutputPin"] = None):
        self.assured = assured
        self.determinate = determinate
        self.xmof_CompleteStructuredActivities_ConditionalNode = xmof_CompleteStructuredActivities_ConditionalNode if xmof_CompleteStructuredActivities_ConditionalNode is not None else set()
        self.xmof_CompleteStructuredActivities_ConditionalNode104 = xmof_CompleteStructuredActivities_ConditionalNode104 if xmof_CompleteStructuredActivities_ConditionalNode104 is not None else set()
        
    @property
    def assured(self) -> bool:
        return self.__assured

    @assured.setter
    def assured(self, assured: bool):
        self.__assured = assured

    @property
    def determinate(self) -> bool:
        return self.__determinate

    @determinate.setter
    def determinate(self, determinate: bool):
        self.__determinate = determinate

    @property
    def xmof_CompleteStructuredActivities_ConditionalNode(self):
        return self.__xmof_CompleteStructuredActivities_ConditionalNode

    @xmof_CompleteStructuredActivities_ConditionalNode.setter
    def xmof_CompleteStructuredActivities_ConditionalNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_ConditionalNode__xmof_CompleteStructuredActivities_ConditionalNode", None)
        self.__xmof_CompleteStructuredActivities_ConditionalNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteStructuredActivities_Clause"):
                    opp_val = getattr(item, "CompleteStructuredActivities_Clause", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteStructuredActivities_Clause", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteStructuredActivities_Clause"):
                    opp_val = getattr(item, "CompleteStructuredActivities_Clause", None)
                    
                    setattr(item, "CompleteStructuredActivities_Clause", self)
                    

    @property
    def xmof_CompleteStructuredActivities_ConditionalNode104(self):
        return self.__xmof_CompleteStructuredActivities_ConditionalNode104

    @xmof_CompleteStructuredActivities_ConditionalNode104.setter
    def xmof_CompleteStructuredActivities_ConditionalNode104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_ConditionalNode__xmof_CompleteStructuredActivities_ConditionalNode104", None)
        self.__xmof_CompleteStructuredActivities_ConditionalNode104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin105"):
                    opp_val = getattr(item, "BasicActions_OutputPin105", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin105"):
                    opp_val = getattr(item, "BasicActions_OutputPin105", None)
                    
                    setattr(item, "BasicActions_OutputPin105", self)
                    

class xmof_CompleteStructuredActivities_LoopNode(StructuredActivityNode):

    def __init__(self, testedFirst: bool, xmof_CompleteStructuredActivities_LoopNode69: set["BasicActions_OutputPin"] = None, xmof_CompleteStructuredActivities_LoopNode: "BasicActions_OutputPin" = None, xmof_CompleteStructuredActivities_LoopNode67: set["CompleteStructuredActivities_ExecutableNode"] = None, xmof_CompleteStructuredActivities_LoopNode72: set["BasicActions_InputPin"] = None, xmof_CompleteStructuredActivities_LoopNode74: set["CompleteStructuredActivities_ExecutableNode"] = None, xmof_CompleteStructuredActivities_LoopNode77: set["BasicActions_OutputPin"] = None, xmof_CompleteStructuredActivities_LoopNode80: set["BasicActions_OutputPin"] = None, xmof_CompleteStructuredActivities_LoopNode83: set["CompleteStructuredActivities_ExecutableNode"] = None):
        self.testedFirst = testedFirst
        self.xmof_CompleteStructuredActivities_LoopNode69 = xmof_CompleteStructuredActivities_LoopNode69 if xmof_CompleteStructuredActivities_LoopNode69 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode = xmof_CompleteStructuredActivities_LoopNode
        self.xmof_CompleteStructuredActivities_LoopNode67 = xmof_CompleteStructuredActivities_LoopNode67 if xmof_CompleteStructuredActivities_LoopNode67 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode72 = xmof_CompleteStructuredActivities_LoopNode72 if xmof_CompleteStructuredActivities_LoopNode72 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode74 = xmof_CompleteStructuredActivities_LoopNode74 if xmof_CompleteStructuredActivities_LoopNode74 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode77 = xmof_CompleteStructuredActivities_LoopNode77 if xmof_CompleteStructuredActivities_LoopNode77 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode80 = xmof_CompleteStructuredActivities_LoopNode80 if xmof_CompleteStructuredActivities_LoopNode80 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode83 = xmof_CompleteStructuredActivities_LoopNode83 if xmof_CompleteStructuredActivities_LoopNode83 is not None else set()
        
    @property
    def testedFirst(self) -> bool:
        return self.__testedFirst

    @testedFirst.setter
    def testedFirst(self, testedFirst: bool):
        self.__testedFirst = testedFirst

    @property
    def xmof_CompleteStructuredActivities_LoopNode67(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode67

    @xmof_CompleteStructuredActivities_LoopNode67.setter
    def xmof_CompleteStructuredActivities_LoopNode67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode67", None)
        self.__xmof_CompleteStructuredActivities_LoopNode67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteStructuredActivities_ExecutableNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode", None)
                    
                    setattr(item, "CompleteStructuredActivities_ExecutableNode", self)
                    

    @property
    def xmof_CompleteStructuredActivities_LoopNode69(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode69

    @xmof_CompleteStructuredActivities_LoopNode69.setter
    def xmof_CompleteStructuredActivities_LoopNode69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode69", None)
        self.__xmof_CompleteStructuredActivities_LoopNode69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin70"):
                    opp_val = getattr(item, "BasicActions_OutputPin70", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin70"):
                    opp_val = getattr(item, "BasicActions_OutputPin70", None)
                    
                    setattr(item, "BasicActions_OutputPin70", self)
                    

    @property
    def xmof_CompleteStructuredActivities_LoopNode(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode

    @xmof_CompleteStructuredActivities_LoopNode.setter
    def xmof_CompleteStructuredActivities_LoopNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode", None)
        self.__xmof_CompleteStructuredActivities_LoopNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_OutputPin"):
                opp_val = getattr(old_value, "BasicActions_OutputPin", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_OutputPin", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_OutputPin"):
                opp_val = getattr(value, "BasicActions_OutputPin", None)
                setattr(value, "BasicActions_OutputPin", self)

    @property
    def xmof_CompleteStructuredActivities_LoopNode72(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode72

    @xmof_CompleteStructuredActivities_LoopNode72.setter
    def xmof_CompleteStructuredActivities_LoopNode72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode72", None)
        self.__xmof_CompleteStructuredActivities_LoopNode72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_InputPin"):
                    opp_val = getattr(item, "BasicActions_InputPin", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_InputPin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_InputPin"):
                    opp_val = getattr(item, "BasicActions_InputPin", None)
                    
                    setattr(item, "BasicActions_InputPin", self)
                    

    @property
    def xmof_CompleteStructuredActivities_LoopNode77(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode77

    @xmof_CompleteStructuredActivities_LoopNode77.setter
    def xmof_CompleteStructuredActivities_LoopNode77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode77", None)
        self.__xmof_CompleteStructuredActivities_LoopNode77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin78"):
                    opp_val = getattr(item, "BasicActions_OutputPin78", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin78"):
                    opp_val = getattr(item, "BasicActions_OutputPin78", None)
                    
                    setattr(item, "BasicActions_OutputPin78", self)
                    

    @property
    def xmof_CompleteStructuredActivities_LoopNode80(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode80

    @xmof_CompleteStructuredActivities_LoopNode80.setter
    def xmof_CompleteStructuredActivities_LoopNode80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode80", None)
        self.__xmof_CompleteStructuredActivities_LoopNode80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin81"):
                    opp_val = getattr(item, "BasicActions_OutputPin81", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin81"):
                    opp_val = getattr(item, "BasicActions_OutputPin81", None)
                    
                    setattr(item, "BasicActions_OutputPin81", self)
                    

    @property
    def xmof_CompleteStructuredActivities_LoopNode74(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode74

    @xmof_CompleteStructuredActivities_LoopNode74.setter
    def xmof_CompleteStructuredActivities_LoopNode74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode74", None)
        self.__xmof_CompleteStructuredActivities_LoopNode74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode75"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode75", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteStructuredActivities_ExecutableNode75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode75"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode75", None)
                    
                    setattr(item, "CompleteStructuredActivities_ExecutableNode75", self)
                    

    @property
    def xmof_CompleteStructuredActivities_LoopNode83(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode83

    @xmof_CompleteStructuredActivities_LoopNode83.setter
    def xmof_CompleteStructuredActivities_LoopNode83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode83", None)
        self.__xmof_CompleteStructuredActivities_LoopNode83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode84"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode84", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteStructuredActivities_ExecutableNode84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode84"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode84", None)
                    
                    setattr(item, "CompleteStructuredActivities_ExecutableNode84", self)
                    

class ObjectNode:

    pass
class xmof_ExtraStructuredActivities_ExpansionNode(ObjectNode):

    pass
class xmof_IntermediateActivities_ActivityParameterNode(ObjectNode):

    pass
class FinalNode:

    pass
class xmof_IntermediateActivities_ActivityFinalNode(FinalNode):

    pass
class IntermediateActivities_ObjectFlow:

    pass
class ActivityNode:

    pass
class xmof_CompleteStructuredActivities_ExecutableNode(ActivityNode):

    pass
class xmof_IntermediateActivities_ControlNode(ActivityNode):

    pass
class CompleteStructuredActivities_StructuredActivityNode:

    pass
class IntermediateActivities_ActivityEdge:

    pass
class ControlNode:

    pass
class xmof_IntermediateActivities_InitialNode(ControlNode):

    pass
class xmof_IntermediateActivities_JoinNode(ControlNode):

    pass
class xmof_IntermediateActivities_ForkNode(ControlNode):

    pass
class xmof_IntermediateActivities_DecisionNode(ControlNode):

    pass
class xmof_IntermediateActivities_FinalNode(ControlNode):

    pass
class xmof_IntermediateActivities_MergeNode(ControlNode):

    pass
class EDataType:

    pass
class xmof_Kernel_PrimitiveType(EDataType):

    pass
class IntermediateActivities_ActivityNode:

    pass
class IntermediateActivities_Activity:

    pass
class ActivityEdge:

    pass
class xmof_IntermediateActivities_ObjectFlow(ActivityEdge):

    pass
class xmof_IntermediateActivities_ControlFlow(ActivityEdge):

    pass
class Kernel_ValueSpecification:

    pass
class Kernel_xmof_EStructuralFeature:

    pass
class EModelElement:

    pass
class xmof_IntermediateActions_LinkEndData(EModelElement):

    pass
class xmof_CompleteStructuredActivities_Clause(EModelElement):

    pass
class xmof_Kernel_Slot(EModelElement):

    pass
class LiteralSpecification:

    pass
class xmof_Kernel_LiteralInteger(LiteralSpecification):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class xmof_Kernel_LiteralNull(LiteralSpecification):

    pass
class xmof_Kernel_LiteralString(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class xmof_Kernel_LiteralUnlimitedNatural(LiteralSpecification):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class xmof_Kernel_LiteralBoolean(LiteralSpecification):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class Kernel_InstanceSpecification:

    pass
class EOperation:

    pass
class xmof_Kernel_BehavioredEOperation(EOperation):

    pass
class Kernel_Slot:

    pass
class Kernel_xmof_EClassifier:

    pass
class ETypedElement:

    pass
class xmof_BasicActions_Pin(ETypedElement, IntermediateActivities_ObjectNode):

    pass
class xmof_IntermediateActivities_ObjectNode(ETypedElement, IntermediateActivities_ActivityNode):

    pass
class xmof_Kernel_ValueSpecification(ETypedElement):

    pass
class Kernel_EEnumLiteralSpecification:

    pass
class ValueSpecification:

    pass
class xmof_Kernel_InstanceValue(ValueSpecification):

    pass
class xmof_Kernel_LiteralSpecification(ValueSpecification):

    pass
class xmof_Kernel_EnumValue(ValueSpecification):

    pass
class Kernel_xmof_EEnumLiteral:

    pass
class InstanceSpecification:

    pass
class xmof_Kernel_EEnumLiteralSpecification(InstanceSpecification):

    pass
class EParameter:

    pass
class xmof_Kernel_DirectedParameter(EParameter):

    def __init__(self, direction: str):
        self.direction = direction
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

class EClass:

    pass
class OpaqueBehavior:

    pass
class xmof_BasicBehaviors_FunctionBehavior(OpaqueBehavior):

    pass
class BasicBehaviors_Behavior:

    pass
class BehavioredEOperation:

    pass
class EClassifier:

    pass
class xmof_Communications_Reception(BehavioredEOperation):

    pass
class xmof_BasicBehaviors_BehavioredClassifier(EClassifier):

    pass
class Event:

    pass
class xmof_Communications_MessageEvent(Event):

    pass
class Communications_Signal:

    pass
class BasicBehaviors_BehavioredClassifier:

    pass
class xmof_Kernel_BehavioredEClass(BasicBehaviors_BehavioredClassifier, EClass):

    pass
class MessageEvent:

    pass
class xmof_Communications_SignalEvent(MessageEvent):

    pass
class Kernel_DirectedParameter:

    pass
class Communications_xmof_EAttribute:

    pass
class xmof_Communications_Signal(EClassifier):

    pass
class Communications_Event:

    pass
class ENamedElement:

    pass
class xmof_IntermediateActivities_ActivityNode(ENamedElement):

    pass
class xmof_IntermediateActivities_ActivityEdge(ENamedElement):

    pass
class xmof_Kernel_InstanceSpecification(ENamedElement):

    pass
class xmof_Communications_Event(ENamedElement):

    pass
class xmof_Communications_Trigger(ENamedElement):

    pass
class Behavior:

    pass
class xmof_IntermediateActivities_Activity(Behavior):

    def __init__(self, readOnly: bool, Activities42: set["IntermediateActivities_ActivityNode"] = None, Activities45: set["IntermediateActivities_ActivityEdge"] = None):
        self.readOnly = readOnly
        self.Activities42 = Activities42 if Activities42 is not None else set()
        self.Activities45 = Activities45 if Activities45 is not None else set()
        
    @property
    def readOnly(self) -> bool:
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly

    @property
    def Activities45(self):
        return self.__Activities45

    @Activities45.setter
    def Activities45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_IntermediateActivities_Activity__Activities45", None)
        self.__Activities45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax46"):
                    opp_val = getattr(item, "Syntax46", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax46"):
                    opp_val = getattr(item, "Syntax46", None)
                    
                    setattr(item, "Syntax46", self)
                    

    @property
    def Activities42(self):
        return self.__Activities42

    @Activities42.setter
    def Activities42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_IntermediateActivities_Activity__Activities42", None)
        self.__Activities42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax43"):
                    opp_val = getattr(item, "Syntax43", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax43"):
                    opp_val = getattr(item, "Syntax43", None)
                    
                    setattr(item, "Syntax43", self)
                    

class xmof_BasicBehaviors_OpaqueBehavior(Behavior):

    def __init__(self, language: str, body: str):
        self.language = language
        self.body = body
        
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

class Kernel_BehavioredEOperation:

    pass
class BehavioredEClass:

    pass
class xmof_BasicBehaviors_Behavior(BehavioredEClass):

    def __init__(self, reentrant: bool, Classes: "Kernel_BehavioredEOperation" = None, xmof_BasicBehaviors_Behavior: set["Kernel_DirectedParameter"] = None, xmof_BasicBehaviors_Behavior3: "BasicBehaviors_BehavioredClassifier" = None):
        self.reentrant = reentrant
        self.Classes = Classes
        self.xmof_BasicBehaviors_Behavior = xmof_BasicBehaviors_Behavior if xmof_BasicBehaviors_Behavior is not None else set()
        self.xmof_BasicBehaviors_Behavior3 = xmof_BasicBehaviors_Behavior3
        
    @property
    def reentrant(self) -> bool:
        return self.__reentrant

    @reentrant.setter
    def reentrant(self, reentrant: bool):
        self.__reentrant = reentrant

    @property
    def xmof_BasicBehaviors_Behavior(self):
        return self.__xmof_BasicBehaviors_Behavior

    @xmof_BasicBehaviors_Behavior.setter
    def xmof_BasicBehaviors_Behavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_BasicBehaviors_Behavior__xmof_BasicBehaviors_Behavior", None)
        self.__xmof_BasicBehaviors_Behavior = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_DirectedParameter"):
                    opp_val = getattr(item, "Kernel_DirectedParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_DirectedParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_DirectedParameter"):
                    opp_val = getattr(item, "Kernel_DirectedParameter", None)
                    
                    setattr(item, "Kernel_DirectedParameter", self)
                    

    @property
    def xmof_BasicBehaviors_Behavior3(self):
        return self.__xmof_BasicBehaviors_Behavior3

    @xmof_BasicBehaviors_Behavior3.setter
    def xmof_BasicBehaviors_Behavior3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_BasicBehaviors_Behavior__xmof_BasicBehaviors_Behavior3", None)
        self.__xmof_BasicBehaviors_Behavior3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicBehaviors_BehavioredClassifier"):
                opp_val = getattr(old_value, "BasicBehaviors_BehavioredClassifier", None)
                if opp_val == self:
                    setattr(old_value, "BasicBehaviors_BehavioredClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicBehaviors_BehavioredClassifier"):
                opp_val = getattr(value, "BasicBehaviors_BehavioredClassifier", None)
                setattr(value, "BasicBehaviors_BehavioredClassifier", self)

    @property
    def Classes(self):
        return self.__Classes

    @Classes.setter
    def Classes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_BasicBehaviors_Behavior__Classes", None)
        self.__Classes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Syntax"):
                opp_val = getattr(old_value, "Syntax", None)
                if opp_val == self:
                    setattr(old_value, "Syntax", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Syntax"):
                opp_val = getattr(value, "Syntax", None)
                setattr(value, "Syntax", self)
