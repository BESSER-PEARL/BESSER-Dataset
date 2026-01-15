from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VisibilityKind(Enum):
    public = "public"
    private = "private"
    protected = "protected"
    package = "package"
class AggregationKind(Enum):
    none = "none"
    shared = "shared"
    composite = "composite"
class ExpansionKind(Enum):
    parallel = "parallel"
    iterative = "iterative"
    stream = "stream"
class CallConcurrencyKind(Enum):
    sequential = "sequential"
class ParameterDirectionKind(Enum):
    out = "out"
    return = "return"
    in = "in"
    inout = "inout"


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
        
    @property
    def synchronous(self) -> bool:
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
                if hasattr(item, "BasicActions_OutputPin365"):
                    opp_val = getattr(item, "BasicActions_OutputPin365", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin365", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin365"):
                    opp_val = getattr(item, "BasicActions_OutputPin365", None)
                    
                    setattr(item, "BasicActions_OutputPin365", self)
                    

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

    def __init__(self, locallyReentrant: bool, fUML_BasicActions_Action: set["BasicActions_OutputPin"] = None, fUML_BasicActions_Action359: "Kernel_Classifier" = None, fUML_BasicActions_Action362: set["BasicActions_InputPin"] = None):
        self.locallyReentrant = locallyReentrant
        self.fUML_BasicActions_Action = fUML_BasicActions_Action if fUML_BasicActions_Action is not None else set()
        self.fUML_BasicActions_Action359 = fUML_BasicActions_Action359
        self.fUML_BasicActions_Action362 = fUML_BasicActions_Action362 if fUML_BasicActions_Action362 is not None else set()
        
    @property
    def locallyReentrant(self) -> bool:
        return self.__locallyReentrant

    @locallyReentrant.setter
    def locallyReentrant(self, locallyReentrant: bool):
        self.__locallyReentrant = locallyReentrant

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
                if hasattr(item, "BasicActions_OutputPin357"):
                    opp_val = getattr(item, "BasicActions_OutputPin357", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin357", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin357"):
                    opp_val = getattr(item, "BasicActions_OutputPin357", None)
                    
                    setattr(item, "BasicActions_OutputPin357", self)
                    

    @property
    def fUML_BasicActions_Action362(self):
        return self.__fUML_BasicActions_Action362

    @fUML_BasicActions_Action362.setter
    def fUML_BasicActions_Action362(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_BasicActions_Action__fUML_BasicActions_Action362", None)
        self.__fUML_BasicActions_Action362 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_InputPin363"):
                    opp_val = getattr(item, "BasicActions_InputPin363", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_InputPin363", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_InputPin363"):
                    opp_val = getattr(item, "BasicActions_InputPin363", None)
                    
                    setattr(item, "BasicActions_InputPin363", self)
                    

    @property
    def fUML_BasicActions_Action359(self):
        return self.__fUML_BasicActions_Action359

    @fUML_BasicActions_Action359.setter
    def fUML_BasicActions_Action359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_BasicActions_Action__fUML_BasicActions_Action359", None)
        self.__fUML_BasicActions_Action359 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel_Classifier360"):
                opp_val = getattr(old_value, "Kernel_Classifier360", None)
                if opp_val == self:
                    setattr(old_value, "Kernel_Classifier360", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel_Classifier360"):
                opp_val = getattr(value, "Kernel_Classifier360", None)
                setattr(value, "Kernel_Classifier360", self)

class Communications_Trigger:

    pass
class WriteLinkAction:

    pass
class fUML_IntermediateActions_CreateLinkAction(WriteLinkAction):

    pass
class CallAction:

    pass
class fUML_BasicActions_CallBehaviorAction(CallAction):

    pass
class fUML_BasicActions_CallOperationAction(CallAction):

    pass
class fUML_CompleteActions_StartObjectBehaviorAction(CallAction):

    pass
class fUML_IntermediateActions_DestroyLinkAction(WriteLinkAction):

    pass
class WriteStructuralFeatureAction:

    pass
class fUML_IntermediateActions_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    def __init__(self, replaceAll: bool, fUML_IntermediateActions_AddStructuralFeatureValueAction: "BasicActions_InputPin" = None):
        self.replaceAll = replaceAll
        self.fUML_IntermediateActions_AddStructuralFeatureValueAction = fUML_IntermediateActions_AddStructuralFeatureValueAction
        
    @property
    def replaceAll(self) -> bool:
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
            if hasattr(old_value, "BasicActions_InputPin318"):
                opp_val = getattr(old_value, "BasicActions_InputPin318", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin318"):
                opp_val = getattr(value, "BasicActions_InputPin318", None)
                setattr(value, "BasicActions_InputPin318", self)

class fUML_IntermediateActions_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    def __init__(self, removeDuplicates: bool, fUML_IntermediateActions_RemoveStructuralFeatureValueAction: "BasicActions_InputPin" = None):
        self.removeDuplicates = removeDuplicates
        self.fUML_IntermediateActions_RemoveStructuralFeatureValueAction = fUML_IntermediateActions_RemoveStructuralFeatureValueAction
        
    @property
    def removeDuplicates(self) -> bool:
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
            if hasattr(old_value, "BasicActions_InputPin293"):
                opp_val = getattr(old_value, "BasicActions_InputPin293", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin293"):
                opp_val = getattr(value, "BasicActions_InputPin293", None)
                setattr(value, "BasicActions_InputPin293", self)

class LinkEndData:

    pass
class fUML_IntermediateActions_LinkEndDestructionData(LinkEndData):

    def __init__(self, destroyDuplicates: bool, fUML_IntermediateActions_LinkEndDestructionData: "BasicActions_InputPin" = None):
        self.destroyDuplicates = destroyDuplicates
        self.fUML_IntermediateActions_LinkEndDestructionData = fUML_IntermediateActions_LinkEndDestructionData
        
    @property
    def destroyDuplicates(self) -> bool:
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
            if hasattr(old_value, "BasicActions_InputPin303"):
                opp_val = getattr(old_value, "BasicActions_InputPin303", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin303", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin303"):
                opp_val = getattr(value, "BasicActions_InputPin303", None)
                setattr(value, "BasicActions_InputPin303", self)

class fUML_IntermediateActions_LinkEndCreationData(LinkEndData):

    def __init__(self, replaceAll: bool, fUML_IntermediateActions_LinkEndCreationData: "BasicActions_InputPin" = None):
        self.replaceAll = replaceAll
        self.fUML_IntermediateActions_LinkEndCreationData = fUML_IntermediateActions_LinkEndCreationData
        
    @property
    def replaceAll(self) -> bool:
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
            if hasattr(old_value, "BasicActions_InputPin301"):
                opp_val = getattr(old_value, "BasicActions_InputPin301", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin301"):
                opp_val = getattr(value, "BasicActions_InputPin301", None)
                setattr(value, "BasicActions_InputPin301", self)

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
class fUML_CompleteActions_ReadExtentAction(Action):

    pass
class fUML_IntermediateActions_StructuralFeatureAction(Action):

    pass
class fUML_IntermediateActions_TestIdentityAction(Action):

    pass
class fUML_CompleteActions_AcceptEventAction(Action):

    def __init__(self, unmarshall: bool, fUML_CompleteActions_AcceptEventAction355: set["Communications_Trigger"] = None, fUML_CompleteActions_AcceptEventAction: set["BasicActions_OutputPin"] = None):
        self.unmarshall = unmarshall
        self.fUML_CompleteActions_AcceptEventAction355 = fUML_CompleteActions_AcceptEventAction355 if fUML_CompleteActions_AcceptEventAction355 is not None else set()
        self.fUML_CompleteActions_AcceptEventAction = fUML_CompleteActions_AcceptEventAction if fUML_CompleteActions_AcceptEventAction is not None else set()
        
    @property
    def unmarshall(self) -> bool:
        return self.__unmarshall

    @unmarshall.setter
    def unmarshall(self, unmarshall: bool):
        self.__unmarshall = unmarshall

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
                if hasattr(item, "BasicActions_OutputPin353"):
                    opp_val = getattr(item, "BasicActions_OutputPin353", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin353", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin353"):
                    opp_val = getattr(item, "BasicActions_OutputPin353", None)
                    
                    setattr(item, "BasicActions_OutputPin353", self)
                    

    @property
    def fUML_CompleteActions_AcceptEventAction355(self):
        return self.__fUML_CompleteActions_AcceptEventAction355

    @fUML_CompleteActions_AcceptEventAction355.setter
    def fUML_CompleteActions_AcceptEventAction355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteActions_AcceptEventAction__fUML_CompleteActions_AcceptEventAction355", None)
        self.__fUML_CompleteActions_AcceptEventAction355 = value if value is not None else set()
        
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
                    

class fUML_BasicActions_InvocationAction(Action):

    pass
class fUML_IntermediateActions_ClearAssociationAction(Action):

    pass
class fUML_IntermediateActions_ValueSpecificationAction(Action):

    pass
class fUML_IntermediateActions_ReadSelfAction(Action):

    pass
class fUML_CompleteActions_ReadIsClassifiedObjectAction(Action):

    def __init__(self, direct: bool, fUML_CompleteActions_ReadIsClassifiedObjectAction: "Kernel_Classifier" = None, fUML_CompleteActions_ReadIsClassifiedObjectAction339: "BasicActions_OutputPin" = None, fUML_CompleteActions_ReadIsClassifiedObjectAction342: "BasicActions_InputPin" = None):
        self.direct = direct
        self.fUML_CompleteActions_ReadIsClassifiedObjectAction = fUML_CompleteActions_ReadIsClassifiedObjectAction
        self.fUML_CompleteActions_ReadIsClassifiedObjectAction339 = fUML_CompleteActions_ReadIsClassifiedObjectAction339
        self.fUML_CompleteActions_ReadIsClassifiedObjectAction342 = fUML_CompleteActions_ReadIsClassifiedObjectAction342
        
    @property
    def direct(self) -> bool:
        return self.__direct

    @direct.setter
    def direct(self, direct: bool):
        self.__direct = direct

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
            if hasattr(old_value, "Kernel_Classifier337"):
                opp_val = getattr(old_value, "Kernel_Classifier337", None)
                if opp_val == self:
                    setattr(old_value, "Kernel_Classifier337", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel_Classifier337"):
                opp_val = getattr(value, "Kernel_Classifier337", None)
                setattr(value, "Kernel_Classifier337", self)

    @property
    def fUML_CompleteActions_ReadIsClassifiedObjectAction342(self):
        return self.__fUML_CompleteActions_ReadIsClassifiedObjectAction342

    @fUML_CompleteActions_ReadIsClassifiedObjectAction342.setter
    def fUML_CompleteActions_ReadIsClassifiedObjectAction342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteActions_ReadIsClassifiedObjectAction__fUML_CompleteActions_ReadIsClassifiedObjectAction342", None)
        self.__fUML_CompleteActions_ReadIsClassifiedObjectAction342 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin343"):
                opp_val = getattr(old_value, "BasicActions_InputPin343", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin343", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin343"):
                opp_val = getattr(value, "BasicActions_InputPin343", None)
                setattr(value, "BasicActions_InputPin343", self)

    @property
    def fUML_CompleteActions_ReadIsClassifiedObjectAction339(self):
        return self.__fUML_CompleteActions_ReadIsClassifiedObjectAction339

    @fUML_CompleteActions_ReadIsClassifiedObjectAction339.setter
    def fUML_CompleteActions_ReadIsClassifiedObjectAction339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteActions_ReadIsClassifiedObjectAction__fUML_CompleteActions_ReadIsClassifiedObjectAction339", None)
        self.__fUML_CompleteActions_ReadIsClassifiedObjectAction339 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_OutputPin340"):
                opp_val = getattr(old_value, "BasicActions_OutputPin340", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_OutputPin340", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_OutputPin340"):
                opp_val = getattr(value, "BasicActions_OutputPin340", None)
                setattr(value, "BasicActions_OutputPin340", self)

class fUML_CompleteActions_ReclassifyObjectAction(Action):

    def __init__(self, replaceAll: bool, fUML_CompleteActions_ReclassifyObjectAction: set["Kernel_Classifier"] = None, fUML_CompleteActions_ReclassifyObjectAction347: "BasicActions_InputPin" = None, fUML_CompleteActions_ReclassifyObjectAction350: set["Kernel_Classifier"] = None):
        self.replaceAll = replaceAll
        self.fUML_CompleteActions_ReclassifyObjectAction = fUML_CompleteActions_ReclassifyObjectAction if fUML_CompleteActions_ReclassifyObjectAction is not None else set()
        self.fUML_CompleteActions_ReclassifyObjectAction347 = fUML_CompleteActions_ReclassifyObjectAction347
        self.fUML_CompleteActions_ReclassifyObjectAction350 = fUML_CompleteActions_ReclassifyObjectAction350 if fUML_CompleteActions_ReclassifyObjectAction350 is not None else set()
        
    @property
    def replaceAll(self) -> bool:
        return self.__replaceAll

    @replaceAll.setter
    def replaceAll(self, replaceAll: bool):
        self.__replaceAll = replaceAll

    @property
    def fUML_CompleteActions_ReclassifyObjectAction347(self):
        return self.__fUML_CompleteActions_ReclassifyObjectAction347

    @fUML_CompleteActions_ReclassifyObjectAction347.setter
    def fUML_CompleteActions_ReclassifyObjectAction347(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteActions_ReclassifyObjectAction__fUML_CompleteActions_ReclassifyObjectAction347", None)
        self.__fUML_CompleteActions_ReclassifyObjectAction347 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin348"):
                opp_val = getattr(old_value, "BasicActions_InputPin348", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin348", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin348"):
                opp_val = getattr(value, "BasicActions_InputPin348", None)
                setattr(value, "BasicActions_InputPin348", self)

    @property
    def fUML_CompleteActions_ReclassifyObjectAction350(self):
        return self.__fUML_CompleteActions_ReclassifyObjectAction350

    @fUML_CompleteActions_ReclassifyObjectAction350.setter
    def fUML_CompleteActions_ReclassifyObjectAction350(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteActions_ReclassifyObjectAction__fUML_CompleteActions_ReclassifyObjectAction350", None)
        self.__fUML_CompleteActions_ReclassifyObjectAction350 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_Classifier351"):
                    opp_val = getattr(item, "Kernel_Classifier351", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Classifier351", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Classifier351"):
                    opp_val = getattr(item, "Kernel_Classifier351", None)
                    
                    setattr(item, "Kernel_Classifier351", self)
                    

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
                if hasattr(item, "Kernel_Classifier345"):
                    opp_val = getattr(item, "Kernel_Classifier345", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Classifier345", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Classifier345"):
                    opp_val = getattr(item, "Kernel_Classifier345", None)
                    
                    setattr(item, "Kernel_Classifier345", self)
                    

class fUML_IntermediateActions_CreateObjectAction(Action):

    pass
class fUML_IntermediateActions_LinkAction(Action):

    pass
class fUML_IntermediateActions_DestroyObjectAction(Action):

    def __init__(self, destroyLinks: bool, destroyOwnedObjects: bool, fUML_IntermediateActions_DestroyObjectAction: "BasicActions_InputPin" = None):
        self.destroyLinks = destroyLinks
        self.destroyOwnedObjects = destroyOwnedObjects
        self.fUML_IntermediateActions_DestroyObjectAction = fUML_IntermediateActions_DestroyObjectAction
        
    @property
    def destroyOwnedObjects(self) -> bool:
        return self.__destroyOwnedObjects

    @destroyOwnedObjects.setter
    def destroyOwnedObjects(self, destroyOwnedObjects: bool):
        self.__destroyOwnedObjects = destroyOwnedObjects

    @property
    def destroyLinks(self) -> bool:
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
            if hasattr(old_value, "BasicActions_InputPin316"):
                opp_val = getattr(old_value, "BasicActions_InputPin316", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin316"):
                opp_val = getattr(value, "BasicActions_InputPin316", None)
                setattr(value, "BasicActions_InputPin316", self)

class fUML_CompleteActions_ReduceAction(Action):

    def __init__(self, ordered: bool, fUML_CompleteActions_ReduceAction: "BasicBehaviors_Behavior" = None, fUML_CompleteActions_ReduceAction326: "BasicActions_OutputPin" = None, fUML_CompleteActions_ReduceAction329: "BasicActions_InputPin" = None):
        self.ordered = ordered
        self.fUML_CompleteActions_ReduceAction = fUML_CompleteActions_ReduceAction
        self.fUML_CompleteActions_ReduceAction326 = fUML_CompleteActions_ReduceAction326
        self.fUML_CompleteActions_ReduceAction329 = fUML_CompleteActions_ReduceAction329
        
    @property
    def ordered(self) -> bool:
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered

    @property
    def fUML_CompleteActions_ReduceAction326(self):
        return self.__fUML_CompleteActions_ReduceAction326

    @fUML_CompleteActions_ReduceAction326.setter
    def fUML_CompleteActions_ReduceAction326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteActions_ReduceAction__fUML_CompleteActions_ReduceAction326", None)
        self.__fUML_CompleteActions_ReduceAction326 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_OutputPin327"):
                opp_val = getattr(old_value, "BasicActions_OutputPin327", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_OutputPin327", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_OutputPin327"):
                opp_val = getattr(value, "BasicActions_OutputPin327", None)
                setattr(value, "BasicActions_OutputPin327", self)

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
            if hasattr(old_value, "BasicBehaviors_Behavior324"):
                opp_val = getattr(old_value, "BasicBehaviors_Behavior324", None)
                if opp_val == self:
                    setattr(old_value, "BasicBehaviors_Behavior324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicBehaviors_Behavior324"):
                opp_val = getattr(value, "BasicBehaviors_Behavior324", None)
                setattr(value, "BasicBehaviors_Behavior324", self)

    @property
    def fUML_CompleteActions_ReduceAction329(self):
        return self.__fUML_CompleteActions_ReduceAction329

    @fUML_CompleteActions_ReduceAction329.setter
    def fUML_CompleteActions_ReduceAction329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteActions_ReduceAction__fUML_CompleteActions_ReduceAction329", None)
        self.__fUML_CompleteActions_ReduceAction329 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin330"):
                opp_val = getattr(old_value, "BasicActions_InputPin330", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin330", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin330"):
                opp_val = getattr(value, "BasicActions_InputPin330", None)
                setattr(value, "BasicActions_InputPin330", self)

class fUML_CompleteActions_StartClassifierBehaviorAction(Action):

    pass
class fUML_CompleteStructuredActivities_StructuredActivityNode(Action):

    def __init__(self, mustIsolate: bool, Activities238: set["IntermediateActivities_ActivityNode"] = None, Activities241: set["IntermediateActivities_ActivityEdge"] = None, fUML_CompleteStructuredActivities_StructuredActivityNode: set["BasicActions_OutputPin"] = None, fUML_CompleteStructuredActivities_StructuredActivityNode246: set["BasicActions_InputPin"] = None):
        self.mustIsolate = mustIsolate
        self.Activities238 = Activities238 if Activities238 is not None else set()
        self.Activities241 = Activities241 if Activities241 is not None else set()
        self.fUML_CompleteStructuredActivities_StructuredActivityNode = fUML_CompleteStructuredActivities_StructuredActivityNode if fUML_CompleteStructuredActivities_StructuredActivityNode is not None else set()
        self.fUML_CompleteStructuredActivities_StructuredActivityNode246 = fUML_CompleteStructuredActivities_StructuredActivityNode246 if fUML_CompleteStructuredActivities_StructuredActivityNode246 is not None else set()
        
    @property
    def mustIsolate(self) -> bool:
        return self.__mustIsolate

    @mustIsolate.setter
    def mustIsolate(self, mustIsolate: bool):
        self.__mustIsolate = mustIsolate

    @property
    def Activities241(self):
        return self.__Activities241

    @Activities241.setter
    def Activities241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_StructuredActivityNode__Activities241", None)
        self.__Activities241 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax242"):
                    opp_val = getattr(item, "Syntax242", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax242", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax242"):
                    opp_val = getattr(item, "Syntax242", None)
                    
                    setattr(item, "Syntax242", self)
                    

    @property
    def Activities238(self):
        return self.__Activities238

    @Activities238.setter
    def Activities238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_StructuredActivityNode__Activities238", None)
        self.__Activities238 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax239"):
                    opp_val = getattr(item, "Syntax239", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax239", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax239"):
                    opp_val = getattr(item, "Syntax239", None)
                    
                    setattr(item, "Syntax239", self)
                    

    @property
    def fUML_CompleteStructuredActivities_StructuredActivityNode246(self):
        return self.__fUML_CompleteStructuredActivities_StructuredActivityNode246

    @fUML_CompleteStructuredActivities_StructuredActivityNode246.setter
    def fUML_CompleteStructuredActivities_StructuredActivityNode246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_StructuredActivityNode__fUML_CompleteStructuredActivities_StructuredActivityNode246", None)
        self.__fUML_CompleteStructuredActivities_StructuredActivityNode246 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_InputPin247"):
                    opp_val = getattr(item, "BasicActions_InputPin247", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_InputPin247", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_InputPin247"):
                    opp_val = getattr(item, "BasicActions_InputPin247", None)
                    
                    setattr(item, "BasicActions_InputPin247", self)
                    

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
                if hasattr(item, "BasicActions_OutputPin244"):
                    opp_val = getattr(item, "BasicActions_OutputPin244", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin244", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin244"):
                    opp_val = getattr(item, "BasicActions_OutputPin244", None)
                    
                    setattr(item, "BasicActions_OutputPin244", self)
                    

class CompleteStructuredActivities_ExecutableNode:

    pass
class CompleteStructuredActivities_Clause:

    pass
class BasicActions_InputPin:

    pass
class BasicActions_OutputPin:

    pass
class StructuredActivityNode:

    pass
class fUML_ExtraStructuredActivities_ExpansionRegion(StructuredActivityNode):

    def __init__(self, mode: str, Activities255: set["ExtraStructuredActivities_ExpansionNode"] = None, Activities258: set["ExtraStructuredActivities_ExpansionNode"] = None):
        self.mode = mode
        self.Activities255 = Activities255 if Activities255 is not None else set()
        self.Activities258 = Activities258 if Activities258 is not None else set()
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def Activities255(self):
        return self.__Activities255

    @Activities255.setter
    def Activities255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_ExtraStructuredActivities_ExpansionRegion__Activities255", None)
        self.__Activities255 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax256"):
                    opp_val = getattr(item, "Syntax256", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax256", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax256"):
                    opp_val = getattr(item, "Syntax256", None)
                    
                    setattr(item, "Syntax256", self)
                    

    @property
    def Activities258(self):
        return self.__Activities258

    @Activities258.setter
    def Activities258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_ExtraStructuredActivities_ExpansionRegion__Activities258", None)
        self.__Activities258 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax259"):
                    opp_val = getattr(item, "Syntax259", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax259", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax259"):
                    opp_val = getattr(item, "Syntax259", None)
                    
                    setattr(item, "Syntax259", self)
                    

class fUML_CompleteStructuredActivities_ConditionalNode(StructuredActivityNode):

    def __init__(self, assured: bool, determinate: bool, fUML_CompleteStructuredActivities_ConditionalNode: set["CompleteStructuredActivities_Clause"] = None, fUML_CompleteStructuredActivities_ConditionalNode235: set["BasicActions_OutputPin"] = None):
        self.assured = assured
        self.determinate = determinate
        self.fUML_CompleteStructuredActivities_ConditionalNode = fUML_CompleteStructuredActivities_ConditionalNode if fUML_CompleteStructuredActivities_ConditionalNode is not None else set()
        self.fUML_CompleteStructuredActivities_ConditionalNode235 = fUML_CompleteStructuredActivities_ConditionalNode235 if fUML_CompleteStructuredActivities_ConditionalNode235 is not None else set()
        
    @property
    def determinate(self) -> bool:
        return self.__determinate

    @determinate.setter
    def determinate(self, determinate: bool):
        self.__determinate = determinate

    @property
    def assured(self) -> bool:
        return self.__assured

    @assured.setter
    def assured(self, assured: bool):
        self.__assured = assured

    @property
    def fUML_CompleteStructuredActivities_ConditionalNode235(self):
        return self.__fUML_CompleteStructuredActivities_ConditionalNode235

    @fUML_CompleteStructuredActivities_ConditionalNode235.setter
    def fUML_CompleteStructuredActivities_ConditionalNode235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_ConditionalNode__fUML_CompleteStructuredActivities_ConditionalNode235", None)
        self.__fUML_CompleteStructuredActivities_ConditionalNode235 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin236"):
                    opp_val = getattr(item, "BasicActions_OutputPin236", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin236", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin236"):
                    opp_val = getattr(item, "BasicActions_OutputPin236", None)
                    
                    setattr(item, "BasicActions_OutputPin236", self)
                    

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

    def __init__(self, testedFirst: bool, fUML_CompleteStructuredActivities_LoopNode: "BasicActions_OutputPin" = None, fUML_CompleteStructuredActivities_LoopNode200: set["BasicActions_OutputPin"] = None, fUML_CompleteStructuredActivities_LoopNode203: set["BasicActions_InputPin"] = None, fUML_CompleteStructuredActivities_LoopNode205: set["CompleteStructuredActivities_ExecutableNode"] = None, fUML_CompleteStructuredActivities_LoopNode208: set["BasicActions_OutputPin"] = None, fUML_CompleteStructuredActivities_LoopNode211: set["BasicActions_OutputPin"] = None, fUML_CompleteStructuredActivities_LoopNode214: set["CompleteStructuredActivities_ExecutableNode"] = None, fUML_CompleteStructuredActivities_LoopNode198: set["CompleteStructuredActivities_ExecutableNode"] = None):
        self.testedFirst = testedFirst
        self.fUML_CompleteStructuredActivities_LoopNode = fUML_CompleteStructuredActivities_LoopNode
        self.fUML_CompleteStructuredActivities_LoopNode200 = fUML_CompleteStructuredActivities_LoopNode200 if fUML_CompleteStructuredActivities_LoopNode200 is not None else set()
        self.fUML_CompleteStructuredActivities_LoopNode203 = fUML_CompleteStructuredActivities_LoopNode203 if fUML_CompleteStructuredActivities_LoopNode203 is not None else set()
        self.fUML_CompleteStructuredActivities_LoopNode205 = fUML_CompleteStructuredActivities_LoopNode205 if fUML_CompleteStructuredActivities_LoopNode205 is not None else set()
        self.fUML_CompleteStructuredActivities_LoopNode208 = fUML_CompleteStructuredActivities_LoopNode208 if fUML_CompleteStructuredActivities_LoopNode208 is not None else set()
        self.fUML_CompleteStructuredActivities_LoopNode211 = fUML_CompleteStructuredActivities_LoopNode211 if fUML_CompleteStructuredActivities_LoopNode211 is not None else set()
        self.fUML_CompleteStructuredActivities_LoopNode214 = fUML_CompleteStructuredActivities_LoopNode214 if fUML_CompleteStructuredActivities_LoopNode214 is not None else set()
        self.fUML_CompleteStructuredActivities_LoopNode198 = fUML_CompleteStructuredActivities_LoopNode198 if fUML_CompleteStructuredActivities_LoopNode198 is not None else set()
        
    @property
    def testedFirst(self) -> bool:
        return self.__testedFirst

    @testedFirst.setter
    def testedFirst(self, testedFirst: bool):
        self.__testedFirst = testedFirst

    @property
    def fUML_CompleteStructuredActivities_LoopNode205(self):
        return self.__fUML_CompleteStructuredActivities_LoopNode205

    @fUML_CompleteStructuredActivities_LoopNode205.setter
    def fUML_CompleteStructuredActivities_LoopNode205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_LoopNode__fUML_CompleteStructuredActivities_LoopNode205", None)
        self.__fUML_CompleteStructuredActivities_LoopNode205 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode206"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode206", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteStructuredActivities_ExecutableNode206", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode206"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode206", None)
                    
                    setattr(item, "CompleteStructuredActivities_ExecutableNode206", self)
                    

    @property
    def fUML_CompleteStructuredActivities_LoopNode200(self):
        return self.__fUML_CompleteStructuredActivities_LoopNode200

    @fUML_CompleteStructuredActivities_LoopNode200.setter
    def fUML_CompleteStructuredActivities_LoopNode200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_LoopNode__fUML_CompleteStructuredActivities_LoopNode200", None)
        self.__fUML_CompleteStructuredActivities_LoopNode200 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin201"):
                    opp_val = getattr(item, "BasicActions_OutputPin201", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin201", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin201"):
                    opp_val = getattr(item, "BasicActions_OutputPin201", None)
                    
                    setattr(item, "BasicActions_OutputPin201", self)
                    

    @property
    def fUML_CompleteStructuredActivities_LoopNode198(self):
        return self.__fUML_CompleteStructuredActivities_LoopNode198

    @fUML_CompleteStructuredActivities_LoopNode198.setter
    def fUML_CompleteStructuredActivities_LoopNode198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_LoopNode__fUML_CompleteStructuredActivities_LoopNode198", None)
        self.__fUML_CompleteStructuredActivities_LoopNode198 = value if value is not None else set()
        
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
    def fUML_CompleteStructuredActivities_LoopNode208(self):
        return self.__fUML_CompleteStructuredActivities_LoopNode208

    @fUML_CompleteStructuredActivities_LoopNode208.setter
    def fUML_CompleteStructuredActivities_LoopNode208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_LoopNode__fUML_CompleteStructuredActivities_LoopNode208", None)
        self.__fUML_CompleteStructuredActivities_LoopNode208 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin209"):
                    opp_val = getattr(item, "BasicActions_OutputPin209", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin209", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin209"):
                    opp_val = getattr(item, "BasicActions_OutputPin209", None)
                    
                    setattr(item, "BasicActions_OutputPin209", self)
                    

    @property
    def fUML_CompleteStructuredActivities_LoopNode214(self):
        return self.__fUML_CompleteStructuredActivities_LoopNode214

    @fUML_CompleteStructuredActivities_LoopNode214.setter
    def fUML_CompleteStructuredActivities_LoopNode214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_LoopNode__fUML_CompleteStructuredActivities_LoopNode214", None)
        self.__fUML_CompleteStructuredActivities_LoopNode214 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode215"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode215", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteStructuredActivities_ExecutableNode215", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode215"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode215", None)
                    
                    setattr(item, "CompleteStructuredActivities_ExecutableNode215", self)
                    

    @property
    def fUML_CompleteStructuredActivities_LoopNode203(self):
        return self.__fUML_CompleteStructuredActivities_LoopNode203

    @fUML_CompleteStructuredActivities_LoopNode203.setter
    def fUML_CompleteStructuredActivities_LoopNode203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_LoopNode__fUML_CompleteStructuredActivities_LoopNode203", None)
        self.__fUML_CompleteStructuredActivities_LoopNode203 = value if value is not None else set()
        
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
    def fUML_CompleteStructuredActivities_LoopNode211(self):
        return self.__fUML_CompleteStructuredActivities_LoopNode211

    @fUML_CompleteStructuredActivities_LoopNode211.setter
    def fUML_CompleteStructuredActivities_LoopNode211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_CompleteStructuredActivities_LoopNode__fUML_CompleteStructuredActivities_LoopNode211", None)
        self.__fUML_CompleteStructuredActivities_LoopNode211 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin212"):
                    opp_val = getattr(item, "BasicActions_OutputPin212", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin212", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin212"):
                    opp_val = getattr(item, "BasicActions_OutputPin212", None)
                    
                    setattr(item, "BasicActions_OutputPin212", self)
                    

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
class fUML_IntermediateActivities_DecisionNode(ControlNode):

    pass
class fUML_IntermediateActivities_InitialNode(ControlNode):

    pass
class fUML_IntermediateActivities_FinalNode(ControlNode):

    pass
class fUML_IntermediateActivities_ForkNode(ControlNode):

    pass
class fUML_IntermediateActivities_MergeNode(ControlNode):

    pass
class IntermediateActivities_ActivityEdge:

    pass
class CompleteStructuredActivities_StructuredActivityNode:

    pass
class IntermediateActivities_ActivityNode:

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
class Kernel_InstanceSpecification:

    pass
class BehavioredClassifier:

    pass
class fUML_Kernel_Class(BehavioredClassifier):

    def __init__(self, active: bool, Classes148: set["Kernel_Property"] = None, Classes151: set["Kernel_Operation"] = None, fUML_Kernel_Class155: set["Communications_Reception"] = None, fUML_Kernel_Class157: set["Kernel_Classifier"] = None, fUML_Kernel_Class: set["Kernel_Class"] = None):
        self.active = active
        self.Classes148 = Classes148 if Classes148 is not None else set()
        self.Classes151 = Classes151 if Classes151 is not None else set()
        self.fUML_Kernel_Class155 = fUML_Kernel_Class155 if fUML_Kernel_Class155 is not None else set()
        self.fUML_Kernel_Class157 = fUML_Kernel_Class157 if fUML_Kernel_Class157 is not None else set()
        self.fUML_Kernel_Class = fUML_Kernel_Class if fUML_Kernel_Class is not None else set()
        
    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

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
    def Classes151(self):
        return self.__Classes151

    @Classes151.setter
    def Classes151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Class__Classes151", None)
        self.__Classes151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax152"):
                    opp_val = getattr(item, "Syntax152", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax152", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax152"):
                    opp_val = getattr(item, "Syntax152", None)
                    
                    setattr(item, "Syntax152", self)
                    

    @property
    def fUML_Kernel_Class155(self):
        return self.__fUML_Kernel_Class155

    @fUML_Kernel_Class155.setter
    def fUML_Kernel_Class155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Class__fUML_Kernel_Class155", None)
        self.__fUML_Kernel_Class155 = value if value is not None else set()
        
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
    def Classes148(self):
        return self.__Classes148

    @Classes148.setter
    def Classes148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Class__Classes148", None)
        self.__Classes148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax149"):
                    opp_val = getattr(item, "Syntax149", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax149"):
                    opp_val = getattr(item, "Syntax149", None)
                    
                    setattr(item, "Syntax149", self)
                    

    @property
    def fUML_Kernel_Class157(self):
        return self.__fUML_Kernel_Class157

    @fUML_Kernel_Class157.setter
    def fUML_Kernel_Class157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Class__fUML_Kernel_Class157", None)
        self.__fUML_Kernel_Class157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_Classifier158"):
                    opp_val = getattr(item, "Kernel_Classifier158", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Classifier158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Classifier158"):
                    opp_val = getattr(item, "Kernel_Classifier158", None)
                    
                    setattr(item, "Kernel_Classifier158", self)
                    

class Kernel_Enumeration:

    pass
class InstanceSpecification:

    pass
class fUML_Kernel_EnumerationLiteral(InstanceSpecification):

    pass
class Kernel_EnumerationLiteral:

    pass
class DataType:

    pass
class fUML_Kernel_Enumeration(DataType):

    pass
class fUML_Kernel_PrimitiveType(DataType):

    pass
class LiteralSpecification:

    pass
class fUML_Kernel_LiteralUnlimitedNatural(LiteralSpecification):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class fUML_Kernel_LiteralString(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class fUML_Kernel_LiteralNull(LiteralSpecification):

    pass
class fUML_Kernel_LiteralInteger(LiteralSpecification):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class fUML_Kernel_LiteralBoolean(LiteralSpecification):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class ValueSpecification:

    pass
class fUML_Kernel_LiteralSpecification(ValueSpecification):

    pass
class fUML_Kernel_InstanceValue(ValueSpecification):

    pass
class Kernel_StructuralFeature:

    pass
class Kernel_Slot:

    pass
class Kernel_Operation:

    pass
class Feature:

    pass
class fUML_Kernel_BehavioralFeature(Feature):

    def __init__(self, abstract: bool, concurrency: str, fUML_Kernel_BehavioralFeature: set["Kernel_Parameter"] = None, CommonBehaviors: set["BasicBehaviors_Behavior"] = None):
        self.abstract = abstract
        self.concurrency = concurrency
        self.fUML_Kernel_BehavioralFeature = fUML_Kernel_BehavioralFeature if fUML_Kernel_BehavioralFeature is not None else set()
        self.CommonBehaviors = CommonBehaviors if CommonBehaviors is not None else set()
        
    @property
    def concurrency(self) -> str:
        return self.__concurrency

    @concurrency.setter
    def concurrency(self, concurrency: str):
        self.__concurrency = concurrency

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def CommonBehaviors(self):
        return self.__CommonBehaviors

    @CommonBehaviors.setter
    def CommonBehaviors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_BehavioralFeature__CommonBehaviors", None)
        self.__CommonBehaviors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax120"):
                    opp_val = getattr(item, "Syntax120", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax120"):
                    opp_val = getattr(item, "Syntax120", None)
                    
                    setattr(item, "Syntax120", self)
                    

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
                if hasattr(item, "Kernel_Parameter118"):
                    opp_val = getattr(item, "Kernel_Parameter118", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Parameter118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Parameter118"):
                    opp_val = getattr(item, "Kernel_Parameter118", None)
                    
                    setattr(item, "Kernel_Parameter118", self)
                    

class Kernel_ValueSpecification:

    pass
class Kernel_Class:

    pass
class Kernel_DataType:

    pass
class Kernel_Association:

    pass
class Kernel_RedefinableElement:

    pass
class StructuralFeature:

    pass
class fUML_Kernel_Property(StructuralFeature):

    def __init__(self, composite: bool, derived: bool, derivedUnion: bool, aggregation: str, Classes86: "Kernel_Association" = None, Classes89: "Kernel_Association" = None, Classes92: "Kernel_DataType" = None, Classes95: "Kernel_Class" = None, fUML_Kernel_Property: "Kernel_Property" = None):
        self.composite = composite
        self.derived = derived
        self.derivedUnion = derivedUnion
        self.aggregation = aggregation
        self.Classes86 = Classes86
        self.Classes89 = Classes89
        self.Classes92 = Classes92
        self.Classes95 = Classes95
        self.fUML_Kernel_Property = fUML_Kernel_Property
        
    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

    @property
    def derivedUnion(self) -> bool:
        return self.__derivedUnion

    @derivedUnion.setter
    def derivedUnion(self, derivedUnion: bool):
        self.__derivedUnion = derivedUnion

    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def composite(self) -> bool:
        return self.__composite

    @composite.setter
    def composite(self, composite: bool):
        self.__composite = composite

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
            if hasattr(old_value, "Kernel_Property98"):
                opp_val = getattr(old_value, "Kernel_Property98", None)
                if opp_val == self:
                    setattr(old_value, "Kernel_Property98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel_Property98"):
                opp_val = getattr(value, "Kernel_Property98", None)
                setattr(value, "Kernel_Property98", self)

    @property
    def Classes95(self):
        return self.__Classes95

    @Classes95.setter
    def Classes95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Property__Classes95", None)
        self.__Classes95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Syntax96"):
                opp_val = getattr(old_value, "Syntax96", None)
                if opp_val == self:
                    setattr(old_value, "Syntax96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Syntax96"):
                opp_val = getattr(value, "Syntax96", None)
                setattr(value, "Syntax96", self)

    @property
    def Classes89(self):
        return self.__Classes89

    @Classes89.setter
    def Classes89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Property__Classes89", None)
        self.__Classes89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Syntax90"):
                opp_val = getattr(old_value, "Syntax90", None)
                if opp_val == self:
                    setattr(old_value, "Syntax90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Syntax90"):
                opp_val = getattr(value, "Syntax90", None)
                setattr(value, "Syntax90", self)

    @property
    def Classes92(self):
        return self.__Classes92

    @Classes92.setter
    def Classes92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Property__Classes92", None)
        self.__Classes92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Syntax93"):
                opp_val = getattr(old_value, "Syntax93", None)
                if opp_val == self:
                    setattr(old_value, "Syntax93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Syntax93"):
                opp_val = getattr(value, "Syntax93", None)
                setattr(value, "Syntax93", self)

    @property
    def Classes86(self):
        return self.__Classes86

    @Classes86.setter
    def Classes86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Property__Classes86", None)
        self.__Classes86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Syntax87"):
                opp_val = getattr(old_value, "Syntax87", None)
                if opp_val == self:
                    setattr(old_value, "Syntax87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Syntax87"):
                opp_val = getattr(value, "Syntax87", None)
                setattr(value, "Syntax87", self)

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

    def __init__(self, static: bool, Classes61: set["Kernel_Classifier"] = None):
        self.static = static
        self.Classes61 = Classes61 if Classes61 is not None else set()
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def Classes61(self):
        return self.__Classes61

    @Classes61.setter
    def Classes61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Feature__Classes61", None)
        self.__Classes61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax62"):
                    opp_val = getattr(item, "Syntax62", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax62"):
                    opp_val = getattr(item, "Syntax62", None)
                    
                    setattr(item, "Syntax62", self)
                    

class Kernel_TypedElement:

    pass
class fUML_IntermediateActivities_ObjectNode(Kernel_TypedElement, IntermediateActivities_ActivityNode):

    pass
class Kernel_MultiplicityElement:

    pass
class fUML_Kernel_Parameter(Kernel_TypedElement, Kernel_MultiplicityElement):

    def __init__(self, direction: str):
        self.direction = direction
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

class fUML_BasicActions_Pin(IntermediateActivities_ObjectNode, Kernel_MultiplicityElement):

    pass
class Kernel_Feature:

    pass
class fUML_Kernel_StructuralFeature(Kernel_Feature, Kernel_TypedElement, Kernel_MultiplicityElement):

    def __init__(self, readOnly: bool, Syntax71: "fUML_Kernel_Classifier"):
        self.readOnly = readOnly
        
    @property
    def readOnly(self) -> bool:
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly

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
        
    @property
    def body(self) -> str:
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
class Kernel_Namespace:

    pass
class fUML_Kernel_Package(Kernel_Namespace, Kernel_PackageableElement):

    pass
class BasicBehaviors_Behavior:

    pass
class Classifier:

    pass
class fUML_Kernel_DataType(Classifier):

    pass
class fUML_Kernel_Association(Classifier):

    def __init__(self, derived: bool, fUML_Kernel_Association: set["Kernel_Type"] = None, Classes102: set["Kernel_Property"] = None, fUML_Kernel_Association105: set["Kernel_Property"] = None, Classes108: set["Kernel_Property"] = None):
        self.derived = derived
        self.fUML_Kernel_Association = fUML_Kernel_Association if fUML_Kernel_Association is not None else set()
        self.Classes102 = Classes102 if Classes102 is not None else set()
        self.fUML_Kernel_Association105 = fUML_Kernel_Association105 if fUML_Kernel_Association105 is not None else set()
        self.Classes108 = Classes108 if Classes108 is not None else set()
        
    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def Classes108(self):
        return self.__Classes108

    @Classes108.setter
    def Classes108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Association__Classes108", None)
        self.__Classes108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax109"):
                    opp_val = getattr(item, "Syntax109", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax109"):
                    opp_val = getattr(item, "Syntax109", None)
                    
                    setattr(item, "Syntax109", self)
                    

    @property
    def Classes102(self):
        return self.__Classes102

    @Classes102.setter
    def Classes102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Association__Classes102", None)
        self.__Classes102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax103"):
                    opp_val = getattr(item, "Syntax103", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax103"):
                    opp_val = getattr(item, "Syntax103", None)
                    
                    setattr(item, "Syntax103", self)
                    

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
                if hasattr(item, "Kernel_Type100"):
                    opp_val = getattr(item, "Kernel_Type100", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Type100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Type100"):
                    opp_val = getattr(item, "Kernel_Type100", None)
                    
                    setattr(item, "Kernel_Type100", self)
                    

    @property
    def fUML_Kernel_Association105(self):
        return self.__fUML_Kernel_Association105

    @fUML_Kernel_Association105.setter
    def fUML_Kernel_Association105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Association__fUML_Kernel_Association105", None)
        self.__fUML_Kernel_Association105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_Property106"):
                    opp_val = getattr(item, "Kernel_Property106", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Property106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Property106"):
                    opp_val = getattr(item, "Kernel_Property106", None)
                    
                    setattr(item, "Kernel_Property106", self)
                    

class fUML_BasicBehaviors_BehavioredClassifier(Classifier):

    pass
class Element:

    pass
class fUML_Kernel_ElementImport(Element):

    def __init__(self, visibility: str, alias: str, fUML_Kernel_ElementImport: "Kernel_PackageableElement" = None, Classes40: "Kernel_Namespace" = None):
        self.visibility = visibility
        self.alias = alias
        self.fUML_Kernel_ElementImport = fUML_Kernel_ElementImport
        self.Classes40 = Classes40
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def visibility(self) -> str:
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
            if hasattr(old_value, "Kernel_PackageableElement38"):
                opp_val = getattr(old_value, "Kernel_PackageableElement38", None)
                if opp_val == self:
                    setattr(old_value, "Kernel_PackageableElement38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel_PackageableElement38"):
                opp_val = getattr(value, "Kernel_PackageableElement38", None)
                setattr(value, "Kernel_PackageableElement38", self)

    @property
    def Classes40(self):
        return self.__Classes40

    @Classes40.setter
    def Classes40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_ElementImport__Classes40", None)
        self.__Classes40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Syntax41"):
                opp_val = getattr(old_value, "Syntax41", None)
                if opp_val == self:
                    setattr(old_value, "Syntax41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Syntax41"):
                opp_val = getattr(value, "Syntax41", None)
                setattr(value, "Syntax41", self)

class fUML_Kernel_Slot(Element):

    pass
class fUML_Kernel_Generalization(Element):

    def __init__(self, substitutable: bool, fUML_Kernel_Generalization: "Kernel_Classifier" = None, Classes83: "Kernel_Classifier" = None):
        self.substitutable = substitutable
        self.fUML_Kernel_Generalization = fUML_Kernel_Generalization
        self.Classes83 = Classes83
        
    @property
    def substitutable(self) -> bool:
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
            if hasattr(old_value, "Kernel_Classifier81"):
                opp_val = getattr(old_value, "Kernel_Classifier81", None)
                if opp_val == self:
                    setattr(old_value, "Kernel_Classifier81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel_Classifier81"):
                opp_val = getattr(value, "Kernel_Classifier81", None)
                setattr(value, "Kernel_Classifier81", self)

    @property
    def Classes83(self):
        return self.__Classes83

    @Classes83.setter
    def Classes83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Generalization__Classes83", None)
        self.__Classes83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Syntax84"):
                opp_val = getattr(old_value, "Syntax84", None)
                if opp_val == self:
                    setattr(old_value, "Syntax84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Syntax84"):
                opp_val = getattr(value, "Syntax84", None)
                setattr(value, "Syntax84", self)

class fUML_Kernel_PackageImport(Element):

    def __init__(self, visibility: str, fUML_Kernel_PackageImport: "Kernel_Package" = None, Classes44: "Kernel_Namespace" = None):
        self.visibility = visibility
        self.fUML_Kernel_PackageImport = fUML_Kernel_PackageImport
        self.Classes44 = Classes44
        
    @property
    def visibility(self) -> str:
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
    def Classes44(self):
        return self.__Classes44

    @Classes44.setter
    def Classes44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_PackageImport__Classes44", None)
        self.__Classes44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Syntax45"):
                opp_val = getattr(old_value, "Syntax45", None)
                if opp_val == self:
                    setattr(old_value, "Syntax45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Syntax45"):
                opp_val = getattr(value, "Syntax45", None)
                setattr(value, "Syntax45", self)

class fUML_CompleteStructuredActivities_Clause(Element):

    pass
class fUML_Kernel_MultiplicityElement(Element):

    def __init__(self, ordered: bool, unique: bool, upper: int, lower: int, fUML_Kernel_MultiplicityElement: "Kernel_ValueSpecification" = None, fUML_Kernel_MultiplicityElement115: "Kernel_ValueSpecification" = None):
        self.ordered = ordered
        self.unique = unique
        self.upper = upper
        self.lower = lower
        self.fUML_Kernel_MultiplicityElement = fUML_Kernel_MultiplicityElement
        self.fUML_Kernel_MultiplicityElement115 = fUML_Kernel_MultiplicityElement115
        
    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def ordered(self) -> bool:
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered

    @property
    def fUML_Kernel_MultiplicityElement115(self):
        return self.__fUML_Kernel_MultiplicityElement115

    @fUML_Kernel_MultiplicityElement115.setter
    def fUML_Kernel_MultiplicityElement115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_MultiplicityElement__fUML_Kernel_MultiplicityElement115", None)
        self.__fUML_Kernel_MultiplicityElement115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel_ValueSpecification116"):
                opp_val = getattr(old_value, "Kernel_ValueSpecification116", None)
                if opp_val == self:
                    setattr(old_value, "Kernel_ValueSpecification116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel_ValueSpecification116"):
                opp_val = getattr(value, "Kernel_ValueSpecification116", None)
                setattr(value, "Kernel_ValueSpecification116", self)

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

class fUML_IntermediateActions_LinkEndData(Element):

    pass
class fUML_Kernel_NamedElement(Element):

    def __init__(self, name: str, visibility: str, qualifiedName: str, Classes15: "Kernel_Namespace" = None):
        self.name = name
        self.visibility = visibility
        self.qualifiedName = qualifiedName
        self.Classes15 = Classes15
        
    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def Classes15(self):
        return self.__Classes15

    @Classes15.setter
    def Classes15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_NamedElement__Classes15", None)
        self.__Classes15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Syntax16"):
                opp_val = getattr(old_value, "Syntax16", None)
                if opp_val == self:
                    setattr(old_value, "Syntax16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Syntax16"):
                opp_val = getattr(value, "Syntax16", None)
                setattr(value, "Syntax16", self)

class Kernel_Type:

    pass
class fUML_Kernel_Classifier(Kernel_Namespace, Kernel_Type):

    def __init__(self, abstract: bool, finalSpecialization: bool, Classes67: set["Kernel_Generalization"] = None, Classes70: set["Kernel_Feature"] = None, fUML_Kernel_Classifier: set["Kernel_NamedElement"] = None, fUML_Kernel_Classifier75: set["Kernel_Property"] = None, fUML_Kernel_Classifier78: set["Kernel_Classifier"] = None, Kernel_Type100: "fUML_Kernel_Association", Kernel_Type: "fUML_Kernel_TypedElement", Kernel_Type127: "fUML_Kernel_Operation", Syntax50: "fUML_Kernel_Package", Syntax16: "fUML_Kernel_NamedElement", Syntax41: "fUML_Kernel_ElementImport", Syntax45: "fUML_Kernel_PackageImport"):
        self.abstract = abstract
        self.finalSpecialization = finalSpecialization
        self.Classes67 = Classes67 if Classes67 is not None else set()
        self.Classes70 = Classes70 if Classes70 is not None else set()
        self.fUML_Kernel_Classifier = fUML_Kernel_Classifier if fUML_Kernel_Classifier is not None else set()
        self.fUML_Kernel_Classifier75 = fUML_Kernel_Classifier75 if fUML_Kernel_Classifier75 is not None else set()
        self.fUML_Kernel_Classifier78 = fUML_Kernel_Classifier78 if fUML_Kernel_Classifier78 is not None else set()
        
    @property
    def finalSpecialization(self) -> bool:
        return self.__finalSpecialization

    @finalSpecialization.setter
    def finalSpecialization(self, finalSpecialization: bool):
        self.__finalSpecialization = finalSpecialization

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def fUML_Kernel_Classifier75(self):
        return self.__fUML_Kernel_Classifier75

    @fUML_Kernel_Classifier75.setter
    def fUML_Kernel_Classifier75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Classifier__fUML_Kernel_Classifier75", None)
        self.__fUML_Kernel_Classifier75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_Property76"):
                    opp_val = getattr(item, "Kernel_Property76", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Property76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Property76"):
                    opp_val = getattr(item, "Kernel_Property76", None)
                    
                    setattr(item, "Kernel_Property76", self)
                    

    @property
    def Classes67(self):
        return self.__Classes67

    @Classes67.setter
    def Classes67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Classifier__Classes67", None)
        self.__Classes67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax68"):
                    opp_val = getattr(item, "Syntax68", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax68"):
                    opp_val = getattr(item, "Syntax68", None)
                    
                    setattr(item, "Syntax68", self)
                    

    @property
    def Classes70(self):
        return self.__Classes70

    @Classes70.setter
    def Classes70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Classifier__Classes70", None)
        self.__Classes70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax71"):
                    opp_val = getattr(item, "Syntax71", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax71"):
                    opp_val = getattr(item, "Syntax71", None)
                    
                    setattr(item, "Syntax71", self)
                    

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
                if hasattr(item, "Kernel_NamedElement73"):
                    opp_val = getattr(item, "Kernel_NamedElement73", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_NamedElement73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_NamedElement73"):
                    opp_val = getattr(item, "Kernel_NamedElement73", None)
                    
                    setattr(item, "Kernel_NamedElement73", self)
                    

    @property
    def fUML_Kernel_Classifier78(self):
        return self.__fUML_Kernel_Classifier78

    @fUML_Kernel_Classifier78.setter
    def fUML_Kernel_Classifier78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Classifier__fUML_Kernel_Classifier78", None)
        self.__fUML_Kernel_Classifier78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_Classifier79"):
                    opp_val = getattr(item, "Kernel_Classifier79", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Classifier79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Classifier79"):
                    opp_val = getattr(item, "Kernel_Classifier79", None)
                    
                    setattr(item, "Kernel_Classifier79", self)
                    

class TypedElement:

    pass
class fUML_Kernel_ValueSpecification(TypedElement):

    pass
class BehavioralFeature:

    pass
class fUML_Kernel_Operation(BehavioralFeature):

    def __init__(self, query: bool, ordered: bool, unique: bool, lower: int, upper: int, Classes122: "Kernel_Class" = None, fUML_Kernel_Operation: set["Kernel_Operation"] = None, fUML_Kernel_Operation126: "Kernel_Type" = None):
        self.query = query
        self.ordered = ordered
        self.unique = unique
        self.lower = lower
        self.upper = upper
        self.Classes122 = Classes122
        self.fUML_Kernel_Operation = fUML_Kernel_Operation if fUML_Kernel_Operation is not None else set()
        self.fUML_Kernel_Operation126 = fUML_Kernel_Operation126
        
    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def query(self) -> bool:
        return self.__query

    @query.setter
    def query(self, query: bool):
        self.__query = query

    @property
    def ordered(self) -> bool:
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered

    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

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
    def fUML_Kernel_Operation126(self):
        return self.__fUML_Kernel_Operation126

    @fUML_Kernel_Operation126.setter
    def fUML_Kernel_Operation126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Operation__fUML_Kernel_Operation126", None)
        self.__fUML_Kernel_Operation126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel_Type127"):
                opp_val = getattr(old_value, "Kernel_Type127", None)
                if opp_val == self:
                    setattr(old_value, "Kernel_Type127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel_Type127"):
                opp_val = getattr(value, "Kernel_Type127", None)
                setattr(value, "Kernel_Type127", self)

    @property
    def Classes122(self):
        return self.__Classes122

    @Classes122.setter
    def Classes122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_Operation__Classes122", None)
        self.__Classes122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Syntax123"):
                opp_val = getattr(old_value, "Syntax123", None)
                if opp_val == self:
                    setattr(old_value, "Syntax123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Syntax123"):
                opp_val = getattr(value, "Syntax123", None)
                setattr(value, "Syntax123", self)

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
class fUML_Communications_Signal(Classifier):

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
class fUML_Kernel_TypedElement(NamedElement):

    pass
class fUML_Kernel_InstanceSpecification(NamedElement):

    pass
class fUML_Kernel_PackageableElement(NamedElement):

    pass
class fUML_Kernel_RedefinableElement(NamedElement):

    def __init__(self, leaf: bool, fUML_Kernel_RedefinableElement65: set["Kernel_Classifier"] = None, fUML_Kernel_RedefinableElement: set["Kernel_RedefinableElement"] = None):
        self.leaf = leaf
        self.fUML_Kernel_RedefinableElement65 = fUML_Kernel_RedefinableElement65 if fUML_Kernel_RedefinableElement65 is not None else set()
        self.fUML_Kernel_RedefinableElement = fUML_Kernel_RedefinableElement if fUML_Kernel_RedefinableElement is not None else set()
        
    @property
    def leaf(self) -> bool:
        return self.__leaf

    @leaf.setter
    def leaf(self, leaf: bool):
        self.__leaf = leaf

    @property
    def fUML_Kernel_RedefinableElement65(self):
        return self.__fUML_Kernel_RedefinableElement65

    @fUML_Kernel_RedefinableElement65.setter
    def fUML_Kernel_RedefinableElement65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_Kernel_RedefinableElement__fUML_Kernel_RedefinableElement65", None)
        self.__fUML_Kernel_RedefinableElement65 = value if value is not None else set()
        
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
                    

class fUML_Kernel_Namespace(NamedElement):

    pass
class fUML_Communications_Trigger(NamedElement):

    pass
class OpaqueBehavior:

    pass
class fUML_BasicBehaviors_FunctionBehavior(OpaqueBehavior):

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

    def __init__(self, reentrant: bool, Classes: "Kernel_BehavioralFeature" = None, fUML_BasicBehaviors_Behavior: set["Kernel_Parameter"] = None, fUML_BasicBehaviors_Behavior3: "BasicBehaviors_BehavioredClassifier" = None):
        self.reentrant = reentrant
        self.Classes = Classes
        self.fUML_BasicBehaviors_Behavior = fUML_BasicBehaviors_Behavior if fUML_BasicBehaviors_Behavior is not None else set()
        self.fUML_BasicBehaviors_Behavior3 = fUML_BasicBehaviors_Behavior3
        
    @property
    def reentrant(self) -> bool:
        return self.__reentrant

    @reentrant.setter
    def reentrant(self, reentrant: bool):
        self.__reentrant = reentrant

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
    def Classes(self):
        return self.__Classes

    @Classes.setter
    def Classes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_BasicBehaviors_Behavior__Classes", None)
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

class Behavior:

    pass
class fUML_IntermediateActivities_Activity(Behavior):

    def __init__(self, readOnly: bool, Activities173: set["IntermediateActivities_ActivityNode"] = None, Activities176: set["IntermediateActivities_ActivityEdge"] = None):
        self.readOnly = readOnly
        self.Activities173 = Activities173 if Activities173 is not None else set()
        self.Activities176 = Activities176 if Activities176 is not None else set()
        
    @property
    def readOnly(self) -> bool:
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly

    @property
    def Activities173(self):
        return self.__Activities173

    @Activities173.setter
    def Activities173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_IntermediateActivities_Activity__Activities173", None)
        self.__Activities173 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax174"):
                    opp_val = getattr(item, "Syntax174", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax174", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax174"):
                    opp_val = getattr(item, "Syntax174", None)
                    
                    setattr(item, "Syntax174", self)
                    

    @property
    def Activities176(self):
        return self.__Activities176

    @Activities176.setter
    def Activities176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fUML_IntermediateActivities_Activity__Activities176", None)
        self.__Activities176 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax177"):
                    opp_val = getattr(item, "Syntax177", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax177", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax177"):
                    opp_val = getattr(item, "Syntax177", None)
                    
                    setattr(item, "Syntax177", self)
                    

class fUML_BasicBehaviors_OpaqueBehavior(Behavior):

    def __init__(self, body: str, language: str):
        self.body = body
        self.language = language
        
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
