from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ObjectNodeOrderingKind(Enum):
    unordered = "unordered"
    ordered = "ordered"
    LIFO = "LIFO"
    FIFO = "FIFO"
class ExpansionKind(Enum):
    parallel = "parallel"
    iterative = "iterative"
    stream = "stream"
class ParameterEffectKind(Enum):
    create = "create"
    read = "read"
    update = "update"
    delete = "delete"


############################################
# Definition of Classes
############################################

class ExpansionRegion:

    pass
class ExpansionNode:

    pass
class Clause:

    pass
class Activities_ExtraStructuredActivities_Classifier(ABC):

    pass
class Classifier:

    pass
class Activities_CompleteStructuredActivities_InputPin:

    pass
class ExecutableNode:

    pass
class Activities_StructuredActivities_MultiplicityElement(ABC):

    pass
class StructuredActivities_MultiplicityElement:

    pass
class ExceptionHandler:

    pass
class Activities_StructuredActivities_OutputPin:

    pass
class Activities_IntermediateActivities_Class:

    pass
class Activities_IntermediateActivities_Feature(ABC):

    pass
class IntermediateActivities_Feature:

    pass
class FundamentalActivities_Namespace:

    pass
class Activities_IntermediateActivities_BehavioralFeature(FundamentalActivities_Namespace, IntermediateActivities_Feature):

    pass
class CentralBufferNode:

    pass
class Activities_IntermediateActivities_DataStoreNode(CentralBufferNode):

    pass
class Activities_IntermediateActivities_State:

    pass
class Activities_IntermediateActivities_Constraint:

    pass
class Activities_IntermediateActivities_Element(ABC):

    pass
class FundamentalActivities_Action:

    pass
class FundamentalActivities_ActivityGroup:

    pass
class StructuredActivities_ExecutableNode:

    pass
class Activities_StructuredActivities_StructuredActivityNode(FundamentalActivities_ActivityGroup, FundamentalActivities_Action, FundamentalActivities_Namespace, StructuredActivities_ExecutableNode):

    def __init__(self, mustIsolate: bool, Activity118: "Activity" = None, Activities_StructuredActivities_StructuredActivityNode: set["Variable"] = None, ActivityNode123: set["ActivityNode"] = None, Activities_StructuredActivities_StructuredActivityNode126: set["InputPin"] = None, ActivityEdge129: set["ActivityEdge"] = None, Activities_StructuredActivities_StructuredActivityNode132: set["OutputPin"] = None):
        self.mustIsolate = mustIsolate
        self.Activity118 = Activity118
        self.Activities_StructuredActivities_StructuredActivityNode = Activities_StructuredActivities_StructuredActivityNode if Activities_StructuredActivities_StructuredActivityNode is not None else set()
        self.ActivityNode123 = ActivityNode123 if ActivityNode123 is not None else set()
        self.Activities_StructuredActivities_StructuredActivityNode126 = Activities_StructuredActivities_StructuredActivityNode126 if Activities_StructuredActivities_StructuredActivityNode126 is not None else set()
        self.ActivityEdge129 = ActivityEdge129 if ActivityEdge129 is not None else set()
        self.Activities_StructuredActivities_StructuredActivityNode132 = Activities_StructuredActivities_StructuredActivityNode132 if Activities_StructuredActivities_StructuredActivityNode132 is not None else set()
        
    @property
    def mustIsolate(self) -> bool:
        return self.__mustIsolate

    @mustIsolate.setter
    def mustIsolate(self, mustIsolate: bool):
        self.__mustIsolate = mustIsolate

    @property
    def Activities_StructuredActivities_StructuredActivityNode126(self):
        return self.__Activities_StructuredActivities_StructuredActivityNode126

    @Activities_StructuredActivities_StructuredActivityNode126.setter
    def Activities_StructuredActivities_StructuredActivityNode126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_StructuredActivityNode__Activities_StructuredActivities_StructuredActivityNode126", None)
        self.__Activities_StructuredActivities_StructuredActivityNode126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputPin127"):
                    opp_val = getattr(item, "InputPin127", None)
                    
                    if opp_val == self:
                        setattr(item, "InputPin127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputPin127"):
                    opp_val = getattr(item, "InputPin127", None)
                    
                    setattr(item, "InputPin127", self)
                    

    @property
    def ActivityNode123(self):
        return self.__ActivityNode123

    @ActivityNode123.setter
    def ActivityNode123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_StructuredActivityNode__ActivityNode123", None)
        self.__ActivityNode123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FundamentalActivities124"):
                    opp_val = getattr(item, "FundamentalActivities124", None)
                    
                    if opp_val == self:
                        setattr(item, "FundamentalActivities124", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FundamentalActivities124"):
                    opp_val = getattr(item, "FundamentalActivities124", None)
                    
                    setattr(item, "FundamentalActivities124", self)
                    

    @property
    def Activities_StructuredActivities_StructuredActivityNode132(self):
        return self.__Activities_StructuredActivities_StructuredActivityNode132

    @Activities_StructuredActivities_StructuredActivityNode132.setter
    def Activities_StructuredActivities_StructuredActivityNode132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_StructuredActivityNode__Activities_StructuredActivities_StructuredActivityNode132", None)
        self.__Activities_StructuredActivities_StructuredActivityNode132 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputPin133"):
                    opp_val = getattr(item, "OutputPin133", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputPin133", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputPin133"):
                    opp_val = getattr(item, "OutputPin133", None)
                    
                    setattr(item, "OutputPin133", self)
                    

    @property
    def ActivityEdge129(self):
        return self.__ActivityEdge129

    @ActivityEdge129.setter
    def ActivityEdge129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_StructuredActivityNode__ActivityEdge129", None)
        self.__ActivityEdge129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActivities130"):
                    opp_val = getattr(item, "BasicActivities130", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActivities130", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActivities130"):
                    opp_val = getattr(item, "BasicActivities130", None)
                    
                    setattr(item, "BasicActivities130", self)
                    

    @property
    def Activity118(self):
        return self.__Activity118

    @Activity118.setter
    def Activity118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_StructuredActivityNode__Activity118", None)
        self.__Activity118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FundamentalActivities119"):
                opp_val = getattr(old_value, "FundamentalActivities119", None)
                if opp_val == self:
                    setattr(old_value, "FundamentalActivities119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FundamentalActivities119"):
                opp_val = getattr(value, "FundamentalActivities119", None)
                setattr(value, "FundamentalActivities119", self)

    @property
    def Activities_StructuredActivities_StructuredActivityNode(self):
        return self.__Activities_StructuredActivities_StructuredActivityNode

    @Activities_StructuredActivities_StructuredActivityNode.setter
    def Activities_StructuredActivities_StructuredActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_StructuredActivityNode__Activities_StructuredActivities_StructuredActivityNode", None)
        self.__Activities_StructuredActivities_StructuredActivityNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable121"):
                    opp_val = getattr(item, "Variable121", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable121"):
                    opp_val = getattr(item, "Variable121", None)
                    
                    setattr(item, "Variable121", self)
                    

class ObjectFlow:

    pass
class FinalNode:

    pass
class Activities_IntermediateActivities_FlowFinalNode(FinalNode):

    pass
class State:

    pass
class Element:

    pass
class Activities_StructuredActivities_Clause(Element):

    pass
class Activities_ExtraStructuredActivities_ExceptionHandler(Element):

    pass
class Activities_IntermediateActivities_ValueSpecification(ABC):

    pass
class ValueSpecification:

    pass
class ControlNode:

    pass
class Activities_IntermediateActivities_FinalNode(ControlNode):

    pass
class Activities_IntermediateActivities_ForkNode(ControlNode):

    pass
class Activities_IntermediateActivities_DecisionNode(ControlNode):

    pass
class Activities_IntermediateActivities_MergeNode(ControlNode):

    pass
class Activities_IntermediateActivities_JoinNode(ControlNode):

    def __init__(self, isCombineDuplicate: bool, Activities_IntermediateActivities_JoinNode: "ValueSpecification" = None):
        self.isCombineDuplicate = isCombineDuplicate
        self.Activities_IntermediateActivities_JoinNode = Activities_IntermediateActivities_JoinNode
        
    @property
    def isCombineDuplicate(self) -> bool:
        return self.__isCombineDuplicate

    @isCombineDuplicate.setter
    def isCombineDuplicate(self, isCombineDuplicate: bool):
        self.__isCombineDuplicate = isCombineDuplicate

    @property
    def Activities_IntermediateActivities_JoinNode(self):
        return self.__Activities_IntermediateActivities_JoinNode

    @Activities_IntermediateActivities_JoinNode.setter
    def Activities_IntermediateActivities_JoinNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_IntermediateActivities_JoinNode__Activities_IntermediateActivities_JoinNode", None)
        self.__Activities_IntermediateActivities_JoinNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueSpecification86"):
                opp_val = getattr(old_value, "ValueSpecification86", None)
                if opp_val == self:
                    setattr(old_value, "ValueSpecification86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueSpecification86"):
                opp_val = getattr(value, "ValueSpecification86", None)
                setattr(value, "ValueSpecification86", self)

class Activities_BasicActivities_InitialNode(ControlNode):

    pass
class IntermediateActivities_FinalNode:

    pass
class BasicActivities_ControlNode:

    pass
class Activities_BasicActivities_ActivityFinalNode(IntermediateActivities_FinalNode, BasicActivities_ControlNode):

    pass
class Activities_BasicActivities_Parameter:

    def __init__(self, isException: bool, isStream: bool, effect: str, ParameterSet52: set["ParameterSet"] = None):
        self.isException = isException
        self.isStream = isStream
        self.effect = effect
        self.ParameterSet52 = ParameterSet52 if ParameterSet52 is not None else set()
        
    @property
    def isException(self) -> bool:
        return self.__isException

    @isException.setter
    def isException(self, isException: bool):
        self.__isException = isException

    @property
    def isStream(self) -> bool:
        return self.__isStream

    @isStream.setter
    def isStream(self, isStream: bool):
        self.__isStream = isStream

    @property
    def effect(self) -> str:
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect

    @property
    def ParameterSet52(self):
        return self.__ParameterSet52

    @ParameterSet52.setter
    def ParameterSet52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_BasicActivities_Parameter__ParameterSet52", None)
        self.__ParameterSet52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IntermediateActivities53"):
                    opp_val = getattr(item, "IntermediateActivities53", None)
                    
                    if opp_val == self:
                        setattr(item, "IntermediateActivities53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IntermediateActivities53"):
                    opp_val = getattr(item, "IntermediateActivities53", None)
                    
                    setattr(item, "IntermediateActivities53", self)
                    

class Activities_FundamentalActivities_Namespace(ABC):

    pass
class Activity:

    pass
class NamedElement:

    pass
class Activities_IntermediateActivities_ParameterSet(NamedElement):

    pass
class Activities_FundamentalActivities_ActivityGroup(NamedElement):

    pass
class OutputPin:

    pass
class InputPin:

    pass
class Constraint:

    pass
class Parameter:

    pass
class ObjectNode:

    pass
class Activities_ExtraStructuredActivities_ExpansionNode(ObjectNode):

    pass
class Activities_IntermediateActivities_CentralBufferNode(ObjectNode):

    pass
class Activities_BasicActivities_ActivityParameterNode(ObjectNode):

    pass
class Activities_BasicActivities_Pin(ObjectNode):

    def __init__(self, isControl: bool, ObjectNode: "Activities_ExtraStructuredActivities_ExceptionHandler"):
        self.isControl = isControl
        
    @property
    def isControl(self) -> bool:
        return self.__isControl

    @isControl.setter
    def isControl(self, isControl: bool):
        self.__isControl = isControl

class Activities_BasicActivities_TypedElement:

    pass
class BasicActivities_TypedElement:

    pass
class Activities_StructuredActivities_Variable(BasicActivities_TypedElement, StructuredActivities_MultiplicityElement):

    pass
class FundamentalActivities_ActivityNode:

    pass
class Activities_BasicActivities_ObjectNode(BasicActivities_TypedElement, FundamentalActivities_ActivityNode):

    pass
class RedefinableElement:

    pass
class Activities_BasicActivities_ActivityEdge(RedefinableElement):

    pass
class Activities_BasicActivities_RedefinableElement(ABC):

    pass
class BasicActivities_RedefinableElement:

    pass
class FundamentalActivities_NamedElement:

    pass
class Activities_FundamentalActivities_ActivityNode(BasicActivities_RedefinableElement, FundamentalActivities_NamedElement):

    pass
class Activities_FundamentalActivities_NamedElement(ABC):

    pass
class ParameterSet:

    pass
class Class:

    pass
class Activities_FundamentalActivities_Behavior(Class):

    pass
class Variable:

    pass
class StructuredActivityNode:

    pass
class Activities_StructuredActivities_ConditionalNode(StructuredActivityNode):

    def __init__(self, isDeterminate: bool, isAssumed: bool, Activities_StructuredActivities_ConditionalNode: set["Clause"] = None, Activities_StructuredActivities_ConditionalNode159: set["ExecutableNode"] = None, Activities_StructuredActivities_ConditionalNode162: set["ExecutableNode"] = None, Activities_StructuredActivities_ConditionalNode165: set["OutputPin"] = None, StructuredActivities78: "Activities_BasicActivities_ActivityEdge", StructuredActivities26: "Activities_FundamentalActivities_ActivityNode", StructuredActivities: "Activities_FundamentalActivities_Activity"):
        self.isDeterminate = isDeterminate
        self.isAssumed = isAssumed
        self.Activities_StructuredActivities_ConditionalNode = Activities_StructuredActivities_ConditionalNode if Activities_StructuredActivities_ConditionalNode is not None else set()
        self.Activities_StructuredActivities_ConditionalNode159 = Activities_StructuredActivities_ConditionalNode159 if Activities_StructuredActivities_ConditionalNode159 is not None else set()
        self.Activities_StructuredActivities_ConditionalNode162 = Activities_StructuredActivities_ConditionalNode162 if Activities_StructuredActivities_ConditionalNode162 is not None else set()
        self.Activities_StructuredActivities_ConditionalNode165 = Activities_StructuredActivities_ConditionalNode165 if Activities_StructuredActivities_ConditionalNode165 is not None else set()
        
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
    def Activities_StructuredActivities_ConditionalNode159(self):
        return self.__Activities_StructuredActivities_ConditionalNode159

    @Activities_StructuredActivities_ConditionalNode159.setter
    def Activities_StructuredActivities_ConditionalNode159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_ConditionalNode__Activities_StructuredActivities_ConditionalNode159", None)
        self.__Activities_StructuredActivities_ConditionalNode159 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExecutableNode160"):
                    opp_val = getattr(item, "ExecutableNode160", None)
                    
                    if opp_val == self:
                        setattr(item, "ExecutableNode160", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExecutableNode160"):
                    opp_val = getattr(item, "ExecutableNode160", None)
                    
                    setattr(item, "ExecutableNode160", self)
                    

    @property
    def Activities_StructuredActivities_ConditionalNode165(self):
        return self.__Activities_StructuredActivities_ConditionalNode165

    @Activities_StructuredActivities_ConditionalNode165.setter
    def Activities_StructuredActivities_ConditionalNode165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_ConditionalNode__Activities_StructuredActivities_ConditionalNode165", None)
        self.__Activities_StructuredActivities_ConditionalNode165 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputPin166"):
                    opp_val = getattr(item, "OutputPin166", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputPin166", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputPin166"):
                    opp_val = getattr(item, "OutputPin166", None)
                    
                    setattr(item, "OutputPin166", self)
                    

    @property
    def Activities_StructuredActivities_ConditionalNode162(self):
        return self.__Activities_StructuredActivities_ConditionalNode162

    @Activities_StructuredActivities_ConditionalNode162.setter
    def Activities_StructuredActivities_ConditionalNode162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_ConditionalNode__Activities_StructuredActivities_ConditionalNode162", None)
        self.__Activities_StructuredActivities_ConditionalNode162 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExecutableNode163"):
                    opp_val = getattr(item, "ExecutableNode163", None)
                    
                    if opp_val == self:
                        setattr(item, "ExecutableNode163", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExecutableNode163"):
                    opp_val = getattr(item, "ExecutableNode163", None)
                    
                    setattr(item, "ExecutableNode163", self)
                    

    @property
    def Activities_StructuredActivities_ConditionalNode(self):
        return self.__Activities_StructuredActivities_ConditionalNode

    @Activities_StructuredActivities_ConditionalNode.setter
    def Activities_StructuredActivities_ConditionalNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_ConditionalNode__Activities_StructuredActivities_ConditionalNode", None)
        self.__Activities_StructuredActivities_ConditionalNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Clause"):
                    opp_val = getattr(item, "Clause", None)
                    
                    if opp_val == self:
                        setattr(item, "Clause", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Clause"):
                    opp_val = getattr(item, "Clause", None)
                    
                    setattr(item, "Clause", self)
                    

class Activities_StructuredActivities_LoopNode(StructuredActivityNode):

    def __init__(self, isTestedFirst: bool, Activities_StructuredActivities_LoopNode137: set["ExecutableNode"] = None, Activities_StructuredActivities_LoopNode140: set["ExecutableNode"] = None, Activities_StructuredActivities_LoopNode143: "OutputPin" = None, Activities_StructuredActivities_LoopNode146: set["InputPin"] = None, Activities_StructuredActivities_LoopNode149: set["OutputPin"] = None, Activities_StructuredActivities_LoopNode152: set["OutputPin"] = None, Activities_StructuredActivities_LoopNode155: set["OutputPin"] = None, Activities_StructuredActivities_LoopNode: set["ExecutableNode"] = None, StructuredActivities78: "Activities_BasicActivities_ActivityEdge", StructuredActivities26: "Activities_FundamentalActivities_ActivityNode", StructuredActivities: "Activities_FundamentalActivities_Activity"):
        self.isTestedFirst = isTestedFirst
        self.Activities_StructuredActivities_LoopNode137 = Activities_StructuredActivities_LoopNode137 if Activities_StructuredActivities_LoopNode137 is not None else set()
        self.Activities_StructuredActivities_LoopNode140 = Activities_StructuredActivities_LoopNode140 if Activities_StructuredActivities_LoopNode140 is not None else set()
        self.Activities_StructuredActivities_LoopNode143 = Activities_StructuredActivities_LoopNode143
        self.Activities_StructuredActivities_LoopNode146 = Activities_StructuredActivities_LoopNode146 if Activities_StructuredActivities_LoopNode146 is not None else set()
        self.Activities_StructuredActivities_LoopNode149 = Activities_StructuredActivities_LoopNode149 if Activities_StructuredActivities_LoopNode149 is not None else set()
        self.Activities_StructuredActivities_LoopNode152 = Activities_StructuredActivities_LoopNode152 if Activities_StructuredActivities_LoopNode152 is not None else set()
        self.Activities_StructuredActivities_LoopNode155 = Activities_StructuredActivities_LoopNode155 if Activities_StructuredActivities_LoopNode155 is not None else set()
        self.Activities_StructuredActivities_LoopNode = Activities_StructuredActivities_LoopNode if Activities_StructuredActivities_LoopNode is not None else set()
        
    @property
    def isTestedFirst(self) -> bool:
        return self.__isTestedFirst

    @isTestedFirst.setter
    def isTestedFirst(self, isTestedFirst: bool):
        self.__isTestedFirst = isTestedFirst

    @property
    def Activities_StructuredActivities_LoopNode152(self):
        return self.__Activities_StructuredActivities_LoopNode152

    @Activities_StructuredActivities_LoopNode152.setter
    def Activities_StructuredActivities_LoopNode152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_LoopNode__Activities_StructuredActivities_LoopNode152", None)
        self.__Activities_StructuredActivities_LoopNode152 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputPin153"):
                    opp_val = getattr(item, "OutputPin153", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputPin153", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputPin153"):
                    opp_val = getattr(item, "OutputPin153", None)
                    
                    setattr(item, "OutputPin153", self)
                    

    @property
    def Activities_StructuredActivities_LoopNode137(self):
        return self.__Activities_StructuredActivities_LoopNode137

    @Activities_StructuredActivities_LoopNode137.setter
    def Activities_StructuredActivities_LoopNode137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_LoopNode__Activities_StructuredActivities_LoopNode137", None)
        self.__Activities_StructuredActivities_LoopNode137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExecutableNode138"):
                    opp_val = getattr(item, "ExecutableNode138", None)
                    
                    if opp_val == self:
                        setattr(item, "ExecutableNode138", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExecutableNode138"):
                    opp_val = getattr(item, "ExecutableNode138", None)
                    
                    setattr(item, "ExecutableNode138", self)
                    

    @property
    def Activities_StructuredActivities_LoopNode146(self):
        return self.__Activities_StructuredActivities_LoopNode146

    @Activities_StructuredActivities_LoopNode146.setter
    def Activities_StructuredActivities_LoopNode146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_LoopNode__Activities_StructuredActivities_LoopNode146", None)
        self.__Activities_StructuredActivities_LoopNode146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputPin147"):
                    opp_val = getattr(item, "InputPin147", None)
                    
                    if opp_val == self:
                        setattr(item, "InputPin147", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputPin147"):
                    opp_val = getattr(item, "InputPin147", None)
                    
                    setattr(item, "InputPin147", self)
                    

    @property
    def Activities_StructuredActivities_LoopNode149(self):
        return self.__Activities_StructuredActivities_LoopNode149

    @Activities_StructuredActivities_LoopNode149.setter
    def Activities_StructuredActivities_LoopNode149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_LoopNode__Activities_StructuredActivities_LoopNode149", None)
        self.__Activities_StructuredActivities_LoopNode149 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputPin150"):
                    opp_val = getattr(item, "OutputPin150", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputPin150", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputPin150"):
                    opp_val = getattr(item, "OutputPin150", None)
                    
                    setattr(item, "OutputPin150", self)
                    

    @property
    def Activities_StructuredActivities_LoopNode140(self):
        return self.__Activities_StructuredActivities_LoopNode140

    @Activities_StructuredActivities_LoopNode140.setter
    def Activities_StructuredActivities_LoopNode140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_LoopNode__Activities_StructuredActivities_LoopNode140", None)
        self.__Activities_StructuredActivities_LoopNode140 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExecutableNode141"):
                    opp_val = getattr(item, "ExecutableNode141", None)
                    
                    if opp_val == self:
                        setattr(item, "ExecutableNode141", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExecutableNode141"):
                    opp_val = getattr(item, "ExecutableNode141", None)
                    
                    setattr(item, "ExecutableNode141", self)
                    

    @property
    def Activities_StructuredActivities_LoopNode155(self):
        return self.__Activities_StructuredActivities_LoopNode155

    @Activities_StructuredActivities_LoopNode155.setter
    def Activities_StructuredActivities_LoopNode155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_LoopNode__Activities_StructuredActivities_LoopNode155", None)
        self.__Activities_StructuredActivities_LoopNode155 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputPin156"):
                    opp_val = getattr(item, "OutputPin156", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputPin156", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputPin156"):
                    opp_val = getattr(item, "OutputPin156", None)
                    
                    setattr(item, "OutputPin156", self)
                    

    @property
    def Activities_StructuredActivities_LoopNode(self):
        return self.__Activities_StructuredActivities_LoopNode

    @Activities_StructuredActivities_LoopNode.setter
    def Activities_StructuredActivities_LoopNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_LoopNode__Activities_StructuredActivities_LoopNode", None)
        self.__Activities_StructuredActivities_LoopNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExecutableNode"):
                    opp_val = getattr(item, "ExecutableNode", None)
                    
                    if opp_val == self:
                        setattr(item, "ExecutableNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExecutableNode"):
                    opp_val = getattr(item, "ExecutableNode", None)
                    
                    setattr(item, "ExecutableNode", self)
                    

    @property
    def Activities_StructuredActivities_LoopNode143(self):
        return self.__Activities_StructuredActivities_LoopNode143

    @Activities_StructuredActivities_LoopNode143.setter
    def Activities_StructuredActivities_LoopNode143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_StructuredActivities_LoopNode__Activities_StructuredActivities_LoopNode143", None)
        self.__Activities_StructuredActivities_LoopNode143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OutputPin144"):
                opp_val = getattr(old_value, "OutputPin144", None)
                if opp_val == self:
                    setattr(old_value, "OutputPin144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OutputPin144"):
                opp_val = getattr(value, "OutputPin144", None)
                setattr(value, "OutputPin144", self)

class Activities_StructuredActivities_SequenceNode(StructuredActivityNode):

    pass
class Activities_ExtraStructuredActivities_ExpansionRegion(StructuredActivityNode):

    def __init__(self, mode: str, ExpansionNode: set["ExpansionNode"] = None, ExpansionNode189: set["ExpansionNode"] = None, StructuredActivities78: "Activities_BasicActivities_ActivityEdge", StructuredActivities26: "Activities_FundamentalActivities_ActivityNode", StructuredActivities: "Activities_FundamentalActivities_Activity"):
        self.mode = mode
        self.ExpansionNode = ExpansionNode if ExpansionNode is not None else set()
        self.ExpansionNode189 = ExpansionNode189 if ExpansionNode189 is not None else set()
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def ExpansionNode(self):
        return self.__ExpansionNode

    @ExpansionNode.setter
    def ExpansionNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_ExtraStructuredActivities_ExpansionRegion__ExpansionNode", None)
        self.__ExpansionNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExtraStructuredActivities187"):
                    opp_val = getattr(item, "ExtraStructuredActivities187", None)
                    
                    if opp_val == self:
                        setattr(item, "ExtraStructuredActivities187", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExtraStructuredActivities187"):
                    opp_val = getattr(item, "ExtraStructuredActivities187", None)
                    
                    setattr(item, "ExtraStructuredActivities187", self)
                    

    @property
    def ExpansionNode189(self):
        return self.__ExpansionNode189

    @ExpansionNode189.setter
    def ExpansionNode189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_ExtraStructuredActivities_ExpansionRegion__ExpansionNode189", None)
        self.__ExpansionNode189 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExtraStructuredActivities190"):
                    opp_val = getattr(item, "ExtraStructuredActivities190", None)
                    
                    if opp_val == self:
                        setattr(item, "ExtraStructuredActivities190", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExtraStructuredActivities190"):
                    opp_val = getattr(item, "ExtraStructuredActivities190", None)
                    
                    setattr(item, "ExtraStructuredActivities190", self)
                    

class ActivityPartition:

    pass
class ActivityEdge:

    pass
class Activities_BasicActivities_ObjectFlow(ActivityEdge):

    def __init__(self, isMulticast: bool, isMultireceive: bool, ordering: str, isControlType: bool, Activities_BasicActivities_ObjectFlow: "Behavior" = None, Activities_BasicActivities_ObjectFlow81: "Behavior" = None, Activities_BasicActivities_ObjectFlow84: set["State"] = None, BasicActivities19: "Activities_FundamentalActivities_ActivityNode", BasicActivities48: "Activities_FundamentalActivities_ActivityGroup", BasicActivities113: "Activities_IntermediateActivities_InterruptibleActivityRegion", BasicActivities93: "Activities_IntermediateActivities_ActivityPartition", ActivityEdge: "Activities_FundamentalActivities_Activity", ActivityEdge61: "Activities_BasicActivities_ActivityEdge", BasicActivities130: "Activities_StructuredActivities_StructuredActivityNode", BasicActivities: "Activities_FundamentalActivities_ActivityNode"):
        self.isMulticast = isMulticast
        self.isMultireceive = isMultireceive
        self.ordering = ordering
        self.isControlType = isControlType
        self.Activities_BasicActivities_ObjectFlow = Activities_BasicActivities_ObjectFlow
        self.Activities_BasicActivities_ObjectFlow81 = Activities_BasicActivities_ObjectFlow81
        self.Activities_BasicActivities_ObjectFlow84 = Activities_BasicActivities_ObjectFlow84 if Activities_BasicActivities_ObjectFlow84 is not None else set()
        
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
    def Activities_BasicActivities_ObjectFlow84(self):
        return self.__Activities_BasicActivities_ObjectFlow84

    @Activities_BasicActivities_ObjectFlow84.setter
    def Activities_BasicActivities_ObjectFlow84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_BasicActivities_ObjectFlow__Activities_BasicActivities_ObjectFlow84", None)
        self.__Activities_BasicActivities_ObjectFlow84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    if opp_val == self:
                        setattr(item, "State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    setattr(item, "State", self)
                    

    @property
    def Activities_BasicActivities_ObjectFlow(self):
        return self.__Activities_BasicActivities_ObjectFlow

    @Activities_BasicActivities_ObjectFlow.setter
    def Activities_BasicActivities_ObjectFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_BasicActivities_ObjectFlow__Activities_BasicActivities_ObjectFlow", None)
        self.__Activities_BasicActivities_ObjectFlow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behavior"):
                opp_val = getattr(old_value, "Behavior", None)
                if opp_val == self:
                    setattr(old_value, "Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behavior"):
                opp_val = getattr(value, "Behavior", None)
                setattr(value, "Behavior", self)

    @property
    def Activities_BasicActivities_ObjectFlow81(self):
        return self.__Activities_BasicActivities_ObjectFlow81

    @Activities_BasicActivities_ObjectFlow81.setter
    def Activities_BasicActivities_ObjectFlow81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_BasicActivities_ObjectFlow__Activities_BasicActivities_ObjectFlow81", None)
        self.__Activities_BasicActivities_ObjectFlow81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behavior82"):
                opp_val = getattr(old_value, "Behavior82", None)
                if opp_val == self:
                    setattr(old_value, "Behavior82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behavior82"):
                opp_val = getattr(value, "Behavior82", None)
                setattr(value, "Behavior82", self)

class Activities_BasicActivities_ControlFlow(ActivityEdge):

    pass
class ActivityGroup:

    pass
class Activities_IntermediateActivities_InterruptibleActivityRegion(ActivityGroup):

    pass
class Activities_IntermediateActivities_ActivityPartition(ActivityGroup):

    pass
class ActivityNode:

    pass
class Activities_BasicActivities_ControlNode(ActivityNode):

    pass
class Activities_FundamentalActivities_Action(ActivityNode):

    def __init__(self, isLocallyReentrant: bool, Activities_FundamentalActivities_Action: set["Constraint"] = None, Activities_FundamentalActivities_Action29: set["Constraint"] = None, Activities_FundamentalActivities_Action32: set["InputPin"] = None, Activities_FundamentalActivities_Action34: set["OutputPin"] = None, FundamentalActivities103: "Activities_IntermediateActivities_ActivityPartition", FundamentalActivities116: "Activities_IntermediateActivities_InterruptibleActivityRegion", ActivityNode: "Activities_FundamentalActivities_Activity", FundamentalActivities56: "Activities_BasicActivities_ActivityEdge", ActivityNode14: "Activities_FundamentalActivities_ActivityNode", FundamentalActivities59: "Activities_BasicActivities_ActivityEdge", FundamentalActivities124: "Activities_StructuredActivities_StructuredActivityNode", FundamentalActivities45: "Activities_FundamentalActivities_ActivityGroup"):
        self.isLocallyReentrant = isLocallyReentrant
        self.Activities_FundamentalActivities_Action = Activities_FundamentalActivities_Action if Activities_FundamentalActivities_Action is not None else set()
        self.Activities_FundamentalActivities_Action29 = Activities_FundamentalActivities_Action29 if Activities_FundamentalActivities_Action29 is not None else set()
        self.Activities_FundamentalActivities_Action32 = Activities_FundamentalActivities_Action32 if Activities_FundamentalActivities_Action32 is not None else set()
        self.Activities_FundamentalActivities_Action34 = Activities_FundamentalActivities_Action34 if Activities_FundamentalActivities_Action34 is not None else set()
        
    @property
    def isLocallyReentrant(self) -> bool:
        return self.__isLocallyReentrant

    @isLocallyReentrant.setter
    def isLocallyReentrant(self, isLocallyReentrant: bool):
        self.__isLocallyReentrant = isLocallyReentrant

    @property
    def Activities_FundamentalActivities_Action32(self):
        return self.__Activities_FundamentalActivities_Action32

    @Activities_FundamentalActivities_Action32.setter
    def Activities_FundamentalActivities_Action32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_FundamentalActivities_Action__Activities_FundamentalActivities_Action32", None)
        self.__Activities_FundamentalActivities_Action32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputPin"):
                    opp_val = getattr(item, "InputPin", None)
                    
                    if opp_val == self:
                        setattr(item, "InputPin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputPin"):
                    opp_val = getattr(item, "InputPin", None)
                    
                    setattr(item, "InputPin", self)
                    

    @property
    def Activities_FundamentalActivities_Action(self):
        return self.__Activities_FundamentalActivities_Action

    @Activities_FundamentalActivities_Action.setter
    def Activities_FundamentalActivities_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_FundamentalActivities_Action__Activities_FundamentalActivities_Action", None)
        self.__Activities_FundamentalActivities_Action = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    setattr(item, "Constraint", self)
                    

    @property
    def Activities_FundamentalActivities_Action29(self):
        return self.__Activities_FundamentalActivities_Action29

    @Activities_FundamentalActivities_Action29.setter
    def Activities_FundamentalActivities_Action29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_FundamentalActivities_Action__Activities_FundamentalActivities_Action29", None)
        self.__Activities_FundamentalActivities_Action29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint30"):
                    opp_val = getattr(item, "Constraint30", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint30"):
                    opp_val = getattr(item, "Constraint30", None)
                    
                    setattr(item, "Constraint30", self)
                    

    @property
    def Activities_FundamentalActivities_Action34(self):
        return self.__Activities_FundamentalActivities_Action34

    @Activities_FundamentalActivities_Action34.setter
    def Activities_FundamentalActivities_Action34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_FundamentalActivities_Action__Activities_FundamentalActivities_Action34", None)
        self.__Activities_FundamentalActivities_Action34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputPin"):
                    opp_val = getattr(item, "OutputPin", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputPin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputPin"):
                    opp_val = getattr(item, "OutputPin", None)
                    
                    setattr(item, "OutputPin", self)
                    

class Activities_StructuredActivities_ExecutableNode(ActivityNode):

    pass
class Behavior:

    pass
class InterruptibleActivityRegion:

    pass
class Activities_FundamentalActivities_Activity(Behavior):

    def __init__(self, isReadOnly: bool, isSingleExecution: bool, Activities_FundamentalActivities_Activity: set["ActivityNode"] = None, ActivityGroup: set["ActivityGroup"] = None, Activities_FundamentalActivities_Activity3: set["ActivityEdge"] = None, Activities_FundamentalActivities_Activity5: set["ActivityPartition"] = None, StructuredActivityNode: set["StructuredActivityNode"] = None, Activities_FundamentalActivities_Activity8: set["Variable"] = None, Behavior82: "Activities_BasicActivities_ObjectFlow", Behavior90: "Activities_IntermediateActivities_DecisionNode", Behavior: "Activities_BasicActivities_ObjectFlow"):
        self.isReadOnly = isReadOnly
        self.isSingleExecution = isSingleExecution
        self.Activities_FundamentalActivities_Activity = Activities_FundamentalActivities_Activity if Activities_FundamentalActivities_Activity is not None else set()
        self.ActivityGroup = ActivityGroup if ActivityGroup is not None else set()
        self.Activities_FundamentalActivities_Activity3 = Activities_FundamentalActivities_Activity3 if Activities_FundamentalActivities_Activity3 is not None else set()
        self.Activities_FundamentalActivities_Activity5 = Activities_FundamentalActivities_Activity5 if Activities_FundamentalActivities_Activity5 is not None else set()
        self.StructuredActivityNode = StructuredActivityNode if StructuredActivityNode is not None else set()
        self.Activities_FundamentalActivities_Activity8 = Activities_FundamentalActivities_Activity8 if Activities_FundamentalActivities_Activity8 is not None else set()
        
    @property
    def isReadOnly(self) -> bool:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly

    @property
    def isSingleExecution(self) -> bool:
        return self.__isSingleExecution

    @isSingleExecution.setter
    def isSingleExecution(self, isSingleExecution: bool):
        self.__isSingleExecution = isSingleExecution

    @property
    def Activities_FundamentalActivities_Activity3(self):
        return self.__Activities_FundamentalActivities_Activity3

    @Activities_FundamentalActivities_Activity3.setter
    def Activities_FundamentalActivities_Activity3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_FundamentalActivities_Activity__Activities_FundamentalActivities_Activity3", None)
        self.__Activities_FundamentalActivities_Activity3 = value if value is not None else set()
        
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
    def ActivityGroup(self):
        return self.__ActivityGroup

    @ActivityGroup.setter
    def ActivityGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_FundamentalActivities_Activity__ActivityGroup", None)
        self.__ActivityGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FundamentalActivities"):
                    opp_val = getattr(item, "FundamentalActivities", None)
                    
                    if opp_val == self:
                        setattr(item, "FundamentalActivities", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FundamentalActivities"):
                    opp_val = getattr(item, "FundamentalActivities", None)
                    
                    setattr(item, "FundamentalActivities", self)
                    

    @property
    def Activities_FundamentalActivities_Activity(self):
        return self.__Activities_FundamentalActivities_Activity

    @Activities_FundamentalActivities_Activity.setter
    def Activities_FundamentalActivities_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_FundamentalActivities_Activity__Activities_FundamentalActivities_Activity", None)
        self.__Activities_FundamentalActivities_Activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityNode"):
                    opp_val = getattr(item, "ActivityNode", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityNode"):
                    opp_val = getattr(item, "ActivityNode", None)
                    
                    setattr(item, "ActivityNode", self)
                    

    @property
    def Activities_FundamentalActivities_Activity5(self):
        return self.__Activities_FundamentalActivities_Activity5

    @Activities_FundamentalActivities_Activity5.setter
    def Activities_FundamentalActivities_Activity5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_FundamentalActivities_Activity__Activities_FundamentalActivities_Activity5", None)
        self.__Activities_FundamentalActivities_Activity5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityPartition"):
                    opp_val = getattr(item, "ActivityPartition", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityPartition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityPartition"):
                    opp_val = getattr(item, "ActivityPartition", None)
                    
                    setattr(item, "ActivityPartition", self)
                    

    @property
    def Activities_FundamentalActivities_Activity8(self):
        return self.__Activities_FundamentalActivities_Activity8

    @Activities_FundamentalActivities_Activity8.setter
    def Activities_FundamentalActivities_Activity8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_FundamentalActivities_Activity__Activities_FundamentalActivities_Activity8", None)
        self.__Activities_FundamentalActivities_Activity8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable"):
                    opp_val = getattr(item, "Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable"):
                    opp_val = getattr(item, "Variable", None)
                    
                    setattr(item, "Variable", self)
                    

    @property
    def StructuredActivityNode(self):
        return self.__StructuredActivityNode

    @StructuredActivityNode.setter
    def StructuredActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activities_FundamentalActivities_Activity__StructuredActivityNode", None)
        self.__StructuredActivityNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StructuredActivities"):
                    opp_val = getattr(item, "StructuredActivities", None)
                    
                    if opp_val == self:
                        setattr(item, "StructuredActivities", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StructuredActivities"):
                    opp_val = getattr(item, "StructuredActivities", None)
                    
                    setattr(item, "StructuredActivities", self)
                    
