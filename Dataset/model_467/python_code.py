from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParameterDirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
    return = "return"
class ExpansionKind(Enum):
    parallel = "parallel"
    iterative = "iterative"
    stream = "stream"
class CallConcurrencyKind(Enum):
    sequential = "sequential"
class AggregationKind(Enum):
    none = "none"
    shared = "shared"
    composite = "composite"
class VisibilityKind(Enum):
    public = "public"
    private = "private"
    protected = "protected"
    package = "package"


############################################
# Definition of Classes
############################################

class fuml_BasicBehaviors_ParameterValue:

    pass
class Kernel_ExtensionalValue:

    pass
class fuml_LociL1_Locus:

    pass
class fuml_LociL1_SemanticVisitor(ABC):

    pass
class SemanticVisitor:

    pass
class fuml_Kernel_Value(SemanticVisitor):

    pass
class Kernel_FeatureValue:

    pass
class LociL1_Locus:

    pass
class CompoundValue:

    pass
class fuml_Kernel_DataValue(CompoundValue):

    pass
class fuml_Kernel_ExtensionalValue(CompoundValue):

    pass
class ExtensionalValue:

    pass
class fuml_Kernel_Link(ExtensionalValue):

    pass
class fuml_Kernel_Object(ExtensionalValue):

    pass
class Kernel_Object:

    pass
class StructuredValue:

    pass
class fuml_Kernel_CompoundValue(StructuredValue):

    pass
class fuml_Kernel_Reference(StructuredValue):

    pass
class Kernel_PrimitiveType:

    pass
class PrimitiveValue:

    pass
class fuml_Kernel_IntegerValue(PrimitiveValue):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class fuml_Kernel_BooleanValue(PrimitiveValue):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class fuml_Kernel_StringValue(PrimitiveValue):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class fuml_Kernel_UnlimitedNaturalValue(PrimitiveValue):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class Kernel_Value:

    pass
class fuml_Kernel_FeatureValue:

    def __init__(self, position: int, fuml_Kernel_FeatureValue: "Kernel_StructuralFeature" = None, fuml_Kernel_FeatureValue383: set["Kernel_Value"] = None):
        self.position = position
        self.fuml_Kernel_FeatureValue = fuml_Kernel_FeatureValue
        self.fuml_Kernel_FeatureValue383 = fuml_Kernel_FeatureValue383 if fuml_Kernel_FeatureValue383 is not None else set()
        
    @property
    def position(self) -> int:
        return self.__position

    @position.setter
    def position(self, position: int):
        self.__position = position

    @property
    def fuml_Kernel_FeatureValue383(self):
        return self.__fuml_Kernel_FeatureValue383

    @fuml_Kernel_FeatureValue383.setter
    def fuml_Kernel_FeatureValue383(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_FeatureValue__fuml_Kernel_FeatureValue383", None)
        self.__fuml_Kernel_FeatureValue383 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Kernel_Value"):
                    opp_val = getattr(item, "Kernel_Value", None)
                    
                    if opp_val == self:
                        setattr(item, "Kernel_Value", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Kernel_Value"):
                    opp_val = getattr(item, "Kernel_Value", None)
                    
                    setattr(item, "Kernel_Value", self)
                    

    @property
    def fuml_Kernel_FeatureValue(self):
        return self.__fuml_Kernel_FeatureValue

    @fuml_Kernel_FeatureValue.setter
    def fuml_Kernel_FeatureValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_FeatureValue__fuml_Kernel_FeatureValue", None)
        self.__fuml_Kernel_FeatureValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Kernel_StructuralFeature381"):
                opp_val = getattr(old_value, "Kernel_StructuralFeature381", None)
                if opp_val == self:
                    setattr(old_value, "Kernel_StructuralFeature381", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Kernel_StructuralFeature381"):
                opp_val = getattr(value, "Kernel_StructuralFeature381", None)
                setattr(value, "Kernel_StructuralFeature381", self)

class InvocationAction:

    pass
class fuml_BasicActions_SendSignalAction(InvocationAction):

    pass
class fuml_BasicActions_CallAction(InvocationAction):

    def __init__(self, synchronous: bool, fuml_BasicActions_CallAction: set["BasicActions_OutputPin"] = None):
        self.synchronous = synchronous
        self.fuml_BasicActions_CallAction = fuml_BasicActions_CallAction if fuml_BasicActions_CallAction is not None else set()
        
    @property
    def synchronous(self) -> bool:
        return self.__synchronous

    @synchronous.setter
    def synchronous(self, synchronous: bool):
        self.__synchronous = synchronous

    @property
    def fuml_BasicActions_CallAction(self):
        return self.__fuml_BasicActions_CallAction

    @fuml_BasicActions_CallAction.setter
    def fuml_BasicActions_CallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_BasicActions_CallAction__fuml_BasicActions_CallAction", None)
        self.__fuml_BasicActions_CallAction = value if value is not None else set()
        
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
class fuml_BasicActions_InputPin(Pin):

    pass
class Value:

    pass
class fuml_Kernel_EnumerationValue(Value):

    pass
class fuml_Kernel_PrimitiveValue(Value):

    pass
class fuml_Kernel_StructuredValue(Value):

    pass
class fuml_BasicActions_OutputPin(Pin):

    pass
class ExecutableNode:

    pass
class fuml_BasicActions_Action(ExecutableNode):

    def __init__(self, locallyReentrant: bool, fuml_BasicActions_Action: set["BasicActions_OutputPin"] = None, fuml_BasicActions_Action359: "Kernel_Classifier" = None, fuml_BasicActions_Action362: set["BasicActions_InputPin"] = None):
        self.locallyReentrant = locallyReentrant
        self.fuml_BasicActions_Action = fuml_BasicActions_Action if fuml_BasicActions_Action is not None else set()
        self.fuml_BasicActions_Action359 = fuml_BasicActions_Action359
        self.fuml_BasicActions_Action362 = fuml_BasicActions_Action362 if fuml_BasicActions_Action362 is not None else set()
        
    @property
    def locallyReentrant(self) -> bool:
        return self.__locallyReentrant

    @locallyReentrant.setter
    def locallyReentrant(self, locallyReentrant: bool):
        self.__locallyReentrant = locallyReentrant

    @property
    def fuml_BasicActions_Action(self):
        return self.__fuml_BasicActions_Action

    @fuml_BasicActions_Action.setter
    def fuml_BasicActions_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_BasicActions_Action__fuml_BasicActions_Action", None)
        self.__fuml_BasicActions_Action = value if value is not None else set()
        
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
    def fuml_BasicActions_Action359(self):
        return self.__fuml_BasicActions_Action359

    @fuml_BasicActions_Action359.setter
    def fuml_BasicActions_Action359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_BasicActions_Action__fuml_BasicActions_Action359", None)
        self.__fuml_BasicActions_Action359 = value
        
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

    @property
    def fuml_BasicActions_Action362(self):
        return self.__fuml_BasicActions_Action362

    @fuml_BasicActions_Action362.setter
    def fuml_BasicActions_Action362(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_BasicActions_Action__fuml_BasicActions_Action362", None)
        self.__fuml_BasicActions_Action362 = value if value is not None else set()
        
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
                    

class Communications_Trigger:

    pass
class CallAction:

    pass
class fuml_BasicActions_CallBehaviorAction(CallAction):

    pass
class fuml_BasicActions_CallOperationAction(CallAction):

    pass
class fuml_CompleteActions_StartObjectBehaviorAction(CallAction):

    pass
class WriteLinkAction:

    pass
class fuml_IntermediateActions_DestroyLinkAction(WriteLinkAction):

    pass
class fuml_IntermediateActions_CreateLinkAction(WriteLinkAction):

    pass
class WriteStructuralFeatureAction:

    pass
class fuml_IntermediateActions_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    def __init__(self, replaceAll: bool, fuml_IntermediateActions_AddStructuralFeatureValueAction: "BasicActions_InputPin" = None):
        self.replaceAll = replaceAll
        self.fuml_IntermediateActions_AddStructuralFeatureValueAction = fuml_IntermediateActions_AddStructuralFeatureValueAction
        
    @property
    def replaceAll(self) -> bool:
        return self.__replaceAll

    @replaceAll.setter
    def replaceAll(self, replaceAll: bool):
        self.__replaceAll = replaceAll

    @property
    def fuml_IntermediateActions_AddStructuralFeatureValueAction(self):
        return self.__fuml_IntermediateActions_AddStructuralFeatureValueAction

    @fuml_IntermediateActions_AddStructuralFeatureValueAction.setter
    def fuml_IntermediateActions_AddStructuralFeatureValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_IntermediateActions_AddStructuralFeatureValueAction__fuml_IntermediateActions_AddStructuralFeatureValueAction", None)
        self.__fuml_IntermediateActions_AddStructuralFeatureValueAction = value
        
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

class fuml_IntermediateActions_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    def __init__(self, removeDuplicates: bool, fuml_IntermediateActions_RemoveStructuralFeatureValueAction: "BasicActions_InputPin" = None):
        self.removeDuplicates = removeDuplicates
        self.fuml_IntermediateActions_RemoveStructuralFeatureValueAction = fuml_IntermediateActions_RemoveStructuralFeatureValueAction
        
    @property
    def removeDuplicates(self) -> bool:
        return self.__removeDuplicates

    @removeDuplicates.setter
    def removeDuplicates(self, removeDuplicates: bool):
        self.__removeDuplicates = removeDuplicates

    @property
    def fuml_IntermediateActions_RemoveStructuralFeatureValueAction(self):
        return self.__fuml_IntermediateActions_RemoveStructuralFeatureValueAction

    @fuml_IntermediateActions_RemoveStructuralFeatureValueAction.setter
    def fuml_IntermediateActions_RemoveStructuralFeatureValueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_IntermediateActions_RemoveStructuralFeatureValueAction__fuml_IntermediateActions_RemoveStructuralFeatureValueAction", None)
        self.__fuml_IntermediateActions_RemoveStructuralFeatureValueAction = value
        
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

class StructuralFeatureAction:

    pass
class fuml_IntermediateActions_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class fuml_IntermediateActions_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class LinkEndData:

    pass
class fuml_IntermediateActions_LinkEndDestructionData(LinkEndData):

    def __init__(self, destroyDuplicates: bool, fuml_IntermediateActions_LinkEndDestructionData: "BasicActions_InputPin" = None):
        self.destroyDuplicates = destroyDuplicates
        self.fuml_IntermediateActions_LinkEndDestructionData = fuml_IntermediateActions_LinkEndDestructionData
        
    @property
    def destroyDuplicates(self) -> bool:
        return self.__destroyDuplicates

    @destroyDuplicates.setter
    def destroyDuplicates(self, destroyDuplicates: bool):
        self.__destroyDuplicates = destroyDuplicates

    @property
    def fuml_IntermediateActions_LinkEndDestructionData(self):
        return self.__fuml_IntermediateActions_LinkEndDestructionData

    @fuml_IntermediateActions_LinkEndDestructionData.setter
    def fuml_IntermediateActions_LinkEndDestructionData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_IntermediateActions_LinkEndDestructionData__fuml_IntermediateActions_LinkEndDestructionData", None)
        self.__fuml_IntermediateActions_LinkEndDestructionData = value
        
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

class fuml_IntermediateActions_LinkEndCreationData(LinkEndData):

    def __init__(self, replaceAll: bool, fuml_IntermediateActions_LinkEndCreationData: "BasicActions_InputPin" = None):
        self.replaceAll = replaceAll
        self.fuml_IntermediateActions_LinkEndCreationData = fuml_IntermediateActions_LinkEndCreationData
        
    @property
    def replaceAll(self) -> bool:
        return self.__replaceAll

    @replaceAll.setter
    def replaceAll(self, replaceAll: bool):
        self.__replaceAll = replaceAll

    @property
    def fuml_IntermediateActions_LinkEndCreationData(self):
        return self.__fuml_IntermediateActions_LinkEndCreationData

    @fuml_IntermediateActions_LinkEndCreationData.setter
    def fuml_IntermediateActions_LinkEndCreationData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_IntermediateActions_LinkEndCreationData__fuml_IntermediateActions_LinkEndCreationData", None)
        self.__fuml_IntermediateActions_LinkEndCreationData = value
        
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

class fuml_IntermediateActions_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class ExtraStructuredActivities_ExpansionNode:

    pass
class IntermediateActions_LinkEndData:

    pass
class LinkAction:

    pass
class fuml_IntermediateActions_ReadLinkAction(LinkAction):

    pass
class fuml_IntermediateActions_WriteLinkAction(LinkAction):

    pass
class ExtraStructuredActivities_ExpansionRegion:

    pass
class Action:

    pass
class fuml_IntermediateActions_ClearAssociationAction(Action):

    pass
class fuml_CompleteActions_ReadIsClassifiedObjectAction(Action):

    def __init__(self, direct: bool, fuml_CompleteActions_ReadIsClassifiedObjectAction: "Kernel_Classifier" = None, fuml_CompleteActions_ReadIsClassifiedObjectAction339: "BasicActions_OutputPin" = None, fuml_CompleteActions_ReadIsClassifiedObjectAction342: "BasicActions_InputPin" = None):
        self.direct = direct
        self.fuml_CompleteActions_ReadIsClassifiedObjectAction = fuml_CompleteActions_ReadIsClassifiedObjectAction
        self.fuml_CompleteActions_ReadIsClassifiedObjectAction339 = fuml_CompleteActions_ReadIsClassifiedObjectAction339
        self.fuml_CompleteActions_ReadIsClassifiedObjectAction342 = fuml_CompleteActions_ReadIsClassifiedObjectAction342
        
    @property
    def direct(self) -> bool:
        return self.__direct

    @direct.setter
    def direct(self, direct: bool):
        self.__direct = direct

    @property
    def fuml_CompleteActions_ReadIsClassifiedObjectAction342(self):
        return self.__fuml_CompleteActions_ReadIsClassifiedObjectAction342

    @fuml_CompleteActions_ReadIsClassifiedObjectAction342.setter
    def fuml_CompleteActions_ReadIsClassifiedObjectAction342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteActions_ReadIsClassifiedObjectAction__fuml_CompleteActions_ReadIsClassifiedObjectAction342", None)
        self.__fuml_CompleteActions_ReadIsClassifiedObjectAction342 = value
        
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
    def fuml_CompleteActions_ReadIsClassifiedObjectAction339(self):
        return self.__fuml_CompleteActions_ReadIsClassifiedObjectAction339

    @fuml_CompleteActions_ReadIsClassifiedObjectAction339.setter
    def fuml_CompleteActions_ReadIsClassifiedObjectAction339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteActions_ReadIsClassifiedObjectAction__fuml_CompleteActions_ReadIsClassifiedObjectAction339", None)
        self.__fuml_CompleteActions_ReadIsClassifiedObjectAction339 = value
        
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

    @property
    def fuml_CompleteActions_ReadIsClassifiedObjectAction(self):
        return self.__fuml_CompleteActions_ReadIsClassifiedObjectAction

    @fuml_CompleteActions_ReadIsClassifiedObjectAction.setter
    def fuml_CompleteActions_ReadIsClassifiedObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteActions_ReadIsClassifiedObjectAction__fuml_CompleteActions_ReadIsClassifiedObjectAction", None)
        self.__fuml_CompleteActions_ReadIsClassifiedObjectAction = value
        
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

class fuml_IntermediateActions_LinkAction(Action):

    pass
class fuml_CompleteActions_AcceptEventAction(Action):

    def __init__(self, unmarshall: bool, fuml_CompleteActions_AcceptEventAction: set["BasicActions_OutputPin"] = None, fuml_CompleteActions_AcceptEventAction355: set["Communications_Trigger"] = None):
        self.unmarshall = unmarshall
        self.fuml_CompleteActions_AcceptEventAction = fuml_CompleteActions_AcceptEventAction if fuml_CompleteActions_AcceptEventAction is not None else set()
        self.fuml_CompleteActions_AcceptEventAction355 = fuml_CompleteActions_AcceptEventAction355 if fuml_CompleteActions_AcceptEventAction355 is not None else set()
        
    @property
    def unmarshall(self) -> bool:
        return self.__unmarshall

    @unmarshall.setter
    def unmarshall(self, unmarshall: bool):
        self.__unmarshall = unmarshall

    @property
    def fuml_CompleteActions_AcceptEventAction355(self):
        return self.__fuml_CompleteActions_AcceptEventAction355

    @fuml_CompleteActions_AcceptEventAction355.setter
    def fuml_CompleteActions_AcceptEventAction355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteActions_AcceptEventAction__fuml_CompleteActions_AcceptEventAction355", None)
        self.__fuml_CompleteActions_AcceptEventAction355 = value if value is not None else set()
        
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
    def fuml_CompleteActions_AcceptEventAction(self):
        return self.__fuml_CompleteActions_AcceptEventAction

    @fuml_CompleteActions_AcceptEventAction.setter
    def fuml_CompleteActions_AcceptEventAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteActions_AcceptEventAction__fuml_CompleteActions_AcceptEventAction", None)
        self.__fuml_CompleteActions_AcceptEventAction = value if value is not None else set()
        
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
                    

class fuml_IntermediateActions_ValueSpecificationAction(Action):

    pass
class fuml_IntermediateActions_StructuralFeatureAction(Action):

    pass
class fuml_IntermediateActions_DestroyObjectAction(Action):

    def __init__(self, destroyLinks: bool, destroyOwnedObjects: bool, fuml_IntermediateActions_DestroyObjectAction: "BasicActions_InputPin" = None):
        self.destroyLinks = destroyLinks
        self.destroyOwnedObjects = destroyOwnedObjects
        self.fuml_IntermediateActions_DestroyObjectAction = fuml_IntermediateActions_DestroyObjectAction
        
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
    def fuml_IntermediateActions_DestroyObjectAction(self):
        return self.__fuml_IntermediateActions_DestroyObjectAction

    @fuml_IntermediateActions_DestroyObjectAction.setter
    def fuml_IntermediateActions_DestroyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_IntermediateActions_DestroyObjectAction__fuml_IntermediateActions_DestroyObjectAction", None)
        self.__fuml_IntermediateActions_DestroyObjectAction = value
        
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

class fuml_BasicActions_InvocationAction(Action):

    pass
class fuml_CompleteActions_ReadExtentAction(Action):

    pass
class fuml_IntermediateActions_CreateObjectAction(Action):

    pass
class fuml_IntermediateActions_TestIdentityAction(Action):

    pass
class fuml_IntermediateActions_ReadSelfAction(Action):

    pass
class fuml_CompleteActions_StartClassifierBehaviorAction(Action):

    pass
class fuml_CompleteActions_ReclassifyObjectAction(Action):

    def __init__(self, replaceAll: bool, fuml_CompleteActions_ReclassifyObjectAction: set["Kernel_Classifier"] = None, fuml_CompleteActions_ReclassifyObjectAction347: "BasicActions_InputPin" = None, fuml_CompleteActions_ReclassifyObjectAction350: set["Kernel_Classifier"] = None):
        self.replaceAll = replaceAll
        self.fuml_CompleteActions_ReclassifyObjectAction = fuml_CompleteActions_ReclassifyObjectAction if fuml_CompleteActions_ReclassifyObjectAction is not None else set()
        self.fuml_CompleteActions_ReclassifyObjectAction347 = fuml_CompleteActions_ReclassifyObjectAction347
        self.fuml_CompleteActions_ReclassifyObjectAction350 = fuml_CompleteActions_ReclassifyObjectAction350 if fuml_CompleteActions_ReclassifyObjectAction350 is not None else set()
        
    @property
    def replaceAll(self) -> bool:
        return self.__replaceAll

    @replaceAll.setter
    def replaceAll(self, replaceAll: bool):
        self.__replaceAll = replaceAll

    @property
    def fuml_CompleteActions_ReclassifyObjectAction350(self):
        return self.__fuml_CompleteActions_ReclassifyObjectAction350

    @fuml_CompleteActions_ReclassifyObjectAction350.setter
    def fuml_CompleteActions_ReclassifyObjectAction350(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteActions_ReclassifyObjectAction__fuml_CompleteActions_ReclassifyObjectAction350", None)
        self.__fuml_CompleteActions_ReclassifyObjectAction350 = value if value is not None else set()
        
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
    def fuml_CompleteActions_ReclassifyObjectAction(self):
        return self.__fuml_CompleteActions_ReclassifyObjectAction

    @fuml_CompleteActions_ReclassifyObjectAction.setter
    def fuml_CompleteActions_ReclassifyObjectAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteActions_ReclassifyObjectAction__fuml_CompleteActions_ReclassifyObjectAction", None)
        self.__fuml_CompleteActions_ReclassifyObjectAction = value if value is not None else set()
        
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
                    

    @property
    def fuml_CompleteActions_ReclassifyObjectAction347(self):
        return self.__fuml_CompleteActions_ReclassifyObjectAction347

    @fuml_CompleteActions_ReclassifyObjectAction347.setter
    def fuml_CompleteActions_ReclassifyObjectAction347(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteActions_ReclassifyObjectAction__fuml_CompleteActions_ReclassifyObjectAction347", None)
        self.__fuml_CompleteActions_ReclassifyObjectAction347 = value
        
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

class fuml_CompleteActions_ReduceAction(Action):

    def __init__(self, ordered: bool, fuml_CompleteActions_ReduceAction: "BasicBehaviors_Behavior" = None, fuml_CompleteActions_ReduceAction326: "BasicActions_OutputPin" = None, fuml_CompleteActions_ReduceAction329: "BasicActions_InputPin" = None):
        self.ordered = ordered
        self.fuml_CompleteActions_ReduceAction = fuml_CompleteActions_ReduceAction
        self.fuml_CompleteActions_ReduceAction326 = fuml_CompleteActions_ReduceAction326
        self.fuml_CompleteActions_ReduceAction329 = fuml_CompleteActions_ReduceAction329
        
    @property
    def ordered(self) -> bool:
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered

    @property
    def fuml_CompleteActions_ReduceAction326(self):
        return self.__fuml_CompleteActions_ReduceAction326

    @fuml_CompleteActions_ReduceAction326.setter
    def fuml_CompleteActions_ReduceAction326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteActions_ReduceAction__fuml_CompleteActions_ReduceAction326", None)
        self.__fuml_CompleteActions_ReduceAction326 = value
        
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
    def fuml_CompleteActions_ReduceAction329(self):
        return self.__fuml_CompleteActions_ReduceAction329

    @fuml_CompleteActions_ReduceAction329.setter
    def fuml_CompleteActions_ReduceAction329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteActions_ReduceAction__fuml_CompleteActions_ReduceAction329", None)
        self.__fuml_CompleteActions_ReduceAction329 = value
        
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

    @property
    def fuml_CompleteActions_ReduceAction(self):
        return self.__fuml_CompleteActions_ReduceAction

    @fuml_CompleteActions_ReduceAction.setter
    def fuml_CompleteActions_ReduceAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteActions_ReduceAction__fuml_CompleteActions_ReduceAction", None)
        self.__fuml_CompleteActions_ReduceAction = value
        
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

class fuml_CompleteStructuredActivities_StructuredActivityNode(Action):

    def __init__(self, mustIsolate: bool, Activities238: set["IntermediateActivities_ActivityNode"] = None, Activities241: set["IntermediateActivities_ActivityEdge"] = None, fuml_CompleteStructuredActivities_StructuredActivityNode: set["BasicActions_OutputPin"] = None, fuml_CompleteStructuredActivities_StructuredActivityNode246: set["BasicActions_InputPin"] = None):
        self.mustIsolate = mustIsolate
        self.Activities238 = Activities238 if Activities238 is not None else set()
        self.Activities241 = Activities241 if Activities241 is not None else set()
        self.fuml_CompleteStructuredActivities_StructuredActivityNode = fuml_CompleteStructuredActivities_StructuredActivityNode if fuml_CompleteStructuredActivities_StructuredActivityNode is not None else set()
        self.fuml_CompleteStructuredActivities_StructuredActivityNode246 = fuml_CompleteStructuredActivities_StructuredActivityNode246 if fuml_CompleteStructuredActivities_StructuredActivityNode246 is not None else set()
        
    @property
    def mustIsolate(self) -> bool:
        return self.__mustIsolate

    @mustIsolate.setter
    def mustIsolate(self, mustIsolate: bool):
        self.__mustIsolate = mustIsolate

    @property
    def fuml_CompleteStructuredActivities_StructuredActivityNode246(self):
        return self.__fuml_CompleteStructuredActivities_StructuredActivityNode246

    @fuml_CompleteStructuredActivities_StructuredActivityNode246.setter
    def fuml_CompleteStructuredActivities_StructuredActivityNode246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteStructuredActivities_StructuredActivityNode__fuml_CompleteStructuredActivities_StructuredActivityNode246", None)
        self.__fuml_CompleteStructuredActivities_StructuredActivityNode246 = value if value is not None else set()
        
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
    def Activities241(self):
        return self.__Activities241

    @Activities241.setter
    def Activities241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteStructuredActivities_StructuredActivityNode__Activities241", None)
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
        old_value = getattr(self, f"_fuml_CompleteStructuredActivities_StructuredActivityNode__Activities238", None)
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
    def fuml_CompleteStructuredActivities_StructuredActivityNode(self):
        return self.__fuml_CompleteStructuredActivities_StructuredActivityNode

    @fuml_CompleteStructuredActivities_StructuredActivityNode.setter
    def fuml_CompleteStructuredActivities_StructuredActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteStructuredActivities_StructuredActivityNode__fuml_CompleteStructuredActivities_StructuredActivityNode", None)
        self.__fuml_CompleteStructuredActivities_StructuredActivityNode = value if value is not None else set()
        
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
                    

class CompleteStructuredActivities_Clause:

    pass
class BasicActions_InputPin:

    pass
class BasicActions_OutputPin:

    pass
class StructuredActivityNode:

    pass
class fuml_CompleteStructuredActivities_ConditionalNode(StructuredActivityNode):

    def __init__(self, determinate: bool, assured: bool, fuml_CompleteStructuredActivities_ConditionalNode: set["CompleteStructuredActivities_Clause"] = None, fuml_CompleteStructuredActivities_ConditionalNode235: set["BasicActions_OutputPin"] = None):
        self.determinate = determinate
        self.assured = assured
        self.fuml_CompleteStructuredActivities_ConditionalNode = fuml_CompleteStructuredActivities_ConditionalNode if fuml_CompleteStructuredActivities_ConditionalNode is not None else set()
        self.fuml_CompleteStructuredActivities_ConditionalNode235 = fuml_CompleteStructuredActivities_ConditionalNode235 if fuml_CompleteStructuredActivities_ConditionalNode235 is not None else set()
        
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
    def fuml_CompleteStructuredActivities_ConditionalNode(self):
        return self.__fuml_CompleteStructuredActivities_ConditionalNode

    @fuml_CompleteStructuredActivities_ConditionalNode.setter
    def fuml_CompleteStructuredActivities_ConditionalNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteStructuredActivities_ConditionalNode__fuml_CompleteStructuredActivities_ConditionalNode", None)
        self.__fuml_CompleteStructuredActivities_ConditionalNode = value if value is not None else set()
        
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
    def fuml_CompleteStructuredActivities_ConditionalNode235(self):
        return self.__fuml_CompleteStructuredActivities_ConditionalNode235

    @fuml_CompleteStructuredActivities_ConditionalNode235.setter
    def fuml_CompleteStructuredActivities_ConditionalNode235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteStructuredActivities_ConditionalNode__fuml_CompleteStructuredActivities_ConditionalNode235", None)
        self.__fuml_CompleteStructuredActivities_ConditionalNode235 = value if value is not None else set()
        
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
                    

class fuml_ExtraStructuredActivities_ExpansionRegion(StructuredActivityNode):

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
    def Activities258(self):
        return self.__Activities258

    @Activities258.setter
    def Activities258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_ExtraStructuredActivities_ExpansionRegion__Activities258", None)
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
                    

    @property
    def Activities255(self):
        return self.__Activities255

    @Activities255.setter
    def Activities255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_ExtraStructuredActivities_ExpansionRegion__Activities255", None)
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
                    

class fuml_CompleteStructuredActivities_LoopNode(StructuredActivityNode):

    def __init__(self, testedFirst: bool, fuml_CompleteStructuredActivities_LoopNode198: set["CompleteStructuredActivities_ExecutableNode"] = None, fuml_CompleteStructuredActivities_LoopNode200: set["BasicActions_OutputPin"] = None, fuml_CompleteStructuredActivities_LoopNode: "BasicActions_OutputPin" = None, fuml_CompleteStructuredActivities_LoopNode203: set["BasicActions_InputPin"] = None, fuml_CompleteStructuredActivities_LoopNode205: set["CompleteStructuredActivities_ExecutableNode"] = None, fuml_CompleteStructuredActivities_LoopNode208: set["BasicActions_OutputPin"] = None, fuml_CompleteStructuredActivities_LoopNode211: set["BasicActions_OutputPin"] = None, fuml_CompleteStructuredActivities_LoopNode214: set["CompleteStructuredActivities_ExecutableNode"] = None):
        self.testedFirst = testedFirst
        self.fuml_CompleteStructuredActivities_LoopNode198 = fuml_CompleteStructuredActivities_LoopNode198 if fuml_CompleteStructuredActivities_LoopNode198 is not None else set()
        self.fuml_CompleteStructuredActivities_LoopNode200 = fuml_CompleteStructuredActivities_LoopNode200 if fuml_CompleteStructuredActivities_LoopNode200 is not None else set()
        self.fuml_CompleteStructuredActivities_LoopNode = fuml_CompleteStructuredActivities_LoopNode
        self.fuml_CompleteStructuredActivities_LoopNode203 = fuml_CompleteStructuredActivities_LoopNode203 if fuml_CompleteStructuredActivities_LoopNode203 is not None else set()
        self.fuml_CompleteStructuredActivities_LoopNode205 = fuml_CompleteStructuredActivities_LoopNode205 if fuml_CompleteStructuredActivities_LoopNode205 is not None else set()
        self.fuml_CompleteStructuredActivities_LoopNode208 = fuml_CompleteStructuredActivities_LoopNode208 if fuml_CompleteStructuredActivities_LoopNode208 is not None else set()
        self.fuml_CompleteStructuredActivities_LoopNode211 = fuml_CompleteStructuredActivities_LoopNode211 if fuml_CompleteStructuredActivities_LoopNode211 is not None else set()
        self.fuml_CompleteStructuredActivities_LoopNode214 = fuml_CompleteStructuredActivities_LoopNode214 if fuml_CompleteStructuredActivities_LoopNode214 is not None else set()
        
    @property
    def testedFirst(self) -> bool:
        return self.__testedFirst

    @testedFirst.setter
    def testedFirst(self, testedFirst: bool):
        self.__testedFirst = testedFirst

    @property
    def fuml_CompleteStructuredActivities_LoopNode203(self):
        return self.__fuml_CompleteStructuredActivities_LoopNode203

    @fuml_CompleteStructuredActivities_LoopNode203.setter
    def fuml_CompleteStructuredActivities_LoopNode203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteStructuredActivities_LoopNode__fuml_CompleteStructuredActivities_LoopNode203", None)
        self.__fuml_CompleteStructuredActivities_LoopNode203 = value if value is not None else set()
        
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
    def fuml_CompleteStructuredActivities_LoopNode208(self):
        return self.__fuml_CompleteStructuredActivities_LoopNode208

    @fuml_CompleteStructuredActivities_LoopNode208.setter
    def fuml_CompleteStructuredActivities_LoopNode208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteStructuredActivities_LoopNode__fuml_CompleteStructuredActivities_LoopNode208", None)
        self.__fuml_CompleteStructuredActivities_LoopNode208 = value if value is not None else set()
        
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
    def fuml_CompleteStructuredActivities_LoopNode211(self):
        return self.__fuml_CompleteStructuredActivities_LoopNode211

    @fuml_CompleteStructuredActivities_LoopNode211.setter
    def fuml_CompleteStructuredActivities_LoopNode211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteStructuredActivities_LoopNode__fuml_CompleteStructuredActivities_LoopNode211", None)
        self.__fuml_CompleteStructuredActivities_LoopNode211 = value if value is not None else set()
        
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
                    

    @property
    def fuml_CompleteStructuredActivities_LoopNode198(self):
        return self.__fuml_CompleteStructuredActivities_LoopNode198

    @fuml_CompleteStructuredActivities_LoopNode198.setter
    def fuml_CompleteStructuredActivities_LoopNode198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteStructuredActivities_LoopNode__fuml_CompleteStructuredActivities_LoopNode198", None)
        self.__fuml_CompleteStructuredActivities_LoopNode198 = value if value is not None else set()
        
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
    def fuml_CompleteStructuredActivities_LoopNode214(self):
        return self.__fuml_CompleteStructuredActivities_LoopNode214

    @fuml_CompleteStructuredActivities_LoopNode214.setter
    def fuml_CompleteStructuredActivities_LoopNode214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteStructuredActivities_LoopNode__fuml_CompleteStructuredActivities_LoopNode214", None)
        self.__fuml_CompleteStructuredActivities_LoopNode214 = value if value is not None else set()
        
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
    def fuml_CompleteStructuredActivities_LoopNode205(self):
        return self.__fuml_CompleteStructuredActivities_LoopNode205

    @fuml_CompleteStructuredActivities_LoopNode205.setter
    def fuml_CompleteStructuredActivities_LoopNode205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteStructuredActivities_LoopNode__fuml_CompleteStructuredActivities_LoopNode205", None)
        self.__fuml_CompleteStructuredActivities_LoopNode205 = value if value is not None else set()
        
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
    def fuml_CompleteStructuredActivities_LoopNode200(self):
        return self.__fuml_CompleteStructuredActivities_LoopNode200

    @fuml_CompleteStructuredActivities_LoopNode200.setter
    def fuml_CompleteStructuredActivities_LoopNode200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteStructuredActivities_LoopNode__fuml_CompleteStructuredActivities_LoopNode200", None)
        self.__fuml_CompleteStructuredActivities_LoopNode200 = value if value is not None else set()
        
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
    def fuml_CompleteStructuredActivities_LoopNode(self):
        return self.__fuml_CompleteStructuredActivities_LoopNode

    @fuml_CompleteStructuredActivities_LoopNode.setter
    def fuml_CompleteStructuredActivities_LoopNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_CompleteStructuredActivities_LoopNode__fuml_CompleteStructuredActivities_LoopNode", None)
        self.__fuml_CompleteStructuredActivities_LoopNode = value
        
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

class ObjectNode:

    pass
class fuml_ExtraStructuredActivities_ExpansionNode(ObjectNode):

    pass
class fuml_IntermediateActivities_ActivityParameterNode(ObjectNode):

    pass
class FinalNode:

    pass
class fuml_IntermediateActivities_ActivityFinalNode(FinalNode):

    pass
class IntermediateActivities_ObjectFlow:

    pass
class ActivityNode:

    pass
class fuml_CompleteStructuredActivities_ExecutableNode(ActivityNode):

    pass
class fuml_IntermediateActivities_ControlNode(ActivityNode):

    pass
class ControlNode:

    pass
class fuml_IntermediateActivities_FinalNode(ControlNode):

    pass
class fuml_IntermediateActivities_InitialNode(ControlNode):

    pass
class fuml_IntermediateActivities_ForkNode(ControlNode):

    pass
class fuml_IntermediateActivities_DecisionNode(ControlNode):

    pass
class fuml_IntermediateActivities_JoinNode(ControlNode):

    pass
class fuml_IntermediateActivities_MergeNode(ControlNode):

    pass
class CompleteStructuredActivities_ExecutableNode:

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
class fuml_IntermediateActivities_ControlFlow(ActivityEdge):

    pass
class fuml_IntermediateActivities_ObjectFlow(ActivityEdge):

    pass
class BehavioredClassifier:

    pass
class fuml_Kernel_Class(BehavioredClassifier):

    def __init__(self, active: bool, fuml_Kernel_Class155: set["Communications_Reception"] = None, fuml_Kernel_Class157: set["Kernel_Classifier"] = None, Classes148: set["Kernel_Property"] = None, Classes151: set["Kernel_Operation"] = None, fuml_Kernel_Class: set["Kernel_Class"] = None):
        self.active = active
        self.fuml_Kernel_Class155 = fuml_Kernel_Class155 if fuml_Kernel_Class155 is not None else set()
        self.fuml_Kernel_Class157 = fuml_Kernel_Class157 if fuml_Kernel_Class157 is not None else set()
        self.Classes148 = Classes148 if Classes148 is not None else set()
        self.Classes151 = Classes151 if Classes151 is not None else set()
        self.fuml_Kernel_Class = fuml_Kernel_Class if fuml_Kernel_Class is not None else set()
        
    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def Classes151(self):
        return self.__Classes151

    @Classes151.setter
    def Classes151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Class__Classes151", None)
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
    def fuml_Kernel_Class155(self):
        return self.__fuml_Kernel_Class155

    @fuml_Kernel_Class155.setter
    def fuml_Kernel_Class155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Class__fuml_Kernel_Class155", None)
        self.__fuml_Kernel_Class155 = value if value is not None else set()
        
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
    def fuml_Kernel_Class(self):
        return self.__fuml_Kernel_Class

    @fuml_Kernel_Class.setter
    def fuml_Kernel_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Class__fuml_Kernel_Class", None)
        self.__fuml_Kernel_Class = value if value is not None else set()
        
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
    def fuml_Kernel_Class157(self):
        return self.__fuml_Kernel_Class157

    @fuml_Kernel_Class157.setter
    def fuml_Kernel_Class157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Class__fuml_Kernel_Class157", None)
        self.__fuml_Kernel_Class157 = value if value is not None else set()
        
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
                    

    @property
    def Classes148(self):
        return self.__Classes148

    @Classes148.setter
    def Classes148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Class__Classes148", None)
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
                    

class Kernel_Enumeration:

    pass
class InstanceSpecification:

    pass
class fuml_Kernel_EnumerationLiteral(InstanceSpecification):

    pass
class Kernel_EnumerationLiteral:

    pass
class DataType:

    pass
class fuml_Kernel_Enumeration(DataType):

    pass
class fuml_Kernel_PrimitiveType(DataType):

    pass
class Communications_Reception:

    pass
class ValueSpecification:

    pass
class fuml_Kernel_InstanceValue(ValueSpecification):

    pass
class Kernel_InstanceSpecification:

    pass
class Kernel_StructuralFeature:

    pass
class Kernel_Slot:

    pass
class fuml_Kernel_LiteralSpecification(ValueSpecification):

    pass
class LiteralSpecification:

    pass
class fuml_Kernel_LiteralInteger(LiteralSpecification):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class fuml_Kernel_LiteralString(LiteralSpecification):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class fuml_Kernel_LiteralUnlimitedNatural(LiteralSpecification):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class fuml_Kernel_LiteralNull(LiteralSpecification):

    pass
class fuml_Kernel_LiteralBoolean(LiteralSpecification):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class Feature:

    pass
class Kernel_Operation:

    pass
class fuml_Kernel_BehavioralFeature(Feature):

    def __init__(self, abstract: bool, concurrency: str, fuml_Kernel_BehavioralFeature: set["Kernel_Parameter"] = None, CommonBehaviors: set["BasicBehaviors_Behavior"] = None):
        self.abstract = abstract
        self.concurrency = concurrency
        self.fuml_Kernel_BehavioralFeature = fuml_Kernel_BehavioralFeature if fuml_Kernel_BehavioralFeature is not None else set()
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
        old_value = getattr(self, f"_fuml_Kernel_BehavioralFeature__CommonBehaviors", None)
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
    def fuml_Kernel_BehavioralFeature(self):
        return self.__fuml_Kernel_BehavioralFeature

    @fuml_Kernel_BehavioralFeature.setter
    def fuml_Kernel_BehavioralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_BehavioralFeature__fuml_Kernel_BehavioralFeature", None)
        self.__fuml_Kernel_BehavioralFeature = value if value is not None else set()
        
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
class Kernel_Association:

    pass
class StructuralFeature:

    pass
class fuml_Kernel_Property(StructuralFeature):

    def __init__(self, derived: bool, derivedUnion: bool, aggregation: str, composite: bool, Classes92: "Kernel_DataType" = None, Classes95: "Kernel_Class" = None, fuml_Kernel_Property: "Kernel_Property" = None, Classes86: "Kernel_Association" = None, Classes89: "Kernel_Association" = None):
        self.derived = derived
        self.derivedUnion = derivedUnion
        self.aggregation = aggregation
        self.composite = composite
        self.Classes92 = Classes92
        self.Classes95 = Classes95
        self.fuml_Kernel_Property = fuml_Kernel_Property
        self.Classes86 = Classes86
        self.Classes89 = Classes89
        
    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

    @property
    def composite(self) -> bool:
        return self.__composite

    @composite.setter
    def composite(self, composite: bool):
        self.__composite = composite

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
    def Classes86(self):
        return self.__Classes86

    @Classes86.setter
    def Classes86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Property__Classes86", None)
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

    @property
    def Classes92(self):
        return self.__Classes92

    @Classes92.setter
    def Classes92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Property__Classes92", None)
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
    def Classes89(self):
        return self.__Classes89

    @Classes89.setter
    def Classes89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Property__Classes89", None)
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
    def fuml_Kernel_Property(self):
        return self.__fuml_Kernel_Property

    @fuml_Kernel_Property.setter
    def fuml_Kernel_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Property__fuml_Kernel_Property", None)
        self.__fuml_Kernel_Property = value
        
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
        old_value = getattr(self, f"_fuml_Kernel_Property__Classes95", None)
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

class Kernel_Class:

    pass
class Kernel_DataType:

    pass
class Kernel_Generalization:

    pass
class Kernel_RedefinableElement:

    pass
class Kernel_Classifier:

    pass
class RedefinableElement:

    pass
class fuml_IntermediateActivities_ActivityEdge(RedefinableElement):

    pass
class fuml_IntermediateActivities_ActivityNode(RedefinableElement):

    pass
class fuml_Kernel_Feature(RedefinableElement):

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
        old_value = getattr(self, f"_fuml_Kernel_Feature__Classes61", None)
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
class fuml_IntermediateActivities_ObjectNode(Kernel_TypedElement, IntermediateActivities_ActivityNode):

    pass
class Kernel_MultiplicityElement:

    pass
class fuml_Kernel_Parameter(Kernel_TypedElement, Kernel_MultiplicityElement):

    def __init__(self, direction: str):
        self.direction = direction
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

class fuml_BasicActions_Pin(IntermediateActivities_ObjectNode, Kernel_MultiplicityElement):

    pass
class Kernel_Feature:

    pass
class fuml_Kernel_StructuralFeature(Kernel_Feature, Kernel_TypedElement, Kernel_MultiplicityElement):

    def __init__(self, readOnly: bool, Syntax71: "fuml_Kernel_Classifier"):
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
class fuml_Kernel_Comment:

    def __init__(self, body: str, fuml_Kernel_Comment: set["Kernel_Element"] = None):
        self.body = body
        self.fuml_Kernel_Comment = fuml_Kernel_Comment if fuml_Kernel_Comment is not None else set()
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def fuml_Kernel_Comment(self):
        return self.__fuml_Kernel_Comment

    @fuml_Kernel_Comment.setter
    def fuml_Kernel_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Comment__fuml_Kernel_Comment", None)
        self.__fuml_Kernel_Comment = value if value is not None else set()
        
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
class fuml_Kernel_Element(ABC):

    pass
class Kernel_Namespace:

    pass
class fuml_Kernel_Package(Kernel_Namespace, Kernel_PackageableElement):

    pass
class Element:

    pass
class fuml_Kernel_Generalization(Element):

    def __init__(self, substitutable: bool, fuml_Kernel_Generalization: "Kernel_Classifier" = None, Classes83: "Kernel_Classifier" = None):
        self.substitutable = substitutable
        self.fuml_Kernel_Generalization = fuml_Kernel_Generalization
        self.Classes83 = Classes83
        
    @property
    def substitutable(self) -> bool:
        return self.__substitutable

    @substitutable.setter
    def substitutable(self, substitutable: bool):
        self.__substitutable = substitutable

    @property
    def Classes83(self):
        return self.__Classes83

    @Classes83.setter
    def Classes83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Generalization__Classes83", None)
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

    @property
    def fuml_Kernel_Generalization(self):
        return self.__fuml_Kernel_Generalization

    @fuml_Kernel_Generalization.setter
    def fuml_Kernel_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Generalization__fuml_Kernel_Generalization", None)
        self.__fuml_Kernel_Generalization = value
        
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

class fuml_Kernel_ElementImport(Element):

    def __init__(self, visibility: str, alias: str, fuml_Kernel_ElementImport: "Kernel_PackageableElement" = None, Classes40: "Kernel_Namespace" = None):
        self.visibility = visibility
        self.alias = alias
        self.fuml_Kernel_ElementImport = fuml_Kernel_ElementImport
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
    def Classes40(self):
        return self.__Classes40

    @Classes40.setter
    def Classes40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_ElementImport__Classes40", None)
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

    @property
    def fuml_Kernel_ElementImport(self):
        return self.__fuml_Kernel_ElementImport

    @fuml_Kernel_ElementImport.setter
    def fuml_Kernel_ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_ElementImport__fuml_Kernel_ElementImport", None)
        self.__fuml_Kernel_ElementImport = value
        
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

class fuml_Kernel_Slot(Element):

    pass
class fuml_Kernel_PackageImport(Element):

    def __init__(self, visibility: str, fuml_Kernel_PackageImport: "Kernel_Package" = None, Classes44: "Kernel_Namespace" = None):
        self.visibility = visibility
        self.fuml_Kernel_PackageImport = fuml_Kernel_PackageImport
        self.Classes44 = Classes44
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def fuml_Kernel_PackageImport(self):
        return self.__fuml_Kernel_PackageImport

    @fuml_Kernel_PackageImport.setter
    def fuml_Kernel_PackageImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_PackageImport__fuml_Kernel_PackageImport", None)
        self.__fuml_Kernel_PackageImport = value
        
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
        old_value = getattr(self, f"_fuml_Kernel_PackageImport__Classes44", None)
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

class fuml_IntermediateActions_LinkEndData(Element):

    pass
class fuml_Kernel_MultiplicityElement(Element):

    def __init__(self, lower: int, ordered: bool, unique: bool, upper: int, fuml_Kernel_MultiplicityElement: "Kernel_ValueSpecification" = None, fuml_Kernel_MultiplicityElement115: "Kernel_ValueSpecification" = None):
        self.lower = lower
        self.ordered = ordered
        self.unique = unique
        self.upper = upper
        self.fuml_Kernel_MultiplicityElement = fuml_Kernel_MultiplicityElement
        self.fuml_Kernel_MultiplicityElement115 = fuml_Kernel_MultiplicityElement115
        
    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

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
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def fuml_Kernel_MultiplicityElement(self):
        return self.__fuml_Kernel_MultiplicityElement

    @fuml_Kernel_MultiplicityElement.setter
    def fuml_Kernel_MultiplicityElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_MultiplicityElement__fuml_Kernel_MultiplicityElement", None)
        self.__fuml_Kernel_MultiplicityElement = value
        
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

    @property
    def fuml_Kernel_MultiplicityElement115(self):
        return self.__fuml_Kernel_MultiplicityElement115

    @fuml_Kernel_MultiplicityElement115.setter
    def fuml_Kernel_MultiplicityElement115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_MultiplicityElement__fuml_Kernel_MultiplicityElement115", None)
        self.__fuml_Kernel_MultiplicityElement115 = value
        
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

class fuml_CompleteStructuredActivities_Clause(Element):

    pass
class fuml_Kernel_NamedElement(Element):

    def __init__(self, name: str, visibility: str, qualifiedName: str, Classes15: "Kernel_Namespace" = None):
        self.name = name
        self.visibility = visibility
        self.qualifiedName = qualifiedName
        self.Classes15 = Classes15
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

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
    def Classes15(self):
        return self.__Classes15

    @Classes15.setter
    def Classes15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_NamedElement__Classes15", None)
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
class fuml_Kernel_Classifier(Kernel_Namespace, Kernel_Type):

    def __init__(self, abstract: bool, finalSpecialization: bool, Classes70: set["Kernel_Feature"] = None, fuml_Kernel_Classifier: set["Kernel_NamedElement"] = None, Classes67: set["Kernel_Generalization"] = None, fuml_Kernel_Classifier75: set["Kernel_Property"] = None, fuml_Kernel_Classifier78: set["Kernel_Classifier"] = None, Kernel_Type127: "fuml_Kernel_Operation", Kernel_Type100: "fuml_Kernel_Association", Syntax50: "fuml_Kernel_Package", Kernel_Type: "fuml_Kernel_TypedElement", Syntax41: "fuml_Kernel_ElementImport", Syntax16: "fuml_Kernel_NamedElement", Syntax45: "fuml_Kernel_PackageImport"):
        self.abstract = abstract
        self.finalSpecialization = finalSpecialization
        self.Classes70 = Classes70 if Classes70 is not None else set()
        self.fuml_Kernel_Classifier = fuml_Kernel_Classifier if fuml_Kernel_Classifier is not None else set()
        self.Classes67 = Classes67 if Classes67 is not None else set()
        self.fuml_Kernel_Classifier75 = fuml_Kernel_Classifier75 if fuml_Kernel_Classifier75 is not None else set()
        self.fuml_Kernel_Classifier78 = fuml_Kernel_Classifier78 if fuml_Kernel_Classifier78 is not None else set()
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def finalSpecialization(self) -> bool:
        return self.__finalSpecialization

    @finalSpecialization.setter
    def finalSpecialization(self, finalSpecialization: bool):
        self.__finalSpecialization = finalSpecialization

    @property
    def Classes70(self):
        return self.__Classes70

    @Classes70.setter
    def Classes70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Classifier__Classes70", None)
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
    def fuml_Kernel_Classifier(self):
        return self.__fuml_Kernel_Classifier

    @fuml_Kernel_Classifier.setter
    def fuml_Kernel_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Classifier__fuml_Kernel_Classifier", None)
        self.__fuml_Kernel_Classifier = value if value is not None else set()
        
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
    def Classes67(self):
        return self.__Classes67

    @Classes67.setter
    def Classes67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Classifier__Classes67", None)
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
    def fuml_Kernel_Classifier75(self):
        return self.__fuml_Kernel_Classifier75

    @fuml_Kernel_Classifier75.setter
    def fuml_Kernel_Classifier75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Classifier__fuml_Kernel_Classifier75", None)
        self.__fuml_Kernel_Classifier75 = value if value is not None else set()
        
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
    def fuml_Kernel_Classifier78(self):
        return self.__fuml_Kernel_Classifier78

    @fuml_Kernel_Classifier78.setter
    def fuml_Kernel_Classifier78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Classifier__fuml_Kernel_Classifier78", None)
        self.__fuml_Kernel_Classifier78 = value if value is not None else set()
        
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
class fuml_Kernel_ValueSpecification(TypedElement):

    pass
class BehavioralFeature:

    pass
class fuml_Kernel_Operation(BehavioralFeature):

    def __init__(self, lower: int, upper: int, query: bool, ordered: bool, unique: bool, Classes122: "Kernel_Class" = None, fuml_Kernel_Operation: set["Kernel_Operation"] = None, fuml_Kernel_Operation126: "Kernel_Type" = None):
        self.lower = lower
        self.upper = upper
        self.query = query
        self.ordered = ordered
        self.unique = unique
        self.Classes122 = Classes122
        self.fuml_Kernel_Operation = fuml_Kernel_Operation if fuml_Kernel_Operation is not None else set()
        self.fuml_Kernel_Operation126 = fuml_Kernel_Operation126
        
    @property
    def query(self) -> bool:
        return self.__query

    @query.setter
    def query(self, query: bool):
        self.__query = query

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
    def fuml_Kernel_Operation126(self):
        return self.__fuml_Kernel_Operation126

    @fuml_Kernel_Operation126.setter
    def fuml_Kernel_Operation126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Operation__fuml_Kernel_Operation126", None)
        self.__fuml_Kernel_Operation126 = value
        
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
        old_value = getattr(self, f"_fuml_Kernel_Operation__Classes122", None)
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

    @property
    def fuml_Kernel_Operation(self):
        return self.__fuml_Kernel_Operation

    @fuml_Kernel_Operation.setter
    def fuml_Kernel_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Operation__fuml_Kernel_Operation", None)
        self.__fuml_Kernel_Operation = value if value is not None else set()
        
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
                    

class fuml_Communications_Reception(BehavioralFeature):

    pass
class Event:

    pass
class fuml_Communications_MessageEvent(Event):

    pass
class Communications_Signal:

    pass
class MessageEvent:

    pass
class fuml_Communications_SignalEvent(MessageEvent):

    pass
class Kernel_Property:

    pass
class PackageableElement:

    pass
class fuml_Kernel_Type(PackageableElement):

    pass
class fuml_Communications_Event(PackageableElement):

    pass
class Communications_Event:

    pass
class NamedElement:

    pass
class fuml_Kernel_Namespace(NamedElement):

    pass
class fuml_Kernel_RedefinableElement(NamedElement):

    def __init__(self, leaf: bool, fuml_Kernel_RedefinableElement: set["Kernel_RedefinableElement"] = None, fuml_Kernel_RedefinableElement65: set["Kernel_Classifier"] = None):
        self.leaf = leaf
        self.fuml_Kernel_RedefinableElement = fuml_Kernel_RedefinableElement if fuml_Kernel_RedefinableElement is not None else set()
        self.fuml_Kernel_RedefinableElement65 = fuml_Kernel_RedefinableElement65 if fuml_Kernel_RedefinableElement65 is not None else set()
        
    @property
    def leaf(self) -> bool:
        return self.__leaf

    @leaf.setter
    def leaf(self, leaf: bool):
        self.__leaf = leaf

    @property
    def fuml_Kernel_RedefinableElement65(self):
        return self.__fuml_Kernel_RedefinableElement65

    @fuml_Kernel_RedefinableElement65.setter
    def fuml_Kernel_RedefinableElement65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_RedefinableElement__fuml_Kernel_RedefinableElement65", None)
        self.__fuml_Kernel_RedefinableElement65 = value if value is not None else set()
        
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
    def fuml_Kernel_RedefinableElement(self):
        return self.__fuml_Kernel_RedefinableElement

    @fuml_Kernel_RedefinableElement.setter
    def fuml_Kernel_RedefinableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_RedefinableElement__fuml_Kernel_RedefinableElement", None)
        self.__fuml_Kernel_RedefinableElement = value if value is not None else set()
        
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
                    

class fuml_Kernel_PackageableElement(NamedElement):

    pass
class fuml_Kernel_TypedElement(NamedElement):

    pass
class fuml_Kernel_InstanceSpecification(NamedElement):

    pass
class fuml_Communications_Trigger(NamedElement):

    pass
class OpaqueBehavior:

    pass
class fuml_BasicBehaviors_FunctionBehavior(OpaqueBehavior):

    pass
class BasicBehaviors_Behavior:

    pass
class Classifier:

    pass
class fuml_Communications_Signal(Classifier):

    pass
class fuml_Kernel_Association(Classifier):

    def __init__(self, derived: bool, fuml_Kernel_Association: set["Kernel_Type"] = None, Classes102: set["Kernel_Property"] = None, fuml_Kernel_Association105: set["Kernel_Property"] = None, Classes108: set["Kernel_Property"] = None):
        self.derived = derived
        self.fuml_Kernel_Association = fuml_Kernel_Association if fuml_Kernel_Association is not None else set()
        self.Classes102 = Classes102 if Classes102 is not None else set()
        self.fuml_Kernel_Association105 = fuml_Kernel_Association105 if fuml_Kernel_Association105 is not None else set()
        self.Classes108 = Classes108 if Classes108 is not None else set()
        
    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def Classes102(self):
        return self.__Classes102

    @Classes102.setter
    def Classes102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Association__Classes102", None)
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
    def Classes108(self):
        return self.__Classes108

    @Classes108.setter
    def Classes108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Association__Classes108", None)
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
    def fuml_Kernel_Association(self):
        return self.__fuml_Kernel_Association

    @fuml_Kernel_Association.setter
    def fuml_Kernel_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Association__fuml_Kernel_Association", None)
        self.__fuml_Kernel_Association = value if value is not None else set()
        
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
    def fuml_Kernel_Association105(self):
        return self.__fuml_Kernel_Association105

    @fuml_Kernel_Association105.setter
    def fuml_Kernel_Association105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_Kernel_Association__fuml_Kernel_Association105", None)
        self.__fuml_Kernel_Association105 = value if value is not None else set()
        
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
                    

class fuml_Kernel_DataType(Classifier):

    pass
class fuml_BasicBehaviors_BehavioredClassifier(Classifier):

    pass
class BasicBehaviors_BehavioredClassifier:

    pass
class Kernel_Parameter:

    pass
class Kernel_BehavioralFeature:

    pass
class Class:

    pass
class fuml_BasicBehaviors_Behavior(Class):

    def __init__(self, reentrant: bool, Classes: "Kernel_BehavioralFeature" = None, fuml_BasicBehaviors_Behavior: set["Kernel_Parameter"] = None, fuml_BasicBehaviors_Behavior3: "BasicBehaviors_BehavioredClassifier" = None):
        self.reentrant = reentrant
        self.Classes = Classes
        self.fuml_BasicBehaviors_Behavior = fuml_BasicBehaviors_Behavior if fuml_BasicBehaviors_Behavior is not None else set()
        self.fuml_BasicBehaviors_Behavior3 = fuml_BasicBehaviors_Behavior3
        
    @property
    def reentrant(self) -> bool:
        return self.__reentrant

    @reentrant.setter
    def reentrant(self, reentrant: bool):
        self.__reentrant = reentrant

    @property
    def Classes(self):
        return self.__Classes

    @Classes.setter
    def Classes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_BasicBehaviors_Behavior__Classes", None)
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

    @property
    def fuml_BasicBehaviors_Behavior3(self):
        return self.__fuml_BasicBehaviors_Behavior3

    @fuml_BasicBehaviors_Behavior3.setter
    def fuml_BasicBehaviors_Behavior3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_BasicBehaviors_Behavior__fuml_BasicBehaviors_Behavior3", None)
        self.__fuml_BasicBehaviors_Behavior3 = value
        
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
    def fuml_BasicBehaviors_Behavior(self):
        return self.__fuml_BasicBehaviors_Behavior

    @fuml_BasicBehaviors_Behavior.setter
    def fuml_BasicBehaviors_Behavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_BasicBehaviors_Behavior__fuml_BasicBehaviors_Behavior", None)
        self.__fuml_BasicBehaviors_Behavior = value if value is not None else set()
        
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
class fuml_IntermediateActivities_Activity(Behavior):

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
    def Activities176(self):
        return self.__Activities176

    @Activities176.setter
    def Activities176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_IntermediateActivities_Activity__Activities176", None)
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
                    

    @property
    def Activities173(self):
        return self.__Activities173

    @Activities173.setter
    def Activities173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fuml_IntermediateActivities_Activity__Activities173", None)
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
                    

class fuml_BasicBehaviors_OpaqueBehavior(Behavior):

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
