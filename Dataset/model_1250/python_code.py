from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CallConcurrencyKind(Enum):
    sequential = "sequential"
class ExpansionKind(Enum):
    parallel = "parallel"
    iterative = "iterative"
    stream = "stream"
class ParameterDirectionKind(Enum):
    in_ = "in_"
    out = "out"
    inout = "inout"
    return_ = "return_"


############################################
# Definition of Classes
############################################

class ActivityNode:

    pass
class xmof_IntermediateActivities_ControlNode(ActivityNode):

    pass
class ControlNode:

    pass
class xmof_IntermediateActivities_JoinNode(ControlNode):

    pass
class xmof_IntermediateActivities_MergeNode(ControlNode):

    pass
class BasicActions_InputPin:

    pass
class CompleteStructuredActivities_ExecutableNode:

    pass
class BasicActions_OutputPin:

    pass
class StructuredActivityNode:

    pass
class xmof_CompleteStructuredActivities_LoopNode(StructuredActivityNode):

    def __init__(self, testedFirst: bool, xmof_CompleteStructuredActivities_LoopNode59: set["CompleteStructuredActivities_ExecutableNode"] = None, xmof_CompleteStructuredActivities_LoopNode62: set["BasicActions_OutputPin"] = None, xmof_CompleteStructuredActivities_LoopNode65: set["BasicActions_OutputPin"] = None, xmof_CompleteStructuredActivities_LoopNode68: set["CompleteStructuredActivities_ExecutableNode"] = None, xmof_CompleteStructuredActivities_LoopNode: "BasicActions_OutputPin" = None, xmof_CompleteStructuredActivities_LoopNode52: set["CompleteStructuredActivities_ExecutableNode"] = None, xmof_CompleteStructuredActivities_LoopNode54: set["BasicActions_OutputPin"] = None, xmof_CompleteStructuredActivities_LoopNode57: set["BasicActions_InputPin"] = None):
        self.testedFirst = testedFirst
        self.xmof_CompleteStructuredActivities_LoopNode59 = xmof_CompleteStructuredActivities_LoopNode59 if xmof_CompleteStructuredActivities_LoopNode59 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode62 = xmof_CompleteStructuredActivities_LoopNode62 if xmof_CompleteStructuredActivities_LoopNode62 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode65 = xmof_CompleteStructuredActivities_LoopNode65 if xmof_CompleteStructuredActivities_LoopNode65 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode68 = xmof_CompleteStructuredActivities_LoopNode68 if xmof_CompleteStructuredActivities_LoopNode68 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode = xmof_CompleteStructuredActivities_LoopNode
        self.xmof_CompleteStructuredActivities_LoopNode52 = xmof_CompleteStructuredActivities_LoopNode52 if xmof_CompleteStructuredActivities_LoopNode52 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode54 = xmof_CompleteStructuredActivities_LoopNode54 if xmof_CompleteStructuredActivities_LoopNode54 is not None else set()
        self.xmof_CompleteStructuredActivities_LoopNode57 = xmof_CompleteStructuredActivities_LoopNode57 if xmof_CompleteStructuredActivities_LoopNode57 is not None else set()
        
        pass
    @property
    def testedFirst(self):
        return self.__testedFirst

    @testedFirst.setter
    def testedFirst(self, testedFirst: bool):
        self.__testedFirst = testedFirst


    @property
    def xmof_CompleteStructuredActivities_LoopNode54(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode54

    @xmof_CompleteStructuredActivities_LoopNode54.setter
    def xmof_CompleteStructuredActivities_LoopNode54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode54", None)
        self.__xmof_CompleteStructuredActivities_LoopNode54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin55"):
                    opp_val = getattr(item, "BasicActions_OutputPin55", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin55"):
                    opp_val = getattr(item, "BasicActions_OutputPin55", None)
                    
                    setattr(item, "BasicActions_OutputPin55", self)
                    

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
    def xmof_CompleteStructuredActivities_LoopNode62(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode62

    @xmof_CompleteStructuredActivities_LoopNode62.setter
    def xmof_CompleteStructuredActivities_LoopNode62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode62", None)
        self.__xmof_CompleteStructuredActivities_LoopNode62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin63"):
                    opp_val = getattr(item, "BasicActions_OutputPin63", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin63"):
                    opp_val = getattr(item, "BasicActions_OutputPin63", None)
                    
                    setattr(item, "BasicActions_OutputPin63", self)
                    

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
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode69"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode69", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteStructuredActivities_ExecutableNode69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode69"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode69", None)
                    
                    setattr(item, "CompleteStructuredActivities_ExecutableNode69", self)
                    

    @property
    def xmof_CompleteStructuredActivities_LoopNode52(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode52

    @xmof_CompleteStructuredActivities_LoopNode52.setter
    def xmof_CompleteStructuredActivities_LoopNode52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode52", None)
        self.__xmof_CompleteStructuredActivities_LoopNode52 = value if value is not None else set()
        
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
    def xmof_CompleteStructuredActivities_LoopNode59(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode59

    @xmof_CompleteStructuredActivities_LoopNode59.setter
    def xmof_CompleteStructuredActivities_LoopNode59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode59", None)
        self.__xmof_CompleteStructuredActivities_LoopNode59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode60"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode60", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteStructuredActivities_ExecutableNode60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteStructuredActivities_ExecutableNode60"):
                    opp_val = getattr(item, "CompleteStructuredActivities_ExecutableNode60", None)
                    
                    setattr(item, "CompleteStructuredActivities_ExecutableNode60", self)
                    

    @property
    def xmof_CompleteStructuredActivities_LoopNode65(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode65

    @xmof_CompleteStructuredActivities_LoopNode65.setter
    def xmof_CompleteStructuredActivities_LoopNode65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode65", None)
        self.__xmof_CompleteStructuredActivities_LoopNode65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin66"):
                    opp_val = getattr(item, "BasicActions_OutputPin66", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin66"):
                    opp_val = getattr(item, "BasicActions_OutputPin66", None)
                    
                    setattr(item, "BasicActions_OutputPin66", self)
                    

    @property
    def xmof_CompleteStructuredActivities_LoopNode57(self):
        return self.__xmof_CompleteStructuredActivities_LoopNode57

    @xmof_CompleteStructuredActivities_LoopNode57.setter
    def xmof_CompleteStructuredActivities_LoopNode57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_LoopNode__xmof_CompleteStructuredActivities_LoopNode57", None)
        self.__xmof_CompleteStructuredActivities_LoopNode57 = value if value is not None else set()
        
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
                    

class ObjectNode:

    pass
class xmof_IntermediateActivities_ActivityParameterNode(ObjectNode):

    pass
class FinalNode:

    pass
class xmof_IntermediateActivities_ActivityFinalNode(FinalNode):

    pass
class IntermediateActivities_ObjectFlow:

    pass
class CompleteStructuredActivities_StructuredActivityNode:

    pass
class IntermediateActivities_ActivityNode:

    pass
class IntermediateActivities_Activity:

    pass
class ActivityEdge:

    pass
class xmof_IntermediateActivities_ObjectFlow(ActivityEdge):

    pass
class IntermediateActivities_ActivityEdge:

    pass
class Kernel_InstanceSpecification:

    pass
class Kernel_ValueSpecification:

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
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


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


class Kernel_Slot:

    pass
class Kernel_xmof_EClassifier:

    pass
class Kernel_xmof_EStructuralFeature:

    pass
class EModelElement:

    pass
class xmof_Kernel_Slot(EModelElement):

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
class ETypedElement:

    pass
class xmof_IntermediateActivities_ObjectNode(ETypedElement, IntermediateActivities_ActivityNode):

    pass
class xmof_Kernel_ValueSpecification(ETypedElement):

    pass
class Kernel_EEnumLiteralSpecification:

    pass
class ValueSpecification:

    pass
class xmof_Kernel_LiteralSpecification(ValueSpecification):

    pass
class xmof_Kernel_InstanceValue(ValueSpecification):

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
        
        pass
    @property
    def direction(self):
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
class EClassifier:

    pass
class xmof_BasicBehaviors_BehavioredClassifier(EClassifier):

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
class xmof_Kernel_InstanceSpecification(ENamedElement):

    pass
class xmof_IntermediateActivities_ActivityEdge(ENamedElement):

    pass
class xmof_Communications_Event(ENamedElement):

    pass
class xmof_Communications_Trigger(ENamedElement):

    pass
class BehavioredEClass:

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

class Behavior:

    pass
class xmof_IntermediateActivities_Activity(Behavior):

    def __init__(self, readOnly: bool, activity: set["IntermediateActivities_ActivityNode"] = None, activity34: set["IntermediateActivities_ActivityEdge"] = None):
        self.readOnly = readOnly
        self.activity = activity if activity is not None else set()
        self.activity34 = activity34 if activity34 is not None else set()
        
        pass
    @property
    def readOnly(self):
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly


    @property
    def activity34(self):
        return self.__activity34

    @activity34.setter
    def activity34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_IntermediateActivities_Activity__activity34", None)
        self.__activity34 = value if value is not None else set()
        
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
                if hasattr(item, "ActivityNode32"):
                    opp_val = getattr(item, "ActivityNode32", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityNode32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityNode32"):
                    opp_val = getattr(item, "ActivityNode32", None)
                    
                    setattr(item, "ActivityNode32", self)
                    

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


class BasicBehaviors_BehavioredClassifier:

    pass
class xmof_Kernel_BehavioredEClass(BasicBehaviors_BehavioredClassifier, EClass):

    pass
class Kernel_DirectedParameter:

    pass
class Kernel_BehavioredEOperation:

    pass
class BasicBehaviors_ParameterValue:

    pass
class xmof_BasicBehaviors_ParameterValueDefinition:

    pass
class Kernel_Value:

    pass
class xmof_BasicBehaviors_ParameterValue:

    pass
class PrimitiveValue:

    pass
class xmof_Kernel_IntegerValue(PrimitiveValue):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class xmof_Kernel_StringValue(PrimitiveValue):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Kernel_PrimitiveType:

    pass
class Value:

    pass
class xmof_Kernel_EnumerationValue(Value):

    pass
class xmof_Kernel_PrimitiveValue(Value):

    pass
class xmof_LociL1_SemanticVisitor(ABC):

    pass
class Kernel_xmof_EObject:

    pass
class xmof_Kernel_ObjectValue(Value):

    pass
class SemanticVisitor:

    pass
class xmof_Kernel_Value(SemanticVisitor):

    pass
class xmof_Kernel_BooleanValue(PrimitiveValue):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class Kernel_xmof_EEnum:

    pass
class InvocationAction:

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
                if hasattr(item, "BasicActions_OutputPin205"):
                    opp_val = getattr(item, "BasicActions_OutputPin205", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin205", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin205"):
                    opp_val = getattr(item, "BasicActions_OutputPin205", None)
                    
                    setattr(item, "BasicActions_OutputPin205", self)
                    

class IntermediateActivities_ObjectNode:

    pass
class xmof_BasicActions_Pin(ETypedElement, IntermediateActivities_ObjectNode):

    pass
class Pin:

    pass
class xmof_BasicActions_OutputPin(Pin):

    pass
class xmof_BasicActions_InputPin(Pin):

    pass
class xmof_BasicActions_SendSignalAction(InvocationAction):

    pass
class BasicActions_xmof_EClassifier:

    pass
class ExecutableNode:

    pass
class xmof_BasicActions_Action(ExecutableNode):

    def __init__(self, locallyReentrant: bool, xmof_BasicActions_Action: set["BasicActions_OutputPin"] = None, xmof_BasicActions_Action200: "BasicActions_xmof_EClassifier" = None, xmof_BasicActions_Action202: set["BasicActions_InputPin"] = None):
        self.locallyReentrant = locallyReentrant
        self.xmof_BasicActions_Action = xmof_BasicActions_Action if xmof_BasicActions_Action is not None else set()
        self.xmof_BasicActions_Action200 = xmof_BasicActions_Action200
        self.xmof_BasicActions_Action202 = xmof_BasicActions_Action202 if xmof_BasicActions_Action202 is not None else set()
        
        pass
    @property
    def locallyReentrant(self):
        return self.__locallyReentrant

    @locallyReentrant.setter
    def locallyReentrant(self, locallyReentrant: bool):
        self.__locallyReentrant = locallyReentrant


    @property
    def xmof_BasicActions_Action202(self):
        return self.__xmof_BasicActions_Action202

    @xmof_BasicActions_Action202.setter
    def xmof_BasicActions_Action202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_BasicActions_Action__xmof_BasicActions_Action202", None)
        self.__xmof_BasicActions_Action202 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_InputPin203"):
                    opp_val = getattr(item, "BasicActions_InputPin203", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_InputPin203", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_InputPin203"):
                    opp_val = getattr(item, "BasicActions_InputPin203", None)
                    
                    setattr(item, "BasicActions_InputPin203", self)
                    

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
                if hasattr(item, "BasicActions_OutputPin198"):
                    opp_val = getattr(item, "BasicActions_OutputPin198", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin198", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin198"):
                    opp_val = getattr(item, "BasicActions_OutputPin198", None)
                    
                    setattr(item, "BasicActions_OutputPin198", self)
                    

    @property
    def xmof_BasicActions_Action200(self):
        return self.__xmof_BasicActions_Action200

    @xmof_BasicActions_Action200.setter
    def xmof_BasicActions_Action200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_BasicActions_Action__xmof_BasicActions_Action200", None)
        self.__xmof_BasicActions_Action200 = value
        
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

class Communications_Trigger:

    pass
class CompleteActions_xmof_EClassifier:

    pass
class WriteLinkAction:

    pass
class xmof_IntermediateActions_CreateLinkAction(WriteLinkAction):

    pass
class CallAction:

    pass
class xmof_BasicActions_CallBehaviorAction(CallAction):

    pass
class xmof_BasicActions_CallOperationAction(CallAction):

    pass
class xmof_CompleteActions_StartObjectBehaviorAction(CallAction):

    pass
class xmof_IntermediateActions_DestroyLinkAction(WriteLinkAction):

    pass
class IntermediateActions_xmof_EClassifier:

    pass
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
            if hasattr(old_value, "BasicActions_InputPin160"):
                opp_val = getattr(old_value, "BasicActions_InputPin160", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin160"):
                opp_val = getattr(value, "BasicActions_InputPin160", None)
                setattr(value, "BasicActions_InputPin160", self)

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
            if hasattr(old_value, "BasicActions_InputPin135"):
                opp_val = getattr(old_value, "BasicActions_InputPin135", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin135"):
                opp_val = getattr(value, "BasicActions_InputPin135", None)
                setattr(value, "BasicActions_InputPin135", self)

class StructuralFeatureAction:

    pass
class xmof_IntermediateActions_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class xmof_IntermediateActions_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class IntermediateActions_xmof_EReference:

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
            if hasattr(old_value, "BasicActions_InputPin145"):
                opp_val = getattr(old_value, "BasicActions_InputPin145", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin145"):
                opp_val = getattr(value, "BasicActions_InputPin145", None)
                setattr(value, "BasicActions_InputPin145", self)

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
            if hasattr(old_value, "BasicActions_InputPin143"):
                opp_val = getattr(old_value, "BasicActions_InputPin143", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin143"):
                opp_val = getattr(value, "BasicActions_InputPin143", None)
                setattr(value, "BasicActions_InputPin143", self)

class xmof_IntermediateActions_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class IntermediateActions_xmof_EStructuralFeature:

    pass
class xmof_IntermediateActions_LinkEndData(EModelElement):

    pass
class IntermediateActions_LinkEndData:

    pass
class LinkAction:

    pass
class xmof_IntermediateActions_ReadLinkAction(LinkAction):

    pass
class xmof_IntermediateActions_WriteLinkAction(LinkAction):

    pass
class Action:

    pass
class xmof_IntermediateActions_StructuralFeatureAction(Action):

    pass
class xmof_BasicActions_InvocationAction(Action):

    pass
class xmof_CompleteActions_ReadExtentAction(Action):

    pass
class xmof_IntermediateActions_ValueSpecificationAction(Action):

    pass
class xmof_CompleteActions_AcceptEventAction(Action):

    def __init__(self, unmarshall: bool, xmof_CompleteActions_AcceptEventAction: set["BasicActions_OutputPin"] = None, xmof_CompleteActions_AcceptEventAction196: set["Communications_Trigger"] = None):
        self.unmarshall = unmarshall
        self.xmof_CompleteActions_AcceptEventAction = xmof_CompleteActions_AcceptEventAction if xmof_CompleteActions_AcceptEventAction is not None else set()
        self.xmof_CompleteActions_AcceptEventAction196 = xmof_CompleteActions_AcceptEventAction196 if xmof_CompleteActions_AcceptEventAction196 is not None else set()
        
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
                if hasattr(item, "BasicActions_OutputPin194"):
                    opp_val = getattr(item, "BasicActions_OutputPin194", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin194", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin194"):
                    opp_val = getattr(item, "BasicActions_OutputPin194", None)
                    
                    setattr(item, "BasicActions_OutputPin194", self)
                    

    @property
    def xmof_CompleteActions_AcceptEventAction196(self):
        return self.__xmof_CompleteActions_AcceptEventAction196

    @xmof_CompleteActions_AcceptEventAction196.setter
    def xmof_CompleteActions_AcceptEventAction196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_AcceptEventAction__xmof_CompleteActions_AcceptEventAction196", None)
        self.__xmof_CompleteActions_AcceptEventAction196 = value if value is not None else set()
        
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

    def __init__(self, ordered: bool, xmof_CompleteActions_ReduceAction: "BasicBehaviors_Behavior" = None, xmof_CompleteActions_ReduceAction168: "BasicActions_OutputPin" = None, xmof_CompleteActions_ReduceAction171: "BasicActions_InputPin" = None):
        self.ordered = ordered
        self.xmof_CompleteActions_ReduceAction = xmof_CompleteActions_ReduceAction
        self.xmof_CompleteActions_ReduceAction168 = xmof_CompleteActions_ReduceAction168
        self.xmof_CompleteActions_ReduceAction171 = xmof_CompleteActions_ReduceAction171
        
        pass
    @property
    def ordered(self):
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered


    @property
    def xmof_CompleteActions_ReduceAction168(self):
        return self.__xmof_CompleteActions_ReduceAction168

    @xmof_CompleteActions_ReduceAction168.setter
    def xmof_CompleteActions_ReduceAction168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReduceAction__xmof_CompleteActions_ReduceAction168", None)
        self.__xmof_CompleteActions_ReduceAction168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_OutputPin169"):
                opp_val = getattr(old_value, "BasicActions_OutputPin169", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_OutputPin169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_OutputPin169"):
                opp_val = getattr(value, "BasicActions_OutputPin169", None)
                setattr(value, "BasicActions_OutputPin169", self)

    @property
    def xmof_CompleteActions_ReduceAction171(self):
        return self.__xmof_CompleteActions_ReduceAction171

    @xmof_CompleteActions_ReduceAction171.setter
    def xmof_CompleteActions_ReduceAction171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReduceAction__xmof_CompleteActions_ReduceAction171", None)
        self.__xmof_CompleteActions_ReduceAction171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin172"):
                opp_val = getattr(old_value, "BasicActions_InputPin172", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin172"):
                opp_val = getattr(value, "BasicActions_InputPin172", None)
                setattr(value, "BasicActions_InputPin172", self)

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
            if hasattr(old_value, "BasicBehaviors_Behavior166"):
                opp_val = getattr(old_value, "BasicBehaviors_Behavior166", None)
                if opp_val == self:
                    setattr(old_value, "BasicBehaviors_Behavior166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicBehaviors_Behavior166"):
                opp_val = getattr(value, "BasicBehaviors_Behavior166", None)
                setattr(value, "BasicBehaviors_Behavior166", self)

class xmof_CompleteActions_ReadIsClassifiedObjectAction(Action):

    def __init__(self, direct: bool, xmof_CompleteActions_ReadIsClassifiedObjectAction: "CompleteActions_xmof_EClassifier" = None, xmof_CompleteActions_ReadIsClassifiedObjectAction180: "BasicActions_OutputPin" = None, xmof_CompleteActions_ReadIsClassifiedObjectAction183: "BasicActions_InputPin" = None):
        self.direct = direct
        self.xmof_CompleteActions_ReadIsClassifiedObjectAction = xmof_CompleteActions_ReadIsClassifiedObjectAction
        self.xmof_CompleteActions_ReadIsClassifiedObjectAction180 = xmof_CompleteActions_ReadIsClassifiedObjectAction180
        self.xmof_CompleteActions_ReadIsClassifiedObjectAction183 = xmof_CompleteActions_ReadIsClassifiedObjectAction183
        
        pass
    @property
    def direct(self):
        return self.__direct

    @direct.setter
    def direct(self, direct: bool):
        self.__direct = direct


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
            if hasattr(old_value, "CompleteActions_xmof_EClassifier178"):
                opp_val = getattr(old_value, "CompleteActions_xmof_EClassifier178", None)
                if opp_val == self:
                    setattr(old_value, "CompleteActions_xmof_EClassifier178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompleteActions_xmof_EClassifier178"):
                opp_val = getattr(value, "CompleteActions_xmof_EClassifier178", None)
                setattr(value, "CompleteActions_xmof_EClassifier178", self)

    @property
    def xmof_CompleteActions_ReadIsClassifiedObjectAction183(self):
        return self.__xmof_CompleteActions_ReadIsClassifiedObjectAction183

    @xmof_CompleteActions_ReadIsClassifiedObjectAction183.setter
    def xmof_CompleteActions_ReadIsClassifiedObjectAction183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReadIsClassifiedObjectAction__xmof_CompleteActions_ReadIsClassifiedObjectAction183", None)
        self.__xmof_CompleteActions_ReadIsClassifiedObjectAction183 = value
        
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

    @property
    def xmof_CompleteActions_ReadIsClassifiedObjectAction180(self):
        return self.__xmof_CompleteActions_ReadIsClassifiedObjectAction180

    @xmof_CompleteActions_ReadIsClassifiedObjectAction180.setter
    def xmof_CompleteActions_ReadIsClassifiedObjectAction180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReadIsClassifiedObjectAction__xmof_CompleteActions_ReadIsClassifiedObjectAction180", None)
        self.__xmof_CompleteActions_ReadIsClassifiedObjectAction180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_OutputPin181"):
                opp_val = getattr(old_value, "BasicActions_OutputPin181", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_OutputPin181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_OutputPin181"):
                opp_val = getattr(value, "BasicActions_OutputPin181", None)
                setattr(value, "BasicActions_OutputPin181", self)

class xmof_CompleteActions_StartClassifierBehaviorAction(Action):

    pass
class xmof_IntermediateActions_LinkAction(Action):

    pass
class xmof_IntermediateActions_DestroyObjectAction(Action):

    def __init__(self, destroyLinks: bool, destroyOwnedObjects: bool, xmof_IntermediateActions_DestroyObjectAction: "BasicActions_InputPin" = None):
        self.destroyLinks = destroyLinks
        self.destroyOwnedObjects = destroyOwnedObjects
        self.xmof_IntermediateActions_DestroyObjectAction = xmof_IntermediateActions_DestroyObjectAction
        
        pass
    @property
    def destroyLinks(self):
        return self.__destroyLinks

    @destroyLinks.setter
    def destroyLinks(self, destroyLinks: bool):
        self.__destroyLinks = destroyLinks


    @property
    def destroyOwnedObjects(self):
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
            if hasattr(old_value, "BasicActions_InputPin158"):
                opp_val = getattr(old_value, "BasicActions_InputPin158", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin158"):
                opp_val = getattr(value, "BasicActions_InputPin158", None)
                setattr(value, "BasicActions_InputPin158", self)

class xmof_IntermediateActions_TestIdentityAction(Action):

    pass
class xmof_IntermediateActions_CreateObjectAction(Action):

    pass
class xmof_IntermediateActions_ReadSelfAction(Action):

    pass
class xmof_CompleteActions_ReclassifyObjectAction(Action):

    def __init__(self, replaceAll: bool, xmof_CompleteActions_ReclassifyObjectAction: set["CompleteActions_xmof_EClassifier"] = None, xmof_CompleteActions_ReclassifyObjectAction188: "BasicActions_InputPin" = None, xmof_CompleteActions_ReclassifyObjectAction191: set["CompleteActions_xmof_EClassifier"] = None):
        self.replaceAll = replaceAll
        self.xmof_CompleteActions_ReclassifyObjectAction = xmof_CompleteActions_ReclassifyObjectAction if xmof_CompleteActions_ReclassifyObjectAction is not None else set()
        self.xmof_CompleteActions_ReclassifyObjectAction188 = xmof_CompleteActions_ReclassifyObjectAction188
        self.xmof_CompleteActions_ReclassifyObjectAction191 = xmof_CompleteActions_ReclassifyObjectAction191 if xmof_CompleteActions_ReclassifyObjectAction191 is not None else set()
        
        pass
    @property
    def replaceAll(self):
        return self.__replaceAll

    @replaceAll.setter
    def replaceAll(self, replaceAll: bool):
        self.__replaceAll = replaceAll


    @property
    def xmof_CompleteActions_ReclassifyObjectAction191(self):
        return self.__xmof_CompleteActions_ReclassifyObjectAction191

    @xmof_CompleteActions_ReclassifyObjectAction191.setter
    def xmof_CompleteActions_ReclassifyObjectAction191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReclassifyObjectAction__xmof_CompleteActions_ReclassifyObjectAction191", None)
        self.__xmof_CompleteActions_ReclassifyObjectAction191 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteActions_xmof_EClassifier192"):
                    opp_val = getattr(item, "CompleteActions_xmof_EClassifier192", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteActions_xmof_EClassifier192", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteActions_xmof_EClassifier192"):
                    opp_val = getattr(item, "CompleteActions_xmof_EClassifier192", None)
                    
                    setattr(item, "CompleteActions_xmof_EClassifier192", self)
                    

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
                if hasattr(item, "CompleteActions_xmof_EClassifier186"):
                    opp_val = getattr(item, "CompleteActions_xmof_EClassifier186", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteActions_xmof_EClassifier186", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteActions_xmof_EClassifier186"):
                    opp_val = getattr(item, "CompleteActions_xmof_EClassifier186", None)
                    
                    setattr(item, "CompleteActions_xmof_EClassifier186", self)
                    

    @property
    def xmof_CompleteActions_ReclassifyObjectAction188(self):
        return self.__xmof_CompleteActions_ReclassifyObjectAction188

    @xmof_CompleteActions_ReclassifyObjectAction188.setter
    def xmof_CompleteActions_ReclassifyObjectAction188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteActions_ReclassifyObjectAction__xmof_CompleteActions_ReclassifyObjectAction188", None)
        self.__xmof_CompleteActions_ReclassifyObjectAction188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicActions_InputPin189"):
                opp_val = getattr(old_value, "BasicActions_InputPin189", None)
                if opp_val == self:
                    setattr(old_value, "BasicActions_InputPin189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicActions_InputPin189"):
                opp_val = getattr(value, "BasicActions_InputPin189", None)
                setattr(value, "BasicActions_InputPin189", self)

class xmof_IntermediateActions_ClearAssociationAction(Action):

    pass
class xmof_CompleteStructuredActivities_StructuredActivityNode(Action):

    def __init__(self, mustIsolate: bool, inStructuredNode: set["IntermediateActivities_ActivityNode"] = None, inStructuredNode91: set["IntermediateActivities_ActivityEdge"] = None, xmof_CompleteStructuredActivities_StructuredActivityNode: set["BasicActions_OutputPin"] = None, xmof_CompleteStructuredActivities_StructuredActivityNode96: set["BasicActions_InputPin"] = None):
        self.mustIsolate = mustIsolate
        self.inStructuredNode = inStructuredNode if inStructuredNode is not None else set()
        self.inStructuredNode91 = inStructuredNode91 if inStructuredNode91 is not None else set()
        self.xmof_CompleteStructuredActivities_StructuredActivityNode = xmof_CompleteStructuredActivities_StructuredActivityNode if xmof_CompleteStructuredActivities_StructuredActivityNode is not None else set()
        self.xmof_CompleteStructuredActivities_StructuredActivityNode96 = xmof_CompleteStructuredActivities_StructuredActivityNode96 if xmof_CompleteStructuredActivities_StructuredActivityNode96 is not None else set()
        
        pass
    @property
    def mustIsolate(self):
        return self.__mustIsolate

    @mustIsolate.setter
    def mustIsolate(self, mustIsolate: bool):
        self.__mustIsolate = mustIsolate


    @property
    def inStructuredNode91(self):
        return self.__inStructuredNode91

    @inStructuredNode91.setter
    def inStructuredNode91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_StructuredActivityNode__inStructuredNode91", None)
        self.__inStructuredNode91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge92"):
                    opp_val = getattr(item, "ActivityEdge92", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge92"):
                    opp_val = getattr(item, "ActivityEdge92", None)
                    
                    setattr(item, "ActivityEdge92", self)
                    

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
                if hasattr(item, "BasicActions_OutputPin94"):
                    opp_val = getattr(item, "BasicActions_OutputPin94", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin94"):
                    opp_val = getattr(item, "BasicActions_OutputPin94", None)
                    
                    setattr(item, "BasicActions_OutputPin94", self)
                    

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
                if hasattr(item, "ActivityNode89"):
                    opp_val = getattr(item, "ActivityNode89", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityNode89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityNode89"):
                    opp_val = getattr(item, "ActivityNode89", None)
                    
                    setattr(item, "ActivityNode89", self)
                    

    @property
    def xmof_CompleteStructuredActivities_StructuredActivityNode96(self):
        return self.__xmof_CompleteStructuredActivities_StructuredActivityNode96

    @xmof_CompleteStructuredActivities_StructuredActivityNode96.setter
    def xmof_CompleteStructuredActivities_StructuredActivityNode96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_StructuredActivityNode__xmof_CompleteStructuredActivities_StructuredActivityNode96", None)
        self.__xmof_CompleteStructuredActivities_StructuredActivityNode96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_InputPin97"):
                    opp_val = getattr(item, "BasicActions_InputPin97", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_InputPin97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_InputPin97"):
                    opp_val = getattr(item, "BasicActions_InputPin97", None)
                    
                    setattr(item, "BasicActions_InputPin97", self)
                    

class ExtraStructuredActivities_ExpansionNode:

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
                if hasattr(item, "ExpansionNode103"):
                    opp_val = getattr(item, "ExpansionNode103", None)
                    
                    if opp_val == self:
                        setattr(item, "ExpansionNode103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExpansionNode103"):
                    opp_val = getattr(item, "ExpansionNode103", None)
                    
                    setattr(item, "ExpansionNode103", self)
                    

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
                    

class ExtraStructuredActivities_ExpansionRegion:

    pass
class xmof_ExtraStructuredActivities_ExpansionNode(ObjectNode):

    pass
class xmof_CompleteStructuredActivities_Clause(EModelElement):

    pass
class xmof_CompleteStructuredActivities_ExecutableNode(ActivityNode):

    pass
class xmof_CompleteStructuredActivities_ConditionalNode(StructuredActivityNode):

    def __init__(self, determinate: bool, assured: bool, xmof_CompleteStructuredActivities_ConditionalNode: set["CompleteStructuredActivities_Clause"] = None, xmof_CompleteStructuredActivities_ConditionalNode86: set["BasicActions_OutputPin"] = None):
        self.determinate = determinate
        self.assured = assured
        self.xmof_CompleteStructuredActivities_ConditionalNode = xmof_CompleteStructuredActivities_ConditionalNode if xmof_CompleteStructuredActivities_ConditionalNode is not None else set()
        self.xmof_CompleteStructuredActivities_ConditionalNode86 = xmof_CompleteStructuredActivities_ConditionalNode86 if xmof_CompleteStructuredActivities_ConditionalNode86 is not None else set()
        
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
    def xmof_CompleteStructuredActivities_ConditionalNode86(self):
        return self.__xmof_CompleteStructuredActivities_ConditionalNode86

    @xmof_CompleteStructuredActivities_ConditionalNode86.setter
    def xmof_CompleteStructuredActivities_ConditionalNode86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xmof_CompleteStructuredActivities_ConditionalNode__xmof_CompleteStructuredActivities_ConditionalNode86", None)
        self.__xmof_CompleteStructuredActivities_ConditionalNode86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicActions_OutputPin87"):
                    opp_val = getattr(item, "BasicActions_OutputPin87", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicActions_OutputPin87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicActions_OutputPin87"):
                    opp_val = getattr(item, "BasicActions_OutputPin87", None)
                    
                    setattr(item, "BasicActions_OutputPin87", self)
                    

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
                    

class CompleteStructuredActivities_Clause:

    pass
class xmof_IntermediateActivities_DecisionNode(ControlNode):

    pass
class xmof_IntermediateActivities_ControlFlow(ActivityEdge):

    pass
class xmof_IntermediateActivities_ForkNode(ControlNode):

    pass
class xmof_IntermediateActivities_FinalNode(ControlNode):

    pass
class xmof_IntermediateActivities_InitialNode(ControlNode):

    pass