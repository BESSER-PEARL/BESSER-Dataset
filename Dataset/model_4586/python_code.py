from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class StructuredActivityNode:

    pass
class ActivitiesProv_LoopNode(StructuredActivityNode):

    def __init__(self, isTestedFirst: bool, ActivitiesProv_LoopNode100: set["ActivitiesProv_ExecutableNode"] = None, ActivitiesProv_LoopNode: set["ActivitiesProv_ExecutableNode"] = None, ActivitiesProv_LoopNode97: set["ActivitiesProv_ExecutableNode"] = None):
        self.isTestedFirst = isTestedFirst
        self.ActivitiesProv_LoopNode100 = ActivitiesProv_LoopNode100 if ActivitiesProv_LoopNode100 is not None else set()
        self.ActivitiesProv_LoopNode = ActivitiesProv_LoopNode if ActivitiesProv_LoopNode is not None else set()
        self.ActivitiesProv_LoopNode97 = ActivitiesProv_LoopNode97 if ActivitiesProv_LoopNode97 is not None else set()
        
    @property
    def isTestedFirst(self) -> bool:
        return self.__isTestedFirst

    @isTestedFirst.setter
    def isTestedFirst(self, isTestedFirst: bool):
        self.__isTestedFirst = isTestedFirst

    @property
    def ActivitiesProv_LoopNode97(self):
        return self.__ActivitiesProv_LoopNode97

    @ActivitiesProv_LoopNode97.setter
    def ActivitiesProv_LoopNode97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivitiesProv_LoopNode__ActivitiesProv_LoopNode97", None)
        self.__ActivitiesProv_LoopNode97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivitiesProv_ExecutableNode98"):
                    opp_val = getattr(item, "ActivitiesProv_ExecutableNode98", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivitiesProv_ExecutableNode98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivitiesProv_ExecutableNode98"):
                    opp_val = getattr(item, "ActivitiesProv_ExecutableNode98", None)
                    
                    setattr(item, "ActivitiesProv_ExecutableNode98", self)
                    

    @property
    def ActivitiesProv_LoopNode100(self):
        return self.__ActivitiesProv_LoopNode100

    @ActivitiesProv_LoopNode100.setter
    def ActivitiesProv_LoopNode100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivitiesProv_LoopNode__ActivitiesProv_LoopNode100", None)
        self.__ActivitiesProv_LoopNode100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivitiesProv_ExecutableNode101"):
                    opp_val = getattr(item, "ActivitiesProv_ExecutableNode101", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivitiesProv_ExecutableNode101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivitiesProv_ExecutableNode101"):
                    opp_val = getattr(item, "ActivitiesProv_ExecutableNode101", None)
                    
                    setattr(item, "ActivitiesProv_ExecutableNode101", self)
                    

    @property
    def ActivitiesProv_LoopNode(self):
        return self.__ActivitiesProv_LoopNode

    @ActivitiesProv_LoopNode.setter
    def ActivitiesProv_LoopNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivitiesProv_LoopNode__ActivitiesProv_LoopNode", None)
        self.__ActivitiesProv_LoopNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivitiesProv_ExecutableNode95"):
                    opp_val = getattr(item, "ActivitiesProv_ExecutableNode95", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivitiesProv_ExecutableNode95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivitiesProv_ExecutableNode95"):
                    opp_val = getattr(item, "ActivitiesProv_ExecutableNode95", None)
                    
                    setattr(item, "ActivitiesProv_ExecutableNode95", self)
                    

class ActivitiesProv_ExceptionHandler:

    pass
class ActivitiesProv_ExpansionRegion(StructuredActivityNode):

    pass
class ActivitiesProv_SequenceNode(StructuredActivityNode):

    pass
class ActivitiesProv_Clause:

    pass
class ActivitiesProv_ConditionalNode(StructuredActivityNode):

    def __init__(self, isDeterminate: bool, isAssumed: bool, ActivitiesProv_ConditionalNode: set["ActivitiesProv_Clause"] = None, ActivitiesProv_ConditionalNode104: set["ActivitiesProv_ExecutableNode"] = None, ActivitiesProv_ConditionalNode107: set["ActivitiesProv_ExecutableNode"] = None):
        self.isDeterminate = isDeterminate
        self.isAssumed = isAssumed
        self.ActivitiesProv_ConditionalNode = ActivitiesProv_ConditionalNode if ActivitiesProv_ConditionalNode is not None else set()
        self.ActivitiesProv_ConditionalNode104 = ActivitiesProv_ConditionalNode104 if ActivitiesProv_ConditionalNode104 is not None else set()
        self.ActivitiesProv_ConditionalNode107 = ActivitiesProv_ConditionalNode107 if ActivitiesProv_ConditionalNode107 is not None else set()
        
    @property
    def isAssumed(self) -> bool:
        return self.__isAssumed

    @isAssumed.setter
    def isAssumed(self, isAssumed: bool):
        self.__isAssumed = isAssumed

    @property
    def isDeterminate(self) -> bool:
        return self.__isDeterminate

    @isDeterminate.setter
    def isDeterminate(self, isDeterminate: bool):
        self.__isDeterminate = isDeterminate

    @property
    def ActivitiesProv_ConditionalNode(self):
        return self.__ActivitiesProv_ConditionalNode

    @ActivitiesProv_ConditionalNode.setter
    def ActivitiesProv_ConditionalNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivitiesProv_ConditionalNode__ActivitiesProv_ConditionalNode", None)
        self.__ActivitiesProv_ConditionalNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivitiesProv_Clause"):
                    opp_val = getattr(item, "ActivitiesProv_Clause", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivitiesProv_Clause", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivitiesProv_Clause"):
                    opp_val = getattr(item, "ActivitiesProv_Clause", None)
                    
                    setattr(item, "ActivitiesProv_Clause", self)
                    

    @property
    def ActivitiesProv_ConditionalNode104(self):
        return self.__ActivitiesProv_ConditionalNode104

    @ActivitiesProv_ConditionalNode104.setter
    def ActivitiesProv_ConditionalNode104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivitiesProv_ConditionalNode__ActivitiesProv_ConditionalNode104", None)
        self.__ActivitiesProv_ConditionalNode104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivitiesProv_ExecutableNode105"):
                    opp_val = getattr(item, "ActivitiesProv_ExecutableNode105", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivitiesProv_ExecutableNode105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivitiesProv_ExecutableNode105"):
                    opp_val = getattr(item, "ActivitiesProv_ExecutableNode105", None)
                    
                    setattr(item, "ActivitiesProv_ExecutableNode105", self)
                    

    @property
    def ActivitiesProv_ConditionalNode107(self):
        return self.__ActivitiesProv_ConditionalNode107

    @ActivitiesProv_ConditionalNode107.setter
    def ActivitiesProv_ConditionalNode107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivitiesProv_ConditionalNode__ActivitiesProv_ConditionalNode107", None)
        self.__ActivitiesProv_ConditionalNode107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivitiesProv_ExecutableNode108"):
                    opp_val = getattr(item, "ActivitiesProv_ExecutableNode108", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivitiesProv_ExecutableNode108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivitiesProv_ExecutableNode108"):
                    opp_val = getattr(item, "ActivitiesProv_ExecutableNode108", None)
                    
                    setattr(item, "ActivitiesProv_ExecutableNode108", self)
                    

class ExecutableNode:

    pass
class ActivitiesProv_ParameterSet:

    pass
class CentralBufferNode:

    pass
class ActivitiesProv_DataStoreNode(CentralBufferNode):

    pass
class ActivityGroup:

    pass
class ActivityEdge:

    pass
class ActivitiesProv_ObjectFlow(ActivityEdge):

    def __init__(self, isMulticast: bool, isMultireceive: bool, isControlType: bool, ActivitiesProv_ObjectFlow: "ActivitiesProv_DecisionNode" = None):
        self.isMulticast = isMulticast
        self.isMultireceive = isMultireceive
        self.isControlType = isControlType
        self.ActivitiesProv_ObjectFlow = ActivitiesProv_ObjectFlow
        
    @property
    def isMulticast(self) -> bool:
        return self.__isMulticast

    @isMulticast.setter
    def isMulticast(self, isMulticast: bool):
        self.__isMulticast = isMulticast

    @property
    def isMultireceive(self) -> bool:
        return self.__isMultireceive

    @isMultireceive.setter
    def isMultireceive(self, isMultireceive: bool):
        self.__isMultireceive = isMultireceive

    @property
    def isControlType(self) -> bool:
        return self.__isControlType

    @isControlType.setter
    def isControlType(self, isControlType: bool):
        self.__isControlType = isControlType

    @property
    def ActivitiesProv_ObjectFlow(self):
        return self.__ActivitiesProv_ObjectFlow

    @ActivitiesProv_ObjectFlow.setter
    def ActivitiesProv_ObjectFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivitiesProv_ObjectFlow__ActivitiesProv_ObjectFlow", None)
        self.__ActivitiesProv_ObjectFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivitiesProv_DecisionNode"):
                opp_val = getattr(old_value, "ActivitiesProv_DecisionNode", None)
                if opp_val == self:
                    setattr(old_value, "ActivitiesProv_DecisionNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivitiesProv_DecisionNode"):
                opp_val = getattr(value, "ActivitiesProv_DecisionNode", None)
                setattr(value, "ActivitiesProv_DecisionNode", self)

class ActivitiesProv_ControlFlow(ActivityEdge):

    pass
class FinalNode:

    pass
class ActivitiesProv_FlowFinalNode(FinalNode):

    pass
class ControlNode:

    pass
class ActivitiesProv_JoinNode(ControlNode):

    def __init__(self, isCombineDuplicate: bool):
        self.isCombineDuplicate = isCombineDuplicate
        
    @property
    def isCombineDuplicate(self) -> bool:
        return self.__isCombineDuplicate

    @isCombineDuplicate.setter
    def isCombineDuplicate(self, isCombineDuplicate: bool):
        self.__isCombineDuplicate = isCombineDuplicate

class ActivitiesProv_DecisionNode(ControlNode):

    pass
class ActivitiesProv_MergeNode(ControlNode):

    pass
class ActivitiesProv_ForkNode(ControlNode):

    pass
class ActivitiesProv_InitialNode(ControlNode):

    pass
class ActivitiesProv_FinalNode(ControlNode):

    pass
class ActivitiesProv_ActivityFinalNode(FinalNode, ControlNode):

    pass
class ObjectNode:

    pass
class ActivitiesProv_CentralBufferNode(ObjectNode):

    pass
class ActivitiesProv_ExpansionNode(ObjectNode):

    pass
class ActivitiesProv_ActivityParameterNode(ObjectNode):

    pass
class ActivityNode:

    pass
class ActivitiesProv_ExecutableNode(ActivityNode):

    pass
class ActivitiesProv_ControlNode(ActivityNode):

    pass
class ActivitiesProv_ObjectNode(ActivityNode):

    pass
class ActivitiesProv_InterruptibleActivityRegion(ActivityGroup):

    pass
class ActivitiesProv_StructuredActivityNode(ExecutableNode, ActivityGroup):

    def __init__(self, mustIsolate: bool, ActivitiesProv_StructuredActivityNode: "ActivitiesProv_Activity" = None, ActivitiesProv_StructuredActivityNode64: "ActivitiesProv_ActivityEdge" = None, ActivitiesProv_StructuredActivityNode28: "ActivitiesProv_ActivityNode" = None, ActivitiesProv_StructuredActivityNode85: "ActivitiesProv_Activity" = None, ActivitiesProv_StructuredActivityNode88: set["ActivitiesProv_ActivityNode"] = None, ActivitiesProv_StructuredActivityNode91: set["ActivitiesProv_ActivityEdge"] = None):
        self.mustIsolate = mustIsolate
        self.ActivitiesProv_StructuredActivityNode = ActivitiesProv_StructuredActivityNode
        self.ActivitiesProv_StructuredActivityNode64 = ActivitiesProv_StructuredActivityNode64
        self.ActivitiesProv_StructuredActivityNode28 = ActivitiesProv_StructuredActivityNode28
        self.ActivitiesProv_StructuredActivityNode85 = ActivitiesProv_StructuredActivityNode85
        self.ActivitiesProv_StructuredActivityNode88 = ActivitiesProv_StructuredActivityNode88 if ActivitiesProv_StructuredActivityNode88 is not None else set()
        self.ActivitiesProv_StructuredActivityNode91 = ActivitiesProv_StructuredActivityNode91 if ActivitiesProv_StructuredActivityNode91 is not None else set()
        
    @property
    def mustIsolate(self) -> bool:
        return self.__mustIsolate

    @mustIsolate.setter
    def mustIsolate(self, mustIsolate: bool):
        self.__mustIsolate = mustIsolate

    @property
    def ActivitiesProv_StructuredActivityNode28(self):
        return self.__ActivitiesProv_StructuredActivityNode28

    @ActivitiesProv_StructuredActivityNode28.setter
    def ActivitiesProv_StructuredActivityNode28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivitiesProv_StructuredActivityNode__ActivitiesProv_StructuredActivityNode28", None)
        self.__ActivitiesProv_StructuredActivityNode28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivitiesProv_ActivityNode27"):
                opp_val = getattr(old_value, "ActivitiesProv_ActivityNode27", None)
                if opp_val == self:
                    setattr(old_value, "ActivitiesProv_ActivityNode27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivitiesProv_ActivityNode27"):
                opp_val = getattr(value, "ActivitiesProv_ActivityNode27", None)
                setattr(value, "ActivitiesProv_ActivityNode27", self)

    @property
    def ActivitiesProv_StructuredActivityNode(self):
        return self.__ActivitiesProv_StructuredActivityNode

    @ActivitiesProv_StructuredActivityNode.setter
    def ActivitiesProv_StructuredActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivitiesProv_StructuredActivityNode__ActivitiesProv_StructuredActivityNode", None)
        self.__ActivitiesProv_StructuredActivityNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivitiesProv_Activity8"):
                opp_val = getattr(old_value, "ActivitiesProv_Activity8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivitiesProv_Activity8"):
                opp_val = getattr(value, "ActivitiesProv_Activity8", None)
                if opp_val is None:
                    setattr(value, "ActivitiesProv_Activity8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ActivitiesProv_StructuredActivityNode64(self):
        return self.__ActivitiesProv_StructuredActivityNode64

    @ActivitiesProv_StructuredActivityNode64.setter
    def ActivitiesProv_StructuredActivityNode64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivitiesProv_StructuredActivityNode__ActivitiesProv_StructuredActivityNode64", None)
        self.__ActivitiesProv_StructuredActivityNode64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivitiesProv_ActivityEdge63"):
                opp_val = getattr(old_value, "ActivitiesProv_ActivityEdge63", None)
                if opp_val == self:
                    setattr(old_value, "ActivitiesProv_ActivityEdge63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivitiesProv_ActivityEdge63"):
                opp_val = getattr(value, "ActivitiesProv_ActivityEdge63", None)
                setattr(value, "ActivitiesProv_ActivityEdge63", self)

    @property
    def ActivitiesProv_StructuredActivityNode85(self):
        return self.__ActivitiesProv_StructuredActivityNode85

    @ActivitiesProv_StructuredActivityNode85.setter
    def ActivitiesProv_StructuredActivityNode85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivitiesProv_StructuredActivityNode__ActivitiesProv_StructuredActivityNode85", None)
        self.__ActivitiesProv_StructuredActivityNode85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivitiesProv_Activity86"):
                opp_val = getattr(old_value, "ActivitiesProv_Activity86", None)
                if opp_val == self:
                    setattr(old_value, "ActivitiesProv_Activity86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivitiesProv_Activity86"):
                opp_val = getattr(value, "ActivitiesProv_Activity86", None)
                setattr(value, "ActivitiesProv_Activity86", self)

    @property
    def ActivitiesProv_StructuredActivityNode88(self):
        return self.__ActivitiesProv_StructuredActivityNode88

    @ActivitiesProv_StructuredActivityNode88.setter
    def ActivitiesProv_StructuredActivityNode88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivitiesProv_StructuredActivityNode__ActivitiesProv_StructuredActivityNode88", None)
        self.__ActivitiesProv_StructuredActivityNode88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivitiesProv_ActivityNode89"):
                    opp_val = getattr(item, "ActivitiesProv_ActivityNode89", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivitiesProv_ActivityNode89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivitiesProv_ActivityNode89"):
                    opp_val = getattr(item, "ActivitiesProv_ActivityNode89", None)
                    
                    setattr(item, "ActivitiesProv_ActivityNode89", self)
                    

    @property
    def ActivitiesProv_StructuredActivityNode91(self):
        return self.__ActivitiesProv_StructuredActivityNode91

    @ActivitiesProv_StructuredActivityNode91.setter
    def ActivitiesProv_StructuredActivityNode91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivitiesProv_StructuredActivityNode__ActivitiesProv_StructuredActivityNode91", None)
        self.__ActivitiesProv_StructuredActivityNode91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivitiesProv_ActivityEdge92"):
                    opp_val = getattr(item, "ActivitiesProv_ActivityEdge92", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivitiesProv_ActivityEdge92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivitiesProv_ActivityEdge92"):
                    opp_val = getattr(item, "ActivitiesProv_ActivityEdge92", None)
                    
                    setattr(item, "ActivitiesProv_ActivityEdge92", self)
                    

class ActivitiesProv_ActivityPartition(ActivityGroup):

    pass
class ActivitiesProv_ActivityEdge(ABC):

    pass
class ActivitiesProv_ActivityGroup(ABC):

    pass
class ActivitiesProv_ActivityNode(ABC):

    pass
class ActivitiesProv_Activity:

    def __init__(self, isReadOnly: bool, isSingleExecution: bool, ActivitiesProv_Activity: set["ActivitiesProv_ActivityNode"] = None, ActivitiesProv_Activity2: set["ActivitiesProv_ActivityGroup"] = None, ActivitiesProv_Activity4: set["ActivitiesProv_ActivityEdge"] = None, ActivitiesProv_Activity6: set["ActivitiesProv_ActivityPartition"] = None, ActivitiesProv_Activity8: set["ActivitiesProv_StructuredActivityNode"] = None, ActivitiesProv_Activity37: "ActivitiesProv_ActivityGroup" = None, ActivitiesProv_Activity86: "ActivitiesProv_StructuredActivityNode" = None):
        self.isReadOnly = isReadOnly
        self.isSingleExecution = isSingleExecution
        self.ActivitiesProv_Activity = ActivitiesProv_Activity if ActivitiesProv_Activity is not None else set()
        self.ActivitiesProv_Activity2 = ActivitiesProv_Activity2 if ActivitiesProv_Activity2 is not None else set()
        self.ActivitiesProv_Activity4 = ActivitiesProv_Activity4 if ActivitiesProv_Activity4 is not None else set()
        self.ActivitiesProv_Activity6 = ActivitiesProv_Activity6 if ActivitiesProv_Activity6 is not None else set()
        self.ActivitiesProv_Activity8 = ActivitiesProv_Activity8 if ActivitiesProv_Activity8 is not None else set()
        self.ActivitiesProv_Activity37 = ActivitiesProv_Activity37
        self.ActivitiesProv_Activity86 = ActivitiesProv_Activity86
        
    @property
    def isSingleExecution(self) -> bool:
        return self.__isSingleExecution

    @isSingleExecution.setter
    def isSingleExecution(self, isSingleExecution: bool):
        self.__isSingleExecution = isSingleExecution

    @property
    def isReadOnly(self) -> bool:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly

    @property
    def ActivitiesProv_Activity2(self):
        return self.__ActivitiesProv_Activity2

    @ActivitiesProv_Activity2.setter
    def ActivitiesProv_Activity2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivitiesProv_Activity__ActivitiesProv_Activity2", None)
        self.__ActivitiesProv_Activity2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivitiesProv_ActivityGroup"):
                    opp_val = getattr(item, "ActivitiesProv_ActivityGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivitiesProv_ActivityGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivitiesProv_ActivityGroup"):
                    opp_val = getattr(item, "ActivitiesProv_ActivityGroup", None)
                    
                    setattr(item, "ActivitiesProv_ActivityGroup", self)
                    

    @property
    def ActivitiesProv_Activity86(self):
        return self.__ActivitiesProv_Activity86

    @ActivitiesProv_Activity86.setter
    def ActivitiesProv_Activity86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivitiesProv_Activity__ActivitiesProv_Activity86", None)
        self.__ActivitiesProv_Activity86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivitiesProv_StructuredActivityNode85"):
                opp_val = getattr(old_value, "ActivitiesProv_StructuredActivityNode85", None)
                if opp_val == self:
                    setattr(old_value, "ActivitiesProv_StructuredActivityNode85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivitiesProv_StructuredActivityNode85"):
                opp_val = getattr(value, "ActivitiesProv_StructuredActivityNode85", None)
                setattr(value, "ActivitiesProv_StructuredActivityNode85", self)

    @property
    def ActivitiesProv_Activity6(self):
        return self.__ActivitiesProv_Activity6

    @ActivitiesProv_Activity6.setter
    def ActivitiesProv_Activity6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivitiesProv_Activity__ActivitiesProv_Activity6", None)
        self.__ActivitiesProv_Activity6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivitiesProv_ActivityPartition"):
                    opp_val = getattr(item, "ActivitiesProv_ActivityPartition", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivitiesProv_ActivityPartition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivitiesProv_ActivityPartition"):
                    opp_val = getattr(item, "ActivitiesProv_ActivityPartition", None)
                    
                    setattr(item, "ActivitiesProv_ActivityPartition", self)
                    

    @property
    def ActivitiesProv_Activity4(self):
        return self.__ActivitiesProv_Activity4

    @ActivitiesProv_Activity4.setter
    def ActivitiesProv_Activity4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivitiesProv_Activity__ActivitiesProv_Activity4", None)
        self.__ActivitiesProv_Activity4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivitiesProv_ActivityEdge"):
                    opp_val = getattr(item, "ActivitiesProv_ActivityEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivitiesProv_ActivityEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivitiesProv_ActivityEdge"):
                    opp_val = getattr(item, "ActivitiesProv_ActivityEdge", None)
                    
                    setattr(item, "ActivitiesProv_ActivityEdge", self)
                    

    @property
    def ActivitiesProv_Activity37(self):
        return self.__ActivitiesProv_Activity37

    @ActivitiesProv_Activity37.setter
    def ActivitiesProv_Activity37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivitiesProv_Activity__ActivitiesProv_Activity37", None)
        self.__ActivitiesProv_Activity37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivitiesProv_ActivityGroup36"):
                opp_val = getattr(old_value, "ActivitiesProv_ActivityGroup36", None)
                if opp_val == self:
                    setattr(old_value, "ActivitiesProv_ActivityGroup36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivitiesProv_ActivityGroup36"):
                opp_val = getattr(value, "ActivitiesProv_ActivityGroup36", None)
                setattr(value, "ActivitiesProv_ActivityGroup36", self)

    @property
    def ActivitiesProv_Activity8(self):
        return self.__ActivitiesProv_Activity8

    @ActivitiesProv_Activity8.setter
    def ActivitiesProv_Activity8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivitiesProv_Activity__ActivitiesProv_Activity8", None)
        self.__ActivitiesProv_Activity8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivitiesProv_StructuredActivityNode"):
                    opp_val = getattr(item, "ActivitiesProv_StructuredActivityNode", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivitiesProv_StructuredActivityNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivitiesProv_StructuredActivityNode"):
                    opp_val = getattr(item, "ActivitiesProv_StructuredActivityNode", None)
                    
                    setattr(item, "ActivitiesProv_StructuredActivityNode", self)
                    

    @property
    def ActivitiesProv_Activity(self):
        return self.__ActivitiesProv_Activity

    @ActivitiesProv_Activity.setter
    def ActivitiesProv_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivitiesProv_Activity__ActivitiesProv_Activity", None)
        self.__ActivitiesProv_Activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivitiesProv_ActivityNode"):
                    opp_val = getattr(item, "ActivitiesProv_ActivityNode", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivitiesProv_ActivityNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivitiesProv_ActivityNode"):
                    opp_val = getattr(item, "ActivitiesProv_ActivityNode", None)
                    
                    setattr(item, "ActivitiesProv_ActivityNode", self)
                    
