from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class OperationKind(Enum):
    and = "and"
    or = "or"
    not = "not"
    plus = "plus"
    minus = "minus"
class PortCategory(Enum):
    data = "data"
    event = "event"
    eventData = "eventData"
class FlowKind(Enum):
    source = "source"
    path = "path"
    sink = "sink"
class ComponentCategory(Enum):
    system = "system"
    thread = "thread"
    threadGroup = "threadGroup"
    virtualBus = "virtualBus"
    virtualProcessor = "virtualProcessor"
    abstract = "abstract"
    bus = "bus"
    data = "data"
    device = "device"
    memory = "memory"
    process = "process"
    processor = "processor"
    subprogram = "subprogram"
    subprogramGroup = "subprogramGroup"
class AccessType(Enum):
    provides = "provides"
    requires = "requires"
class AccessCategory(Enum):
    bus = "bus"
    data = "data"
    subprogram = "subprogram"
    subprogramGroup = "subprogramGroup"
class DirectionType(Enum):
    in = "in"
    out = "out"
    inOut = "inOut"


############################################
# Definition of Classes
############################################

class EnumerationType:

    pass
class aadl2_UnitsType(EnumerationType):

    pass
class NumberType:

    pass
class aadl2_AadlReal(NumberType):

    pass
class aadl2_AadlInteger(NumberType):

    pass
class NonListType:

    pass
class aadl2_AadlString(NonListType):

    pass
class aadl2_NumberType(NonListType):

    pass
class aadl2_RangeType(NonListType):

    pass
class aadl2_ClassifierType(NonListType):

    pass
class aadl2_ReferenceType(NonListType):

    pass
class aadl2_AadlBoolean(NonListType):

    pass
class PropertyType:

    pass
class aadl2_ListType(PropertyType):

    pass
class aadl2_NonListType(PropertyType):

    pass
class NumberValue:

    pass
class aadl2_RealLiteral(NumberValue):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class aadl2_IntegerLiteral(NumberValue):

    def __init__(self, base: str, value: str):
        self.base = base
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def base(self) -> str:
        return self.__base

    @base.setter
    def base(self, base: str):
        self.__base = base

class ContainedNamedElement:

    pass
class PropertyValue:

    pass
class aadl2_NamedValue(PropertyValue):

    pass
class aadl2_RangeValue(PropertyValue):

    pass
class aadl2_BooleanLiteral(PropertyValue):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class aadl2_ReferenceValue(PropertyValue, ContainedNamedElement):

    pass
class aadl2_RecordValue(PropertyValue):

    pass
class aadl2_ComputedValue(PropertyValue):

    def __init__(self, function: str):
        self.function = function
        
    @property
    def function(self) -> str:
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

class aadl2_StringLiteral(PropertyValue):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class EnumerationLiteral:

    pass
class aadl2_UnitLiteral(EnumerationLiteral):

    def __init__(self, aadl2_UnitLiteral: "aadl2_NumberValue" = None, aadl2_UnitLiteral785: "aadl2_UnitLiteral" = None, aadl2_UnitLiteral783: "aadl2_UnitLiteral" = None, aadl2_UnitLiteral787: "aadl2_NumberValue" = None):
        self.aadl2_UnitLiteral = aadl2_UnitLiteral
        self.aadl2_UnitLiteral785 = aadl2_UnitLiteral785
        self.aadl2_UnitLiteral783 = aadl2_UnitLiteral783
        self.aadl2_UnitLiteral787 = aadl2_UnitLiteral787
        
    @property
    def aadl2_UnitLiteral783(self):
        return self.__aadl2_UnitLiteral783

    @aadl2_UnitLiteral783.setter
    def aadl2_UnitLiteral783(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_UnitLiteral__aadl2_UnitLiteral783", None)
        self.__aadl2_UnitLiteral783 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_UnitLiteral785"):
                opp_val = getattr(old_value, "aadl2_UnitLiteral785", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_UnitLiteral785", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_UnitLiteral785"):
                opp_val = getattr(value, "aadl2_UnitLiteral785", None)
                setattr(value, "aadl2_UnitLiteral785", self)

    @property
    def aadl2_UnitLiteral(self):
        return self.__aadl2_UnitLiteral

    @aadl2_UnitLiteral.setter
    def aadl2_UnitLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_UnitLiteral__aadl2_UnitLiteral", None)
        self.__aadl2_UnitLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_NumberValue"):
                opp_val = getattr(old_value, "aadl2_NumberValue", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_NumberValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_NumberValue"):
                opp_val = getattr(value, "aadl2_NumberValue", None)
                setattr(value, "aadl2_NumberValue", self)

    @property
    def aadl2_UnitLiteral785(self):
        return self.__aadl2_UnitLiteral785

    @aadl2_UnitLiteral785.setter
    def aadl2_UnitLiteral785(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_UnitLiteral__aadl2_UnitLiteral785", None)
        self.__aadl2_UnitLiteral785 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_UnitLiteral783"):
                opp_val = getattr(old_value, "aadl2_UnitLiteral783", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_UnitLiteral783", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_UnitLiteral783"):
                opp_val = getattr(value, "aadl2_UnitLiteral783", None)
                setattr(value, "aadl2_UnitLiteral783", self)

    @property
    def aadl2_UnitLiteral787(self):
        return self.__aadl2_UnitLiteral787

    @aadl2_UnitLiteral787.setter
    def aadl2_UnitLiteral787(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_UnitLiteral__aadl2_UnitLiteral787", None)
        self.__aadl2_UnitLiteral787 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_NumberValue788"):
                opp_val = getattr(old_value, "aadl2_NumberValue788", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_NumberValue788", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_NumberValue788"):
                opp_val = getattr(value, "aadl2_NumberValue788", None)
                setattr(value, "aadl2_NumberValue788", self)

    def getAbsoluteFactor(self, target: str) -> str:
        # TODO: Implement getAbsoluteFactor method
        pass

class aadl2_NumberValue(PropertyValue):

    def __init__(self, aadl2_NumberValue: "aadl2_UnitLiteral" = None, aadl2_NumberValue788: "aadl2_UnitLiteral" = None):
        self.aadl2_NumberValue = aadl2_NumberValue
        self.aadl2_NumberValue788 = aadl2_NumberValue788
        
    @property
    def aadl2_NumberValue788(self):
        return self.__aadl2_NumberValue788

    @aadl2_NumberValue788.setter
    def aadl2_NumberValue788(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_NumberValue__aadl2_NumberValue788", None)
        self.__aadl2_NumberValue788 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_UnitLiteral787"):
                opp_val = getattr(old_value, "aadl2_UnitLiteral787", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_UnitLiteral787", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_UnitLiteral787"):
                opp_val = getattr(value, "aadl2_UnitLiteral787", None)
                setattr(value, "aadl2_UnitLiteral787", self)

    @property
    def aadl2_NumberValue(self):
        return self.__aadl2_NumberValue

    @aadl2_NumberValue.setter
    def aadl2_NumberValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_NumberValue__aadl2_NumberValue", None)
        self.__aadl2_NumberValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_UnitLiteral"):
                opp_val = getattr(old_value, "aadl2_UnitLiteral", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_UnitLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_UnitLiteral"):
                opp_val = getattr(value, "aadl2_UnitLiteral", None)
                setattr(value, "aadl2_UnitLiteral", self)

    def getScaledValue(self, target: str) -> str:
        # TODO: Implement getScaledValue method
        pass

    def getScaledValue(self, target: str) -> str:
        # TODO: Implement getScaledValue method
        pass

    def getScaledValue(self) -> str:
        # TODO: Implement getScaledValue method
        pass

class PropertyExpression:

    pass
class aadl2_Operation(PropertyExpression):

    def __init__(self, op: str, aadl2_Operation: set["aadl2_PropertyExpression"] = None):
        self.op = op
        self.aadl2_Operation = aadl2_Operation if aadl2_Operation is not None else set()
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def aadl2_Operation(self):
        return self.__aadl2_Operation

    @aadl2_Operation.setter
    def aadl2_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Operation__aadl2_Operation", None)
        self.__aadl2_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_PropertyExpression800"):
                    opp_val = getattr(item, "aadl2_PropertyExpression800", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_PropertyExpression800", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_PropertyExpression800"):
                    opp_val = getattr(item, "aadl2_PropertyExpression800", None)
                    
                    setattr(item, "aadl2_PropertyExpression800", self)
                    

class aadl2_ListValue(PropertyExpression):

    pass
class aadl2_PropertyValue(PropertyExpression):

    pass
class VirtualBusClassifier:

    pass
class VirtualProcessorClassifier:

    pass
class ThreadGroupClassifier:

    pass
class ThreadClassifier:

    pass
class ProcessClassifier:

    pass
class ProcessorClassifier:

    pass
class SubprogramGroupClassifier:

    pass
class SystemClassifier:

    pass
class SubprogramClassifier:

    pass
class MemoryClassifier:

    pass
class DeviceClassifier:

    pass
class BusClassifier:

    pass
class ComponentPrototype:

    pass
class DataClassifier:

    pass
class BehavioredImplementation:

    pass
class aadl2_ThreadImplementation(BehavioredImplementation, ThreadClassifier):

    pass
class aadl2_SubprogramImplementation(BehavioredImplementation, SubprogramClassifier):

    pass
class Processor:

    pass
class Device:

    pass
class Memory:

    pass
class Process:

    pass
class System:

    pass
class Thread:

    pass
class ThreadSubcomponentType:

    pass
class aadl2_ThreadPrototype(ComponentPrototype, ThreadSubcomponentType):

    pass
class ThreadGroupSubcomponentType:

    pass
class aadl2_ThreadGroupPrototype(ComponentPrototype, ThreadGroupSubcomponentType):

    pass
class SystemSubcomponentType:

    pass
class aadl2_SystemPrototype(ComponentPrototype, SystemSubcomponentType):

    pass
class SubprogramSubcomponentType:

    pass
class aadl2_SubprogramPrototype(ComponentPrototype, SubprogramSubcomponentType):

    pass
class SubprogramGroupSubcomponentType:

    pass
class aadl2_SubprogramGroupPrototype(ComponentPrototype, SubprogramGroupSubcomponentType):

    pass
class ProcessSubcomponentType:

    pass
class aadl2_ProcessPrototype(ComponentPrototype, ProcessSubcomponentType):

    pass
class ProcessorSubcomponentType:

    pass
class aadl2_ProcessorPrototype(ProcessorSubcomponentType, ComponentPrototype):

    pass
class MemorySubcomponentType:

    pass
class aadl2_MemoryPrototype(ComponentPrototype, MemorySubcomponentType):

    pass
class DeviceSubcomponentType:

    pass
class aadl2_DevicePrototype(ComponentPrototype, DeviceSubcomponentType):

    pass
class DataSubcomponentType:

    pass
class aadl2_DataPrototype(ComponentPrototype, DataSubcomponentType):

    pass
class BusSubcomponentType:

    pass
class aadl2_BusPrototype(ComponentPrototype, BusSubcomponentType):

    pass
class AbstractSubcomponentType:

    pass
class ThreadGroup:

    pass
class VirtualBus:

    pass
class VirtualProcessor:

    pass
class VirtualProcessorSubcomponentType:

    pass
class aadl2_VirtualProcessorPrototype(ComponentPrototype, VirtualProcessorSubcomponentType):

    pass
class VirtualBusSubcomponentType:

    pass
class aadl2_VirtualBusPrototype(ComponentPrototype, VirtualBusSubcomponentType):

    pass
class aadl2_AbstractPrototype(VirtualBusSubcomponentType, SubprogramSubcomponentType, VirtualProcessorSubcomponentType, AbstractSubcomponentType, SubprogramGroupSubcomponentType, DeviceSubcomponentType, ThreadGroupSubcomponentType, ComponentPrototype, DataSubcomponentType, MemorySubcomponentType, SystemSubcomponentType, ProcessorSubcomponentType, BusSubcomponentType, ProcessSubcomponentType, ThreadSubcomponentType):

    pass
class BehavioralFeature:

    pass
class AbstractClassifier:

    pass
class aadl2_AbstractImplementation(BehavioredImplementation, AbstractClassifier):

    pass
class ComponentType:

    pass
class aadl2_BusType(ComponentType, BusClassifier):

    pass
class aadl2_ProcessType(ComponentType, ProcessClassifier):

    pass
class aadl2_VirtualProcessorType(ComponentType, VirtualProcessorClassifier):

    pass
class aadl2_ThreadGroupType(ComponentType, ThreadGroupClassifier):

    pass
class aadl2_VirtualBusType(ComponentType, VirtualBusClassifier):

    pass
class aadl2_ThreadType(ComponentType, ThreadClassifier):

    pass
class aadl2_SystemType(ComponentType, SystemClassifier):

    pass
class aadl2_DeviceType(DeviceClassifier, ComponentType):

    pass
class aadl2_ProcessorType(ComponentType, ProcessorClassifier):

    pass
class aadl2_MemoryType(ComponentType, MemoryClassifier):

    pass
class ComponentImplementation:

    pass
class aadl2_DeviceImplementation(DeviceClassifier, ComponentImplementation):

    pass
class aadl2_ThreadGroupImplementation(ComponentImplementation, ThreadGroupClassifier):

    pass
class aadl2_MemoryImplementation(ComponentImplementation, MemoryClassifier):

    pass
class aadl2_VirtualProcessorImplementation(ComponentImplementation, VirtualProcessorClassifier):

    pass
class aadl2_ProcessImplementation(ComponentImplementation, ProcessClassifier):

    pass
class aadl2_ProcessorImplementation(ComponentImplementation, ProcessorClassifier):

    pass
class aadl2_SystemImplementation(ComponentImplementation, SystemClassifier):

    pass
class aadl2_SubprogramGroupImplementation(ComponentImplementation, SubprogramGroupClassifier):

    pass
class aadl2_VirtualBusImplementation(ComponentImplementation, VirtualBusClassifier):

    pass
class aadl2_DataImplementation(DataClassifier, ComponentImplementation):

    pass
class aadl2_BusImplementation(ComponentImplementation, BusClassifier):

    pass
class aadl2_BehavioredImplementation(ComponentImplementation):

    def __init__(self, aadl2_BehavioredImplementation: set["aadl2_SubprogramCall"] = None, aadl2_BehavioredImplementation394: set["aadl2_SubprogramCallSequence"] = None):
        self.aadl2_BehavioredImplementation = aadl2_BehavioredImplementation if aadl2_BehavioredImplementation is not None else set()
        self.aadl2_BehavioredImplementation394 = aadl2_BehavioredImplementation394 if aadl2_BehavioredImplementation394 is not None else set()
        
    @property
    def aadl2_BehavioredImplementation394(self):
        return self.__aadl2_BehavioredImplementation394

    @aadl2_BehavioredImplementation394.setter
    def aadl2_BehavioredImplementation394(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_BehavioredImplementation__aadl2_BehavioredImplementation394", None)
        self.__aadl2_BehavioredImplementation394 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_SubprogramCallSequence395"):
                    opp_val = getattr(item, "aadl2_SubprogramCallSequence395", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_SubprogramCallSequence395", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_SubprogramCallSequence395"):
                    opp_val = getattr(item, "aadl2_SubprogramCallSequence395", None)
                    
                    setattr(item, "aadl2_SubprogramCallSequence395", self)
                    

    @property
    def aadl2_BehavioredImplementation(self):
        return self.__aadl2_BehavioredImplementation

    @aadl2_BehavioredImplementation.setter
    def aadl2_BehavioredImplementation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_BehavioredImplementation__aadl2_BehavioredImplementation", None)
        self.__aadl2_BehavioredImplementation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_SubprogramCall392"):
                    opp_val = getattr(item, "aadl2_SubprogramCall392", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_SubprogramCall392", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_SubprogramCall392"):
                    opp_val = getattr(item, "aadl2_SubprogramCall392", None)
                    
                    setattr(item, "aadl2_SubprogramCall392", self)
                    

    def subprogramCalls(self) -> str:
        # TODO: Implement subprogramCalls method
        pass

class FeaturePrototypeActual:

    pass
class aadl2_FeaturePrototypeReference(FeaturePrototypeActual):

    def __init__(self, direction: str, aadl2_FeaturePrototypeReference: "aadl2_FeaturePrototype" = None):
        self.direction = direction
        self.aadl2_FeaturePrototypeReference = aadl2_FeaturePrototypeReference
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def aadl2_FeaturePrototypeReference(self):
        return self.__aadl2_FeaturePrototypeReference

    @aadl2_FeaturePrototypeReference.setter
    def aadl2_FeaturePrototypeReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeaturePrototypeReference__aadl2_FeaturePrototypeReference", None)
        self.__aadl2_FeaturePrototypeReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FeaturePrototype385"):
                opp_val = getattr(old_value, "aadl2_FeaturePrototype385", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FeaturePrototype385", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FeaturePrototype385"):
                opp_val = getattr(value, "aadl2_FeaturePrototype385", None)
                setattr(value, "aadl2_FeaturePrototype385", self)

class aadl2_PortSpecification(FeaturePrototypeActual):

    def __init__(self, direction: str, category: str, aadl2_PortSpecification: "aadl2_ComponentClassifier" = None, aadl2_PortSpecification382: "aadl2_ComponentPrototype" = None):
        self.direction = direction
        self.category = category
        self.aadl2_PortSpecification = aadl2_PortSpecification
        self.aadl2_PortSpecification382 = aadl2_PortSpecification382
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def aadl2_PortSpecification(self):
        return self.__aadl2_PortSpecification

    @aadl2_PortSpecification.setter
    def aadl2_PortSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PortSpecification__aadl2_PortSpecification", None)
        self.__aadl2_PortSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentClassifier380"):
                opp_val = getattr(old_value, "aadl2_ComponentClassifier380", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentClassifier380", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentClassifier380"):
                opp_val = getattr(value, "aadl2_ComponentClassifier380", None)
                setattr(value, "aadl2_ComponentClassifier380", self)

    @property
    def aadl2_PortSpecification382(self):
        return self.__aadl2_PortSpecification382

    @aadl2_PortSpecification382.setter
    def aadl2_PortSpecification382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PortSpecification__aadl2_PortSpecification382", None)
        self.__aadl2_PortSpecification382 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentPrototype383"):
                opp_val = getattr(old_value, "aadl2_ComponentPrototype383", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentPrototype383", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentPrototype383"):
                opp_val = getattr(value, "aadl2_ComponentPrototype383", None)
                setattr(value, "aadl2_ComponentPrototype383", self)

class aadl2_FeatureGroupPrototypeActual(FeaturePrototypeActual):

    pass
class PrototypeBinding:

    pass
class aadl2_FeatureGroupPrototypeBinding(PrototypeBinding):

    pass
class aadl2_ComponentPrototypeBinding(PrototypeBinding):

    pass
class aadl2_AccessSpecification(FeaturePrototypeActual):

    def __init__(self, kind: str, category: str, aadl2_AccessSpecification: "aadl2_ComponentClassifier" = None, aadl2_AccessSpecification377: "aadl2_ComponentPrototype" = None):
        self.kind = kind
        self.category = category
        self.aadl2_AccessSpecification = aadl2_AccessSpecification
        self.aadl2_AccessSpecification377 = aadl2_AccessSpecification377
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def aadl2_AccessSpecification(self):
        return self.__aadl2_AccessSpecification

    @aadl2_AccessSpecification.setter
    def aadl2_AccessSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_AccessSpecification__aadl2_AccessSpecification", None)
        self.__aadl2_AccessSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentClassifier375"):
                opp_val = getattr(old_value, "aadl2_ComponentClassifier375", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentClassifier375", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentClassifier375"):
                opp_val = getattr(value, "aadl2_ComponentClassifier375", None)
                setattr(value, "aadl2_ComponentClassifier375", self)

    @property
    def aadl2_AccessSpecification377(self):
        return self.__aadl2_AccessSpecification377

    @aadl2_AccessSpecification377.setter
    def aadl2_AccessSpecification377(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_AccessSpecification__aadl2_AccessSpecification377", None)
        self.__aadl2_AccessSpecification377 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentPrototype378"):
                opp_val = getattr(old_value, "aadl2_ComponentPrototype378", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentPrototype378", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentPrototype378"):
                opp_val = getattr(value, "aadl2_ComponentPrototype378", None)
                setattr(value, "aadl2_ComponentPrototype378", self)

class aadl2_FeaturePrototypeBinding(PrototypeBinding):

    pass
class ModelUnit:

    pass
class aadl2_AadlPackage(ModelUnit):

    pass
class PackageSection:

    pass
class aadl2_PrivatePackageSection(PackageSection):

    pass
class aadl2_PublicPackageSection(PackageSection):

    pass
class AnnexSubclause:

    pass
class aadl2_DefaultAnnexSubclause(AnnexSubclause):

    def __init__(self, sourceText: str, aadl2_DefaultAnnexSubclause: "aadl2_AnnexSubclause" = None):
        self.sourceText = sourceText
        self.aadl2_DefaultAnnexSubclause = aadl2_DefaultAnnexSubclause
        
    @property
    def sourceText(self) -> str:
        return self.__sourceText

    @sourceText.setter
    def sourceText(self, sourceText: str):
        self.__sourceText = sourceText

    @property
    def aadl2_DefaultAnnexSubclause(self):
        return self.__aadl2_DefaultAnnexSubclause

    @aadl2_DefaultAnnexSubclause.setter
    def aadl2_DefaultAnnexSubclause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_DefaultAnnexSubclause__aadl2_DefaultAnnexSubclause", None)
        self.__aadl2_DefaultAnnexSubclause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_AnnexSubclause325"):
                opp_val = getattr(old_value, "aadl2_AnnexSubclause325", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_AnnexSubclause325", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_AnnexSubclause325"):
                opp_val = getattr(value, "aadl2_AnnexSubclause325", None)
                setattr(value, "aadl2_AnnexSubclause325", self)

class ProcessorFeature:

    pass
class InternalFeature:

    pass
class AnnexLibrary:

    pass
class aadl2_DefaultAnnexLibrary(AnnexLibrary):

    def __init__(self, sourceText: str, aadl2_DefaultAnnexLibrary: "aadl2_AnnexLibrary" = None):
        self.sourceText = sourceText
        self.aadl2_DefaultAnnexLibrary = aadl2_DefaultAnnexLibrary
        
    @property
    def sourceText(self) -> str:
        return self.__sourceText

    @sourceText.setter
    def sourceText(self, sourceText: str):
        self.__sourceText = sourceText

    @property
    def aadl2_DefaultAnnexLibrary(self):
        return self.__aadl2_DefaultAnnexLibrary

    @aadl2_DefaultAnnexLibrary.setter
    def aadl2_DefaultAnnexLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_DefaultAnnexLibrary__aadl2_DefaultAnnexLibrary", None)
        self.__aadl2_DefaultAnnexLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_AnnexLibrary"):
                opp_val = getattr(old_value, "aadl2_AnnexLibrary", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_AnnexLibrary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_AnnexLibrary"):
                opp_val = getattr(value, "aadl2_AnnexLibrary", None)
                setattr(value, "aadl2_AnnexLibrary", self)

class Connection:

    pass
class Abstract:

    pass
class Subcomponent:

    pass
class aadl2_VirtualProcessorSubcomponent(VirtualProcessor, Subcomponent):

    pass
class aadl2_DeviceSubcomponent(Device, Subcomponent):

    pass
class aadl2_ThreadSubcomponent(Thread, Subcomponent):

    pass
class aadl2_MemorySubcomponent(Subcomponent, Memory):

    pass
class aadl2_ProcessSubcomponent(Process, Subcomponent):

    pass
class aadl2_ProcessorSubcomponent(Processor, Subcomponent):

    pass
class aadl2_ThreadGroupSubcomponent(ThreadGroup, Subcomponent):

    pass
class aadl2_VirtualBusSubcomponent(VirtualBus, Subcomponent):

    pass
class aadl2_SystemSubcomponent(System, Subcomponent):

    pass
class SubprogramGroup:

    pass
class TriggerPort:

    pass
class Subprogram:

    pass
class PortConnectionEnd:

    pass
class ParameterConnectionEnd:

    pass
class Data:

    pass
class Port:

    pass
class AccessConnectionEnd:

    pass
class aadl2_DataSubcomponent(Subcomponent, AccessConnectionEnd, ParameterConnectionEnd, PortConnectionEnd, Data):

    pass
class aadl2_SubprogramSubcomponent(Subprogram, AccessConnectionEnd, Subcomponent):

    pass
class Bus:

    pass
class aadl2_BusSubcomponent(AccessConnectionEnd, Bus, Subcomponent):

    pass
class Access:

    pass
class aadl2_EventPort(Port):

    pass
class aadl2_BusAccess(Bus, Access):

    pass
class aadl2_SubprogramAccess(Subprogram, Access):

    pass
class FeatureType:

    pass
class Feature:

    pass
class aadl2_Access(AccessConnectionEnd, Feature):

    def __init__(self, kind: str, category: str):
        self.kind = kind
        self.category = category
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

class aadl2_DirectedFeature(Feature):

    def __init__(self, direction: str):
        self.direction = direction
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

class aadl2_CallContext(ABC):

    pass
class aadl2_FeatureType(ABC):

    pass
class CallContext:

    pass
class aadl2_SubprogramGroupSubcomponent(AccessConnectionEnd, SubprogramGroup, CallContext, Subcomponent):

    pass
class aadl2_SubprogramGroupAccess(Access, SubprogramGroup, CallContext):

    pass
class aadl2_SubprogramGroupType(ComponentType, SubprogramGroupClassifier, CallContext):

    pass
class aadl2_SubprogramType(ComponentType, CallContext, SubprogramClassifier):

    pass
class aadl2_DataType(DataClassifier, ComponentType, CallContext):

    pass
class aadl2_AbstractType(ComponentType, AbstractClassifier, CallContext):

    pass
class FeatureGroupConnectionEnd:

    pass
class Context:

    pass
class aadl2_DataPort(Port, ParameterConnectionEnd, Context, Data):

    pass
class aadl2_EventDataPort(Port, ParameterConnectionEnd, Context, Data):

    pass
class aadl2_SubprogramCall(BehavioralFeature, Context):

    pass
class DirectedFeature:

    pass
class aadl2_Parameter(ParameterConnectionEnd, DirectedFeature, Context):

    pass
class aadl2_Port(PortConnectionEnd, TriggerPort, DirectedFeature):

    def __init__(self, category: str):
        self.category = category
        
    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

class Generalization:

    pass
class aadl2_GroupExtension(Generalization):

    pass
class EndToEndFlowElement:

    pass
class aadl2_FlowElement(EndToEndFlowElement):

    pass
class Flow:

    pass
class FlowFeature:

    pass
class Prototype:

    pass
class aadl2_FeaturePrototype(Prototype):

    def __init__(self, direction: str, aadl2_FeaturePrototype: "aadl2_AbstractFeature" = None, aadl2_FeaturePrototype252: "aadl2_ComponentClassifier" = None, aadl2_FeaturePrototype385: "aadl2_FeaturePrototypeReference" = None):
        self.direction = direction
        self.aadl2_FeaturePrototype = aadl2_FeaturePrototype
        self.aadl2_FeaturePrototype252 = aadl2_FeaturePrototype252
        self.aadl2_FeaturePrototype385 = aadl2_FeaturePrototype385
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def aadl2_FeaturePrototype(self):
        return self.__aadl2_FeaturePrototype

    @aadl2_FeaturePrototype.setter
    def aadl2_FeaturePrototype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeaturePrototype__aadl2_FeaturePrototype", None)
        self.__aadl2_FeaturePrototype = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_AbstractFeature250"):
                opp_val = getattr(old_value, "aadl2_AbstractFeature250", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_AbstractFeature250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_AbstractFeature250"):
                opp_val = getattr(value, "aadl2_AbstractFeature250", None)
                setattr(value, "aadl2_AbstractFeature250", self)

    @property
    def aadl2_FeaturePrototype252(self):
        return self.__aadl2_FeaturePrototype252

    @aadl2_FeaturePrototype252.setter
    def aadl2_FeaturePrototype252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeaturePrototype__aadl2_FeaturePrototype252", None)
        self.__aadl2_FeaturePrototype252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentClassifier253"):
                opp_val = getattr(old_value, "aadl2_ComponentClassifier253", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentClassifier253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentClassifier253"):
                opp_val = getattr(value, "aadl2_ComponentClassifier253", None)
                setattr(value, "aadl2_ComponentClassifier253", self)

    @property
    def aadl2_FeaturePrototype385(self):
        return self.__aadl2_FeaturePrototype385

    @aadl2_FeaturePrototype385.setter
    def aadl2_FeaturePrototype385(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeaturePrototype__aadl2_FeaturePrototype385", None)
        self.__aadl2_FeaturePrototype385 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FeaturePrototypeReference"):
                opp_val = getattr(old_value, "aadl2_FeaturePrototypeReference", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FeaturePrototypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FeaturePrototypeReference"):
                opp_val = getattr(value, "aadl2_FeaturePrototypeReference", None)
                setattr(value, "aadl2_FeaturePrototypeReference", self)

class aadl2_FeatureGroupPrototype(FeatureType, Prototype):

    pass
class ConnectionEnd:

    pass
class aadl2_FeatureGroupConnectionEnd(ConnectionEnd):

    pass
class aadl2_PortConnectionEnd(ConnectionEnd):

    pass
class aadl2_ParameterConnectionEnd(ConnectionEnd):

    pass
class aadl2_AccessConnectionEnd(ConnectionEnd):

    pass
class aadl2_FeatureConnectionEnd(ConnectionEnd):

    pass
class FlowElement:

    pass
class aadl2_DataAccess(Access, FlowElement, ParameterConnectionEnd, PortConnectionEnd, Data):

    pass
class ModalPath:

    pass
class aadl2_AbstractFeature(TriggerPort, DirectedFeature):

    pass
class aadl2_FeatureGroup(FeatureGroupConnectionEnd, Context, CallContext, DirectedFeature):

    def __init__(self, inverse: str, aadl2_FeatureGroup: "aadl2_ComponentType" = None, aadl2_FeatureGroup195: "aadl2_FeatureGroupPrototype" = None, aadl2_FeatureGroup191: "aadl2_FeatureType" = None, aadl2_FeatureGroup193: "aadl2_FeatureGroupType" = None, aadl2_FeatureGroup219: "aadl2_FeatureGroupType" = None):
        self.inverse = inverse
        self.aadl2_FeatureGroup = aadl2_FeatureGroup
        self.aadl2_FeatureGroup195 = aadl2_FeatureGroup195
        self.aadl2_FeatureGroup191 = aadl2_FeatureGroup191
        self.aadl2_FeatureGroup193 = aadl2_FeatureGroup193
        self.aadl2_FeatureGroup219 = aadl2_FeatureGroup219
        
    @property
    def inverse(self) -> str:
        return self.__inverse

    @inverse.setter
    def inverse(self, inverse: str):
        self.__inverse = inverse

    @property
    def aadl2_FeatureGroup191(self):
        return self.__aadl2_FeatureGroup191

    @aadl2_FeatureGroup191.setter
    def aadl2_FeatureGroup191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroup__aadl2_FeatureGroup191", None)
        self.__aadl2_FeatureGroup191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FeatureType"):
                opp_val = getattr(old_value, "aadl2_FeatureType", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FeatureType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FeatureType"):
                opp_val = getattr(value, "aadl2_FeatureType", None)
                setattr(value, "aadl2_FeatureType", self)

    @property
    def aadl2_FeatureGroup(self):
        return self.__aadl2_FeatureGroup

    @aadl2_FeatureGroup.setter
    def aadl2_FeatureGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroup__aadl2_FeatureGroup", None)
        self.__aadl2_FeatureGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentType156"):
                opp_val = getattr(old_value, "aadl2_ComponentType156", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentType156"):
                opp_val = getattr(value, "aadl2_ComponentType156", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentType156", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_FeatureGroup219(self):
        return self.__aadl2_FeatureGroup219

    @aadl2_FeatureGroup219.setter
    def aadl2_FeatureGroup219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroup__aadl2_FeatureGroup219", None)
        self.__aadl2_FeatureGroup219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FeatureGroupType218"):
                opp_val = getattr(old_value, "aadl2_FeatureGroupType218", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FeatureGroupType218"):
                opp_val = getattr(value, "aadl2_FeatureGroupType218", None)
                if opp_val is None:
                    setattr(value, "aadl2_FeatureGroupType218", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_FeatureGroup195(self):
        return self.__aadl2_FeatureGroup195

    @aadl2_FeatureGroup195.setter
    def aadl2_FeatureGroup195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroup__aadl2_FeatureGroup195", None)
        self.__aadl2_FeatureGroup195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FeatureGroupPrototype"):
                opp_val = getattr(old_value, "aadl2_FeatureGroupPrototype", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FeatureGroupPrototype", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FeatureGroupPrototype"):
                opp_val = getattr(value, "aadl2_FeatureGroupPrototype", None)
                setattr(value, "aadl2_FeatureGroupPrototype", self)

    @property
    def aadl2_FeatureGroup193(self):
        return self.__aadl2_FeatureGroup193

    @aadl2_FeatureGroup193.setter
    def aadl2_FeatureGroup193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroup__aadl2_FeatureGroup193", None)
        self.__aadl2_FeatureGroup193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FeatureGroupType"):
                opp_val = getattr(old_value, "aadl2_FeatureGroupType", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FeatureGroupType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FeatureGroupType"):
                opp_val = getattr(value, "aadl2_FeatureGroupType", None)
                setattr(value, "aadl2_FeatureGroupType", self)

class aadl2_TypeExtension(Generalization):

    pass
class aadl2_FlowSpecification(FlowElement, FlowFeature, ModalPath):

    def __init__(self, kind: str, aadl2_FlowSpecification: "aadl2_ComponentType" = None, aadl2_FlowSpecification174: "aadl2_FlowSpecification" = None, aadl2_FlowSpecification172: "aadl2_FlowSpecification" = None, aadl2_FlowSpecification176: "aadl2_FlowEnd" = None, aadl2_FlowSpecification178: "aadl2_FlowEnd" = None, aadl2_FlowSpecification284: "aadl2_FlowImplementation" = None):
        self.kind = kind
        self.aadl2_FlowSpecification = aadl2_FlowSpecification
        self.aadl2_FlowSpecification174 = aadl2_FlowSpecification174
        self.aadl2_FlowSpecification172 = aadl2_FlowSpecification172
        self.aadl2_FlowSpecification176 = aadl2_FlowSpecification176
        self.aadl2_FlowSpecification178 = aadl2_FlowSpecification178
        self.aadl2_FlowSpecification284 = aadl2_FlowSpecification284
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def aadl2_FlowSpecification178(self):
        return self.__aadl2_FlowSpecification178

    @aadl2_FlowSpecification178.setter
    def aadl2_FlowSpecification178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowSpecification__aadl2_FlowSpecification178", None)
        self.__aadl2_FlowSpecification178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FlowEnd179"):
                opp_val = getattr(old_value, "aadl2_FlowEnd179", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FlowEnd179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FlowEnd179"):
                opp_val = getattr(value, "aadl2_FlowEnd179", None)
                setattr(value, "aadl2_FlowEnd179", self)

    @property
    def aadl2_FlowSpecification172(self):
        return self.__aadl2_FlowSpecification172

    @aadl2_FlowSpecification172.setter
    def aadl2_FlowSpecification172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowSpecification__aadl2_FlowSpecification172", None)
        self.__aadl2_FlowSpecification172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FlowSpecification174"):
                opp_val = getattr(old_value, "aadl2_FlowSpecification174", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FlowSpecification174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FlowSpecification174"):
                opp_val = getattr(value, "aadl2_FlowSpecification174", None)
                setattr(value, "aadl2_FlowSpecification174", self)

    @property
    def aadl2_FlowSpecification284(self):
        return self.__aadl2_FlowSpecification284

    @aadl2_FlowSpecification284.setter
    def aadl2_FlowSpecification284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowSpecification__aadl2_FlowSpecification284", None)
        self.__aadl2_FlowSpecification284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FlowImplementation283"):
                opp_val = getattr(old_value, "aadl2_FlowImplementation283", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FlowImplementation283", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FlowImplementation283"):
                opp_val = getattr(value, "aadl2_FlowImplementation283", None)
                setattr(value, "aadl2_FlowImplementation283", self)

    @property
    def aadl2_FlowSpecification176(self):
        return self.__aadl2_FlowSpecification176

    @aadl2_FlowSpecification176.setter
    def aadl2_FlowSpecification176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowSpecification__aadl2_FlowSpecification176", None)
        self.__aadl2_FlowSpecification176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FlowEnd"):
                opp_val = getattr(old_value, "aadl2_FlowEnd", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FlowEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FlowEnd"):
                opp_val = getattr(value, "aadl2_FlowEnd", None)
                setattr(value, "aadl2_FlowEnd", self)

    @property
    def aadl2_FlowSpecification(self):
        return self.__aadl2_FlowSpecification

    @aadl2_FlowSpecification.setter
    def aadl2_FlowSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowSpecification__aadl2_FlowSpecification", None)
        self.__aadl2_FlowSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentType152"):
                opp_val = getattr(old_value, "aadl2_ComponentType152", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentType152"):
                opp_val = getattr(value, "aadl2_ComponentType152", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentType152", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_FlowSpecification174(self):
        return self.__aadl2_FlowSpecification174

    @aadl2_FlowSpecification174.setter
    def aadl2_FlowSpecification174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowSpecification__aadl2_FlowSpecification174", None)
        self.__aadl2_FlowSpecification174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FlowSpecification172"):
                opp_val = getattr(old_value, "aadl2_FlowSpecification172", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FlowSpecification172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FlowSpecification172"):
                opp_val = getattr(value, "aadl2_FlowSpecification172", None)
                setattr(value, "aadl2_FlowSpecification172", self)

class ArrayableElement:

    pass
class aadl2_FeaturePrototypeActual(ArrayableElement):

    pass
class aadl2_ComponentPrototypeActual(ArrayableElement):

    def __init__(self, category: str, aadl2_ComponentPrototypeActual: "aadl2_ComponentPrototypeBinding" = None, aadl2_ComponentPrototypeActual361: set["aadl2_PrototypeBinding"] = None, aadl2_ComponentPrototypeActual364: "aadl2_SubcomponentType" = None):
        self.category = category
        self.aadl2_ComponentPrototypeActual = aadl2_ComponentPrototypeActual
        self.aadl2_ComponentPrototypeActual361 = aadl2_ComponentPrototypeActual361 if aadl2_ComponentPrototypeActual361 is not None else set()
        self.aadl2_ComponentPrototypeActual364 = aadl2_ComponentPrototypeActual364
        
    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def aadl2_ComponentPrototypeActual364(self):
        return self.__aadl2_ComponentPrototypeActual364

    @aadl2_ComponentPrototypeActual364.setter
    def aadl2_ComponentPrototypeActual364(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentPrototypeActual__aadl2_ComponentPrototypeActual364", None)
        self.__aadl2_ComponentPrototypeActual364 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_SubcomponentType365"):
                opp_val = getattr(old_value, "aadl2_SubcomponentType365", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_SubcomponentType365", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_SubcomponentType365"):
                opp_val = getattr(value, "aadl2_SubcomponentType365", None)
                setattr(value, "aadl2_SubcomponentType365", self)

    @property
    def aadl2_ComponentPrototypeActual361(self):
        return self.__aadl2_ComponentPrototypeActual361

    @aadl2_ComponentPrototypeActual361.setter
    def aadl2_ComponentPrototypeActual361(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentPrototypeActual__aadl2_ComponentPrototypeActual361", None)
        self.__aadl2_ComponentPrototypeActual361 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_PrototypeBinding362"):
                    opp_val = getattr(item, "aadl2_PrototypeBinding362", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_PrototypeBinding362", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_PrototypeBinding362"):
                    opp_val = getattr(item, "aadl2_PrototypeBinding362", None)
                    
                    setattr(item, "aadl2_PrototypeBinding362", self)
                    

    @property
    def aadl2_ComponentPrototypeActual(self):
        return self.__aadl2_ComponentPrototypeActual

    @aadl2_ComponentPrototypeActual.setter
    def aadl2_ComponentPrototypeActual(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentPrototypeActual__aadl2_ComponentPrototypeActual", None)
        self.__aadl2_ComponentPrototypeActual = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentPrototypeBinding"):
                opp_val = getattr(old_value, "aadl2_ComponentPrototypeBinding", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentPrototypeBinding"):
                opp_val = getattr(value, "aadl2_ComponentPrototypeBinding", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentPrototypeBinding", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class FeatureConnectionEnd:

    pass
class aadl2_FeatureClassifier(ABC):

    pass
class FeatureClassifier:

    pass
class SubcomponentType:

    pass
class aadl2_ProcessorSubcomponentType(Processor, SubcomponentType):

    pass
class aadl2_ComponentPrototype(SubcomponentType, FeatureClassifier, Prototype):

    def __init__(self, array: str, aadl2_ComponentPrototype: "aadl2_Feature" = None, aadl2_ComponentPrototype170: "aadl2_ComponentClassifier" = None, aadl2_ComponentPrototype264: "aadl2_Subcomponent" = None, aadl2_ComponentPrototype378: "aadl2_AccessSpecification" = None, aadl2_ComponentPrototype383: "aadl2_PortSpecification" = None):
        self.array = array
        self.aadl2_ComponentPrototype = aadl2_ComponentPrototype
        self.aadl2_ComponentPrototype170 = aadl2_ComponentPrototype170
        self.aadl2_ComponentPrototype264 = aadl2_ComponentPrototype264
        self.aadl2_ComponentPrototype378 = aadl2_ComponentPrototype378
        self.aadl2_ComponentPrototype383 = aadl2_ComponentPrototype383
        
    @property
    def array(self) -> str:
        return self.__array

    @array.setter
    def array(self, array: str):
        self.__array = array

    @property
    def aadl2_ComponentPrototype264(self):
        return self.__aadl2_ComponentPrototype264

    @aadl2_ComponentPrototype264.setter
    def aadl2_ComponentPrototype264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentPrototype__aadl2_ComponentPrototype264", None)
        self.__aadl2_ComponentPrototype264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Subcomponent263"):
                opp_val = getattr(old_value, "aadl2_Subcomponent263", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Subcomponent263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Subcomponent263"):
                opp_val = getattr(value, "aadl2_Subcomponent263", None)
                setattr(value, "aadl2_Subcomponent263", self)

    @property
    def aadl2_ComponentPrototype378(self):
        return self.__aadl2_ComponentPrototype378

    @aadl2_ComponentPrototype378.setter
    def aadl2_ComponentPrototype378(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentPrototype__aadl2_ComponentPrototype378", None)
        self.__aadl2_ComponentPrototype378 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_AccessSpecification377"):
                opp_val = getattr(old_value, "aadl2_AccessSpecification377", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_AccessSpecification377", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_AccessSpecification377"):
                opp_val = getattr(value, "aadl2_AccessSpecification377", None)
                setattr(value, "aadl2_AccessSpecification377", self)

    @property
    def aadl2_ComponentPrototype383(self):
        return self.__aadl2_ComponentPrototype383

    @aadl2_ComponentPrototype383.setter
    def aadl2_ComponentPrototype383(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentPrototype__aadl2_ComponentPrototype383", None)
        self.__aadl2_ComponentPrototype383 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PortSpecification382"):
                opp_val = getattr(old_value, "aadl2_PortSpecification382", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_PortSpecification382", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PortSpecification382"):
                opp_val = getattr(value, "aadl2_PortSpecification382", None)
                setattr(value, "aadl2_PortSpecification382", self)

    @property
    def aadl2_ComponentPrototype170(self):
        return self.__aadl2_ComponentPrototype170

    @aadl2_ComponentPrototype170.setter
    def aadl2_ComponentPrototype170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentPrototype__aadl2_ComponentPrototype170", None)
        self.__aadl2_ComponentPrototype170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentClassifier171"):
                opp_val = getattr(old_value, "aadl2_ComponentClassifier171", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentClassifier171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentClassifier171"):
                opp_val = getattr(value, "aadl2_ComponentClassifier171", None)
                setattr(value, "aadl2_ComponentClassifier171", self)

    @property
    def aadl2_ComponentPrototype(self):
        return self.__aadl2_ComponentPrototype

    @aadl2_ComponentPrototype.setter
    def aadl2_ComponentPrototype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentPrototype__aadl2_ComponentPrototype", None)
        self.__aadl2_ComponentPrototype = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Feature160"):
                opp_val = getattr(old_value, "aadl2_Feature160", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Feature160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Feature160"):
                opp_val = getattr(value, "aadl2_Feature160", None)
                setattr(value, "aadl2_Feature160", self)

class aadl2_BusSubcomponentType(Bus, FeatureClassifier, SubcomponentType):

    pass
class aadl2_SubprogramGroupSubcomponentType(SubprogramGroup, FeatureClassifier, SubcomponentType):

    pass
class aadl2_ThreadSubcomponentType(Thread, SubcomponentType):

    pass
class aadl2_SubprogramSubcomponentType(Subprogram, FeatureClassifier, SubcomponentType):

    pass
class aadl2_DeviceSubcomponentType(Device, SubcomponentType):

    pass
class aadl2_SystemSubcomponentType(System, SubcomponentType):

    pass
class aadl2_MemorySubcomponentType(SubcomponentType, Memory):

    pass
class aadl2_VirtualProcessorSubcomponentType(VirtualProcessor, SubcomponentType):

    pass
class aadl2_AbstractSubcomponentType(Abstract, SubcomponentType):

    pass
class aadl2_DataSubcomponentType(FeatureClassifier, Data, SubcomponentType):

    pass
class aadl2_ThreadGroupSubcomponentType(ThreadGroup, SubcomponentType):

    pass
class aadl2_ProcessSubcomponentType(Process, SubcomponentType):

    pass
class aadl2_VirtualBusSubcomponentType(SubcomponentType, VirtualBus):

    pass
class Classifier:

    pass
class aadl2_FeatureGroupType(Classifier, FeatureType):

    pass
class aadl2_ComponentClassifier(Classifier, FeatureClassifier, SubcomponentType):

    def __init__(self, derivedModes: str, noFlows: str, noModes: str, aadl2_ComponentClassifier: set["aadl2_Mode"] = None, aadl2_ComponentClassifier133: set["aadl2_ModeTransition"] = None, aadl2_ComponentClassifier171: "aadl2_ComponentPrototype" = None, aadl2_ComponentClassifier253: "aadl2_FeaturePrototype" = None, aadl2_ComponentClassifier275: "aadl2_Subcomponent" = None, aadl2_ComponentClassifier375: "aadl2_AccessSpecification" = None, aadl2_ComponentClassifier380: "aadl2_PortSpecification" = None):
        self.derivedModes = derivedModes
        self.noFlows = noFlows
        self.noModes = noModes
        self.aadl2_ComponentClassifier = aadl2_ComponentClassifier if aadl2_ComponentClassifier is not None else set()
        self.aadl2_ComponentClassifier133 = aadl2_ComponentClassifier133 if aadl2_ComponentClassifier133 is not None else set()
        self.aadl2_ComponentClassifier171 = aadl2_ComponentClassifier171
        self.aadl2_ComponentClassifier253 = aadl2_ComponentClassifier253
        self.aadl2_ComponentClassifier275 = aadl2_ComponentClassifier275
        self.aadl2_ComponentClassifier375 = aadl2_ComponentClassifier375
        self.aadl2_ComponentClassifier380 = aadl2_ComponentClassifier380
        
    @property
    def noModes(self) -> str:
        return self.__noModes

    @noModes.setter
    def noModes(self, noModes: str):
        self.__noModes = noModes

    @property
    def noFlows(self) -> str:
        return self.__noFlows

    @noFlows.setter
    def noFlows(self, noFlows: str):
        self.__noFlows = noFlows

    @property
    def derivedModes(self) -> str:
        return self.__derivedModes

    @derivedModes.setter
    def derivedModes(self, derivedModes: str):
        self.__derivedModes = derivedModes

    @property
    def aadl2_ComponentClassifier375(self):
        return self.__aadl2_ComponentClassifier375

    @aadl2_ComponentClassifier375.setter
    def aadl2_ComponentClassifier375(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier375", None)
        self.__aadl2_ComponentClassifier375 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_AccessSpecification"):
                opp_val = getattr(old_value, "aadl2_AccessSpecification", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_AccessSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_AccessSpecification"):
                opp_val = getattr(value, "aadl2_AccessSpecification", None)
                setattr(value, "aadl2_AccessSpecification", self)

    @property
    def aadl2_ComponentClassifier171(self):
        return self.__aadl2_ComponentClassifier171

    @aadl2_ComponentClassifier171.setter
    def aadl2_ComponentClassifier171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier171", None)
        self.__aadl2_ComponentClassifier171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentPrototype170"):
                opp_val = getattr(old_value, "aadl2_ComponentPrototype170", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentPrototype170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentPrototype170"):
                opp_val = getattr(value, "aadl2_ComponentPrototype170", None)
                setattr(value, "aadl2_ComponentPrototype170", self)

    @property
    def aadl2_ComponentClassifier133(self):
        return self.__aadl2_ComponentClassifier133

    @aadl2_ComponentClassifier133.setter
    def aadl2_ComponentClassifier133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier133", None)
        self.__aadl2_ComponentClassifier133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ModeTransition"):
                    opp_val = getattr(item, "aadl2_ModeTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ModeTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ModeTransition"):
                    opp_val = getattr(item, "aadl2_ModeTransition", None)
                    
                    setattr(item, "aadl2_ModeTransition", self)
                    

    @property
    def aadl2_ComponentClassifier(self):
        return self.__aadl2_ComponentClassifier

    @aadl2_ComponentClassifier.setter
    def aadl2_ComponentClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier", None)
        self.__aadl2_ComponentClassifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_Mode131"):
                    opp_val = getattr(item, "aadl2_Mode131", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Mode131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Mode131"):
                    opp_val = getattr(item, "aadl2_Mode131", None)
                    
                    setattr(item, "aadl2_Mode131", self)
                    

    @property
    def aadl2_ComponentClassifier275(self):
        return self.__aadl2_ComponentClassifier275

    @aadl2_ComponentClassifier275.setter
    def aadl2_ComponentClassifier275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier275", None)
        self.__aadl2_ComponentClassifier275 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Subcomponent274"):
                opp_val = getattr(old_value, "aadl2_Subcomponent274", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Subcomponent274", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Subcomponent274"):
                opp_val = getattr(value, "aadl2_Subcomponent274", None)
                setattr(value, "aadl2_Subcomponent274", self)

    @property
    def aadl2_ComponentClassifier380(self):
        return self.__aadl2_ComponentClassifier380

    @aadl2_ComponentClassifier380.setter
    def aadl2_ComponentClassifier380(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier380", None)
        self.__aadl2_ComponentClassifier380 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PortSpecification"):
                opp_val = getattr(old_value, "aadl2_PortSpecification", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_PortSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PortSpecification"):
                opp_val = getattr(value, "aadl2_PortSpecification", None)
                setattr(value, "aadl2_PortSpecification", self)

    @property
    def aadl2_ComponentClassifier253(self):
        return self.__aadl2_ComponentClassifier253

    @aadl2_ComponentClassifier253.setter
    def aadl2_ComponentClassifier253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier253", None)
        self.__aadl2_ComponentClassifier253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FeaturePrototype252"):
                opp_val = getattr(old_value, "aadl2_FeaturePrototype252", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FeaturePrototype252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FeaturePrototype252"):
                opp_val = getattr(value, "aadl2_FeaturePrototype252", None)
                setattr(value, "aadl2_FeaturePrototype252", self)

class aadl2_PortProxy(FeatureConnectionEnd, ProcessorFeature, TriggerPort, PortConnectionEnd):

    def __init__(self, direction: str, aadl2_PortProxy: "aadl2_ComponentImplementation" = None):
        self.direction = direction
        self.aadl2_PortProxy = aadl2_PortProxy
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def aadl2_PortProxy(self):
        return self.__aadl2_PortProxy

    @aadl2_PortProxy.setter
    def aadl2_PortProxy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PortProxy__aadl2_PortProxy", None)
        self.__aadl2_PortProxy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentImplementation127"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation127", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation127"):
                opp_val = getattr(value, "aadl2_ComponentImplementation127", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentImplementation127", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aadl2_EventDataSource(InternalFeature):

    pass
class aadl2_FeatureGroupConnection(Connection):

    pass
class aadl2_FeatureConnection(Connection):

    pass
class aadl2_PortConnection(Connection):

    pass
class aadl2_EventSource(InternalFeature):

    pass
class aadl2_AbstractSubcomponent(Abstract, Subcomponent):

    pass
class aadl2_EndToEndFlow(FlowFeature, ModalPath, EndToEndFlowElement):

    pass
class aadl2_Realization(Generalization):

    pass
class aadl2_ImplementationExtension(Generalization):

    pass
class aadl2_ParameterConnection(Connection):

    pass
class aadl2_AccessConnection(Connection):

    def __init__(self, accessCategory: str, aadl2_AccessConnection: "aadl2_ComponentImplementation" = None):
        self.accessCategory = accessCategory
        self.aadl2_AccessConnection = aadl2_AccessConnection
        
    @property
    def accessCategory(self) -> str:
        return self.__accessCategory

    @accessCategory.setter
    def accessCategory(self, accessCategory: str):
        self.__accessCategory = accessCategory

    @property
    def aadl2_AccessConnection(self):
        return self.__aadl2_AccessConnection

    @aadl2_AccessConnection.setter
    def aadl2_AccessConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_AccessConnection__aadl2_AccessConnection", None)
        self.__aadl2_AccessConnection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentImplementation109"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation109", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation109"):
                opp_val = getattr(value, "aadl2_ComponentImplementation109", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentImplementation109", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ComponentClassifier:

    pass
class aadl2_VirtualBusClassifier(ComponentClassifier, VirtualBusSubcomponentType):

    pass
class aadl2_DeviceClassifier(ComponentClassifier, DeviceSubcomponentType):

    pass
class aadl2_VirtualProcessorClassifier(ComponentClassifier, VirtualProcessorSubcomponentType):

    pass
class aadl2_SystemClassifier(ComponentClassifier, SystemSubcomponentType):

    pass
class aadl2_DataClassifier(ComponentClassifier, DataSubcomponentType):

    pass
class aadl2_SubprogramGroupClassifier(ComponentClassifier, SubprogramGroupSubcomponentType):

    pass
class aadl2_MemoryClassifier(ComponentClassifier, MemorySubcomponentType):

    pass
class aadl2_BusClassifier(ComponentClassifier, BusSubcomponentType):

    pass
class aadl2_ComponentType(ComponentClassifier):

    def __init__(self, noFeatures: str, aadl2_ComponentType: "aadl2_ComponentImplementation" = None, aadl2_ComponentType147: set["aadl2_Feature"] = None, aadl2_ComponentType150: "aadl2_ComponentType" = None, aadl2_ComponentType148: "aadl2_ComponentType" = None, aadl2_ComponentType152: set["aadl2_FlowSpecification"] = None, aadl2_ComponentType154: "aadl2_TypeExtension" = None, aadl2_ComponentType156: set["aadl2_FeatureGroup"] = None, aadl2_ComponentType158: set["aadl2_AbstractFeature"] = None, aadl2_ComponentType189: "aadl2_TypeExtension" = None, aadl2_ComponentType310: "aadl2_Realization" = None, aadl2_ComponentType355: "aadl2_ComponentTypeRename" = None):
        self.noFeatures = noFeatures
        self.aadl2_ComponentType = aadl2_ComponentType
        self.aadl2_ComponentType147 = aadl2_ComponentType147 if aadl2_ComponentType147 is not None else set()
        self.aadl2_ComponentType150 = aadl2_ComponentType150
        self.aadl2_ComponentType148 = aadl2_ComponentType148
        self.aadl2_ComponentType152 = aadl2_ComponentType152 if aadl2_ComponentType152 is not None else set()
        self.aadl2_ComponentType154 = aadl2_ComponentType154
        self.aadl2_ComponentType156 = aadl2_ComponentType156 if aadl2_ComponentType156 is not None else set()
        self.aadl2_ComponentType158 = aadl2_ComponentType158 if aadl2_ComponentType158 is not None else set()
        self.aadl2_ComponentType189 = aadl2_ComponentType189
        self.aadl2_ComponentType310 = aadl2_ComponentType310
        self.aadl2_ComponentType355 = aadl2_ComponentType355
        
    @property
    def noFeatures(self) -> str:
        return self.__noFeatures

    @noFeatures.setter
    def noFeatures(self, noFeatures: str):
        self.__noFeatures = noFeatures

    @property
    def aadl2_ComponentType355(self):
        return self.__aadl2_ComponentType355

    @aadl2_ComponentType355.setter
    def aadl2_ComponentType355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType355", None)
        self.__aadl2_ComponentType355 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentTypeRename354"):
                opp_val = getattr(old_value, "aadl2_ComponentTypeRename354", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentTypeRename354", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentTypeRename354"):
                opp_val = getattr(value, "aadl2_ComponentTypeRename354", None)
                setattr(value, "aadl2_ComponentTypeRename354", self)

    @property
    def aadl2_ComponentType(self):
        return self.__aadl2_ComponentType

    @aadl2_ComponentType.setter
    def aadl2_ComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType", None)
        self.__aadl2_ComponentType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentImplementation90"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation90", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentImplementation90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation90"):
                opp_val = getattr(value, "aadl2_ComponentImplementation90", None)
                setattr(value, "aadl2_ComponentImplementation90", self)

    @property
    def aadl2_ComponentType189(self):
        return self.__aadl2_ComponentType189

    @aadl2_ComponentType189.setter
    def aadl2_ComponentType189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType189", None)
        self.__aadl2_ComponentType189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_TypeExtension188"):
                opp_val = getattr(old_value, "aadl2_TypeExtension188", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_TypeExtension188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_TypeExtension188"):
                opp_val = getattr(value, "aadl2_TypeExtension188", None)
                setattr(value, "aadl2_TypeExtension188", self)

    @property
    def aadl2_ComponentType152(self):
        return self.__aadl2_ComponentType152

    @aadl2_ComponentType152.setter
    def aadl2_ComponentType152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType152", None)
        self.__aadl2_ComponentType152 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_FlowSpecification"):
                    opp_val = getattr(item, "aadl2_FlowSpecification", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_FlowSpecification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_FlowSpecification"):
                    opp_val = getattr(item, "aadl2_FlowSpecification", None)
                    
                    setattr(item, "aadl2_FlowSpecification", self)
                    

    @property
    def aadl2_ComponentType156(self):
        return self.__aadl2_ComponentType156

    @aadl2_ComponentType156.setter
    def aadl2_ComponentType156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType156", None)
        self.__aadl2_ComponentType156 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_FeatureGroup"):
                    opp_val = getattr(item, "aadl2_FeatureGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_FeatureGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_FeatureGroup"):
                    opp_val = getattr(item, "aadl2_FeatureGroup", None)
                    
                    setattr(item, "aadl2_FeatureGroup", self)
                    

    @property
    def aadl2_ComponentType310(self):
        return self.__aadl2_ComponentType310

    @aadl2_ComponentType310.setter
    def aadl2_ComponentType310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType310", None)
        self.__aadl2_ComponentType310 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Realization309"):
                opp_val = getattr(old_value, "aadl2_Realization309", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Realization309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Realization309"):
                opp_val = getattr(value, "aadl2_Realization309", None)
                setattr(value, "aadl2_Realization309", self)

    @property
    def aadl2_ComponentType150(self):
        return self.__aadl2_ComponentType150

    @aadl2_ComponentType150.setter
    def aadl2_ComponentType150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType150", None)
        self.__aadl2_ComponentType150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentType148"):
                opp_val = getattr(old_value, "aadl2_ComponentType148", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentType148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentType148"):
                opp_val = getattr(value, "aadl2_ComponentType148", None)
                setattr(value, "aadl2_ComponentType148", self)

    @property
    def aadl2_ComponentType148(self):
        return self.__aadl2_ComponentType148

    @aadl2_ComponentType148.setter
    def aadl2_ComponentType148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType148", None)
        self.__aadl2_ComponentType148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentType150"):
                opp_val = getattr(old_value, "aadl2_ComponentType150", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentType150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentType150"):
                opp_val = getattr(value, "aadl2_ComponentType150", None)
                setattr(value, "aadl2_ComponentType150", self)

    @property
    def aadl2_ComponentType154(self):
        return self.__aadl2_ComponentType154

    @aadl2_ComponentType154.setter
    def aadl2_ComponentType154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType154", None)
        self.__aadl2_ComponentType154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_TypeExtension"):
                opp_val = getattr(old_value, "aadl2_TypeExtension", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_TypeExtension", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_TypeExtension"):
                opp_val = getattr(value, "aadl2_TypeExtension", None)
                setattr(value, "aadl2_TypeExtension", self)

    @property
    def aadl2_ComponentType147(self):
        return self.__aadl2_ComponentType147

    @aadl2_ComponentType147.setter
    def aadl2_ComponentType147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType147", None)
        self.__aadl2_ComponentType147 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_Feature"):
                    opp_val = getattr(item, "aadl2_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Feature"):
                    opp_val = getattr(item, "aadl2_Feature", None)
                    
                    setattr(item, "aadl2_Feature", self)
                    

    @property
    def aadl2_ComponentType158(self):
        return self.__aadl2_ComponentType158

    @aadl2_ComponentType158.setter
    def aadl2_ComponentType158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType158", None)
        self.__aadl2_ComponentType158 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_AbstractFeature"):
                    opp_val = getattr(item, "aadl2_AbstractFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_AbstractFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_AbstractFeature"):
                    opp_val = getattr(item, "aadl2_AbstractFeature", None)
                    
                    setattr(item, "aadl2_AbstractFeature", self)
                    

class aadl2_AbstractClassifier(VirtualBusSubcomponentType, SubprogramSubcomponentType, VirtualProcessorSubcomponentType, SubprogramGroupSubcomponentType, AbstractSubcomponentType, DeviceSubcomponentType, ThreadGroupSubcomponentType, DataSubcomponentType, MemorySubcomponentType, SystemSubcomponentType, ComponentClassifier, ProcessorSubcomponentType, BusSubcomponentType, ProcessSubcomponentType, ThreadSubcomponentType):

    pass
class aadl2_ThreadClassifier(ComponentClassifier, ThreadSubcomponentType):

    pass
class aadl2_ProcessorClassifier(ComponentClassifier, ProcessorSubcomponentType):

    pass
class aadl2_SubprogramClassifier(ComponentClassifier, SubprogramSubcomponentType):

    pass
class aadl2_ThreadGroupClassifier(ComponentClassifier, ThreadGroupSubcomponentType):

    pass
class aadl2_ProcessClassifier(ComponentClassifier, ProcessSubcomponentType):

    pass
class aadl2_ComponentImplementation(ComponentClassifier):

    def __init__(self, noSubcomponents: str, noConnections: str, noCalls: str, aadl2_ComponentImplementation95: "aadl2_ComponentImplementation" = None, aadl2_ComponentImplementation93: "aadl2_ComponentImplementation" = None, aadl2_ComponentImplementation: "aadl2_ComponentImplementationReference" = None, aadl2_ComponentImplementation90: "aadl2_ComponentType" = None, aadl2_ComponentImplementation92: set["aadl2_Subcomponent"] = None, aadl2_ComponentImplementation109: set["aadl2_AccessConnection"] = None, aadl2_ComponentImplementation111: set["aadl2_ParameterConnection"] = None, aadl2_ComponentImplementation97: set["aadl2_FlowImplementation"] = None, aadl2_ComponentImplementation99: set["aadl2_Connection"] = None, aadl2_ComponentImplementation101: "aadl2_ImplementationExtension" = None, aadl2_ComponentImplementation103: "aadl2_Realization" = None, aadl2_ComponentImplementation105: set["aadl2_EndToEndFlow"] = None, aadl2_ComponentImplementation107: set["aadl2_AbstractSubcomponent"] = None, aadl2_ComponentImplementation121: set["aadl2_InternalFeature"] = None, aadl2_ComponentImplementation123: set["aadl2_EventSource"] = None, aadl2_ComponentImplementation113: set["aadl2_PortConnection"] = None, aadl2_ComponentImplementation115: set["aadl2_FeatureConnection"] = None, aadl2_ComponentImplementation117: set["aadl2_FeatureGroupConnection"] = None, aadl2_ComponentImplementation119: set["aadl2_ProcessorFeature"] = None, aadl2_ComponentImplementation125: set["aadl2_EventDataSource"] = None, aadl2_ComponentImplementation127: set["aadl2_PortProxy"] = None, aadl2_ComponentImplementation129: set["aadl2_SubprogramProxy"] = None, aadl2_ComponentImplementation307: "aadl2_ImplementationExtension" = None):
        self.noSubcomponents = noSubcomponents
        self.noConnections = noConnections
        self.noCalls = noCalls
        self.aadl2_ComponentImplementation95 = aadl2_ComponentImplementation95
        self.aadl2_ComponentImplementation93 = aadl2_ComponentImplementation93
        self.aadl2_ComponentImplementation = aadl2_ComponentImplementation
        self.aadl2_ComponentImplementation90 = aadl2_ComponentImplementation90
        self.aadl2_ComponentImplementation92 = aadl2_ComponentImplementation92 if aadl2_ComponentImplementation92 is not None else set()
        self.aadl2_ComponentImplementation109 = aadl2_ComponentImplementation109 if aadl2_ComponentImplementation109 is not None else set()
        self.aadl2_ComponentImplementation111 = aadl2_ComponentImplementation111 if aadl2_ComponentImplementation111 is not None else set()
        self.aadl2_ComponentImplementation97 = aadl2_ComponentImplementation97 if aadl2_ComponentImplementation97 is not None else set()
        self.aadl2_ComponentImplementation99 = aadl2_ComponentImplementation99 if aadl2_ComponentImplementation99 is not None else set()
        self.aadl2_ComponentImplementation101 = aadl2_ComponentImplementation101
        self.aadl2_ComponentImplementation103 = aadl2_ComponentImplementation103
        self.aadl2_ComponentImplementation105 = aadl2_ComponentImplementation105 if aadl2_ComponentImplementation105 is not None else set()
        self.aadl2_ComponentImplementation107 = aadl2_ComponentImplementation107 if aadl2_ComponentImplementation107 is not None else set()
        self.aadl2_ComponentImplementation121 = aadl2_ComponentImplementation121 if aadl2_ComponentImplementation121 is not None else set()
        self.aadl2_ComponentImplementation123 = aadl2_ComponentImplementation123 if aadl2_ComponentImplementation123 is not None else set()
        self.aadl2_ComponentImplementation113 = aadl2_ComponentImplementation113 if aadl2_ComponentImplementation113 is not None else set()
        self.aadl2_ComponentImplementation115 = aadl2_ComponentImplementation115 if aadl2_ComponentImplementation115 is not None else set()
        self.aadl2_ComponentImplementation117 = aadl2_ComponentImplementation117 if aadl2_ComponentImplementation117 is not None else set()
        self.aadl2_ComponentImplementation119 = aadl2_ComponentImplementation119 if aadl2_ComponentImplementation119 is not None else set()
        self.aadl2_ComponentImplementation125 = aadl2_ComponentImplementation125 if aadl2_ComponentImplementation125 is not None else set()
        self.aadl2_ComponentImplementation127 = aadl2_ComponentImplementation127 if aadl2_ComponentImplementation127 is not None else set()
        self.aadl2_ComponentImplementation129 = aadl2_ComponentImplementation129 if aadl2_ComponentImplementation129 is not None else set()
        self.aadl2_ComponentImplementation307 = aadl2_ComponentImplementation307
        
    @property
    def noConnections(self) -> str:
        return self.__noConnections

    @noConnections.setter
    def noConnections(self, noConnections: str):
        self.__noConnections = noConnections

    @property
    def noCalls(self) -> str:
        return self.__noCalls

    @noCalls.setter
    def noCalls(self, noCalls: str):
        self.__noCalls = noCalls

    @property
    def noSubcomponents(self) -> str:
        return self.__noSubcomponents

    @noSubcomponents.setter
    def noSubcomponents(self, noSubcomponents: str):
        self.__noSubcomponents = noSubcomponents

    @property
    def aadl2_ComponentImplementation93(self):
        return self.__aadl2_ComponentImplementation93

    @aadl2_ComponentImplementation93.setter
    def aadl2_ComponentImplementation93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation93", None)
        self.__aadl2_ComponentImplementation93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentImplementation95"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation95", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentImplementation95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation95"):
                opp_val = getattr(value, "aadl2_ComponentImplementation95", None)
                setattr(value, "aadl2_ComponentImplementation95", self)

    @property
    def aadl2_ComponentImplementation115(self):
        return self.__aadl2_ComponentImplementation115

    @aadl2_ComponentImplementation115.setter
    def aadl2_ComponentImplementation115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation115", None)
        self.__aadl2_ComponentImplementation115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_FeatureConnection"):
                    opp_val = getattr(item, "aadl2_FeatureConnection", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_FeatureConnection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_FeatureConnection"):
                    opp_val = getattr(item, "aadl2_FeatureConnection", None)
                    
                    setattr(item, "aadl2_FeatureConnection", self)
                    

    @property
    def aadl2_ComponentImplementation97(self):
        return self.__aadl2_ComponentImplementation97

    @aadl2_ComponentImplementation97.setter
    def aadl2_ComponentImplementation97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation97", None)
        self.__aadl2_ComponentImplementation97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_FlowImplementation"):
                    opp_val = getattr(item, "aadl2_FlowImplementation", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_FlowImplementation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_FlowImplementation"):
                    opp_val = getattr(item, "aadl2_FlowImplementation", None)
                    
                    setattr(item, "aadl2_FlowImplementation", self)
                    

    @property
    def aadl2_ComponentImplementation(self):
        return self.__aadl2_ComponentImplementation

    @aadl2_ComponentImplementation.setter
    def aadl2_ComponentImplementation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation", None)
        self.__aadl2_ComponentImplementation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentImplementationReference"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementationReference", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentImplementationReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementationReference"):
                opp_val = getattr(value, "aadl2_ComponentImplementationReference", None)
                setattr(value, "aadl2_ComponentImplementationReference", self)

    @property
    def aadl2_ComponentImplementation111(self):
        return self.__aadl2_ComponentImplementation111

    @aadl2_ComponentImplementation111.setter
    def aadl2_ComponentImplementation111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation111", None)
        self.__aadl2_ComponentImplementation111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ParameterConnection"):
                    opp_val = getattr(item, "aadl2_ParameterConnection", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ParameterConnection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ParameterConnection"):
                    opp_val = getattr(item, "aadl2_ParameterConnection", None)
                    
                    setattr(item, "aadl2_ParameterConnection", self)
                    

    @property
    def aadl2_ComponentImplementation307(self):
        return self.__aadl2_ComponentImplementation307

    @aadl2_ComponentImplementation307.setter
    def aadl2_ComponentImplementation307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation307", None)
        self.__aadl2_ComponentImplementation307 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ImplementationExtension306"):
                opp_val = getattr(old_value, "aadl2_ImplementationExtension306", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ImplementationExtension306", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ImplementationExtension306"):
                opp_val = getattr(value, "aadl2_ImplementationExtension306", None)
                setattr(value, "aadl2_ImplementationExtension306", self)

    @property
    def aadl2_ComponentImplementation109(self):
        return self.__aadl2_ComponentImplementation109

    @aadl2_ComponentImplementation109.setter
    def aadl2_ComponentImplementation109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation109", None)
        self.__aadl2_ComponentImplementation109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_AccessConnection"):
                    opp_val = getattr(item, "aadl2_AccessConnection", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_AccessConnection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_AccessConnection"):
                    opp_val = getattr(item, "aadl2_AccessConnection", None)
                    
                    setattr(item, "aadl2_AccessConnection", self)
                    

    @property
    def aadl2_ComponentImplementation105(self):
        return self.__aadl2_ComponentImplementation105

    @aadl2_ComponentImplementation105.setter
    def aadl2_ComponentImplementation105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation105", None)
        self.__aadl2_ComponentImplementation105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_EndToEndFlow"):
                    opp_val = getattr(item, "aadl2_EndToEndFlow", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_EndToEndFlow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_EndToEndFlow"):
                    opp_val = getattr(item, "aadl2_EndToEndFlow", None)
                    
                    setattr(item, "aadl2_EndToEndFlow", self)
                    

    @property
    def aadl2_ComponentImplementation92(self):
        return self.__aadl2_ComponentImplementation92

    @aadl2_ComponentImplementation92.setter
    def aadl2_ComponentImplementation92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation92", None)
        self.__aadl2_ComponentImplementation92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_Subcomponent"):
                    opp_val = getattr(item, "aadl2_Subcomponent", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Subcomponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Subcomponent"):
                    opp_val = getattr(item, "aadl2_Subcomponent", None)
                    
                    setattr(item, "aadl2_Subcomponent", self)
                    

    @property
    def aadl2_ComponentImplementation125(self):
        return self.__aadl2_ComponentImplementation125

    @aadl2_ComponentImplementation125.setter
    def aadl2_ComponentImplementation125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation125", None)
        self.__aadl2_ComponentImplementation125 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_EventDataSource"):
                    opp_val = getattr(item, "aadl2_EventDataSource", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_EventDataSource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_EventDataSource"):
                    opp_val = getattr(item, "aadl2_EventDataSource", None)
                    
                    setattr(item, "aadl2_EventDataSource", self)
                    

    @property
    def aadl2_ComponentImplementation129(self):
        return self.__aadl2_ComponentImplementation129

    @aadl2_ComponentImplementation129.setter
    def aadl2_ComponentImplementation129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation129", None)
        self.__aadl2_ComponentImplementation129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_SubprogramProxy"):
                    opp_val = getattr(item, "aadl2_SubprogramProxy", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_SubprogramProxy", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_SubprogramProxy"):
                    opp_val = getattr(item, "aadl2_SubprogramProxy", None)
                    
                    setattr(item, "aadl2_SubprogramProxy", self)
                    

    @property
    def aadl2_ComponentImplementation123(self):
        return self.__aadl2_ComponentImplementation123

    @aadl2_ComponentImplementation123.setter
    def aadl2_ComponentImplementation123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation123", None)
        self.__aadl2_ComponentImplementation123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_EventSource"):
                    opp_val = getattr(item, "aadl2_EventSource", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_EventSource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_EventSource"):
                    opp_val = getattr(item, "aadl2_EventSource", None)
                    
                    setattr(item, "aadl2_EventSource", self)
                    

    @property
    def aadl2_ComponentImplementation99(self):
        return self.__aadl2_ComponentImplementation99

    @aadl2_ComponentImplementation99.setter
    def aadl2_ComponentImplementation99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation99", None)
        self.__aadl2_ComponentImplementation99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_Connection"):
                    opp_val = getattr(item, "aadl2_Connection", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Connection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Connection"):
                    opp_val = getattr(item, "aadl2_Connection", None)
                    
                    setattr(item, "aadl2_Connection", self)
                    

    @property
    def aadl2_ComponentImplementation95(self):
        return self.__aadl2_ComponentImplementation95

    @aadl2_ComponentImplementation95.setter
    def aadl2_ComponentImplementation95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation95", None)
        self.__aadl2_ComponentImplementation95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentImplementation93"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation93", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentImplementation93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation93"):
                opp_val = getattr(value, "aadl2_ComponentImplementation93", None)
                setattr(value, "aadl2_ComponentImplementation93", self)

    @property
    def aadl2_ComponentImplementation101(self):
        return self.__aadl2_ComponentImplementation101

    @aadl2_ComponentImplementation101.setter
    def aadl2_ComponentImplementation101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation101", None)
        self.__aadl2_ComponentImplementation101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ImplementationExtension"):
                opp_val = getattr(old_value, "aadl2_ImplementationExtension", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ImplementationExtension", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ImplementationExtension"):
                opp_val = getattr(value, "aadl2_ImplementationExtension", None)
                setattr(value, "aadl2_ImplementationExtension", self)

    @property
    def aadl2_ComponentImplementation107(self):
        return self.__aadl2_ComponentImplementation107

    @aadl2_ComponentImplementation107.setter
    def aadl2_ComponentImplementation107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation107", None)
        self.__aadl2_ComponentImplementation107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_AbstractSubcomponent"):
                    opp_val = getattr(item, "aadl2_AbstractSubcomponent", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_AbstractSubcomponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_AbstractSubcomponent"):
                    opp_val = getattr(item, "aadl2_AbstractSubcomponent", None)
                    
                    setattr(item, "aadl2_AbstractSubcomponent", self)
                    

    @property
    def aadl2_ComponentImplementation127(self):
        return self.__aadl2_ComponentImplementation127

    @aadl2_ComponentImplementation127.setter
    def aadl2_ComponentImplementation127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation127", None)
        self.__aadl2_ComponentImplementation127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_PortProxy"):
                    opp_val = getattr(item, "aadl2_PortProxy", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_PortProxy", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_PortProxy"):
                    opp_val = getattr(item, "aadl2_PortProxy", None)
                    
                    setattr(item, "aadl2_PortProxy", self)
                    

    @property
    def aadl2_ComponentImplementation113(self):
        return self.__aadl2_ComponentImplementation113

    @aadl2_ComponentImplementation113.setter
    def aadl2_ComponentImplementation113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation113", None)
        self.__aadl2_ComponentImplementation113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_PortConnection"):
                    opp_val = getattr(item, "aadl2_PortConnection", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_PortConnection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_PortConnection"):
                    opp_val = getattr(item, "aadl2_PortConnection", None)
                    
                    setattr(item, "aadl2_PortConnection", self)
                    

    @property
    def aadl2_ComponentImplementation119(self):
        return self.__aadl2_ComponentImplementation119

    @aadl2_ComponentImplementation119.setter
    def aadl2_ComponentImplementation119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation119", None)
        self.__aadl2_ComponentImplementation119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ProcessorFeature"):
                    opp_val = getattr(item, "aadl2_ProcessorFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ProcessorFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ProcessorFeature"):
                    opp_val = getattr(item, "aadl2_ProcessorFeature", None)
                    
                    setattr(item, "aadl2_ProcessorFeature", self)
                    

    @property
    def aadl2_ComponentImplementation121(self):
        return self.__aadl2_ComponentImplementation121

    @aadl2_ComponentImplementation121.setter
    def aadl2_ComponentImplementation121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation121", None)
        self.__aadl2_ComponentImplementation121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_InternalFeature"):
                    opp_val = getattr(item, "aadl2_InternalFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_InternalFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_InternalFeature"):
                    opp_val = getattr(item, "aadl2_InternalFeature", None)
                    
                    setattr(item, "aadl2_InternalFeature", self)
                    

    @property
    def aadl2_ComponentImplementation103(self):
        return self.__aadl2_ComponentImplementation103

    @aadl2_ComponentImplementation103.setter
    def aadl2_ComponentImplementation103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation103", None)
        self.__aadl2_ComponentImplementation103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Realization"):
                opp_val = getattr(old_value, "aadl2_Realization", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Realization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Realization"):
                opp_val = getattr(value, "aadl2_Realization", None)
                setattr(value, "aadl2_Realization", self)

    @property
    def aadl2_ComponentImplementation117(self):
        return self.__aadl2_ComponentImplementation117

    @aadl2_ComponentImplementation117.setter
    def aadl2_ComponentImplementation117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation117", None)
        self.__aadl2_ComponentImplementation117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_FeatureGroupConnection"):
                    opp_val = getattr(item, "aadl2_FeatureGroupConnection", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_FeatureGroupConnection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_FeatureGroupConnection"):
                    opp_val = getattr(item, "aadl2_FeatureGroupConnection", None)
                    
                    setattr(item, "aadl2_FeatureGroupConnection", self)
                    

    @property
    def aadl2_ComponentImplementation90(self):
        return self.__aadl2_ComponentImplementation90

    @aadl2_ComponentImplementation90.setter
    def aadl2_ComponentImplementation90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation90", None)
        self.__aadl2_ComponentImplementation90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentType"):
                opp_val = getattr(old_value, "aadl2_ComponentType", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentType"):
                opp_val = getattr(value, "aadl2_ComponentType", None)
                setattr(value, "aadl2_ComponentType", self)

    def getAllSubcomponents(self) -> str:
        # TODO: Implement getAllSubcomponents method
        pass

class aadl2_CalledSubprogram(ABC):

    pass
class RefinableElement:

    pass
class CalledSubprogram:

    pass
class aadl2_SubprogramProxy(AccessConnectionEnd, ProcessorFeature, CalledSubprogram):

    pass
class StructuralFeature:

    pass
class aadl2_Feature(ArrayableElement, FeatureConnectionEnd, StructuralFeature):

    pass
class aadl2_FlowFeature(Flow, StructuralFeature):

    pass
class aadl2_Connection(FlowElement, ModalPath, StructuralFeature):

    def __init__(self, bidirectional: str, aadl2_Connection: "aadl2_ComponentImplementation" = None, aadl2_Connection293: "aadl2_ConnectedElement" = None, aadl2_Connection295: "aadl2_ConnectedElement" = None, aadl2_Connection299: "aadl2_Connection" = None, aadl2_Connection297: "aadl2_Connection" = None):
        self.bidirectional = bidirectional
        self.aadl2_Connection = aadl2_Connection
        self.aadl2_Connection293 = aadl2_Connection293
        self.aadl2_Connection295 = aadl2_Connection295
        self.aadl2_Connection299 = aadl2_Connection299
        self.aadl2_Connection297 = aadl2_Connection297
        
    @property
    def bidirectional(self) -> str:
        return self.__bidirectional

    @bidirectional.setter
    def bidirectional(self, bidirectional: str):
        self.__bidirectional = bidirectional

    @property
    def aadl2_Connection295(self):
        return self.__aadl2_Connection295

    @aadl2_Connection295.setter
    def aadl2_Connection295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Connection__aadl2_Connection295", None)
        self.__aadl2_Connection295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ConnectedElement296"):
                opp_val = getattr(old_value, "aadl2_ConnectedElement296", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ConnectedElement296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ConnectedElement296"):
                opp_val = getattr(value, "aadl2_ConnectedElement296", None)
                setattr(value, "aadl2_ConnectedElement296", self)

    @property
    def aadl2_Connection(self):
        return self.__aadl2_Connection

    @aadl2_Connection.setter
    def aadl2_Connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Connection__aadl2_Connection", None)
        self.__aadl2_Connection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentImplementation99"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation99", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation99"):
                opp_val = getattr(value, "aadl2_ComponentImplementation99", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentImplementation99", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_Connection293(self):
        return self.__aadl2_Connection293

    @aadl2_Connection293.setter
    def aadl2_Connection293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Connection__aadl2_Connection293", None)
        self.__aadl2_Connection293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ConnectedElement"):
                opp_val = getattr(old_value, "aadl2_ConnectedElement", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ConnectedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ConnectedElement"):
                opp_val = getattr(value, "aadl2_ConnectedElement", None)
                setattr(value, "aadl2_ConnectedElement", self)

    @property
    def aadl2_Connection299(self):
        return self.__aadl2_Connection299

    @aadl2_Connection299.setter
    def aadl2_Connection299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Connection__aadl2_Connection299", None)
        self.__aadl2_Connection299 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Connection297"):
                opp_val = getattr(old_value, "aadl2_Connection297", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Connection297", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Connection297"):
                opp_val = getattr(value, "aadl2_Connection297", None)
                setattr(value, "aadl2_Connection297", self)

    @property
    def aadl2_Connection297(self):
        return self.__aadl2_Connection297

    @aadl2_Connection297.setter
    def aadl2_Connection297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Connection__aadl2_Connection297", None)
        self.__aadl2_Connection297 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Connection299"):
                opp_val = getattr(old_value, "aadl2_Connection299", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Connection299", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Connection299"):
                opp_val = getattr(value, "aadl2_Connection299", None)
                setattr(value, "aadl2_Connection299", self)

class ClassifierFeature:

    pass
class aadl2_StructuralFeature(ClassifierFeature, RefinableElement):

    pass
class aadl2_FlowImplementation(Flow, ModalPath, ClassifierFeature):

    def __init__(self, kind: str, aadl2_FlowImplementation: "aadl2_ComponentImplementation" = None, aadl2_FlowImplementation283: "aadl2_FlowSpecification" = None, aadl2_FlowImplementation286: set["aadl2_FlowSegment"] = None):
        self.kind = kind
        self.aadl2_FlowImplementation = aadl2_FlowImplementation
        self.aadl2_FlowImplementation283 = aadl2_FlowImplementation283
        self.aadl2_FlowImplementation286 = aadl2_FlowImplementation286 if aadl2_FlowImplementation286 is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def aadl2_FlowImplementation(self):
        return self.__aadl2_FlowImplementation

    @aadl2_FlowImplementation.setter
    def aadl2_FlowImplementation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowImplementation__aadl2_FlowImplementation", None)
        self.__aadl2_FlowImplementation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentImplementation97"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation97", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation97"):
                opp_val = getattr(value, "aadl2_ComponentImplementation97", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentImplementation97", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_FlowImplementation286(self):
        return self.__aadl2_FlowImplementation286

    @aadl2_FlowImplementation286.setter
    def aadl2_FlowImplementation286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowImplementation__aadl2_FlowImplementation286", None)
        self.__aadl2_FlowImplementation286 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_FlowSegment"):
                    opp_val = getattr(item, "aadl2_FlowSegment", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_FlowSegment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_FlowSegment"):
                    opp_val = getattr(item, "aadl2_FlowSegment", None)
                    
                    setattr(item, "aadl2_FlowSegment", self)
                    

    @property
    def aadl2_FlowImplementation283(self):
        return self.__aadl2_FlowImplementation283

    @aadl2_FlowImplementation283.setter
    def aadl2_FlowImplementation283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowImplementation__aadl2_FlowImplementation283", None)
        self.__aadl2_FlowImplementation283 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FlowSpecification284"):
                opp_val = getattr(old_value, "aadl2_FlowSpecification284", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FlowSpecification284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FlowSpecification284"):
                opp_val = getattr(value, "aadl2_FlowSpecification284", None)
                setattr(value, "aadl2_FlowSpecification284", self)

class aadl2_BehavioralFeature(ClassifierFeature):

    pass
class aadl2_ModeFeature(ClassifierFeature):

    pass
class ModeFeature:

    pass
class aadl2_ModeTransition(ModeFeature):

    pass
class aadl2_Mode(ModeFeature):

    def __init__(self, initial: str, derived: str, aadl2_Mode: "aadl2_ModalElement" = None, aadl2_Mode131: "aadl2_ComponentClassifier" = None, aadl2_Mode136: "aadl2_ModeTransition" = None, aadl2_Mode139: "aadl2_ModeTransition" = None, aadl2_Mode278: "aadl2_ModeBinding" = None, aadl2_Mode281: "aadl2_ModeBinding" = None):
        self.initial = initial
        self.derived = derived
        self.aadl2_Mode = aadl2_Mode
        self.aadl2_Mode131 = aadl2_Mode131
        self.aadl2_Mode136 = aadl2_Mode136
        self.aadl2_Mode139 = aadl2_Mode139
        self.aadl2_Mode278 = aadl2_Mode278
        self.aadl2_Mode281 = aadl2_Mode281
        
    @property
    def derived(self) -> str:
        return self.__derived

    @derived.setter
    def derived(self, derived: str):
        self.__derived = derived

    @property
    def initial(self) -> str:
        return self.__initial

    @initial.setter
    def initial(self, initial: str):
        self.__initial = initial

    @property
    def aadl2_Mode139(self):
        return self.__aadl2_Mode139

    @aadl2_Mode139.setter
    def aadl2_Mode139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Mode__aadl2_Mode139", None)
        self.__aadl2_Mode139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ModeTransition138"):
                opp_val = getattr(old_value, "aadl2_ModeTransition138", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ModeTransition138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ModeTransition138"):
                opp_val = getattr(value, "aadl2_ModeTransition138", None)
                setattr(value, "aadl2_ModeTransition138", self)

    @property
    def aadl2_Mode136(self):
        return self.__aadl2_Mode136

    @aadl2_Mode136.setter
    def aadl2_Mode136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Mode__aadl2_Mode136", None)
        self.__aadl2_Mode136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ModeTransition135"):
                opp_val = getattr(old_value, "aadl2_ModeTransition135", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ModeTransition135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ModeTransition135"):
                opp_val = getattr(value, "aadl2_ModeTransition135", None)
                setattr(value, "aadl2_ModeTransition135", self)

    @property
    def aadl2_Mode131(self):
        return self.__aadl2_Mode131

    @aadl2_Mode131.setter
    def aadl2_Mode131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Mode__aadl2_Mode131", None)
        self.__aadl2_Mode131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentClassifier"):
                opp_val = getattr(old_value, "aadl2_ComponentClassifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentClassifier"):
                opp_val = getattr(value, "aadl2_ComponentClassifier", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentClassifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_Mode281(self):
        return self.__aadl2_Mode281

    @aadl2_Mode281.setter
    def aadl2_Mode281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Mode__aadl2_Mode281", None)
        self.__aadl2_Mode281 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ModeBinding280"):
                opp_val = getattr(old_value, "aadl2_ModeBinding280", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ModeBinding280", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ModeBinding280"):
                opp_val = getattr(value, "aadl2_ModeBinding280", None)
                setattr(value, "aadl2_ModeBinding280", self)

    @property
    def aadl2_Mode278(self):
        return self.__aadl2_Mode278

    @aadl2_Mode278.setter
    def aadl2_Mode278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Mode__aadl2_Mode278", None)
        self.__aadl2_Mode278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ModeBinding277"):
                opp_val = getattr(old_value, "aadl2_ModeBinding277", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ModeBinding277", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ModeBinding277"):
                opp_val = getattr(value, "aadl2_ModeBinding277", None)
                setattr(value, "aadl2_ModeBinding277", self)

    @property
    def aadl2_Mode(self):
        return self.__aadl2_Mode

    @aadl2_Mode.setter
    def aadl2_Mode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Mode__aadl2_Mode", None)
        self.__aadl2_Mode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ModalElement"):
                opp_val = getattr(old_value, "aadl2_ModalElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ModalElement"):
                opp_val = getattr(value, "aadl2_ModalElement", None)
                if opp_val is None:
                    setattr(value, "aadl2_ModalElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ModalElement:

    pass
class aadl2_InternalFeature(FeatureConnectionEnd, TriggerPort, ModalElement, StructuralFeature, PortConnectionEnd):

    def __init__(self, direction: str, aadl2_InternalFeature: "aadl2_ComponentImplementation" = None):
        self.direction = direction
        self.aadl2_InternalFeature = aadl2_InternalFeature
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def aadl2_InternalFeature(self):
        return self.__aadl2_InternalFeature

    @aadl2_InternalFeature.setter
    def aadl2_InternalFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_InternalFeature__aadl2_InternalFeature", None)
        self.__aadl2_InternalFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentImplementation121"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation121", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation121"):
                opp_val = getattr(value, "aadl2_ComponentImplementation121", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentImplementation121", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aadl2_ProcessorFeature(StructuralFeature, ModalElement):

    pass
class aadl2_SubprogramCallSequence(BehavioralFeature, ModalElement):

    pass
class aadl2_ModalPath(ModalElement):

    def __init__(self, aadl2_ModalPath: set["aadl2_ModeFeature"] = None):
        self.aadl2_ModalPath = aadl2_ModalPath if aadl2_ModalPath is not None else set()
        
    @property
    def aadl2_ModalPath(self):
        return self.__aadl2_ModalPath

    @aadl2_ModalPath.setter
    def aadl2_ModalPath(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ModalPath__aadl2_ModalPath", None)
        self.__aadl2_ModalPath = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ModeFeature"):
                    opp_val = getattr(item, "aadl2_ModeFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ModeFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ModeFeature"):
                    opp_val = getattr(item, "aadl2_ModeFeature", None)
                    
                    setattr(item, "aadl2_ModeFeature", self)
                    

    def getInModes(self) -> str:
        # TODO: Implement getInModes method
        pass

    def getInModeTransitions(self) -> str:
        # TODO: Implement getInModeTransitions method
        pass

    def getAllInModeTransitions(self) -> str:
        # TODO: Implement getAllInModeTransitions method
        pass

class aadl2_Subcomponent(ModalElement, FlowElement, StructuralFeature, ArrayableElement, Context):

    def __init__(self, allModes: str, aadl2_Subcomponent: "aadl2_ComponentImplementation" = None, aadl2_Subcomponent266: set["aadl2_ModeBinding"] = None, aadl2_Subcomponent258: "aadl2_SubcomponentType" = None, aadl2_Subcomponent260: set["aadl2_PrototypeBinding"] = None, aadl2_Subcomponent263: "aadl2_ComponentPrototype" = None, aadl2_Subcomponent268: set["aadl2_ComponentImplementationReference"] = None, aadl2_Subcomponent272: "aadl2_Subcomponent" = None, aadl2_Subcomponent270: "aadl2_Subcomponent" = None, aadl2_Subcomponent274: "aadl2_ComponentClassifier" = None):
        self.allModes = allModes
        self.aadl2_Subcomponent = aadl2_Subcomponent
        self.aadl2_Subcomponent266 = aadl2_Subcomponent266 if aadl2_Subcomponent266 is not None else set()
        self.aadl2_Subcomponent258 = aadl2_Subcomponent258
        self.aadl2_Subcomponent260 = aadl2_Subcomponent260 if aadl2_Subcomponent260 is not None else set()
        self.aadl2_Subcomponent263 = aadl2_Subcomponent263
        self.aadl2_Subcomponent268 = aadl2_Subcomponent268 if aadl2_Subcomponent268 is not None else set()
        self.aadl2_Subcomponent272 = aadl2_Subcomponent272
        self.aadl2_Subcomponent270 = aadl2_Subcomponent270
        self.aadl2_Subcomponent274 = aadl2_Subcomponent274
        
    @property
    def allModes(self) -> str:
        return self.__allModes

    @allModes.setter
    def allModes(self, allModes: str):
        self.__allModes = allModes

    @property
    def aadl2_Subcomponent270(self):
        return self.__aadl2_Subcomponent270

    @aadl2_Subcomponent270.setter
    def aadl2_Subcomponent270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent270", None)
        self.__aadl2_Subcomponent270 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Subcomponent272"):
                opp_val = getattr(old_value, "aadl2_Subcomponent272", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Subcomponent272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Subcomponent272"):
                opp_val = getattr(value, "aadl2_Subcomponent272", None)
                setattr(value, "aadl2_Subcomponent272", self)

    @property
    def aadl2_Subcomponent274(self):
        return self.__aadl2_Subcomponent274

    @aadl2_Subcomponent274.setter
    def aadl2_Subcomponent274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent274", None)
        self.__aadl2_Subcomponent274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentClassifier275"):
                opp_val = getattr(old_value, "aadl2_ComponentClassifier275", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentClassifier275", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentClassifier275"):
                opp_val = getattr(value, "aadl2_ComponentClassifier275", None)
                setattr(value, "aadl2_ComponentClassifier275", self)

    @property
    def aadl2_Subcomponent272(self):
        return self.__aadl2_Subcomponent272

    @aadl2_Subcomponent272.setter
    def aadl2_Subcomponent272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent272", None)
        self.__aadl2_Subcomponent272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Subcomponent270"):
                opp_val = getattr(old_value, "aadl2_Subcomponent270", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Subcomponent270", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Subcomponent270"):
                opp_val = getattr(value, "aadl2_Subcomponent270", None)
                setattr(value, "aadl2_Subcomponent270", self)

    @property
    def aadl2_Subcomponent258(self):
        return self.__aadl2_Subcomponent258

    @aadl2_Subcomponent258.setter
    def aadl2_Subcomponent258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent258", None)
        self.__aadl2_Subcomponent258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_SubcomponentType"):
                opp_val = getattr(old_value, "aadl2_SubcomponentType", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_SubcomponentType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_SubcomponentType"):
                opp_val = getattr(value, "aadl2_SubcomponentType", None)
                setattr(value, "aadl2_SubcomponentType", self)

    @property
    def aadl2_Subcomponent268(self):
        return self.__aadl2_Subcomponent268

    @aadl2_Subcomponent268.setter
    def aadl2_Subcomponent268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent268", None)
        self.__aadl2_Subcomponent268 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ComponentImplementationReference269"):
                    opp_val = getattr(item, "aadl2_ComponentImplementationReference269", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ComponentImplementationReference269", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ComponentImplementationReference269"):
                    opp_val = getattr(item, "aadl2_ComponentImplementationReference269", None)
                    
                    setattr(item, "aadl2_ComponentImplementationReference269", self)
                    

    @property
    def aadl2_Subcomponent(self):
        return self.__aadl2_Subcomponent

    @aadl2_Subcomponent.setter
    def aadl2_Subcomponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent", None)
        self.__aadl2_Subcomponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentImplementation92"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation92"):
                opp_val = getattr(value, "aadl2_ComponentImplementation92", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentImplementation92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_Subcomponent266(self):
        return self.__aadl2_Subcomponent266

    @aadl2_Subcomponent266.setter
    def aadl2_Subcomponent266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent266", None)
        self.__aadl2_Subcomponent266 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ModeBinding"):
                    opp_val = getattr(item, "aadl2_ModeBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ModeBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ModeBinding"):
                    opp_val = getattr(item, "aadl2_ModeBinding", None)
                    
                    setattr(item, "aadl2_ModeBinding", self)
                    

    @property
    def aadl2_Subcomponent260(self):
        return self.__aadl2_Subcomponent260

    @aadl2_Subcomponent260.setter
    def aadl2_Subcomponent260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent260", None)
        self.__aadl2_Subcomponent260 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_PrototypeBinding261"):
                    opp_val = getattr(item, "aadl2_PrototypeBinding261", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_PrototypeBinding261", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_PrototypeBinding261"):
                    opp_val = getattr(item, "aadl2_PrototypeBinding261", None)
                    
                    setattr(item, "aadl2_PrototypeBinding261", self)
                    

    @property
    def aadl2_Subcomponent263(self):
        return self.__aadl2_Subcomponent263

    @aadl2_Subcomponent263.setter
    def aadl2_Subcomponent263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent263", None)
        self.__aadl2_Subcomponent263 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentPrototype264"):
                opp_val = getattr(old_value, "aadl2_ComponentPrototype264", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentPrototype264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentPrototype264"):
                opp_val = getattr(value, "aadl2_ComponentPrototype264", None)
                setattr(value, "aadl2_ComponentPrototype264", self)

class Relationship:

    pass
class aadl2_DirectedRelationship(Relationship):

    pass
class DirectedRelationship:

    pass
class aadl2_Prototype(CalledSubprogram, StructuralFeature):

    def __init__(self, aadl2_Prototype: "aadl2_Classifier" = None, aadl2_Prototype61: "aadl2_Prototype" = None, aadl2_Prototype59: "aadl2_Prototype" = None, aadl2_Prototype69: "aadl2_PrototypeBinding" = None):
        self.aadl2_Prototype = aadl2_Prototype
        self.aadl2_Prototype61 = aadl2_Prototype61
        self.aadl2_Prototype59 = aadl2_Prototype59
        self.aadl2_Prototype69 = aadl2_Prototype69
        
    @property
    def aadl2_Prototype61(self):
        return self.__aadl2_Prototype61

    @aadl2_Prototype61.setter
    def aadl2_Prototype61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Prototype__aadl2_Prototype61", None)
        self.__aadl2_Prototype61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Prototype59"):
                opp_val = getattr(old_value, "aadl2_Prototype59", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Prototype59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Prototype59"):
                opp_val = getattr(value, "aadl2_Prototype59", None)
                setattr(value, "aadl2_Prototype59", self)

    @property
    def aadl2_Prototype(self):
        return self.__aadl2_Prototype

    @aadl2_Prototype.setter
    def aadl2_Prototype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Prototype__aadl2_Prototype", None)
        self.__aadl2_Prototype = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Classifier38"):
                opp_val = getattr(old_value, "aadl2_Classifier38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Classifier38"):
                opp_val = getattr(value, "aadl2_Classifier38", None)
                if opp_val is None:
                    setattr(value, "aadl2_Classifier38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_Prototype59(self):
        return self.__aadl2_Prototype59

    @aadl2_Prototype59.setter
    def aadl2_Prototype59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Prototype__aadl2_Prototype59", None)
        self.__aadl2_Prototype59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Prototype61"):
                opp_val = getattr(old_value, "aadl2_Prototype61", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Prototype61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Prototype61"):
                opp_val = getattr(value, "aadl2_Prototype61", None)
                setattr(value, "aadl2_Prototype61", self)

    @property
    def aadl2_Prototype69(self):
        return self.__aadl2_Prototype69

    @aadl2_Prototype69.setter
    def aadl2_Prototype69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Prototype__aadl2_Prototype69", None)
        self.__aadl2_Prototype69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PrototypeBinding68"):
                opp_val = getattr(old_value, "aadl2_PrototypeBinding68", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_PrototypeBinding68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PrototypeBinding68"):
                opp_val = getattr(value, "aadl2_PrototypeBinding68", None)
                setattr(value, "aadl2_PrototypeBinding68", self)

    def categoryConstraint(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement categoryConstraint method
        pass

class aadl2_Generalization(DirectedRelationship):

    pass
class aadl2_AnnexSubclause(ModalElement):

    pass
class Namespace:

    pass
class aadl2_PropertySet(ModelUnit, Namespace):

    pass
class aadl2_PackageSection(Namespace):

    def __init__(self, noAnnexes: str, noProperties: str, aadl2_PackageSection: set["aadl2_PackageRename"] = None, aadl2_PackageSection329: set["aadl2_ComponentTypeRename"] = None, aadl2_PackageSection331: set["aadl2_Classifier"] = None, aadl2_PackageSection334: set["aadl2_FeatureGroupTypeRename"] = None, aadl2_PackageSection336: set["aadl2_AnnexLibrary"] = None, aadl2_PackageSection339: set["aadl2_ModelUnit"] = None):
        self.noAnnexes = noAnnexes
        self.noProperties = noProperties
        self.aadl2_PackageSection = aadl2_PackageSection if aadl2_PackageSection is not None else set()
        self.aadl2_PackageSection329 = aadl2_PackageSection329 if aadl2_PackageSection329 is not None else set()
        self.aadl2_PackageSection331 = aadl2_PackageSection331 if aadl2_PackageSection331 is not None else set()
        self.aadl2_PackageSection334 = aadl2_PackageSection334 if aadl2_PackageSection334 is not None else set()
        self.aadl2_PackageSection336 = aadl2_PackageSection336 if aadl2_PackageSection336 is not None else set()
        self.aadl2_PackageSection339 = aadl2_PackageSection339 if aadl2_PackageSection339 is not None else set()
        
    @property
    def noAnnexes(self) -> str:
        return self.__noAnnexes

    @noAnnexes.setter
    def noAnnexes(self, noAnnexes: str):
        self.__noAnnexes = noAnnexes

    @property
    def noProperties(self) -> str:
        return self.__noProperties

    @noProperties.setter
    def noProperties(self, noProperties: str):
        self.__noProperties = noProperties

    @property
    def aadl2_PackageSection334(self):
        return self.__aadl2_PackageSection334

    @aadl2_PackageSection334.setter
    def aadl2_PackageSection334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection334", None)
        self.__aadl2_PackageSection334 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_FeatureGroupTypeRename"):
                    opp_val = getattr(item, "aadl2_FeatureGroupTypeRename", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_FeatureGroupTypeRename", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_FeatureGroupTypeRename"):
                    opp_val = getattr(item, "aadl2_FeatureGroupTypeRename", None)
                    
                    setattr(item, "aadl2_FeatureGroupTypeRename", self)
                    

    @property
    def aadl2_PackageSection331(self):
        return self.__aadl2_PackageSection331

    @aadl2_PackageSection331.setter
    def aadl2_PackageSection331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection331", None)
        self.__aadl2_PackageSection331 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_Classifier332"):
                    opp_val = getattr(item, "aadl2_Classifier332", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Classifier332", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Classifier332"):
                    opp_val = getattr(item, "aadl2_Classifier332", None)
                    
                    setattr(item, "aadl2_Classifier332", self)
                    

    @property
    def aadl2_PackageSection(self):
        return self.__aadl2_PackageSection

    @aadl2_PackageSection.setter
    def aadl2_PackageSection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection", None)
        self.__aadl2_PackageSection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_PackageRename"):
                    opp_val = getattr(item, "aadl2_PackageRename", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_PackageRename", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_PackageRename"):
                    opp_val = getattr(item, "aadl2_PackageRename", None)
                    
                    setattr(item, "aadl2_PackageRename", self)
                    

    @property
    def aadl2_PackageSection339(self):
        return self.__aadl2_PackageSection339

    @aadl2_PackageSection339.setter
    def aadl2_PackageSection339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection339", None)
        self.__aadl2_PackageSection339 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ModelUnit"):
                    opp_val = getattr(item, "aadl2_ModelUnit", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ModelUnit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ModelUnit"):
                    opp_val = getattr(item, "aadl2_ModelUnit", None)
                    
                    setattr(item, "aadl2_ModelUnit", self)
                    

    @property
    def aadl2_PackageSection329(self):
        return self.__aadl2_PackageSection329

    @aadl2_PackageSection329.setter
    def aadl2_PackageSection329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection329", None)
        self.__aadl2_PackageSection329 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ComponentTypeRename"):
                    opp_val = getattr(item, "aadl2_ComponentTypeRename", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ComponentTypeRename", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ComponentTypeRename"):
                    opp_val = getattr(item, "aadl2_ComponentTypeRename", None)
                    
                    setattr(item, "aadl2_ComponentTypeRename", self)
                    

    @property
    def aadl2_PackageSection336(self):
        return self.__aadl2_PackageSection336

    @aadl2_PackageSection336.setter
    def aadl2_PackageSection336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection336", None)
        self.__aadl2_PackageSection336 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_AnnexLibrary337"):
                    opp_val = getattr(item, "aadl2_AnnexLibrary337", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_AnnexLibrary337", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_AnnexLibrary337"):
                    opp_val = getattr(item, "aadl2_AnnexLibrary337", None)
                    
                    setattr(item, "aadl2_AnnexLibrary337", self)
                    

class aadl2_EnumerationType(NonListType, Namespace):

    pass
class aadl2_RecordType(NonListType, Namespace):

    pass
class aadl2_GlobalNamespace(Namespace):

    pass
class PropertyOwner:

    pass
class aadl2_ClassifierValue(PropertyValue, PropertyOwner):

    pass
class aadl2_ArraySizeProperty(ABC):

    pass
class TypedElement:

    pass
class aadl2_BasicProperty(TypedElement):

    pass
class aadl2_MetaclassReference(PropertyOwner):

    def __init__(self, annexName: str, metaclassName: str, aadl2_MetaclassReference: "aadl2_Property" = None, aadl2_MetaclassReference848: "aadl2_ReferenceType" = None, aadl2_MetaclassReference839: "aadl2_ClassifierType" = None):
        self.annexName = annexName
        self.metaclassName = metaclassName
        self.aadl2_MetaclassReference = aadl2_MetaclassReference
        self.aadl2_MetaclassReference848 = aadl2_MetaclassReference848
        self.aadl2_MetaclassReference839 = aadl2_MetaclassReference839
        
    @property
    def annexName(self) -> str:
        return self.__annexName

    @annexName.setter
    def annexName(self, annexName: str):
        self.__annexName = annexName

    @property
    def metaclassName(self) -> str:
        return self.__metaclassName

    @metaclassName.setter
    def metaclassName(self, metaclassName: str):
        self.__metaclassName = metaclassName

    @property
    def aadl2_MetaclassReference(self):
        return self.__aadl2_MetaclassReference

    @aadl2_MetaclassReference.setter
    def aadl2_MetaclassReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_MetaclassReference__aadl2_MetaclassReference", None)
        self.__aadl2_MetaclassReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Property16"):
                opp_val = getattr(old_value, "aadl2_Property16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Property16"):
                opp_val = getattr(value, "aadl2_Property16", None)
                if opp_val is None:
                    setattr(value, "aadl2_Property16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_MetaclassReference839(self):
        return self.__aadl2_MetaclassReference839

    @aadl2_MetaclassReference839.setter
    def aadl2_MetaclassReference839(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_MetaclassReference__aadl2_MetaclassReference839", None)
        self.__aadl2_MetaclassReference839 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ClassifierType"):
                opp_val = getattr(old_value, "aadl2_ClassifierType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ClassifierType"):
                opp_val = getattr(value, "aadl2_ClassifierType", None)
                if opp_val is None:
                    setattr(value, "aadl2_ClassifierType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_MetaclassReference848(self):
        return self.__aadl2_MetaclassReference848

    @aadl2_MetaclassReference848.setter
    def aadl2_MetaclassReference848(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_MetaclassReference__aadl2_MetaclassReference848", None)
        self.__aadl2_MetaclassReference848 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ReferenceType"):
                opp_val = getattr(old_value, "aadl2_ReferenceType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ReferenceType"):
                opp_val = getattr(value, "aadl2_ReferenceType", None)
                if opp_val is None:
                    setattr(value, "aadl2_ReferenceType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aadl2_AbstractNamedValue(ABC):

    pass
class Type:

    pass
class aadl2_PropertyType(Type):

    pass
class aadl2_SubcomponentType(Type):

    pass
class AbstractNamedValue:

    pass
class BasicProperty:

    pass
class aadl2_RecordField(BasicProperty):

    pass
class aadl2_ModalPropertyValue(ModalElement):

    pass
class aadl2_Classifier(Namespace, Type):

    def __init__(self, noPrototypes: str, noAnnexes: str, noProperties: str, aadl2_Classifier: "aadl2_PropertyAssociation" = None, aadl2_Classifier19: "aadl2_Property" = None, aadl2_Classifier34: "aadl2_Classifier" = None, aadl2_Classifier32: set["aadl2_Classifier"] = None, featuringClassifier: set["aadl2_ClassifierFeature"] = None, aadl2_Classifier29: set["aadl2_NamedElement"] = None, specific: set["aadl2_Generalization"] = None, aadl2_Classifier36: set["aadl2_AnnexSubclause"] = None, aadl2_Classifier38: set["aadl2_Prototype"] = None, aadl2_Classifier40: set["aadl2_PrototypeBinding"] = None, Classifier: "aadl2_ClassifierFeature" = None, aadl2_Classifier48: "aadl2_Generalization" = None, Classifier50: "aadl2_Generalization" = None, aadl2_Classifier63: "aadl2_RefinableElement" = None, aadl2_Classifier168: "aadl2_Feature" = None, aadl2_Classifier332: "aadl2_PackageSection" = None, aadl2_Classifier790: "aadl2_ClassifierValue" = None):
        self.noPrototypes = noPrototypes
        self.noAnnexes = noAnnexes
        self.noProperties = noProperties
        self.aadl2_Classifier = aadl2_Classifier
        self.aadl2_Classifier19 = aadl2_Classifier19
        self.aadl2_Classifier34 = aadl2_Classifier34
        self.aadl2_Classifier32 = aadl2_Classifier32 if aadl2_Classifier32 is not None else set()
        self.featuringClassifier = featuringClassifier if featuringClassifier is not None else set()
        self.aadl2_Classifier29 = aadl2_Classifier29 if aadl2_Classifier29 is not None else set()
        self.specific = specific if specific is not None else set()
        self.aadl2_Classifier36 = aadl2_Classifier36 if aadl2_Classifier36 is not None else set()
        self.aadl2_Classifier38 = aadl2_Classifier38 if aadl2_Classifier38 is not None else set()
        self.aadl2_Classifier40 = aadl2_Classifier40 if aadl2_Classifier40 is not None else set()
        self.Classifier = Classifier
        self.aadl2_Classifier48 = aadl2_Classifier48
        self.Classifier50 = Classifier50
        self.aadl2_Classifier63 = aadl2_Classifier63
        self.aadl2_Classifier168 = aadl2_Classifier168
        self.aadl2_Classifier332 = aadl2_Classifier332
        self.aadl2_Classifier790 = aadl2_Classifier790
        
    @property
    def noAnnexes(self) -> str:
        return self.__noAnnexes

    @noAnnexes.setter
    def noAnnexes(self, noAnnexes: str):
        self.__noAnnexes = noAnnexes

    @property
    def noPrototypes(self) -> str:
        return self.__noPrototypes

    @noPrototypes.setter
    def noPrototypes(self, noPrototypes: str):
        self.__noPrototypes = noPrototypes

    @property
    def noProperties(self) -> str:
        return self.__noProperties

    @noProperties.setter
    def noProperties(self, noProperties: str):
        self.__noProperties = noProperties

    @property
    def aadl2_Classifier34(self):
        return self.__aadl2_Classifier34

    @aadl2_Classifier34.setter
    def aadl2_Classifier34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier34", None)
        self.__aadl2_Classifier34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Classifier32"):
                opp_val = getattr(old_value, "aadl2_Classifier32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Classifier32"):
                opp_val = getattr(value, "aadl2_Classifier32", None)
                if opp_val is None:
                    setattr(value, "aadl2_Classifier32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_Classifier19(self):
        return self.__aadl2_Classifier19

    @aadl2_Classifier19.setter
    def aadl2_Classifier19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier19", None)
        self.__aadl2_Classifier19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Property18"):
                opp_val = getattr(old_value, "aadl2_Property18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Property18"):
                opp_val = getattr(value, "aadl2_Property18", None)
                if opp_val is None:
                    setattr(value, "aadl2_Property18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_Classifier168(self):
        return self.__aadl2_Classifier168

    @aadl2_Classifier168.setter
    def aadl2_Classifier168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier168", None)
        self.__aadl2_Classifier168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Feature167"):
                opp_val = getattr(old_value, "aadl2_Feature167", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Feature167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Feature167"):
                opp_val = getattr(value, "aadl2_Feature167", None)
                setattr(value, "aadl2_Feature167", self)

    @property
    def aadl2_Classifier63(self):
        return self.__aadl2_Classifier63

    @aadl2_Classifier63.setter
    def aadl2_Classifier63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier63", None)
        self.__aadl2_Classifier63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_RefinableElement"):
                opp_val = getattr(old_value, "aadl2_RefinableElement", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_RefinableElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_RefinableElement"):
                opp_val = getattr(value, "aadl2_RefinableElement", None)
                setattr(value, "aadl2_RefinableElement", self)

    @property
    def aadl2_Classifier29(self):
        return self.__aadl2_Classifier29

    @aadl2_Classifier29.setter
    def aadl2_Classifier29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier29", None)
        self.__aadl2_Classifier29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_NamedElement30"):
                    opp_val = getattr(item, "aadl2_NamedElement30", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_NamedElement30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_NamedElement30"):
                    opp_val = getattr(item, "aadl2_NamedElement30", None)
                    
                    setattr(item, "aadl2_NamedElement30", self)
                    

    @property
    def specific(self):
        return self.__specific

    @specific.setter
    def specific(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__specific", None)
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
    def featuringClassifier(self):
        return self.__featuringClassifier

    @featuringClassifier.setter
    def featuringClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__featuringClassifier", None)
        self.__featuringClassifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassifierFeature"):
                    opp_val = getattr(item, "ClassifierFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassifierFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassifierFeature"):
                    opp_val = getattr(item, "ClassifierFeature", None)
                    
                    setattr(item, "ClassifierFeature", self)
                    

    @property
    def aadl2_Classifier32(self):
        return self.__aadl2_Classifier32

    @aadl2_Classifier32.setter
    def aadl2_Classifier32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier32", None)
        self.__aadl2_Classifier32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_Classifier34"):
                    opp_val = getattr(item, "aadl2_Classifier34", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Classifier34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Classifier34"):
                    opp_val = getattr(item, "aadl2_Classifier34", None)
                    
                    setattr(item, "aadl2_Classifier34", self)
                    

    @property
    def aadl2_Classifier38(self):
        return self.__aadl2_Classifier38

    @aadl2_Classifier38.setter
    def aadl2_Classifier38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier38", None)
        self.__aadl2_Classifier38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_Prototype"):
                    opp_val = getattr(item, "aadl2_Prototype", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Prototype", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Prototype"):
                    opp_val = getattr(item, "aadl2_Prototype", None)
                    
                    setattr(item, "aadl2_Prototype", self)
                    

    @property
    def aadl2_Classifier48(self):
        return self.__aadl2_Classifier48

    @aadl2_Classifier48.setter
    def aadl2_Classifier48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier48", None)
        self.__aadl2_Classifier48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Generalization"):
                opp_val = getattr(old_value, "aadl2_Generalization", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Generalization"):
                opp_val = getattr(value, "aadl2_Generalization", None)
                setattr(value, "aadl2_Generalization", self)

    @property
    def aadl2_Classifier(self):
        return self.__aadl2_Classifier

    @aadl2_Classifier.setter
    def aadl2_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier", None)
        self.__aadl2_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PropertyAssociation10"):
                opp_val = getattr(old_value, "aadl2_PropertyAssociation10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PropertyAssociation10"):
                opp_val = getattr(value, "aadl2_PropertyAssociation10", None)
                if opp_val is None:
                    setattr(value, "aadl2_PropertyAssociation10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__Classifier", None)
        self.__Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classifierFeature"):
                opp_val = getattr(old_value, "classifierFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classifierFeature"):
                opp_val = getattr(value, "classifierFeature", None)
                if opp_val is None:
                    setattr(value, "classifierFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_Classifier40(self):
        return self.__aadl2_Classifier40

    @aadl2_Classifier40.setter
    def aadl2_Classifier40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier40", None)
        self.__aadl2_Classifier40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_PrototypeBinding"):
                    opp_val = getattr(item, "aadl2_PrototypeBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_PrototypeBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_PrototypeBinding"):
                    opp_val = getattr(item, "aadl2_PrototypeBinding", None)
                    
                    setattr(item, "aadl2_PrototypeBinding", self)
                    

    @property
    def aadl2_Classifier36(self):
        return self.__aadl2_Classifier36

    @aadl2_Classifier36.setter
    def aadl2_Classifier36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier36", None)
        self.__aadl2_Classifier36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_AnnexSubclause"):
                    opp_val = getattr(item, "aadl2_AnnexSubclause", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_AnnexSubclause", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_AnnexSubclause"):
                    opp_val = getattr(item, "aadl2_AnnexSubclause", None)
                    
                    setattr(item, "aadl2_AnnexSubclause", self)
                    

    @property
    def aadl2_Classifier790(self):
        return self.__aadl2_Classifier790

    @aadl2_Classifier790.setter
    def aadl2_Classifier790(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier790", None)
        self.__aadl2_Classifier790 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ClassifierValue"):
                opp_val = getattr(old_value, "aadl2_ClassifierValue", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ClassifierValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ClassifierValue"):
                opp_val = getattr(value, "aadl2_ClassifierValue", None)
                setattr(value, "aadl2_ClassifierValue", self)

    @property
    def Classifier50(self):
        return self.__Classifier50

    @Classifier50.setter
    def Classifier50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__Classifier50", None)
        self.__Classifier50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generalization"):
                opp_val = getattr(old_value, "generalization", None)
                if opp_val == self:
                    setattr(old_value, "generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generalization"):
                opp_val = getattr(value, "generalization", None)
                setattr(value, "generalization", self)

    @property
    def aadl2_Classifier332(self):
        return self.__aadl2_Classifier332

    @aadl2_Classifier332.setter
    def aadl2_Classifier332(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier332", None)
        self.__aadl2_Classifier332 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PackageSection331"):
                opp_val = getattr(old_value, "aadl2_PackageSection331", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PackageSection331"):
                opp_val = getattr(value, "aadl2_PackageSection331", None)
                if opp_val is None:
                    setattr(value, "aadl2_PackageSection331", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def allFeatures(self) -> str:
        # TODO: Implement allFeatures method
        pass

    def inherit(self, inhs: NamedElement) -> NamedElement:
        # TODO: Implement inherit method
        pass

    def parents(self) -> str:
        # TODO: Implement parents method
        pass

    def inheritableMembers(self, c: str) -> NamedElement:
        # TODO: Implement inheritableMembers method
        pass

    def specialize_type(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement specialize_type method
        pass

    def allParents(self) -> str:
        # TODO: Implement allParents method
        pass

    def no_cycles_in_generalization(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement no_cycles_in_generalization method
        pass

    def maySpecializeType(self, c: str) -> str:
        # TODO: Implement maySpecializeType method
        pass

    def inheritedMember(self) -> NamedElement:
        # TODO: Implement inheritedMember method
        pass

    def hasVisibilityOf(self, n: NamedElement) -> str:
        # TODO: Implement hasVisibilityOf method
        pass

class ArraySizeProperty:

    pass
class aadl2_Property(AbstractNamedValue, BasicProperty, ArraySizeProperty):

    def __init__(self, inherit: str, emptyListDefault: str, aadl2_Property14: "aadl2_PropertyExpression" = None, aadl2_Property: "aadl2_PropertyAssociation" = None, aadl2_Property16: set["aadl2_MetaclassReference"] = None, aadl2_Property18: set["aadl2_Classifier"] = None, aadl2_Property21: set["aadl2_PropertyOwner"] = None, aadl2_Property810: "aadl2_PropertySet" = None):
        self.inherit = inherit
        self.emptyListDefault = emptyListDefault
        self.aadl2_Property14 = aadl2_Property14
        self.aadl2_Property = aadl2_Property
        self.aadl2_Property16 = aadl2_Property16 if aadl2_Property16 is not None else set()
        self.aadl2_Property18 = aadl2_Property18 if aadl2_Property18 is not None else set()
        self.aadl2_Property21 = aadl2_Property21 if aadl2_Property21 is not None else set()
        self.aadl2_Property810 = aadl2_Property810
        
    @property
    def emptyListDefault(self) -> str:
        return self.__emptyListDefault

    @emptyListDefault.setter
    def emptyListDefault(self, emptyListDefault: str):
        self.__emptyListDefault = emptyListDefault

    @property
    def inherit(self) -> str:
        return self.__inherit

    @inherit.setter
    def inherit(self, inherit: str):
        self.__inherit = inherit

    @property
    def aadl2_Property(self):
        return self.__aadl2_Property

    @aadl2_Property.setter
    def aadl2_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Property__aadl2_Property", None)
        self.__aadl2_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PropertyAssociation6"):
                opp_val = getattr(old_value, "aadl2_PropertyAssociation6", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_PropertyAssociation6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PropertyAssociation6"):
                opp_val = getattr(value, "aadl2_PropertyAssociation6", None)
                setattr(value, "aadl2_PropertyAssociation6", self)

    @property
    def aadl2_Property16(self):
        return self.__aadl2_Property16

    @aadl2_Property16.setter
    def aadl2_Property16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Property__aadl2_Property16", None)
        self.__aadl2_Property16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_MetaclassReference"):
                    opp_val = getattr(item, "aadl2_MetaclassReference", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_MetaclassReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_MetaclassReference"):
                    opp_val = getattr(item, "aadl2_MetaclassReference", None)
                    
                    setattr(item, "aadl2_MetaclassReference", self)
                    

    @property
    def aadl2_Property810(self):
        return self.__aadl2_Property810

    @aadl2_Property810.setter
    def aadl2_Property810(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Property__aadl2_Property810", None)
        self.__aadl2_Property810 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PropertySet809"):
                opp_val = getattr(old_value, "aadl2_PropertySet809", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PropertySet809"):
                opp_val = getattr(value, "aadl2_PropertySet809", None)
                if opp_val is None:
                    setattr(value, "aadl2_PropertySet809", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_Property14(self):
        return self.__aadl2_Property14

    @aadl2_Property14.setter
    def aadl2_Property14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Property__aadl2_Property14", None)
        self.__aadl2_Property14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PropertyExpression"):
                opp_val = getattr(old_value, "aadl2_PropertyExpression", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_PropertyExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PropertyExpression"):
                opp_val = getattr(value, "aadl2_PropertyExpression", None)
                setattr(value, "aadl2_PropertyExpression", self)

    @property
    def aadl2_Property21(self):
        return self.__aadl2_Property21

    @aadl2_Property21.setter
    def aadl2_Property21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Property__aadl2_Property21", None)
        self.__aadl2_Property21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_PropertyOwner"):
                    opp_val = getattr(item, "aadl2_PropertyOwner", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_PropertyOwner", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_PropertyOwner"):
                    opp_val = getattr(item, "aadl2_PropertyOwner", None)
                    
                    setattr(item, "aadl2_PropertyOwner", self)
                    

    @property
    def aadl2_Property18(self):
        return self.__aadl2_Property18

    @aadl2_Property18.setter
    def aadl2_Property18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Property__aadl2_Property18", None)
        self.__aadl2_Property18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_Classifier19"):
                    opp_val = getattr(item, "aadl2_Classifier19", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Classifier19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Classifier19"):
                    opp_val = getattr(item, "aadl2_Classifier19", None)
                    
                    setattr(item, "aadl2_Classifier19", self)
                    

class aadl2_PropertyConstant(TypedElement, AbstractNamedValue, ArraySizeProperty):

    pass
class NamedElement:

    pass
class aadl2_RefinableElement(NamedElement):

    pass
class aadl2_ThreadGroup(NamedElement):

    pass
class aadl2_VirtualProcessor(NamedElement):

    pass
class aadl2_ConnectionEnd(NamedElement):

    pass
class aadl2_Data(NamedElement):

    pass
class aadl2_Device(NamedElement):

    pass
class aadl2_ComponentTypeRename(NamedElement):

    def __init__(self, category: str, aadl2_ComponentTypeRename: "aadl2_PackageSection" = None, aadl2_ComponentTypeRename354: "aadl2_ComponentType" = None):
        self.category = category
        self.aadl2_ComponentTypeRename = aadl2_ComponentTypeRename
        self.aadl2_ComponentTypeRename354 = aadl2_ComponentTypeRename354
        
    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def aadl2_ComponentTypeRename354(self):
        return self.__aadl2_ComponentTypeRename354

    @aadl2_ComponentTypeRename354.setter
    def aadl2_ComponentTypeRename354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentTypeRename__aadl2_ComponentTypeRename354", None)
        self.__aadl2_ComponentTypeRename354 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentType355"):
                opp_val = getattr(old_value, "aadl2_ComponentType355", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentType355", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentType355"):
                opp_val = getattr(value, "aadl2_ComponentType355", None)
                setattr(value, "aadl2_ComponentType355", self)

    @property
    def aadl2_ComponentTypeRename(self):
        return self.__aadl2_ComponentTypeRename

    @aadl2_ComponentTypeRename.setter
    def aadl2_ComponentTypeRename(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentTypeRename__aadl2_ComponentTypeRename", None)
        self.__aadl2_ComponentTypeRename = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PackageSection329"):
                opp_val = getattr(old_value, "aadl2_PackageSection329", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PackageSection329"):
                opp_val = getattr(value, "aadl2_PackageSection329", None)
                if opp_val is None:
                    setattr(value, "aadl2_PackageSection329", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aadl2_ModalElement(NamedElement):

    def __init__(self, aadl2_ModalElement: set["aadl2_Mode"] = None):
        self.aadl2_ModalElement = aadl2_ModalElement if aadl2_ModalElement is not None else set()
        
    @property
    def aadl2_ModalElement(self):
        return self.__aadl2_ModalElement

    @aadl2_ModalElement.setter
    def aadl2_ModalElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ModalElement__aadl2_ModalElement", None)
        self.__aadl2_ModalElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_Mode"):
                    opp_val = getattr(item, "aadl2_Mode", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Mode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Mode"):
                    opp_val = getattr(item, "aadl2_Mode", None)
                    
                    setattr(item, "aadl2_Mode", self)
                    

    def getAllInModes(self) -> str:
        # TODO: Implement getAllInModes method
        pass

class aadl2_ModelUnit(NamedElement):

    pass
class aadl2_FeatureGroupTypeRename(NamedElement):

    pass
class aadl2_AnnexLibrary(NamedElement):

    pass
class aadl2_EnumerationLiteral(AbstractNamedValue, NamedElement):

    pass
class aadl2_Namespace(NamedElement):

    def __init__(self, aadl2_Namespace: set["aadl2_NamedElement"] = None, aadl2_Namespace44: set["aadl2_NamedElement"] = None):
        self.aadl2_Namespace = aadl2_Namespace if aadl2_Namespace is not None else set()
        self.aadl2_Namespace44 = aadl2_Namespace44 if aadl2_Namespace44 is not None else set()
        
    @property
    def aadl2_Namespace44(self):
        return self.__aadl2_Namespace44

    @aadl2_Namespace44.setter
    def aadl2_Namespace44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Namespace__aadl2_Namespace44", None)
        self.__aadl2_Namespace44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_NamedElement45"):
                    opp_val = getattr(item, "aadl2_NamedElement45", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_NamedElement45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_NamedElement45"):
                    opp_val = getattr(item, "aadl2_NamedElement45", None)
                    
                    setattr(item, "aadl2_NamedElement45", self)
                    

    @property
    def aadl2_Namespace(self):
        return self.__aadl2_Namespace

    @aadl2_Namespace.setter
    def aadl2_Namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Namespace__aadl2_Namespace", None)
        self.__aadl2_Namespace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_NamedElement42"):
                    opp_val = getattr(item, "aadl2_NamedElement42", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_NamedElement42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_NamedElement42"):
                    opp_val = getattr(item, "aadl2_NamedElement42", None)
                    
                    setattr(item, "aadl2_NamedElement42", self)
                    

    def membersAreDistinguishable(self) -> str:
        # TODO: Implement membersAreDistinguishable method
        pass

    def members_distinguishable(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement members_distinguishable method
        pass

    def getNamesOfMember(self, element: NamedElement) -> str:
        # TODO: Implement getNamesOfMember method
        pass

class aadl2_Abstract(NamedElement):

    pass
class aadl2_Bus(NamedElement):

    pass
class aadl2_Subprogram(CalledSubprogram, NamedElement):

    pass
class aadl2_TypedElement(NamedElement):

    pass
class aadl2_EndToEndFlowElement(NamedElement):

    pass
class aadl2_Flow(NamedElement):

    pass
class aadl2_Processor(NamedElement):

    pass
class aadl2_Memory(NamedElement):

    pass
class aadl2_SubprogramGroup(NamedElement):

    pass
class aadl2_Process(NamedElement):

    pass
class aadl2_PackageRename(NamedElement):

    def __init__(self, renameAll: str, aadl2_PackageRename: "aadl2_PackageSection" = None, aadl2_PackageRename341: "aadl2_AadlPackage" = None):
        self.renameAll = renameAll
        self.aadl2_PackageRename = aadl2_PackageRename
        self.aadl2_PackageRename341 = aadl2_PackageRename341
        
    @property
    def renameAll(self) -> str:
        return self.__renameAll

    @renameAll.setter
    def renameAll(self, renameAll: str):
        self.__renameAll = renameAll

    @property
    def aadl2_PackageRename(self):
        return self.__aadl2_PackageRename

    @aadl2_PackageRename.setter
    def aadl2_PackageRename(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageRename__aadl2_PackageRename", None)
        self.__aadl2_PackageRename = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PackageSection"):
                opp_val = getattr(old_value, "aadl2_PackageSection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PackageSection"):
                opp_val = getattr(value, "aadl2_PackageSection", None)
                if opp_val is None:
                    setattr(value, "aadl2_PackageSection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_PackageRename341(self):
        return self.__aadl2_PackageRename341

    @aadl2_PackageRename341.setter
    def aadl2_PackageRename341(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageRename__aadl2_PackageRename341", None)
        self.__aadl2_PackageRename341 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_AadlPackage"):
                opp_val = getattr(old_value, "aadl2_AadlPackage", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_AadlPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_AadlPackage"):
                opp_val = getattr(value, "aadl2_AadlPackage", None)
                setattr(value, "aadl2_AadlPackage", self)

class aadl2_ClassifierFeature(NamedElement):

    pass
class aadl2_Thread(NamedElement):

    pass
class aadl2_System(NamedElement):

    pass
class aadl2_TriggerPort(NamedElement):

    pass
class aadl2_VirtualBus(NamedElement):

    pass
class aadl2_Context(NamedElement):

    pass
class aadl2_Type(NamedElement):

    def __init__(self, aadl2_Type: "aadl2_TypedElement" = None):
        self.aadl2_Type = aadl2_Type
        
    @property
    def aadl2_Type(self):
        return self.__aadl2_Type

    @aadl2_Type.setter
    def aadl2_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Type__aadl2_Type", None)
        self.__aadl2_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_TypedElement"):
                opp_val = getattr(old_value, "aadl2_TypedElement", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_TypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_TypedElement"):
                opp_val = getattr(value, "aadl2_TypedElement", None)
                setattr(value, "aadl2_TypedElement", self)

    def conformsTo(self, other: str) -> str:
        # TODO: Implement conformsTo method
        pass

class Element:

    pass
class aadl2_ArrayableElement(Element):

    pass
class aadl2_PropertyAssociation(Element):

    def __init__(self, append: str, constant: str, aadl2_PropertyAssociation: "aadl2_NamedElement" = None, aadl2_PropertyAssociation6: "aadl2_Property" = None, aadl2_PropertyAssociation8: set["aadl2_ContainedNamedElement"] = None, aadl2_PropertyAssociation10: set["aadl2_Classifier"] = None, aadl2_PropertyAssociation12: set["aadl2_ModalPropertyValue"] = None):
        self.append = append
        self.constant = constant
        self.aadl2_PropertyAssociation = aadl2_PropertyAssociation
        self.aadl2_PropertyAssociation6 = aadl2_PropertyAssociation6
        self.aadl2_PropertyAssociation8 = aadl2_PropertyAssociation8 if aadl2_PropertyAssociation8 is not None else set()
        self.aadl2_PropertyAssociation10 = aadl2_PropertyAssociation10 if aadl2_PropertyAssociation10 is not None else set()
        self.aadl2_PropertyAssociation12 = aadl2_PropertyAssociation12 if aadl2_PropertyAssociation12 is not None else set()
        
    @property
    def constant(self) -> str:
        return self.__constant

    @constant.setter
    def constant(self, constant: str):
        self.__constant = constant

    @property
    def append(self) -> str:
        return self.__append

    @append.setter
    def append(self, append: str):
        self.__append = append

    @property
    def aadl2_PropertyAssociation8(self):
        return self.__aadl2_PropertyAssociation8

    @aadl2_PropertyAssociation8.setter
    def aadl2_PropertyAssociation8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertyAssociation__aadl2_PropertyAssociation8", None)
        self.__aadl2_PropertyAssociation8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ContainedNamedElement"):
                    opp_val = getattr(item, "aadl2_ContainedNamedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ContainedNamedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ContainedNamedElement"):
                    opp_val = getattr(item, "aadl2_ContainedNamedElement", None)
                    
                    setattr(item, "aadl2_ContainedNamedElement", self)
                    

    @property
    def aadl2_PropertyAssociation12(self):
        return self.__aadl2_PropertyAssociation12

    @aadl2_PropertyAssociation12.setter
    def aadl2_PropertyAssociation12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertyAssociation__aadl2_PropertyAssociation12", None)
        self.__aadl2_PropertyAssociation12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ModalPropertyValue"):
                    opp_val = getattr(item, "aadl2_ModalPropertyValue", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ModalPropertyValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ModalPropertyValue"):
                    opp_val = getattr(item, "aadl2_ModalPropertyValue", None)
                    
                    setattr(item, "aadl2_ModalPropertyValue", self)
                    

    @property
    def aadl2_PropertyAssociation6(self):
        return self.__aadl2_PropertyAssociation6

    @aadl2_PropertyAssociation6.setter
    def aadl2_PropertyAssociation6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertyAssociation__aadl2_PropertyAssociation6", None)
        self.__aadl2_PropertyAssociation6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Property"):
                opp_val = getattr(old_value, "aadl2_Property", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Property"):
                opp_val = getattr(value, "aadl2_Property", None)
                setattr(value, "aadl2_Property", self)

    @property
    def aadl2_PropertyAssociation10(self):
        return self.__aadl2_PropertyAssociation10

    @aadl2_PropertyAssociation10.setter
    def aadl2_PropertyAssociation10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertyAssociation__aadl2_PropertyAssociation10", None)
        self.__aadl2_PropertyAssociation10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_Classifier"):
                    opp_val = getattr(item, "aadl2_Classifier", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Classifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Classifier"):
                    opp_val = getattr(item, "aadl2_Classifier", None)
                    
                    setattr(item, "aadl2_Classifier", self)
                    

    @property
    def aadl2_PropertyAssociation(self):
        return self.__aadl2_PropertyAssociation

    @aadl2_PropertyAssociation.setter
    def aadl2_PropertyAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertyAssociation__aadl2_PropertyAssociation", None)
        self.__aadl2_PropertyAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_NamedElement"):
                opp_val = getattr(old_value, "aadl2_NamedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_NamedElement"):
                opp_val = getattr(value, "aadl2_NamedElement", None)
                if opp_val is None:
                    setattr(value, "aadl2_NamedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aadl2_PropertyOwner(Element):

    pass
class aadl2_ComponentImplementationReference(Element):

    pass
class aadl2_ArraySize(Element):

    def __init__(self, size: str, aadl2_ArraySize: "aadl2_ArrayDimension" = None, aadl2_ArraySize82: "aadl2_ArraySizeProperty" = None):
        self.size = size
        self.aadl2_ArraySize = aadl2_ArraySize
        self.aadl2_ArraySize82 = aadl2_ArraySize82
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def aadl2_ArraySize(self):
        return self.__aadl2_ArraySize

    @aadl2_ArraySize.setter
    def aadl2_ArraySize(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ArraySize__aadl2_ArraySize", None)
        self.__aadl2_ArraySize = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ArrayDimension"):
                opp_val = getattr(old_value, "aadl2_ArrayDimension", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ArrayDimension", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ArrayDimension"):
                opp_val = getattr(value, "aadl2_ArrayDimension", None)
                setattr(value, "aadl2_ArrayDimension", self)

    @property
    def aadl2_ArraySize82(self):
        return self.__aadl2_ArraySize82

    @aadl2_ArraySize82.setter
    def aadl2_ArraySize82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ArraySize__aadl2_ArraySize82", None)
        self.__aadl2_ArraySize82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ArraySizeProperty"):
                opp_val = getattr(old_value, "aadl2_ArraySizeProperty", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ArraySizeProperty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ArraySizeProperty"):
                opp_val = getattr(value, "aadl2_ArraySizeProperty", None)
                setattr(value, "aadl2_ArraySizeProperty", self)

class aadl2_ArrayRange(Element):

    def __init__(self, lowerBound: str, upperBound: str, aadl2_ArrayRange: "aadl2_ContainmentPathElement" = None):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.aadl2_ArrayRange = aadl2_ArrayRange
        
    @property
    def upperBound(self) -> str:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: str):
        self.__upperBound = upperBound

    @property
    def lowerBound(self) -> str:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: str):
        self.__lowerBound = lowerBound

    @property
    def aadl2_ArrayRange(self):
        return self.__aadl2_ArrayRange

    @aadl2_ArrayRange.setter
    def aadl2_ArrayRange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ArrayRange__aadl2_ArrayRange", None)
        self.__aadl2_ArrayRange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ContainmentPathElement73"):
                opp_val = getattr(old_value, "aadl2_ContainmentPathElement73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ContainmentPathElement73"):
                opp_val = getattr(value, "aadl2_ContainmentPathElement73", None)
                if opp_val is None:
                    setattr(value, "aadl2_ContainmentPathElement73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aadl2_Relationship(Element):

    pass
class aadl2_BasicPropertyAssociation(Element):

    pass
class aadl2_ConnectedElement(Element):

    pass
class aadl2_EndToEndFlowSegment(Element):

    pass
class aadl2_FlowEnd(Element):

    pass
class aadl2_PropertyExpression(Element):

    pass
class aadl2_NamedElement(Element):

    def __init__(self, qualifiedName: str, name: str, aadl2_NamedElement: set["aadl2_PropertyAssociation"] = None, aadl2_NamedElement30: "aadl2_Classifier" = None, aadl2_NamedElement42: "aadl2_Namespace" = None, aadl2_NamedElement45: "aadl2_Namespace" = None, aadl2_NamedElement76: "aadl2_ContainmentPathElement" = None):
        self.qualifiedName = qualifiedName
        self.name = name
        self.aadl2_NamedElement = aadl2_NamedElement if aadl2_NamedElement is not None else set()
        self.aadl2_NamedElement30 = aadl2_NamedElement30
        self.aadl2_NamedElement42 = aadl2_NamedElement42
        self.aadl2_NamedElement45 = aadl2_NamedElement45
        self.aadl2_NamedElement76 = aadl2_NamedElement76
        
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
    def aadl2_NamedElement42(self):
        return self.__aadl2_NamedElement42

    @aadl2_NamedElement42.setter
    def aadl2_NamedElement42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_NamedElement__aadl2_NamedElement42", None)
        self.__aadl2_NamedElement42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Namespace"):
                opp_val = getattr(old_value, "aadl2_Namespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Namespace"):
                opp_val = getattr(value, "aadl2_Namespace", None)
                if opp_val is None:
                    setattr(value, "aadl2_Namespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_NamedElement(self):
        return self.__aadl2_NamedElement

    @aadl2_NamedElement.setter
    def aadl2_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_NamedElement__aadl2_NamedElement", None)
        self.__aadl2_NamedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_PropertyAssociation"):
                    opp_val = getattr(item, "aadl2_PropertyAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_PropertyAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_PropertyAssociation"):
                    opp_val = getattr(item, "aadl2_PropertyAssociation", None)
                    
                    setattr(item, "aadl2_PropertyAssociation", self)
                    

    @property
    def aadl2_NamedElement45(self):
        return self.__aadl2_NamedElement45

    @aadl2_NamedElement45.setter
    def aadl2_NamedElement45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_NamedElement__aadl2_NamedElement45", None)
        self.__aadl2_NamedElement45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Namespace44"):
                opp_val = getattr(old_value, "aadl2_Namespace44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Namespace44"):
                opp_val = getattr(value, "aadl2_Namespace44", None)
                if opp_val is None:
                    setattr(value, "aadl2_Namespace44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_NamedElement76(self):
        return self.__aadl2_NamedElement76

    @aadl2_NamedElement76.setter
    def aadl2_NamedElement76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_NamedElement__aadl2_NamedElement76", None)
        self.__aadl2_NamedElement76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ContainmentPathElement75"):
                opp_val = getattr(old_value, "aadl2_ContainmentPathElement75", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ContainmentPathElement75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ContainmentPathElement75"):
                opp_val = getattr(value, "aadl2_ContainmentPathElement75", None)
                setattr(value, "aadl2_ContainmentPathElement75", self)

    @property
    def aadl2_NamedElement30(self):
        return self.__aadl2_NamedElement30

    @aadl2_NamedElement30.setter
    def aadl2_NamedElement30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_NamedElement__aadl2_NamedElement30", None)
        self.__aadl2_NamedElement30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Classifier29"):
                opp_val = getattr(old_value, "aadl2_Classifier29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Classifier29"):
                opp_val = getattr(value, "aadl2_Classifier29", None)
                if opp_val is None:
                    setattr(value, "aadl2_Classifier29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getNamespace(self) -> str:
        # TODO: Implement getNamespace method
        pass

    def separator(self) -> str:
        # TODO: Implement separator method
        pass

    def isDistinguishableFrom(self, n: NamedElement, ns: str) -> str:
        # TODO: Implement isDistinguishableFrom method
        pass

    def has_no_qualified_name(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement has_no_qualified_name method
        pass

    def qualifiedName(self) -> str:
        # TODO: Implement qualifiedName method
        pass

    def has_qualified_name(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement has_qualified_name method
        pass

    def allNamespaces(self) -> str:
        # TODO: Implement allNamespaces method
        pass

    def getPropertyValues(self, propertySetName: str, propertyName: str) -> str:
        # TODO: Implement getPropertyValues method
        pass

class aadl2_ContainedNamedElement(Element):

    pass
class aadl2_PrototypeBinding(Element):

    pass
class aadl2_ModeTransitionTrigger(Element):

    pass
class aadl2_FlowSegment(Element):

    pass
class aadl2_NumericRange(Element):

    pass
class aadl2_ContainmentPathElement(Element):

    def __init__(self, annexName: str, aadl2_ContainmentPathElement: "aadl2_ContainedNamedElement" = None, aadl2_ContainmentPathElement73: set["aadl2_ArrayRange"] = None, aadl2_ContainmentPathElement75: "aadl2_NamedElement" = None):
        self.annexName = annexName
        self.aadl2_ContainmentPathElement = aadl2_ContainmentPathElement
        self.aadl2_ContainmentPathElement73 = aadl2_ContainmentPathElement73 if aadl2_ContainmentPathElement73 is not None else set()
        self.aadl2_ContainmentPathElement75 = aadl2_ContainmentPathElement75
        
    @property
    def annexName(self) -> str:
        return self.__annexName

    @annexName.setter
    def annexName(self, annexName: str):
        self.__annexName = annexName

    @property
    def aadl2_ContainmentPathElement75(self):
        return self.__aadl2_ContainmentPathElement75

    @aadl2_ContainmentPathElement75.setter
    def aadl2_ContainmentPathElement75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ContainmentPathElement__aadl2_ContainmentPathElement75", None)
        self.__aadl2_ContainmentPathElement75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_NamedElement76"):
                opp_val = getattr(old_value, "aadl2_NamedElement76", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_NamedElement76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_NamedElement76"):
                opp_val = getattr(value, "aadl2_NamedElement76", None)
                setattr(value, "aadl2_NamedElement76", self)

    @property
    def aadl2_ContainmentPathElement(self):
        return self.__aadl2_ContainmentPathElement

    @aadl2_ContainmentPathElement.setter
    def aadl2_ContainmentPathElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ContainmentPathElement__aadl2_ContainmentPathElement", None)
        self.__aadl2_ContainmentPathElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ContainedNamedElement71"):
                opp_val = getattr(old_value, "aadl2_ContainedNamedElement71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ContainedNamedElement71"):
                opp_val = getattr(value, "aadl2_ContainedNamedElement71", None)
                if opp_val is None:
                    setattr(value, "aadl2_ContainedNamedElement71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_ContainmentPathElement73(self):
        return self.__aadl2_ContainmentPathElement73

    @aadl2_ContainmentPathElement73.setter
    def aadl2_ContainmentPathElement73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ContainmentPathElement__aadl2_ContainmentPathElement73", None)
        self.__aadl2_ContainmentPathElement73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ArrayRange"):
                    opp_val = getattr(item, "aadl2_ArrayRange", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ArrayRange", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ArrayRange"):
                    opp_val = getattr(item, "aadl2_ArrayRange", None)
                    
                    setattr(item, "aadl2_ArrayRange", self)
                    

class aadl2_ModeBinding(Element):

    pass
class aadl2_ArrayDimension(Element):

    pass
class aadl2_Comment(Element):

    def __init__(self, body: str, aadl2_Comment: "aadl2_Element" = None):
        self.body = body
        self.aadl2_Comment = aadl2_Comment
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def aadl2_Comment(self):
        return self.__aadl2_Comment

    @aadl2_Comment.setter
    def aadl2_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Comment__aadl2_Comment", None)
        self.__aadl2_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Element3"):
                opp_val = getattr(old_value, "aadl2_Element3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Element3"):
                opp_val = getattr(value, "aadl2_Element3", None)
                if opp_val is None:
                    setattr(value, "aadl2_Element3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aadl2_Element(ABC):

    def __init__(self, aadl2_Element: "aadl2_Element" = None, aadl2_Element0: set["aadl2_Element"] = None, aadl2_Element3: set["aadl2_Comment"] = None, aadl2_Element52: "aadl2_DirectedRelationship" = None, aadl2_Element55: "aadl2_DirectedRelationship" = None, aadl2_Element57: "aadl2_Relationship" = None):
        self.aadl2_Element = aadl2_Element
        self.aadl2_Element0 = aadl2_Element0 if aadl2_Element0 is not None else set()
        self.aadl2_Element3 = aadl2_Element3 if aadl2_Element3 is not None else set()
        self.aadl2_Element52 = aadl2_Element52
        self.aadl2_Element55 = aadl2_Element55
        self.aadl2_Element57 = aadl2_Element57
        
    @property
    def aadl2_Element3(self):
        return self.__aadl2_Element3

    @aadl2_Element3.setter
    def aadl2_Element3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Element__aadl2_Element3", None)
        self.__aadl2_Element3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_Comment"):
                    opp_val = getattr(item, "aadl2_Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Comment"):
                    opp_val = getattr(item, "aadl2_Comment", None)
                    
                    setattr(item, "aadl2_Comment", self)
                    

    @property
    def aadl2_Element0(self):
        return self.__aadl2_Element0

    @aadl2_Element0.setter
    def aadl2_Element0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Element__aadl2_Element0", None)
        self.__aadl2_Element0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_Element"):
                    opp_val = getattr(item, "aadl2_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Element"):
                    opp_val = getattr(item, "aadl2_Element", None)
                    
                    setattr(item, "aadl2_Element", self)
                    

    @property
    def aadl2_Element57(self):
        return self.__aadl2_Element57

    @aadl2_Element57.setter
    def aadl2_Element57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Element__aadl2_Element57", None)
        self.__aadl2_Element57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Relationship"):
                opp_val = getattr(old_value, "aadl2_Relationship", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Relationship"):
                opp_val = getattr(value, "aadl2_Relationship", None)
                if opp_val is None:
                    setattr(value, "aadl2_Relationship", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_Element52(self):
        return self.__aadl2_Element52

    @aadl2_Element52.setter
    def aadl2_Element52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Element__aadl2_Element52", None)
        self.__aadl2_Element52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_DirectedRelationship"):
                opp_val = getattr(old_value, "aadl2_DirectedRelationship", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_DirectedRelationship"):
                opp_val = getattr(value, "aadl2_DirectedRelationship", None)
                if opp_val is None:
                    setattr(value, "aadl2_DirectedRelationship", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_Element(self):
        return self.__aadl2_Element

    @aadl2_Element.setter
    def aadl2_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Element__aadl2_Element", None)
        self.__aadl2_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Element0"):
                opp_val = getattr(old_value, "aadl2_Element0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Element0"):
                opp_val = getattr(value, "aadl2_Element0", None)
                if opp_val is None:
                    setattr(value, "aadl2_Element0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_Element55(self):
        return self.__aadl2_Element55

    @aadl2_Element55.setter
    def aadl2_Element55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Element__aadl2_Element55", None)
        self.__aadl2_Element55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_DirectedRelationship54"):
                opp_val = getattr(old_value, "aadl2_DirectedRelationship54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_DirectedRelationship54"):
                opp_val = getattr(value, "aadl2_DirectedRelationship54", None)
                if opp_val is None:
                    setattr(value, "aadl2_DirectedRelationship54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getOwner(self) -> str:
        # TODO: Implement getOwner method
        pass

    def has_owner(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement has_owner method
        pass

    def allOwnedElements(self) -> str:
        # TODO: Implement allOwnedElements method
        pass

    def mustBeOwned(self) -> str:
        # TODO: Implement mustBeOwned method
        pass

    def not_own_self(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement not_own_self method
        pass
