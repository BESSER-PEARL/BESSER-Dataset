from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AttributeTypesE(Enum):
    STRING = "STRING"
    NUMERIC = "NUMERIC"
    BOOL = "BOOL"
class EndianessE(Enum):
    BIG = "BIG"
    LITTLE = "LITTLE"
class AttributeTargetsE(Enum):
    DEVICE_TYPE = "DEVICE_TYPE"
    DEVICE = "DEVICE"
    TASK_TYPE = "TASK_TYPE"
    TASK = "TASK"
    CONNECTION_TYPE = "CONNECTION_TYPE"
    CONNECTION = "CONNECTION"
    LOCATION_TYPE = "LOCATION_TYPE"
    LOCATION = "LOCATION"
    WIRE_TYPE = "WIRE_TYPE"
    DUCT_TYPE = "DUCT_TYPE"
    RESOURCE_TYPE = "RESOURCE_TYPE"
    RESOURCE = "RESOURCE"
    SIGNAL_TYPE = "SIGNAL_TYPE"
    SIGNAL = "SIGNAL"
    DUCT = "DUCT"
    RESOURCE_BUNDLE = "RESOURCE_BUNDLE"
    RESOURCE_ALTERNATIVE = "RESOURCE_ALTERNATIVE"
    RESOURCE_GROUP = "RESOURCE_GROUP"
    AREA = "AREA"
    VARIANT = "VARIANT"
class IntegretyStateE(Enum):
    FAILED = "FAILED"
    UNKNOWN = "UNKNOWN"
    OK = "OK"
class IoDirectionE(Enum):
    NONE = "NONE"
    IN = "IN"
    OUT = "OUT"
    BOTH = "BOTH"
class BoolOperationTypesE(Enum):
    AND = "AND"
    OR = "OR"
    XOR = "XOR"
class SymmetryTypesE(Enum):
    LOCATION = "LOCATION"
    DEVICE = "DEVICE"
    AREA = "AREA"
    DEVICE_TYPE = "DEVICE_TYPE"


############################################
# Definition of Classes
############################################

class allocations_AllocationsContainerA:

    pass
class AllocationsContainerA:

    pass
class oaam_allocations_Allocations(AllocationsContainerA):

    pass
class oaam_allocations_SignalToMessageAssignment:

    def __init__(self, position: int, oaam_allocations_SignalToMessageAssignment730: set["OperationModeReference"] = None, oaam_allocations_SignalToMessageAssignment733: "DataTypeA" = None, oaam_allocations_SignalToMessageAssignment: "Signal" = None, oaam_allocations_SignalToMessageAssignment724: set["AttributeA"] = None, oaam_allocations_SignalToMessageAssignment727: set["Variant"] = None, oaam_allocations_SignalToMessageAssignment736: "SignalInMessageCapability" = None):
        self.position = position
        self.oaam_allocations_SignalToMessageAssignment730 = oaam_allocations_SignalToMessageAssignment730 if oaam_allocations_SignalToMessageAssignment730 is not None else set()
        self.oaam_allocations_SignalToMessageAssignment733 = oaam_allocations_SignalToMessageAssignment733
        self.oaam_allocations_SignalToMessageAssignment = oaam_allocations_SignalToMessageAssignment
        self.oaam_allocations_SignalToMessageAssignment724 = oaam_allocations_SignalToMessageAssignment724 if oaam_allocations_SignalToMessageAssignment724 is not None else set()
        self.oaam_allocations_SignalToMessageAssignment727 = oaam_allocations_SignalToMessageAssignment727 if oaam_allocations_SignalToMessageAssignment727 is not None else set()
        self.oaam_allocations_SignalToMessageAssignment736 = oaam_allocations_SignalToMessageAssignment736
        
    @property
    def position(self) -> int:
        return self.__position

    @position.setter
    def position(self, position: int):
        self.__position = position

    @property
    def oaam_allocations_SignalToMessageAssignment724(self):
        return self.__oaam_allocations_SignalToMessageAssignment724

    @oaam_allocations_SignalToMessageAssignment724.setter
    def oaam_allocations_SignalToMessageAssignment724(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_allocations_SignalToMessageAssignment__oaam_allocations_SignalToMessageAssignment724", None)
        self.__oaam_allocations_SignalToMessageAssignment724 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AttributeA725"):
                    opp_val = getattr(item, "AttributeA725", None)
                    
                    if opp_val == self:
                        setattr(item, "AttributeA725", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AttributeA725"):
                    opp_val = getattr(item, "AttributeA725", None)
                    
                    setattr(item, "AttributeA725", self)
                    

    @property
    def oaam_allocations_SignalToMessageAssignment730(self):
        return self.__oaam_allocations_SignalToMessageAssignment730

    @oaam_allocations_SignalToMessageAssignment730.setter
    def oaam_allocations_SignalToMessageAssignment730(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_allocations_SignalToMessageAssignment__oaam_allocations_SignalToMessageAssignment730", None)
        self.__oaam_allocations_SignalToMessageAssignment730 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OperationModeReference731"):
                    opp_val = getattr(item, "OperationModeReference731", None)
                    
                    if opp_val == self:
                        setattr(item, "OperationModeReference731", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OperationModeReference731"):
                    opp_val = getattr(item, "OperationModeReference731", None)
                    
                    setattr(item, "OperationModeReference731", self)
                    

    @property
    def oaam_allocations_SignalToMessageAssignment(self):
        return self.__oaam_allocations_SignalToMessageAssignment

    @oaam_allocations_SignalToMessageAssignment.setter
    def oaam_allocations_SignalToMessageAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_allocations_SignalToMessageAssignment__oaam_allocations_SignalToMessageAssignment", None)
        self.__oaam_allocations_SignalToMessageAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Signal722"):
                opp_val = getattr(old_value, "Signal722", None)
                if opp_val == self:
                    setattr(old_value, "Signal722", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Signal722"):
                opp_val = getattr(value, "Signal722", None)
                setattr(value, "Signal722", self)

    @property
    def oaam_allocations_SignalToMessageAssignment727(self):
        return self.__oaam_allocations_SignalToMessageAssignment727

    @oaam_allocations_SignalToMessageAssignment727.setter
    def oaam_allocations_SignalToMessageAssignment727(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_allocations_SignalToMessageAssignment__oaam_allocations_SignalToMessageAssignment727", None)
        self.__oaam_allocations_SignalToMessageAssignment727 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variant728"):
                    opp_val = getattr(item, "Variant728", None)
                    
                    if opp_val == self:
                        setattr(item, "Variant728", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variant728"):
                    opp_val = getattr(item, "Variant728", None)
                    
                    setattr(item, "Variant728", self)
                    

    @property
    def oaam_allocations_SignalToMessageAssignment733(self):
        return self.__oaam_allocations_SignalToMessageAssignment733

    @oaam_allocations_SignalToMessageAssignment733.setter
    def oaam_allocations_SignalToMessageAssignment733(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_allocations_SignalToMessageAssignment__oaam_allocations_SignalToMessageAssignment733", None)
        self.__oaam_allocations_SignalToMessageAssignment733 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataTypeA734"):
                opp_val = getattr(old_value, "DataTypeA734", None)
                if opp_val == self:
                    setattr(old_value, "DataTypeA734", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataTypeA734"):
                opp_val = getattr(value, "DataTypeA734", None)
                setattr(value, "DataTypeA734", self)

    @property
    def oaam_allocations_SignalToMessageAssignment736(self):
        return self.__oaam_allocations_SignalToMessageAssignment736

    @oaam_allocations_SignalToMessageAssignment736.setter
    def oaam_allocations_SignalToMessageAssignment736(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_allocations_SignalToMessageAssignment__oaam_allocations_SignalToMessageAssignment736", None)
        self.__oaam_allocations_SignalToMessageAssignment736 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SignalInMessageCapability737"):
                opp_val = getattr(old_value, "SignalInMessageCapability737", None)
                if opp_val == self:
                    setattr(old_value, "SignalInMessageCapability737", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SignalInMessageCapability737"):
                opp_val = getattr(value, "SignalInMessageCapability737", None)
                setattr(value, "SignalInMessageCapability737", self)

class MessageA:

    pass
class oaam_allocations_Submessage(MessageA):

    def __init__(self, position: int, oaam_allocations_Submessage: "SubmessageInMessageCapability" = None):
        self.position = position
        self.oaam_allocations_Submessage = oaam_allocations_Submessage
        
    @property
    def position(self) -> int:
        return self.__position

    @position.setter
    def position(self, position: int):
        self.__position = position

    @property
    def oaam_allocations_Submessage(self):
        return self.__oaam_allocations_Submessage

    @oaam_allocations_Submessage.setter
    def oaam_allocations_Submessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_allocations_Submessage__oaam_allocations_Submessage", None)
        self.__oaam_allocations_Submessage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SubmessageInMessageCapability720"):
                opp_val = getattr(old_value, "SubmessageInMessageCapability720", None)
                if opp_val == self:
                    setattr(old_value, "SubmessageInMessageCapability720", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SubmessageInMessageCapability720"):
                opp_val = getattr(value, "SubmessageInMessageCapability720", None)
                setattr(value, "SubmessageInMessageCapability720", self)

class oaam_allocations_Message(MessageA):

    pass
class SignalToMessageAssignment:

    pass
class Submessage:

    pass
class MessageSegment:

    pass
class ScheduledTime:

    pass
class ConnectionAssignmentSegment:

    pass
class SignalAssignmentSegment:

    pass
class Schedule:

    pass
class TaskAssignment:

    pass
class ConnectionAssignment:

    pass
class SubdeviceAssignment:

    pass
class DeviceAssignment:

    pass
class Message:

    pass
class SubconnectionAssignment:

    pass
class Suballocations:

    pass
class SignalAssignment:

    pass
class restrictions_RestrictionsContainerA:

    pass
class restrictions_ConnectionRestrinctionA:

    pass
class restrictions_DeviceRestrictionA:

    pass
class restrictions_SubfunctionRestrictionA:

    pass
class restrictions_SignalGroupRestrictionA:

    pass
class restrictions_SignalRestrictionA:

    pass
class restrictions_TaskGroupRestrictionA:

    pass
class restrictions_TaskRestrictionA:

    pass
class oaam_restrictions_SignalGroupRestrictionA(ABC):

    pass
class oaam_restrictions_SubfunctionRestrictionA(ABC):

    pass
class oaam_restrictions_SignalRestrictionA(ABC):

    pass
class oaam_restrictions_TaskRestrictionA(ABC):

    pass
class oaam_restrictions_TaskGroupRestrictionA(ABC):

    pass
class oaam_restrictions_DeviceRestrictionA(ABC):

    pass
class RestrictionsContainerA:

    pass
class oaam_restrictions_Restrictions(RestrictionsContainerA):

    pass
class TimeDelayRestriction:

    pass
class oaam_restrictions_ConnectionRestrinctionA(ABC):

    pass
class ConnectionTypeRestriction:

    pass
class ConnectionRestriction:

    pass
class SynchronicityRestriction:

    pass
class TaskSymmetryRestriction:

    pass
class Subrestrictions:

    pass
class SegregationRestriction:

    pass
class LocationRestriction:

    pass
class DeviceRestriction:

    pass
class DeviceTypeRestriction:

    pass
class TaskAtomicRestriction:

    pass
class PowerSourceRestriction:

    pass
class AreaRestriction:

    pass
class capabilities_CapabilitiesContainerA:

    pass
class CapabilitiesContainerA:

    pass
class oaam_capabilities_Capabilities(CapabilitiesContainerA):

    pass
class SignalInMessageCapability:

    pass
class SubmessageInMessageCapability:

    pass
class MessageOnBusCapability:

    pass
class SubconnectionInDeviceCapability:

    pass
class capabilities_CapabilityA:

    pass
class MessageOnConnectionOrDeviceCapability:

    pass
class SubdeviceInDeviceCapability:

    pass
class DeviceInLocationCapability:

    pass
class SignalOnConnectionOrDeviceCapability:

    pass
class Subcapabilities:

    pass
class ConnectionInDuctOrLocationCapability:

    pass
class ResourceConsumption:

    pass
class oaam_capabilities_CapabilityA(ABC):

    pass
class AnatomyContainerA:

    pass
class oaam_anatomy_Anatomy(AnatomyContainerA):

    pass
class anatomy_AnatomyContainerA:

    pass
class TaskOnDeviceCapability:

    pass
class Position3D:

    pass
class DuctOpening:

    pass
class Subanatomy:

    pass
class Area:

    pass
class Duct:

    pass
class LocationSymmetry:

    pass
class AreaSymmetry:

    pass
class hardware_HardwareContainerA:

    pass
class library_ResourceProviderInstanceA:

    pass
class Bus:

    pass
class Location:

    pass
class DeviceSymmetry:

    pass
class Subhardware:

    pass
class ExternalOutputLink:

    pass
class Io:

    pass
class Connection:

    pass
class OutputIntegrityState:

    pass
class TaskParameter:

    pass
class Device:

    pass
class Input:

    pass
class Output:

    pass
class SignalGroup:

    pass
class Signal:

    pass
class TaskRedundancy:

    pass
class TaskSymmetry:

    pass
class Subfunctions:

    pass
class FailureCondition:

    pass
class Task:

    pass
class FunctionsContainerA:

    pass
class oaam_functions_Subfunctions(FunctionsContainerA):

    def __init__(self, multiplicityMin: int, multiplicityMax: int, FunctionsContainerA576: "oaam_restrictions_SegregationRestriction", FunctionsContainerA: "oaam_restrictions_SegregationRestriction"):
        self.multiplicityMin = multiplicityMin
        self.multiplicityMax = multiplicityMax
        
    @property
    def multiplicityMin(self) -> int:
        return self.__multiplicityMin

    @multiplicityMin.setter
    def multiplicityMin(self, multiplicityMin: int):
        self.__multiplicityMin = multiplicityMin

    @property
    def multiplicityMax(self) -> int:
        return self.__multiplicityMax

    @multiplicityMax.setter
    def multiplicityMax(self, multiplicityMax: int):
        self.__multiplicityMax = multiplicityMax

class oaam_functions_Functions(FunctionsContainerA):

    pass
class TaskGroup:

    pass
class ExternalTaskLink:

    pass
class InformationPower:

    pass
class oaam_systems_LinearPower(InformationPower):

    def __init__(self, force: float, velocity: float):
        self.force = force
        self.velocity = velocity
        
    @property
    def force(self) -> float:
        return self.__force

    @force.setter
    def force(self, force: float):
        self.__force = force

    @property
    def velocity(self) -> float:
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity: float):
        self.__velocity = velocity

class oaam_systems_RotaryPower(InformationPower):

    def __init__(self, momentum: float, angularVelocity: float):
        self.momentum = momentum
        self.angularVelocity = angularVelocity
        
    @property
    def angularVelocity(self) -> float:
        return self.__angularVelocity

    @angularVelocity.setter
    def angularVelocity(self, angularVelocity: float):
        self.__angularVelocity = angularVelocity

    @property
    def momentum(self) -> float:
        return self.__momentum

    @momentum.setter
    def momentum(self, momentum: float):
        self.__momentum = momentum

class oaam_systems_ElectricPower(InformationPower):

    def __init__(self, current: float, frequency: float, nPhases: int, voltage: float):
        self.current = current
        self.frequency = frequency
        self.nPhases = nPhases
        self.voltage = voltage
        
    @property
    def current(self) -> float:
        return self.__current

    @current.setter
    def current(self, current: float):
        self.__current = current

    @property
    def voltage(self) -> float:
        return self.__voltage

    @voltage.setter
    def voltage(self, voltage: float):
        self.__voltage = voltage

    @property
    def frequency(self) -> float:
        return self.__frequency

    @frequency.setter
    def frequency(self, frequency: float):
        self.__frequency = frequency

    @property
    def nPhases(self) -> int:
        return self.__nPhases

    @nPhases.setter
    def nPhases(self, nPhases: int):
        self.__nPhases = nPhases

class oaam_systems_HydraulicPower(InformationPower):

    def __init__(self, pressure: float, massFlowRate: float):
        self.pressure = pressure
        self.massFlowRate = massFlowRate
        
    @property
    def massFlowRate(self) -> float:
        return self.__massFlowRate

    @massFlowRate.setter
    def massFlowRate(self, massFlowRate: float):
        self.__massFlowRate = massFlowRate

    @property
    def pressure(self) -> float:
        return self.__pressure

    @pressure.setter
    def pressure(self, pressure: float):
        self.__pressure = pressure

class systems_RequiredInformationA:

    pass
class systems_ProvidedInformationA:

    pass
class oaam_systems_ProvidedInformationA(ABC):

    pass
class oaam_systems_RequiredInformationA(ABC):

    pass
class RequiredInformationA:

    pass
class ProvidedInformationA:

    pass
class Subsystem:

    pass
class InputSegregation:

    pass
class InformationFlow:

    pass
class System:

    pass
class systems_SystemsContainerA:

    pass
class SystemsContainerA:

    pass
class oaam_systems_Systems(SystemsContainerA):

    pass
class ScenarioContainerA:

    pass
class oaam_scenario_Subscenario(ScenarioContainerA):

    pass
class oaam_scenario_Scenario(ScenarioContainerA):

    pass
class Subscenario:

    pass
class OperationMode:

    pass
class ScenarioParameterA:

    pass
class scenario_ScenarioParameterA:

    pass
class OperationModeReference:

    pass
class oaam_scenario_ModeDependentElementA(ABC):

    pass
class scenario_VariantDependentElementA:

    pass
class scenario_ModeDependentElementA:

    pass
class oaam_systems_Subsystem(scenario_VariantDependentElementA, systems_SystemsContainerA, scenario_ModeDependentElementA):

    pass
class oaam_hardware_Subhardware(scenario_VariantDependentElementA, scenario_ModeDependentElementA, hardware_HardwareContainerA):

    pass
class oaam_capabilities_Subcapabilities(scenario_VariantDependentElementA, capabilities_CapabilitiesContainerA, scenario_ModeDependentElementA):

    pass
class oaam_allocations_Suballocations(scenario_VariantDependentElementA, scenario_ModeDependentElementA, allocations_AllocationsContainerA):

    pass
class oaam_anatomy_Subanatomy(anatomy_AnatomyContainerA, scenario_VariantDependentElementA, scenario_ModeDependentElementA):

    pass
class oaam_hardware_Hardware(scenario_VariantDependentElementA, hardware_HardwareContainerA, scenario_ModeDependentElementA):

    pass
class oaam_restrictions_Subrestrictions(scenario_VariantDependentElementA, restrictions_RestrictionsContainerA, scenario_ModeDependentElementA):

    pass
class oaam_scenario_ScenarioParameterA(scenario_VariantDependentElementA, scenario_ModeDependentElementA):

    pass
class Variant:

    pass
class oaam_scenario_VariantDependentElementA(ABC):

    pass
class LibraryContainerA:

    pass
class oaam_library_Sublibrary(LibraryContainerA):

    pass
class oaam_library_Library(LibraryContainerA):

    pass
class TaskInputTrigger:

    pass
class TaskInputState:

    pass
class BoolNot:

    pass
class BoolOperation:

    pass
class FaultPropagation:

    pass
class TaskOutputTrigger:

    pass
class DuctOpeningDeclaration:

    pass
class IoGroup:

    pass
class IoDeclaration:

    pass
class library_ResourceProviderA:

    pass
class TaskParameterDeclaration:

    pass
class InputDeclaration:

    pass
class OutputDeclaration:

    pass
class TaskStateDeclaration:

    pass
class ResourceTypeModifierReference:

    pass
class library_ResourceConsumerA:

    pass
class MessageType:

    pass
class ResourceAlternatives:

    pass
class DeviceTypeSymmetry:

    pass
class Sublibrary:

    pass
class DeviceType:

    pass
class PowerSource:

    pass
class AttributeDefinition:

    pass
class DuctType:

    pass
class LocationType:

    pass
class WireType:

    pass
class ConnectionType:

    pass
class BusType:

    pass
class DeviceTypeDissimilarity:

    pass
class IoType:

    pass
class ResourceTypeModifierLevel:

    pass
class SignalType:

    pass
class TaskTypeDissimilarity:

    pass
class TaskType:

    pass
class ResourceTypeDissimilarity:

    pass
class ResourceTypeModifier:

    pass
class Resource:

    pass
class oaam_library_ResourceConsumerA(ABC):

    pass
class oaam_library_ResourceProviderInstanceA(ABC):

    pass
class ResourceLink:

    pass
class ResourceType:

    pass
class ResourceBundle:

    pass
class oaam_library_ResourceProviderA(ABC):

    pass
class ResourceGroup:

    pass
class Struct:

    pass
class DataTypeA:

    pass
class oaam_common_FloatingPoint(DataTypeA):

    def __init__(self, nBits: int, endianess: str, DataTypeA200: "oaam_library_TaskParameterDeclaration", DataTypeA134: "oaam_library_InputDeclaration", DataTypeA213: "oaam_library_MessageType", DataTypeA: "oaam_common_Array", DataTypeA138: "oaam_library_OutputDeclaration", DataTypeA210: "oaam_library_MessageType", DataTypeA198: "oaam_library_TaskStateDeclaration", DataTypeA48: "oaam_library_LibraryContainerA", DataTypeA734: "oaam_allocations_SignalToMessageAssignment", DataTypeA114: "oaam_library_SignalType", DataTypeA32: "oaam_common_Struct"):
        self.nBits = nBits
        self.endianess = endianess
        
    @property
    def endianess(self) -> str:
        return self.__endianess

    @endianess.setter
    def endianess(self, endianess: str):
        self.__endianess = endianess

    @property
    def nBits(self) -> int:
        return self.__nBits

    @nBits.setter
    def nBits(self, nBits: int):
        self.__nBits = nBits

class oaam_common_Character(DataTypeA):

    def __init__(self, encoding: str, nBits: int, DataTypeA200: "oaam_library_TaskParameterDeclaration", DataTypeA134: "oaam_library_InputDeclaration", DataTypeA213: "oaam_library_MessageType", DataTypeA: "oaam_common_Array", DataTypeA138: "oaam_library_OutputDeclaration", DataTypeA210: "oaam_library_MessageType", DataTypeA198: "oaam_library_TaskStateDeclaration", DataTypeA48: "oaam_library_LibraryContainerA", DataTypeA734: "oaam_allocations_SignalToMessageAssignment", DataTypeA114: "oaam_library_SignalType", DataTypeA32: "oaam_common_Struct"):
        self.encoding = encoding
        self.nBits = nBits
        
    @property
    def nBits(self) -> int:
        return self.__nBits

    @nBits.setter
    def nBits(self, nBits: int):
        self.__nBits = nBits

    @property
    def encoding(self) -> str:
        return self.__encoding

    @encoding.setter
    def encoding(self, encoding: str):
        self.__encoding = encoding

class oaam_common_Struct(DataTypeA):

    def __init__(self, isAbstract: bool, alignment: int, oaam_common_Struct: set["DataTypeA"] = None, oaam_common_Struct34: "Struct" = None, DataTypeA200: "oaam_library_TaskParameterDeclaration", DataTypeA134: "oaam_library_InputDeclaration", DataTypeA213: "oaam_library_MessageType", DataTypeA: "oaam_common_Array", DataTypeA138: "oaam_library_OutputDeclaration", DataTypeA210: "oaam_library_MessageType", DataTypeA198: "oaam_library_TaskStateDeclaration", DataTypeA48: "oaam_library_LibraryContainerA", DataTypeA734: "oaam_allocations_SignalToMessageAssignment", DataTypeA114: "oaam_library_SignalType", DataTypeA32: "oaam_common_Struct"):
        self.isAbstract = isAbstract
        self.alignment = alignment
        self.oaam_common_Struct = oaam_common_Struct if oaam_common_Struct is not None else set()
        self.oaam_common_Struct34 = oaam_common_Struct34
        
    @property
    def alignment(self) -> int:
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: int):
        self.__alignment = alignment

    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def oaam_common_Struct34(self):
        return self.__oaam_common_Struct34

    @oaam_common_Struct34.setter
    def oaam_common_Struct34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_common_Struct__oaam_common_Struct34", None)
        self.__oaam_common_Struct34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Struct"):
                opp_val = getattr(old_value, "Struct", None)
                if opp_val == self:
                    setattr(old_value, "Struct", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Struct"):
                opp_val = getattr(value, "Struct", None)
                setattr(value, "Struct", self)

    @property
    def oaam_common_Struct(self):
        return self.__oaam_common_Struct

    @oaam_common_Struct.setter
    def oaam_common_Struct(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_common_Struct__oaam_common_Struct", None)
        self.__oaam_common_Struct = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataTypeA32"):
                    opp_val = getattr(item, "DataTypeA32", None)
                    
                    if opp_val == self:
                        setattr(item, "DataTypeA32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataTypeA32"):
                    opp_val = getattr(item, "DataTypeA32", None)
                    
                    setattr(item, "DataTypeA32", self)
                    

class oaam_common_Byte(DataTypeA):

    def __init__(self, nBits: int, DataTypeA200: "oaam_library_TaskParameterDeclaration", DataTypeA134: "oaam_library_InputDeclaration", DataTypeA213: "oaam_library_MessageType", DataTypeA: "oaam_common_Array", DataTypeA138: "oaam_library_OutputDeclaration", DataTypeA210: "oaam_library_MessageType", DataTypeA198: "oaam_library_TaskStateDeclaration", DataTypeA48: "oaam_library_LibraryContainerA", DataTypeA734: "oaam_allocations_SignalToMessageAssignment", DataTypeA114: "oaam_library_SignalType", DataTypeA32: "oaam_common_Struct"):
        self.nBits = nBits
        
    @property
    def nBits(self) -> int:
        return self.__nBits

    @nBits.setter
    def nBits(self, nBits: int):
        self.__nBits = nBits

class oaam_common_Boolean(DataTypeA):

    def __init__(self, nBits: int, DataTypeA200: "oaam_library_TaskParameterDeclaration", DataTypeA134: "oaam_library_InputDeclaration", DataTypeA213: "oaam_library_MessageType", DataTypeA: "oaam_common_Array", DataTypeA138: "oaam_library_OutputDeclaration", DataTypeA210: "oaam_library_MessageType", DataTypeA198: "oaam_library_TaskStateDeclaration", DataTypeA48: "oaam_library_LibraryContainerA", DataTypeA734: "oaam_allocations_SignalToMessageAssignment", DataTypeA114: "oaam_library_SignalType", DataTypeA32: "oaam_common_Struct"):
        self.nBits = nBits
        
    @property
    def nBits(self) -> int:
        return self.__nBits

    @nBits.setter
    def nBits(self, nBits: int):
        self.__nBits = nBits

class oaam_common_Integer(DataTypeA):

    def __init__(self, nBits: int, endianess: str, signed: bool, DataTypeA200: "oaam_library_TaskParameterDeclaration", DataTypeA134: "oaam_library_InputDeclaration", DataTypeA213: "oaam_library_MessageType", DataTypeA: "oaam_common_Array", DataTypeA138: "oaam_library_OutputDeclaration", DataTypeA210: "oaam_library_MessageType", DataTypeA198: "oaam_library_TaskStateDeclaration", DataTypeA48: "oaam_library_LibraryContainerA", DataTypeA734: "oaam_allocations_SignalToMessageAssignment", DataTypeA114: "oaam_library_SignalType", DataTypeA32: "oaam_common_Struct"):
        self.nBits = nBits
        self.endianess = endianess
        self.signed = signed
        
    @property
    def nBits(self) -> int:
        return self.__nBits

    @nBits.setter
    def nBits(self, nBits: int):
        self.__nBits = nBits

    @property
    def endianess(self) -> str:
        return self.__endianess

    @endianess.setter
    def endianess(self, endianess: str):
        self.__endianess = endianess

    @property
    def signed(self) -> bool:
        return self.__signed

    @signed.setter
    def signed(self, signed: bool):
        self.__signed = signed

class oaam_common_Array(DataTypeA):

    def __init__(self, nElements: int, alignment: int, oaam_common_Array: "DataTypeA" = None, DataTypeA200: "oaam_library_TaskParameterDeclaration", DataTypeA134: "oaam_library_InputDeclaration", DataTypeA213: "oaam_library_MessageType", DataTypeA: "oaam_common_Array", DataTypeA138: "oaam_library_OutputDeclaration", DataTypeA210: "oaam_library_MessageType", DataTypeA198: "oaam_library_TaskStateDeclaration", DataTypeA48: "oaam_library_LibraryContainerA", DataTypeA734: "oaam_allocations_SignalToMessageAssignment", DataTypeA114: "oaam_library_SignalType", DataTypeA32: "oaam_common_Struct"):
        self.nElements = nElements
        self.alignment = alignment
        self.oaam_common_Array = oaam_common_Array
        
    @property
    def alignment(self) -> int:
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: int):
        self.__alignment = alignment

    @property
    def nElements(self) -> int:
        return self.__nElements

    @nElements.setter
    def nElements(self, nElements: int):
        self.__nElements = nElements

    @property
    def oaam_common_Array(self):
        return self.__oaam_common_Array

    @oaam_common_Array.setter
    def oaam_common_Array(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_common_Array__oaam_common_Array", None)
        self.__oaam_common_Array = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataTypeA"):
                opp_val = getattr(old_value, "DataTypeA", None)
                if opp_val == self:
                    setattr(old_value, "DataTypeA", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataTypeA"):
                opp_val = getattr(value, "DataTypeA", None)
                setattr(value, "DataTypeA", self)

class BoolA:

    pass
class common_OaamBaseElementA:

    pass
class oaam_allocations_ConnectionAssignment(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_functions_Task(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    def __init__(self, nParallels: int, fixedRate: float, oaam_functions_Task268: set["Output"] = None, oaam_functions_Task270: "System" = None, oaam_functions_Task: "TaskType" = None, oaam_functions_Task266: set["Input"] = None, oaam_functions_Task273: "Device" = None, oaam_functions_Task275: set["TaskParameter"] = None):
        self.nParallels = nParallels
        self.fixedRate = fixedRate
        self.oaam_functions_Task268 = oaam_functions_Task268 if oaam_functions_Task268 is not None else set()
        self.oaam_functions_Task270 = oaam_functions_Task270
        self.oaam_functions_Task = oaam_functions_Task
        self.oaam_functions_Task266 = oaam_functions_Task266 if oaam_functions_Task266 is not None else set()
        self.oaam_functions_Task273 = oaam_functions_Task273
        self.oaam_functions_Task275 = oaam_functions_Task275 if oaam_functions_Task275 is not None else set()
        
    @property
    def nParallels(self) -> int:
        return self.__nParallels

    @nParallels.setter
    def nParallels(self, nParallels: int):
        self.__nParallels = nParallels

    @property
    def fixedRate(self) -> float:
        return self.__fixedRate

    @fixedRate.setter
    def fixedRate(self, fixedRate: float):
        self.__fixedRate = fixedRate

    @property
    def oaam_functions_Task270(self):
        return self.__oaam_functions_Task270

    @oaam_functions_Task270.setter
    def oaam_functions_Task270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_Task__oaam_functions_Task270", None)
        self.__oaam_functions_Task270 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "System271"):
                opp_val = getattr(old_value, "System271", None)
                if opp_val == self:
                    setattr(old_value, "System271", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "System271"):
                opp_val = getattr(value, "System271", None)
                setattr(value, "System271", self)

    @property
    def oaam_functions_Task(self):
        return self.__oaam_functions_Task

    @oaam_functions_Task.setter
    def oaam_functions_Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_Task__oaam_functions_Task", None)
        self.__oaam_functions_Task = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TaskType264"):
                opp_val = getattr(old_value, "TaskType264", None)
                if opp_val == self:
                    setattr(old_value, "TaskType264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TaskType264"):
                opp_val = getattr(value, "TaskType264", None)
                setattr(value, "TaskType264", self)

    @property
    def oaam_functions_Task275(self):
        return self.__oaam_functions_Task275

    @oaam_functions_Task275.setter
    def oaam_functions_Task275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_Task__oaam_functions_Task275", None)
        self.__oaam_functions_Task275 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaskParameter"):
                    opp_val = getattr(item, "TaskParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "TaskParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaskParameter"):
                    opp_val = getattr(item, "TaskParameter", None)
                    
                    setattr(item, "TaskParameter", self)
                    

    @property
    def oaam_functions_Task273(self):
        return self.__oaam_functions_Task273

    @oaam_functions_Task273.setter
    def oaam_functions_Task273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_Task__oaam_functions_Task273", None)
        self.__oaam_functions_Task273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Device"):
                opp_val = getattr(old_value, "Device", None)
                if opp_val == self:
                    setattr(old_value, "Device", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Device"):
                opp_val = getattr(value, "Device", None)
                setattr(value, "Device", self)

    @property
    def oaam_functions_Task266(self):
        return self.__oaam_functions_Task266

    @oaam_functions_Task266.setter
    def oaam_functions_Task266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_Task__oaam_functions_Task266", None)
        self.__oaam_functions_Task266 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Input"):
                    opp_val = getattr(item, "Input", None)
                    
                    if opp_val == self:
                        setattr(item, "Input", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Input"):
                    opp_val = getattr(item, "Input", None)
                    
                    setattr(item, "Input", self)
                    

    @property
    def oaam_functions_Task268(self):
        return self.__oaam_functions_Task268

    @oaam_functions_Task268.setter
    def oaam_functions_Task268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_Task__oaam_functions_Task268", None)
        self.__oaam_functions_Task268 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Output"):
                    opp_val = getattr(item, "Output", None)
                    
                    if opp_val == self:
                        setattr(item, "Output", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Output"):
                    opp_val = getattr(item, "Output", None)
                    
                    setattr(item, "Output", self)
                    

class oaam_restrictions_ConnectionRestriction(common_OaamBaseElementA, restrictions_SubfunctionRestrictionA, restrictions_SignalGroupRestrictionA, scenario_VariantDependentElementA, scenario_ModeDependentElementA, restrictions_SignalRestrictionA):

    def __init__(self, connectionName: str, isForbidden: bool, oaam_restrictions_ConnectionRestriction: set["Connection"] = None):
        self.connectionName = connectionName
        self.isForbidden = isForbidden
        self.oaam_restrictions_ConnectionRestriction = oaam_restrictions_ConnectionRestriction if oaam_restrictions_ConnectionRestriction is not None else set()
        
    @property
    def connectionName(self) -> str:
        return self.__connectionName

    @connectionName.setter
    def connectionName(self, connectionName: str):
        self.__connectionName = connectionName

    @property
    def isForbidden(self) -> bool:
        return self.__isForbidden

    @isForbidden.setter
    def isForbidden(self, isForbidden: bool):
        self.__isForbidden = isForbidden

    @property
    def oaam_restrictions_ConnectionRestriction(self):
        return self.__oaam_restrictions_ConnectionRestriction

    @oaam_restrictions_ConnectionRestriction.setter
    def oaam_restrictions_ConnectionRestriction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_ConnectionRestriction__oaam_restrictions_ConnectionRestriction", None)
        self.__oaam_restrictions_ConnectionRestriction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connection566"):
                    opp_val = getattr(item, "Connection566", None)
                    
                    if opp_val == self:
                        setattr(item, "Connection566", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connection566"):
                    opp_val = getattr(item, "Connection566", None)
                    
                    setattr(item, "Connection566", self)
                    

class oaam_allocations_TaskAssignment(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_allocations_ConnectionAssignmentSegment(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_functions_Output(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    def __init__(self, fixedRate: float, oaam_functions_Output: "ProvidedInformationA" = None, oaam_functions_Output329: "OutputDeclaration" = None, oaam_functions_Output332: set["Io"] = None):
        self.fixedRate = fixedRate
        self.oaam_functions_Output = oaam_functions_Output
        self.oaam_functions_Output329 = oaam_functions_Output329
        self.oaam_functions_Output332 = oaam_functions_Output332 if oaam_functions_Output332 is not None else set()
        
    @property
    def fixedRate(self) -> float:
        return self.__fixedRate

    @fixedRate.setter
    def fixedRate(self, fixedRate: float):
        self.__fixedRate = fixedRate

    @property
    def oaam_functions_Output(self):
        return self.__oaam_functions_Output

    @oaam_functions_Output.setter
    def oaam_functions_Output(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_Output__oaam_functions_Output", None)
        self.__oaam_functions_Output = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProvidedInformationA327"):
                opp_val = getattr(old_value, "ProvidedInformationA327", None)
                if opp_val == self:
                    setattr(old_value, "ProvidedInformationA327", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProvidedInformationA327"):
                opp_val = getattr(value, "ProvidedInformationA327", None)
                setattr(value, "ProvidedInformationA327", self)

    @property
    def oaam_functions_Output332(self):
        return self.__oaam_functions_Output332

    @oaam_functions_Output332.setter
    def oaam_functions_Output332(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_Output__oaam_functions_Output332", None)
        self.__oaam_functions_Output332 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Io333"):
                    opp_val = getattr(item, "Io333", None)
                    
                    if opp_val == self:
                        setattr(item, "Io333", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Io333"):
                    opp_val = getattr(item, "Io333", None)
                    
                    setattr(item, "Io333", self)
                    

    @property
    def oaam_functions_Output329(self):
        return self.__oaam_functions_Output329

    @oaam_functions_Output329.setter
    def oaam_functions_Output329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_Output__oaam_functions_Output329", None)
        self.__oaam_functions_Output329 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OutputDeclaration330"):
                opp_val = getattr(old_value, "OutputDeclaration330", None)
                if opp_val == self:
                    setattr(old_value, "OutputDeclaration330", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OutputDeclaration330"):
                opp_val = getattr(value, "OutputDeclaration330", None)
                setattr(value, "OutputDeclaration330", self)

class oaam_capabilities_SubconnectionInDeviceCapability(scenario_VariantDependentElementA, common_OaamBaseElementA, capabilities_CapabilityA, scenario_ModeDependentElementA):

    pass
class oaam_allocations_MessageA(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    def __init__(self, isPersistent: bool, length: int, oaam_allocations_MessageA: set["Schedule"] = None, oaam_allocations_MessageA696: set["MessageSegment"] = None, oaam_allocations_MessageA698: "MessageType" = None, oaam_allocations_MessageA692: set["Submessage"] = None, oaam_allocations_MessageA694: set["SignalToMessageAssignment"] = None):
        self.isPersistent = isPersistent
        self.length = length
        self.oaam_allocations_MessageA = oaam_allocations_MessageA if oaam_allocations_MessageA is not None else set()
        self.oaam_allocations_MessageA696 = oaam_allocations_MessageA696 if oaam_allocations_MessageA696 is not None else set()
        self.oaam_allocations_MessageA698 = oaam_allocations_MessageA698
        self.oaam_allocations_MessageA692 = oaam_allocations_MessageA692 if oaam_allocations_MessageA692 is not None else set()
        self.oaam_allocations_MessageA694 = oaam_allocations_MessageA694 if oaam_allocations_MessageA694 is not None else set()
        
    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def isPersistent(self) -> bool:
        return self.__isPersistent

    @isPersistent.setter
    def isPersistent(self, isPersistent: bool):
        self.__isPersistent = isPersistent

    @property
    def oaam_allocations_MessageA696(self):
        return self.__oaam_allocations_MessageA696

    @oaam_allocations_MessageA696.setter
    def oaam_allocations_MessageA696(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_allocations_MessageA__oaam_allocations_MessageA696", None)
        self.__oaam_allocations_MessageA696 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageSegment"):
                    opp_val = getattr(item, "MessageSegment", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageSegment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageSegment"):
                    opp_val = getattr(item, "MessageSegment", None)
                    
                    setattr(item, "MessageSegment", self)
                    

    @property
    def oaam_allocations_MessageA694(self):
        return self.__oaam_allocations_MessageA694

    @oaam_allocations_MessageA694.setter
    def oaam_allocations_MessageA694(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_allocations_MessageA__oaam_allocations_MessageA694", None)
        self.__oaam_allocations_MessageA694 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SignalToMessageAssignment"):
                    opp_val = getattr(item, "SignalToMessageAssignment", None)
                    
                    if opp_val == self:
                        setattr(item, "SignalToMessageAssignment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SignalToMessageAssignment"):
                    opp_val = getattr(item, "SignalToMessageAssignment", None)
                    
                    setattr(item, "SignalToMessageAssignment", self)
                    

    @property
    def oaam_allocations_MessageA692(self):
        return self.__oaam_allocations_MessageA692

    @oaam_allocations_MessageA692.setter
    def oaam_allocations_MessageA692(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_allocations_MessageA__oaam_allocations_MessageA692", None)
        self.__oaam_allocations_MessageA692 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Submessage"):
                    opp_val = getattr(item, "Submessage", None)
                    
                    if opp_val == self:
                        setattr(item, "Submessage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Submessage"):
                    opp_val = getattr(item, "Submessage", None)
                    
                    setattr(item, "Submessage", self)
                    

    @property
    def oaam_allocations_MessageA(self):
        return self.__oaam_allocations_MessageA

    @oaam_allocations_MessageA.setter
    def oaam_allocations_MessageA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_allocations_MessageA__oaam_allocations_MessageA", None)
        self.__oaam_allocations_MessageA = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Schedule690"):
                    opp_val = getattr(item, "Schedule690", None)
                    
                    if opp_val == self:
                        setattr(item, "Schedule690", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Schedule690"):
                    opp_val = getattr(item, "Schedule690", None)
                    
                    setattr(item, "Schedule690", self)
                    

    @property
    def oaam_allocations_MessageA698(self):
        return self.__oaam_allocations_MessageA698

    @oaam_allocations_MessageA698.setter
    def oaam_allocations_MessageA698(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_allocations_MessageA__oaam_allocations_MessageA698", None)
        self.__oaam_allocations_MessageA698 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageType699"):
                opp_val = getattr(old_value, "MessageType699", None)
                if opp_val == self:
                    setattr(old_value, "MessageType699", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageType699"):
                opp_val = getattr(value, "MessageType699", None)
                setattr(value, "MessageType699", self)

class oaam_systems_System(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_anatomy_Area(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_capabilities_SignalInMessageCapability(scenario_VariantDependentElementA, common_OaamBaseElementA, capabilities_CapabilityA, scenario_ModeDependentElementA):

    pass
class oaam_allocations_DeviceAssignment(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_allocations_ScheduledTime(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    def __init__(self, startTime: float, duration: float, restart: bool, cycle: int):
        self.startTime = startTime
        self.duration = duration
        self.restart = restart
        self.cycle = cycle
        
    @property
    def restart(self) -> bool:
        return self.__restart

    @restart.setter
    def restart(self, restart: bool):
        self.__restart = restart

    @property
    def duration(self) -> float:
        return self.__duration

    @duration.setter
    def duration(self, duration: float):
        self.__duration = duration

    @property
    def startTime(self) -> float:
        return self.__startTime

    @startTime.setter
    def startTime(self, startTime: float):
        self.__startTime = startTime

    @property
    def cycle(self) -> int:
        return self.__cycle

    @cycle.setter
    def cycle(self, cycle: int):
        self.__cycle = cycle

class oaam_allocations_SignalAssignment(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_hardware_Io(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_restrictions_AreaRestriction(restrictions_DeviceRestrictionA, restrictions_TaskGroupRestrictionA, common_OaamBaseElementA, restrictions_ConnectionRestrinctionA, restrictions_SubfunctionRestrictionA, restrictions_SignalGroupRestrictionA, scenario_VariantDependentElementA, scenario_ModeDependentElementA, restrictions_TaskRestrictionA, restrictions_SignalRestrictionA):

    def __init__(self, areaName: str, isForbidden: bool, oaam_restrictions_AreaRestriction: set["Area"] = None):
        self.areaName = areaName
        self.isForbidden = isForbidden
        self.oaam_restrictions_AreaRestriction = oaam_restrictions_AreaRestriction if oaam_restrictions_AreaRestriction is not None else set()
        
    @property
    def isForbidden(self) -> bool:
        return self.__isForbidden

    @isForbidden.setter
    def isForbidden(self, isForbidden: bool):
        self.__isForbidden = isForbidden

    @property
    def areaName(self) -> str:
        return self.__areaName

    @areaName.setter
    def areaName(self, areaName: str):
        self.__areaName = areaName

    @property
    def oaam_restrictions_AreaRestriction(self):
        return self.__oaam_restrictions_AreaRestriction

    @oaam_restrictions_AreaRestriction.setter
    def oaam_restrictions_AreaRestriction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_AreaRestriction__oaam_restrictions_AreaRestriction", None)
        self.__oaam_restrictions_AreaRestriction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Area556"):
                    opp_val = getattr(item, "Area556", None)
                    
                    if opp_val == self:
                        setattr(item, "Area556", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Area556"):
                    opp_val = getattr(item, "Area556", None)
                    
                    setattr(item, "Area556", self)
                    

class oaam_anatomy_LocationSymmetry(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_library_TaskType(library_ResourceConsumerA, common_OaamBaseElementA):

    def __init__(self, isDeterministic: bool, preferredExecutionRate: float, oaam_library_TaskType110: set["TaskStateDeclaration"] = None, oaam_library_TaskType: set["OutputDeclaration"] = None, oaam_library_TaskType108: set["InputDeclaration"] = None, oaam_library_TaskType112: set["TaskParameterDeclaration"] = None):
        self.isDeterministic = isDeterministic
        self.preferredExecutionRate = preferredExecutionRate
        self.oaam_library_TaskType110 = oaam_library_TaskType110 if oaam_library_TaskType110 is not None else set()
        self.oaam_library_TaskType = oaam_library_TaskType if oaam_library_TaskType is not None else set()
        self.oaam_library_TaskType108 = oaam_library_TaskType108 if oaam_library_TaskType108 is not None else set()
        self.oaam_library_TaskType112 = oaam_library_TaskType112 if oaam_library_TaskType112 is not None else set()
        
    @property
    def preferredExecutionRate(self) -> float:
        return self.__preferredExecutionRate

    @preferredExecutionRate.setter
    def preferredExecutionRate(self, preferredExecutionRate: float):
        self.__preferredExecutionRate = preferredExecutionRate

    @property
    def isDeterministic(self) -> bool:
        return self.__isDeterministic

    @isDeterministic.setter
    def isDeterministic(self, isDeterministic: bool):
        self.__isDeterministic = isDeterministic

    @property
    def oaam_library_TaskType(self):
        return self.__oaam_library_TaskType

    @oaam_library_TaskType.setter
    def oaam_library_TaskType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_TaskType__oaam_library_TaskType", None)
        self.__oaam_library_TaskType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputDeclaration"):
                    opp_val = getattr(item, "OutputDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputDeclaration"):
                    opp_val = getattr(item, "OutputDeclaration", None)
                    
                    setattr(item, "OutputDeclaration", self)
                    

    @property
    def oaam_library_TaskType112(self):
        return self.__oaam_library_TaskType112

    @oaam_library_TaskType112.setter
    def oaam_library_TaskType112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_TaskType__oaam_library_TaskType112", None)
        self.__oaam_library_TaskType112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaskParameterDeclaration"):
                    opp_val = getattr(item, "TaskParameterDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "TaskParameterDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaskParameterDeclaration"):
                    opp_val = getattr(item, "TaskParameterDeclaration", None)
                    
                    setattr(item, "TaskParameterDeclaration", self)
                    

    @property
    def oaam_library_TaskType110(self):
        return self.__oaam_library_TaskType110

    @oaam_library_TaskType110.setter
    def oaam_library_TaskType110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_TaskType__oaam_library_TaskType110", None)
        self.__oaam_library_TaskType110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaskStateDeclaration"):
                    opp_val = getattr(item, "TaskStateDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "TaskStateDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaskStateDeclaration"):
                    opp_val = getattr(item, "TaskStateDeclaration", None)
                    
                    setattr(item, "TaskStateDeclaration", self)
                    

    @property
    def oaam_library_TaskType108(self):
        return self.__oaam_library_TaskType108

    @oaam_library_TaskType108.setter
    def oaam_library_TaskType108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_TaskType__oaam_library_TaskType108", None)
        self.__oaam_library_TaskType108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputDeclaration"):
                    opp_val = getattr(item, "InputDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "InputDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputDeclaration"):
                    opp_val = getattr(item, "InputDeclaration", None)
                    
                    setattr(item, "InputDeclaration", self)
                    

class oaam_capabilities_SubmessageInMessageCapability(scenario_VariantDependentElementA, capabilities_CapabilityA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_anatomy_Duct(library_ResourceProviderInstanceA, common_OaamBaseElementA, scenario_VariantDependentElementA, scenario_ModeDependentElementA):

    def __init__(self, length: float, oaam_anatomy_Duct: "DuctType" = None, oaam_anatomy_Duct414: "DuctOpening" = None, oaam_anatomy_Duct417: "DuctOpening" = None):
        self.length = length
        self.oaam_anatomy_Duct = oaam_anatomy_Duct
        self.oaam_anatomy_Duct414 = oaam_anatomy_Duct414
        self.oaam_anatomy_Duct417 = oaam_anatomy_Duct417
        
    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, length: float):
        self.__length = length

    @property
    def oaam_anatomy_Duct417(self):
        return self.__oaam_anatomy_Duct417

    @oaam_anatomy_Duct417.setter
    def oaam_anatomy_Duct417(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_anatomy_Duct__oaam_anatomy_Duct417", None)
        self.__oaam_anatomy_Duct417 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DuctOpening418"):
                opp_val = getattr(old_value, "DuctOpening418", None)
                if opp_val == self:
                    setattr(old_value, "DuctOpening418", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DuctOpening418"):
                opp_val = getattr(value, "DuctOpening418", None)
                setattr(value, "DuctOpening418", self)

    @property
    def oaam_anatomy_Duct414(self):
        return self.__oaam_anatomy_Duct414

    @oaam_anatomy_Duct414.setter
    def oaam_anatomy_Duct414(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_anatomy_Duct__oaam_anatomy_Duct414", None)
        self.__oaam_anatomy_Duct414 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DuctOpening415"):
                opp_val = getattr(old_value, "DuctOpening415", None)
                if opp_val == self:
                    setattr(old_value, "DuctOpening415", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DuctOpening415"):
                opp_val = getattr(value, "DuctOpening415", None)
                setattr(value, "DuctOpening415", self)

    @property
    def oaam_anatomy_Duct(self):
        return self.__oaam_anatomy_Duct

    @oaam_anatomy_Duct.setter
    def oaam_anatomy_Duct(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_anatomy_Duct__oaam_anatomy_Duct", None)
        self.__oaam_anatomy_Duct = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DuctType412"):
                opp_val = getattr(old_value, "DuctType412", None)
                if opp_val == self:
                    setattr(old_value, "DuctType412", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DuctType412"):
                opp_val = getattr(value, "DuctType412", None)
                setattr(value, "DuctType412", self)

class oaam_library_ResourceBundle(common_OaamBaseElementA, library_ResourceConsumerA):

    def __init__(self, mtbf: float, cost: float, mass: float, oaam_library_ResourceBundle: set["Resource"] = None):
        self.mtbf = mtbf
        self.cost = cost
        self.mass = mass
        self.oaam_library_ResourceBundle = oaam_library_ResourceBundle if oaam_library_ResourceBundle is not None else set()
        
    @property
    def mtbf(self) -> float:
        return self.__mtbf

    @mtbf.setter
    def mtbf(self, mtbf: float):
        self.__mtbf = mtbf

    @property
    def cost(self) -> float:
        return self.__cost

    @cost.setter
    def cost(self, cost: float):
        self.__cost = cost

    @property
    def mass(self) -> float:
        return self.__mass

    @mass.setter
    def mass(self, mass: float):
        self.__mass = mass

    @property
    def oaam_library_ResourceBundle(self):
        return self.__oaam_library_ResourceBundle

    @oaam_library_ResourceBundle.setter
    def oaam_library_ResourceBundle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_ResourceBundle__oaam_library_ResourceBundle", None)
        self.__oaam_library_ResourceBundle = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Resource105"):
                    opp_val = getattr(item, "Resource105", None)
                    
                    if opp_val == self:
                        setattr(item, "Resource105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Resource105"):
                    opp_val = getattr(item, "Resource105", None)
                    
                    setattr(item, "Resource105", self)
                    

class oaam_anatomy_Location(library_ResourceProviderInstanceA, common_OaamBaseElementA, scenario_VariantDependentElementA, scenario_ModeDependentElementA):

    def __init__(self, length: float, oaam_anatomy_Location405: set["DuctOpening"] = None, oaam_anatomy_Location: "LocationType" = None, oaam_anatomy_Location403: "Position3D" = None):
        self.length = length
        self.oaam_anatomy_Location405 = oaam_anatomy_Location405 if oaam_anatomy_Location405 is not None else set()
        self.oaam_anatomy_Location = oaam_anatomy_Location
        self.oaam_anatomy_Location403 = oaam_anatomy_Location403
        
    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, length: float):
        self.__length = length

    @property
    def oaam_anatomy_Location403(self):
        return self.__oaam_anatomy_Location403

    @oaam_anatomy_Location403.setter
    def oaam_anatomy_Location403(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_anatomy_Location__oaam_anatomy_Location403", None)
        self.__oaam_anatomy_Location403 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Position3D"):
                opp_val = getattr(old_value, "Position3D", None)
                if opp_val == self:
                    setattr(old_value, "Position3D", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Position3D"):
                opp_val = getattr(value, "Position3D", None)
                setattr(value, "Position3D", self)

    @property
    def oaam_anatomy_Location(self):
        return self.__oaam_anatomy_Location

    @oaam_anatomy_Location.setter
    def oaam_anatomy_Location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_anatomy_Location__oaam_anatomy_Location", None)
        self.__oaam_anatomy_Location = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LocationType401"):
                opp_val = getattr(old_value, "LocationType401", None)
                if opp_val == self:
                    setattr(old_value, "LocationType401", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LocationType401"):
                opp_val = getattr(value, "LocationType401", None)
                setattr(value, "LocationType401", self)

    @property
    def oaam_anatomy_Location405(self):
        return self.__oaam_anatomy_Location405

    @oaam_anatomy_Location405.setter
    def oaam_anatomy_Location405(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_anatomy_Location__oaam_anatomy_Location405", None)
        self.__oaam_anatomy_Location405 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DuctOpening"):
                    opp_val = getattr(item, "DuctOpening", None)
                    
                    if opp_val == self:
                        setattr(item, "DuctOpening", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DuctOpening"):
                    opp_val = getattr(item, "DuctOpening", None)
                    
                    setattr(item, "DuctOpening", self)
                    

class oaam_functions_TaskSymmetry(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_allocations_SignalAssignmentSegment(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_hardware_Bus(scenario_VariantDependentElementA, common_OaamBaseElementA, library_ResourceProviderInstanceA, scenario_ModeDependentElementA):

    pass
class oaam_functions_ExternalOutputLink(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    def __init__(self, filter: str, oaam_functions_ExternalOutputLink: "Output" = None):
        self.filter = filter
        self.oaam_functions_ExternalOutputLink = oaam_functions_ExternalOutputLink
        
    @property
    def filter(self) -> str:
        return self.__filter

    @filter.setter
    def filter(self, filter: str):
        self.__filter = filter

    @property
    def oaam_functions_ExternalOutputLink(self):
        return self.__oaam_functions_ExternalOutputLink

    @oaam_functions_ExternalOutputLink.setter
    def oaam_functions_ExternalOutputLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_ExternalOutputLink__oaam_functions_ExternalOutputLink", None)
        self.__oaam_functions_ExternalOutputLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Output335"):
                opp_val = getattr(old_value, "Output335", None)
                if opp_val == self:
                    setattr(old_value, "Output335", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Output335"):
                opp_val = getattr(value, "Output335", None)
                setattr(value, "Output335", self)

class oaam_restrictions_PowerSourceRestriction(restrictions_DeviceRestrictionA, restrictions_TaskGroupRestrictionA, scenario_ModeDependentElementA, common_OaamBaseElementA, restrictions_SubfunctionRestrictionA, scenario_VariantDependentElementA, restrictions_SignalGroupRestrictionA, restrictions_TaskRestrictionA, restrictions_SignalRestrictionA):

    def __init__(self, powerSourceName: str, isForbidden: bool, oaam_restrictions_PowerSourceRestriction: set["PowerSource"] = None):
        self.powerSourceName = powerSourceName
        self.isForbidden = isForbidden
        self.oaam_restrictions_PowerSourceRestriction = oaam_restrictions_PowerSourceRestriction if oaam_restrictions_PowerSourceRestriction is not None else set()
        
    @property
    def isForbidden(self) -> bool:
        return self.__isForbidden

    @isForbidden.setter
    def isForbidden(self, isForbidden: bool):
        self.__isForbidden = isForbidden

    @property
    def powerSourceName(self) -> str:
        return self.__powerSourceName

    @powerSourceName.setter
    def powerSourceName(self, powerSourceName: str):
        self.__powerSourceName = powerSourceName

    @property
    def oaam_restrictions_PowerSourceRestriction(self):
        return self.__oaam_restrictions_PowerSourceRestriction

    @oaam_restrictions_PowerSourceRestriction.setter
    def oaam_restrictions_PowerSourceRestriction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_PowerSourceRestriction__oaam_restrictions_PowerSourceRestriction", None)
        self.__oaam_restrictions_PowerSourceRestriction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PowerSource558"):
                    opp_val = getattr(item, "PowerSource558", None)
                    
                    if opp_val == self:
                        setattr(item, "PowerSource558", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PowerSource558"):
                    opp_val = getattr(item, "PowerSource558", None)
                    
                    setattr(item, "PowerSource558", self)
                    

class oaam_scenario_ScenarioParameterNumeric(common_OaamBaseElementA, scenario_ScenarioParameterA):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class oaam_systems_InformationPower(systems_ProvidedInformationA, common_OaamBaseElementA, scenario_VariantDependentElementA, scenario_ModeDependentElementA, systems_RequiredInformationA):

    def __init__(self, power: float):
        self.power = power
        
    @property
    def power(self) -> float:
        return self.__power

    @power.setter
    def power(self, power: float):
        self.__power = power

class oaam_library_SignalType(library_ResourceConsumerA, common_OaamBaseElementA):

    pass
class oaam_functions_ExternalTaskLink(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    def __init__(self, filter: str, oaam_functions_ExternalTaskLink279: set["Input"] = None, oaam_functions_ExternalTaskLink282: set["Output"] = None, oaam_functions_ExternalTaskLink: "TaskType" = None, oaam_functions_ExternalTaskLink285: "Task" = None):
        self.filter = filter
        self.oaam_functions_ExternalTaskLink279 = oaam_functions_ExternalTaskLink279 if oaam_functions_ExternalTaskLink279 is not None else set()
        self.oaam_functions_ExternalTaskLink282 = oaam_functions_ExternalTaskLink282 if oaam_functions_ExternalTaskLink282 is not None else set()
        self.oaam_functions_ExternalTaskLink = oaam_functions_ExternalTaskLink
        self.oaam_functions_ExternalTaskLink285 = oaam_functions_ExternalTaskLink285
        
    @property
    def filter(self) -> str:
        return self.__filter

    @filter.setter
    def filter(self, filter: str):
        self.__filter = filter

    @property
    def oaam_functions_ExternalTaskLink282(self):
        return self.__oaam_functions_ExternalTaskLink282

    @oaam_functions_ExternalTaskLink282.setter
    def oaam_functions_ExternalTaskLink282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_ExternalTaskLink__oaam_functions_ExternalTaskLink282", None)
        self.__oaam_functions_ExternalTaskLink282 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Output283"):
                    opp_val = getattr(item, "Output283", None)
                    
                    if opp_val == self:
                        setattr(item, "Output283", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Output283"):
                    opp_val = getattr(item, "Output283", None)
                    
                    setattr(item, "Output283", self)
                    

    @property
    def oaam_functions_ExternalTaskLink(self):
        return self.__oaam_functions_ExternalTaskLink

    @oaam_functions_ExternalTaskLink.setter
    def oaam_functions_ExternalTaskLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_ExternalTaskLink__oaam_functions_ExternalTaskLink", None)
        self.__oaam_functions_ExternalTaskLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TaskType277"):
                opp_val = getattr(old_value, "TaskType277", None)
                if opp_val == self:
                    setattr(old_value, "TaskType277", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TaskType277"):
                opp_val = getattr(value, "TaskType277", None)
                setattr(value, "TaskType277", self)

    @property
    def oaam_functions_ExternalTaskLink285(self):
        return self.__oaam_functions_ExternalTaskLink285

    @oaam_functions_ExternalTaskLink285.setter
    def oaam_functions_ExternalTaskLink285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_ExternalTaskLink__oaam_functions_ExternalTaskLink285", None)
        self.__oaam_functions_ExternalTaskLink285 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Task286"):
                opp_val = getattr(old_value, "Task286", None)
                if opp_val == self:
                    setattr(old_value, "Task286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Task286"):
                opp_val = getattr(value, "Task286", None)
                setattr(value, "Task286", self)

    @property
    def oaam_functions_ExternalTaskLink279(self):
        return self.__oaam_functions_ExternalTaskLink279

    @oaam_functions_ExternalTaskLink279.setter
    def oaam_functions_ExternalTaskLink279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_ExternalTaskLink__oaam_functions_ExternalTaskLink279", None)
        self.__oaam_functions_ExternalTaskLink279 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Input280"):
                    opp_val = getattr(item, "Input280", None)
                    
                    if opp_val == self:
                        setattr(item, "Input280", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Input280"):
                    opp_val = getattr(item, "Input280", None)
                    
                    setattr(item, "Input280", self)
                    

class oaam_hardware_Device(library_ResourceProviderInstanceA, common_OaamBaseElementA, scenario_VariantDependentElementA, scenario_ModeDependentElementA):

    pass
class oaam_allocations_Schedule(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    def __init__(self, rate: float, isPeriodic: bool, priority: int, oaam_allocations_Schedule: set["ScheduledTime"] = None):
        self.rate = rate
        self.isPeriodic = isPeriodic
        self.priority = priority
        self.oaam_allocations_Schedule = oaam_allocations_Schedule if oaam_allocations_Schedule is not None else set()
        
    @property
    def rate(self) -> float:
        return self.__rate

    @rate.setter
    def rate(self, rate: float):
        self.__rate = rate

    @property
    def isPeriodic(self) -> bool:
        return self.__isPeriodic

    @isPeriodic.setter
    def isPeriodic(self, isPeriodic: bool):
        self.__isPeriodic = isPeriodic

    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def oaam_allocations_Schedule(self):
        return self.__oaam_allocations_Schedule

    @oaam_allocations_Schedule.setter
    def oaam_allocations_Schedule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_allocations_Schedule__oaam_allocations_Schedule", None)
        self.__oaam_allocations_Schedule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ScheduledTime"):
                    opp_val = getattr(item, "ScheduledTime", None)
                    
                    if opp_val == self:
                        setattr(item, "ScheduledTime", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ScheduledTime"):
                    opp_val = getattr(item, "ScheduledTime", None)
                    
                    setattr(item, "ScheduledTime", self)
                    

class oaam_functions_FailureCondition(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    def __init__(self, maxOccurrenceProbability: float, noSingleFailure: bool, oaam_functions_FailureCondition: "BoolA" = None, oaam_functions_FailureCondition299: set["BoolNot"] = None, oaam_functions_FailureCondition296: set["BoolOperation"] = None, oaam_functions_FailureCondition302: set["OutputIntegrityState"] = None):
        self.maxOccurrenceProbability = maxOccurrenceProbability
        self.noSingleFailure = noSingleFailure
        self.oaam_functions_FailureCondition = oaam_functions_FailureCondition
        self.oaam_functions_FailureCondition299 = oaam_functions_FailureCondition299 if oaam_functions_FailureCondition299 is not None else set()
        self.oaam_functions_FailureCondition296 = oaam_functions_FailureCondition296 if oaam_functions_FailureCondition296 is not None else set()
        self.oaam_functions_FailureCondition302 = oaam_functions_FailureCondition302 if oaam_functions_FailureCondition302 is not None else set()
        
    @property
    def maxOccurrenceProbability(self) -> float:
        return self.__maxOccurrenceProbability

    @maxOccurrenceProbability.setter
    def maxOccurrenceProbability(self, maxOccurrenceProbability: float):
        self.__maxOccurrenceProbability = maxOccurrenceProbability

    @property
    def noSingleFailure(self) -> bool:
        return self.__noSingleFailure

    @noSingleFailure.setter
    def noSingleFailure(self, noSingleFailure: bool):
        self.__noSingleFailure = noSingleFailure

    @property
    def oaam_functions_FailureCondition(self):
        return self.__oaam_functions_FailureCondition

    @oaam_functions_FailureCondition.setter
    def oaam_functions_FailureCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_FailureCondition__oaam_functions_FailureCondition", None)
        self.__oaam_functions_FailureCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BoolA294"):
                opp_val = getattr(old_value, "BoolA294", None)
                if opp_val == self:
                    setattr(old_value, "BoolA294", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BoolA294"):
                opp_val = getattr(value, "BoolA294", None)
                setattr(value, "BoolA294", self)

    @property
    def oaam_functions_FailureCondition296(self):
        return self.__oaam_functions_FailureCondition296

    @oaam_functions_FailureCondition296.setter
    def oaam_functions_FailureCondition296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_FailureCondition__oaam_functions_FailureCondition296", None)
        self.__oaam_functions_FailureCondition296 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BoolOperation297"):
                    opp_val = getattr(item, "BoolOperation297", None)
                    
                    if opp_val == self:
                        setattr(item, "BoolOperation297", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BoolOperation297"):
                    opp_val = getattr(item, "BoolOperation297", None)
                    
                    setattr(item, "BoolOperation297", self)
                    

    @property
    def oaam_functions_FailureCondition302(self):
        return self.__oaam_functions_FailureCondition302

    @oaam_functions_FailureCondition302.setter
    def oaam_functions_FailureCondition302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_FailureCondition__oaam_functions_FailureCondition302", None)
        self.__oaam_functions_FailureCondition302 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputIntegrityState"):
                    opp_val = getattr(item, "OutputIntegrityState", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputIntegrityState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputIntegrityState"):
                    opp_val = getattr(item, "OutputIntegrityState", None)
                    
                    setattr(item, "OutputIntegrityState", self)
                    

    @property
    def oaam_functions_FailureCondition299(self):
        return self.__oaam_functions_FailureCondition299

    @oaam_functions_FailureCondition299.setter
    def oaam_functions_FailureCondition299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_FailureCondition__oaam_functions_FailureCondition299", None)
        self.__oaam_functions_FailureCondition299 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BoolNot300"):
                    opp_val = getattr(item, "BoolNot300", None)
                    
                    if opp_val == self:
                        setattr(item, "BoolNot300", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BoolNot300"):
                    opp_val = getattr(item, "BoolNot300", None)
                    
                    setattr(item, "BoolNot300", self)
                    

class oaam_library_DuctType(library_ResourceProviderA, common_OaamBaseElementA):

    pass
class oaam_restrictions_DeviceRestriction(restrictions_TaskGroupRestrictionA, scenario_ModeDependentElementA, common_OaamBaseElementA, restrictions_SubfunctionRestrictionA, scenario_VariantDependentElementA, restrictions_SignalGroupRestrictionA, restrictions_TaskRestrictionA, restrictions_SignalRestrictionA):

    def __init__(self, deviceName: str, isForbidden: bool, oaam_restrictions_DeviceRestriction: set["Device"] = None):
        self.deviceName = deviceName
        self.isForbidden = isForbidden
        self.oaam_restrictions_DeviceRestriction = oaam_restrictions_DeviceRestriction if oaam_restrictions_DeviceRestriction is not None else set()
        
    @property
    def isForbidden(self) -> bool:
        return self.__isForbidden

    @isForbidden.setter
    def isForbidden(self, isForbidden: bool):
        self.__isForbidden = isForbidden

    @property
    def deviceName(self) -> str:
        return self.__deviceName

    @deviceName.setter
    def deviceName(self, deviceName: str):
        self.__deviceName = deviceName

    @property
    def oaam_restrictions_DeviceRestriction(self):
        return self.__oaam_restrictions_DeviceRestriction

    @oaam_restrictions_DeviceRestriction.setter
    def oaam_restrictions_DeviceRestriction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_DeviceRestriction__oaam_restrictions_DeviceRestriction", None)
        self.__oaam_restrictions_DeviceRestriction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Device560"):
                    opp_val = getattr(item, "Device560", None)
                    
                    if opp_val == self:
                        setattr(item, "Device560", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Device560"):
                    opp_val = getattr(item, "Device560", None)
                    
                    setattr(item, "Device560", self)
                    

class oaam_restrictions_LocationRestriction(restrictions_DeviceRestrictionA, restrictions_TaskGroupRestrictionA, scenario_ModeDependentElementA, common_OaamBaseElementA, restrictions_SubfunctionRestrictionA, restrictions_ConnectionRestrinctionA, scenario_VariantDependentElementA, restrictions_SignalGroupRestrictionA, restrictions_TaskRestrictionA, restrictions_SignalRestrictionA):

    def __init__(self, locationName: str, isForbidden: bool, oaam_restrictions_LocationRestriction: set["Location"] = None):
        self.locationName = locationName
        self.isForbidden = isForbidden
        self.oaam_restrictions_LocationRestriction = oaam_restrictions_LocationRestriction if oaam_restrictions_LocationRestriction is not None else set()
        
    @property
    def isForbidden(self) -> bool:
        return self.__isForbidden

    @isForbidden.setter
    def isForbidden(self, isForbidden: bool):
        self.__isForbidden = isForbidden

    @property
    def locationName(self) -> str:
        return self.__locationName

    @locationName.setter
    def locationName(self, locationName: str):
        self.__locationName = locationName

    @property
    def oaam_restrictions_LocationRestriction(self):
        return self.__oaam_restrictions_LocationRestriction

    @oaam_restrictions_LocationRestriction.setter
    def oaam_restrictions_LocationRestriction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_LocationRestriction__oaam_restrictions_LocationRestriction", None)
        self.__oaam_restrictions_LocationRestriction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Location554"):
                    opp_val = getattr(item, "Location554", None)
                    
                    if opp_val == self:
                        setattr(item, "Location554", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Location554"):
                    opp_val = getattr(item, "Location554", None)
                    
                    setattr(item, "Location554", self)
                    

class oaam_capabilities_ConnectionInDuctOrLocationCapability(scenario_VariantDependentElementA, common_OaamBaseElementA, capabilities_CapabilityA, scenario_ModeDependentElementA):

    pass
class oaam_restrictions_SynchronicityRestriction(scenario_VariantDependentElementA, common_OaamBaseElementA, restrictions_TaskRestrictionA, scenario_ModeDependentElementA):

    def __init__(self, maxJitter: float):
        self.maxJitter = maxJitter
        
    @property
    def maxJitter(self) -> float:
        return self.__maxJitter

    @maxJitter.setter
    def maxJitter(self, maxJitter: float):
        self.__maxJitter = maxJitter

class oaam_restrictions_TimeDelayRestriction(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    def __init__(self, delay: float, oaam_restrictions_TimeDelayRestriction: "Task" = None, oaam_restrictions_TimeDelayRestriction610: "Task" = None):
        self.delay = delay
        self.oaam_restrictions_TimeDelayRestriction = oaam_restrictions_TimeDelayRestriction
        self.oaam_restrictions_TimeDelayRestriction610 = oaam_restrictions_TimeDelayRestriction610
        
    @property
    def delay(self) -> float:
        return self.__delay

    @delay.setter
    def delay(self, delay: float):
        self.__delay = delay

    @property
    def oaam_restrictions_TimeDelayRestriction610(self):
        return self.__oaam_restrictions_TimeDelayRestriction610

    @oaam_restrictions_TimeDelayRestriction610.setter
    def oaam_restrictions_TimeDelayRestriction610(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_TimeDelayRestriction__oaam_restrictions_TimeDelayRestriction610", None)
        self.__oaam_restrictions_TimeDelayRestriction610 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Task611"):
                opp_val = getattr(old_value, "Task611", None)
                if opp_val == self:
                    setattr(old_value, "Task611", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Task611"):
                opp_val = getattr(value, "Task611", None)
                setattr(value, "Task611", self)

    @property
    def oaam_restrictions_TimeDelayRestriction(self):
        return self.__oaam_restrictions_TimeDelayRestriction

    @oaam_restrictions_TimeDelayRestriction.setter
    def oaam_restrictions_TimeDelayRestriction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_TimeDelayRestriction__oaam_restrictions_TimeDelayRestriction", None)
        self.__oaam_restrictions_TimeDelayRestriction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Task608"):
                opp_val = getattr(old_value, "Task608", None)
                if opp_val == self:
                    setattr(old_value, "Task608", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Task608"):
                opp_val = getattr(value, "Task608", None)
                setattr(value, "Task608", self)

class oaam_library_LocationType(library_ResourceProviderA, common_OaamBaseElementA):

    def __init__(self, isJoint: bool, oaam_library_LocationType: set["DuctOpeningDeclaration"] = None):
        self.isJoint = isJoint
        self.oaam_library_LocationType = oaam_library_LocationType if oaam_library_LocationType is not None else set()
        
    @property
    def isJoint(self) -> bool:
        return self.__isJoint

    @isJoint.setter
    def isJoint(self, isJoint: bool):
        self.__isJoint = isJoint

    @property
    def oaam_library_LocationType(self):
        return self.__oaam_library_LocationType

    @oaam_library_LocationType.setter
    def oaam_library_LocationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_LocationType__oaam_library_LocationType", None)
        self.__oaam_library_LocationType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DuctOpeningDeclaration"):
                    opp_val = getattr(item, "DuctOpeningDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "DuctOpeningDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DuctOpeningDeclaration"):
                    opp_val = getattr(item, "DuctOpeningDeclaration", None)
                    
                    setattr(item, "DuctOpeningDeclaration", self)
                    

class oaam_library_ResourceTypeModifierLevel(common_OaamBaseElementA, library_ResourceConsumerA):

    pass
class oaam_systems_InformationMaterial(systems_ProvidedInformationA, common_OaamBaseElementA, scenario_VariantDependentElementA, scenario_ModeDependentElementA, systems_RequiredInformationA):

    def __init__(self, density: float, velocity: float):
        self.density = density
        self.velocity = velocity
        
    @property
    def velocity(self) -> float:
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity: float):
        self.__velocity = velocity

    @property
    def density(self) -> float:
        return self.__density

    @density.setter
    def density(self, density: float):
        self.__density = density

class oaam_library_ResourceType(library_ResourceConsumerA, common_OaamBaseElementA):

    def __init__(self, unit: str, isConsumed: bool, isDistinguishable: bool, isPropagated: bool, direction: str, isIo: bool, isConfigurable: bool, oaam_library_ResourceType96: set["ResourceAlternatives"] = None, oaam_library_ResourceType: set["Resource"] = None, oaam_library_ResourceType94: set["ResourceTypeModifierReference"] = None):
        self.unit = unit
        self.isConsumed = isConsumed
        self.isDistinguishable = isDistinguishable
        self.isPropagated = isPropagated
        self.direction = direction
        self.isIo = isIo
        self.isConfigurable = isConfigurable
        self.oaam_library_ResourceType96 = oaam_library_ResourceType96 if oaam_library_ResourceType96 is not None else set()
        self.oaam_library_ResourceType = oaam_library_ResourceType if oaam_library_ResourceType is not None else set()
        self.oaam_library_ResourceType94 = oaam_library_ResourceType94 if oaam_library_ResourceType94 is not None else set()
        
    @property
    def isPropagated(self) -> bool:
        return self.__isPropagated

    @isPropagated.setter
    def isPropagated(self, isPropagated: bool):
        self.__isPropagated = isPropagated

    @property
    def isConsumed(self) -> bool:
        return self.__isConsumed

    @isConsumed.setter
    def isConsumed(self, isConsumed: bool):
        self.__isConsumed = isConsumed

    @property
    def isConfigurable(self) -> bool:
        return self.__isConfigurable

    @isConfigurable.setter
    def isConfigurable(self, isConfigurable: bool):
        self.__isConfigurable = isConfigurable

    @property
    def isDistinguishable(self) -> bool:
        return self.__isDistinguishable

    @isDistinguishable.setter
    def isDistinguishable(self, isDistinguishable: bool):
        self.__isDistinguishable = isDistinguishable

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def isIo(self) -> bool:
        return self.__isIo

    @isIo.setter
    def isIo(self, isIo: bool):
        self.__isIo = isIo

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def oaam_library_ResourceType94(self):
        return self.__oaam_library_ResourceType94

    @oaam_library_ResourceType94.setter
    def oaam_library_ResourceType94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_ResourceType__oaam_library_ResourceType94", None)
        self.__oaam_library_ResourceType94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ResourceTypeModifierReference"):
                    opp_val = getattr(item, "ResourceTypeModifierReference", None)
                    
                    if opp_val == self:
                        setattr(item, "ResourceTypeModifierReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ResourceTypeModifierReference"):
                    opp_val = getattr(item, "ResourceTypeModifierReference", None)
                    
                    setattr(item, "ResourceTypeModifierReference", self)
                    

    @property
    def oaam_library_ResourceType(self):
        return self.__oaam_library_ResourceType

    @oaam_library_ResourceType.setter
    def oaam_library_ResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_ResourceType__oaam_library_ResourceType", None)
        self.__oaam_library_ResourceType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Resource92"):
                    opp_val = getattr(item, "Resource92", None)
                    
                    if opp_val == self:
                        setattr(item, "Resource92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Resource92"):
                    opp_val = getattr(item, "Resource92", None)
                    
                    setattr(item, "Resource92", self)
                    

    @property
    def oaam_library_ResourceType96(self):
        return self.__oaam_library_ResourceType96

    @oaam_library_ResourceType96.setter
    def oaam_library_ResourceType96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_ResourceType__oaam_library_ResourceType96", None)
        self.__oaam_library_ResourceType96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ResourceAlternatives"):
                    opp_val = getattr(item, "ResourceAlternatives", None)
                    
                    if opp_val == self:
                        setattr(item, "ResourceAlternatives", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ResourceAlternatives"):
                    opp_val = getattr(item, "ResourceAlternatives", None)
                    
                    setattr(item, "ResourceAlternatives", self)
                    

class oaam_capabilities_TaskOnDeviceCapability(scenario_VariantDependentElementA, common_OaamBaseElementA, capabilities_CapabilityA, scenario_ModeDependentElementA):

    def __init__(self, worstCaseExecutionTime: float, failureProbability: float, oaam_capabilities_TaskOnDeviceCapability: "TaskType" = None, oaam_capabilities_TaskOnDeviceCapability453: "DeviceType" = None):
        self.worstCaseExecutionTime = worstCaseExecutionTime
        self.failureProbability = failureProbability
        self.oaam_capabilities_TaskOnDeviceCapability = oaam_capabilities_TaskOnDeviceCapability
        self.oaam_capabilities_TaskOnDeviceCapability453 = oaam_capabilities_TaskOnDeviceCapability453
        
    @property
    def worstCaseExecutionTime(self) -> float:
        return self.__worstCaseExecutionTime

    @worstCaseExecutionTime.setter
    def worstCaseExecutionTime(self, worstCaseExecutionTime: float):
        self.__worstCaseExecutionTime = worstCaseExecutionTime

    @property
    def failureProbability(self) -> float:
        return self.__failureProbability

    @failureProbability.setter
    def failureProbability(self, failureProbability: float):
        self.__failureProbability = failureProbability

    @property
    def oaam_capabilities_TaskOnDeviceCapability453(self):
        return self.__oaam_capabilities_TaskOnDeviceCapability453

    @oaam_capabilities_TaskOnDeviceCapability453.setter
    def oaam_capabilities_TaskOnDeviceCapability453(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_capabilities_TaskOnDeviceCapability__oaam_capabilities_TaskOnDeviceCapability453", None)
        self.__oaam_capabilities_TaskOnDeviceCapability453 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DeviceType454"):
                opp_val = getattr(old_value, "DeviceType454", None)
                if opp_val == self:
                    setattr(old_value, "DeviceType454", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DeviceType454"):
                opp_val = getattr(value, "DeviceType454", None)
                setattr(value, "DeviceType454", self)

    @property
    def oaam_capabilities_TaskOnDeviceCapability(self):
        return self.__oaam_capabilities_TaskOnDeviceCapability

    @oaam_capabilities_TaskOnDeviceCapability.setter
    def oaam_capabilities_TaskOnDeviceCapability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_capabilities_TaskOnDeviceCapability__oaam_capabilities_TaskOnDeviceCapability", None)
        self.__oaam_capabilities_TaskOnDeviceCapability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TaskType451"):
                opp_val = getattr(old_value, "TaskType451", None)
                if opp_val == self:
                    setattr(old_value, "TaskType451", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TaskType451"):
                opp_val = getattr(value, "TaskType451", None)
                setattr(value, "TaskType451", self)

class oaam_scenario_Variant(common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_restrictions_DeviceTypeRestriction(restrictions_TaskGroupRestrictionA, common_OaamBaseElementA, restrictions_SubfunctionRestrictionA, restrictions_SignalGroupRestrictionA, scenario_VariantDependentElementA, scenario_ModeDependentElementA, restrictions_TaskRestrictionA, restrictions_SignalRestrictionA):

    def __init__(self, deviceTypeName: str, isForbidden: bool, oaam_restrictions_DeviceTypeRestriction: set["DeviceType"] = None):
        self.deviceTypeName = deviceTypeName
        self.isForbidden = isForbidden
        self.oaam_restrictions_DeviceTypeRestriction = oaam_restrictions_DeviceTypeRestriction if oaam_restrictions_DeviceTypeRestriction is not None else set()
        
    @property
    def deviceTypeName(self) -> str:
        return self.__deviceTypeName

    @deviceTypeName.setter
    def deviceTypeName(self, deviceTypeName: str):
        self.__deviceTypeName = deviceTypeName

    @property
    def isForbidden(self) -> bool:
        return self.__isForbidden

    @isForbidden.setter
    def isForbidden(self, isForbidden: bool):
        self.__isForbidden = isForbidden

    @property
    def oaam_restrictions_DeviceTypeRestriction(self):
        return self.__oaam_restrictions_DeviceTypeRestriction

    @oaam_restrictions_DeviceTypeRestriction.setter
    def oaam_restrictions_DeviceTypeRestriction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_DeviceTypeRestriction__oaam_restrictions_DeviceTypeRestriction", None)
        self.__oaam_restrictions_DeviceTypeRestriction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DeviceType562"):
                    opp_val = getattr(item, "DeviceType562", None)
                    
                    if opp_val == self:
                        setattr(item, "DeviceType562", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DeviceType562"):
                    opp_val = getattr(item, "DeviceType562", None)
                    
                    setattr(item, "DeviceType562", self)
                    

class oaam_restrictions_ConnectionTypeRestriction(scenario_ModeDependentElementA, common_OaamBaseElementA, restrictions_SignalGroupRestrictionA, scenario_VariantDependentElementA, restrictions_SubfunctionRestrictionA, restrictions_SignalRestrictionA):

    def __init__(self, connectionTypeName: str, isForbidden: bool, oaam_restrictions_ConnectionTypeRestriction: set["ConnectionType"] = None):
        self.connectionTypeName = connectionTypeName
        self.isForbidden = isForbidden
        self.oaam_restrictions_ConnectionTypeRestriction = oaam_restrictions_ConnectionTypeRestriction if oaam_restrictions_ConnectionTypeRestriction is not None else set()
        
    @property
    def connectionTypeName(self) -> str:
        return self.__connectionTypeName

    @connectionTypeName.setter
    def connectionTypeName(self, connectionTypeName: str):
        self.__connectionTypeName = connectionTypeName

    @property
    def isForbidden(self) -> bool:
        return self.__isForbidden

    @isForbidden.setter
    def isForbidden(self, isForbidden: bool):
        self.__isForbidden = isForbidden

    @property
    def oaam_restrictions_ConnectionTypeRestriction(self):
        return self.__oaam_restrictions_ConnectionTypeRestriction

    @oaam_restrictions_ConnectionTypeRestriction.setter
    def oaam_restrictions_ConnectionTypeRestriction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_ConnectionTypeRestriction__oaam_restrictions_ConnectionTypeRestriction", None)
        self.__oaam_restrictions_ConnectionTypeRestriction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConnectionType564"):
                    opp_val = getattr(item, "ConnectionType564", None)
                    
                    if opp_val == self:
                        setattr(item, "ConnectionType564", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConnectionType564"):
                    opp_val = getattr(item, "ConnectionType564", None)
                    
                    setattr(item, "ConnectionType564", self)
                    

class oaam_functions_Signal(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    def __init__(self, inIndex: int, outIndex: int, oaam_functions_Signal311: "SignalType" = None, oaam_functions_Signal: "Output" = None, oaam_functions_Signal308: "Input" = None, oaam_functions_Signal314: "Connection" = None):
        self.inIndex = inIndex
        self.outIndex = outIndex
        self.oaam_functions_Signal311 = oaam_functions_Signal311
        self.oaam_functions_Signal = oaam_functions_Signal
        self.oaam_functions_Signal308 = oaam_functions_Signal308
        self.oaam_functions_Signal314 = oaam_functions_Signal314
        
    @property
    def outIndex(self) -> int:
        return self.__outIndex

    @outIndex.setter
    def outIndex(self, outIndex: int):
        self.__outIndex = outIndex

    @property
    def inIndex(self) -> int:
        return self.__inIndex

    @inIndex.setter
    def inIndex(self, inIndex: int):
        self.__inIndex = inIndex

    @property
    def oaam_functions_Signal308(self):
        return self.__oaam_functions_Signal308

    @oaam_functions_Signal308.setter
    def oaam_functions_Signal308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_Signal__oaam_functions_Signal308", None)
        self.__oaam_functions_Signal308 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Input309"):
                opp_val = getattr(old_value, "Input309", None)
                if opp_val == self:
                    setattr(old_value, "Input309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Input309"):
                opp_val = getattr(value, "Input309", None)
                setattr(value, "Input309", self)

    @property
    def oaam_functions_Signal314(self):
        return self.__oaam_functions_Signal314

    @oaam_functions_Signal314.setter
    def oaam_functions_Signal314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_Signal__oaam_functions_Signal314", None)
        self.__oaam_functions_Signal314 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Connection"):
                opp_val = getattr(old_value, "Connection", None)
                if opp_val == self:
                    setattr(old_value, "Connection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Connection"):
                opp_val = getattr(value, "Connection", None)
                setattr(value, "Connection", self)

    @property
    def oaam_functions_Signal(self):
        return self.__oaam_functions_Signal

    @oaam_functions_Signal.setter
    def oaam_functions_Signal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_Signal__oaam_functions_Signal", None)
        self.__oaam_functions_Signal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Output306"):
                opp_val = getattr(old_value, "Output306", None)
                if opp_val == self:
                    setattr(old_value, "Output306", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Output306"):
                opp_val = getattr(value, "Output306", None)
                setattr(value, "Output306", self)

    @property
    def oaam_functions_Signal311(self):
        return self.__oaam_functions_Signal311

    @oaam_functions_Signal311.setter
    def oaam_functions_Signal311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_Signal__oaam_functions_Signal311", None)
        self.__oaam_functions_Signal311 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SignalType312"):
                opp_val = getattr(old_value, "SignalType312", None)
                if opp_val == self:
                    setattr(old_value, "SignalType312", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SignalType312"):
                opp_val = getattr(value, "SignalType312", None)
                setattr(value, "SignalType312", self)

class oaam_allocations_SubconnectionAssignment(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_restrictions_SegregationRestriction(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    def __init__(self, dissimilarArea: bool, dissimilarPowerSource: bool, dissimilarTechnology: bool, dissimilarLocation: bool, oaam_restrictions_SegregationRestriction: set["Task"] = None, oaam_restrictions_SegregationRestriction578: set["Signal"] = None, oaam_restrictions_SegregationRestriction581: set["Signal"] = None, oaam_restrictions_SegregationRestriction570: set["Task"] = None, oaam_restrictions_SegregationRestriction573: set["FunctionsContainerA"] = None, oaam_restrictions_SegregationRestriction575: set["FunctionsContainerA"] = None, oaam_restrictions_SegregationRestriction596: set["Device"] = None, oaam_restrictions_SegregationRestriction599: set["Device"] = None, oaam_restrictions_SegregationRestriction602: set["Connection"] = None, oaam_restrictions_SegregationRestriction584: set["TaskGroup"] = None, oaam_restrictions_SegregationRestriction587: set["TaskGroup"] = None, oaam_restrictions_SegregationRestriction590: set["SignalGroup"] = None, oaam_restrictions_SegregationRestriction593: set["SignalGroup"] = None, oaam_restrictions_SegregationRestriction605: set["Connection"] = None):
        self.dissimilarArea = dissimilarArea
        self.dissimilarPowerSource = dissimilarPowerSource
        self.dissimilarTechnology = dissimilarTechnology
        self.dissimilarLocation = dissimilarLocation
        self.oaam_restrictions_SegregationRestriction = oaam_restrictions_SegregationRestriction if oaam_restrictions_SegregationRestriction is not None else set()
        self.oaam_restrictions_SegregationRestriction578 = oaam_restrictions_SegregationRestriction578 if oaam_restrictions_SegregationRestriction578 is not None else set()
        self.oaam_restrictions_SegregationRestriction581 = oaam_restrictions_SegregationRestriction581 if oaam_restrictions_SegregationRestriction581 is not None else set()
        self.oaam_restrictions_SegregationRestriction570 = oaam_restrictions_SegregationRestriction570 if oaam_restrictions_SegregationRestriction570 is not None else set()
        self.oaam_restrictions_SegregationRestriction573 = oaam_restrictions_SegregationRestriction573 if oaam_restrictions_SegregationRestriction573 is not None else set()
        self.oaam_restrictions_SegregationRestriction575 = oaam_restrictions_SegregationRestriction575 if oaam_restrictions_SegregationRestriction575 is not None else set()
        self.oaam_restrictions_SegregationRestriction596 = oaam_restrictions_SegregationRestriction596 if oaam_restrictions_SegregationRestriction596 is not None else set()
        self.oaam_restrictions_SegregationRestriction599 = oaam_restrictions_SegregationRestriction599 if oaam_restrictions_SegregationRestriction599 is not None else set()
        self.oaam_restrictions_SegregationRestriction602 = oaam_restrictions_SegregationRestriction602 if oaam_restrictions_SegregationRestriction602 is not None else set()
        self.oaam_restrictions_SegregationRestriction584 = oaam_restrictions_SegregationRestriction584 if oaam_restrictions_SegregationRestriction584 is not None else set()
        self.oaam_restrictions_SegregationRestriction587 = oaam_restrictions_SegregationRestriction587 if oaam_restrictions_SegregationRestriction587 is not None else set()
        self.oaam_restrictions_SegregationRestriction590 = oaam_restrictions_SegregationRestriction590 if oaam_restrictions_SegregationRestriction590 is not None else set()
        self.oaam_restrictions_SegregationRestriction593 = oaam_restrictions_SegregationRestriction593 if oaam_restrictions_SegregationRestriction593 is not None else set()
        self.oaam_restrictions_SegregationRestriction605 = oaam_restrictions_SegregationRestriction605 if oaam_restrictions_SegregationRestriction605 is not None else set()
        
    @property
    def dissimilarPowerSource(self) -> bool:
        return self.__dissimilarPowerSource

    @dissimilarPowerSource.setter
    def dissimilarPowerSource(self, dissimilarPowerSource: bool):
        self.__dissimilarPowerSource = dissimilarPowerSource

    @property
    def dissimilarArea(self) -> bool:
        return self.__dissimilarArea

    @dissimilarArea.setter
    def dissimilarArea(self, dissimilarArea: bool):
        self.__dissimilarArea = dissimilarArea

    @property
    def dissimilarTechnology(self) -> bool:
        return self.__dissimilarTechnology

    @dissimilarTechnology.setter
    def dissimilarTechnology(self, dissimilarTechnology: bool):
        self.__dissimilarTechnology = dissimilarTechnology

    @property
    def dissimilarLocation(self) -> bool:
        return self.__dissimilarLocation

    @dissimilarLocation.setter
    def dissimilarLocation(self, dissimilarLocation: bool):
        self.__dissimilarLocation = dissimilarLocation

    @property
    def oaam_restrictions_SegregationRestriction590(self):
        return self.__oaam_restrictions_SegregationRestriction590

    @oaam_restrictions_SegregationRestriction590.setter
    def oaam_restrictions_SegregationRestriction590(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_SegregationRestriction__oaam_restrictions_SegregationRestriction590", None)
        self.__oaam_restrictions_SegregationRestriction590 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SignalGroup591"):
                    opp_val = getattr(item, "SignalGroup591", None)
                    
                    if opp_val == self:
                        setattr(item, "SignalGroup591", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SignalGroup591"):
                    opp_val = getattr(item, "SignalGroup591", None)
                    
                    setattr(item, "SignalGroup591", self)
                    

    @property
    def oaam_restrictions_SegregationRestriction602(self):
        return self.__oaam_restrictions_SegregationRestriction602

    @oaam_restrictions_SegregationRestriction602.setter
    def oaam_restrictions_SegregationRestriction602(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_SegregationRestriction__oaam_restrictions_SegregationRestriction602", None)
        self.__oaam_restrictions_SegregationRestriction602 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connection603"):
                    opp_val = getattr(item, "Connection603", None)
                    
                    if opp_val == self:
                        setattr(item, "Connection603", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connection603"):
                    opp_val = getattr(item, "Connection603", None)
                    
                    setattr(item, "Connection603", self)
                    

    @property
    def oaam_restrictions_SegregationRestriction570(self):
        return self.__oaam_restrictions_SegregationRestriction570

    @oaam_restrictions_SegregationRestriction570.setter
    def oaam_restrictions_SegregationRestriction570(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_SegregationRestriction__oaam_restrictions_SegregationRestriction570", None)
        self.__oaam_restrictions_SegregationRestriction570 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Task571"):
                    opp_val = getattr(item, "Task571", None)
                    
                    if opp_val == self:
                        setattr(item, "Task571", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Task571"):
                    opp_val = getattr(item, "Task571", None)
                    
                    setattr(item, "Task571", self)
                    

    @property
    def oaam_restrictions_SegregationRestriction581(self):
        return self.__oaam_restrictions_SegregationRestriction581

    @oaam_restrictions_SegregationRestriction581.setter
    def oaam_restrictions_SegregationRestriction581(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_SegregationRestriction__oaam_restrictions_SegregationRestriction581", None)
        self.__oaam_restrictions_SegregationRestriction581 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Signal582"):
                    opp_val = getattr(item, "Signal582", None)
                    
                    if opp_val == self:
                        setattr(item, "Signal582", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Signal582"):
                    opp_val = getattr(item, "Signal582", None)
                    
                    setattr(item, "Signal582", self)
                    

    @property
    def oaam_restrictions_SegregationRestriction587(self):
        return self.__oaam_restrictions_SegregationRestriction587

    @oaam_restrictions_SegregationRestriction587.setter
    def oaam_restrictions_SegregationRestriction587(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_SegregationRestriction__oaam_restrictions_SegregationRestriction587", None)
        self.__oaam_restrictions_SegregationRestriction587 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaskGroup588"):
                    opp_val = getattr(item, "TaskGroup588", None)
                    
                    if opp_val == self:
                        setattr(item, "TaskGroup588", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaskGroup588"):
                    opp_val = getattr(item, "TaskGroup588", None)
                    
                    setattr(item, "TaskGroup588", self)
                    

    @property
    def oaam_restrictions_SegregationRestriction599(self):
        return self.__oaam_restrictions_SegregationRestriction599

    @oaam_restrictions_SegregationRestriction599.setter
    def oaam_restrictions_SegregationRestriction599(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_SegregationRestriction__oaam_restrictions_SegregationRestriction599", None)
        self.__oaam_restrictions_SegregationRestriction599 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Device600"):
                    opp_val = getattr(item, "Device600", None)
                    
                    if opp_val == self:
                        setattr(item, "Device600", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Device600"):
                    opp_val = getattr(item, "Device600", None)
                    
                    setattr(item, "Device600", self)
                    

    @property
    def oaam_restrictions_SegregationRestriction578(self):
        return self.__oaam_restrictions_SegregationRestriction578

    @oaam_restrictions_SegregationRestriction578.setter
    def oaam_restrictions_SegregationRestriction578(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_SegregationRestriction__oaam_restrictions_SegregationRestriction578", None)
        self.__oaam_restrictions_SegregationRestriction578 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Signal579"):
                    opp_val = getattr(item, "Signal579", None)
                    
                    if opp_val == self:
                        setattr(item, "Signal579", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Signal579"):
                    opp_val = getattr(item, "Signal579", None)
                    
                    setattr(item, "Signal579", self)
                    

    @property
    def oaam_restrictions_SegregationRestriction605(self):
        return self.__oaam_restrictions_SegregationRestriction605

    @oaam_restrictions_SegregationRestriction605.setter
    def oaam_restrictions_SegregationRestriction605(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_SegregationRestriction__oaam_restrictions_SegregationRestriction605", None)
        self.__oaam_restrictions_SegregationRestriction605 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connection606"):
                    opp_val = getattr(item, "Connection606", None)
                    
                    if opp_val == self:
                        setattr(item, "Connection606", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connection606"):
                    opp_val = getattr(item, "Connection606", None)
                    
                    setattr(item, "Connection606", self)
                    

    @property
    def oaam_restrictions_SegregationRestriction(self):
        return self.__oaam_restrictions_SegregationRestriction

    @oaam_restrictions_SegregationRestriction.setter
    def oaam_restrictions_SegregationRestriction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_SegregationRestriction__oaam_restrictions_SegregationRestriction", None)
        self.__oaam_restrictions_SegregationRestriction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Task568"):
                    opp_val = getattr(item, "Task568", None)
                    
                    if opp_val == self:
                        setattr(item, "Task568", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Task568"):
                    opp_val = getattr(item, "Task568", None)
                    
                    setattr(item, "Task568", self)
                    

    @property
    def oaam_restrictions_SegregationRestriction596(self):
        return self.__oaam_restrictions_SegregationRestriction596

    @oaam_restrictions_SegregationRestriction596.setter
    def oaam_restrictions_SegregationRestriction596(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_SegregationRestriction__oaam_restrictions_SegregationRestriction596", None)
        self.__oaam_restrictions_SegregationRestriction596 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Device597"):
                    opp_val = getattr(item, "Device597", None)
                    
                    if opp_val == self:
                        setattr(item, "Device597", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Device597"):
                    opp_val = getattr(item, "Device597", None)
                    
                    setattr(item, "Device597", self)
                    

    @property
    def oaam_restrictions_SegregationRestriction584(self):
        return self.__oaam_restrictions_SegregationRestriction584

    @oaam_restrictions_SegregationRestriction584.setter
    def oaam_restrictions_SegregationRestriction584(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_SegregationRestriction__oaam_restrictions_SegregationRestriction584", None)
        self.__oaam_restrictions_SegregationRestriction584 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaskGroup585"):
                    opp_val = getattr(item, "TaskGroup585", None)
                    
                    if opp_val == self:
                        setattr(item, "TaskGroup585", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaskGroup585"):
                    opp_val = getattr(item, "TaskGroup585", None)
                    
                    setattr(item, "TaskGroup585", self)
                    

    @property
    def oaam_restrictions_SegregationRestriction593(self):
        return self.__oaam_restrictions_SegregationRestriction593

    @oaam_restrictions_SegregationRestriction593.setter
    def oaam_restrictions_SegregationRestriction593(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_SegregationRestriction__oaam_restrictions_SegregationRestriction593", None)
        self.__oaam_restrictions_SegregationRestriction593 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SignalGroup594"):
                    opp_val = getattr(item, "SignalGroup594", None)
                    
                    if opp_val == self:
                        setattr(item, "SignalGroup594", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SignalGroup594"):
                    opp_val = getattr(item, "SignalGroup594", None)
                    
                    setattr(item, "SignalGroup594", self)
                    

    @property
    def oaam_restrictions_SegregationRestriction573(self):
        return self.__oaam_restrictions_SegregationRestriction573

    @oaam_restrictions_SegregationRestriction573.setter
    def oaam_restrictions_SegregationRestriction573(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_SegregationRestriction__oaam_restrictions_SegregationRestriction573", None)
        self.__oaam_restrictions_SegregationRestriction573 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FunctionsContainerA"):
                    opp_val = getattr(item, "FunctionsContainerA", None)
                    
                    if opp_val == self:
                        setattr(item, "FunctionsContainerA", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FunctionsContainerA"):
                    opp_val = getattr(item, "FunctionsContainerA", None)
                    
                    setattr(item, "FunctionsContainerA", self)
                    

    @property
    def oaam_restrictions_SegregationRestriction575(self):
        return self.__oaam_restrictions_SegregationRestriction575

    @oaam_restrictions_SegregationRestriction575.setter
    def oaam_restrictions_SegregationRestriction575(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_restrictions_SegregationRestriction__oaam_restrictions_SegregationRestriction575", None)
        self.__oaam_restrictions_SegregationRestriction575 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FunctionsContainerA576"):
                    opp_val = getattr(item, "FunctionsContainerA576", None)
                    
                    if opp_val == self:
                        setattr(item, "FunctionsContainerA576", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FunctionsContainerA576"):
                    opp_val = getattr(item, "FunctionsContainerA576", None)
                    
                    setattr(item, "FunctionsContainerA576", self)
                    

class oaam_capabilities_SubdeviceInDeviceCapability(scenario_VariantDependentElementA, common_OaamBaseElementA, capabilities_CapabilityA, scenario_ModeDependentElementA):

    pass
class oaam_library_MessageType(library_ResourceProviderA, common_OaamBaseElementA, library_ResourceConsumerA):

    def __init__(self, maxLength: int, minLength: int, alignment: int, oaam_library_MessageType: "DataTypeA" = None, oaam_library_MessageType212: "DataTypeA" = None):
        self.maxLength = maxLength
        self.minLength = minLength
        self.alignment = alignment
        self.oaam_library_MessageType = oaam_library_MessageType
        self.oaam_library_MessageType212 = oaam_library_MessageType212
        
    @property
    def maxLength(self) -> int:
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: int):
        self.__maxLength = maxLength

    @property
    def minLength(self) -> int:
        return self.__minLength

    @minLength.setter
    def minLength(self, minLength: int):
        self.__minLength = minLength

    @property
    def alignment(self) -> int:
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: int):
        self.__alignment = alignment

    @property
    def oaam_library_MessageType212(self):
        return self.__oaam_library_MessageType212

    @oaam_library_MessageType212.setter
    def oaam_library_MessageType212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_MessageType__oaam_library_MessageType212", None)
        self.__oaam_library_MessageType212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataTypeA213"):
                opp_val = getattr(old_value, "DataTypeA213", None)
                if opp_val == self:
                    setattr(old_value, "DataTypeA213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataTypeA213"):
                opp_val = getattr(value, "DataTypeA213", None)
                setattr(value, "DataTypeA213", self)

    @property
    def oaam_library_MessageType(self):
        return self.__oaam_library_MessageType

    @oaam_library_MessageType.setter
    def oaam_library_MessageType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_MessageType__oaam_library_MessageType", None)
        self.__oaam_library_MessageType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataTypeA210"):
                opp_val = getattr(old_value, "DataTypeA210", None)
                if opp_val == self:
                    setattr(old_value, "DataTypeA210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataTypeA210"):
                opp_val = getattr(value, "DataTypeA210", None)
                setattr(value, "DataTypeA210", self)

class oaam_functions_FunctionsContainerA(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_allocations_MessageSegment(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_allocations_SubdeviceAssignment(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_anatomy_Position3D(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z
        
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def z(self) -> float:
        return self.__z

    @z.setter
    def z(self, z: float):
        self.__z = z

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

class oaam_scenario_ScenarioParameterBool(common_OaamBaseElementA, scenario_ScenarioParameterA):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class oaam_capabilities_DeviceInLocationCapability(scenario_VariantDependentElementA, common_OaamBaseElementA, capabilities_CapabilityA, scenario_ModeDependentElementA):

    pass
class oaam_capabilities_MessageOnBusCapability(scenario_VariantDependentElementA, capabilities_CapabilityA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_restrictions_TaskAtomicRestriction(restrictions_TaskGroupRestrictionA, scenario_ModeDependentElementA, common_OaamBaseElementA, scenario_VariantDependentElementA, restrictions_SubfunctionRestrictionA, restrictions_TaskRestrictionA):

    pass
class oaam_capabilities_MessageOnConnectionOrDeviceCapability(scenario_VariantDependentElementA, common_OaamBaseElementA, capabilities_CapabilityA, scenario_ModeDependentElementA):

    def __init__(self, worstCaseTransmissionTime: float, oaam_capabilities_MessageOnConnectionOrDeviceCapability: "MessageType" = None, oaam_capabilities_MessageOnConnectionOrDeviceCapability499: "DeviceType" = None, oaam_capabilities_MessageOnConnectionOrDeviceCapability502: "ConnectionType" = None):
        self.worstCaseTransmissionTime = worstCaseTransmissionTime
        self.oaam_capabilities_MessageOnConnectionOrDeviceCapability = oaam_capabilities_MessageOnConnectionOrDeviceCapability
        self.oaam_capabilities_MessageOnConnectionOrDeviceCapability499 = oaam_capabilities_MessageOnConnectionOrDeviceCapability499
        self.oaam_capabilities_MessageOnConnectionOrDeviceCapability502 = oaam_capabilities_MessageOnConnectionOrDeviceCapability502
        
    @property
    def worstCaseTransmissionTime(self) -> float:
        return self.__worstCaseTransmissionTime

    @worstCaseTransmissionTime.setter
    def worstCaseTransmissionTime(self, worstCaseTransmissionTime: float):
        self.__worstCaseTransmissionTime = worstCaseTransmissionTime

    @property
    def oaam_capabilities_MessageOnConnectionOrDeviceCapability(self):
        return self.__oaam_capabilities_MessageOnConnectionOrDeviceCapability

    @oaam_capabilities_MessageOnConnectionOrDeviceCapability.setter
    def oaam_capabilities_MessageOnConnectionOrDeviceCapability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_capabilities_MessageOnConnectionOrDeviceCapability__oaam_capabilities_MessageOnConnectionOrDeviceCapability", None)
        self.__oaam_capabilities_MessageOnConnectionOrDeviceCapability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageType497"):
                opp_val = getattr(old_value, "MessageType497", None)
                if opp_val == self:
                    setattr(old_value, "MessageType497", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageType497"):
                opp_val = getattr(value, "MessageType497", None)
                setattr(value, "MessageType497", self)

    @property
    def oaam_capabilities_MessageOnConnectionOrDeviceCapability499(self):
        return self.__oaam_capabilities_MessageOnConnectionOrDeviceCapability499

    @oaam_capabilities_MessageOnConnectionOrDeviceCapability499.setter
    def oaam_capabilities_MessageOnConnectionOrDeviceCapability499(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_capabilities_MessageOnConnectionOrDeviceCapability__oaam_capabilities_MessageOnConnectionOrDeviceCapability499", None)
        self.__oaam_capabilities_MessageOnConnectionOrDeviceCapability499 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DeviceType500"):
                opp_val = getattr(old_value, "DeviceType500", None)
                if opp_val == self:
                    setattr(old_value, "DeviceType500", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DeviceType500"):
                opp_val = getattr(value, "DeviceType500", None)
                setattr(value, "DeviceType500", self)

    @property
    def oaam_capabilities_MessageOnConnectionOrDeviceCapability502(self):
        return self.__oaam_capabilities_MessageOnConnectionOrDeviceCapability502

    @oaam_capabilities_MessageOnConnectionOrDeviceCapability502.setter
    def oaam_capabilities_MessageOnConnectionOrDeviceCapability502(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_capabilities_MessageOnConnectionOrDeviceCapability__oaam_capabilities_MessageOnConnectionOrDeviceCapability502", None)
        self.__oaam_capabilities_MessageOnConnectionOrDeviceCapability502 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConnectionType503"):
                opp_val = getattr(old_value, "ConnectionType503", None)
                if opp_val == self:
                    setattr(old_value, "ConnectionType503", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConnectionType503"):
                opp_val = getattr(value, "ConnectionType503", None)
                setattr(value, "ConnectionType503", self)

class oaam_anatomy_AreaSymmetry(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_systems_InformationFlow(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_scenario_OperationMode(scenario_VariantDependentElementA, common_OaamBaseElementA):

    pass
class oaam_capabilities_SignalOnConnectionOrDeviceCapability(scenario_VariantDependentElementA, common_OaamBaseElementA, capabilities_CapabilityA, scenario_ModeDependentElementA):

    def __init__(self, worstCaseTransmissionTime: float, oaam_capabilities_SignalOnConnectionOrDeviceCapability: "SignalType" = None, oaam_capabilities_SignalOnConnectionOrDeviceCapability471: "DeviceType" = None, oaam_capabilities_SignalOnConnectionOrDeviceCapability474: "ConnectionType" = None):
        self.worstCaseTransmissionTime = worstCaseTransmissionTime
        self.oaam_capabilities_SignalOnConnectionOrDeviceCapability = oaam_capabilities_SignalOnConnectionOrDeviceCapability
        self.oaam_capabilities_SignalOnConnectionOrDeviceCapability471 = oaam_capabilities_SignalOnConnectionOrDeviceCapability471
        self.oaam_capabilities_SignalOnConnectionOrDeviceCapability474 = oaam_capabilities_SignalOnConnectionOrDeviceCapability474
        
    @property
    def worstCaseTransmissionTime(self) -> float:
        return self.__worstCaseTransmissionTime

    @worstCaseTransmissionTime.setter
    def worstCaseTransmissionTime(self, worstCaseTransmissionTime: float):
        self.__worstCaseTransmissionTime = worstCaseTransmissionTime

    @property
    def oaam_capabilities_SignalOnConnectionOrDeviceCapability471(self):
        return self.__oaam_capabilities_SignalOnConnectionOrDeviceCapability471

    @oaam_capabilities_SignalOnConnectionOrDeviceCapability471.setter
    def oaam_capabilities_SignalOnConnectionOrDeviceCapability471(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_capabilities_SignalOnConnectionOrDeviceCapability__oaam_capabilities_SignalOnConnectionOrDeviceCapability471", None)
        self.__oaam_capabilities_SignalOnConnectionOrDeviceCapability471 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DeviceType472"):
                opp_val = getattr(old_value, "DeviceType472", None)
                if opp_val == self:
                    setattr(old_value, "DeviceType472", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DeviceType472"):
                opp_val = getattr(value, "DeviceType472", None)
                setattr(value, "DeviceType472", self)

    @property
    def oaam_capabilities_SignalOnConnectionOrDeviceCapability474(self):
        return self.__oaam_capabilities_SignalOnConnectionOrDeviceCapability474

    @oaam_capabilities_SignalOnConnectionOrDeviceCapability474.setter
    def oaam_capabilities_SignalOnConnectionOrDeviceCapability474(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_capabilities_SignalOnConnectionOrDeviceCapability__oaam_capabilities_SignalOnConnectionOrDeviceCapability474", None)
        self.__oaam_capabilities_SignalOnConnectionOrDeviceCapability474 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConnectionType475"):
                opp_val = getattr(old_value, "ConnectionType475", None)
                if opp_val == self:
                    setattr(old_value, "ConnectionType475", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConnectionType475"):
                opp_val = getattr(value, "ConnectionType475", None)
                setattr(value, "ConnectionType475", self)

    @property
    def oaam_capabilities_SignalOnConnectionOrDeviceCapability(self):
        return self.__oaam_capabilities_SignalOnConnectionOrDeviceCapability

    @oaam_capabilities_SignalOnConnectionOrDeviceCapability.setter
    def oaam_capabilities_SignalOnConnectionOrDeviceCapability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_capabilities_SignalOnConnectionOrDeviceCapability__oaam_capabilities_SignalOnConnectionOrDeviceCapability", None)
        self.__oaam_capabilities_SignalOnConnectionOrDeviceCapability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SignalType469"):
                opp_val = getattr(old_value, "SignalType469", None)
                if opp_val == self:
                    setattr(old_value, "SignalType469", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SignalType469"):
                opp_val = getattr(value, "SignalType469", None)
                setattr(value, "SignalType469", self)

class oaam_functions_Input(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    def __init__(self, queueLength: int, oaam_functions_Input: "InputDeclaration" = None, oaam_functions_Input320: "RequiredInformationA" = None, oaam_functions_Input323: set["Io"] = None, oaam_functions_Input325: "ExternalOutputLink" = None):
        self.queueLength = queueLength
        self.oaam_functions_Input = oaam_functions_Input
        self.oaam_functions_Input320 = oaam_functions_Input320
        self.oaam_functions_Input323 = oaam_functions_Input323 if oaam_functions_Input323 is not None else set()
        self.oaam_functions_Input325 = oaam_functions_Input325
        
    @property
    def queueLength(self) -> int:
        return self.__queueLength

    @queueLength.setter
    def queueLength(self, queueLength: int):
        self.__queueLength = queueLength

    @property
    def oaam_functions_Input320(self):
        return self.__oaam_functions_Input320

    @oaam_functions_Input320.setter
    def oaam_functions_Input320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_Input__oaam_functions_Input320", None)
        self.__oaam_functions_Input320 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RequiredInformationA321"):
                opp_val = getattr(old_value, "RequiredInformationA321", None)
                if opp_val == self:
                    setattr(old_value, "RequiredInformationA321", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequiredInformationA321"):
                opp_val = getattr(value, "RequiredInformationA321", None)
                setattr(value, "RequiredInformationA321", self)

    @property
    def oaam_functions_Input325(self):
        return self.__oaam_functions_Input325

    @oaam_functions_Input325.setter
    def oaam_functions_Input325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_Input__oaam_functions_Input325", None)
        self.__oaam_functions_Input325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExternalOutputLink"):
                opp_val = getattr(old_value, "ExternalOutputLink", None)
                if opp_val == self:
                    setattr(old_value, "ExternalOutputLink", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExternalOutputLink"):
                opp_val = getattr(value, "ExternalOutputLink", None)
                setattr(value, "ExternalOutputLink", self)

    @property
    def oaam_functions_Input(self):
        return self.__oaam_functions_Input

    @oaam_functions_Input.setter
    def oaam_functions_Input(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_Input__oaam_functions_Input", None)
        self.__oaam_functions_Input = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InputDeclaration318"):
                opp_val = getattr(old_value, "InputDeclaration318", None)
                if opp_val == self:
                    setattr(old_value, "InputDeclaration318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InputDeclaration318"):
                opp_val = getattr(value, "InputDeclaration318", None)
                setattr(value, "InputDeclaration318", self)

    @property
    def oaam_functions_Input323(self):
        return self.__oaam_functions_Input323

    @oaam_functions_Input323.setter
    def oaam_functions_Input323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_Input__oaam_functions_Input323", None)
        self.__oaam_functions_Input323 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Io"):
                    opp_val = getattr(item, "Io", None)
                    
                    if opp_val == self:
                        setattr(item, "Io", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Io"):
                    opp_val = getattr(item, "Io", None)
                    
                    setattr(item, "Io", self)
                    

class oaam_functions_SignalGroup(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_hardware_Connection(scenario_VariantDependentElementA, common_OaamBaseElementA, library_ResourceProviderInstanceA, scenario_ModeDependentElementA):

    pass
class oaam_hardware_DeviceSymmetry(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_library_BusType(library_ResourceProviderA, common_OaamBaseElementA):

    def __init__(self, requiresMaster: bool, mtbf: float, isSelfManaging: bool, oaam_library_BusType: set["DeviceType"] = None, oaam_library_BusType204: set["ConnectionType"] = None, oaam_library_BusType207: set["MessageType"] = None):
        self.requiresMaster = requiresMaster
        self.mtbf = mtbf
        self.isSelfManaging = isSelfManaging
        self.oaam_library_BusType = oaam_library_BusType if oaam_library_BusType is not None else set()
        self.oaam_library_BusType204 = oaam_library_BusType204 if oaam_library_BusType204 is not None else set()
        self.oaam_library_BusType207 = oaam_library_BusType207 if oaam_library_BusType207 is not None else set()
        
    @property
    def requiresMaster(self) -> bool:
        return self.__requiresMaster

    @requiresMaster.setter
    def requiresMaster(self, requiresMaster: bool):
        self.__requiresMaster = requiresMaster

    @property
    def mtbf(self) -> float:
        return self.__mtbf

    @mtbf.setter
    def mtbf(self, mtbf: float):
        self.__mtbf = mtbf

    @property
    def isSelfManaging(self) -> bool:
        return self.__isSelfManaging

    @isSelfManaging.setter
    def isSelfManaging(self, isSelfManaging: bool):
        self.__isSelfManaging = isSelfManaging

    @property
    def oaam_library_BusType(self):
        return self.__oaam_library_BusType

    @oaam_library_BusType.setter
    def oaam_library_BusType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_BusType__oaam_library_BusType", None)
        self.__oaam_library_BusType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DeviceType202"):
                    opp_val = getattr(item, "DeviceType202", None)
                    
                    if opp_val == self:
                        setattr(item, "DeviceType202", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DeviceType202"):
                    opp_val = getattr(item, "DeviceType202", None)
                    
                    setattr(item, "DeviceType202", self)
                    

    @property
    def oaam_library_BusType204(self):
        return self.__oaam_library_BusType204

    @oaam_library_BusType204.setter
    def oaam_library_BusType204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_BusType__oaam_library_BusType204", None)
        self.__oaam_library_BusType204 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConnectionType205"):
                    opp_val = getattr(item, "ConnectionType205", None)
                    
                    if opp_val == self:
                        setattr(item, "ConnectionType205", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConnectionType205"):
                    opp_val = getattr(item, "ConnectionType205", None)
                    
                    setattr(item, "ConnectionType205", self)
                    

    @property
    def oaam_library_BusType207(self):
        return self.__oaam_library_BusType207

    @oaam_library_BusType207.setter
    def oaam_library_BusType207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_BusType__oaam_library_BusType207", None)
        self.__oaam_library_BusType207 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageType208"):
                    opp_val = getattr(item, "MessageType208", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageType208", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageType208"):
                    opp_val = getattr(item, "MessageType208", None)
                    
                    setattr(item, "MessageType208", self)
                    

class oaam_systems_InformationSignal(systems_ProvidedInformationA, common_OaamBaseElementA, scenario_VariantDependentElementA, scenario_ModeDependentElementA, systems_RequiredInformationA):

    def __init__(self, rate: float, latency: float, accuracy: float, resolution: float, unit: str):
        self.rate = rate
        self.latency = latency
        self.accuracy = accuracy
        self.resolution = resolution
        self.unit = unit
        
    @property
    def rate(self) -> float:
        return self.__rate

    @rate.setter
    def rate(self, rate: float):
        self.__rate = rate

    @property
    def latency(self) -> float:
        return self.__latency

    @latency.setter
    def latency(self, latency: float):
        self.__latency = latency

    @property
    def resolution(self) -> float:
        return self.__resolution

    @resolution.setter
    def resolution(self, resolution: float):
        self.__resolution = resolution

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def accuracy(self) -> float:
        return self.__accuracy

    @accuracy.setter
    def accuracy(self, accuracy: float):
        self.__accuracy = accuracy

class oaam_anatomy_DuctOpening(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_restrictions_TaskSymmetryRestriction(restrictions_TaskGroupRestrictionA, common_OaamBaseElementA, restrictions_SubfunctionRestrictionA, scenario_VariantDependentElementA, scenario_ModeDependentElementA, restrictions_TaskRestrictionA):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class oaam_functions_TaskRedundancy(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class oaam_library_ConnectionType(library_ResourceProviderA, library_ResourceConsumerA, common_OaamBaseElementA):

    def __init__(self, nEndPoints: int, isInformation: bool, isPower: bool, isWireless: bool, allowsCircles: bool, nStartingPoints: int, nJoints: int, maxJointBranches: int, maxInterfaceToJointDistance: float, isSwitched: bool, directConnectionsAllowed: bool, maxLength: float, isUnidirectional: bool, requiresMaster: bool, oaam_library_ConnectionType121: set["ResourceType"] = None, oaam_library_ConnectionType: set["WireType"] = None, oaam_library_ConnectionType130: "MessageType" = None, oaam_library_ConnectionType124: set["ResourceType"] = None, oaam_library_ConnectionType127: set["DeviceType"] = None):
        self.nEndPoints = nEndPoints
        self.isInformation = isInformation
        self.isPower = isPower
        self.isWireless = isWireless
        self.allowsCircles = allowsCircles
        self.nStartingPoints = nStartingPoints
        self.nJoints = nJoints
        self.maxJointBranches = maxJointBranches
        self.maxInterfaceToJointDistance = maxInterfaceToJointDistance
        self.isSwitched = isSwitched
        self.directConnectionsAllowed = directConnectionsAllowed
        self.maxLength = maxLength
        self.isUnidirectional = isUnidirectional
        self.requiresMaster = requiresMaster
        self.oaam_library_ConnectionType121 = oaam_library_ConnectionType121 if oaam_library_ConnectionType121 is not None else set()
        self.oaam_library_ConnectionType = oaam_library_ConnectionType if oaam_library_ConnectionType is not None else set()
        self.oaam_library_ConnectionType130 = oaam_library_ConnectionType130
        self.oaam_library_ConnectionType124 = oaam_library_ConnectionType124 if oaam_library_ConnectionType124 is not None else set()
        self.oaam_library_ConnectionType127 = oaam_library_ConnectionType127 if oaam_library_ConnectionType127 is not None else set()
        
    @property
    def isPower(self) -> bool:
        return self.__isPower

    @isPower.setter
    def isPower(self, isPower: bool):
        self.__isPower = isPower

    @property
    def isInformation(self) -> bool:
        return self.__isInformation

    @isInformation.setter
    def isInformation(self, isInformation: bool):
        self.__isInformation = isInformation

    @property
    def isSwitched(self) -> bool:
        return self.__isSwitched

    @isSwitched.setter
    def isSwitched(self, isSwitched: bool):
        self.__isSwitched = isSwitched

    @property
    def isWireless(self) -> bool:
        return self.__isWireless

    @isWireless.setter
    def isWireless(self, isWireless: bool):
        self.__isWireless = isWireless

    @property
    def maxLength(self) -> float:
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: float):
        self.__maxLength = maxLength

    @property
    def nJoints(self) -> int:
        return self.__nJoints

    @nJoints.setter
    def nJoints(self, nJoints: int):
        self.__nJoints = nJoints

    @property
    def directConnectionsAllowed(self) -> bool:
        return self.__directConnectionsAllowed

    @directConnectionsAllowed.setter
    def directConnectionsAllowed(self, directConnectionsAllowed: bool):
        self.__directConnectionsAllowed = directConnectionsAllowed

    @property
    def requiresMaster(self) -> bool:
        return self.__requiresMaster

    @requiresMaster.setter
    def requiresMaster(self, requiresMaster: bool):
        self.__requiresMaster = requiresMaster

    @property
    def maxInterfaceToJointDistance(self) -> float:
        return self.__maxInterfaceToJointDistance

    @maxInterfaceToJointDistance.setter
    def maxInterfaceToJointDistance(self, maxInterfaceToJointDistance: float):
        self.__maxInterfaceToJointDistance = maxInterfaceToJointDistance

    @property
    def nEndPoints(self) -> int:
        return self.__nEndPoints

    @nEndPoints.setter
    def nEndPoints(self, nEndPoints: int):
        self.__nEndPoints = nEndPoints

    @property
    def isUnidirectional(self) -> bool:
        return self.__isUnidirectional

    @isUnidirectional.setter
    def isUnidirectional(self, isUnidirectional: bool):
        self.__isUnidirectional = isUnidirectional

    @property
    def allowsCircles(self) -> bool:
        return self.__allowsCircles

    @allowsCircles.setter
    def allowsCircles(self, allowsCircles: bool):
        self.__allowsCircles = allowsCircles

    @property
    def nStartingPoints(self) -> int:
        return self.__nStartingPoints

    @nStartingPoints.setter
    def nStartingPoints(self, nStartingPoints: int):
        self.__nStartingPoints = nStartingPoints

    @property
    def maxJointBranches(self) -> int:
        return self.__maxJointBranches

    @maxJointBranches.setter
    def maxJointBranches(self, maxJointBranches: int):
        self.__maxJointBranches = maxJointBranches

    @property
    def oaam_library_ConnectionType121(self):
        return self.__oaam_library_ConnectionType121

    @oaam_library_ConnectionType121.setter
    def oaam_library_ConnectionType121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_ConnectionType__oaam_library_ConnectionType121", None)
        self.__oaam_library_ConnectionType121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ResourceType122"):
                    opp_val = getattr(item, "ResourceType122", None)
                    
                    if opp_val == self:
                        setattr(item, "ResourceType122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ResourceType122"):
                    opp_val = getattr(item, "ResourceType122", None)
                    
                    setattr(item, "ResourceType122", self)
                    

    @property
    def oaam_library_ConnectionType130(self):
        return self.__oaam_library_ConnectionType130

    @oaam_library_ConnectionType130.setter
    def oaam_library_ConnectionType130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_ConnectionType__oaam_library_ConnectionType130", None)
        self.__oaam_library_ConnectionType130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageType131"):
                opp_val = getattr(old_value, "MessageType131", None)
                if opp_val == self:
                    setattr(old_value, "MessageType131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageType131"):
                opp_val = getattr(value, "MessageType131", None)
                setattr(value, "MessageType131", self)

    @property
    def oaam_library_ConnectionType124(self):
        return self.__oaam_library_ConnectionType124

    @oaam_library_ConnectionType124.setter
    def oaam_library_ConnectionType124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_ConnectionType__oaam_library_ConnectionType124", None)
        self.__oaam_library_ConnectionType124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ResourceType125"):
                    opp_val = getattr(item, "ResourceType125", None)
                    
                    if opp_val == self:
                        setattr(item, "ResourceType125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ResourceType125"):
                    opp_val = getattr(item, "ResourceType125", None)
                    
                    setattr(item, "ResourceType125", self)
                    

    @property
    def oaam_library_ConnectionType(self):
        return self.__oaam_library_ConnectionType

    @oaam_library_ConnectionType.setter
    def oaam_library_ConnectionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_ConnectionType__oaam_library_ConnectionType", None)
        self.__oaam_library_ConnectionType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WireType119"):
                    opp_val = getattr(item, "WireType119", None)
                    
                    if opp_val == self:
                        setattr(item, "WireType119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WireType119"):
                    opp_val = getattr(item, "WireType119", None)
                    
                    setattr(item, "WireType119", self)
                    

    @property
    def oaam_library_ConnectionType127(self):
        return self.__oaam_library_ConnectionType127

    @oaam_library_ConnectionType127.setter
    def oaam_library_ConnectionType127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_ConnectionType__oaam_library_ConnectionType127", None)
        self.__oaam_library_ConnectionType127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DeviceType128"):
                    opp_val = getattr(item, "DeviceType128", None)
                    
                    if opp_val == self:
                        setattr(item, "DeviceType128", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DeviceType128"):
                    opp_val = getattr(item, "DeviceType128", None)
                    
                    setattr(item, "DeviceType128", self)
                    

class oaam_library_DeviceType(library_ResourceProviderA, common_OaamBaseElementA, library_ResourceConsumerA):

    def __init__(self, mtbf: float, weight: float, cost: float, isSubdevice: bool, canHaveSubdevices: bool, isSelfManaging: bool, oaam_library_DeviceType: set["IoDeclaration"] = None, oaam_library_DeviceType117: set["IoGroup"] = None):
        self.mtbf = mtbf
        self.weight = weight
        self.cost = cost
        self.isSubdevice = isSubdevice
        self.canHaveSubdevices = canHaveSubdevices
        self.isSelfManaging = isSelfManaging
        self.oaam_library_DeviceType = oaam_library_DeviceType if oaam_library_DeviceType is not None else set()
        self.oaam_library_DeviceType117 = oaam_library_DeviceType117 if oaam_library_DeviceType117 is not None else set()
        
    @property
    def cost(self) -> float:
        return self.__cost

    @cost.setter
    def cost(self, cost: float):
        self.__cost = cost

    @property
    def isSubdevice(self) -> bool:
        return self.__isSubdevice

    @isSubdevice.setter
    def isSubdevice(self, isSubdevice: bool):
        self.__isSubdevice = isSubdevice

    @property
    def isSelfManaging(self) -> bool:
        return self.__isSelfManaging

    @isSelfManaging.setter
    def isSelfManaging(self, isSelfManaging: bool):
        self.__isSelfManaging = isSelfManaging

    @property
    def mtbf(self) -> float:
        return self.__mtbf

    @mtbf.setter
    def mtbf(self, mtbf: float):
        self.__mtbf = mtbf

    @property
    def canHaveSubdevices(self) -> bool:
        return self.__canHaveSubdevices

    @canHaveSubdevices.setter
    def canHaveSubdevices(self, canHaveSubdevices: bool):
        self.__canHaveSubdevices = canHaveSubdevices

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        self.__weight = weight

    @property
    def oaam_library_DeviceType117(self):
        return self.__oaam_library_DeviceType117

    @oaam_library_DeviceType117.setter
    def oaam_library_DeviceType117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_DeviceType__oaam_library_DeviceType117", None)
        self.__oaam_library_DeviceType117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IoGroup"):
                    opp_val = getattr(item, "IoGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "IoGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IoGroup"):
                    opp_val = getattr(item, "IoGroup", None)
                    
                    setattr(item, "IoGroup", self)
                    

    @property
    def oaam_library_DeviceType(self):
        return self.__oaam_library_DeviceType

    @oaam_library_DeviceType.setter
    def oaam_library_DeviceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_DeviceType__oaam_library_DeviceType", None)
        self.__oaam_library_DeviceType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IoDeclaration"):
                    opp_val = getattr(item, "IoDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "IoDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IoDeclaration"):
                    opp_val = getattr(item, "IoDeclaration", None)
                    
                    setattr(item, "IoDeclaration", self)
                    

class oaam_functions_TaskGroup(scenario_VariantDependentElementA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    pass
class common_BoolA:

    pass
class oaam_common_BoolNot(common_OaamBaseElementA, common_BoolA):

    pass
class oaam_library_TaskInputState(common_BoolA, common_OaamBaseElementA):

    def __init__(self, state: str, oaam_library_TaskInputState: "InputDeclaration" = None):
        self.state = state
        self.oaam_library_TaskInputState = oaam_library_TaskInputState
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def oaam_library_TaskInputState(self):
        return self.__oaam_library_TaskInputState

    @oaam_library_TaskInputState.setter
    def oaam_library_TaskInputState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_TaskInputState__oaam_library_TaskInputState", None)
        self.__oaam_library_TaskInputState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InputDeclaration161"):
                opp_val = getattr(old_value, "InputDeclaration161", None)
                if opp_val == self:
                    setattr(old_value, "InputDeclaration161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InputDeclaration161"):
                opp_val = getattr(value, "InputDeclaration161", None)
                setattr(value, "InputDeclaration161", self)

class oaam_functions_OutputIntegrityState(scenario_VariantDependentElementA, common_BoolA, common_OaamBaseElementA, scenario_ModeDependentElementA):

    def __init__(self, state: str, oaam_functions_OutputIntegrityState: "Output" = None):
        self.state = state
        self.oaam_functions_OutputIntegrityState = oaam_functions_OutputIntegrityState
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def oaam_functions_OutputIntegrityState(self):
        return self.__oaam_functions_OutputIntegrityState

    @oaam_functions_OutputIntegrityState.setter
    def oaam_functions_OutputIntegrityState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_OutputIntegrityState__oaam_functions_OutputIntegrityState", None)
        self.__oaam_functions_OutputIntegrityState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Output304"):
                opp_val = getattr(old_value, "Output304", None)
                if opp_val == self:
                    setattr(old_value, "Output304", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Output304"):
                opp_val = getattr(value, "Output304", None)
                setattr(value, "Output304", self)

class oaam_library_TaskInputTrigger(common_BoolA, common_OaamBaseElementA):

    pass
class oaam_common_BoolOperation(common_BoolA, common_OaamBaseElementA):

    def __init__(self, type: str, oaam_common_BoolOperation: "BoolA" = None, oaam_common_BoolOperation26: "BoolA" = None):
        self.type = type
        self.oaam_common_BoolOperation = oaam_common_BoolOperation
        self.oaam_common_BoolOperation26 = oaam_common_BoolOperation26
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def oaam_common_BoolOperation26(self):
        return self.__oaam_common_BoolOperation26

    @oaam_common_BoolOperation26.setter
    def oaam_common_BoolOperation26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_common_BoolOperation__oaam_common_BoolOperation26", None)
        self.__oaam_common_BoolOperation26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BoolA27"):
                opp_val = getattr(old_value, "BoolA27", None)
                if opp_val == self:
                    setattr(old_value, "BoolA27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BoolA27"):
                opp_val = getattr(value, "BoolA27", None)
                setattr(value, "BoolA27", self)

    @property
    def oaam_common_BoolOperation(self):
        return self.__oaam_common_BoolOperation

    @oaam_common_BoolOperation.setter
    def oaam_common_BoolOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_common_BoolOperation__oaam_common_BoolOperation", None)
        self.__oaam_common_BoolOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BoolA"):
                opp_val = getattr(old_value, "BoolA", None)
                if opp_val == self:
                    setattr(old_value, "BoolA", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BoolA"):
                opp_val = getattr(value, "BoolA", None)
                setattr(value, "BoolA", self)

class oaam_common_BoolA(ABC):

    pass
class AttributeA:

    pass
class oaam_common_AttributeReference(AttributeA):

    pass
class oaam_common_AttributeContainment(AttributeA):

    pass
class oaam_common_AttributeNumeric(AttributeA):

    def __init__(self, value: float, AttributeA725: "oaam_allocations_SignalToMessageAssignment", AttributeA: "oaam_common_OaamBaseElementA"):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class oaam_common_AttributeString(AttributeA):

    def __init__(self, value: str, AttributeA725: "oaam_allocations_SignalToMessageAssignment", AttributeA: "oaam_common_OaamBaseElementA"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Allocations:

    pass
class Restrictions:

    pass
class oaam_common_OaamBaseElementA(ABC):

    def __init__(self, id: str, name: str, style: str, documentation: str, modified: date, modifier: str, traceLink: str, oaam_common_OaamBaseElementA: set["AttributeA"] = None):
        self.id = id
        self.name = name
        self.style = style
        self.documentation = documentation
        self.modified = modified
        self.modifier = modifier
        self.traceLink = traceLink
        self.oaam_common_OaamBaseElementA = oaam_common_OaamBaseElementA if oaam_common_OaamBaseElementA is not None else set()
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def modifier(self) -> str:
        return self.__modifier

    @modifier.setter
    def modifier(self, modifier: str):
        self.__modifier = modifier

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def modified(self) -> date:
        return self.__modified

    @modified.setter
    def modified(self, modified: date):
        self.__modified = modified

    @property
    def traceLink(self) -> str:
        return self.__traceLink

    @traceLink.setter
    def traceLink(self, traceLink: str):
        self.__traceLink = traceLink

    @property
    def documentation(self) -> str:
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oaam_common_OaamBaseElementA(self):
        return self.__oaam_common_OaamBaseElementA

    @oaam_common_OaamBaseElementA.setter
    def oaam_common_OaamBaseElementA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_common_OaamBaseElementA__oaam_common_OaamBaseElementA", None)
        self.__oaam_common_OaamBaseElementA = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AttributeA"):
                    opp_val = getattr(item, "AttributeA", None)
                    
                    if opp_val == self:
                        setattr(item, "AttributeA", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AttributeA"):
                    opp_val = getattr(item, "AttributeA", None)
                    
                    setattr(item, "AttributeA", self)
                    

class Hardware:

    pass
class Functions:

    pass
class Systems:

    pass
class Scenario:

    pass
class Library:

    pass
class Capabilities:

    pass
class Anatomy:

    pass
class OaamBaseElementA:

    pass
class oaam_library_LibraryContainerA(OaamBaseElementA):

    pass
class oaam_library_IoDeclaration(OaamBaseElementA):

    pass
class oaam_scenario_ScenarioContainerA(OaamBaseElementA):

    pass
class oaam_library_ResourceGroup(OaamBaseElementA):

    pass
class oaam_library_ResourceTypeModifier(OaamBaseElementA):

    pass
class oaam_scenario_OperationModeReference(OaamBaseElementA):

    def __init__(self, activeProbability: float, oaam_scenario_OperationModeReference: "OperationMode" = None, OaamBaseElementA: "oaam_common_AttributeContainment", OaamBaseElementA23: "oaam_common_AttributeReference"):
        self.activeProbability = activeProbability
        self.oaam_scenario_OperationModeReference = oaam_scenario_OperationModeReference
        
    @property
    def activeProbability(self) -> float:
        return self.__activeProbability

    @activeProbability.setter
    def activeProbability(self, activeProbability: float):
        self.__activeProbability = activeProbability

    @property
    def oaam_scenario_OperationModeReference(self):
        return self.__oaam_scenario_OperationModeReference

    @oaam_scenario_OperationModeReference.setter
    def oaam_scenario_OperationModeReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_scenario_OperationModeReference__oaam_scenario_OperationModeReference", None)
        self.__oaam_scenario_OperationModeReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationMode225"):
                opp_val = getattr(old_value, "OperationMode225", None)
                if opp_val == self:
                    setattr(old_value, "OperationMode225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationMode225"):
                opp_val = getattr(value, "OperationMode225", None)
                setattr(value, "OperationMode225", self)

class oaam_library_OutputDeclaration(OaamBaseElementA):

    def __init__(self, range: str, unit: str, postcondition: str, lowerBound: int, upperBound: int, oaam_library_OutputDeclaration: "TaskOutputTrigger" = None, oaam_library_OutputDeclaration137: "DataTypeA" = None, oaam_library_OutputDeclaration140: set["FaultPropagation"] = None, OaamBaseElementA: "oaam_common_AttributeContainment", OaamBaseElementA23: "oaam_common_AttributeReference"):
        self.range = range
        self.unit = unit
        self.postcondition = postcondition
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.oaam_library_OutputDeclaration = oaam_library_OutputDeclaration
        self.oaam_library_OutputDeclaration137 = oaam_library_OutputDeclaration137
        self.oaam_library_OutputDeclaration140 = oaam_library_OutputDeclaration140 if oaam_library_OutputDeclaration140 is not None else set()
        
    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def range(self) -> str:
        return self.__range

    @range.setter
    def range(self, range: str):
        self.__range = range

    @property
    def postcondition(self) -> str:
        return self.__postcondition

    @postcondition.setter
    def postcondition(self, postcondition: str):
        self.__postcondition = postcondition

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def oaam_library_OutputDeclaration(self):
        return self.__oaam_library_OutputDeclaration

    @oaam_library_OutputDeclaration.setter
    def oaam_library_OutputDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_OutputDeclaration__oaam_library_OutputDeclaration", None)
        self.__oaam_library_OutputDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TaskOutputTrigger"):
                opp_val = getattr(old_value, "TaskOutputTrigger", None)
                if opp_val == self:
                    setattr(old_value, "TaskOutputTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TaskOutputTrigger"):
                opp_val = getattr(value, "TaskOutputTrigger", None)
                setattr(value, "TaskOutputTrigger", self)

    @property
    def oaam_library_OutputDeclaration140(self):
        return self.__oaam_library_OutputDeclaration140

    @oaam_library_OutputDeclaration140.setter
    def oaam_library_OutputDeclaration140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_OutputDeclaration__oaam_library_OutputDeclaration140", None)
        self.__oaam_library_OutputDeclaration140 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FaultPropagation"):
                    opp_val = getattr(item, "FaultPropagation", None)
                    
                    if opp_val == self:
                        setattr(item, "FaultPropagation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FaultPropagation"):
                    opp_val = getattr(item, "FaultPropagation", None)
                    
                    setattr(item, "FaultPropagation", self)
                    

    @property
    def oaam_library_OutputDeclaration137(self):
        return self.__oaam_library_OutputDeclaration137

    @oaam_library_OutputDeclaration137.setter
    def oaam_library_OutputDeclaration137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_OutputDeclaration__oaam_library_OutputDeclaration137", None)
        self.__oaam_library_OutputDeclaration137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataTypeA138"):
                opp_val = getattr(old_value, "DataTypeA138", None)
                if opp_val == self:
                    setattr(old_value, "DataTypeA138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataTypeA138"):
                opp_val = getattr(value, "DataTypeA138", None)
                setattr(value, "DataTypeA138", self)

class oaam_restrictions_RestrictionsContainerA(OaamBaseElementA):

    pass
class oaam_library_ResourceLink(OaamBaseElementA):

    pass
class oaam_library_TaskStateDeclaration(OaamBaseElementA):

    pass
class oaam_common_AttributeA(OaamBaseElementA):

    pass
class oaam_library_IoType(OaamBaseElementA):

    def __init__(self, direction: str, OaamBaseElementA: "oaam_common_AttributeContainment", OaamBaseElementA23: "oaam_common_AttributeReference"):
        self.direction = direction
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

class oaam_library_IoGroup(OaamBaseElementA):

    pass
class oaam_library_FaultPropagation(OaamBaseElementA):

    def __init__(self, outputState: str, oaam_library_FaultPropagation: "BoolA" = None, oaam_library_FaultPropagation155: set["BoolOperation"] = None, oaam_library_FaultPropagation157: set["BoolNot"] = None, oaam_library_FaultPropagation159: set["TaskInputState"] = None, OaamBaseElementA: "oaam_common_AttributeContainment", OaamBaseElementA23: "oaam_common_AttributeReference"):
        self.outputState = outputState
        self.oaam_library_FaultPropagation = oaam_library_FaultPropagation
        self.oaam_library_FaultPropagation155 = oaam_library_FaultPropagation155 if oaam_library_FaultPropagation155 is not None else set()
        self.oaam_library_FaultPropagation157 = oaam_library_FaultPropagation157 if oaam_library_FaultPropagation157 is not None else set()
        self.oaam_library_FaultPropagation159 = oaam_library_FaultPropagation159 if oaam_library_FaultPropagation159 is not None else set()
        
    @property
    def outputState(self) -> str:
        return self.__outputState

    @outputState.setter
    def outputState(self, outputState: str):
        self.__outputState = outputState

    @property
    def oaam_library_FaultPropagation157(self):
        return self.__oaam_library_FaultPropagation157

    @oaam_library_FaultPropagation157.setter
    def oaam_library_FaultPropagation157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_FaultPropagation__oaam_library_FaultPropagation157", None)
        self.__oaam_library_FaultPropagation157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BoolNot"):
                    opp_val = getattr(item, "BoolNot", None)
                    
                    if opp_val == self:
                        setattr(item, "BoolNot", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BoolNot"):
                    opp_val = getattr(item, "BoolNot", None)
                    
                    setattr(item, "BoolNot", self)
                    

    @property
    def oaam_library_FaultPropagation(self):
        return self.__oaam_library_FaultPropagation

    @oaam_library_FaultPropagation.setter
    def oaam_library_FaultPropagation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_FaultPropagation__oaam_library_FaultPropagation", None)
        self.__oaam_library_FaultPropagation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BoolA153"):
                opp_val = getattr(old_value, "BoolA153", None)
                if opp_val == self:
                    setattr(old_value, "BoolA153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BoolA153"):
                opp_val = getattr(value, "BoolA153", None)
                setattr(value, "BoolA153", self)

    @property
    def oaam_library_FaultPropagation159(self):
        return self.__oaam_library_FaultPropagation159

    @oaam_library_FaultPropagation159.setter
    def oaam_library_FaultPropagation159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_FaultPropagation__oaam_library_FaultPropagation159", None)
        self.__oaam_library_FaultPropagation159 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaskInputState"):
                    opp_val = getattr(item, "TaskInputState", None)
                    
                    if opp_val == self:
                        setattr(item, "TaskInputState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaskInputState"):
                    opp_val = getattr(item, "TaskInputState", None)
                    
                    setattr(item, "TaskInputState", self)
                    

    @property
    def oaam_library_FaultPropagation155(self):
        return self.__oaam_library_FaultPropagation155

    @oaam_library_FaultPropagation155.setter
    def oaam_library_FaultPropagation155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_FaultPropagation__oaam_library_FaultPropagation155", None)
        self.__oaam_library_FaultPropagation155 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BoolOperation"):
                    opp_val = getattr(item, "BoolOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "BoolOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BoolOperation"):
                    opp_val = getattr(item, "BoolOperation", None)
                    
                    setattr(item, "BoolOperation", self)
                    

class oaam_systems_InputSegregation(OaamBaseElementA):

    def __init__(self, dissimilarSource: bool, dissimilarRoute: bool, dissimilarTechnology: bool, oaam_systems_InputSegregation: set["RequiredInformationA"] = None, oaam_systems_InputSegregation244: set["RequiredInformationA"] = None, OaamBaseElementA: "oaam_common_AttributeContainment", OaamBaseElementA23: "oaam_common_AttributeReference"):
        self.dissimilarSource = dissimilarSource
        self.dissimilarRoute = dissimilarRoute
        self.dissimilarTechnology = dissimilarTechnology
        self.oaam_systems_InputSegregation = oaam_systems_InputSegregation if oaam_systems_InputSegregation is not None else set()
        self.oaam_systems_InputSegregation244 = oaam_systems_InputSegregation244 if oaam_systems_InputSegregation244 is not None else set()
        
    @property
    def dissimilarTechnology(self) -> bool:
        return self.__dissimilarTechnology

    @dissimilarTechnology.setter
    def dissimilarTechnology(self, dissimilarTechnology: bool):
        self.__dissimilarTechnology = dissimilarTechnology

    @property
    def dissimilarRoute(self) -> bool:
        return self.__dissimilarRoute

    @dissimilarRoute.setter
    def dissimilarRoute(self, dissimilarRoute: bool):
        self.__dissimilarRoute = dissimilarRoute

    @property
    def dissimilarSource(self) -> bool:
        return self.__dissimilarSource

    @dissimilarSource.setter
    def dissimilarSource(self, dissimilarSource: bool):
        self.__dissimilarSource = dissimilarSource

    @property
    def oaam_systems_InputSegregation(self):
        return self.__oaam_systems_InputSegregation

    @oaam_systems_InputSegregation.setter
    def oaam_systems_InputSegregation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_systems_InputSegregation__oaam_systems_InputSegregation", None)
        self.__oaam_systems_InputSegregation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RequiredInformationA242"):
                    opp_val = getattr(item, "RequiredInformationA242", None)
                    
                    if opp_val == self:
                        setattr(item, "RequiredInformationA242", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RequiredInformationA242"):
                    opp_val = getattr(item, "RequiredInformationA242", None)
                    
                    setattr(item, "RequiredInformationA242", self)
                    

    @property
    def oaam_systems_InputSegregation244(self):
        return self.__oaam_systems_InputSegregation244

    @oaam_systems_InputSegregation244.setter
    def oaam_systems_InputSegregation244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_systems_InputSegregation__oaam_systems_InputSegregation244", None)
        self.__oaam_systems_InputSegregation244 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RequiredInformationA245"):
                    opp_val = getattr(item, "RequiredInformationA245", None)
                    
                    if opp_val == self:
                        setattr(item, "RequiredInformationA245", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RequiredInformationA245"):
                    opp_val = getattr(item, "RequiredInformationA245", None)
                    
                    setattr(item, "RequiredInformationA245", self)
                    

class oaam_library_WireType(OaamBaseElementA):

    def __init__(self, specificWeight: float, specificPrice: float, nConductors: int, minBendingRadius: float, nShields: int, mtbf: float, OaamBaseElementA: "oaam_common_AttributeContainment", OaamBaseElementA23: "oaam_common_AttributeReference"):
        self.specificWeight = specificWeight
        self.specificPrice = specificPrice
        self.nConductors = nConductors
        self.minBendingRadius = minBendingRadius
        self.nShields = nShields
        self.mtbf = mtbf
        
    @property
    def minBendingRadius(self) -> float:
        return self.__minBendingRadius

    @minBendingRadius.setter
    def minBendingRadius(self, minBendingRadius: float):
        self.__minBendingRadius = minBendingRadius

    @property
    def nShields(self) -> int:
        return self.__nShields

    @nShields.setter
    def nShields(self, nShields: int):
        self.__nShields = nShields

    @property
    def mtbf(self) -> float:
        return self.__mtbf

    @mtbf.setter
    def mtbf(self, mtbf: float):
        self.__mtbf = mtbf

    @property
    def specificPrice(self) -> float:
        return self.__specificPrice

    @specificPrice.setter
    def specificPrice(self, specificPrice: float):
        self.__specificPrice = specificPrice

    @property
    def specificWeight(self) -> float:
        return self.__specificWeight

    @specificWeight.setter
    def specificWeight(self, specificWeight: float):
        self.__specificWeight = specificWeight

    @property
    def nConductors(self) -> int:
        return self.__nConductors

    @nConductors.setter
    def nConductors(self, nConductors: int):
        self.__nConductors = nConductors

class oaam_library_DeviceTypeDissimilarity(OaamBaseElementA):

    def __init__(self, percentageOfCommonHardware: float, oaam_library_DeviceTypeDissimilarity: set["DeviceType"] = None, OaamBaseElementA: "oaam_common_AttributeContainment", OaamBaseElementA23: "oaam_common_AttributeReference"):
        self.percentageOfCommonHardware = percentageOfCommonHardware
        self.oaam_library_DeviceTypeDissimilarity = oaam_library_DeviceTypeDissimilarity if oaam_library_DeviceTypeDissimilarity is not None else set()
        
    @property
    def percentageOfCommonHardware(self) -> float:
        return self.__percentageOfCommonHardware

    @percentageOfCommonHardware.setter
    def percentageOfCommonHardware(self, percentageOfCommonHardware: float):
        self.__percentageOfCommonHardware = percentageOfCommonHardware

    @property
    def oaam_library_DeviceTypeDissimilarity(self):
        return self.__oaam_library_DeviceTypeDissimilarity

    @oaam_library_DeviceTypeDissimilarity.setter
    def oaam_library_DeviceTypeDissimilarity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_DeviceTypeDissimilarity__oaam_library_DeviceTypeDissimilarity", None)
        self.__oaam_library_DeviceTypeDissimilarity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DeviceType182"):
                    opp_val = getattr(item, "DeviceType182", None)
                    
                    if opp_val == self:
                        setattr(item, "DeviceType182", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DeviceType182"):
                    opp_val = getattr(item, "DeviceType182", None)
                    
                    setattr(item, "DeviceType182", self)
                    

class oaam_functions_TaskParameter(OaamBaseElementA):

    def __init__(self, value: str, oaam_functions_TaskParameter: "TaskParameterDeclaration" = None, OaamBaseElementA: "oaam_common_AttributeContainment", OaamBaseElementA23: "oaam_common_AttributeReference"):
        self.value = value
        self.oaam_functions_TaskParameter = oaam_functions_TaskParameter
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def oaam_functions_TaskParameter(self):
        return self.__oaam_functions_TaskParameter

    @oaam_functions_TaskParameter.setter
    def oaam_functions_TaskParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_functions_TaskParameter__oaam_functions_TaskParameter", None)
        self.__oaam_functions_TaskParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TaskParameterDeclaration337"):
                opp_val = getattr(old_value, "TaskParameterDeclaration337", None)
                if opp_val == self:
                    setattr(old_value, "TaskParameterDeclaration337", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TaskParameterDeclaration337"):
                opp_val = getattr(value, "TaskParameterDeclaration337", None)
                setattr(value, "TaskParameterDeclaration337", self)

class oaam_capabilities_CapabilitiesContainerA(OaamBaseElementA):

    pass
class oaam_allocations_AllocationsContainerA(OaamBaseElementA):

    pass
class oaam_library_ResourceTypeDissimilarity(OaamBaseElementA):

    pass
class oaam_anatomy_AnatomyContainerA(OaamBaseElementA):

    pass
class oaam_hardware_HardwareContainerA(OaamBaseElementA):

    pass
class oaam_library_TaskOutputTrigger(OaamBaseElementA):

    def __init__(self, fixedRate: float, isFixedRate: bool, oaam_library_TaskOutputTrigger: "BoolA" = None, oaam_library_TaskOutputTrigger188: set["BoolOperation"] = None, oaam_library_TaskOutputTrigger191: set["BoolNot"] = None, oaam_library_TaskOutputTrigger194: set["TaskInputTrigger"] = None, OaamBaseElementA: "oaam_common_AttributeContainment", OaamBaseElementA23: "oaam_common_AttributeReference"):
        self.fixedRate = fixedRate
        self.isFixedRate = isFixedRate
        self.oaam_library_TaskOutputTrigger = oaam_library_TaskOutputTrigger
        self.oaam_library_TaskOutputTrigger188 = oaam_library_TaskOutputTrigger188 if oaam_library_TaskOutputTrigger188 is not None else set()
        self.oaam_library_TaskOutputTrigger191 = oaam_library_TaskOutputTrigger191 if oaam_library_TaskOutputTrigger191 is not None else set()
        self.oaam_library_TaskOutputTrigger194 = oaam_library_TaskOutputTrigger194 if oaam_library_TaskOutputTrigger194 is not None else set()
        
    @property
    def isFixedRate(self) -> bool:
        return self.__isFixedRate

    @isFixedRate.setter
    def isFixedRate(self, isFixedRate: bool):
        self.__isFixedRate = isFixedRate

    @property
    def fixedRate(self) -> float:
        return self.__fixedRate

    @fixedRate.setter
    def fixedRate(self, fixedRate: float):
        self.__fixedRate = fixedRate

    @property
    def oaam_library_TaskOutputTrigger191(self):
        return self.__oaam_library_TaskOutputTrigger191

    @oaam_library_TaskOutputTrigger191.setter
    def oaam_library_TaskOutputTrigger191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_TaskOutputTrigger__oaam_library_TaskOutputTrigger191", None)
        self.__oaam_library_TaskOutputTrigger191 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BoolNot192"):
                    opp_val = getattr(item, "BoolNot192", None)
                    
                    if opp_val == self:
                        setattr(item, "BoolNot192", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BoolNot192"):
                    opp_val = getattr(item, "BoolNot192", None)
                    
                    setattr(item, "BoolNot192", self)
                    

    @property
    def oaam_library_TaskOutputTrigger188(self):
        return self.__oaam_library_TaskOutputTrigger188

    @oaam_library_TaskOutputTrigger188.setter
    def oaam_library_TaskOutputTrigger188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_TaskOutputTrigger__oaam_library_TaskOutputTrigger188", None)
        self.__oaam_library_TaskOutputTrigger188 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BoolOperation189"):
                    opp_val = getattr(item, "BoolOperation189", None)
                    
                    if opp_val == self:
                        setattr(item, "BoolOperation189", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BoolOperation189"):
                    opp_val = getattr(item, "BoolOperation189", None)
                    
                    setattr(item, "BoolOperation189", self)
                    

    @property
    def oaam_library_TaskOutputTrigger(self):
        return self.__oaam_library_TaskOutputTrigger

    @oaam_library_TaskOutputTrigger.setter
    def oaam_library_TaskOutputTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_TaskOutputTrigger__oaam_library_TaskOutputTrigger", None)
        self.__oaam_library_TaskOutputTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BoolA186"):
                opp_val = getattr(old_value, "BoolA186", None)
                if opp_val == self:
                    setattr(old_value, "BoolA186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BoolA186"):
                opp_val = getattr(value, "BoolA186", None)
                setattr(value, "BoolA186", self)

    @property
    def oaam_library_TaskOutputTrigger194(self):
        return self.__oaam_library_TaskOutputTrigger194

    @oaam_library_TaskOutputTrigger194.setter
    def oaam_library_TaskOutputTrigger194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_TaskOutputTrigger__oaam_library_TaskOutputTrigger194", None)
        self.__oaam_library_TaskOutputTrigger194 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaskInputTrigger"):
                    opp_val = getattr(item, "TaskInputTrigger", None)
                    
                    if opp_val == self:
                        setattr(item, "TaskInputTrigger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaskInputTrigger"):
                    opp_val = getattr(item, "TaskInputTrigger", None)
                    
                    setattr(item, "TaskInputTrigger", self)
                    

class oaam_library_DeviceTypeSymmetry(OaamBaseElementA):

    pass
class oaam_library_DuctOpeningDeclaration(OaamBaseElementA):

    pass
class oaam_library_Resource(OaamBaseElementA):

    def __init__(self, count: float, oaam_library_Resource: "ResourceType" = None, oaam_library_Resource100: set["ResourceTypeModifierLevel"] = None, OaamBaseElementA: "oaam_common_AttributeContainment", OaamBaseElementA23: "oaam_common_AttributeReference"):
        self.count = count
        self.oaam_library_Resource = oaam_library_Resource
        self.oaam_library_Resource100 = oaam_library_Resource100 if oaam_library_Resource100 is not None else set()
        
    @property
    def count(self) -> float:
        return self.__count

    @count.setter
    def count(self, count: float):
        self.__count = count

    @property
    def oaam_library_Resource100(self):
        return self.__oaam_library_Resource100

    @oaam_library_Resource100.setter
    def oaam_library_Resource100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_Resource__oaam_library_Resource100", None)
        self.__oaam_library_Resource100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ResourceTypeModifierLevel101"):
                    opp_val = getattr(item, "ResourceTypeModifierLevel101", None)
                    
                    if opp_val == self:
                        setattr(item, "ResourceTypeModifierLevel101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ResourceTypeModifierLevel101"):
                    opp_val = getattr(item, "ResourceTypeModifierLevel101", None)
                    
                    setattr(item, "ResourceTypeModifierLevel101", self)
                    

    @property
    def oaam_library_Resource(self):
        return self.__oaam_library_Resource

    @oaam_library_Resource.setter
    def oaam_library_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_Resource__oaam_library_Resource", None)
        self.__oaam_library_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceType98"):
                opp_val = getattr(old_value, "ResourceType98", None)
                if opp_val == self:
                    setattr(old_value, "ResourceType98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceType98"):
                opp_val = getattr(value, "ResourceType98", None)
                setattr(value, "ResourceType98", self)

class oaam_library_PowerSource(OaamBaseElementA):

    pass
class oaam_capabilities_ResourceConsumption(OaamBaseElementA):

    def __init__(self, count: float, oaam_capabilities_ResourceConsumption: set["Resource"] = None, oaam_capabilities_ResourceConsumption489: "ResourceType" = None, OaamBaseElementA: "oaam_common_AttributeContainment", OaamBaseElementA23: "oaam_common_AttributeReference"):
        self.count = count
        self.oaam_capabilities_ResourceConsumption = oaam_capabilities_ResourceConsumption if oaam_capabilities_ResourceConsumption is not None else set()
        self.oaam_capabilities_ResourceConsumption489 = oaam_capabilities_ResourceConsumption489
        
    @property
    def count(self) -> float:
        return self.__count

    @count.setter
    def count(self, count: float):
        self.__count = count

    @property
    def oaam_capabilities_ResourceConsumption(self):
        return self.__oaam_capabilities_ResourceConsumption

    @oaam_capabilities_ResourceConsumption.setter
    def oaam_capabilities_ResourceConsumption(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_capabilities_ResourceConsumption__oaam_capabilities_ResourceConsumption", None)
        self.__oaam_capabilities_ResourceConsumption = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Resource487"):
                    opp_val = getattr(item, "Resource487", None)
                    
                    if opp_val == self:
                        setattr(item, "Resource487", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Resource487"):
                    opp_val = getattr(item, "Resource487", None)
                    
                    setattr(item, "Resource487", self)
                    

    @property
    def oaam_capabilities_ResourceConsumption489(self):
        return self.__oaam_capabilities_ResourceConsumption489

    @oaam_capabilities_ResourceConsumption489.setter
    def oaam_capabilities_ResourceConsumption489(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_capabilities_ResourceConsumption__oaam_capabilities_ResourceConsumption489", None)
        self.__oaam_capabilities_ResourceConsumption489 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceType490"):
                opp_val = getattr(old_value, "ResourceType490", None)
                if opp_val == self:
                    setattr(old_value, "ResourceType490", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceType490"):
                opp_val = getattr(value, "ResourceType490", None)
                setattr(value, "ResourceType490", self)

class oaam_library_ResourceAlternatives(OaamBaseElementA):

    pass
class oaam_systems_SystemsContainerA(OaamBaseElementA):

    pass
class oaam_library_ResourceTypeModifierReference(OaamBaseElementA):

    pass
class oaam_library_TaskParameterDeclaration(OaamBaseElementA):

    pass
class oaam_common_DataTypeA(OaamBaseElementA):

    pass
class oaam_library_TaskTypeDissimilarity(OaamBaseElementA):

    def __init__(self, percentageOfCommonCode: float, oaam_library_TaskTypeDissimilarity: set["TaskType"] = None, OaamBaseElementA: "oaam_common_AttributeContainment", OaamBaseElementA23: "oaam_common_AttributeReference"):
        self.percentageOfCommonCode = percentageOfCommonCode
        self.oaam_library_TaskTypeDissimilarity = oaam_library_TaskTypeDissimilarity if oaam_library_TaskTypeDissimilarity is not None else set()
        
    @property
    def percentageOfCommonCode(self) -> float:
        return self.__percentageOfCommonCode

    @percentageOfCommonCode.setter
    def percentageOfCommonCode(self, percentageOfCommonCode: float):
        self.__percentageOfCommonCode = percentageOfCommonCode

    @property
    def oaam_library_TaskTypeDissimilarity(self):
        return self.__oaam_library_TaskTypeDissimilarity

    @oaam_library_TaskTypeDissimilarity.setter
    def oaam_library_TaskTypeDissimilarity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_TaskTypeDissimilarity__oaam_library_TaskTypeDissimilarity", None)
        self.__oaam_library_TaskTypeDissimilarity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaskType180"):
                    opp_val = getattr(item, "TaskType180", None)
                    
                    if opp_val == self:
                        setattr(item, "TaskType180", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaskType180"):
                    opp_val = getattr(item, "TaskType180", None)
                    
                    setattr(item, "TaskType180", self)
                    

class oaam_library_AttributeDefinition(OaamBaseElementA):

    def __init__(self, dataType: str, target: str, OaamBaseElementA: "oaam_common_AttributeContainment", OaamBaseElementA23: "oaam_common_AttributeReference"):
        self.dataType = dataType
        self.target = target
        
    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

class oaam_library_InputDeclaration(OaamBaseElementA):

    def __init__(self, unit: str, precondition: str, range: str, lowerBound: int, upperBound: int, oaam_library_InputDeclaration: "DataTypeA" = None, OaamBaseElementA: "oaam_common_AttributeContainment", OaamBaseElementA23: "oaam_common_AttributeReference"):
        self.unit = unit
        self.precondition = precondition
        self.range = range
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.oaam_library_InputDeclaration = oaam_library_InputDeclaration
        
    @property
    def precondition(self) -> str:
        return self.__precondition

    @precondition.setter
    def precondition(self, precondition: str):
        self.__precondition = precondition

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def range(self) -> str:
        return self.__range

    @range.setter
    def range(self, range: str):
        self.__range = range

    @property
    def oaam_library_InputDeclaration(self):
        return self.__oaam_library_InputDeclaration

    @oaam_library_InputDeclaration.setter
    def oaam_library_InputDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oaam_library_InputDeclaration__oaam_library_InputDeclaration", None)
        self.__oaam_library_InputDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataTypeA134"):
                opp_val = getattr(old_value, "DataTypeA134", None)
                if opp_val == self:
                    setattr(old_value, "DataTypeA134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataTypeA134"):
                opp_val = getattr(value, "DataTypeA134", None)
                setattr(value, "DataTypeA134", self)

class oaam_Architecture(OaamBaseElementA):

    pass