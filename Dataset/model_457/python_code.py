from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TransitionKind(Enum):
    external = "external"
    internal = "internal"
class ExpansionKind(Enum):
    parallel = "parallel"
    iterative = "iterative"
    stream = "stream"
class AggregationKind(Enum):
    none = "none"
    shared = "shared"
    composite = "composite"
class VisibilityKind(Enum):
    package = "package"
    public = "public"
    private = "private"
    protected = "protected"
class MessageSort(Enum):
    synchCall = "synchCall"
    asynchCall = "asynchCall"
    asynchSignal = "asynchSignal"
    createMessage = "createMessage"
    deleteMessage = "deleteMessage"
    reply = "reply"
class ObjectNodeOrderingKind(Enum):
    unordered = "unordered"
    ordered = "ordered"
    LIFO = "LIFO"
    FIFO = "FIFO"
class ParameterEffectKind(Enum):
    create = "create"
    read = "read"
    update = "update"
    delete = "delete"
class InteractionOperandKind(Enum):
    seq = "seq"
    alt = "alt"
    opt = "opt"
    break = "break"
    par = "par"
    strict = "strict"
    loop = "loop"
    critical = "critical"
    neg = "neg"
    assert = "assert"
    ignore = "ignore"
    consider = "consider"
class CallConcurrencyFeature(Enum):
    sequential = "sequential"
    guarded = "guarded"
    concurrent = "concurrent"
class ConnectorKind(Enum):
    assembly = "assembly"
    delegation = "delegation"
class MessageKind(Enum):
    complete = "complete"
    lost = "lost"
    found = "found"
    unknown = "unknown"


############################################
# Definition of Classes
############################################

class MessageEnd:

    pass
class InteractionUse:

    pass
class ExecutionSpecification:

    pass
class CompleteDSLPckg_ActionExecutionSpecification(ExecutionSpecification):

    pass
class CompleteDSLPckg_BehaviorExecutionSpecification(ExecutionSpecification):

    pass
class MessageOccurrenceSpecification:

    pass
class CompleteDSLPckg_DestructionOccurrenceSpecification(MessageOccurrenceSpecification):

    pass
class CombinedFragment:

    pass
class CompleteDSLPckg_ConsiderIgnoreFragment(CombinedFragment):

    pass
class CompleteDSLPckg_CombinedFragment:

    def __init__(self, interactionOperator: str, CompleteDSLPckg_CombinedFragment: "CompleteDSLPckg_InteractionOperand" = None, CompleteDSLPckg_CombinedFragment1042: set["CompleteDSLPckg_Gate"] = None):
        self.interactionOperator = interactionOperator
        self.CompleteDSLPckg_CombinedFragment = CompleteDSLPckg_CombinedFragment
        self.CompleteDSLPckg_CombinedFragment1042 = CompleteDSLPckg_CombinedFragment1042 if CompleteDSLPckg_CombinedFragment1042 is not None else set()
        
    @property
    def interactionOperator(self) -> str:
        return self.__interactionOperator

    @interactionOperator.setter
    def interactionOperator(self, interactionOperator: str):
        self.__interactionOperator = interactionOperator

    @property
    def CompleteDSLPckg_CombinedFragment(self):
        return self.__CompleteDSLPckg_CombinedFragment

    @CompleteDSLPckg_CombinedFragment.setter
    def CompleteDSLPckg_CombinedFragment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_CombinedFragment__CompleteDSLPckg_CombinedFragment", None)
        self.__CompleteDSLPckg_CombinedFragment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_InteractionOperand1040"):
                opp_val = getattr(old_value, "CompleteDSLPckg_InteractionOperand1040", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_InteractionOperand1040", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_InteractionOperand1040"):
                opp_val = getattr(value, "CompleteDSLPckg_InteractionOperand1040", None)
                setattr(value, "CompleteDSLPckg_InteractionOperand1040", self)

    @property
    def CompleteDSLPckg_CombinedFragment1042(self):
        return self.__CompleteDSLPckg_CombinedFragment1042

    @CompleteDSLPckg_CombinedFragment1042.setter
    def CompleteDSLPckg_CombinedFragment1042(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_CombinedFragment__CompleteDSLPckg_CombinedFragment1042", None)
        self.__CompleteDSLPckg_CombinedFragment1042 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Gate1043"):
                    opp_val = getattr(item, "CompleteDSLPckg_Gate1043", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Gate1043", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Gate1043"):
                    opp_val = getattr(item, "CompleteDSLPckg_Gate1043", None)
                    
                    setattr(item, "CompleteDSLPckg_Gate1043", self)
                    

class CompleteDSLPckg_PartDecomposition(InteractionUse):

    pass
class OccurenceSpecification:

    pass
class CompleteDSLPckg_MessageOccurrenceSpecification(OccurenceSpecification):

    pass
class CompleteDSLPckg_ExecutionOccurrenceSpecification(OccurenceSpecification):

    pass
class InteractionFragment:

    pass
class CompleteDSLPckg_OccurenceSpecification(InteractionFragment):

    pass
class CompleteDSLPckg_Continuation(InteractionFragment):

    def __init__(self, setting: bool):
        self.setting = setting
        
    @property
    def setting(self) -> bool:
        return self.__setting

    @setting.setter
    def setting(self, setting: bool):
        self.__setting = setting

class CompleteDSLPckg_InteractionUse(InteractionFragment):

    pass
class CompleteDSLPckg_ExecutionSpecification(InteractionFragment):

    pass
class CompleteDSLPckg_Gate(MessageEnd):

    pass
class CompleteDSLPckg_StateInvariant(InteractionFragment):

    pass
class StructuredActivityNode:

    pass
class CompleteDSLPckg_ExpansionRegion(StructuredActivityNode):

    def __init__(self, mode: str, CompleteDSLPckg_ExpansionRegion: set["CompleteDSLPckg_ExpansionNode"] = None, CompleteDSLPckg_ExpansionRegion957: set["CompleteDSLPckg_ExpansionNode"] = None, CompleteDSLPckg_ExpansionRegion961: "CompleteDSLPckg_ExpansionNode" = None, CompleteDSLPckg_ExpansionRegion964: "CompleteDSLPckg_ExpansionNode" = None):
        self.mode = mode
        self.CompleteDSLPckg_ExpansionRegion = CompleteDSLPckg_ExpansionRegion if CompleteDSLPckg_ExpansionRegion is not None else set()
        self.CompleteDSLPckg_ExpansionRegion957 = CompleteDSLPckg_ExpansionRegion957 if CompleteDSLPckg_ExpansionRegion957 is not None else set()
        self.CompleteDSLPckg_ExpansionRegion961 = CompleteDSLPckg_ExpansionRegion961
        self.CompleteDSLPckg_ExpansionRegion964 = CompleteDSLPckg_ExpansionRegion964
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def CompleteDSLPckg_ExpansionRegion(self):
        return self.__CompleteDSLPckg_ExpansionRegion

    @CompleteDSLPckg_ExpansionRegion.setter
    def CompleteDSLPckg_ExpansionRegion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ExpansionRegion__CompleteDSLPckg_ExpansionRegion", None)
        self.__CompleteDSLPckg_ExpansionRegion = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ExpansionNode"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExpansionNode", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ExpansionNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ExpansionNode"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExpansionNode", None)
                    
                    setattr(item, "CompleteDSLPckg_ExpansionNode", self)
                    

    @property
    def CompleteDSLPckg_ExpansionRegion961(self):
        return self.__CompleteDSLPckg_ExpansionRegion961

    @CompleteDSLPckg_ExpansionRegion961.setter
    def CompleteDSLPckg_ExpansionRegion961(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ExpansionRegion__CompleteDSLPckg_ExpansionRegion961", None)
        self.__CompleteDSLPckg_ExpansionRegion961 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ExpansionNode960"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ExpansionNode960", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ExpansionNode960", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ExpansionNode960"):
                opp_val = getattr(value, "CompleteDSLPckg_ExpansionNode960", None)
                setattr(value, "CompleteDSLPckg_ExpansionNode960", self)

    @property
    def CompleteDSLPckg_ExpansionRegion957(self):
        return self.__CompleteDSLPckg_ExpansionRegion957

    @CompleteDSLPckg_ExpansionRegion957.setter
    def CompleteDSLPckg_ExpansionRegion957(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ExpansionRegion__CompleteDSLPckg_ExpansionRegion957", None)
        self.__CompleteDSLPckg_ExpansionRegion957 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ExpansionNode958"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExpansionNode958", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ExpansionNode958", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ExpansionNode958"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExpansionNode958", None)
                    
                    setattr(item, "CompleteDSLPckg_ExpansionNode958", self)
                    

    @property
    def CompleteDSLPckg_ExpansionRegion964(self):
        return self.__CompleteDSLPckg_ExpansionRegion964

    @CompleteDSLPckg_ExpansionRegion964.setter
    def CompleteDSLPckg_ExpansionRegion964(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ExpansionRegion__CompleteDSLPckg_ExpansionRegion964", None)
        self.__CompleteDSLPckg_ExpansionRegion964 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ExpansionNode963"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ExpansionNode963", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ExpansionNode963", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ExpansionNode963"):
                opp_val = getattr(value, "CompleteDSLPckg_ExpansionNode963", None)
                setattr(value, "CompleteDSLPckg_ExpansionNode963", self)

class CompleteDSLPckg_SequenceNode(StructuredActivityNode):

    pass
class CompleteDSLPckg_LoopNode(StructuredActivityNode):

    def __init__(self, isTestedFirst: bool, CompleteDSLPckg_LoopNode912: set["CompleteDSLPckg_InputPin"] = None, CompleteDSLPckg_LoopNode915: set["CompleteDSLPckg_OutputPin"] = None, CompleteDSLPckg_LoopNode918: set["CompleteDSLPckg_OutputPin"] = None, CompleteDSLPckg_LoopNode921: set["CompleteDSLPckg_OutputPin"] = None, CompleteDSLPckg_LoopNode: set["CompleteDSLPckg_ExecutableNode"] = None, CompleteDSLPckg_LoopNode903: set["CompleteDSLPckg_ExecutableNode"] = None, CompleteDSLPckg_LoopNode906: set["CompleteDSLPckg_ExecutableNode"] = None, CompleteDSLPckg_LoopNode909: "CompleteDSLPckg_OutputPin" = None):
        self.isTestedFirst = isTestedFirst
        self.CompleteDSLPckg_LoopNode912 = CompleteDSLPckg_LoopNode912 if CompleteDSLPckg_LoopNode912 is not None else set()
        self.CompleteDSLPckg_LoopNode915 = CompleteDSLPckg_LoopNode915 if CompleteDSLPckg_LoopNode915 is not None else set()
        self.CompleteDSLPckg_LoopNode918 = CompleteDSLPckg_LoopNode918 if CompleteDSLPckg_LoopNode918 is not None else set()
        self.CompleteDSLPckg_LoopNode921 = CompleteDSLPckg_LoopNode921 if CompleteDSLPckg_LoopNode921 is not None else set()
        self.CompleteDSLPckg_LoopNode = CompleteDSLPckg_LoopNode if CompleteDSLPckg_LoopNode is not None else set()
        self.CompleteDSLPckg_LoopNode903 = CompleteDSLPckg_LoopNode903 if CompleteDSLPckg_LoopNode903 is not None else set()
        self.CompleteDSLPckg_LoopNode906 = CompleteDSLPckg_LoopNode906 if CompleteDSLPckg_LoopNode906 is not None else set()
        self.CompleteDSLPckg_LoopNode909 = CompleteDSLPckg_LoopNode909
        
    @property
    def isTestedFirst(self) -> bool:
        return self.__isTestedFirst

    @isTestedFirst.setter
    def isTestedFirst(self, isTestedFirst: bool):
        self.__isTestedFirst = isTestedFirst

    @property
    def CompleteDSLPckg_LoopNode915(self):
        return self.__CompleteDSLPckg_LoopNode915

    @CompleteDSLPckg_LoopNode915.setter
    def CompleteDSLPckg_LoopNode915(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_LoopNode__CompleteDSLPckg_LoopNode915", None)
        self.__CompleteDSLPckg_LoopNode915 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_OutputPin916"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin916", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_OutputPin916", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_OutputPin916"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin916", None)
                    
                    setattr(item, "CompleteDSLPckg_OutputPin916", self)
                    

    @property
    def CompleteDSLPckg_LoopNode921(self):
        return self.__CompleteDSLPckg_LoopNode921

    @CompleteDSLPckg_LoopNode921.setter
    def CompleteDSLPckg_LoopNode921(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_LoopNode__CompleteDSLPckg_LoopNode921", None)
        self.__CompleteDSLPckg_LoopNode921 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_OutputPin922"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin922", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_OutputPin922", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_OutputPin922"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin922", None)
                    
                    setattr(item, "CompleteDSLPckg_OutputPin922", self)
                    

    @property
    def CompleteDSLPckg_LoopNode903(self):
        return self.__CompleteDSLPckg_LoopNode903

    @CompleteDSLPckg_LoopNode903.setter
    def CompleteDSLPckg_LoopNode903(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_LoopNode__CompleteDSLPckg_LoopNode903", None)
        self.__CompleteDSLPckg_LoopNode903 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ExecutableNode904"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExecutableNode904", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ExecutableNode904", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ExecutableNode904"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExecutableNode904", None)
                    
                    setattr(item, "CompleteDSLPckg_ExecutableNode904", self)
                    

    @property
    def CompleteDSLPckg_LoopNode(self):
        return self.__CompleteDSLPckg_LoopNode

    @CompleteDSLPckg_LoopNode.setter
    def CompleteDSLPckg_LoopNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_LoopNode__CompleteDSLPckg_LoopNode", None)
        self.__CompleteDSLPckg_LoopNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ExecutableNode901"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExecutableNode901", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ExecutableNode901", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ExecutableNode901"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExecutableNode901", None)
                    
                    setattr(item, "CompleteDSLPckg_ExecutableNode901", self)
                    

    @property
    def CompleteDSLPckg_LoopNode909(self):
        return self.__CompleteDSLPckg_LoopNode909

    @CompleteDSLPckg_LoopNode909.setter
    def CompleteDSLPckg_LoopNode909(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_LoopNode__CompleteDSLPckg_LoopNode909", None)
        self.__CompleteDSLPckg_LoopNode909 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_OutputPin910"):
                opp_val = getattr(old_value, "CompleteDSLPckg_OutputPin910", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_OutputPin910", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_OutputPin910"):
                opp_val = getattr(value, "CompleteDSLPckg_OutputPin910", None)
                setattr(value, "CompleteDSLPckg_OutputPin910", self)

    @property
    def CompleteDSLPckg_LoopNode912(self):
        return self.__CompleteDSLPckg_LoopNode912

    @CompleteDSLPckg_LoopNode912.setter
    def CompleteDSLPckg_LoopNode912(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_LoopNode__CompleteDSLPckg_LoopNode912", None)
        self.__CompleteDSLPckg_LoopNode912 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_InputPin913"):
                    opp_val = getattr(item, "CompleteDSLPckg_InputPin913", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_InputPin913", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_InputPin913"):
                    opp_val = getattr(item, "CompleteDSLPckg_InputPin913", None)
                    
                    setattr(item, "CompleteDSLPckg_InputPin913", self)
                    

    @property
    def CompleteDSLPckg_LoopNode918(self):
        return self.__CompleteDSLPckg_LoopNode918

    @CompleteDSLPckg_LoopNode918.setter
    def CompleteDSLPckg_LoopNode918(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_LoopNode__CompleteDSLPckg_LoopNode918", None)
        self.__CompleteDSLPckg_LoopNode918 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_OutputPin919"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin919", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_OutputPin919", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_OutputPin919"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin919", None)
                    
                    setattr(item, "CompleteDSLPckg_OutputPin919", self)
                    

    @property
    def CompleteDSLPckg_LoopNode906(self):
        return self.__CompleteDSLPckg_LoopNode906

    @CompleteDSLPckg_LoopNode906.setter
    def CompleteDSLPckg_LoopNode906(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_LoopNode__CompleteDSLPckg_LoopNode906", None)
        self.__CompleteDSLPckg_LoopNode906 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ExecutableNode907"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExecutableNode907", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ExecutableNode907", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ExecutableNode907"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExecutableNode907", None)
                    
                    setattr(item, "CompleteDSLPckg_ExecutableNode907", self)
                    

class CompleteDSLPckg_ConditionalNode(StructuredActivityNode):

    def __init__(self, isDeterminate: bool, isAssumed: bool, CompleteDSLPckg_ConditionalNode: set["CompleteDSLPckg_Clause"] = None, CompleteDSLPckg_ConditionalNode925: set["CompleteDSLPckg_ExecutableNode"] = None, CompleteDSLPckg_ConditionalNode928: set["CompleteDSLPckg_ExecutableNode"] = None, CompleteDSLPckg_ConditionalNode931: set["CompleteDSLPckg_OutputPin"] = None):
        self.isDeterminate = isDeterminate
        self.isAssumed = isAssumed
        self.CompleteDSLPckg_ConditionalNode = CompleteDSLPckg_ConditionalNode if CompleteDSLPckg_ConditionalNode is not None else set()
        self.CompleteDSLPckg_ConditionalNode925 = CompleteDSLPckg_ConditionalNode925 if CompleteDSLPckg_ConditionalNode925 is not None else set()
        self.CompleteDSLPckg_ConditionalNode928 = CompleteDSLPckg_ConditionalNode928 if CompleteDSLPckg_ConditionalNode928 is not None else set()
        self.CompleteDSLPckg_ConditionalNode931 = CompleteDSLPckg_ConditionalNode931 if CompleteDSLPckg_ConditionalNode931 is not None else set()
        
    @property
    def isDeterminate(self) -> bool:
        return self.__isDeterminate

    @isDeterminate.setter
    def isDeterminate(self, isDeterminate: bool):
        self.__isDeterminate = isDeterminate

    @property
    def isAssumed(self) -> bool:
        return self.__isAssumed

    @isAssumed.setter
    def isAssumed(self, isAssumed: bool):
        self.__isAssumed = isAssumed

    @property
    def CompleteDSLPckg_ConditionalNode931(self):
        return self.__CompleteDSLPckg_ConditionalNode931

    @CompleteDSLPckg_ConditionalNode931.setter
    def CompleteDSLPckg_ConditionalNode931(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ConditionalNode__CompleteDSLPckg_ConditionalNode931", None)
        self.__CompleteDSLPckg_ConditionalNode931 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_OutputPin932"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin932", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_OutputPin932", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_OutputPin932"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin932", None)
                    
                    setattr(item, "CompleteDSLPckg_OutputPin932", self)
                    

    @property
    def CompleteDSLPckg_ConditionalNode925(self):
        return self.__CompleteDSLPckg_ConditionalNode925

    @CompleteDSLPckg_ConditionalNode925.setter
    def CompleteDSLPckg_ConditionalNode925(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ConditionalNode__CompleteDSLPckg_ConditionalNode925", None)
        self.__CompleteDSLPckg_ConditionalNode925 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ExecutableNode926"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExecutableNode926", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ExecutableNode926", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ExecutableNode926"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExecutableNode926", None)
                    
                    setattr(item, "CompleteDSLPckg_ExecutableNode926", self)
                    

    @property
    def CompleteDSLPckg_ConditionalNode(self):
        return self.__CompleteDSLPckg_ConditionalNode

    @CompleteDSLPckg_ConditionalNode.setter
    def CompleteDSLPckg_ConditionalNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ConditionalNode__CompleteDSLPckg_ConditionalNode", None)
        self.__CompleteDSLPckg_ConditionalNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Clause"):
                    opp_val = getattr(item, "CompleteDSLPckg_Clause", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Clause", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Clause"):
                    opp_val = getattr(item, "CompleteDSLPckg_Clause", None)
                    
                    setattr(item, "CompleteDSLPckg_Clause", self)
                    

    @property
    def CompleteDSLPckg_ConditionalNode928(self):
        return self.__CompleteDSLPckg_ConditionalNode928

    @CompleteDSLPckg_ConditionalNode928.setter
    def CompleteDSLPckg_ConditionalNode928(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ConditionalNode__CompleteDSLPckg_ConditionalNode928", None)
        self.__CompleteDSLPckg_ConditionalNode928 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ExecutableNode929"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExecutableNode929", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ExecutableNode929", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ExecutableNode929"):
                    opp_val = getattr(item, "CompleteDSLPckg_ExecutableNode929", None)
                    
                    setattr(item, "CompleteDSLPckg_ExecutableNode929", self)
                    

class CentralBufferNode:

    pass
class CompleteDSLPckg_DataStoreNode(CentralBufferNode):

    pass
class ExecutableNode:

    pass
class ActivityGroup:

    pass
class FinalNode:

    pass
class CompleteDSLPckg_FlowFinalNode(FinalNode):

    pass
class ControlNode:

    pass
class CompleteDSLPckg_ForkNode(ControlNode):

    pass
class CompleteDSLPckg_MergeNode(ControlNode):

    pass
class CompleteDSLPckg_DecisionNode(ControlNode):

    pass
class CompleteDSLPckg_JoinNode(ControlNode):

    def __init__(self, isCombineDuplicate: bool, CompleteDSLPckg_JoinNode: "CompleteDSLPckg_ValueSpecification" = None):
        self.isCombineDuplicate = isCombineDuplicate
        self.CompleteDSLPckg_JoinNode = CompleteDSLPckg_JoinNode
        
    @property
    def isCombineDuplicate(self) -> bool:
        return self.__isCombineDuplicate

    @isCombineDuplicate.setter
    def isCombineDuplicate(self, isCombineDuplicate: bool):
        self.__isCombineDuplicate = isCombineDuplicate

    @property
    def CompleteDSLPckg_JoinNode(self):
        return self.__CompleteDSLPckg_JoinNode

    @CompleteDSLPckg_JoinNode.setter
    def CompleteDSLPckg_JoinNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_JoinNode__CompleteDSLPckg_JoinNode", None)
        self.__CompleteDSLPckg_JoinNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ValueSpecification849"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ValueSpecification849", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ValueSpecification849", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ValueSpecification849"):
                opp_val = getattr(value, "CompleteDSLPckg_ValueSpecification849", None)
                setattr(value, "CompleteDSLPckg_ValueSpecification849", self)

class CompleteDSLPckg_InitialNode(ControlNode):

    pass
class CompleteDSLPckg_FinalNode(ControlNode):

    pass
class CompleteDSLPckg_ActivityFinalNode(ControlNode, FinalNode):

    pass
class ObjectNode:

    pass
class CompleteDSLPckg_CentralBufferNode(ObjectNode):

    pass
class CompleteDSLPckg_ExpansionNode(ObjectNode):

    pass
class CompleteDSLPckg_ActivityParameterNode(ObjectNode):

    pass
class ActivityNode:

    pass
class CompleteDSLPckg_ExecutableNode(ActivityNode):

    pass
class CompleteDSLPckg_ControlNode(ActivityNode):

    pass
class ActivityEdge:

    pass
class CompleteDSLPckg_ObjectFlow(ActivityEdge):

    def __init__(self, isMulticast: bool, isMultireceive: bool, ordering: str, isControlType: bool, CompleteDSLPckg_ObjectFlow851: "CompleteDSLPckg_DecisionNode" = None, CompleteDSLPckg_ObjectFlow: "CompleteDSLPckg_Behavior" = None, CompleteDSLPckg_ObjectFlow843: "CompleteDSLPckg_Behavior" = None, CompleteDSLPckg_ObjectFlow846: set["CompleteDSLPckg_State"] = None):
        self.isMulticast = isMulticast
        self.isMultireceive = isMultireceive
        self.ordering = ordering
        self.isControlType = isControlType
        self.CompleteDSLPckg_ObjectFlow851 = CompleteDSLPckg_ObjectFlow851
        self.CompleteDSLPckg_ObjectFlow = CompleteDSLPckg_ObjectFlow
        self.CompleteDSLPckg_ObjectFlow843 = CompleteDSLPckg_ObjectFlow843
        self.CompleteDSLPckg_ObjectFlow846 = CompleteDSLPckg_ObjectFlow846 if CompleteDSLPckg_ObjectFlow846 is not None else set()
        
    @property
    def isControlType(self) -> bool:
        return self.__isControlType

    @isControlType.setter
    def isControlType(self, isControlType: bool):
        self.__isControlType = isControlType

    @property
    def isMulticast(self) -> bool:
        return self.__isMulticast

    @isMulticast.setter
    def isMulticast(self, isMulticast: bool):
        self.__isMulticast = isMulticast

    @property
    def ordering(self) -> str:
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering

    @property
    def isMultireceive(self) -> bool:
        return self.__isMultireceive

    @isMultireceive.setter
    def isMultireceive(self, isMultireceive: bool):
        self.__isMultireceive = isMultireceive

    @property
    def CompleteDSLPckg_ObjectFlow851(self):
        return self.__CompleteDSLPckg_ObjectFlow851

    @CompleteDSLPckg_ObjectFlow851.setter
    def CompleteDSLPckg_ObjectFlow851(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ObjectFlow__CompleteDSLPckg_ObjectFlow851", None)
        self.__CompleteDSLPckg_ObjectFlow851 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_DecisionNode"):
                opp_val = getattr(old_value, "CompleteDSLPckg_DecisionNode", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_DecisionNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_DecisionNode"):
                opp_val = getattr(value, "CompleteDSLPckg_DecisionNode", None)
                setattr(value, "CompleteDSLPckg_DecisionNode", self)

    @property
    def CompleteDSLPckg_ObjectFlow843(self):
        return self.__CompleteDSLPckg_ObjectFlow843

    @CompleteDSLPckg_ObjectFlow843.setter
    def CompleteDSLPckg_ObjectFlow843(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ObjectFlow__CompleteDSLPckg_ObjectFlow843", None)
        self.__CompleteDSLPckg_ObjectFlow843 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Behavior844"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Behavior844", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Behavior844", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Behavior844"):
                opp_val = getattr(value, "CompleteDSLPckg_Behavior844", None)
                setattr(value, "CompleteDSLPckg_Behavior844", self)

    @property
    def CompleteDSLPckg_ObjectFlow846(self):
        return self.__CompleteDSLPckg_ObjectFlow846

    @CompleteDSLPckg_ObjectFlow846.setter
    def CompleteDSLPckg_ObjectFlow846(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ObjectFlow__CompleteDSLPckg_ObjectFlow846", None)
        self.__CompleteDSLPckg_ObjectFlow846 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_State847"):
                    opp_val = getattr(item, "CompleteDSLPckg_State847", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_State847", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_State847"):
                    opp_val = getattr(item, "CompleteDSLPckg_State847", None)
                    
                    setattr(item, "CompleteDSLPckg_State847", self)
                    

    @property
    def CompleteDSLPckg_ObjectFlow(self):
        return self.__CompleteDSLPckg_ObjectFlow

    @CompleteDSLPckg_ObjectFlow.setter
    def CompleteDSLPckg_ObjectFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ObjectFlow__CompleteDSLPckg_ObjectFlow", None)
        self.__CompleteDSLPckg_ObjectFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Behavior841"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Behavior841", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Behavior841", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Behavior841"):
                opp_val = getattr(value, "CompleteDSLPckg_Behavior841", None)
                setattr(value, "CompleteDSLPckg_Behavior841", self)

class CompleteDSLPckg_ControlFlow(ActivityEdge):

    pass
class CompleteDSLPckg_InterruptibleActivityRegion(ActivityGroup):

    pass
class Transition:

    pass
class CompleteDSLPckg_ProtocolTransition(Transition):

    pass
class StateMachine:

    pass
class CompleteDSLPckg_ProtocolStateMachine(StateMachine):

    pass
class State:

    pass
class CompleteDSLPckg_FinalState(State):

    pass
class CompleteDSLPckg_ActivityPartition(ActivityGroup):

    pass
class Vertex:

    pass
class CompleteDSLPckg_ConnectionPointReference(Vertex):

    pass
class VariableAction:

    pass
class CompleteDSLPckg_WriteVariableAction(VariableAction):

    pass
class CompleteDSLPckg_ReadVariableAction(VariableAction):

    pass
class CompleteDSLPckg_Pseudostate(Vertex):

    pass
class CompleteDSLPckg_ClearVariableAction(VariableAction):

    pass
class WriteVariableAction:

    pass
class CompleteDSLPckg_RemoveVariableValueAction(WriteVariableAction):

    pass
class CompleteDSLPckg_AddVariableValueAction(WriteVariableAction):

    pass
class CreateLinkAction:

    pass
class CompleteDSLPckg_CreateLinkObjectAction(CreateLinkAction):

    pass
class AcceptEventAction:

    pass
class CompleteDSLPckg_AcceptCallAction(AcceptEventAction):

    pass
class CompleteDSLPckg_ReadlsClassifiedObjectAction:

    pass
class LinkEndData:

    pass
class CompleteDSLPckg_LinkEndDestructionData(LinkEndData):

    def __init__(self, isDestroyDuplicates: bool, CompleteDSLPckg_LinkEndDestructionData: "CompleteDSLPckg_InputPin" = None):
        self.isDestroyDuplicates = isDestroyDuplicates
        self.CompleteDSLPckg_LinkEndDestructionData = CompleteDSLPckg_LinkEndDestructionData
        
    @property
    def isDestroyDuplicates(self) -> bool:
        return self.__isDestroyDuplicates

    @isDestroyDuplicates.setter
    def isDestroyDuplicates(self, isDestroyDuplicates: bool):
        self.__isDestroyDuplicates = isDestroyDuplicates

    @property
    def CompleteDSLPckg_LinkEndDestructionData(self):
        return self.__CompleteDSLPckg_LinkEndDestructionData

    @CompleteDSLPckg_LinkEndDestructionData.setter
    def CompleteDSLPckg_LinkEndDestructionData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_LinkEndDestructionData__CompleteDSLPckg_LinkEndDestructionData", None)
        self.__CompleteDSLPckg_LinkEndDestructionData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_InputPin566"):
                opp_val = getattr(old_value, "CompleteDSLPckg_InputPin566", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_InputPin566", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_InputPin566"):
                opp_val = getattr(value, "CompleteDSLPckg_InputPin566", None)
                setattr(value, "CompleteDSLPckg_InputPin566", self)

class CompleteDSLPckg_LinkEndCreationData(LinkEndData):

    def __init__(self, isReplaceAll: bool, CompleteDSLPckg_LinkEndCreationData: "CompleteDSLPckg_InputPin" = None):
        self.isReplaceAll = isReplaceAll
        self.CompleteDSLPckg_LinkEndCreationData = CompleteDSLPckg_LinkEndCreationData
        
    @property
    def isReplaceAll(self) -> bool:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: bool):
        self.__isReplaceAll = isReplaceAll

    @property
    def CompleteDSLPckg_LinkEndCreationData(self):
        return self.__CompleteDSLPckg_LinkEndCreationData

    @CompleteDSLPckg_LinkEndCreationData.setter
    def CompleteDSLPckg_LinkEndCreationData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_LinkEndCreationData__CompleteDSLPckg_LinkEndCreationData", None)
        self.__CompleteDSLPckg_LinkEndCreationData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_InputPin564"):
                opp_val = getattr(old_value, "CompleteDSLPckg_InputPin564", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_InputPin564", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_InputPin564"):
                opp_val = getattr(value, "CompleteDSLPckg_InputPin564", None)
                setattr(value, "CompleteDSLPckg_InputPin564", self)

class WriteLinkAction:

    pass
class CompleteDSLPckg_DestroyLinkAction(WriteLinkAction):

    pass
class CompleteDSLPckg_CreateLinkAction(WriteLinkAction):

    pass
class WriteStructuralFeatureAction:

    pass
class CompleteDSLPckg_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class CompleteDSLPckg_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class StructuralFeatureAction:

    pass
class CompleteDSLPckg_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class CompleteDSLPckg_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class LinkAction:

    pass
class CompleteDSLPckg_WriteLinkAction(LinkAction):

    pass
class CompleteDSLPckg_ReadLinkAction(LinkAction):

    pass
class CompleteDSLPckg_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class Action:

    pass
class CompleteDSLPckg_ReadSelfAction(Action):

    pass
class CompleteDSLPckg_ValueSpecificationAction(Action):

    pass
class CompleteDSLPckg_ReplyAction(Action):

    pass
class CompleteDSLPckg_LinkAction(Action):

    pass
class CompleteDSLPckg_TestIdentityAction(Action):

    pass
class CompleteDSLPckg_AcceptEventAction(Action):

    def __init__(self, isUnmarshall: bool, CompleteDSLPckg_AcceptEventAction: set["CompleteDSLPckg_OutputPin"] = None, CompleteDSLPckg_AcceptEventAction586: set["CompleteDSLPckg_Trigger"] = None):
        self.isUnmarshall = isUnmarshall
        self.CompleteDSLPckg_AcceptEventAction = CompleteDSLPckg_AcceptEventAction if CompleteDSLPckg_AcceptEventAction is not None else set()
        self.CompleteDSLPckg_AcceptEventAction586 = CompleteDSLPckg_AcceptEventAction586 if CompleteDSLPckg_AcceptEventAction586 is not None else set()
        
    @property
    def isUnmarshall(self) -> bool:
        return self.__isUnmarshall

    @isUnmarshall.setter
    def isUnmarshall(self, isUnmarshall: bool):
        self.__isUnmarshall = isUnmarshall

    @property
    def CompleteDSLPckg_AcceptEventAction(self):
        return self.__CompleteDSLPckg_AcceptEventAction

    @CompleteDSLPckg_AcceptEventAction.setter
    def CompleteDSLPckg_AcceptEventAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_AcceptEventAction__CompleteDSLPckg_AcceptEventAction", None)
        self.__CompleteDSLPckg_AcceptEventAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_OutputPin584"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin584", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_OutputPin584", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_OutputPin584"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin584", None)
                    
                    setattr(item, "CompleteDSLPckg_OutputPin584", self)
                    

    @property
    def CompleteDSLPckg_AcceptEventAction586(self):
        return self.__CompleteDSLPckg_AcceptEventAction586

    @CompleteDSLPckg_AcceptEventAction586.setter
    def CompleteDSLPckg_AcceptEventAction586(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_AcceptEventAction__CompleteDSLPckg_AcceptEventAction586", None)
        self.__CompleteDSLPckg_AcceptEventAction586 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Trigger587"):
                    opp_val = getattr(item, "CompleteDSLPckg_Trigger587", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Trigger587", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Trigger587"):
                    opp_val = getattr(item, "CompleteDSLPckg_Trigger587", None)
                    
                    setattr(item, "CompleteDSLPckg_Trigger587", self)
                    

class CompleteDSLPckg_ReadLinkObjectEndQualifierAction(Action):

    pass
class CompleteDSLPckg_ReadExtendAction(Action):

    pass
class CompleteDSLPckg_UnmarshallAction(Action):

    pass
class CompleteDSLPckg_ReadLinkObjectEndAction(Action):

    pass
class CompleteDSLPckg_StructuralFeatureAction(Action):

    pass
class CompleteDSLPckg_ReclassifyObjectAction(Action):

    def __init__(self, isReplaceAll: bool, CompleteDSLPckg_ReclassifyObjectAction: "CompleteDSLPckg_InputPin" = None, CompleteDSLPckg_ReclassifyObjectAction598: set["CompleteDSLPckg_Classifier"] = None, CompleteDSLPckg_ReclassifyObjectAction601: set["CompleteDSLPckg_Classifier"] = None):
        self.isReplaceAll = isReplaceAll
        self.CompleteDSLPckg_ReclassifyObjectAction = CompleteDSLPckg_ReclassifyObjectAction
        self.CompleteDSLPckg_ReclassifyObjectAction598 = CompleteDSLPckg_ReclassifyObjectAction598 if CompleteDSLPckg_ReclassifyObjectAction598 is not None else set()
        self.CompleteDSLPckg_ReclassifyObjectAction601 = CompleteDSLPckg_ReclassifyObjectAction601 if CompleteDSLPckg_ReclassifyObjectAction601 is not None else set()
        
    @property
    def isReplaceAll(self) -> bool:
        return self.__isReplaceAll

    @isReplaceAll.setter
    def isReplaceAll(self, isReplaceAll: bool):
        self.__isReplaceAll = isReplaceAll

    @property
    def CompleteDSLPckg_ReclassifyObjectAction598(self):
        return self.__CompleteDSLPckg_ReclassifyObjectAction598

    @CompleteDSLPckg_ReclassifyObjectAction598.setter
    def CompleteDSLPckg_ReclassifyObjectAction598(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ReclassifyObjectAction__CompleteDSLPckg_ReclassifyObjectAction598", None)
        self.__CompleteDSLPckg_ReclassifyObjectAction598 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Classifier599"):
                    opp_val = getattr(item, "CompleteDSLPckg_Classifier599", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Classifier599", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Classifier599"):
                    opp_val = getattr(item, "CompleteDSLPckg_Classifier599", None)
                    
                    setattr(item, "CompleteDSLPckg_Classifier599", self)
                    

    @property
    def CompleteDSLPckg_ReclassifyObjectAction(self):
        return self.__CompleteDSLPckg_ReclassifyObjectAction

    @CompleteDSLPckg_ReclassifyObjectAction.setter
    def CompleteDSLPckg_ReclassifyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ReclassifyObjectAction__CompleteDSLPckg_ReclassifyObjectAction", None)
        self.__CompleteDSLPckg_ReclassifyObjectAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_InputPin596"):
                opp_val = getattr(old_value, "CompleteDSLPckg_InputPin596", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_InputPin596", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_InputPin596"):
                opp_val = getattr(value, "CompleteDSLPckg_InputPin596", None)
                setattr(value, "CompleteDSLPckg_InputPin596", self)

    @property
    def CompleteDSLPckg_ReclassifyObjectAction601(self):
        return self.__CompleteDSLPckg_ReclassifyObjectAction601

    @CompleteDSLPckg_ReclassifyObjectAction601.setter
    def CompleteDSLPckg_ReclassifyObjectAction601(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ReclassifyObjectAction__CompleteDSLPckg_ReclassifyObjectAction601", None)
        self.__CompleteDSLPckg_ReclassifyObjectAction601 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Classifier602"):
                    opp_val = getattr(item, "CompleteDSLPckg_Classifier602", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Classifier602", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Classifier602"):
                    opp_val = getattr(item, "CompleteDSLPckg_Classifier602", None)
                    
                    setattr(item, "CompleteDSLPckg_Classifier602", self)
                    

class CompleteDSLPckg_RaiseExceptionAction(Action):

    pass
class CompleteDSLPckg_CreateObjectAction(Action):

    pass
class CompleteDSLPckg_StartClassifierBehaviorAction(Action):

    pass
class CompleteDSLPckg_DestroyObjectAction(Action):

    pass
class CompleteDSLPckg_ReduceAction(Action):

    def __init__(self, isOrdered: bool, CompleteDSLPckg_ReduceAction: "CompleteDSLPckg_OutputPin" = None, CompleteDSLPckg_ReduceAction639: "CompleteDSLPckg_InputPin" = None, CompleteDSLPckg_ReduceAction642: "CompleteDSLPckg_Behavior" = None):
        self.isOrdered = isOrdered
        self.CompleteDSLPckg_ReduceAction = CompleteDSLPckg_ReduceAction
        self.CompleteDSLPckg_ReduceAction639 = CompleteDSLPckg_ReduceAction639
        self.CompleteDSLPckg_ReduceAction642 = CompleteDSLPckg_ReduceAction642
        
    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def CompleteDSLPckg_ReduceAction642(self):
        return self.__CompleteDSLPckg_ReduceAction642

    @CompleteDSLPckg_ReduceAction642.setter
    def CompleteDSLPckg_ReduceAction642(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ReduceAction__CompleteDSLPckg_ReduceAction642", None)
        self.__CompleteDSLPckg_ReduceAction642 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Behavior643"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Behavior643", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Behavior643", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Behavior643"):
                opp_val = getattr(value, "CompleteDSLPckg_Behavior643", None)
                setattr(value, "CompleteDSLPckg_Behavior643", self)

    @property
    def CompleteDSLPckg_ReduceAction639(self):
        return self.__CompleteDSLPckg_ReduceAction639

    @CompleteDSLPckg_ReduceAction639.setter
    def CompleteDSLPckg_ReduceAction639(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ReduceAction__CompleteDSLPckg_ReduceAction639", None)
        self.__CompleteDSLPckg_ReduceAction639 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_InputPin640"):
                opp_val = getattr(old_value, "CompleteDSLPckg_InputPin640", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_InputPin640", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_InputPin640"):
                opp_val = getattr(value, "CompleteDSLPckg_InputPin640", None)
                setattr(value, "CompleteDSLPckg_InputPin640", self)

    @property
    def CompleteDSLPckg_ReduceAction(self):
        return self.__CompleteDSLPckg_ReduceAction

    @CompleteDSLPckg_ReduceAction.setter
    def CompleteDSLPckg_ReduceAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ReduceAction__CompleteDSLPckg_ReduceAction", None)
        self.__CompleteDSLPckg_ReduceAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_OutputPin637"):
                opp_val = getattr(old_value, "CompleteDSLPckg_OutputPin637", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_OutputPin637", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_OutputPin637"):
                opp_val = getattr(value, "CompleteDSLPckg_OutputPin637", None)
                setattr(value, "CompleteDSLPckg_OutputPin637", self)

class CompleteDSLPckg_VariableAction(Action):

    pass
class CompleteDSLPckg_OpaqueAction(Action):

    def __init__(self, body: str, language: str, CompleteDSLPckg_OpaqueAction484: set["CompleteDSLPckg_OutputPin"] = None, CompleteDSLPckg_OpaqueAction: set["CompleteDSLPckg_InputPin"] = None):
        self.body = body
        self.language = language
        self.CompleteDSLPckg_OpaqueAction484 = CompleteDSLPckg_OpaqueAction484 if CompleteDSLPckg_OpaqueAction484 is not None else set()
        self.CompleteDSLPckg_OpaqueAction = CompleteDSLPckg_OpaqueAction if CompleteDSLPckg_OpaqueAction is not None else set()
        
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
    def CompleteDSLPckg_OpaqueAction484(self):
        return self.__CompleteDSLPckg_OpaqueAction484

    @CompleteDSLPckg_OpaqueAction484.setter
    def CompleteDSLPckg_OpaqueAction484(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_OpaqueAction__CompleteDSLPckg_OpaqueAction484", None)
        self.__CompleteDSLPckg_OpaqueAction484 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_OutputPin485"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin485", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_OutputPin485", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_OutputPin485"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin485", None)
                    
                    setattr(item, "CompleteDSLPckg_OutputPin485", self)
                    

    @property
    def CompleteDSLPckg_OpaqueAction(self):
        return self.__CompleteDSLPckg_OpaqueAction

    @CompleteDSLPckg_OpaqueAction.setter
    def CompleteDSLPckg_OpaqueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_OpaqueAction__CompleteDSLPckg_OpaqueAction", None)
        self.__CompleteDSLPckg_OpaqueAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_InputPin482"):
                    opp_val = getattr(item, "CompleteDSLPckg_InputPin482", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_InputPin482", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_InputPin482"):
                    opp_val = getattr(item, "CompleteDSLPckg_InputPin482", None)
                    
                    setattr(item, "CompleteDSLPckg_InputPin482", self)
                    

class CompleteDSLPckg_CallOperationAction:

    pass
class CallAction:

    pass
class CompleteDSLPckg_StartObjectBehaviorAction(CallAction):

    pass
class CompleteDSLPckg_CallBehaviorAction(CallAction):

    pass
class InvocationAction:

    pass
class CompleteDSLPckg_SendObjectAction(InvocationAction):

    pass
class CompleteDSLPckg_BroadcastSignalAction(InvocationAction):

    pass
class CompleteDSLPckg_SendSignalAction(InvocationAction):

    pass
class CompleteDSLPckg_CallAction(InvocationAction):

    def __init__(self, isSynchronous: bool, CompleteDSLPckg_CallAction: set["CompleteDSLPckg_OutputPin"] = None):
        self.isSynchronous = isSynchronous
        self.CompleteDSLPckg_CallAction = CompleteDSLPckg_CallAction if CompleteDSLPckg_CallAction is not None else set()
        
    @property
    def isSynchronous(self) -> bool:
        return self.__isSynchronous

    @isSynchronous.setter
    def isSynchronous(self, isSynchronous: bool):
        self.__isSynchronous = isSynchronous

    @property
    def CompleteDSLPckg_CallAction(self):
        return self.__CompleteDSLPckg_CallAction

    @CompleteDSLPckg_CallAction.setter
    def CompleteDSLPckg_CallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_CallAction__CompleteDSLPckg_CallAction", None)
        self.__CompleteDSLPckg_CallAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_OutputPin489"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin489", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_OutputPin489", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_OutputPin489"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin489", None)
                    
                    setattr(item, "CompleteDSLPckg_OutputPin489", self)
                    

class InputPin:

    pass
class CompleteDSLPckg_ActionInputPin(InputPin):

    pass
class CompleteDSLPckg_ValuePin(InputPin):

    pass
class Pin:

    pass
class CompleteDSLPckg_InputPin(Pin):

    pass
class CompleteDSLPckg_OutputPin(Pin):

    pass
class DeployedArtifact:

    pass
class Artifact:

    pass
class CompleteDSLPckg_DeploymentSpecification(Artifact):

    def __init__(self, deploymentLocation: str, executionLocation: str, CompleteDSLPckg_DeploymentSpecification: "CompleteDSLPckg_Deployment" = None, CompleteDSLPckg_DeploymentSpecification473: "CompleteDSLPckg_Deployment" = None):
        self.deploymentLocation = deploymentLocation
        self.executionLocation = executionLocation
        self.CompleteDSLPckg_DeploymentSpecification = CompleteDSLPckg_DeploymentSpecification
        self.CompleteDSLPckg_DeploymentSpecification473 = CompleteDSLPckg_DeploymentSpecification473
        
    @property
    def executionLocation(self) -> str:
        return self.__executionLocation

    @executionLocation.setter
    def executionLocation(self, executionLocation: str):
        self.__executionLocation = executionLocation

    @property
    def deploymentLocation(self) -> str:
        return self.__deploymentLocation

    @deploymentLocation.setter
    def deploymentLocation(self, deploymentLocation: str):
        self.__deploymentLocation = deploymentLocation

    @property
    def CompleteDSLPckg_DeploymentSpecification(self):
        return self.__CompleteDSLPckg_DeploymentSpecification

    @CompleteDSLPckg_DeploymentSpecification.setter
    def CompleteDSLPckg_DeploymentSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_DeploymentSpecification__CompleteDSLPckg_DeploymentSpecification", None)
        self.__CompleteDSLPckg_DeploymentSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Deployment471"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Deployment471", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Deployment471"):
                opp_val = getattr(value, "CompleteDSLPckg_Deployment471", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Deployment471", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_DeploymentSpecification473(self):
        return self.__CompleteDSLPckg_DeploymentSpecification473

    @CompleteDSLPckg_DeploymentSpecification473.setter
    def CompleteDSLPckg_DeploymentSpecification473(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_DeploymentSpecification__CompleteDSLPckg_DeploymentSpecification473", None)
        self.__CompleteDSLPckg_DeploymentSpecification473 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Deployment474"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Deployment474", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Deployment474", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Deployment474"):
                opp_val = getattr(value, "CompleteDSLPckg_Deployment474", None)
                setattr(value, "CompleteDSLPckg_Deployment474", self)

class Node:

    pass
class CompleteDSLPckg_ExecutionEnvironment(Node):

    pass
class CompleteDSLPckg_Device(Node):

    pass
class Property:

    pass
class CompleteDSLPckg_Port(Property):

    def __init__(self, isBehavior: bool, isService: bool, isConjugated: bool, CompleteDSLPckg_Port429: set["CompleteDSLPckg_Interface"] = None, CompleteDSLPckg_Port433: "CompleteDSLPckg_Port" = None, CompleteDSLPckg_Port431: set["CompleteDSLPckg_Port"] = None, CompleteDSLPckg_Port435: "CompleteDSLPckg_EncapsulatedClassifier" = None, CompleteDSLPckg_Port445: "CompleteDSLPckg_InvocationAction" = None, CompleteDSLPckg_Port: set["CompleteDSLPckg_Interface"] = None):
        self.isBehavior = isBehavior
        self.isService = isService
        self.isConjugated = isConjugated
        self.CompleteDSLPckg_Port429 = CompleteDSLPckg_Port429 if CompleteDSLPckg_Port429 is not None else set()
        self.CompleteDSLPckg_Port433 = CompleteDSLPckg_Port433
        self.CompleteDSLPckg_Port431 = CompleteDSLPckg_Port431 if CompleteDSLPckg_Port431 is not None else set()
        self.CompleteDSLPckg_Port435 = CompleteDSLPckg_Port435
        self.CompleteDSLPckg_Port445 = CompleteDSLPckg_Port445
        self.CompleteDSLPckg_Port = CompleteDSLPckg_Port if CompleteDSLPckg_Port is not None else set()
        
    @property
    def isService(self) -> bool:
        return self.__isService

    @isService.setter
    def isService(self, isService: bool):
        self.__isService = isService

    @property
    def isBehavior(self) -> bool:
        return self.__isBehavior

    @isBehavior.setter
    def isBehavior(self, isBehavior: bool):
        self.__isBehavior = isBehavior

    @property
    def isConjugated(self) -> bool:
        return self.__isConjugated

    @isConjugated.setter
    def isConjugated(self, isConjugated: bool):
        self.__isConjugated = isConjugated

    @property
    def CompleteDSLPckg_Port435(self):
        return self.__CompleteDSLPckg_Port435

    @CompleteDSLPckg_Port435.setter
    def CompleteDSLPckg_Port435(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Port__CompleteDSLPckg_Port435", None)
        self.__CompleteDSLPckg_Port435 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_EncapsulatedClassifier"):
                opp_val = getattr(old_value, "CompleteDSLPckg_EncapsulatedClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_EncapsulatedClassifier"):
                opp_val = getattr(value, "CompleteDSLPckg_EncapsulatedClassifier", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_EncapsulatedClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Port445(self):
        return self.__CompleteDSLPckg_Port445

    @CompleteDSLPckg_Port445.setter
    def CompleteDSLPckg_Port445(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Port__CompleteDSLPckg_Port445", None)
        self.__CompleteDSLPckg_Port445 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_InvocationAction"):
                opp_val = getattr(old_value, "CompleteDSLPckg_InvocationAction", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_InvocationAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_InvocationAction"):
                opp_val = getattr(value, "CompleteDSLPckg_InvocationAction", None)
                setattr(value, "CompleteDSLPckg_InvocationAction", self)

    @property
    def CompleteDSLPckg_Port433(self):
        return self.__CompleteDSLPckg_Port433

    @CompleteDSLPckg_Port433.setter
    def CompleteDSLPckg_Port433(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Port__CompleteDSLPckg_Port433", None)
        self.__CompleteDSLPckg_Port433 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Port431"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Port431", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Port431"):
                opp_val = getattr(value, "CompleteDSLPckg_Port431", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Port431", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Port(self):
        return self.__CompleteDSLPckg_Port

    @CompleteDSLPckg_Port.setter
    def CompleteDSLPckg_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Port__CompleteDSLPckg_Port", None)
        self.__CompleteDSLPckg_Port = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Interface427"):
                    opp_val = getattr(item, "CompleteDSLPckg_Interface427", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Interface427", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Interface427"):
                    opp_val = getattr(item, "CompleteDSLPckg_Interface427", None)
                    
                    setattr(item, "CompleteDSLPckg_Interface427", self)
                    

    @property
    def CompleteDSLPckg_Port429(self):
        return self.__CompleteDSLPckg_Port429

    @CompleteDSLPckg_Port429.setter
    def CompleteDSLPckg_Port429(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Port__CompleteDSLPckg_Port429", None)
        self.__CompleteDSLPckg_Port429 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Interface430"):
                    opp_val = getattr(item, "CompleteDSLPckg_Interface430", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Interface430", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Interface430"):
                    opp_val = getattr(item, "CompleteDSLPckg_Interface430", None)
                    
                    setattr(item, "CompleteDSLPckg_Interface430", self)
                    

    @property
    def CompleteDSLPckg_Port431(self):
        return self.__CompleteDSLPckg_Port431

    @CompleteDSLPckg_Port431.setter
    def CompleteDSLPckg_Port431(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Port__CompleteDSLPckg_Port431", None)
        self.__CompleteDSLPckg_Port431 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Port433"):
                    opp_val = getattr(item, "CompleteDSLPckg_Port433", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Port433", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Port433"):
                    opp_val = getattr(item, "CompleteDSLPckg_Port433", None)
                    
                    setattr(item, "CompleteDSLPckg_Port433", self)
                    

class CompleteDSLPckg_InvocationAction(ABC):

    pass
class CompleteDSLPckg_ConnectorEnd:

    pass
class IntervalConstraint:

    pass
class CompleteDSLPckg_DurationConstraint(IntervalConstraint):

    def __init__(self, firstEvent: bool, CompleteDSLPckg_DurationConstraint: "CompleteDSLPckg_DurationInterval" = None):
        self.firstEvent = firstEvent
        self.CompleteDSLPckg_DurationConstraint = CompleteDSLPckg_DurationConstraint
        
    @property
    def firstEvent(self) -> bool:
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: bool):
        self.__firstEvent = firstEvent

    @property
    def CompleteDSLPckg_DurationConstraint(self):
        return self.__CompleteDSLPckg_DurationConstraint

    @CompleteDSLPckg_DurationConstraint.setter
    def CompleteDSLPckg_DurationConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_DurationConstraint__CompleteDSLPckg_DurationConstraint", None)
        self.__CompleteDSLPckg_DurationConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_DurationInterval377"):
                opp_val = getattr(old_value, "CompleteDSLPckg_DurationInterval377", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_DurationInterval377", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_DurationInterval377"):
                opp_val = getattr(value, "CompleteDSLPckg_DurationInterval377", None)
                setattr(value, "CompleteDSLPckg_DurationInterval377", self)

class CompleteDSLPckg_TimeConstraint(IntervalConstraint):

    def __init__(self, firstEvent: bool, CompleteDSLPckg_TimeConstraint: "CompleteDSLPckg_TimeInterval" = None):
        self.firstEvent = firstEvent
        self.CompleteDSLPckg_TimeConstraint = CompleteDSLPckg_TimeConstraint
        
    @property
    def firstEvent(self) -> bool:
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: bool):
        self.__firstEvent = firstEvent

    @property
    def CompleteDSLPckg_TimeConstraint(self):
        return self.__CompleteDSLPckg_TimeConstraint

    @CompleteDSLPckg_TimeConstraint.setter
    def CompleteDSLPckg_TimeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_TimeConstraint__CompleteDSLPckg_TimeConstraint", None)
        self.__CompleteDSLPckg_TimeConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_TimeInterval375"):
                opp_val = getattr(old_value, "CompleteDSLPckg_TimeInterval375", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_TimeInterval375", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_TimeInterval375"):
                opp_val = getattr(value, "CompleteDSLPckg_TimeInterval375", None)
                setattr(value, "CompleteDSLPckg_TimeInterval375", self)

class Constraint:

    pass
class CompleteDSLPckg_InteractionConstraint(Constraint):

    pass
class CompleteDSLPckg_IntervalConstraint(Constraint):

    pass
class Interval:

    pass
class CompleteDSLPckg_DurationInterval(Interval):

    pass
class CompleteDSLPckg_TimeInterval(Interval):

    pass
class MessageEvent:

    pass
class CompleteDSLPckg_CallEvent(MessageEvent):

    pass
class CompleteDSLPckg_SignalEvent(MessageEvent):

    pass
class CompleteDSLPckg_AnyReceiveEvent(MessageEvent):

    pass
class Event:

    pass
class CompleteDSLPckg_ChangeEvent(Event):

    pass
class CompleteDSLPckg_MessageEvent(Event):

    pass
class Observation:

    pass
class CompleteDSLPckg_DurationObservation(Observation):

    def __init__(self, firstEvent: bool, CompleteDSLPckg_DurationObservation: set["CompleteDSLPckg_NamedElement"] = None):
        self.firstEvent = firstEvent
        self.CompleteDSLPckg_DurationObservation = CompleteDSLPckg_DurationObservation if CompleteDSLPckg_DurationObservation is not None else set()
        
    @property
    def firstEvent(self) -> bool:
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: bool):
        self.__firstEvent = firstEvent

    @property
    def CompleteDSLPckg_DurationObservation(self):
        return self.__CompleteDSLPckg_DurationObservation

    @CompleteDSLPckg_DurationObservation.setter
    def CompleteDSLPckg_DurationObservation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_DurationObservation__CompleteDSLPckg_DurationObservation", None)
        self.__CompleteDSLPckg_DurationObservation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_NamedElement353"):
                    opp_val = getattr(item, "CompleteDSLPckg_NamedElement353", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_NamedElement353", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_NamedElement353"):
                    opp_val = getattr(item, "CompleteDSLPckg_NamedElement353", None)
                    
                    setattr(item, "CompleteDSLPckg_NamedElement353", self)
                    

class CompleteDSLPckg_TimeObservation(Observation):

    def __init__(self, firstEvent: bool, CompleteDSLPckg_TimeObservation: "CompleteDSLPckg_NamedElement" = None):
        self.firstEvent = firstEvent
        self.CompleteDSLPckg_TimeObservation = CompleteDSLPckg_TimeObservation
        
    @property
    def firstEvent(self) -> bool:
        return self.__firstEvent

    @firstEvent.setter
    def firstEvent(self, firstEvent: bool):
        self.__firstEvent = firstEvent

    @property
    def CompleteDSLPckg_TimeObservation(self):
        return self.__CompleteDSLPckg_TimeObservation

    @CompleteDSLPckg_TimeObservation.setter
    def CompleteDSLPckg_TimeObservation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_TimeObservation__CompleteDSLPckg_TimeObservation", None)
        self.__CompleteDSLPckg_TimeObservation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_NamedElement351"):
                opp_val = getattr(old_value, "CompleteDSLPckg_NamedElement351", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_NamedElement351", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_NamedElement351"):
                opp_val = getattr(value, "CompleteDSLPckg_NamedElement351", None)
                setattr(value, "CompleteDSLPckg_NamedElement351", self)

class CompleteDSLPckg_TimeEvent:

    def __init__(self, isRelative: bool, CompleteDSLPckg_TimeEvent: "CompleteDSLPckg_TimeExpression" = None):
        self.isRelative = isRelative
        self.CompleteDSLPckg_TimeEvent = CompleteDSLPckg_TimeEvent
        
    @property
    def isRelative(self) -> bool:
        return self.__isRelative

    @isRelative.setter
    def isRelative(self, isRelative: bool):
        self.__isRelative = isRelative

    @property
    def CompleteDSLPckg_TimeEvent(self):
        return self.__CompleteDSLPckg_TimeEvent

    @CompleteDSLPckg_TimeEvent.setter
    def CompleteDSLPckg_TimeEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_TimeEvent__CompleteDSLPckg_TimeEvent", None)
        self.__CompleteDSLPckg_TimeEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_TimeExpression"):
                opp_val = getattr(old_value, "CompleteDSLPckg_TimeExpression", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_TimeExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_TimeExpression"):
                opp_val = getattr(value, "CompleteDSLPckg_TimeExpression", None)
                setattr(value, "CompleteDSLPckg_TimeExpression", self)

class OpaqueBehavior:

    pass
class CompleteDSLPckg_FunctionBehavior(OpaqueBehavior):

    pass
class Association:

    pass
class CompleteDSLPckg_CommunicationPath(Association):

    pass
class Class:

    pass
class CompleteDSLPckg_AssociationClass(Association, Class):

    pass
class Behavior:

    pass
class CompleteDSLPckg_Interaction(Behavior, InteractionFragment):

    pass
class CompleteDSLPckg_Activity(Behavior):

    def __init__(self, isReadOnly: bool, isSingleExecution: bool, CompleteDSLPckg_Activity: set["CompleteDSLPckg_ActivityNode"] = None, CompleteDSLPckg_Activity766: set["CompleteDSLPckg_ActivityGroup"] = None, CompleteDSLPckg_Activity768: set["CompleteDSLPckg_ActivityEdge"] = None, CompleteDSLPckg_Activity770: set["CompleteDSLPckg_ActivityPartition"] = None, CompleteDSLPckg_Activity804: "CompleteDSLPckg_ActivityGroup" = None, CompleteDSLPckg_Activity772: set["CompleteDSLPckg_StructuredActivityNode"] = None, CompleteDSLPckg_Activity774: set["CompleteDSLPckg_Variable"] = None, CompleteDSLPckg_Activity883: "CompleteDSLPckg_StructuredActivityNode" = None):
        self.isReadOnly = isReadOnly
        self.isSingleExecution = isSingleExecution
        self.CompleteDSLPckg_Activity = CompleteDSLPckg_Activity if CompleteDSLPckg_Activity is not None else set()
        self.CompleteDSLPckg_Activity766 = CompleteDSLPckg_Activity766 if CompleteDSLPckg_Activity766 is not None else set()
        self.CompleteDSLPckg_Activity768 = CompleteDSLPckg_Activity768 if CompleteDSLPckg_Activity768 is not None else set()
        self.CompleteDSLPckg_Activity770 = CompleteDSLPckg_Activity770 if CompleteDSLPckg_Activity770 is not None else set()
        self.CompleteDSLPckg_Activity804 = CompleteDSLPckg_Activity804
        self.CompleteDSLPckg_Activity772 = CompleteDSLPckg_Activity772 if CompleteDSLPckg_Activity772 is not None else set()
        self.CompleteDSLPckg_Activity774 = CompleteDSLPckg_Activity774 if CompleteDSLPckg_Activity774 is not None else set()
        self.CompleteDSLPckg_Activity883 = CompleteDSLPckg_Activity883
        
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
    def CompleteDSLPckg_Activity772(self):
        return self.__CompleteDSLPckg_Activity772

    @CompleteDSLPckg_Activity772.setter
    def CompleteDSLPckg_Activity772(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Activity__CompleteDSLPckg_Activity772", None)
        self.__CompleteDSLPckg_Activity772 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_StructuredActivityNode"):
                    opp_val = getattr(item, "CompleteDSLPckg_StructuredActivityNode", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_StructuredActivityNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_StructuredActivityNode"):
                    opp_val = getattr(item, "CompleteDSLPckg_StructuredActivityNode", None)
                    
                    setattr(item, "CompleteDSLPckg_StructuredActivityNode", self)
                    

    @property
    def CompleteDSLPckg_Activity(self):
        return self.__CompleteDSLPckg_Activity

    @CompleteDSLPckg_Activity.setter
    def CompleteDSLPckg_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Activity__CompleteDSLPckg_Activity", None)
        self.__CompleteDSLPckg_Activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ActivityNode"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityNode", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ActivityNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ActivityNode"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityNode", None)
                    
                    setattr(item, "CompleteDSLPckg_ActivityNode", self)
                    

    @property
    def CompleteDSLPckg_Activity768(self):
        return self.__CompleteDSLPckg_Activity768

    @CompleteDSLPckg_Activity768.setter
    def CompleteDSLPckg_Activity768(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Activity__CompleteDSLPckg_Activity768", None)
        self.__CompleteDSLPckg_Activity768 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ActivityEdge"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ActivityEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ActivityEdge"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityEdge", None)
                    
                    setattr(item, "CompleteDSLPckg_ActivityEdge", self)
                    

    @property
    def CompleteDSLPckg_Activity770(self):
        return self.__CompleteDSLPckg_Activity770

    @CompleteDSLPckg_Activity770.setter
    def CompleteDSLPckg_Activity770(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Activity__CompleteDSLPckg_Activity770", None)
        self.__CompleteDSLPckg_Activity770 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ActivityPartition"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityPartition", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ActivityPartition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ActivityPartition"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityPartition", None)
                    
                    setattr(item, "CompleteDSLPckg_ActivityPartition", self)
                    

    @property
    def CompleteDSLPckg_Activity883(self):
        return self.__CompleteDSLPckg_Activity883

    @CompleteDSLPckg_Activity883.setter
    def CompleteDSLPckg_Activity883(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Activity__CompleteDSLPckg_Activity883", None)
        self.__CompleteDSLPckg_Activity883 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_StructuredActivityNode882"):
                opp_val = getattr(old_value, "CompleteDSLPckg_StructuredActivityNode882", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_StructuredActivityNode882", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_StructuredActivityNode882"):
                opp_val = getattr(value, "CompleteDSLPckg_StructuredActivityNode882", None)
                setattr(value, "CompleteDSLPckg_StructuredActivityNode882", self)

    @property
    def CompleteDSLPckg_Activity766(self):
        return self.__CompleteDSLPckg_Activity766

    @CompleteDSLPckg_Activity766.setter
    def CompleteDSLPckg_Activity766(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Activity__CompleteDSLPckg_Activity766", None)
        self.__CompleteDSLPckg_Activity766 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ActivityGroup"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ActivityGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ActivityGroup"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityGroup", None)
                    
                    setattr(item, "CompleteDSLPckg_ActivityGroup", self)
                    

    @property
    def CompleteDSLPckg_Activity804(self):
        return self.__CompleteDSLPckg_Activity804

    @CompleteDSLPckg_Activity804.setter
    def CompleteDSLPckg_Activity804(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Activity__CompleteDSLPckg_Activity804", None)
        self.__CompleteDSLPckg_Activity804 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ActivityGroup803"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ActivityGroup803", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ActivityGroup803", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ActivityGroup803"):
                opp_val = getattr(value, "CompleteDSLPckg_ActivityGroup803", None)
                setattr(value, "CompleteDSLPckg_ActivityGroup803", self)

    @property
    def CompleteDSLPckg_Activity774(self):
        return self.__CompleteDSLPckg_Activity774

    @CompleteDSLPckg_Activity774.setter
    def CompleteDSLPckg_Activity774(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Activity__CompleteDSLPckg_Activity774", None)
        self.__CompleteDSLPckg_Activity774 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Variable775"):
                    opp_val = getattr(item, "CompleteDSLPckg_Variable775", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Variable775", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Variable775"):
                    opp_val = getattr(item, "CompleteDSLPckg_Variable775", None)
                    
                    setattr(item, "CompleteDSLPckg_Variable775", self)
                    

class CompleteDSLPckg_StateMachine(Behavior):

    pass
class CompleteDSLPckg_OpaqueBehavior(Behavior):

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

class Dependency:

    pass
class CompleteDSLPckg_Abstraction(Dependency):

    pass
class CompleteDSLPckg_Deployment(Dependency):

    pass
class CompleteDSLPckg_Usage(Dependency):

    pass
class InstanceSpecification:

    pass
class Realization:

    pass
class CompleteDSLPckg_InterfaceRealization(Realization):

    pass
class CompleteDSLPckg_ComponentRealization(Realization):

    pass
class Abstraction:

    pass
class CompleteDSLPckg_Manifestation(Abstraction):

    pass
class CompleteDSLPckg_Realization(Abstraction):

    pass
class EncapsulatedClassifier:

    pass
class StructuredClassifier:

    pass
class CompleteDSLPckg_EncapsulatedClassifier(StructuredClassifier):

    pass
class BehavioredClassifier:

    pass
class CompleteDSLPckg_Actor(BehavioredClassifier):

    pass
class CompleteDSLPckg_Collaboration(StructuredClassifier, BehavioredClassifier):

    pass
class CompleteDSLPckg_UseCase(BehavioredClassifier):

    pass
class Classifier:

    pass
class CompleteDSLPckg_BehavioredClassifier(Classifier):

    pass
class CompleteDSLPckg_Signal(Classifier):

    pass
class CompleteDSLPckg_StructuredClassifier(Classifier):

    pass
class CompleteDSLPckg_EnumerationLiteral(InstanceSpecification):

    pass
class DataType:

    pass
class CompleteDSLPckg_Enumeration(DataType):

    pass
class CompleteDSLPckg_PrimitiveType(DataType):

    pass
class BehavioralFeature:

    pass
class CompleteDSLPckg_Reception(BehavioralFeature):

    pass
class CompleteDSLPckg_Operation(BehavioralFeature):

    def __init__(self, isQuery: bool, isOrdered: bool, isUnique: bool, upper: int, lower: int, CompleteDSLPckg_Operation: "CompleteDSLPckg_Type" = None, CompleteDSLPckg_Operation214: set["CompleteDSLPckg_Constraint"] = None, CompleteDSLPckg_Operation217: set["CompleteDSLPckg_Constraint"] = None, CompleteDSLPckg_Operation220: set["CompleteDSLPckg_Constraint"] = None, 223: "CompleteDSLPckg_Class" = None, 257: "CompleteDSLPckg_DataType" = None, 226: "CompleteDSLPckg_DataType" = None, 229: "CompleteDSLPckg_Interface" = None, 235: "CompleteDSLPckg_Class" = None, 291: "CompleteDSLPckg_Interface" = None, CompleteDSLPckg_Operation341: "CompleteDSLPckg_CallEvent" = None, CompleteDSLPckg_Operation447: "CompleteDSLPckg_Artifact" = None, CompleteDSLPckg_Operation493: "CompleteDSLPckg_CallOperationAction" = None, CompleteDSLPckg_Operation763: "CompleteDSLPckg_ProtocolTransition" = None):
        self.isQuery = isQuery
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.upper = upper
        self.lower = lower
        self.CompleteDSLPckg_Operation = CompleteDSLPckg_Operation
        self.CompleteDSLPckg_Operation214 = CompleteDSLPckg_Operation214 if CompleteDSLPckg_Operation214 is not None else set()
        self.CompleteDSLPckg_Operation217 = CompleteDSLPckg_Operation217 if CompleteDSLPckg_Operation217 is not None else set()
        self.CompleteDSLPckg_Operation220 = CompleteDSLPckg_Operation220 if CompleteDSLPckg_Operation220 is not None else set()
        self.223 = 223
        self.257 = 257
        self.226 = 226
        self.229 = 229
        self.235 = 235
        self.291 = 291
        self.CompleteDSLPckg_Operation341 = CompleteDSLPckg_Operation341
        self.CompleteDSLPckg_Operation447 = CompleteDSLPckg_Operation447
        self.CompleteDSLPckg_Operation493 = CompleteDSLPckg_Operation493
        self.CompleteDSLPckg_Operation763 = CompleteDSLPckg_Operation763
        
    @property
    def isUnique(self) -> bool:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique

    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def isQuery(self) -> bool:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: bool):
        self.__isQuery = isQuery

    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def CompleteDSLPckg_Operation(self):
        return self.__CompleteDSLPckg_Operation

    @CompleteDSLPckg_Operation.setter
    def CompleteDSLPckg_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__CompleteDSLPckg_Operation", None)
        self.__CompleteDSLPckg_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Type212"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Type212", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Type212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Type212"):
                opp_val = getattr(value, "CompleteDSLPckg_Type212", None)
                setattr(value, "CompleteDSLPckg_Type212", self)

    @property
    def 291(self):
        return self.__291

    @291.setter
    def 291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__291", None)
        self.__291 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "290"):
                opp_val = getattr(old_value, "290", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "290"):
                opp_val = getattr(value, "290", None)
                if opp_val is None:
                    setattr(value, "290", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 223(self):
        return self.__223

    @223.setter
    def 223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__223", None)
        self.__223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "224"):
                opp_val = getattr(old_value, "224", None)
                if opp_val == self:
                    setattr(old_value, "224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "224"):
                opp_val = getattr(value, "224", None)
                setattr(value, "224", self)

    @property
    def 226(self):
        return self.__226

    @226.setter
    def 226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__226", None)
        self.__226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "227"):
                opp_val = getattr(old_value, "227", None)
                if opp_val == self:
                    setattr(old_value, "227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "227"):
                opp_val = getattr(value, "227", None)
                setattr(value, "227", self)

    @property
    def CompleteDSLPckg_Operation220(self):
        return self.__CompleteDSLPckg_Operation220

    @CompleteDSLPckg_Operation220.setter
    def CompleteDSLPckg_Operation220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__CompleteDSLPckg_Operation220", None)
        self.__CompleteDSLPckg_Operation220 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Constraint221"):
                    opp_val = getattr(item, "CompleteDSLPckg_Constraint221", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Constraint221", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Constraint221"):
                    opp_val = getattr(item, "CompleteDSLPckg_Constraint221", None)
                    
                    setattr(item, "CompleteDSLPckg_Constraint221", self)
                    

    @property
    def CompleteDSLPckg_Operation217(self):
        return self.__CompleteDSLPckg_Operation217

    @CompleteDSLPckg_Operation217.setter
    def CompleteDSLPckg_Operation217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__CompleteDSLPckg_Operation217", None)
        self.__CompleteDSLPckg_Operation217 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Constraint218"):
                    opp_val = getattr(item, "CompleteDSLPckg_Constraint218", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Constraint218", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Constraint218"):
                    opp_val = getattr(item, "CompleteDSLPckg_Constraint218", None)
                    
                    setattr(item, "CompleteDSLPckg_Constraint218", self)
                    

    @property
    def CompleteDSLPckg_Operation214(self):
        return self.__CompleteDSLPckg_Operation214

    @CompleteDSLPckg_Operation214.setter
    def CompleteDSLPckg_Operation214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__CompleteDSLPckg_Operation214", None)
        self.__CompleteDSLPckg_Operation214 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Constraint215"):
                    opp_val = getattr(item, "CompleteDSLPckg_Constraint215", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Constraint215", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Constraint215"):
                    opp_val = getattr(item, "CompleteDSLPckg_Constraint215", None)
                    
                    setattr(item, "CompleteDSLPckg_Constraint215", self)
                    

    @property
    def CompleteDSLPckg_Operation447(self):
        return self.__CompleteDSLPckg_Operation447

    @CompleteDSLPckg_Operation447.setter
    def CompleteDSLPckg_Operation447(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__CompleteDSLPckg_Operation447", None)
        self.__CompleteDSLPckg_Operation447 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Artifact"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Artifact", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Artifact"):
                opp_val = getattr(value, "CompleteDSLPckg_Artifact", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Artifact", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 229(self):
        return self.__229

    @229.setter
    def 229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__229", None)
        self.__229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "230"):
                opp_val = getattr(old_value, "230", None)
                if opp_val == self:
                    setattr(old_value, "230", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "230"):
                opp_val = getattr(value, "230", None)
                setattr(value, "230", self)

    @property
    def 235(self):
        return self.__235

    @235.setter
    def 235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__235", None)
        self.__235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "234"):
                opp_val = getattr(old_value, "234", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "234"):
                opp_val = getattr(value, "234", None)
                if opp_val is None:
                    setattr(value, "234", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Operation763(self):
        return self.__CompleteDSLPckg_Operation763

    @CompleteDSLPckg_Operation763.setter
    def CompleteDSLPckg_Operation763(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__CompleteDSLPckg_Operation763", None)
        self.__CompleteDSLPckg_Operation763 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ProtocolTransition762"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ProtocolTransition762", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ProtocolTransition762"):
                opp_val = getattr(value, "CompleteDSLPckg_ProtocolTransition762", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_ProtocolTransition762", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Operation341(self):
        return self.__CompleteDSLPckg_Operation341

    @CompleteDSLPckg_Operation341.setter
    def CompleteDSLPckg_Operation341(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__CompleteDSLPckg_Operation341", None)
        self.__CompleteDSLPckg_Operation341 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_CallEvent"):
                opp_val = getattr(old_value, "CompleteDSLPckg_CallEvent", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_CallEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_CallEvent"):
                opp_val = getattr(value, "CompleteDSLPckg_CallEvent", None)
                setattr(value, "CompleteDSLPckg_CallEvent", self)

    @property
    def CompleteDSLPckg_Operation493(self):
        return self.__CompleteDSLPckg_Operation493

    @CompleteDSLPckg_Operation493.setter
    def CompleteDSLPckg_Operation493(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__CompleteDSLPckg_Operation493", None)
        self.__CompleteDSLPckg_Operation493 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_CallOperationAction"):
                opp_val = getattr(old_value, "CompleteDSLPckg_CallOperationAction", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_CallOperationAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_CallOperationAction"):
                opp_val = getattr(value, "CompleteDSLPckg_CallOperationAction", None)
                setattr(value, "CompleteDSLPckg_CallOperationAction", self)

    @property
    def 257(self):
        return self.__257

    @257.setter
    def 257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Operation__257", None)
        self.__257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "256"):
                opp_val = getattr(old_value, "256", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "256"):
                opp_val = getattr(value, "256", None)
                if opp_val is None:
                    setattr(value, "256", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DeploymentTarget:

    pass
class CompleteDSLPckg_Node(DeploymentTarget, Class):

    pass
class ConnectableElement:

    pass
class StructuralFeature:

    pass
class MultiplicityElement:

    pass
class Feature:

    pass
class CompleteDSLPckg_Connector(Feature):

    def __init__(self, kind: str, CompleteDSLPckg_Connector: set["CompleteDSLPckg_ConnectorEnd"] = None, CompleteDSLPckg_Connector396: set["CompleteDSLPckg_Behavior"] = None, CompleteDSLPckg_Connector400: "CompleteDSLPckg_Connector" = None, CompleteDSLPckg_Connector398: set["CompleteDSLPckg_Connector"] = None, CompleteDSLPckg_Connector416: "CompleteDSLPckg_StructuredClassifier" = None, CompleteDSLPckg_Connector1010: "CompleteDSLPckg_Message" = None):
        self.kind = kind
        self.CompleteDSLPckg_Connector = CompleteDSLPckg_Connector if CompleteDSLPckg_Connector is not None else set()
        self.CompleteDSLPckg_Connector396 = CompleteDSLPckg_Connector396 if CompleteDSLPckg_Connector396 is not None else set()
        self.CompleteDSLPckg_Connector400 = CompleteDSLPckg_Connector400
        self.CompleteDSLPckg_Connector398 = CompleteDSLPckg_Connector398 if CompleteDSLPckg_Connector398 is not None else set()
        self.CompleteDSLPckg_Connector416 = CompleteDSLPckg_Connector416
        self.CompleteDSLPckg_Connector1010 = CompleteDSLPckg_Connector1010
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def CompleteDSLPckg_Connector(self):
        return self.__CompleteDSLPckg_Connector

    @CompleteDSLPckg_Connector.setter
    def CompleteDSLPckg_Connector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Connector__CompleteDSLPckg_Connector", None)
        self.__CompleteDSLPckg_Connector = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ConnectorEnd"):
                    opp_val = getattr(item, "CompleteDSLPckg_ConnectorEnd", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ConnectorEnd", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ConnectorEnd"):
                    opp_val = getattr(item, "CompleteDSLPckg_ConnectorEnd", None)
                    
                    setattr(item, "CompleteDSLPckg_ConnectorEnd", self)
                    

    @property
    def CompleteDSLPckg_Connector416(self):
        return self.__CompleteDSLPckg_Connector416

    @CompleteDSLPckg_Connector416.setter
    def CompleteDSLPckg_Connector416(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Connector__CompleteDSLPckg_Connector416", None)
        self.__CompleteDSLPckg_Connector416 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_StructuredClassifier"):
                opp_val = getattr(old_value, "CompleteDSLPckg_StructuredClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_StructuredClassifier"):
                opp_val = getattr(value, "CompleteDSLPckg_StructuredClassifier", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_StructuredClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Connector400(self):
        return self.__CompleteDSLPckg_Connector400

    @CompleteDSLPckg_Connector400.setter
    def CompleteDSLPckg_Connector400(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Connector__CompleteDSLPckg_Connector400", None)
        self.__CompleteDSLPckg_Connector400 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Connector398"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Connector398", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Connector398"):
                opp_val = getattr(value, "CompleteDSLPckg_Connector398", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Connector398", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Connector396(self):
        return self.__CompleteDSLPckg_Connector396

    @CompleteDSLPckg_Connector396.setter
    def CompleteDSLPckg_Connector396(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Connector__CompleteDSLPckg_Connector396", None)
        self.__CompleteDSLPckg_Connector396 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Behavior397"):
                    opp_val = getattr(item, "CompleteDSLPckg_Behavior397", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Behavior397", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Behavior397"):
                    opp_val = getattr(item, "CompleteDSLPckg_Behavior397", None)
                    
                    setattr(item, "CompleteDSLPckg_Behavior397", self)
                    

    @property
    def CompleteDSLPckg_Connector1010(self):
        return self.__CompleteDSLPckg_Connector1010

    @CompleteDSLPckg_Connector1010.setter
    def CompleteDSLPckg_Connector1010(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Connector__CompleteDSLPckg_Connector1010", None)
        self.__CompleteDSLPckg_Connector1010 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Message1009"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Message1009", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Message1009", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Message1009"):
                opp_val = getattr(value, "CompleteDSLPckg_Message1009", None)
                setattr(value, "CompleteDSLPckg_Message1009", self)

    @property
    def CompleteDSLPckg_Connector398(self):
        return self.__CompleteDSLPckg_Connector398

    @CompleteDSLPckg_Connector398.setter
    def CompleteDSLPckg_Connector398(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Connector__CompleteDSLPckg_Connector398", None)
        self.__CompleteDSLPckg_Connector398 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Connector400"):
                    opp_val = getattr(item, "CompleteDSLPckg_Connector400", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Connector400", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Connector400"):
                    opp_val = getattr(item, "CompleteDSLPckg_Connector400", None)
                    
                    setattr(item, "CompleteDSLPckg_Connector400", self)
                    

class CompleteDSLPckg_Interface(Classifier):

    pass
class CompleteDSLPckg_DataType(Classifier):

    pass
class CompleteDSLPckg_Class(StructuredClassifier, EncapsulatedClassifier, Classifier, BehavioredClassifier):

    pass
class Type:

    pass
class RedefinableElement:

    pass
class CompleteDSLPckg_ExtensionPoint(RedefinableElement):

    pass
class CompleteDSLPckg_ActivityEdge(RedefinableElement):

    pass
class CompleteDSLPckg_Substitution(Realization):

    pass
class CompleteDSLPckg_Property(DeploymentTarget, ConnectableElement, StructuralFeature):

    def __init__(self, isComposite: bool, isID: bool, aggregation: str, isDerived: bool, isDerivedUnion: bool, default: str, CompleteDSLPckg_Property: "CompleteDSLPckg_Classifier" = None, 158: "CompleteDSLPckg_Class" = None, CompleteDSLPckg_Property162: "CompleteDSLPckg_Property" = None, CompleteDSLPckg_Property160: set["CompleteDSLPckg_Property"] = None, CompleteDSLPckg_Property164: "CompleteDSLPckg_ValueSpecification" = None, CompleteDSLPckg_Property168: "CompleteDSLPckg_Property" = None, CompleteDSLPckg_Property166: "CompleteDSLPckg_Property" = None, CompleteDSLPckg_Property171: "CompleteDSLPckg_Property" = None, CompleteDSLPckg_Property169: "CompleteDSLPckg_Property" = None, 173: "CompleteDSLPckg_Association" = None, 176: "CompleteDSLPckg_Association" = None, 179: "CompleteDSLPckg_DataType" = None, 182: "CompleteDSLPckg_Interface" = None, 187: "CompleteDSLPckg_Property" = None, 186: set["CompleteDSLPckg_Property"] = None, 191: "CompleteDSLPckg_Property" = None, 190: "CompleteDSLPckg_Property" = None, CompleteDSLPckg_Property245: "CompleteDSLPckg_Association" = None, 248: "CompleteDSLPckg_Association" = None, 251: "CompleteDSLPckg_Association" = None, 254: "CompleteDSLPckg_DataType" = None, 241: "CompleteDSLPckg_Class" = None, 288: "CompleteDSLPckg_Interface" = None, CompleteDSLPckg_Property333: "CompleteDSLPckg_Signal" = None, CompleteDSLPckg_Property403: "CompleteDSLPckg_ConnectorEnd" = None, CompleteDSLPckg_Property411: "CompleteDSLPckg_ConnectorEnd" = None, CompleteDSLPckg_Property422: "CompleteDSLPckg_StructuredClassifier" = None, CompleteDSLPckg_Property425: "CompleteDSLPckg_StructuredClassifier" = None, CompleteDSLPckg_Property450: "CompleteDSLPckg_Artifact" = None, CompleteDSLPckg_Property558: "CompleteDSLPckg_LinkEndData" = None, CompleteDSLPckg_Property633: "CompleteDSLPckg_ReadLinkObjectEndQualifierAction" = None, CompleteDSLPckg_Property614: "CompleteDSLPckg_QualifierValue" = None, CompleteDSLPckg_Property619: "CompleteDSLPckg_ReadLinkObjectEndAction" = None, CompleteDSLPckg_Property1062: "CompleteDSLPckg_InteractionUse" = None):
        self.isComposite = isComposite
        self.isID = isID
        self.aggregation = aggregation
        self.isDerived = isDerived
        self.isDerivedUnion = isDerivedUnion
        self.default = default
        self.CompleteDSLPckg_Property = CompleteDSLPckg_Property
        self.158 = 158
        self.CompleteDSLPckg_Property162 = CompleteDSLPckg_Property162
        self.CompleteDSLPckg_Property160 = CompleteDSLPckg_Property160 if CompleteDSLPckg_Property160 is not None else set()
        self.CompleteDSLPckg_Property164 = CompleteDSLPckg_Property164
        self.CompleteDSLPckg_Property168 = CompleteDSLPckg_Property168
        self.CompleteDSLPckg_Property166 = CompleteDSLPckg_Property166
        self.CompleteDSLPckg_Property171 = CompleteDSLPckg_Property171
        self.CompleteDSLPckg_Property169 = CompleteDSLPckg_Property169
        self.173 = 173
        self.176 = 176
        self.179 = 179
        self.182 = 182
        self.187 = 187
        self.186 = 186 if 186 is not None else set()
        self.191 = 191
        self.190 = 190
        self.CompleteDSLPckg_Property245 = CompleteDSLPckg_Property245
        self.248 = 248
        self.251 = 251
        self.254 = 254
        self.241 = 241
        self.288 = 288
        self.CompleteDSLPckg_Property333 = CompleteDSLPckg_Property333
        self.CompleteDSLPckg_Property403 = CompleteDSLPckg_Property403
        self.CompleteDSLPckg_Property411 = CompleteDSLPckg_Property411
        self.CompleteDSLPckg_Property422 = CompleteDSLPckg_Property422
        self.CompleteDSLPckg_Property425 = CompleteDSLPckg_Property425
        self.CompleteDSLPckg_Property450 = CompleteDSLPckg_Property450
        self.CompleteDSLPckg_Property558 = CompleteDSLPckg_Property558
        self.CompleteDSLPckg_Property633 = CompleteDSLPckg_Property633
        self.CompleteDSLPckg_Property614 = CompleteDSLPckg_Property614
        self.CompleteDSLPckg_Property619 = CompleteDSLPckg_Property619
        self.CompleteDSLPckg_Property1062 = CompleteDSLPckg_Property1062
        
    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

    @property
    def isDerivedUnion(self) -> bool:
        return self.__isDerivedUnion

    @isDerivedUnion.setter
    def isDerivedUnion(self, isDerivedUnion: bool):
        self.__isDerivedUnion = isDerivedUnion

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def isID(self) -> bool:
        return self.__isID

    @isID.setter
    def isID(self, isID: bool):
        self.__isID = isID

    @property
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

    @property
    def CompleteDSLPckg_Property245(self):
        return self.__CompleteDSLPckg_Property245

    @CompleteDSLPckg_Property245.setter
    def CompleteDSLPckg_Property245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property245", None)
        self.__CompleteDSLPckg_Property245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Association"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Association"):
                opp_val = getattr(value, "CompleteDSLPckg_Association", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Property333(self):
        return self.__CompleteDSLPckg_Property333

    @CompleteDSLPckg_Property333.setter
    def CompleteDSLPckg_Property333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property333", None)
        self.__CompleteDSLPckg_Property333 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Signal"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Signal", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Signal"):
                opp_val = getattr(value, "CompleteDSLPckg_Signal", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Signal", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Property614(self):
        return self.__CompleteDSLPckg_Property614

    @CompleteDSLPckg_Property614.setter
    def CompleteDSLPckg_Property614(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property614", None)
        self.__CompleteDSLPckg_Property614 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_QualifierValue613"):
                opp_val = getattr(old_value, "CompleteDSLPckg_QualifierValue613", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_QualifierValue613", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_QualifierValue613"):
                opp_val = getattr(value, "CompleteDSLPckg_QualifierValue613", None)
                setattr(value, "CompleteDSLPckg_QualifierValue613", self)

    @property
    def 187(self):
        return self.__187

    @187.setter
    def 187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__187", None)
        self.__187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "186"):
                opp_val = getattr(old_value, "186", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "186"):
                opp_val = getattr(value, "186", None)
                if opp_val is None:
                    setattr(value, "186", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 173(self):
        return self.__173

    @173.setter
    def 173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__173", None)
        self.__173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "174"):
                opp_val = getattr(old_value, "174", None)
                if opp_val == self:
                    setattr(old_value, "174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "174"):
                opp_val = getattr(value, "174", None)
                setattr(value, "174", self)

    @property
    def CompleteDSLPckg_Property633(self):
        return self.__CompleteDSLPckg_Property633

    @CompleteDSLPckg_Property633.setter
    def CompleteDSLPckg_Property633(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property633", None)
        self.__CompleteDSLPckg_Property633 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ReadLinkObjectEndQualifierAction632"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ReadLinkObjectEndQualifierAction632", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ReadLinkObjectEndQualifierAction632", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ReadLinkObjectEndQualifierAction632"):
                opp_val = getattr(value, "CompleteDSLPckg_ReadLinkObjectEndQualifierAction632", None)
                setattr(value, "CompleteDSLPckg_ReadLinkObjectEndQualifierAction632", self)

    @property
    def CompleteDSLPckg_Property411(self):
        return self.__CompleteDSLPckg_Property411

    @CompleteDSLPckg_Property411.setter
    def CompleteDSLPckg_Property411(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property411", None)
        self.__CompleteDSLPckg_Property411 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ConnectorEnd410"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ConnectorEnd410", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ConnectorEnd410", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ConnectorEnd410"):
                opp_val = getattr(value, "CompleteDSLPckg_ConnectorEnd410", None)
                setattr(value, "CompleteDSLPckg_ConnectorEnd410", self)

    @property
    def CompleteDSLPckg_Property425(self):
        return self.__CompleteDSLPckg_Property425

    @CompleteDSLPckg_Property425.setter
    def CompleteDSLPckg_Property425(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property425", None)
        self.__CompleteDSLPckg_Property425 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_StructuredClassifier424"):
                opp_val = getattr(old_value, "CompleteDSLPckg_StructuredClassifier424", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_StructuredClassifier424"):
                opp_val = getattr(value, "CompleteDSLPckg_StructuredClassifier424", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_StructuredClassifier424", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 191(self):
        return self.__191

    @191.setter
    def 191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__191", None)
        self.__191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "190"):
                opp_val = getattr(old_value, "190", None)
                if opp_val == self:
                    setattr(old_value, "190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "190"):
                opp_val = getattr(value, "190", None)
                setattr(value, "190", self)

    @property
    def 248(self):
        return self.__248

    @248.setter
    def 248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__248", None)
        self.__248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "247"):
                opp_val = getattr(old_value, "247", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "247"):
                opp_val = getattr(value, "247", None)
                if opp_val is None:
                    setattr(value, "247", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Property164(self):
        return self.__CompleteDSLPckg_Property164

    @CompleteDSLPckg_Property164.setter
    def CompleteDSLPckg_Property164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property164", None)
        self.__CompleteDSLPckg_Property164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ValueSpecification165"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ValueSpecification165", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ValueSpecification165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ValueSpecification165"):
                opp_val = getattr(value, "CompleteDSLPckg_ValueSpecification165", None)
                setattr(value, "CompleteDSLPckg_ValueSpecification165", self)

    @property
    def CompleteDSLPckg_Property166(self):
        return self.__CompleteDSLPckg_Property166

    @CompleteDSLPckg_Property166.setter
    def CompleteDSLPckg_Property166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property166", None)
        self.__CompleteDSLPckg_Property166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Property168"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Property168", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Property168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Property168"):
                opp_val = getattr(value, "CompleteDSLPckg_Property168", None)
                setattr(value, "CompleteDSLPckg_Property168", self)

    @property
    def CompleteDSLPckg_Property450(self):
        return self.__CompleteDSLPckg_Property450

    @CompleteDSLPckg_Property450.setter
    def CompleteDSLPckg_Property450(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property450", None)
        self.__CompleteDSLPckg_Property450 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Artifact449"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Artifact449", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Artifact449"):
                opp_val = getattr(value, "CompleteDSLPckg_Artifact449", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Artifact449", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Property1062(self):
        return self.__CompleteDSLPckg_Property1062

    @CompleteDSLPckg_Property1062.setter
    def CompleteDSLPckg_Property1062(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property1062", None)
        self.__CompleteDSLPckg_Property1062 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_InteractionUse1061"):
                opp_val = getattr(old_value, "CompleteDSLPckg_InteractionUse1061", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_InteractionUse1061", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_InteractionUse1061"):
                opp_val = getattr(value, "CompleteDSLPckg_InteractionUse1061", None)
                setattr(value, "CompleteDSLPckg_InteractionUse1061", self)

    @property
    def CompleteDSLPckg_Property160(self):
        return self.__CompleteDSLPckg_Property160

    @CompleteDSLPckg_Property160.setter
    def CompleteDSLPckg_Property160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property160", None)
        self.__CompleteDSLPckg_Property160 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Property162"):
                    opp_val = getattr(item, "CompleteDSLPckg_Property162", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Property162", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Property162"):
                    opp_val = getattr(item, "CompleteDSLPckg_Property162", None)
                    
                    setattr(item, "CompleteDSLPckg_Property162", self)
                    

    @property
    def 190(self):
        return self.__190

    @190.setter
    def 190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__190", None)
        self.__190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "191"):
                opp_val = getattr(old_value, "191", None)
                if opp_val == self:
                    setattr(old_value, "191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "191"):
                opp_val = getattr(value, "191", None)
                setattr(value, "191", self)

    @property
    def CompleteDSLPckg_Property162(self):
        return self.__CompleteDSLPckg_Property162

    @CompleteDSLPckg_Property162.setter
    def CompleteDSLPckg_Property162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property162", None)
        self.__CompleteDSLPckg_Property162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Property160"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Property160", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Property160"):
                opp_val = getattr(value, "CompleteDSLPckg_Property160", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Property160", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 158(self):
        return self.__158

    @158.setter
    def 158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__158", None)
        self.__158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "159"):
                opp_val = getattr(old_value, "159", None)
                if opp_val == self:
                    setattr(old_value, "159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "159"):
                opp_val = getattr(value, "159", None)
                setattr(value, "159", self)

    @property
    def CompleteDSLPckg_Property558(self):
        return self.__CompleteDSLPckg_Property558

    @CompleteDSLPckg_Property558.setter
    def CompleteDSLPckg_Property558(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property558", None)
        self.__CompleteDSLPckg_Property558 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_LinkEndData557"):
                opp_val = getattr(old_value, "CompleteDSLPckg_LinkEndData557", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_LinkEndData557", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_LinkEndData557"):
                opp_val = getattr(value, "CompleteDSLPckg_LinkEndData557", None)
                setattr(value, "CompleteDSLPckg_LinkEndData557", self)

    @property
    def 179(self):
        return self.__179

    @179.setter
    def 179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__179", None)
        self.__179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "180"):
                opp_val = getattr(old_value, "180", None)
                if opp_val == self:
                    setattr(old_value, "180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "180"):
                opp_val = getattr(value, "180", None)
                setattr(value, "180", self)

    @property
    def CompleteDSLPckg_Property171(self):
        return self.__CompleteDSLPckg_Property171

    @CompleteDSLPckg_Property171.setter
    def CompleteDSLPckg_Property171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property171", None)
        self.__CompleteDSLPckg_Property171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Property169"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Property169", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Property169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Property169"):
                opp_val = getattr(value, "CompleteDSLPckg_Property169", None)
                setattr(value, "CompleteDSLPckg_Property169", self)

    @property
    def CompleteDSLPckg_Property169(self):
        return self.__CompleteDSLPckg_Property169

    @CompleteDSLPckg_Property169.setter
    def CompleteDSLPckg_Property169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property169", None)
        self.__CompleteDSLPckg_Property169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Property171"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Property171", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Property171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Property171"):
                opp_val = getattr(value, "CompleteDSLPckg_Property171", None)
                setattr(value, "CompleteDSLPckg_Property171", self)

    @property
    def 176(self):
        return self.__176

    @176.setter
    def 176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__176", None)
        self.__176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "177"):
                opp_val = getattr(old_value, "177", None)
                if opp_val == self:
                    setattr(old_value, "177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "177"):
                opp_val = getattr(value, "177", None)
                setattr(value, "177", self)

    @property
    def 186(self):
        return self.__186

    @186.setter
    def 186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__186", None)
        self.__186 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "187"):
                    opp_val = getattr(item, "187", None)
                    
                    if opp_val == self:
                        setattr(item, "187", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "187"):
                    opp_val = getattr(item, "187", None)
                    
                    setattr(item, "187", self)
                    

    @property
    def 182(self):
        return self.__182

    @182.setter
    def 182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__182", None)
        self.__182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "183"):
                opp_val = getattr(old_value, "183", None)
                if opp_val == self:
                    setattr(old_value, "183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "183"):
                opp_val = getattr(value, "183", None)
                setattr(value, "183", self)

    @property
    def 241(self):
        return self.__241

    @241.setter
    def 241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__241", None)
        self.__241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "240"):
                opp_val = getattr(old_value, "240", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "240"):
                opp_val = getattr(value, "240", None)
                if opp_val is None:
                    setattr(value, "240", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 251(self):
        return self.__251

    @251.setter
    def 251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__251", None)
        self.__251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "250"):
                opp_val = getattr(old_value, "250", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "250"):
                opp_val = getattr(value, "250", None)
                if opp_val is None:
                    setattr(value, "250", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Property619(self):
        return self.__CompleteDSLPckg_Property619

    @CompleteDSLPckg_Property619.setter
    def CompleteDSLPckg_Property619(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property619", None)
        self.__CompleteDSLPckg_Property619 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ReadLinkObjectEndAction"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ReadLinkObjectEndAction", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ReadLinkObjectEndAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ReadLinkObjectEndAction"):
                opp_val = getattr(value, "CompleteDSLPckg_ReadLinkObjectEndAction", None)
                setattr(value, "CompleteDSLPckg_ReadLinkObjectEndAction", self)

    @property
    def CompleteDSLPckg_Property403(self):
        return self.__CompleteDSLPckg_Property403

    @CompleteDSLPckg_Property403.setter
    def CompleteDSLPckg_Property403(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property403", None)
        self.__CompleteDSLPckg_Property403 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ConnectorEnd402"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ConnectorEnd402", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ConnectorEnd402", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ConnectorEnd402"):
                opp_val = getattr(value, "CompleteDSLPckg_ConnectorEnd402", None)
                setattr(value, "CompleteDSLPckg_ConnectorEnd402", self)

    @property
    def CompleteDSLPckg_Property422(self):
        return self.__CompleteDSLPckg_Property422

    @CompleteDSLPckg_Property422.setter
    def CompleteDSLPckg_Property422(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property422", None)
        self.__CompleteDSLPckg_Property422 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_StructuredClassifier421"):
                opp_val = getattr(old_value, "CompleteDSLPckg_StructuredClassifier421", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_StructuredClassifier421"):
                opp_val = getattr(value, "CompleteDSLPckg_StructuredClassifier421", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_StructuredClassifier421", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 288(self):
        return self.__288

    @288.setter
    def 288(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__288", None)
        self.__288 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "287"):
                opp_val = getattr(old_value, "287", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "287"):
                opp_val = getattr(value, "287", None)
                if opp_val is None:
                    setattr(value, "287", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Property(self):
        return self.__CompleteDSLPckg_Property

    @CompleteDSLPckg_Property.setter
    def CompleteDSLPckg_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property", None)
        self.__CompleteDSLPckg_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Classifier133"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Classifier133", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Classifier133"):
                opp_val = getattr(value, "CompleteDSLPckg_Classifier133", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Classifier133", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 254(self):
        return self.__254

    @254.setter
    def 254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__254", None)
        self.__254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "253"):
                opp_val = getattr(old_value, "253", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "253"):
                opp_val = getattr(value, "253", None)
                if opp_val is None:
                    setattr(value, "253", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Property168(self):
        return self.__CompleteDSLPckg_Property168

    @CompleteDSLPckg_Property168.setter
    def CompleteDSLPckg_Property168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Property__CompleteDSLPckg_Property168", None)
        self.__CompleteDSLPckg_Property168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Property166"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Property166", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Property166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Property166"):
                opp_val = getattr(value, "CompleteDSLPckg_Property166", None)
                setattr(value, "CompleteDSLPckg_Property166", self)

class CompleteDSLPckg_Feature(RedefinableElement):

    def __init__(self, isStatic: bool, 131: "CompleteDSLPckg_Classifier" = None, 155: set["CompleteDSLPckg_Classifier"] = None):
        self.isStatic = isStatic
        self.131 = 131
        self.155 = 155 if 155 is not None else set()
        
    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def 131(self):
        return self.__131

    @131.setter
    def 131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Feature__131", None)
        self.__131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "130"):
                opp_val = getattr(old_value, "130", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "130"):
                opp_val = getattr(value, "130", None)
                if opp_val is None:
                    setattr(value, "130", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 155(self):
        return self.__155

    @155.setter
    def 155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Feature__155", None)
        self.__155 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "156"):
                    opp_val = getattr(item, "156", None)
                    
                    if opp_val == self:
                        setattr(item, "156", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "156"):
                    opp_val = getattr(item, "156", None)
                    
                    setattr(item, "156", self)
                    

class LiteralSpecification:

    pass
class CompleteDSLPckg_LiteralBoolean(LiteralSpecification):

    pass
class CompleteDSLPckg_LiteralNull(LiteralSpecification):

    pass
class CompleteDSLPckg_Behavior(Class):

    def __init__(self, isReentrant: bool, CompleteDSLPckg_Behavior: "CompleteDSLPckg_OpaqueExpression" = None, CompleteDSLPckg_Behavior315: "CompleteDSLPckg_BehavioredClassifier" = None, CompleteDSLPckg_Behavior319: "CompleteDSLPckg_Behavior" = None, CompleteDSLPckg_Behavior317: set["CompleteDSLPckg_Behavior"] = None, CompleteDSLPckg_Behavior321: "CompleteDSLPckg_BehavioralFeature" = None, CompleteDSLPckg_Behavior324: set["CompleteDSLPckg_Parameter"] = None, CompleteDSLPckg_Behavior327: set["CompleteDSLPckg_Constraint"] = None, CompleteDSLPckg_Behavior330: set["CompleteDSLPckg_Constraint"] = None, CompleteDSLPckg_Behavior304: "CompleteDSLPckg_BehavioredClassifier" = None, CompleteDSLPckg_Behavior307: "CompleteDSLPckg_BehavioredClassifier" = None, CompleteDSLPckg_Behavior397: "CompleteDSLPckg_Connector" = None, CompleteDSLPckg_Behavior491: "CompleteDSLPckg_CallBehaviorAction" = None, CompleteDSLPckg_Behavior643: "CompleteDSLPckg_ReduceAction" = None, CompleteDSLPckg_Behavior695: "CompleteDSLPckg_Transition" = None, CompleteDSLPckg_Behavior736: "CompleteDSLPckg_State" = None, CompleteDSLPckg_Behavior739: "CompleteDSLPckg_State" = None, CompleteDSLPckg_Behavior742: "CompleteDSLPckg_State" = None, CompleteDSLPckg_Behavior854: "CompleteDSLPckg_DecisionNode" = None, CompleteDSLPckg_Behavior841: "CompleteDSLPckg_ObjectFlow" = None, CompleteDSLPckg_Behavior844: "CompleteDSLPckg_ObjectFlow" = None, CompleteDSLPckg_Behavior1025: "CompleteDSLPckg_BehaviorExecutionSpecification" = None):
        self.isReentrant = isReentrant
        self.CompleteDSLPckg_Behavior = CompleteDSLPckg_Behavior
        self.CompleteDSLPckg_Behavior315 = CompleteDSLPckg_Behavior315
        self.CompleteDSLPckg_Behavior319 = CompleteDSLPckg_Behavior319
        self.CompleteDSLPckg_Behavior317 = CompleteDSLPckg_Behavior317 if CompleteDSLPckg_Behavior317 is not None else set()
        self.CompleteDSLPckg_Behavior321 = CompleteDSLPckg_Behavior321
        self.CompleteDSLPckg_Behavior324 = CompleteDSLPckg_Behavior324 if CompleteDSLPckg_Behavior324 is not None else set()
        self.CompleteDSLPckg_Behavior327 = CompleteDSLPckg_Behavior327 if CompleteDSLPckg_Behavior327 is not None else set()
        self.CompleteDSLPckg_Behavior330 = CompleteDSLPckg_Behavior330 if CompleteDSLPckg_Behavior330 is not None else set()
        self.CompleteDSLPckg_Behavior304 = CompleteDSLPckg_Behavior304
        self.CompleteDSLPckg_Behavior307 = CompleteDSLPckg_Behavior307
        self.CompleteDSLPckg_Behavior397 = CompleteDSLPckg_Behavior397
        self.CompleteDSLPckg_Behavior491 = CompleteDSLPckg_Behavior491
        self.CompleteDSLPckg_Behavior643 = CompleteDSLPckg_Behavior643
        self.CompleteDSLPckg_Behavior695 = CompleteDSLPckg_Behavior695
        self.CompleteDSLPckg_Behavior736 = CompleteDSLPckg_Behavior736
        self.CompleteDSLPckg_Behavior739 = CompleteDSLPckg_Behavior739
        self.CompleteDSLPckg_Behavior742 = CompleteDSLPckg_Behavior742
        self.CompleteDSLPckg_Behavior854 = CompleteDSLPckg_Behavior854
        self.CompleteDSLPckg_Behavior841 = CompleteDSLPckg_Behavior841
        self.CompleteDSLPckg_Behavior844 = CompleteDSLPckg_Behavior844
        self.CompleteDSLPckg_Behavior1025 = CompleteDSLPckg_Behavior1025
        
    @property
    def isReentrant(self) -> bool:
        return self.__isReentrant

    @isReentrant.setter
    def isReentrant(self, isReentrant: bool):
        self.__isReentrant = isReentrant

    @property
    def CompleteDSLPckg_Behavior304(self):
        return self.__CompleteDSLPckg_Behavior304

    @CompleteDSLPckg_Behavior304.setter
    def CompleteDSLPckg_Behavior304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior304", None)
        self.__CompleteDSLPckg_Behavior304 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_BehavioredClassifier"):
                opp_val = getattr(old_value, "CompleteDSLPckg_BehavioredClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_BehavioredClassifier"):
                opp_val = getattr(value, "CompleteDSLPckg_BehavioredClassifier", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_BehavioredClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Behavior1025(self):
        return self.__CompleteDSLPckg_Behavior1025

    @CompleteDSLPckg_Behavior1025.setter
    def CompleteDSLPckg_Behavior1025(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior1025", None)
        self.__CompleteDSLPckg_Behavior1025 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_BehaviorExecutionSpecification"):
                opp_val = getattr(old_value, "CompleteDSLPckg_BehaviorExecutionSpecification", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_BehaviorExecutionSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_BehaviorExecutionSpecification"):
                opp_val = getattr(value, "CompleteDSLPckg_BehaviorExecutionSpecification", None)
                setattr(value, "CompleteDSLPckg_BehaviorExecutionSpecification", self)

    @property
    def CompleteDSLPckg_Behavior307(self):
        return self.__CompleteDSLPckg_Behavior307

    @CompleteDSLPckg_Behavior307.setter
    def CompleteDSLPckg_Behavior307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior307", None)
        self.__CompleteDSLPckg_Behavior307 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_BehavioredClassifier306"):
                opp_val = getattr(old_value, "CompleteDSLPckg_BehavioredClassifier306", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_BehavioredClassifier306", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_BehavioredClassifier306"):
                opp_val = getattr(value, "CompleteDSLPckg_BehavioredClassifier306", None)
                setattr(value, "CompleteDSLPckg_BehavioredClassifier306", self)

    @property
    def CompleteDSLPckg_Behavior491(self):
        return self.__CompleteDSLPckg_Behavior491

    @CompleteDSLPckg_Behavior491.setter
    def CompleteDSLPckg_Behavior491(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior491", None)
        self.__CompleteDSLPckg_Behavior491 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_CallBehaviorAction"):
                opp_val = getattr(old_value, "CompleteDSLPckg_CallBehaviorAction", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_CallBehaviorAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_CallBehaviorAction"):
                opp_val = getattr(value, "CompleteDSLPckg_CallBehaviorAction", None)
                setattr(value, "CompleteDSLPckg_CallBehaviorAction", self)

    @property
    def CompleteDSLPckg_Behavior315(self):
        return self.__CompleteDSLPckg_Behavior315

    @CompleteDSLPckg_Behavior315.setter
    def CompleteDSLPckg_Behavior315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior315", None)
        self.__CompleteDSLPckg_Behavior315 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_BehavioredClassifier316"):
                opp_val = getattr(old_value, "CompleteDSLPckg_BehavioredClassifier316", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_BehavioredClassifier316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_BehavioredClassifier316"):
                opp_val = getattr(value, "CompleteDSLPckg_BehavioredClassifier316", None)
                setattr(value, "CompleteDSLPckg_BehavioredClassifier316", self)

    @property
    def CompleteDSLPckg_Behavior854(self):
        return self.__CompleteDSLPckg_Behavior854

    @CompleteDSLPckg_Behavior854.setter
    def CompleteDSLPckg_Behavior854(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior854", None)
        self.__CompleteDSLPckg_Behavior854 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_DecisionNode853"):
                opp_val = getattr(old_value, "CompleteDSLPckg_DecisionNode853", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_DecisionNode853", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_DecisionNode853"):
                opp_val = getattr(value, "CompleteDSLPckg_DecisionNode853", None)
                setattr(value, "CompleteDSLPckg_DecisionNode853", self)

    @property
    def CompleteDSLPckg_Behavior327(self):
        return self.__CompleteDSLPckg_Behavior327

    @CompleteDSLPckg_Behavior327.setter
    def CompleteDSLPckg_Behavior327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior327", None)
        self.__CompleteDSLPckg_Behavior327 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Constraint328"):
                    opp_val = getattr(item, "CompleteDSLPckg_Constraint328", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Constraint328", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Constraint328"):
                    opp_val = getattr(item, "CompleteDSLPckg_Constraint328", None)
                    
                    setattr(item, "CompleteDSLPckg_Constraint328", self)
                    

    @property
    def CompleteDSLPckg_Behavior739(self):
        return self.__CompleteDSLPckg_Behavior739

    @CompleteDSLPckg_Behavior739.setter
    def CompleteDSLPckg_Behavior739(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior739", None)
        self.__CompleteDSLPckg_Behavior739 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_State738"):
                opp_val = getattr(old_value, "CompleteDSLPckg_State738", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_State738", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_State738"):
                opp_val = getattr(value, "CompleteDSLPckg_State738", None)
                setattr(value, "CompleteDSLPckg_State738", self)

    @property
    def CompleteDSLPckg_Behavior317(self):
        return self.__CompleteDSLPckg_Behavior317

    @CompleteDSLPckg_Behavior317.setter
    def CompleteDSLPckg_Behavior317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior317", None)
        self.__CompleteDSLPckg_Behavior317 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Behavior319"):
                    opp_val = getattr(item, "CompleteDSLPckg_Behavior319", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Behavior319", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Behavior319"):
                    opp_val = getattr(item, "CompleteDSLPckg_Behavior319", None)
                    
                    setattr(item, "CompleteDSLPckg_Behavior319", self)
                    

    @property
    def CompleteDSLPckg_Behavior324(self):
        return self.__CompleteDSLPckg_Behavior324

    @CompleteDSLPckg_Behavior324.setter
    def CompleteDSLPckg_Behavior324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior324", None)
        self.__CompleteDSLPckg_Behavior324 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Parameter325"):
                    opp_val = getattr(item, "CompleteDSLPckg_Parameter325", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Parameter325", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Parameter325"):
                    opp_val = getattr(item, "CompleteDSLPckg_Parameter325", None)
                    
                    setattr(item, "CompleteDSLPckg_Parameter325", self)
                    

    @property
    def CompleteDSLPckg_Behavior844(self):
        return self.__CompleteDSLPckg_Behavior844

    @CompleteDSLPckg_Behavior844.setter
    def CompleteDSLPckg_Behavior844(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior844", None)
        self.__CompleteDSLPckg_Behavior844 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ObjectFlow843"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ObjectFlow843", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ObjectFlow843", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ObjectFlow843"):
                opp_val = getattr(value, "CompleteDSLPckg_ObjectFlow843", None)
                setattr(value, "CompleteDSLPckg_ObjectFlow843", self)

    @property
    def CompleteDSLPckg_Behavior742(self):
        return self.__CompleteDSLPckg_Behavior742

    @CompleteDSLPckg_Behavior742.setter
    def CompleteDSLPckg_Behavior742(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior742", None)
        self.__CompleteDSLPckg_Behavior742 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_State741"):
                opp_val = getattr(old_value, "CompleteDSLPckg_State741", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_State741", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_State741"):
                opp_val = getattr(value, "CompleteDSLPckg_State741", None)
                setattr(value, "CompleteDSLPckg_State741", self)

    @property
    def CompleteDSLPckg_Behavior319(self):
        return self.__CompleteDSLPckg_Behavior319

    @CompleteDSLPckg_Behavior319.setter
    def CompleteDSLPckg_Behavior319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior319", None)
        self.__CompleteDSLPckg_Behavior319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Behavior317"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Behavior317", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Behavior317"):
                opp_val = getattr(value, "CompleteDSLPckg_Behavior317", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Behavior317", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Behavior330(self):
        return self.__CompleteDSLPckg_Behavior330

    @CompleteDSLPckg_Behavior330.setter
    def CompleteDSLPckg_Behavior330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior330", None)
        self.__CompleteDSLPckg_Behavior330 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Constraint331"):
                    opp_val = getattr(item, "CompleteDSLPckg_Constraint331", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Constraint331", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Constraint331"):
                    opp_val = getattr(item, "CompleteDSLPckg_Constraint331", None)
                    
                    setattr(item, "CompleteDSLPckg_Constraint331", self)
                    

    @property
    def CompleteDSLPckg_Behavior321(self):
        return self.__CompleteDSLPckg_Behavior321

    @CompleteDSLPckg_Behavior321.setter
    def CompleteDSLPckg_Behavior321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior321", None)
        self.__CompleteDSLPckg_Behavior321 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_BehavioralFeature322"):
                opp_val = getattr(old_value, "CompleteDSLPckg_BehavioralFeature322", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_BehavioralFeature322", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_BehavioralFeature322"):
                opp_val = getattr(value, "CompleteDSLPckg_BehavioralFeature322", None)
                setattr(value, "CompleteDSLPckg_BehavioralFeature322", self)

    @property
    def CompleteDSLPckg_Behavior695(self):
        return self.__CompleteDSLPckg_Behavior695

    @CompleteDSLPckg_Behavior695.setter
    def CompleteDSLPckg_Behavior695(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior695", None)
        self.__CompleteDSLPckg_Behavior695 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Transition694"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Transition694", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Transition694", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Transition694"):
                opp_val = getattr(value, "CompleteDSLPckg_Transition694", None)
                setattr(value, "CompleteDSLPckg_Transition694", self)

    @property
    def CompleteDSLPckg_Behavior397(self):
        return self.__CompleteDSLPckg_Behavior397

    @CompleteDSLPckg_Behavior397.setter
    def CompleteDSLPckg_Behavior397(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior397", None)
        self.__CompleteDSLPckg_Behavior397 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Connector396"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Connector396", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Connector396"):
                opp_val = getattr(value, "CompleteDSLPckg_Connector396", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Connector396", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Behavior841(self):
        return self.__CompleteDSLPckg_Behavior841

    @CompleteDSLPckg_Behavior841.setter
    def CompleteDSLPckg_Behavior841(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior841", None)
        self.__CompleteDSLPckg_Behavior841 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ObjectFlow"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ObjectFlow", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ObjectFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ObjectFlow"):
                opp_val = getattr(value, "CompleteDSLPckg_ObjectFlow", None)
                setattr(value, "CompleteDSLPckg_ObjectFlow", self)

    @property
    def CompleteDSLPckg_Behavior(self):
        return self.__CompleteDSLPckg_Behavior

    @CompleteDSLPckg_Behavior.setter
    def CompleteDSLPckg_Behavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior", None)
        self.__CompleteDSLPckg_Behavior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_OpaqueExpression96"):
                opp_val = getattr(old_value, "CompleteDSLPckg_OpaqueExpression96", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_OpaqueExpression96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_OpaqueExpression96"):
                opp_val = getattr(value, "CompleteDSLPckg_OpaqueExpression96", None)
                setattr(value, "CompleteDSLPckg_OpaqueExpression96", self)

    @property
    def CompleteDSLPckg_Behavior736(self):
        return self.__CompleteDSLPckg_Behavior736

    @CompleteDSLPckg_Behavior736.setter
    def CompleteDSLPckg_Behavior736(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior736", None)
        self.__CompleteDSLPckg_Behavior736 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_State735"):
                opp_val = getattr(old_value, "CompleteDSLPckg_State735", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_State735", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_State735"):
                opp_val = getattr(value, "CompleteDSLPckg_State735", None)
                setattr(value, "CompleteDSLPckg_State735", self)

    @property
    def CompleteDSLPckg_Behavior643(self):
        return self.__CompleteDSLPckg_Behavior643

    @CompleteDSLPckg_Behavior643.setter
    def CompleteDSLPckg_Behavior643(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Behavior__CompleteDSLPckg_Behavior643", None)
        self.__CompleteDSLPckg_Behavior643 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ReduceAction642"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ReduceAction642", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ReduceAction642", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ReduceAction642"):
                opp_val = getattr(value, "CompleteDSLPckg_ReduceAction642", None)
                setattr(value, "CompleteDSLPckg_ReduceAction642", self)

class CompleteDSLPckg_InstanceValue:

    pass
class CompleteDSLPckg_LiteralUnilimitedNatural(LiteralSpecification):

    pass
class CompleteDSLPckg_LiteralString(LiteralSpecification):

    pass
class CompleteDSLPckg_LiteralReal(LiteralSpecification):

    pass
class CompleteDSLPckg_LiteralInteger(LiteralSpecification):

    pass
class ValueSpecification:

    pass
class CompleteDSLPckg_TimeExpression(ValueSpecification):

    pass
class CompleteDSLPckg_Interval(ValueSpecification):

    pass
class CompleteDSLPckg_Duration(ValueSpecification):

    pass
class CompleteDSLPckg_LiteralSpecification(ValueSpecification):

    pass
class CompleteDSLPckg_OpaqueExpression(ValueSpecification):

    def __init__(self, body: str, language: str, CompleteDSLPckg_OpaqueExpression: "CompleteDSLPckg_Parameter" = None, CompleteDSLPckg_OpaqueExpression96: "CompleteDSLPckg_Behavior" = None, CompleteDSLPckg_OpaqueExpression275: "CompleteDSLPckg_Abstraction" = None):
        self.body = body
        self.language = language
        self.CompleteDSLPckg_OpaqueExpression = CompleteDSLPckg_OpaqueExpression
        self.CompleteDSLPckg_OpaqueExpression96 = CompleteDSLPckg_OpaqueExpression96
        self.CompleteDSLPckg_OpaqueExpression275 = CompleteDSLPckg_OpaqueExpression275
        
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
    def CompleteDSLPckg_OpaqueExpression96(self):
        return self.__CompleteDSLPckg_OpaqueExpression96

    @CompleteDSLPckg_OpaqueExpression96.setter
    def CompleteDSLPckg_OpaqueExpression96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_OpaqueExpression__CompleteDSLPckg_OpaqueExpression96", None)
        self.__CompleteDSLPckg_OpaqueExpression96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Behavior"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Behavior", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Behavior"):
                opp_val = getattr(value, "CompleteDSLPckg_Behavior", None)
                setattr(value, "CompleteDSLPckg_Behavior", self)

    @property
    def CompleteDSLPckg_OpaqueExpression(self):
        return self.__CompleteDSLPckg_OpaqueExpression

    @CompleteDSLPckg_OpaqueExpression.setter
    def CompleteDSLPckg_OpaqueExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_OpaqueExpression__CompleteDSLPckg_OpaqueExpression", None)
        self.__CompleteDSLPckg_OpaqueExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Parameter"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Parameter"):
                opp_val = getattr(value, "CompleteDSLPckg_Parameter", None)
                setattr(value, "CompleteDSLPckg_Parameter", self)

    @property
    def CompleteDSLPckg_OpaqueExpression275(self):
        return self.__CompleteDSLPckg_OpaqueExpression275

    @CompleteDSLPckg_OpaqueExpression275.setter
    def CompleteDSLPckg_OpaqueExpression275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_OpaqueExpression__CompleteDSLPckg_OpaqueExpression275", None)
        self.__CompleteDSLPckg_OpaqueExpression275 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Abstraction"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Abstraction", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Abstraction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Abstraction"):
                opp_val = getattr(value, "CompleteDSLPckg_Abstraction", None)
                setattr(value, "CompleteDSLPckg_Abstraction", self)

class CompleteDSLPckg_Expression(ValueSpecification):

    def __init__(self, symbol: str, CompleteDSLPckg_Expression: "CompleteDSLPckg_ValueSpecification" = None):
        self.symbol = symbol
        self.CompleteDSLPckg_Expression = CompleteDSLPckg_Expression
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def CompleteDSLPckg_Expression(self):
        return self.__CompleteDSLPckg_Expression

    @CompleteDSLPckg_Expression.setter
    def CompleteDSLPckg_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Expression__CompleteDSLPckg_Expression", None)
        self.__CompleteDSLPckg_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ValueSpecification"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ValueSpecification", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ValueSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ValueSpecification"):
                opp_val = getattr(value, "CompleteDSLPckg_ValueSpecification", None)
                setattr(value, "CompleteDSLPckg_ValueSpecification", self)

class TypedElement:

    pass
class CompleteDSLPckg_ConnectableElement(TypedElement):

    pass
class CompleteDSLPckg_Parameter(TypedElement):

    def __init__(self, default: str, CompleteDSLPckg_Parameter: "CompleteDSLPckg_OpaqueExpression" = None, CompleteDSLPckg_Parameter206: "CompleteDSLPckg_BehavioralFeature" = None, CompleteDSLPckg_Parameter209: "CompleteDSLPckg_ValueSpecification" = None, CompleteDSLPckg_Parameter201: "CompleteDSLPckg_BehavioralFeature" = None, CompleteDSLPckg_Parameter325: "CompleteDSLPckg_Behavior" = None, CompleteDSLPckg_Parameter812: "CompleteDSLPckg_ActivityParameterNode" = None, CompleteDSLPckg_Parameter871: "CompleteDSLPckg_ParameterSet" = None):
        self.default = default
        self.CompleteDSLPckg_Parameter = CompleteDSLPckg_Parameter
        self.CompleteDSLPckg_Parameter206 = CompleteDSLPckg_Parameter206
        self.CompleteDSLPckg_Parameter209 = CompleteDSLPckg_Parameter209
        self.CompleteDSLPckg_Parameter201 = CompleteDSLPckg_Parameter201
        self.CompleteDSLPckg_Parameter325 = CompleteDSLPckg_Parameter325
        self.CompleteDSLPckg_Parameter812 = CompleteDSLPckg_Parameter812
        self.CompleteDSLPckg_Parameter871 = CompleteDSLPckg_Parameter871
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def CompleteDSLPckg_Parameter201(self):
        return self.__CompleteDSLPckg_Parameter201

    @CompleteDSLPckg_Parameter201.setter
    def CompleteDSLPckg_Parameter201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Parameter__CompleteDSLPckg_Parameter201", None)
        self.__CompleteDSLPckg_Parameter201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_BehavioralFeature"):
                opp_val = getattr(old_value, "CompleteDSLPckg_BehavioralFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_BehavioralFeature"):
                opp_val = getattr(value, "CompleteDSLPckg_BehavioralFeature", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_BehavioralFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Parameter206(self):
        return self.__CompleteDSLPckg_Parameter206

    @CompleteDSLPckg_Parameter206.setter
    def CompleteDSLPckg_Parameter206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Parameter__CompleteDSLPckg_Parameter206", None)
        self.__CompleteDSLPckg_Parameter206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_BehavioralFeature207"):
                opp_val = getattr(old_value, "CompleteDSLPckg_BehavioralFeature207", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_BehavioralFeature207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_BehavioralFeature207"):
                opp_val = getattr(value, "CompleteDSLPckg_BehavioralFeature207", None)
                setattr(value, "CompleteDSLPckg_BehavioralFeature207", self)

    @property
    def CompleteDSLPckg_Parameter209(self):
        return self.__CompleteDSLPckg_Parameter209

    @CompleteDSLPckg_Parameter209.setter
    def CompleteDSLPckg_Parameter209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Parameter__CompleteDSLPckg_Parameter209", None)
        self.__CompleteDSLPckg_Parameter209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ValueSpecification210"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ValueSpecification210", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ValueSpecification210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ValueSpecification210"):
                opp_val = getattr(value, "CompleteDSLPckg_ValueSpecification210", None)
                setattr(value, "CompleteDSLPckg_ValueSpecification210", self)

    @property
    def CompleteDSLPckg_Parameter(self):
        return self.__CompleteDSLPckg_Parameter

    @CompleteDSLPckg_Parameter.setter
    def CompleteDSLPckg_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Parameter__CompleteDSLPckg_Parameter", None)
        self.__CompleteDSLPckg_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_OpaqueExpression"):
                opp_val = getattr(old_value, "CompleteDSLPckg_OpaqueExpression", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_OpaqueExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_OpaqueExpression"):
                opp_val = getattr(value, "CompleteDSLPckg_OpaqueExpression", None)
                setattr(value, "CompleteDSLPckg_OpaqueExpression", self)

    @property
    def CompleteDSLPckg_Parameter871(self):
        return self.__CompleteDSLPckg_Parameter871

    @CompleteDSLPckg_Parameter871.setter
    def CompleteDSLPckg_Parameter871(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Parameter__CompleteDSLPckg_Parameter871", None)
        self.__CompleteDSLPckg_Parameter871 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ParameterSet"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ParameterSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ParameterSet"):
                opp_val = getattr(value, "CompleteDSLPckg_ParameterSet", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_ParameterSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Parameter325(self):
        return self.__CompleteDSLPckg_Parameter325

    @CompleteDSLPckg_Parameter325.setter
    def CompleteDSLPckg_Parameter325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Parameter__CompleteDSLPckg_Parameter325", None)
        self.__CompleteDSLPckg_Parameter325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Behavior324"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Behavior324", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Behavior324"):
                opp_val = getattr(value, "CompleteDSLPckg_Behavior324", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Behavior324", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Parameter812(self):
        return self.__CompleteDSLPckg_Parameter812

    @CompleteDSLPckg_Parameter812.setter
    def CompleteDSLPckg_Parameter812(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Parameter__CompleteDSLPckg_Parameter812", None)
        self.__CompleteDSLPckg_Parameter812 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ActivityParameterNode"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ActivityParameterNode", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ActivityParameterNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ActivityParameterNode"):
                opp_val = getattr(value, "CompleteDSLPckg_ActivityParameterNode", None)
                setattr(value, "CompleteDSLPckg_ActivityParameterNode", self)

class CompleteDSLPckg_ObjectNode(TypedElement, ActivityNode):

    pass
class CompleteDSLPckg_StructuralFeature(TypedElement, Feature, MultiplicityElement):

    def __init__(self, isReadOnly: bool, CompleteDSLPckg_StructuralFeature: "CompleteDSLPckg_Slot" = None, CompleteDSLPckg_StructuralFeature532: "CompleteDSLPckg_StructuralFeatureAction" = None):
        self.isReadOnly = isReadOnly
        self.CompleteDSLPckg_StructuralFeature = CompleteDSLPckg_StructuralFeature
        self.CompleteDSLPckg_StructuralFeature532 = CompleteDSLPckg_StructuralFeature532
        
    @property
    def isReadOnly(self) -> bool:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly

    @property
    def CompleteDSLPckg_StructuralFeature532(self):
        return self.__CompleteDSLPckg_StructuralFeature532

    @CompleteDSLPckg_StructuralFeature532.setter
    def CompleteDSLPckg_StructuralFeature532(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuralFeature__CompleteDSLPckg_StructuralFeature532", None)
        self.__CompleteDSLPckg_StructuralFeature532 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_StructuralFeatureAction"):
                opp_val = getattr(old_value, "CompleteDSLPckg_StructuralFeatureAction", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_StructuralFeatureAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_StructuralFeatureAction"):
                opp_val = getattr(value, "CompleteDSLPckg_StructuralFeatureAction", None)
                setattr(value, "CompleteDSLPckg_StructuralFeatureAction", self)

    @property
    def CompleteDSLPckg_StructuralFeature(self):
        return self.__CompleteDSLPckg_StructuralFeature

    @CompleteDSLPckg_StructuralFeature.setter
    def CompleteDSLPckg_StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuralFeature__CompleteDSLPckg_StructuralFeature", None)
        self.__CompleteDSLPckg_StructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Slot"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Slot", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Slot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Slot"):
                opp_val = getattr(value, "CompleteDSLPckg_Slot", None)
                setattr(value, "CompleteDSLPckg_Slot", self)

class CompleteDSLPckg_Pin(TypedElement, MultiplicityElement):

    pass
class CompleteDSLPckg_Variable(TypedElement, MultiplicityElement, ConnectableElement):

    pass
class Relationship:

    pass
class CompleteDSLPckg_Association(Relationship, Classifier):

    def __init__(self, isDerived: bool, 174: "CompleteDSLPckg_Property" = None, 177: "CompleteDSLPckg_Property" = None, CompleteDSLPckg_Association: set["CompleteDSLPckg_Property"] = None, 247: set["CompleteDSLPckg_Property"] = None, 250: set["CompleteDSLPckg_Property"] = None, CompleteDSLPckg_Association408: "CompleteDSLPckg_ConnectorEnd" = None):
        self.isDerived = isDerived
        self.174 = 174
        self.177 = 177
        self.CompleteDSLPckg_Association = CompleteDSLPckg_Association if CompleteDSLPckg_Association is not None else set()
        self.247 = 247 if 247 is not None else set()
        self.250 = 250 if 250 is not None else set()
        self.CompleteDSLPckg_Association408 = CompleteDSLPckg_Association408
        
    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

    @property
    def CompleteDSLPckg_Association408(self):
        return self.__CompleteDSLPckg_Association408

    @CompleteDSLPckg_Association408.setter
    def CompleteDSLPckg_Association408(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Association__CompleteDSLPckg_Association408", None)
        self.__CompleteDSLPckg_Association408 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ConnectorEnd407"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ConnectorEnd407", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ConnectorEnd407", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ConnectorEnd407"):
                opp_val = getattr(value, "CompleteDSLPckg_ConnectorEnd407", None)
                setattr(value, "CompleteDSLPckg_ConnectorEnd407", self)

    @property
    def 174(self):
        return self.__174

    @174.setter
    def 174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Association__174", None)
        self.__174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "173"):
                opp_val = getattr(old_value, "173", None)
                if opp_val == self:
                    setattr(old_value, "173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "173"):
                opp_val = getattr(value, "173", None)
                setattr(value, "173", self)

    @property
    def 177(self):
        return self.__177

    @177.setter
    def 177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Association__177", None)
        self.__177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "176"):
                opp_val = getattr(old_value, "176", None)
                if opp_val == self:
                    setattr(old_value, "176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "176"):
                opp_val = getattr(value, "176", None)
                setattr(value, "176", self)

    @property
    def 247(self):
        return self.__247

    @247.setter
    def 247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Association__247", None)
        self.__247 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "248"):
                    opp_val = getattr(item, "248", None)
                    
                    if opp_val == self:
                        setattr(item, "248", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "248"):
                    opp_val = getattr(item, "248", None)
                    
                    setattr(item, "248", self)
                    

    @property
    def 250(self):
        return self.__250

    @250.setter
    def 250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Association__250", None)
        self.__250 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "251"):
                    opp_val = getattr(item, "251", None)
                    
                    if opp_val == self:
                        setattr(item, "251", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "251"):
                    opp_val = getattr(item, "251", None)
                    
                    setattr(item, "251", self)
                    

    @property
    def CompleteDSLPckg_Association(self):
        return self.__CompleteDSLPckg_Association

    @CompleteDSLPckg_Association.setter
    def CompleteDSLPckg_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Association__CompleteDSLPckg_Association", None)
        self.__CompleteDSLPckg_Association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Property245"):
                    opp_val = getattr(item, "CompleteDSLPckg_Property245", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Property245", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Property245"):
                    opp_val = getattr(item, "CompleteDSLPckg_Property245", None)
                    
                    setattr(item, "CompleteDSLPckg_Property245", self)
                    

class CompleteDSLPckg_DirectedRelationship(Relationship):

    pass
class NamedElement:

    pass
class CompleteDSLPckg_Message(NamedElement):

    def __init__(self, messageKind: str, messageSort: str, CompleteDSLPckg_Message1012: "CompleteDSLPckg_NamedElement" = None, CompleteDSLPckg_Message1015: "CompleteDSLPckg_MessageEnd" = None, CompleteDSLPckg_Message1017: "CompleteDSLPckg_MessageEnd" = None, CompleteDSLPckg_Message1021: "CompleteDSLPckg_MessageEnd" = None, CompleteDSLPckg_Message: set["CompleteDSLPckg_ValueSpecification"] = None, CompleteDSLPckg_Message1009: "CompleteDSLPckg_Connector" = None):
        self.messageKind = messageKind
        self.messageSort = messageSort
        self.CompleteDSLPckg_Message1012 = CompleteDSLPckg_Message1012
        self.CompleteDSLPckg_Message1015 = CompleteDSLPckg_Message1015
        self.CompleteDSLPckg_Message1017 = CompleteDSLPckg_Message1017
        self.CompleteDSLPckg_Message1021 = CompleteDSLPckg_Message1021
        self.CompleteDSLPckg_Message = CompleteDSLPckg_Message if CompleteDSLPckg_Message is not None else set()
        self.CompleteDSLPckg_Message1009 = CompleteDSLPckg_Message1009
        
    @property
    def messageKind(self) -> str:
        return self.__messageKind

    @messageKind.setter
    def messageKind(self, messageKind: str):
        self.__messageKind = messageKind

    @property
    def messageSort(self) -> str:
        return self.__messageSort

    @messageSort.setter
    def messageSort(self, messageSort: str):
        self.__messageSort = messageSort

    @property
    def CompleteDSLPckg_Message1021(self):
        return self.__CompleteDSLPckg_Message1021

    @CompleteDSLPckg_Message1021.setter
    def CompleteDSLPckg_Message1021(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Message__CompleteDSLPckg_Message1021", None)
        self.__CompleteDSLPckg_Message1021 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_MessageEnd1020"):
                opp_val = getattr(old_value, "CompleteDSLPckg_MessageEnd1020", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_MessageEnd1020", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_MessageEnd1020"):
                opp_val = getattr(value, "CompleteDSLPckg_MessageEnd1020", None)
                setattr(value, "CompleteDSLPckg_MessageEnd1020", self)

    @property
    def CompleteDSLPckg_Message1015(self):
        return self.__CompleteDSLPckg_Message1015

    @CompleteDSLPckg_Message1015.setter
    def CompleteDSLPckg_Message1015(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Message__CompleteDSLPckg_Message1015", None)
        self.__CompleteDSLPckg_Message1015 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_MessageEnd"):
                opp_val = getattr(old_value, "CompleteDSLPckg_MessageEnd", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_MessageEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_MessageEnd"):
                opp_val = getattr(value, "CompleteDSLPckg_MessageEnd", None)
                setattr(value, "CompleteDSLPckg_MessageEnd", self)

    @property
    def CompleteDSLPckg_Message1009(self):
        return self.__CompleteDSLPckg_Message1009

    @CompleteDSLPckg_Message1009.setter
    def CompleteDSLPckg_Message1009(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Message__CompleteDSLPckg_Message1009", None)
        self.__CompleteDSLPckg_Message1009 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Connector1010"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Connector1010", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Connector1010", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Connector1010"):
                opp_val = getattr(value, "CompleteDSLPckg_Connector1010", None)
                setattr(value, "CompleteDSLPckg_Connector1010", self)

    @property
    def CompleteDSLPckg_Message1012(self):
        return self.__CompleteDSLPckg_Message1012

    @CompleteDSLPckg_Message1012.setter
    def CompleteDSLPckg_Message1012(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Message__CompleteDSLPckg_Message1012", None)
        self.__CompleteDSLPckg_Message1012 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_NamedElement1013"):
                opp_val = getattr(old_value, "CompleteDSLPckg_NamedElement1013", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_NamedElement1013", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_NamedElement1013"):
                opp_val = getattr(value, "CompleteDSLPckg_NamedElement1013", None)
                setattr(value, "CompleteDSLPckg_NamedElement1013", self)

    @property
    def CompleteDSLPckg_Message1017(self):
        return self.__CompleteDSLPckg_Message1017

    @CompleteDSLPckg_Message1017.setter
    def CompleteDSLPckg_Message1017(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Message__CompleteDSLPckg_Message1017", None)
        self.__CompleteDSLPckg_Message1017 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_MessageEnd1018"):
                opp_val = getattr(old_value, "CompleteDSLPckg_MessageEnd1018", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_MessageEnd1018", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_MessageEnd1018"):
                opp_val = getattr(value, "CompleteDSLPckg_MessageEnd1018", None)
                setattr(value, "CompleteDSLPckg_MessageEnd1018", self)

    @property
    def CompleteDSLPckg_Message(self):
        return self.__CompleteDSLPckg_Message

    @CompleteDSLPckg_Message.setter
    def CompleteDSLPckg_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Message__CompleteDSLPckg_Message", None)
        self.__CompleteDSLPckg_Message = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ValueSpecification1007"):
                    opp_val = getattr(item, "CompleteDSLPckg_ValueSpecification1007", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ValueSpecification1007", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ValueSpecification1007"):
                    opp_val = getattr(item, "CompleteDSLPckg_ValueSpecification1007", None)
                    
                    setattr(item, "CompleteDSLPckg_ValueSpecification1007", self)
                    

class CompleteDSLPckg_ActivityGroup(NamedElement):

    pass
class CompleteDSLPckg_ParameterSet(NamedElement):

    pass
class CompleteDSLPckg_CollaborationUse(NamedElement):

    pass
class CompleteDSLPckg_ActivityNode(RedefinableElement, NamedElement):

    pass
class CompleteDSLPckg_TypedElement(NamedElement):

    pass
class CompleteDSLPckg_GeneralOrdering(NamedElement):

    pass
class CompleteDSLPckg_RedefinableElement(NamedElement):

    def __init__(self, isLeaf: bool, CompleteDSLPckg_RedefinableElement: "CompleteDSLPckg_RedefinableElement" = None, CompleteDSLPckg_RedefinableElement121: set["CompleteDSLPckg_RedefinableElement"] = None, CompleteDSLPckg_RedefinableElement124: set["CompleteDSLPckg_Classifier"] = None):
        self.isLeaf = isLeaf
        self.CompleteDSLPckg_RedefinableElement = CompleteDSLPckg_RedefinableElement
        self.CompleteDSLPckg_RedefinableElement121 = CompleteDSLPckg_RedefinableElement121 if CompleteDSLPckg_RedefinableElement121 is not None else set()
        self.CompleteDSLPckg_RedefinableElement124 = CompleteDSLPckg_RedefinableElement124 if CompleteDSLPckg_RedefinableElement124 is not None else set()
        
    @property
    def isLeaf(self) -> bool:
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: bool):
        self.__isLeaf = isLeaf

    @property
    def CompleteDSLPckg_RedefinableElement(self):
        return self.__CompleteDSLPckg_RedefinableElement

    @CompleteDSLPckg_RedefinableElement.setter
    def CompleteDSLPckg_RedefinableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_RedefinableElement__CompleteDSLPckg_RedefinableElement", None)
        self.__CompleteDSLPckg_RedefinableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_RedefinableElement121"):
                opp_val = getattr(old_value, "CompleteDSLPckg_RedefinableElement121", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_RedefinableElement121"):
                opp_val = getattr(value, "CompleteDSLPckg_RedefinableElement121", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_RedefinableElement121", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_RedefinableElement124(self):
        return self.__CompleteDSLPckg_RedefinableElement124

    @CompleteDSLPckg_RedefinableElement124.setter
    def CompleteDSLPckg_RedefinableElement124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_RedefinableElement__CompleteDSLPckg_RedefinableElement124", None)
        self.__CompleteDSLPckg_RedefinableElement124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Classifier125"):
                    opp_val = getattr(item, "CompleteDSLPckg_Classifier125", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Classifier125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Classifier125"):
                    opp_val = getattr(item, "CompleteDSLPckg_Classifier125", None)
                    
                    setattr(item, "CompleteDSLPckg_Classifier125", self)
                    

    @property
    def CompleteDSLPckg_RedefinableElement121(self):
        return self.__CompleteDSLPckg_RedefinableElement121

    @CompleteDSLPckg_RedefinableElement121.setter
    def CompleteDSLPckg_RedefinableElement121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_RedefinableElement__CompleteDSLPckg_RedefinableElement121", None)
        self.__CompleteDSLPckg_RedefinableElement121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_RedefinableElement"):
                    opp_val = getattr(item, "CompleteDSLPckg_RedefinableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_RedefinableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_RedefinableElement"):
                    opp_val = getattr(item, "CompleteDSLPckg_RedefinableElement", None)
                    
                    setattr(item, "CompleteDSLPckg_RedefinableElement", self)
                    

class CompleteDSLPckg_Component(NamedElement, Class):

    def __init__(self, isIndirectlyInstantiated: bool, CompleteDSLPckg_Component: set["CompleteDSLPckg_Interface"] = None, CompleteDSLPckg_Component381: set["CompleteDSLPckg_Interface"] = None, CompleteDSLPckg_Component384: set["CompleteDSLPckg_ComponentRealization"] = None, CompleteDSLPckg_Component386: set["CompleteDSLPckg_PackageableElement"] = None, CompleteDSLPckg_Component390: "CompleteDSLPckg_ComponentRealization" = None):
        self.isIndirectlyInstantiated = isIndirectlyInstantiated
        self.CompleteDSLPckg_Component = CompleteDSLPckg_Component if CompleteDSLPckg_Component is not None else set()
        self.CompleteDSLPckg_Component381 = CompleteDSLPckg_Component381 if CompleteDSLPckg_Component381 is not None else set()
        self.CompleteDSLPckg_Component384 = CompleteDSLPckg_Component384 if CompleteDSLPckg_Component384 is not None else set()
        self.CompleteDSLPckg_Component386 = CompleteDSLPckg_Component386 if CompleteDSLPckg_Component386 is not None else set()
        self.CompleteDSLPckg_Component390 = CompleteDSLPckg_Component390
        
    @property
    def isIndirectlyInstantiated(self) -> bool:
        return self.__isIndirectlyInstantiated

    @isIndirectlyInstantiated.setter
    def isIndirectlyInstantiated(self, isIndirectlyInstantiated: bool):
        self.__isIndirectlyInstantiated = isIndirectlyInstantiated

    @property
    def CompleteDSLPckg_Component(self):
        return self.__CompleteDSLPckg_Component

    @CompleteDSLPckg_Component.setter
    def CompleteDSLPckg_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Component__CompleteDSLPckg_Component", None)
        self.__CompleteDSLPckg_Component = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Interface379"):
                    opp_val = getattr(item, "CompleteDSLPckg_Interface379", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Interface379", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Interface379"):
                    opp_val = getattr(item, "CompleteDSLPckg_Interface379", None)
                    
                    setattr(item, "CompleteDSLPckg_Interface379", self)
                    

    @property
    def CompleteDSLPckg_Component384(self):
        return self.__CompleteDSLPckg_Component384

    @CompleteDSLPckg_Component384.setter
    def CompleteDSLPckg_Component384(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Component__CompleteDSLPckg_Component384", None)
        self.__CompleteDSLPckg_Component384 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ComponentRealization"):
                    opp_val = getattr(item, "CompleteDSLPckg_ComponentRealization", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ComponentRealization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ComponentRealization"):
                    opp_val = getattr(item, "CompleteDSLPckg_ComponentRealization", None)
                    
                    setattr(item, "CompleteDSLPckg_ComponentRealization", self)
                    

    @property
    def CompleteDSLPckg_Component381(self):
        return self.__CompleteDSLPckg_Component381

    @CompleteDSLPckg_Component381.setter
    def CompleteDSLPckg_Component381(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Component__CompleteDSLPckg_Component381", None)
        self.__CompleteDSLPckg_Component381 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Interface382"):
                    opp_val = getattr(item, "CompleteDSLPckg_Interface382", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Interface382", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Interface382"):
                    opp_val = getattr(item, "CompleteDSLPckg_Interface382", None)
                    
                    setattr(item, "CompleteDSLPckg_Interface382", self)
                    

    @property
    def CompleteDSLPckg_Component390(self):
        return self.__CompleteDSLPckg_Component390

    @CompleteDSLPckg_Component390.setter
    def CompleteDSLPckg_Component390(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Component__CompleteDSLPckg_Component390", None)
        self.__CompleteDSLPckg_Component390 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ComponentRealization389"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ComponentRealization389", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ComponentRealization389", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ComponentRealization389"):
                opp_val = getattr(value, "CompleteDSLPckg_ComponentRealization389", None)
                setattr(value, "CompleteDSLPckg_ComponentRealization389", self)

    @property
    def CompleteDSLPckg_Component386(self):
        return self.__CompleteDSLPckg_Component386

    @CompleteDSLPckg_Component386.setter
    def CompleteDSLPckg_Component386(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Component__CompleteDSLPckg_Component386", None)
        self.__CompleteDSLPckg_Component386 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_PackageableElement387"):
                    opp_val = getattr(item, "CompleteDSLPckg_PackageableElement387", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_PackageableElement387", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_PackageableElement387"):
                    opp_val = getattr(item, "CompleteDSLPckg_PackageableElement387", None)
                    
                    setattr(item, "CompleteDSLPckg_PackageableElement387", self)
                    

class CompleteDSLPckg_Artifact(NamedElement, Classifier, DeployedArtifact):

    def __init__(self, fileName: str, CompleteDSLPckg_Artifact: set["CompleteDSLPckg_Operation"] = None, CompleteDSLPckg_Artifact449: set["CompleteDSLPckg_Property"] = None, CompleteDSLPckg_Artifact453: "CompleteDSLPckg_Artifact" = None, CompleteDSLPckg_Artifact451: set["CompleteDSLPckg_Artifact"] = None, CompleteDSLPckg_Artifact455: set["CompleteDSLPckg_Manifestation"] = None):
        self.fileName = fileName
        self.CompleteDSLPckg_Artifact = CompleteDSLPckg_Artifact if CompleteDSLPckg_Artifact is not None else set()
        self.CompleteDSLPckg_Artifact449 = CompleteDSLPckg_Artifact449 if CompleteDSLPckg_Artifact449 is not None else set()
        self.CompleteDSLPckg_Artifact453 = CompleteDSLPckg_Artifact453
        self.CompleteDSLPckg_Artifact451 = CompleteDSLPckg_Artifact451 if CompleteDSLPckg_Artifact451 is not None else set()
        self.CompleteDSLPckg_Artifact455 = CompleteDSLPckg_Artifact455 if CompleteDSLPckg_Artifact455 is not None else set()
        
    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def CompleteDSLPckg_Artifact455(self):
        return self.__CompleteDSLPckg_Artifact455

    @CompleteDSLPckg_Artifact455.setter
    def CompleteDSLPckg_Artifact455(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Artifact__CompleteDSLPckg_Artifact455", None)
        self.__CompleteDSLPckg_Artifact455 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Manifestation"):
                    opp_val = getattr(item, "CompleteDSLPckg_Manifestation", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Manifestation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Manifestation"):
                    opp_val = getattr(item, "CompleteDSLPckg_Manifestation", None)
                    
                    setattr(item, "CompleteDSLPckg_Manifestation", self)
                    

    @property
    def CompleteDSLPckg_Artifact451(self):
        return self.__CompleteDSLPckg_Artifact451

    @CompleteDSLPckg_Artifact451.setter
    def CompleteDSLPckg_Artifact451(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Artifact__CompleteDSLPckg_Artifact451", None)
        self.__CompleteDSLPckg_Artifact451 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Artifact453"):
                    opp_val = getattr(item, "CompleteDSLPckg_Artifact453", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Artifact453", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Artifact453"):
                    opp_val = getattr(item, "CompleteDSLPckg_Artifact453", None)
                    
                    setattr(item, "CompleteDSLPckg_Artifact453", self)
                    

    @property
    def CompleteDSLPckg_Artifact(self):
        return self.__CompleteDSLPckg_Artifact

    @CompleteDSLPckg_Artifact.setter
    def CompleteDSLPckg_Artifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Artifact__CompleteDSLPckg_Artifact", None)
        self.__CompleteDSLPckg_Artifact = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Operation447"):
                    opp_val = getattr(item, "CompleteDSLPckg_Operation447", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Operation447", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Operation447"):
                    opp_val = getattr(item, "CompleteDSLPckg_Operation447", None)
                    
                    setattr(item, "CompleteDSLPckg_Operation447", self)
                    

    @property
    def CompleteDSLPckg_Artifact453(self):
        return self.__CompleteDSLPckg_Artifact453

    @CompleteDSLPckg_Artifact453.setter
    def CompleteDSLPckg_Artifact453(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Artifact__CompleteDSLPckg_Artifact453", None)
        self.__CompleteDSLPckg_Artifact453 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Artifact451"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Artifact451", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Artifact451"):
                opp_val = getattr(value, "CompleteDSLPckg_Artifact451", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Artifact451", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Artifact449(self):
        return self.__CompleteDSLPckg_Artifact449

    @CompleteDSLPckg_Artifact449.setter
    def CompleteDSLPckg_Artifact449(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Artifact__CompleteDSLPckg_Artifact449", None)
        self.__CompleteDSLPckg_Artifact449 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Property450"):
                    opp_val = getattr(item, "CompleteDSLPckg_Property450", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Property450", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Property450"):
                    opp_val = getattr(item, "CompleteDSLPckg_Property450", None)
                    
                    setattr(item, "CompleteDSLPckg_Property450", self)
                    

class CompleteDSLPckg_PackageableElement(NamedElement):

    pass
class CompleteDSLPckg_Action(NamedElement):

    pass
class CompleteDSLPckg_DeploymentTarget(NamedElement):

    pass
class CompleteDSLPckg_Lifeline(NamedElement):

    pass
class CompleteDSLPckg_DeployedArtifact(NamedElement):

    pass
class CompleteDSLPckg_InteractionFragment(NamedElement):

    pass
class CompleteDSLPckg_Vertex(NamedElement):

    pass
class CompleteDSLPckg_Trigger(NamedElement):

    pass
class CompleteDSLPckg_MessageEnd(NamedElement):

    pass
class PackageableElement:

    pass
class CompleteDSLPckg_GeneralizationSet(PackageableElement):

    def __init__(self, isCovering: bool, isDisjoint: bool, 148: "CompleteDSLPckg_Classifier" = None, 199: "CompleteDSLPckg_Generalization" = None, 312: set["CompleteDSLPckg_Generalization"] = None, 309: "CompleteDSLPckg_Classifier" = None):
        self.isCovering = isCovering
        self.isDisjoint = isDisjoint
        self.148 = 148
        self.199 = 199
        self.312 = 312 if 312 is not None else set()
        self.309 = 309
        
    @property
    def isDisjoint(self) -> bool:
        return self.__isDisjoint

    @isDisjoint.setter
    def isDisjoint(self, isDisjoint: bool):
        self.__isDisjoint = isDisjoint

    @property
    def isCovering(self) -> bool:
        return self.__isCovering

    @isCovering.setter
    def isCovering(self, isCovering: bool):
        self.__isCovering = isCovering

    @property
    def 148(self):
        return self.__148

    @148.setter
    def 148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_GeneralizationSet__148", None)
        self.__148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "147"):
                opp_val = getattr(old_value, "147", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "147"):
                opp_val = getattr(value, "147", None)
                if opp_val is None:
                    setattr(value, "147", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 312(self):
        return self.__312

    @312.setter
    def 312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_GeneralizationSet__312", None)
        self.__312 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "313"):
                    opp_val = getattr(item, "313", None)
                    
                    if opp_val == self:
                        setattr(item, "313", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "313"):
                    opp_val = getattr(item, "313", None)
                    
                    setattr(item, "313", self)
                    

    @property
    def 199(self):
        return self.__199

    @199.setter
    def 199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_GeneralizationSet__199", None)
        self.__199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "198"):
                opp_val = getattr(old_value, "198", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "198"):
                opp_val = getattr(value, "198", None)
                if opp_val is None:
                    setattr(value, "198", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 309(self):
        return self.__309

    @309.setter
    def 309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_GeneralizationSet__309", None)
        self.__309 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "310"):
                opp_val = getattr(old_value, "310", None)
                if opp_val == self:
                    setattr(old_value, "310", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "310"):
                opp_val = getattr(value, "310", None)
                setattr(value, "310", self)

class CompleteDSLPckg_Event(PackageableElement):

    pass
class CompleteDSLPckg_InstanceSpecification(PackageableElement):

    pass
class CompleteDSLPckg_Observation(PackageableElement):

    pass
class CompleteDSLPckg_Type(PackageableElement):

    pass
class CompleteDSLPckg_ValueSpecification(TypedElement, PackageableElement):

    pass
class Namespace:

    pass
class CompleteDSLPckg_Transition(RedefinableElement, Namespace):

    def __init__(self, kind: str, CompleteDSLPckg_Transition683: "CompleteDSLPckg_Vertex" = None, CompleteDSLPckg_Transition688: "CompleteDSLPckg_Vertex" = None, CompleteDSLPckg_Transition691: "CompleteDSLPckg_Vertex" = None, CompleteDSLPckg_Transition694: "CompleteDSLPckg_Behavior" = None, CompleteDSLPckg_Transition697: "CompleteDSLPckg_Trigger" = None, CompleteDSLPckg_Transition700: "CompleteDSLPckg_Constraint" = None, CompleteDSLPckg_Transition703: "CompleteDSLPckg_Region" = None, CompleteDSLPckg_Transition: "CompleteDSLPckg_Region" = None, CompleteDSLPckg_Transition680: "CompleteDSLPckg_Vertex" = None, CompleteDSLPckg_Transition707: "CompleteDSLPckg_Transition" = None, CompleteDSLPckg_Transition705: "CompleteDSLPckg_Transition" = None):
        self.kind = kind
        self.CompleteDSLPckg_Transition683 = CompleteDSLPckg_Transition683
        self.CompleteDSLPckg_Transition688 = CompleteDSLPckg_Transition688
        self.CompleteDSLPckg_Transition691 = CompleteDSLPckg_Transition691
        self.CompleteDSLPckg_Transition694 = CompleteDSLPckg_Transition694
        self.CompleteDSLPckg_Transition697 = CompleteDSLPckg_Transition697
        self.CompleteDSLPckg_Transition700 = CompleteDSLPckg_Transition700
        self.CompleteDSLPckg_Transition703 = CompleteDSLPckg_Transition703
        self.CompleteDSLPckg_Transition = CompleteDSLPckg_Transition
        self.CompleteDSLPckg_Transition680 = CompleteDSLPckg_Transition680
        self.CompleteDSLPckg_Transition707 = CompleteDSLPckg_Transition707
        self.CompleteDSLPckg_Transition705 = CompleteDSLPckg_Transition705
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def CompleteDSLPckg_Transition703(self):
        return self.__CompleteDSLPckg_Transition703

    @CompleteDSLPckg_Transition703.setter
    def CompleteDSLPckg_Transition703(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition703", None)
        self.__CompleteDSLPckg_Transition703 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Region704"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Region704", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Region704", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Region704"):
                opp_val = getattr(value, "CompleteDSLPckg_Region704", None)
                setattr(value, "CompleteDSLPckg_Region704", self)

    @property
    def CompleteDSLPckg_Transition680(self):
        return self.__CompleteDSLPckg_Transition680

    @CompleteDSLPckg_Transition680.setter
    def CompleteDSLPckg_Transition680(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition680", None)
        self.__CompleteDSLPckg_Transition680 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Vertex679"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Vertex679", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Vertex679"):
                opp_val = getattr(value, "CompleteDSLPckg_Vertex679", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Vertex679", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Transition694(self):
        return self.__CompleteDSLPckg_Transition694

    @CompleteDSLPckg_Transition694.setter
    def CompleteDSLPckg_Transition694(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition694", None)
        self.__CompleteDSLPckg_Transition694 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Behavior695"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Behavior695", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Behavior695", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Behavior695"):
                opp_val = getattr(value, "CompleteDSLPckg_Behavior695", None)
                setattr(value, "CompleteDSLPckg_Behavior695", self)

    @property
    def CompleteDSLPckg_Transition683(self):
        return self.__CompleteDSLPckg_Transition683

    @CompleteDSLPckg_Transition683.setter
    def CompleteDSLPckg_Transition683(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition683", None)
        self.__CompleteDSLPckg_Transition683 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Vertex682"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Vertex682", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Vertex682"):
                opp_val = getattr(value, "CompleteDSLPckg_Vertex682", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Vertex682", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Transition700(self):
        return self.__CompleteDSLPckg_Transition700

    @CompleteDSLPckg_Transition700.setter
    def CompleteDSLPckg_Transition700(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition700", None)
        self.__CompleteDSLPckg_Transition700 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Constraint701"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Constraint701", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Constraint701", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Constraint701"):
                opp_val = getattr(value, "CompleteDSLPckg_Constraint701", None)
                setattr(value, "CompleteDSLPckg_Constraint701", self)

    @property
    def CompleteDSLPckg_Transition688(self):
        return self.__CompleteDSLPckg_Transition688

    @CompleteDSLPckg_Transition688.setter
    def CompleteDSLPckg_Transition688(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition688", None)
        self.__CompleteDSLPckg_Transition688 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Vertex689"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Vertex689", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Vertex689", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Vertex689"):
                opp_val = getattr(value, "CompleteDSLPckg_Vertex689", None)
                setattr(value, "CompleteDSLPckg_Vertex689", self)

    @property
    def CompleteDSLPckg_Transition707(self):
        return self.__CompleteDSLPckg_Transition707

    @CompleteDSLPckg_Transition707.setter
    def CompleteDSLPckg_Transition707(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition707", None)
        self.__CompleteDSLPckg_Transition707 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Transition705"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Transition705", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Transition705", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Transition705"):
                opp_val = getattr(value, "CompleteDSLPckg_Transition705", None)
                setattr(value, "CompleteDSLPckg_Transition705", self)

    @property
    def CompleteDSLPckg_Transition697(self):
        return self.__CompleteDSLPckg_Transition697

    @CompleteDSLPckg_Transition697.setter
    def CompleteDSLPckg_Transition697(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition697", None)
        self.__CompleteDSLPckg_Transition697 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Trigger698"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Trigger698", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Trigger698", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Trigger698"):
                opp_val = getattr(value, "CompleteDSLPckg_Trigger698", None)
                setattr(value, "CompleteDSLPckg_Trigger698", self)

    @property
    def CompleteDSLPckg_Transition(self):
        return self.__CompleteDSLPckg_Transition

    @CompleteDSLPckg_Transition.setter
    def CompleteDSLPckg_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition", None)
        self.__CompleteDSLPckg_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Region671"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Region671", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Region671"):
                opp_val = getattr(value, "CompleteDSLPckg_Region671", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Region671", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Transition691(self):
        return self.__CompleteDSLPckg_Transition691

    @CompleteDSLPckg_Transition691.setter
    def CompleteDSLPckg_Transition691(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition691", None)
        self.__CompleteDSLPckg_Transition691 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Vertex692"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Vertex692", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Vertex692", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Vertex692"):
                opp_val = getattr(value, "CompleteDSLPckg_Vertex692", None)
                setattr(value, "CompleteDSLPckg_Vertex692", self)

    @property
    def CompleteDSLPckg_Transition705(self):
        return self.__CompleteDSLPckg_Transition705

    @CompleteDSLPckg_Transition705.setter
    def CompleteDSLPckg_Transition705(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Transition__CompleteDSLPckg_Transition705", None)
        self.__CompleteDSLPckg_Transition705 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Transition707"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Transition707", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Transition707", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Transition707"):
                opp_val = getattr(value, "CompleteDSLPckg_Transition707", None)
                setattr(value, "CompleteDSLPckg_Transition707", self)

class CompleteDSLPckg_State(RedefinableElement, Vertex, Namespace):

    def __init__(self, isOrthogonal: bool, isSimple: bool, isSubmachineState: bool, isComposite: bool, CompleteDSLPckg_State: "CompleteDSLPckg_StateMachine" = None, CompleteDSLPckg_State674: "CompleteDSLPckg_Region" = None, CompleteDSLPckg_State720: set["CompleteDSLPckg_ConnectionPointReference"] = None, CompleteDSLPckg_State723: set["CompleteDSLPckg_Pseudostate"] = None, CompleteDSLPckg_State726: "CompleteDSLPckg_StateMachine" = None, CompleteDSLPckg_State729: set["CompleteDSLPckg_Region"] = None, CompleteDSLPckg_State732: set["CompleteDSLPckg_Trigger"] = None, CompleteDSLPckg_State735: "CompleteDSLPckg_Behavior" = None, CompleteDSLPckg_State738: "CompleteDSLPckg_Behavior" = None, CompleteDSLPckg_State741: "CompleteDSLPckg_Behavior" = None, CompleteDSLPckg_State710: "CompleteDSLPckg_Pseudostate" = None, CompleteDSLPckg_State718: "CompleteDSLPckg_ConnectionPointReference" = None, CompleteDSLPckg_State744: "CompleteDSLPckg_Constraint" = None, CompleteDSLPckg_State748: "CompleteDSLPckg_State" = None, CompleteDSLPckg_State746: "CompleteDSLPckg_State" = None, CompleteDSLPckg_State847: "CompleteDSLPckg_ObjectFlow" = None):
        self.isOrthogonal = isOrthogonal
        self.isSimple = isSimple
        self.isSubmachineState = isSubmachineState
        self.isComposite = isComposite
        self.CompleteDSLPckg_State = CompleteDSLPckg_State
        self.CompleteDSLPckg_State674 = CompleteDSLPckg_State674
        self.CompleteDSLPckg_State720 = CompleteDSLPckg_State720 if CompleteDSLPckg_State720 is not None else set()
        self.CompleteDSLPckg_State723 = CompleteDSLPckg_State723 if CompleteDSLPckg_State723 is not None else set()
        self.CompleteDSLPckg_State726 = CompleteDSLPckg_State726
        self.CompleteDSLPckg_State729 = CompleteDSLPckg_State729 if CompleteDSLPckg_State729 is not None else set()
        self.CompleteDSLPckg_State732 = CompleteDSLPckg_State732 if CompleteDSLPckg_State732 is not None else set()
        self.CompleteDSLPckg_State735 = CompleteDSLPckg_State735
        self.CompleteDSLPckg_State738 = CompleteDSLPckg_State738
        self.CompleteDSLPckg_State741 = CompleteDSLPckg_State741
        self.CompleteDSLPckg_State710 = CompleteDSLPckg_State710
        self.CompleteDSLPckg_State718 = CompleteDSLPckg_State718
        self.CompleteDSLPckg_State744 = CompleteDSLPckg_State744
        self.CompleteDSLPckg_State748 = CompleteDSLPckg_State748
        self.CompleteDSLPckg_State746 = CompleteDSLPckg_State746
        self.CompleteDSLPckg_State847 = CompleteDSLPckg_State847
        
    @property
    def isOrthogonal(self) -> bool:
        return self.__isOrthogonal

    @isOrthogonal.setter
    def isOrthogonal(self, isOrthogonal: bool):
        self.__isOrthogonal = isOrthogonal

    @property
    def isSubmachineState(self) -> bool:
        return self.__isSubmachineState

    @isSubmachineState.setter
    def isSubmachineState(self, isSubmachineState: bool):
        self.__isSubmachineState = isSubmachineState

    @property
    def isSimple(self) -> bool:
        return self.__isSimple

    @isSimple.setter
    def isSimple(self, isSimple: bool):
        self.__isSimple = isSimple

    @property
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

    @property
    def CompleteDSLPckg_State726(self):
        return self.__CompleteDSLPckg_State726

    @CompleteDSLPckg_State726.setter
    def CompleteDSLPckg_State726(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State726", None)
        self.__CompleteDSLPckg_State726 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_StateMachine727"):
                opp_val = getattr(old_value, "CompleteDSLPckg_StateMachine727", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_StateMachine727", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_StateMachine727"):
                opp_val = getattr(value, "CompleteDSLPckg_StateMachine727", None)
                setattr(value, "CompleteDSLPckg_StateMachine727", self)

    @property
    def CompleteDSLPckg_State718(self):
        return self.__CompleteDSLPckg_State718

    @CompleteDSLPckg_State718.setter
    def CompleteDSLPckg_State718(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State718", None)
        self.__CompleteDSLPckg_State718 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ConnectionPointReference717"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ConnectionPointReference717", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ConnectionPointReference717", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ConnectionPointReference717"):
                opp_val = getattr(value, "CompleteDSLPckg_ConnectionPointReference717", None)
                setattr(value, "CompleteDSLPckg_ConnectionPointReference717", self)

    @property
    def CompleteDSLPckg_State732(self):
        return self.__CompleteDSLPckg_State732

    @CompleteDSLPckg_State732.setter
    def CompleteDSLPckg_State732(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State732", None)
        self.__CompleteDSLPckg_State732 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Trigger733"):
                    opp_val = getattr(item, "CompleteDSLPckg_Trigger733", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Trigger733", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Trigger733"):
                    opp_val = getattr(item, "CompleteDSLPckg_Trigger733", None)
                    
                    setattr(item, "CompleteDSLPckg_Trigger733", self)
                    

    @property
    def CompleteDSLPckg_State746(self):
        return self.__CompleteDSLPckg_State746

    @CompleteDSLPckg_State746.setter
    def CompleteDSLPckg_State746(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State746", None)
        self.__CompleteDSLPckg_State746 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_State748"):
                opp_val = getattr(old_value, "CompleteDSLPckg_State748", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_State748", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_State748"):
                opp_val = getattr(value, "CompleteDSLPckg_State748", None)
                setattr(value, "CompleteDSLPckg_State748", self)

    @property
    def CompleteDSLPckg_State741(self):
        return self.__CompleteDSLPckg_State741

    @CompleteDSLPckg_State741.setter
    def CompleteDSLPckg_State741(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State741", None)
        self.__CompleteDSLPckg_State741 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Behavior742"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Behavior742", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Behavior742", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Behavior742"):
                opp_val = getattr(value, "CompleteDSLPckg_Behavior742", None)
                setattr(value, "CompleteDSLPckg_Behavior742", self)

    @property
    def CompleteDSLPckg_State710(self):
        return self.__CompleteDSLPckg_State710

    @CompleteDSLPckg_State710.setter
    def CompleteDSLPckg_State710(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State710", None)
        self.__CompleteDSLPckg_State710 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Pseudostate709"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Pseudostate709", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Pseudostate709", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Pseudostate709"):
                opp_val = getattr(value, "CompleteDSLPckg_Pseudostate709", None)
                setattr(value, "CompleteDSLPckg_Pseudostate709", self)

    @property
    def CompleteDSLPckg_State847(self):
        return self.__CompleteDSLPckg_State847

    @CompleteDSLPckg_State847.setter
    def CompleteDSLPckg_State847(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State847", None)
        self.__CompleteDSLPckg_State847 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ObjectFlow846"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ObjectFlow846", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ObjectFlow846"):
                opp_val = getattr(value, "CompleteDSLPckg_ObjectFlow846", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_ObjectFlow846", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_State744(self):
        return self.__CompleteDSLPckg_State744

    @CompleteDSLPckg_State744.setter
    def CompleteDSLPckg_State744(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State744", None)
        self.__CompleteDSLPckg_State744 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Constraint745"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Constraint745", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Constraint745", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Constraint745"):
                opp_val = getattr(value, "CompleteDSLPckg_Constraint745", None)
                setattr(value, "CompleteDSLPckg_Constraint745", self)

    @property
    def CompleteDSLPckg_State720(self):
        return self.__CompleteDSLPckg_State720

    @CompleteDSLPckg_State720.setter
    def CompleteDSLPckg_State720(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State720", None)
        self.__CompleteDSLPckg_State720 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ConnectionPointReference721"):
                    opp_val = getattr(item, "CompleteDSLPckg_ConnectionPointReference721", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ConnectionPointReference721", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ConnectionPointReference721"):
                    opp_val = getattr(item, "CompleteDSLPckg_ConnectionPointReference721", None)
                    
                    setattr(item, "CompleteDSLPckg_ConnectionPointReference721", self)
                    

    @property
    def CompleteDSLPckg_State723(self):
        return self.__CompleteDSLPckg_State723

    @CompleteDSLPckg_State723.setter
    def CompleteDSLPckg_State723(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State723", None)
        self.__CompleteDSLPckg_State723 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Pseudostate724"):
                    opp_val = getattr(item, "CompleteDSLPckg_Pseudostate724", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Pseudostate724", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Pseudostate724"):
                    opp_val = getattr(item, "CompleteDSLPckg_Pseudostate724", None)
                    
                    setattr(item, "CompleteDSLPckg_Pseudostate724", self)
                    

    @property
    def CompleteDSLPckg_State674(self):
        return self.__CompleteDSLPckg_State674

    @CompleteDSLPckg_State674.setter
    def CompleteDSLPckg_State674(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State674", None)
        self.__CompleteDSLPckg_State674 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Region673"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Region673", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Region673", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Region673"):
                opp_val = getattr(value, "CompleteDSLPckg_Region673", None)
                setattr(value, "CompleteDSLPckg_Region673", self)

    @property
    def CompleteDSLPckg_State735(self):
        return self.__CompleteDSLPckg_State735

    @CompleteDSLPckg_State735.setter
    def CompleteDSLPckg_State735(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State735", None)
        self.__CompleteDSLPckg_State735 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Behavior736"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Behavior736", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Behavior736", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Behavior736"):
                opp_val = getattr(value, "CompleteDSLPckg_Behavior736", None)
                setattr(value, "CompleteDSLPckg_Behavior736", self)

    @property
    def CompleteDSLPckg_State729(self):
        return self.__CompleteDSLPckg_State729

    @CompleteDSLPckg_State729.setter
    def CompleteDSLPckg_State729(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State729", None)
        self.__CompleteDSLPckg_State729 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Region730"):
                    opp_val = getattr(item, "CompleteDSLPckg_Region730", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Region730", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Region730"):
                    opp_val = getattr(item, "CompleteDSLPckg_Region730", None)
                    
                    setattr(item, "CompleteDSLPckg_Region730", self)
                    

    @property
    def CompleteDSLPckg_State748(self):
        return self.__CompleteDSLPckg_State748

    @CompleteDSLPckg_State748.setter
    def CompleteDSLPckg_State748(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State748", None)
        self.__CompleteDSLPckg_State748 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_State746"):
                opp_val = getattr(old_value, "CompleteDSLPckg_State746", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_State746", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_State746"):
                opp_val = getattr(value, "CompleteDSLPckg_State746", None)
                setattr(value, "CompleteDSLPckg_State746", self)

    @property
    def CompleteDSLPckg_State738(self):
        return self.__CompleteDSLPckg_State738

    @CompleteDSLPckg_State738.setter
    def CompleteDSLPckg_State738(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State738", None)
        self.__CompleteDSLPckg_State738 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Behavior739"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Behavior739", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Behavior739", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Behavior739"):
                opp_val = getattr(value, "CompleteDSLPckg_Behavior739", None)
                setattr(value, "CompleteDSLPckg_Behavior739", self)

    @property
    def CompleteDSLPckg_State(self):
        return self.__CompleteDSLPckg_State

    @CompleteDSLPckg_State.setter
    def CompleteDSLPckg_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_State__CompleteDSLPckg_State", None)
        self.__CompleteDSLPckg_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_StateMachine661"):
                opp_val = getattr(old_value, "CompleteDSLPckg_StateMachine661", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_StateMachine661"):
                opp_val = getattr(value, "CompleteDSLPckg_StateMachine661", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_StateMachine661", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CompleteDSLPckg_Region(RedefinableElement, Namespace):

    pass
class CompleteDSLPckg_BehavioralFeature(Feature, Namespace):

    pass
class CompleteDSLPckg_InteractionOperand(Namespace):

    pass
class CompleteDSLPckg_Classifier(RedefinableElement, Type, Namespace):

    def __init__(self, isAbstract: bool, isFinalSpecialization: bool, CompleteDSLPckg_Classifier: "CompleteDSLPckg_InstanceSpecification" = None, CompleteDSLPckg_Classifier127: set["CompleteDSLPckg_NamedElement"] = None, 130: set["CompleteDSLPckg_Feature"] = None, CompleteDSLPckg_Classifier133: set["CompleteDSLPckg_Property"] = None, CompleteDSLPckg_Classifier136: "CompleteDSLPckg_Classifier" = None, CompleteDSLPckg_Classifier134: set["CompleteDSLPckg_Classifier"] = None, CompleteDSLPckg_Classifier139: "CompleteDSLPckg_Classifier" = None, CompleteDSLPckg_Classifier137: set["CompleteDSLPckg_Classifier"] = None, 141: set["CompleteDSLPckg_Generalization"] = None, 144: set["CompleteDSLPckg_Substitution"] = None, 147: set["CompleteDSLPckg_GeneralizationSet"] = None, CompleteDSLPckg_Classifier125: "CompleteDSLPckg_RedefinableElement" = None, CompleteDSLPckg_Classifier150: set["CompleteDSLPckg_CollaborationUse"] = None, CompleteDSLPckg_Classifier152: "CompleteDSLPckg_CollaborationUse" = None, 156: "CompleteDSLPckg_Feature" = None, CompleteDSLPckg_Classifier193: "CompleteDSLPckg_Generalization" = None, 196: "CompleteDSLPckg_Generalization" = None, CompleteDSLPckg_Classifier232: "CompleteDSLPckg_Class" = None, 278: "CompleteDSLPckg_Substitution" = None, CompleteDSLPckg_Classifier280: "CompleteDSLPckg_Substitution" = None, CompleteDSLPckg_Classifier282: "CompleteDSLPckg_Interface" = None, 310: "CompleteDSLPckg_GeneralizationSet" = None, CompleteDSLPckg_Classifier393: "CompleteDSLPckg_ComponentRealization" = None, CompleteDSLPckg_Classifier476: "CompleteDSLPckg_Action" = None, CompleteDSLPckg_Classifier510: "CompleteDSLPckg_CreateObjectAction" = None, CompleteDSLPckg_Classifier579: "CompleteDSLPckg_UnmarshallAction" = None, CompleteDSLPckg_Classifier599: "CompleteDSLPckg_ReclassifyObjectAction" = None, CompleteDSLPckg_Classifier602: "CompleteDSLPckg_ReclassifyObjectAction" = None, CompleteDSLPckg_Classifier594: "CompleteDSLPckg_ReadExtendAction" = None, CompleteDSLPckg_Classifier954: "CompleteDSLPckg_ExceptionHandler" = None, CompleteDSLPckg_Classifier1067: "CompleteDSLPckg_UseCase" = None):
        self.isAbstract = isAbstract
        self.isFinalSpecialization = isFinalSpecialization
        self.CompleteDSLPckg_Classifier = CompleteDSLPckg_Classifier
        self.CompleteDSLPckg_Classifier127 = CompleteDSLPckg_Classifier127 if CompleteDSLPckg_Classifier127 is not None else set()
        self.130 = 130 if 130 is not None else set()
        self.CompleteDSLPckg_Classifier133 = CompleteDSLPckg_Classifier133 if CompleteDSLPckg_Classifier133 is not None else set()
        self.CompleteDSLPckg_Classifier136 = CompleteDSLPckg_Classifier136
        self.CompleteDSLPckg_Classifier134 = CompleteDSLPckg_Classifier134 if CompleteDSLPckg_Classifier134 is not None else set()
        self.CompleteDSLPckg_Classifier139 = CompleteDSLPckg_Classifier139
        self.CompleteDSLPckg_Classifier137 = CompleteDSLPckg_Classifier137 if CompleteDSLPckg_Classifier137 is not None else set()
        self.141 = 141 if 141 is not None else set()
        self.144 = 144 if 144 is not None else set()
        self.147 = 147 if 147 is not None else set()
        self.CompleteDSLPckg_Classifier125 = CompleteDSLPckg_Classifier125
        self.CompleteDSLPckg_Classifier150 = CompleteDSLPckg_Classifier150 if CompleteDSLPckg_Classifier150 is not None else set()
        self.CompleteDSLPckg_Classifier152 = CompleteDSLPckg_Classifier152
        self.156 = 156
        self.CompleteDSLPckg_Classifier193 = CompleteDSLPckg_Classifier193
        self.196 = 196
        self.CompleteDSLPckg_Classifier232 = CompleteDSLPckg_Classifier232
        self.278 = 278
        self.CompleteDSLPckg_Classifier280 = CompleteDSLPckg_Classifier280
        self.CompleteDSLPckg_Classifier282 = CompleteDSLPckg_Classifier282
        self.310 = 310
        self.CompleteDSLPckg_Classifier393 = CompleteDSLPckg_Classifier393
        self.CompleteDSLPckg_Classifier476 = CompleteDSLPckg_Classifier476
        self.CompleteDSLPckg_Classifier510 = CompleteDSLPckg_Classifier510
        self.CompleteDSLPckg_Classifier579 = CompleteDSLPckg_Classifier579
        self.CompleteDSLPckg_Classifier599 = CompleteDSLPckg_Classifier599
        self.CompleteDSLPckg_Classifier602 = CompleteDSLPckg_Classifier602
        self.CompleteDSLPckg_Classifier594 = CompleteDSLPckg_Classifier594
        self.CompleteDSLPckg_Classifier954 = CompleteDSLPckg_Classifier954
        self.CompleteDSLPckg_Classifier1067 = CompleteDSLPckg_Classifier1067
        
    @property
    def isFinalSpecialization(self) -> bool:
        return self.__isFinalSpecialization

    @isFinalSpecialization.setter
    def isFinalSpecialization(self, isFinalSpecialization: bool):
        self.__isFinalSpecialization = isFinalSpecialization

    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def CompleteDSLPckg_Classifier134(self):
        return self.__CompleteDSLPckg_Classifier134

    @CompleteDSLPckg_Classifier134.setter
    def CompleteDSLPckg_Classifier134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier134", None)
        self.__CompleteDSLPckg_Classifier134 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Classifier136"):
                    opp_val = getattr(item, "CompleteDSLPckg_Classifier136", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Classifier136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Classifier136"):
                    opp_val = getattr(item, "CompleteDSLPckg_Classifier136", None)
                    
                    setattr(item, "CompleteDSLPckg_Classifier136", self)
                    

    @property
    def CompleteDSLPckg_Classifier594(self):
        return self.__CompleteDSLPckg_Classifier594

    @CompleteDSLPckg_Classifier594.setter
    def CompleteDSLPckg_Classifier594(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier594", None)
        self.__CompleteDSLPckg_Classifier594 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ReadExtendAction593"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ReadExtendAction593", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ReadExtendAction593", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ReadExtendAction593"):
                opp_val = getattr(value, "CompleteDSLPckg_ReadExtendAction593", None)
                setattr(value, "CompleteDSLPckg_ReadExtendAction593", self)

    @property
    def CompleteDSLPckg_Classifier599(self):
        return self.__CompleteDSLPckg_Classifier599

    @CompleteDSLPckg_Classifier599.setter
    def CompleteDSLPckg_Classifier599(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier599", None)
        self.__CompleteDSLPckg_Classifier599 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ReclassifyObjectAction598"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ReclassifyObjectAction598", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ReclassifyObjectAction598"):
                opp_val = getattr(value, "CompleteDSLPckg_ReclassifyObjectAction598", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_ReclassifyObjectAction598", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 310(self):
        return self.__310

    @310.setter
    def 310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__310", None)
        self.__310 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "309"):
                opp_val = getattr(old_value, "309", None)
                if opp_val == self:
                    setattr(old_value, "309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "309"):
                opp_val = getattr(value, "309", None)
                setattr(value, "309", self)

    @property
    def CompleteDSLPckg_Classifier1067(self):
        return self.__CompleteDSLPckg_Classifier1067

    @CompleteDSLPckg_Classifier1067.setter
    def CompleteDSLPckg_Classifier1067(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier1067", None)
        self.__CompleteDSLPckg_Classifier1067 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_UseCase"):
                opp_val = getattr(old_value, "CompleteDSLPckg_UseCase", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_UseCase"):
                opp_val = getattr(value, "CompleteDSLPckg_UseCase", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_UseCase", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Classifier136(self):
        return self.__CompleteDSLPckg_Classifier136

    @CompleteDSLPckg_Classifier136.setter
    def CompleteDSLPckg_Classifier136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier136", None)
        self.__CompleteDSLPckg_Classifier136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Classifier134"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Classifier134", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Classifier134"):
                opp_val = getattr(value, "CompleteDSLPckg_Classifier134", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Classifier134", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Classifier954(self):
        return self.__CompleteDSLPckg_Classifier954

    @CompleteDSLPckg_Classifier954.setter
    def CompleteDSLPckg_Classifier954(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier954", None)
        self.__CompleteDSLPckg_Classifier954 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ExceptionHandler953"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ExceptionHandler953", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ExceptionHandler953"):
                opp_val = getattr(value, "CompleteDSLPckg_ExceptionHandler953", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_ExceptionHandler953", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 156(self):
        return self.__156

    @156.setter
    def 156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__156", None)
        self.__156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "155"):
                opp_val = getattr(old_value, "155", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "155"):
                opp_val = getattr(value, "155", None)
                if opp_val is None:
                    setattr(value, "155", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Classifier150(self):
        return self.__CompleteDSLPckg_Classifier150

    @CompleteDSLPckg_Classifier150.setter
    def CompleteDSLPckg_Classifier150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier150", None)
        self.__CompleteDSLPckg_Classifier150 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_CollaborationUse"):
                    opp_val = getattr(item, "CompleteDSLPckg_CollaborationUse", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_CollaborationUse", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_CollaborationUse"):
                    opp_val = getattr(item, "CompleteDSLPckg_CollaborationUse", None)
                    
                    setattr(item, "CompleteDSLPckg_CollaborationUse", self)
                    

    @property
    def CompleteDSLPckg_Classifier393(self):
        return self.__CompleteDSLPckg_Classifier393

    @CompleteDSLPckg_Classifier393.setter
    def CompleteDSLPckg_Classifier393(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier393", None)
        self.__CompleteDSLPckg_Classifier393 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ComponentRealization392"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ComponentRealization392", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ComponentRealization392"):
                opp_val = getattr(value, "CompleteDSLPckg_ComponentRealization392", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_ComponentRealization392", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Classifier(self):
        return self.__CompleteDSLPckg_Classifier

    @CompleteDSLPckg_Classifier.setter
    def CompleteDSLPckg_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier", None)
        self.__CompleteDSLPckg_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_InstanceSpecification105"):
                opp_val = getattr(old_value, "CompleteDSLPckg_InstanceSpecification105", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_InstanceSpecification105"):
                opp_val = getattr(value, "CompleteDSLPckg_InstanceSpecification105", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_InstanceSpecification105", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Classifier193(self):
        return self.__CompleteDSLPckg_Classifier193

    @CompleteDSLPckg_Classifier193.setter
    def CompleteDSLPckg_Classifier193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier193", None)
        self.__CompleteDSLPckg_Classifier193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Generalization"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Generalization", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Generalization"):
                opp_val = getattr(value, "CompleteDSLPckg_Generalization", None)
                setattr(value, "CompleteDSLPckg_Generalization", self)

    @property
    def CompleteDSLPckg_Classifier137(self):
        return self.__CompleteDSLPckg_Classifier137

    @CompleteDSLPckg_Classifier137.setter
    def CompleteDSLPckg_Classifier137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier137", None)
        self.__CompleteDSLPckg_Classifier137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Classifier139"):
                    opp_val = getattr(item, "CompleteDSLPckg_Classifier139", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Classifier139", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Classifier139"):
                    opp_val = getattr(item, "CompleteDSLPckg_Classifier139", None)
                    
                    setattr(item, "CompleteDSLPckg_Classifier139", self)
                    

    @property
    def CompleteDSLPckg_Classifier280(self):
        return self.__CompleteDSLPckg_Classifier280

    @CompleteDSLPckg_Classifier280.setter
    def CompleteDSLPckg_Classifier280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier280", None)
        self.__CompleteDSLPckg_Classifier280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Substitution"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Substitution", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Substitution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Substitution"):
                opp_val = getattr(value, "CompleteDSLPckg_Substitution", None)
                setattr(value, "CompleteDSLPckg_Substitution", self)

    @property
    def CompleteDSLPckg_Classifier232(self):
        return self.__CompleteDSLPckg_Classifier232

    @CompleteDSLPckg_Classifier232.setter
    def CompleteDSLPckg_Classifier232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier232", None)
        self.__CompleteDSLPckg_Classifier232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Class"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Class"):
                opp_val = getattr(value, "CompleteDSLPckg_Class", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Classifier127(self):
        return self.__CompleteDSLPckg_Classifier127

    @CompleteDSLPckg_Classifier127.setter
    def CompleteDSLPckg_Classifier127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier127", None)
        self.__CompleteDSLPckg_Classifier127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_NamedElement128"):
                    opp_val = getattr(item, "CompleteDSLPckg_NamedElement128", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_NamedElement128", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_NamedElement128"):
                    opp_val = getattr(item, "CompleteDSLPckg_NamedElement128", None)
                    
                    setattr(item, "CompleteDSLPckg_NamedElement128", self)
                    

    @property
    def CompleteDSLPckg_Classifier579(self):
        return self.__CompleteDSLPckg_Classifier579

    @CompleteDSLPckg_Classifier579.setter
    def CompleteDSLPckg_Classifier579(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier579", None)
        self.__CompleteDSLPckg_Classifier579 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_UnmarshallAction578"):
                opp_val = getattr(old_value, "CompleteDSLPckg_UnmarshallAction578", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_UnmarshallAction578", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_UnmarshallAction578"):
                opp_val = getattr(value, "CompleteDSLPckg_UnmarshallAction578", None)
                setattr(value, "CompleteDSLPckg_UnmarshallAction578", self)

    @property
    def CompleteDSLPckg_Classifier139(self):
        return self.__CompleteDSLPckg_Classifier139

    @CompleteDSLPckg_Classifier139.setter
    def CompleteDSLPckg_Classifier139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier139", None)
        self.__CompleteDSLPckg_Classifier139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Classifier137"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Classifier137", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Classifier137"):
                opp_val = getattr(value, "CompleteDSLPckg_Classifier137", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Classifier137", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 147(self):
        return self.__147

    @147.setter
    def 147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__147", None)
        self.__147 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "148"):
                    opp_val = getattr(item, "148", None)
                    
                    if opp_val == self:
                        setattr(item, "148", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "148"):
                    opp_val = getattr(item, "148", None)
                    
                    setattr(item, "148", self)
                    

    @property
    def 278(self):
        return self.__278

    @278.setter
    def 278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__278", None)
        self.__278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "277"):
                opp_val = getattr(old_value, "277", None)
                if opp_val == self:
                    setattr(old_value, "277", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "277"):
                opp_val = getattr(value, "277", None)
                setattr(value, "277", self)

    @property
    def 141(self):
        return self.__141

    @141.setter
    def 141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__141", None)
        self.__141 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "142"):
                    opp_val = getattr(item, "142", None)
                    
                    if opp_val == self:
                        setattr(item, "142", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "142"):
                    opp_val = getattr(item, "142", None)
                    
                    setattr(item, "142", self)
                    

    @property
    def 130(self):
        return self.__130

    @130.setter
    def 130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__130", None)
        self.__130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "131"):
                    opp_val = getattr(item, "131", None)
                    
                    if opp_val == self:
                        setattr(item, "131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "131"):
                    opp_val = getattr(item, "131", None)
                    
                    setattr(item, "131", self)
                    

    @property
    def CompleteDSLPckg_Classifier510(self):
        return self.__CompleteDSLPckg_Classifier510

    @CompleteDSLPckg_Classifier510.setter
    def CompleteDSLPckg_Classifier510(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier510", None)
        self.__CompleteDSLPckg_Classifier510 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_CreateObjectAction"):
                opp_val = getattr(old_value, "CompleteDSLPckg_CreateObjectAction", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_CreateObjectAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_CreateObjectAction"):
                opp_val = getattr(value, "CompleteDSLPckg_CreateObjectAction", None)
                setattr(value, "CompleteDSLPckg_CreateObjectAction", self)

    @property
    def CompleteDSLPckg_Classifier602(self):
        return self.__CompleteDSLPckg_Classifier602

    @CompleteDSLPckg_Classifier602.setter
    def CompleteDSLPckg_Classifier602(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier602", None)
        self.__CompleteDSLPckg_Classifier602 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ReclassifyObjectAction601"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ReclassifyObjectAction601", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ReclassifyObjectAction601"):
                opp_val = getattr(value, "CompleteDSLPckg_ReclassifyObjectAction601", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_ReclassifyObjectAction601", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 196(self):
        return self.__196

    @196.setter
    def 196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__196", None)
        self.__196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "195"):
                opp_val = getattr(old_value, "195", None)
                if opp_val == self:
                    setattr(old_value, "195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "195"):
                opp_val = getattr(value, "195", None)
                setattr(value, "195", self)

    @property
    def CompleteDSLPckg_Classifier125(self):
        return self.__CompleteDSLPckg_Classifier125

    @CompleteDSLPckg_Classifier125.setter
    def CompleteDSLPckg_Classifier125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier125", None)
        self.__CompleteDSLPckg_Classifier125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_RedefinableElement124"):
                opp_val = getattr(old_value, "CompleteDSLPckg_RedefinableElement124", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_RedefinableElement124"):
                opp_val = getattr(value, "CompleteDSLPckg_RedefinableElement124", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_RedefinableElement124", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_Classifier282(self):
        return self.__CompleteDSLPckg_Classifier282

    @CompleteDSLPckg_Classifier282.setter
    def CompleteDSLPckg_Classifier282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier282", None)
        self.__CompleteDSLPckg_Classifier282 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Interface"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Interface", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Interface", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Interface"):
                opp_val = getattr(value, "CompleteDSLPckg_Interface", None)
                setattr(value, "CompleteDSLPckg_Interface", self)

    @property
    def CompleteDSLPckg_Classifier476(self):
        return self.__CompleteDSLPckg_Classifier476

    @CompleteDSLPckg_Classifier476.setter
    def CompleteDSLPckg_Classifier476(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier476", None)
        self.__CompleteDSLPckg_Classifier476 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Action"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Action", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Action"):
                opp_val = getattr(value, "CompleteDSLPckg_Action", None)
                setattr(value, "CompleteDSLPckg_Action", self)

    @property
    def CompleteDSLPckg_Classifier133(self):
        return self.__CompleteDSLPckg_Classifier133

    @CompleteDSLPckg_Classifier133.setter
    def CompleteDSLPckg_Classifier133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier133", None)
        self.__CompleteDSLPckg_Classifier133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Property"):
                    opp_val = getattr(item, "CompleteDSLPckg_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Property"):
                    opp_val = getattr(item, "CompleteDSLPckg_Property", None)
                    
                    setattr(item, "CompleteDSLPckg_Property", self)
                    

    @property
    def 144(self):
        return self.__144

    @144.setter
    def 144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__144", None)
        self.__144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "145"):
                    opp_val = getattr(item, "145", None)
                    
                    if opp_val == self:
                        setattr(item, "145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "145"):
                    opp_val = getattr(item, "145", None)
                    
                    setattr(item, "145", self)
                    

    @property
    def CompleteDSLPckg_Classifier152(self):
        return self.__CompleteDSLPckg_Classifier152

    @CompleteDSLPckg_Classifier152.setter
    def CompleteDSLPckg_Classifier152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Classifier__CompleteDSLPckg_Classifier152", None)
        self.__CompleteDSLPckg_Classifier152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_CollaborationUse153"):
                opp_val = getattr(old_value, "CompleteDSLPckg_CollaborationUse153", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_CollaborationUse153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_CollaborationUse153"):
                opp_val = getattr(value, "CompleteDSLPckg_CollaborationUse153", None)
                setattr(value, "CompleteDSLPckg_CollaborationUse153", self)

class CompleteDSLPckg_StructuredActivityNode(Action, ActivityGroup, ExecutableNode, Namespace):

    def __init__(self, mustIsolate: bool, CompleteDSLPckg_StructuredActivityNode795: "CompleteDSLPckg_ActivityNode" = None, CompleteDSLPckg_StructuredActivityNode: "CompleteDSLPckg_Activity" = None, CompleteDSLPckg_StructuredActivityNode839: "CompleteDSLPckg_ActivityEdge" = None, CompleteDSLPckg_StructuredActivityNode882: "CompleteDSLPckg_Activity" = None, CompleteDSLPckg_StructuredActivityNode885: set["CompleteDSLPckg_Variable"] = None, CompleteDSLPckg_StructuredActivityNode888: set["CompleteDSLPckg_ActivityNode"] = None, CompleteDSLPckg_StructuredActivityNode891: set["CompleteDSLPckg_InputPin"] = None, CompleteDSLPckg_StructuredActivityNode894: set["CompleteDSLPckg_ActivityEdge"] = None, CompleteDSLPckg_StructuredActivityNode897: set["CompleteDSLPckg_OutputPin"] = None):
        self.mustIsolate = mustIsolate
        self.CompleteDSLPckg_StructuredActivityNode795 = CompleteDSLPckg_StructuredActivityNode795
        self.CompleteDSLPckg_StructuredActivityNode = CompleteDSLPckg_StructuredActivityNode
        self.CompleteDSLPckg_StructuredActivityNode839 = CompleteDSLPckg_StructuredActivityNode839
        self.CompleteDSLPckg_StructuredActivityNode882 = CompleteDSLPckg_StructuredActivityNode882
        self.CompleteDSLPckg_StructuredActivityNode885 = CompleteDSLPckg_StructuredActivityNode885 if CompleteDSLPckg_StructuredActivityNode885 is not None else set()
        self.CompleteDSLPckg_StructuredActivityNode888 = CompleteDSLPckg_StructuredActivityNode888 if CompleteDSLPckg_StructuredActivityNode888 is not None else set()
        self.CompleteDSLPckg_StructuredActivityNode891 = CompleteDSLPckg_StructuredActivityNode891 if CompleteDSLPckg_StructuredActivityNode891 is not None else set()
        self.CompleteDSLPckg_StructuredActivityNode894 = CompleteDSLPckg_StructuredActivityNode894 if CompleteDSLPckg_StructuredActivityNode894 is not None else set()
        self.CompleteDSLPckg_StructuredActivityNode897 = CompleteDSLPckg_StructuredActivityNode897 if CompleteDSLPckg_StructuredActivityNode897 is not None else set()
        
    @property
    def mustIsolate(self) -> bool:
        return self.__mustIsolate

    @mustIsolate.setter
    def mustIsolate(self, mustIsolate: bool):
        self.__mustIsolate = mustIsolate

    @property
    def CompleteDSLPckg_StructuredActivityNode888(self):
        return self.__CompleteDSLPckg_StructuredActivityNode888

    @CompleteDSLPckg_StructuredActivityNode888.setter
    def CompleteDSLPckg_StructuredActivityNode888(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuredActivityNode__CompleteDSLPckg_StructuredActivityNode888", None)
        self.__CompleteDSLPckg_StructuredActivityNode888 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ActivityNode889"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityNode889", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ActivityNode889", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ActivityNode889"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityNode889", None)
                    
                    setattr(item, "CompleteDSLPckg_ActivityNode889", self)
                    

    @property
    def CompleteDSLPckg_StructuredActivityNode885(self):
        return self.__CompleteDSLPckg_StructuredActivityNode885

    @CompleteDSLPckg_StructuredActivityNode885.setter
    def CompleteDSLPckg_StructuredActivityNode885(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuredActivityNode__CompleteDSLPckg_StructuredActivityNode885", None)
        self.__CompleteDSLPckg_StructuredActivityNode885 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Variable886"):
                    opp_val = getattr(item, "CompleteDSLPckg_Variable886", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Variable886", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Variable886"):
                    opp_val = getattr(item, "CompleteDSLPckg_Variable886", None)
                    
                    setattr(item, "CompleteDSLPckg_Variable886", self)
                    

    @property
    def CompleteDSLPckg_StructuredActivityNode894(self):
        return self.__CompleteDSLPckg_StructuredActivityNode894

    @CompleteDSLPckg_StructuredActivityNode894.setter
    def CompleteDSLPckg_StructuredActivityNode894(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuredActivityNode__CompleteDSLPckg_StructuredActivityNode894", None)
        self.__CompleteDSLPckg_StructuredActivityNode894 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_ActivityEdge895"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityEdge895", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_ActivityEdge895", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_ActivityEdge895"):
                    opp_val = getattr(item, "CompleteDSLPckg_ActivityEdge895", None)
                    
                    setattr(item, "CompleteDSLPckg_ActivityEdge895", self)
                    

    @property
    def CompleteDSLPckg_StructuredActivityNode882(self):
        return self.__CompleteDSLPckg_StructuredActivityNode882

    @CompleteDSLPckg_StructuredActivityNode882.setter
    def CompleteDSLPckg_StructuredActivityNode882(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuredActivityNode__CompleteDSLPckg_StructuredActivityNode882", None)
        self.__CompleteDSLPckg_StructuredActivityNode882 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Activity883"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Activity883", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Activity883", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Activity883"):
                opp_val = getattr(value, "CompleteDSLPckg_Activity883", None)
                setattr(value, "CompleteDSLPckg_Activity883", self)

    @property
    def CompleteDSLPckg_StructuredActivityNode795(self):
        return self.__CompleteDSLPckg_StructuredActivityNode795

    @CompleteDSLPckg_StructuredActivityNode795.setter
    def CompleteDSLPckg_StructuredActivityNode795(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuredActivityNode__CompleteDSLPckg_StructuredActivityNode795", None)
        self.__CompleteDSLPckg_StructuredActivityNode795 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ActivityNode794"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ActivityNode794", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ActivityNode794", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ActivityNode794"):
                opp_val = getattr(value, "CompleteDSLPckg_ActivityNode794", None)
                setattr(value, "CompleteDSLPckg_ActivityNode794", self)

    @property
    def CompleteDSLPckg_StructuredActivityNode(self):
        return self.__CompleteDSLPckg_StructuredActivityNode

    @CompleteDSLPckg_StructuredActivityNode.setter
    def CompleteDSLPckg_StructuredActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuredActivityNode__CompleteDSLPckg_StructuredActivityNode", None)
        self.__CompleteDSLPckg_StructuredActivityNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Activity772"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Activity772", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Activity772"):
                opp_val = getattr(value, "CompleteDSLPckg_Activity772", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Activity772", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_StructuredActivityNode839(self):
        return self.__CompleteDSLPckg_StructuredActivityNode839

    @CompleteDSLPckg_StructuredActivityNode839.setter
    def CompleteDSLPckg_StructuredActivityNode839(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuredActivityNode__CompleteDSLPckg_StructuredActivityNode839", None)
        self.__CompleteDSLPckg_StructuredActivityNode839 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ActivityEdge838"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ActivityEdge838", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_ActivityEdge838", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ActivityEdge838"):
                opp_val = getattr(value, "CompleteDSLPckg_ActivityEdge838", None)
                setattr(value, "CompleteDSLPckg_ActivityEdge838", self)

    @property
    def CompleteDSLPckg_StructuredActivityNode891(self):
        return self.__CompleteDSLPckg_StructuredActivityNode891

    @CompleteDSLPckg_StructuredActivityNode891.setter
    def CompleteDSLPckg_StructuredActivityNode891(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuredActivityNode__CompleteDSLPckg_StructuredActivityNode891", None)
        self.__CompleteDSLPckg_StructuredActivityNode891 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_InputPin892"):
                    opp_val = getattr(item, "CompleteDSLPckg_InputPin892", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_InputPin892", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_InputPin892"):
                    opp_val = getattr(item, "CompleteDSLPckg_InputPin892", None)
                    
                    setattr(item, "CompleteDSLPckg_InputPin892", self)
                    

    @property
    def CompleteDSLPckg_StructuredActivityNode897(self):
        return self.__CompleteDSLPckg_StructuredActivityNode897

    @CompleteDSLPckg_StructuredActivityNode897.setter
    def CompleteDSLPckg_StructuredActivityNode897(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_StructuredActivityNode__CompleteDSLPckg_StructuredActivityNode897", None)
        self.__CompleteDSLPckg_StructuredActivityNode897 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_OutputPin898"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin898", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_OutputPin898", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_OutputPin898"):
                    opp_val = getattr(item, "CompleteDSLPckg_OutputPin898", None)
                    
                    setattr(item, "CompleteDSLPckg_OutputPin898", self)
                    

class CompleteDSLPckg_Package(PackageableElement, Namespace):

    def __init__(self, URI: str, CompleteDSLPckg_Package: "CompleteDSLPckg_PackageImport" = None, 43: "CompleteDSLPckg_Package" = None, 42: set["CompleteDSLPckg_Package"] = None, 47: "CompleteDSLPckg_Package" = None, 46: "CompleteDSLPckg_Package" = None, CompleteDSLPckg_Package49: set["CompleteDSLPckg_PackageableElement"] = None, 52: set["CompleteDSLPckg_Type"] = None, 55: set["CompleteDSLPckg_PackageMerge"] = None, 92: "CompleteDSLPckg_Type" = None, 266: "CompleteDSLPckg_PackageMerge" = None, CompleteDSLPckg_Package268: "CompleteDSLPckg_PackageMerge" = None):
        self.URI = URI
        self.CompleteDSLPckg_Package = CompleteDSLPckg_Package
        self.43 = 43
        self.42 = 42 if 42 is not None else set()
        self.47 = 47
        self.46 = 46
        self.CompleteDSLPckg_Package49 = CompleteDSLPckg_Package49 if CompleteDSLPckg_Package49 is not None else set()
        self.52 = 52 if 52 is not None else set()
        self.55 = 55 if 55 is not None else set()
        self.92 = 92
        self.266 = 266
        self.CompleteDSLPckg_Package268 = CompleteDSLPckg_Package268
        
    @property
    def URI(self) -> str:
        return self.__URI

    @URI.setter
    def URI(self, URI: str):
        self.__URI = URI

    @property
    def 52(self):
        return self.__52

    @52.setter
    def 52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__52", None)
        self.__52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "53"):
                    opp_val = getattr(item, "53", None)
                    
                    if opp_val == self:
                        setattr(item, "53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "53"):
                    opp_val = getattr(item, "53", None)
                    
                    setattr(item, "53", self)
                    

    @property
    def CompleteDSLPckg_Package268(self):
        return self.__CompleteDSLPckg_Package268

    @CompleteDSLPckg_Package268.setter
    def CompleteDSLPckg_Package268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__CompleteDSLPckg_Package268", None)
        self.__CompleteDSLPckg_Package268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_PackageMerge"):
                opp_val = getattr(old_value, "CompleteDSLPckg_PackageMerge", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_PackageMerge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_PackageMerge"):
                opp_val = getattr(value, "CompleteDSLPckg_PackageMerge", None)
                setattr(value, "CompleteDSLPckg_PackageMerge", self)

    @property
    def 266(self):
        return self.__266

    @266.setter
    def 266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__266", None)
        self.__266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "265"):
                opp_val = getattr(old_value, "265", None)
                if opp_val == self:
                    setattr(old_value, "265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "265"):
                opp_val = getattr(value, "265", None)
                setattr(value, "265", self)

    @property
    def 43(self):
        return self.__43

    @43.setter
    def 43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__43", None)
        self.__43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "42"):
                opp_val = getattr(old_value, "42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "42"):
                opp_val = getattr(value, "42", None)
                if opp_val is None:
                    setattr(value, "42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 55(self):
        return self.__55

    @55.setter
    def 55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__55", None)
        self.__55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "56"):
                    opp_val = getattr(item, "56", None)
                    
                    if opp_val == self:
                        setattr(item, "56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "56"):
                    opp_val = getattr(item, "56", None)
                    
                    setattr(item, "56", self)
                    

    @property
    def 92(self):
        return self.__92

    @92.setter
    def 92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__92", None)
        self.__92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "91"):
                opp_val = getattr(old_value, "91", None)
                if opp_val == self:
                    setattr(old_value, "91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "91"):
                opp_val = getattr(value, "91", None)
                setattr(value, "91", self)

    @property
    def 46(self):
        return self.__46

    @46.setter
    def 46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__46", None)
        self.__46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "47"):
                opp_val = getattr(old_value, "47", None)
                if opp_val == self:
                    setattr(old_value, "47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "47"):
                opp_val = getattr(value, "47", None)
                setattr(value, "47", self)

    @property
    def CompleteDSLPckg_Package(self):
        return self.__CompleteDSLPckg_Package

    @CompleteDSLPckg_Package.setter
    def CompleteDSLPckg_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__CompleteDSLPckg_Package", None)
        self.__CompleteDSLPckg_Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_PackageImport"):
                opp_val = getattr(old_value, "CompleteDSLPckg_PackageImport", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_PackageImport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_PackageImport"):
                opp_val = getattr(value, "CompleteDSLPckg_PackageImport", None)
                setattr(value, "CompleteDSLPckg_PackageImport", self)

    @property
    def CompleteDSLPckg_Package49(self):
        return self.__CompleteDSLPckg_Package49

    @CompleteDSLPckg_Package49.setter
    def CompleteDSLPckg_Package49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__CompleteDSLPckg_Package49", None)
        self.__CompleteDSLPckg_Package49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_PackageableElement50"):
                    opp_val = getattr(item, "CompleteDSLPckg_PackageableElement50", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_PackageableElement50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_PackageableElement50"):
                    opp_val = getattr(item, "CompleteDSLPckg_PackageableElement50", None)
                    
                    setattr(item, "CompleteDSLPckg_PackageableElement50", self)
                    

    @property
    def 47(self):
        return self.__47

    @47.setter
    def 47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__47", None)
        self.__47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "46"):
                opp_val = getattr(old_value, "46", None)
                if opp_val == self:
                    setattr(old_value, "46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "46"):
                opp_val = getattr(value, "46", None)
                setattr(value, "46", self)

    @property
    def 42(self):
        return self.__42

    @42.setter
    def 42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Package__42", None)
        self.__42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "43"):
                    opp_val = getattr(item, "43", None)
                    
                    if opp_val == self:
                        setattr(item, "43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "43"):
                    opp_val = getattr(item, "43", None)
                    
                    setattr(item, "43", self)
                    

class DirectedRelationship:

    pass
class CompleteDSLPckg_Dependency(PackageableElement, DirectedRelationship):

    pass
class CompleteDSLPckg_ProtocolConformance(DirectedRelationship):

    pass
class CompleteDSLPckg_Generalization(DirectedRelationship):

    def __init__(self, isSubstitutable: bool, 142: "CompleteDSLPckg_Classifier" = None, CompleteDSLPckg_Generalization: "CompleteDSLPckg_Classifier" = None, 195: "CompleteDSLPckg_Classifier" = None, 198: set["CompleteDSLPckg_GeneralizationSet"] = None, 313: "CompleteDSLPckg_GeneralizationSet" = None):
        self.isSubstitutable = isSubstitutable
        self.142 = 142
        self.CompleteDSLPckg_Generalization = CompleteDSLPckg_Generalization
        self.195 = 195
        self.198 = 198 if 198 is not None else set()
        self.313 = 313
        
    @property
    def isSubstitutable(self) -> bool:
        return self.__isSubstitutable

    @isSubstitutable.setter
    def isSubstitutable(self, isSubstitutable: bool):
        self.__isSubstitutable = isSubstitutable

    @property
    def 313(self):
        return self.__313

    @313.setter
    def 313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Generalization__313", None)
        self.__313 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "312"):
                opp_val = getattr(old_value, "312", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "312"):
                opp_val = getattr(value, "312", None)
                if opp_val is None:
                    setattr(value, "312", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 142(self):
        return self.__142

    @142.setter
    def 142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Generalization__142", None)
        self.__142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "141"):
                opp_val = getattr(old_value, "141", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "141"):
                opp_val = getattr(value, "141", None)
                if opp_val is None:
                    setattr(value, "141", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 195(self):
        return self.__195

    @195.setter
    def 195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Generalization__195", None)
        self.__195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "196"):
                opp_val = getattr(old_value, "196", None)
                if opp_val == self:
                    setattr(old_value, "196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "196"):
                opp_val = getattr(value, "196", None)
                setattr(value, "196", self)

    @property
    def CompleteDSLPckg_Generalization(self):
        return self.__CompleteDSLPckg_Generalization

    @CompleteDSLPckg_Generalization.setter
    def CompleteDSLPckg_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Generalization__CompleteDSLPckg_Generalization", None)
        self.__CompleteDSLPckg_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Classifier193"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Classifier193", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Classifier193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Classifier193"):
                opp_val = getattr(value, "CompleteDSLPckg_Classifier193", None)
                setattr(value, "CompleteDSLPckg_Classifier193", self)

    @property
    def 198(self):
        return self.__198

    @198.setter
    def 198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Generalization__198", None)
        self.__198 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "199"):
                    opp_val = getattr(item, "199", None)
                    
                    if opp_val == self:
                        setattr(item, "199", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "199"):
                    opp_val = getattr(item, "199", None)
                    
                    setattr(item, "199", self)
                    

class CompleteDSLPckg_PackageImport(DirectedRelationship):

    def __init__(self, visibility: str, CompleteDSLPckg_PackageImport: "CompleteDSLPckg_Package" = None, 38: "CompleteDSLPckg_Namespace" = None, 27: "CompleteDSLPckg_Namespace" = None):
        self.visibility = visibility
        self.CompleteDSLPckg_PackageImport = CompleteDSLPckg_PackageImport
        self.38 = 38
        self.27 = 27
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def 27(self):
        return self.__27

    @27.setter
    def 27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_PackageImport__27", None)
        self.__27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "26"):
                opp_val = getattr(old_value, "26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "26"):
                opp_val = getattr(value, "26", None)
                if opp_val is None:
                    setattr(value, "26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_PackageImport(self):
        return self.__CompleteDSLPckg_PackageImport

    @CompleteDSLPckg_PackageImport.setter
    def CompleteDSLPckg_PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_PackageImport__CompleteDSLPckg_PackageImport", None)
        self.__CompleteDSLPckg_PackageImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Package"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Package", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Package"):
                opp_val = getattr(value, "CompleteDSLPckg_Package", None)
                setattr(value, "CompleteDSLPckg_Package", self)

    @property
    def 38(self):
        return self.__38

    @38.setter
    def 38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_PackageImport__38", None)
        self.__38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "39"):
                opp_val = getattr(old_value, "39", None)
                if opp_val == self:
                    setattr(old_value, "39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "39"):
                opp_val = getattr(value, "39", None)
                setattr(value, "39", self)

class CompleteDSLPckg_ElementImport(DirectedRelationship):

    def __init__(self, visibility: str, alias: str, CompleteDSLPckg_ElementImport: "CompleteDSLPckg_PackageableElement" = None, 34: "CompleteDSLPckg_Namespace" = None, 24: "CompleteDSLPckg_Namespace" = None):
        self.visibility = visibility
        self.alias = alias
        self.CompleteDSLPckg_ElementImport = CompleteDSLPckg_ElementImport
        self.34 = 34
        self.24 = 24
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def CompleteDSLPckg_ElementImport(self):
        return self.__CompleteDSLPckg_ElementImport

    @CompleteDSLPckg_ElementImport.setter
    def CompleteDSLPckg_ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ElementImport__CompleteDSLPckg_ElementImport", None)
        self.__CompleteDSLPckg_ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_PackageableElement32"):
                opp_val = getattr(old_value, "CompleteDSLPckg_PackageableElement32", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_PackageableElement32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_PackageableElement32"):
                opp_val = getattr(value, "CompleteDSLPckg_PackageableElement32", None)
                setattr(value, "CompleteDSLPckg_PackageableElement32", self)

    @property
    def 24(self):
        return self.__24

    @24.setter
    def 24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ElementImport__24", None)
        self.__24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "23"):
                opp_val = getattr(old_value, "23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "23"):
                opp_val = getattr(value, "23", None)
                if opp_val is None:
                    setattr(value, "23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 34(self):
        return self.__34

    @34.setter
    def 34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_ElementImport__34", None)
        self.__34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "35"):
                opp_val = getattr(old_value, "35", None)
                if opp_val == self:
                    setattr(old_value, "35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "35"):
                opp_val = getattr(value, "35", None)
                setattr(value, "35", self)

class CompleteDSLPckg_Extend(NamedElement, DirectedRelationship):

    pass
class CompleteDSLPckg_Include(NamedElement, DirectedRelationship):

    pass
class CompleteDSLPckg_PackageMerge(DirectedRelationship):

    pass
class CompleteDSLPckg_Constraint(PackageableElement):

    pass
class CompleteDSLPckg_Namespace(NamedElement):

    pass
class Element:

    pass
class CompleteDSLPckg_Relationship(Element):

    pass
class CompleteDSLPckg_Clause(Element):

    pass
class CompleteDSLPckg_LinkEndData(Element):

    pass
class CompleteDSLPckg_MultiplicityElement(Element):

    def __init__(self, isOrdered: bool, isUnique: bool, upper: int, lower: int, 69: "CompleteDSLPckg_ValueSpecification" = None, 72: "CompleteDSLPckg_ValueSpecification" = None, 76: "CompleteDSLPckg_ValueSpecification" = None, 79: "CompleteDSLPckg_ValueSpecification" = None):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.upper = upper
        self.lower = lower
        self.69 = 69
        self.72 = 72
        self.76 = 76
        self.79 = 79
        
    @property
    def isUnique(self) -> bool:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def 76(self):
        return self.__76

    @76.setter
    def 76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_MultiplicityElement__76", None)
        self.__76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "75"):
                opp_val = getattr(old_value, "75", None)
                if opp_val == self:
                    setattr(old_value, "75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "75"):
                opp_val = getattr(value, "75", None)
                setattr(value, "75", self)

    @property
    def 79(self):
        return self.__79

    @79.setter
    def 79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_MultiplicityElement__79", None)
        self.__79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "78"):
                opp_val = getattr(old_value, "78", None)
                if opp_val == self:
                    setattr(old_value, "78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "78"):
                opp_val = getattr(value, "78", None)
                setattr(value, "78", self)

    @property
    def 69(self):
        return self.__69

    @69.setter
    def 69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_MultiplicityElement__69", None)
        self.__69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "70"):
                opp_val = getattr(old_value, "70", None)
                if opp_val == self:
                    setattr(old_value, "70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "70"):
                opp_val = getattr(value, "70", None)
                setattr(value, "70", self)

    @property
    def 72(self):
        return self.__72

    @72.setter
    def 72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_MultiplicityElement__72", None)
        self.__72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "73"):
                opp_val = getattr(old_value, "73", None)
                if opp_val == self:
                    setattr(old_value, "73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "73"):
                opp_val = getattr(value, "73", None)
                setattr(value, "73", self)

class CompleteDSLPckg_QualifierValue(Element):

    pass
class CompleteDSLPckg_ExceptionHandler(Element):

    pass
class CompleteDSLPckg_Slot(Element):

    pass
class CompleteDSLPckg_NamedElement(Element):

    def __init__(self, name: str, qualifiedName: str, visibility: str, 11: "CompleteDSLPckg_Namespace" = None, 14: set["CompleteDSLPckg_Dependency"] = None, CompleteDSLPckg_NamedElement: "CompleteDSLPckg_Namespace" = None, 21: "CompleteDSLPckg_Namespace" = None, CompleteDSLPckg_NamedElement128: "CompleteDSLPckg_Classifier" = None, 271: "CompleteDSLPckg_Dependency" = None, CompleteDSLPckg_NamedElement273: "CompleteDSLPckg_Dependency" = None, CompleteDSLPckg_NamedElement351: "CompleteDSLPckg_TimeObservation" = None, CompleteDSLPckg_NamedElement353: "CompleteDSLPckg_DurationObservation" = None, CompleteDSLPckg_NamedElement1013: "CompleteDSLPckg_Message" = None, CompleteDSLPckg_NamedElement1045: "CompleteDSLPckg_ConsiderIgnoreFragment" = None):
        self.name = name
        self.qualifiedName = qualifiedName
        self.visibility = visibility
        self.11 = 11
        self.14 = 14 if 14 is not None else set()
        self.CompleteDSLPckg_NamedElement = CompleteDSLPckg_NamedElement
        self.21 = 21
        self.CompleteDSLPckg_NamedElement128 = CompleteDSLPckg_NamedElement128
        self.271 = 271
        self.CompleteDSLPckg_NamedElement273 = CompleteDSLPckg_NamedElement273
        self.CompleteDSLPckg_NamedElement351 = CompleteDSLPckg_NamedElement351
        self.CompleteDSLPckg_NamedElement353 = CompleteDSLPckg_NamedElement353
        self.CompleteDSLPckg_NamedElement1013 = CompleteDSLPckg_NamedElement1013
        self.CompleteDSLPckg_NamedElement1045 = CompleteDSLPckg_NamedElement1045
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def 14(self):
        return self.__14

    @14.setter
    def 14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__14", None)
        self.__14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "15"):
                    opp_val = getattr(item, "15", None)
                    
                    if opp_val == self:
                        setattr(item, "15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "15"):
                    opp_val = getattr(item, "15", None)
                    
                    setattr(item, "15", self)
                    

    @property
    def 11(self):
        return self.__11

    @11.setter
    def 11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__11", None)
        self.__11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "12"):
                opp_val = getattr(old_value, "12", None)
                if opp_val == self:
                    setattr(old_value, "12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "12"):
                opp_val = getattr(value, "12", None)
                setattr(value, "12", self)

    @property
    def CompleteDSLPckg_NamedElement353(self):
        return self.__CompleteDSLPckg_NamedElement353

    @CompleteDSLPckg_NamedElement353.setter
    def CompleteDSLPckg_NamedElement353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__CompleteDSLPckg_NamedElement353", None)
        self.__CompleteDSLPckg_NamedElement353 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_DurationObservation"):
                opp_val = getattr(old_value, "CompleteDSLPckg_DurationObservation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_DurationObservation"):
                opp_val = getattr(value, "CompleteDSLPckg_DurationObservation", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_DurationObservation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 271(self):
        return self.__271

    @271.setter
    def 271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__271", None)
        self.__271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "270"):
                opp_val = getattr(old_value, "270", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "270"):
                opp_val = getattr(value, "270", None)
                if opp_val is None:
                    setattr(value, "270", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_NamedElement273(self):
        return self.__CompleteDSLPckg_NamedElement273

    @CompleteDSLPckg_NamedElement273.setter
    def CompleteDSLPckg_NamedElement273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__CompleteDSLPckg_NamedElement273", None)
        self.__CompleteDSLPckg_NamedElement273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Dependency"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Dependency", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Dependency"):
                opp_val = getattr(value, "CompleteDSLPckg_Dependency", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Dependency", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_NamedElement1013(self):
        return self.__CompleteDSLPckg_NamedElement1013

    @CompleteDSLPckg_NamedElement1013.setter
    def CompleteDSLPckg_NamedElement1013(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__CompleteDSLPckg_NamedElement1013", None)
        self.__CompleteDSLPckg_NamedElement1013 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Message1012"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Message1012", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_Message1012", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Message1012"):
                opp_val = getattr(value, "CompleteDSLPckg_Message1012", None)
                setattr(value, "CompleteDSLPckg_Message1012", self)

    @property
    def 21(self):
        return self.__21

    @21.setter
    def 21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__21", None)
        self.__21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "20"):
                opp_val = getattr(old_value, "20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "20"):
                opp_val = getattr(value, "20", None)
                if opp_val is None:
                    setattr(value, "20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_NamedElement(self):
        return self.__CompleteDSLPckg_NamedElement

    @CompleteDSLPckg_NamedElement.setter
    def CompleteDSLPckg_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__CompleteDSLPckg_NamedElement", None)
        self.__CompleteDSLPckg_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Namespace18"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Namespace18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Namespace18"):
                opp_val = getattr(value, "CompleteDSLPckg_Namespace18", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Namespace18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_NamedElement1045(self):
        return self.__CompleteDSLPckg_NamedElement1045

    @CompleteDSLPckg_NamedElement1045.setter
    def CompleteDSLPckg_NamedElement1045(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__CompleteDSLPckg_NamedElement1045", None)
        self.__CompleteDSLPckg_NamedElement1045 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_ConsiderIgnoreFragment"):
                opp_val = getattr(old_value, "CompleteDSLPckg_ConsiderIgnoreFragment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_ConsiderIgnoreFragment"):
                opp_val = getattr(value, "CompleteDSLPckg_ConsiderIgnoreFragment", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_ConsiderIgnoreFragment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_NamedElement128(self):
        return self.__CompleteDSLPckg_NamedElement128

    @CompleteDSLPckg_NamedElement128.setter
    def CompleteDSLPckg_NamedElement128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__CompleteDSLPckg_NamedElement128", None)
        self.__CompleteDSLPckg_NamedElement128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_Classifier127"):
                opp_val = getattr(old_value, "CompleteDSLPckg_Classifier127", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_Classifier127"):
                opp_val = getattr(value, "CompleteDSLPckg_Classifier127", None)
                if opp_val is None:
                    setattr(value, "CompleteDSLPckg_Classifier127", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompleteDSLPckg_NamedElement351(self):
        return self.__CompleteDSLPckg_NamedElement351

    @CompleteDSLPckg_NamedElement351.setter
    def CompleteDSLPckg_NamedElement351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_NamedElement__CompleteDSLPckg_NamedElement351", None)
        self.__CompleteDSLPckg_NamedElement351 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompleteDSLPckg_TimeObservation"):
                opp_val = getattr(old_value, "CompleteDSLPckg_TimeObservation", None)
                if opp_val == self:
                    setattr(old_value, "CompleteDSLPckg_TimeObservation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteDSLPckg_TimeObservation"):
                opp_val = getattr(value, "CompleteDSLPckg_TimeObservation", None)
                setattr(value, "CompleteDSLPckg_TimeObservation", self)

class CompleteDSLPckg_Comment(Element):

    def __init__(self, body: str, 1: "CompleteDSLPckg_Element" = None, 58: "CompleteDSLPckg_Element" = None, CompleteDSLPckg_Comment: set["CompleteDSLPckg_Element"] = None):
        self.body = body
        self.1 = 1
        self.58 = 58
        self.CompleteDSLPckg_Comment = CompleteDSLPckg_Comment if CompleteDSLPckg_Comment is not None else set()
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def CompleteDSLPckg_Comment(self):
        return self.__CompleteDSLPckg_Comment

    @CompleteDSLPckg_Comment.setter
    def CompleteDSLPckg_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Comment__CompleteDSLPckg_Comment", None)
        self.__CompleteDSLPckg_Comment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteDSLPckg_Element"):
                    opp_val = getattr(item, "CompleteDSLPckg_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteDSLPckg_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteDSLPckg_Element"):
                    opp_val = getattr(item, "CompleteDSLPckg_Element", None)
                    
                    setattr(item, "CompleteDSLPckg_Element", self)
                    

    @property
    def 58(self):
        return self.__58

    @58.setter
    def 58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Comment__58", None)
        self.__58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "59"):
                opp_val = getattr(old_value, "59", None)
                if opp_val == self:
                    setattr(old_value, "59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "59"):
                opp_val = getattr(value, "59", None)
                setattr(value, "59", self)

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CompleteDSLPckg_Comment__1", None)
        self.__1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                if opp_val is None:
                    setattr(value, "", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CompleteDSLPckg_Element(ABC):

    pass