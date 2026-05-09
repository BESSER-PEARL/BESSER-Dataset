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
class ParameterDirectionKind(Enum):
    in_ = "in_"
    inout = "inout"
    out = "out"
    return_ = "return_"
class VisibilityKind(Enum):
    public = "public"
    private = "private"
    protected = "protected"
    package = "package"
class AggregationKind(Enum):
    none = "none"
    shared = "shared"
    composite = "composite"
class CallConcurrencyKind(Enum):
    sequential = "sequential"


############################################
# Definition of Classes
############################################

class InvocationAction:

    pass
class fUML_BasicActions_SendSignalAction(InvocationAction):

    pass
class fUML_BasicActions_CallAction(InvocationAction):

    def __init__(self, synchronous: bool, fUML_BasicActions_CallAction: set["BasicActions_OutputPin"] = None):
        self.synchronous = synchronous
        self.fUML_BasicActions_CallAction = fUML_BasicActions_CallAction if fUML_BasicActions_CallAction is not None else set()
        
        pass
    @property
    def synchronous(self):
        return self.__synchronous

    @synchronous.setter
    def synchronous(self, synchronous: bool):
        self.__synchronous = synchronous


    @property
    def fUML_BasicActions_CallAction(self):
        return self.__fUML_BasicActions_CallAction

    @fUML_BasicActions_CallAction.setter
    def fUML_BasicActions_CallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_BasicActions_CallAction__fUML_BasicActions_CallAction", None)
        self.__fUML_BasicActions_CallAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin298"):
                    opp_val = getattr(item, "BasicActions_OutputPin298", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin298", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin298"):
                    opp_val = getattr(item, "BasicActions_OutputPin298", None)
                    
                    setattr(item, "BasicActions_OutputPin298", self)
                    

class IntermediateActivities_ObjectNode:

    pass
class Pin:

    pass
class fUML_BasicActions_OutputPin(Pin):

    pass
class fUML_BasicActions_InputPin(Pin):

    pass
class ExecutableNode:

    pass
class fUML_BasicActions_Action(ExecutableNode):

    def __init__(self, locallyReentrant: bool, fUML_BasicActions_Action292: "Kernel_Classifier" = None, fUML_BasicActions_Action295: set["BasicActions_InputPin"] = None, fUML_BasicActions_Action: set["BasicActions_OutputPin"] = None):
        self.locallyReentrant = locallyReentrant
        self.fUML_BasicActions_Action292 = fUML_BasicActions_Action292
        self.fUML_BasicActions_Action295 = fUML_BasicActions_Action295 if fUML_BasicActions_Action295 is not None else set()
        self.fUML_BasicActions_Action = fUML_BasicActions_Action if fUML_BasicActions_Action is not None else set()
        
        pass
    @property
    def locallyReentrant(self):
        return self.__locallyReentrant

    @locallyReentrant.setter
    def locallyReentrant(self, locallyReentrant: bool):
        self.__locallyReentrant = locallyReentrant


    @property
    def fUML_BasicActions_Action295(self):
        return self.__fUML_BasicActions_Action295

    @fUML_BasicActions_Action295.setter
    def fUML_BasicActions_Action295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_BasicActions_Action__fUML_BasicActions_Action295", None)
        self.__fUML_BasicActions_Action295 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_InputPin296"):
                    opp_val = getattr(item, "BasicActions_InputPin296", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_InputPin296", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_InputPin296"):
                    opp_val = getattr(item, "BasicActions_InputPin296", None)
                    
                    setattr(item, "BasicActions_InputPin296", self)
                    

    @property
    def fUML_BasicActions_Action292(self):
        return self.__fUML_BasicActions_Action292

    @fUML_BasicActions_Action292.setter
    def fUML_BasicActions_Action292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_BasicActions_Action__fUML_BasicActions_Action292", None)
        self.__fUML_BasicActions_Action292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel_Classifier293"):
                opp_val = getattr(old_value, "Kernel_Classifier293", None)
                if opp_val == self:
                    setattr(old_value, "Kernel_Classifier293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel_Classifier293"):
                opp_val = getattr(value, "Kernel_Classifier293", None)
                setattr(value, "Kernel_Classifier293", self)

    @property
    def fUML_BasicActions_Action(self):
        return self.__fUML_BasicActions_Action

    @fUML_BasicActions_Action.setter
    def fUML_BasicActions_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_BasicActions_Action__fUML_BasicActions_Action", None)
        self.__fUML_BasicActions_Action = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin290"):
                    opp_val = getattr(item, "BasicActions_OutputPin290", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin290", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin290"):
                    opp_val = getattr(item, "BasicActions_OutputPin290", None)
                    
                    setattr(item, "BasicActions_OutputPin290", self)
                    

class Communications_Trigger:

    pass
class CallAction:

    pass
class fUML_BasicActions_CallBehaviorAction(CallAction):

    pass
class fUML_BasicActions_CallOperationAction(CallAction):

    pass
class fUML_CompleteActions_StartObjectBehaviorAction(CallAction):

    pass
class WriteLinkAction:

    pass
class fUML_IntermediateActions_DestroyLinkAction(WriteLinkAction):

    pass
class fUML_IntermediateActions_CreateLinkAction(WriteLinkAction):

    pass
class LinkEndData:

    pass
class fUML_IntermediateActions_LinkEndDestructionData(LinkEndData):

    def __init__(self, destroyDuplicates: bool, fUML_IntermediateActions_LinkEndDestructionData: "BasicActions_InputPin" = None):
        self.destroyDuplicates = destroyDuplicates
        self.fUML_IntermediateActions_LinkEndDestructionData = fUML_IntermediateActions_LinkEndDestructionData
        
        pass
    @property
    def destroyDuplicates(self):
        return self.__destroyDuplicates

    @destroyDuplicates.setter
    def destroyDuplicates(self, destroyDuplicates: bool):
        self.__destroyDuplicates = destroyDuplicates


    @property
    def fUML_IntermediateActions_LinkEndDestructionData(self):
        return self.__fUML_IntermediateActions_LinkEndDestructionData

    @fUML_IntermediateActions_LinkEndDestructionData.setter
    def fUML_IntermediateActions_LinkEndDestructionData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_IntermediateActions_LinkEndDestructionData__fUML_IntermediateActions_LinkEndDestructionData", None)
        self.__fUML_IntermediateActions_LinkEndDestructionData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin236"):
                opp_val = getattr(old_value, "BasicActions_InputPin236", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin236", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin236"):
                opp_val = getattr(value, "BasicActions_InputPin236", None)
                setattr(value, "BasicActions_InputPin236", self)

class fUML_IntermediateActions_LinkEndCreationData(LinkEndData):

    def __init__(self, replaceAll: bool, fUML_IntermediateActions_LinkEndCreationData: "BasicActions_InputPin" = None):
        self.replaceAll = replaceAll
        self.fUML_IntermediateActions_LinkEndCreationData = fUML_IntermediateActions_LinkEndCreationData
        
        pass
    @property
    def replaceAll(self):
        return self.__replaceAll

    @replaceAll.setter
    def replaceAll(self, replaceAll: bool):
        self.__replaceAll = replaceAll


    @property
    def fUML_IntermediateActions_LinkEndCreationData(self):
        return self.__fUML_IntermediateActions_LinkEndCreationData

    @fUML_IntermediateActions_LinkEndCreationData.setter
    def fUML_IntermediateActions_LinkEndCreationData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_IntermediateActions_LinkEndCreationData__fUML_IntermediateActions_LinkEndCreationData", None)
        self.__fUML_IntermediateActions_LinkEndCreationData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin234"):
                opp_val = getattr(old_value, "BasicActions_InputPin234", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin234"):
                opp_val = getattr(value, "BasicActions_InputPin234", None)
                setattr(value, "BasicActions_InputPin234", self)

class WriteStructuralFeatureAction:

    pass
class fUML_IntermediateActions_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    def __init__(self, replaceAll: bool, fUML_IntermediateActions_AddStructuralFeatureValueAction: "BasicActions_InputPin" = None):
        self.replaceAll = replaceAll
        self.fUML_IntermediateActions_AddStructuralFeatureValueAction = fUML_IntermediateActions_AddStructuralFeatureValueAction
        
        pass
    @property
    def replaceAll(self):
        return self.__replaceAll

    @replaceAll.setter
    def replaceAll(self, replaceAll: bool):
        self.__replaceAll = replaceAll


    @property
    def fUML_IntermediateActions_AddStructuralFeatureValueAction(self):
        return self.__fUML_IntermediateActions_AddStructuralFeatureValueAction

    @fUML_IntermediateActions_AddStructuralFeatureValueAction.setter
    def fUML_IntermediateActions_AddStructuralFeatureValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_IntermediateActions_AddStructuralFeatureValueAction__fUML_IntermediateActions_AddStructuralFeatureValueAction", None)
        self.__fUML_IntermediateActions_AddStructuralFeatureValueAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin251"):
                opp_val = getattr(old_value, "BasicActions_InputPin251", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin251", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin251"):
                opp_val = getattr(value, "BasicActions_InputPin251", None)
                setattr(value, "BasicActions_InputPin251", self)

class fUML_IntermediateActions_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    def __init__(self, removeDuplicates: bool, fUML_IntermediateActions_RemoveStructuralFeatureValueAction: "BasicActions_InputPin" = None):
        self.removeDuplicates = removeDuplicates
        self.fUML_IntermediateActions_RemoveStructuralFeatureValueAction = fUML_IntermediateActions_RemoveStructuralFeatureValueAction
        
        pass
    @property
    def removeDuplicates(self):
        return self.__removeDuplicates

    @removeDuplicates.setter
    def removeDuplicates(self, removeDuplicates: bool):
        self.__removeDuplicates = removeDuplicates


    @property
    def fUML_IntermediateActions_RemoveStructuralFeatureValueAction(self):
        return self.__fUML_IntermediateActions_RemoveStructuralFeatureValueAction

    @fUML_IntermediateActions_RemoveStructuralFeatureValueAction.setter
    def fUML_IntermediateActions_RemoveStructuralFeatureValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_IntermediateActions_RemoveStructuralFeatureValueAction__fUML_IntermediateActions_RemoveStructuralFeatureValueAction", None)
        self.__fUML_IntermediateActions_RemoveStructuralFeatureValueAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin226"):
                opp_val = getattr(old_value, "BasicActions_InputPin226", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin226"):
                opp_val = getattr(value, "BasicActions_InputPin226", None)
                setattr(value, "BasicActions_InputPin226", self)

class StructuralFeatureAction:

    pass
class fUML_IntermediateActions_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class fUML_IntermediateActions_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class fUML_IntermediateActions_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class IntermediateActions_LinkEndData:

    pass
class LinkAction:

    pass
class fUML_IntermediateActions_ReadLinkAction(LinkAction):

    pass
class fUML_IntermediateActions_WriteLinkAction(LinkAction):

    pass
class ExtraStructuredActivities_ExpansionNode:

    pass
class ExtraStructuredActivities_ExpansionRegion:

    pass
class Action:

    pass
class fUML_CompleteActions_ReduceAction(Action):

    def __init__(self, ordered: bool, fUML_CompleteActions_ReduceAction: "BasicBehaviors_Behavior" = None, fUML_CompleteActions_ReduceAction259: "BasicActions_OutputPin" = None, fUML_CompleteActions_ReduceAction262: "BasicActions_InputPin" = None):
        self.ordered = ordered
        self.fUML_CompleteActions_ReduceAction = fUML_CompleteActions_ReduceAction
        self.fUML_CompleteActions_ReduceAction259 = fUML_CompleteActions_ReduceAction259
        self.fUML_CompleteActions_ReduceAction262 = fUML_CompleteActions_ReduceAction262
        
        pass
    @property
    def ordered(self):
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered


    @property
    def fUML_CompleteActions_ReduceAction262(self):
        return self.__fUML_CompleteActions_ReduceAction262

    @fUML_CompleteActions_ReduceAction262.setter
    def fUML_CompleteActions_ReduceAction262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteActions_ReduceAction__fUML_CompleteActions_ReduceAction262", None)
        self.__fUML_CompleteActions_ReduceAction262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin263"):
                opp_val = getattr(old_value, "BasicActions_InputPin263", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin263"):
                opp_val = getattr(value, "BasicActions_InputPin263", None)
                setattr(value, "BasicActions_InputPin263", self)

    @property
    def fUML_CompleteActions_ReduceAction259(self):
        return self.__fUML_CompleteActions_ReduceAction259

    @fUML_CompleteActions_ReduceAction259.setter
    def fUML_CompleteActions_ReduceAction259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteActions_ReduceAction__fUML_CompleteActions_ReduceAction259", None)
        self.__fUML_CompleteActions_ReduceAction259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_OutputPin260"):
                opp_val = getattr(old_value, "BasicActions_OutputPin260", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_OutputPin260", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_OutputPin260"):
                opp_val = getattr(value, "BasicActions_OutputPin260", None)
                setattr(value, "BasicActions_OutputPin260", self)

    @property
    def fUML_CompleteActions_ReduceAction(self):
        return self.__fUML_CompleteActions_ReduceAction

    @fUML_CompleteActions_ReduceAction.setter
    def fUML_CompleteActions_ReduceAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteActions_ReduceAction__fUML_CompleteActions_ReduceAction", None)
        self.__fUML_CompleteActions_ReduceAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicBehaviors_Behavior257"):
                opp_val = getattr(old_value, "BasicBehaviors_Behavior257", None)
                if opp_val == self:
                    setattr(old_value, "BasicBehaviors_Behavior257", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicBehaviors_Behavior257"):
                opp_val = getattr(value, "BasicBehaviors_Behavior257", None)
                setattr(value, "BasicBehaviors_Behavior257", self)

class fUML_CompleteActions_StartClassifierBehaviorAction(Action):

    pass
class fUML_CompleteActions_AcceptEventAction(Action):

    def __init__(self, unmarshall: bool, fUML_CompleteActions_AcceptEventAction: set["BasicActions_OutputPin"] = None, fUML_CompleteActions_AcceptEventAction288: set["Communications_Trigger"] = None):
        self.unmarshall = unmarshall
        self.fUML_CompleteActions_AcceptEventAction = fUML_CompleteActions_AcceptEventAction if fUML_CompleteActions_AcceptEventAction is not None else set()
        self.fUML_CompleteActions_AcceptEventAction288 = fUML_CompleteActions_AcceptEventAction288 if fUML_CompleteActions_AcceptEventAction288 is not None else set()
        
        pass
    @property
    def unmarshall(self):
        return self.__unmarshall

    @unmarshall.setter
    def unmarshall(self, unmarshall: bool):
        self.__unmarshall = unmarshall


    @property
    def fUML_CompleteActions_AcceptEventAction288(self):
        return self.__fUML_CompleteActions_AcceptEventAction288

    @fUML_CompleteActions_AcceptEventAction288.setter
    def fUML_CompleteActions_AcceptEventAction288(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteActions_AcceptEventAction__fUML_CompleteActions_AcceptEventAction288", None)
        self.__fUML_CompleteActions_AcceptEventAction288 = value if value is not None else set()
        
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
                    

    @property
    def fUML_CompleteActions_AcceptEventAction(self):
        return self.__fUML_CompleteActions_AcceptEventAction

    @fUML_CompleteActions_AcceptEventAction.setter
    def fUML_CompleteActions_AcceptEventAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteActions_AcceptEventAction__fUML_CompleteActions_AcceptEventAction", None)
        self.__fUML_CompleteActions_AcceptEventAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin286"):
                    opp_val = getattr(item, "BasicActions_OutputPin286", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin286", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin286"):
                    opp_val = getattr(item, "BasicActions_OutputPin286", None)
                    
                    setattr(item, "BasicActions_OutputPin286", self)
                    

class fUML_IntermediateActions_ClearAssociationAction(Action):

    pass
class fUML_IntermediateActions_ReadSelfAction(Action):

    pass
class fUML_CompleteActions_ReadExtentAction(Action):

    pass
class fUML_CompleteActions_ReclassifyObjectAction(Action):

    def __init__(self, replaceAll: bool, fUML_CompleteActions_ReclassifyObjectAction: set["Kernel_Classifier"] = None, fUML_CompleteActions_ReclassifyObjectAction280: "BasicActions_InputPin" = None, fUML_CompleteActions_ReclassifyObjectAction283: set["Kernel_Classifier"] = None):
        self.replaceAll = replaceAll
        self.fUML_CompleteActions_ReclassifyObjectAction = fUML_CompleteActions_ReclassifyObjectAction if fUML_CompleteActions_ReclassifyObjectAction is not None else set()
        self.fUML_CompleteActions_ReclassifyObjectAction280 = fUML_CompleteActions_ReclassifyObjectAction280
        self.fUML_CompleteActions_ReclassifyObjectAction283 = fUML_CompleteActions_ReclassifyObjectAction283 if fUML_CompleteActions_ReclassifyObjectAction283 is not None else set()
        
        pass
    @property
    def replaceAll(self):
        return self.__replaceAll

    @replaceAll.setter
    def replaceAll(self, replaceAll: bool):
        self.__replaceAll = replaceAll


    @property
    def fUML_CompleteActions_ReclassifyObjectAction(self):
        return self.__fUML_CompleteActions_ReclassifyObjectAction

    @fUML_CompleteActions_ReclassifyObjectAction.setter
    def fUML_CompleteActions_ReclassifyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteActions_ReclassifyObjectAction__fUML_CompleteActions_ReclassifyObjectAction", None)
        self.__fUML_CompleteActions_ReclassifyObjectAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_Classifier278"):
                    opp_val = getattr(item, "Kernel_Classifier278", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Classifier278", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Classifier278"):
                    opp_val = getattr(item, "Kernel_Classifier278", None)
                    
                    setattr(item, "Kernel_Classifier278", self)
                    

    @property
    def fUML_CompleteActions_ReclassifyObjectAction283(self):
        return self.__fUML_CompleteActions_ReclassifyObjectAction283

    @fUML_CompleteActions_ReclassifyObjectAction283.setter
    def fUML_CompleteActions_ReclassifyObjectAction283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteActions_ReclassifyObjectAction__fUML_CompleteActions_ReclassifyObjectAction283", None)
        self.__fUML_CompleteActions_ReclassifyObjectAction283 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_Classifier284"):
                    opp_val = getattr(item, "Kernel_Classifier284", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Classifier284", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Classifier284"):
                    opp_val = getattr(item, "Kernel_Classifier284", None)
                    
                    setattr(item, "Kernel_Classifier284", self)
                    

    @property
    def fUML_CompleteActions_ReclassifyObjectAction280(self):
        return self.__fUML_CompleteActions_ReclassifyObjectAction280

    @fUML_CompleteActions_ReclassifyObjectAction280.setter
    def fUML_CompleteActions_ReclassifyObjectAction280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteActions_ReclassifyObjectAction__fUML_CompleteActions_ReclassifyObjectAction280", None)
        self.__fUML_CompleteActions_ReclassifyObjectAction280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin281"):
                opp_val = getattr(old_value, "BasicActions_InputPin281", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin281"):
                opp_val = getattr(value, "BasicActions_InputPin281", None)
                setattr(value, "BasicActions_InputPin281", self)

class fUML_IntermediateActions_LinkAction(Action):

    pass
class fUML_IntermediateActions_TestIdentityAction(Action):

    pass
class fUML_IntermediateActions_ValueSpecificationAction(Action):

    pass
class fUML_IntermediateActions_DestroyObjectAction(Action):

    def __init__(self, destroyLinks: bool, destroyOwnedObjects: bool, fUML_IntermediateActions_DestroyObjectAction: "BasicActions_InputPin" = None):
        self.destroyLinks = destroyLinks
        self.destroyOwnedObjects = destroyOwnedObjects
        self.fUML_IntermediateActions_DestroyObjectAction = fUML_IntermediateActions_DestroyObjectAction
        
        pass
    @property
    def destroyOwnedObjects(self):
        return self.__destroyOwnedObjects

    @destroyOwnedObjects.setter
    def destroyOwnedObjects(self, destroyOwnedObjects: bool):
        self.__destroyOwnedObjects = destroyOwnedObjects


    @property
    def destroyLinks(self):
        return self.__destroyLinks

    @destroyLinks.setter
    def destroyLinks(self, destroyLinks: bool):
        self.__destroyLinks = destroyLinks


    @property
    def fUML_IntermediateActions_DestroyObjectAction(self):
        return self.__fUML_IntermediateActions_DestroyObjectAction

    @fUML_IntermediateActions_DestroyObjectAction.setter
    def fUML_IntermediateActions_DestroyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_IntermediateActions_DestroyObjectAction__fUML_IntermediateActions_DestroyObjectAction", None)
        self.__fUML_IntermediateActions_DestroyObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin249"):
                opp_val = getattr(old_value, "BasicActions_InputPin249", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin249"):
                opp_val = getattr(value, "BasicActions_InputPin249", None)
                setattr(value, "BasicActions_InputPin249", self)

class fUML_BasicActions_InvocationAction(Action):

    pass
class fUML_CompleteActions_ReadIsClassifiedObjectAction(Action):

    def __init__(self, direct: bool, fUML_CompleteActions_ReadIsClassifiedObjectAction: "Kernel_Classifier" = None, fUML_CompleteActions_ReadIsClassifiedObjectAction275: "BasicActions_InputPin" = None, fUML_CompleteActions_ReadIsClassifiedObjectAction272: "BasicActions_OutputPin" = None):
        self.direct = direct
        self.fUML_CompleteActions_ReadIsClassifiedObjectAction = fUML_CompleteActions_ReadIsClassifiedObjectAction
        self.fUML_CompleteActions_ReadIsClassifiedObjectAction275 = fUML_CompleteActions_ReadIsClassifiedObjectAction275
        self.fUML_CompleteActions_ReadIsClassifiedObjectAction272 = fUML_CompleteActions_ReadIsClassifiedObjectAction272
        
        pass
    @property
    def direct(self):
        return self.__direct

    @direct.setter
    def direct(self, direct: bool):
        self.__direct = direct


    @property
    def fUML_CompleteActions_ReadIsClassifiedObjectAction275(self):
        return self.__fUML_CompleteActions_ReadIsClassifiedObjectAction275

    @fUML_CompleteActions_ReadIsClassifiedObjectAction275.setter
    def fUML_CompleteActions_ReadIsClassifiedObjectAction275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteActions_ReadIsClassifiedObjectAction__fUML_CompleteActions_ReadIsClassifiedObjectAction275", None)
        self.__fUML_CompleteActions_ReadIsClassifiedObjectAction275 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin276"):
                opp_val = getattr(old_value, "BasicActions_InputPin276", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin276", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin276"):
                opp_val = getattr(value, "BasicActions_InputPin276", None)
                setattr(value, "BasicActions_InputPin276", self)

    @property
    def fUML_CompleteActions_ReadIsClassifiedObjectAction272(self):
        return self.__fUML_CompleteActions_ReadIsClassifiedObjectAction272

    @fUML_CompleteActions_ReadIsClassifiedObjectAction272.setter
    def fUML_CompleteActions_ReadIsClassifiedObjectAction272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteActions_ReadIsClassifiedObjectAction__fUML_CompleteActions_ReadIsClassifiedObjectAction272", None)
        self.__fUML_CompleteActions_ReadIsClassifiedObjectAction272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_OutputPin273"):
                opp_val = getattr(old_value, "BasicActions_OutputPin273", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_OutputPin273", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_OutputPin273"):
                opp_val = getattr(value, "BasicActions_OutputPin273", None)
                setattr(value, "BasicActions_OutputPin273", self)

    @property
    def fUML_CompleteActions_ReadIsClassifiedObjectAction(self):
        return self.__fUML_CompleteActions_ReadIsClassifiedObjectAction

    @fUML_CompleteActions_ReadIsClassifiedObjectAction.setter
    def fUML_CompleteActions_ReadIsClassifiedObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteActions_ReadIsClassifiedObjectAction__fUML_CompleteActions_ReadIsClassifiedObjectAction", None)
        self.__fUML_CompleteActions_ReadIsClassifiedObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel_Classifier270"):
                opp_val = getattr(old_value, "Kernel_Classifier270", None)
                if opp_val == self:
                    setattr(old_value, "Kernel_Classifier270", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel_Classifier270"):
                opp_val = getattr(value, "Kernel_Classifier270", None)
                setattr(value, "Kernel_Classifier270", self)

class fUML_IntermediateActions_CreateObjectAction(Action):

    pass
class fUML_IntermediateActions_StructuralFeatureAction(Action):

    pass
class fUML_CompleteStructuredActivities_StructuredActivityNode(Action):

    def __init__(self, mustIsolate: bool, inStructuredNode: set["IntermediateActivities_ActivityNode"] = None, fUML_CompleteStructuredActivities_StructuredActivityNode: set["BasicActions_OutputPin"] = None, fUML_CompleteStructuredActivities_StructuredActivityNode185: set["BasicActions_InputPin"] = None, inStructuredNode180: set["IntermediateActivities_ActivityEdge"] = None):
        self.mustIsolate = mustIsolate
        self.inStructuredNode = inStructuredNode if inStructuredNode is not None else set()
        self.fUML_CompleteStructuredActivities_StructuredActivityNode = fUML_CompleteStructuredActivities_StructuredActivityNode if fUML_CompleteStructuredActivities_StructuredActivityNode is not None else set()
        self.fUML_CompleteStructuredActivities_StructuredActivityNode185 = fUML_CompleteStructuredActivities_StructuredActivityNode185 if fUML_CompleteStructuredActivities_StructuredActivityNode185 is not None else set()
        self.inStructuredNode180 = inStructuredNode180 if inStructuredNode180 is not None else set()
        
        pass
    @property
    def mustIsolate(self):
        return self.__mustIsolate

    @mustIsolate.setter
    def mustIsolate(self, mustIsolate: bool):
        self.__mustIsolate = mustIsolate


    @property
    def fUML_CompleteStructuredActivities_StructuredActivityNode(self):
        return self.__fUML_CompleteStructuredActivities_StructuredActivityNode

    @fUML_CompleteStructuredActivities_StructuredActivityNode.setter
    def fUML_CompleteStructuredActivities_StructuredActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_StructuredActivityNode__fUML_CompleteStructuredActivities_StructuredActivityNode", None)
        self.__fUML_CompleteStructuredActivities_StructuredActivityNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin183"):
                    opp_val = getattr(item, "BasicActions_OutputPin183", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin183", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin183"):
                    opp_val = getattr(item, "BasicActions_OutputPin183", None)
                    
                    setattr(item, "BasicActions_OutputPin183", self)
                    

    @property
    def inStructuredNode180(self):
        return self.__inStructuredNode180

    @inStructuredNode180.setter
    def inStructuredNode180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_StructuredActivityNode__inStructuredNode180", None)
        self.__inStructuredNode180 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge181"):
                    opp_val = getattr(item, "ActivityEdge181", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge181", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge181"):
                    opp_val = getattr(item, "ActivityEdge181", None)
                    
                    setattr(item, "ActivityEdge181", self)
                    

    @property
    def inStructuredNode(self):
        return self.__inStructuredNode

    @inStructuredNode.setter
    def inStructuredNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_StructuredActivityNode__inStructuredNode", None)
        self.__inStructuredNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityNode178"):
                    opp_val = getattr(item, "ActivityNode178", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityNode178", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityNode178"):
                    opp_val = getattr(item, "ActivityNode178", None)
                    
                    setattr(item, "ActivityNode178", self)
                    

    @property
    def fUML_CompleteStructuredActivities_StructuredActivityNode185(self):
        return self.__fUML_CompleteStructuredActivities_StructuredActivityNode185

    @fUML_CompleteStructuredActivities_StructuredActivityNode185.setter
    def fUML_CompleteStructuredActivities_StructuredActivityNode185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_StructuredActivityNode__fUML_CompleteStructuredActivities_StructuredActivityNode185", None)
        self.__fUML_CompleteStructuredActivities_StructuredActivityNode185 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_InputPin186"):
                    opp_val = getattr(item, "BasicActions_InputPin186", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_InputPin186", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_InputPin186"):
                    opp_val = getattr(item, "BasicActions_InputPin186", None)
                    
                    setattr(item, "BasicActions_InputPin186", self)
                    

class CompleteStructuredActivities_Clause:

    pass
class ActivityNode:

    pass
class fUML_CompleteStructuredActivities_ExecutableNode(ActivityNode):

    pass
class fUML_IntermediateActivities_ControlNode(ActivityNode):

    pass
class ControlNode:

    pass
class fUML_IntermediateActivities_JoinNode(ControlNode):

    pass
class fUML_IntermediateActivities_InitialNode(ControlNode):

    pass
class fUML_IntermediateActivities_MergeNode(ControlNode):

    pass
class BasicActions_InputPin:

    pass
class CompleteStructuredActivities_ExecutableNode:

    pass
class BasicActions_OutputPin:

    pass
class StructuredActivityNode:

    pass
class fUML_ExtraStructuredActivities_ExpansionRegion(StructuredActivityNode):

    def __init__(self, mode: str, regionAsInput: set["ExtraStructuredActivities_ExpansionNode"] = None, regionAsOutput: set["ExtraStructuredActivities_ExpansionNode"] = None):
        self.mode = mode
        self.regionAsInput = regionAsInput if regionAsInput is not None else set()
        self.regionAsOutput = regionAsOutput if regionAsOutput is not None else set()
        
        pass
    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode


    @property
    def regionAsOutput(self):
        return self.__regionAsOutput

    @regionAsOutput.setter
    def regionAsOutput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_ExtraStructuredActivities_ExpansionRegion__regionAsOutput", None)
        self.__regionAsOutput = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExpansionNode192"):
                    opp_val = getattr(item, "ExpansionNode192", None)
                    
                    if opp_val == self:
                        setattr(item, "ExpansionNode192", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExpansionNode192"):
                    opp_val = getattr(item, "ExpansionNode192", None)
                    
                    setattr(item, "ExpansionNode192", self)
                    

    @property
    def regionAsInput(self):
        return self.__regionAsInput

    @regionAsInput.setter
    def regionAsInput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_ExtraStructuredActivities_ExpansionRegion__regionAsInput", None)
        self.__regionAsInput = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExpansionNode"):
                    opp_val = getattr(item, "ExpansionNode", None)
                    
                    if opp_val == self:
                        setattr(item, "ExpansionNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExpansionNode"):
                    opp_val = getattr(item, "ExpansionNode", None)
                    
                    setattr(item, "ExpansionNode", self)
                    

class fUML_CompleteStructuredActivities_ConditionalNode(StructuredActivityNode):

    def __init__(self, determinate: bool, assured: bool, fUML_CompleteStructuredActivities_ConditionalNode: set["CompleteStructuredActivities_Clause"] = None, fUML_CompleteStructuredActivities_ConditionalNode175: set["BasicActions_OutputPin"] = None):
        self.determinate = determinate
        self.assured = assured
        self.fUML_CompleteStructuredActivities_ConditionalNode = fUML_CompleteStructuredActivities_ConditionalNode if fUML_CompleteStructuredActivities_ConditionalNode is not None else set()
        self.fUML_CompleteStructuredActivities_ConditionalNode175 = fUML_CompleteStructuredActivities_ConditionalNode175 if fUML_CompleteStructuredActivities_ConditionalNode175 is not None else set()
        
        pass
    @property
    def assured(self):
        return self.__assured

    @assured.setter
    def assured(self, assured: bool):
        self.__assured = assured


    @property
    def determinate(self):
        return self.__determinate

    @determinate.setter
    def determinate(self, determinate: bool):
        self.__determinate = determinate


    @property
    def fUML_CompleteStructuredActivities_ConditionalNode175(self):
        return self.__fUML_CompleteStructuredActivities_ConditionalNode175

    @fUML_CompleteStructuredActivities_ConditionalNode175.setter
    def fUML_CompleteStructuredActivities_ConditionalNode175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_ConditionalNode__fUML_CompleteStructuredActivities_ConditionalNode175", None)
        self.__fUML_CompleteStructuredActivities_ConditionalNode175 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin176"):
                    opp_val = getattr(item, "BasicActions_OutputPin176", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin176", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin176"):
                    opp_val = getattr(item, "BasicActions_OutputPin176", None)
                    
                    setattr(item, "BasicActions_OutputPin176", self)
                    

    @property
    def fUML_CompleteStructuredActivities_ConditionalNode(self):
        return self.__fUML_CompleteStructuredActivities_ConditionalNode

    @fUML_CompleteStructuredActivities_ConditionalNode.setter
    def fUML_CompleteStructuredActivities_ConditionalNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_ConditionalNode__fUML_CompleteStructuredActivities_ConditionalNode", None)
        self.__fUML_CompleteStructuredActivities_ConditionalNode = value if value is not None else set()
        
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
                    

class fUML_CompleteStructuredActivities_LoopNode(StructuredActivityNode):

    def __init__(self, testedFirst: bool, fUML_CompleteStructuredActivities_LoopNode: "BasicActions_OutputPin" = None, fUML_CompleteStructuredActivities_LoopNode141: set["CompleteStructuredActivities_ExecutableNode"] = None, fUML_CompleteStructuredActivities_LoopNode143: set["BasicActions_OutputPin"] = None, fUML_CompleteStructuredActivities_LoopNode146: set["BasicActions_InputPin"] = None, fUML_CompleteStructuredActivities_LoopNode148: set["CompleteStructuredActivities_ExecutableNode"] = None, fUML_CompleteStructuredActivities_LoopNode151: set["BasicActions_OutputPin"] = None, fUML_CompleteStructuredActivities_LoopNode154: set["BasicActions_OutputPin"] = None, fUML_CompleteStructuredActivities_LoopNode157: set["CompleteStructuredActivities_ExecutableNode"] = None):
        self.testedFirst = testedFirst
        self.fUML_CompleteStructuredActivities_LoopNode = fUML_CompleteStructuredActivities_LoopNode
        self.fUML_CompleteStructuredActivities_LoopNode141 = fUML_CompleteStructuredActivities_LoopNode141 if fUML_CompleteStructuredActivities_LoopNode141 is not None else set()
        self.fUML_CompleteStructuredActivities_LoopNode143 = fUML_CompleteStructuredActivities_LoopNode143 if fUML_CompleteStructuredActivities_LoopNode143 is not None else set()
        self.fUML_CompleteStructuredActivities_LoopNode146 = fUML_CompleteStructuredActivities_LoopNode146 if fUML_CompleteStructuredActivities_LoopNode146 is not None else set()
        self.fUML_CompleteStructuredActivities_LoopNode148 = fUML_CompleteStructuredActivities_LoopNode148 if fUML_CompleteStructuredActivities_LoopNode148 is not None else set()
        self.fUML_CompleteStructuredActivities_LoopNode151 = fUML_CompleteStructuredActivities_LoopNode151 if fUML_CompleteStructuredActivities_LoopNode151 is not None else set()
        self.fUML_CompleteStructuredActivities_LoopNode154 = fUML_CompleteStructuredActivities_LoopNode154 if fUML_CompleteStructuredActivities_LoopNode154 is not None else set()
        self.fUML_CompleteStructuredActivities_LoopNode157 = fUML_CompleteStructuredActivities_LoopNode157 if fUML_CompleteStructuredActivities_LoopNode157 is not None else set()
        
        pass
    @property
    def testedFirst(self):
        return self.__testedFirst

    @testedFirst.setter
    def testedFirst(self, testedFirst: bool):
        self.__testedFirst = testedFirst


    @property
    def fUML_CompleteStructuredActivities_LoopNode154(self):
        return self.__fUML_CompleteStructuredActivities_LoopNode154

    @fUML_CompleteStructuredActivities_LoopNode154.setter
    def fUML_CompleteStructuredActivities_LoopNode154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_LoopNode__fUML_CompleteStructuredActivities_LoopNode154", None)
        self.__fUML_CompleteStructuredActivities_LoopNode154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin155"):
                    opp_val = getattr(item, "BasicActions_OutputPin155", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin155"):
                    opp_val = getattr(item, "BasicActions_OutputPin155", None)
                    
                    setattr(item, "BasicActions_OutputPin155", self)
                    

    @property
    def fUML_CompleteStructuredActivities_LoopNode146(self):
        return self.__fUML_CompleteStructuredActivities_LoopNode146

    @fUML_CompleteStructuredActivities_LoopNode146.setter
    def fUML_CompleteStructuredActivities_LoopNode146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_LoopNode__fUML_CompleteStructuredActivities_LoopNode146", None)
        self.__fUML_CompleteStructuredActivities_LoopNode146 = value if value is not None else set()
        
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
    def fUML_CompleteStructuredActivities_LoopNode143(self):
        return self.__fUML_CompleteStructuredActivities_LoopNode143

    @fUML_CompleteStructuredActivities_LoopNode143.setter
    def fUML_CompleteStructuredActivities_LoopNode143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_LoopNode__fUML_CompleteStructuredActivities_LoopNode143", None)
        self.__fUML_CompleteStructuredActivities_LoopNode143 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin144"):
                    opp_val = getattr(item, "BasicActions_OutputPin144", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin144", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin144"):
                    opp_val = getattr(item, "BasicActions_OutputPin144", None)
                    
                    setattr(item, "BasicActions_OutputPin144", self)
                    

    @property
    def fUML_CompleteStructuredActivities_LoopNode148(self):
        return self.__fUML_CompleteStructuredActivities_LoopNode148

    @fUML_CompleteStructuredActivities_LoopNode148.setter
    def fUML_CompleteStructuredActivities_LoopNode148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_LoopNode__fUML_CompleteStructuredActivities_LoopNode148", None)
        self.__fUML_CompleteStructuredActivities_LoopNode148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode149"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode149", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteStructuredActivities_ExecutableNode149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode149"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode149", None)
                    
                    setattr(item, "CompleteStructuredActivities_ExecutableNode149", self)
                    

    @property
    def fUML_CompleteStructuredActivities_LoopNode151(self):
        return self.__fUML_CompleteStructuredActivities_LoopNode151

    @fUML_CompleteStructuredActivities_LoopNode151.setter
    def fUML_CompleteStructuredActivities_LoopNode151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_LoopNode__fUML_CompleteStructuredActivities_LoopNode151", None)
        self.__fUML_CompleteStructuredActivities_LoopNode151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin152"):
                    opp_val = getattr(item, "BasicActions_OutputPin152", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin152", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin152"):
                    opp_val = getattr(item, "BasicActions_OutputPin152", None)
                    
                    setattr(item, "BasicActions_OutputPin152", self)
                    

    @property
    def fUML_CompleteStructuredActivities_LoopNode141(self):
        return self.__fUML_CompleteStructuredActivities_LoopNode141

    @fUML_CompleteStructuredActivities_LoopNode141.setter
    def fUML_CompleteStructuredActivities_LoopNode141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_LoopNode__fUML_CompleteStructuredActivities_LoopNode141", None)
        self.__fUML_CompleteStructuredActivities_LoopNode141 = value if value is not None else set()
        
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
    def fUML_CompleteStructuredActivities_LoopNode(self):
        return self.__fUML_CompleteStructuredActivities_LoopNode

    @fUML_CompleteStructuredActivities_LoopNode.setter
    def fUML_CompleteStructuredActivities_LoopNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_LoopNode__fUML_CompleteStructuredActivities_LoopNode", None)
        self.__fUML_CompleteStructuredActivities_LoopNode = value
        
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
    def fUML_CompleteStructuredActivities_LoopNode157(self):
        return self.__fUML_CompleteStructuredActivities_LoopNode157

    @fUML_CompleteStructuredActivities_LoopNode157.setter
    def fUML_CompleteStructuredActivities_LoopNode157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_LoopNode__fUML_CompleteStructuredActivities_LoopNode157", None)
        self.__fUML_CompleteStructuredActivities_LoopNode157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode158"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode158", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteStructuredActivities_ExecutableNode158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode158"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode158", None)
                    
                    setattr(item, "CompleteStructuredActivities_ExecutableNode158", self)
                    

class ObjectNode:

    pass
class fUML_ExtraStructuredActivities_ExpansionNode(ObjectNode):

    pass
class fUML_IntermediateActivities_ActivityParameterNode(ObjectNode):

    pass
class FinalNode:

    pass
class fUML_IntermediateActivities_ActivityFinalNode(FinalNode):

    pass
class IntermediateActivities_ObjectFlow:

    pass
class fUML_IntermediateActivities_DecisionNode(ControlNode):

    pass
class fUML_IntermediateActivities_ForkNode(ControlNode):

    pass
class fUML_IntermediateActivities_FinalNode(ControlNode):

    pass
class IntermediateActivities_ActivityNode:

    pass
class IntermediateActivities_ActivityEdge:

    pass
class CompleteStructuredActivities_StructuredActivityNode:

    pass
class DataType:

    pass
class fUML_Kernel_Enumeration(DataType):

    pass
class fUML_Kernel_PrimitiveType(DataType):

    pass
class IntermediateActivities_Activity:

    pass
class ActivityEdge:

    pass
class fUML_IntermediateActivities_ControlFlow(ActivityEdge):

    pass
class fUML_IntermediateActivities_ObjectFlow(ActivityEdge):

    pass
class Communications_Reception:

    pass
class BehavioredClassifier:

    pass
class fUML_Kernel_Class(BehavioredClassifier):

    def __init__(self, active: bool, class_: set["Kernel_Property"] = None, class_105: set["Kernel_Operation"] = None, fUML_Kernel_Class: set["Kernel_Class"] = None, fUML_Kernel_Class108: set["Communications_Reception"] = None, fUML_Kernel_Class110: set["Kernel_Classifier"] = None):
        self.active = active
        self.class_ = class_ if class_ is not None else set()
        self.class_105 = class_105 if class_105 is not None else set()
        self.fUML_Kernel_Class = fUML_Kernel_Class if fUML_Kernel_Class is not None else set()
        self.fUML_Kernel_Class108 = fUML_Kernel_Class108 if fUML_Kernel_Class108 is not None else set()
        self.fUML_Kernel_Class110 = fUML_Kernel_Class110 if fUML_Kernel_Class110 is not None else set()
        
        pass
    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active


    @property
    def fUML_Kernel_Class108(self):
        return self.__fUML_Kernel_Class108

    @fUML_Kernel_Class108.setter
    def fUML_Kernel_Class108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Class__fUML_Kernel_Class108", None)
        self.__fUML_Kernel_Class108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Communications_Reception"):
                    opp_val = getattr(item, "Communications_Reception", None)
                    
                    if opp_val == self:
                        setattr(item, "Communications_Reception", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Communications_Reception"):
                    opp_val = getattr(item, "Communications_Reception", None)
                    
                    setattr(item, "Communications_Reception", self)
                    

    @property
    def class_(self):
        return self.__class_

    @class_.setter
    def class_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Class__class_", None)
        self.__class_ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property103"):
                    opp_val = getattr(item, "Property103", None)
                    
                    if opp_val == self:
                        setattr(item, "Property103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property103"):
                    opp_val = getattr(item, "Property103", None)
                    
                    setattr(item, "Property103", self)
                    

    @property
    def fUML_Kernel_Class110(self):
        return self.__fUML_Kernel_Class110

    @fUML_Kernel_Class110.setter
    def fUML_Kernel_Class110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Class__fUML_Kernel_Class110", None)
        self.__fUML_Kernel_Class110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_Classifier111"):
                    opp_val = getattr(item, "Kernel_Classifier111", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Classifier111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Classifier111"):
                    opp_val = getattr(item, "Kernel_Classifier111", None)
                    
                    setattr(item, "Kernel_Classifier111", self)
                    

    @property
    def fUML_Kernel_Class(self):
        return self.__fUML_Kernel_Class

    @fUML_Kernel_Class.setter
    def fUML_Kernel_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Class__fUML_Kernel_Class", None)
        self.__fUML_Kernel_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_Class"):
                    opp_val = getattr(item, "Kernel_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Class"):
                    opp_val = getattr(item, "Kernel_Class", None)
                    
                    setattr(item, "Kernel_Class", self)
                    

    @property
    def class_105(self):
        return self.__class_105

    @class_105.setter
    def class_105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Class__class_105", None)
        self.__class_105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    setattr(item, "Operation", self)
                    

class Kernel_Enumeration:

    pass
class InstanceSpecification:

    pass
class fUML_Kernel_EnumerationLiteral(InstanceSpecification):

    pass
class Kernel_EnumerationLiteral:

    pass
class Kernel_Slot:

    pass
class LiteralSpecification:

    pass
class fUML_Kernel_LiteralString(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class fUML_Kernel_LiteralUnlimitedNatural(LiteralSpecification):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class fUML_Kernel_LiteralInteger(LiteralSpecification):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class fUML_Kernel_LiteralNull(LiteralSpecification):

    pass
class ValueSpecification:

    pass
class fUML_Kernel_LiteralSpecification(ValueSpecification):

    pass
class fUML_Kernel_InstanceValue(ValueSpecification):

    pass
class Kernel_InstanceSpecification:

    pass
class Kernel_StructuralFeature:

    pass
class Kernel_Operation:

    pass
class Feature:

    pass
class fUML_Kernel_BehavioralFeature(Feature):

    def __init__(self, abstract: bool, concurrency: str, fUML_Kernel_BehavioralFeature: set["Kernel_Parameter"] = None, specification: set["BasicBehaviors_Behavior"] = None):
        self.abstract = abstract
        self.concurrency = concurrency
        self.fUML_Kernel_BehavioralFeature = fUML_Kernel_BehavioralFeature if fUML_Kernel_BehavioralFeature is not None else set()
        self.specification = specification if specification is not None else set()
        
        pass
    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract


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
        old_value = getattr(self, f"_fUML_Kernel_BehavioralFeature__specification", None)
        self.__specification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Behavior"):
                    opp_val = getattr(item, "Behavior", None)
                    
                    if opp_val == self:
                        setattr(item, "Behavior", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Behavior"):
                    opp_val = getattr(item, "Behavior", None)
                    
                    setattr(item, "Behavior", self)
                    

    @property
    def fUML_Kernel_BehavioralFeature(self):
        return self.__fUML_Kernel_BehavioralFeature

    @fUML_Kernel_BehavioralFeature.setter
    def fUML_Kernel_BehavioralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_BehavioralFeature__fUML_Kernel_BehavioralFeature", None)
        self.__fUML_Kernel_BehavioralFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_Parameter83"):
                    opp_val = getattr(item, "Kernel_Parameter83", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Parameter83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Parameter83"):
                    opp_val = getattr(item, "Kernel_Parameter83", None)
                    
                    setattr(item, "Kernel_Parameter83", self)
                    

class Kernel_ValueSpecification:

    pass
class StructuralFeature:

    pass
class fUML_Kernel_Property(StructuralFeature):

    def __init__(self, aggregation: str, composite: bool, derived: bool, derivedUnion: bool, ownedEnd: "Kernel_Association" = None, memberEnd: "Kernel_Association" = None, ownedAttribute: "Kernel_DataType" = None, ownedAttribute65: "Kernel_Class" = None, fUML_Kernel_Property: "Kernel_Property" = None):
        self.aggregation = aggregation
        self.composite = composite
        self.derived = derived
        self.derivedUnion = derivedUnion
        self.ownedEnd = ownedEnd
        self.memberEnd = memberEnd
        self.ownedAttribute = ownedAttribute
        self.ownedAttribute65 = ownedAttribute65
        self.fUML_Kernel_Property = fUML_Kernel_Property
        
        pass
    @property
    def derived(self):
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived


    @property
    def aggregation(self):
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation


    @property
    def derivedUnion(self):
        return self.__derivedUnion

    @derivedUnion.setter
    def derivedUnion(self, derivedUnion: bool):
        self.__derivedUnion = derivedUnion


    @property
    def composite(self):
        return self.__composite

    @composite.setter
    def composite(self, composite: bool):
        self.__composite = composite


    @property
    def ownedAttribute65(self):
        return self.__ownedAttribute65

    @ownedAttribute65.setter
    def ownedAttribute65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Property__ownedAttribute65", None)
        self.__ownedAttribute65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class"):
                opp_val = getattr(old_value, "Class", None)
                if opp_val == self:
                    setattr(old_value, "Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class"):
                opp_val = getattr(value, "Class", None)
                setattr(value, "Class", self)

    @property
    def ownedAttribute(self):
        return self.__ownedAttribute

    @ownedAttribute.setter
    def ownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Property__ownedAttribute", None)
        self.__ownedAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType"):
                opp_val = getattr(old_value, "DataType", None)
                if opp_val == self:
                    setattr(old_value, "DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType"):
                opp_val = getattr(value, "DataType", None)
                setattr(value, "DataType", self)

    @property
    def memberEnd(self):
        return self.__memberEnd

    @memberEnd.setter
    def memberEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Property__memberEnd", None)
        self.__memberEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association62"):
                opp_val = getattr(old_value, "Association62", None)
                if opp_val == self:
                    setattr(old_value, "Association62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association62"):
                opp_val = getattr(value, "Association62", None)
                setattr(value, "Association62", self)

    @property
    def ownedEnd(self):
        return self.__ownedEnd

    @ownedEnd.setter
    def ownedEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Property__ownedEnd", None)
        self.__ownedEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association"):
                opp_val = getattr(old_value, "Association", None)
                if opp_val == self:
                    setattr(old_value, "Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association"):
                opp_val = getattr(value, "Association", None)
                setattr(value, "Association", self)

    @property
    def fUML_Kernel_Property(self):
        return self.__fUML_Kernel_Property

    @fUML_Kernel_Property.setter
    def fUML_Kernel_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Property__fUML_Kernel_Property", None)
        self.__fUML_Kernel_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel_Property67"):
                opp_val = getattr(old_value, "Kernel_Property67", None)
                if opp_val == self:
                    setattr(old_value, "Kernel_Property67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel_Property67"):
                opp_val = getattr(value, "Kernel_Property67", None)
                setattr(value, "Kernel_Property67", self)

class Kernel_Class:

    pass
class Kernel_DataType:

    pass
class Kernel_Association:

    pass
class Kernel_Generalization:

    pass
class Kernel_Classifier:

    pass
class RedefinableElement:

    pass
class fUML_IntermediateActivities_ActivityNode(RedefinableElement):

    pass
class fUML_IntermediateActivities_ActivityEdge(RedefinableElement):

    pass
class fUML_Kernel_Feature(RedefinableElement):

    def __init__(self, static: bool, feature: set["Kernel_Classifier"] = None):
        self.static = static
        self.feature = feature if feature is not None else set()
        
        pass
    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static


    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Feature__feature", None)
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
                    

class Kernel_TypedElement:

    pass
class fUML_IntermediateActivities_ObjectNode(IntermediateActivities_ActivityNode, Kernel_TypedElement):

    pass
class Kernel_MultiplicityElement:

    pass
class fUML_Kernel_Parameter(Kernel_MultiplicityElement, Kernel_TypedElement):

    def __init__(self, direction: str):
        self.direction = direction
        
        pass
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


class fUML_BasicActions_Pin(IntermediateActivities_ObjectNode, Kernel_MultiplicityElement):

    pass
class Kernel_Feature:

    pass
class fUML_Kernel_StructuralFeature(Kernel_MultiplicityElement, Kernel_TypedElement, Kernel_Feature):

    def __init__(self, readOnly: bool, Feature: "fUML_Kernel_Classifier" = None):
        self.readOnly = readOnly
        
        pass
    @property
    def readOnly(self):
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly


class Kernel_RedefinableElement:

    pass
class Kernel_Package:

    pass
class Kernel_PackageableElement:

    pass
class Kernel_PackageImport:

    pass
class Kernel_ElementImport:

    pass
class Kernel_NamedElement:

    pass
class fUML_Kernel_Comment:

    def __init__(self, body: str, fUML_Kernel_Comment: set["Kernel_Element"] = None):
        self.body = body
        self.fUML_Kernel_Comment = fUML_Kernel_Comment if fUML_Kernel_Comment is not None else set()
        
        pass
    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


    @property
    def fUML_Kernel_Comment(self):
        return self.__fUML_Kernel_Comment

    @fUML_Kernel_Comment.setter
    def fUML_Kernel_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Comment__fUML_Kernel_Comment", None)
        self.__fUML_Kernel_Comment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_Element"):
                    opp_val = getattr(item, "Kernel_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Element"):
                    opp_val = getattr(item, "Kernel_Element", None)
                    
                    setattr(item, "Kernel_Element", self)
                    

class Kernel_Comment:

    pass
class Kernel_Element:

    pass
class fUML_Kernel_Element(ABC):

    pass
class Element:

    pass
class fUML_Kernel_MultiplicityElement(Element):

    def __init__(self, ordered: bool, unique: bool, upper: int, lower: int, fUML_Kernel_MultiplicityElement: "Kernel_ValueSpecification" = None, fUML_Kernel_MultiplicityElement80: "Kernel_ValueSpecification" = None):
        self.ordered = ordered
        self.unique = unique
        self.upper = upper
        self.lower = lower
        self.fUML_Kernel_MultiplicityElement = fUML_Kernel_MultiplicityElement
        self.fUML_Kernel_MultiplicityElement80 = fUML_Kernel_MultiplicityElement80
        
        pass
    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper


    @property
    def ordered(self):
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered


    @property
    def unique(self):
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique


    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower


    @property
    def fUML_Kernel_MultiplicityElement80(self):
        return self.__fUML_Kernel_MultiplicityElement80

    @fUML_Kernel_MultiplicityElement80.setter
    def fUML_Kernel_MultiplicityElement80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_MultiplicityElement__fUML_Kernel_MultiplicityElement80", None)
        self.__fUML_Kernel_MultiplicityElement80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel_ValueSpecification81"):
                opp_val = getattr(old_value, "Kernel_ValueSpecification81", None)
                if opp_val == self:
                    setattr(old_value, "Kernel_ValueSpecification81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel_ValueSpecification81"):
                opp_val = getattr(value, "Kernel_ValueSpecification81", None)
                setattr(value, "Kernel_ValueSpecification81", self)

    @property
    def fUML_Kernel_MultiplicityElement(self):
        return self.__fUML_Kernel_MultiplicityElement

    @fUML_Kernel_MultiplicityElement.setter
    def fUML_Kernel_MultiplicityElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_MultiplicityElement__fUML_Kernel_MultiplicityElement", None)
        self.__fUML_Kernel_MultiplicityElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel_ValueSpecification"):
                opp_val = getattr(old_value, "Kernel_ValueSpecification", None)
                if opp_val == self:
                    setattr(old_value, "Kernel_ValueSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel_ValueSpecification"):
                opp_val = getattr(value, "Kernel_ValueSpecification", None)
                setattr(value, "Kernel_ValueSpecification", self)

class fUML_Kernel_Generalization(Element):

    def __init__(self, substitutable: bool, fUML_Kernel_Generalization: "Kernel_Classifier" = None, generalization: "Kernel_Classifier" = None):
        self.substitutable = substitutable
        self.fUML_Kernel_Generalization = fUML_Kernel_Generalization
        self.generalization = generalization
        
        pass
    @property
    def substitutable(self):
        return self.__substitutable

    @substitutable.setter
    def substitutable(self, substitutable: bool):
        self.__substitutable = substitutable


    @property
    def fUML_Kernel_Generalization(self):
        return self.__fUML_Kernel_Generalization

    @fUML_Kernel_Generalization.setter
    def fUML_Kernel_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Generalization__fUML_Kernel_Generalization", None)
        self.__fUML_Kernel_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel_Classifier57"):
                opp_val = getattr(old_value, "Kernel_Classifier57", None)
                if opp_val == self:
                    setattr(old_value, "Kernel_Classifier57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel_Classifier57"):
                opp_val = getattr(value, "Kernel_Classifier57", None)
                setattr(value, "Kernel_Classifier57", self)

    @property
    def generalization(self):
        return self.__generalization

    @generalization.setter
    def generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Generalization__generalization", None)
        self.__generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier59"):
                opp_val = getattr(old_value, "Classifier59", None)
                if opp_val == self:
                    setattr(old_value, "Classifier59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier59"):
                opp_val = getattr(value, "Classifier59", None)
                setattr(value, "Classifier59", self)

class fUML_CompleteStructuredActivities_Clause(Element):

    pass
class fUML_IntermediateActions_LinkEndData(Element):

    pass
class fUML_Kernel_ElementImport(Element):

    def __init__(self, visibility: str, alias: str, fUML_Kernel_ElementImport: "Kernel_PackageableElement" = None, elementImport: "Kernel_Namespace" = None):
        self.visibility = visibility
        self.alias = alias
        self.fUML_Kernel_ElementImport = fUML_Kernel_ElementImport
        self.elementImport = elementImport
        
        pass
    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias


    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility


    @property
    def fUML_Kernel_ElementImport(self):
        return self.__fUML_Kernel_ElementImport

    @fUML_Kernel_ElementImport.setter
    def fUML_Kernel_ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_ElementImport__fUML_Kernel_ElementImport", None)
        self.__fUML_Kernel_ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel_PackageableElement28"):
                opp_val = getattr(old_value, "Kernel_PackageableElement28", None)
                if opp_val == self:
                    setattr(old_value, "Kernel_PackageableElement28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel_PackageableElement28"):
                opp_val = getattr(value, "Kernel_PackageableElement28", None)
                setattr(value, "Kernel_PackageableElement28", self)

    @property
    def elementImport(self):
        return self.__elementImport

    @elementImport.setter
    def elementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_ElementImport__elementImport", None)
        self.__elementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace30"):
                opp_val = getattr(old_value, "Namespace30", None)
                if opp_val == self:
                    setattr(old_value, "Namespace30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace30"):
                opp_val = getattr(value, "Namespace30", None)
                setattr(value, "Namespace30", self)

class fUML_Kernel_Slot(Element):

    pass
class fUML_Kernel_PackageImport(Element):

    def __init__(self, visibility: str, fUML_Kernel_PackageImport: "Kernel_Package" = None, packageImport: "Kernel_Namespace" = None):
        self.visibility = visibility
        self.fUML_Kernel_PackageImport = fUML_Kernel_PackageImport
        self.packageImport = packageImport
        
        pass
    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility


    @property
    def fUML_Kernel_PackageImport(self):
        return self.__fUML_Kernel_PackageImport

    @fUML_Kernel_PackageImport.setter
    def fUML_Kernel_PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_PackageImport__fUML_Kernel_PackageImport", None)
        self.__fUML_Kernel_PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel_Package"):
                opp_val = getattr(old_value, "Kernel_Package", None)
                if opp_val == self:
                    setattr(old_value, "Kernel_Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel_Package"):
                opp_val = getattr(value, "Kernel_Package", None)
                setattr(value, "Kernel_Package", self)

    @property
    def packageImport(self):
        return self.__packageImport

    @packageImport.setter
    def packageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_PackageImport__packageImport", None)
        self.__packageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace33"):
                opp_val = getattr(old_value, "Namespace33", None)
                if opp_val == self:
                    setattr(old_value, "Namespace33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace33"):
                opp_val = getattr(value, "Namespace33", None)
                setattr(value, "Namespace33", self)

class fUML_Kernel_NamedElement(Element):

    def __init__(self, qualifiedName: str, name: str, visibility: str, ownedMember: "Kernel_Namespace" = None):
        self.qualifiedName = qualifiedName
        self.name = name
        self.visibility = visibility
        self.ownedMember = ownedMember
        
        pass
    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility


    @property
    def qualifiedName(self):
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def ownedMember(self):
        return self.__ownedMember

    @ownedMember.setter
    def ownedMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_NamedElement__ownedMember", None)
        self.__ownedMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace"):
                opp_val = getattr(old_value, "Namespace", None)
                if opp_val == self:
                    setattr(old_value, "Namespace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace"):
                opp_val = getattr(value, "Namespace", None)
                setattr(value, "Namespace", self)

class Kernel_Type:

    pass
class TypedElement:

    pass
class fUML_Kernel_ValueSpecification(TypedElement):

    pass
class BehavioralFeature:

    pass
class fUML_Kernel_Operation(BehavioralFeature):

    def __init__(self, query: bool, ordered: bool, unique: bool, lower: int, upper: int, ownedOperation: "Kernel_Class" = None, fUML_Kernel_Operation: set["Kernel_Operation"] = None, fUML_Kernel_Operation89: "Kernel_Type" = None):
        self.query = query
        self.ordered = ordered
        self.unique = unique
        self.lower = lower
        self.upper = upper
        self.ownedOperation = ownedOperation
        self.fUML_Kernel_Operation = fUML_Kernel_Operation if fUML_Kernel_Operation is not None else set()
        self.fUML_Kernel_Operation89 = fUML_Kernel_Operation89
        
        pass
    @property
    def ordered(self):
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered


    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper


    @property
    def query(self):
        return self.__query

    @query.setter
    def query(self, query: bool):
        self.__query = query


    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower


    @property
    def unique(self):
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique


    @property
    def ownedOperation(self):
        return self.__ownedOperation

    @ownedOperation.setter
    def ownedOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Operation__ownedOperation", None)
        self.__ownedOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class86"):
                opp_val = getattr(old_value, "Class86", None)
                if opp_val == self:
                    setattr(old_value, "Class86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class86"):
                opp_val = getattr(value, "Class86", None)
                setattr(value, "Class86", self)

    @property
    def fUML_Kernel_Operation(self):
        return self.__fUML_Kernel_Operation

    @fUML_Kernel_Operation.setter
    def fUML_Kernel_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Operation__fUML_Kernel_Operation", None)
        self.__fUML_Kernel_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_Operation"):
                    opp_val = getattr(item, "Kernel_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Operation"):
                    opp_val = getattr(item, "Kernel_Operation", None)
                    
                    setattr(item, "Kernel_Operation", self)
                    

    @property
    def fUML_Kernel_Operation89(self):
        return self.__fUML_Kernel_Operation89

    @fUML_Kernel_Operation89.setter
    def fUML_Kernel_Operation89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Operation__fUML_Kernel_Operation89", None)
        self.__fUML_Kernel_Operation89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel_Type90"):
                opp_val = getattr(old_value, "Kernel_Type90", None)
                if opp_val == self:
                    setattr(old_value, "Kernel_Type90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel_Type90"):
                opp_val = getattr(value, "Kernel_Type90", None)
                setattr(value, "Kernel_Type90", self)

class fUML_Communications_Reception(BehavioralFeature):

    pass
class Event:

    pass
class fUML_Communications_MessageEvent(Event):

    pass
class Communications_Signal:

    pass
class MessageEvent:

    pass
class fUML_Communications_SignalEvent(MessageEvent):

    pass
class Kernel_Property:

    pass
class PackageableElement:

    pass
class fUML_Kernel_Type(PackageableElement):

    pass
class fUML_Communications_Event(PackageableElement):

    pass
class Communications_Event:

    pass
class NamedElement:

    pass
class fUML_Kernel_Namespace(NamedElement):

    pass
class fUML_Kernel_PackageableElement(NamedElement):

    pass
class fUML_Kernel_TypedElement(NamedElement):

    pass
class fUML_Kernel_RedefinableElement(NamedElement):

    def __init__(self, leaf: bool, fUML_Kernel_RedefinableElement: set["Kernel_RedefinableElement"] = None, fUML_Kernel_RedefinableElement45: set["Kernel_Classifier"] = None):
        self.leaf = leaf
        self.fUML_Kernel_RedefinableElement = fUML_Kernel_RedefinableElement if fUML_Kernel_RedefinableElement is not None else set()
        self.fUML_Kernel_RedefinableElement45 = fUML_Kernel_RedefinableElement45 if fUML_Kernel_RedefinableElement45 is not None else set()
        
        pass
    @property
    def leaf(self):
        return self.__leaf

    @leaf.setter
    def leaf(self, leaf: bool):
        self.__leaf = leaf


    @property
    def fUML_Kernel_RedefinableElement(self):
        return self.__fUML_Kernel_RedefinableElement

    @fUML_Kernel_RedefinableElement.setter
    def fUML_Kernel_RedefinableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_RedefinableElement__fUML_Kernel_RedefinableElement", None)
        self.__fUML_Kernel_RedefinableElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_RedefinableElement"):
                    opp_val = getattr(item, "Kernel_RedefinableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_RedefinableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_RedefinableElement"):
                    opp_val = getattr(item, "Kernel_RedefinableElement", None)
                    
                    setattr(item, "Kernel_RedefinableElement", self)
                    

    @property
    def fUML_Kernel_RedefinableElement45(self):
        return self.__fUML_Kernel_RedefinableElement45

    @fUML_Kernel_RedefinableElement45.setter
    def fUML_Kernel_RedefinableElement45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_RedefinableElement__fUML_Kernel_RedefinableElement45", None)
        self.__fUML_Kernel_RedefinableElement45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_Classifier"):
                    opp_val = getattr(item, "Kernel_Classifier", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Classifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Classifier"):
                    opp_val = getattr(item, "Kernel_Classifier", None)
                    
                    setattr(item, "Kernel_Classifier", self)
                    

class fUML_Kernel_InstanceSpecification(NamedElement):

    pass
class fUML_Communications_Trigger(NamedElement):

    pass
class OpaqueBehavior:

    pass
class fUML_BasicBehaviors_FunctionBehavior(OpaqueBehavior):

    pass
class Kernel_Namespace:

    pass
class fUML_Kernel_Classifier(Kernel_Type, Kernel_Namespace):

    def __init__(self, abstract: bool, finalSpecialization: bool, specific: set["Kernel_Generalization"] = None, featuringClassifier: set["Kernel_Feature"] = None, fUML_Kernel_Classifier: set["Kernel_NamedElement"] = None, fUML_Kernel_Classifier51: set["Kernel_Property"] = None, fUML_Kernel_Classifier54: set["Kernel_Classifier"] = None, Namespace: "fUML_Kernel_NamedElement" = None, Namespace30: "fUML_Kernel_ElementImport" = None, Namespace33: "fUML_Kernel_PackageImport" = None, Kernel_Type90: "fUML_Kernel_Operation" = None, Type: "fUML_Kernel_Package" = None, Kernel_Type69: "fUML_Kernel_Association" = None, Kernel_Type: "fUML_Kernel_TypedElement" = None):
        self.abstract = abstract
        self.finalSpecialization = finalSpecialization
        self.specific = specific if specific is not None else set()
        self.featuringClassifier = featuringClassifier if featuringClassifier is not None else set()
        self.fUML_Kernel_Classifier = fUML_Kernel_Classifier if fUML_Kernel_Classifier is not None else set()
        self.fUML_Kernel_Classifier51 = fUML_Kernel_Classifier51 if fUML_Kernel_Classifier51 is not None else set()
        self.fUML_Kernel_Classifier54 = fUML_Kernel_Classifier54 if fUML_Kernel_Classifier54 is not None else set()
        
        pass
    @property
    def finalSpecialization(self):
        return self.__finalSpecialization

    @finalSpecialization.setter
    def finalSpecialization(self, finalSpecialization: bool):
        self.__finalSpecialization = finalSpecialization


    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract


    @property
    def specific(self):
        return self.__specific

    @specific.setter
    def specific(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Classifier__specific", None)
        self.__specific = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Generalization"):
                    opp_val = getattr(item, "Generalization", None)
                    
                    if opp_val == self:
                        setattr(item, "Generalization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Generalization"):
                    opp_val = getattr(item, "Generalization", None)
                    
                    setattr(item, "Generalization", self)
                    

    @property
    def fUML_Kernel_Classifier54(self):
        return self.__fUML_Kernel_Classifier54

    @fUML_Kernel_Classifier54.setter
    def fUML_Kernel_Classifier54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Classifier__fUML_Kernel_Classifier54", None)
        self.__fUML_Kernel_Classifier54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_Classifier55"):
                    opp_val = getattr(item, "Kernel_Classifier55", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Classifier55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Classifier55"):
                    opp_val = getattr(item, "Kernel_Classifier55", None)
                    
                    setattr(item, "Kernel_Classifier55", self)
                    

    @property
    def fUML_Kernel_Classifier(self):
        return self.__fUML_Kernel_Classifier

    @fUML_Kernel_Classifier.setter
    def fUML_Kernel_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Classifier__fUML_Kernel_Classifier", None)
        self.__fUML_Kernel_Classifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_NamedElement49"):
                    opp_val = getattr(item, "Kernel_NamedElement49", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_NamedElement49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_NamedElement49"):
                    opp_val = getattr(item, "Kernel_NamedElement49", None)
                    
                    setattr(item, "Kernel_NamedElement49", self)
                    

    @property
    def featuringClassifier(self):
        return self.__featuringClassifier

    @featuringClassifier.setter
    def featuringClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Classifier__featuringClassifier", None)
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
    def fUML_Kernel_Classifier51(self):
        return self.__fUML_Kernel_Classifier51

    @fUML_Kernel_Classifier51.setter
    def fUML_Kernel_Classifier51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Classifier__fUML_Kernel_Classifier51", None)
        self.__fUML_Kernel_Classifier51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_Property52"):
                    opp_val = getattr(item, "Kernel_Property52", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Property52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Property52"):
                    opp_val = getattr(item, "Kernel_Property52", None)
                    
                    setattr(item, "Kernel_Property52", self)
                    

class fUML_Kernel_Package(Kernel_Namespace, Kernel_PackageableElement):

    pass
class BasicBehaviors_Behavior:

    pass
class Classifier:

    pass
class fUML_Kernel_Association(Classifier):

    def __init__(self, derived: bool, fUML_Kernel_Association: set["Kernel_Type"] = None, association: set["Kernel_Property"] = None, fUML_Kernel_Association72: set["Kernel_Property"] = None, owningAssociation: set["Kernel_Property"] = None):
        self.derived = derived
        self.fUML_Kernel_Association = fUML_Kernel_Association if fUML_Kernel_Association is not None else set()
        self.association = association if association is not None else set()
        self.fUML_Kernel_Association72 = fUML_Kernel_Association72 if fUML_Kernel_Association72 is not None else set()
        self.owningAssociation = owningAssociation if owningAssociation is not None else set()
        
        pass
    @property
    def derived(self):
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived


    @property
    def fUML_Kernel_Association72(self):
        return self.__fUML_Kernel_Association72

    @fUML_Kernel_Association72.setter
    def fUML_Kernel_Association72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Association__fUML_Kernel_Association72", None)
        self.__fUML_Kernel_Association72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_Property73"):
                    opp_val = getattr(item, "Kernel_Property73", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Property73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Property73"):
                    opp_val = getattr(item, "Kernel_Property73", None)
                    
                    setattr(item, "Kernel_Property73", self)
                    

    @property
    def fUML_Kernel_Association(self):
        return self.__fUML_Kernel_Association

    @fUML_Kernel_Association.setter
    def fUML_Kernel_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Association__fUML_Kernel_Association", None)
        self.__fUML_Kernel_Association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_Type69"):
                    opp_val = getattr(item, "Kernel_Type69", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Type69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Type69"):
                    opp_val = getattr(item, "Kernel_Type69", None)
                    
                    setattr(item, "Kernel_Type69", self)
                    

    @property
    def association(self):
        return self.__association

    @association.setter
    def association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Association__association", None)
        self.__association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    if opp_val == self:
                        setattr(item, "Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    setattr(item, "Property", self)
                    

    @property
    def owningAssociation(self):
        return self.__owningAssociation

    @owningAssociation.setter
    def owningAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Association__owningAssociation", None)
        self.__owningAssociation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property75"):
                    opp_val = getattr(item, "Property75", None)
                    
                    if opp_val == self:
                        setattr(item, "Property75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property75"):
                    opp_val = getattr(item, "Property75", None)
                    
                    setattr(item, "Property75", self)
                    

class fUML_Communications_Signal(Classifier):

    pass
class fUML_Kernel_DataType(Classifier):

    pass
class fUML_BasicBehaviors_BehavioredClassifier(Classifier):

    pass
class BasicBehaviors_BehavioredClassifier:

    pass
class Kernel_Parameter:

    pass
class Kernel_BehavioralFeature:

    pass
class Class:

    pass
class fUML_BasicBehaviors_Behavior(Class):

    def __init__(self, reentrant: bool, method: "Kernel_BehavioralFeature" = None, fUML_BasicBehaviors_Behavior: set["Kernel_Parameter"] = None, fUML_BasicBehaviors_Behavior3: "BasicBehaviors_BehavioredClassifier" = None):
        self.reentrant = reentrant
        self.method = method
        self.fUML_BasicBehaviors_Behavior = fUML_BasicBehaviors_Behavior if fUML_BasicBehaviors_Behavior is not None else set()
        self.fUML_BasicBehaviors_Behavior3 = fUML_BasicBehaviors_Behavior3
        
        pass
    @property
    def reentrant(self):
        return self.__reentrant

    @reentrant.setter
    def reentrant(self, reentrant: bool):
        self.__reentrant = reentrant


    @property
    def fUML_BasicBehaviors_Behavior3(self):
        return self.__fUML_BasicBehaviors_Behavior3

    @fUML_BasicBehaviors_Behavior3.setter
    def fUML_BasicBehaviors_Behavior3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_BasicBehaviors_Behavior__fUML_BasicBehaviors_Behavior3", None)
        self.__fUML_BasicBehaviors_Behavior3 = value
        
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
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_BasicBehaviors_Behavior__method", None)
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

    @property
    def fUML_BasicBehaviors_Behavior(self):
        return self.__fUML_BasicBehaviors_Behavior

    @fUML_BasicBehaviors_Behavior.setter
    def fUML_BasicBehaviors_Behavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_BasicBehaviors_Behavior__fUML_BasicBehaviors_Behavior", None)
        self.__fUML_BasicBehaviors_Behavior = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_Parameter"):
                    opp_val = getattr(item, "Kernel_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Parameter"):
                    opp_val = getattr(item, "Kernel_Parameter", None)
                    
                    setattr(item, "Kernel_Parameter", self)
                    

class Behavior:

    pass
class fUML_IntermediateActivities_Activity(Behavior):

    def __init__(self, readOnly: bool, activity: set["IntermediateActivities_ActivityNode"] = None, activity123: set["IntermediateActivities_ActivityEdge"] = None):
        self.readOnly = readOnly
        self.activity = activity if activity is not None else set()
        self.activity123 = activity123 if activity123 is not None else set()
        
        pass
    @property
    def readOnly(self):
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly


    @property
    def activity123(self):
        return self.__activity123

    @activity123.setter
    def activity123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_IntermediateActivities_Activity__activity123", None)
        self.__activity123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge"):
                    opp_val = getattr(item, "ActivityEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge"):
                    opp_val = getattr(item, "ActivityEdge", None)
                    
                    setattr(item, "ActivityEdge", self)
                    

    @property
    def activity(self):
        return self.__activity

    @activity.setter
    def activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_IntermediateActivities_Activity__activity", None)
        self.__activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityNode121"):
                    opp_val = getattr(item, "ActivityNode121", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityNode121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityNode121"):
                    opp_val = getattr(item, "ActivityNode121", None)
                    
                    setattr(item, "ActivityNode121", self)
                    

class fUML_BasicBehaviors_OpaqueBehavior(Behavior):

    def __init__(self, body: str, language: str):
        self.body = body
        self.language = language
        
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


class fUML_Kernel_LiteralBoolean(LiteralSpecification):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

