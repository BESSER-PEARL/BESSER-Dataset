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
    in_ = "in_"
    out = "out"
    inout = "inout"
    return_ = "return_"


############################################
# Definition of Classes
############################################

class InvocationAction:

    pass
class xmof_BasicActions_SendSignalAction(InvocationAction):

    pass
class xmof_BasicActions_CallAction(InvocationAction):

    def __init__(self, synchronous: bool, xmof_BasicActions_CallAction: set["BasicActions_OutputPin"] = None):
        self.synchronous = synchronous
        self.xmof_BasicActions_CallAction = xmof_BasicActions_CallAction if xmof_BasicActions_CallAction is not None else set()
        
        pass
    @property
    def synchronous(self):
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
                if hasattr(item, "BasicActions_OutputPin204"):
                    opp_val = getattr(item, "BasicActions_OutputPin204", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin204", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin204"):
                    opp_val = getattr(item, "BasicActions_OutputPin204", None)
                    
                    setattr(item, "BasicActions_OutputPin204", self)
                    

class IntermediateActivities_ObjectNode:

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

    def __init__(self, locallyReentrant: bool, xmof_BasicActions_Action: set["BasicActions_OutputPin"] = None, xmof_BasicActions_Action199: "BasicActions_xmof_EClassifier" = None, xmof_BasicActions_Action201: set["BasicActions_InputPin"] = None):
        self.locallyReentrant = locallyReentrant
        self.xmof_BasicActions_Action = xmof_BasicActions_Action if xmof_BasicActions_Action is not None else set()
        self.xmof_BasicActions_Action199 = xmof_BasicActions_Action199
        self.xmof_BasicActions_Action201 = xmof_BasicActions_Action201 if xmof_BasicActions_Action201 is not None else set()
        
        pass
    @property
    def locallyReentrant(self):
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
                if hasattr(item, "BasicActions_OutputPin197"):
                    opp_val = getattr(item, "BasicActions_OutputPin197", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin197", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin197"):
                    opp_val = getattr(item, "BasicActions_OutputPin197", None)
                    
                    setattr(item, "BasicActions_OutputPin197", self)
                    

    @property
    def xmof_BasicActions_Action199(self):
        return self.__xmof_BasicActions_Action199

    @xmof_BasicActions_Action199.setter
    def xmof_BasicActions_Action199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_BasicActions_Action__xmof_BasicActions_Action199", None)
        self.__xmof_BasicActions_Action199 = value
        
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
    def xmof_BasicActions_Action201(self):
        return self.__xmof_BasicActions_Action201

    @xmof_BasicActions_Action201.setter
    def xmof_BasicActions_Action201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_BasicActions_Action__xmof_BasicActions_Action201", None)
        self.__xmof_BasicActions_Action201 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_InputPin202"):
                    opp_val = getattr(item, "BasicActions_InputPin202", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_InputPin202", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_InputPin202"):
                    opp_val = getattr(item, "BasicActions_InputPin202", None)
                    
                    setattr(item, "BasicActions_InputPin202", self)
                    

class Communications_Trigger:

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
class IntermediateActions_xmof_EClassifier:

    pass
class WriteLinkAction:

    pass
class xmof_IntermediateActions_DestroyLinkAction(WriteLinkAction):

    pass
class xmof_IntermediateActions_CreateLinkAction(WriteLinkAction):

    pass
class LinkEndData:

    pass
class xmof_IntermediateActions_LinkEndDestructionData(LinkEndData):

    def __init__(self, destroyDuplicates: bool, xmof_IntermediateActions_LinkEndDestructionData: "BasicActions_InputPin" = None):
        self.destroyDuplicates = destroyDuplicates
        self.xmof_IntermediateActions_LinkEndDestructionData = xmof_IntermediateActions_LinkEndDestructionData
        
        pass
    @property
    def destroyDuplicates(self):
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
            if hasattr(old_value, "BasicActions_InputPin144"):
                opp_val = getattr(old_value, "BasicActions_InputPin144", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin144"):
                opp_val = getattr(value, "BasicActions_InputPin144", None)
                setattr(value, "BasicActions_InputPin144", self)

class xmof_IntermediateActions_LinkEndCreationData(LinkEndData):

    def __init__(self, replaceAll: bool, xmof_IntermediateActions_LinkEndCreationData: "BasicActions_InputPin" = None):
        self.replaceAll = replaceAll
        self.xmof_IntermediateActions_LinkEndCreationData = xmof_IntermediateActions_LinkEndCreationData
        
        pass
    @property
    def replaceAll(self):
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
            if hasattr(old_value, "BasicActions_InputPin142"):
                opp_val = getattr(old_value, "BasicActions_InputPin142", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin142"):
                opp_val = getattr(value, "BasicActions_InputPin142", None)
                setattr(value, "BasicActions_InputPin142", self)

class WriteStructuralFeatureAction:

    pass
class xmof_IntermediateActions_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    def __init__(self, replaceAll: bool, xmof_IntermediateActions_AddStructuralFeatureValueAction: "BasicActions_InputPin" = None):
        self.replaceAll = replaceAll
        self.xmof_IntermediateActions_AddStructuralFeatureValueAction = xmof_IntermediateActions_AddStructuralFeatureValueAction
        
        pass
    @property
    def replaceAll(self):
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
            if hasattr(old_value, "BasicActions_InputPin159"):
                opp_val = getattr(old_value, "BasicActions_InputPin159", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin159"):
                opp_val = getattr(value, "BasicActions_InputPin159", None)
                setattr(value, "BasicActions_InputPin159", self)

class xmof_IntermediateActions_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    def __init__(self, removeDuplicates: bool, xmof_IntermediateActions_RemoveStructuralFeatureValueAction: "BasicActions_InputPin" = None):
        self.removeDuplicates = removeDuplicates
        self.xmof_IntermediateActions_RemoveStructuralFeatureValueAction = xmof_IntermediateActions_RemoveStructuralFeatureValueAction
        
        pass
    @property
    def removeDuplicates(self):
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
            if hasattr(old_value, "BasicActions_InputPin134"):
                opp_val = getattr(old_value, "BasicActions_InputPin134", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin134"):
                opp_val = getattr(value, "BasicActions_InputPin134", None)
                setattr(value, "BasicActions_InputPin134", self)

class StructuralFeatureAction:

    pass
class xmof_IntermediateActions_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class xmof_IntermediateActions_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class xmof_IntermediateActions_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class IntermediateActions_xmof_EReference:

    pass
class IntermediateActions_LinkEndData:

    pass
class LinkAction:

    pass
class xmof_IntermediateActions_ReadLinkAction(LinkAction):

    pass
class xmof_IntermediateActions_WriteLinkAction(LinkAction):

    pass
class IntermediateActions_xmof_EStructuralFeature:

    pass
class ExtraStructuredActivities_ExpansionNode:

    pass
class ExtraStructuredActivities_ExpansionRegion:

    pass
class Action:

    pass
class xmof_IntermediateActions_TestIdentityAction(Action):

    pass
class xmof_CompleteActions_StartClassifierBehaviorAction(Action):

    pass
class xmof_CompleteActions_ReduceAction(Action):

    def __init__(self, ordered: bool, xmof_CompleteActions_ReduceAction: "BasicBehaviors_Behavior" = None, xmof_CompleteActions_ReduceAction167: "BasicActions_OutputPin" = None, xmof_CompleteActions_ReduceAction170: "BasicActions_InputPin" = None):
        self.ordered = ordered
        self.xmof_CompleteActions_ReduceAction = xmof_CompleteActions_ReduceAction
        self.xmof_CompleteActions_ReduceAction167 = xmof_CompleteActions_ReduceAction167
        self.xmof_CompleteActions_ReduceAction170 = xmof_CompleteActions_ReduceAction170
        
        pass
    @property
    def ordered(self):
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
            if hasattr(old_value, "BasicBehaviors_Behavior165"):
                opp_val = getattr(old_value, "BasicBehaviors_Behavior165", None)
                if opp_val == self:
                    setattr(old_value, "BasicBehaviors_Behavior165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicBehaviors_Behavior165"):
                opp_val = getattr(value, "BasicBehaviors_Behavior165", None)
                setattr(value, "BasicBehaviors_Behavior165", self)

    @property
    def xmof_CompleteActions_ReduceAction170(self):
        return self.__xmof_CompleteActions_ReduceAction170

    @xmof_CompleteActions_ReduceAction170.setter
    def xmof_CompleteActions_ReduceAction170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReduceAction__xmof_CompleteActions_ReduceAction170", None)
        self.__xmof_CompleteActions_ReduceAction170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin171"):
                opp_val = getattr(old_value, "BasicActions_InputPin171", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin171"):
                opp_val = getattr(value, "BasicActions_InputPin171", None)
                setattr(value, "BasicActions_InputPin171", self)

    @property
    def xmof_CompleteActions_ReduceAction167(self):
        return self.__xmof_CompleteActions_ReduceAction167

    @xmof_CompleteActions_ReduceAction167.setter
    def xmof_CompleteActions_ReduceAction167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReduceAction__xmof_CompleteActions_ReduceAction167", None)
        self.__xmof_CompleteActions_ReduceAction167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_OutputPin168"):
                opp_val = getattr(old_value, "BasicActions_OutputPin168", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_OutputPin168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_OutputPin168"):
                opp_val = getattr(value, "BasicActions_OutputPin168", None)
                setattr(value, "BasicActions_OutputPin168", self)

class xmof_IntermediateActions_ReadSelfAction(Action):

    pass
class xmof_IntermediateActions_DestroyObjectAction(Action):

    def __init__(self, destroyLinks: bool, destroyOwnedObjects: bool, xmof_IntermediateActions_DestroyObjectAction: "BasicActions_InputPin" = None):
        self.destroyLinks = destroyLinks
        self.destroyOwnedObjects = destroyOwnedObjects
        self.xmof_IntermediateActions_DestroyObjectAction = xmof_IntermediateActions_DestroyObjectAction
        
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
    def xmof_IntermediateActions_DestroyObjectAction(self):
        return self.__xmof_IntermediateActions_DestroyObjectAction

    @xmof_IntermediateActions_DestroyObjectAction.setter
    def xmof_IntermediateActions_DestroyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_IntermediateActions_DestroyObjectAction__xmof_IntermediateActions_DestroyObjectAction", None)
        self.__xmof_IntermediateActions_DestroyObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin157"):
                opp_val = getattr(old_value, "BasicActions_InputPin157", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin157"):
                opp_val = getattr(value, "BasicActions_InputPin157", None)
                setattr(value, "BasicActions_InputPin157", self)

class xmof_IntermediateActions_ClearAssociationAction(Action):

    pass
class xmof_BasicActions_InvocationAction(Action):

    pass
class xmof_IntermediateActions_LinkAction(Action):

    pass
class xmof_IntermediateActions_ValueSpecificationAction(Action):

    pass
class xmof_CompleteActions_ReadIsClassifiedObjectAction(Action):

    def __init__(self, direct: bool, xmof_CompleteActions_ReadIsClassifiedObjectAction: "CompleteActions_xmof_EClassifier" = None, xmof_CompleteActions_ReadIsClassifiedObjectAction179: "BasicActions_OutputPin" = None, xmof_CompleteActions_ReadIsClassifiedObjectAction182: "BasicActions_InputPin" = None):
        self.direct = direct
        self.xmof_CompleteActions_ReadIsClassifiedObjectAction = xmof_CompleteActions_ReadIsClassifiedObjectAction
        self.xmof_CompleteActions_ReadIsClassifiedObjectAction179 = xmof_CompleteActions_ReadIsClassifiedObjectAction179
        self.xmof_CompleteActions_ReadIsClassifiedObjectAction182 = xmof_CompleteActions_ReadIsClassifiedObjectAction182
        
        pass
    @property
    def direct(self):
        return self.__direct

    @direct.setter
    def direct(self, direct: bool):
        self.__direct = direct


    @property
    def xmof_CompleteActions_ReadIsClassifiedObjectAction179(self):
        return self.__xmof_CompleteActions_ReadIsClassifiedObjectAction179

    @xmof_CompleteActions_ReadIsClassifiedObjectAction179.setter
    def xmof_CompleteActions_ReadIsClassifiedObjectAction179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReadIsClassifiedObjectAction__xmof_CompleteActions_ReadIsClassifiedObjectAction179", None)
        self.__xmof_CompleteActions_ReadIsClassifiedObjectAction179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_OutputPin180"):
                opp_val = getattr(old_value, "BasicActions_OutputPin180", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_OutputPin180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_OutputPin180"):
                opp_val = getattr(value, "BasicActions_OutputPin180", None)
                setattr(value, "BasicActions_OutputPin180", self)

    @property
    def xmof_CompleteActions_ReadIsClassifiedObjectAction182(self):
        return self.__xmof_CompleteActions_ReadIsClassifiedObjectAction182

    @xmof_CompleteActions_ReadIsClassifiedObjectAction182.setter
    def xmof_CompleteActions_ReadIsClassifiedObjectAction182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReadIsClassifiedObjectAction__xmof_CompleteActions_ReadIsClassifiedObjectAction182", None)
        self.__xmof_CompleteActions_ReadIsClassifiedObjectAction182 = value
        
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
            if hasattr(old_value, "CompleteActions_xmof_EClassifier177"):
                opp_val = getattr(old_value, "CompleteActions_xmof_EClassifier177", None)
                if opp_val == self:
                    setattr(old_value, "CompleteActions_xmof_EClassifier177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteActions_xmof_EClassifier177"):
                opp_val = getattr(value, "CompleteActions_xmof_EClassifier177", None)
                setattr(value, "CompleteActions_xmof_EClassifier177", self)

class xmof_CompleteActions_ReclassifyObjectAction(Action):

    def __init__(self, replaceAll: bool, xmof_CompleteActions_ReclassifyObjectAction: set["CompleteActions_xmof_EClassifier"] = None, xmof_CompleteActions_ReclassifyObjectAction187: "BasicActions_InputPin" = None, xmof_CompleteActions_ReclassifyObjectAction190: set["CompleteActions_xmof_EClassifier"] = None):
        self.replaceAll = replaceAll
        self.xmof_CompleteActions_ReclassifyObjectAction = xmof_CompleteActions_ReclassifyObjectAction if xmof_CompleteActions_ReclassifyObjectAction is not None else set()
        self.xmof_CompleteActions_ReclassifyObjectAction187 = xmof_CompleteActions_ReclassifyObjectAction187
        self.xmof_CompleteActions_ReclassifyObjectAction190 = xmof_CompleteActions_ReclassifyObjectAction190 if xmof_CompleteActions_ReclassifyObjectAction190 is not None else set()
        
        pass
    @property
    def replaceAll(self):
        return self.__replaceAll

    @replaceAll.setter
    def replaceAll(self, replaceAll: bool):
        self.__replaceAll = replaceAll


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
                if hasattr(item, "CompleteActions_xmof_EClassifier185"):
                    opp_val = getattr(item, "CompleteActions_xmof_EClassifier185", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteActions_xmof_EClassifier185", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteActions_xmof_EClassifier185"):
                    opp_val = getattr(item, "CompleteActions_xmof_EClassifier185", None)
                    
                    setattr(item, "CompleteActions_xmof_EClassifier185", self)
                    

    @property
    def xmof_CompleteActions_ReclassifyObjectAction190(self):
        return self.__xmof_CompleteActions_ReclassifyObjectAction190

    @xmof_CompleteActions_ReclassifyObjectAction190.setter
    def xmof_CompleteActions_ReclassifyObjectAction190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReclassifyObjectAction__xmof_CompleteActions_ReclassifyObjectAction190", None)
        self.__xmof_CompleteActions_ReclassifyObjectAction190 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteActions_xmof_EClassifier191"):
                    opp_val = getattr(item, "CompleteActions_xmof_EClassifier191", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteActions_xmof_EClassifier191", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteActions_xmof_EClassifier191"):
                    opp_val = getattr(item, "CompleteActions_xmof_EClassifier191", None)
                    
                    setattr(item, "CompleteActions_xmof_EClassifier191", self)
                    

    @property
    def xmof_CompleteActions_ReclassifyObjectAction187(self):
        return self.__xmof_CompleteActions_ReclassifyObjectAction187

    @xmof_CompleteActions_ReclassifyObjectAction187.setter
    def xmof_CompleteActions_ReclassifyObjectAction187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReclassifyObjectAction__xmof_CompleteActions_ReclassifyObjectAction187", None)
        self.__xmof_CompleteActions_ReclassifyObjectAction187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin188"):
                opp_val = getattr(old_value, "BasicActions_InputPin188", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin188"):
                opp_val = getattr(value, "BasicActions_InputPin188", None)
                setattr(value, "BasicActions_InputPin188", self)

class xmof_IntermediateActions_CreateObjectAction(Action):

    pass
class xmof_CompleteActions_ReadExtentAction(Action):

    pass
class xmof_CompleteActions_AcceptEventAction(Action):

    def __init__(self, unmarshall: bool, xmof_CompleteActions_AcceptEventAction195: set["Communications_Trigger"] = None, xmof_CompleteActions_AcceptEventAction: set["BasicActions_OutputPin"] = None):
        self.unmarshall = unmarshall
        self.xmof_CompleteActions_AcceptEventAction195 = xmof_CompleteActions_AcceptEventAction195 if xmof_CompleteActions_AcceptEventAction195 is not None else set()
        self.xmof_CompleteActions_AcceptEventAction = xmof_CompleteActions_AcceptEventAction if xmof_CompleteActions_AcceptEventAction is not None else set()
        
        pass
    @property
    def unmarshall(self):
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
                if hasattr(item, "BasicActions_OutputPin193"):
                    opp_val = getattr(item, "BasicActions_OutputPin193", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin193", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin193"):
                    opp_val = getattr(item, "BasicActions_OutputPin193", None)
                    
                    setattr(item, "BasicActions_OutputPin193", self)
                    

    @property
    def xmof_CompleteActions_AcceptEventAction195(self):
        return self.__xmof_CompleteActions_AcceptEventAction195

    @xmof_CompleteActions_AcceptEventAction195.setter
    def xmof_CompleteActions_AcceptEventAction195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_AcceptEventAction__xmof_CompleteActions_AcceptEventAction195", None)
        self.__xmof_CompleteActions_AcceptEventAction195 = value if value is not None else set()
        
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
                    

class xmof_IntermediateActions_StructuralFeatureAction(Action):

    pass
class xmof_CompleteStructuredActivities_StructuredActivityNode(Action):

    def __init__(self, mustIsolate: bool, xmof_CompleteStructuredActivities_StructuredActivityNode95: set["BasicActions_InputPin"] = None, inStructuredNode: set["IntermediateActivities_ActivityNode"] = None, inStructuredNode90: set["IntermediateActivities_ActivityEdge"] = None, xmof_CompleteStructuredActivities_StructuredActivityNode: set["BasicActions_OutputPin"] = None):
        self.mustIsolate = mustIsolate
        self.xmof_CompleteStructuredActivities_StructuredActivityNode95 = xmof_CompleteStructuredActivities_StructuredActivityNode95 if xmof_CompleteStructuredActivities_StructuredActivityNode95 is not None else set()
        self.inStructuredNode = inStructuredNode if inStructuredNode is not None else set()
        self.inStructuredNode90 = inStructuredNode90 if inStructuredNode90 is not None else set()
        self.xmof_CompleteStructuredActivities_StructuredActivityNode = xmof_CompleteStructuredActivities_StructuredActivityNode if xmof_CompleteStructuredActivities_StructuredActivityNode is not None else set()
        
        pass
    @property
    def mustIsolate(self):
        return self.__mustIsolate

    @mustIsolate.setter
    def mustIsolate(self, mustIsolate: bool):
        self.__mustIsolate = mustIsolate


    @property
    def inStructuredNode(self):
        return self.__inStructuredNode

    @inStructuredNode.setter
    def inStructuredNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_StructuredActivityNode__inStructuredNode", None)
        self.__inStructuredNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityNode88"):
                    opp_val = getattr(item, "ActivityNode88", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityNode88", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityNode88"):
                    opp_val = getattr(item, "ActivityNode88", None)
                    
                    setattr(item, "ActivityNode88", self)
                    

    @property
    def xmof_CompleteStructuredActivities_StructuredActivityNode95(self):
        return self.__xmof_CompleteStructuredActivities_StructuredActivityNode95

    @xmof_CompleteStructuredActivities_StructuredActivityNode95.setter
    def xmof_CompleteStructuredActivities_StructuredActivityNode95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_StructuredActivityNode__xmof_CompleteStructuredActivities_StructuredActivityNode95", None)
        self.__xmof_CompleteStructuredActivities_StructuredActivityNode95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_InputPin96"):
                    opp_val = getattr(item, "BasicActions_InputPin96", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_InputPin96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_InputPin96"):
                    opp_val = getattr(item, "BasicActions_InputPin96", None)
                    
                    setattr(item, "BasicActions_InputPin96", self)
                    

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
                if hasattr(item, "BasicActions_OutputPin93"):
                    opp_val = getattr(item, "BasicActions_OutputPin93", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin93"):
                    opp_val = getattr(item, "BasicActions_OutputPin93", None)
                    
                    setattr(item, "BasicActions_OutputPin93", self)
                    

    @property
    def inStructuredNode90(self):
        return self.__inStructuredNode90

    @inStructuredNode90.setter
    def inStructuredNode90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_StructuredActivityNode__inStructuredNode90", None)
        self.__inStructuredNode90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge91"):
                    opp_val = getattr(item, "ActivityEdge91", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge91"):
                    opp_val = getattr(item, "ActivityEdge91", None)
                    
                    setattr(item, "ActivityEdge91", self)
                    

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
        old_value = getattr(self, f"_xmof_ExtraStructuredActivities_ExpansionRegion__regionAsOutput", None)
        self.__regionAsOutput = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExpansionNode102"):
                    opp_val = getattr(item, "ExpansionNode102", None)
                    
                    if opp_val == self:
                        setattr(item, "ExpansionNode102", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExpansionNode102"):
                    opp_val = getattr(item, "ExpansionNode102", None)
                    
                    setattr(item, "ExpansionNode102", self)
                    

    @property
    def regionAsInput(self):
        return self.__regionAsInput

    @regionAsInput.setter
    def regionAsInput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_ExtraStructuredActivities_ExpansionRegion__regionAsInput", None)
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
                    

class xmof_CompleteStructuredActivities_ConditionalNode(StructuredActivityNode):

    def __init__(self, assured: bool, determinate: bool, xmof_CompleteStructuredActivities_ConditionalNode: set["CompleteStructuredActivities_Clause"] = None, xmof_CompleteStructuredActivities_ConditionalNode85: set["BasicActions_OutputPin"] = None):
        self.assured = assured
        self.determinate = determinate
        self.xmof_CompleteStructuredActivities_ConditionalNode = xmof_CompleteStructuredActivities_ConditionalNode if xmof_CompleteStructuredActivities_ConditionalNode is not None else set()
        self.xmof_CompleteStructuredActivities_ConditionalNode85 = xmof_CompleteStructuredActivities_ConditionalNode85 if xmof_CompleteStructuredActivities_ConditionalNode85 is not None else set()
        
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
    def xmof_CompleteStructuredActivities_ConditionalNode85(self):
        return self.__xmof_CompleteStructuredActivities_ConditionalNode85

    @xmof_CompleteStructuredActivities_ConditionalNode85.setter
    def xmof_CompleteStructuredActivities_ConditionalNode85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_ConditionalNode__xmof_CompleteStructuredActivities_ConditionalNode85", None)
        self.__xmof_CompleteStructuredActivities_ConditionalNode85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin86"):
                    opp_val = getattr(item, "BasicActions_OutputPin86", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin86", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin86"):
                    opp_val = getattr(item, "BasicActions_OutputPin86", None)
                    
                    setattr(item, "BasicActions_OutputPin86", self)
                    

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
                    

class xmof_CompleteStructuredActivities_LoopNode(StructuredActivityNode):

    def __init__(self, testedFirst: bool, xmof_CompleteStructuredActivities_LoopNode: "BasicActions_OutputPin" = None, xmof_CompleteStructuredActivities_LoopNode51: set["CompleteStructuredActivities_ExecutableNode"] = None, xmof_CompleteStructuredActivities_LoopNode53: set["BasicActions_OutputPin"] = None, xmof_CompleteStructuredActivities_LoopNode56: set["BasicActions_InputPin"] = None, xmof_CompleteStructuredActivities_LoopNode58: set["CompleteStructuredActivities_ExecutableNode"] = None, xmof_CompleteStructuredActivities_LoopNode61: set["BasicActions_OutputPin"] = None, xmof_CompleteStructuredActivities_LoopNode64: set["BasicActions_OutputPin"] = None, xmof_CompleteStructuredActivities_LoopNode67: set["CompleteStructuredActivities_ExecutableNode"] = None):
        self.testedFirst = testedFirst
        self.xmof_CompleteStructuredActivities_LoopNode = xmof_CompleteStructuredActivities_LoopNode
        self.xmof_CompleteStructuredActivities_LoopNode51 = xmof_CompleteStructuredActivities_LoopNode51 if xmof_CompleteStructuredActivities_LoopNode51 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode53 = xmof_CompleteStructuredActivities_LoopNode53 if xmof_CompleteStructuredActivities_LoopNode53 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode56 = xmof_CompleteStructuredActivities_LoopNode56 if xmof_CompleteStructuredActivities_LoopNode56 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode58 = xmof_CompleteStructuredActivities_LoopNode58 if xmof_CompleteStructuredActivities_LoopNode58 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode61 = xmof_CompleteStructuredActivities_LoopNode61 if xmof_CompleteStructuredActivities_LoopNode61 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode64 = xmof_CompleteStructuredActivities_LoopNode64 if xmof_CompleteStructuredActivities_LoopNode64 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode67 = xmof_CompleteStructuredActivities_LoopNode67 if xmof_CompleteStructuredActivities_LoopNode67 is not None else set()
        
        pass
    @property
    def testedFirst(self):
        return self.__testedFirst

    @testedFirst.setter
    def testedFirst(self, testedFirst: bool):
        self.__testedFirst = testedFirst


    @property
    def xmof_CompleteStructuredActivities_LoopNode61(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode61

    @xmof_CompleteStructuredActivities_LoopNode61.setter
    def xmof_CompleteStructuredActivities_LoopNode61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode61", None)
        self.__xmof_CompleteStructuredActivities_LoopNode61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin62"):
                    opp_val = getattr(item, "BasicActions_OutputPin62", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin62"):
                    opp_val = getattr(item, "BasicActions_OutputPin62", None)
                    
                    setattr(item, "BasicActions_OutputPin62", self)
                    

    @property
    def xmof_CompleteStructuredActivities_LoopNode53(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode53

    @xmof_CompleteStructuredActivities_LoopNode53.setter
    def xmof_CompleteStructuredActivities_LoopNode53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode53", None)
        self.__xmof_CompleteStructuredActivities_LoopNode53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin54"):
                    opp_val = getattr(item, "BasicActions_OutputPin54", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin54"):
                    opp_val = getattr(item, "BasicActions_OutputPin54", None)
                    
                    setattr(item, "BasicActions_OutputPin54", self)
                    

    @property
    def xmof_CompleteStructuredActivities_LoopNode64(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode64

    @xmof_CompleteStructuredActivities_LoopNode64.setter
    def xmof_CompleteStructuredActivities_LoopNode64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode64", None)
        self.__xmof_CompleteStructuredActivities_LoopNode64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin65"):
                    opp_val = getattr(item, "BasicActions_OutputPin65", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin65"):
                    opp_val = getattr(item, "BasicActions_OutputPin65", None)
                    
                    setattr(item, "BasicActions_OutputPin65", self)
                    

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
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode68"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode68", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteStructuredActivities_ExecutableNode68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode68"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode68", None)
                    
                    setattr(item, "CompleteStructuredActivities_ExecutableNode68", self)
                    

    @property
    def xmof_CompleteStructuredActivities_LoopNode51(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode51

    @xmof_CompleteStructuredActivities_LoopNode51.setter
    def xmof_CompleteStructuredActivities_LoopNode51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode51", None)
        self.__xmof_CompleteStructuredActivities_LoopNode51 = value if value is not None else set()
        
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
    def xmof_CompleteStructuredActivities_LoopNode56(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode56

    @xmof_CompleteStructuredActivities_LoopNode56.setter
    def xmof_CompleteStructuredActivities_LoopNode56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode56", None)
        self.__xmof_CompleteStructuredActivities_LoopNode56 = value if value is not None else set()
        
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
    def xmof_CompleteStructuredActivities_LoopNode58(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode58

    @xmof_CompleteStructuredActivities_LoopNode58.setter
    def xmof_CompleteStructuredActivities_LoopNode58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode58", None)
        self.__xmof_CompleteStructuredActivities_LoopNode58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode59"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode59", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteStructuredActivities_ExecutableNode59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode59"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode59", None)
                    
                    setattr(item, "CompleteStructuredActivities_ExecutableNode59", self)
                    

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
class ControlNode:

    pass
class xmof_IntermediateActivities_JoinNode(ControlNode):

    pass
class xmof_IntermediateActivities_DecisionNode(ControlNode):

    pass
class xmof_IntermediateActivities_InitialNode(ControlNode):

    pass
class xmof_IntermediateActivities_FinalNode(ControlNode):

    pass
class xmof_IntermediateActivities_ForkNode(ControlNode):

    pass
class xmof_IntermediateActivities_MergeNode(ControlNode):

    pass
class IntermediateActivities_ActivityEdge:

    pass
class CompleteStructuredActivities_StructuredActivityNode:

    pass
class IntermediateActivities_Activity:

    pass
class ActivityEdge:

    pass
class xmof_IntermediateActivities_ControlFlow(ActivityEdge):

    pass
class xmof_IntermediateActivities_ObjectFlow(ActivityEdge):

    pass
class EDataType:

    pass
class xmof_Kernel_PrimitiveType(EDataType):

    pass
class LiteralSpecification:

    pass
class xmof_Kernel_LiteralNull(LiteralSpecification):

    pass
class xmof_Kernel_LiteralUnlimitedNatural(LiteralSpecification):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class xmof_Kernel_LiteralInteger(LiteralSpecification):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class xmof_Kernel_LiteralString(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class xmof_Kernel_LiteralBoolean(LiteralSpecification):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class ValueSpecification:

    pass
class xmof_Kernel_LiteralSpecification(ValueSpecification):

    pass
class xmof_Kernel_InstanceValue(ValueSpecification):

    pass
class Kernel_InstanceSpecification:

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
class Kernel_Slot:

    pass
class IntermediateActivities_ActivityNode:

    pass
class ETypedElement:

    pass
class xmof_BasicActions_Pin(ETypedElement, IntermediateActivities_ObjectNode):

    pass
class xmof_IntermediateActivities_ObjectNode(ETypedElement, IntermediateActivities_ActivityNode):

    pass
class xmof_Kernel_ValueSpecification(ETypedElement):

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
        
        pass
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


class EClass:

    pass
class EOperation:

    pass
class xmof_Kernel_BehavioredEOperation(EOperation):

    pass
class BehavioredEOperation:

    pass
class xmof_Communications_Reception(BehavioredEOperation):

    pass
class Event:

    pass
class xmof_Communications_MessageEvent(Event):

    pass
class Communications_Signal:

    pass
class MessageEvent:

    pass
class xmof_Communications_SignalEvent(MessageEvent):

    pass
class Communications_xmof_EAttribute:

    pass
class Communications_Event:

    pass
class ENamedElement:

    pass
class xmof_IntermediateActivities_ActivityEdge(ENamedElement):

    pass
class xmof_Kernel_InstanceSpecification(ENamedElement):

    pass
class xmof_Communications_Event(ENamedElement):

    pass
class xmof_IntermediateActivities_ActivityNode(ENamedElement):

    pass
class xmof_Communications_Trigger(ENamedElement):

    pass
class OpaqueBehavior:

    pass
class xmof_BasicBehaviors_FunctionBehavior(OpaqueBehavior):

    pass
class Kernel_xmof_EClassifier:

    pass
class BasicBehaviors_Behavior:

    pass
class EClassifier:

    pass
class xmof_Communications_Signal(EClassifier):

    pass
class xmof_BasicBehaviors_BehavioredClassifier(EClassifier):

    pass
class BasicBehaviors_BehavioredClassifier:

    pass
class xmof_Kernel_BehavioredEClass(BasicBehaviors_BehavioredClassifier, EClass):

    pass
class Kernel_DirectedParameter:

    pass
class Kernel_BehavioredEOperation:

    pass
class BehavioredEClass:

    pass
class xmof_Kernel_MainEClass(BehavioredEClass):

    pass
class xmof_BasicBehaviors_Behavior(BehavioredEClass):

    def __init__(self, reentrant: bool, method: "Kernel_BehavioredEOperation" = None, xmof_BasicBehaviors_Behavior: set["Kernel_DirectedParameter"] = None, xmof_BasicBehaviors_Behavior3: "BasicBehaviors_BehavioredClassifier" = None):
        self.reentrant = reentrant
        self.method = method
        self.xmof_BasicBehaviors_Behavior = xmof_BasicBehaviors_Behavior if xmof_BasicBehaviors_Behavior is not None else set()
        self.xmof_BasicBehaviors_Behavior3 = xmof_BasicBehaviors_Behavior3
        
        pass
    @property
    def reentrant(self):
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
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_BasicBehaviors_Behavior__method", None)
        self.__method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BehavioredEOperation"):
                opp_val = getattr(old_value, "BehavioredEOperation", None)
                if opp_val == self:
                    setattr(old_value, "BehavioredEOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BehavioredEOperation"):
                opp_val = getattr(value, "BehavioredEOperation", None)
                setattr(value, "BehavioredEOperation", self)

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

class Behavior:

    pass
class xmof_IntermediateActivities_Activity(Behavior):

    def __init__(self, readOnly: bool, activity: set["IntermediateActivities_ActivityNode"] = None, activity33: set["IntermediateActivities_ActivityEdge"] = None):
        self.readOnly = readOnly
        self.activity = activity if activity is not None else set()
        self.activity33 = activity33 if activity33 is not None else set()
        
        pass
    @property
    def readOnly(self):
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly


    @property
    def activity33(self):
        return self.__activity33

    @activity33.setter
    def activity33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_IntermediateActivities_Activity__activity33", None)
        self.__activity33 = value if value is not None else set()
        
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
        old_value = getattr(self, f"_xmof_IntermediateActivities_Activity__activity", None)
        self.__activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityNode31"):
                    opp_val = getattr(item, "ActivityNode31", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityNode31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityNode31"):
                    opp_val = getattr(item, "ActivityNode31", None)
                    
                    setattr(item, "ActivityNode31", self)
                    

class xmof_BasicBehaviors_OpaqueBehavior(Behavior):

    def __init__(self, body: str, language: str):
        self.body = body
        self.language = language
        
        pass
    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

