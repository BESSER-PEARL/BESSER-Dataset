from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FlowKind(Enum):
    source = "source"
    path = "path"
    sink = "sink"
class PortCategory(Enum):
    data = "data"
    event = "event"
    eventData = "eventData"
class OperationKind(Enum):
    and = "and"
    or = "or"
    not = "not"
    plus = "plus"
    minus = "minus"
class AccessCategory(Enum):
    bus = "bus"
    data = "data"
    subprogram = "subprogram"
    subprogramGroup = "subprogramGroup"
    virtualBus = "virtualBus"
class ComponentCategory(Enum):
    abstract = "abstract"
    bus = "bus"
    data = "data"
    device = "device"
    memory = "memory"
    process = "process"
    processor = "processor"
    subprogram = "subprogram"
    subprogramGroup = "subprogramGroup"
    system = "system"
    thread = "thread"
    threadGroup = "threadGroup"
    virtualBus = "virtualBus"
    virtualProcessor = "virtualProcessor"
class AccessType(Enum):
    provides = "provides"
    requires = "requires"
class DirectionType(Enum):
    out = "out"
    inOut = "inOut"
    in = "in"


############################################
# Definition of Classes
############################################

class EnumerationType:

    pass
class NonListType:

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
class aadl2_UnitsType(EnumerationType):

    pass
class aadl2_NumberType(NonListType):

    pass
class NumberType:

    pass
class aadl2_AadlReal(NumberType):

    pass
class aadl2_AadlInteger(NumberType):

    pass
class aadl2_AadlString(NonListType):

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
class EnumerationLiteral:

    pass
class aadl2_UnitLiteral(EnumerationLiteral):

    def __init__(self, aadl2_UnitLiteral820: "aadl2_UnitLiteral" = None, aadl2_UnitLiteral818: "aadl2_UnitLiteral" = None, aadl2_UnitLiteral822: "aadl2_NumberValue" = None, aadl2_UnitLiteral: "aadl2_NumberValue" = None):
        self.aadl2_UnitLiteral820 = aadl2_UnitLiteral820
        self.aadl2_UnitLiteral818 = aadl2_UnitLiteral818
        self.aadl2_UnitLiteral822 = aadl2_UnitLiteral822
        self.aadl2_UnitLiteral = aadl2_UnitLiteral
        
    @property
    def aadl2_UnitLiteral822(self):
        return self.__aadl2_UnitLiteral822

    @aadl2_UnitLiteral822.setter
    def aadl2_UnitLiteral822(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_UnitLiteral__aadl2_UnitLiteral822", None)
        self.__aadl2_UnitLiteral822 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_NumberValue823"):
                opp_val = getattr(old_value, "aadl2_NumberValue823", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_NumberValue823", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_NumberValue823"):
                opp_val = getattr(value, "aadl2_NumberValue823", None)
                setattr(value, "aadl2_NumberValue823", self)

    @property
    def aadl2_UnitLiteral820(self):
        return self.__aadl2_UnitLiteral820

    @aadl2_UnitLiteral820.setter
    def aadl2_UnitLiteral820(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_UnitLiteral__aadl2_UnitLiteral820", None)
        self.__aadl2_UnitLiteral820 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_UnitLiteral818"):
                opp_val = getattr(old_value, "aadl2_UnitLiteral818", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_UnitLiteral818", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_UnitLiteral818"):
                opp_val = getattr(value, "aadl2_UnitLiteral818", None)
                setattr(value, "aadl2_UnitLiteral818", self)

    @property
    def aadl2_UnitLiteral818(self):
        return self.__aadl2_UnitLiteral818

    @aadl2_UnitLiteral818.setter
    def aadl2_UnitLiteral818(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_UnitLiteral__aadl2_UnitLiteral818", None)
        self.__aadl2_UnitLiteral818 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_UnitLiteral820"):
                opp_val = getattr(old_value, "aadl2_UnitLiteral820", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_UnitLiteral820", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_UnitLiteral820"):
                opp_val = getattr(value, "aadl2_UnitLiteral820", None)
                setattr(value, "aadl2_UnitLiteral820", self)

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

    def getAbsoluteFactor(self, target: str) -> str:
        # TODO: Implement getAbsoluteFactor method
        pass

class PropertyExpression:

    pass
class aadl2_ListValue(PropertyExpression):

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
                if hasattr(item, "aadl2_PropertyExpression835"):
                    opp_val = getattr(item, "aadl2_PropertyExpression835", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_PropertyExpression835", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_PropertyExpression835"):
                    opp_val = getattr(item, "aadl2_PropertyExpression835", None)
                    
                    setattr(item, "aadl2_PropertyExpression835", self)
                    

class aadl2_PropertyValue(PropertyExpression):

    pass
class PropertyValue:

    pass
class aadl2_NumberValue(PropertyValue):

    def __init__(self, aadl2_NumberValue823: "aadl2_UnitLiteral" = None, aadl2_NumberValue: "aadl2_UnitLiteral" = None):
        self.aadl2_NumberValue823 = aadl2_NumberValue823
        self.aadl2_NumberValue = aadl2_NumberValue
        
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

    @property
    def aadl2_NumberValue823(self):
        return self.__aadl2_NumberValue823

    @aadl2_NumberValue823.setter
    def aadl2_NumberValue823(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_NumberValue__aadl2_NumberValue823", None)
        self.__aadl2_NumberValue823 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_UnitLiteral822"):
                opp_val = getattr(old_value, "aadl2_UnitLiteral822", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_UnitLiteral822", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_UnitLiteral822"):
                opp_val = getattr(value, "aadl2_UnitLiteral822", None)
                setattr(value, "aadl2_UnitLiteral822", self)

    def getScaledValue(self) -> str:
        # TODO: Implement getScaledValue method
        pass

    def getScaledValue(self, target: str) -> str:
        # TODO: Implement getScaledValue method
        pass

    def getScaledValue(self, target: str) -> str:
        # TODO: Implement getScaledValue method
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

class aadl2_ReferenceValue(PropertyValue, ContainedNamedElement):

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

class aadl2_RecordValue(PropertyValue):

    pass
class aadl2_NamedValue(PropertyValue):

    pass
class aadl2_StringLiteral(PropertyValue):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ArraySizeProperty:

    pass
class VirtualProcessorClassifier:

    pass
class VirtualBusClassifier:

    pass
class ThreadGroupClassifier:

    pass
class ThreadClassifier:

    pass
class ProcessClassifier:

    pass
class ProcessorClassifier:

    pass
class SystemClassifier:

    pass
class SubprogramGroupClassifier:

    pass
class SubprogramClassifier:

    pass
class MemoryClassifier:

    pass
class DeviceClassifier:

    pass
class BusClassifier:

    pass
class DataClassifier:

    pass
class ThreadGroup:

    pass
class ComponentPrototype:

    pass
class VirtualProcessor:

    pass
class VirtualBus:

    pass
class Thread:

    pass
class SubprogramGroup:

    pass
class System:

    pass
class Memory:

    pass
class Processor:

    pass
class Device:

    pass
class Process:

    pass
class Bus:

    pass
class VirtualProcessorSubcomponentType:

    pass
class aadl2_VirtualProcessorPrototype(VirtualProcessorSubcomponentType, VirtualProcessor, ComponentPrototype):

    pass
class VirtualBusSubcomponentType:

    pass
class aadl2_VirtualBusPrototype(VirtualBusSubcomponentType, VirtualBus, ComponentPrototype):

    pass
class ThreadSubcomponentType:

    pass
class aadl2_ThreadPrototype(ThreadSubcomponentType, Thread, ComponentPrototype):

    pass
class BehavioredImplementation:

    pass
class aadl2_SubprogramImplementation(SubprogramClassifier, BehavioredImplementation):

    pass
class aadl2_ThreadImplementation(ThreadClassifier, BehavioredImplementation):

    pass
class ThreadGroupSubcomponentType:

    pass
class aadl2_ThreadGroupPrototype(ThreadGroupSubcomponentType, ComponentPrototype, ThreadGroup):

    pass
class BusFeatureClassifier:

    pass
class SystemSubcomponentType:

    pass
class aadl2_SystemPrototype(System, SystemSubcomponentType, ComponentPrototype):

    pass
class SubprogramGroupSubcomponentType:

    pass
class aadl2_SubprogramGroupPrototype(SubprogramGroupSubcomponentType, ComponentPrototype, SubprogramGroup):

    pass
class ProcessSubcomponentType:

    pass
class aadl2_ProcessPrototype(ProcessSubcomponentType, Process, ComponentPrototype):

    pass
class ProcessorSubcomponentType:

    pass
class aadl2_ProcessorPrototype(Processor, ProcessorSubcomponentType, ComponentPrototype):

    pass
class MemorySubcomponentType:

    pass
class aadl2_MemoryPrototype(MemorySubcomponentType, Memory, ComponentPrototype):

    pass
class DeviceSubcomponentType:

    pass
class aadl2_DevicePrototype(DeviceSubcomponentType, Device, ComponentPrototype):

    pass
class BusSubcomponentType:

    pass
class aadl2_BusPrototype(ComponentPrototype, Bus, BusSubcomponentType):

    pass
class AbstractSubcomponentType:

    pass
class AbstractClassifier:

    pass
class aadl2_AbstractImplementation(BehavioredImplementation, AbstractClassifier):

    pass
class ComponentType:

    pass
class aadl2_ThreadGroupType(ComponentType, ThreadGroupClassifier):

    pass
class aadl2_VirtualBusType(ComponentType, VirtualBusClassifier):

    pass
class aadl2_ProcessorType(ComponentType, ProcessorClassifier):

    pass
class aadl2_MemoryType(ComponentType, MemoryClassifier):

    pass
class aadl2_SystemType(ComponentType, SystemClassifier):

    pass
class aadl2_ThreadType(ComponentType, ThreadClassifier):

    pass
class aadl2_VirtualProcessorType(VirtualProcessorClassifier, ComponentType):

    pass
class aadl2_ProcessType(ComponentType, ProcessClassifier):

    pass
class aadl2_DeviceType(ComponentType, DeviceClassifier):

    pass
class aadl2_BusType(ComponentType, BusClassifier):

    pass
class ComponentImplementation:

    pass
class aadl2_SystemImplementation(ComponentImplementation, SystemClassifier):

    pass
class aadl2_SubprogramGroupImplementation(ComponentImplementation, SubprogramGroupClassifier):

    pass
class aadl2_MemoryImplementation(ComponentImplementation, MemoryClassifier):

    pass
class aadl2_ThreadGroupImplementation(ComponentImplementation, ThreadGroupClassifier):

    pass
class aadl2_DeviceImplementation(ComponentImplementation, DeviceClassifier):

    pass
class aadl2_BusImplementation(ComponentImplementation, BusClassifier):

    pass
class aadl2_ProcessorImplementation(ComponentImplementation, ProcessorClassifier):

    pass
class aadl2_DataImplementation(ComponentImplementation, DataClassifier):

    pass
class aadl2_VirtualProcessorImplementation(ComponentImplementation, VirtualProcessorClassifier):

    pass
class aadl2_ProcessImplementation(ComponentImplementation, ProcessClassifier):

    pass
class aadl2_VirtualBusImplementation(ComponentImplementation, VirtualBusClassifier):

    pass
class aadl2_BehavioredImplementation(ComponentImplementation):

    def __init__(self, aadl2_BehavioredImplementation: set["aadl2_SubprogramCall"] = None, aadl2_BehavioredImplementation421: set["aadl2_SubprogramCallSequence"] = None):
        self.aadl2_BehavioredImplementation = aadl2_BehavioredImplementation if aadl2_BehavioredImplementation is not None else set()
        self.aadl2_BehavioredImplementation421 = aadl2_BehavioredImplementation421 if aadl2_BehavioredImplementation421 is not None else set()
        
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
                if hasattr(item, "aadl2_SubprogramCall419"):
                    opp_val = getattr(item, "aadl2_SubprogramCall419", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_SubprogramCall419", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_SubprogramCall419"):
                    opp_val = getattr(item, "aadl2_SubprogramCall419", None)
                    
                    setattr(item, "aadl2_SubprogramCall419", self)
                    

    @property
    def aadl2_BehavioredImplementation421(self):
        return self.__aadl2_BehavioredImplementation421

    @aadl2_BehavioredImplementation421.setter
    def aadl2_BehavioredImplementation421(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_BehavioredImplementation__aadl2_BehavioredImplementation421", None)
        self.__aadl2_BehavioredImplementation421 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_SubprogramCallSequence422"):
                    opp_val = getattr(item, "aadl2_SubprogramCallSequence422", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_SubprogramCallSequence422", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_SubprogramCallSequence422"):
                    opp_val = getattr(item, "aadl2_SubprogramCallSequence422", None)
                    
                    setattr(item, "aadl2_SubprogramCallSequence422", self)
                    

    def subprogramCalls(self) -> str:
        # TODO: Implement subprogramCalls method
        pass

class BehavioralFeature:

    pass
class PrototypeBinding:

    pass
class aadl2_FeaturePrototypeBinding(PrototypeBinding):

    pass
class aadl2_ComponentPrototypeBinding(PrototypeBinding):

    pass
class FeaturePrototypeActual:

    pass
class aadl2_PortSpecification(FeaturePrototypeActual):

    def __init__(self, direction: str, category: str, in: str, out: str, aadl2_PortSpecification: "aadl2_ComponentClassifier" = None, aadl2_PortSpecification409: "aadl2_ComponentPrototype" = None):
        self.direction = direction
        self.category = category
        self.in = in
        self.out = out
        self.aadl2_PortSpecification = aadl2_PortSpecification
        self.aadl2_PortSpecification409 = aadl2_PortSpecification409
        
    @property
    def out(self) -> str:
        return self.__out

    @out.setter
    def out(self, out: str):
        self.__out = out

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def in(self) -> str:
        return self.__in

    @in.setter
    def in(self, in: str):
        self.__in = in

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def aadl2_PortSpecification409(self):
        return self.__aadl2_PortSpecification409

    @aadl2_PortSpecification409.setter
    def aadl2_PortSpecification409(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PortSpecification__aadl2_PortSpecification409", None)
        self.__aadl2_PortSpecification409 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentPrototype410"):
                opp_val = getattr(old_value, "aadl2_ComponentPrototype410", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentPrototype410", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentPrototype410"):
                opp_val = getattr(value, "aadl2_ComponentPrototype410", None)
                setattr(value, "aadl2_ComponentPrototype410", self)

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
            if hasattr(old_value, "aadl2_ComponentClassifier407"):
                opp_val = getattr(old_value, "aadl2_ComponentClassifier407", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentClassifier407", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentClassifier407"):
                opp_val = getattr(value, "aadl2_ComponentClassifier407", None)
                setattr(value, "aadl2_ComponentClassifier407", self)

class aadl2_AccessSpecification(FeaturePrototypeActual):

    def __init__(self, kind: str, category: str, aadl2_AccessSpecification: "aadl2_ComponentClassifier" = None, aadl2_AccessSpecification404: "aadl2_ComponentPrototype" = None):
        self.kind = kind
        self.category = category
        self.aadl2_AccessSpecification = aadl2_AccessSpecification
        self.aadl2_AccessSpecification404 = aadl2_AccessSpecification404
        
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
            if hasattr(old_value, "aadl2_ComponentClassifier402"):
                opp_val = getattr(old_value, "aadl2_ComponentClassifier402", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentClassifier402", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentClassifier402"):
                opp_val = getattr(value, "aadl2_ComponentClassifier402", None)
                setattr(value, "aadl2_ComponentClassifier402", self)

    @property
    def aadl2_AccessSpecification404(self):
        return self.__aadl2_AccessSpecification404

    @aadl2_AccessSpecification404.setter
    def aadl2_AccessSpecification404(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_AccessSpecification__aadl2_AccessSpecification404", None)
        self.__aadl2_AccessSpecification404 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentPrototype405"):
                opp_val = getattr(old_value, "aadl2_ComponentPrototype405", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentPrototype405", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentPrototype405"):
                opp_val = getattr(value, "aadl2_ComponentPrototype405", None)
                setattr(value, "aadl2_ComponentPrototype405", self)

class aadl2_FeaturePrototypeReference(FeaturePrototypeActual):

    def __init__(self, out: str, direction: str, in: str, aadl2_FeaturePrototypeReference: "aadl2_FeaturePrototype" = None):
        self.out = out
        self.direction = direction
        self.in = in
        self.aadl2_FeaturePrototypeReference = aadl2_FeaturePrototypeReference
        
    @property
    def in(self) -> str:
        return self.__in

    @in.setter
    def in(self, in: str):
        self.__in = in

    @property
    def out(self) -> str:
        return self.__out

    @out.setter
    def out(self, out: str):
        self.__out = out

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
            if hasattr(old_value, "aadl2_FeaturePrototype412"):
                opp_val = getattr(old_value, "aadl2_FeaturePrototype412", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FeaturePrototype412", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FeaturePrototype412"):
                opp_val = getattr(value, "aadl2_FeaturePrototype412", None)
                setattr(value, "aadl2_FeaturePrototype412", self)

class aadl2_FeatureGroupPrototypeActual(FeaturePrototypeActual):

    pass
class aadl2_FeatureGroupPrototypeBinding(PrototypeBinding):

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
            if hasattr(old_value, "aadl2_AnnexSubclause352"):
                opp_val = getattr(old_value, "aadl2_AnnexSubclause352", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_AnnexSubclause352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_AnnexSubclause352"):
                opp_val = getattr(value, "aadl2_AnnexSubclause352", None)
                setattr(value, "aadl2_AnnexSubclause352", self)

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

class SubprogramSubcomponentType:

    pass
class Subprogram:

    pass
class aadl2_SubprogramPrototype(SubprogramSubcomponentType, ComponentPrototype, Subprogram):

    pass
class ProcessorFeature:

    pass
class DataSubcomponentType:

    pass
class Data:

    pass
class aadl2_DataPrototype(Data, DataSubcomponentType, ComponentPrototype):

    pass
class InternalFeature:

    pass
class Connection:

    pass
class Abstract:

    pass
class aadl2_AbstractPrototype(ThreadSubcomponentType, MemorySubcomponentType, SystemSubcomponentType, AbstractSubcomponentType, SubprogramGroupSubcomponentType, Abstract, VirtualBusSubcomponentType, ComponentPrototype, BusSubcomponentType, ProcessSubcomponentType, SubprogramSubcomponentType, DataSubcomponentType, ThreadGroupSubcomponentType, VirtualProcessorSubcomponentType, DeviceSubcomponentType, ProcessorSubcomponentType):

    pass
class Subcomponent:

    pass
class aadl2_ProcessSubcomponent(Process, Subcomponent):

    pass
class aadl2_ThreadSubcomponent(Thread, Subcomponent):

    pass
class aadl2_VirtualProcessorSubcomponent(VirtualProcessor, Subcomponent):

    pass
class aadl2_ThreadGroupSubcomponent(Subcomponent, ThreadGroup):

    pass
class aadl2_DeviceSubcomponent(Subcomponent, Device):

    pass
class aadl2_ProcessorSubcomponent(Processor, Subcomponent):

    pass
class aadl2_SystemSubcomponent(System, Subcomponent):

    pass
class aadl2_MemorySubcomponent(Memory, Subcomponent):

    pass
class PortConnectionEnd:

    pass
class ParameterConnectionEnd:

    pass
class TriggerPort:

    pass
class Port:

    pass
class AbstractFeatureClassifier:

    pass
class aadl2_EventPort(Port):

    pass
class AccessConnectionEnd:

    pass
class aadl2_DataSubcomponent(ParameterConnectionEnd, Data, Subcomponent, PortConnectionEnd, AccessConnectionEnd):

    pass
class aadl2_SubprogramSubcomponent(Subcomponent, AccessConnectionEnd, Subprogram):

    pass
class aadl2_BusSubcomponent(AccessConnectionEnd, Subcomponent, Bus):

    pass
class aadl2_VirtualBusSubcomponent(Subcomponent, VirtualBus, AccessConnectionEnd):

    pass
class Access:

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

    def __init__(self, direction: str, in: str, out: str):
        self.direction = direction
        self.in = in
        self.out = out
        
    @property
    def in(self) -> str:
        return self.__in

    @in.setter
    def in(self, in: str):
        self.__in = in

    @property
    def out(self) -> str:
        return self.__out

    @out.setter
    def out(self, out: str):
        self.__out = out

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

class aadl2_CallContext(ABC):

    pass
class aadl2_BusAccess(Access):

    def __init__(self, virtual: str, aadl2_BusAccess: "aadl2_FeatureGroupType" = None, aadl2_BusAccess242: "aadl2_BusFeatureClassifier" = None, aadl2_BusAccess424: "aadl2_AbstractType" = None, aadl2_BusAccess498: "aadl2_BusType" = None, aadl2_BusAccess533: "aadl2_DeviceType" = None, aadl2_BusAccess549: "aadl2_MemoryType" = None, aadl2_BusAccess600: "aadl2_SystemType" = None, aadl2_BusAccess661: "aadl2_ProcessorType" = None, aadl2_BusAccess776: "aadl2_VirtualBusType" = None, aadl2_BusAccess795: "aadl2_VirtualProcessorType" = None):
        self.virtual = virtual
        self.aadl2_BusAccess = aadl2_BusAccess
        self.aadl2_BusAccess242 = aadl2_BusAccess242
        self.aadl2_BusAccess424 = aadl2_BusAccess424
        self.aadl2_BusAccess498 = aadl2_BusAccess498
        self.aadl2_BusAccess533 = aadl2_BusAccess533
        self.aadl2_BusAccess549 = aadl2_BusAccess549
        self.aadl2_BusAccess600 = aadl2_BusAccess600
        self.aadl2_BusAccess661 = aadl2_BusAccess661
        self.aadl2_BusAccess776 = aadl2_BusAccess776
        self.aadl2_BusAccess795 = aadl2_BusAccess795
        
    @property
    def virtual(self) -> str:
        return self.__virtual

    @virtual.setter
    def virtual(self, virtual: str):
        self.__virtual = virtual

    @property
    def aadl2_BusAccess498(self):
        return self.__aadl2_BusAccess498

    @aadl2_BusAccess498.setter
    def aadl2_BusAccess498(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_BusAccess__aadl2_BusAccess498", None)
        self.__aadl2_BusAccess498 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_BusType"):
                opp_val = getattr(old_value, "aadl2_BusType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_BusType"):
                opp_val = getattr(value, "aadl2_BusType", None)
                if opp_val is None:
                    setattr(value, "aadl2_BusType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_BusAccess661(self):
        return self.__aadl2_BusAccess661

    @aadl2_BusAccess661.setter
    def aadl2_BusAccess661(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_BusAccess__aadl2_BusAccess661", None)
        self.__aadl2_BusAccess661 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ProcessorType660"):
                opp_val = getattr(old_value, "aadl2_ProcessorType660", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ProcessorType660"):
                opp_val = getattr(value, "aadl2_ProcessorType660", None)
                if opp_val is None:
                    setattr(value, "aadl2_ProcessorType660", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_BusAccess549(self):
        return self.__aadl2_BusAccess549

    @aadl2_BusAccess549.setter
    def aadl2_BusAccess549(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_BusAccess__aadl2_BusAccess549", None)
        self.__aadl2_BusAccess549 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_MemoryType"):
                opp_val = getattr(old_value, "aadl2_MemoryType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_MemoryType"):
                opp_val = getattr(value, "aadl2_MemoryType", None)
                if opp_val is None:
                    setattr(value, "aadl2_MemoryType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_BusAccess242(self):
        return self.__aadl2_BusAccess242

    @aadl2_BusAccess242.setter
    def aadl2_BusAccess242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_BusAccess__aadl2_BusAccess242", None)
        self.__aadl2_BusAccess242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_BusFeatureClassifier"):
                opp_val = getattr(old_value, "aadl2_BusFeatureClassifier", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_BusFeatureClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_BusFeatureClassifier"):
                opp_val = getattr(value, "aadl2_BusFeatureClassifier", None)
                setattr(value, "aadl2_BusFeatureClassifier", self)

    @property
    def aadl2_BusAccess600(self):
        return self.__aadl2_BusAccess600

    @aadl2_BusAccess600.setter
    def aadl2_BusAccess600(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_BusAccess__aadl2_BusAccess600", None)
        self.__aadl2_BusAccess600 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_SystemType"):
                opp_val = getattr(old_value, "aadl2_SystemType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_SystemType"):
                opp_val = getattr(value, "aadl2_SystemType", None)
                if opp_val is None:
                    setattr(value, "aadl2_SystemType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_BusAccess776(self):
        return self.__aadl2_BusAccess776

    @aadl2_BusAccess776.setter
    def aadl2_BusAccess776(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_BusAccess__aadl2_BusAccess776", None)
        self.__aadl2_BusAccess776 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_VirtualBusType775"):
                opp_val = getattr(old_value, "aadl2_VirtualBusType775", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_VirtualBusType775"):
                opp_val = getattr(value, "aadl2_VirtualBusType775", None)
                if opp_val is None:
                    setattr(value, "aadl2_VirtualBusType775", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_BusAccess(self):
        return self.__aadl2_BusAccess

    @aadl2_BusAccess.setter
    def aadl2_BusAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_BusAccess__aadl2_BusAccess", None)
        self.__aadl2_BusAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FeatureGroupType217"):
                opp_val = getattr(old_value, "aadl2_FeatureGroupType217", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FeatureGroupType217"):
                opp_val = getattr(value, "aadl2_FeatureGroupType217", None)
                if opp_val is None:
                    setattr(value, "aadl2_FeatureGroupType217", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_BusAccess533(self):
        return self.__aadl2_BusAccess533

    @aadl2_BusAccess533.setter
    def aadl2_BusAccess533(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_BusAccess__aadl2_BusAccess533", None)
        self.__aadl2_BusAccess533 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_DeviceType532"):
                opp_val = getattr(old_value, "aadl2_DeviceType532", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_DeviceType532"):
                opp_val = getattr(value, "aadl2_DeviceType532", None)
                if opp_val is None:
                    setattr(value, "aadl2_DeviceType532", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_BusAccess424(self):
        return self.__aadl2_BusAccess424

    @aadl2_BusAccess424.setter
    def aadl2_BusAccess424(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_BusAccess__aadl2_BusAccess424", None)
        self.__aadl2_BusAccess424 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_AbstractType"):
                opp_val = getattr(old_value, "aadl2_AbstractType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_AbstractType"):
                opp_val = getattr(value, "aadl2_AbstractType", None)
                if opp_val is None:
                    setattr(value, "aadl2_AbstractType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_BusAccess795(self):
        return self.__aadl2_BusAccess795

    @aadl2_BusAccess795.setter
    def aadl2_BusAccess795(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_BusAccess__aadl2_BusAccess795", None)
        self.__aadl2_BusAccess795 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_VirtualProcessorType794"):
                opp_val = getattr(old_value, "aadl2_VirtualProcessorType794", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_VirtualProcessorType794"):
                opp_val = getattr(value, "aadl2_VirtualProcessorType794", None)
                if opp_val is None:
                    setattr(value, "aadl2_VirtualProcessorType794", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class FeatureType:

    pass
class aadl2_FeatureType(ABC):

    pass
class CallContext:

    pass
class aadl2_SubprogramGroupAccess(Access, CallContext):

    pass
class aadl2_SubprogramType(ComponentType, CallContext, SubprogramClassifier):

    pass
class aadl2_DataType(ComponentType, CallContext, DataClassifier):

    pass
class aadl2_AbstractType(ComponentType, CallContext, AbstractClassifier):

    pass
class aadl2_SubprogramGroupType(SubprogramGroupClassifier, CallContext, ComponentType):

    pass
class aadl2_SubprogramGroupSubcomponent(CallContext, Subcomponent, AccessConnectionEnd, SubprogramGroup):

    pass
class FeatureGroupConnectionEnd:

    pass
class Context:

    pass
class aadl2_SubprogramCall(Context, BehavioralFeature):

    pass
class aadl2_EventDataPort(Port, Context, ParameterConnectionEnd):

    pass
class aadl2_DataPort(ParameterConnectionEnd, Port, Context):

    pass
class DirectedFeature:

    pass
class aadl2_Parameter(ParameterConnectionEnd, DirectedFeature, Context):

    pass
class aadl2_Port(TriggerPort, PortConnectionEnd, DirectedFeature):

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
class Flow:

    pass
class EndToEndFlowElement:

    pass
class aadl2_FlowElement(EndToEndFlowElement):

    pass
class Prototype:

    pass
class aadl2_FeaturePrototype(Prototype):

    def __init__(self, in: str, out: str, direction: str, aadl2_FeaturePrototype: "aadl2_AbstractFeature" = None, aadl2_FeaturePrototype263: "aadl2_ComponentClassifier" = None, aadl2_FeaturePrototype412: "aadl2_FeaturePrototypeReference" = None):
        self.in = in
        self.out = out
        self.direction = direction
        self.aadl2_FeaturePrototype = aadl2_FeaturePrototype
        self.aadl2_FeaturePrototype263 = aadl2_FeaturePrototype263
        self.aadl2_FeaturePrototype412 = aadl2_FeaturePrototype412
        
    @property
    def in(self) -> str:
        return self.__in

    @in.setter
    def in(self, in: str):
        self.__in = in

    @property
    def out(self) -> str:
        return self.__out

    @out.setter
    def out(self, out: str):
        self.__out = out

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def aadl2_FeaturePrototype412(self):
        return self.__aadl2_FeaturePrototype412

    @aadl2_FeaturePrototype412.setter
    def aadl2_FeaturePrototype412(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeaturePrototype__aadl2_FeaturePrototype412", None)
        self.__aadl2_FeaturePrototype412 = value
        
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
            if hasattr(old_value, "aadl2_AbstractFeature259"):
                opp_val = getattr(old_value, "aadl2_AbstractFeature259", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_AbstractFeature259", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_AbstractFeature259"):
                opp_val = getattr(value, "aadl2_AbstractFeature259", None)
                setattr(value, "aadl2_AbstractFeature259", self)

    @property
    def aadl2_FeaturePrototype263(self):
        return self.__aadl2_FeaturePrototype263

    @aadl2_FeaturePrototype263.setter
    def aadl2_FeaturePrototype263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeaturePrototype__aadl2_FeaturePrototype263", None)
        self.__aadl2_FeaturePrototype263 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentClassifier264"):
                opp_val = getattr(old_value, "aadl2_ComponentClassifier264", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentClassifier264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentClassifier264"):
                opp_val = getattr(value, "aadl2_ComponentClassifier264", None)
                setattr(value, "aadl2_ComponentClassifier264", self)

class aadl2_FeatureGroupPrototype(FeatureType, Prototype):

    pass
class ConnectionEnd:

    pass
class aadl2_AccessConnectionEnd(ConnectionEnd):

    pass
class aadl2_FeatureGroupConnectionEnd(ConnectionEnd):

    pass
class aadl2_ParameterConnectionEnd(ConnectionEnd):

    pass
class aadl2_PortConnectionEnd(ConnectionEnd):

    pass
class FlowElement:

    pass
class aadl2_DataAccess(ParameterConnectionEnd, FlowElement, Access, PortConnectionEnd):

    pass
class ModalPath:

    pass
class FlowFeature:

    pass
class aadl2_AbstractFeature(TriggerPort, DirectedFeature):

    pass
class aadl2_FeatureGroup(FeatureGroupConnectionEnd, CallContext, DirectedFeature, Context):

    def __init__(self, inverse: str, aadl2_FeatureGroup: "aadl2_ComponentType" = None, aadl2_FeatureGroup200: "aadl2_FeatureType" = None, aadl2_FeatureGroup202: "aadl2_FeatureGroupType" = None, aadl2_FeatureGroup204: "aadl2_FeatureGroupPrototype" = None, aadl2_FeatureGroup228: "aadl2_FeatureGroupType" = None):
        self.inverse = inverse
        self.aadl2_FeatureGroup = aadl2_FeatureGroup
        self.aadl2_FeatureGroup200 = aadl2_FeatureGroup200
        self.aadl2_FeatureGroup202 = aadl2_FeatureGroup202
        self.aadl2_FeatureGroup204 = aadl2_FeatureGroup204
        self.aadl2_FeatureGroup228 = aadl2_FeatureGroup228
        
    @property
    def inverse(self) -> str:
        return self.__inverse

    @inverse.setter
    def inverse(self, inverse: str):
        self.__inverse = inverse

    @property
    def aadl2_FeatureGroup200(self):
        return self.__aadl2_FeatureGroup200

    @aadl2_FeatureGroup200.setter
    def aadl2_FeatureGroup200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroup__aadl2_FeatureGroup200", None)
        self.__aadl2_FeatureGroup200 = value
        
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
    def aadl2_FeatureGroup202(self):
        return self.__aadl2_FeatureGroup202

    @aadl2_FeatureGroup202.setter
    def aadl2_FeatureGroup202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroup__aadl2_FeatureGroup202", None)
        self.__aadl2_FeatureGroup202 = value
        
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
            if hasattr(old_value, "aadl2_ComponentType165"):
                opp_val = getattr(old_value, "aadl2_ComponentType165", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentType165"):
                opp_val = getattr(value, "aadl2_ComponentType165", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentType165", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_FeatureGroup228(self):
        return self.__aadl2_FeatureGroup228

    @aadl2_FeatureGroup228.setter
    def aadl2_FeatureGroup228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroup__aadl2_FeatureGroup228", None)
        self.__aadl2_FeatureGroup228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FeatureGroupType227"):
                opp_val = getattr(old_value, "aadl2_FeatureGroupType227", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FeatureGroupType227"):
                opp_val = getattr(value, "aadl2_FeatureGroupType227", None)
                if opp_val is None:
                    setattr(value, "aadl2_FeatureGroupType227", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_FeatureGroup204(self):
        return self.__aadl2_FeatureGroup204

    @aadl2_FeatureGroup204.setter
    def aadl2_FeatureGroup204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroup__aadl2_FeatureGroup204", None)
        self.__aadl2_FeatureGroup204 = value
        
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

class aadl2_FeatureConnectionEnd(ConnectionEnd):

    pass
class ArrayableElement:

    pass
class aadl2_FeaturePrototypeActual(ArrayableElement):

    pass
class aadl2_ComponentPrototypeActual(ArrayableElement):

    def __init__(self, category: str, aadl2_ComponentPrototypeActual: "aadl2_ComponentPrototypeBinding" = None, aadl2_ComponentPrototypeActual388: set["aadl2_PrototypeBinding"] = None, aadl2_ComponentPrototypeActual391: "aadl2_SubcomponentType" = None):
        self.category = category
        self.aadl2_ComponentPrototypeActual = aadl2_ComponentPrototypeActual
        self.aadl2_ComponentPrototypeActual388 = aadl2_ComponentPrototypeActual388 if aadl2_ComponentPrototypeActual388 is not None else set()
        self.aadl2_ComponentPrototypeActual391 = aadl2_ComponentPrototypeActual391
        
    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def aadl2_ComponentPrototypeActual388(self):
        return self.__aadl2_ComponentPrototypeActual388

    @aadl2_ComponentPrototypeActual388.setter
    def aadl2_ComponentPrototypeActual388(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentPrototypeActual__aadl2_ComponentPrototypeActual388", None)
        self.__aadl2_ComponentPrototypeActual388 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_PrototypeBinding389"):
                    opp_val = getattr(item, "aadl2_PrototypeBinding389", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_PrototypeBinding389", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_PrototypeBinding389"):
                    opp_val = getattr(item, "aadl2_PrototypeBinding389", None)
                    
                    setattr(item, "aadl2_PrototypeBinding389", self)
                    

    @property
    def aadl2_ComponentPrototypeActual391(self):
        return self.__aadl2_ComponentPrototypeActual391

    @aadl2_ComponentPrototypeActual391.setter
    def aadl2_ComponentPrototypeActual391(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentPrototypeActual__aadl2_ComponentPrototypeActual391", None)
        self.__aadl2_ComponentPrototypeActual391 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_SubcomponentType392"):
                opp_val = getattr(old_value, "aadl2_SubcomponentType392", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_SubcomponentType392", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_SubcomponentType392"):
                opp_val = getattr(value, "aadl2_SubcomponentType392", None)
                setattr(value, "aadl2_SubcomponentType392", self)

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
class aadl2_TypeExtension(Generalization):

    pass
class aadl2_FlowSpecification(FlowElement, FlowFeature, ModalPath):

    def __init__(self, kind: str, aadl2_FlowSpecification: "aadl2_ComponentType" = None, aadl2_FlowSpecification183: "aadl2_FlowSpecification" = None, aadl2_FlowSpecification181: "aadl2_FlowSpecification" = None, aadl2_FlowSpecification185: "aadl2_FlowEnd" = None, aadl2_FlowSpecification187: "aadl2_FlowEnd" = None, aadl2_FlowSpecification295: "aadl2_FlowImplementation" = None):
        self.kind = kind
        self.aadl2_FlowSpecification = aadl2_FlowSpecification
        self.aadl2_FlowSpecification183 = aadl2_FlowSpecification183
        self.aadl2_FlowSpecification181 = aadl2_FlowSpecification181
        self.aadl2_FlowSpecification185 = aadl2_FlowSpecification185
        self.aadl2_FlowSpecification187 = aadl2_FlowSpecification187
        self.aadl2_FlowSpecification295 = aadl2_FlowSpecification295
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def aadl2_FlowSpecification295(self):
        return self.__aadl2_FlowSpecification295

    @aadl2_FlowSpecification295.setter
    def aadl2_FlowSpecification295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowSpecification__aadl2_FlowSpecification295", None)
        self.__aadl2_FlowSpecification295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FlowImplementation294"):
                opp_val = getattr(old_value, "aadl2_FlowImplementation294", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FlowImplementation294", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FlowImplementation294"):
                opp_val = getattr(value, "aadl2_FlowImplementation294", None)
                setattr(value, "aadl2_FlowImplementation294", self)

    @property
    def aadl2_FlowSpecification187(self):
        return self.__aadl2_FlowSpecification187

    @aadl2_FlowSpecification187.setter
    def aadl2_FlowSpecification187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowSpecification__aadl2_FlowSpecification187", None)
        self.__aadl2_FlowSpecification187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FlowEnd188"):
                opp_val = getattr(old_value, "aadl2_FlowEnd188", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FlowEnd188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FlowEnd188"):
                opp_val = getattr(value, "aadl2_FlowEnd188", None)
                setattr(value, "aadl2_FlowEnd188", self)

    @property
    def aadl2_FlowSpecification181(self):
        return self.__aadl2_FlowSpecification181

    @aadl2_FlowSpecification181.setter
    def aadl2_FlowSpecification181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowSpecification__aadl2_FlowSpecification181", None)
        self.__aadl2_FlowSpecification181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FlowSpecification183"):
                opp_val = getattr(old_value, "aadl2_FlowSpecification183", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FlowSpecification183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FlowSpecification183"):
                opp_val = getattr(value, "aadl2_FlowSpecification183", None)
                setattr(value, "aadl2_FlowSpecification183", self)

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
            if hasattr(old_value, "aadl2_ComponentType161"):
                opp_val = getattr(old_value, "aadl2_ComponentType161", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentType161"):
                opp_val = getattr(value, "aadl2_ComponentType161", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentType161", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_FlowSpecification185(self):
        return self.__aadl2_FlowSpecification185

    @aadl2_FlowSpecification185.setter
    def aadl2_FlowSpecification185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowSpecification__aadl2_FlowSpecification185", None)
        self.__aadl2_FlowSpecification185 = value
        
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
    def aadl2_FlowSpecification183(self):
        return self.__aadl2_FlowSpecification183

    @aadl2_FlowSpecification183.setter
    def aadl2_FlowSpecification183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowSpecification__aadl2_FlowSpecification183", None)
        self.__aadl2_FlowSpecification183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FlowSpecification181"):
                opp_val = getattr(old_value, "aadl2_FlowSpecification181", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FlowSpecification181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FlowSpecification181"):
                opp_val = getattr(value, "aadl2_FlowSpecification181", None)
                setattr(value, "aadl2_FlowSpecification181", self)

class aadl2_PortProxy(TriggerPort, ProcessorFeature, PortConnectionEnd, FeatureConnectionEnd):

    def __init__(self, direction: str, in: str, out: str, aadl2_PortProxy: "aadl2_ComponentImplementation" = None, aadl2_PortProxy346: "aadl2_DataClassifier" = None):
        self.direction = direction
        self.in = in
        self.out = out
        self.aadl2_PortProxy = aadl2_PortProxy
        self.aadl2_PortProxy346 = aadl2_PortProxy346
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def out(self) -> str:
        return self.__out

    @out.setter
    def out(self, out: str):
        self.__out = out

    @property
    def in(self) -> str:
        return self.__in

    @in.setter
    def in(self, in: str):
        self.__in = in

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
            if hasattr(old_value, "aadl2_ComponentImplementation136"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation136", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation136"):
                opp_val = getattr(value, "aadl2_ComponentImplementation136", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentImplementation136", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_PortProxy346(self):
        return self.__aadl2_PortProxy346

    @aadl2_PortProxy346.setter
    def aadl2_PortProxy346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PortProxy__aadl2_PortProxy346", None)
        self.__aadl2_PortProxy346 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_DataClassifier347"):
                opp_val = getattr(old_value, "aadl2_DataClassifier347", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_DataClassifier347", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_DataClassifier347"):
                opp_val = getattr(value, "aadl2_DataClassifier347", None)
                setattr(value, "aadl2_DataClassifier347", self)

class aadl2_FeatureClassifier(ABC):

    pass
class FeatureClassifier:

    pass
class aadl2_AbstractFeatureClassifier(FeatureClassifier):

    pass
class aadl2_BusFeatureClassifier(FeatureClassifier):

    pass
class SubcomponentType:

    pass
class aadl2_SubprogramGroupSubcomponentType(AbstractFeatureClassifier, SubcomponentType):

    pass
class aadl2_VirtualBusSubcomponentType(AbstractFeatureClassifier, SubcomponentType, BusFeatureClassifier):

    pass
class aadl2_AbstractSubcomponentType(AbstractFeatureClassifier, SubcomponentType):

    pass
class aadl2_VirtualProcessorSubcomponentType(SubcomponentType):

    pass
class aadl2_ProcessorSubcomponentType(SubcomponentType):

    pass
class aadl2_BusSubcomponentType(AbstractFeatureClassifier, SubcomponentType, BusFeatureClassifier):

    pass
class aadl2_ThreadGroupSubcomponentType(SubcomponentType):

    pass
class aadl2_SubprogramSubcomponentType(AbstractFeatureClassifier, SubcomponentType):

    pass
class aadl2_ProcessSubcomponentType(SubcomponentType):

    pass
class aadl2_SystemSubcomponentType(SubcomponentType):

    pass
class aadl2_DeviceSubcomponentType(SubcomponentType):

    pass
class aadl2_ComponentPrototype(FeatureClassifier, SubcomponentType, Prototype):

    def __init__(self, array: str, aadl2_ComponentPrototype: "aadl2_Feature" = None, aadl2_ComponentPrototype179: "aadl2_ComponentClassifier" = None, aadl2_ComponentPrototype275: "aadl2_Subcomponent" = None, aadl2_ComponentPrototype405: "aadl2_AccessSpecification" = None, aadl2_ComponentPrototype410: "aadl2_PortSpecification" = None):
        self.array = array
        self.aadl2_ComponentPrototype = aadl2_ComponentPrototype
        self.aadl2_ComponentPrototype179 = aadl2_ComponentPrototype179
        self.aadl2_ComponentPrototype275 = aadl2_ComponentPrototype275
        self.aadl2_ComponentPrototype405 = aadl2_ComponentPrototype405
        self.aadl2_ComponentPrototype410 = aadl2_ComponentPrototype410
        
    @property
    def array(self) -> str:
        return self.__array

    @array.setter
    def array(self, array: str):
        self.__array = array

    @property
    def aadl2_ComponentPrototype179(self):
        return self.__aadl2_ComponentPrototype179

    @aadl2_ComponentPrototype179.setter
    def aadl2_ComponentPrototype179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentPrototype__aadl2_ComponentPrototype179", None)
        self.__aadl2_ComponentPrototype179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentClassifier180"):
                opp_val = getattr(old_value, "aadl2_ComponentClassifier180", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentClassifier180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentClassifier180"):
                opp_val = getattr(value, "aadl2_ComponentClassifier180", None)
                setattr(value, "aadl2_ComponentClassifier180", self)

    @property
    def aadl2_ComponentPrototype275(self):
        return self.__aadl2_ComponentPrototype275

    @aadl2_ComponentPrototype275.setter
    def aadl2_ComponentPrototype275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentPrototype__aadl2_ComponentPrototype275", None)
        self.__aadl2_ComponentPrototype275 = value
        
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
    def aadl2_ComponentPrototype410(self):
        return self.__aadl2_ComponentPrototype410

    @aadl2_ComponentPrototype410.setter
    def aadl2_ComponentPrototype410(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentPrototype__aadl2_ComponentPrototype410", None)
        self.__aadl2_ComponentPrototype410 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PortSpecification409"):
                opp_val = getattr(old_value, "aadl2_PortSpecification409", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_PortSpecification409", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PortSpecification409"):
                opp_val = getattr(value, "aadl2_PortSpecification409", None)
                setattr(value, "aadl2_PortSpecification409", self)

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
            if hasattr(old_value, "aadl2_Feature169"):
                opp_val = getattr(old_value, "aadl2_Feature169", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Feature169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Feature169"):
                opp_val = getattr(value, "aadl2_Feature169", None)
                setattr(value, "aadl2_Feature169", self)

    @property
    def aadl2_ComponentPrototype405(self):
        return self.__aadl2_ComponentPrototype405

    @aadl2_ComponentPrototype405.setter
    def aadl2_ComponentPrototype405(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentPrototype__aadl2_ComponentPrototype405", None)
        self.__aadl2_ComponentPrototype405 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_AccessSpecification404"):
                opp_val = getattr(old_value, "aadl2_AccessSpecification404", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_AccessSpecification404", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_AccessSpecification404"):
                opp_val = getattr(value, "aadl2_AccessSpecification404", None)
                setattr(value, "aadl2_AccessSpecification404", self)

class aadl2_MemorySubcomponentType(SubcomponentType):

    pass
class aadl2_ThreadSubcomponentType(SubcomponentType):

    pass
class aadl2_DataSubcomponentType(AbstractFeatureClassifier, SubcomponentType):

    pass
class Classifier:

    pass
class aadl2_FeatureGroupType(FeatureType, Classifier):

    pass
class aadl2_ComponentClassifier(FeatureClassifier, SubcomponentType, Classifier):

    def __init__(self, derivedModes: str, noFlows: str, noModes: str, aadl2_ComponentClassifier: set["aadl2_Mode"] = None, aadl2_ComponentClassifier142: set["aadl2_ModeTransition"] = None, aadl2_ComponentClassifier180: "aadl2_ComponentPrototype" = None, aadl2_ComponentClassifier264: "aadl2_FeaturePrototype" = None, aadl2_ComponentClassifier286: "aadl2_Subcomponent" = None, aadl2_ComponentClassifier402: "aadl2_AccessSpecification" = None, aadl2_ComponentClassifier407: "aadl2_PortSpecification" = None):
        self.derivedModes = derivedModes
        self.noFlows = noFlows
        self.noModes = noModes
        self.aadl2_ComponentClassifier = aadl2_ComponentClassifier if aadl2_ComponentClassifier is not None else set()
        self.aadl2_ComponentClassifier142 = aadl2_ComponentClassifier142 if aadl2_ComponentClassifier142 is not None else set()
        self.aadl2_ComponentClassifier180 = aadl2_ComponentClassifier180
        self.aadl2_ComponentClassifier264 = aadl2_ComponentClassifier264
        self.aadl2_ComponentClassifier286 = aadl2_ComponentClassifier286
        self.aadl2_ComponentClassifier402 = aadl2_ComponentClassifier402
        self.aadl2_ComponentClassifier407 = aadl2_ComponentClassifier407
        
    @property
    def noFlows(self) -> str:
        return self.__noFlows

    @noFlows.setter
    def noFlows(self, noFlows: str):
        self.__noFlows = noFlows

    @property
    def noModes(self) -> str:
        return self.__noModes

    @noModes.setter
    def noModes(self, noModes: str):
        self.__noModes = noModes

    @property
    def derivedModes(self) -> str:
        return self.__derivedModes

    @derivedModes.setter
    def derivedModes(self, derivedModes: str):
        self.__derivedModes = derivedModes

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
                if hasattr(item, "aadl2_Mode140"):
                    opp_val = getattr(item, "aadl2_Mode140", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Mode140", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Mode140"):
                    opp_val = getattr(item, "aadl2_Mode140", None)
                    
                    setattr(item, "aadl2_Mode140", self)
                    

    @property
    def aadl2_ComponentClassifier142(self):
        return self.__aadl2_ComponentClassifier142

    @aadl2_ComponentClassifier142.setter
    def aadl2_ComponentClassifier142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier142", None)
        self.__aadl2_ComponentClassifier142 = value if value is not None else set()
        
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
    def aadl2_ComponentClassifier402(self):
        return self.__aadl2_ComponentClassifier402

    @aadl2_ComponentClassifier402.setter
    def aadl2_ComponentClassifier402(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier402", None)
        self.__aadl2_ComponentClassifier402 = value
        
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
    def aadl2_ComponentClassifier407(self):
        return self.__aadl2_ComponentClassifier407

    @aadl2_ComponentClassifier407.setter
    def aadl2_ComponentClassifier407(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier407", None)
        self.__aadl2_ComponentClassifier407 = value
        
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
    def aadl2_ComponentClassifier264(self):
        return self.__aadl2_ComponentClassifier264

    @aadl2_ComponentClassifier264.setter
    def aadl2_ComponentClassifier264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier264", None)
        self.__aadl2_ComponentClassifier264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FeaturePrototype263"):
                opp_val = getattr(old_value, "aadl2_FeaturePrototype263", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FeaturePrototype263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FeaturePrototype263"):
                opp_val = getattr(value, "aadl2_FeaturePrototype263", None)
                setattr(value, "aadl2_FeaturePrototype263", self)

    @property
    def aadl2_ComponentClassifier286(self):
        return self.__aadl2_ComponentClassifier286

    @aadl2_ComponentClassifier286.setter
    def aadl2_ComponentClassifier286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier286", None)
        self.__aadl2_ComponentClassifier286 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Subcomponent285"):
                opp_val = getattr(old_value, "aadl2_Subcomponent285", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Subcomponent285", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Subcomponent285"):
                opp_val = getattr(value, "aadl2_Subcomponent285", None)
                setattr(value, "aadl2_Subcomponent285", self)

    @property
    def aadl2_ComponentClassifier180(self):
        return self.__aadl2_ComponentClassifier180

    @aadl2_ComponentClassifier180.setter
    def aadl2_ComponentClassifier180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier180", None)
        self.__aadl2_ComponentClassifier180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentPrototype179"):
                opp_val = getattr(old_value, "aadl2_ComponentPrototype179", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentPrototype179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentPrototype179"):
                opp_val = getattr(value, "aadl2_ComponentPrototype179", None)
                setattr(value, "aadl2_ComponentPrototype179", self)

class aadl2_EventDataSource(InternalFeature):

    pass
class aadl2_EventSource(InternalFeature):

    pass
class aadl2_ImplementationExtension(Generalization):

    pass
class aadl2_FeatureGroupConnection(Connection):

    pass
class aadl2_FeatureConnection(Connection):

    pass
class aadl2_PortConnection(Connection):

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
            if hasattr(old_value, "aadl2_ComponentImplementation118"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation118", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation118"):
                opp_val = getattr(value, "aadl2_ComponentImplementation118", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentImplementation118", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aadl2_AbstractSubcomponent(Abstract, Subcomponent):

    pass
class aadl2_EndToEndFlow(ModalPath, FlowFeature, EndToEndFlowElement):

    pass
class aadl2_Realization(Generalization):

    pass
class aadl2_ArraySizeProperty(ABC):

    pass
class ComponentClassifier:

    pass
class aadl2_AbstractClassifier(ThreadSubcomponentType, MemorySubcomponentType, SystemSubcomponentType, AbstractSubcomponentType, VirtualProcessorSubcomponentType, SubprogramGroupSubcomponentType, Abstract, VirtualBusSubcomponentType, BusSubcomponentType, ProcessSubcomponentType, DataSubcomponentType, ComponentClassifier, ThreadGroupSubcomponentType, SubprogramSubcomponentType, DeviceSubcomponentType, ProcessorSubcomponentType):

    pass
class aadl2_SubprogramClassifier(SubprogramSubcomponentType, ComponentClassifier, Subprogram):

    pass
class aadl2_ComponentType(ComponentClassifier):

    def __init__(self, noFeatures: str, aadl2_ComponentType: "aadl2_ComponentImplementation" = None, aadl2_ComponentType156: set["aadl2_Feature"] = None, aadl2_ComponentType159: "aadl2_ComponentType" = None, aadl2_ComponentType157: "aadl2_ComponentType" = None, aadl2_ComponentType161: set["aadl2_FlowSpecification"] = None, aadl2_ComponentType163: "aadl2_TypeExtension" = None, aadl2_ComponentType165: set["aadl2_FeatureGroup"] = None, aadl2_ComponentType167: set["aadl2_AbstractFeature"] = None, aadl2_ComponentType198: "aadl2_TypeExtension" = None, aadl2_ComponentType330: "aadl2_Realization" = None, aadl2_ComponentType382: "aadl2_ComponentTypeRename" = None):
        self.noFeatures = noFeatures
        self.aadl2_ComponentType = aadl2_ComponentType
        self.aadl2_ComponentType156 = aadl2_ComponentType156 if aadl2_ComponentType156 is not None else set()
        self.aadl2_ComponentType159 = aadl2_ComponentType159
        self.aadl2_ComponentType157 = aadl2_ComponentType157
        self.aadl2_ComponentType161 = aadl2_ComponentType161 if aadl2_ComponentType161 is not None else set()
        self.aadl2_ComponentType163 = aadl2_ComponentType163
        self.aadl2_ComponentType165 = aadl2_ComponentType165 if aadl2_ComponentType165 is not None else set()
        self.aadl2_ComponentType167 = aadl2_ComponentType167 if aadl2_ComponentType167 is not None else set()
        self.aadl2_ComponentType198 = aadl2_ComponentType198
        self.aadl2_ComponentType330 = aadl2_ComponentType330
        self.aadl2_ComponentType382 = aadl2_ComponentType382
        
    @property
    def noFeatures(self) -> str:
        return self.__noFeatures

    @noFeatures.setter
    def noFeatures(self, noFeatures: str):
        self.__noFeatures = noFeatures

    @property
    def aadl2_ComponentType159(self):
        return self.__aadl2_ComponentType159

    @aadl2_ComponentType159.setter
    def aadl2_ComponentType159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType159", None)
        self.__aadl2_ComponentType159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentType157"):
                opp_val = getattr(old_value, "aadl2_ComponentType157", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentType157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentType157"):
                opp_val = getattr(value, "aadl2_ComponentType157", None)
                setattr(value, "aadl2_ComponentType157", self)

    @property
    def aadl2_ComponentType161(self):
        return self.__aadl2_ComponentType161

    @aadl2_ComponentType161.setter
    def aadl2_ComponentType161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType161", None)
        self.__aadl2_ComponentType161 = value if value is not None else set()
        
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
    def aadl2_ComponentType165(self):
        return self.__aadl2_ComponentType165

    @aadl2_ComponentType165.setter
    def aadl2_ComponentType165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType165", None)
        self.__aadl2_ComponentType165 = value if value is not None else set()
        
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
    def aadl2_ComponentType(self):
        return self.__aadl2_ComponentType

    @aadl2_ComponentType.setter
    def aadl2_ComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType", None)
        self.__aadl2_ComponentType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentImplementation99"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation99", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentImplementation99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation99"):
                opp_val = getattr(value, "aadl2_ComponentImplementation99", None)
                setattr(value, "aadl2_ComponentImplementation99", self)

    @property
    def aadl2_ComponentType198(self):
        return self.__aadl2_ComponentType198

    @aadl2_ComponentType198.setter
    def aadl2_ComponentType198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType198", None)
        self.__aadl2_ComponentType198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_TypeExtension197"):
                opp_val = getattr(old_value, "aadl2_TypeExtension197", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_TypeExtension197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_TypeExtension197"):
                opp_val = getattr(value, "aadl2_TypeExtension197", None)
                setattr(value, "aadl2_TypeExtension197", self)

    @property
    def aadl2_ComponentType330(self):
        return self.__aadl2_ComponentType330

    @aadl2_ComponentType330.setter
    def aadl2_ComponentType330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType330", None)
        self.__aadl2_ComponentType330 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Realization329"):
                opp_val = getattr(old_value, "aadl2_Realization329", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Realization329", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Realization329"):
                opp_val = getattr(value, "aadl2_Realization329", None)
                setattr(value, "aadl2_Realization329", self)

    @property
    def aadl2_ComponentType382(self):
        return self.__aadl2_ComponentType382

    @aadl2_ComponentType382.setter
    def aadl2_ComponentType382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType382", None)
        self.__aadl2_ComponentType382 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentTypeRename381"):
                opp_val = getattr(old_value, "aadl2_ComponentTypeRename381", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentTypeRename381", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentTypeRename381"):
                opp_val = getattr(value, "aadl2_ComponentTypeRename381", None)
                setattr(value, "aadl2_ComponentTypeRename381", self)

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
    def aadl2_ComponentType163(self):
        return self.__aadl2_ComponentType163

    @aadl2_ComponentType163.setter
    def aadl2_ComponentType163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType163", None)
        self.__aadl2_ComponentType163 = value
        
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
    def aadl2_ComponentType157(self):
        return self.__aadl2_ComponentType157

    @aadl2_ComponentType157.setter
    def aadl2_ComponentType157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType157", None)
        self.__aadl2_ComponentType157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentType159"):
                opp_val = getattr(old_value, "aadl2_ComponentType159", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentType159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentType159"):
                opp_val = getattr(value, "aadl2_ComponentType159", None)
                setattr(value, "aadl2_ComponentType159", self)

    @property
    def aadl2_ComponentType167(self):
        return self.__aadl2_ComponentType167

    @aadl2_ComponentType167.setter
    def aadl2_ComponentType167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType167", None)
        self.__aadl2_ComponentType167 = value if value is not None else set()
        
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
                    

class aadl2_DeviceClassifier(DeviceSubcomponentType, Device, ComponentClassifier):

    pass
class aadl2_ThreadClassifier(ThreadSubcomponentType, Thread, ComponentClassifier):

    pass
class aadl2_VirtualProcessorClassifier(VirtualProcessorSubcomponentType, VirtualProcessor, ComponentClassifier):

    pass
class aadl2_BusClassifier(ComponentClassifier, Bus, BusSubcomponentType):

    pass
class aadl2_SubprogramGroupClassifier(SubprogramGroupSubcomponentType, ComponentClassifier, SubprogramGroup):

    pass
class aadl2_SystemClassifier(System, SystemSubcomponentType, ComponentClassifier):

    pass
class aadl2_ProcessorClassifier(Processor, ProcessorSubcomponentType, ComponentClassifier):

    pass
class aadl2_VirtualBusClassifier(VirtualBusSubcomponentType, VirtualBus, ComponentClassifier):

    pass
class aadl2_ThreadGroupClassifier(ThreadGroup, ComponentClassifier, ThreadGroupSubcomponentType):

    pass
class aadl2_ProcessClassifier(ProcessSubcomponentType, Process, ComponentClassifier):

    pass
class aadl2_DataClassifier(Data, DataSubcomponentType, ComponentClassifier):

    pass
class aadl2_MemoryClassifier(MemorySubcomponentType, Memory, ComponentClassifier):

    pass
class aadl2_ComponentImplementation(ComponentClassifier):

    def __init__(self, noSubcomponents: str, noConnections: str, noCalls: str, aadl2_ComponentImplementation: "aadl2_ComponentImplementationReference" = None, aadl2_ComponentImplementation99: "aadl2_ComponentType" = None, aadl2_ComponentImplementation101: set["aadl2_Subcomponent"] = None, aadl2_ComponentImplementation104: "aadl2_ComponentImplementation" = None, aadl2_ComponentImplementation102: "aadl2_ComponentImplementation" = None, aadl2_ComponentImplementation112: "aadl2_Realization" = None, aadl2_ComponentImplementation114: set["aadl2_EndToEndFlow"] = None, aadl2_ComponentImplementation116: set["aadl2_AbstractSubcomponent"] = None, aadl2_ComponentImplementation118: set["aadl2_AccessConnection"] = None, aadl2_ComponentImplementation120: set["aadl2_ParameterConnection"] = None, aadl2_ComponentImplementation122: set["aadl2_PortConnection"] = None, aadl2_ComponentImplementation124: set["aadl2_FeatureConnection"] = None, aadl2_ComponentImplementation126: set["aadl2_FeatureGroupConnection"] = None, aadl2_ComponentImplementation106: set["aadl2_FlowImplementation"] = None, aadl2_ComponentImplementation108: set["aadl2_Connection"] = None, aadl2_ComponentImplementation110: "aadl2_ImplementationExtension" = None, aadl2_ComponentImplementation128: set["aadl2_ProcessorFeature"] = None, aadl2_ComponentImplementation130: set["aadl2_InternalFeature"] = None, aadl2_ComponentImplementation132: set["aadl2_EventSource"] = None, aadl2_ComponentImplementation134: set["aadl2_EventDataSource"] = None, aadl2_ComponentImplementation136: set["aadl2_PortProxy"] = None, aadl2_ComponentImplementation138: set["aadl2_SubprogramProxy"] = None, aadl2_ComponentImplementation327: "aadl2_ImplementationExtension" = None):
        self.noSubcomponents = noSubcomponents
        self.noConnections = noConnections
        self.noCalls = noCalls
        self.aadl2_ComponentImplementation = aadl2_ComponentImplementation
        self.aadl2_ComponentImplementation99 = aadl2_ComponentImplementation99
        self.aadl2_ComponentImplementation101 = aadl2_ComponentImplementation101 if aadl2_ComponentImplementation101 is not None else set()
        self.aadl2_ComponentImplementation104 = aadl2_ComponentImplementation104
        self.aadl2_ComponentImplementation102 = aadl2_ComponentImplementation102
        self.aadl2_ComponentImplementation112 = aadl2_ComponentImplementation112
        self.aadl2_ComponentImplementation114 = aadl2_ComponentImplementation114 if aadl2_ComponentImplementation114 is not None else set()
        self.aadl2_ComponentImplementation116 = aadl2_ComponentImplementation116 if aadl2_ComponentImplementation116 is not None else set()
        self.aadl2_ComponentImplementation118 = aadl2_ComponentImplementation118 if aadl2_ComponentImplementation118 is not None else set()
        self.aadl2_ComponentImplementation120 = aadl2_ComponentImplementation120 if aadl2_ComponentImplementation120 is not None else set()
        self.aadl2_ComponentImplementation122 = aadl2_ComponentImplementation122 if aadl2_ComponentImplementation122 is not None else set()
        self.aadl2_ComponentImplementation124 = aadl2_ComponentImplementation124 if aadl2_ComponentImplementation124 is not None else set()
        self.aadl2_ComponentImplementation126 = aadl2_ComponentImplementation126 if aadl2_ComponentImplementation126 is not None else set()
        self.aadl2_ComponentImplementation106 = aadl2_ComponentImplementation106 if aadl2_ComponentImplementation106 is not None else set()
        self.aadl2_ComponentImplementation108 = aadl2_ComponentImplementation108 if aadl2_ComponentImplementation108 is not None else set()
        self.aadl2_ComponentImplementation110 = aadl2_ComponentImplementation110
        self.aadl2_ComponentImplementation128 = aadl2_ComponentImplementation128 if aadl2_ComponentImplementation128 is not None else set()
        self.aadl2_ComponentImplementation130 = aadl2_ComponentImplementation130 if aadl2_ComponentImplementation130 is not None else set()
        self.aadl2_ComponentImplementation132 = aadl2_ComponentImplementation132 if aadl2_ComponentImplementation132 is not None else set()
        self.aadl2_ComponentImplementation134 = aadl2_ComponentImplementation134 if aadl2_ComponentImplementation134 is not None else set()
        self.aadl2_ComponentImplementation136 = aadl2_ComponentImplementation136 if aadl2_ComponentImplementation136 is not None else set()
        self.aadl2_ComponentImplementation138 = aadl2_ComponentImplementation138 if aadl2_ComponentImplementation138 is not None else set()
        self.aadl2_ComponentImplementation327 = aadl2_ComponentImplementation327
        
    @property
    def noSubcomponents(self) -> str:
        return self.__noSubcomponents

    @noSubcomponents.setter
    def noSubcomponents(self, noSubcomponents: str):
        self.__noSubcomponents = noSubcomponents

    @property
    def noCalls(self) -> str:
        return self.__noCalls

    @noCalls.setter
    def noCalls(self, noCalls: str):
        self.__noCalls = noCalls

    @property
    def noConnections(self) -> str:
        return self.__noConnections

    @noConnections.setter
    def noConnections(self, noConnections: str):
        self.__noConnections = noConnections

    @property
    def aadl2_ComponentImplementation116(self):
        return self.__aadl2_ComponentImplementation116

    @aadl2_ComponentImplementation116.setter
    def aadl2_ComponentImplementation116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation116", None)
        self.__aadl2_ComponentImplementation116 = value if value is not None else set()
        
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
    def aadl2_ComponentImplementation108(self):
        return self.__aadl2_ComponentImplementation108

    @aadl2_ComponentImplementation108.setter
    def aadl2_ComponentImplementation108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation108", None)
        self.__aadl2_ComponentImplementation108 = value if value is not None else set()
        
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
    def aadl2_ComponentImplementation114(self):
        return self.__aadl2_ComponentImplementation114

    @aadl2_ComponentImplementation114.setter
    def aadl2_ComponentImplementation114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation114", None)
        self.__aadl2_ComponentImplementation114 = value if value is not None else set()
        
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
    def aadl2_ComponentImplementation126(self):
        return self.__aadl2_ComponentImplementation126

    @aadl2_ComponentImplementation126.setter
    def aadl2_ComponentImplementation126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation126", None)
        self.__aadl2_ComponentImplementation126 = value if value is not None else set()
        
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
    def aadl2_ComponentImplementation132(self):
        return self.__aadl2_ComponentImplementation132

    @aadl2_ComponentImplementation132.setter
    def aadl2_ComponentImplementation132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation132", None)
        self.__aadl2_ComponentImplementation132 = value if value is not None else set()
        
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
    def aadl2_ComponentImplementation120(self):
        return self.__aadl2_ComponentImplementation120

    @aadl2_ComponentImplementation120.setter
    def aadl2_ComponentImplementation120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation120", None)
        self.__aadl2_ComponentImplementation120 = value if value is not None else set()
        
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
    def aadl2_ComponentImplementation112(self):
        return self.__aadl2_ComponentImplementation112

    @aadl2_ComponentImplementation112.setter
    def aadl2_ComponentImplementation112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation112", None)
        self.__aadl2_ComponentImplementation112 = value
        
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
    def aadl2_ComponentImplementation104(self):
        return self.__aadl2_ComponentImplementation104

    @aadl2_ComponentImplementation104.setter
    def aadl2_ComponentImplementation104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation104", None)
        self.__aadl2_ComponentImplementation104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentImplementation102"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation102", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentImplementation102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation102"):
                opp_val = getattr(value, "aadl2_ComponentImplementation102", None)
                setattr(value, "aadl2_ComponentImplementation102", self)

    @property
    def aadl2_ComponentImplementation327(self):
        return self.__aadl2_ComponentImplementation327

    @aadl2_ComponentImplementation327.setter
    def aadl2_ComponentImplementation327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation327", None)
        self.__aadl2_ComponentImplementation327 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ImplementationExtension326"):
                opp_val = getattr(old_value, "aadl2_ImplementationExtension326", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ImplementationExtension326", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ImplementationExtension326"):
                opp_val = getattr(value, "aadl2_ImplementationExtension326", None)
                setattr(value, "aadl2_ImplementationExtension326", self)

    @property
    def aadl2_ComponentImplementation130(self):
        return self.__aadl2_ComponentImplementation130

    @aadl2_ComponentImplementation130.setter
    def aadl2_ComponentImplementation130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation130", None)
        self.__aadl2_ComponentImplementation130 = value if value is not None else set()
        
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
    def aadl2_ComponentImplementation99(self):
        return self.__aadl2_ComponentImplementation99

    @aadl2_ComponentImplementation99.setter
    def aadl2_ComponentImplementation99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation99", None)
        self.__aadl2_ComponentImplementation99 = value
        
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

    @property
    def aadl2_ComponentImplementation138(self):
        return self.__aadl2_ComponentImplementation138

    @aadl2_ComponentImplementation138.setter
    def aadl2_ComponentImplementation138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation138", None)
        self.__aadl2_ComponentImplementation138 = value if value is not None else set()
        
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
    def aadl2_ComponentImplementation124(self):
        return self.__aadl2_ComponentImplementation124

    @aadl2_ComponentImplementation124.setter
    def aadl2_ComponentImplementation124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation124", None)
        self.__aadl2_ComponentImplementation124 = value if value is not None else set()
        
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
    def aadl2_ComponentImplementation102(self):
        return self.__aadl2_ComponentImplementation102

    @aadl2_ComponentImplementation102.setter
    def aadl2_ComponentImplementation102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation102", None)
        self.__aadl2_ComponentImplementation102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentImplementation104"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation104", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentImplementation104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation104"):
                opp_val = getattr(value, "aadl2_ComponentImplementation104", None)
                setattr(value, "aadl2_ComponentImplementation104", self)

    @property
    def aadl2_ComponentImplementation128(self):
        return self.__aadl2_ComponentImplementation128

    @aadl2_ComponentImplementation128.setter
    def aadl2_ComponentImplementation128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation128", None)
        self.__aadl2_ComponentImplementation128 = value if value is not None else set()
        
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
    def aadl2_ComponentImplementation118(self):
        return self.__aadl2_ComponentImplementation118

    @aadl2_ComponentImplementation118.setter
    def aadl2_ComponentImplementation118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation118", None)
        self.__aadl2_ComponentImplementation118 = value if value is not None else set()
        
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
    def aadl2_ComponentImplementation110(self):
        return self.__aadl2_ComponentImplementation110

    @aadl2_ComponentImplementation110.setter
    def aadl2_ComponentImplementation110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation110", None)
        self.__aadl2_ComponentImplementation110 = value
        
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
    def aadl2_ComponentImplementation136(self):
        return self.__aadl2_ComponentImplementation136

    @aadl2_ComponentImplementation136.setter
    def aadl2_ComponentImplementation136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation136", None)
        self.__aadl2_ComponentImplementation136 = value if value is not None else set()
        
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
    def aadl2_ComponentImplementation122(self):
        return self.__aadl2_ComponentImplementation122

    @aadl2_ComponentImplementation122.setter
    def aadl2_ComponentImplementation122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation122", None)
        self.__aadl2_ComponentImplementation122 = value if value is not None else set()
        
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
    def aadl2_ComponentImplementation106(self):
        return self.__aadl2_ComponentImplementation106

    @aadl2_ComponentImplementation106.setter
    def aadl2_ComponentImplementation106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation106", None)
        self.__aadl2_ComponentImplementation106 = value if value is not None else set()
        
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
    def aadl2_ComponentImplementation134(self):
        return self.__aadl2_ComponentImplementation134

    @aadl2_ComponentImplementation134.setter
    def aadl2_ComponentImplementation134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation134", None)
        self.__aadl2_ComponentImplementation134 = value if value is not None else set()
        
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
    def aadl2_ComponentImplementation101(self):
        return self.__aadl2_ComponentImplementation101

    @aadl2_ComponentImplementation101.setter
    def aadl2_ComponentImplementation101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation101", None)
        self.__aadl2_ComponentImplementation101 = value if value is not None else set()
        
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
                    

    def getAllSubcomponents(self) -> str:
        # TODO: Implement getAllSubcomponents method
        pass

class aadl2_CalledSubprogram(ABC):

    pass
class ModeFeature:

    pass
class aadl2_ModeTransition(ModeFeature):

    pass
class RefinableElement:

    pass
class CalledSubprogram:

    pass
class aadl2_SubprogramAccess(Access, CalledSubprogram, Context):

    pass
class aadl2_SubprogramProxy(ProcessorFeature, CalledSubprogram, AccessConnectionEnd):

    pass
class StructuralFeature:

    pass
class aadl2_ProcessorFeature(StructuralFeature):

    pass
class aadl2_InternalFeature(FeatureConnectionEnd, PortConnectionEnd, TriggerPort, StructuralFeature):

    def __init__(self, direction: str, in: str, out: str, aadl2_InternalFeature: "aadl2_ComponentImplementation" = None):
        self.direction = direction
        self.in = in
        self.out = out
        self.aadl2_InternalFeature = aadl2_InternalFeature
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def in(self) -> str:
        return self.__in

    @in.setter
    def in(self, in: str):
        self.__in = in

    @property
    def out(self) -> str:
        return self.__out

    @out.setter
    def out(self, out: str):
        self.__out = out

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
            if hasattr(old_value, "aadl2_ComponentImplementation130"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation130", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation130"):
                opp_val = getattr(value, "aadl2_ComponentImplementation130", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentImplementation130", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aadl2_Feature(FeatureConnectionEnd, ArrayableElement, StructuralFeature):

    pass
class aadl2_Connection(ModalPath, StructuralFeature, FlowElement):

    def __init__(self, bidirectional: str, aadl2_Connection: "aadl2_ComponentImplementation" = None, aadl2_Connection310: "aadl2_ConnectedElement" = None, aadl2_Connection312: "aadl2_ConnectedElement" = None, aadl2_Connection316: "aadl2_Connection" = None, aadl2_Connection314: "aadl2_Connection" = None):
        self.bidirectional = bidirectional
        self.aadl2_Connection = aadl2_Connection
        self.aadl2_Connection310 = aadl2_Connection310
        self.aadl2_Connection312 = aadl2_Connection312
        self.aadl2_Connection316 = aadl2_Connection316
        self.aadl2_Connection314 = aadl2_Connection314
        
    @property
    def bidirectional(self) -> str:
        return self.__bidirectional

    @bidirectional.setter
    def bidirectional(self, bidirectional: str):
        self.__bidirectional = bidirectional

    @property
    def aadl2_Connection316(self):
        return self.__aadl2_Connection316

    @aadl2_Connection316.setter
    def aadl2_Connection316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Connection__aadl2_Connection316", None)
        self.__aadl2_Connection316 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Connection314"):
                opp_val = getattr(old_value, "aadl2_Connection314", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Connection314", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Connection314"):
                opp_val = getattr(value, "aadl2_Connection314", None)
                setattr(value, "aadl2_Connection314", self)

    @property
    def aadl2_Connection312(self):
        return self.__aadl2_Connection312

    @aadl2_Connection312.setter
    def aadl2_Connection312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Connection__aadl2_Connection312", None)
        self.__aadl2_Connection312 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ConnectedElement313"):
                opp_val = getattr(old_value, "aadl2_ConnectedElement313", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ConnectedElement313", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ConnectedElement313"):
                opp_val = getattr(value, "aadl2_ConnectedElement313", None)
                setattr(value, "aadl2_ConnectedElement313", self)

    @property
    def aadl2_Connection310(self):
        return self.__aadl2_Connection310

    @aadl2_Connection310.setter
    def aadl2_Connection310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Connection__aadl2_Connection310", None)
        self.__aadl2_Connection310 = value
        
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
    def aadl2_Connection314(self):
        return self.__aadl2_Connection314

    @aadl2_Connection314.setter
    def aadl2_Connection314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Connection__aadl2_Connection314", None)
        self.__aadl2_Connection314 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Connection316"):
                opp_val = getattr(old_value, "aadl2_Connection316", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Connection316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Connection316"):
                opp_val = getattr(value, "aadl2_Connection316", None)
                setattr(value, "aadl2_Connection316", self)

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
            if hasattr(old_value, "aadl2_ComponentImplementation108"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation108", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation108"):
                opp_val = getattr(value, "aadl2_ComponentImplementation108", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentImplementation108", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aadl2_FlowFeature(Flow, StructuralFeature):

    pass
class ClassifierFeature:

    pass
class aadl2_StructuralFeature(ClassifierFeature, RefinableElement):

    pass
class aadl2_BehavioralFeature(ClassifierFeature):

    pass
class aadl2_FlowImplementation(Flow, ClassifierFeature, ModalPath):

    def __init__(self, kind: str, aadl2_FlowImplementation: "aadl2_ComponentImplementation" = None, aadl2_FlowImplementation294: "aadl2_FlowSpecification" = None, aadl2_FlowImplementation297: set["aadl2_FlowSegment"] = None, aadl2_FlowImplementation299: "aadl2_FlowEnd" = None, aadl2_FlowImplementation302: "aadl2_FlowEnd" = None):
        self.kind = kind
        self.aadl2_FlowImplementation = aadl2_FlowImplementation
        self.aadl2_FlowImplementation294 = aadl2_FlowImplementation294
        self.aadl2_FlowImplementation297 = aadl2_FlowImplementation297 if aadl2_FlowImplementation297 is not None else set()
        self.aadl2_FlowImplementation299 = aadl2_FlowImplementation299
        self.aadl2_FlowImplementation302 = aadl2_FlowImplementation302
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def aadl2_FlowImplementation294(self):
        return self.__aadl2_FlowImplementation294

    @aadl2_FlowImplementation294.setter
    def aadl2_FlowImplementation294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowImplementation__aadl2_FlowImplementation294", None)
        self.__aadl2_FlowImplementation294 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FlowSpecification295"):
                opp_val = getattr(old_value, "aadl2_FlowSpecification295", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FlowSpecification295", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FlowSpecification295"):
                opp_val = getattr(value, "aadl2_FlowSpecification295", None)
                setattr(value, "aadl2_FlowSpecification295", self)

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
            if hasattr(old_value, "aadl2_ComponentImplementation106"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation106", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation106"):
                opp_val = getattr(value, "aadl2_ComponentImplementation106", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentImplementation106", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_FlowImplementation297(self):
        return self.__aadl2_FlowImplementation297

    @aadl2_FlowImplementation297.setter
    def aadl2_FlowImplementation297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowImplementation__aadl2_FlowImplementation297", None)
        self.__aadl2_FlowImplementation297 = value if value is not None else set()
        
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
    def aadl2_FlowImplementation299(self):
        return self.__aadl2_FlowImplementation299

    @aadl2_FlowImplementation299.setter
    def aadl2_FlowImplementation299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowImplementation__aadl2_FlowImplementation299", None)
        self.__aadl2_FlowImplementation299 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FlowEnd300"):
                opp_val = getattr(old_value, "aadl2_FlowEnd300", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FlowEnd300", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FlowEnd300"):
                opp_val = getattr(value, "aadl2_FlowEnd300", None)
                setattr(value, "aadl2_FlowEnd300", self)

    @property
    def aadl2_FlowImplementation302(self):
        return self.__aadl2_FlowImplementation302

    @aadl2_FlowImplementation302.setter
    def aadl2_FlowImplementation302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowImplementation__aadl2_FlowImplementation302", None)
        self.__aadl2_FlowImplementation302 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FlowEnd303"):
                opp_val = getattr(old_value, "aadl2_FlowEnd303", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FlowEnd303", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FlowEnd303"):
                opp_val = getattr(value, "aadl2_FlowEnd303", None)
                setattr(value, "aadl2_FlowEnd303", self)

class aadl2_ModeFeature(ClassifierFeature):

    pass
class aadl2_Mode(ModeFeature):

    def __init__(self, initial: str, derived: str, aadl2_Mode: "aadl2_ModalElement" = None, aadl2_Mode140: "aadl2_ComponentClassifier" = None, aadl2_Mode145: "aadl2_ModeTransition" = None, aadl2_Mode148: "aadl2_ModeTransition" = None, aadl2_Mode289: "aadl2_ModeBinding" = None, aadl2_Mode292: "aadl2_ModeBinding" = None):
        self.initial = initial
        self.derived = derived
        self.aadl2_Mode = aadl2_Mode
        self.aadl2_Mode140 = aadl2_Mode140
        self.aadl2_Mode145 = aadl2_Mode145
        self.aadl2_Mode148 = aadl2_Mode148
        self.aadl2_Mode289 = aadl2_Mode289
        self.aadl2_Mode292 = aadl2_Mode292
        
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
    def aadl2_Mode148(self):
        return self.__aadl2_Mode148

    @aadl2_Mode148.setter
    def aadl2_Mode148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Mode__aadl2_Mode148", None)
        self.__aadl2_Mode148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ModeTransition147"):
                opp_val = getattr(old_value, "aadl2_ModeTransition147", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ModeTransition147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ModeTransition147"):
                opp_val = getattr(value, "aadl2_ModeTransition147", None)
                setattr(value, "aadl2_ModeTransition147", self)

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

    @property
    def aadl2_Mode140(self):
        return self.__aadl2_Mode140

    @aadl2_Mode140.setter
    def aadl2_Mode140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Mode__aadl2_Mode140", None)
        self.__aadl2_Mode140 = value
        
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
    def aadl2_Mode292(self):
        return self.__aadl2_Mode292

    @aadl2_Mode292.setter
    def aadl2_Mode292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Mode__aadl2_Mode292", None)
        self.__aadl2_Mode292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ModeBinding291"):
                opp_val = getattr(old_value, "aadl2_ModeBinding291", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ModeBinding291", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ModeBinding291"):
                opp_val = getattr(value, "aadl2_ModeBinding291", None)
                setattr(value, "aadl2_ModeBinding291", self)

    @property
    def aadl2_Mode289(self):
        return self.__aadl2_Mode289

    @aadl2_Mode289.setter
    def aadl2_Mode289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Mode__aadl2_Mode289", None)
        self.__aadl2_Mode289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ModeBinding288"):
                opp_val = getattr(old_value, "aadl2_ModeBinding288", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ModeBinding288", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ModeBinding288"):
                opp_val = getattr(value, "aadl2_ModeBinding288", None)
                setattr(value, "aadl2_ModeBinding288", self)

    @property
    def aadl2_Mode145(self):
        return self.__aadl2_Mode145

    @aadl2_Mode145.setter
    def aadl2_Mode145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Mode__aadl2_Mode145", None)
        self.__aadl2_Mode145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ModeTransition144"):
                opp_val = getattr(old_value, "aadl2_ModeTransition144", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ModeTransition144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ModeTransition144"):
                opp_val = getattr(value, "aadl2_ModeTransition144", None)
                setattr(value, "aadl2_ModeTransition144", self)

class ModalElement:

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

class aadl2_Subcomponent(ArrayableElement, ModalElement, FlowElement, StructuralFeature, Context):

    def __init__(self, allModes: str, aadl2_Subcomponent: "aadl2_ComponentImplementation" = None, aadl2_Subcomponent269: "aadl2_SubcomponentType" = None, aadl2_Subcomponent271: set["aadl2_PrototypeBinding"] = None, aadl2_Subcomponent274: "aadl2_ComponentPrototype" = None, aadl2_Subcomponent277: set["aadl2_ModeBinding"] = None, aadl2_Subcomponent285: "aadl2_ComponentClassifier" = None, aadl2_Subcomponent279: set["aadl2_ComponentImplementationReference"] = None, aadl2_Subcomponent283: "aadl2_Subcomponent" = None, aadl2_Subcomponent281: "aadl2_Subcomponent" = None):
        self.allModes = allModes
        self.aadl2_Subcomponent = aadl2_Subcomponent
        self.aadl2_Subcomponent269 = aadl2_Subcomponent269
        self.aadl2_Subcomponent271 = aadl2_Subcomponent271 if aadl2_Subcomponent271 is not None else set()
        self.aadl2_Subcomponent274 = aadl2_Subcomponent274
        self.aadl2_Subcomponent277 = aadl2_Subcomponent277 if aadl2_Subcomponent277 is not None else set()
        self.aadl2_Subcomponent285 = aadl2_Subcomponent285
        self.aadl2_Subcomponent279 = aadl2_Subcomponent279 if aadl2_Subcomponent279 is not None else set()
        self.aadl2_Subcomponent283 = aadl2_Subcomponent283
        self.aadl2_Subcomponent281 = aadl2_Subcomponent281
        
    @property
    def allModes(self) -> str:
        return self.__allModes

    @allModes.setter
    def allModes(self, allModes: str):
        self.__allModes = allModes

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
            if hasattr(old_value, "aadl2_ComponentPrototype275"):
                opp_val = getattr(old_value, "aadl2_ComponentPrototype275", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentPrototype275", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentPrototype275"):
                opp_val = getattr(value, "aadl2_ComponentPrototype275", None)
                setattr(value, "aadl2_ComponentPrototype275", self)

    @property
    def aadl2_Subcomponent269(self):
        return self.__aadl2_Subcomponent269

    @aadl2_Subcomponent269.setter
    def aadl2_Subcomponent269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent269", None)
        self.__aadl2_Subcomponent269 = value
        
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
    def aadl2_Subcomponent(self):
        return self.__aadl2_Subcomponent

    @aadl2_Subcomponent.setter
    def aadl2_Subcomponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent", None)
        self.__aadl2_Subcomponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentImplementation101"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation101", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation101"):
                opp_val = getattr(value, "aadl2_ComponentImplementation101", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentImplementation101", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_Subcomponent271(self):
        return self.__aadl2_Subcomponent271

    @aadl2_Subcomponent271.setter
    def aadl2_Subcomponent271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent271", None)
        self.__aadl2_Subcomponent271 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_PrototypeBinding272"):
                    opp_val = getattr(item, "aadl2_PrototypeBinding272", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_PrototypeBinding272", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_PrototypeBinding272"):
                    opp_val = getattr(item, "aadl2_PrototypeBinding272", None)
                    
                    setattr(item, "aadl2_PrototypeBinding272", self)
                    

    @property
    def aadl2_Subcomponent281(self):
        return self.__aadl2_Subcomponent281

    @aadl2_Subcomponent281.setter
    def aadl2_Subcomponent281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent281", None)
        self.__aadl2_Subcomponent281 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Subcomponent283"):
                opp_val = getattr(old_value, "aadl2_Subcomponent283", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Subcomponent283", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Subcomponent283"):
                opp_val = getattr(value, "aadl2_Subcomponent283", None)
                setattr(value, "aadl2_Subcomponent283", self)

    @property
    def aadl2_Subcomponent279(self):
        return self.__aadl2_Subcomponent279

    @aadl2_Subcomponent279.setter
    def aadl2_Subcomponent279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent279", None)
        self.__aadl2_Subcomponent279 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ComponentImplementationReference280"):
                    opp_val = getattr(item, "aadl2_ComponentImplementationReference280", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ComponentImplementationReference280", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ComponentImplementationReference280"):
                    opp_val = getattr(item, "aadl2_ComponentImplementationReference280", None)
                    
                    setattr(item, "aadl2_ComponentImplementationReference280", self)
                    

    @property
    def aadl2_Subcomponent277(self):
        return self.__aadl2_Subcomponent277

    @aadl2_Subcomponent277.setter
    def aadl2_Subcomponent277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent277", None)
        self.__aadl2_Subcomponent277 = value if value is not None else set()
        
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
    def aadl2_Subcomponent283(self):
        return self.__aadl2_Subcomponent283

    @aadl2_Subcomponent283.setter
    def aadl2_Subcomponent283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent283", None)
        self.__aadl2_Subcomponent283 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Subcomponent281"):
                opp_val = getattr(old_value, "aadl2_Subcomponent281", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Subcomponent281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Subcomponent281"):
                opp_val = getattr(value, "aadl2_Subcomponent281", None)
                setattr(value, "aadl2_Subcomponent281", self)

    @property
    def aadl2_Subcomponent285(self):
        return self.__aadl2_Subcomponent285

    @aadl2_Subcomponent285.setter
    def aadl2_Subcomponent285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent285", None)
        self.__aadl2_Subcomponent285 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentClassifier286"):
                opp_val = getattr(old_value, "aadl2_ComponentClassifier286", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentClassifier286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentClassifier286"):
                opp_val = getattr(value, "aadl2_ComponentClassifier286", None)
                setattr(value, "aadl2_ComponentClassifier286", self)

class aadl2_SubprogramCallSequence(ModalElement, BehavioralFeature):

    pass
class Relationship:

    pass
class aadl2_DirectedRelationship(Relationship):

    pass
class DirectedRelationship:

    pass
class aadl2_Prototype(CalledSubprogram, StructuralFeature):

    pass
class aadl2_AnnexSubclause(ModalElement):

    pass
class aadl2_Generalization(DirectedRelationship):

    pass
class Namespace:

    pass
class aadl2_GlobalNamespace(Namespace):

    pass
class aadl2_PropertySet(Namespace, ModelUnit):

    pass
class aadl2_PackageSection(Namespace):

    def __init__(self, noAnnexes: str, noProperties: str, aadl2_PackageSection: set["aadl2_PackageRename"] = None, aadl2_PackageSection356: set["aadl2_ComponentTypeRename"] = None, aadl2_PackageSection358: set["aadl2_Classifier"] = None, aadl2_PackageSection361: set["aadl2_FeatureGroupTypeRename"] = None, aadl2_PackageSection363: set["aadl2_AnnexLibrary"] = None, aadl2_PackageSection366: set["aadl2_ModelUnit"] = None):
        self.noAnnexes = noAnnexes
        self.noProperties = noProperties
        self.aadl2_PackageSection = aadl2_PackageSection if aadl2_PackageSection is not None else set()
        self.aadl2_PackageSection356 = aadl2_PackageSection356 if aadl2_PackageSection356 is not None else set()
        self.aadl2_PackageSection358 = aadl2_PackageSection358 if aadl2_PackageSection358 is not None else set()
        self.aadl2_PackageSection361 = aadl2_PackageSection361 if aadl2_PackageSection361 is not None else set()
        self.aadl2_PackageSection363 = aadl2_PackageSection363 if aadl2_PackageSection363 is not None else set()
        self.aadl2_PackageSection366 = aadl2_PackageSection366 if aadl2_PackageSection366 is not None else set()
        
    @property
    def noProperties(self) -> str:
        return self.__noProperties

    @noProperties.setter
    def noProperties(self, noProperties: str):
        self.__noProperties = noProperties

    @property
    def noAnnexes(self) -> str:
        return self.__noAnnexes

    @noAnnexes.setter
    def noAnnexes(self, noAnnexes: str):
        self.__noAnnexes = noAnnexes

    @property
    def aadl2_PackageSection358(self):
        return self.__aadl2_PackageSection358

    @aadl2_PackageSection358.setter
    def aadl2_PackageSection358(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection358", None)
        self.__aadl2_PackageSection358 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_Classifier359"):
                    opp_val = getattr(item, "aadl2_Classifier359", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Classifier359", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Classifier359"):
                    opp_val = getattr(item, "aadl2_Classifier359", None)
                    
                    setattr(item, "aadl2_Classifier359", self)
                    

    @property
    def aadl2_PackageSection366(self):
        return self.__aadl2_PackageSection366

    @aadl2_PackageSection366.setter
    def aadl2_PackageSection366(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection366", None)
        self.__aadl2_PackageSection366 = value if value is not None else set()
        
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
    def aadl2_PackageSection363(self):
        return self.__aadl2_PackageSection363

    @aadl2_PackageSection363.setter
    def aadl2_PackageSection363(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection363", None)
        self.__aadl2_PackageSection363 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_AnnexLibrary364"):
                    opp_val = getattr(item, "aadl2_AnnexLibrary364", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_AnnexLibrary364", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_AnnexLibrary364"):
                    opp_val = getattr(item, "aadl2_AnnexLibrary364", None)
                    
                    setattr(item, "aadl2_AnnexLibrary364", self)
                    

    @property
    def aadl2_PackageSection361(self):
        return self.__aadl2_PackageSection361

    @aadl2_PackageSection361.setter
    def aadl2_PackageSection361(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection361", None)
        self.__aadl2_PackageSection361 = value if value is not None else set()
        
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
    def aadl2_PackageSection356(self):
        return self.__aadl2_PackageSection356

    @aadl2_PackageSection356.setter
    def aadl2_PackageSection356(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection356", None)
        self.__aadl2_PackageSection356 = value if value is not None else set()
        
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
                    

class aadl2_RecordType(Namespace, NonListType):

    pass
class aadl2_EnumerationType(Namespace, NonListType):

    pass
class PropertyOwner:

    pass
class aadl2_ClassifierValue(PropertyValue, PropertyOwner):

    pass
class aadl2_AbstractNamedValue(ABC):

    pass
class Type:

    pass
class aadl2_SubcomponentType(Type):

    pass
class aadl2_ModalPropertyValue(ModalElement):

    pass
class aadl2_PropertyType(Type):

    pass
class TypedElement:

    pass
class aadl2_BasicProperty(TypedElement):

    pass
class aadl2_MetaclassReference(PropertyOwner):

    def __init__(self, annexName: str, metaclassName: str, aadl2_MetaclassReference: "aadl2_Property" = None, aadl2_MetaclassReference877: "aadl2_ClassifierType" = None, aadl2_MetaclassReference889: "aadl2_ReferenceType" = None):
        self.annexName = annexName
        self.metaclassName = metaclassName
        self.aadl2_MetaclassReference = aadl2_MetaclassReference
        self.aadl2_MetaclassReference877 = aadl2_MetaclassReference877
        self.aadl2_MetaclassReference889 = aadl2_MetaclassReference889
        
    @property
    def metaclassName(self) -> str:
        return self.__metaclassName

    @metaclassName.setter
    def metaclassName(self, metaclassName: str):
        self.__metaclassName = metaclassName

    @property
    def annexName(self) -> str:
        return self.__annexName

    @annexName.setter
    def annexName(self, annexName: str):
        self.__annexName = annexName

    @property
    def aadl2_MetaclassReference877(self):
        return self.__aadl2_MetaclassReference877

    @aadl2_MetaclassReference877.setter
    def aadl2_MetaclassReference877(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_MetaclassReference__aadl2_MetaclassReference877", None)
        self.__aadl2_MetaclassReference877 = value
        
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
    def aadl2_MetaclassReference889(self):
        return self.__aadl2_MetaclassReference889

    @aadl2_MetaclassReference889.setter
    def aadl2_MetaclassReference889(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_MetaclassReference__aadl2_MetaclassReference889", None)
        self.__aadl2_MetaclassReference889 = value
        
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

class AbstractNamedValue:

    pass
class aadl2_PropertyConstant(ArraySizeProperty, AbstractNamedValue, TypedElement):

    pass
class BasicProperty:

    pass
class aadl2_RecordField(BasicProperty):

    pass
class aadl2_Classifier(Type, Namespace):

    def __init__(self, noPrototypes: str, noAnnexes: str, noProperties: str, aadl2_Classifier: "aadl2_PropertyAssociation" = None, aadl2_Classifier19: "aadl2_Property" = None, featuringClassifier: set["aadl2_ClassifierFeature"] = None, aadl2_Classifier32: set["aadl2_NamedElement"] = None, specific: set["aadl2_Generalization"] = None, aadl2_Classifier37: "aadl2_Classifier" = None, aadl2_Classifier35: set["aadl2_Classifier"] = None, aadl2_Classifier39: set["aadl2_AnnexSubclause"] = None, aadl2_Classifier41: set["aadl2_Prototype"] = None, aadl2_Classifier43: set["aadl2_PrototypeBinding"] = None, aadl2_Classifier51: "aadl2_Generalization" = None, Classifier53: "aadl2_Generalization" = None, Classifier: "aadl2_ClassifierFeature" = None, aadl2_Classifier66: "aadl2_RefinableElement" = None, aadl2_Classifier177: "aadl2_Feature" = None, aadl2_Classifier359: "aadl2_PackageSection" = None, aadl2_Classifier825: "aadl2_ClassifierValue" = None):
        self.noPrototypes = noPrototypes
        self.noAnnexes = noAnnexes
        self.noProperties = noProperties
        self.aadl2_Classifier = aadl2_Classifier
        self.aadl2_Classifier19 = aadl2_Classifier19
        self.featuringClassifier = featuringClassifier if featuringClassifier is not None else set()
        self.aadl2_Classifier32 = aadl2_Classifier32 if aadl2_Classifier32 is not None else set()
        self.specific = specific if specific is not None else set()
        self.aadl2_Classifier37 = aadl2_Classifier37
        self.aadl2_Classifier35 = aadl2_Classifier35 if aadl2_Classifier35 is not None else set()
        self.aadl2_Classifier39 = aadl2_Classifier39 if aadl2_Classifier39 is not None else set()
        self.aadl2_Classifier41 = aadl2_Classifier41 if aadl2_Classifier41 is not None else set()
        self.aadl2_Classifier43 = aadl2_Classifier43 if aadl2_Classifier43 is not None else set()
        self.aadl2_Classifier51 = aadl2_Classifier51
        self.Classifier53 = Classifier53
        self.Classifier = Classifier
        self.aadl2_Classifier66 = aadl2_Classifier66
        self.aadl2_Classifier177 = aadl2_Classifier177
        self.aadl2_Classifier359 = aadl2_Classifier359
        self.aadl2_Classifier825 = aadl2_Classifier825
        
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
    def Classifier53(self):
        return self.__Classifier53

    @Classifier53.setter
    def Classifier53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__Classifier53", None)
        self.__Classifier53 = value
        
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
    def aadl2_Classifier39(self):
        return self.__aadl2_Classifier39

    @aadl2_Classifier39.setter
    def aadl2_Classifier39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier39", None)
        self.__aadl2_Classifier39 = value if value is not None else set()
        
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
    def aadl2_Classifier41(self):
        return self.__aadl2_Classifier41

    @aadl2_Classifier41.setter
    def aadl2_Classifier41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier41", None)
        self.__aadl2_Classifier41 = value if value is not None else set()
        
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
    def aadl2_Classifier43(self):
        return self.__aadl2_Classifier43

    @aadl2_Classifier43.setter
    def aadl2_Classifier43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier43", None)
        self.__aadl2_Classifier43 = value if value is not None else set()
        
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
    def aadl2_Classifier35(self):
        return self.__aadl2_Classifier35

    @aadl2_Classifier35.setter
    def aadl2_Classifier35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier35", None)
        self.__aadl2_Classifier35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_Classifier37"):
                    opp_val = getattr(item, "aadl2_Classifier37", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Classifier37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Classifier37"):
                    opp_val = getattr(item, "aadl2_Classifier37", None)
                    
                    setattr(item, "aadl2_Classifier37", self)
                    

    @property
    def aadl2_Classifier66(self):
        return self.__aadl2_Classifier66

    @aadl2_Classifier66.setter
    def aadl2_Classifier66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier66", None)
        self.__aadl2_Classifier66 = value
        
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
                if hasattr(item, "aadl2_NamedElement33"):
                    opp_val = getattr(item, "aadl2_NamedElement33", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_NamedElement33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_NamedElement33"):
                    opp_val = getattr(item, "aadl2_NamedElement33", None)
                    
                    setattr(item, "aadl2_NamedElement33", self)
                    

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
    def aadl2_Classifier359(self):
        return self.__aadl2_Classifier359

    @aadl2_Classifier359.setter
    def aadl2_Classifier359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier359", None)
        self.__aadl2_Classifier359 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PackageSection358"):
                opp_val = getattr(old_value, "aadl2_PackageSection358", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PackageSection358"):
                opp_val = getattr(value, "aadl2_PackageSection358", None)
                if opp_val is None:
                    setattr(value, "aadl2_PackageSection358", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def aadl2_Classifier51(self):
        return self.__aadl2_Classifier51

    @aadl2_Classifier51.setter
    def aadl2_Classifier51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier51", None)
        self.__aadl2_Classifier51 = value
        
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
    def aadl2_Classifier37(self):
        return self.__aadl2_Classifier37

    @aadl2_Classifier37.setter
    def aadl2_Classifier37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier37", None)
        self.__aadl2_Classifier37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Classifier35"):
                opp_val = getattr(old_value, "aadl2_Classifier35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Classifier35"):
                opp_val = getattr(value, "aadl2_Classifier35", None)
                if opp_val is None:
                    setattr(value, "aadl2_Classifier35", set([self]))
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
    def aadl2_Classifier177(self):
        return self.__aadl2_Classifier177

    @aadl2_Classifier177.setter
    def aadl2_Classifier177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier177", None)
        self.__aadl2_Classifier177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Feature176"):
                opp_val = getattr(old_value, "aadl2_Feature176", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Feature176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Feature176"):
                opp_val = getattr(value, "aadl2_Feature176", None)
                setattr(value, "aadl2_Feature176", self)

    @property
    def aadl2_Classifier825(self):
        return self.__aadl2_Classifier825

    @aadl2_Classifier825.setter
    def aadl2_Classifier825(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier825", None)
        self.__aadl2_Classifier825 = value
        
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

class aadl2_Property(BasicProperty, AbstractNamedValue):

    def __init__(self, inherit: str, emptyListDefault: str, aadl2_Property: "aadl2_PropertyAssociation" = None, aadl2_Property14: "aadl2_PropertyExpression" = None, aadl2_Property16: set["aadl2_MetaclassReference"] = None, aadl2_Property18: set["aadl2_Classifier"] = None, aadl2_Property21: set["aadl2_PropertyOwner"] = None, aadl2_Property845: "aadl2_PropertySet" = None):
        self.inherit = inherit
        self.emptyListDefault = emptyListDefault
        self.aadl2_Property = aadl2_Property
        self.aadl2_Property14 = aadl2_Property14
        self.aadl2_Property16 = aadl2_Property16 if aadl2_Property16 is not None else set()
        self.aadl2_Property18 = aadl2_Property18 if aadl2_Property18 is not None else set()
        self.aadl2_Property21 = aadl2_Property21 if aadl2_Property21 is not None else set()
        self.aadl2_Property845 = aadl2_Property845
        
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
    def aadl2_Property845(self):
        return self.__aadl2_Property845

    @aadl2_Property845.setter
    def aadl2_Property845(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Property__aadl2_Property845", None)
        self.__aadl2_Property845 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PropertySet844"):
                opp_val = getattr(old_value, "aadl2_PropertySet844", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PropertySet844"):
                opp_val = getattr(value, "aadl2_PropertySet844", None)
                if opp_val is None:
                    setattr(value, "aadl2_PropertySet844", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class NamedElement:

    pass
class aadl2_Namespace(NamedElement):

    pass
class aadl2_SubprogramGroup(NamedElement):

    pass
class aadl2_Subprogram(NamedElement, CalledSubprogram):

    pass
class aadl2_System(NamedElement):

    pass
class aadl2_ClassifierFeature(NamedElement):

    pass
class aadl2_RefinableElement(NamedElement):

    pass
class aadl2_ConnectionEnd(NamedElement):

    pass
class aadl2_Device(NamedElement):

    pass
class aadl2_VirtualBus(NamedElement):

    pass
class aadl2_Context(NamedElement):

    pass
class aadl2_AnnexLibrary(NamedElement):

    pass
class aadl2_EndToEndFlowElement(NamedElement):

    pass
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

class aadl2_Flow(NamedElement):

    pass
class aadl2_EnumerationLiteral(NamedElement, AbstractNamedValue):

    pass
class aadl2_Abstract(NamedElement):

    pass
class aadl2_Processor(NamedElement):

    pass
class aadl2_ComponentTypeRename(NamedElement):

    def __init__(self, category: str, aadl2_ComponentTypeRename: "aadl2_PackageSection" = None, aadl2_ComponentTypeRename381: "aadl2_ComponentType" = None):
        self.category = category
        self.aadl2_ComponentTypeRename = aadl2_ComponentTypeRename
        self.aadl2_ComponentTypeRename381 = aadl2_ComponentTypeRename381
        
    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

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
            if hasattr(old_value, "aadl2_PackageSection356"):
                opp_val = getattr(old_value, "aadl2_PackageSection356", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PackageSection356"):
                opp_val = getattr(value, "aadl2_PackageSection356", None)
                if opp_val is None:
                    setattr(value, "aadl2_PackageSection356", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_ComponentTypeRename381(self):
        return self.__aadl2_ComponentTypeRename381

    @aadl2_ComponentTypeRename381.setter
    def aadl2_ComponentTypeRename381(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentTypeRename__aadl2_ComponentTypeRename381", None)
        self.__aadl2_ComponentTypeRename381 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentType382"):
                opp_val = getattr(old_value, "aadl2_ComponentType382", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentType382", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentType382"):
                opp_val = getattr(value, "aadl2_ComponentType382", None)
                setattr(value, "aadl2_ComponentType382", self)

class aadl2_ModelUnit(NamedElement):

    pass
class aadl2_VirtualProcessor(NamedElement):

    pass
class aadl2_FeatureGroupTypeRename(NamedElement):

    pass
class aadl2_Bus(NamedElement):

    pass
class aadl2_Data(NamedElement):

    pass
class aadl2_TriggerPort(NamedElement):

    pass
class aadl2_TypedElement(NamedElement):

    pass
class aadl2_ThreadGroup(NamedElement):

    pass
class aadl2_PackageRename(NamedElement):

    def __init__(self, renameAll: str, aadl2_PackageRename: "aadl2_PackageSection" = None, aadl2_PackageRename368: "aadl2_AadlPackage" = None):
        self.renameAll = renameAll
        self.aadl2_PackageRename = aadl2_PackageRename
        self.aadl2_PackageRename368 = aadl2_PackageRename368
        
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
    def aadl2_PackageRename368(self):
        return self.__aadl2_PackageRename368

    @aadl2_PackageRename368.setter
    def aadl2_PackageRename368(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageRename__aadl2_PackageRename368", None)
        self.__aadl2_PackageRename368 = value
        
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

class aadl2_Thread(NamedElement):

    pass
class aadl2_Memory(NamedElement):

    pass
class aadl2_Process(NamedElement):

    pass
class aadl2_Type(NamedElement):

    pass
class Element:

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

class aadl2_ContainmentPathElement(Element):

    def __init__(self, annexName: str, aadl2_ContainmentPathElement: "aadl2_ContainedNamedElement" = None, aadl2_ContainmentPathElement77: "aadl2_ContainedNamedElement" = None, aadl2_ContainmentPathElement85: "aadl2_ContainmentPathElement" = None, aadl2_ContainmentPathElement83: "aadl2_ContainmentPathElement" = None, aadl2_ContainmentPathElement79: set["aadl2_ArrayRange"] = None, aadl2_ContainmentPathElement81: "aadl2_NamedElement" = None):
        self.annexName = annexName
        self.aadl2_ContainmentPathElement = aadl2_ContainmentPathElement
        self.aadl2_ContainmentPathElement77 = aadl2_ContainmentPathElement77
        self.aadl2_ContainmentPathElement85 = aadl2_ContainmentPathElement85
        self.aadl2_ContainmentPathElement83 = aadl2_ContainmentPathElement83
        self.aadl2_ContainmentPathElement79 = aadl2_ContainmentPathElement79 if aadl2_ContainmentPathElement79 is not None else set()
        self.aadl2_ContainmentPathElement81 = aadl2_ContainmentPathElement81
        
    @property
    def annexName(self) -> str:
        return self.__annexName

    @annexName.setter
    def annexName(self, annexName: str):
        self.__annexName = annexName

    @property
    def aadl2_ContainmentPathElement83(self):
        return self.__aadl2_ContainmentPathElement83

    @aadl2_ContainmentPathElement83.setter
    def aadl2_ContainmentPathElement83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ContainmentPathElement__aadl2_ContainmentPathElement83", None)
        self.__aadl2_ContainmentPathElement83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ContainmentPathElement85"):
                opp_val = getattr(old_value, "aadl2_ContainmentPathElement85", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ContainmentPathElement85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ContainmentPathElement85"):
                opp_val = getattr(value, "aadl2_ContainmentPathElement85", None)
                setattr(value, "aadl2_ContainmentPathElement85", self)

    @property
    def aadl2_ContainmentPathElement81(self):
        return self.__aadl2_ContainmentPathElement81

    @aadl2_ContainmentPathElement81.setter
    def aadl2_ContainmentPathElement81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ContainmentPathElement__aadl2_ContainmentPathElement81", None)
        self.__aadl2_ContainmentPathElement81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_NamedElement82"):
                opp_val = getattr(old_value, "aadl2_NamedElement82", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_NamedElement82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_NamedElement82"):
                opp_val = getattr(value, "aadl2_NamedElement82", None)
                setattr(value, "aadl2_NamedElement82", self)

    @property
    def aadl2_ContainmentPathElement77(self):
        return self.__aadl2_ContainmentPathElement77

    @aadl2_ContainmentPathElement77.setter
    def aadl2_ContainmentPathElement77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ContainmentPathElement__aadl2_ContainmentPathElement77", None)
        self.__aadl2_ContainmentPathElement77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ContainedNamedElement76"):
                opp_val = getattr(old_value, "aadl2_ContainedNamedElement76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ContainedNamedElement76"):
                opp_val = getattr(value, "aadl2_ContainedNamedElement76", None)
                if opp_val is None:
                    setattr(value, "aadl2_ContainedNamedElement76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "aadl2_ContainedNamedElement74"):
                opp_val = getattr(old_value, "aadl2_ContainedNamedElement74", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ContainedNamedElement74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ContainedNamedElement74"):
                opp_val = getattr(value, "aadl2_ContainedNamedElement74", None)
                setattr(value, "aadl2_ContainedNamedElement74", self)

    @property
    def aadl2_ContainmentPathElement85(self):
        return self.__aadl2_ContainmentPathElement85

    @aadl2_ContainmentPathElement85.setter
    def aadl2_ContainmentPathElement85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ContainmentPathElement__aadl2_ContainmentPathElement85", None)
        self.__aadl2_ContainmentPathElement85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ContainmentPathElement83"):
                opp_val = getattr(old_value, "aadl2_ContainmentPathElement83", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ContainmentPathElement83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ContainmentPathElement83"):
                opp_val = getattr(value, "aadl2_ContainmentPathElement83", None)
                setattr(value, "aadl2_ContainmentPathElement83", self)

    @property
    def aadl2_ContainmentPathElement79(self):
        return self.__aadl2_ContainmentPathElement79

    @aadl2_ContainmentPathElement79.setter
    def aadl2_ContainmentPathElement79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ContainmentPathElement__aadl2_ContainmentPathElement79", None)
        self.__aadl2_ContainmentPathElement79 = value if value is not None else set()
        
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
                    

class aadl2_ModeTransitionTrigger(Element):

    pass
class aadl2_Relationship(Element):

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

class aadl2_PropertyOwner(Element):

    pass
class aadl2_BasicPropertyAssociation(Element):

    pass
class aadl2_ConnectedElement(Element):

    pass
class aadl2_ContainedNamedElement(Element):

    pass
class aadl2_FlowSegment(Element):

    pass
class aadl2_PrototypeBinding(Element):

    pass
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
            if hasattr(old_value, "aadl2_ContainmentPathElement79"):
                opp_val = getattr(old_value, "aadl2_ContainmentPathElement79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ContainmentPathElement79"):
                opp_val = getattr(value, "aadl2_ContainmentPathElement79", None)
                if opp_val is None:
                    setattr(value, "aadl2_ContainmentPathElement79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aadl2_ModeBinding(Element):

    pass
class aadl2_PropertyExpression(Element):

    pass
class aadl2_EndToEndFlowSegment(Element):

    pass
class aadl2_NamedElement(Element):

    def __init__(self, name: str, qualifiedName: str, aadl2_NamedElement: set["aadl2_PropertyAssociation"] = None, aadl2_NamedElement33: "aadl2_Classifier" = None, aadl2_NamedElement45: "aadl2_Namespace" = None, aadl2_NamedElement48: "aadl2_Namespace" = None, aadl2_NamedElement82: "aadl2_ContainmentPathElement" = None):
        self.name = name
        self.qualifiedName = qualifiedName
        self.aadl2_NamedElement = aadl2_NamedElement if aadl2_NamedElement is not None else set()
        self.aadl2_NamedElement33 = aadl2_NamedElement33
        self.aadl2_NamedElement45 = aadl2_NamedElement45
        self.aadl2_NamedElement48 = aadl2_NamedElement48
        self.aadl2_NamedElement82 = aadl2_NamedElement82
        
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
    def aadl2_NamedElement82(self):
        return self.__aadl2_NamedElement82

    @aadl2_NamedElement82.setter
    def aadl2_NamedElement82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_NamedElement__aadl2_NamedElement82", None)
        self.__aadl2_NamedElement82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ContainmentPathElement81"):
                opp_val = getattr(old_value, "aadl2_ContainmentPathElement81", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ContainmentPathElement81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ContainmentPathElement81"):
                opp_val = getattr(value, "aadl2_ContainmentPathElement81", None)
                setattr(value, "aadl2_ContainmentPathElement81", self)

    @property
    def aadl2_NamedElement33(self):
        return self.__aadl2_NamedElement33

    @aadl2_NamedElement33.setter
    def aadl2_NamedElement33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_NamedElement__aadl2_NamedElement33", None)
        self.__aadl2_NamedElement33 = value
        
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
    def aadl2_NamedElement45(self):
        return self.__aadl2_NamedElement45

    @aadl2_NamedElement45.setter
    def aadl2_NamedElement45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_NamedElement__aadl2_NamedElement45", None)
        self.__aadl2_NamedElement45 = value
        
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
    def aadl2_NamedElement48(self):
        return self.__aadl2_NamedElement48

    @aadl2_NamedElement48.setter
    def aadl2_NamedElement48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_NamedElement__aadl2_NamedElement48", None)
        self.__aadl2_NamedElement48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Namespace47"):
                opp_val = getattr(old_value, "aadl2_Namespace47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Namespace47"):
                opp_val = getattr(value, "aadl2_Namespace47", None)
                if opp_val is None:
                    setattr(value, "aadl2_Namespace47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def qualifiedName(self) -> str:
        # TODO: Implement qualifiedName method
        pass

    def getNamespace(self) -> str:
        # TODO: Implement getNamespace method
        pass

    def getPropertyValues(self, propertySetName: str, propertyName: str) -> str:
        # TODO: Implement getPropertyValues method
        pass

class aadl2_FlowEnd(Element):

    pass
class aadl2_ComponentImplementationReference(Element):

    pass
class aadl2_ArraySize(Element):

    def __init__(self, size: str, aadl2_ArraySize: "aadl2_ArrayDimension" = None, aadl2_ArraySize91: "aadl2_ArraySizeProperty" = None):
        self.size = size
        self.aadl2_ArraySize = aadl2_ArraySize
        self.aadl2_ArraySize91 = aadl2_ArraySize91
        
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
    def aadl2_ArraySize91(self):
        return self.__aadl2_ArraySize91

    @aadl2_ArraySize91.setter
    def aadl2_ArraySize91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ArraySize__aadl2_ArraySize91", None)
        self.__aadl2_ArraySize91 = value
        
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

class aadl2_NumericRange(Element):

    pass
class aadl2_ArrayDimension(Element):

    pass
class aadl2_ArrayableElement(Element):

    pass
class aadl2_Element(ABC):

    def __init__(self, aadl2_Element: "aadl2_Element" = None, aadl2_Element0: set["aadl2_Element"] = None, aadl2_Element3: set["aadl2_Comment"] = None, aadl2_Element60: "aadl2_Relationship" = None, aadl2_Element55: "aadl2_DirectedRelationship" = None, aadl2_Element58: "aadl2_DirectedRelationship" = None):
        self.aadl2_Element = aadl2_Element
        self.aadl2_Element0 = aadl2_Element0 if aadl2_Element0 is not None else set()
        self.aadl2_Element3 = aadl2_Element3 if aadl2_Element3 is not None else set()
        self.aadl2_Element60 = aadl2_Element60
        self.aadl2_Element55 = aadl2_Element55
        self.aadl2_Element58 = aadl2_Element58
        
    @property
    def aadl2_Element60(self):
        return self.__aadl2_Element60

    @aadl2_Element60.setter
    def aadl2_Element60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Element__aadl2_Element60", None)
        self.__aadl2_Element60 = value
        
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
    def aadl2_Element55(self):
        return self.__aadl2_Element55

    @aadl2_Element55.setter
    def aadl2_Element55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Element__aadl2_Element55", None)
        self.__aadl2_Element55 = value
        
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
    def aadl2_Element58(self):
        return self.__aadl2_Element58

    @aadl2_Element58.setter
    def aadl2_Element58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Element__aadl2_Element58", None)
        self.__aadl2_Element58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_DirectedRelationship57"):
                opp_val = getattr(old_value, "aadl2_DirectedRelationship57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_DirectedRelationship57"):
                opp_val = getattr(value, "aadl2_DirectedRelationship57", None)
                if opp_val is None:
                    setattr(value, "aadl2_DirectedRelationship57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getOwner(self) -> str:
        # TODO: Implement getOwner method
        pass
