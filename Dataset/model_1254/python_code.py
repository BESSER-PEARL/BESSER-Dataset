from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CallConcurrencyKind(Enum):
    sequential = "sequential"
class ParameterDirectionKind(Enum):
    in = "in"
    out = "out"
    inout = "inout"
    return = "return"
class ExpansionKind(Enum):
    parallel = "parallel"
    iterative = "iterative"
    stream = "stream"


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
                if hasattr(item, "BasicActions_OutputPin229"):
                    opp_val = getattr(item, "BasicActions_OutputPin229", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin229", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin229"):
                    opp_val = getattr(item, "BasicActions_OutputPin229", None)
                    
                    setattr(item, "BasicActions_OutputPin229", self)
                    

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

    def __init__(self, locallyReentrant: bool, xmof_BasicActions_Action: set["BasicActions_OutputPin"] = None, xmof_BasicActions_Action224: "BasicActions_xmof_EClassifier" = None, xmof_BasicActions_Action226: set["BasicActions_InputPin"] = None):
        self.locallyReentrant = locallyReentrant
        self.xmof_BasicActions_Action = xmof_BasicActions_Action if xmof_BasicActions_Action is not None else set()
        self.xmof_BasicActions_Action224 = xmof_BasicActions_Action224
        self.xmof_BasicActions_Action226 = xmof_BasicActions_Action226 if xmof_BasicActions_Action226 is not None else set()
        
    @property
    def locallyReentrant(self) -> bool:
        return self.__locallyReentrant

    @locallyReentrant.setter
    def locallyReentrant(self, locallyReentrant: bool):
        self.__locallyReentrant = locallyReentrant

    @property
    def xmof_BasicActions_Action224(self):
        return self.__xmof_BasicActions_Action224

    @xmof_BasicActions_Action224.setter
    def xmof_BasicActions_Action224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_BasicActions_Action__xmof_BasicActions_Action224", None)
        self.__xmof_BasicActions_Action224 = value
        
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
                if hasattr(item, "BasicActions_OutputPin222"):
                    opp_val = getattr(item, "BasicActions_OutputPin222", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin222", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin222"):
                    opp_val = getattr(item, "BasicActions_OutputPin222", None)
                    
                    setattr(item, "BasicActions_OutputPin222", self)
                    

    @property
    def xmof_BasicActions_Action226(self):
        return self.__xmof_BasicActions_Action226

    @xmof_BasicActions_Action226.setter
    def xmof_BasicActions_Action226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_BasicActions_Action__xmof_BasicActions_Action226", None)
        self.__xmof_BasicActions_Action226 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_InputPin227"):
                    opp_val = getattr(item, "BasicActions_InputPin227", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_InputPin227", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_InputPin227"):
                    opp_val = getattr(item, "BasicActions_InputPin227", None)
                    
                    setattr(item, "BasicActions_InputPin227", self)
                    

class Communications_Trigger:

    pass
class CompleteActions_xmof_EClassifier:

    pass
class CallAction:

    pass
class xmof_BasicActions_CallOperationAction(CallAction):

    pass
class xmof_BasicActions_CallBehaviorAction(CallAction):

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
            if hasattr(old_value, "BasicActions_InputPin169"):
                opp_val = getattr(old_value, "BasicActions_InputPin169", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin169"):
                opp_val = getattr(value, "BasicActions_InputPin169", None)
                setattr(value, "BasicActions_InputPin169", self)

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
            if hasattr(old_value, "BasicActions_InputPin167"):
                opp_val = getattr(old_value, "BasicActions_InputPin167", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin167"):
                opp_val = getattr(value, "BasicActions_InputPin167", None)
                setattr(value, "BasicActions_InputPin167", self)

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
            if hasattr(old_value, "BasicActions_InputPin184"):
                opp_val = getattr(old_value, "BasicActions_InputPin184", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin184"):
                opp_val = getattr(value, "BasicActions_InputPin184", None)
                setattr(value, "BasicActions_InputPin184", self)

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
            if hasattr(old_value, "BasicActions_InputPin159"):
                opp_val = getattr(old_value, "BasicActions_InputPin159", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin159"):
                opp_val = getattr(value, "BasicActions_InputPin159", None)
                setattr(value, "BasicActions_InputPin159", self)

class StructuralFeatureAction:

    pass
class xmof_IntermediateActions_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class xmof_IntermediateActions_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class xmof_IntermediateActions_WriteStructuralFeatureAction(StructuralFeatureAction):

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
class xmof_CompleteActions_ReadIsClassifiedObjectAction(Action):

    def __init__(self, direct: bool, xmof_CompleteActions_ReadIsClassifiedObjectAction: "CompleteActions_xmof_EClassifier" = None, xmof_CompleteActions_ReadIsClassifiedObjectAction204: "BasicActions_OutputPin" = None, xmof_CompleteActions_ReadIsClassifiedObjectAction207: "BasicActions_InputPin" = None):
        self.direct = direct
        self.xmof_CompleteActions_ReadIsClassifiedObjectAction = xmof_CompleteActions_ReadIsClassifiedObjectAction
        self.xmof_CompleteActions_ReadIsClassifiedObjectAction204 = xmof_CompleteActions_ReadIsClassifiedObjectAction204
        self.xmof_CompleteActions_ReadIsClassifiedObjectAction207 = xmof_CompleteActions_ReadIsClassifiedObjectAction207
        
    @property
    def direct(self) -> bool:
        return self.__direct

    @direct.setter
    def direct(self, direct: bool):
        self.__direct = direct

    @property
    def xmof_CompleteActions_ReadIsClassifiedObjectAction204(self):
        return self.__xmof_CompleteActions_ReadIsClassifiedObjectAction204

    @xmof_CompleteActions_ReadIsClassifiedObjectAction204.setter
    def xmof_CompleteActions_ReadIsClassifiedObjectAction204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReadIsClassifiedObjectAction__xmof_CompleteActions_ReadIsClassifiedObjectAction204", None)
        self.__xmof_CompleteActions_ReadIsClassifiedObjectAction204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_OutputPin205"):
                opp_val = getattr(old_value, "BasicActions_OutputPin205", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_OutputPin205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_OutputPin205"):
                opp_val = getattr(value, "BasicActions_OutputPin205", None)
                setattr(value, "BasicActions_OutputPin205", self)

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
            if hasattr(old_value, "CompleteActions_xmof_EClassifier202"):
                opp_val = getattr(old_value, "CompleteActions_xmof_EClassifier202", None)
                if opp_val == self:
                    setattr(old_value, "CompleteActions_xmof_EClassifier202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteActions_xmof_EClassifier202"):
                opp_val = getattr(value, "CompleteActions_xmof_EClassifier202", None)
                setattr(value, "CompleteActions_xmof_EClassifier202", self)

    @property
    def xmof_CompleteActions_ReadIsClassifiedObjectAction207(self):
        return self.__xmof_CompleteActions_ReadIsClassifiedObjectAction207

    @xmof_CompleteActions_ReadIsClassifiedObjectAction207.setter
    def xmof_CompleteActions_ReadIsClassifiedObjectAction207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReadIsClassifiedObjectAction__xmof_CompleteActions_ReadIsClassifiedObjectAction207", None)
        self.__xmof_CompleteActions_ReadIsClassifiedObjectAction207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin208"):
                opp_val = getattr(old_value, "BasicActions_InputPin208", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin208"):
                opp_val = getattr(value, "BasicActions_InputPin208", None)
                setattr(value, "BasicActions_InputPin208", self)

class xmof_IntermediateActions_ValueSpecificationAction(Action):

    pass
class xmof_IntermediateActions_StructuralFeatureAction(Action):

    pass
class xmof_IntermediateActions_LinkAction(Action):

    pass
class xmof_CompleteActions_StartClassifierBehaviorAction(Action):

    pass
class xmof_CompleteActions_ReduceAction(Action):

    def __init__(self, ordered: bool, xmof_CompleteActions_ReduceAction: "BasicBehaviors_Behavior" = None, xmof_CompleteActions_ReduceAction192: "BasicActions_OutputPin" = None, xmof_CompleteActions_ReduceAction195: "BasicActions_InputPin" = None):
        self.ordered = ordered
        self.xmof_CompleteActions_ReduceAction = xmof_CompleteActions_ReduceAction
        self.xmof_CompleteActions_ReduceAction192 = xmof_CompleteActions_ReduceAction192
        self.xmof_CompleteActions_ReduceAction195 = xmof_CompleteActions_ReduceAction195
        
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
            if hasattr(old_value, "BasicBehaviors_Behavior190"):
                opp_val = getattr(old_value, "BasicBehaviors_Behavior190", None)
                if opp_val == self:
                    setattr(old_value, "BasicBehaviors_Behavior190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicBehaviors_Behavior190"):
                opp_val = getattr(value, "BasicBehaviors_Behavior190", None)
                setattr(value, "BasicBehaviors_Behavior190", self)

    @property
    def xmof_CompleteActions_ReduceAction192(self):
        return self.__xmof_CompleteActions_ReduceAction192

    @xmof_CompleteActions_ReduceAction192.setter
    def xmof_CompleteActions_ReduceAction192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReduceAction__xmof_CompleteActions_ReduceAction192", None)
        self.__xmof_CompleteActions_ReduceAction192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_OutputPin193"):
                opp_val = getattr(old_value, "BasicActions_OutputPin193", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_OutputPin193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_OutputPin193"):
                opp_val = getattr(value, "BasicActions_OutputPin193", None)
                setattr(value, "BasicActions_OutputPin193", self)

    @property
    def xmof_CompleteActions_ReduceAction195(self):
        return self.__xmof_CompleteActions_ReduceAction195

    @xmof_CompleteActions_ReduceAction195.setter
    def xmof_CompleteActions_ReduceAction195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReduceAction__xmof_CompleteActions_ReduceAction195", None)
        self.__xmof_CompleteActions_ReduceAction195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin196"):
                opp_val = getattr(old_value, "BasicActions_InputPin196", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin196"):
                opp_val = getattr(value, "BasicActions_InputPin196", None)
                setattr(value, "BasicActions_InputPin196", self)

class xmof_CompleteActions_AcceptEventAction(Action):

    def __init__(self, unmarshall: bool, xmof_CompleteActions_AcceptEventAction: set["BasicActions_OutputPin"] = None, xmof_CompleteActions_AcceptEventAction220: set["Communications_Trigger"] = None):
        self.unmarshall = unmarshall
        self.xmof_CompleteActions_AcceptEventAction = xmof_CompleteActions_AcceptEventAction if xmof_CompleteActions_AcceptEventAction is not None else set()
        self.xmof_CompleteActions_AcceptEventAction220 = xmof_CompleteActions_AcceptEventAction220 if xmof_CompleteActions_AcceptEventAction220 is not None else set()
        
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
                if hasattr(item, "BasicActions_OutputPin218"):
                    opp_val = getattr(item, "BasicActions_OutputPin218", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin218", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin218"):
                    opp_val = getattr(item, "BasicActions_OutputPin218", None)
                    
                    setattr(item, "BasicActions_OutputPin218", self)
                    

    @property
    def xmof_CompleteActions_AcceptEventAction220(self):
        return self.__xmof_CompleteActions_AcceptEventAction220

    @xmof_CompleteActions_AcceptEventAction220.setter
    def xmof_CompleteActions_AcceptEventAction220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_AcceptEventAction__xmof_CompleteActions_AcceptEventAction220", None)
        self.__xmof_CompleteActions_AcceptEventAction220 = value if value is not None else set()
        
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
                    

class xmof_IntermediateActions_ClearAssociationAction(Action):

    pass
class xmof_BasicActions_InvocationAction(Action):

    pass
class xmof_IntermediateActions_DestroyObjectAction(Action):

    def __init__(self, destroyLinks: bool, destroyOwnedObjects: bool, xmof_IntermediateActions_DestroyObjectAction: "BasicActions_InputPin" = None):
        self.destroyLinks = destroyLinks
        self.destroyOwnedObjects = destroyOwnedObjects
        self.xmof_IntermediateActions_DestroyObjectAction = xmof_IntermediateActions_DestroyObjectAction
        
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
    def xmof_IntermediateActions_DestroyObjectAction(self):
        return self.__xmof_IntermediateActions_DestroyObjectAction

    @xmof_IntermediateActions_DestroyObjectAction.setter
    def xmof_IntermediateActions_DestroyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_IntermediateActions_DestroyObjectAction__xmof_IntermediateActions_DestroyObjectAction", None)
        self.__xmof_IntermediateActions_DestroyObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin182"):
                opp_val = getattr(old_value, "BasicActions_InputPin182", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin182"):
                opp_val = getattr(value, "BasicActions_InputPin182", None)
                setattr(value, "BasicActions_InputPin182", self)

class xmof_CompleteActions_ReadExtentAction(Action):

    pass
class xmof_CompleteActions_ReclassifyObjectAction(Action):

    def __init__(self, replaceAll: bool, xmof_CompleteActions_ReclassifyObjectAction: set["CompleteActions_xmof_EClassifier"] = None, xmof_CompleteActions_ReclassifyObjectAction212: "BasicActions_InputPin" = None, xmof_CompleteActions_ReclassifyObjectAction215: set["CompleteActions_xmof_EClassifier"] = None):
        self.replaceAll = replaceAll
        self.xmof_CompleteActions_ReclassifyObjectAction = xmof_CompleteActions_ReclassifyObjectAction if xmof_CompleteActions_ReclassifyObjectAction is not None else set()
        self.xmof_CompleteActions_ReclassifyObjectAction212 = xmof_CompleteActions_ReclassifyObjectAction212
        self.xmof_CompleteActions_ReclassifyObjectAction215 = xmof_CompleteActions_ReclassifyObjectAction215 if xmof_CompleteActions_ReclassifyObjectAction215 is not None else set()
        
    @property
    def replaceAll(self) -> bool:
        return self.__replaceAll

    @replaceAll.setter
    def replaceAll(self, replaceAll: bool):
        self.__replaceAll = replaceAll

    @property
    def xmof_CompleteActions_ReclassifyObjectAction215(self):
        return self.__xmof_CompleteActions_ReclassifyObjectAction215

    @xmof_CompleteActions_ReclassifyObjectAction215.setter
    def xmof_CompleteActions_ReclassifyObjectAction215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReclassifyObjectAction__xmof_CompleteActions_ReclassifyObjectAction215", None)
        self.__xmof_CompleteActions_ReclassifyObjectAction215 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteActions_xmof_EClassifier216"):
                    opp_val = getattr(item, "CompleteActions_xmof_EClassifier216", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteActions_xmof_EClassifier216", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteActions_xmof_EClassifier216"):
                    opp_val = getattr(item, "CompleteActions_xmof_EClassifier216", None)
                    
                    setattr(item, "CompleteActions_xmof_EClassifier216", self)
                    

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
                if hasattr(item, "CompleteActions_xmof_EClassifier210"):
                    opp_val = getattr(item, "CompleteActions_xmof_EClassifier210", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteActions_xmof_EClassifier210", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteActions_xmof_EClassifier210"):
                    opp_val = getattr(item, "CompleteActions_xmof_EClassifier210", None)
                    
                    setattr(item, "CompleteActions_xmof_EClassifier210", self)
                    

    @property
    def xmof_CompleteActions_ReclassifyObjectAction212(self):
        return self.__xmof_CompleteActions_ReclassifyObjectAction212

    @xmof_CompleteActions_ReclassifyObjectAction212.setter
    def xmof_CompleteActions_ReclassifyObjectAction212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReclassifyObjectAction__xmof_CompleteActions_ReclassifyObjectAction212", None)
        self.__xmof_CompleteActions_ReclassifyObjectAction212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin213"):
                opp_val = getattr(old_value, "BasicActions_InputPin213", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin213"):
                opp_val = getattr(value, "BasicActions_InputPin213", None)
                setattr(value, "BasicActions_InputPin213", self)

class xmof_IntermediateActions_CreateObjectAction(Action):

    pass
class xmof_IntermediateActions_ReadSelfAction(Action):

    pass
class xmof_IntermediateActions_TestIdentityAction(Action):

    pass
class xmof_CompleteStructuredActivities_StructuredActivityNode(Action):

    def __init__(self, mustIsolate: bool, Activities106: set["IntermediateActivities_ActivityNode"] = None, Activities109: set["IntermediateActivities_ActivityEdge"] = None, xmof_CompleteStructuredActivities_StructuredActivityNode: set["BasicActions_OutputPin"] = None, xmof_CompleteStructuredActivities_StructuredActivityNode114: set["BasicActions_InputPin"] = None):
        self.mustIsolate = mustIsolate
        self.Activities106 = Activities106 if Activities106 is not None else set()
        self.Activities109 = Activities109 if Activities109 is not None else set()
        self.xmof_CompleteStructuredActivities_StructuredActivityNode = xmof_CompleteStructuredActivities_StructuredActivityNode if xmof_CompleteStructuredActivities_StructuredActivityNode is not None else set()
        self.xmof_CompleteStructuredActivities_StructuredActivityNode114 = xmof_CompleteStructuredActivities_StructuredActivityNode114 if xmof_CompleteStructuredActivities_StructuredActivityNode114 is not None else set()
        
    @property
    def mustIsolate(self) -> bool:
        return self.__mustIsolate

    @mustIsolate.setter
    def mustIsolate(self, mustIsolate: bool):
        self.__mustIsolate = mustIsolate

    @property
    def Activities109(self):
        return self.__Activities109

    @Activities109.setter
    def Activities109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_StructuredActivityNode__Activities109", None)
        self.__Activities109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax110"):
                    opp_val = getattr(item, "Syntax110", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax110"):
                    opp_val = getattr(item, "Syntax110", None)
                    
                    setattr(item, "Syntax110", self)
                    

    @property
    def Activities106(self):
        return self.__Activities106

    @Activities106.setter
    def Activities106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_StructuredActivityNode__Activities106", None)
        self.__Activities106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax107"):
                    opp_val = getattr(item, "Syntax107", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax107"):
                    opp_val = getattr(item, "Syntax107", None)
                    
                    setattr(item, "Syntax107", self)
                    

    @property
    def xmof_CompleteStructuredActivities_StructuredActivityNode114(self):
        return self.__xmof_CompleteStructuredActivities_StructuredActivityNode114

    @xmof_CompleteStructuredActivities_StructuredActivityNode114.setter
    def xmof_CompleteStructuredActivities_StructuredActivityNode114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_StructuredActivityNode__xmof_CompleteStructuredActivities_StructuredActivityNode114", None)
        self.__xmof_CompleteStructuredActivities_StructuredActivityNode114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_InputPin115"):
                    opp_val = getattr(item, "BasicActions_InputPin115", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_InputPin115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_InputPin115"):
                    opp_val = getattr(item, "BasicActions_InputPin115", None)
                    
                    setattr(item, "BasicActions_InputPin115", self)
                    

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
                if hasattr(item, "BasicActions_OutputPin112"):
                    opp_val = getattr(item, "BasicActions_OutputPin112", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin112", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin112"):
                    opp_val = getattr(item, "BasicActions_OutputPin112", None)
                    
                    setattr(item, "BasicActions_OutputPin112", self)
                    

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
class xmof_CompleteStructuredActivities_ConditionalNode(StructuredActivityNode):

    def __init__(self, determinate: bool, assured: bool, xmof_CompleteStructuredActivities_ConditionalNode: set["CompleteStructuredActivities_Clause"] = None, xmof_CompleteStructuredActivities_ConditionalNode103: set["BasicActions_OutputPin"] = None):
        self.determinate = determinate
        self.assured = assured
        self.xmof_CompleteStructuredActivities_ConditionalNode = xmof_CompleteStructuredActivities_ConditionalNode if xmof_CompleteStructuredActivities_ConditionalNode is not None else set()
        self.xmof_CompleteStructuredActivities_ConditionalNode103 = xmof_CompleteStructuredActivities_ConditionalNode103 if xmof_CompleteStructuredActivities_ConditionalNode103 is not None else set()
        
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
    def xmof_CompleteStructuredActivities_ConditionalNode103(self):
        return self.__xmof_CompleteStructuredActivities_ConditionalNode103

    @xmof_CompleteStructuredActivities_ConditionalNode103.setter
    def xmof_CompleteStructuredActivities_ConditionalNode103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_ConditionalNode__xmof_CompleteStructuredActivities_ConditionalNode103", None)
        self.__xmof_CompleteStructuredActivities_ConditionalNode103 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin104"):
                    opp_val = getattr(item, "BasicActions_OutputPin104", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin104"):
                    opp_val = getattr(item, "BasicActions_OutputPin104", None)
                    
                    setattr(item, "BasicActions_OutputPin104", self)
                    

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
                    

class xmof_ExtraStructuredActivities_ExpansionRegion(StructuredActivityNode):

    def __init__(self, mode: str, Activities123: set["ExtraStructuredActivities_ExpansionNode"] = None, Activities126: set["ExtraStructuredActivities_ExpansionNode"] = None):
        self.mode = mode
        self.Activities123 = Activities123 if Activities123 is not None else set()
        self.Activities126 = Activities126 if Activities126 is not None else set()
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def Activities123(self):
        return self.__Activities123

    @Activities123.setter
    def Activities123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_ExtraStructuredActivities_ExpansionRegion__Activities123", None)
        self.__Activities123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax124"):
                    opp_val = getattr(item, "Syntax124", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax124", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax124"):
                    opp_val = getattr(item, "Syntax124", None)
                    
                    setattr(item, "Syntax124", self)
                    

    @property
    def Activities126(self):
        return self.__Activities126

    @Activities126.setter
    def Activities126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_ExtraStructuredActivities_ExpansionRegion__Activities126", None)
        self.__Activities126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax127"):
                    opp_val = getattr(item, "Syntax127", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax127"):
                    opp_val = getattr(item, "Syntax127", None)
                    
                    setattr(item, "Syntax127", self)
                    

class xmof_CompleteStructuredActivities_LoopNode(StructuredActivityNode):

    def __init__(self, testedFirst: bool, xmof_CompleteStructuredActivities_LoopNode: "BasicActions_OutputPin" = None, xmof_CompleteStructuredActivities_LoopNode66: set["CompleteStructuredActivities_ExecutableNode"] = None, xmof_CompleteStructuredActivities_LoopNode68: set["BasicActions_OutputPin"] = None, xmof_CompleteStructuredActivities_LoopNode71: set["BasicActions_InputPin"] = None, xmof_CompleteStructuredActivities_LoopNode73: set["CompleteStructuredActivities_ExecutableNode"] = None, xmof_CompleteStructuredActivities_LoopNode76: set["BasicActions_OutputPin"] = None, xmof_CompleteStructuredActivities_LoopNode79: set["BasicActions_OutputPin"] = None, xmof_CompleteStructuredActivities_LoopNode82: set["CompleteStructuredActivities_ExecutableNode"] = None):
        self.testedFirst = testedFirst
        self.xmof_CompleteStructuredActivities_LoopNode = xmof_CompleteStructuredActivities_LoopNode
        self.xmof_CompleteStructuredActivities_LoopNode66 = xmof_CompleteStructuredActivities_LoopNode66 if xmof_CompleteStructuredActivities_LoopNode66 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode68 = xmof_CompleteStructuredActivities_LoopNode68 if xmof_CompleteStructuredActivities_LoopNode68 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode71 = xmof_CompleteStructuredActivities_LoopNode71 if xmof_CompleteStructuredActivities_LoopNode71 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode73 = xmof_CompleteStructuredActivities_LoopNode73 if xmof_CompleteStructuredActivities_LoopNode73 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode76 = xmof_CompleteStructuredActivities_LoopNode76 if xmof_CompleteStructuredActivities_LoopNode76 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode79 = xmof_CompleteStructuredActivities_LoopNode79 if xmof_CompleteStructuredActivities_LoopNode79 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode82 = xmof_CompleteStructuredActivities_LoopNode82 if xmof_CompleteStructuredActivities_LoopNode82 is not None else set()
        
    @property
    def testedFirst(self) -> bool:
        return self.__testedFirst

    @testedFirst.setter
    def testedFirst(self, testedFirst: bool):
        self.__testedFirst = testedFirst

    @property
    def xmof_CompleteStructuredActivities_LoopNode82(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode82

    @xmof_CompleteStructuredActivities_LoopNode82.setter
    def xmof_CompleteStructuredActivities_LoopNode82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode82", None)
        self.__xmof_CompleteStructuredActivities_LoopNode82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode83"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode83", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteStructuredActivities_ExecutableNode83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode83"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode83", None)
                    
                    setattr(item, "CompleteStructuredActivities_ExecutableNode83", self)
                    

    @property
    def xmof_CompleteStructuredActivities_LoopNode79(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode79

    @xmof_CompleteStructuredActivities_LoopNode79.setter
    def xmof_CompleteStructuredActivities_LoopNode79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode79", None)
        self.__xmof_CompleteStructuredActivities_LoopNode79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin80"):
                    opp_val = getattr(item, "BasicActions_OutputPin80", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin80"):
                    opp_val = getattr(item, "BasicActions_OutputPin80", None)
                    
                    setattr(item, "BasicActions_OutputPin80", self)
                    

    @property
    def xmof_CompleteStructuredActivities_LoopNode66(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode66

    @xmof_CompleteStructuredActivities_LoopNode66.setter
    def xmof_CompleteStructuredActivities_LoopNode66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode66", None)
        self.__xmof_CompleteStructuredActivities_LoopNode66 = value if value is not None else set()
        
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
    def xmof_CompleteStructuredActivities_LoopNode71(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode71

    @xmof_CompleteStructuredActivities_LoopNode71.setter
    def xmof_CompleteStructuredActivities_LoopNode71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode71", None)
        self.__xmof_CompleteStructuredActivities_LoopNode71 = value if value is not None else set()
        
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
    def xmof_CompleteStructuredActivities_LoopNode73(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode73

    @xmof_CompleteStructuredActivities_LoopNode73.setter
    def xmof_CompleteStructuredActivities_LoopNode73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode73", None)
        self.__xmof_CompleteStructuredActivities_LoopNode73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode74"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode74", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteStructuredActivities_ExecutableNode74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode74"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode74", None)
                    
                    setattr(item, "CompleteStructuredActivities_ExecutableNode74", self)
                    

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
    def xmof_CompleteStructuredActivities_LoopNode68(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode68

    @xmof_CompleteStructuredActivities_LoopNode68.setter
    def xmof_CompleteStructuredActivities_LoopNode68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode68", None)
        self.__xmof_CompleteStructuredActivities_LoopNode68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin69"):
                    opp_val = getattr(item, "BasicActions_OutputPin69", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin69"):
                    opp_val = getattr(item, "BasicActions_OutputPin69", None)
                    
                    setattr(item, "BasicActions_OutputPin69", self)
                    

    @property
    def xmof_CompleteStructuredActivities_LoopNode76(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode76

    @xmof_CompleteStructuredActivities_LoopNode76.setter
    def xmof_CompleteStructuredActivities_LoopNode76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode76", None)
        self.__xmof_CompleteStructuredActivities_LoopNode76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin77"):
                    opp_val = getattr(item, "BasicActions_OutputPin77", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin77"):
                    opp_val = getattr(item, "BasicActions_OutputPin77", None)
                    
                    setattr(item, "BasicActions_OutputPin77", self)
                    

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
class xmof_IntermediateActivities_FinalNode(ControlNode):

    pass
class xmof_IntermediateActivities_DecisionNode(ControlNode):

    pass
class xmof_IntermediateActivities_JoinNode(ControlNode):

    pass
class xmof_IntermediateActivities_ForkNode(ControlNode):

    pass
class xmof_IntermediateActivities_InitialNode(ControlNode):

    pass
class xmof_IntermediateActivities_MergeNode(ControlNode):

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
class xmof_Kernel_LiteralString(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class xmof_Kernel_LiteralNull(LiteralSpecification):

    pass
class xmof_Kernel_LiteralUnlimitedNatural(LiteralSpecification):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class xmof_Kernel_LiteralInteger(LiteralSpecification):

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
class Kernel_xmof_EClassifier:

    pass
class ETypedElement:

    pass
class xmof_IntermediateActivities_ObjectNode(IntermediateActivities_ActivityNode, ETypedElement):

    pass
class xmof_BasicActions_Pin(IntermediateActivities_ObjectNode, ETypedElement):

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
        
    @property
    def direction(self) -> str:
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
class xmof_IntermediateActivities_ActivityNode(ENamedElement):

    pass
class xmof_Communications_Event(ENamedElement):

    pass
class xmof_IntermediateActivities_ActivityEdge(ENamedElement):

    pass
class xmof_Kernel_InstanceSpecification(ENamedElement):

    pass
class xmof_Communications_Trigger(ENamedElement):

    pass
class OpaqueBehavior:

    pass
class xmof_BasicBehaviors_FunctionBehavior(OpaqueBehavior):

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
class xmof_Kernel_BehavioredEClass(EClass, BasicBehaviors_BehavioredClassifier):

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

class Behavior:

    pass
class xmof_IntermediateActivities_Activity(Behavior):

    def __init__(self, readOnly: bool, Activities41: set["IntermediateActivities_ActivityNode"] = None, Activities44: set["IntermediateActivities_ActivityEdge"] = None):
        self.readOnly = readOnly
        self.Activities41 = Activities41 if Activities41 is not None else set()
        self.Activities44 = Activities44 if Activities44 is not None else set()
        
    @property
    def readOnly(self) -> bool:
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly

    @property
    def Activities44(self):
        return self.__Activities44

    @Activities44.setter
    def Activities44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_IntermediateActivities_Activity__Activities44", None)
        self.__Activities44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax45"):
                    opp_val = getattr(item, "Syntax45", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax45"):
                    opp_val = getattr(item, "Syntax45", None)
                    
                    setattr(item, "Syntax45", self)
                    

    @property
    def Activities41(self):
        return self.__Activities41

    @Activities41.setter
    def Activities41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_IntermediateActivities_Activity__Activities41", None)
        self.__Activities41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Syntax42"):
                    opp_val = getattr(item, "Syntax42", None)
                    
                    if opp_val == self:
                        setattr(item, "Syntax42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Syntax42"):
                    opp_val = getattr(item, "Syntax42", None)
                    
                    setattr(item, "Syntax42", self)
                    

class xmof_BasicBehaviors_OpaqueBehavior(Behavior):

    def __init__(self, body: str, language: str):
        self.body = body
        self.language = language
        
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
