from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class WriteVariableAction:

    pass
class ActionsProv_RemoveVariableValueAction(WriteVariableAction):

    pass
class ActionsProv_AddVariableValueAction(WriteVariableAction):

    pass
class VariableAction:

    pass
class ActionsProv_ClearVariableAction(VariableAction):

    pass
class ActionsProv_WriteVariableAction(VariableAction):

    pass
class ActionsProv_ReadVariableAction(VariableAction):

    pass
class CreateLinkAction:

    pass
class ActionsProv_CreateLinkObjectAction(CreateLinkAction):

    pass
class ActionsProv_ReadlsClassifiedObjectAction:

    pass
class AcceptEventAction:

    pass
class ActionsProv_AcceptCallAction(AcceptEventAction):

    pass
class LinkEndData:

    pass
class ActionsProv_LinkEndDestructionData(LinkEndData):

    def __init__(self, isDestroyDuplicates: bool, ActionsProv_LinkEndDestructionData: "ActionsProv_InputPin" = None):
        self.isDestroyDuplicates = isDestroyDuplicates
        self.ActionsProv_LinkEndDestructionData = ActionsProv_LinkEndDestructionData
        
    @property
    def isDestroyDuplicates(self) -> bool:
        return self.__isDestroyDuplicates

    @isDestroyDuplicates.setter
    def isDestroyDuplicates(self, isDestroyDuplicates: bool):
        self.__isDestroyDuplicates = isDestroyDuplicates

    @property
    def ActionsProv_LinkEndDestructionData(self):
        return self.__ActionsProv_LinkEndDestructionData

    @ActionsProv_LinkEndDestructionData.setter
    def ActionsProv_LinkEndDestructionData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActionsProv_LinkEndDestructionData__ActionsProv_LinkEndDestructionData", None)
        self.__ActionsProv_LinkEndDestructionData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActionsProv_InputPin66"):
                opp_val = getattr(old_value, "ActionsProv_InputPin66", None)
                if opp_val == self:
                    setattr(old_value, "ActionsProv_InputPin66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionsProv_InputPin66"):
                opp_val = getattr(value, "ActionsProv_InputPin66", None)
                setattr(value, "ActionsProv_InputPin66", self)

class ActionsProv_LinkEndCreationData(LinkEndData):

    def __init__(self, isReplaceAll: bool, ActionsProv_LinkEndCreationData: "ActionsProv_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.ActionsProv_LinkEndCreationData = ActionsProv_LinkEndCreationData
        
    @property
    def isReplaceAll(self) -> bool:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: bool):
        self.__isReplaceAll = isReplaceAll

    @property
    def ActionsProv_LinkEndCreationData(self):
        return self.__ActionsProv_LinkEndCreationData

    @ActionsProv_LinkEndCreationData.setter
    def ActionsProv_LinkEndCreationData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActionsProv_LinkEndCreationData__ActionsProv_LinkEndCreationData", None)
        self.__ActionsProv_LinkEndCreationData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActionsProv_InputPin64"):
                opp_val = getattr(old_value, "ActionsProv_InputPin64", None)
                if opp_val == self:
                    setattr(old_value, "ActionsProv_InputPin64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionsProv_InputPin64"):
                opp_val = getattr(value, "ActionsProv_InputPin64", None)
                setattr(value, "ActionsProv_InputPin64", self)

class WriteLinkAction:

    pass
class ActionsProv_DestroyLinkAction(WriteLinkAction):

    pass
class ActionsProv_CreateLinkAction(WriteLinkAction):

    pass
class LinkAction:

    pass
class ActionsProv_WriteLinkAction(LinkAction):

    pass
class ActionsProv_ReadLinkAction(LinkAction):

    pass
class ActionsProv_QualifierValue:

    pass
class ActionsProv_LinkEndData(ABC):

    pass
class WriteStructuralFeatureAction:

    pass
class ActionsProv_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class ActionsProv_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class StructuralFeatureAction:

    pass
class ActionsProv_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class ActionsProv_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class ActionsProv_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class ActionsProv_CallOperationAction:

    pass
class CallAction:

    pass
class ActionsProv_StartObjectBehaviorAction(CallAction):

    pass
class ActionsProv_CallBehaviorAction(CallAction):

    pass
class InvocationAction:

    pass
class ActionsProv_BroadcastSignalAction(InvocationAction):

    pass
class ActionsProv_SendObjectAction(InvocationAction):

    pass
class ActionsProv_SendSignalAction(InvocationAction):

    pass
class ActionsProv_CallAction(InvocationAction):

    def __init__(self, isSynchronous: bool, ActionsProv_CallAction: set["ActionsProv_OutputPin"] = None):
        self.isSynchronous = isSynchronous
        self.ActionsProv_CallAction = ActionsProv_CallAction if ActionsProv_CallAction is not None else set()
        
    @property
    def isSynchronous(self) -> bool:
        return self.__isSynchronous

    @isSynchronous.setter
    def isSynchronous(self, isSynchronous: bool):
        self.__isSynchronous = isSynchronous

    @property
    def ActionsProv_CallAction(self):
        return self.__ActionsProv_CallAction

    @ActionsProv_CallAction.setter
    def ActionsProv_CallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActionsProv_CallAction__ActionsProv_CallAction", None)
        self.__ActionsProv_CallAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActionsProv_OutputPin11"):
                    opp_val = getattr(item, "ActionsProv_OutputPin11", None)
                    
                    if opp_val == self:
                        setattr(item, "ActionsProv_OutputPin11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActionsProv_OutputPin11"):
                    opp_val = getattr(item, "ActionsProv_OutputPin11", None)
                    
                    setattr(item, "ActionsProv_OutputPin11", self)
                    

class InputPin:

    pass
class ActionsProv_ActionInputPin(InputPin):

    pass
class ActionsProv_ValuePin(InputPin):

    pass
class ActionsProv_Pin(ABC):

    pass
class Pin:

    pass
class Action:

    pass
class ActionsProv_ReadSelfAction(Action):

    pass
class ActionsProv_UnmarshallAction(Action):

    pass
class ActionsProv_AcceptEventAction(Action):

    def __init__(self, isUnmarshall: bool, ActionsProv_AcceptEventAction: set["ActionsProv_OutputPin"] = None):
        self.isUnmarshall = isUnmarshall
        self.ActionsProv_AcceptEventAction = ActionsProv_AcceptEventAction if ActionsProv_AcceptEventAction is not None else set()
        
    @property
    def isUnmarshall(self) -> bool:
        return self.__isUnmarshall

    @isUnmarshall.setter
    def isUnmarshall(self, isUnmarshall: bool):
        self.__isUnmarshall = isUnmarshall

    @property
    def ActionsProv_AcceptEventAction(self):
        return self.__ActionsProv_AcceptEventAction

    @ActionsProv_AcceptEventAction.setter
    def ActionsProv_AcceptEventAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActionsProv_AcceptEventAction__ActionsProv_AcceptEventAction", None)
        self.__ActionsProv_AcceptEventAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActionsProv_OutputPin78"):
                    opp_val = getattr(item, "ActionsProv_OutputPin78", None)
                    
                    if opp_val == self:
                        setattr(item, "ActionsProv_OutputPin78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActionsProv_OutputPin78"):
                    opp_val = getattr(item, "ActionsProv_OutputPin78", None)
                    
                    setattr(item, "ActionsProv_OutputPin78", self)
                    

class ActionsProv_CreateObjectAction(Action):

    pass
class ActionsProv_ReadLinkObjectEndQualifierAction(Action):

    pass
class ActionsProv_DestroyObjectAction(Action):

    pass
class ActionsProv_LinkAction(Action):

    pass
class ActionsProv_ValueSpecificationAction(Action):

    pass
class ActionsProv_ReduceAction(Action):

    def __init__(self, isOrdered: bool, ActionsProv_ReduceAction: "ActionsProv_OutputPin" = None, ActionsProv_ReduceAction112: "ActionsProv_InputPin" = None):
        self.isOrdered = isOrdered
        self.ActionsProv_ReduceAction = ActionsProv_ReduceAction
        self.ActionsProv_ReduceAction112 = ActionsProv_ReduceAction112
        
    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def ActionsProv_ReduceAction(self):
        return self.__ActionsProv_ReduceAction

    @ActionsProv_ReduceAction.setter
    def ActionsProv_ReduceAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActionsProv_ReduceAction__ActionsProv_ReduceAction", None)
        self.__ActionsProv_ReduceAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActionsProv_OutputPin110"):
                opp_val = getattr(old_value, "ActionsProv_OutputPin110", None)
                if opp_val == self:
                    setattr(old_value, "ActionsProv_OutputPin110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionsProv_OutputPin110"):
                opp_val = getattr(value, "ActionsProv_OutputPin110", None)
                setattr(value, "ActionsProv_OutputPin110", self)

    @property
    def ActionsProv_ReduceAction112(self):
        return self.__ActionsProv_ReduceAction112

    @ActionsProv_ReduceAction112.setter
    def ActionsProv_ReduceAction112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActionsProv_ReduceAction__ActionsProv_ReduceAction112", None)
        self.__ActionsProv_ReduceAction112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActionsProv_InputPin113"):
                opp_val = getattr(old_value, "ActionsProv_InputPin113", None)
                if opp_val == self:
                    setattr(old_value, "ActionsProv_InputPin113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionsProv_InputPin113"):
                opp_val = getattr(value, "ActionsProv_InputPin113", None)
                setattr(value, "ActionsProv_InputPin113", self)

class ActionsProv_ReplyAction(Action):

    pass
class ActionsProv_RaiseExceptionAction(Action):

    pass
class ActionsProv_ReadExtendAction(Action):

    pass
class ActionsProv_InvocationAction(Action):

    pass
class ActionsProv_TestIdentityAction(Action):

    pass
class ActionsProv_ReadLinkObjectEndAction(Action):

    pass
class ActionsProv_StructuralFeatureAction(Action):

    pass
class ActionsProv_StartClassifierBehaviorAction(Action):

    pass
class ActionsProv_VariableAction(Action):

    pass
class ActionsProv_ReclassifyObjectAction(Action):

    def __init__(self, isReplaceAll: bool, ActionsProv_ReclassifyObjectAction: "ActionsProv_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.ActionsProv_ReclassifyObjectAction = ActionsProv_ReclassifyObjectAction
        
    @property
    def isReplaceAll(self) -> bool:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: bool):
        self.__isReplaceAll = isReplaceAll

    @property
    def ActionsProv_ReclassifyObjectAction(self):
        return self.__ActionsProv_ReclassifyObjectAction

    @ActionsProv_ReclassifyObjectAction.setter
    def ActionsProv_ReclassifyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActionsProv_ReclassifyObjectAction__ActionsProv_ReclassifyObjectAction", None)
        self.__ActionsProv_ReclassifyObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActionsProv_InputPin84"):
                opp_val = getattr(old_value, "ActionsProv_InputPin84", None)
                if opp_val == self:
                    setattr(old_value, "ActionsProv_InputPin84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionsProv_InputPin84"):
                opp_val = getattr(value, "ActionsProv_InputPin84", None)
                setattr(value, "ActionsProv_InputPin84", self)

class ActionsProv_OpaqueAction(Action):

    def __init__(self, body: str, language: str, ActionsProv_OpaqueAction: set["ActionsProv_InputPin"] = None, ActionsProv_OpaqueAction6: set["ActionsProv_OutputPin"] = None):
        self.body = body
        self.language = language
        self.ActionsProv_OpaqueAction = ActionsProv_OpaqueAction if ActionsProv_OpaqueAction is not None else set()
        self.ActionsProv_OpaqueAction6 = ActionsProv_OpaqueAction6 if ActionsProv_OpaqueAction6 is not None else set()
        
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
    def ActionsProv_OpaqueAction6(self):
        return self.__ActionsProv_OpaqueAction6

    @ActionsProv_OpaqueAction6.setter
    def ActionsProv_OpaqueAction6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActionsProv_OpaqueAction__ActionsProv_OpaqueAction6", None)
        self.__ActionsProv_OpaqueAction6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActionsProv_OutputPin7"):
                    opp_val = getattr(item, "ActionsProv_OutputPin7", None)
                    
                    if opp_val == self:
                        setattr(item, "ActionsProv_OutputPin7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActionsProv_OutputPin7"):
                    opp_val = getattr(item, "ActionsProv_OutputPin7", None)
                    
                    setattr(item, "ActionsProv_OutputPin7", self)
                    

    @property
    def ActionsProv_OpaqueAction(self):
        return self.__ActionsProv_OpaqueAction

    @ActionsProv_OpaqueAction.setter
    def ActionsProv_OpaqueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActionsProv_OpaqueAction__ActionsProv_OpaqueAction", None)
        self.__ActionsProv_OpaqueAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActionsProv_InputPin4"):
                    opp_val = getattr(item, "ActionsProv_InputPin4", None)
                    
                    if opp_val == self:
                        setattr(item, "ActionsProv_InputPin4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActionsProv_InputPin4"):
                    opp_val = getattr(item, "ActionsProv_InputPin4", None)
                    
                    setattr(item, "ActionsProv_InputPin4", self)
                    

class ActionsProv_InputPin(Pin):

    pass
class ActionsProv_Action(ABC):

    pass
class ActionsProv_OutputPin(Pin):

    pass