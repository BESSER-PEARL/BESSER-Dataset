from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AccessType(Enum):
    provided = "provided"
    required = "required"
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
class ConnectionKind(Enum):
    Access = "Access"
    Feature = "Feature"
    FeatureGroup = "FeatureGroup"
    Parameter = "Parameter"
    Port = "Port"
class AccessCategory(Enum):
    bus = "bus"
    data = "data"
    subprogram = "subprogram"
    subprogramGroup = "subprogramGroup"
class OperationKind(Enum):
    and = "and"
    or = "or"
    not = "not"
    plus = "plus"
    minus = "minus"
class FlowKind(Enum):
    source = "source"
    path = "path"
    sink = "sink"
class PortCategory(Enum):
    data = "data"
    event = "event"
    eventData = "eventData"
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
class PropertyType:

    pass
class aadl2_ClassifierType(PropertyType):

    pass
class aadl2_NumberType(PropertyType):

    pass
class aadl2_ReferenceType(PropertyType):

    pass
class aadl2_AadlString(PropertyType):

    pass
class aadl2_RangeType(PropertyType):

    pass
class aadl2_AadlBoolean(PropertyType):

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
    def base(self) -> str:
        return self.__base

    @base.setter
    def base(self, base: str):
        self.__base = base

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ContainedNamedElement:

    pass
class EnumerationLiteral:

    pass
class aadl2_UnitLiteral(EnumerationLiteral):

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
                if hasattr(item, "aadl2_PropertyExpression854"):
                    opp_val = getattr(item, "aadl2_PropertyExpression854", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_PropertyExpression854", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_PropertyExpression854"):
                    opp_val = getattr(item, "aadl2_PropertyExpression854", None)
                    
                    setattr(item, "aadl2_PropertyExpression854", self)
                    

class aadl2_PropertyValue(PropertyExpression):

    pass
class PropertyValue:

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

class aadl2_NumberValue(PropertyValue):

    def __init__(self, valueString: str, aadl2_NumberValue: "aadl2_UnitLiteral" = None, aadl2_NumberValue837: "aadl2_UnitLiteral" = None):
        self.valueString = valueString
        self.aadl2_NumberValue = aadl2_NumberValue
        self.aadl2_NumberValue837 = aadl2_NumberValue837
        
    @property
    def valueString(self) -> str:
        return self.__valueString

    @valueString.setter
    def valueString(self, valueString: str):
        self.__valueString = valueString

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
            if hasattr(old_value, "aadl2_UnitLiteral835"):
                opp_val = getattr(old_value, "aadl2_UnitLiteral835", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_UnitLiteral835", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_UnitLiteral835"):
                opp_val = getattr(value, "aadl2_UnitLiteral835", None)
                setattr(value, "aadl2_UnitLiteral835", self)

    @property
    def aadl2_NumberValue837(self):
        return self.__aadl2_NumberValue837

    @aadl2_NumberValue837.setter
    def aadl2_NumberValue837(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_NumberValue__aadl2_NumberValue837", None)
        self.__aadl2_NumberValue837 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_UnitLiteral838"):
                opp_val = getattr(old_value, "aadl2_UnitLiteral838", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_UnitLiteral838", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_UnitLiteral838"):
                opp_val = getattr(value, "aadl2_UnitLiteral838", None)
                setattr(value, "aadl2_UnitLiteral838", self)

class aadl2_BooleanLiteral(PropertyValue):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class aadl2_UnitValue(PropertyValue):

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

class aadl2_RangeValue(PropertyValue):

    pass
class aadl2_ReferenceValue(PropertyValue, ContainedNamedElement):

    pass
class aadl2_RecordValue(PropertyValue):

    pass
class aadl2_EnumerationValue(PropertyValue):

    pass
class CallSpecification:

    pass
class aadl2_ProcessorCall(CallSpecification):

    def __init__(self, subprogramAccessName: str):
        self.subprogramAccessName = subprogramAccessName
        
    @property
    def subprogramAccessName(self) -> str:
        return self.__subprogramAccessName

    @subprogramAccessName.setter
    def subprogramAccessName(self, subprogramAccessName: str):
        self.__subprogramAccessName = subprogramAccessName

class FeatureGroupPrototypeActual:

    pass
class aadl2_FeatureGroupReference(FeatureGroupPrototypeActual):

    pass
class aadl2_FeatureGroupPrototypeReference(FeatureGroupPrototypeActual):

    pass
class ComponentPrototypeActual:

    pass
class aadl2_ComponentReference(ComponentPrototypeActual):

    pass
class aadl2_ComponentPrototypeReference(ComponentPrototypeActual):

    pass
class FeaturePrototypeActual:

    pass
class aadl2_PortSpecification(FeaturePrototypeActual):

    def __init__(self, direction: str, category: str, aadl2_PortSpecification: "aadl2_ComponentClassifier" = None):
        self.direction = direction
        self.category = category
        self.aadl2_PortSpecification = aadl2_PortSpecification
        
    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

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
            if hasattr(old_value, "aadl2_ComponentClassifier801"):
                opp_val = getattr(old_value, "aadl2_ComponentClassifier801", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentClassifier801", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentClassifier801"):
                opp_val = getattr(value, "aadl2_ComponentClassifier801", None)
                setattr(value, "aadl2_ComponentClassifier801", self)

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
            if hasattr(old_value, "aadl2_FeaturePrototype803"):
                opp_val = getattr(old_value, "aadl2_FeaturePrototype803", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FeaturePrototype803", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FeaturePrototype803"):
                opp_val = getattr(value, "aadl2_FeaturePrototype803", None)
                setattr(value, "aadl2_FeaturePrototype803", self)

class aadl2_AccessSpecification(FeaturePrototypeActual):

    def __init__(self, kind: str, category: str, aadl2_AccessSpecification: "aadl2_ComponentClassifier" = None):
        self.kind = kind
        self.category = category
        self.aadl2_AccessSpecification = aadl2_AccessSpecification
        
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
            if hasattr(old_value, "aadl2_ComponentClassifier799"):
                opp_val = getattr(old_value, "aadl2_ComponentClassifier799", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentClassifier799", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentClassifier799"):
                opp_val = getattr(value, "aadl2_ComponentClassifier799", None)
                setattr(value, "aadl2_ComponentClassifier799", self)

class PrototypeBinding:

    pass
class aadl2_FeatureGroupPrototypeBinding(PrototypeBinding):

    pass
class aadl2_FeaturePrototypeBinding(PrototypeBinding):

    pass
class aadl2_ComponentPrototypeBinding(PrototypeBinding):

    pass
class VirtualProcessorClassifier:

    pass
class VirtualBusClassifier:

    pass
class ThreadGroupClassifier:

    pass
class ThreadClassifier:

    pass
class SystemClassifier:

    pass
class SubprogramGroupClassifier:

    pass
class SubprogramClassifier:

    pass
class ProcessorClassifier:

    pass
class ProcessClassifier:

    pass
class MemoryClassifier:

    pass
class DeviceClassifier:

    pass
class DataClassifier:

    pass
class BusClassifier:

    pass
class VirtualProcessor:

    pass
class VirtualBus:

    pass
class ThreadGroup:

    pass
class Thread:

    pass
class System:

    pass
class Processor:

    pass
class Process:

    pass
class Memory:

    pass
class BehavioralFeature:

    pass
class aadl2_CallSpecification(BehavioralFeature):

    pass
class ComponentImplementation:

    pass
class aadl2_BehavioredImplementation(ComponentImplementation):

    def __init__(self, aadl2_BehavioredImplementation: set["aadl2_CallSpecification"] = None, aadl2_BehavioredImplementation452: set["aadl2_SubprogramCallSequence"] = None):
        self.aadl2_BehavioredImplementation = aadl2_BehavioredImplementation if aadl2_BehavioredImplementation is not None else set()
        self.aadl2_BehavioredImplementation452 = aadl2_BehavioredImplementation452 if aadl2_BehavioredImplementation452 is not None else set()
        
    @property
    def aadl2_BehavioredImplementation452(self):
        return self.__aadl2_BehavioredImplementation452

    @aadl2_BehavioredImplementation452.setter
    def aadl2_BehavioredImplementation452(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_BehavioredImplementation__aadl2_BehavioredImplementation452", None)
        self.__aadl2_BehavioredImplementation452 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_SubprogramCallSequence"):
                    opp_val = getattr(item, "aadl2_SubprogramCallSequence", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_SubprogramCallSequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_SubprogramCallSequence"):
                    opp_val = getattr(item, "aadl2_SubprogramCallSequence", None)
                    
                    setattr(item, "aadl2_SubprogramCallSequence", self)
                    

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
                if hasattr(item, "aadl2_CallSpecification"):
                    opp_val = getattr(item, "aadl2_CallSpecification", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_CallSpecification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_CallSpecification"):
                    opp_val = getattr(item, "aadl2_CallSpecification", None)
                    
                    setattr(item, "aadl2_CallSpecification", self)
                    

    def callSpecifications(self) -> str:
        # TODO: Implement callSpecifications method
        pass

class Device:

    pass
class BehavioredImplementation:

    pass
class AbstractClassifier:

    pass
class ComponentType:

    pass
class aadl2_VirtualProcessorImplementation(ComponentImplementation, VirtualProcessorClassifier):

    pass
class aadl2_VirtualProcessorType(VirtualProcessorClassifier, ComponentType):

    pass
class aadl2_VirtualBusImplementation(ComponentImplementation, VirtualBusClassifier):

    pass
class aadl2_VirtualBusType(VirtualBusClassifier, ComponentType):

    pass
class aadl2_ThreadGroupImplementation(ComponentImplementation, ThreadGroupClassifier):

    pass
class aadl2_ThreadGroupType(ThreadGroupClassifier, ComponentType):

    pass
class aadl2_ThreadImplementation(ThreadClassifier, BehavioredImplementation):

    pass
class aadl2_ThreadType(ThreadClassifier, ComponentType):

    pass
class aadl2_SystemImplementation(ComponentImplementation, SystemClassifier):

    pass
class aadl2_SystemType(SystemClassifier, ComponentType):

    pass
class aadl2_SubprogramGroupImplementation(ComponentImplementation, SubprogramGroupClassifier):

    pass
class aadl2_SubprogramImplementation(SubprogramClassifier, BehavioredImplementation):

    pass
class aadl2_SubprogramType(SubprogramClassifier, ComponentType):

    pass
class aadl2_ProcessorImplementation(ComponentImplementation, ProcessorClassifier):

    pass
class aadl2_ProcessImplementation(ComponentImplementation, ProcessClassifier):

    pass
class aadl2_ProcessorType(ProcessorClassifier, ComponentType):

    pass
class aadl2_ProcessType(ProcessClassifier, ComponentType):

    pass
class aadl2_MemoryImplementation(ComponentImplementation, MemoryClassifier):

    pass
class aadl2_MemoryType(MemoryClassifier, ComponentType):

    pass
class aadl2_DeviceImplementation(ComponentImplementation, DeviceClassifier):

    pass
class aadl2_DeviceType(DeviceClassifier, ComponentType):

    pass
class aadl2_DataImplementation(ComponentImplementation, DataClassifier):

    pass
class aadl2_BusImplementation(ComponentImplementation, BusClassifier):

    pass
class aadl2_BusType(BusClassifier, ComponentType):

    pass
class aadl2_AbstractImplementation(AbstractClassifier, BehavioredImplementation):

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

    def __init__(self, sourceText: str):
        self.sourceText = sourceText
        
    @property
    def sourceText(self) -> str:
        return self.__sourceText

    @sourceText.setter
    def sourceText(self, sourceText: str):
        self.__sourceText = sourceText

class AnnexLibrary:

    pass
class aadl2_DefaultAnnexLibrary(AnnexLibrary):

    def __init__(self, sourceText: str):
        self.sourceText = sourceText
        
    @property
    def sourceText(self) -> str:
        return self.__sourceText

    @sourceText.setter
    def sourceText(self, sourceText: str):
        self.__sourceText = sourceText

class Connection:

    pass
class Subcomponent:

    pass
class aadl2_MemorySubcomponent(Subcomponent, Memory):

    pass
class aadl2_SystemSubcomponent(Subcomponent, System):

    pass
class aadl2_DeviceSubcomponent(Subcomponent, Device):

    pass
class aadl2_ProcessorSubcomponent(Subcomponent, Processor):

    pass
class aadl2_ThreadGroupSubcomponent(Subcomponent, ThreadGroup):

    pass
class aadl2_VirtualBusSubcomponent(Subcomponent, VirtualBus):

    pass
class aadl2_ThreadSubcomponent(Subcomponent, Thread):

    pass
class aadl2_ProcessSubcomponent(Subcomponent, Process):

    pass
class aadl2_VirtualProcessorSubcomponent(Subcomponent, VirtualProcessor):

    pass
class Prototype:

    pass
class aadl2_FeatureGroupPrototype(Prototype):

    pass
class aadl2_FeaturePrototype(Prototype):

    def __init__(self, direction: str, aadl2_FeaturePrototype: "aadl2_ComponentClassifier" = None, aadl2_FeaturePrototype803: "aadl2_FeaturePrototypeReference" = None):
        self.direction = direction
        self.aadl2_FeaturePrototype = aadl2_FeaturePrototype
        self.aadl2_FeaturePrototype803 = aadl2_FeaturePrototype803
        
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
            if hasattr(old_value, "aadl2_ComponentClassifier796"):
                opp_val = getattr(old_value, "aadl2_ComponentClassifier796", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentClassifier796", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentClassifier796"):
                opp_val = getattr(value, "aadl2_ComponentClassifier796", None)
                setattr(value, "aadl2_ComponentClassifier796", self)

    @property
    def aadl2_FeaturePrototype803(self):
        return self.__aadl2_FeaturePrototype803

    @aadl2_FeaturePrototype803.setter
    def aadl2_FeaturePrototype803(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeaturePrototype__aadl2_FeaturePrototype803", None)
        self.__aadl2_FeaturePrototype803 = value
        
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

class ModalPath:

    pass
class Abstract:

    pass
class CalledSubprogram:

    pass
class aadl2_ComponentPrototype(Prototype):

    def __init__(self, category: str, array: str, aadl2_ComponentPrototype: "aadl2_Subcomponent" = None, aadl2_ComponentPrototype255: "aadl2_ComponentClassifier" = None, aadl2_ComponentPrototype805: "aadl2_ComponentPrototypeReference" = None):
        self.category = category
        self.array = array
        self.aadl2_ComponentPrototype = aadl2_ComponentPrototype
        self.aadl2_ComponentPrototype255 = aadl2_ComponentPrototype255
        self.aadl2_ComponentPrototype805 = aadl2_ComponentPrototype805
        
    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def array(self) -> str:
        return self.__array

    @array.setter
    def array(self, array: str):
        self.__array = array

    @property
    def aadl2_ComponentPrototype805(self):
        return self.__aadl2_ComponentPrototype805

    @aadl2_ComponentPrototype805.setter
    def aadl2_ComponentPrototype805(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentPrototype__aadl2_ComponentPrototype805", None)
        self.__aadl2_ComponentPrototype805 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentPrototypeReference"):
                opp_val = getattr(old_value, "aadl2_ComponentPrototypeReference", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentPrototypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentPrototypeReference"):
                opp_val = getattr(value, "aadl2_ComponentPrototypeReference", None)
                setattr(value, "aadl2_ComponentPrototypeReference", self)

    @property
    def aadl2_ComponentPrototype255(self):
        return self.__aadl2_ComponentPrototype255

    @aadl2_ComponentPrototype255.setter
    def aadl2_ComponentPrototype255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentPrototype__aadl2_ComponentPrototype255", None)
        self.__aadl2_ComponentPrototype255 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentClassifier256"):
                opp_val = getattr(old_value, "aadl2_ComponentClassifier256", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentClassifier256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentClassifier256"):
                opp_val = getattr(value, "aadl2_ComponentClassifier256", None)
                setattr(value, "aadl2_ComponentClassifier256", self)

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
            if hasattr(old_value, "aadl2_Subcomponent243"):
                opp_val = getattr(old_value, "aadl2_Subcomponent243", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Subcomponent243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Subcomponent243"):
                opp_val = getattr(value, "aadl2_Subcomponent243", None)
                setattr(value, "aadl2_Subcomponent243", self)

class SubprogramGroup:

    pass
class Subprogram:

    pass
class AccessConnectionEnd:

    pass
class aadl2_SubprogramSubcomponent(Subcomponent, Subprogram, AccessConnectionEnd):

    pass
class Port:

    pass
class Data:

    pass
class EndToEndFlowElement:

    pass
class aadl2_FlowElement(EndToEndFlowElement):

    pass
class ParameterConnectionEnd:

    pass
class FlowElement:

    pass
class aadl2_SubcomponentFlow(FlowElement):

    pass
class Bus:

    pass
class aadl2_BusSubcomponent(AccessConnectionEnd, Bus, Subcomponent):

    pass
class Access:

    pass
class aadl2_SubprogramAccess(CalledSubprogram, Access):

    pass
class aadl2_EventPort(Port):

    pass
class aadl2_BusAccess(Access):

    pass
class CallContext:

    pass
class aadl2_SubprogramGroupSubcomponent(AccessConnectionEnd, CallContext, SubprogramGroup, Subcomponent):

    pass
class aadl2_SubprogramGroupAccess(CallContext, Access):

    pass
class aadl2_DataType(CallContext, DataClassifier, ComponentType):

    pass
class aadl2_SubprogramGroupType(SubprogramGroupClassifier, CallContext, ComponentType):

    pass
class aadl2_AbstractType(CallContext, AbstractClassifier, ComponentType):

    pass
class FeatureGroupConnectionEnd:

    pass
class Context:

    pass
class aadl2_SubprogramCall(CallSpecification, Context):

    pass
class aadl2_DataPort(ParameterConnectionEnd, Port, Context):

    pass
class aadl2_EventDataPort(ParameterConnectionEnd, Port, Context):

    pass
class Generalization:

    pass
class aadl2_GroupExtension(Generalization):

    pass
class Flow:

    pass
class aadl2_TypeExtension(Generalization):

    pass
class ConnectionEnd:

    pass
class aadl2_AccessConnectionEnd(ConnectionEnd):

    pass
class aadl2_FeatureGroupConnectionEnd(ConnectionEnd):

    pass
class aadl2_PortConnectionEnd(ConnectionEnd):

    pass
class aadl2_ParameterConnectionEnd(ConnectionEnd):

    pass
class aadl2_FeatureConnectionEnd(ConnectionEnd):

    pass
class ArrayableElement:

    pass
class FeatureConnectionEnd:

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

class PortConnectionEnd:

    pass
class aadl2_DataAccess(ParameterConnectionEnd, Access, FlowElement, PortConnectionEnd):

    pass
class aadl2_DataSubcomponent(ParameterConnectionEnd, AccessConnectionEnd, Data, Subcomponent, PortConnectionEnd):

    pass
class DirectedFeature:

    pass
class aadl2_Parameter(DirectedFeature, ParameterConnectionEnd, Context):

    pass
class aadl2_FeatureGroup(FeatureGroupConnectionEnd, DirectedFeature, CallContext, Context):

    def __init__(self, inverse: str, aadl2_FeatureGroup: "aadl2_ComponentType" = None, aadl2_FeatureGroup179: "aadl2_FeatureGroupType" = None, aadl2_FeatureGroup203: "aadl2_FeatureGroupType" = None):
        self.inverse = inverse
        self.aadl2_FeatureGroup = aadl2_FeatureGroup
        self.aadl2_FeatureGroup179 = aadl2_FeatureGroup179
        self.aadl2_FeatureGroup203 = aadl2_FeatureGroup203
        
    @property
    def inverse(self) -> str:
        return self.__inverse

    @inverse.setter
    def inverse(self, inverse: str):
        self.__inverse = inverse

    @property
    def aadl2_FeatureGroup203(self):
        return self.__aadl2_FeatureGroup203

    @aadl2_FeatureGroup203.setter
    def aadl2_FeatureGroup203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroup__aadl2_FeatureGroup203", None)
        self.__aadl2_FeatureGroup203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FeatureGroupType202"):
                opp_val = getattr(old_value, "aadl2_FeatureGroupType202", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FeatureGroupType202"):
                opp_val = getattr(value, "aadl2_FeatureGroupType202", None)
                if opp_val is None:
                    setattr(value, "aadl2_FeatureGroupType202", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_FeatureGroup179(self):
        return self.__aadl2_FeatureGroup179

    @aadl2_FeatureGroup179.setter
    def aadl2_FeatureGroup179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroup__aadl2_FeatureGroup179", None)
        self.__aadl2_FeatureGroup179 = value
        
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
            if hasattr(old_value, "aadl2_ComponentType157"):
                opp_val = getattr(old_value, "aadl2_ComponentType157", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentType157"):
                opp_val = getattr(value, "aadl2_ComponentType157", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentType157", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aadl2_AbstractFeature(DirectedFeature):

    pass
class aadl2_Port(DirectedFeature, PortConnectionEnd):

    def __init__(self, category: str, aadl2_Port: "aadl2_TriggerPort" = None):
        self.category = category
        self.aadl2_Port = aadl2_Port
        
    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def aadl2_Port(self):
        return self.__aadl2_Port

    @aadl2_Port.setter
    def aadl2_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Port__aadl2_Port", None)
        self.__aadl2_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_TriggerPort137"):
                opp_val = getattr(old_value, "aadl2_TriggerPort137", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_TriggerPort137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_TriggerPort137"):
                opp_val = getattr(value, "aadl2_TriggerPort137", None)
                setattr(value, "aadl2_TriggerPort137", self)

class ModeTransitionTrigger:

    pass
class aadl2_ProcessorPort(ModeTransitionTrigger, PortConnectionEnd):

    pass
class aadl2_InternalEvent(ModeTransitionTrigger, PortConnectionEnd):

    pass
class aadl2_TriggerPort(ModeTransitionTrigger):

    pass
class Classifier:

    pass
class aadl2_FeatureGroupType(Classifier):

    def __init__(self, feature: str, aadl2_FeatureGroupType: "aadl2_FeatureGroup" = None, aadl2_FeatureGroupType181: set["aadl2_Feature"] = None, aadl2_FeatureGroupType185: "aadl2_FeatureGroupType" = None, aadl2_FeatureGroupType183: "aadl2_FeatureGroupType" = None, aadl2_FeatureGroupType188: "aadl2_FeatureGroupType" = None, aadl2_FeatureGroupType186: "aadl2_FeatureGroupType" = None, aadl2_FeatureGroupType190: "aadl2_GroupExtension" = None, aadl2_FeatureGroupType192: set["aadl2_BusAccess"] = None, aadl2_FeatureGroupType194: set["aadl2_DataAccess"] = None, aadl2_FeatureGroupType198: set["aadl2_EventDataPort"] = None, aadl2_FeatureGroupType200: set["aadl2_EventPort"] = None, aadl2_FeatureGroupType202: set["aadl2_FeatureGroup"] = None, aadl2_FeatureGroupType205: set["aadl2_Parameter"] = None, aadl2_FeatureGroupType207: set["aadl2_SubprogramAccess"] = None, aadl2_FeatureGroupType209: set["aadl2_SubprogramGroupAccess"] = None, aadl2_FeatureGroupType211: set["aadl2_AbstractFeature"] = None, aadl2_FeatureGroupType215: "aadl2_GroupExtension" = None, aadl2_FeatureGroupType196: set["aadl2_DataPort"] = None, aadl2_FeatureGroupType380: "aadl2_PackageSection" = None, aadl2_FeatureGroupType402: "aadl2_FeatureGroupTypeRename" = None, aadl2_FeatureGroupType793: "aadl2_FeatureGroupPrototype" = None, aadl2_FeatureGroupType817: "aadl2_FeatureGroupReference" = None):
        self.feature = feature
        self.aadl2_FeatureGroupType = aadl2_FeatureGroupType
        self.aadl2_FeatureGroupType181 = aadl2_FeatureGroupType181 if aadl2_FeatureGroupType181 is not None else set()
        self.aadl2_FeatureGroupType185 = aadl2_FeatureGroupType185
        self.aadl2_FeatureGroupType183 = aadl2_FeatureGroupType183
        self.aadl2_FeatureGroupType188 = aadl2_FeatureGroupType188
        self.aadl2_FeatureGroupType186 = aadl2_FeatureGroupType186
        self.aadl2_FeatureGroupType190 = aadl2_FeatureGroupType190
        self.aadl2_FeatureGroupType192 = aadl2_FeatureGroupType192 if aadl2_FeatureGroupType192 is not None else set()
        self.aadl2_FeatureGroupType194 = aadl2_FeatureGroupType194 if aadl2_FeatureGroupType194 is not None else set()
        self.aadl2_FeatureGroupType198 = aadl2_FeatureGroupType198 if aadl2_FeatureGroupType198 is not None else set()
        self.aadl2_FeatureGroupType200 = aadl2_FeatureGroupType200 if aadl2_FeatureGroupType200 is not None else set()
        self.aadl2_FeatureGroupType202 = aadl2_FeatureGroupType202 if aadl2_FeatureGroupType202 is not None else set()
        self.aadl2_FeatureGroupType205 = aadl2_FeatureGroupType205 if aadl2_FeatureGroupType205 is not None else set()
        self.aadl2_FeatureGroupType207 = aadl2_FeatureGroupType207 if aadl2_FeatureGroupType207 is not None else set()
        self.aadl2_FeatureGroupType209 = aadl2_FeatureGroupType209 if aadl2_FeatureGroupType209 is not None else set()
        self.aadl2_FeatureGroupType211 = aadl2_FeatureGroupType211 if aadl2_FeatureGroupType211 is not None else set()
        self.aadl2_FeatureGroupType215 = aadl2_FeatureGroupType215
        self.aadl2_FeatureGroupType196 = aadl2_FeatureGroupType196 if aadl2_FeatureGroupType196 is not None else set()
        self.aadl2_FeatureGroupType380 = aadl2_FeatureGroupType380
        self.aadl2_FeatureGroupType402 = aadl2_FeatureGroupType402
        self.aadl2_FeatureGroupType793 = aadl2_FeatureGroupType793
        self.aadl2_FeatureGroupType817 = aadl2_FeatureGroupType817
        
    @property
    def feature(self) -> str:
        return self.__feature

    @feature.setter
    def feature(self, feature: str):
        self.__feature = feature

    @property
    def aadl2_FeatureGroupType215(self):
        return self.__aadl2_FeatureGroupType215

    @aadl2_FeatureGroupType215.setter
    def aadl2_FeatureGroupType215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType215", None)
        self.__aadl2_FeatureGroupType215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_GroupExtension214"):
                opp_val = getattr(old_value, "aadl2_GroupExtension214", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_GroupExtension214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_GroupExtension214"):
                opp_val = getattr(value, "aadl2_GroupExtension214", None)
                setattr(value, "aadl2_GroupExtension214", self)

    @property
    def aadl2_FeatureGroupType194(self):
        return self.__aadl2_FeatureGroupType194

    @aadl2_FeatureGroupType194.setter
    def aadl2_FeatureGroupType194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType194", None)
        self.__aadl2_FeatureGroupType194 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_DataAccess"):
                    opp_val = getattr(item, "aadl2_DataAccess", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_DataAccess", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_DataAccess"):
                    opp_val = getattr(item, "aadl2_DataAccess", None)
                    
                    setattr(item, "aadl2_DataAccess", self)
                    

    @property
    def aadl2_FeatureGroupType185(self):
        return self.__aadl2_FeatureGroupType185

    @aadl2_FeatureGroupType185.setter
    def aadl2_FeatureGroupType185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType185", None)
        self.__aadl2_FeatureGroupType185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FeatureGroupType183"):
                opp_val = getattr(old_value, "aadl2_FeatureGroupType183", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FeatureGroupType183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FeatureGroupType183"):
                opp_val = getattr(value, "aadl2_FeatureGroupType183", None)
                setattr(value, "aadl2_FeatureGroupType183", self)

    @property
    def aadl2_FeatureGroupType205(self):
        return self.__aadl2_FeatureGroupType205

    @aadl2_FeatureGroupType205.setter
    def aadl2_FeatureGroupType205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType205", None)
        self.__aadl2_FeatureGroupType205 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_Parameter"):
                    opp_val = getattr(item, "aadl2_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Parameter"):
                    opp_val = getattr(item, "aadl2_Parameter", None)
                    
                    setattr(item, "aadl2_Parameter", self)
                    

    @property
    def aadl2_FeatureGroupType192(self):
        return self.__aadl2_FeatureGroupType192

    @aadl2_FeatureGroupType192.setter
    def aadl2_FeatureGroupType192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType192", None)
        self.__aadl2_FeatureGroupType192 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_BusAccess"):
                    opp_val = getattr(item, "aadl2_BusAccess", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_BusAccess", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_BusAccess"):
                    opp_val = getattr(item, "aadl2_BusAccess", None)
                    
                    setattr(item, "aadl2_BusAccess", self)
                    

    @property
    def aadl2_FeatureGroupType198(self):
        return self.__aadl2_FeatureGroupType198

    @aadl2_FeatureGroupType198.setter
    def aadl2_FeatureGroupType198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType198", None)
        self.__aadl2_FeatureGroupType198 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_EventDataPort"):
                    opp_val = getattr(item, "aadl2_EventDataPort", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_EventDataPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_EventDataPort"):
                    opp_val = getattr(item, "aadl2_EventDataPort", None)
                    
                    setattr(item, "aadl2_EventDataPort", self)
                    

    @property
    def aadl2_FeatureGroupType196(self):
        return self.__aadl2_FeatureGroupType196

    @aadl2_FeatureGroupType196.setter
    def aadl2_FeatureGroupType196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType196", None)
        self.__aadl2_FeatureGroupType196 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_DataPort"):
                    opp_val = getattr(item, "aadl2_DataPort", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_DataPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_DataPort"):
                    opp_val = getattr(item, "aadl2_DataPort", None)
                    
                    setattr(item, "aadl2_DataPort", self)
                    

    @property
    def aadl2_FeatureGroupType181(self):
        return self.__aadl2_FeatureGroupType181

    @aadl2_FeatureGroupType181.setter
    def aadl2_FeatureGroupType181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType181", None)
        self.__aadl2_FeatureGroupType181 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_Feature182"):
                    opp_val = getattr(item, "aadl2_Feature182", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Feature182", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Feature182"):
                    opp_val = getattr(item, "aadl2_Feature182", None)
                    
                    setattr(item, "aadl2_Feature182", self)
                    

    @property
    def aadl2_FeatureGroupType202(self):
        return self.__aadl2_FeatureGroupType202

    @aadl2_FeatureGroupType202.setter
    def aadl2_FeatureGroupType202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType202", None)
        self.__aadl2_FeatureGroupType202 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_FeatureGroup203"):
                    opp_val = getattr(item, "aadl2_FeatureGroup203", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_FeatureGroup203", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_FeatureGroup203"):
                    opp_val = getattr(item, "aadl2_FeatureGroup203", None)
                    
                    setattr(item, "aadl2_FeatureGroup203", self)
                    

    @property
    def aadl2_FeatureGroupType186(self):
        return self.__aadl2_FeatureGroupType186

    @aadl2_FeatureGroupType186.setter
    def aadl2_FeatureGroupType186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType186", None)
        self.__aadl2_FeatureGroupType186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FeatureGroupType188"):
                opp_val = getattr(old_value, "aadl2_FeatureGroupType188", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FeatureGroupType188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FeatureGroupType188"):
                opp_val = getattr(value, "aadl2_FeatureGroupType188", None)
                setattr(value, "aadl2_FeatureGroupType188", self)

    @property
    def aadl2_FeatureGroupType793(self):
        return self.__aadl2_FeatureGroupType793

    @aadl2_FeatureGroupType793.setter
    def aadl2_FeatureGroupType793(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType793", None)
        self.__aadl2_FeatureGroupType793 = value
        
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
    def aadl2_FeatureGroupType188(self):
        return self.__aadl2_FeatureGroupType188

    @aadl2_FeatureGroupType188.setter
    def aadl2_FeatureGroupType188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType188", None)
        self.__aadl2_FeatureGroupType188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FeatureGroupType186"):
                opp_val = getattr(old_value, "aadl2_FeatureGroupType186", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FeatureGroupType186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FeatureGroupType186"):
                opp_val = getattr(value, "aadl2_FeatureGroupType186", None)
                setattr(value, "aadl2_FeatureGroupType186", self)

    @property
    def aadl2_FeatureGroupType380(self):
        return self.__aadl2_FeatureGroupType380

    @aadl2_FeatureGroupType380.setter
    def aadl2_FeatureGroupType380(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType380", None)
        self.__aadl2_FeatureGroupType380 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PackageSection379"):
                opp_val = getattr(old_value, "aadl2_PackageSection379", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PackageSection379"):
                opp_val = getattr(value, "aadl2_PackageSection379", None)
                if opp_val is None:
                    setattr(value, "aadl2_PackageSection379", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_FeatureGroupType(self):
        return self.__aadl2_FeatureGroupType

    @aadl2_FeatureGroupType.setter
    def aadl2_FeatureGroupType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType", None)
        self.__aadl2_FeatureGroupType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FeatureGroup179"):
                opp_val = getattr(old_value, "aadl2_FeatureGroup179", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FeatureGroup179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FeatureGroup179"):
                opp_val = getattr(value, "aadl2_FeatureGroup179", None)
                setattr(value, "aadl2_FeatureGroup179", self)

    @property
    def aadl2_FeatureGroupType200(self):
        return self.__aadl2_FeatureGroupType200

    @aadl2_FeatureGroupType200.setter
    def aadl2_FeatureGroupType200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType200", None)
        self.__aadl2_FeatureGroupType200 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_EventPort"):
                    opp_val = getattr(item, "aadl2_EventPort", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_EventPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_EventPort"):
                    opp_val = getattr(item, "aadl2_EventPort", None)
                    
                    setattr(item, "aadl2_EventPort", self)
                    

    @property
    def aadl2_FeatureGroupType190(self):
        return self.__aadl2_FeatureGroupType190

    @aadl2_FeatureGroupType190.setter
    def aadl2_FeatureGroupType190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType190", None)
        self.__aadl2_FeatureGroupType190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_GroupExtension"):
                opp_val = getattr(old_value, "aadl2_GroupExtension", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_GroupExtension", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_GroupExtension"):
                opp_val = getattr(value, "aadl2_GroupExtension", None)
                setattr(value, "aadl2_GroupExtension", self)

    @property
    def aadl2_FeatureGroupType207(self):
        return self.__aadl2_FeatureGroupType207

    @aadl2_FeatureGroupType207.setter
    def aadl2_FeatureGroupType207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType207", None)
        self.__aadl2_FeatureGroupType207 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_SubprogramAccess"):
                    opp_val = getattr(item, "aadl2_SubprogramAccess", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_SubprogramAccess", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_SubprogramAccess"):
                    opp_val = getattr(item, "aadl2_SubprogramAccess", None)
                    
                    setattr(item, "aadl2_SubprogramAccess", self)
                    

    @property
    def aadl2_FeatureGroupType817(self):
        return self.__aadl2_FeatureGroupType817

    @aadl2_FeatureGroupType817.setter
    def aadl2_FeatureGroupType817(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType817", None)
        self.__aadl2_FeatureGroupType817 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FeatureGroupReference816"):
                opp_val = getattr(old_value, "aadl2_FeatureGroupReference816", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FeatureGroupReference816", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FeatureGroupReference816"):
                opp_val = getattr(value, "aadl2_FeatureGroupReference816", None)
                setattr(value, "aadl2_FeatureGroupReference816", self)

    @property
    def aadl2_FeatureGroupType209(self):
        return self.__aadl2_FeatureGroupType209

    @aadl2_FeatureGroupType209.setter
    def aadl2_FeatureGroupType209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType209", None)
        self.__aadl2_FeatureGroupType209 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_SubprogramGroupAccess"):
                    opp_val = getattr(item, "aadl2_SubprogramGroupAccess", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_SubprogramGroupAccess", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_SubprogramGroupAccess"):
                    opp_val = getattr(item, "aadl2_SubprogramGroupAccess", None)
                    
                    setattr(item, "aadl2_SubprogramGroupAccess", self)
                    

    @property
    def aadl2_FeatureGroupType402(self):
        return self.__aadl2_FeatureGroupType402

    @aadl2_FeatureGroupType402.setter
    def aadl2_FeatureGroupType402(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType402", None)
        self.__aadl2_FeatureGroupType402 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FeatureGroupTypeRename401"):
                opp_val = getattr(old_value, "aadl2_FeatureGroupTypeRename401", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FeatureGroupTypeRename401", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FeatureGroupTypeRename401"):
                opp_val = getattr(value, "aadl2_FeatureGroupTypeRename401", None)
                setattr(value, "aadl2_FeatureGroupTypeRename401", self)

    @property
    def aadl2_FeatureGroupType211(self):
        return self.__aadl2_FeatureGroupType211

    @aadl2_FeatureGroupType211.setter
    def aadl2_FeatureGroupType211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType211", None)
        self.__aadl2_FeatureGroupType211 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_AbstractFeature212"):
                    opp_val = getattr(item, "aadl2_AbstractFeature212", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_AbstractFeature212", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_AbstractFeature212"):
                    opp_val = getattr(item, "aadl2_AbstractFeature212", None)
                    
                    setattr(item, "aadl2_AbstractFeature212", self)
                    

    @property
    def aadl2_FeatureGroupType183(self):
        return self.__aadl2_FeatureGroupType183

    @aadl2_FeatureGroupType183.setter
    def aadl2_FeatureGroupType183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FeatureGroupType__aadl2_FeatureGroupType183", None)
        self.__aadl2_FeatureGroupType183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FeatureGroupType185"):
                opp_val = getattr(old_value, "aadl2_FeatureGroupType185", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FeatureGroupType185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FeatureGroupType185"):
                opp_val = getattr(value, "aadl2_FeatureGroupType185", None)
                setattr(value, "aadl2_FeatureGroupType185", self)

class aadl2_ComponentClassifier(Classifier):

    def __init__(self, noFlows: str, noModes: str, aadl2_ComponentClassifier: set["aadl2_Mode"] = None, aadl2_ComponentClassifier119: set["aadl2_ModeTransition"] = None, aadl2_ComponentClassifier123: set["aadl2_InternalEvent"] = None, aadl2_ComponentClassifier142: "aadl2_Feature" = None, aadl2_ComponentClassifier121: set["aadl2_ProcessorPort"] = None, aadl2_ComponentClassifier235: "aadl2_AbstractFeature" = None, aadl2_ComponentClassifier238: "aadl2_Subcomponent" = None, aadl2_ComponentClassifier256: "aadl2_ComponentPrototype" = None, aadl2_ComponentClassifier796: "aadl2_FeaturePrototype" = None, aadl2_ComponentClassifier799: "aadl2_AccessSpecification" = None, aadl2_ComponentClassifier801: "aadl2_PortSpecification" = None, aadl2_ComponentClassifier810: "aadl2_ComponentReference" = None):
        self.noFlows = noFlows
        self.noModes = noModes
        self.aadl2_ComponentClassifier = aadl2_ComponentClassifier if aadl2_ComponentClassifier is not None else set()
        self.aadl2_ComponentClassifier119 = aadl2_ComponentClassifier119 if aadl2_ComponentClassifier119 is not None else set()
        self.aadl2_ComponentClassifier123 = aadl2_ComponentClassifier123 if aadl2_ComponentClassifier123 is not None else set()
        self.aadl2_ComponentClassifier142 = aadl2_ComponentClassifier142
        self.aadl2_ComponentClassifier121 = aadl2_ComponentClassifier121 if aadl2_ComponentClassifier121 is not None else set()
        self.aadl2_ComponentClassifier235 = aadl2_ComponentClassifier235
        self.aadl2_ComponentClassifier238 = aadl2_ComponentClassifier238
        self.aadl2_ComponentClassifier256 = aadl2_ComponentClassifier256
        self.aadl2_ComponentClassifier796 = aadl2_ComponentClassifier796
        self.aadl2_ComponentClassifier799 = aadl2_ComponentClassifier799
        self.aadl2_ComponentClassifier801 = aadl2_ComponentClassifier801
        self.aadl2_ComponentClassifier810 = aadl2_ComponentClassifier810
        
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
    def aadl2_ComponentClassifier238(self):
        return self.__aadl2_ComponentClassifier238

    @aadl2_ComponentClassifier238.setter
    def aadl2_ComponentClassifier238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier238", None)
        self.__aadl2_ComponentClassifier238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Subcomponent237"):
                opp_val = getattr(old_value, "aadl2_Subcomponent237", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Subcomponent237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Subcomponent237"):
                opp_val = getattr(value, "aadl2_Subcomponent237", None)
                setattr(value, "aadl2_Subcomponent237", self)

    @property
    def aadl2_ComponentClassifier801(self):
        return self.__aadl2_ComponentClassifier801

    @aadl2_ComponentClassifier801.setter
    def aadl2_ComponentClassifier801(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier801", None)
        self.__aadl2_ComponentClassifier801 = value
        
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
    def aadl2_ComponentClassifier799(self):
        return self.__aadl2_ComponentClassifier799

    @aadl2_ComponentClassifier799.setter
    def aadl2_ComponentClassifier799(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier799", None)
        self.__aadl2_ComponentClassifier799 = value
        
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
    def aadl2_ComponentClassifier121(self):
        return self.__aadl2_ComponentClassifier121

    @aadl2_ComponentClassifier121.setter
    def aadl2_ComponentClassifier121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier121", None)
        self.__aadl2_ComponentClassifier121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ProcessorPort"):
                    opp_val = getattr(item, "aadl2_ProcessorPort", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ProcessorPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ProcessorPort"):
                    opp_val = getattr(item, "aadl2_ProcessorPort", None)
                    
                    setattr(item, "aadl2_ProcessorPort", self)
                    

    @property
    def aadl2_ComponentClassifier123(self):
        return self.__aadl2_ComponentClassifier123

    @aadl2_ComponentClassifier123.setter
    def aadl2_ComponentClassifier123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier123", None)
        self.__aadl2_ComponentClassifier123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_InternalEvent"):
                    opp_val = getattr(item, "aadl2_InternalEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_InternalEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_InternalEvent"):
                    opp_val = getattr(item, "aadl2_InternalEvent", None)
                    
                    setattr(item, "aadl2_InternalEvent", self)
                    

    @property
    def aadl2_ComponentClassifier235(self):
        return self.__aadl2_ComponentClassifier235

    @aadl2_ComponentClassifier235.setter
    def aadl2_ComponentClassifier235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier235", None)
        self.__aadl2_ComponentClassifier235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_AbstractFeature234"):
                opp_val = getattr(old_value, "aadl2_AbstractFeature234", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_AbstractFeature234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_AbstractFeature234"):
                opp_val = getattr(value, "aadl2_AbstractFeature234", None)
                setattr(value, "aadl2_AbstractFeature234", self)

    @property
    def aadl2_ComponentClassifier256(self):
        return self.__aadl2_ComponentClassifier256

    @aadl2_ComponentClassifier256.setter
    def aadl2_ComponentClassifier256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier256", None)
        self.__aadl2_ComponentClassifier256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentPrototype255"):
                opp_val = getattr(old_value, "aadl2_ComponentPrototype255", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentPrototype255", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentPrototype255"):
                opp_val = getattr(value, "aadl2_ComponentPrototype255", None)
                setattr(value, "aadl2_ComponentPrototype255", self)

    @property
    def aadl2_ComponentClassifier796(self):
        return self.__aadl2_ComponentClassifier796

    @aadl2_ComponentClassifier796.setter
    def aadl2_ComponentClassifier796(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier796", None)
        self.__aadl2_ComponentClassifier796 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FeaturePrototype"):
                opp_val = getattr(old_value, "aadl2_FeaturePrototype", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FeaturePrototype", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FeaturePrototype"):
                opp_val = getattr(value, "aadl2_FeaturePrototype", None)
                setattr(value, "aadl2_FeaturePrototype", self)

    @property
    def aadl2_ComponentClassifier810(self):
        return self.__aadl2_ComponentClassifier810

    @aadl2_ComponentClassifier810.setter
    def aadl2_ComponentClassifier810(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier810", None)
        self.__aadl2_ComponentClassifier810 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentReference809"):
                opp_val = getattr(old_value, "aadl2_ComponentReference809", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentReference809", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentReference809"):
                opp_val = getattr(value, "aadl2_ComponentReference809", None)
                setattr(value, "aadl2_ComponentReference809", self)

    @property
    def aadl2_ComponentClassifier142(self):
        return self.__aadl2_ComponentClassifier142

    @aadl2_ComponentClassifier142.setter
    def aadl2_ComponentClassifier142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier142", None)
        self.__aadl2_ComponentClassifier142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Feature141"):
                opp_val = getattr(old_value, "aadl2_Feature141", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Feature141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Feature141"):
                opp_val = getattr(value, "aadl2_Feature141", None)
                setattr(value, "aadl2_Feature141", self)

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
                if hasattr(item, "aadl2_Mode117"):
                    opp_val = getattr(item, "aadl2_Mode117", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Mode117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Mode117"):
                    opp_val = getattr(item, "aadl2_Mode117", None)
                    
                    setattr(item, "aadl2_Mode117", self)
                    

    @property
    def aadl2_ComponentClassifier119(self):
        return self.__aadl2_ComponentClassifier119

    @aadl2_ComponentClassifier119.setter
    def aadl2_ComponentClassifier119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentClassifier__aadl2_ComponentClassifier119", None)
        self.__aadl2_ComponentClassifier119 = value if value is not None else set()
        
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
                    

class aadl2_ProcessorSubprogram(AccessConnectionEnd):

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
            if hasattr(old_value, "aadl2_ComponentImplementation105"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation105", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation105"):
                opp_val = getattr(value, "aadl2_ComponentImplementation105", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentImplementation105", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aadl2_AbstractSubcomponent(Subcomponent, Abstract):

    pass
class aadl2_EndToEndFlow(EndToEndFlowElement, ModalPath, Flow):

    pass
class aadl2_Realization(Generalization):

    pass
class aadl2_ImplementationExtension(Generalization):

    pass
class ComponentClassifier:

    pass
class aadl2_MemoryClassifier(ComponentClassifier, Memory):

    pass
class aadl2_AbstractClassifier(ComponentClassifier, Abstract):

    pass
class aadl2_SystemClassifier(ComponentClassifier, System):

    pass
class aadl2_SubprogramGroupClassifier(ComponentClassifier, SubprogramGroup):

    pass
class aadl2_ThreadGroupClassifier(ComponentClassifier, ThreadGroup):

    pass
class aadl2_SubprogramClassifier(ComponentClassifier, Subprogram):

    pass
class aadl2_ProcessClassifier(ComponentClassifier, Process):

    pass
class aadl2_BusClassifier(ComponentClassifier, Bus):

    pass
class aadl2_VirtualBusClassifier(ComponentClassifier, VirtualBus):

    pass
class aadl2_ProcessorClassifier(ComponentClassifier, Processor):

    pass
class aadl2_ThreadClassifier(ComponentClassifier, Thread):

    pass
class aadl2_VirtualProcessorClassifier(ComponentClassifier, VirtualProcessor):

    pass
class aadl2_DataClassifier(ComponentClassifier, Data):

    pass
class aadl2_ComponentType(ComponentClassifier):

    def __init__(self, features: str, noFeatures: str, aadl2_ComponentType: "aadl2_ComponentImplementation" = None, aadl2_ComponentType147: set["aadl2_Feature"] = None, aadl2_ComponentType151: "aadl2_ComponentType" = None, aadl2_ComponentType149: "aadl2_ComponentType" = None, aadl2_ComponentType153: set["aadl2_FlowSpecification"] = None, aadl2_ComponentType155: "aadl2_TypeExtension" = None, aadl2_ComponentType157: set["aadl2_FeatureGroup"] = None, aadl2_ComponentType159: set["aadl2_AbstractFeature"] = None, aadl2_ComponentType177: "aadl2_TypeExtension" = None, aadl2_ComponentType300: "aadl2_Realization" = None, aadl2_ComponentType399: "aadl2_ComponentTypeRename" = None):
        self.features = features
        self.noFeatures = noFeatures
        self.aadl2_ComponentType = aadl2_ComponentType
        self.aadl2_ComponentType147 = aadl2_ComponentType147 if aadl2_ComponentType147 is not None else set()
        self.aadl2_ComponentType151 = aadl2_ComponentType151
        self.aadl2_ComponentType149 = aadl2_ComponentType149
        self.aadl2_ComponentType153 = aadl2_ComponentType153 if aadl2_ComponentType153 is not None else set()
        self.aadl2_ComponentType155 = aadl2_ComponentType155
        self.aadl2_ComponentType157 = aadl2_ComponentType157 if aadl2_ComponentType157 is not None else set()
        self.aadl2_ComponentType159 = aadl2_ComponentType159 if aadl2_ComponentType159 is not None else set()
        self.aadl2_ComponentType177 = aadl2_ComponentType177
        self.aadl2_ComponentType300 = aadl2_ComponentType300
        self.aadl2_ComponentType399 = aadl2_ComponentType399
        
    @property
    def noFeatures(self) -> str:
        return self.__noFeatures

    @noFeatures.setter
    def noFeatures(self, noFeatures: str):
        self.__noFeatures = noFeatures

    @property
    def features(self) -> str:
        return self.__features

    @features.setter
    def features(self, features: str):
        self.__features = features

    @property
    def aadl2_ComponentType151(self):
        return self.__aadl2_ComponentType151

    @aadl2_ComponentType151.setter
    def aadl2_ComponentType151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType151", None)
        self.__aadl2_ComponentType151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentType149"):
                opp_val = getattr(old_value, "aadl2_ComponentType149", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentType149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentType149"):
                opp_val = getattr(value, "aadl2_ComponentType149", None)
                setattr(value, "aadl2_ComponentType149", self)

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
            if hasattr(old_value, "aadl2_ComponentImplementation86"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation86", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentImplementation86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation86"):
                opp_val = getattr(value, "aadl2_ComponentImplementation86", None)
                setattr(value, "aadl2_ComponentImplementation86", self)

    @property
    def aadl2_ComponentType177(self):
        return self.__aadl2_ComponentType177

    @aadl2_ComponentType177.setter
    def aadl2_ComponentType177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType177", None)
        self.__aadl2_ComponentType177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_TypeExtension176"):
                opp_val = getattr(old_value, "aadl2_TypeExtension176", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_TypeExtension176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_TypeExtension176"):
                opp_val = getattr(value, "aadl2_TypeExtension176", None)
                setattr(value, "aadl2_TypeExtension176", self)

    @property
    def aadl2_ComponentType153(self):
        return self.__aadl2_ComponentType153

    @aadl2_ComponentType153.setter
    def aadl2_ComponentType153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType153", None)
        self.__aadl2_ComponentType153 = value if value is not None else set()
        
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
                if hasattr(item, "aadl2_Feature148"):
                    opp_val = getattr(item, "aadl2_Feature148", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Feature148", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Feature148"):
                    opp_val = getattr(item, "aadl2_Feature148", None)
                    
                    setattr(item, "aadl2_Feature148", self)
                    

    @property
    def aadl2_ComponentType155(self):
        return self.__aadl2_ComponentType155

    @aadl2_ComponentType155.setter
    def aadl2_ComponentType155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType155", None)
        self.__aadl2_ComponentType155 = value
        
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
    def aadl2_ComponentType159(self):
        return self.__aadl2_ComponentType159

    @aadl2_ComponentType159.setter
    def aadl2_ComponentType159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType159", None)
        self.__aadl2_ComponentType159 = value if value is not None else set()
        
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
                    

    @property
    def aadl2_ComponentType157(self):
        return self.__aadl2_ComponentType157

    @aadl2_ComponentType157.setter
    def aadl2_ComponentType157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType157", None)
        self.__aadl2_ComponentType157 = value if value is not None else set()
        
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
    def aadl2_ComponentType300(self):
        return self.__aadl2_ComponentType300

    @aadl2_ComponentType300.setter
    def aadl2_ComponentType300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType300", None)
        self.__aadl2_ComponentType300 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Realization299"):
                opp_val = getattr(old_value, "aadl2_Realization299", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Realization299", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Realization299"):
                opp_val = getattr(value, "aadl2_Realization299", None)
                setattr(value, "aadl2_Realization299", self)

    @property
    def aadl2_ComponentType399(self):
        return self.__aadl2_ComponentType399

    @aadl2_ComponentType399.setter
    def aadl2_ComponentType399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType399", None)
        self.__aadl2_ComponentType399 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentTypeRename398"):
                opp_val = getattr(old_value, "aadl2_ComponentTypeRename398", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentTypeRename398", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentTypeRename398"):
                opp_val = getattr(value, "aadl2_ComponentTypeRename398", None)
                setattr(value, "aadl2_ComponentTypeRename398", self)

    @property
    def aadl2_ComponentType149(self):
        return self.__aadl2_ComponentType149

    @aadl2_ComponentType149.setter
    def aadl2_ComponentType149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentType__aadl2_ComponentType149", None)
        self.__aadl2_ComponentType149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentType151"):
                opp_val = getattr(old_value, "aadl2_ComponentType151", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentType151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentType151"):
                opp_val = getattr(value, "aadl2_ComponentType151", None)
                setattr(value, "aadl2_ComponentType151", self)

class aadl2_DeviceClassifier(ComponentClassifier, Device):

    pass
class aadl2_ComponentImplementation(ComponentClassifier):

    def __init__(self, connections: str, subcomponents: str, flows: str, noSubcomponents: str, noConnections: str, noCalls: str, aadl2_ComponentImplementation: "aadl2_ComponentImplementationReference" = None, aadl2_ComponentImplementation86: "aadl2_ComponentType" = None, aadl2_ComponentImplementation88: set["aadl2_Subcomponent"] = None, aadl2_ComponentImplementation91: "aadl2_ComponentImplementation" = None, aadl2_ComponentImplementation89: "aadl2_ComponentImplementation" = None, aadl2_ComponentImplementation93: set["aadl2_FlowImplementation"] = None, aadl2_ComponentImplementation95: set["aadl2_Connection"] = None, aadl2_ComponentImplementation97: "aadl2_ImplementationExtension" = None, aadl2_ComponentImplementation99: "aadl2_Realization" = None, aadl2_ComponentImplementation101: set["aadl2_EndToEndFlow"] = None, aadl2_ComponentImplementation103: set["aadl2_AbstractSubcomponent"] = None, aadl2_ComponentImplementation105: set["aadl2_AccessConnection"] = None, aadl2_ComponentImplementation107: set["aadl2_ParameterConnection"] = None, aadl2_ComponentImplementation109: set["aadl2_PortConnection"] = None, aadl2_ComponentImplementation111: set["aadl2_FeatureConnection"] = None, aadl2_ComponentImplementation113: set["aadl2_FeatureGroupConnection"] = None, aadl2_ComponentImplementation115: set["aadl2_ProcessorSubprogram"] = None, aadl2_ComponentImplementation297: "aadl2_ImplementationExtension" = None):
        self.connections = connections
        self.subcomponents = subcomponents
        self.flows = flows
        self.noSubcomponents = noSubcomponents
        self.noConnections = noConnections
        self.noCalls = noCalls
        self.aadl2_ComponentImplementation = aadl2_ComponentImplementation
        self.aadl2_ComponentImplementation86 = aadl2_ComponentImplementation86
        self.aadl2_ComponentImplementation88 = aadl2_ComponentImplementation88 if aadl2_ComponentImplementation88 is not None else set()
        self.aadl2_ComponentImplementation91 = aadl2_ComponentImplementation91
        self.aadl2_ComponentImplementation89 = aadl2_ComponentImplementation89
        self.aadl2_ComponentImplementation93 = aadl2_ComponentImplementation93 if aadl2_ComponentImplementation93 is not None else set()
        self.aadl2_ComponentImplementation95 = aadl2_ComponentImplementation95 if aadl2_ComponentImplementation95 is not None else set()
        self.aadl2_ComponentImplementation97 = aadl2_ComponentImplementation97
        self.aadl2_ComponentImplementation99 = aadl2_ComponentImplementation99
        self.aadl2_ComponentImplementation101 = aadl2_ComponentImplementation101 if aadl2_ComponentImplementation101 is not None else set()
        self.aadl2_ComponentImplementation103 = aadl2_ComponentImplementation103 if aadl2_ComponentImplementation103 is not None else set()
        self.aadl2_ComponentImplementation105 = aadl2_ComponentImplementation105 if aadl2_ComponentImplementation105 is not None else set()
        self.aadl2_ComponentImplementation107 = aadl2_ComponentImplementation107 if aadl2_ComponentImplementation107 is not None else set()
        self.aadl2_ComponentImplementation109 = aadl2_ComponentImplementation109 if aadl2_ComponentImplementation109 is not None else set()
        self.aadl2_ComponentImplementation111 = aadl2_ComponentImplementation111 if aadl2_ComponentImplementation111 is not None else set()
        self.aadl2_ComponentImplementation113 = aadl2_ComponentImplementation113 if aadl2_ComponentImplementation113 is not None else set()
        self.aadl2_ComponentImplementation115 = aadl2_ComponentImplementation115 if aadl2_ComponentImplementation115 is not None else set()
        self.aadl2_ComponentImplementation297 = aadl2_ComponentImplementation297
        
    @property
    def noSubcomponents(self) -> str:
        return self.__noSubcomponents

    @noSubcomponents.setter
    def noSubcomponents(self, noSubcomponents: str):
        self.__noSubcomponents = noSubcomponents

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
    def connections(self) -> str:
        return self.__connections

    @connections.setter
    def connections(self, connections: str):
        self.__connections = connections

    @property
    def flows(self) -> str:
        return self.__flows

    @flows.setter
    def flows(self, flows: str):
        self.__flows = flows

    @property
    def subcomponents(self) -> str:
        return self.__subcomponents

    @subcomponents.setter
    def subcomponents(self, subcomponents: str):
        self.__subcomponents = subcomponents

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
                if hasattr(item, "aadl2_ProcessorSubprogram"):
                    opp_val = getattr(item, "aadl2_ProcessorSubprogram", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ProcessorSubprogram", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ProcessorSubprogram"):
                    opp_val = getattr(item, "aadl2_ProcessorSubprogram", None)
                    
                    setattr(item, "aadl2_ProcessorSubprogram", self)
                    

    @property
    def aadl2_ComponentImplementation91(self):
        return self.__aadl2_ComponentImplementation91

    @aadl2_ComponentImplementation91.setter
    def aadl2_ComponentImplementation91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation91", None)
        self.__aadl2_ComponentImplementation91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentImplementation89"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation89", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentImplementation89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation89"):
                opp_val = getattr(value, "aadl2_ComponentImplementation89", None)
                setattr(value, "aadl2_ComponentImplementation89", self)

    @property
    def aadl2_ComponentImplementation93(self):
        return self.__aadl2_ComponentImplementation93

    @aadl2_ComponentImplementation93.setter
    def aadl2_ComponentImplementation93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation93", None)
        self.__aadl2_ComponentImplementation93 = value if value is not None else set()
        
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
    def aadl2_ComponentImplementation95(self):
        return self.__aadl2_ComponentImplementation95

    @aadl2_ComponentImplementation95.setter
    def aadl2_ComponentImplementation95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation95", None)
        self.__aadl2_ComponentImplementation95 = value if value is not None else set()
        
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
    def aadl2_ComponentImplementation99(self):
        return self.__aadl2_ComponentImplementation99

    @aadl2_ComponentImplementation99.setter
    def aadl2_ComponentImplementation99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation99", None)
        self.__aadl2_ComponentImplementation99 = value
        
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
    def aadl2_ComponentImplementation297(self):
        return self.__aadl2_ComponentImplementation297

    @aadl2_ComponentImplementation297.setter
    def aadl2_ComponentImplementation297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation297", None)
        self.__aadl2_ComponentImplementation297 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ImplementationExtension296"):
                opp_val = getattr(old_value, "aadl2_ImplementationExtension296", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ImplementationExtension296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ImplementationExtension296"):
                opp_val = getattr(value, "aadl2_ImplementationExtension296", None)
                setattr(value, "aadl2_ImplementationExtension296", self)

    @property
    def aadl2_ComponentImplementation86(self):
        return self.__aadl2_ComponentImplementation86

    @aadl2_ComponentImplementation86.setter
    def aadl2_ComponentImplementation86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation86", None)
        self.__aadl2_ComponentImplementation86 = value
        
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
    def aadl2_ComponentImplementation103(self):
        return self.__aadl2_ComponentImplementation103

    @aadl2_ComponentImplementation103.setter
    def aadl2_ComponentImplementation103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation103", None)
        self.__aadl2_ComponentImplementation103 = value if value is not None else set()
        
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
    def aadl2_ComponentImplementation97(self):
        return self.__aadl2_ComponentImplementation97

    @aadl2_ComponentImplementation97.setter
    def aadl2_ComponentImplementation97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation97", None)
        self.__aadl2_ComponentImplementation97 = value
        
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
    def aadl2_ComponentImplementation89(self):
        return self.__aadl2_ComponentImplementation89

    @aadl2_ComponentImplementation89.setter
    def aadl2_ComponentImplementation89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation89", None)
        self.__aadl2_ComponentImplementation89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentImplementation91"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation91", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentImplementation91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation91"):
                opp_val = getattr(value, "aadl2_ComponentImplementation91", None)
                setattr(value, "aadl2_ComponentImplementation91", self)

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
    def aadl2_ComponentImplementation88(self):
        return self.__aadl2_ComponentImplementation88

    @aadl2_ComponentImplementation88.setter
    def aadl2_ComponentImplementation88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentImplementation__aadl2_ComponentImplementation88", None)
        self.__aadl2_ComponentImplementation88 = value if value is not None else set()
        
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
                    

class ArraySize:

    pass
class aadl2_ConstantValue(ArraySize, PropertyValue):

    pass
class aadl2_PropertyReference(ArraySize, PropertyValue):

    pass
class aadl2_Numeral(ArraySize):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class RefinableElement:

    pass
class StructuralFeature:

    pass
class aadl2_Feature(ArrayableElement, StructuralFeature, FeatureConnectionEnd):

    pass
class aadl2_Connection(StructuralFeature, ModalPath, FlowElement):

    def __init__(self, kind: str, bidirectional: str, aadl2_Connection: "aadl2_ComponentImplementation" = None, aadl2_Connection282: "aadl2_ConnectionEnd" = None, aadl2_Connection284: "aadl2_ConnectionEnd" = None, aadl2_Connection287: "aadl2_Context" = None, aadl2_Connection290: "aadl2_Context" = None, aadl2_Connection294: "aadl2_Connection" = None, aadl2_Connection292: "aadl2_Connection" = None):
        self.kind = kind
        self.bidirectional = bidirectional
        self.aadl2_Connection = aadl2_Connection
        self.aadl2_Connection282 = aadl2_Connection282
        self.aadl2_Connection284 = aadl2_Connection284
        self.aadl2_Connection287 = aadl2_Connection287
        self.aadl2_Connection290 = aadl2_Connection290
        self.aadl2_Connection294 = aadl2_Connection294
        self.aadl2_Connection292 = aadl2_Connection292
        
    @property
    def bidirectional(self) -> str:
        return self.__bidirectional

    @bidirectional.setter
    def bidirectional(self, bidirectional: str):
        self.__bidirectional = bidirectional

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def aadl2_Connection290(self):
        return self.__aadl2_Connection290

    @aadl2_Connection290.setter
    def aadl2_Connection290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Connection__aadl2_Connection290", None)
        self.__aadl2_Connection290 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Context291"):
                opp_val = getattr(old_value, "aadl2_Context291", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Context291", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Context291"):
                opp_val = getattr(value, "aadl2_Context291", None)
                setattr(value, "aadl2_Context291", self)

    @property
    def aadl2_Connection292(self):
        return self.__aadl2_Connection292

    @aadl2_Connection292.setter
    def aadl2_Connection292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Connection__aadl2_Connection292", None)
        self.__aadl2_Connection292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Connection294"):
                opp_val = getattr(old_value, "aadl2_Connection294", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Connection294", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Connection294"):
                opp_val = getattr(value, "aadl2_Connection294", None)
                setattr(value, "aadl2_Connection294", self)

    @property
    def aadl2_Connection282(self):
        return self.__aadl2_Connection282

    @aadl2_Connection282.setter
    def aadl2_Connection282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Connection__aadl2_Connection282", None)
        self.__aadl2_Connection282 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ConnectionEnd"):
                opp_val = getattr(old_value, "aadl2_ConnectionEnd", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ConnectionEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ConnectionEnd"):
                opp_val = getattr(value, "aadl2_ConnectionEnd", None)
                setattr(value, "aadl2_ConnectionEnd", self)

    @property
    def aadl2_Connection287(self):
        return self.__aadl2_Connection287

    @aadl2_Connection287.setter
    def aadl2_Connection287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Connection__aadl2_Connection287", None)
        self.__aadl2_Connection287 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Context288"):
                opp_val = getattr(old_value, "aadl2_Context288", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Context288", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Context288"):
                opp_val = getattr(value, "aadl2_Context288", None)
                setattr(value, "aadl2_Context288", self)

    @property
    def aadl2_Connection294(self):
        return self.__aadl2_Connection294

    @aadl2_Connection294.setter
    def aadl2_Connection294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Connection__aadl2_Connection294", None)
        self.__aadl2_Connection294 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Connection292"):
                opp_val = getattr(old_value, "aadl2_Connection292", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Connection292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Connection292"):
                opp_val = getattr(value, "aadl2_Connection292", None)
                setattr(value, "aadl2_Connection292", self)

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
            if hasattr(old_value, "aadl2_ComponentImplementation95"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation95"):
                opp_val = getattr(value, "aadl2_ComponentImplementation95", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentImplementation95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_Connection284(self):
        return self.__aadl2_Connection284

    @aadl2_Connection284.setter
    def aadl2_Connection284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Connection__aadl2_Connection284", None)
        self.__aadl2_Connection284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ConnectionEnd285"):
                opp_val = getattr(old_value, "aadl2_ConnectionEnd285", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ConnectionEnd285", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ConnectionEnd285"):
                opp_val = getattr(value, "aadl2_ConnectionEnd285", None)
                setattr(value, "aadl2_ConnectionEnd285", self)

class aadl2_Flow(StructuralFeature):

    pass
class aadl2_FlowImplementation(ModalPath, StructuralFeature):

    def __init__(self, kind: str, aadl2_FlowImplementation: "aadl2_ComponentImplementation" = None, aadl2_FlowImplementation264: "aadl2_FlowSpecification" = None, aadl2_FlowImplementation267: set["aadl2_FlowElement"] = None, aadl2_FlowImplementation269: set["aadl2_SubcomponentFlow"] = None):
        self.kind = kind
        self.aadl2_FlowImplementation = aadl2_FlowImplementation
        self.aadl2_FlowImplementation264 = aadl2_FlowImplementation264
        self.aadl2_FlowImplementation267 = aadl2_FlowImplementation267 if aadl2_FlowImplementation267 is not None else set()
        self.aadl2_FlowImplementation269 = aadl2_FlowImplementation269 if aadl2_FlowImplementation269 is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def aadl2_FlowImplementation264(self):
        return self.__aadl2_FlowImplementation264

    @aadl2_FlowImplementation264.setter
    def aadl2_FlowImplementation264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowImplementation__aadl2_FlowImplementation264", None)
        self.__aadl2_FlowImplementation264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FlowSpecification265"):
                opp_val = getattr(old_value, "aadl2_FlowSpecification265", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FlowSpecification265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FlowSpecification265"):
                opp_val = getattr(value, "aadl2_FlowSpecification265", None)
                setattr(value, "aadl2_FlowSpecification265", self)

    @property
    def aadl2_FlowImplementation269(self):
        return self.__aadl2_FlowImplementation269

    @aadl2_FlowImplementation269.setter
    def aadl2_FlowImplementation269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowImplementation__aadl2_FlowImplementation269", None)
        self.__aadl2_FlowImplementation269 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_SubcomponentFlow"):
                    opp_val = getattr(item, "aadl2_SubcomponentFlow", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_SubcomponentFlow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_SubcomponentFlow"):
                    opp_val = getattr(item, "aadl2_SubcomponentFlow", None)
                    
                    setattr(item, "aadl2_SubcomponentFlow", self)
                    

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
            if hasattr(old_value, "aadl2_ComponentImplementation93"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation93", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation93"):
                opp_val = getattr(value, "aadl2_ComponentImplementation93", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentImplementation93", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_FlowImplementation267(self):
        return self.__aadl2_FlowImplementation267

    @aadl2_FlowImplementation267.setter
    def aadl2_FlowImplementation267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowImplementation__aadl2_FlowImplementation267", None)
        self.__aadl2_FlowImplementation267 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_FlowElement"):
                    opp_val = getattr(item, "aadl2_FlowElement", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_FlowElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_FlowElement"):
                    opp_val = getattr(item, "aadl2_FlowElement", None)
                    
                    setattr(item, "aadl2_FlowElement", self)
                    

class ClassifierFeature:

    pass
class aadl2_StructuralFeature(ClassifierFeature, RefinableElement):

    pass
class aadl2_BehavioralFeature(ClassifierFeature):

    pass
class aadl2_ModeFeature(ClassifierFeature):

    pass
class ModeFeature:

    pass
class aadl2_ModeTransition(ModeFeature):

    pass
class aadl2_Mode(ModeFeature):

    def __init__(self, initial: str, derived: str, aadl2_Mode: "aadl2_ModalElement" = None, aadl2_Mode117: "aadl2_ComponentClassifier" = None, aadl2_Mode126: "aadl2_ModeTransition" = None, aadl2_Mode129: "aadl2_ModeTransition" = None, aadl2_Mode259: "aadl2_ModeBinding" = None, aadl2_Mode262: "aadl2_ModeBinding" = None):
        self.initial = initial
        self.derived = derived
        self.aadl2_Mode = aadl2_Mode
        self.aadl2_Mode117 = aadl2_Mode117
        self.aadl2_Mode126 = aadl2_Mode126
        self.aadl2_Mode129 = aadl2_Mode129
        self.aadl2_Mode259 = aadl2_Mode259
        self.aadl2_Mode262 = aadl2_Mode262
        
    @property
    def initial(self) -> str:
        return self.__initial

    @initial.setter
    def initial(self, initial: str):
        self.__initial = initial

    @property
    def derived(self) -> str:
        return self.__derived

    @derived.setter
    def derived(self, derived: str):
        self.__derived = derived

    @property
    def aadl2_Mode262(self):
        return self.__aadl2_Mode262

    @aadl2_Mode262.setter
    def aadl2_Mode262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Mode__aadl2_Mode262", None)
        self.__aadl2_Mode262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ModeBinding261"):
                opp_val = getattr(old_value, "aadl2_ModeBinding261", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ModeBinding261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ModeBinding261"):
                opp_val = getattr(value, "aadl2_ModeBinding261", None)
                setattr(value, "aadl2_ModeBinding261", self)

    @property
    def aadl2_Mode126(self):
        return self.__aadl2_Mode126

    @aadl2_Mode126.setter
    def aadl2_Mode126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Mode__aadl2_Mode126", None)
        self.__aadl2_Mode126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ModeTransition125"):
                opp_val = getattr(old_value, "aadl2_ModeTransition125", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ModeTransition125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ModeTransition125"):
                opp_val = getattr(value, "aadl2_ModeTransition125", None)
                setattr(value, "aadl2_ModeTransition125", self)

    @property
    def aadl2_Mode259(self):
        return self.__aadl2_Mode259

    @aadl2_Mode259.setter
    def aadl2_Mode259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Mode__aadl2_Mode259", None)
        self.__aadl2_Mode259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ModeBinding258"):
                opp_val = getattr(old_value, "aadl2_ModeBinding258", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ModeBinding258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ModeBinding258"):
                opp_val = getattr(value, "aadl2_ModeBinding258", None)
                setattr(value, "aadl2_ModeBinding258", self)

    @property
    def aadl2_Mode129(self):
        return self.__aadl2_Mode129

    @aadl2_Mode129.setter
    def aadl2_Mode129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Mode__aadl2_Mode129", None)
        self.__aadl2_Mode129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ModeTransition128"):
                opp_val = getattr(old_value, "aadl2_ModeTransition128", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ModeTransition128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ModeTransition128"):
                opp_val = getattr(value, "aadl2_ModeTransition128", None)
                setattr(value, "aadl2_ModeTransition128", self)

    @property
    def aadl2_Mode117(self):
        return self.__aadl2_Mode117

    @aadl2_Mode117.setter
    def aadl2_Mode117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Mode__aadl2_Mode117", None)
        self.__aadl2_Mode117 = value
        
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
class aadl2_Subcomponent(ModalElement, Context, FlowElement, ArrayableElement, StructuralFeature):

    def __init__(self, allModes: str, aadl2_Subcomponent: "aadl2_ComponentImplementation" = None, aadl2_Subcomponent237: "aadl2_ComponentClassifier" = None, aadl2_Subcomponent240: set["aadl2_PrototypeBinding"] = None, aadl2_Subcomponent243: "aadl2_ComponentPrototype" = None, aadl2_Subcomponent245: set["aadl2_ModeBinding"] = None, aadl2_Subcomponent247: set["aadl2_ComponentImplementationReference"] = None, aadl2_Subcomponent251: "aadl2_Subcomponent" = None, aadl2_Subcomponent249: "aadl2_Subcomponent" = None, aadl2_Subcomponent253: "aadl2_AbstractClassifier" = None, aadl2_Subcomponent274: "aadl2_SubcomponentFlow" = None):
        self.allModes = allModes
        self.aadl2_Subcomponent = aadl2_Subcomponent
        self.aadl2_Subcomponent237 = aadl2_Subcomponent237
        self.aadl2_Subcomponent240 = aadl2_Subcomponent240 if aadl2_Subcomponent240 is not None else set()
        self.aadl2_Subcomponent243 = aadl2_Subcomponent243
        self.aadl2_Subcomponent245 = aadl2_Subcomponent245 if aadl2_Subcomponent245 is not None else set()
        self.aadl2_Subcomponent247 = aadl2_Subcomponent247 if aadl2_Subcomponent247 is not None else set()
        self.aadl2_Subcomponent251 = aadl2_Subcomponent251
        self.aadl2_Subcomponent249 = aadl2_Subcomponent249
        self.aadl2_Subcomponent253 = aadl2_Subcomponent253
        self.aadl2_Subcomponent274 = aadl2_Subcomponent274
        
    @property
    def allModes(self) -> str:
        return self.__allModes

    @allModes.setter
    def allModes(self, allModes: str):
        self.__allModes = allModes

    @property
    def aadl2_Subcomponent237(self):
        return self.__aadl2_Subcomponent237

    @aadl2_Subcomponent237.setter
    def aadl2_Subcomponent237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent237", None)
        self.__aadl2_Subcomponent237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentClassifier238"):
                opp_val = getattr(old_value, "aadl2_ComponentClassifier238", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentClassifier238", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentClassifier238"):
                opp_val = getattr(value, "aadl2_ComponentClassifier238", None)
                setattr(value, "aadl2_ComponentClassifier238", self)

    @property
    def aadl2_Subcomponent249(self):
        return self.__aadl2_Subcomponent249

    @aadl2_Subcomponent249.setter
    def aadl2_Subcomponent249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent249", None)
        self.__aadl2_Subcomponent249 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Subcomponent251"):
                opp_val = getattr(old_value, "aadl2_Subcomponent251", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Subcomponent251", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Subcomponent251"):
                opp_val = getattr(value, "aadl2_Subcomponent251", None)
                setattr(value, "aadl2_Subcomponent251", self)

    @property
    def aadl2_Subcomponent243(self):
        return self.__aadl2_Subcomponent243

    @aadl2_Subcomponent243.setter
    def aadl2_Subcomponent243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent243", None)
        self.__aadl2_Subcomponent243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentPrototype"):
                opp_val = getattr(old_value, "aadl2_ComponentPrototype", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentPrototype", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentPrototype"):
                opp_val = getattr(value, "aadl2_ComponentPrototype", None)
                setattr(value, "aadl2_ComponentPrototype", self)

    @property
    def aadl2_Subcomponent247(self):
        return self.__aadl2_Subcomponent247

    @aadl2_Subcomponent247.setter
    def aadl2_Subcomponent247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent247", None)
        self.__aadl2_Subcomponent247 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ComponentImplementationReference248"):
                    opp_val = getattr(item, "aadl2_ComponentImplementationReference248", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ComponentImplementationReference248", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ComponentImplementationReference248"):
                    opp_val = getattr(item, "aadl2_ComponentImplementationReference248", None)
                    
                    setattr(item, "aadl2_ComponentImplementationReference248", self)
                    

    @property
    def aadl2_Subcomponent240(self):
        return self.__aadl2_Subcomponent240

    @aadl2_Subcomponent240.setter
    def aadl2_Subcomponent240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent240", None)
        self.__aadl2_Subcomponent240 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_PrototypeBinding241"):
                    opp_val = getattr(item, "aadl2_PrototypeBinding241", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_PrototypeBinding241", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_PrototypeBinding241"):
                    opp_val = getattr(item, "aadl2_PrototypeBinding241", None)
                    
                    setattr(item, "aadl2_PrototypeBinding241", self)
                    

    @property
    def aadl2_Subcomponent251(self):
        return self.__aadl2_Subcomponent251

    @aadl2_Subcomponent251.setter
    def aadl2_Subcomponent251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent251", None)
        self.__aadl2_Subcomponent251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Subcomponent249"):
                opp_val = getattr(old_value, "aadl2_Subcomponent249", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Subcomponent249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Subcomponent249"):
                opp_val = getattr(value, "aadl2_Subcomponent249", None)
                setattr(value, "aadl2_Subcomponent249", self)

    @property
    def aadl2_Subcomponent245(self):
        return self.__aadl2_Subcomponent245

    @aadl2_Subcomponent245.setter
    def aadl2_Subcomponent245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent245", None)
        self.__aadl2_Subcomponent245 = value if value is not None else set()
        
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
    def aadl2_Subcomponent253(self):
        return self.__aadl2_Subcomponent253

    @aadl2_Subcomponent253.setter
    def aadl2_Subcomponent253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Subcomponent__aadl2_Subcomponent253", None)
        self.__aadl2_Subcomponent253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_AbstractClassifier"):
                opp_val = getattr(old_value, "aadl2_AbstractClassifier", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_AbstractClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_AbstractClassifier"):
                opp_val = getattr(value, "aadl2_AbstractClassifier", None)
                setattr(value, "aadl2_AbstractClassifier", self)

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
            if hasattr(old_value, "aadl2_ComponentImplementation88"):
                opp_val = getattr(old_value, "aadl2_ComponentImplementation88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentImplementation88"):
                opp_val = getattr(value, "aadl2_ComponentImplementation88", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentImplementation88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "aadl2_SubcomponentFlow273"):
                opp_val = getattr(old_value, "aadl2_SubcomponentFlow273", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_SubcomponentFlow273", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_SubcomponentFlow273"):
                opp_val = getattr(value, "aadl2_SubcomponentFlow273", None)
                setattr(value, "aadl2_SubcomponentFlow273", self)

class aadl2_ModalPath(ModalElement):

    pass
class aadl2_SubprogramCallSequence(ModalElement, BehavioralFeature):

    pass
class aadl2_FlowSpecification(ModalElement, Flow):

    def __init__(self, kind: str, aadl2_FlowSpecification: "aadl2_ComponentType" = None, aadl2_FlowSpecification162: "aadl2_FlowSpecification" = None, aadl2_FlowSpecification160: "aadl2_FlowSpecification" = None, aadl2_FlowSpecification164: "aadl2_Feature" = None, aadl2_FlowSpecification167: "aadl2_Context" = None, aadl2_FlowSpecification170: "aadl2_Feature" = None, aadl2_FlowSpecification173: "aadl2_Context" = None, aadl2_FlowSpecification265: "aadl2_FlowImplementation" = None, aadl2_FlowSpecification277: "aadl2_SubcomponentFlow" = None):
        self.kind = kind
        self.aadl2_FlowSpecification = aadl2_FlowSpecification
        self.aadl2_FlowSpecification162 = aadl2_FlowSpecification162
        self.aadl2_FlowSpecification160 = aadl2_FlowSpecification160
        self.aadl2_FlowSpecification164 = aadl2_FlowSpecification164
        self.aadl2_FlowSpecification167 = aadl2_FlowSpecification167
        self.aadl2_FlowSpecification170 = aadl2_FlowSpecification170
        self.aadl2_FlowSpecification173 = aadl2_FlowSpecification173
        self.aadl2_FlowSpecification265 = aadl2_FlowSpecification265
        self.aadl2_FlowSpecification277 = aadl2_FlowSpecification277
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def aadl2_FlowSpecification170(self):
        return self.__aadl2_FlowSpecification170

    @aadl2_FlowSpecification170.setter
    def aadl2_FlowSpecification170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowSpecification__aadl2_FlowSpecification170", None)
        self.__aadl2_FlowSpecification170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Feature171"):
                opp_val = getattr(old_value, "aadl2_Feature171", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Feature171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Feature171"):
                opp_val = getattr(value, "aadl2_Feature171", None)
                setattr(value, "aadl2_Feature171", self)

    @property
    def aadl2_FlowSpecification164(self):
        return self.__aadl2_FlowSpecification164

    @aadl2_FlowSpecification164.setter
    def aadl2_FlowSpecification164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowSpecification__aadl2_FlowSpecification164", None)
        self.__aadl2_FlowSpecification164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Feature165"):
                opp_val = getattr(old_value, "aadl2_Feature165", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Feature165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Feature165"):
                opp_val = getattr(value, "aadl2_Feature165", None)
                setattr(value, "aadl2_Feature165", self)

    @property
    def aadl2_FlowSpecification173(self):
        return self.__aadl2_FlowSpecification173

    @aadl2_FlowSpecification173.setter
    def aadl2_FlowSpecification173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowSpecification__aadl2_FlowSpecification173", None)
        self.__aadl2_FlowSpecification173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Context174"):
                opp_val = getattr(old_value, "aadl2_Context174", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Context174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Context174"):
                opp_val = getattr(value, "aadl2_Context174", None)
                setattr(value, "aadl2_Context174", self)

    @property
    def aadl2_FlowSpecification167(self):
        return self.__aadl2_FlowSpecification167

    @aadl2_FlowSpecification167.setter
    def aadl2_FlowSpecification167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowSpecification__aadl2_FlowSpecification167", None)
        self.__aadl2_FlowSpecification167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Context168"):
                opp_val = getattr(old_value, "aadl2_Context168", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Context168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Context168"):
                opp_val = getattr(value, "aadl2_Context168", None)
                setattr(value, "aadl2_Context168", self)

    @property
    def aadl2_FlowSpecification277(self):
        return self.__aadl2_FlowSpecification277

    @aadl2_FlowSpecification277.setter
    def aadl2_FlowSpecification277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowSpecification__aadl2_FlowSpecification277", None)
        self.__aadl2_FlowSpecification277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_SubcomponentFlow276"):
                opp_val = getattr(old_value, "aadl2_SubcomponentFlow276", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_SubcomponentFlow276", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_SubcomponentFlow276"):
                opp_val = getattr(value, "aadl2_SubcomponentFlow276", None)
                setattr(value, "aadl2_SubcomponentFlow276", self)

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
            if hasattr(old_value, "aadl2_ComponentType153"):
                opp_val = getattr(old_value, "aadl2_ComponentType153", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentType153"):
                opp_val = getattr(value, "aadl2_ComponentType153", None)
                if opp_val is None:
                    setattr(value, "aadl2_ComponentType153", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_FlowSpecification265(self):
        return self.__aadl2_FlowSpecification265

    @aadl2_FlowSpecification265.setter
    def aadl2_FlowSpecification265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowSpecification__aadl2_FlowSpecification265", None)
        self.__aadl2_FlowSpecification265 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FlowImplementation264"):
                opp_val = getattr(old_value, "aadl2_FlowImplementation264", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FlowImplementation264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FlowImplementation264"):
                opp_val = getattr(value, "aadl2_FlowImplementation264", None)
                setattr(value, "aadl2_FlowImplementation264", self)

    @property
    def aadl2_FlowSpecification160(self):
        return self.__aadl2_FlowSpecification160

    @aadl2_FlowSpecification160.setter
    def aadl2_FlowSpecification160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowSpecification__aadl2_FlowSpecification160", None)
        self.__aadl2_FlowSpecification160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FlowSpecification162"):
                opp_val = getattr(old_value, "aadl2_FlowSpecification162", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FlowSpecification162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FlowSpecification162"):
                opp_val = getattr(value, "aadl2_FlowSpecification162", None)
                setattr(value, "aadl2_FlowSpecification162", self)

    @property
    def aadl2_FlowSpecification162(self):
        return self.__aadl2_FlowSpecification162

    @aadl2_FlowSpecification162.setter
    def aadl2_FlowSpecification162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_FlowSpecification__aadl2_FlowSpecification162", None)
        self.__aadl2_FlowSpecification162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_FlowSpecification160"):
                opp_val = getattr(old_value, "aadl2_FlowSpecification160", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_FlowSpecification160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_FlowSpecification160"):
                opp_val = getattr(value, "aadl2_FlowSpecification160", None)
                setattr(value, "aadl2_FlowSpecification160", self)

class Relationship:

    pass
class aadl2_DirectedRelationship(Relationship):

    pass
class DirectedRelationship:

    pass
class aadl2_Prototype(StructuralFeature):

    def __init__(self, aadl2_Prototype: "aadl2_Classifier" = None, aadl2_Prototype59: "aadl2_Prototype" = None, aadl2_Prototype57: "aadl2_Prototype" = None, aadl2_Prototype67: "aadl2_PrototypeBinding" = None, aadl2_Prototype139: "aadl2_Feature" = None, aadl2_Prototype821: "aadl2_SubprogramCall" = None):
        self.aadl2_Prototype = aadl2_Prototype
        self.aadl2_Prototype59 = aadl2_Prototype59
        self.aadl2_Prototype57 = aadl2_Prototype57
        self.aadl2_Prototype67 = aadl2_Prototype67
        self.aadl2_Prototype139 = aadl2_Prototype139
        self.aadl2_Prototype821 = aadl2_Prototype821
        
    @property
    def aadl2_Prototype67(self):
        return self.__aadl2_Prototype67

    @aadl2_Prototype67.setter
    def aadl2_Prototype67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Prototype__aadl2_Prototype67", None)
        self.__aadl2_Prototype67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PrototypeBinding66"):
                opp_val = getattr(old_value, "aadl2_PrototypeBinding66", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_PrototypeBinding66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PrototypeBinding66"):
                opp_val = getattr(value, "aadl2_PrototypeBinding66", None)
                setattr(value, "aadl2_PrototypeBinding66", self)

    @property
    def aadl2_Prototype57(self):
        return self.__aadl2_Prototype57

    @aadl2_Prototype57.setter
    def aadl2_Prototype57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Prototype__aadl2_Prototype57", None)
        self.__aadl2_Prototype57 = value
        
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
    def aadl2_Prototype59(self):
        return self.__aadl2_Prototype59

    @aadl2_Prototype59.setter
    def aadl2_Prototype59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Prototype__aadl2_Prototype59", None)
        self.__aadl2_Prototype59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Prototype57"):
                opp_val = getattr(old_value, "aadl2_Prototype57", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Prototype57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Prototype57"):
                opp_val = getattr(value, "aadl2_Prototype57", None)
                setattr(value, "aadl2_Prototype57", self)

    @property
    def aadl2_Prototype821(self):
        return self.__aadl2_Prototype821

    @aadl2_Prototype821.setter
    def aadl2_Prototype821(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Prototype__aadl2_Prototype821", None)
        self.__aadl2_Prototype821 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_SubprogramCall820"):
                opp_val = getattr(old_value, "aadl2_SubprogramCall820", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_SubprogramCall820", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_SubprogramCall820"):
                opp_val = getattr(value, "aadl2_SubprogramCall820", None)
                setattr(value, "aadl2_SubprogramCall820", self)

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
            if hasattr(old_value, "aadl2_Classifier41"):
                opp_val = getattr(old_value, "aadl2_Classifier41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Classifier41"):
                opp_val = getattr(value, "aadl2_Classifier41", None)
                if opp_val is None:
                    setattr(value, "aadl2_Classifier41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_Prototype139(self):
        return self.__aadl2_Prototype139

    @aadl2_Prototype139.setter
    def aadl2_Prototype139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Prototype__aadl2_Prototype139", None)
        self.__aadl2_Prototype139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Feature"):
                opp_val = getattr(old_value, "aadl2_Feature", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Feature"):
                opp_val = getattr(value, "aadl2_Feature", None)
                setattr(value, "aadl2_Feature", self)

    def categoryConstraint(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement categoryConstraint method
        pass

class aadl2_AnnexSubclause(ModalElement):

    pass
class aadl2_Generalization(DirectedRelationship):

    pass
class Namespace:

    pass
class aadl2_RecordType(PropertyType, Namespace):

    pass
class aadl2_EnumerationType(PropertyType, Namespace):

    pass
class aadl2_GlobalNamespace(Namespace):

    pass
class aadl2_PropertySet(Namespace):

    def __init__(self, imports: str, contents: str, aadl2_PropertySet: "aadl2_PackageSection" = None, aadl2_PropertySet772: set["aadl2_PropertyType"] = None, aadl2_PropertySet775: set["aadl2_Property"] = None, aadl2_PropertySet778: set["aadl2_PropertyConstant"] = None, aadl2_PropertySet781: "aadl2_PropertySet" = None, aadl2_PropertySet779: set["aadl2_PropertySet"] = None, aadl2_PropertySet783: set["aadl2_AadlPackage"] = None, aadl2_PropertySet863: "aadl2_GlobalNamespace" = None):
        self.imports = imports
        self.contents = contents
        self.aadl2_PropertySet = aadl2_PropertySet
        self.aadl2_PropertySet772 = aadl2_PropertySet772 if aadl2_PropertySet772 is not None else set()
        self.aadl2_PropertySet775 = aadl2_PropertySet775 if aadl2_PropertySet775 is not None else set()
        self.aadl2_PropertySet778 = aadl2_PropertySet778 if aadl2_PropertySet778 is not None else set()
        self.aadl2_PropertySet781 = aadl2_PropertySet781
        self.aadl2_PropertySet779 = aadl2_PropertySet779 if aadl2_PropertySet779 is not None else set()
        self.aadl2_PropertySet783 = aadl2_PropertySet783 if aadl2_PropertySet783 is not None else set()
        self.aadl2_PropertySet863 = aadl2_PropertySet863
        
    @property
    def contents(self) -> str:
        return self.__contents

    @contents.setter
    def contents(self, contents: str):
        self.__contents = contents

    @property
    def imports(self) -> str:
        return self.__imports

    @imports.setter
    def imports(self, imports: str):
        self.__imports = imports

    @property
    def aadl2_PropertySet772(self):
        return self.__aadl2_PropertySet772

    @aadl2_PropertySet772.setter
    def aadl2_PropertySet772(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertySet__aadl2_PropertySet772", None)
        self.__aadl2_PropertySet772 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_PropertyType773"):
                    opp_val = getattr(item, "aadl2_PropertyType773", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_PropertyType773", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_PropertyType773"):
                    opp_val = getattr(item, "aadl2_PropertyType773", None)
                    
                    setattr(item, "aadl2_PropertyType773", self)
                    

    @property
    def aadl2_PropertySet781(self):
        return self.__aadl2_PropertySet781

    @aadl2_PropertySet781.setter
    def aadl2_PropertySet781(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertySet__aadl2_PropertySet781", None)
        self.__aadl2_PropertySet781 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PropertySet779"):
                opp_val = getattr(old_value, "aadl2_PropertySet779", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PropertySet779"):
                opp_val = getattr(value, "aadl2_PropertySet779", None)
                if opp_val is None:
                    setattr(value, "aadl2_PropertySet779", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_PropertySet863(self):
        return self.__aadl2_PropertySet863

    @aadl2_PropertySet863.setter
    def aadl2_PropertySet863(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertySet__aadl2_PropertySet863", None)
        self.__aadl2_PropertySet863 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_GlobalNamespace862"):
                opp_val = getattr(old_value, "aadl2_GlobalNamespace862", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_GlobalNamespace862"):
                opp_val = getattr(value, "aadl2_GlobalNamespace862", None)
                if opp_val is None:
                    setattr(value, "aadl2_GlobalNamespace862", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_PropertySet779(self):
        return self.__aadl2_PropertySet779

    @aadl2_PropertySet779.setter
    def aadl2_PropertySet779(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertySet__aadl2_PropertySet779", None)
        self.__aadl2_PropertySet779 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_PropertySet781"):
                    opp_val = getattr(item, "aadl2_PropertySet781", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_PropertySet781", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_PropertySet781"):
                    opp_val = getattr(item, "aadl2_PropertySet781", None)
                    
                    setattr(item, "aadl2_PropertySet781", self)
                    

    @property
    def aadl2_PropertySet783(self):
        return self.__aadl2_PropertySet783

    @aadl2_PropertySet783.setter
    def aadl2_PropertySet783(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertySet__aadl2_PropertySet783", None)
        self.__aadl2_PropertySet783 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_AadlPackage784"):
                    opp_val = getattr(item, "aadl2_AadlPackage784", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_AadlPackage784", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_AadlPackage784"):
                    opp_val = getattr(item, "aadl2_AadlPackage784", None)
                    
                    setattr(item, "aadl2_AadlPackage784", self)
                    

    @property
    def aadl2_PropertySet778(self):
        return self.__aadl2_PropertySet778

    @aadl2_PropertySet778.setter
    def aadl2_PropertySet778(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertySet__aadl2_PropertySet778", None)
        self.__aadl2_PropertySet778 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_PropertyConstant"):
                    opp_val = getattr(item, "aadl2_PropertyConstant", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_PropertyConstant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_PropertyConstant"):
                    opp_val = getattr(item, "aadl2_PropertyConstant", None)
                    
                    setattr(item, "aadl2_PropertyConstant", self)
                    

    @property
    def aadl2_PropertySet775(self):
        return self.__aadl2_PropertySet775

    @aadl2_PropertySet775.setter
    def aadl2_PropertySet775(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertySet__aadl2_PropertySet775", None)
        self.__aadl2_PropertySet775 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_Property776"):
                    opp_val = getattr(item, "aadl2_Property776", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Property776", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Property776"):
                    opp_val = getattr(item, "aadl2_Property776", None)
                    
                    setattr(item, "aadl2_Property776", self)
                    

    @property
    def aadl2_PropertySet(self):
        return self.__aadl2_PropertySet

    @aadl2_PropertySet.setter
    def aadl2_PropertySet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertySet__aadl2_PropertySet", None)
        self.__aadl2_PropertySet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PackageSection382"):
                opp_val = getattr(old_value, "aadl2_PackageSection382", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PackageSection382"):
                opp_val = getattr(value, "aadl2_PackageSection382", None)
                if opp_val is None:
                    setattr(value, "aadl2_PackageSection382", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aadl2_PackageSection(Namespace):

    def __init__(self, imports: str, aliases: str, declarations: str, noAnnexes: str, noProperties: str, aadl2_PackageSection: set["aadl2_PackageRename"] = None, aadl2_PackageSection312: set["aadl2_ComponentTypeRename"] = None, aadl2_PackageSection314: set["aadl2_Classifier"] = None, aadl2_PackageSection317: set["aadl2_FeatureGroupTypeRename"] = None, aadl2_PackageSection319: set["aadl2_AnnexLibrary"] = None, aadl2_PackageSection321: set["aadl2_AadlPackage"] = None, aadl2_PackageSection323: set["aadl2_AbstractType"] = None, aadl2_PackageSection325: set["aadl2_AbstractImplementation"] = None, aadl2_PackageSection327: set["aadl2_BusType"] = None, aadl2_PackageSection329: set["aadl2_BusImplementation"] = None, aadl2_PackageSection331: set["aadl2_DataType"] = None, aadl2_PackageSection333: set["aadl2_DataImplementation"] = None, aadl2_PackageSection335: set["aadl2_DeviceType"] = None, aadl2_PackageSection337: set["aadl2_DeviceImplementation"] = None, aadl2_PackageSection339: set["aadl2_MemoryType"] = None, aadl2_PackageSection341: set["aadl2_MemoryImplementation"] = None, aadl2_PackageSection343: set["aadl2_ProcessType"] = None, aadl2_PackageSection345: set["aadl2_ProcessorType"] = None, aadl2_PackageSection347: set["aadl2_ProcessImplementation"] = None, aadl2_PackageSection349: set["aadl2_ProcessorImplementation"] = None, aadl2_PackageSection351: set["aadl2_SubprogramType"] = None, aadl2_PackageSection353: set["aadl2_SubprogramImplementation"] = None, aadl2_PackageSection355: set["aadl2_SubprogramGroupType"] = None, aadl2_PackageSection357: set["aadl2_SubprogramGroupImplementation"] = None, aadl2_PackageSection359: set["aadl2_SystemType"] = None, aadl2_PackageSection361: set["aadl2_SystemImplementation"] = None, aadl2_PackageSection363: set["aadl2_ThreadType"] = None, aadl2_PackageSection365: set["aadl2_ThreadImplementation"] = None, aadl2_PackageSection367: set["aadl2_ThreadGroupType"] = None, aadl2_PackageSection369: set["aadl2_ThreadGroupImplementation"] = None, aadl2_PackageSection371: set["aadl2_VirtualBusType"] = None, aadl2_PackageSection373: set["aadl2_VirtualBusImplementation"] = None, aadl2_PackageSection375: set["aadl2_VirtualProcessorType"] = None, aadl2_PackageSection377: set["aadl2_VirtualProcessorImplementation"] = None, aadl2_PackageSection379: set["aadl2_FeatureGroupType"] = None, aadl2_PackageSection382: set["aadl2_PropertySet"] = None):
        self.imports = imports
        self.aliases = aliases
        self.declarations = declarations
        self.noAnnexes = noAnnexes
        self.noProperties = noProperties
        self.aadl2_PackageSection = aadl2_PackageSection if aadl2_PackageSection is not None else set()
        self.aadl2_PackageSection312 = aadl2_PackageSection312 if aadl2_PackageSection312 is not None else set()
        self.aadl2_PackageSection314 = aadl2_PackageSection314 if aadl2_PackageSection314 is not None else set()
        self.aadl2_PackageSection317 = aadl2_PackageSection317 if aadl2_PackageSection317 is not None else set()
        self.aadl2_PackageSection319 = aadl2_PackageSection319 if aadl2_PackageSection319 is not None else set()
        self.aadl2_PackageSection321 = aadl2_PackageSection321 if aadl2_PackageSection321 is not None else set()
        self.aadl2_PackageSection323 = aadl2_PackageSection323 if aadl2_PackageSection323 is not None else set()
        self.aadl2_PackageSection325 = aadl2_PackageSection325 if aadl2_PackageSection325 is not None else set()
        self.aadl2_PackageSection327 = aadl2_PackageSection327 if aadl2_PackageSection327 is not None else set()
        self.aadl2_PackageSection329 = aadl2_PackageSection329 if aadl2_PackageSection329 is not None else set()
        self.aadl2_PackageSection331 = aadl2_PackageSection331 if aadl2_PackageSection331 is not None else set()
        self.aadl2_PackageSection333 = aadl2_PackageSection333 if aadl2_PackageSection333 is not None else set()
        self.aadl2_PackageSection335 = aadl2_PackageSection335 if aadl2_PackageSection335 is not None else set()
        self.aadl2_PackageSection337 = aadl2_PackageSection337 if aadl2_PackageSection337 is not None else set()
        self.aadl2_PackageSection339 = aadl2_PackageSection339 if aadl2_PackageSection339 is not None else set()
        self.aadl2_PackageSection341 = aadl2_PackageSection341 if aadl2_PackageSection341 is not None else set()
        self.aadl2_PackageSection343 = aadl2_PackageSection343 if aadl2_PackageSection343 is not None else set()
        self.aadl2_PackageSection345 = aadl2_PackageSection345 if aadl2_PackageSection345 is not None else set()
        self.aadl2_PackageSection347 = aadl2_PackageSection347 if aadl2_PackageSection347 is not None else set()
        self.aadl2_PackageSection349 = aadl2_PackageSection349 if aadl2_PackageSection349 is not None else set()
        self.aadl2_PackageSection351 = aadl2_PackageSection351 if aadl2_PackageSection351 is not None else set()
        self.aadl2_PackageSection353 = aadl2_PackageSection353 if aadl2_PackageSection353 is not None else set()
        self.aadl2_PackageSection355 = aadl2_PackageSection355 if aadl2_PackageSection355 is not None else set()
        self.aadl2_PackageSection357 = aadl2_PackageSection357 if aadl2_PackageSection357 is not None else set()
        self.aadl2_PackageSection359 = aadl2_PackageSection359 if aadl2_PackageSection359 is not None else set()
        self.aadl2_PackageSection361 = aadl2_PackageSection361 if aadl2_PackageSection361 is not None else set()
        self.aadl2_PackageSection363 = aadl2_PackageSection363 if aadl2_PackageSection363 is not None else set()
        self.aadl2_PackageSection365 = aadl2_PackageSection365 if aadl2_PackageSection365 is not None else set()
        self.aadl2_PackageSection367 = aadl2_PackageSection367 if aadl2_PackageSection367 is not None else set()
        self.aadl2_PackageSection369 = aadl2_PackageSection369 if aadl2_PackageSection369 is not None else set()
        self.aadl2_PackageSection371 = aadl2_PackageSection371 if aadl2_PackageSection371 is not None else set()
        self.aadl2_PackageSection373 = aadl2_PackageSection373 if aadl2_PackageSection373 is not None else set()
        self.aadl2_PackageSection375 = aadl2_PackageSection375 if aadl2_PackageSection375 is not None else set()
        self.aadl2_PackageSection377 = aadl2_PackageSection377 if aadl2_PackageSection377 is not None else set()
        self.aadl2_PackageSection379 = aadl2_PackageSection379 if aadl2_PackageSection379 is not None else set()
        self.aadl2_PackageSection382 = aadl2_PackageSection382 if aadl2_PackageSection382 is not None else set()
        
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
    def imports(self) -> str:
        return self.__imports

    @imports.setter
    def imports(self, imports: str):
        self.__imports = imports

    @property
    def aliases(self) -> str:
        return self.__aliases

    @aliases.setter
    def aliases(self, aliases: str):
        self.__aliases = aliases

    @property
    def declarations(self) -> str:
        return self.__declarations

    @declarations.setter
    def declarations(self, declarations: str):
        self.__declarations = declarations

    @property
    def aadl2_PackageSection377(self):
        return self.__aadl2_PackageSection377

    @aadl2_PackageSection377.setter
    def aadl2_PackageSection377(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection377", None)
        self.__aadl2_PackageSection377 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_VirtualProcessorImplementation"):
                    opp_val = getattr(item, "aadl2_VirtualProcessorImplementation", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_VirtualProcessorImplementation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_VirtualProcessorImplementation"):
                    opp_val = getattr(item, "aadl2_VirtualProcessorImplementation", None)
                    
                    setattr(item, "aadl2_VirtualProcessorImplementation", self)
                    

    @property
    def aadl2_PackageSection343(self):
        return self.__aadl2_PackageSection343

    @aadl2_PackageSection343.setter
    def aadl2_PackageSection343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection343", None)
        self.__aadl2_PackageSection343 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ProcessType"):
                    opp_val = getattr(item, "aadl2_ProcessType", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ProcessType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ProcessType"):
                    opp_val = getattr(item, "aadl2_ProcessType", None)
                    
                    setattr(item, "aadl2_ProcessType", self)
                    

    @property
    def aadl2_PackageSection333(self):
        return self.__aadl2_PackageSection333

    @aadl2_PackageSection333.setter
    def aadl2_PackageSection333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection333", None)
        self.__aadl2_PackageSection333 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_DataImplementation"):
                    opp_val = getattr(item, "aadl2_DataImplementation", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_DataImplementation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_DataImplementation"):
                    opp_val = getattr(item, "aadl2_DataImplementation", None)
                    
                    setattr(item, "aadl2_DataImplementation", self)
                    

    @property
    def aadl2_PackageSection373(self):
        return self.__aadl2_PackageSection373

    @aadl2_PackageSection373.setter
    def aadl2_PackageSection373(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection373", None)
        self.__aadl2_PackageSection373 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_VirtualBusImplementation"):
                    opp_val = getattr(item, "aadl2_VirtualBusImplementation", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_VirtualBusImplementation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_VirtualBusImplementation"):
                    opp_val = getattr(item, "aadl2_VirtualBusImplementation", None)
                    
                    setattr(item, "aadl2_VirtualBusImplementation", self)
                    

    @property
    def aadl2_PackageSection325(self):
        return self.__aadl2_PackageSection325

    @aadl2_PackageSection325.setter
    def aadl2_PackageSection325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection325", None)
        self.__aadl2_PackageSection325 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_AbstractImplementation"):
                    opp_val = getattr(item, "aadl2_AbstractImplementation", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_AbstractImplementation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_AbstractImplementation"):
                    opp_val = getattr(item, "aadl2_AbstractImplementation", None)
                    
                    setattr(item, "aadl2_AbstractImplementation", self)
                    

    @property
    def aadl2_PackageSection355(self):
        return self.__aadl2_PackageSection355

    @aadl2_PackageSection355.setter
    def aadl2_PackageSection355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection355", None)
        self.__aadl2_PackageSection355 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_SubprogramGroupType"):
                    opp_val = getattr(item, "aadl2_SubprogramGroupType", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_SubprogramGroupType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_SubprogramGroupType"):
                    opp_val = getattr(item, "aadl2_SubprogramGroupType", None)
                    
                    setattr(item, "aadl2_SubprogramGroupType", self)
                    

    @property
    def aadl2_PackageSection371(self):
        return self.__aadl2_PackageSection371

    @aadl2_PackageSection371.setter
    def aadl2_PackageSection371(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection371", None)
        self.__aadl2_PackageSection371 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_VirtualBusType"):
                    opp_val = getattr(item, "aadl2_VirtualBusType", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_VirtualBusType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_VirtualBusType"):
                    opp_val = getattr(item, "aadl2_VirtualBusType", None)
                    
                    setattr(item, "aadl2_VirtualBusType", self)
                    

    @property
    def aadl2_PackageSection341(self):
        return self.__aadl2_PackageSection341

    @aadl2_PackageSection341.setter
    def aadl2_PackageSection341(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection341", None)
        self.__aadl2_PackageSection341 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_MemoryImplementation"):
                    opp_val = getattr(item, "aadl2_MemoryImplementation", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_MemoryImplementation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_MemoryImplementation"):
                    opp_val = getattr(item, "aadl2_MemoryImplementation", None)
                    
                    setattr(item, "aadl2_MemoryImplementation", self)
                    

    @property
    def aadl2_PackageSection327(self):
        return self.__aadl2_PackageSection327

    @aadl2_PackageSection327.setter
    def aadl2_PackageSection327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection327", None)
        self.__aadl2_PackageSection327 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_BusType"):
                    opp_val = getattr(item, "aadl2_BusType", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_BusType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_BusType"):
                    opp_val = getattr(item, "aadl2_BusType", None)
                    
                    setattr(item, "aadl2_BusType", self)
                    

    @property
    def aadl2_PackageSection369(self):
        return self.__aadl2_PackageSection369

    @aadl2_PackageSection369.setter
    def aadl2_PackageSection369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection369", None)
        self.__aadl2_PackageSection369 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ThreadGroupImplementation"):
                    opp_val = getattr(item, "aadl2_ThreadGroupImplementation", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ThreadGroupImplementation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ThreadGroupImplementation"):
                    opp_val = getattr(item, "aadl2_ThreadGroupImplementation", None)
                    
                    setattr(item, "aadl2_ThreadGroupImplementation", self)
                    

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
                if hasattr(item, "aadl2_MemoryType"):
                    opp_val = getattr(item, "aadl2_MemoryType", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_MemoryType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_MemoryType"):
                    opp_val = getattr(item, "aadl2_MemoryType", None)
                    
                    setattr(item, "aadl2_MemoryType", self)
                    

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
                if hasattr(item, "aadl2_SystemImplementation"):
                    opp_val = getattr(item, "aadl2_SystemImplementation", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_SystemImplementation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_SystemImplementation"):
                    opp_val = getattr(item, "aadl2_SystemImplementation", None)
                    
                    setattr(item, "aadl2_SystemImplementation", self)
                    

    @property
    def aadl2_PackageSection347(self):
        return self.__aadl2_PackageSection347

    @aadl2_PackageSection347.setter
    def aadl2_PackageSection347(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection347", None)
        self.__aadl2_PackageSection347 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ProcessImplementation"):
                    opp_val = getattr(item, "aadl2_ProcessImplementation", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ProcessImplementation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ProcessImplementation"):
                    opp_val = getattr(item, "aadl2_ProcessImplementation", None)
                    
                    setattr(item, "aadl2_ProcessImplementation", self)
                    

    @property
    def aadl2_PackageSection375(self):
        return self.__aadl2_PackageSection375

    @aadl2_PackageSection375.setter
    def aadl2_PackageSection375(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection375", None)
        self.__aadl2_PackageSection375 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_VirtualProcessorType"):
                    opp_val = getattr(item, "aadl2_VirtualProcessorType", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_VirtualProcessorType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_VirtualProcessorType"):
                    opp_val = getattr(item, "aadl2_VirtualProcessorType", None)
                    
                    setattr(item, "aadl2_VirtualProcessorType", self)
                    

    @property
    def aadl2_PackageSection379(self):
        return self.__aadl2_PackageSection379

    @aadl2_PackageSection379.setter
    def aadl2_PackageSection379(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection379", None)
        self.__aadl2_PackageSection379 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_FeatureGroupType380"):
                    opp_val = getattr(item, "aadl2_FeatureGroupType380", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_FeatureGroupType380", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_FeatureGroupType380"):
                    opp_val = getattr(item, "aadl2_FeatureGroupType380", None)
                    
                    setattr(item, "aadl2_FeatureGroupType380", self)
                    

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
    def aadl2_PackageSection367(self):
        return self.__aadl2_PackageSection367

    @aadl2_PackageSection367.setter
    def aadl2_PackageSection367(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection367", None)
        self.__aadl2_PackageSection367 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ThreadGroupType"):
                    opp_val = getattr(item, "aadl2_ThreadGroupType", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ThreadGroupType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ThreadGroupType"):
                    opp_val = getattr(item, "aadl2_ThreadGroupType", None)
                    
                    setattr(item, "aadl2_ThreadGroupType", self)
                    

    @property
    def aadl2_PackageSection357(self):
        return self.__aadl2_PackageSection357

    @aadl2_PackageSection357.setter
    def aadl2_PackageSection357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection357", None)
        self.__aadl2_PackageSection357 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_SubprogramGroupImplementation"):
                    opp_val = getattr(item, "aadl2_SubprogramGroupImplementation", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_SubprogramGroupImplementation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_SubprogramGroupImplementation"):
                    opp_val = getattr(item, "aadl2_SubprogramGroupImplementation", None)
                    
                    setattr(item, "aadl2_SubprogramGroupImplementation", self)
                    

    @property
    def aadl2_PackageSection382(self):
        return self.__aadl2_PackageSection382

    @aadl2_PackageSection382.setter
    def aadl2_PackageSection382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection382", None)
        self.__aadl2_PackageSection382 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_PropertySet"):
                    opp_val = getattr(item, "aadl2_PropertySet", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_PropertySet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_PropertySet"):
                    opp_val = getattr(item, "aadl2_PropertySet", None)
                    
                    setattr(item, "aadl2_PropertySet", self)
                    

    @property
    def aadl2_PackageSection365(self):
        return self.__aadl2_PackageSection365

    @aadl2_PackageSection365.setter
    def aadl2_PackageSection365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection365", None)
        self.__aadl2_PackageSection365 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ThreadImplementation"):
                    opp_val = getattr(item, "aadl2_ThreadImplementation", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ThreadImplementation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ThreadImplementation"):
                    opp_val = getattr(item, "aadl2_ThreadImplementation", None)
                    
                    setattr(item, "aadl2_ThreadImplementation", self)
                    

    @property
    def aadl2_PackageSection359(self):
        return self.__aadl2_PackageSection359

    @aadl2_PackageSection359.setter
    def aadl2_PackageSection359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection359", None)
        self.__aadl2_PackageSection359 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_SystemType"):
                    opp_val = getattr(item, "aadl2_SystemType", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_SystemType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_SystemType"):
                    opp_val = getattr(item, "aadl2_SystemType", None)
                    
                    setattr(item, "aadl2_SystemType", self)
                    

    @property
    def aadl2_PackageSection337(self):
        return self.__aadl2_PackageSection337

    @aadl2_PackageSection337.setter
    def aadl2_PackageSection337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection337", None)
        self.__aadl2_PackageSection337 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_DeviceImplementation"):
                    opp_val = getattr(item, "aadl2_DeviceImplementation", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_DeviceImplementation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_DeviceImplementation"):
                    opp_val = getattr(item, "aadl2_DeviceImplementation", None)
                    
                    setattr(item, "aadl2_DeviceImplementation", self)
                    

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
                if hasattr(item, "aadl2_ThreadType"):
                    opp_val = getattr(item, "aadl2_ThreadType", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ThreadType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ThreadType"):
                    opp_val = getattr(item, "aadl2_ThreadType", None)
                    
                    setattr(item, "aadl2_ThreadType", self)
                    

    @property
    def aadl2_PackageSection335(self):
        return self.__aadl2_PackageSection335

    @aadl2_PackageSection335.setter
    def aadl2_PackageSection335(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection335", None)
        self.__aadl2_PackageSection335 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_DeviceType"):
                    opp_val = getattr(item, "aadl2_DeviceType", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_DeviceType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_DeviceType"):
                    opp_val = getattr(item, "aadl2_DeviceType", None)
                    
                    setattr(item, "aadl2_DeviceType", self)
                    

    @property
    def aadl2_PackageSection319(self):
        return self.__aadl2_PackageSection319

    @aadl2_PackageSection319.setter
    def aadl2_PackageSection319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection319", None)
        self.__aadl2_PackageSection319 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_AnnexLibrary"):
                    opp_val = getattr(item, "aadl2_AnnexLibrary", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_AnnexLibrary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_AnnexLibrary"):
                    opp_val = getattr(item, "aadl2_AnnexLibrary", None)
                    
                    setattr(item, "aadl2_AnnexLibrary", self)
                    

    @property
    def aadl2_PackageSection349(self):
        return self.__aadl2_PackageSection349

    @aadl2_PackageSection349.setter
    def aadl2_PackageSection349(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection349", None)
        self.__aadl2_PackageSection349 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ProcessorImplementation"):
                    opp_val = getattr(item, "aadl2_ProcessorImplementation", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ProcessorImplementation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ProcessorImplementation"):
                    opp_val = getattr(item, "aadl2_ProcessorImplementation", None)
                    
                    setattr(item, "aadl2_ProcessorImplementation", self)
                    

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
                if hasattr(item, "aadl2_BusImplementation"):
                    opp_val = getattr(item, "aadl2_BusImplementation", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_BusImplementation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_BusImplementation"):
                    opp_val = getattr(item, "aadl2_BusImplementation", None)
                    
                    setattr(item, "aadl2_BusImplementation", self)
                    

    @property
    def aadl2_PackageSection345(self):
        return self.__aadl2_PackageSection345

    @aadl2_PackageSection345.setter
    def aadl2_PackageSection345(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection345", None)
        self.__aadl2_PackageSection345 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ProcessorType"):
                    opp_val = getattr(item, "aadl2_ProcessorType", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ProcessorType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ProcessorType"):
                    opp_val = getattr(item, "aadl2_ProcessorType", None)
                    
                    setattr(item, "aadl2_ProcessorType", self)
                    

    @property
    def aadl2_PackageSection317(self):
        return self.__aadl2_PackageSection317

    @aadl2_PackageSection317.setter
    def aadl2_PackageSection317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection317", None)
        self.__aadl2_PackageSection317 = value if value is not None else set()
        
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
                if hasattr(item, "aadl2_DataType"):
                    opp_val = getattr(item, "aadl2_DataType", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_DataType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_DataType"):
                    opp_val = getattr(item, "aadl2_DataType", None)
                    
                    setattr(item, "aadl2_DataType", self)
                    

    @property
    def aadl2_PackageSection353(self):
        return self.__aadl2_PackageSection353

    @aadl2_PackageSection353.setter
    def aadl2_PackageSection353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection353", None)
        self.__aadl2_PackageSection353 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_SubprogramImplementation"):
                    opp_val = getattr(item, "aadl2_SubprogramImplementation", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_SubprogramImplementation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_SubprogramImplementation"):
                    opp_val = getattr(item, "aadl2_SubprogramImplementation", None)
                    
                    setattr(item, "aadl2_SubprogramImplementation", self)
                    

    @property
    def aadl2_PackageSection314(self):
        return self.__aadl2_PackageSection314

    @aadl2_PackageSection314.setter
    def aadl2_PackageSection314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection314", None)
        self.__aadl2_PackageSection314 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_Classifier315"):
                    opp_val = getattr(item, "aadl2_Classifier315", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Classifier315", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Classifier315"):
                    opp_val = getattr(item, "aadl2_Classifier315", None)
                    
                    setattr(item, "aadl2_Classifier315", self)
                    

    @property
    def aadl2_PackageSection351(self):
        return self.__aadl2_PackageSection351

    @aadl2_PackageSection351.setter
    def aadl2_PackageSection351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection351", None)
        self.__aadl2_PackageSection351 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_SubprogramType"):
                    opp_val = getattr(item, "aadl2_SubprogramType", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_SubprogramType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_SubprogramType"):
                    opp_val = getattr(item, "aadl2_SubprogramType", None)
                    
                    setattr(item, "aadl2_SubprogramType", self)
                    

    @property
    def aadl2_PackageSection312(self):
        return self.__aadl2_PackageSection312

    @aadl2_PackageSection312.setter
    def aadl2_PackageSection312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection312", None)
        self.__aadl2_PackageSection312 = value if value is not None else set()
        
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
    def aadl2_PackageSection321(self):
        return self.__aadl2_PackageSection321

    @aadl2_PackageSection321.setter
    def aadl2_PackageSection321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection321", None)
        self.__aadl2_PackageSection321 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_AadlPackage"):
                    opp_val = getattr(item, "aadl2_AadlPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_AadlPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_AadlPackage"):
                    opp_val = getattr(item, "aadl2_AadlPackage", None)
                    
                    setattr(item, "aadl2_AadlPackage", self)
                    

    @property
    def aadl2_PackageSection323(self):
        return self.__aadl2_PackageSection323

    @aadl2_PackageSection323.setter
    def aadl2_PackageSection323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageSection__aadl2_PackageSection323", None)
        self.__aadl2_PackageSection323 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_AbstractType"):
                    opp_val = getattr(item, "aadl2_AbstractType", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_AbstractType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_AbstractType"):
                    opp_val = getattr(item, "aadl2_AbstractType", None)
                    
                    setattr(item, "aadl2_AbstractType", self)
                    

class PropertyOwner:

    pass
class aadl2_ClassifierValue(PropertyOwner, PropertyValue):

    pass
class Type:

    pass
class aadl2_PropertyType(Type):

    pass
class TypedElement:

    pass
class aadl2_PropertyConstant(TypedElement):

    def __init__(self, list: str, aadl2_PropertyConstant: "aadl2_PropertySet" = None, aadl2_PropertyConstant786: "aadl2_PropertyType" = None, aadl2_PropertyConstant789: "aadl2_PropertyExpression" = None, aadl2_PropertyConstant850: "aadl2_ConstantValue" = None):
        self.list = list
        self.aadl2_PropertyConstant = aadl2_PropertyConstant
        self.aadl2_PropertyConstant786 = aadl2_PropertyConstant786
        self.aadl2_PropertyConstant789 = aadl2_PropertyConstant789
        self.aadl2_PropertyConstant850 = aadl2_PropertyConstant850
        
    @property
    def list(self) -> str:
        return self.__list

    @list.setter
    def list(self, list: str):
        self.__list = list

    @property
    def aadl2_PropertyConstant786(self):
        return self.__aadl2_PropertyConstant786

    @aadl2_PropertyConstant786.setter
    def aadl2_PropertyConstant786(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertyConstant__aadl2_PropertyConstant786", None)
        self.__aadl2_PropertyConstant786 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PropertyType787"):
                opp_val = getattr(old_value, "aadl2_PropertyType787", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_PropertyType787", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PropertyType787"):
                opp_val = getattr(value, "aadl2_PropertyType787", None)
                setattr(value, "aadl2_PropertyType787", self)

    @property
    def aadl2_PropertyConstant850(self):
        return self.__aadl2_PropertyConstant850

    @aadl2_PropertyConstant850.setter
    def aadl2_PropertyConstant850(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertyConstant__aadl2_PropertyConstant850", None)
        self.__aadl2_PropertyConstant850 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ConstantValue"):
                opp_val = getattr(old_value, "aadl2_ConstantValue", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ConstantValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ConstantValue"):
                opp_val = getattr(value, "aadl2_ConstantValue", None)
                setattr(value, "aadl2_ConstantValue", self)

    @property
    def aadl2_PropertyConstant789(self):
        return self.__aadl2_PropertyConstant789

    @aadl2_PropertyConstant789.setter
    def aadl2_PropertyConstant789(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertyConstant__aadl2_PropertyConstant789", None)
        self.__aadl2_PropertyConstant789 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PropertyExpression790"):
                opp_val = getattr(old_value, "aadl2_PropertyExpression790", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_PropertyExpression790", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PropertyExpression790"):
                opp_val = getattr(value, "aadl2_PropertyExpression790", None)
                setattr(value, "aadl2_PropertyExpression790", self)

    @property
    def aadl2_PropertyConstant(self):
        return self.__aadl2_PropertyConstant

    @aadl2_PropertyConstant.setter
    def aadl2_PropertyConstant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertyConstant__aadl2_PropertyConstant", None)
        self.__aadl2_PropertyConstant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PropertySet778"):
                opp_val = getattr(old_value, "aadl2_PropertySet778", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PropertySet778"):
                opp_val = getattr(value, "aadl2_PropertySet778", None)
                if opp_val is None:
                    setattr(value, "aadl2_PropertySet778", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aadl2_BasicProperty(TypedElement):

    def __init__(self, list: str, aadl2_BasicProperty: "aadl2_PropertyType" = None, aadl2_BasicProperty825: "aadl2_BasicPropertyAssociation" = None, aadl2_BasicProperty886: "aadl2_RecordType" = None):
        self.list = list
        self.aadl2_BasicProperty = aadl2_BasicProperty
        self.aadl2_BasicProperty825 = aadl2_BasicProperty825
        self.aadl2_BasicProperty886 = aadl2_BasicProperty886
        
    @property
    def list(self) -> str:
        return self.__list

    @list.setter
    def list(self, list: str):
        self.__list = list

    @property
    def aadl2_BasicProperty886(self):
        return self.__aadl2_BasicProperty886

    @aadl2_BasicProperty886.setter
    def aadl2_BasicProperty886(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_BasicProperty__aadl2_BasicProperty886", None)
        self.__aadl2_BasicProperty886 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_RecordType"):
                opp_val = getattr(old_value, "aadl2_RecordType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_RecordType"):
                opp_val = getattr(value, "aadl2_RecordType", None)
                if opp_val is None:
                    setattr(value, "aadl2_RecordType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_BasicProperty825(self):
        return self.__aadl2_BasicProperty825

    @aadl2_BasicProperty825.setter
    def aadl2_BasicProperty825(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_BasicProperty__aadl2_BasicProperty825", None)
        self.__aadl2_BasicProperty825 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_BasicPropertyAssociation"):
                opp_val = getattr(old_value, "aadl2_BasicPropertyAssociation", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_BasicPropertyAssociation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_BasicPropertyAssociation"):
                opp_val = getattr(value, "aadl2_BasicPropertyAssociation", None)
                setattr(value, "aadl2_BasicPropertyAssociation", self)

    @property
    def aadl2_BasicProperty(self):
        return self.__aadl2_BasicProperty

    @aadl2_BasicProperty.setter
    def aadl2_BasicProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_BasicProperty__aadl2_BasicProperty", None)
        self.__aadl2_BasicProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PropertyType"):
                opp_val = getattr(old_value, "aadl2_PropertyType", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_PropertyType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PropertyType"):
                opp_val = getattr(value, "aadl2_PropertyType", None)
                setattr(value, "aadl2_PropertyType", self)

class aadl2_MetaclassReference(PropertyOwner):

    def __init__(self, annexName: str, metaclassName: str, aadl2_MetaclassReference: "aadl2_Property" = None, aadl2_MetaclassReference879: "aadl2_ClassifierType" = None, aadl2_MetaclassReference888: "aadl2_ReferenceType" = None):
        self.annexName = annexName
        self.metaclassName = metaclassName
        self.aadl2_MetaclassReference = aadl2_MetaclassReference
        self.aadl2_MetaclassReference879 = aadl2_MetaclassReference879
        self.aadl2_MetaclassReference888 = aadl2_MetaclassReference888
        
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
            if hasattr(old_value, "aadl2_Property22"):
                opp_val = getattr(old_value, "aadl2_Property22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Property22"):
                opp_val = getattr(value, "aadl2_Property22", None)
                if opp_val is None:
                    setattr(value, "aadl2_Property22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_MetaclassReference888(self):
        return self.__aadl2_MetaclassReference888

    @aadl2_MetaclassReference888.setter
    def aadl2_MetaclassReference888(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_MetaclassReference__aadl2_MetaclassReference888", None)
        self.__aadl2_MetaclassReference888 = value
        
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
    def aadl2_MetaclassReference879(self):
        return self.__aadl2_MetaclassReference879

    @aadl2_MetaclassReference879.setter
    def aadl2_MetaclassReference879(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_MetaclassReference__aadl2_MetaclassReference879", None)
        self.__aadl2_MetaclassReference879 = value
        
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

class BasicProperty:

    pass
class aadl2_RecordField(BasicProperty):

    pass
class aadl2_ModalPropertyValue(ModalElement):

    pass
class aadl2_Classifier(Namespace, Type):

    def __init__(self, noPrototypes: str, noAnnexes: str, noProperties: str, aadl2_Classifier: "aadl2_PropertyAssociation" = None, aadl2_Classifier25: "aadl2_Property" = None, featuringClassifier: set["aadl2_ClassifierFeature"] = None, aadl2_Classifier32: set["aadl2_NamedElement"] = None, specific: set["aadl2_Generalization"] = None, aadl2_Classifier37: "aadl2_Classifier" = None, aadl2_Classifier35: set["aadl2_Classifier"] = None, aadl2_Classifier39: set["aadl2_AnnexSubclause"] = None, aadl2_Classifier41: set["aadl2_Prototype"] = None, aadl2_Classifier43: set["aadl2_PrototypeBinding"] = None, Classifier: "aadl2_ClassifierFeature" = None, aadl2_Classifier46: "aadl2_Generalization" = None, Classifier48: "aadl2_Generalization" = None, aadl2_Classifier61: "aadl2_RefinableElement" = None, aadl2_Classifier315: "aadl2_PackageSection" = None, aadl2_Classifier840: "aadl2_ClassifierValue" = None):
        self.noPrototypes = noPrototypes
        self.noAnnexes = noAnnexes
        self.noProperties = noProperties
        self.aadl2_Classifier = aadl2_Classifier
        self.aadl2_Classifier25 = aadl2_Classifier25
        self.featuringClassifier = featuringClassifier if featuringClassifier is not None else set()
        self.aadl2_Classifier32 = aadl2_Classifier32 if aadl2_Classifier32 is not None else set()
        self.specific = specific if specific is not None else set()
        self.aadl2_Classifier37 = aadl2_Classifier37
        self.aadl2_Classifier35 = aadl2_Classifier35 if aadl2_Classifier35 is not None else set()
        self.aadl2_Classifier39 = aadl2_Classifier39 if aadl2_Classifier39 is not None else set()
        self.aadl2_Classifier41 = aadl2_Classifier41 if aadl2_Classifier41 is not None else set()
        self.aadl2_Classifier43 = aadl2_Classifier43 if aadl2_Classifier43 is not None else set()
        self.Classifier = Classifier
        self.aadl2_Classifier46 = aadl2_Classifier46
        self.Classifier48 = Classifier48
        self.aadl2_Classifier61 = aadl2_Classifier61
        self.aadl2_Classifier315 = aadl2_Classifier315
        self.aadl2_Classifier840 = aadl2_Classifier840
        
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
    def noAnnexes(self) -> str:
        return self.__noAnnexes

    @noAnnexes.setter
    def noAnnexes(self, noAnnexes: str):
        self.__noAnnexes = noAnnexes

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
    def aadl2_Classifier(self):
        return self.__aadl2_Classifier

    @aadl2_Classifier.setter
    def aadl2_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier", None)
        self.__aadl2_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PropertyAssociation16"):
                opp_val = getattr(old_value, "aadl2_PropertyAssociation16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PropertyAssociation16"):
                opp_val = getattr(value, "aadl2_PropertyAssociation16", None)
                if opp_val is None:
                    setattr(value, "aadl2_PropertyAssociation16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def aadl2_Classifier25(self):
        return self.__aadl2_Classifier25

    @aadl2_Classifier25.setter
    def aadl2_Classifier25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier25", None)
        self.__aadl2_Classifier25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_Property24"):
                opp_val = getattr(old_value, "aadl2_Property24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Property24"):
                opp_val = getattr(value, "aadl2_Property24", None)
                if opp_val is None:
                    setattr(value, "aadl2_Property24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_Classifier46(self):
        return self.__aadl2_Classifier46

    @aadl2_Classifier46.setter
    def aadl2_Classifier46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier46", None)
        self.__aadl2_Classifier46 = value
        
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
    def aadl2_Classifier315(self):
        return self.__aadl2_Classifier315

    @aadl2_Classifier315.setter
    def aadl2_Classifier315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier315", None)
        self.__aadl2_Classifier315 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PackageSection314"):
                opp_val = getattr(old_value, "aadl2_PackageSection314", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PackageSection314"):
                opp_val = getattr(value, "aadl2_PackageSection314", None)
                if opp_val is None:
                    setattr(value, "aadl2_PackageSection314", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_Classifier61(self):
        return self.__aadl2_Classifier61

    @aadl2_Classifier61.setter
    def aadl2_Classifier61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier61", None)
        self.__aadl2_Classifier61 = value
        
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
    def aadl2_Classifier840(self):
        return self.__aadl2_Classifier840

    @aadl2_Classifier840.setter
    def aadl2_Classifier840(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__aadl2_Classifier840", None)
        self.__aadl2_Classifier840 = value
        
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
    def Classifier48(self):
        return self.__Classifier48

    @Classifier48.setter
    def Classifier48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Classifier__Classifier48", None)
        self.__Classifier48 = value
        
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

    def inheritableMembers(self, c: str) -> NamedElement:
        # TODO: Implement inheritableMembers method
        pass

    def inherit(self, inhs: NamedElement) -> NamedElement:
        # TODO: Implement inherit method
        pass

    def maySpecializeType(self, c: str) -> str:
        # TODO: Implement maySpecializeType method
        pass

    def parents(self) -> str:
        # TODO: Implement parents method
        pass

    def no_cycles_in_generalization(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement no_cycles_in_generalization method
        pass

    def allFeatures(self) -> str:
        # TODO: Implement allFeatures method
        pass

    def inheritedMember(self) -> NamedElement:
        # TODO: Implement inheritedMember method
        pass

    def allParents(self) -> str:
        # TODO: Implement allParents method
        pass

    def hasVisibilityOf(self, n: NamedElement) -> str:
        # TODO: Implement hasVisibilityOf method
        pass

    def specialize_type(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement specialize_type method
        pass

class aadl2_Property(BasicProperty):

    def __init__(self, inherit: str, emptyListDefault: str, aadl2_Property: "aadl2_PropertyAssociation" = None, aadl2_Property20: "aadl2_PropertyExpression" = None, aadl2_Property22: set["aadl2_MetaclassReference"] = None, aadl2_Property24: set["aadl2_Classifier"] = None, aadl2_Property27: set["aadl2_PropertyOwner"] = None, aadl2_Property776: "aadl2_PropertySet" = None, aadl2_Property852: "aadl2_PropertyReference" = None):
        self.inherit = inherit
        self.emptyListDefault = emptyListDefault
        self.aadl2_Property = aadl2_Property
        self.aadl2_Property20 = aadl2_Property20
        self.aadl2_Property22 = aadl2_Property22 if aadl2_Property22 is not None else set()
        self.aadl2_Property24 = aadl2_Property24 if aadl2_Property24 is not None else set()
        self.aadl2_Property27 = aadl2_Property27 if aadl2_Property27 is not None else set()
        self.aadl2_Property776 = aadl2_Property776
        self.aadl2_Property852 = aadl2_Property852
        
    @property
    def inherit(self) -> str:
        return self.__inherit

    @inherit.setter
    def inherit(self, inherit: str):
        self.__inherit = inherit

    @property
    def emptyListDefault(self) -> str:
        return self.__emptyListDefault

    @emptyListDefault.setter
    def emptyListDefault(self, emptyListDefault: str):
        self.__emptyListDefault = emptyListDefault

    @property
    def aadl2_Property22(self):
        return self.__aadl2_Property22

    @aadl2_Property22.setter
    def aadl2_Property22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Property__aadl2_Property22", None)
        self.__aadl2_Property22 = value if value is not None else set()
        
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
    def aadl2_Property776(self):
        return self.__aadl2_Property776

    @aadl2_Property776.setter
    def aadl2_Property776(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Property__aadl2_Property776", None)
        self.__aadl2_Property776 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PropertySet775"):
                opp_val = getattr(old_value, "aadl2_PropertySet775", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PropertySet775"):
                opp_val = getattr(value, "aadl2_PropertySet775", None)
                if opp_val is None:
                    setattr(value, "aadl2_PropertySet775", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_Property27(self):
        return self.__aadl2_Property27

    @aadl2_Property27.setter
    def aadl2_Property27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Property__aadl2_Property27", None)
        self.__aadl2_Property27 = value if value is not None else set()
        
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
    def aadl2_Property20(self):
        return self.__aadl2_Property20

    @aadl2_Property20.setter
    def aadl2_Property20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Property__aadl2_Property20", None)
        self.__aadl2_Property20 = value
        
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
    def aadl2_Property852(self):
        return self.__aadl2_Property852

    @aadl2_Property852.setter
    def aadl2_Property852(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Property__aadl2_Property852", None)
        self.__aadl2_Property852 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_PropertyReference"):
                opp_val = getattr(old_value, "aadl2_PropertyReference", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_PropertyReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PropertyReference"):
                opp_val = getattr(value, "aadl2_PropertyReference", None)
                setattr(value, "aadl2_PropertyReference", self)

    @property
    def aadl2_Property24(self):
        return self.__aadl2_Property24

    @aadl2_Property24.setter
    def aadl2_Property24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Property__aadl2_Property24", None)
        self.__aadl2_Property24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_Classifier25"):
                    opp_val = getattr(item, "aadl2_Classifier25", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_Classifier25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_Classifier25"):
                    opp_val = getattr(item, "aadl2_Classifier25", None)
                    
                    setattr(item, "aadl2_Classifier25", self)
                    

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
            if hasattr(old_value, "aadl2_PropertyAssociation12"):
                opp_val = getattr(old_value, "aadl2_PropertyAssociation12", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_PropertyAssociation12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PropertyAssociation12"):
                opp_val = getattr(value, "aadl2_PropertyAssociation12", None)
                setattr(value, "aadl2_PropertyAssociation12", self)

class NamedElement:

    pass
class aadl2_Abstract(NamedElement):

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

class aadl2_EnumerationLiteral(NamedElement):

    pass
class aadl2_ThreadGroup(NamedElement):

    pass
class aadl2_ModalElement(NamedElement):

    def __init__(self, modesAndTransitions: str, aadl2_ModalElement: set["aadl2_Mode"] = None):
        self.modesAndTransitions = modesAndTransitions
        self.aadl2_ModalElement = aadl2_ModalElement if aadl2_ModalElement is not None else set()
        
    @property
    def modesAndTransitions(self) -> str:
        return self.__modesAndTransitions

    @modesAndTransitions.setter
    def modesAndTransitions(self, modesAndTransitions: str):
        self.__modesAndTransitions = modesAndTransitions

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
                    

class aadl2_AnnexLibrary(NamedElement):

    pass
class aadl2_TypedElement(NamedElement):

    pass
class aadl2_Device(NamedElement):

    pass
class aadl2_Bus(NamedElement):

    pass
class aadl2_Process(NamedElement):

    pass
class aadl2_RefinableElement(NamedElement):

    pass
class aadl2_PackageRename(NamedElement):

    def __init__(self, renameAll: str, aadl2_PackageRename: "aadl2_PackageSection" = None, aadl2_PackageRename384: "aadl2_AadlPackage" = None):
        self.renameAll = renameAll
        self.aadl2_PackageRename = aadl2_PackageRename
        self.aadl2_PackageRename384 = aadl2_PackageRename384
        
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
    def aadl2_PackageRename384(self):
        return self.__aadl2_PackageRename384

    @aadl2_PackageRename384.setter
    def aadl2_PackageRename384(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PackageRename__aadl2_PackageRename384", None)
        self.__aadl2_PackageRename384 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_AadlPackage385"):
                opp_val = getattr(old_value, "aadl2_AadlPackage385", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_AadlPackage385", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_AadlPackage385"):
                opp_val = getattr(value, "aadl2_AadlPackage385", None)
                setattr(value, "aadl2_AadlPackage385", self)

class aadl2_ComponentTypeRename(NamedElement):

    def __init__(self, category: str, aadl2_ComponentTypeRename: "aadl2_PackageSection" = None, aadl2_ComponentTypeRename398: "aadl2_ComponentType" = None):
        self.category = category
        self.aadl2_ComponentTypeRename = aadl2_ComponentTypeRename
        self.aadl2_ComponentTypeRename398 = aadl2_ComponentTypeRename398
        
    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def aadl2_ComponentTypeRename398(self):
        return self.__aadl2_ComponentTypeRename398

    @aadl2_ComponentTypeRename398.setter
    def aadl2_ComponentTypeRename398(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ComponentTypeRename__aadl2_ComponentTypeRename398", None)
        self.__aadl2_ComponentTypeRename398 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ComponentType399"):
                opp_val = getattr(old_value, "aadl2_ComponentType399", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ComponentType399", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ComponentType399"):
                opp_val = getattr(value, "aadl2_ComponentType399", None)
                setattr(value, "aadl2_ComponentType399", self)

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
            if hasattr(old_value, "aadl2_PackageSection312"):
                opp_val = getattr(old_value, "aadl2_PackageSection312", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_PackageSection312"):
                opp_val = getattr(value, "aadl2_PackageSection312", None)
                if opp_val is None:
                    setattr(value, "aadl2_PackageSection312", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aadl2_AadlPackage(NamedElement):

    pass
class aadl2_Thread(NamedElement):

    pass
class aadl2_Processor(NamedElement):

    pass
class aadl2_Subprogram(CalledSubprogram, NamedElement):

    pass
class aadl2_SubprogramGroup(NamedElement):

    pass
class aadl2_VirtualBus(NamedElement):

    pass
class aadl2_FeatureGroupTypeRename(NamedElement):

    pass
class aadl2_ClassifierFeature(NamedElement):

    pass
class aadl2_System(NamedElement):

    pass
class aadl2_EndToEndFlowElement(NamedElement):

    pass
class aadl2_Context(NamedElement):

    pass
class aadl2_VirtualProcessor(NamedElement):

    pass
class aadl2_Data(NamedElement):

    pass
class aadl2_ConnectionEnd(NamedElement):

    pass
class aadl2_Memory(NamedElement):

    pass
class aadl2_Namespace(NamedElement):

    def __init__(self, namespace: set["aadl2_NamedElement"] = None, aadl2_Namespace: set["aadl2_NamedElement"] = None, Namespace: "aadl2_NamedElement" = None):
        self.namespace = namespace if namespace is not None else set()
        self.aadl2_Namespace = aadl2_Namespace if aadl2_Namespace is not None else set()
        self.Namespace = Namespace
        
    @property
    def Namespace(self):
        return self.__Namespace

    @Namespace.setter
    def Namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Namespace__Namespace", None)
        self.__Namespace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedMember"):
                opp_val = getattr(old_value, "ownedMember", None)
                if opp_val == self:
                    setattr(old_value, "ownedMember", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedMember"):
                opp_val = getattr(value, "ownedMember", None)
                setattr(value, "ownedMember", self)

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
                if hasattr(item, "aadl2_NamedElement"):
                    opp_val = getattr(item, "aadl2_NamedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_NamedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_NamedElement"):
                    opp_val = getattr(item, "aadl2_NamedElement", None)
                    
                    setattr(item, "aadl2_NamedElement", self)
                    

    @property
    def namespace(self):
        return self.__namespace

    @namespace.setter
    def namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Namespace__namespace", None)
        self.__namespace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NamedElement"):
                    opp_val = getattr(item, "NamedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "NamedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NamedElement"):
                    opp_val = getattr(item, "NamedElement", None)
                    
                    setattr(item, "NamedElement", self)
                    

    def membersAreDistinguishable(self) -> str:
        # TODO: Implement membersAreDistinguishable method
        pass

    def members_distinguishable(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement members_distinguishable method
        pass

    def getNamesOfMember(self, element: NamedElement) -> str:
        # TODO: Implement getNamesOfMember method
        pass

class Element:

    pass
class aadl2_ArraySize(Element):

    pass
class aadl2_CalledSubprogram(Element):

    pass
class aadl2_ComponentPrototypeActual(Element):

    def __init__(self, category: str, aadl2_ComponentPrototypeActual: "aadl2_ComponentPrototypeBinding" = None):
        self.category = category
        self.aadl2_ComponentPrototypeActual = aadl2_ComponentPrototypeActual
        
    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

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

class aadl2_PropertyAssociation(Element):

    def __init__(self, append: str, constant: str, aadl2_PropertyAssociation: "aadl2_NamedElement" = None, aadl2_PropertyAssociation12: "aadl2_Property" = None, aadl2_PropertyAssociation14: set["aadl2_ContainedNamedElement"] = None, aadl2_PropertyAssociation16: set["aadl2_Classifier"] = None, aadl2_PropertyAssociation18: set["aadl2_ModalPropertyValue"] = None):
        self.append = append
        self.constant = constant
        self.aadl2_PropertyAssociation = aadl2_PropertyAssociation
        self.aadl2_PropertyAssociation12 = aadl2_PropertyAssociation12
        self.aadl2_PropertyAssociation14 = aadl2_PropertyAssociation14 if aadl2_PropertyAssociation14 is not None else set()
        self.aadl2_PropertyAssociation16 = aadl2_PropertyAssociation16 if aadl2_PropertyAssociation16 is not None else set()
        self.aadl2_PropertyAssociation18 = aadl2_PropertyAssociation18 if aadl2_PropertyAssociation18 is not None else set()
        
    @property
    def append(self) -> str:
        return self.__append

    @append.setter
    def append(self, append: str):
        self.__append = append

    @property
    def constant(self) -> str:
        return self.__constant

    @constant.setter
    def constant(self, constant: str):
        self.__constant = constant

    @property
    def aadl2_PropertyAssociation16(self):
        return self.__aadl2_PropertyAssociation16

    @aadl2_PropertyAssociation16.setter
    def aadl2_PropertyAssociation16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertyAssociation__aadl2_PropertyAssociation16", None)
        self.__aadl2_PropertyAssociation16 = value if value is not None else set()
        
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
    def aadl2_PropertyAssociation18(self):
        return self.__aadl2_PropertyAssociation18

    @aadl2_PropertyAssociation18.setter
    def aadl2_PropertyAssociation18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertyAssociation__aadl2_PropertyAssociation18", None)
        self.__aadl2_PropertyAssociation18 = value if value is not None else set()
        
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
    def aadl2_PropertyAssociation(self):
        return self.__aadl2_PropertyAssociation

    @aadl2_PropertyAssociation.setter
    def aadl2_PropertyAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertyAssociation__aadl2_PropertyAssociation", None)
        self.__aadl2_PropertyAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_NamedElement10"):
                opp_val = getattr(old_value, "aadl2_NamedElement10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_NamedElement10"):
                opp_val = getattr(value, "aadl2_NamedElement10", None)
                if opp_val is None:
                    setattr(value, "aadl2_NamedElement10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_PropertyAssociation12(self):
        return self.__aadl2_PropertyAssociation12

    @aadl2_PropertyAssociation12.setter
    def aadl2_PropertyAssociation12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertyAssociation__aadl2_PropertyAssociation12", None)
        self.__aadl2_PropertyAssociation12 = value
        
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
    def aadl2_PropertyAssociation14(self):
        return self.__aadl2_PropertyAssociation14

    @aadl2_PropertyAssociation14.setter
    def aadl2_PropertyAssociation14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_PropertyAssociation__aadl2_PropertyAssociation14", None)
        self.__aadl2_PropertyAssociation14 = value if value is not None else set()
        
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
                    

class aadl2_ModeBinding(Element):

    pass
class aadl2_PropertyOwner(Element):

    pass
class aadl2_BasicPropertyAssociation(Element):

    pass
class aadl2_CallContext(Element):

    pass
class aadl2_ContainmentPathElement(Element):

    pass
class aadl2_ModeTransitionTrigger(Element):

    pass
class aadl2_FeaturePrototypeActual(Element):

    pass
class aadl2_ArraySpecification(Element):

    def __init__(self, dimension: str, aadl2_ArraySpecification: set["aadl2_ArraySize"] = None, aadl2_ArraySpecification80: "aadl2_ArrayableElement" = None):
        self.dimension = dimension
        self.aadl2_ArraySpecification = aadl2_ArraySpecification if aadl2_ArraySpecification is not None else set()
        self.aadl2_ArraySpecification80 = aadl2_ArraySpecification80
        
    @property
    def dimension(self) -> str:
        return self.__dimension

    @dimension.setter
    def dimension(self, dimension: str):
        self.__dimension = dimension

    @property
    def aadl2_ArraySpecification80(self):
        return self.__aadl2_ArraySpecification80

    @aadl2_ArraySpecification80.setter
    def aadl2_ArraySpecification80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ArraySpecification__aadl2_ArraySpecification80", None)
        self.__aadl2_ArraySpecification80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ArrayableElement"):
                opp_val = getattr(old_value, "aadl2_ArrayableElement", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ArrayableElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ArrayableElement"):
                opp_val = getattr(value, "aadl2_ArrayableElement", None)
                setattr(value, "aadl2_ArrayableElement", self)

    @property
    def aadl2_ArraySpecification(self):
        return self.__aadl2_ArraySpecification

    @aadl2_ArraySpecification.setter
    def aadl2_ArraySpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_ArraySpecification__aadl2_ArraySpecification", None)
        self.__aadl2_ArraySpecification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aadl2_ArraySize"):
                    opp_val = getattr(item, "aadl2_ArraySize", None)
                    
                    if opp_val == self:
                        setattr(item, "aadl2_ArraySize", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aadl2_ArraySize"):
                    opp_val = getattr(item, "aadl2_ArraySize", None)
                    
                    setattr(item, "aadl2_ArraySize", self)
                    

class aadl2_NumericRange(Element):

    pass
class aadl2_ContainedNamedElement(Element):

    pass
class aadl2_PrototypeBinding(Element):

    pass
class aadl2_ComponentImplementationReference(Element):

    pass
class aadl2_Relationship(Element):

    pass
class aadl2_ArrayableElement(Element):

    pass
class aadl2_FeatureGroupPrototypeActual(Element):

    pass
class aadl2_NamedElement(Element):

    def __init__(self, name: str, qualifiedName: str, NamedElement: "aadl2_Namespace" = None, aadl2_NamedElement: "aadl2_Namespace" = None, ownedMember: "aadl2_Namespace" = None, aadl2_NamedElement10: set["aadl2_PropertyAssociation"] = None, aadl2_NamedElement33: "aadl2_Classifier" = None, aadl2_NamedElement74: "aadl2_ContainmentPathElement" = None):
        self.name = name
        self.qualifiedName = qualifiedName
        self.NamedElement = NamedElement
        self.aadl2_NamedElement = aadl2_NamedElement
        self.ownedMember = ownedMember
        self.aadl2_NamedElement10 = aadl2_NamedElement10 if aadl2_NamedElement10 is not None else set()
        self.aadl2_NamedElement33 = aadl2_NamedElement33
        self.aadl2_NamedElement74 = aadl2_NamedElement74
        
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
    def aadl2_NamedElement10(self):
        return self.__aadl2_NamedElement10

    @aadl2_NamedElement10.setter
    def aadl2_NamedElement10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_NamedElement__aadl2_NamedElement10", None)
        self.__aadl2_NamedElement10 = value if value is not None else set()
        
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
    def NamedElement(self):
        return self.__NamedElement

    @NamedElement.setter
    def NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_NamedElement__NamedElement", None)
        self.__NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "namespace"):
                opp_val = getattr(old_value, "namespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "namespace"):
                opp_val = getattr(value, "namespace", None)
                if opp_val is None:
                    setattr(value, "namespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedMember(self):
        return self.__ownedMember

    @ownedMember.setter
    def ownedMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_NamedElement__ownedMember", None)
        self.__ownedMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace"):
                opp_val = getattr(old_value, "Namespace", None)
                if opp_val == self:
                    setattr(old_value, "Namespace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace"):
                opp_val = getattr(value, "Namespace", None)
                setattr(value, "Namespace", self)

    @property
    def aadl2_NamedElement(self):
        return self.__aadl2_NamedElement

    @aadl2_NamedElement.setter
    def aadl2_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_NamedElement__aadl2_NamedElement", None)
        self.__aadl2_NamedElement = value
        
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
    def aadl2_NamedElement74(self):
        return self.__aadl2_NamedElement74

    @aadl2_NamedElement74.setter
    def aadl2_NamedElement74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_NamedElement__aadl2_NamedElement74", None)
        self.__aadl2_NamedElement74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_ContainmentPathElement73"):
                opp_val = getattr(old_value, "aadl2_ContainmentPathElement73", None)
                if opp_val == self:
                    setattr(old_value, "aadl2_ContainmentPathElement73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ContainmentPathElement73"):
                opp_val = getattr(value, "aadl2_ContainmentPathElement73", None)
                setattr(value, "aadl2_ContainmentPathElement73", self)

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

    def separator(self) -> str:
        # TODO: Implement separator method
        pass

    def has_no_qualified_name(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement has_no_qualified_name method
        pass

    def isDistinguishableFrom(self, n: NamedElement, ns: str) -> str:
        # TODO: Implement isDistinguishableFrom method
        pass

    def has_qualified_name(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement has_qualified_name method
        pass

    def allNamespaces(self) -> str:
        # TODO: Implement allNamespaces method
        pass

    def qualifiedName(self) -> str:
        # TODO: Implement qualifiedName method
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
            if hasattr(old_value, "aadl2_ContainmentPathElement71"):
                opp_val = getattr(old_value, "aadl2_ContainmentPathElement71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_ContainmentPathElement71"):
                opp_val = getattr(value, "aadl2_ContainmentPathElement71", None)
                if opp_val is None:
                    setattr(value, "aadl2_ContainmentPathElement71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aadl2_PropertyExpression(Element):

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
            if hasattr(old_value, "aadl2_Element"):
                opp_val = getattr(old_value, "aadl2_Element", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_Element"):
                opp_val = getattr(value, "aadl2_Element", None)
                if opp_val is None:
                    setattr(value, "aadl2_Element", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aadl2_Element(ABC):

    def __init__(self, Element: "aadl2_Element" = None, owner: set["aadl2_Element"] = None, Element4: "aadl2_Element" = None, ownedElement: "aadl2_Element" = None, aadl2_Element: set["aadl2_Comment"] = None, aadl2_Element50: "aadl2_DirectedRelationship" = None, aadl2_Element53: "aadl2_DirectedRelationship" = None, aadl2_Element55: "aadl2_Relationship" = None):
        self.Element = Element
        self.owner = owner if owner is not None else set()
        self.Element4 = Element4
        self.ownedElement = ownedElement
        self.aadl2_Element = aadl2_Element if aadl2_Element is not None else set()
        self.aadl2_Element50 = aadl2_Element50
        self.aadl2_Element53 = aadl2_Element53
        self.aadl2_Element55 = aadl2_Element55
        
    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Element__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    if opp_val == self:
                        setattr(item, "Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    setattr(item, "Element", self)
                    

    @property
    def aadl2_Element(self):
        return self.__aadl2_Element

    @aadl2_Element.setter
    def aadl2_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Element__aadl2_Element", None)
        self.__aadl2_Element = value if value is not None else set()
        
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
    def aadl2_Element53(self):
        return self.__aadl2_Element53

    @aadl2_Element53.setter
    def aadl2_Element53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Element__aadl2_Element53", None)
        self.__aadl2_Element53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aadl2_DirectedRelationship52"):
                opp_val = getattr(old_value, "aadl2_DirectedRelationship52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aadl2_DirectedRelationship52"):
                opp_val = getattr(value, "aadl2_DirectedRelationship52", None)
                if opp_val is None:
                    setattr(value, "aadl2_DirectedRelationship52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aadl2_Element50(self):
        return self.__aadl2_Element50

    @aadl2_Element50.setter
    def aadl2_Element50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Element__aadl2_Element50", None)
        self.__aadl2_Element50 = value
        
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
    def aadl2_Element55(self):
        return self.__aadl2_Element55

    @aadl2_Element55.setter
    def aadl2_Element55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Element__aadl2_Element55", None)
        self.__aadl2_Element55 = value
        
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
    def Element4(self):
        return self.__Element4

    @Element4.setter
    def Element4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Element__Element4", None)
        self.__Element4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedElement"):
                opp_val = getattr(old_value, "ownedElement", None)
                if opp_val == self:
                    setattr(old_value, "ownedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedElement"):
                opp_val = getattr(value, "ownedElement", None)
                setattr(value, "ownedElement", self)

    @property
    def Element(self):
        return self.__Element

    @Element.setter
    def Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Element__Element", None)
        self.__Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedElement(self):
        return self.__ownedElement

    @ownedElement.setter
    def ownedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aadl2_Element__ownedElement", None)
        self.__ownedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element4"):
                opp_val = getattr(old_value, "Element4", None)
                if opp_val == self:
                    setattr(old_value, "Element4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element4"):
                opp_val = getattr(value, "Element4", None)
                setattr(value, "Element4", self)

    def mustBeOwned(self) -> str:
        # TODO: Implement mustBeOwned method
        pass

    def not_own_self(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement not_own_self method
        pass

    def has_owner(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement has_owner method
        pass

    def allOwnedElements(self) -> str:
        # TODO: Implement allOwnedElements method
        pass
