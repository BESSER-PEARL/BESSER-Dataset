import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    oaam_allocations_SignalToMessageAssignment,
    allocations_AllocationsContainerA,
    AllocationsContainerA,
    oaam_allocations_Allocations,
    MessageSegment,
    SignalToMessageAssignment,
    Submessage,
    MessageA,
    oaam_allocations_Submessage,
    oaam_allocations_Message,
    ScheduledTime,
    ConnectionAssignmentSegment,
    Area,
    Duct,
    LocationSymmetry,
    Position3D,
    AreaSymmetry,
    Subanatomy,
    hardware_HardwareContainerA,
    library_ResourceProviderInstanceA,
    Bus,
    Subhardware,
    DeviceSymmetry,
    Location,
    Connection,
    ExternalOutputLink,
    Io,
    OutputIntegrityState,
    Output,
    Input,
    Subfunctions,
    FailureCondition,
    TaskParameter,
    Device,
    ExternalTaskLink,
    Task,
    FunctionsContainerA,
    oaam_functions_Subfunctions,
    oaam_functions_Functions,
    SignalGroup,
    Signal,
    TaskRedundancy,
    TaskSymmetry,
    TaskGroup,
    InformationPower,
    oaam_systems_HydraulicPower,
    oaam_systems_RotaryPower,
    oaam_systems_ElectricPower,
    oaam_systems_LinearPower,
    systems_RequiredInformationA,
    systems_ProvidedInformationA,
    oaam_systems_ProvidedInformationA,
    oaam_systems_RequiredInformationA,
    RequiredInformationA,
    Subsystem,
    InputSegregation,
    InformationFlow,
    System,
    ScenarioContainerA,
    oaam_scenario_Subscenario,
    oaam_scenario_Scenario,
    ProvidedInformationA,
    systems_SystemsContainerA,
    SystemsContainerA,
    oaam_systems_Systems,
    scenario_ScenarioParameterA,
    Subscenario,
    OperationMode,
    scenario_VariantDependentElementA,
    scenario_ModeDependentElementA,
    oaam_systems_Subsystem,
    oaam_hardware_Subhardware,
    oaam_hardware_Hardware,
    oaam_allocations_Suballocations,
    oaam_scenario_ScenarioParameterA,
    LibraryContainerA,
    oaam_library_Sublibrary,
    oaam_library_Library,
    ScenarioParameterA,
    Variant,
    oaam_scenario_VariantDependentElementA,
    OperationModeReference,
    oaam_scenario_ModeDependentElementA,
    TaskInputTrigger,
    TaskInputState,
    BoolNot,
    BoolOperation,
    FaultPropagation,
    TaskOutputTrigger,
    DuctOpeningDeclaration,
    IoGroup,
    TaskParameterDeclaration,
    TaskStateDeclaration,
    InputDeclaration,
    OutputDeclaration,
    IoDeclaration,
    library_ResourceProviderA,
    ResourceAlternatives,
    ResourceTypeModifierReference,
    library_ResourceConsumerA,
    MessageType,
    BusType,
    IoType,
    LocationType,
    WireType,
    ConnectionType,
    DeviceTypeDissimilarity,
    Sublibrary,
    Message,
    SubconnectionAssignment,
    SignalAssignmentSegment,
    Schedule,
    SubdeviceAssignment,
    DeviceAssignment,
    Suballocations,
    SignalAssignment,
    TaskAssignment,
    ConnectionAssignment,
    restrictions_RestrictionsContainerA,
    oaam_restrictions_Subrestrictions,
    restrictions_ConnectionRestrinctionA,
    restrictions_DeviceRestrictionA,
    restrictions_SubfunctionRestrictionA,
    restrictions_SignalGroupRestrictionA,
    restrictions_SignalRestrictionA,
    restrictions_TaskGroupRestrictionA,
    restrictions_TaskRestrictionA,
    oaam_restrictions_SignalGroupRestrictionA,
    oaam_restrictions_TaskGroupRestrictionA,
    oaam_restrictions_SubfunctionRestrictionA,
    oaam_restrictions_DeviceRestrictionA,
    RestrictionsContainerA,
    oaam_restrictions_Restrictions,
    TimeDelayRestriction,
    Subrestrictions,
    SegregationRestriction,
    ConnectionTypeRestriction,
    ConnectionRestriction,
    oaam_restrictions_SignalRestrictionA,
    oaam_restrictions_TaskRestrictionA,
    oaam_restrictions_ConnectionRestrinctionA,
    PowerSourceRestriction,
    AreaRestriction,
    LocationRestriction,
    DeviceRestriction,
    DeviceTypeRestriction,
    SynchronicityRestriction,
    TaskSymmetryRestriction,
    TaskAtomicRestriction,
    capabilities_CapabilitiesContainerA,
    oaam_capabilities_Subcapabilities,
    CapabilitiesContainerA,
    oaam_capabilities_Capabilities,
    capabilities_CapabilityA,
    MessageOnConnectionOrDeviceCapability,
    Subcapabilities,
    ConnectionInDuctOrLocationCapability,
    SubdeviceInDeviceCapability,
    DeviceInLocationCapability,
    SignalOnConnectionOrDeviceCapability,
    TaskOnDeviceCapability,
    ResourceConsumption,
    oaam_capabilities_CapabilityA,
    SignalInMessageCapability,
    SubmessageInMessageCapability,
    MessageOnBusCapability,
    SubconnectionInDeviceCapability,
    AnatomyContainerA,
    oaam_anatomy_Anatomy,
    anatomy_AnatomyContainerA,
    oaam_anatomy_Subanatomy,
    DuctOpening,
    DeviceTypeSymmetry,
    PowerSource,
    AttributeDefinition,
    DuctType,
    TaskTypeDissimilarity,
    TaskType,
    ResourceTypeDissimilarity,
    ResourceTypeModifier,
    DeviceType,
    SignalType,
    ResourceTypeModifierLevel,
    oaam_library_ResourceProviderInstanceA,
    ResourceLink,
    ResourceType,
    ResourceBundle,
    oaam_library_ResourceProviderA,
    oaam_library_ResourceConsumerA,
    ResourceGroup,
    Resource,
    Struct,
    DataTypeA,
    oaam_common_Array,
    oaam_common_Byte,
    oaam_common_Character,
    oaam_common_Boolean,
    oaam_common_Struct,
    oaam_common_FloatingPoint,
    oaam_common_Integer,
    BoolA,
    common_OaamBaseElementA,
    oaam_allocations_DeviceAssignment,
    oaam_functions_Signal,
    oaam_restrictions_ConnectionRestriction,
    oaam_capabilities_MessageOnBusCapability,
    oaam_anatomy_DuctOpening,
    oaam_hardware_Connection,
    oaam_allocations_Schedule,
    oaam_scenario_OperationMode,
    oaam_library_ResourceTypeModifierLevel,
    oaam_library_TaskType,
    oaam_anatomy_Location,
    oaam_capabilities_SubconnectionInDeviceCapability,
    oaam_restrictions_ConnectionTypeRestriction,
    oaam_hardware_Device,
    oaam_allocations_ScheduledTime,
    oaam_functions_Task,
    oaam_systems_InformationPower,
    oaam_allocations_MessageSegment,
    oaam_capabilities_DeviceInLocationCapability,
    oaam_scenario_ScenarioParameterNumeric,
    oaam_systems_InformationMaterial,
    oaam_systems_System,
    oaam_restrictions_DeviceRestriction,
    oaam_functions_TaskGroup,
    oaam_capabilities_SubdeviceInDeviceCapability,
    oaam_scenario_Variant,
    oaam_hardware_Io,
    oaam_systems_InformationSignal,
    oaam_allocations_ConnectionAssignment,
    oaam_restrictions_SynchronicityRestriction,
    oaam_functions_ExternalTaskLink,
    oaam_library_MessageType,
    oaam_functions_FunctionsContainerA,
    oaam_allocations_SignalAssignment,
    oaam_anatomy_AreaSymmetry,
    oaam_anatomy_Area,
    oaam_hardware_Bus,
    oaam_restrictions_LocationRestriction,
    oaam_allocations_SubconnectionAssignment,
    oaam_hardware_DeviceSymmetry,
    oaam_library_LocationType,
    oaam_capabilities_SignalOnConnectionOrDeviceCapability,
    oaam_capabilities_TaskOnDeviceCapability,
    oaam_library_DeviceType,
    oaam_restrictions_TaskAtomicRestriction,
    oaam_functions_Input,
    oaam_capabilities_SubmessageInMessageCapability,
    oaam_restrictions_DeviceTypeRestriction,
    oaam_functions_ExternalOutputLink,
    oaam_anatomy_Position3D,
    oaam_library_ConnectionType,
    oaam_allocations_MessageA,
    oaam_functions_TaskRedundancy,
    oaam_library_BusType,
    oaam_capabilities_ConnectionInDuctOrLocationCapability,
    oaam_scenario_ScenarioParameterBool,
    oaam_functions_Output,
    oaam_allocations_SignalAssignmentSegment,
    oaam_allocations_ConnectionAssignmentSegment,
    oaam_restrictions_TimeDelayRestriction,
    oaam_allocations_SubdeviceAssignment,
    oaam_functions_TaskSymmetry,
    oaam_library_DuctType,
    oaam_library_SignalType,
    oaam_restrictions_TaskSymmetryRestriction,
    oaam_library_ResourceBundle,
    oaam_restrictions_PowerSourceRestriction,
    oaam_functions_SignalGroup,
    oaam_systems_InformationFlow,
    oaam_allocations_TaskAssignment,
    oaam_anatomy_Duct,
    oaam_restrictions_SegregationRestriction,
    oaam_anatomy_LocationSymmetry,
    oaam_restrictions_AreaRestriction,
    oaam_capabilities_MessageOnConnectionOrDeviceCapability,
    oaam_library_ResourceType,
    oaam_functions_FailureCondition,
    oaam_capabilities_SignalInMessageCapability,
    common_BoolA,
    oaam_library_TaskInputState,
    oaam_functions_OutputIntegrityState,
    oaam_library_TaskInputTrigger,
    oaam_common_BoolNot,
    oaam_common_BoolOperation,
    oaam_common_BoolA,
    AttributeA,
    oaam_common_AttributeNumeric,
    oaam_common_AttributeString,
    oaam_common_AttributeReference,
    oaam_common_AttributeContainment,
    Allocations,
    Restrictions,
    Capabilities,
    Anatomy,
    Hardware,
    Functions,
    oaam_common_OaamBaseElementA,
    Library,
    OaamBaseElementA,
    oaam_library_PowerSource,
    oaam_library_DeviceTypeDissimilarity,
    oaam_library_Resource,
    oaam_library_ResourceTypeModifier,
    oaam_library_IoGroup,
    oaam_systems_SystemsContainerA,
    oaam_hardware_HardwareContainerA,
    oaam_scenario_ScenarioContainerA,
    oaam_scenario_OperationModeReference,
    oaam_systems_InputSegregation,
    oaam_restrictions_RestrictionsContainerA,
    oaam_library_ResourceAlternatives,
    oaam_library_DuctOpeningDeclaration,
    oaam_common_DataTypeA,
    oaam_library_TaskOutputTrigger,
    oaam_library_ResourceTypeDissimilarity,
    oaam_library_ResourceTypeModifierReference,
    oaam_capabilities_CapabilitiesContainerA,
    oaam_library_ResourceLink,
    oaam_library_DeviceTypeSymmetry,
    oaam_library_WireType,
    oaam_library_LibraryContainerA,
    oaam_library_TaskTypeDissimilarity,
    oaam_library_InputDeclaration,
    oaam_library_FaultPropagation,
    oaam_common_AttributeA,
    oaam_allocations_AllocationsContainerA,
    oaam_anatomy_AnatomyContainerA,
    oaam_functions_TaskParameter,
    oaam_library_AttributeDefinition,
    oaam_library_IoDeclaration,
    oaam_library_TaskParameterDeclaration,
    oaam_capabilities_ResourceConsumption,
    oaam_library_ResourceGroup,
    oaam_library_OutputDeclaration,
    oaam_library_TaskStateDeclaration,
    oaam_library_IoType,
    oaam_Architecture,
    Systems,
    Scenario,
    IoDirectionE,
    AttributeTargetsE,
    EndianessE,
    IntegretyStateE,
    BoolOperationTypesE,
    AttributeTypesE,
    SymmetryTypesE,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oaam_allocations_signaltomessageassignment_is_not_abstract():
    assert not inspect.isabstract(oaam_allocations_SignalToMessageAssignment)


def test_oaam_allocations_signaltomessageassignment_constructor_exists():
    assert callable(oaam_allocations_SignalToMessageAssignment.__init__)


def test_oaam_allocations_signaltomessageassignment_constructor_args():
    sig = inspect.signature(oaam_allocations_SignalToMessageAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_oaam_allocations_signaltomessageassignment_has_position():
    assert hasattr(oaam_allocations_SignalToMessageAssignment, "position")
    descriptor = None
    for klass in oaam_allocations_SignalToMessageAssignment.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_allocations_allocationscontainera_is_not_abstract():
    assert not inspect.isabstract(allocations_AllocationsContainerA)


def test_allocations_allocationscontainera_constructor_exists():
    assert callable(allocations_AllocationsContainerA.__init__)


def test_allocations_allocationscontainera_constructor_args():
    sig = inspect.signature(allocations_AllocationsContainerA.__init__)
    params = list(sig.parameters.keys())



def test_allocationscontainera_is_not_abstract():
    assert not inspect.isabstract(AllocationsContainerA)


def test_allocationscontainera_constructor_exists():
    assert callable(AllocationsContainerA.__init__)


def test_allocationscontainera_constructor_args():
    sig = inspect.signature(AllocationsContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_allocations_allocations_is_not_abstract():
    assert not inspect.isabstract(oaam_allocations_Allocations)


def test_oaam_allocations_allocations_constructor_exists():
    assert callable(oaam_allocations_Allocations.__init__)


def test_oaam_allocations_allocations_constructor_args():
    sig = inspect.signature(oaam_allocations_Allocations.__init__)
    params = list(sig.parameters.keys())



def test_messagesegment_is_not_abstract():
    assert not inspect.isabstract(MessageSegment)


def test_messagesegment_constructor_exists():
    assert callable(MessageSegment.__init__)


def test_messagesegment_constructor_args():
    sig = inspect.signature(MessageSegment.__init__)
    params = list(sig.parameters.keys())



def test_signaltomessageassignment_is_not_abstract():
    assert not inspect.isabstract(SignalToMessageAssignment)


def test_signaltomessageassignment_constructor_exists():
    assert callable(SignalToMessageAssignment.__init__)


def test_signaltomessageassignment_constructor_args():
    sig = inspect.signature(SignalToMessageAssignment.__init__)
    params = list(sig.parameters.keys())



def test_submessage_is_not_abstract():
    assert not inspect.isabstract(Submessage)


def test_submessage_constructor_exists():
    assert callable(Submessage.__init__)


def test_submessage_constructor_args():
    sig = inspect.signature(Submessage.__init__)
    params = list(sig.parameters.keys())



def test_messagea_is_not_abstract():
    assert not inspect.isabstract(MessageA)


def test_messagea_constructor_exists():
    assert callable(MessageA.__init__)


def test_messagea_constructor_args():
    sig = inspect.signature(MessageA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_allocations_submessage_is_not_abstract():
    assert not inspect.isabstract(oaam_allocations_Submessage)


def test_oaam_allocations_submessage_constructor_exists():
    assert callable(oaam_allocations_Submessage.__init__)


def test_oaam_allocations_submessage_constructor_args():
    sig = inspect.signature(oaam_allocations_Submessage.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_oaam_allocations_submessage_has_position():
    assert hasattr(oaam_allocations_Submessage, "position")
    descriptor = None
    for klass in oaam_allocations_Submessage.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_oaam_allocations_message_is_not_abstract():
    assert not inspect.isabstract(oaam_allocations_Message)


def test_oaam_allocations_message_constructor_exists():
    assert callable(oaam_allocations_Message.__init__)


def test_oaam_allocations_message_constructor_args():
    sig = inspect.signature(oaam_allocations_Message.__init__)
    params = list(sig.parameters.keys())



def test_scheduledtime_is_not_abstract():
    assert not inspect.isabstract(ScheduledTime)


def test_scheduledtime_constructor_exists():
    assert callable(ScheduledTime.__init__)


def test_scheduledtime_constructor_args():
    sig = inspect.signature(ScheduledTime.__init__)
    params = list(sig.parameters.keys())



def test_connectionassignmentsegment_is_not_abstract():
    assert not inspect.isabstract(ConnectionAssignmentSegment)


def test_connectionassignmentsegment_constructor_exists():
    assert callable(ConnectionAssignmentSegment.__init__)


def test_connectionassignmentsegment_constructor_args():
    sig = inspect.signature(ConnectionAssignmentSegment.__init__)
    params = list(sig.parameters.keys())



def test_area_is_not_abstract():
    assert not inspect.isabstract(Area)


def test_area_constructor_exists():
    assert callable(Area.__init__)


def test_area_constructor_args():
    sig = inspect.signature(Area.__init__)
    params = list(sig.parameters.keys())



def test_duct_is_not_abstract():
    assert not inspect.isabstract(Duct)


def test_duct_constructor_exists():
    assert callable(Duct.__init__)


def test_duct_constructor_args():
    sig = inspect.signature(Duct.__init__)
    params = list(sig.parameters.keys())



def test_locationsymmetry_is_not_abstract():
    assert not inspect.isabstract(LocationSymmetry)


def test_locationsymmetry_constructor_exists():
    assert callable(LocationSymmetry.__init__)


def test_locationsymmetry_constructor_args():
    sig = inspect.signature(LocationSymmetry.__init__)
    params = list(sig.parameters.keys())



def test_position3d_is_not_abstract():
    assert not inspect.isabstract(Position3D)


def test_position3d_constructor_exists():
    assert callable(Position3D.__init__)


def test_position3d_constructor_args():
    sig = inspect.signature(Position3D.__init__)
    params = list(sig.parameters.keys())



def test_areasymmetry_is_not_abstract():
    assert not inspect.isabstract(AreaSymmetry)


def test_areasymmetry_constructor_exists():
    assert callable(AreaSymmetry.__init__)


def test_areasymmetry_constructor_args():
    sig = inspect.signature(AreaSymmetry.__init__)
    params = list(sig.parameters.keys())



def test_subanatomy_is_not_abstract():
    assert not inspect.isabstract(Subanatomy)


def test_subanatomy_constructor_exists():
    assert callable(Subanatomy.__init__)


def test_subanatomy_constructor_args():
    sig = inspect.signature(Subanatomy.__init__)
    params = list(sig.parameters.keys())



def test_hardware_hardwarecontainera_is_not_abstract():
    assert not inspect.isabstract(hardware_HardwareContainerA)


def test_hardware_hardwarecontainera_constructor_exists():
    assert callable(hardware_HardwareContainerA.__init__)


def test_hardware_hardwarecontainera_constructor_args():
    sig = inspect.signature(hardware_HardwareContainerA.__init__)
    params = list(sig.parameters.keys())



def test_library_resourceproviderinstancea_is_not_abstract():
    assert not inspect.isabstract(library_ResourceProviderInstanceA)


def test_library_resourceproviderinstancea_constructor_exists():
    assert callable(library_ResourceProviderInstanceA.__init__)


def test_library_resourceproviderinstancea_constructor_args():
    sig = inspect.signature(library_ResourceProviderInstanceA.__init__)
    params = list(sig.parameters.keys())



def test_bus_is_not_abstract():
    assert not inspect.isabstract(Bus)


def test_bus_constructor_exists():
    assert callable(Bus.__init__)


def test_bus_constructor_args():
    sig = inspect.signature(Bus.__init__)
    params = list(sig.parameters.keys())



def test_subhardware_is_not_abstract():
    assert not inspect.isabstract(Subhardware)


def test_subhardware_constructor_exists():
    assert callable(Subhardware.__init__)


def test_subhardware_constructor_args():
    sig = inspect.signature(Subhardware.__init__)
    params = list(sig.parameters.keys())



def test_devicesymmetry_is_not_abstract():
    assert not inspect.isabstract(DeviceSymmetry)


def test_devicesymmetry_constructor_exists():
    assert callable(DeviceSymmetry.__init__)


def test_devicesymmetry_constructor_args():
    sig = inspect.signature(DeviceSymmetry.__init__)
    params = list(sig.parameters.keys())



def test_location_is_not_abstract():
    assert not inspect.isabstract(Location)


def test_location_constructor_exists():
    assert callable(Location.__init__)


def test_location_constructor_args():
    sig = inspect.signature(Location.__init__)
    params = list(sig.parameters.keys())



def test_connection_is_not_abstract():
    assert not inspect.isabstract(Connection)


def test_connection_constructor_exists():
    assert callable(Connection.__init__)


def test_connection_constructor_args():
    sig = inspect.signature(Connection.__init__)
    params = list(sig.parameters.keys())



def test_externaloutputlink_is_not_abstract():
    assert not inspect.isabstract(ExternalOutputLink)


def test_externaloutputlink_constructor_exists():
    assert callable(ExternalOutputLink.__init__)


def test_externaloutputlink_constructor_args():
    sig = inspect.signature(ExternalOutputLink.__init__)
    params = list(sig.parameters.keys())



def test_io_is_not_abstract():
    assert not inspect.isabstract(Io)


def test_io_constructor_exists():
    assert callable(Io.__init__)


def test_io_constructor_args():
    sig = inspect.signature(Io.__init__)
    params = list(sig.parameters.keys())



def test_outputintegritystate_is_not_abstract():
    assert not inspect.isabstract(OutputIntegrityState)


def test_outputintegritystate_constructor_exists():
    assert callable(OutputIntegrityState.__init__)


def test_outputintegritystate_constructor_args():
    sig = inspect.signature(OutputIntegrityState.__init__)
    params = list(sig.parameters.keys())



def test_output_is_not_abstract():
    assert not inspect.isabstract(Output)


def test_output_constructor_exists():
    assert callable(Output.__init__)


def test_output_constructor_args():
    sig = inspect.signature(Output.__init__)
    params = list(sig.parameters.keys())



def test_input_is_not_abstract():
    assert not inspect.isabstract(Input)


def test_input_constructor_exists():
    assert callable(Input.__init__)


def test_input_constructor_args():
    sig = inspect.signature(Input.__init__)
    params = list(sig.parameters.keys())



def test_subfunctions_is_not_abstract():
    assert not inspect.isabstract(Subfunctions)


def test_subfunctions_constructor_exists():
    assert callable(Subfunctions.__init__)


def test_subfunctions_constructor_args():
    sig = inspect.signature(Subfunctions.__init__)
    params = list(sig.parameters.keys())



def test_failurecondition_is_not_abstract():
    assert not inspect.isabstract(FailureCondition)


def test_failurecondition_constructor_exists():
    assert callable(FailureCondition.__init__)


def test_failurecondition_constructor_args():
    sig = inspect.signature(FailureCondition.__init__)
    params = list(sig.parameters.keys())



def test_taskparameter_is_not_abstract():
    assert not inspect.isabstract(TaskParameter)


def test_taskparameter_constructor_exists():
    assert callable(TaskParameter.__init__)


def test_taskparameter_constructor_args():
    sig = inspect.signature(TaskParameter.__init__)
    params = list(sig.parameters.keys())



def test_device_is_not_abstract():
    assert not inspect.isabstract(Device)


def test_device_constructor_exists():
    assert callable(Device.__init__)


def test_device_constructor_args():
    sig = inspect.signature(Device.__init__)
    params = list(sig.parameters.keys())



def test_externaltasklink_is_not_abstract():
    assert not inspect.isabstract(ExternalTaskLink)


def test_externaltasklink_constructor_exists():
    assert callable(ExternalTaskLink.__init__)


def test_externaltasklink_constructor_args():
    sig = inspect.signature(ExternalTaskLink.__init__)
    params = list(sig.parameters.keys())



def test_task_is_not_abstract():
    assert not inspect.isabstract(Task)


def test_task_constructor_exists():
    assert callable(Task.__init__)


def test_task_constructor_args():
    sig = inspect.signature(Task.__init__)
    params = list(sig.parameters.keys())



def test_functionscontainera_is_not_abstract():
    assert not inspect.isabstract(FunctionsContainerA)


def test_functionscontainera_constructor_exists():
    assert callable(FunctionsContainerA.__init__)


def test_functionscontainera_constructor_args():
    sig = inspect.signature(FunctionsContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_functions_subfunctions_is_not_abstract():
    assert not inspect.isabstract(oaam_functions_Subfunctions)


def test_oaam_functions_subfunctions_constructor_exists():
    assert callable(oaam_functions_Subfunctions.__init__)


def test_oaam_functions_subfunctions_constructor_args():
    sig = inspect.signature(oaam_functions_Subfunctions.__init__)
    params = list(sig.parameters.keys())
    assert "multiplicityMax" in params, "Missing parameter 'multiplicityMax'"
    assert "multiplicityMin" in params, "Missing parameter 'multiplicityMin'"

def test_oaam_functions_subfunctions_has_multiplicityMax():
    assert hasattr(oaam_functions_Subfunctions, "multiplicityMax")
    descriptor = None
    for klass in oaam_functions_Subfunctions.__mro__:
        if "multiplicityMax" in klass.__dict__:
            descriptor = klass.__dict__["multiplicityMax"]
            break
    assert isinstance(descriptor, property)

def test_oaam_functions_subfunctions_has_multiplicityMin():
    assert hasattr(oaam_functions_Subfunctions, "multiplicityMin")
    descriptor = None
    for klass in oaam_functions_Subfunctions.__mro__:
        if "multiplicityMin" in klass.__dict__:
            descriptor = klass.__dict__["multiplicityMin"]
            break
    assert isinstance(descriptor, property)



def test_oaam_functions_functions_is_not_abstract():
    assert not inspect.isabstract(oaam_functions_Functions)


def test_oaam_functions_functions_constructor_exists():
    assert callable(oaam_functions_Functions.__init__)


def test_oaam_functions_functions_constructor_args():
    sig = inspect.signature(oaam_functions_Functions.__init__)
    params = list(sig.parameters.keys())



def test_signalgroup_is_not_abstract():
    assert not inspect.isabstract(SignalGroup)


def test_signalgroup_constructor_exists():
    assert callable(SignalGroup.__init__)


def test_signalgroup_constructor_args():
    sig = inspect.signature(SignalGroup.__init__)
    params = list(sig.parameters.keys())



def test_signal_is_not_abstract():
    assert not inspect.isabstract(Signal)


def test_signal_constructor_exists():
    assert callable(Signal.__init__)


def test_signal_constructor_args():
    sig = inspect.signature(Signal.__init__)
    params = list(sig.parameters.keys())



def test_taskredundancy_is_not_abstract():
    assert not inspect.isabstract(TaskRedundancy)


def test_taskredundancy_constructor_exists():
    assert callable(TaskRedundancy.__init__)


def test_taskredundancy_constructor_args():
    sig = inspect.signature(TaskRedundancy.__init__)
    params = list(sig.parameters.keys())



def test_tasksymmetry_is_not_abstract():
    assert not inspect.isabstract(TaskSymmetry)


def test_tasksymmetry_constructor_exists():
    assert callable(TaskSymmetry.__init__)


def test_tasksymmetry_constructor_args():
    sig = inspect.signature(TaskSymmetry.__init__)
    params = list(sig.parameters.keys())



def test_taskgroup_is_not_abstract():
    assert not inspect.isabstract(TaskGroup)


def test_taskgroup_constructor_exists():
    assert callable(TaskGroup.__init__)


def test_taskgroup_constructor_args():
    sig = inspect.signature(TaskGroup.__init__)
    params = list(sig.parameters.keys())



def test_informationpower_is_not_abstract():
    assert not inspect.isabstract(InformationPower)


def test_informationpower_constructor_exists():
    assert callable(InformationPower.__init__)


def test_informationpower_constructor_args():
    sig = inspect.signature(InformationPower.__init__)
    params = list(sig.parameters.keys())



def test_oaam_systems_hydraulicpower_is_not_abstract():
    assert not inspect.isabstract(oaam_systems_HydraulicPower)


def test_oaam_systems_hydraulicpower_constructor_exists():
    assert callable(oaam_systems_HydraulicPower.__init__)


def test_oaam_systems_hydraulicpower_constructor_args():
    sig = inspect.signature(oaam_systems_HydraulicPower.__init__)
    params = list(sig.parameters.keys())
    assert "massFlowRate" in params, "Missing parameter 'massFlowRate'"
    assert "pressure" in params, "Missing parameter 'pressure'"

def test_oaam_systems_hydraulicpower_has_massFlowRate():
    assert hasattr(oaam_systems_HydraulicPower, "massFlowRate")
    descriptor = None
    for klass in oaam_systems_HydraulicPower.__mro__:
        if "massFlowRate" in klass.__dict__:
            descriptor = klass.__dict__["massFlowRate"]
            break
    assert isinstance(descriptor, property)

def test_oaam_systems_hydraulicpower_has_pressure():
    assert hasattr(oaam_systems_HydraulicPower, "pressure")
    descriptor = None
    for klass in oaam_systems_HydraulicPower.__mro__:
        if "pressure" in klass.__dict__:
            descriptor = klass.__dict__["pressure"]
            break
    assert isinstance(descriptor, property)



def test_oaam_systems_rotarypower_is_not_abstract():
    assert not inspect.isabstract(oaam_systems_RotaryPower)


def test_oaam_systems_rotarypower_constructor_exists():
    assert callable(oaam_systems_RotaryPower.__init__)


def test_oaam_systems_rotarypower_constructor_args():
    sig = inspect.signature(oaam_systems_RotaryPower.__init__)
    params = list(sig.parameters.keys())
    assert "momentum" in params, "Missing parameter 'momentum'"
    assert "angularVelocity" in params, "Missing parameter 'angularVelocity'"

def test_oaam_systems_rotarypower_has_momentum():
    assert hasattr(oaam_systems_RotaryPower, "momentum")
    descriptor = None
    for klass in oaam_systems_RotaryPower.__mro__:
        if "momentum" in klass.__dict__:
            descriptor = klass.__dict__["momentum"]
            break
    assert isinstance(descriptor, property)

def test_oaam_systems_rotarypower_has_angularVelocity():
    assert hasattr(oaam_systems_RotaryPower, "angularVelocity")
    descriptor = None
    for klass in oaam_systems_RotaryPower.__mro__:
        if "angularVelocity" in klass.__dict__:
            descriptor = klass.__dict__["angularVelocity"]
            break
    assert isinstance(descriptor, property)



def test_oaam_systems_electricpower_is_not_abstract():
    assert not inspect.isabstract(oaam_systems_ElectricPower)


def test_oaam_systems_electricpower_constructor_exists():
    assert callable(oaam_systems_ElectricPower.__init__)


def test_oaam_systems_electricpower_constructor_args():
    sig = inspect.signature(oaam_systems_ElectricPower.__init__)
    params = list(sig.parameters.keys())
    assert "voltage" in params, "Missing parameter 'voltage'"
    assert "nPhases" in params, "Missing parameter 'nPhases'"
    assert "frequency" in params, "Missing parameter 'frequency'"
    assert "current" in params, "Missing parameter 'current'"

def test_oaam_systems_electricpower_has_voltage():
    assert hasattr(oaam_systems_ElectricPower, "voltage")
    descriptor = None
    for klass in oaam_systems_ElectricPower.__mro__:
        if "voltage" in klass.__dict__:
            descriptor = klass.__dict__["voltage"]
            break
    assert isinstance(descriptor, property)

def test_oaam_systems_electricpower_has_nPhases():
    assert hasattr(oaam_systems_ElectricPower, "nPhases")
    descriptor = None
    for klass in oaam_systems_ElectricPower.__mro__:
        if "nPhases" in klass.__dict__:
            descriptor = klass.__dict__["nPhases"]
            break
    assert isinstance(descriptor, property)

def test_oaam_systems_electricpower_has_frequency():
    assert hasattr(oaam_systems_ElectricPower, "frequency")
    descriptor = None
    for klass in oaam_systems_ElectricPower.__mro__:
        if "frequency" in klass.__dict__:
            descriptor = klass.__dict__["frequency"]
            break
    assert isinstance(descriptor, property)

def test_oaam_systems_electricpower_has_current():
    assert hasattr(oaam_systems_ElectricPower, "current")
    descriptor = None
    for klass in oaam_systems_ElectricPower.__mro__:
        if "current" in klass.__dict__:
            descriptor = klass.__dict__["current"]
            break
    assert isinstance(descriptor, property)



def test_oaam_systems_linearpower_is_not_abstract():
    assert not inspect.isabstract(oaam_systems_LinearPower)


def test_oaam_systems_linearpower_constructor_exists():
    assert callable(oaam_systems_LinearPower.__init__)


def test_oaam_systems_linearpower_constructor_args():
    sig = inspect.signature(oaam_systems_LinearPower.__init__)
    params = list(sig.parameters.keys())
    assert "velocity" in params, "Missing parameter 'velocity'"
    assert "force" in params, "Missing parameter 'force'"

def test_oaam_systems_linearpower_has_velocity():
    assert hasattr(oaam_systems_LinearPower, "velocity")
    descriptor = None
    for klass in oaam_systems_LinearPower.__mro__:
        if "velocity" in klass.__dict__:
            descriptor = klass.__dict__["velocity"]
            break
    assert isinstance(descriptor, property)

def test_oaam_systems_linearpower_has_force():
    assert hasattr(oaam_systems_LinearPower, "force")
    descriptor = None
    for klass in oaam_systems_LinearPower.__mro__:
        if "force" in klass.__dict__:
            descriptor = klass.__dict__["force"]
            break
    assert isinstance(descriptor, property)



def test_systems_requiredinformationa_is_not_abstract():
    assert not inspect.isabstract(systems_RequiredInformationA)


def test_systems_requiredinformationa_constructor_exists():
    assert callable(systems_RequiredInformationA.__init__)


def test_systems_requiredinformationa_constructor_args():
    sig = inspect.signature(systems_RequiredInformationA.__init__)
    params = list(sig.parameters.keys())



def test_systems_providedinformationa_is_not_abstract():
    assert not inspect.isabstract(systems_ProvidedInformationA)


def test_systems_providedinformationa_constructor_exists():
    assert callable(systems_ProvidedInformationA.__init__)


def test_systems_providedinformationa_constructor_args():
    sig = inspect.signature(systems_ProvidedInformationA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_systems_providedinformationa_is_not_abstract():
    assert not inspect.isabstract(oaam_systems_ProvidedInformationA)


def test_oaam_systems_providedinformationa_constructor_exists():
    assert callable(oaam_systems_ProvidedInformationA.__init__)


def test_oaam_systems_providedinformationa_constructor_args():
    sig = inspect.signature(oaam_systems_ProvidedInformationA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_systems_requiredinformationa_is_not_abstract():
    assert not inspect.isabstract(oaam_systems_RequiredInformationA)


def test_oaam_systems_requiredinformationa_constructor_exists():
    assert callable(oaam_systems_RequiredInformationA.__init__)


def test_oaam_systems_requiredinformationa_constructor_args():
    sig = inspect.signature(oaam_systems_RequiredInformationA.__init__)
    params = list(sig.parameters.keys())



def test_requiredinformationa_is_not_abstract():
    assert not inspect.isabstract(RequiredInformationA)


def test_requiredinformationa_constructor_exists():
    assert callable(RequiredInformationA.__init__)


def test_requiredinformationa_constructor_args():
    sig = inspect.signature(RequiredInformationA.__init__)
    params = list(sig.parameters.keys())



def test_subsystem_is_not_abstract():
    assert not inspect.isabstract(Subsystem)


def test_subsystem_constructor_exists():
    assert callable(Subsystem.__init__)


def test_subsystem_constructor_args():
    sig = inspect.signature(Subsystem.__init__)
    params = list(sig.parameters.keys())



def test_inputsegregation_is_not_abstract():
    assert not inspect.isabstract(InputSegregation)


def test_inputsegregation_constructor_exists():
    assert callable(InputSegregation.__init__)


def test_inputsegregation_constructor_args():
    sig = inspect.signature(InputSegregation.__init__)
    params = list(sig.parameters.keys())



def test_informationflow_is_not_abstract():
    assert not inspect.isabstract(InformationFlow)


def test_informationflow_constructor_exists():
    assert callable(InformationFlow.__init__)


def test_informationflow_constructor_args():
    sig = inspect.signature(InformationFlow.__init__)
    params = list(sig.parameters.keys())



def test_system_is_not_abstract():
    assert not inspect.isabstract(System)


def test_system_constructor_exists():
    assert callable(System.__init__)


def test_system_constructor_args():
    sig = inspect.signature(System.__init__)
    params = list(sig.parameters.keys())



def test_scenariocontainera_is_not_abstract():
    assert not inspect.isabstract(ScenarioContainerA)


def test_scenariocontainera_constructor_exists():
    assert callable(ScenarioContainerA.__init__)


def test_scenariocontainera_constructor_args():
    sig = inspect.signature(ScenarioContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_scenario_subscenario_is_not_abstract():
    assert not inspect.isabstract(oaam_scenario_Subscenario)


def test_oaam_scenario_subscenario_constructor_exists():
    assert callable(oaam_scenario_Subscenario.__init__)


def test_oaam_scenario_subscenario_constructor_args():
    sig = inspect.signature(oaam_scenario_Subscenario.__init__)
    params = list(sig.parameters.keys())



def test_oaam_scenario_scenario_is_not_abstract():
    assert not inspect.isabstract(oaam_scenario_Scenario)


def test_oaam_scenario_scenario_constructor_exists():
    assert callable(oaam_scenario_Scenario.__init__)


def test_oaam_scenario_scenario_constructor_args():
    sig = inspect.signature(oaam_scenario_Scenario.__init__)
    params = list(sig.parameters.keys())



def test_providedinformationa_is_not_abstract():
    assert not inspect.isabstract(ProvidedInformationA)


def test_providedinformationa_constructor_exists():
    assert callable(ProvidedInformationA.__init__)


def test_providedinformationa_constructor_args():
    sig = inspect.signature(ProvidedInformationA.__init__)
    params = list(sig.parameters.keys())



def test_systems_systemscontainera_is_not_abstract():
    assert not inspect.isabstract(systems_SystemsContainerA)


def test_systems_systemscontainera_constructor_exists():
    assert callable(systems_SystemsContainerA.__init__)


def test_systems_systemscontainera_constructor_args():
    sig = inspect.signature(systems_SystemsContainerA.__init__)
    params = list(sig.parameters.keys())



def test_systemscontainera_is_not_abstract():
    assert not inspect.isabstract(SystemsContainerA)


def test_systemscontainera_constructor_exists():
    assert callable(SystemsContainerA.__init__)


def test_systemscontainera_constructor_args():
    sig = inspect.signature(SystemsContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_systems_systems_is_not_abstract():
    assert not inspect.isabstract(oaam_systems_Systems)


def test_oaam_systems_systems_constructor_exists():
    assert callable(oaam_systems_Systems.__init__)


def test_oaam_systems_systems_constructor_args():
    sig = inspect.signature(oaam_systems_Systems.__init__)
    params = list(sig.parameters.keys())



def test_scenario_scenarioparametera_is_not_abstract():
    assert not inspect.isabstract(scenario_ScenarioParameterA)


def test_scenario_scenarioparametera_constructor_exists():
    assert callable(scenario_ScenarioParameterA.__init__)


def test_scenario_scenarioparametera_constructor_args():
    sig = inspect.signature(scenario_ScenarioParameterA.__init__)
    params = list(sig.parameters.keys())



def test_subscenario_is_not_abstract():
    assert not inspect.isabstract(Subscenario)


def test_subscenario_constructor_exists():
    assert callable(Subscenario.__init__)


def test_subscenario_constructor_args():
    sig = inspect.signature(Subscenario.__init__)
    params = list(sig.parameters.keys())



def test_operationmode_is_not_abstract():
    assert not inspect.isabstract(OperationMode)


def test_operationmode_constructor_exists():
    assert callable(OperationMode.__init__)


def test_operationmode_constructor_args():
    sig = inspect.signature(OperationMode.__init__)
    params = list(sig.parameters.keys())



def test_scenario_variantdependentelementa_is_not_abstract():
    assert not inspect.isabstract(scenario_VariantDependentElementA)


def test_scenario_variantdependentelementa_constructor_exists():
    assert callable(scenario_VariantDependentElementA.__init__)


def test_scenario_variantdependentelementa_constructor_args():
    sig = inspect.signature(scenario_VariantDependentElementA.__init__)
    params = list(sig.parameters.keys())



def test_scenario_modedependentelementa_is_not_abstract():
    assert not inspect.isabstract(scenario_ModeDependentElementA)


def test_scenario_modedependentelementa_constructor_exists():
    assert callable(scenario_ModeDependentElementA.__init__)


def test_scenario_modedependentelementa_constructor_args():
    sig = inspect.signature(scenario_ModeDependentElementA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_systems_subsystem_is_not_abstract():
    assert not inspect.isabstract(oaam_systems_Subsystem)


def test_oaam_systems_subsystem_constructor_exists():
    assert callable(oaam_systems_Subsystem.__init__)


def test_oaam_systems_subsystem_constructor_args():
    sig = inspect.signature(oaam_systems_Subsystem.__init__)
    params = list(sig.parameters.keys())



def test_oaam_hardware_subhardware_is_not_abstract():
    assert not inspect.isabstract(oaam_hardware_Subhardware)


def test_oaam_hardware_subhardware_constructor_exists():
    assert callable(oaam_hardware_Subhardware.__init__)


def test_oaam_hardware_subhardware_constructor_args():
    sig = inspect.signature(oaam_hardware_Subhardware.__init__)
    params = list(sig.parameters.keys())



def test_oaam_hardware_hardware_is_not_abstract():
    assert not inspect.isabstract(oaam_hardware_Hardware)


def test_oaam_hardware_hardware_constructor_exists():
    assert callable(oaam_hardware_Hardware.__init__)


def test_oaam_hardware_hardware_constructor_args():
    sig = inspect.signature(oaam_hardware_Hardware.__init__)
    params = list(sig.parameters.keys())



def test_oaam_allocations_suballocations_is_not_abstract():
    assert not inspect.isabstract(oaam_allocations_Suballocations)


def test_oaam_allocations_suballocations_constructor_exists():
    assert callable(oaam_allocations_Suballocations.__init__)


def test_oaam_allocations_suballocations_constructor_args():
    sig = inspect.signature(oaam_allocations_Suballocations.__init__)
    params = list(sig.parameters.keys())



def test_oaam_scenario_scenarioparametera_is_not_abstract():
    assert not inspect.isabstract(oaam_scenario_ScenarioParameterA)


def test_oaam_scenario_scenarioparametera_constructor_exists():
    assert callable(oaam_scenario_ScenarioParameterA.__init__)


def test_oaam_scenario_scenarioparametera_constructor_args():
    sig = inspect.signature(oaam_scenario_ScenarioParameterA.__init__)
    params = list(sig.parameters.keys())



def test_librarycontainera_is_not_abstract():
    assert not inspect.isabstract(LibraryContainerA)


def test_librarycontainera_constructor_exists():
    assert callable(LibraryContainerA.__init__)


def test_librarycontainera_constructor_args():
    sig = inspect.signature(LibraryContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_sublibrary_is_not_abstract():
    assert not inspect.isabstract(oaam_library_Sublibrary)


def test_oaam_library_sublibrary_constructor_exists():
    assert callable(oaam_library_Sublibrary.__init__)


def test_oaam_library_sublibrary_constructor_args():
    sig = inspect.signature(oaam_library_Sublibrary.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_library_is_not_abstract():
    assert not inspect.isabstract(oaam_library_Library)


def test_oaam_library_library_constructor_exists():
    assert callable(oaam_library_Library.__init__)


def test_oaam_library_library_constructor_args():
    sig = inspect.signature(oaam_library_Library.__init__)
    params = list(sig.parameters.keys())



def test_scenarioparametera_is_not_abstract():
    assert not inspect.isabstract(ScenarioParameterA)


def test_scenarioparametera_constructor_exists():
    assert callable(ScenarioParameterA.__init__)


def test_scenarioparametera_constructor_args():
    sig = inspect.signature(ScenarioParameterA.__init__)
    params = list(sig.parameters.keys())



def test_variant_is_not_abstract():
    assert not inspect.isabstract(Variant)


def test_variant_constructor_exists():
    assert callable(Variant.__init__)


def test_variant_constructor_args():
    sig = inspect.signature(Variant.__init__)
    params = list(sig.parameters.keys())



def test_oaam_scenario_variantdependentelementa_is_not_abstract():
    assert not inspect.isabstract(oaam_scenario_VariantDependentElementA)


def test_oaam_scenario_variantdependentelementa_constructor_exists():
    assert callable(oaam_scenario_VariantDependentElementA.__init__)


def test_oaam_scenario_variantdependentelementa_constructor_args():
    sig = inspect.signature(oaam_scenario_VariantDependentElementA.__init__)
    params = list(sig.parameters.keys())



def test_operationmodereference_is_not_abstract():
    assert not inspect.isabstract(OperationModeReference)


def test_operationmodereference_constructor_exists():
    assert callable(OperationModeReference.__init__)


def test_operationmodereference_constructor_args():
    sig = inspect.signature(OperationModeReference.__init__)
    params = list(sig.parameters.keys())



def test_oaam_scenario_modedependentelementa_is_not_abstract():
    assert not inspect.isabstract(oaam_scenario_ModeDependentElementA)


def test_oaam_scenario_modedependentelementa_constructor_exists():
    assert callable(oaam_scenario_ModeDependentElementA.__init__)


def test_oaam_scenario_modedependentelementa_constructor_args():
    sig = inspect.signature(oaam_scenario_ModeDependentElementA.__init__)
    params = list(sig.parameters.keys())



def test_taskinputtrigger_is_not_abstract():
    assert not inspect.isabstract(TaskInputTrigger)


def test_taskinputtrigger_constructor_exists():
    assert callable(TaskInputTrigger.__init__)


def test_taskinputtrigger_constructor_args():
    sig = inspect.signature(TaskInputTrigger.__init__)
    params = list(sig.parameters.keys())



def test_taskinputstate_is_not_abstract():
    assert not inspect.isabstract(TaskInputState)


def test_taskinputstate_constructor_exists():
    assert callable(TaskInputState.__init__)


def test_taskinputstate_constructor_args():
    sig = inspect.signature(TaskInputState.__init__)
    params = list(sig.parameters.keys())



def test_boolnot_is_not_abstract():
    assert not inspect.isabstract(BoolNot)


def test_boolnot_constructor_exists():
    assert callable(BoolNot.__init__)


def test_boolnot_constructor_args():
    sig = inspect.signature(BoolNot.__init__)
    params = list(sig.parameters.keys())



def test_booloperation_is_not_abstract():
    assert not inspect.isabstract(BoolOperation)


def test_booloperation_constructor_exists():
    assert callable(BoolOperation.__init__)


def test_booloperation_constructor_args():
    sig = inspect.signature(BoolOperation.__init__)
    params = list(sig.parameters.keys())



def test_faultpropagation_is_not_abstract():
    assert not inspect.isabstract(FaultPropagation)


def test_faultpropagation_constructor_exists():
    assert callable(FaultPropagation.__init__)


def test_faultpropagation_constructor_args():
    sig = inspect.signature(FaultPropagation.__init__)
    params = list(sig.parameters.keys())



def test_taskoutputtrigger_is_not_abstract():
    assert not inspect.isabstract(TaskOutputTrigger)


def test_taskoutputtrigger_constructor_exists():
    assert callable(TaskOutputTrigger.__init__)


def test_taskoutputtrigger_constructor_args():
    sig = inspect.signature(TaskOutputTrigger.__init__)
    params = list(sig.parameters.keys())



def test_ductopeningdeclaration_is_not_abstract():
    assert not inspect.isabstract(DuctOpeningDeclaration)


def test_ductopeningdeclaration_constructor_exists():
    assert callable(DuctOpeningDeclaration.__init__)


def test_ductopeningdeclaration_constructor_args():
    sig = inspect.signature(DuctOpeningDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_iogroup_is_not_abstract():
    assert not inspect.isabstract(IoGroup)


def test_iogroup_constructor_exists():
    assert callable(IoGroup.__init__)


def test_iogroup_constructor_args():
    sig = inspect.signature(IoGroup.__init__)
    params = list(sig.parameters.keys())



def test_taskparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(TaskParameterDeclaration)


def test_taskparameterdeclaration_constructor_exists():
    assert callable(TaskParameterDeclaration.__init__)


def test_taskparameterdeclaration_constructor_args():
    sig = inspect.signature(TaskParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_taskstatedeclaration_is_not_abstract():
    assert not inspect.isabstract(TaskStateDeclaration)


def test_taskstatedeclaration_constructor_exists():
    assert callable(TaskStateDeclaration.__init__)


def test_taskstatedeclaration_constructor_args():
    sig = inspect.signature(TaskStateDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_inputdeclaration_is_not_abstract():
    assert not inspect.isabstract(InputDeclaration)


def test_inputdeclaration_constructor_exists():
    assert callable(InputDeclaration.__init__)


def test_inputdeclaration_constructor_args():
    sig = inspect.signature(InputDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_outputdeclaration_is_not_abstract():
    assert not inspect.isabstract(OutputDeclaration)


def test_outputdeclaration_constructor_exists():
    assert callable(OutputDeclaration.__init__)


def test_outputdeclaration_constructor_args():
    sig = inspect.signature(OutputDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_iodeclaration_is_not_abstract():
    assert not inspect.isabstract(IoDeclaration)


def test_iodeclaration_constructor_exists():
    assert callable(IoDeclaration.__init__)


def test_iodeclaration_constructor_args():
    sig = inspect.signature(IoDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_library_resourceprovidera_is_not_abstract():
    assert not inspect.isabstract(library_ResourceProviderA)


def test_library_resourceprovidera_constructor_exists():
    assert callable(library_ResourceProviderA.__init__)


def test_library_resourceprovidera_constructor_args():
    sig = inspect.signature(library_ResourceProviderA.__init__)
    params = list(sig.parameters.keys())



def test_resourcealternatives_is_not_abstract():
    assert not inspect.isabstract(ResourceAlternatives)


def test_resourcealternatives_constructor_exists():
    assert callable(ResourceAlternatives.__init__)


def test_resourcealternatives_constructor_args():
    sig = inspect.signature(ResourceAlternatives.__init__)
    params = list(sig.parameters.keys())



def test_resourcetypemodifierreference_is_not_abstract():
    assert not inspect.isabstract(ResourceTypeModifierReference)


def test_resourcetypemodifierreference_constructor_exists():
    assert callable(ResourceTypeModifierReference.__init__)


def test_resourcetypemodifierreference_constructor_args():
    sig = inspect.signature(ResourceTypeModifierReference.__init__)
    params = list(sig.parameters.keys())



def test_library_resourceconsumera_is_not_abstract():
    assert not inspect.isabstract(library_ResourceConsumerA)


def test_library_resourceconsumera_constructor_exists():
    assert callable(library_ResourceConsumerA.__init__)


def test_library_resourceconsumera_constructor_args():
    sig = inspect.signature(library_ResourceConsumerA.__init__)
    params = list(sig.parameters.keys())



def test_messagetype_is_not_abstract():
    assert not inspect.isabstract(MessageType)


def test_messagetype_constructor_exists():
    assert callable(MessageType.__init__)


def test_messagetype_constructor_args():
    sig = inspect.signature(MessageType.__init__)
    params = list(sig.parameters.keys())



def test_bustype_is_not_abstract():
    assert not inspect.isabstract(BusType)


def test_bustype_constructor_exists():
    assert callable(BusType.__init__)


def test_bustype_constructor_args():
    sig = inspect.signature(BusType.__init__)
    params = list(sig.parameters.keys())



def test_iotype_is_not_abstract():
    assert not inspect.isabstract(IoType)


def test_iotype_constructor_exists():
    assert callable(IoType.__init__)


def test_iotype_constructor_args():
    sig = inspect.signature(IoType.__init__)
    params = list(sig.parameters.keys())



def test_locationtype_is_not_abstract():
    assert not inspect.isabstract(LocationType)


def test_locationtype_constructor_exists():
    assert callable(LocationType.__init__)


def test_locationtype_constructor_args():
    sig = inspect.signature(LocationType.__init__)
    params = list(sig.parameters.keys())



def test_wiretype_is_not_abstract():
    assert not inspect.isabstract(WireType)


def test_wiretype_constructor_exists():
    assert callable(WireType.__init__)


def test_wiretype_constructor_args():
    sig = inspect.signature(WireType.__init__)
    params = list(sig.parameters.keys())



def test_connectiontype_is_not_abstract():
    assert not inspect.isabstract(ConnectionType)


def test_connectiontype_constructor_exists():
    assert callable(ConnectionType.__init__)


def test_connectiontype_constructor_args():
    sig = inspect.signature(ConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_devicetypedissimilarity_is_not_abstract():
    assert not inspect.isabstract(DeviceTypeDissimilarity)


def test_devicetypedissimilarity_constructor_exists():
    assert callable(DeviceTypeDissimilarity.__init__)


def test_devicetypedissimilarity_constructor_args():
    sig = inspect.signature(DeviceTypeDissimilarity.__init__)
    params = list(sig.parameters.keys())



def test_sublibrary_is_not_abstract():
    assert not inspect.isabstract(Sublibrary)


def test_sublibrary_constructor_exists():
    assert callable(Sublibrary.__init__)


def test_sublibrary_constructor_args():
    sig = inspect.signature(Sublibrary.__init__)
    params = list(sig.parameters.keys())



def test_message_is_not_abstract():
    assert not inspect.isabstract(Message)


def test_message_constructor_exists():
    assert callable(Message.__init__)


def test_message_constructor_args():
    sig = inspect.signature(Message.__init__)
    params = list(sig.parameters.keys())



def test_subconnectionassignment_is_not_abstract():
    assert not inspect.isabstract(SubconnectionAssignment)


def test_subconnectionassignment_constructor_exists():
    assert callable(SubconnectionAssignment.__init__)


def test_subconnectionassignment_constructor_args():
    sig = inspect.signature(SubconnectionAssignment.__init__)
    params = list(sig.parameters.keys())



def test_signalassignmentsegment_is_not_abstract():
    assert not inspect.isabstract(SignalAssignmentSegment)


def test_signalassignmentsegment_constructor_exists():
    assert callable(SignalAssignmentSegment.__init__)


def test_signalassignmentsegment_constructor_args():
    sig = inspect.signature(SignalAssignmentSegment.__init__)
    params = list(sig.parameters.keys())



def test_schedule_is_not_abstract():
    assert not inspect.isabstract(Schedule)


def test_schedule_constructor_exists():
    assert callable(Schedule.__init__)


def test_schedule_constructor_args():
    sig = inspect.signature(Schedule.__init__)
    params = list(sig.parameters.keys())



def test_subdeviceassignment_is_not_abstract():
    assert not inspect.isabstract(SubdeviceAssignment)


def test_subdeviceassignment_constructor_exists():
    assert callable(SubdeviceAssignment.__init__)


def test_subdeviceassignment_constructor_args():
    sig = inspect.signature(SubdeviceAssignment.__init__)
    params = list(sig.parameters.keys())



def test_deviceassignment_is_not_abstract():
    assert not inspect.isabstract(DeviceAssignment)


def test_deviceassignment_constructor_exists():
    assert callable(DeviceAssignment.__init__)


def test_deviceassignment_constructor_args():
    sig = inspect.signature(DeviceAssignment.__init__)
    params = list(sig.parameters.keys())



def test_suballocations_is_not_abstract():
    assert not inspect.isabstract(Suballocations)


def test_suballocations_constructor_exists():
    assert callable(Suballocations.__init__)


def test_suballocations_constructor_args():
    sig = inspect.signature(Suballocations.__init__)
    params = list(sig.parameters.keys())



def test_signalassignment_is_not_abstract():
    assert not inspect.isabstract(SignalAssignment)


def test_signalassignment_constructor_exists():
    assert callable(SignalAssignment.__init__)


def test_signalassignment_constructor_args():
    sig = inspect.signature(SignalAssignment.__init__)
    params = list(sig.parameters.keys())



def test_taskassignment_is_not_abstract():
    assert not inspect.isabstract(TaskAssignment)


def test_taskassignment_constructor_exists():
    assert callable(TaskAssignment.__init__)


def test_taskassignment_constructor_args():
    sig = inspect.signature(TaskAssignment.__init__)
    params = list(sig.parameters.keys())



def test_connectionassignment_is_not_abstract():
    assert not inspect.isabstract(ConnectionAssignment)


def test_connectionassignment_constructor_exists():
    assert callable(ConnectionAssignment.__init__)


def test_connectionassignment_constructor_args():
    sig = inspect.signature(ConnectionAssignment.__init__)
    params = list(sig.parameters.keys())



def test_restrictions_restrictionscontainera_is_not_abstract():
    assert not inspect.isabstract(restrictions_RestrictionsContainerA)


def test_restrictions_restrictionscontainera_constructor_exists():
    assert callable(restrictions_RestrictionsContainerA.__init__)


def test_restrictions_restrictionscontainera_constructor_args():
    sig = inspect.signature(restrictions_RestrictionsContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_restrictions_subrestrictions_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_Subrestrictions)


def test_oaam_restrictions_subrestrictions_constructor_exists():
    assert callable(oaam_restrictions_Subrestrictions.__init__)


def test_oaam_restrictions_subrestrictions_constructor_args():
    sig = inspect.signature(oaam_restrictions_Subrestrictions.__init__)
    params = list(sig.parameters.keys())



def test_restrictions_connectionrestrinctiona_is_not_abstract():
    assert not inspect.isabstract(restrictions_ConnectionRestrinctionA)


def test_restrictions_connectionrestrinctiona_constructor_exists():
    assert callable(restrictions_ConnectionRestrinctionA.__init__)


def test_restrictions_connectionrestrinctiona_constructor_args():
    sig = inspect.signature(restrictions_ConnectionRestrinctionA.__init__)
    params = list(sig.parameters.keys())



def test_restrictions_devicerestrictiona_is_not_abstract():
    assert not inspect.isabstract(restrictions_DeviceRestrictionA)


def test_restrictions_devicerestrictiona_constructor_exists():
    assert callable(restrictions_DeviceRestrictionA.__init__)


def test_restrictions_devicerestrictiona_constructor_args():
    sig = inspect.signature(restrictions_DeviceRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_restrictions_subfunctionrestrictiona_is_not_abstract():
    assert not inspect.isabstract(restrictions_SubfunctionRestrictionA)


def test_restrictions_subfunctionrestrictiona_constructor_exists():
    assert callable(restrictions_SubfunctionRestrictionA.__init__)


def test_restrictions_subfunctionrestrictiona_constructor_args():
    sig = inspect.signature(restrictions_SubfunctionRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_restrictions_signalgrouprestrictiona_is_not_abstract():
    assert not inspect.isabstract(restrictions_SignalGroupRestrictionA)


def test_restrictions_signalgrouprestrictiona_constructor_exists():
    assert callable(restrictions_SignalGroupRestrictionA.__init__)


def test_restrictions_signalgrouprestrictiona_constructor_args():
    sig = inspect.signature(restrictions_SignalGroupRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_restrictions_signalrestrictiona_is_not_abstract():
    assert not inspect.isabstract(restrictions_SignalRestrictionA)


def test_restrictions_signalrestrictiona_constructor_exists():
    assert callable(restrictions_SignalRestrictionA.__init__)


def test_restrictions_signalrestrictiona_constructor_args():
    sig = inspect.signature(restrictions_SignalRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_restrictions_taskgrouprestrictiona_is_not_abstract():
    assert not inspect.isabstract(restrictions_TaskGroupRestrictionA)


def test_restrictions_taskgrouprestrictiona_constructor_exists():
    assert callable(restrictions_TaskGroupRestrictionA.__init__)


def test_restrictions_taskgrouprestrictiona_constructor_args():
    sig = inspect.signature(restrictions_TaskGroupRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_restrictions_taskrestrictiona_is_not_abstract():
    assert not inspect.isabstract(restrictions_TaskRestrictionA)


def test_restrictions_taskrestrictiona_constructor_exists():
    assert callable(restrictions_TaskRestrictionA.__init__)


def test_restrictions_taskrestrictiona_constructor_args():
    sig = inspect.signature(restrictions_TaskRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_restrictions_signalgrouprestrictiona_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_SignalGroupRestrictionA)


def test_oaam_restrictions_signalgrouprestrictiona_constructor_exists():
    assert callable(oaam_restrictions_SignalGroupRestrictionA.__init__)


def test_oaam_restrictions_signalgrouprestrictiona_constructor_args():
    sig = inspect.signature(oaam_restrictions_SignalGroupRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_restrictions_taskgrouprestrictiona_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_TaskGroupRestrictionA)


def test_oaam_restrictions_taskgrouprestrictiona_constructor_exists():
    assert callable(oaam_restrictions_TaskGroupRestrictionA.__init__)


def test_oaam_restrictions_taskgrouprestrictiona_constructor_args():
    sig = inspect.signature(oaam_restrictions_TaskGroupRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_restrictions_subfunctionrestrictiona_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_SubfunctionRestrictionA)


def test_oaam_restrictions_subfunctionrestrictiona_constructor_exists():
    assert callable(oaam_restrictions_SubfunctionRestrictionA.__init__)


def test_oaam_restrictions_subfunctionrestrictiona_constructor_args():
    sig = inspect.signature(oaam_restrictions_SubfunctionRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_restrictions_devicerestrictiona_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_DeviceRestrictionA)


def test_oaam_restrictions_devicerestrictiona_constructor_exists():
    assert callable(oaam_restrictions_DeviceRestrictionA.__init__)


def test_oaam_restrictions_devicerestrictiona_constructor_args():
    sig = inspect.signature(oaam_restrictions_DeviceRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_restrictionscontainera_is_not_abstract():
    assert not inspect.isabstract(RestrictionsContainerA)


def test_restrictionscontainera_constructor_exists():
    assert callable(RestrictionsContainerA.__init__)


def test_restrictionscontainera_constructor_args():
    sig = inspect.signature(RestrictionsContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_restrictions_restrictions_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_Restrictions)


def test_oaam_restrictions_restrictions_constructor_exists():
    assert callable(oaam_restrictions_Restrictions.__init__)


def test_oaam_restrictions_restrictions_constructor_args():
    sig = inspect.signature(oaam_restrictions_Restrictions.__init__)
    params = list(sig.parameters.keys())



def test_timedelayrestriction_is_not_abstract():
    assert not inspect.isabstract(TimeDelayRestriction)


def test_timedelayrestriction_constructor_exists():
    assert callable(TimeDelayRestriction.__init__)


def test_timedelayrestriction_constructor_args():
    sig = inspect.signature(TimeDelayRestriction.__init__)
    params = list(sig.parameters.keys())



def test_subrestrictions_is_not_abstract():
    assert not inspect.isabstract(Subrestrictions)


def test_subrestrictions_constructor_exists():
    assert callable(Subrestrictions.__init__)


def test_subrestrictions_constructor_args():
    sig = inspect.signature(Subrestrictions.__init__)
    params = list(sig.parameters.keys())



def test_segregationrestriction_is_not_abstract():
    assert not inspect.isabstract(SegregationRestriction)


def test_segregationrestriction_constructor_exists():
    assert callable(SegregationRestriction.__init__)


def test_segregationrestriction_constructor_args():
    sig = inspect.signature(SegregationRestriction.__init__)
    params = list(sig.parameters.keys())



def test_connectiontyperestriction_is_not_abstract():
    assert not inspect.isabstract(ConnectionTypeRestriction)


def test_connectiontyperestriction_constructor_exists():
    assert callable(ConnectionTypeRestriction.__init__)


def test_connectiontyperestriction_constructor_args():
    sig = inspect.signature(ConnectionTypeRestriction.__init__)
    params = list(sig.parameters.keys())



def test_connectionrestriction_is_not_abstract():
    assert not inspect.isabstract(ConnectionRestriction)


def test_connectionrestriction_constructor_exists():
    assert callable(ConnectionRestriction.__init__)


def test_connectionrestriction_constructor_args():
    sig = inspect.signature(ConnectionRestriction.__init__)
    params = list(sig.parameters.keys())



def test_oaam_restrictions_signalrestrictiona_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_SignalRestrictionA)


def test_oaam_restrictions_signalrestrictiona_constructor_exists():
    assert callable(oaam_restrictions_SignalRestrictionA.__init__)


def test_oaam_restrictions_signalrestrictiona_constructor_args():
    sig = inspect.signature(oaam_restrictions_SignalRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_restrictions_taskrestrictiona_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_TaskRestrictionA)


def test_oaam_restrictions_taskrestrictiona_constructor_exists():
    assert callable(oaam_restrictions_TaskRestrictionA.__init__)


def test_oaam_restrictions_taskrestrictiona_constructor_args():
    sig = inspect.signature(oaam_restrictions_TaskRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_restrictions_connectionrestrinctiona_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_ConnectionRestrinctionA)


def test_oaam_restrictions_connectionrestrinctiona_constructor_exists():
    assert callable(oaam_restrictions_ConnectionRestrinctionA.__init__)


def test_oaam_restrictions_connectionrestrinctiona_constructor_args():
    sig = inspect.signature(oaam_restrictions_ConnectionRestrinctionA.__init__)
    params = list(sig.parameters.keys())



def test_powersourcerestriction_is_not_abstract():
    assert not inspect.isabstract(PowerSourceRestriction)


def test_powersourcerestriction_constructor_exists():
    assert callable(PowerSourceRestriction.__init__)


def test_powersourcerestriction_constructor_args():
    sig = inspect.signature(PowerSourceRestriction.__init__)
    params = list(sig.parameters.keys())



def test_arearestriction_is_not_abstract():
    assert not inspect.isabstract(AreaRestriction)


def test_arearestriction_constructor_exists():
    assert callable(AreaRestriction.__init__)


def test_arearestriction_constructor_args():
    sig = inspect.signature(AreaRestriction.__init__)
    params = list(sig.parameters.keys())



def test_locationrestriction_is_not_abstract():
    assert not inspect.isabstract(LocationRestriction)


def test_locationrestriction_constructor_exists():
    assert callable(LocationRestriction.__init__)


def test_locationrestriction_constructor_args():
    sig = inspect.signature(LocationRestriction.__init__)
    params = list(sig.parameters.keys())



def test_devicerestriction_is_not_abstract():
    assert not inspect.isabstract(DeviceRestriction)


def test_devicerestriction_constructor_exists():
    assert callable(DeviceRestriction.__init__)


def test_devicerestriction_constructor_args():
    sig = inspect.signature(DeviceRestriction.__init__)
    params = list(sig.parameters.keys())



def test_devicetyperestriction_is_not_abstract():
    assert not inspect.isabstract(DeviceTypeRestriction)


def test_devicetyperestriction_constructor_exists():
    assert callable(DeviceTypeRestriction.__init__)


def test_devicetyperestriction_constructor_args():
    sig = inspect.signature(DeviceTypeRestriction.__init__)
    params = list(sig.parameters.keys())



def test_synchronicityrestriction_is_not_abstract():
    assert not inspect.isabstract(SynchronicityRestriction)


def test_synchronicityrestriction_constructor_exists():
    assert callable(SynchronicityRestriction.__init__)


def test_synchronicityrestriction_constructor_args():
    sig = inspect.signature(SynchronicityRestriction.__init__)
    params = list(sig.parameters.keys())



def test_tasksymmetryrestriction_is_not_abstract():
    assert not inspect.isabstract(TaskSymmetryRestriction)


def test_tasksymmetryrestriction_constructor_exists():
    assert callable(TaskSymmetryRestriction.__init__)


def test_tasksymmetryrestriction_constructor_args():
    sig = inspect.signature(TaskSymmetryRestriction.__init__)
    params = list(sig.parameters.keys())



def test_taskatomicrestriction_is_not_abstract():
    assert not inspect.isabstract(TaskAtomicRestriction)


def test_taskatomicrestriction_constructor_exists():
    assert callable(TaskAtomicRestriction.__init__)


def test_taskatomicrestriction_constructor_args():
    sig = inspect.signature(TaskAtomicRestriction.__init__)
    params = list(sig.parameters.keys())



def test_capabilities_capabilitiescontainera_is_not_abstract():
    assert not inspect.isabstract(capabilities_CapabilitiesContainerA)


def test_capabilities_capabilitiescontainera_constructor_exists():
    assert callable(capabilities_CapabilitiesContainerA.__init__)


def test_capabilities_capabilitiescontainera_constructor_args():
    sig = inspect.signature(capabilities_CapabilitiesContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_capabilities_subcapabilities_is_not_abstract():
    assert not inspect.isabstract(oaam_capabilities_Subcapabilities)


def test_oaam_capabilities_subcapabilities_constructor_exists():
    assert callable(oaam_capabilities_Subcapabilities.__init__)


def test_oaam_capabilities_subcapabilities_constructor_args():
    sig = inspect.signature(oaam_capabilities_Subcapabilities.__init__)
    params = list(sig.parameters.keys())



def test_capabilitiescontainera_is_not_abstract():
    assert not inspect.isabstract(CapabilitiesContainerA)


def test_capabilitiescontainera_constructor_exists():
    assert callable(CapabilitiesContainerA.__init__)


def test_capabilitiescontainera_constructor_args():
    sig = inspect.signature(CapabilitiesContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_capabilities_capabilities_is_not_abstract():
    assert not inspect.isabstract(oaam_capabilities_Capabilities)


def test_oaam_capabilities_capabilities_constructor_exists():
    assert callable(oaam_capabilities_Capabilities.__init__)


def test_oaam_capabilities_capabilities_constructor_args():
    sig = inspect.signature(oaam_capabilities_Capabilities.__init__)
    params = list(sig.parameters.keys())



def test_capabilities_capabilitya_is_not_abstract():
    assert not inspect.isabstract(capabilities_CapabilityA)


def test_capabilities_capabilitya_constructor_exists():
    assert callable(capabilities_CapabilityA.__init__)


def test_capabilities_capabilitya_constructor_args():
    sig = inspect.signature(capabilities_CapabilityA.__init__)
    params = list(sig.parameters.keys())



def test_messageonconnectionordevicecapability_is_not_abstract():
    assert not inspect.isabstract(MessageOnConnectionOrDeviceCapability)


def test_messageonconnectionordevicecapability_constructor_exists():
    assert callable(MessageOnConnectionOrDeviceCapability.__init__)


def test_messageonconnectionordevicecapability_constructor_args():
    sig = inspect.signature(MessageOnConnectionOrDeviceCapability.__init__)
    params = list(sig.parameters.keys())



def test_subcapabilities_is_not_abstract():
    assert not inspect.isabstract(Subcapabilities)


def test_subcapabilities_constructor_exists():
    assert callable(Subcapabilities.__init__)


def test_subcapabilities_constructor_args():
    sig = inspect.signature(Subcapabilities.__init__)
    params = list(sig.parameters.keys())



def test_connectioninductorlocationcapability_is_not_abstract():
    assert not inspect.isabstract(ConnectionInDuctOrLocationCapability)


def test_connectioninductorlocationcapability_constructor_exists():
    assert callable(ConnectionInDuctOrLocationCapability.__init__)


def test_connectioninductorlocationcapability_constructor_args():
    sig = inspect.signature(ConnectionInDuctOrLocationCapability.__init__)
    params = list(sig.parameters.keys())



def test_subdeviceindevicecapability_is_not_abstract():
    assert not inspect.isabstract(SubdeviceInDeviceCapability)


def test_subdeviceindevicecapability_constructor_exists():
    assert callable(SubdeviceInDeviceCapability.__init__)


def test_subdeviceindevicecapability_constructor_args():
    sig = inspect.signature(SubdeviceInDeviceCapability.__init__)
    params = list(sig.parameters.keys())



def test_deviceinlocationcapability_is_not_abstract():
    assert not inspect.isabstract(DeviceInLocationCapability)


def test_deviceinlocationcapability_constructor_exists():
    assert callable(DeviceInLocationCapability.__init__)


def test_deviceinlocationcapability_constructor_args():
    sig = inspect.signature(DeviceInLocationCapability.__init__)
    params = list(sig.parameters.keys())



def test_signalonconnectionordevicecapability_is_not_abstract():
    assert not inspect.isabstract(SignalOnConnectionOrDeviceCapability)


def test_signalonconnectionordevicecapability_constructor_exists():
    assert callable(SignalOnConnectionOrDeviceCapability.__init__)


def test_signalonconnectionordevicecapability_constructor_args():
    sig = inspect.signature(SignalOnConnectionOrDeviceCapability.__init__)
    params = list(sig.parameters.keys())



def test_taskondevicecapability_is_not_abstract():
    assert not inspect.isabstract(TaskOnDeviceCapability)


def test_taskondevicecapability_constructor_exists():
    assert callable(TaskOnDeviceCapability.__init__)


def test_taskondevicecapability_constructor_args():
    sig = inspect.signature(TaskOnDeviceCapability.__init__)
    params = list(sig.parameters.keys())



def test_resourceconsumption_is_not_abstract():
    assert not inspect.isabstract(ResourceConsumption)


def test_resourceconsumption_constructor_exists():
    assert callable(ResourceConsumption.__init__)


def test_resourceconsumption_constructor_args():
    sig = inspect.signature(ResourceConsumption.__init__)
    params = list(sig.parameters.keys())



def test_oaam_capabilities_capabilitya_is_not_abstract():
    assert not inspect.isabstract(oaam_capabilities_CapabilityA)


def test_oaam_capabilities_capabilitya_constructor_exists():
    assert callable(oaam_capabilities_CapabilityA.__init__)


def test_oaam_capabilities_capabilitya_constructor_args():
    sig = inspect.signature(oaam_capabilities_CapabilityA.__init__)
    params = list(sig.parameters.keys())



def test_signalinmessagecapability_is_not_abstract():
    assert not inspect.isabstract(SignalInMessageCapability)


def test_signalinmessagecapability_constructor_exists():
    assert callable(SignalInMessageCapability.__init__)


def test_signalinmessagecapability_constructor_args():
    sig = inspect.signature(SignalInMessageCapability.__init__)
    params = list(sig.parameters.keys())



def test_submessageinmessagecapability_is_not_abstract():
    assert not inspect.isabstract(SubmessageInMessageCapability)


def test_submessageinmessagecapability_constructor_exists():
    assert callable(SubmessageInMessageCapability.__init__)


def test_submessageinmessagecapability_constructor_args():
    sig = inspect.signature(SubmessageInMessageCapability.__init__)
    params = list(sig.parameters.keys())



def test_messageonbuscapability_is_not_abstract():
    assert not inspect.isabstract(MessageOnBusCapability)


def test_messageonbuscapability_constructor_exists():
    assert callable(MessageOnBusCapability.__init__)


def test_messageonbuscapability_constructor_args():
    sig = inspect.signature(MessageOnBusCapability.__init__)
    params = list(sig.parameters.keys())



def test_subconnectionindevicecapability_is_not_abstract():
    assert not inspect.isabstract(SubconnectionInDeviceCapability)


def test_subconnectionindevicecapability_constructor_exists():
    assert callable(SubconnectionInDeviceCapability.__init__)


def test_subconnectionindevicecapability_constructor_args():
    sig = inspect.signature(SubconnectionInDeviceCapability.__init__)
    params = list(sig.parameters.keys())



def test_anatomycontainera_is_not_abstract():
    assert not inspect.isabstract(AnatomyContainerA)


def test_anatomycontainera_constructor_exists():
    assert callable(AnatomyContainerA.__init__)


def test_anatomycontainera_constructor_args():
    sig = inspect.signature(AnatomyContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_anatomy_anatomy_is_not_abstract():
    assert not inspect.isabstract(oaam_anatomy_Anatomy)


def test_oaam_anatomy_anatomy_constructor_exists():
    assert callable(oaam_anatomy_Anatomy.__init__)


def test_oaam_anatomy_anatomy_constructor_args():
    sig = inspect.signature(oaam_anatomy_Anatomy.__init__)
    params = list(sig.parameters.keys())



def test_anatomy_anatomycontainera_is_not_abstract():
    assert not inspect.isabstract(anatomy_AnatomyContainerA)


def test_anatomy_anatomycontainera_constructor_exists():
    assert callable(anatomy_AnatomyContainerA.__init__)


def test_anatomy_anatomycontainera_constructor_args():
    sig = inspect.signature(anatomy_AnatomyContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_anatomy_subanatomy_is_not_abstract():
    assert not inspect.isabstract(oaam_anatomy_Subanatomy)


def test_oaam_anatomy_subanatomy_constructor_exists():
    assert callable(oaam_anatomy_Subanatomy.__init__)


def test_oaam_anatomy_subanatomy_constructor_args():
    sig = inspect.signature(oaam_anatomy_Subanatomy.__init__)
    params = list(sig.parameters.keys())



def test_ductopening_is_not_abstract():
    assert not inspect.isabstract(DuctOpening)


def test_ductopening_constructor_exists():
    assert callable(DuctOpening.__init__)


def test_ductopening_constructor_args():
    sig = inspect.signature(DuctOpening.__init__)
    params = list(sig.parameters.keys())



def test_devicetypesymmetry_is_not_abstract():
    assert not inspect.isabstract(DeviceTypeSymmetry)


def test_devicetypesymmetry_constructor_exists():
    assert callable(DeviceTypeSymmetry.__init__)


def test_devicetypesymmetry_constructor_args():
    sig = inspect.signature(DeviceTypeSymmetry.__init__)
    params = list(sig.parameters.keys())



def test_powersource_is_not_abstract():
    assert not inspect.isabstract(PowerSource)


def test_powersource_constructor_exists():
    assert callable(PowerSource.__init__)


def test_powersource_constructor_args():
    sig = inspect.signature(PowerSource.__init__)
    params = list(sig.parameters.keys())



def test_attributedefinition_is_not_abstract():
    assert not inspect.isabstract(AttributeDefinition)


def test_attributedefinition_constructor_exists():
    assert callable(AttributeDefinition.__init__)


def test_attributedefinition_constructor_args():
    sig = inspect.signature(AttributeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ducttype_is_not_abstract():
    assert not inspect.isabstract(DuctType)


def test_ducttype_constructor_exists():
    assert callable(DuctType.__init__)


def test_ducttype_constructor_args():
    sig = inspect.signature(DuctType.__init__)
    params = list(sig.parameters.keys())



def test_tasktypedissimilarity_is_not_abstract():
    assert not inspect.isabstract(TaskTypeDissimilarity)


def test_tasktypedissimilarity_constructor_exists():
    assert callable(TaskTypeDissimilarity.__init__)


def test_tasktypedissimilarity_constructor_args():
    sig = inspect.signature(TaskTypeDissimilarity.__init__)
    params = list(sig.parameters.keys())



def test_tasktype_is_not_abstract():
    assert not inspect.isabstract(TaskType)


def test_tasktype_constructor_exists():
    assert callable(TaskType.__init__)


def test_tasktype_constructor_args():
    sig = inspect.signature(TaskType.__init__)
    params = list(sig.parameters.keys())



def test_resourcetypedissimilarity_is_not_abstract():
    assert not inspect.isabstract(ResourceTypeDissimilarity)


def test_resourcetypedissimilarity_constructor_exists():
    assert callable(ResourceTypeDissimilarity.__init__)


def test_resourcetypedissimilarity_constructor_args():
    sig = inspect.signature(ResourceTypeDissimilarity.__init__)
    params = list(sig.parameters.keys())



def test_resourcetypemodifier_is_not_abstract():
    assert not inspect.isabstract(ResourceTypeModifier)


def test_resourcetypemodifier_constructor_exists():
    assert callable(ResourceTypeModifier.__init__)


def test_resourcetypemodifier_constructor_args():
    sig = inspect.signature(ResourceTypeModifier.__init__)
    params = list(sig.parameters.keys())



def test_devicetype_is_not_abstract():
    assert not inspect.isabstract(DeviceType)


def test_devicetype_constructor_exists():
    assert callable(DeviceType.__init__)


def test_devicetype_constructor_args():
    sig = inspect.signature(DeviceType.__init__)
    params = list(sig.parameters.keys())



def test_signaltype_is_not_abstract():
    assert not inspect.isabstract(SignalType)


def test_signaltype_constructor_exists():
    assert callable(SignalType.__init__)


def test_signaltype_constructor_args():
    sig = inspect.signature(SignalType.__init__)
    params = list(sig.parameters.keys())



def test_resourcetypemodifierlevel_is_not_abstract():
    assert not inspect.isabstract(ResourceTypeModifierLevel)


def test_resourcetypemodifierlevel_constructor_exists():
    assert callable(ResourceTypeModifierLevel.__init__)


def test_resourcetypemodifierlevel_constructor_args():
    sig = inspect.signature(ResourceTypeModifierLevel.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_resourceproviderinstancea_is_not_abstract():
    assert not inspect.isabstract(oaam_library_ResourceProviderInstanceA)


def test_oaam_library_resourceproviderinstancea_constructor_exists():
    assert callable(oaam_library_ResourceProviderInstanceA.__init__)


def test_oaam_library_resourceproviderinstancea_constructor_args():
    sig = inspect.signature(oaam_library_ResourceProviderInstanceA.__init__)
    params = list(sig.parameters.keys())



def test_resourcelink_is_not_abstract():
    assert not inspect.isabstract(ResourceLink)


def test_resourcelink_constructor_exists():
    assert callable(ResourceLink.__init__)


def test_resourcelink_constructor_args():
    sig = inspect.signature(ResourceLink.__init__)
    params = list(sig.parameters.keys())



def test_resourcetype_is_not_abstract():
    assert not inspect.isabstract(ResourceType)


def test_resourcetype_constructor_exists():
    assert callable(ResourceType.__init__)


def test_resourcetype_constructor_args():
    sig = inspect.signature(ResourceType.__init__)
    params = list(sig.parameters.keys())



def test_resourcebundle_is_not_abstract():
    assert not inspect.isabstract(ResourceBundle)


def test_resourcebundle_constructor_exists():
    assert callable(ResourceBundle.__init__)


def test_resourcebundle_constructor_args():
    sig = inspect.signature(ResourceBundle.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_resourceprovidera_is_not_abstract():
    assert not inspect.isabstract(oaam_library_ResourceProviderA)


def test_oaam_library_resourceprovidera_constructor_exists():
    assert callable(oaam_library_ResourceProviderA.__init__)


def test_oaam_library_resourceprovidera_constructor_args():
    sig = inspect.signature(oaam_library_ResourceProviderA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_resourceconsumera_is_not_abstract():
    assert not inspect.isabstract(oaam_library_ResourceConsumerA)


def test_oaam_library_resourceconsumera_constructor_exists():
    assert callable(oaam_library_ResourceConsumerA.__init__)


def test_oaam_library_resourceconsumera_constructor_args():
    sig = inspect.signature(oaam_library_ResourceConsumerA.__init__)
    params = list(sig.parameters.keys())



def test_resourcegroup_is_not_abstract():
    assert not inspect.isabstract(ResourceGroup)


def test_resourcegroup_constructor_exists():
    assert callable(ResourceGroup.__init__)


def test_resourcegroup_constructor_args():
    sig = inspect.signature(ResourceGroup.__init__)
    params = list(sig.parameters.keys())



def test_resource_is_not_abstract():
    assert not inspect.isabstract(Resource)


def test_resource_constructor_exists():
    assert callable(Resource.__init__)


def test_resource_constructor_args():
    sig = inspect.signature(Resource.__init__)
    params = list(sig.parameters.keys())



def test_struct_is_not_abstract():
    assert not inspect.isabstract(Struct)


def test_struct_constructor_exists():
    assert callable(Struct.__init__)


def test_struct_constructor_args():
    sig = inspect.signature(Struct.__init__)
    params = list(sig.parameters.keys())



def test_datatypea_is_not_abstract():
    assert not inspect.isabstract(DataTypeA)


def test_datatypea_constructor_exists():
    assert callable(DataTypeA.__init__)


def test_datatypea_constructor_args():
    sig = inspect.signature(DataTypeA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_common_array_is_not_abstract():
    assert not inspect.isabstract(oaam_common_Array)


def test_oaam_common_array_constructor_exists():
    assert callable(oaam_common_Array.__init__)


def test_oaam_common_array_constructor_args():
    sig = inspect.signature(oaam_common_Array.__init__)
    params = list(sig.parameters.keys())
    assert "nElements" in params, "Missing parameter 'nElements'"
    assert "alignment" in params, "Missing parameter 'alignment'"

def test_oaam_common_array_has_nElements():
    assert hasattr(oaam_common_Array, "nElements")
    descriptor = None
    for klass in oaam_common_Array.__mro__:
        if "nElements" in klass.__dict__:
            descriptor = klass.__dict__["nElements"]
            break
    assert isinstance(descriptor, property)

def test_oaam_common_array_has_alignment():
    assert hasattr(oaam_common_Array, "alignment")
    descriptor = None
    for klass in oaam_common_Array.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)



def test_oaam_common_byte_is_not_abstract():
    assert not inspect.isabstract(oaam_common_Byte)


def test_oaam_common_byte_constructor_exists():
    assert callable(oaam_common_Byte.__init__)


def test_oaam_common_byte_constructor_args():
    sig = inspect.signature(oaam_common_Byte.__init__)
    params = list(sig.parameters.keys())
    assert "nBits" in params, "Missing parameter 'nBits'"

def test_oaam_common_byte_has_nBits():
    assert hasattr(oaam_common_Byte, "nBits")
    descriptor = None
    for klass in oaam_common_Byte.__mro__:
        if "nBits" in klass.__dict__:
            descriptor = klass.__dict__["nBits"]
            break
    assert isinstance(descriptor, property)



def test_oaam_common_character_is_not_abstract():
    assert not inspect.isabstract(oaam_common_Character)


def test_oaam_common_character_constructor_exists():
    assert callable(oaam_common_Character.__init__)


def test_oaam_common_character_constructor_args():
    sig = inspect.signature(oaam_common_Character.__init__)
    params = list(sig.parameters.keys())
    assert "nBits" in params, "Missing parameter 'nBits'"
    assert "encoding" in params, "Missing parameter 'encoding'"

def test_oaam_common_character_has_nBits():
    assert hasattr(oaam_common_Character, "nBits")
    descriptor = None
    for klass in oaam_common_Character.__mro__:
        if "nBits" in klass.__dict__:
            descriptor = klass.__dict__["nBits"]
            break
    assert isinstance(descriptor, property)

def test_oaam_common_character_has_encoding():
    assert hasattr(oaam_common_Character, "encoding")
    descriptor = None
    for klass in oaam_common_Character.__mro__:
        if "encoding" in klass.__dict__:
            descriptor = klass.__dict__["encoding"]
            break
    assert isinstance(descriptor, property)



def test_oaam_common_boolean_is_not_abstract():
    assert not inspect.isabstract(oaam_common_Boolean)


def test_oaam_common_boolean_constructor_exists():
    assert callable(oaam_common_Boolean.__init__)


def test_oaam_common_boolean_constructor_args():
    sig = inspect.signature(oaam_common_Boolean.__init__)
    params = list(sig.parameters.keys())
    assert "nBits" in params, "Missing parameter 'nBits'"

def test_oaam_common_boolean_has_nBits():
    assert hasattr(oaam_common_Boolean, "nBits")
    descriptor = None
    for klass in oaam_common_Boolean.__mro__:
        if "nBits" in klass.__dict__:
            descriptor = klass.__dict__["nBits"]
            break
    assert isinstance(descriptor, property)



def test_oaam_common_struct_is_not_abstract():
    assert not inspect.isabstract(oaam_common_Struct)


def test_oaam_common_struct_constructor_exists():
    assert callable(oaam_common_Struct.__init__)


def test_oaam_common_struct_constructor_args():
    sig = inspect.signature(oaam_common_Struct.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "alignment" in params, "Missing parameter 'alignment'"

def test_oaam_common_struct_has_isAbstract():
    assert hasattr(oaam_common_Struct, "isAbstract")
    descriptor = None
    for klass in oaam_common_Struct.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_oaam_common_struct_has_alignment():
    assert hasattr(oaam_common_Struct, "alignment")
    descriptor = None
    for klass in oaam_common_Struct.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)



def test_oaam_common_floatingpoint_is_not_abstract():
    assert not inspect.isabstract(oaam_common_FloatingPoint)


def test_oaam_common_floatingpoint_constructor_exists():
    assert callable(oaam_common_FloatingPoint.__init__)


def test_oaam_common_floatingpoint_constructor_args():
    sig = inspect.signature(oaam_common_FloatingPoint.__init__)
    params = list(sig.parameters.keys())
    assert "endianess" in params, "Missing parameter 'endianess'"
    assert "nBits" in params, "Missing parameter 'nBits'"

def test_oaam_common_floatingpoint_has_endianess():
    assert hasattr(oaam_common_FloatingPoint, "endianess")
    descriptor = None
    for klass in oaam_common_FloatingPoint.__mro__:
        if "endianess" in klass.__dict__:
            descriptor = klass.__dict__["endianess"]
            break
    assert isinstance(descriptor, property)

def test_oaam_common_floatingpoint_has_nBits():
    assert hasattr(oaam_common_FloatingPoint, "nBits")
    descriptor = None
    for klass in oaam_common_FloatingPoint.__mro__:
        if "nBits" in klass.__dict__:
            descriptor = klass.__dict__["nBits"]
            break
    assert isinstance(descriptor, property)



def test_oaam_common_integer_is_not_abstract():
    assert not inspect.isabstract(oaam_common_Integer)


def test_oaam_common_integer_constructor_exists():
    assert callable(oaam_common_Integer.__init__)


def test_oaam_common_integer_constructor_args():
    sig = inspect.signature(oaam_common_Integer.__init__)
    params = list(sig.parameters.keys())
    assert "nBits" in params, "Missing parameter 'nBits'"
    assert "signed" in params, "Missing parameter 'signed'"
    assert "endianess" in params, "Missing parameter 'endianess'"

def test_oaam_common_integer_has_nBits():
    assert hasattr(oaam_common_Integer, "nBits")
    descriptor = None
    for klass in oaam_common_Integer.__mro__:
        if "nBits" in klass.__dict__:
            descriptor = klass.__dict__["nBits"]
            break
    assert isinstance(descriptor, property)

def test_oaam_common_integer_has_signed():
    assert hasattr(oaam_common_Integer, "signed")
    descriptor = None
    for klass in oaam_common_Integer.__mro__:
        if "signed" in klass.__dict__:
            descriptor = klass.__dict__["signed"]
            break
    assert isinstance(descriptor, property)

def test_oaam_common_integer_has_endianess():
    assert hasattr(oaam_common_Integer, "endianess")
    descriptor = None
    for klass in oaam_common_Integer.__mro__:
        if "endianess" in klass.__dict__:
            descriptor = klass.__dict__["endianess"]
            break
    assert isinstance(descriptor, property)



def test_boola_is_not_abstract():
    assert not inspect.isabstract(BoolA)


def test_boola_constructor_exists():
    assert callable(BoolA.__init__)


def test_boola_constructor_args():
    sig = inspect.signature(BoolA.__init__)
    params = list(sig.parameters.keys())



def test_common_oaambaseelementa_is_not_abstract():
    assert not inspect.isabstract(common_OaamBaseElementA)


def test_common_oaambaseelementa_constructor_exists():
    assert callable(common_OaamBaseElementA.__init__)


def test_common_oaambaseelementa_constructor_args():
    sig = inspect.signature(common_OaamBaseElementA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_allocations_deviceassignment_is_not_abstract():
    assert not inspect.isabstract(oaam_allocations_DeviceAssignment)


def test_oaam_allocations_deviceassignment_constructor_exists():
    assert callable(oaam_allocations_DeviceAssignment.__init__)


def test_oaam_allocations_deviceassignment_constructor_args():
    sig = inspect.signature(oaam_allocations_DeviceAssignment.__init__)
    params = list(sig.parameters.keys())



def test_oaam_functions_signal_is_not_abstract():
    assert not inspect.isabstract(oaam_functions_Signal)


def test_oaam_functions_signal_constructor_exists():
    assert callable(oaam_functions_Signal.__init__)


def test_oaam_functions_signal_constructor_args():
    sig = inspect.signature(oaam_functions_Signal.__init__)
    params = list(sig.parameters.keys())
    assert "outIndex" in params, "Missing parameter 'outIndex'"
    assert "inIndex" in params, "Missing parameter 'inIndex'"

def test_oaam_functions_signal_has_outIndex():
    assert hasattr(oaam_functions_Signal, "outIndex")
    descriptor = None
    for klass in oaam_functions_Signal.__mro__:
        if "outIndex" in klass.__dict__:
            descriptor = klass.__dict__["outIndex"]
            break
    assert isinstance(descriptor, property)

def test_oaam_functions_signal_has_inIndex():
    assert hasattr(oaam_functions_Signal, "inIndex")
    descriptor = None
    for klass in oaam_functions_Signal.__mro__:
        if "inIndex" in klass.__dict__:
            descriptor = klass.__dict__["inIndex"]
            break
    assert isinstance(descriptor, property)



def test_oaam_restrictions_connectionrestriction_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_ConnectionRestriction)


def test_oaam_restrictions_connectionrestriction_constructor_exists():
    assert callable(oaam_restrictions_ConnectionRestriction.__init__)


def test_oaam_restrictions_connectionrestriction_constructor_args():
    sig = inspect.signature(oaam_restrictions_ConnectionRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "isForbidden" in params, "Missing parameter 'isForbidden'"
    assert "connectionName" in params, "Missing parameter 'connectionName'"

def test_oaam_restrictions_connectionrestriction_has_isForbidden():
    assert hasattr(oaam_restrictions_ConnectionRestriction, "isForbidden")
    descriptor = None
    for klass in oaam_restrictions_ConnectionRestriction.__mro__:
        if "isForbidden" in klass.__dict__:
            descriptor = klass.__dict__["isForbidden"]
            break
    assert isinstance(descriptor, property)

def test_oaam_restrictions_connectionrestriction_has_connectionName():
    assert hasattr(oaam_restrictions_ConnectionRestriction, "connectionName")
    descriptor = None
    for klass in oaam_restrictions_ConnectionRestriction.__mro__:
        if "connectionName" in klass.__dict__:
            descriptor = klass.__dict__["connectionName"]
            break
    assert isinstance(descriptor, property)



def test_oaam_capabilities_messageonbuscapability_is_not_abstract():
    assert not inspect.isabstract(oaam_capabilities_MessageOnBusCapability)


def test_oaam_capabilities_messageonbuscapability_constructor_exists():
    assert callable(oaam_capabilities_MessageOnBusCapability.__init__)


def test_oaam_capabilities_messageonbuscapability_constructor_args():
    sig = inspect.signature(oaam_capabilities_MessageOnBusCapability.__init__)
    params = list(sig.parameters.keys())



def test_oaam_anatomy_ductopening_is_not_abstract():
    assert not inspect.isabstract(oaam_anatomy_DuctOpening)


def test_oaam_anatomy_ductopening_constructor_exists():
    assert callable(oaam_anatomy_DuctOpening.__init__)


def test_oaam_anatomy_ductopening_constructor_args():
    sig = inspect.signature(oaam_anatomy_DuctOpening.__init__)
    params = list(sig.parameters.keys())



def test_oaam_hardware_connection_is_not_abstract():
    assert not inspect.isabstract(oaam_hardware_Connection)


def test_oaam_hardware_connection_constructor_exists():
    assert callable(oaam_hardware_Connection.__init__)


def test_oaam_hardware_connection_constructor_args():
    sig = inspect.signature(oaam_hardware_Connection.__init__)
    params = list(sig.parameters.keys())



def test_oaam_allocations_schedule_is_not_abstract():
    assert not inspect.isabstract(oaam_allocations_Schedule)


def test_oaam_allocations_schedule_constructor_exists():
    assert callable(oaam_allocations_Schedule.__init__)


def test_oaam_allocations_schedule_constructor_args():
    sig = inspect.signature(oaam_allocations_Schedule.__init__)
    params = list(sig.parameters.keys())
    assert "isPeriodic" in params, "Missing parameter 'isPeriodic'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "rate" in params, "Missing parameter 'rate'"

def test_oaam_allocations_schedule_has_isPeriodic():
    assert hasattr(oaam_allocations_Schedule, "isPeriodic")
    descriptor = None
    for klass in oaam_allocations_Schedule.__mro__:
        if "isPeriodic" in klass.__dict__:
            descriptor = klass.__dict__["isPeriodic"]
            break
    assert isinstance(descriptor, property)

def test_oaam_allocations_schedule_has_priority():
    assert hasattr(oaam_allocations_Schedule, "priority")
    descriptor = None
    for klass in oaam_allocations_Schedule.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_oaam_allocations_schedule_has_rate():
    assert hasattr(oaam_allocations_Schedule, "rate")
    descriptor = None
    for klass in oaam_allocations_Schedule.__mro__:
        if "rate" in klass.__dict__:
            descriptor = klass.__dict__["rate"]
            break
    assert isinstance(descriptor, property)



def test_oaam_scenario_operationmode_is_not_abstract():
    assert not inspect.isabstract(oaam_scenario_OperationMode)


def test_oaam_scenario_operationmode_constructor_exists():
    assert callable(oaam_scenario_OperationMode.__init__)


def test_oaam_scenario_operationmode_constructor_args():
    sig = inspect.signature(oaam_scenario_OperationMode.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_resourcetypemodifierlevel_is_not_abstract():
    assert not inspect.isabstract(oaam_library_ResourceTypeModifierLevel)


def test_oaam_library_resourcetypemodifierlevel_constructor_exists():
    assert callable(oaam_library_ResourceTypeModifierLevel.__init__)


def test_oaam_library_resourcetypemodifierlevel_constructor_args():
    sig = inspect.signature(oaam_library_ResourceTypeModifierLevel.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_tasktype_is_not_abstract():
    assert not inspect.isabstract(oaam_library_TaskType)


def test_oaam_library_tasktype_constructor_exists():
    assert callable(oaam_library_TaskType.__init__)


def test_oaam_library_tasktype_constructor_args():
    sig = inspect.signature(oaam_library_TaskType.__init__)
    params = list(sig.parameters.keys())
    assert "preferredExecutionRate" in params, "Missing parameter 'preferredExecutionRate'"
    assert "isDeterministic" in params, "Missing parameter 'isDeterministic'"

def test_oaam_library_tasktype_has_preferredExecutionRate():
    assert hasattr(oaam_library_TaskType, "preferredExecutionRate")
    descriptor = None
    for klass in oaam_library_TaskType.__mro__:
        if "preferredExecutionRate" in klass.__dict__:
            descriptor = klass.__dict__["preferredExecutionRate"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_tasktype_has_isDeterministic():
    assert hasattr(oaam_library_TaskType, "isDeterministic")
    descriptor = None
    for klass in oaam_library_TaskType.__mro__:
        if "isDeterministic" in klass.__dict__:
            descriptor = klass.__dict__["isDeterministic"]
            break
    assert isinstance(descriptor, property)



def test_oaam_anatomy_location_is_not_abstract():
    assert not inspect.isabstract(oaam_anatomy_Location)


def test_oaam_anatomy_location_constructor_exists():
    assert callable(oaam_anatomy_Location.__init__)


def test_oaam_anatomy_location_constructor_args():
    sig = inspect.signature(oaam_anatomy_Location.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_oaam_anatomy_location_has_length():
    assert hasattr(oaam_anatomy_Location, "length")
    descriptor = None
    for klass in oaam_anatomy_Location.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_oaam_capabilities_subconnectionindevicecapability_is_not_abstract():
    assert not inspect.isabstract(oaam_capabilities_SubconnectionInDeviceCapability)


def test_oaam_capabilities_subconnectionindevicecapability_constructor_exists():
    assert callable(oaam_capabilities_SubconnectionInDeviceCapability.__init__)


def test_oaam_capabilities_subconnectionindevicecapability_constructor_args():
    sig = inspect.signature(oaam_capabilities_SubconnectionInDeviceCapability.__init__)
    params = list(sig.parameters.keys())



def test_oaam_restrictions_connectiontyperestriction_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_ConnectionTypeRestriction)


def test_oaam_restrictions_connectiontyperestriction_constructor_exists():
    assert callable(oaam_restrictions_ConnectionTypeRestriction.__init__)


def test_oaam_restrictions_connectiontyperestriction_constructor_args():
    sig = inspect.signature(oaam_restrictions_ConnectionTypeRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "connectionTypeName" in params, "Missing parameter 'connectionTypeName'"
    assert "isForbidden" in params, "Missing parameter 'isForbidden'"

def test_oaam_restrictions_connectiontyperestriction_has_connectionTypeName():
    assert hasattr(oaam_restrictions_ConnectionTypeRestriction, "connectionTypeName")
    descriptor = None
    for klass in oaam_restrictions_ConnectionTypeRestriction.__mro__:
        if "connectionTypeName" in klass.__dict__:
            descriptor = klass.__dict__["connectionTypeName"]
            break
    assert isinstance(descriptor, property)

def test_oaam_restrictions_connectiontyperestriction_has_isForbidden():
    assert hasattr(oaam_restrictions_ConnectionTypeRestriction, "isForbidden")
    descriptor = None
    for klass in oaam_restrictions_ConnectionTypeRestriction.__mro__:
        if "isForbidden" in klass.__dict__:
            descriptor = klass.__dict__["isForbidden"]
            break
    assert isinstance(descriptor, property)



def test_oaam_hardware_device_is_not_abstract():
    assert not inspect.isabstract(oaam_hardware_Device)


def test_oaam_hardware_device_constructor_exists():
    assert callable(oaam_hardware_Device.__init__)


def test_oaam_hardware_device_constructor_args():
    sig = inspect.signature(oaam_hardware_Device.__init__)
    params = list(sig.parameters.keys())



def test_oaam_allocations_scheduledtime_is_not_abstract():
    assert not inspect.isabstract(oaam_allocations_ScheduledTime)


def test_oaam_allocations_scheduledtime_constructor_exists():
    assert callable(oaam_allocations_ScheduledTime.__init__)


def test_oaam_allocations_scheduledtime_constructor_args():
    sig = inspect.signature(oaam_allocations_ScheduledTime.__init__)
    params = list(sig.parameters.keys())
    assert "restart" in params, "Missing parameter 'restart'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "cycle" in params, "Missing parameter 'cycle'"
    assert "startTime" in params, "Missing parameter 'startTime'"

def test_oaam_allocations_scheduledtime_has_restart():
    assert hasattr(oaam_allocations_ScheduledTime, "restart")
    descriptor = None
    for klass in oaam_allocations_ScheduledTime.__mro__:
        if "restart" in klass.__dict__:
            descriptor = klass.__dict__["restart"]
            break
    assert isinstance(descriptor, property)

def test_oaam_allocations_scheduledtime_has_duration():
    assert hasattr(oaam_allocations_ScheduledTime, "duration")
    descriptor = None
    for klass in oaam_allocations_ScheduledTime.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_oaam_allocations_scheduledtime_has_cycle():
    assert hasattr(oaam_allocations_ScheduledTime, "cycle")
    descriptor = None
    for klass in oaam_allocations_ScheduledTime.__mro__:
        if "cycle" in klass.__dict__:
            descriptor = klass.__dict__["cycle"]
            break
    assert isinstance(descriptor, property)

def test_oaam_allocations_scheduledtime_has_startTime():
    assert hasattr(oaam_allocations_ScheduledTime, "startTime")
    descriptor = None
    for klass in oaam_allocations_ScheduledTime.__mro__:
        if "startTime" in klass.__dict__:
            descriptor = klass.__dict__["startTime"]
            break
    assert isinstance(descriptor, property)



def test_oaam_functions_task_is_not_abstract():
    assert not inspect.isabstract(oaam_functions_Task)


def test_oaam_functions_task_constructor_exists():
    assert callable(oaam_functions_Task.__init__)


def test_oaam_functions_task_constructor_args():
    sig = inspect.signature(oaam_functions_Task.__init__)
    params = list(sig.parameters.keys())
    assert "fixedRate" in params, "Missing parameter 'fixedRate'"
    assert "nParallels" in params, "Missing parameter 'nParallels'"

def test_oaam_functions_task_has_fixedRate():
    assert hasattr(oaam_functions_Task, "fixedRate")
    descriptor = None
    for klass in oaam_functions_Task.__mro__:
        if "fixedRate" in klass.__dict__:
            descriptor = klass.__dict__["fixedRate"]
            break
    assert isinstance(descriptor, property)

def test_oaam_functions_task_has_nParallels():
    assert hasattr(oaam_functions_Task, "nParallels")
    descriptor = None
    for klass in oaam_functions_Task.__mro__:
        if "nParallels" in klass.__dict__:
            descriptor = klass.__dict__["nParallels"]
            break
    assert isinstance(descriptor, property)



def test_oaam_systems_informationpower_is_not_abstract():
    assert not inspect.isabstract(oaam_systems_InformationPower)


def test_oaam_systems_informationpower_constructor_exists():
    assert callable(oaam_systems_InformationPower.__init__)


def test_oaam_systems_informationpower_constructor_args():
    sig = inspect.signature(oaam_systems_InformationPower.__init__)
    params = list(sig.parameters.keys())
    assert "power" in params, "Missing parameter 'power'"

def test_oaam_systems_informationpower_has_power():
    assert hasattr(oaam_systems_InformationPower, "power")
    descriptor = None
    for klass in oaam_systems_InformationPower.__mro__:
        if "power" in klass.__dict__:
            descriptor = klass.__dict__["power"]
            break
    assert isinstance(descriptor, property)



def test_oaam_allocations_messagesegment_is_not_abstract():
    assert not inspect.isabstract(oaam_allocations_MessageSegment)


def test_oaam_allocations_messagesegment_constructor_exists():
    assert callable(oaam_allocations_MessageSegment.__init__)


def test_oaam_allocations_messagesegment_constructor_args():
    sig = inspect.signature(oaam_allocations_MessageSegment.__init__)
    params = list(sig.parameters.keys())



def test_oaam_capabilities_deviceinlocationcapability_is_not_abstract():
    assert not inspect.isabstract(oaam_capabilities_DeviceInLocationCapability)


def test_oaam_capabilities_deviceinlocationcapability_constructor_exists():
    assert callable(oaam_capabilities_DeviceInLocationCapability.__init__)


def test_oaam_capabilities_deviceinlocationcapability_constructor_args():
    sig = inspect.signature(oaam_capabilities_DeviceInLocationCapability.__init__)
    params = list(sig.parameters.keys())



def test_oaam_scenario_scenarioparameternumeric_is_not_abstract():
    assert not inspect.isabstract(oaam_scenario_ScenarioParameterNumeric)


def test_oaam_scenario_scenarioparameternumeric_constructor_exists():
    assert callable(oaam_scenario_ScenarioParameterNumeric.__init__)


def test_oaam_scenario_scenarioparameternumeric_constructor_args():
    sig = inspect.signature(oaam_scenario_ScenarioParameterNumeric.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oaam_scenario_scenarioparameternumeric_has_value():
    assert hasattr(oaam_scenario_ScenarioParameterNumeric, "value")
    descriptor = None
    for klass in oaam_scenario_ScenarioParameterNumeric.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oaam_systems_informationmaterial_is_not_abstract():
    assert not inspect.isabstract(oaam_systems_InformationMaterial)


def test_oaam_systems_informationmaterial_constructor_exists():
    assert callable(oaam_systems_InformationMaterial.__init__)


def test_oaam_systems_informationmaterial_constructor_args():
    sig = inspect.signature(oaam_systems_InformationMaterial.__init__)
    params = list(sig.parameters.keys())
    assert "density" in params, "Missing parameter 'density'"
    assert "velocity" in params, "Missing parameter 'velocity'"

def test_oaam_systems_informationmaterial_has_density():
    assert hasattr(oaam_systems_InformationMaterial, "density")
    descriptor = None
    for klass in oaam_systems_InformationMaterial.__mro__:
        if "density" in klass.__dict__:
            descriptor = klass.__dict__["density"]
            break
    assert isinstance(descriptor, property)

def test_oaam_systems_informationmaterial_has_velocity():
    assert hasattr(oaam_systems_InformationMaterial, "velocity")
    descriptor = None
    for klass in oaam_systems_InformationMaterial.__mro__:
        if "velocity" in klass.__dict__:
            descriptor = klass.__dict__["velocity"]
            break
    assert isinstance(descriptor, property)



def test_oaam_systems_system_is_not_abstract():
    assert not inspect.isabstract(oaam_systems_System)


def test_oaam_systems_system_constructor_exists():
    assert callable(oaam_systems_System.__init__)


def test_oaam_systems_system_constructor_args():
    sig = inspect.signature(oaam_systems_System.__init__)
    params = list(sig.parameters.keys())



def test_oaam_restrictions_devicerestriction_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_DeviceRestriction)


def test_oaam_restrictions_devicerestriction_constructor_exists():
    assert callable(oaam_restrictions_DeviceRestriction.__init__)


def test_oaam_restrictions_devicerestriction_constructor_args():
    sig = inspect.signature(oaam_restrictions_DeviceRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "deviceName" in params, "Missing parameter 'deviceName'"
    assert "isForbidden" in params, "Missing parameter 'isForbidden'"

def test_oaam_restrictions_devicerestriction_has_deviceName():
    assert hasattr(oaam_restrictions_DeviceRestriction, "deviceName")
    descriptor = None
    for klass in oaam_restrictions_DeviceRestriction.__mro__:
        if "deviceName" in klass.__dict__:
            descriptor = klass.__dict__["deviceName"]
            break
    assert isinstance(descriptor, property)

def test_oaam_restrictions_devicerestriction_has_isForbidden():
    assert hasattr(oaam_restrictions_DeviceRestriction, "isForbidden")
    descriptor = None
    for klass in oaam_restrictions_DeviceRestriction.__mro__:
        if "isForbidden" in klass.__dict__:
            descriptor = klass.__dict__["isForbidden"]
            break
    assert isinstance(descriptor, property)



def test_oaam_functions_taskgroup_is_not_abstract():
    assert not inspect.isabstract(oaam_functions_TaskGroup)


def test_oaam_functions_taskgroup_constructor_exists():
    assert callable(oaam_functions_TaskGroup.__init__)


def test_oaam_functions_taskgroup_constructor_args():
    sig = inspect.signature(oaam_functions_TaskGroup.__init__)
    params = list(sig.parameters.keys())



def test_oaam_capabilities_subdeviceindevicecapability_is_not_abstract():
    assert not inspect.isabstract(oaam_capabilities_SubdeviceInDeviceCapability)


def test_oaam_capabilities_subdeviceindevicecapability_constructor_exists():
    assert callable(oaam_capabilities_SubdeviceInDeviceCapability.__init__)


def test_oaam_capabilities_subdeviceindevicecapability_constructor_args():
    sig = inspect.signature(oaam_capabilities_SubdeviceInDeviceCapability.__init__)
    params = list(sig.parameters.keys())



def test_oaam_scenario_variant_is_not_abstract():
    assert not inspect.isabstract(oaam_scenario_Variant)


def test_oaam_scenario_variant_constructor_exists():
    assert callable(oaam_scenario_Variant.__init__)


def test_oaam_scenario_variant_constructor_args():
    sig = inspect.signature(oaam_scenario_Variant.__init__)
    params = list(sig.parameters.keys())



def test_oaam_hardware_io_is_not_abstract():
    assert not inspect.isabstract(oaam_hardware_Io)


def test_oaam_hardware_io_constructor_exists():
    assert callable(oaam_hardware_Io.__init__)


def test_oaam_hardware_io_constructor_args():
    sig = inspect.signature(oaam_hardware_Io.__init__)
    params = list(sig.parameters.keys())



def test_oaam_systems_informationsignal_is_not_abstract():
    assert not inspect.isabstract(oaam_systems_InformationSignal)


def test_oaam_systems_informationsignal_constructor_exists():
    assert callable(oaam_systems_InformationSignal.__init__)


def test_oaam_systems_informationsignal_constructor_args():
    sig = inspect.signature(oaam_systems_InformationSignal.__init__)
    params = list(sig.parameters.keys())
    assert "rate" in params, "Missing parameter 'rate'"
    assert "resolution" in params, "Missing parameter 'resolution'"
    assert "latency" in params, "Missing parameter 'latency'"
    assert "accuracy" in params, "Missing parameter 'accuracy'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_oaam_systems_informationsignal_has_rate():
    assert hasattr(oaam_systems_InformationSignal, "rate")
    descriptor = None
    for klass in oaam_systems_InformationSignal.__mro__:
        if "rate" in klass.__dict__:
            descriptor = klass.__dict__["rate"]
            break
    assert isinstance(descriptor, property)

def test_oaam_systems_informationsignal_has_resolution():
    assert hasattr(oaam_systems_InformationSignal, "resolution")
    descriptor = None
    for klass in oaam_systems_InformationSignal.__mro__:
        if "resolution" in klass.__dict__:
            descriptor = klass.__dict__["resolution"]
            break
    assert isinstance(descriptor, property)

def test_oaam_systems_informationsignal_has_latency():
    assert hasattr(oaam_systems_InformationSignal, "latency")
    descriptor = None
    for klass in oaam_systems_InformationSignal.__mro__:
        if "latency" in klass.__dict__:
            descriptor = klass.__dict__["latency"]
            break
    assert isinstance(descriptor, property)

def test_oaam_systems_informationsignal_has_accuracy():
    assert hasattr(oaam_systems_InformationSignal, "accuracy")
    descriptor = None
    for klass in oaam_systems_InformationSignal.__mro__:
        if "accuracy" in klass.__dict__:
            descriptor = klass.__dict__["accuracy"]
            break
    assert isinstance(descriptor, property)

def test_oaam_systems_informationsignal_has_unit():
    assert hasattr(oaam_systems_InformationSignal, "unit")
    descriptor = None
    for klass in oaam_systems_InformationSignal.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_oaam_allocations_connectionassignment_is_not_abstract():
    assert not inspect.isabstract(oaam_allocations_ConnectionAssignment)


def test_oaam_allocations_connectionassignment_constructor_exists():
    assert callable(oaam_allocations_ConnectionAssignment.__init__)


def test_oaam_allocations_connectionassignment_constructor_args():
    sig = inspect.signature(oaam_allocations_ConnectionAssignment.__init__)
    params = list(sig.parameters.keys())



def test_oaam_restrictions_synchronicityrestriction_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_SynchronicityRestriction)


def test_oaam_restrictions_synchronicityrestriction_constructor_exists():
    assert callable(oaam_restrictions_SynchronicityRestriction.__init__)


def test_oaam_restrictions_synchronicityrestriction_constructor_args():
    sig = inspect.signature(oaam_restrictions_SynchronicityRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "maxJitter" in params, "Missing parameter 'maxJitter'"

def test_oaam_restrictions_synchronicityrestriction_has_maxJitter():
    assert hasattr(oaam_restrictions_SynchronicityRestriction, "maxJitter")
    descriptor = None
    for klass in oaam_restrictions_SynchronicityRestriction.__mro__:
        if "maxJitter" in klass.__dict__:
            descriptor = klass.__dict__["maxJitter"]
            break
    assert isinstance(descriptor, property)



def test_oaam_functions_externaltasklink_is_not_abstract():
    assert not inspect.isabstract(oaam_functions_ExternalTaskLink)


def test_oaam_functions_externaltasklink_constructor_exists():
    assert callable(oaam_functions_ExternalTaskLink.__init__)


def test_oaam_functions_externaltasklink_constructor_args():
    sig = inspect.signature(oaam_functions_ExternalTaskLink.__init__)
    params = list(sig.parameters.keys())
    assert "filter" in params, "Missing parameter 'filter'"

def test_oaam_functions_externaltasklink_has_filter():
    assert hasattr(oaam_functions_ExternalTaskLink, "filter")
    descriptor = None
    for klass in oaam_functions_ExternalTaskLink.__mro__:
        if "filter" in klass.__dict__:
            descriptor = klass.__dict__["filter"]
            break
    assert isinstance(descriptor, property)



def test_oaam_library_messagetype_is_not_abstract():
    assert not inspect.isabstract(oaam_library_MessageType)


def test_oaam_library_messagetype_constructor_exists():
    assert callable(oaam_library_MessageType.__init__)


def test_oaam_library_messagetype_constructor_args():
    sig = inspect.signature(oaam_library_MessageType.__init__)
    params = list(sig.parameters.keys())
    assert "minLength" in params, "Missing parameter 'minLength'"
    assert "maxLength" in params, "Missing parameter 'maxLength'"
    assert "alignment" in params, "Missing parameter 'alignment'"

def test_oaam_library_messagetype_has_minLength():
    assert hasattr(oaam_library_MessageType, "minLength")
    descriptor = None
    for klass in oaam_library_MessageType.__mro__:
        if "minLength" in klass.__dict__:
            descriptor = klass.__dict__["minLength"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_messagetype_has_maxLength():
    assert hasattr(oaam_library_MessageType, "maxLength")
    descriptor = None
    for klass in oaam_library_MessageType.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_messagetype_has_alignment():
    assert hasattr(oaam_library_MessageType, "alignment")
    descriptor = None
    for klass in oaam_library_MessageType.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)



def test_oaam_functions_functionscontainera_is_not_abstract():
    assert not inspect.isabstract(oaam_functions_FunctionsContainerA)


def test_oaam_functions_functionscontainera_constructor_exists():
    assert callable(oaam_functions_FunctionsContainerA.__init__)


def test_oaam_functions_functionscontainera_constructor_args():
    sig = inspect.signature(oaam_functions_FunctionsContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_allocations_signalassignment_is_not_abstract():
    assert not inspect.isabstract(oaam_allocations_SignalAssignment)


def test_oaam_allocations_signalassignment_constructor_exists():
    assert callable(oaam_allocations_SignalAssignment.__init__)


def test_oaam_allocations_signalassignment_constructor_args():
    sig = inspect.signature(oaam_allocations_SignalAssignment.__init__)
    params = list(sig.parameters.keys())



def test_oaam_anatomy_areasymmetry_is_not_abstract():
    assert not inspect.isabstract(oaam_anatomy_AreaSymmetry)


def test_oaam_anatomy_areasymmetry_constructor_exists():
    assert callable(oaam_anatomy_AreaSymmetry.__init__)


def test_oaam_anatomy_areasymmetry_constructor_args():
    sig = inspect.signature(oaam_anatomy_AreaSymmetry.__init__)
    params = list(sig.parameters.keys())



def test_oaam_anatomy_area_is_not_abstract():
    assert not inspect.isabstract(oaam_anatomy_Area)


def test_oaam_anatomy_area_constructor_exists():
    assert callable(oaam_anatomy_Area.__init__)


def test_oaam_anatomy_area_constructor_args():
    sig = inspect.signature(oaam_anatomy_Area.__init__)
    params = list(sig.parameters.keys())



def test_oaam_hardware_bus_is_not_abstract():
    assert not inspect.isabstract(oaam_hardware_Bus)


def test_oaam_hardware_bus_constructor_exists():
    assert callable(oaam_hardware_Bus.__init__)


def test_oaam_hardware_bus_constructor_args():
    sig = inspect.signature(oaam_hardware_Bus.__init__)
    params = list(sig.parameters.keys())



def test_oaam_restrictions_locationrestriction_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_LocationRestriction)


def test_oaam_restrictions_locationrestriction_constructor_exists():
    assert callable(oaam_restrictions_LocationRestriction.__init__)


def test_oaam_restrictions_locationrestriction_constructor_args():
    sig = inspect.signature(oaam_restrictions_LocationRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "isForbidden" in params, "Missing parameter 'isForbidden'"
    assert "locationName" in params, "Missing parameter 'locationName'"

def test_oaam_restrictions_locationrestriction_has_isForbidden():
    assert hasattr(oaam_restrictions_LocationRestriction, "isForbidden")
    descriptor = None
    for klass in oaam_restrictions_LocationRestriction.__mro__:
        if "isForbidden" in klass.__dict__:
            descriptor = klass.__dict__["isForbidden"]
            break
    assert isinstance(descriptor, property)

def test_oaam_restrictions_locationrestriction_has_locationName():
    assert hasattr(oaam_restrictions_LocationRestriction, "locationName")
    descriptor = None
    for klass in oaam_restrictions_LocationRestriction.__mro__:
        if "locationName" in klass.__dict__:
            descriptor = klass.__dict__["locationName"]
            break
    assert isinstance(descriptor, property)



def test_oaam_allocations_subconnectionassignment_is_not_abstract():
    assert not inspect.isabstract(oaam_allocations_SubconnectionAssignment)


def test_oaam_allocations_subconnectionassignment_constructor_exists():
    assert callable(oaam_allocations_SubconnectionAssignment.__init__)


def test_oaam_allocations_subconnectionassignment_constructor_args():
    sig = inspect.signature(oaam_allocations_SubconnectionAssignment.__init__)
    params = list(sig.parameters.keys())



def test_oaam_hardware_devicesymmetry_is_not_abstract():
    assert not inspect.isabstract(oaam_hardware_DeviceSymmetry)


def test_oaam_hardware_devicesymmetry_constructor_exists():
    assert callable(oaam_hardware_DeviceSymmetry.__init__)


def test_oaam_hardware_devicesymmetry_constructor_args():
    sig = inspect.signature(oaam_hardware_DeviceSymmetry.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_locationtype_is_not_abstract():
    assert not inspect.isabstract(oaam_library_LocationType)


def test_oaam_library_locationtype_constructor_exists():
    assert callable(oaam_library_LocationType.__init__)


def test_oaam_library_locationtype_constructor_args():
    sig = inspect.signature(oaam_library_LocationType.__init__)
    params = list(sig.parameters.keys())
    assert "isJoint" in params, "Missing parameter 'isJoint'"

def test_oaam_library_locationtype_has_isJoint():
    assert hasattr(oaam_library_LocationType, "isJoint")
    descriptor = None
    for klass in oaam_library_LocationType.__mro__:
        if "isJoint" in klass.__dict__:
            descriptor = klass.__dict__["isJoint"]
            break
    assert isinstance(descriptor, property)



def test_oaam_capabilities_signalonconnectionordevicecapability_is_not_abstract():
    assert not inspect.isabstract(oaam_capabilities_SignalOnConnectionOrDeviceCapability)


def test_oaam_capabilities_signalonconnectionordevicecapability_constructor_exists():
    assert callable(oaam_capabilities_SignalOnConnectionOrDeviceCapability.__init__)


def test_oaam_capabilities_signalonconnectionordevicecapability_constructor_args():
    sig = inspect.signature(oaam_capabilities_SignalOnConnectionOrDeviceCapability.__init__)
    params = list(sig.parameters.keys())
    assert "worstCaseTransmissionTime" in params, "Missing parameter 'worstCaseTransmissionTime'"

def test_oaam_capabilities_signalonconnectionordevicecapability_has_worstCaseTransmissionTime():
    assert hasattr(oaam_capabilities_SignalOnConnectionOrDeviceCapability, "worstCaseTransmissionTime")
    descriptor = None
    for klass in oaam_capabilities_SignalOnConnectionOrDeviceCapability.__mro__:
        if "worstCaseTransmissionTime" in klass.__dict__:
            descriptor = klass.__dict__["worstCaseTransmissionTime"]
            break
    assert isinstance(descriptor, property)



def test_oaam_capabilities_taskondevicecapability_is_not_abstract():
    assert not inspect.isabstract(oaam_capabilities_TaskOnDeviceCapability)


def test_oaam_capabilities_taskondevicecapability_constructor_exists():
    assert callable(oaam_capabilities_TaskOnDeviceCapability.__init__)


def test_oaam_capabilities_taskondevicecapability_constructor_args():
    sig = inspect.signature(oaam_capabilities_TaskOnDeviceCapability.__init__)
    params = list(sig.parameters.keys())
    assert "worstCaseExecutionTime" in params, "Missing parameter 'worstCaseExecutionTime'"
    assert "failureProbability" in params, "Missing parameter 'failureProbability'"

def test_oaam_capabilities_taskondevicecapability_has_worstCaseExecutionTime():
    assert hasattr(oaam_capabilities_TaskOnDeviceCapability, "worstCaseExecutionTime")
    descriptor = None
    for klass in oaam_capabilities_TaskOnDeviceCapability.__mro__:
        if "worstCaseExecutionTime" in klass.__dict__:
            descriptor = klass.__dict__["worstCaseExecutionTime"]
            break
    assert isinstance(descriptor, property)

def test_oaam_capabilities_taskondevicecapability_has_failureProbability():
    assert hasattr(oaam_capabilities_TaskOnDeviceCapability, "failureProbability")
    descriptor = None
    for klass in oaam_capabilities_TaskOnDeviceCapability.__mro__:
        if "failureProbability" in klass.__dict__:
            descriptor = klass.__dict__["failureProbability"]
            break
    assert isinstance(descriptor, property)



def test_oaam_library_devicetype_is_not_abstract():
    assert not inspect.isabstract(oaam_library_DeviceType)


def test_oaam_library_devicetype_constructor_exists():
    assert callable(oaam_library_DeviceType.__init__)


def test_oaam_library_devicetype_constructor_args():
    sig = inspect.signature(oaam_library_DeviceType.__init__)
    params = list(sig.parameters.keys())
    assert "isSubdevice" in params, "Missing parameter 'isSubdevice'"
    assert "cost" in params, "Missing parameter 'cost'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "mtbf" in params, "Missing parameter 'mtbf'"
    assert "canHaveSubdevices" in params, "Missing parameter 'canHaveSubdevices'"
    assert "isSelfManaging" in params, "Missing parameter 'isSelfManaging'"

def test_oaam_library_devicetype_has_isSubdevice():
    assert hasattr(oaam_library_DeviceType, "isSubdevice")
    descriptor = None
    for klass in oaam_library_DeviceType.__mro__:
        if "isSubdevice" in klass.__dict__:
            descriptor = klass.__dict__["isSubdevice"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_devicetype_has_cost():
    assert hasattr(oaam_library_DeviceType, "cost")
    descriptor = None
    for klass in oaam_library_DeviceType.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_devicetype_has_weight():
    assert hasattr(oaam_library_DeviceType, "weight")
    descriptor = None
    for klass in oaam_library_DeviceType.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_devicetype_has_mtbf():
    assert hasattr(oaam_library_DeviceType, "mtbf")
    descriptor = None
    for klass in oaam_library_DeviceType.__mro__:
        if "mtbf" in klass.__dict__:
            descriptor = klass.__dict__["mtbf"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_devicetype_has_canHaveSubdevices():
    assert hasattr(oaam_library_DeviceType, "canHaveSubdevices")
    descriptor = None
    for klass in oaam_library_DeviceType.__mro__:
        if "canHaveSubdevices" in klass.__dict__:
            descriptor = klass.__dict__["canHaveSubdevices"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_devicetype_has_isSelfManaging():
    assert hasattr(oaam_library_DeviceType, "isSelfManaging")
    descriptor = None
    for klass in oaam_library_DeviceType.__mro__:
        if "isSelfManaging" in klass.__dict__:
            descriptor = klass.__dict__["isSelfManaging"]
            break
    assert isinstance(descriptor, property)



def test_oaam_restrictions_taskatomicrestriction_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_TaskAtomicRestriction)


def test_oaam_restrictions_taskatomicrestriction_constructor_exists():
    assert callable(oaam_restrictions_TaskAtomicRestriction.__init__)


def test_oaam_restrictions_taskatomicrestriction_constructor_args():
    sig = inspect.signature(oaam_restrictions_TaskAtomicRestriction.__init__)
    params = list(sig.parameters.keys())



def test_oaam_functions_input_is_not_abstract():
    assert not inspect.isabstract(oaam_functions_Input)


def test_oaam_functions_input_constructor_exists():
    assert callable(oaam_functions_Input.__init__)


def test_oaam_functions_input_constructor_args():
    sig = inspect.signature(oaam_functions_Input.__init__)
    params = list(sig.parameters.keys())
    assert "queueLength" in params, "Missing parameter 'queueLength'"

def test_oaam_functions_input_has_queueLength():
    assert hasattr(oaam_functions_Input, "queueLength")
    descriptor = None
    for klass in oaam_functions_Input.__mro__:
        if "queueLength" in klass.__dict__:
            descriptor = klass.__dict__["queueLength"]
            break
    assert isinstance(descriptor, property)



def test_oaam_capabilities_submessageinmessagecapability_is_not_abstract():
    assert not inspect.isabstract(oaam_capabilities_SubmessageInMessageCapability)


def test_oaam_capabilities_submessageinmessagecapability_constructor_exists():
    assert callable(oaam_capabilities_SubmessageInMessageCapability.__init__)


def test_oaam_capabilities_submessageinmessagecapability_constructor_args():
    sig = inspect.signature(oaam_capabilities_SubmessageInMessageCapability.__init__)
    params = list(sig.parameters.keys())



def test_oaam_restrictions_devicetyperestriction_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_DeviceTypeRestriction)


def test_oaam_restrictions_devicetyperestriction_constructor_exists():
    assert callable(oaam_restrictions_DeviceTypeRestriction.__init__)


def test_oaam_restrictions_devicetyperestriction_constructor_args():
    sig = inspect.signature(oaam_restrictions_DeviceTypeRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "isForbidden" in params, "Missing parameter 'isForbidden'"
    assert "deviceTypeName" in params, "Missing parameter 'deviceTypeName'"

def test_oaam_restrictions_devicetyperestriction_has_isForbidden():
    assert hasattr(oaam_restrictions_DeviceTypeRestriction, "isForbidden")
    descriptor = None
    for klass in oaam_restrictions_DeviceTypeRestriction.__mro__:
        if "isForbidden" in klass.__dict__:
            descriptor = klass.__dict__["isForbidden"]
            break
    assert isinstance(descriptor, property)

def test_oaam_restrictions_devicetyperestriction_has_deviceTypeName():
    assert hasattr(oaam_restrictions_DeviceTypeRestriction, "deviceTypeName")
    descriptor = None
    for klass in oaam_restrictions_DeviceTypeRestriction.__mro__:
        if "deviceTypeName" in klass.__dict__:
            descriptor = klass.__dict__["deviceTypeName"]
            break
    assert isinstance(descriptor, property)



def test_oaam_functions_externaloutputlink_is_not_abstract():
    assert not inspect.isabstract(oaam_functions_ExternalOutputLink)


def test_oaam_functions_externaloutputlink_constructor_exists():
    assert callable(oaam_functions_ExternalOutputLink.__init__)


def test_oaam_functions_externaloutputlink_constructor_args():
    sig = inspect.signature(oaam_functions_ExternalOutputLink.__init__)
    params = list(sig.parameters.keys())
    assert "filter" in params, "Missing parameter 'filter'"

def test_oaam_functions_externaloutputlink_has_filter():
    assert hasattr(oaam_functions_ExternalOutputLink, "filter")
    descriptor = None
    for klass in oaam_functions_ExternalOutputLink.__mro__:
        if "filter" in klass.__dict__:
            descriptor = klass.__dict__["filter"]
            break
    assert isinstance(descriptor, property)



def test_oaam_anatomy_position3d_is_not_abstract():
    assert not inspect.isabstract(oaam_anatomy_Position3D)


def test_oaam_anatomy_position3d_constructor_exists():
    assert callable(oaam_anatomy_Position3D.__init__)


def test_oaam_anatomy_position3d_constructor_args():
    sig = inspect.signature(oaam_anatomy_Position3D.__init__)
    params = list(sig.parameters.keys())
    assert "z" in params, "Missing parameter 'z'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_oaam_anatomy_position3d_has_z():
    assert hasattr(oaam_anatomy_Position3D, "z")
    descriptor = None
    for klass in oaam_anatomy_Position3D.__mro__:
        if "z" in klass.__dict__:
            descriptor = klass.__dict__["z"]
            break
    assert isinstance(descriptor, property)

def test_oaam_anatomy_position3d_has_y():
    assert hasattr(oaam_anatomy_Position3D, "y")
    descriptor = None
    for klass in oaam_anatomy_Position3D.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_oaam_anatomy_position3d_has_x():
    assert hasattr(oaam_anatomy_Position3D, "x")
    descriptor = None
    for klass in oaam_anatomy_Position3D.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_oaam_library_connectiontype_is_not_abstract():
    assert not inspect.isabstract(oaam_library_ConnectionType)


def test_oaam_library_connectiontype_constructor_exists():
    assert callable(oaam_library_ConnectionType.__init__)


def test_oaam_library_connectiontype_constructor_args():
    sig = inspect.signature(oaam_library_ConnectionType.__init__)
    params = list(sig.parameters.keys())
    assert "nEndPoints" in params, "Missing parameter 'nEndPoints'"
    assert "nJoints" in params, "Missing parameter 'nJoints'"
    assert "isPower" in params, "Missing parameter 'isPower'"
    assert "maxInterfaceToJointDistance" in params, "Missing parameter 'maxInterfaceToJointDistance'"
    assert "requiresMaster" in params, "Missing parameter 'requiresMaster'"
    assert "maxJointBranches" in params, "Missing parameter 'maxJointBranches'"
    assert "maxLength" in params, "Missing parameter 'maxLength'"
    assert "isInformation" in params, "Missing parameter 'isInformation'"
    assert "nStartingPoints" in params, "Missing parameter 'nStartingPoints'"
    assert "isSwitched" in params, "Missing parameter 'isSwitched'"
    assert "isWireless" in params, "Missing parameter 'isWireless'"
    assert "allowsCircles" in params, "Missing parameter 'allowsCircles'"
    assert "isUnidirectional" in params, "Missing parameter 'isUnidirectional'"
    assert "directConnectionsAllowed" in params, "Missing parameter 'directConnectionsAllowed'"

def test_oaam_library_connectiontype_has_nEndPoints():
    assert hasattr(oaam_library_ConnectionType, "nEndPoints")
    descriptor = None
    for klass in oaam_library_ConnectionType.__mro__:
        if "nEndPoints" in klass.__dict__:
            descriptor = klass.__dict__["nEndPoints"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_connectiontype_has_nJoints():
    assert hasattr(oaam_library_ConnectionType, "nJoints")
    descriptor = None
    for klass in oaam_library_ConnectionType.__mro__:
        if "nJoints" in klass.__dict__:
            descriptor = klass.__dict__["nJoints"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_connectiontype_has_isPower():
    assert hasattr(oaam_library_ConnectionType, "isPower")
    descriptor = None
    for klass in oaam_library_ConnectionType.__mro__:
        if "isPower" in klass.__dict__:
            descriptor = klass.__dict__["isPower"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_connectiontype_has_maxInterfaceToJointDistance():
    assert hasattr(oaam_library_ConnectionType, "maxInterfaceToJointDistance")
    descriptor = None
    for klass in oaam_library_ConnectionType.__mro__:
        if "maxInterfaceToJointDistance" in klass.__dict__:
            descriptor = klass.__dict__["maxInterfaceToJointDistance"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_connectiontype_has_requiresMaster():
    assert hasattr(oaam_library_ConnectionType, "requiresMaster")
    descriptor = None
    for klass in oaam_library_ConnectionType.__mro__:
        if "requiresMaster" in klass.__dict__:
            descriptor = klass.__dict__["requiresMaster"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_connectiontype_has_maxJointBranches():
    assert hasattr(oaam_library_ConnectionType, "maxJointBranches")
    descriptor = None
    for klass in oaam_library_ConnectionType.__mro__:
        if "maxJointBranches" in klass.__dict__:
            descriptor = klass.__dict__["maxJointBranches"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_connectiontype_has_maxLength():
    assert hasattr(oaam_library_ConnectionType, "maxLength")
    descriptor = None
    for klass in oaam_library_ConnectionType.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_connectiontype_has_isInformation():
    assert hasattr(oaam_library_ConnectionType, "isInformation")
    descriptor = None
    for klass in oaam_library_ConnectionType.__mro__:
        if "isInformation" in klass.__dict__:
            descriptor = klass.__dict__["isInformation"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_connectiontype_has_nStartingPoints():
    assert hasattr(oaam_library_ConnectionType, "nStartingPoints")
    descriptor = None
    for klass in oaam_library_ConnectionType.__mro__:
        if "nStartingPoints" in klass.__dict__:
            descriptor = klass.__dict__["nStartingPoints"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_connectiontype_has_isSwitched():
    assert hasattr(oaam_library_ConnectionType, "isSwitched")
    descriptor = None
    for klass in oaam_library_ConnectionType.__mro__:
        if "isSwitched" in klass.__dict__:
            descriptor = klass.__dict__["isSwitched"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_connectiontype_has_isWireless():
    assert hasattr(oaam_library_ConnectionType, "isWireless")
    descriptor = None
    for klass in oaam_library_ConnectionType.__mro__:
        if "isWireless" in klass.__dict__:
            descriptor = klass.__dict__["isWireless"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_connectiontype_has_allowsCircles():
    assert hasattr(oaam_library_ConnectionType, "allowsCircles")
    descriptor = None
    for klass in oaam_library_ConnectionType.__mro__:
        if "allowsCircles" in klass.__dict__:
            descriptor = klass.__dict__["allowsCircles"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_connectiontype_has_isUnidirectional():
    assert hasattr(oaam_library_ConnectionType, "isUnidirectional")
    descriptor = None
    for klass in oaam_library_ConnectionType.__mro__:
        if "isUnidirectional" in klass.__dict__:
            descriptor = klass.__dict__["isUnidirectional"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_connectiontype_has_directConnectionsAllowed():
    assert hasattr(oaam_library_ConnectionType, "directConnectionsAllowed")
    descriptor = None
    for klass in oaam_library_ConnectionType.__mro__:
        if "directConnectionsAllowed" in klass.__dict__:
            descriptor = klass.__dict__["directConnectionsAllowed"]
            break
    assert isinstance(descriptor, property)



def test_oaam_allocations_messagea_is_not_abstract():
    assert not inspect.isabstract(oaam_allocations_MessageA)


def test_oaam_allocations_messagea_constructor_exists():
    assert callable(oaam_allocations_MessageA.__init__)


def test_oaam_allocations_messagea_constructor_args():
    sig = inspect.signature(oaam_allocations_MessageA.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "isPersistent" in params, "Missing parameter 'isPersistent'"

def test_oaam_allocations_messagea_has_length():
    assert hasattr(oaam_allocations_MessageA, "length")
    descriptor = None
    for klass in oaam_allocations_MessageA.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_oaam_allocations_messagea_has_isPersistent():
    assert hasattr(oaam_allocations_MessageA, "isPersistent")
    descriptor = None
    for klass in oaam_allocations_MessageA.__mro__:
        if "isPersistent" in klass.__dict__:
            descriptor = klass.__dict__["isPersistent"]
            break
    assert isinstance(descriptor, property)



def test_oaam_functions_taskredundancy_is_not_abstract():
    assert not inspect.isabstract(oaam_functions_TaskRedundancy)


def test_oaam_functions_taskredundancy_constructor_exists():
    assert callable(oaam_functions_TaskRedundancy.__init__)


def test_oaam_functions_taskredundancy_constructor_args():
    sig = inspect.signature(oaam_functions_TaskRedundancy.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_bustype_is_not_abstract():
    assert not inspect.isabstract(oaam_library_BusType)


def test_oaam_library_bustype_constructor_exists():
    assert callable(oaam_library_BusType.__init__)


def test_oaam_library_bustype_constructor_args():
    sig = inspect.signature(oaam_library_BusType.__init__)
    params = list(sig.parameters.keys())
    assert "isSelfManaging" in params, "Missing parameter 'isSelfManaging'"
    assert "requiresMaster" in params, "Missing parameter 'requiresMaster'"
    assert "mtbf" in params, "Missing parameter 'mtbf'"

def test_oaam_library_bustype_has_isSelfManaging():
    assert hasattr(oaam_library_BusType, "isSelfManaging")
    descriptor = None
    for klass in oaam_library_BusType.__mro__:
        if "isSelfManaging" in klass.__dict__:
            descriptor = klass.__dict__["isSelfManaging"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_bustype_has_requiresMaster():
    assert hasattr(oaam_library_BusType, "requiresMaster")
    descriptor = None
    for klass in oaam_library_BusType.__mro__:
        if "requiresMaster" in klass.__dict__:
            descriptor = klass.__dict__["requiresMaster"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_bustype_has_mtbf():
    assert hasattr(oaam_library_BusType, "mtbf")
    descriptor = None
    for klass in oaam_library_BusType.__mro__:
        if "mtbf" in klass.__dict__:
            descriptor = klass.__dict__["mtbf"]
            break
    assert isinstance(descriptor, property)



def test_oaam_capabilities_connectioninductorlocationcapability_is_not_abstract():
    assert not inspect.isabstract(oaam_capabilities_ConnectionInDuctOrLocationCapability)


def test_oaam_capabilities_connectioninductorlocationcapability_constructor_exists():
    assert callable(oaam_capabilities_ConnectionInDuctOrLocationCapability.__init__)


def test_oaam_capabilities_connectioninductorlocationcapability_constructor_args():
    sig = inspect.signature(oaam_capabilities_ConnectionInDuctOrLocationCapability.__init__)
    params = list(sig.parameters.keys())



def test_oaam_scenario_scenarioparameterbool_is_not_abstract():
    assert not inspect.isabstract(oaam_scenario_ScenarioParameterBool)


def test_oaam_scenario_scenarioparameterbool_constructor_exists():
    assert callable(oaam_scenario_ScenarioParameterBool.__init__)


def test_oaam_scenario_scenarioparameterbool_constructor_args():
    sig = inspect.signature(oaam_scenario_ScenarioParameterBool.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oaam_scenario_scenarioparameterbool_has_value():
    assert hasattr(oaam_scenario_ScenarioParameterBool, "value")
    descriptor = None
    for klass in oaam_scenario_ScenarioParameterBool.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oaam_functions_output_is_not_abstract():
    assert not inspect.isabstract(oaam_functions_Output)


def test_oaam_functions_output_constructor_exists():
    assert callable(oaam_functions_Output.__init__)


def test_oaam_functions_output_constructor_args():
    sig = inspect.signature(oaam_functions_Output.__init__)
    params = list(sig.parameters.keys())
    assert "fixedRate" in params, "Missing parameter 'fixedRate'"

def test_oaam_functions_output_has_fixedRate():
    assert hasattr(oaam_functions_Output, "fixedRate")
    descriptor = None
    for klass in oaam_functions_Output.__mro__:
        if "fixedRate" in klass.__dict__:
            descriptor = klass.__dict__["fixedRate"]
            break
    assert isinstance(descriptor, property)



def test_oaam_allocations_signalassignmentsegment_is_not_abstract():
    assert not inspect.isabstract(oaam_allocations_SignalAssignmentSegment)


def test_oaam_allocations_signalassignmentsegment_constructor_exists():
    assert callable(oaam_allocations_SignalAssignmentSegment.__init__)


def test_oaam_allocations_signalassignmentsegment_constructor_args():
    sig = inspect.signature(oaam_allocations_SignalAssignmentSegment.__init__)
    params = list(sig.parameters.keys())



def test_oaam_allocations_connectionassignmentsegment_is_not_abstract():
    assert not inspect.isabstract(oaam_allocations_ConnectionAssignmentSegment)


def test_oaam_allocations_connectionassignmentsegment_constructor_exists():
    assert callable(oaam_allocations_ConnectionAssignmentSegment.__init__)


def test_oaam_allocations_connectionassignmentsegment_constructor_args():
    sig = inspect.signature(oaam_allocations_ConnectionAssignmentSegment.__init__)
    params = list(sig.parameters.keys())



def test_oaam_restrictions_timedelayrestriction_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_TimeDelayRestriction)


def test_oaam_restrictions_timedelayrestriction_constructor_exists():
    assert callable(oaam_restrictions_TimeDelayRestriction.__init__)


def test_oaam_restrictions_timedelayrestriction_constructor_args():
    sig = inspect.signature(oaam_restrictions_TimeDelayRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "delay" in params, "Missing parameter 'delay'"

def test_oaam_restrictions_timedelayrestriction_has_delay():
    assert hasattr(oaam_restrictions_TimeDelayRestriction, "delay")
    descriptor = None
    for klass in oaam_restrictions_TimeDelayRestriction.__mro__:
        if "delay" in klass.__dict__:
            descriptor = klass.__dict__["delay"]
            break
    assert isinstance(descriptor, property)



def test_oaam_allocations_subdeviceassignment_is_not_abstract():
    assert not inspect.isabstract(oaam_allocations_SubdeviceAssignment)


def test_oaam_allocations_subdeviceassignment_constructor_exists():
    assert callable(oaam_allocations_SubdeviceAssignment.__init__)


def test_oaam_allocations_subdeviceassignment_constructor_args():
    sig = inspect.signature(oaam_allocations_SubdeviceAssignment.__init__)
    params = list(sig.parameters.keys())



def test_oaam_functions_tasksymmetry_is_not_abstract():
    assert not inspect.isabstract(oaam_functions_TaskSymmetry)


def test_oaam_functions_tasksymmetry_constructor_exists():
    assert callable(oaam_functions_TaskSymmetry.__init__)


def test_oaam_functions_tasksymmetry_constructor_args():
    sig = inspect.signature(oaam_functions_TaskSymmetry.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_ducttype_is_not_abstract():
    assert not inspect.isabstract(oaam_library_DuctType)


def test_oaam_library_ducttype_constructor_exists():
    assert callable(oaam_library_DuctType.__init__)


def test_oaam_library_ducttype_constructor_args():
    sig = inspect.signature(oaam_library_DuctType.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_signaltype_is_not_abstract():
    assert not inspect.isabstract(oaam_library_SignalType)


def test_oaam_library_signaltype_constructor_exists():
    assert callable(oaam_library_SignalType.__init__)


def test_oaam_library_signaltype_constructor_args():
    sig = inspect.signature(oaam_library_SignalType.__init__)
    params = list(sig.parameters.keys())



def test_oaam_restrictions_tasksymmetryrestriction_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_TaskSymmetryRestriction)


def test_oaam_restrictions_tasksymmetryrestriction_constructor_exists():
    assert callable(oaam_restrictions_TaskSymmetryRestriction.__init__)


def test_oaam_restrictions_tasksymmetryrestriction_constructor_args():
    sig = inspect.signature(oaam_restrictions_TaskSymmetryRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_oaam_restrictions_tasksymmetryrestriction_has_type():
    assert hasattr(oaam_restrictions_TaskSymmetryRestriction, "type")
    descriptor = None
    for klass in oaam_restrictions_TaskSymmetryRestriction.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_oaam_library_resourcebundle_is_not_abstract():
    assert not inspect.isabstract(oaam_library_ResourceBundle)


def test_oaam_library_resourcebundle_constructor_exists():
    assert callable(oaam_library_ResourceBundle.__init__)


def test_oaam_library_resourcebundle_constructor_args():
    sig = inspect.signature(oaam_library_ResourceBundle.__init__)
    params = list(sig.parameters.keys())
    assert "cost" in params, "Missing parameter 'cost'"
    assert "mtbf" in params, "Missing parameter 'mtbf'"
    assert "mass" in params, "Missing parameter 'mass'"

def test_oaam_library_resourcebundle_has_cost():
    assert hasattr(oaam_library_ResourceBundle, "cost")
    descriptor = None
    for klass in oaam_library_ResourceBundle.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_resourcebundle_has_mtbf():
    assert hasattr(oaam_library_ResourceBundle, "mtbf")
    descriptor = None
    for klass in oaam_library_ResourceBundle.__mro__:
        if "mtbf" in klass.__dict__:
            descriptor = klass.__dict__["mtbf"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_resourcebundle_has_mass():
    assert hasattr(oaam_library_ResourceBundle, "mass")
    descriptor = None
    for klass in oaam_library_ResourceBundle.__mro__:
        if "mass" in klass.__dict__:
            descriptor = klass.__dict__["mass"]
            break
    assert isinstance(descriptor, property)



def test_oaam_restrictions_powersourcerestriction_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_PowerSourceRestriction)


def test_oaam_restrictions_powersourcerestriction_constructor_exists():
    assert callable(oaam_restrictions_PowerSourceRestriction.__init__)


def test_oaam_restrictions_powersourcerestriction_constructor_args():
    sig = inspect.signature(oaam_restrictions_PowerSourceRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "isForbidden" in params, "Missing parameter 'isForbidden'"
    assert "powerSourceName" in params, "Missing parameter 'powerSourceName'"

def test_oaam_restrictions_powersourcerestriction_has_isForbidden():
    assert hasattr(oaam_restrictions_PowerSourceRestriction, "isForbidden")
    descriptor = None
    for klass in oaam_restrictions_PowerSourceRestriction.__mro__:
        if "isForbidden" in klass.__dict__:
            descriptor = klass.__dict__["isForbidden"]
            break
    assert isinstance(descriptor, property)

def test_oaam_restrictions_powersourcerestriction_has_powerSourceName():
    assert hasattr(oaam_restrictions_PowerSourceRestriction, "powerSourceName")
    descriptor = None
    for klass in oaam_restrictions_PowerSourceRestriction.__mro__:
        if "powerSourceName" in klass.__dict__:
            descriptor = klass.__dict__["powerSourceName"]
            break
    assert isinstance(descriptor, property)



def test_oaam_functions_signalgroup_is_not_abstract():
    assert not inspect.isabstract(oaam_functions_SignalGroup)


def test_oaam_functions_signalgroup_constructor_exists():
    assert callable(oaam_functions_SignalGroup.__init__)


def test_oaam_functions_signalgroup_constructor_args():
    sig = inspect.signature(oaam_functions_SignalGroup.__init__)
    params = list(sig.parameters.keys())



def test_oaam_systems_informationflow_is_not_abstract():
    assert not inspect.isabstract(oaam_systems_InformationFlow)


def test_oaam_systems_informationflow_constructor_exists():
    assert callable(oaam_systems_InformationFlow.__init__)


def test_oaam_systems_informationflow_constructor_args():
    sig = inspect.signature(oaam_systems_InformationFlow.__init__)
    params = list(sig.parameters.keys())



def test_oaam_allocations_taskassignment_is_not_abstract():
    assert not inspect.isabstract(oaam_allocations_TaskAssignment)


def test_oaam_allocations_taskassignment_constructor_exists():
    assert callable(oaam_allocations_TaskAssignment.__init__)


def test_oaam_allocations_taskassignment_constructor_args():
    sig = inspect.signature(oaam_allocations_TaskAssignment.__init__)
    params = list(sig.parameters.keys())



def test_oaam_anatomy_duct_is_not_abstract():
    assert not inspect.isabstract(oaam_anatomy_Duct)


def test_oaam_anatomy_duct_constructor_exists():
    assert callable(oaam_anatomy_Duct.__init__)


def test_oaam_anatomy_duct_constructor_args():
    sig = inspect.signature(oaam_anatomy_Duct.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_oaam_anatomy_duct_has_length():
    assert hasattr(oaam_anatomy_Duct, "length")
    descriptor = None
    for klass in oaam_anatomy_Duct.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_oaam_restrictions_segregationrestriction_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_SegregationRestriction)


def test_oaam_restrictions_segregationrestriction_constructor_exists():
    assert callable(oaam_restrictions_SegregationRestriction.__init__)


def test_oaam_restrictions_segregationrestriction_constructor_args():
    sig = inspect.signature(oaam_restrictions_SegregationRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "dissimilarLocation" in params, "Missing parameter 'dissimilarLocation'"
    assert "dissimilarPowerSource" in params, "Missing parameter 'dissimilarPowerSource'"
    assert "dissimilarArea" in params, "Missing parameter 'dissimilarArea'"
    assert "dissimilarTechnology" in params, "Missing parameter 'dissimilarTechnology'"

def test_oaam_restrictions_segregationrestriction_has_dissimilarLocation():
    assert hasattr(oaam_restrictions_SegregationRestriction, "dissimilarLocation")
    descriptor = None
    for klass in oaam_restrictions_SegregationRestriction.__mro__:
        if "dissimilarLocation" in klass.__dict__:
            descriptor = klass.__dict__["dissimilarLocation"]
            break
    assert isinstance(descriptor, property)

def test_oaam_restrictions_segregationrestriction_has_dissimilarPowerSource():
    assert hasattr(oaam_restrictions_SegregationRestriction, "dissimilarPowerSource")
    descriptor = None
    for klass in oaam_restrictions_SegregationRestriction.__mro__:
        if "dissimilarPowerSource" in klass.__dict__:
            descriptor = klass.__dict__["dissimilarPowerSource"]
            break
    assert isinstance(descriptor, property)

def test_oaam_restrictions_segregationrestriction_has_dissimilarArea():
    assert hasattr(oaam_restrictions_SegregationRestriction, "dissimilarArea")
    descriptor = None
    for klass in oaam_restrictions_SegregationRestriction.__mro__:
        if "dissimilarArea" in klass.__dict__:
            descriptor = klass.__dict__["dissimilarArea"]
            break
    assert isinstance(descriptor, property)

def test_oaam_restrictions_segregationrestriction_has_dissimilarTechnology():
    assert hasattr(oaam_restrictions_SegregationRestriction, "dissimilarTechnology")
    descriptor = None
    for klass in oaam_restrictions_SegregationRestriction.__mro__:
        if "dissimilarTechnology" in klass.__dict__:
            descriptor = klass.__dict__["dissimilarTechnology"]
            break
    assert isinstance(descriptor, property)



def test_oaam_anatomy_locationsymmetry_is_not_abstract():
    assert not inspect.isabstract(oaam_anatomy_LocationSymmetry)


def test_oaam_anatomy_locationsymmetry_constructor_exists():
    assert callable(oaam_anatomy_LocationSymmetry.__init__)


def test_oaam_anatomy_locationsymmetry_constructor_args():
    sig = inspect.signature(oaam_anatomy_LocationSymmetry.__init__)
    params = list(sig.parameters.keys())



def test_oaam_restrictions_arearestriction_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_AreaRestriction)


def test_oaam_restrictions_arearestriction_constructor_exists():
    assert callable(oaam_restrictions_AreaRestriction.__init__)


def test_oaam_restrictions_arearestriction_constructor_args():
    sig = inspect.signature(oaam_restrictions_AreaRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "areaName" in params, "Missing parameter 'areaName'"
    assert "isForbidden" in params, "Missing parameter 'isForbidden'"

def test_oaam_restrictions_arearestriction_has_areaName():
    assert hasattr(oaam_restrictions_AreaRestriction, "areaName")
    descriptor = None
    for klass in oaam_restrictions_AreaRestriction.__mro__:
        if "areaName" in klass.__dict__:
            descriptor = klass.__dict__["areaName"]
            break
    assert isinstance(descriptor, property)

def test_oaam_restrictions_arearestriction_has_isForbidden():
    assert hasattr(oaam_restrictions_AreaRestriction, "isForbidden")
    descriptor = None
    for klass in oaam_restrictions_AreaRestriction.__mro__:
        if "isForbidden" in klass.__dict__:
            descriptor = klass.__dict__["isForbidden"]
            break
    assert isinstance(descriptor, property)



def test_oaam_capabilities_messageonconnectionordevicecapability_is_not_abstract():
    assert not inspect.isabstract(oaam_capabilities_MessageOnConnectionOrDeviceCapability)


def test_oaam_capabilities_messageonconnectionordevicecapability_constructor_exists():
    assert callable(oaam_capabilities_MessageOnConnectionOrDeviceCapability.__init__)


def test_oaam_capabilities_messageonconnectionordevicecapability_constructor_args():
    sig = inspect.signature(oaam_capabilities_MessageOnConnectionOrDeviceCapability.__init__)
    params = list(sig.parameters.keys())
    assert "worstCaseTransmissionTime" in params, "Missing parameter 'worstCaseTransmissionTime'"

def test_oaam_capabilities_messageonconnectionordevicecapability_has_worstCaseTransmissionTime():
    assert hasattr(oaam_capabilities_MessageOnConnectionOrDeviceCapability, "worstCaseTransmissionTime")
    descriptor = None
    for klass in oaam_capabilities_MessageOnConnectionOrDeviceCapability.__mro__:
        if "worstCaseTransmissionTime" in klass.__dict__:
            descriptor = klass.__dict__["worstCaseTransmissionTime"]
            break
    assert isinstance(descriptor, property)



def test_oaam_library_resourcetype_is_not_abstract():
    assert not inspect.isabstract(oaam_library_ResourceType)


def test_oaam_library_resourcetype_constructor_exists():
    assert callable(oaam_library_ResourceType.__init__)


def test_oaam_library_resourcetype_constructor_args():
    sig = inspect.signature(oaam_library_ResourceType.__init__)
    params = list(sig.parameters.keys())
    assert "isConfigurable" in params, "Missing parameter 'isConfigurable'"
    assert "isIo" in params, "Missing parameter 'isIo'"
    assert "isDistinguishable" in params, "Missing parameter 'isDistinguishable'"
    assert "isPropagated" in params, "Missing parameter 'isPropagated'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "isConsumed" in params, "Missing parameter 'isConsumed'"

def test_oaam_library_resourcetype_has_isConfigurable():
    assert hasattr(oaam_library_ResourceType, "isConfigurable")
    descriptor = None
    for klass in oaam_library_ResourceType.__mro__:
        if "isConfigurable" in klass.__dict__:
            descriptor = klass.__dict__["isConfigurable"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_resourcetype_has_isIo():
    assert hasattr(oaam_library_ResourceType, "isIo")
    descriptor = None
    for klass in oaam_library_ResourceType.__mro__:
        if "isIo" in klass.__dict__:
            descriptor = klass.__dict__["isIo"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_resourcetype_has_isDistinguishable():
    assert hasattr(oaam_library_ResourceType, "isDistinguishable")
    descriptor = None
    for klass in oaam_library_ResourceType.__mro__:
        if "isDistinguishable" in klass.__dict__:
            descriptor = klass.__dict__["isDistinguishable"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_resourcetype_has_isPropagated():
    assert hasattr(oaam_library_ResourceType, "isPropagated")
    descriptor = None
    for klass in oaam_library_ResourceType.__mro__:
        if "isPropagated" in klass.__dict__:
            descriptor = klass.__dict__["isPropagated"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_resourcetype_has_unit():
    assert hasattr(oaam_library_ResourceType, "unit")
    descriptor = None
    for klass in oaam_library_ResourceType.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_resourcetype_has_direction():
    assert hasattr(oaam_library_ResourceType, "direction")
    descriptor = None
    for klass in oaam_library_ResourceType.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_resourcetype_has_isConsumed():
    assert hasattr(oaam_library_ResourceType, "isConsumed")
    descriptor = None
    for klass in oaam_library_ResourceType.__mro__:
        if "isConsumed" in klass.__dict__:
            descriptor = klass.__dict__["isConsumed"]
            break
    assert isinstance(descriptor, property)



def test_oaam_functions_failurecondition_is_not_abstract():
    assert not inspect.isabstract(oaam_functions_FailureCondition)


def test_oaam_functions_failurecondition_constructor_exists():
    assert callable(oaam_functions_FailureCondition.__init__)


def test_oaam_functions_failurecondition_constructor_args():
    sig = inspect.signature(oaam_functions_FailureCondition.__init__)
    params = list(sig.parameters.keys())
    assert "noSingleFailure" in params, "Missing parameter 'noSingleFailure'"
    assert "maxOccurrenceProbability" in params, "Missing parameter 'maxOccurrenceProbability'"

def test_oaam_functions_failurecondition_has_noSingleFailure():
    assert hasattr(oaam_functions_FailureCondition, "noSingleFailure")
    descriptor = None
    for klass in oaam_functions_FailureCondition.__mro__:
        if "noSingleFailure" in klass.__dict__:
            descriptor = klass.__dict__["noSingleFailure"]
            break
    assert isinstance(descriptor, property)

def test_oaam_functions_failurecondition_has_maxOccurrenceProbability():
    assert hasattr(oaam_functions_FailureCondition, "maxOccurrenceProbability")
    descriptor = None
    for klass in oaam_functions_FailureCondition.__mro__:
        if "maxOccurrenceProbability" in klass.__dict__:
            descriptor = klass.__dict__["maxOccurrenceProbability"]
            break
    assert isinstance(descriptor, property)



def test_oaam_capabilities_signalinmessagecapability_is_not_abstract():
    assert not inspect.isabstract(oaam_capabilities_SignalInMessageCapability)


def test_oaam_capabilities_signalinmessagecapability_constructor_exists():
    assert callable(oaam_capabilities_SignalInMessageCapability.__init__)


def test_oaam_capabilities_signalinmessagecapability_constructor_args():
    sig = inspect.signature(oaam_capabilities_SignalInMessageCapability.__init__)
    params = list(sig.parameters.keys())



def test_common_boola_is_not_abstract():
    assert not inspect.isabstract(common_BoolA)


def test_common_boola_constructor_exists():
    assert callable(common_BoolA.__init__)


def test_common_boola_constructor_args():
    sig = inspect.signature(common_BoolA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_taskinputstate_is_not_abstract():
    assert not inspect.isabstract(oaam_library_TaskInputState)


def test_oaam_library_taskinputstate_constructor_exists():
    assert callable(oaam_library_TaskInputState.__init__)


def test_oaam_library_taskinputstate_constructor_args():
    sig = inspect.signature(oaam_library_TaskInputState.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"

def test_oaam_library_taskinputstate_has_state():
    assert hasattr(oaam_library_TaskInputState, "state")
    descriptor = None
    for klass in oaam_library_TaskInputState.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)



def test_oaam_functions_outputintegritystate_is_not_abstract():
    assert not inspect.isabstract(oaam_functions_OutputIntegrityState)


def test_oaam_functions_outputintegritystate_constructor_exists():
    assert callable(oaam_functions_OutputIntegrityState.__init__)


def test_oaam_functions_outputintegritystate_constructor_args():
    sig = inspect.signature(oaam_functions_OutputIntegrityState.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"

def test_oaam_functions_outputintegritystate_has_state():
    assert hasattr(oaam_functions_OutputIntegrityState, "state")
    descriptor = None
    for klass in oaam_functions_OutputIntegrityState.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)



def test_oaam_library_taskinputtrigger_is_not_abstract():
    assert not inspect.isabstract(oaam_library_TaskInputTrigger)


def test_oaam_library_taskinputtrigger_constructor_exists():
    assert callable(oaam_library_TaskInputTrigger.__init__)


def test_oaam_library_taskinputtrigger_constructor_args():
    sig = inspect.signature(oaam_library_TaskInputTrigger.__init__)
    params = list(sig.parameters.keys())



def test_oaam_common_boolnot_is_not_abstract():
    assert not inspect.isabstract(oaam_common_BoolNot)


def test_oaam_common_boolnot_constructor_exists():
    assert callable(oaam_common_BoolNot.__init__)


def test_oaam_common_boolnot_constructor_args():
    sig = inspect.signature(oaam_common_BoolNot.__init__)
    params = list(sig.parameters.keys())



def test_oaam_common_booloperation_is_not_abstract():
    assert not inspect.isabstract(oaam_common_BoolOperation)


def test_oaam_common_booloperation_constructor_exists():
    assert callable(oaam_common_BoolOperation.__init__)


def test_oaam_common_booloperation_constructor_args():
    sig = inspect.signature(oaam_common_BoolOperation.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_oaam_common_booloperation_has_type():
    assert hasattr(oaam_common_BoolOperation, "type")
    descriptor = None
    for klass in oaam_common_BoolOperation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_oaam_common_boola_is_not_abstract():
    assert not inspect.isabstract(oaam_common_BoolA)


def test_oaam_common_boola_constructor_exists():
    assert callable(oaam_common_BoolA.__init__)


def test_oaam_common_boola_constructor_args():
    sig = inspect.signature(oaam_common_BoolA.__init__)
    params = list(sig.parameters.keys())



def test_attributea_is_not_abstract():
    assert not inspect.isabstract(AttributeA)


def test_attributea_constructor_exists():
    assert callable(AttributeA.__init__)


def test_attributea_constructor_args():
    sig = inspect.signature(AttributeA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_common_attributenumeric_is_not_abstract():
    assert not inspect.isabstract(oaam_common_AttributeNumeric)


def test_oaam_common_attributenumeric_constructor_exists():
    assert callable(oaam_common_AttributeNumeric.__init__)


def test_oaam_common_attributenumeric_constructor_args():
    sig = inspect.signature(oaam_common_AttributeNumeric.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oaam_common_attributenumeric_has_value():
    assert hasattr(oaam_common_AttributeNumeric, "value")
    descriptor = None
    for klass in oaam_common_AttributeNumeric.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oaam_common_attributestring_is_not_abstract():
    assert not inspect.isabstract(oaam_common_AttributeString)


def test_oaam_common_attributestring_constructor_exists():
    assert callable(oaam_common_AttributeString.__init__)


def test_oaam_common_attributestring_constructor_args():
    sig = inspect.signature(oaam_common_AttributeString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oaam_common_attributestring_has_value():
    assert hasattr(oaam_common_AttributeString, "value")
    descriptor = None
    for klass in oaam_common_AttributeString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oaam_common_attributereference_is_not_abstract():
    assert not inspect.isabstract(oaam_common_AttributeReference)


def test_oaam_common_attributereference_constructor_exists():
    assert callable(oaam_common_AttributeReference.__init__)


def test_oaam_common_attributereference_constructor_args():
    sig = inspect.signature(oaam_common_AttributeReference.__init__)
    params = list(sig.parameters.keys())



def test_oaam_common_attributecontainment_is_not_abstract():
    assert not inspect.isabstract(oaam_common_AttributeContainment)


def test_oaam_common_attributecontainment_constructor_exists():
    assert callable(oaam_common_AttributeContainment.__init__)


def test_oaam_common_attributecontainment_constructor_args():
    sig = inspect.signature(oaam_common_AttributeContainment.__init__)
    params = list(sig.parameters.keys())



def test_allocations_is_not_abstract():
    assert not inspect.isabstract(Allocations)


def test_allocations_constructor_exists():
    assert callable(Allocations.__init__)


def test_allocations_constructor_args():
    sig = inspect.signature(Allocations.__init__)
    params = list(sig.parameters.keys())



def test_restrictions_is_not_abstract():
    assert not inspect.isabstract(Restrictions)


def test_restrictions_constructor_exists():
    assert callable(Restrictions.__init__)


def test_restrictions_constructor_args():
    sig = inspect.signature(Restrictions.__init__)
    params = list(sig.parameters.keys())



def test_capabilities_is_not_abstract():
    assert not inspect.isabstract(Capabilities)


def test_capabilities_constructor_exists():
    assert callable(Capabilities.__init__)


def test_capabilities_constructor_args():
    sig = inspect.signature(Capabilities.__init__)
    params = list(sig.parameters.keys())



def test_anatomy_is_not_abstract():
    assert not inspect.isabstract(Anatomy)


def test_anatomy_constructor_exists():
    assert callable(Anatomy.__init__)


def test_anatomy_constructor_args():
    sig = inspect.signature(Anatomy.__init__)
    params = list(sig.parameters.keys())



def test_hardware_is_not_abstract():
    assert not inspect.isabstract(Hardware)


def test_hardware_constructor_exists():
    assert callable(Hardware.__init__)


def test_hardware_constructor_args():
    sig = inspect.signature(Hardware.__init__)
    params = list(sig.parameters.keys())



def test_functions_is_not_abstract():
    assert not inspect.isabstract(Functions)


def test_functions_constructor_exists():
    assert callable(Functions.__init__)


def test_functions_constructor_args():
    sig = inspect.signature(Functions.__init__)
    params = list(sig.parameters.keys())



def test_oaam_common_oaambaseelementa_is_not_abstract():
    assert not inspect.isabstract(oaam_common_OaamBaseElementA)


def test_oaam_common_oaambaseelementa_constructor_exists():
    assert callable(oaam_common_OaamBaseElementA.__init__)


def test_oaam_common_oaambaseelementa_constructor_args():
    sig = inspect.signature(oaam_common_OaamBaseElementA.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "traceLink" in params, "Missing parameter 'traceLink'"
    assert "modified" in params, "Missing parameter 'modified'"
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "modifier" in params, "Missing parameter 'modifier'"
    assert "style" in params, "Missing parameter 'style'"
    assert "name" in params, "Missing parameter 'name'"

def test_oaam_common_oaambaseelementa_has_id():
    assert hasattr(oaam_common_OaamBaseElementA, "id")
    descriptor = None
    for klass in oaam_common_OaamBaseElementA.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_oaam_common_oaambaseelementa_has_traceLink():
    assert hasattr(oaam_common_OaamBaseElementA, "traceLink")
    descriptor = None
    for klass in oaam_common_OaamBaseElementA.__mro__:
        if "traceLink" in klass.__dict__:
            descriptor = klass.__dict__["traceLink"]
            break
    assert isinstance(descriptor, property)

def test_oaam_common_oaambaseelementa_has_modified():
    assert hasattr(oaam_common_OaamBaseElementA, "modified")
    descriptor = None
    for klass in oaam_common_OaamBaseElementA.__mro__:
        if "modified" in klass.__dict__:
            descriptor = klass.__dict__["modified"]
            break
    assert isinstance(descriptor, property)

def test_oaam_common_oaambaseelementa_has_documentation():
    assert hasattr(oaam_common_OaamBaseElementA, "documentation")
    descriptor = None
    for klass in oaam_common_OaamBaseElementA.__mro__:
        if "documentation" in klass.__dict__:
            descriptor = klass.__dict__["documentation"]
            break
    assert isinstance(descriptor, property)

def test_oaam_common_oaambaseelementa_has_modifier():
    assert hasattr(oaam_common_OaamBaseElementA, "modifier")
    descriptor = None
    for klass in oaam_common_OaamBaseElementA.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)

def test_oaam_common_oaambaseelementa_has_style():
    assert hasattr(oaam_common_OaamBaseElementA, "style")
    descriptor = None
    for klass in oaam_common_OaamBaseElementA.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_oaam_common_oaambaseelementa_has_name():
    assert hasattr(oaam_common_OaamBaseElementA, "name")
    descriptor = None
    for klass in oaam_common_OaamBaseElementA.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_library_is_not_abstract():
    assert not inspect.isabstract(Library)


def test_library_constructor_exists():
    assert callable(Library.__init__)


def test_library_constructor_args():
    sig = inspect.signature(Library.__init__)
    params = list(sig.parameters.keys())



def test_oaambaseelementa_is_not_abstract():
    assert not inspect.isabstract(OaamBaseElementA)


def test_oaambaseelementa_constructor_exists():
    assert callable(OaamBaseElementA.__init__)


def test_oaambaseelementa_constructor_args():
    sig = inspect.signature(OaamBaseElementA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_powersource_is_not_abstract():
    assert not inspect.isabstract(oaam_library_PowerSource)


def test_oaam_library_powersource_constructor_exists():
    assert callable(oaam_library_PowerSource.__init__)


def test_oaam_library_powersource_constructor_args():
    sig = inspect.signature(oaam_library_PowerSource.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_devicetypedissimilarity_is_not_abstract():
    assert not inspect.isabstract(oaam_library_DeviceTypeDissimilarity)


def test_oaam_library_devicetypedissimilarity_constructor_exists():
    assert callable(oaam_library_DeviceTypeDissimilarity.__init__)


def test_oaam_library_devicetypedissimilarity_constructor_args():
    sig = inspect.signature(oaam_library_DeviceTypeDissimilarity.__init__)
    params = list(sig.parameters.keys())
    assert "percentageOfCommonHardware" in params, "Missing parameter 'percentageOfCommonHardware'"

def test_oaam_library_devicetypedissimilarity_has_percentageOfCommonHardware():
    assert hasattr(oaam_library_DeviceTypeDissimilarity, "percentageOfCommonHardware")
    descriptor = None
    for klass in oaam_library_DeviceTypeDissimilarity.__mro__:
        if "percentageOfCommonHardware" in klass.__dict__:
            descriptor = klass.__dict__["percentageOfCommonHardware"]
            break
    assert isinstance(descriptor, property)



def test_oaam_library_resource_is_not_abstract():
    assert not inspect.isabstract(oaam_library_Resource)


def test_oaam_library_resource_constructor_exists():
    assert callable(oaam_library_Resource.__init__)


def test_oaam_library_resource_constructor_args():
    sig = inspect.signature(oaam_library_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_oaam_library_resource_has_count():
    assert hasattr(oaam_library_Resource, "count")
    descriptor = None
    for klass in oaam_library_Resource.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_oaam_library_resourcetypemodifier_is_not_abstract():
    assert not inspect.isabstract(oaam_library_ResourceTypeModifier)


def test_oaam_library_resourcetypemodifier_constructor_exists():
    assert callable(oaam_library_ResourceTypeModifier.__init__)


def test_oaam_library_resourcetypemodifier_constructor_args():
    sig = inspect.signature(oaam_library_ResourceTypeModifier.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_iogroup_is_not_abstract():
    assert not inspect.isabstract(oaam_library_IoGroup)


def test_oaam_library_iogroup_constructor_exists():
    assert callable(oaam_library_IoGroup.__init__)


def test_oaam_library_iogroup_constructor_args():
    sig = inspect.signature(oaam_library_IoGroup.__init__)
    params = list(sig.parameters.keys())



def test_oaam_systems_systemscontainera_is_not_abstract():
    assert not inspect.isabstract(oaam_systems_SystemsContainerA)


def test_oaam_systems_systemscontainera_constructor_exists():
    assert callable(oaam_systems_SystemsContainerA.__init__)


def test_oaam_systems_systemscontainera_constructor_args():
    sig = inspect.signature(oaam_systems_SystemsContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_hardware_hardwarecontainera_is_not_abstract():
    assert not inspect.isabstract(oaam_hardware_HardwareContainerA)


def test_oaam_hardware_hardwarecontainera_constructor_exists():
    assert callable(oaam_hardware_HardwareContainerA.__init__)


def test_oaam_hardware_hardwarecontainera_constructor_args():
    sig = inspect.signature(oaam_hardware_HardwareContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_scenario_scenariocontainera_is_not_abstract():
    assert not inspect.isabstract(oaam_scenario_ScenarioContainerA)


def test_oaam_scenario_scenariocontainera_constructor_exists():
    assert callable(oaam_scenario_ScenarioContainerA.__init__)


def test_oaam_scenario_scenariocontainera_constructor_args():
    sig = inspect.signature(oaam_scenario_ScenarioContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_scenario_operationmodereference_is_not_abstract():
    assert not inspect.isabstract(oaam_scenario_OperationModeReference)


def test_oaam_scenario_operationmodereference_constructor_exists():
    assert callable(oaam_scenario_OperationModeReference.__init__)


def test_oaam_scenario_operationmodereference_constructor_args():
    sig = inspect.signature(oaam_scenario_OperationModeReference.__init__)
    params = list(sig.parameters.keys())
    assert "activeProbability" in params, "Missing parameter 'activeProbability'"

def test_oaam_scenario_operationmodereference_has_activeProbability():
    assert hasattr(oaam_scenario_OperationModeReference, "activeProbability")
    descriptor = None
    for klass in oaam_scenario_OperationModeReference.__mro__:
        if "activeProbability" in klass.__dict__:
            descriptor = klass.__dict__["activeProbability"]
            break
    assert isinstance(descriptor, property)



def test_oaam_systems_inputsegregation_is_not_abstract():
    assert not inspect.isabstract(oaam_systems_InputSegregation)


def test_oaam_systems_inputsegregation_constructor_exists():
    assert callable(oaam_systems_InputSegregation.__init__)


def test_oaam_systems_inputsegregation_constructor_args():
    sig = inspect.signature(oaam_systems_InputSegregation.__init__)
    params = list(sig.parameters.keys())
    assert "dissimilarSource" in params, "Missing parameter 'dissimilarSource'"
    assert "dissimilarTechnology" in params, "Missing parameter 'dissimilarTechnology'"
    assert "dissimilarRoute" in params, "Missing parameter 'dissimilarRoute'"

def test_oaam_systems_inputsegregation_has_dissimilarSource():
    assert hasattr(oaam_systems_InputSegregation, "dissimilarSource")
    descriptor = None
    for klass in oaam_systems_InputSegregation.__mro__:
        if "dissimilarSource" in klass.__dict__:
            descriptor = klass.__dict__["dissimilarSource"]
            break
    assert isinstance(descriptor, property)

def test_oaam_systems_inputsegregation_has_dissimilarTechnology():
    assert hasattr(oaam_systems_InputSegregation, "dissimilarTechnology")
    descriptor = None
    for klass in oaam_systems_InputSegregation.__mro__:
        if "dissimilarTechnology" in klass.__dict__:
            descriptor = klass.__dict__["dissimilarTechnology"]
            break
    assert isinstance(descriptor, property)

def test_oaam_systems_inputsegregation_has_dissimilarRoute():
    assert hasattr(oaam_systems_InputSegregation, "dissimilarRoute")
    descriptor = None
    for klass in oaam_systems_InputSegregation.__mro__:
        if "dissimilarRoute" in klass.__dict__:
            descriptor = klass.__dict__["dissimilarRoute"]
            break
    assert isinstance(descriptor, property)



def test_oaam_restrictions_restrictionscontainera_is_not_abstract():
    assert not inspect.isabstract(oaam_restrictions_RestrictionsContainerA)


def test_oaam_restrictions_restrictionscontainera_constructor_exists():
    assert callable(oaam_restrictions_RestrictionsContainerA.__init__)


def test_oaam_restrictions_restrictionscontainera_constructor_args():
    sig = inspect.signature(oaam_restrictions_RestrictionsContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_resourcealternatives_is_not_abstract():
    assert not inspect.isabstract(oaam_library_ResourceAlternatives)


def test_oaam_library_resourcealternatives_constructor_exists():
    assert callable(oaam_library_ResourceAlternatives.__init__)


def test_oaam_library_resourcealternatives_constructor_args():
    sig = inspect.signature(oaam_library_ResourceAlternatives.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_ductopeningdeclaration_is_not_abstract():
    assert not inspect.isabstract(oaam_library_DuctOpeningDeclaration)


def test_oaam_library_ductopeningdeclaration_constructor_exists():
    assert callable(oaam_library_DuctOpeningDeclaration.__init__)


def test_oaam_library_ductopeningdeclaration_constructor_args():
    sig = inspect.signature(oaam_library_DuctOpeningDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_oaam_common_datatypea_is_not_abstract():
    assert not inspect.isabstract(oaam_common_DataTypeA)


def test_oaam_common_datatypea_constructor_exists():
    assert callable(oaam_common_DataTypeA.__init__)


def test_oaam_common_datatypea_constructor_args():
    sig = inspect.signature(oaam_common_DataTypeA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_taskoutputtrigger_is_not_abstract():
    assert not inspect.isabstract(oaam_library_TaskOutputTrigger)


def test_oaam_library_taskoutputtrigger_constructor_exists():
    assert callable(oaam_library_TaskOutputTrigger.__init__)


def test_oaam_library_taskoutputtrigger_constructor_args():
    sig = inspect.signature(oaam_library_TaskOutputTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "isFixedRate" in params, "Missing parameter 'isFixedRate'"
    assert "fixedRate" in params, "Missing parameter 'fixedRate'"

def test_oaam_library_taskoutputtrigger_has_isFixedRate():
    assert hasattr(oaam_library_TaskOutputTrigger, "isFixedRate")
    descriptor = None
    for klass in oaam_library_TaskOutputTrigger.__mro__:
        if "isFixedRate" in klass.__dict__:
            descriptor = klass.__dict__["isFixedRate"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_taskoutputtrigger_has_fixedRate():
    assert hasattr(oaam_library_TaskOutputTrigger, "fixedRate")
    descriptor = None
    for klass in oaam_library_TaskOutputTrigger.__mro__:
        if "fixedRate" in klass.__dict__:
            descriptor = klass.__dict__["fixedRate"]
            break
    assert isinstance(descriptor, property)



def test_oaam_library_resourcetypedissimilarity_is_not_abstract():
    assert not inspect.isabstract(oaam_library_ResourceTypeDissimilarity)


def test_oaam_library_resourcetypedissimilarity_constructor_exists():
    assert callable(oaam_library_ResourceTypeDissimilarity.__init__)


def test_oaam_library_resourcetypedissimilarity_constructor_args():
    sig = inspect.signature(oaam_library_ResourceTypeDissimilarity.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_resourcetypemodifierreference_is_not_abstract():
    assert not inspect.isabstract(oaam_library_ResourceTypeModifierReference)


def test_oaam_library_resourcetypemodifierreference_constructor_exists():
    assert callable(oaam_library_ResourceTypeModifierReference.__init__)


def test_oaam_library_resourcetypemodifierreference_constructor_args():
    sig = inspect.signature(oaam_library_ResourceTypeModifierReference.__init__)
    params = list(sig.parameters.keys())



def test_oaam_capabilities_capabilitiescontainera_is_not_abstract():
    assert not inspect.isabstract(oaam_capabilities_CapabilitiesContainerA)


def test_oaam_capabilities_capabilitiescontainera_constructor_exists():
    assert callable(oaam_capabilities_CapabilitiesContainerA.__init__)


def test_oaam_capabilities_capabilitiescontainera_constructor_args():
    sig = inspect.signature(oaam_capabilities_CapabilitiesContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_resourcelink_is_not_abstract():
    assert not inspect.isabstract(oaam_library_ResourceLink)


def test_oaam_library_resourcelink_constructor_exists():
    assert callable(oaam_library_ResourceLink.__init__)


def test_oaam_library_resourcelink_constructor_args():
    sig = inspect.signature(oaam_library_ResourceLink.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_devicetypesymmetry_is_not_abstract():
    assert not inspect.isabstract(oaam_library_DeviceTypeSymmetry)


def test_oaam_library_devicetypesymmetry_constructor_exists():
    assert callable(oaam_library_DeviceTypeSymmetry.__init__)


def test_oaam_library_devicetypesymmetry_constructor_args():
    sig = inspect.signature(oaam_library_DeviceTypeSymmetry.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_wiretype_is_not_abstract():
    assert not inspect.isabstract(oaam_library_WireType)


def test_oaam_library_wiretype_constructor_exists():
    assert callable(oaam_library_WireType.__init__)


def test_oaam_library_wiretype_constructor_args():
    sig = inspect.signature(oaam_library_WireType.__init__)
    params = list(sig.parameters.keys())
    assert "nConductors" in params, "Missing parameter 'nConductors'"
    assert "mtbf" in params, "Missing parameter 'mtbf'"
    assert "specificPrice" in params, "Missing parameter 'specificPrice'"
    assert "specificWeight" in params, "Missing parameter 'specificWeight'"
    assert "nShields" in params, "Missing parameter 'nShields'"
    assert "minBendingRadius" in params, "Missing parameter 'minBendingRadius'"

def test_oaam_library_wiretype_has_nConductors():
    assert hasattr(oaam_library_WireType, "nConductors")
    descriptor = None
    for klass in oaam_library_WireType.__mro__:
        if "nConductors" in klass.__dict__:
            descriptor = klass.__dict__["nConductors"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_wiretype_has_mtbf():
    assert hasattr(oaam_library_WireType, "mtbf")
    descriptor = None
    for klass in oaam_library_WireType.__mro__:
        if "mtbf" in klass.__dict__:
            descriptor = klass.__dict__["mtbf"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_wiretype_has_specificPrice():
    assert hasattr(oaam_library_WireType, "specificPrice")
    descriptor = None
    for klass in oaam_library_WireType.__mro__:
        if "specificPrice" in klass.__dict__:
            descriptor = klass.__dict__["specificPrice"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_wiretype_has_specificWeight():
    assert hasattr(oaam_library_WireType, "specificWeight")
    descriptor = None
    for klass in oaam_library_WireType.__mro__:
        if "specificWeight" in klass.__dict__:
            descriptor = klass.__dict__["specificWeight"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_wiretype_has_nShields():
    assert hasattr(oaam_library_WireType, "nShields")
    descriptor = None
    for klass in oaam_library_WireType.__mro__:
        if "nShields" in klass.__dict__:
            descriptor = klass.__dict__["nShields"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_wiretype_has_minBendingRadius():
    assert hasattr(oaam_library_WireType, "minBendingRadius")
    descriptor = None
    for klass in oaam_library_WireType.__mro__:
        if "minBendingRadius" in klass.__dict__:
            descriptor = klass.__dict__["minBendingRadius"]
            break
    assert isinstance(descriptor, property)



def test_oaam_library_librarycontainera_is_not_abstract():
    assert not inspect.isabstract(oaam_library_LibraryContainerA)


def test_oaam_library_librarycontainera_constructor_exists():
    assert callable(oaam_library_LibraryContainerA.__init__)


def test_oaam_library_librarycontainera_constructor_args():
    sig = inspect.signature(oaam_library_LibraryContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_tasktypedissimilarity_is_not_abstract():
    assert not inspect.isabstract(oaam_library_TaskTypeDissimilarity)


def test_oaam_library_tasktypedissimilarity_constructor_exists():
    assert callable(oaam_library_TaskTypeDissimilarity.__init__)


def test_oaam_library_tasktypedissimilarity_constructor_args():
    sig = inspect.signature(oaam_library_TaskTypeDissimilarity.__init__)
    params = list(sig.parameters.keys())
    assert "percentageOfCommonCode" in params, "Missing parameter 'percentageOfCommonCode'"

def test_oaam_library_tasktypedissimilarity_has_percentageOfCommonCode():
    assert hasattr(oaam_library_TaskTypeDissimilarity, "percentageOfCommonCode")
    descriptor = None
    for klass in oaam_library_TaskTypeDissimilarity.__mro__:
        if "percentageOfCommonCode" in klass.__dict__:
            descriptor = klass.__dict__["percentageOfCommonCode"]
            break
    assert isinstance(descriptor, property)



def test_oaam_library_inputdeclaration_is_not_abstract():
    assert not inspect.isabstract(oaam_library_InputDeclaration)


def test_oaam_library_inputdeclaration_constructor_exists():
    assert callable(oaam_library_InputDeclaration.__init__)


def test_oaam_library_inputdeclaration_constructor_args():
    sig = inspect.signature(oaam_library_InputDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "range" in params, "Missing parameter 'range'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "precondition" in params, "Missing parameter 'precondition'"

def test_oaam_library_inputdeclaration_has_unit():
    assert hasattr(oaam_library_InputDeclaration, "unit")
    descriptor = None
    for klass in oaam_library_InputDeclaration.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_inputdeclaration_has_range():
    assert hasattr(oaam_library_InputDeclaration, "range")
    descriptor = None
    for klass in oaam_library_InputDeclaration.__mro__:
        if "range" in klass.__dict__:
            descriptor = klass.__dict__["range"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_inputdeclaration_has_upperBound():
    assert hasattr(oaam_library_InputDeclaration, "upperBound")
    descriptor = None
    for klass in oaam_library_InputDeclaration.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_inputdeclaration_has_lowerBound():
    assert hasattr(oaam_library_InputDeclaration, "lowerBound")
    descriptor = None
    for klass in oaam_library_InputDeclaration.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_inputdeclaration_has_precondition():
    assert hasattr(oaam_library_InputDeclaration, "precondition")
    descriptor = None
    for klass in oaam_library_InputDeclaration.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)



def test_oaam_library_faultpropagation_is_not_abstract():
    assert not inspect.isabstract(oaam_library_FaultPropagation)


def test_oaam_library_faultpropagation_constructor_exists():
    assert callable(oaam_library_FaultPropagation.__init__)


def test_oaam_library_faultpropagation_constructor_args():
    sig = inspect.signature(oaam_library_FaultPropagation.__init__)
    params = list(sig.parameters.keys())
    assert "outputState" in params, "Missing parameter 'outputState'"

def test_oaam_library_faultpropagation_has_outputState():
    assert hasattr(oaam_library_FaultPropagation, "outputState")
    descriptor = None
    for klass in oaam_library_FaultPropagation.__mro__:
        if "outputState" in klass.__dict__:
            descriptor = klass.__dict__["outputState"]
            break
    assert isinstance(descriptor, property)



def test_oaam_common_attributea_is_not_abstract():
    assert not inspect.isabstract(oaam_common_AttributeA)


def test_oaam_common_attributea_constructor_exists():
    assert callable(oaam_common_AttributeA.__init__)


def test_oaam_common_attributea_constructor_args():
    sig = inspect.signature(oaam_common_AttributeA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_allocations_allocationscontainera_is_not_abstract():
    assert not inspect.isabstract(oaam_allocations_AllocationsContainerA)


def test_oaam_allocations_allocationscontainera_constructor_exists():
    assert callable(oaam_allocations_AllocationsContainerA.__init__)


def test_oaam_allocations_allocationscontainera_constructor_args():
    sig = inspect.signature(oaam_allocations_AllocationsContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_anatomy_anatomycontainera_is_not_abstract():
    assert not inspect.isabstract(oaam_anatomy_AnatomyContainerA)


def test_oaam_anatomy_anatomycontainera_constructor_exists():
    assert callable(oaam_anatomy_AnatomyContainerA.__init__)


def test_oaam_anatomy_anatomycontainera_constructor_args():
    sig = inspect.signature(oaam_anatomy_AnatomyContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam_functions_taskparameter_is_not_abstract():
    assert not inspect.isabstract(oaam_functions_TaskParameter)


def test_oaam_functions_taskparameter_constructor_exists():
    assert callable(oaam_functions_TaskParameter.__init__)


def test_oaam_functions_taskparameter_constructor_args():
    sig = inspect.signature(oaam_functions_TaskParameter.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oaam_functions_taskparameter_has_value():
    assert hasattr(oaam_functions_TaskParameter, "value")
    descriptor = None
    for klass in oaam_functions_TaskParameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oaam_library_attributedefinition_is_not_abstract():
    assert not inspect.isabstract(oaam_library_AttributeDefinition)


def test_oaam_library_attributedefinition_constructor_exists():
    assert callable(oaam_library_AttributeDefinition.__init__)


def test_oaam_library_attributedefinition_constructor_args():
    sig = inspect.signature(oaam_library_AttributeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "target" in params, "Missing parameter 'target'"
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_oaam_library_attributedefinition_has_target():
    assert hasattr(oaam_library_AttributeDefinition, "target")
    descriptor = None
    for klass in oaam_library_AttributeDefinition.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_attributedefinition_has_dataType():
    assert hasattr(oaam_library_AttributeDefinition, "dataType")
    descriptor = None
    for klass in oaam_library_AttributeDefinition.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_oaam_library_iodeclaration_is_not_abstract():
    assert not inspect.isabstract(oaam_library_IoDeclaration)


def test_oaam_library_iodeclaration_constructor_exists():
    assert callable(oaam_library_IoDeclaration.__init__)


def test_oaam_library_iodeclaration_constructor_args():
    sig = inspect.signature(oaam_library_IoDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_taskparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(oaam_library_TaskParameterDeclaration)


def test_oaam_library_taskparameterdeclaration_constructor_exists():
    assert callable(oaam_library_TaskParameterDeclaration.__init__)


def test_oaam_library_taskparameterdeclaration_constructor_args():
    sig = inspect.signature(oaam_library_TaskParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_oaam_capabilities_resourceconsumption_is_not_abstract():
    assert not inspect.isabstract(oaam_capabilities_ResourceConsumption)


def test_oaam_capabilities_resourceconsumption_constructor_exists():
    assert callable(oaam_capabilities_ResourceConsumption.__init__)


def test_oaam_capabilities_resourceconsumption_constructor_args():
    sig = inspect.signature(oaam_capabilities_ResourceConsumption.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_oaam_capabilities_resourceconsumption_has_count():
    assert hasattr(oaam_capabilities_ResourceConsumption, "count")
    descriptor = None
    for klass in oaam_capabilities_ResourceConsumption.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_oaam_library_resourcegroup_is_not_abstract():
    assert not inspect.isabstract(oaam_library_ResourceGroup)


def test_oaam_library_resourcegroup_constructor_exists():
    assert callable(oaam_library_ResourceGroup.__init__)


def test_oaam_library_resourcegroup_constructor_args():
    sig = inspect.signature(oaam_library_ResourceGroup.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_outputdeclaration_is_not_abstract():
    assert not inspect.isabstract(oaam_library_OutputDeclaration)


def test_oaam_library_outputdeclaration_constructor_exists():
    assert callable(oaam_library_OutputDeclaration.__init__)


def test_oaam_library_outputdeclaration_constructor_args():
    sig = inspect.signature(oaam_library_OutputDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "range" in params, "Missing parameter 'range'"
    assert "postcondition" in params, "Missing parameter 'postcondition'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_oaam_library_outputdeclaration_has_lowerBound():
    assert hasattr(oaam_library_OutputDeclaration, "lowerBound")
    descriptor = None
    for klass in oaam_library_OutputDeclaration.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_outputdeclaration_has_unit():
    assert hasattr(oaam_library_OutputDeclaration, "unit")
    descriptor = None
    for klass in oaam_library_OutputDeclaration.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_outputdeclaration_has_range():
    assert hasattr(oaam_library_OutputDeclaration, "range")
    descriptor = None
    for klass in oaam_library_OutputDeclaration.__mro__:
        if "range" in klass.__dict__:
            descriptor = klass.__dict__["range"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_outputdeclaration_has_postcondition():
    assert hasattr(oaam_library_OutputDeclaration, "postcondition")
    descriptor = None
    for klass in oaam_library_OutputDeclaration.__mro__:
        if "postcondition" in klass.__dict__:
            descriptor = klass.__dict__["postcondition"]
            break
    assert isinstance(descriptor, property)

def test_oaam_library_outputdeclaration_has_upperBound():
    assert hasattr(oaam_library_OutputDeclaration, "upperBound")
    descriptor = None
    for klass in oaam_library_OutputDeclaration.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_oaam_library_taskstatedeclaration_is_not_abstract():
    assert not inspect.isabstract(oaam_library_TaskStateDeclaration)


def test_oaam_library_taskstatedeclaration_constructor_exists():
    assert callable(oaam_library_TaskStateDeclaration.__init__)


def test_oaam_library_taskstatedeclaration_constructor_args():
    sig = inspect.signature(oaam_library_TaskStateDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_oaam_library_iotype_is_not_abstract():
    assert not inspect.isabstract(oaam_library_IoType)


def test_oaam_library_iotype_constructor_exists():
    assert callable(oaam_library_IoType.__init__)


def test_oaam_library_iotype_constructor_args():
    sig = inspect.signature(oaam_library_IoType.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_oaam_library_iotype_has_direction():
    assert hasattr(oaam_library_IoType, "direction")
    descriptor = None
    for klass in oaam_library_IoType.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_oaam_architecture_is_not_abstract():
    assert not inspect.isabstract(oaam_Architecture)


def test_oaam_architecture_constructor_exists():
    assert callable(oaam_Architecture.__init__)


def test_oaam_architecture_constructor_args():
    sig = inspect.signature(oaam_Architecture.__init__)
    params = list(sig.parameters.keys())



def test_systems_is_not_abstract():
    assert not inspect.isabstract(Systems)


def test_systems_constructor_exists():
    assert callable(Systems.__init__)


def test_systems_constructor_args():
    sig = inspect.signature(Systems.__init__)
    params = list(sig.parameters.keys())



def test_scenario_is_not_abstract():
    assert not inspect.isabstract(Scenario)


def test_scenario_constructor_exists():
    assert callable(Scenario.__init__)


def test_scenario_constructor_args():
    sig = inspect.signature(Scenario.__init__)
    params = list(sig.parameters.keys())

def test_iodirectione_exists():
    # Check that the Enumeration exists
    assert IoDirectionE is not None

def test_iodirectione_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IoDirectionE]
    expected_literals = [
        "IN",
        "BOTH",
        "NONE",
        "OUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IoDirectionE"

def test_attributetargetse_exists():
    # Check that the Enumeration exists
    assert AttributeTargetsE is not None

def test_attributetargetse_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AttributeTargetsE]
    expected_literals = [
        "SIGNAL_TYPE",
        "AREA",
        "TASK_TYPE",
        "LOCATION",
        "CONNECTION",
        "VARIANT",
        "SIGNAL",
        "DUCT",
        "TASK",
        "CONNECTION_TYPE",
        "DUCT_TYPE",
        "DEVICE",
        "RESOURCE_GROUP",
        "RESOURCE",
        "RESOURCE_TYPE",
        "RESOURCE_BUNDLE",
        "DEVICE_TYPE",
        "WIRE_TYPE",
        "RESOURCE_ALTERNATIVE",
        "LOCATION_TYPE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AttributeTargetsE"

def test_endianesse_exists():
    # Check that the Enumeration exists
    assert EndianessE is not None

def test_endianesse_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EndianessE]
    expected_literals = [
        "LITTLE",
        "BIG",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EndianessE"

def test_integretystatee_exists():
    # Check that the Enumeration exists
    assert IntegretyStateE is not None

def test_integretystatee_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntegretyStateE]
    expected_literals = [
        "FAILED",
        "UNKNOWN",
        "OK",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntegretyStateE"

def test_booloperationtypese_exists():
    # Check that the Enumeration exists
    assert BoolOperationTypesE is not None

def test_booloperationtypese_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BoolOperationTypesE]
    expected_literals = [
        "XOR",
        "OR",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BoolOperationTypesE"

def test_attributetypese_exists():
    # Check that the Enumeration exists
    assert AttributeTypesE is not None

def test_attributetypese_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AttributeTypesE]
    expected_literals = [
        "NUMERIC",
        "STRING",
        "BOOL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AttributeTypesE"

def test_symmetrytypese_exists():
    # Check that the Enumeration exists
    assert SymmetryTypesE is not None

def test_symmetrytypese_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SymmetryTypesE]
    expected_literals = [
        "DEVICE_TYPE",
        "AREA",
        "LOCATION",
        "DEVICE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SymmetryTypesE"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
oaam_allocations_SignalToMessageAssignment_strategy = st.builds(
    oaam_allocations_SignalToMessageAssignment,
    position=
        st.integers()
)
allocations_AllocationsContainerA_strategy = st.builds(
    allocations_AllocationsContainerA,
)
AllocationsContainerA_strategy = st.builds(
    AllocationsContainerA,
)
oaam_allocations_Allocations_strategy = st.builds(
    oaam_allocations_Allocations,
)
MessageSegment_strategy = st.builds(
    MessageSegment,
)
SignalToMessageAssignment_strategy = st.builds(
    SignalToMessageAssignment,
)
Submessage_strategy = st.builds(
    Submessage,
)
MessageA_strategy = st.builds(
    MessageA,
)
oaam_allocations_Submessage_strategy = st.builds(
    oaam_allocations_Submessage,
    position=
        st.integers()
)
oaam_allocations_Message_strategy = st.builds(
    oaam_allocations_Message,
)
ScheduledTime_strategy = st.builds(
    ScheduledTime,
)
ConnectionAssignmentSegment_strategy = st.builds(
    ConnectionAssignmentSegment,
)
Area_strategy = st.builds(
    Area,
)
Duct_strategy = st.builds(
    Duct,
)
LocationSymmetry_strategy = st.builds(
    LocationSymmetry,
)
Position3D_strategy = st.builds(
    Position3D,
)
AreaSymmetry_strategy = st.builds(
    AreaSymmetry,
)
Subanatomy_strategy = st.builds(
    Subanatomy,
)
hardware_HardwareContainerA_strategy = st.builds(
    hardware_HardwareContainerA,
)
library_ResourceProviderInstanceA_strategy = st.builds(
    library_ResourceProviderInstanceA,
)
Bus_strategy = st.builds(
    Bus,
)
Subhardware_strategy = st.builds(
    Subhardware,
)
DeviceSymmetry_strategy = st.builds(
    DeviceSymmetry,
)
Location_strategy = st.builds(
    Location,
)
Connection_strategy = st.builds(
    Connection,
)
ExternalOutputLink_strategy = st.builds(
    ExternalOutputLink,
)
Io_strategy = st.builds(
    Io,
)
OutputIntegrityState_strategy = st.builds(
    OutputIntegrityState,
)
Output_strategy = st.builds(
    Output,
)
Input_strategy = st.builds(
    Input,
)
Subfunctions_strategy = st.builds(
    Subfunctions,
)
FailureCondition_strategy = st.builds(
    FailureCondition,
)
TaskParameter_strategy = st.builds(
    TaskParameter,
)
Device_strategy = st.builds(
    Device,
)
ExternalTaskLink_strategy = st.builds(
    ExternalTaskLink,
)
Task_strategy = st.builds(
    Task,
)
FunctionsContainerA_strategy = st.builds(
    FunctionsContainerA,
)
oaam_functions_Subfunctions_strategy = st.builds(
    oaam_functions_Subfunctions,
    multiplicityMax=
        st.integers(),
    multiplicityMin=
        st.integers()
)
oaam_functions_Functions_strategy = st.builds(
    oaam_functions_Functions,
)
SignalGroup_strategy = st.builds(
    SignalGroup,
)
Signal_strategy = st.builds(
    Signal,
)
TaskRedundancy_strategy = st.builds(
    TaskRedundancy,
)
TaskSymmetry_strategy = st.builds(
    TaskSymmetry,
)
TaskGroup_strategy = st.builds(
    TaskGroup,
)
InformationPower_strategy = st.builds(
    InformationPower,
)
oaam_systems_HydraulicPower_strategy = st.builds(
    oaam_systems_HydraulicPower,
    massFlowRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    pressure=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_systems_RotaryPower_strategy = st.builds(
    oaam_systems_RotaryPower,
    momentum=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    angularVelocity=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_systems_ElectricPower_strategy = st.builds(
    oaam_systems_ElectricPower,
    voltage=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    nPhases=
        st.integers(),
    frequency=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    current=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_systems_LinearPower_strategy = st.builds(
    oaam_systems_LinearPower,
    velocity=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    force=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
systems_RequiredInformationA_strategy = st.builds(
    systems_RequiredInformationA,
)
systems_ProvidedInformationA_strategy = st.builds(
    systems_ProvidedInformationA,
)
oaam_systems_ProvidedInformationA_strategy = st.builds(
    oaam_systems_ProvidedInformationA,
)
oaam_systems_RequiredInformationA_strategy = st.builds(
    oaam_systems_RequiredInformationA,
)
RequiredInformationA_strategy = st.builds(
    RequiredInformationA,
)
Subsystem_strategy = st.builds(
    Subsystem,
)
InputSegregation_strategy = st.builds(
    InputSegregation,
)
InformationFlow_strategy = st.builds(
    InformationFlow,
)
System_strategy = st.builds(
    System,
)
ScenarioContainerA_strategy = st.builds(
    ScenarioContainerA,
)
oaam_scenario_Subscenario_strategy = st.builds(
    oaam_scenario_Subscenario,
)
oaam_scenario_Scenario_strategy = st.builds(
    oaam_scenario_Scenario,
)
ProvidedInformationA_strategy = st.builds(
    ProvidedInformationA,
)
systems_SystemsContainerA_strategy = st.builds(
    systems_SystemsContainerA,
)
SystemsContainerA_strategy = st.builds(
    SystemsContainerA,
)
oaam_systems_Systems_strategy = st.builds(
    oaam_systems_Systems,
)
scenario_ScenarioParameterA_strategy = st.builds(
    scenario_ScenarioParameterA,
)
Subscenario_strategy = st.builds(
    Subscenario,
)
OperationMode_strategy = st.builds(
    OperationMode,
)
scenario_VariantDependentElementA_strategy = st.builds(
    scenario_VariantDependentElementA,
)
scenario_ModeDependentElementA_strategy = st.builds(
    scenario_ModeDependentElementA,
)
oaam_systems_Subsystem_strategy = st.builds(
    oaam_systems_Subsystem,
)
oaam_hardware_Subhardware_strategy = st.builds(
    oaam_hardware_Subhardware,
)
oaam_hardware_Hardware_strategy = st.builds(
    oaam_hardware_Hardware,
)
oaam_allocations_Suballocations_strategy = st.builds(
    oaam_allocations_Suballocations,
)
oaam_scenario_ScenarioParameterA_strategy = st.builds(
    oaam_scenario_ScenarioParameterA,
)
LibraryContainerA_strategy = st.builds(
    LibraryContainerA,
)
oaam_library_Sublibrary_strategy = st.builds(
    oaam_library_Sublibrary,
)
oaam_library_Library_strategy = st.builds(
    oaam_library_Library,
)
ScenarioParameterA_strategy = st.builds(
    ScenarioParameterA,
)
Variant_strategy = st.builds(
    Variant,
)
oaam_scenario_VariantDependentElementA_strategy = st.builds(
    oaam_scenario_VariantDependentElementA,
)
OperationModeReference_strategy = st.builds(
    OperationModeReference,
)
oaam_scenario_ModeDependentElementA_strategy = st.builds(
    oaam_scenario_ModeDependentElementA,
)
TaskInputTrigger_strategy = st.builds(
    TaskInputTrigger,
)
TaskInputState_strategy = st.builds(
    TaskInputState,
)
BoolNot_strategy = st.builds(
    BoolNot,
)
BoolOperation_strategy = st.builds(
    BoolOperation,
)
FaultPropagation_strategy = st.builds(
    FaultPropagation,
)
TaskOutputTrigger_strategy = st.builds(
    TaskOutputTrigger,
)
DuctOpeningDeclaration_strategy = st.builds(
    DuctOpeningDeclaration,
)
IoGroup_strategy = st.builds(
    IoGroup,
)
TaskParameterDeclaration_strategy = st.builds(
    TaskParameterDeclaration,
)
TaskStateDeclaration_strategy = st.builds(
    TaskStateDeclaration,
)
InputDeclaration_strategy = st.builds(
    InputDeclaration,
)
OutputDeclaration_strategy = st.builds(
    OutputDeclaration,
)
IoDeclaration_strategy = st.builds(
    IoDeclaration,
)
library_ResourceProviderA_strategy = st.builds(
    library_ResourceProviderA,
)
ResourceAlternatives_strategy = st.builds(
    ResourceAlternatives,
)
ResourceTypeModifierReference_strategy = st.builds(
    ResourceTypeModifierReference,
)
library_ResourceConsumerA_strategy = st.builds(
    library_ResourceConsumerA,
)
MessageType_strategy = st.builds(
    MessageType,
)
BusType_strategy = st.builds(
    BusType,
)
IoType_strategy = st.builds(
    IoType,
)
LocationType_strategy = st.builds(
    LocationType,
)
WireType_strategy = st.builds(
    WireType,
)
ConnectionType_strategy = st.builds(
    ConnectionType,
)
DeviceTypeDissimilarity_strategy = st.builds(
    DeviceTypeDissimilarity,
)
Sublibrary_strategy = st.builds(
    Sublibrary,
)
Message_strategy = st.builds(
    Message,
)
SubconnectionAssignment_strategy = st.builds(
    SubconnectionAssignment,
)
SignalAssignmentSegment_strategy = st.builds(
    SignalAssignmentSegment,
)
Schedule_strategy = st.builds(
    Schedule,
)
SubdeviceAssignment_strategy = st.builds(
    SubdeviceAssignment,
)
DeviceAssignment_strategy = st.builds(
    DeviceAssignment,
)
Suballocations_strategy = st.builds(
    Suballocations,
)
SignalAssignment_strategy = st.builds(
    SignalAssignment,
)
TaskAssignment_strategy = st.builds(
    TaskAssignment,
)
ConnectionAssignment_strategy = st.builds(
    ConnectionAssignment,
)
restrictions_RestrictionsContainerA_strategy = st.builds(
    restrictions_RestrictionsContainerA,
)
oaam_restrictions_Subrestrictions_strategy = st.builds(
    oaam_restrictions_Subrestrictions,
)
restrictions_ConnectionRestrinctionA_strategy = st.builds(
    restrictions_ConnectionRestrinctionA,
)
restrictions_DeviceRestrictionA_strategy = st.builds(
    restrictions_DeviceRestrictionA,
)
restrictions_SubfunctionRestrictionA_strategy = st.builds(
    restrictions_SubfunctionRestrictionA,
)
restrictions_SignalGroupRestrictionA_strategy = st.builds(
    restrictions_SignalGroupRestrictionA,
)
restrictions_SignalRestrictionA_strategy = st.builds(
    restrictions_SignalRestrictionA,
)
restrictions_TaskGroupRestrictionA_strategy = st.builds(
    restrictions_TaskGroupRestrictionA,
)
restrictions_TaskRestrictionA_strategy = st.builds(
    restrictions_TaskRestrictionA,
)
oaam_restrictions_SignalGroupRestrictionA_strategy = st.builds(
    oaam_restrictions_SignalGroupRestrictionA,
)
oaam_restrictions_TaskGroupRestrictionA_strategy = st.builds(
    oaam_restrictions_TaskGroupRestrictionA,
)
oaam_restrictions_SubfunctionRestrictionA_strategy = st.builds(
    oaam_restrictions_SubfunctionRestrictionA,
)
oaam_restrictions_DeviceRestrictionA_strategy = st.builds(
    oaam_restrictions_DeviceRestrictionA,
)
RestrictionsContainerA_strategy = st.builds(
    RestrictionsContainerA,
)
oaam_restrictions_Restrictions_strategy = st.builds(
    oaam_restrictions_Restrictions,
)
TimeDelayRestriction_strategy = st.builds(
    TimeDelayRestriction,
)
Subrestrictions_strategy = st.builds(
    Subrestrictions,
)
SegregationRestriction_strategy = st.builds(
    SegregationRestriction,
)
ConnectionTypeRestriction_strategy = st.builds(
    ConnectionTypeRestriction,
)
ConnectionRestriction_strategy = st.builds(
    ConnectionRestriction,
)
oaam_restrictions_SignalRestrictionA_strategy = st.builds(
    oaam_restrictions_SignalRestrictionA,
)
oaam_restrictions_TaskRestrictionA_strategy = st.builds(
    oaam_restrictions_TaskRestrictionA,
)
oaam_restrictions_ConnectionRestrinctionA_strategy = st.builds(
    oaam_restrictions_ConnectionRestrinctionA,
)
PowerSourceRestriction_strategy = st.builds(
    PowerSourceRestriction,
)
AreaRestriction_strategy = st.builds(
    AreaRestriction,
)
LocationRestriction_strategy = st.builds(
    LocationRestriction,
)
DeviceRestriction_strategy = st.builds(
    DeviceRestriction,
)
DeviceTypeRestriction_strategy = st.builds(
    DeviceTypeRestriction,
)
SynchronicityRestriction_strategy = st.builds(
    SynchronicityRestriction,
)
TaskSymmetryRestriction_strategy = st.builds(
    TaskSymmetryRestriction,
)
TaskAtomicRestriction_strategy = st.builds(
    TaskAtomicRestriction,
)
capabilities_CapabilitiesContainerA_strategy = st.builds(
    capabilities_CapabilitiesContainerA,
)
oaam_capabilities_Subcapabilities_strategy = st.builds(
    oaam_capabilities_Subcapabilities,
)
CapabilitiesContainerA_strategy = st.builds(
    CapabilitiesContainerA,
)
oaam_capabilities_Capabilities_strategy = st.builds(
    oaam_capabilities_Capabilities,
)
capabilities_CapabilityA_strategy = st.builds(
    capabilities_CapabilityA,
)
MessageOnConnectionOrDeviceCapability_strategy = st.builds(
    MessageOnConnectionOrDeviceCapability,
)
Subcapabilities_strategy = st.builds(
    Subcapabilities,
)
ConnectionInDuctOrLocationCapability_strategy = st.builds(
    ConnectionInDuctOrLocationCapability,
)
SubdeviceInDeviceCapability_strategy = st.builds(
    SubdeviceInDeviceCapability,
)
DeviceInLocationCapability_strategy = st.builds(
    DeviceInLocationCapability,
)
SignalOnConnectionOrDeviceCapability_strategy = st.builds(
    SignalOnConnectionOrDeviceCapability,
)
TaskOnDeviceCapability_strategy = st.builds(
    TaskOnDeviceCapability,
)
ResourceConsumption_strategy = st.builds(
    ResourceConsumption,
)
oaam_capabilities_CapabilityA_strategy = st.builds(
    oaam_capabilities_CapabilityA,
)
SignalInMessageCapability_strategy = st.builds(
    SignalInMessageCapability,
)
SubmessageInMessageCapability_strategy = st.builds(
    SubmessageInMessageCapability,
)
MessageOnBusCapability_strategy = st.builds(
    MessageOnBusCapability,
)
SubconnectionInDeviceCapability_strategy = st.builds(
    SubconnectionInDeviceCapability,
)
AnatomyContainerA_strategy = st.builds(
    AnatomyContainerA,
)
oaam_anatomy_Anatomy_strategy = st.builds(
    oaam_anatomy_Anatomy,
)
anatomy_AnatomyContainerA_strategy = st.builds(
    anatomy_AnatomyContainerA,
)
oaam_anatomy_Subanatomy_strategy = st.builds(
    oaam_anatomy_Subanatomy,
)
DuctOpening_strategy = st.builds(
    DuctOpening,
)
DeviceTypeSymmetry_strategy = st.builds(
    DeviceTypeSymmetry,
)
PowerSource_strategy = st.builds(
    PowerSource,
)
AttributeDefinition_strategy = st.builds(
    AttributeDefinition,
)
DuctType_strategy = st.builds(
    DuctType,
)
TaskTypeDissimilarity_strategy = st.builds(
    TaskTypeDissimilarity,
)
TaskType_strategy = st.builds(
    TaskType,
)
ResourceTypeDissimilarity_strategy = st.builds(
    ResourceTypeDissimilarity,
)
ResourceTypeModifier_strategy = st.builds(
    ResourceTypeModifier,
)
DeviceType_strategy = st.builds(
    DeviceType,
)
SignalType_strategy = st.builds(
    SignalType,
)
ResourceTypeModifierLevel_strategy = st.builds(
    ResourceTypeModifierLevel,
)
oaam_library_ResourceProviderInstanceA_strategy = st.builds(
    oaam_library_ResourceProviderInstanceA,
)
ResourceLink_strategy = st.builds(
    ResourceLink,
)
ResourceType_strategy = st.builds(
    ResourceType,
)
ResourceBundle_strategy = st.builds(
    ResourceBundle,
)
oaam_library_ResourceProviderA_strategy = st.builds(
    oaam_library_ResourceProviderA,
)
oaam_library_ResourceConsumerA_strategy = st.builds(
    oaam_library_ResourceConsumerA,
)
ResourceGroup_strategy = st.builds(
    ResourceGroup,
)
Resource_strategy = st.builds(
    Resource,
)
Struct_strategy = st.builds(
    Struct,
)
DataTypeA_strategy = st.builds(
    DataTypeA,
)
oaam_common_Array_strategy = st.builds(
    oaam_common_Array,
    nElements=
        st.integers(),
    alignment=
        st.integers()
)
oaam_common_Byte_strategy = st.builds(
    oaam_common_Byte,
    nBits=
        st.integers()
)
oaam_common_Character_strategy = st.builds(
    oaam_common_Character,
    nBits=
        st.integers(),
    encoding=
        safe_text
)
oaam_common_Boolean_strategy = st.builds(
    oaam_common_Boolean,
    nBits=
        st.integers()
)
oaam_common_Struct_strategy = st.builds(
    oaam_common_Struct,
    isAbstract=
        st.booleans(),
    alignment=
        st.integers()
)
oaam_common_FloatingPoint_strategy = st.builds(
    oaam_common_FloatingPoint,
    endianess=
        safe_text,
    nBits=
        st.integers()
)
oaam_common_Integer_strategy = st.builds(
    oaam_common_Integer,
    nBits=
        st.integers(),
    signed=
        st.booleans(),
    endianess=
        safe_text
)
BoolA_strategy = st.builds(
    BoolA,
)
common_OaamBaseElementA_strategy = st.builds(
    common_OaamBaseElementA,
)
oaam_allocations_DeviceAssignment_strategy = st.builds(
    oaam_allocations_DeviceAssignment,
)
oaam_functions_Signal_strategy = st.builds(
    oaam_functions_Signal,
    outIndex=
        st.integers(),
    inIndex=
        st.integers()
)
oaam_restrictions_ConnectionRestriction_strategy = st.builds(
    oaam_restrictions_ConnectionRestriction,
    isForbidden=
        st.booleans(),
    connectionName=
        safe_text
)
oaam_capabilities_MessageOnBusCapability_strategy = st.builds(
    oaam_capabilities_MessageOnBusCapability,
)
oaam_anatomy_DuctOpening_strategy = st.builds(
    oaam_anatomy_DuctOpening,
)
oaam_hardware_Connection_strategy = st.builds(
    oaam_hardware_Connection,
)
oaam_allocations_Schedule_strategy = st.builds(
    oaam_allocations_Schedule,
    isPeriodic=
        st.booleans(),
    priority=
        st.integers(),
    rate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_scenario_OperationMode_strategy = st.builds(
    oaam_scenario_OperationMode,
)
oaam_library_ResourceTypeModifierLevel_strategy = st.builds(
    oaam_library_ResourceTypeModifierLevel,
)
oaam_library_TaskType_strategy = st.builds(
    oaam_library_TaskType,
    preferredExecutionRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    isDeterministic=
        st.booleans()
)
oaam_anatomy_Location_strategy = st.builds(
    oaam_anatomy_Location,
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_capabilities_SubconnectionInDeviceCapability_strategy = st.builds(
    oaam_capabilities_SubconnectionInDeviceCapability,
)
oaam_restrictions_ConnectionTypeRestriction_strategy = st.builds(
    oaam_restrictions_ConnectionTypeRestriction,
    connectionTypeName=
        safe_text,
    isForbidden=
        st.booleans()
)
oaam_hardware_Device_strategy = st.builds(
    oaam_hardware_Device,
)
oaam_allocations_ScheduledTime_strategy = st.builds(
    oaam_allocations_ScheduledTime,
    restart=
        st.booleans(),
    duration=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    cycle=
        st.integers(),
    startTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_functions_Task_strategy = st.builds(
    oaam_functions_Task,
    fixedRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    nParallels=
        st.integers()
)
oaam_systems_InformationPower_strategy = st.builds(
    oaam_systems_InformationPower,
    power=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_allocations_MessageSegment_strategy = st.builds(
    oaam_allocations_MessageSegment,
)
oaam_capabilities_DeviceInLocationCapability_strategy = st.builds(
    oaam_capabilities_DeviceInLocationCapability,
)
oaam_scenario_ScenarioParameterNumeric_strategy = st.builds(
    oaam_scenario_ScenarioParameterNumeric,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_systems_InformationMaterial_strategy = st.builds(
    oaam_systems_InformationMaterial,
    density=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    velocity=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_systems_System_strategy = st.builds(
    oaam_systems_System,
)
oaam_restrictions_DeviceRestriction_strategy = st.builds(
    oaam_restrictions_DeviceRestriction,
    deviceName=
        safe_text,
    isForbidden=
        st.booleans()
)
oaam_functions_TaskGroup_strategy = st.builds(
    oaam_functions_TaskGroup,
)
oaam_capabilities_SubdeviceInDeviceCapability_strategy = st.builds(
    oaam_capabilities_SubdeviceInDeviceCapability,
)
oaam_scenario_Variant_strategy = st.builds(
    oaam_scenario_Variant,
)
oaam_hardware_Io_strategy = st.builds(
    oaam_hardware_Io,
)
oaam_systems_InformationSignal_strategy = st.builds(
    oaam_systems_InformationSignal,
    rate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    resolution=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    latency=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    accuracy=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    unit=
        safe_text
)
oaam_allocations_ConnectionAssignment_strategy = st.builds(
    oaam_allocations_ConnectionAssignment,
)
oaam_restrictions_SynchronicityRestriction_strategy = st.builds(
    oaam_restrictions_SynchronicityRestriction,
    maxJitter=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_functions_ExternalTaskLink_strategy = st.builds(
    oaam_functions_ExternalTaskLink,
    filter=
        safe_text
)
oaam_library_MessageType_strategy = st.builds(
    oaam_library_MessageType,
    minLength=
        st.integers(),
    maxLength=
        st.integers(),
    alignment=
        st.integers()
)
oaam_functions_FunctionsContainerA_strategy = st.builds(
    oaam_functions_FunctionsContainerA,
)
oaam_allocations_SignalAssignment_strategy = st.builds(
    oaam_allocations_SignalAssignment,
)
oaam_anatomy_AreaSymmetry_strategy = st.builds(
    oaam_anatomy_AreaSymmetry,
)
oaam_anatomy_Area_strategy = st.builds(
    oaam_anatomy_Area,
)
oaam_hardware_Bus_strategy = st.builds(
    oaam_hardware_Bus,
)
oaam_restrictions_LocationRestriction_strategy = st.builds(
    oaam_restrictions_LocationRestriction,
    isForbidden=
        st.booleans(),
    locationName=
        safe_text
)
oaam_allocations_SubconnectionAssignment_strategy = st.builds(
    oaam_allocations_SubconnectionAssignment,
)
oaam_hardware_DeviceSymmetry_strategy = st.builds(
    oaam_hardware_DeviceSymmetry,
)
oaam_library_LocationType_strategy = st.builds(
    oaam_library_LocationType,
    isJoint=
        st.booleans()
)
oaam_capabilities_SignalOnConnectionOrDeviceCapability_strategy = st.builds(
    oaam_capabilities_SignalOnConnectionOrDeviceCapability,
    worstCaseTransmissionTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_capabilities_TaskOnDeviceCapability_strategy = st.builds(
    oaam_capabilities_TaskOnDeviceCapability,
    worstCaseExecutionTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    failureProbability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_library_DeviceType_strategy = st.builds(
    oaam_library_DeviceType,
    isSubdevice=
        st.booleans(),
    cost=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    weight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    mtbf=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    canHaveSubdevices=
        st.booleans(),
    isSelfManaging=
        st.booleans()
)
oaam_restrictions_TaskAtomicRestriction_strategy = st.builds(
    oaam_restrictions_TaskAtomicRestriction,
)
oaam_functions_Input_strategy = st.builds(
    oaam_functions_Input,
    queueLength=
        st.integers()
)
oaam_capabilities_SubmessageInMessageCapability_strategy = st.builds(
    oaam_capabilities_SubmessageInMessageCapability,
)
oaam_restrictions_DeviceTypeRestriction_strategy = st.builds(
    oaam_restrictions_DeviceTypeRestriction,
    isForbidden=
        st.booleans(),
    deviceTypeName=
        safe_text
)
oaam_functions_ExternalOutputLink_strategy = st.builds(
    oaam_functions_ExternalOutputLink,
    filter=
        safe_text
)
oaam_anatomy_Position3D_strategy = st.builds(
    oaam_anatomy_Position3D,
    z=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_library_ConnectionType_strategy = st.builds(
    oaam_library_ConnectionType,
    nEndPoints=
        st.integers(),
    nJoints=
        st.integers(),
    isPower=
        st.booleans(),
    maxInterfaceToJointDistance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    requiresMaster=
        st.booleans(),
    maxJointBranches=
        st.integers(),
    maxLength=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    isInformation=
        st.booleans(),
    nStartingPoints=
        st.integers(),
    isSwitched=
        st.booleans(),
    isWireless=
        st.booleans(),
    allowsCircles=
        st.booleans(),
    isUnidirectional=
        st.booleans(),
    directConnectionsAllowed=
        st.booleans()
)
oaam_allocations_MessageA_strategy = st.builds(
    oaam_allocations_MessageA,
    length=
        st.integers(),
    isPersistent=
        st.booleans()
)
oaam_functions_TaskRedundancy_strategy = st.builds(
    oaam_functions_TaskRedundancy,
)
oaam_library_BusType_strategy = st.builds(
    oaam_library_BusType,
    isSelfManaging=
        st.booleans(),
    requiresMaster=
        st.booleans(),
    mtbf=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_capabilities_ConnectionInDuctOrLocationCapability_strategy = st.builds(
    oaam_capabilities_ConnectionInDuctOrLocationCapability,
)
oaam_scenario_ScenarioParameterBool_strategy = st.builds(
    oaam_scenario_ScenarioParameterBool,
    value=
        st.booleans()
)
oaam_functions_Output_strategy = st.builds(
    oaam_functions_Output,
    fixedRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_allocations_SignalAssignmentSegment_strategy = st.builds(
    oaam_allocations_SignalAssignmentSegment,
)
oaam_allocations_ConnectionAssignmentSegment_strategy = st.builds(
    oaam_allocations_ConnectionAssignmentSegment,
)
oaam_restrictions_TimeDelayRestriction_strategy = st.builds(
    oaam_restrictions_TimeDelayRestriction,
    delay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_allocations_SubdeviceAssignment_strategy = st.builds(
    oaam_allocations_SubdeviceAssignment,
)
oaam_functions_TaskSymmetry_strategy = st.builds(
    oaam_functions_TaskSymmetry,
)
oaam_library_DuctType_strategy = st.builds(
    oaam_library_DuctType,
)
oaam_library_SignalType_strategy = st.builds(
    oaam_library_SignalType,
)
oaam_restrictions_TaskSymmetryRestriction_strategy = st.builds(
    oaam_restrictions_TaskSymmetryRestriction,
    type=
        safe_text
)
oaam_library_ResourceBundle_strategy = st.builds(
    oaam_library_ResourceBundle,
    cost=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    mtbf=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    mass=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_restrictions_PowerSourceRestriction_strategy = st.builds(
    oaam_restrictions_PowerSourceRestriction,
    isForbidden=
        st.booleans(),
    powerSourceName=
        safe_text
)
oaam_functions_SignalGroup_strategy = st.builds(
    oaam_functions_SignalGroup,
)
oaam_systems_InformationFlow_strategy = st.builds(
    oaam_systems_InformationFlow,
)
oaam_allocations_TaskAssignment_strategy = st.builds(
    oaam_allocations_TaskAssignment,
)
oaam_anatomy_Duct_strategy = st.builds(
    oaam_anatomy_Duct,
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_restrictions_SegregationRestriction_strategy = st.builds(
    oaam_restrictions_SegregationRestriction,
    dissimilarLocation=
        st.booleans(),
    dissimilarPowerSource=
        st.booleans(),
    dissimilarArea=
        st.booleans(),
    dissimilarTechnology=
        st.booleans()
)
oaam_anatomy_LocationSymmetry_strategy = st.builds(
    oaam_anatomy_LocationSymmetry,
)
oaam_restrictions_AreaRestriction_strategy = st.builds(
    oaam_restrictions_AreaRestriction,
    areaName=
        safe_text,
    isForbidden=
        st.booleans()
)
oaam_capabilities_MessageOnConnectionOrDeviceCapability_strategy = st.builds(
    oaam_capabilities_MessageOnConnectionOrDeviceCapability,
    worstCaseTransmissionTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_library_ResourceType_strategy = st.builds(
    oaam_library_ResourceType,
    isConfigurable=
        st.booleans(),
    isIo=
        st.booleans(),
    isDistinguishable=
        st.booleans(),
    isPropagated=
        st.booleans(),
    unit=
        safe_text,
    direction=
        safe_text,
    isConsumed=
        st.booleans()
)
oaam_functions_FailureCondition_strategy = st.builds(
    oaam_functions_FailureCondition,
    noSingleFailure=
        st.booleans(),
    maxOccurrenceProbability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_capabilities_SignalInMessageCapability_strategy = st.builds(
    oaam_capabilities_SignalInMessageCapability,
)
common_BoolA_strategy = st.builds(
    common_BoolA,
)
oaam_library_TaskInputState_strategy = st.builds(
    oaam_library_TaskInputState,
    state=
        safe_text
)
oaam_functions_OutputIntegrityState_strategy = st.builds(
    oaam_functions_OutputIntegrityState,
    state=
        safe_text
)
oaam_library_TaskInputTrigger_strategy = st.builds(
    oaam_library_TaskInputTrigger,
)
oaam_common_BoolNot_strategy = st.builds(
    oaam_common_BoolNot,
)
oaam_common_BoolOperation_strategy = st.builds(
    oaam_common_BoolOperation,
    type=
        safe_text
)
oaam_common_BoolA_strategy = st.builds(
    oaam_common_BoolA,
)
AttributeA_strategy = st.builds(
    AttributeA,
)
oaam_common_AttributeNumeric_strategy = st.builds(
    oaam_common_AttributeNumeric,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_common_AttributeString_strategy = st.builds(
    oaam_common_AttributeString,
    value=
        safe_text
)
oaam_common_AttributeReference_strategy = st.builds(
    oaam_common_AttributeReference,
)
oaam_common_AttributeContainment_strategy = st.builds(
    oaam_common_AttributeContainment,
)
Allocations_strategy = st.builds(
    Allocations,
)
Restrictions_strategy = st.builds(
    Restrictions,
)
Capabilities_strategy = st.builds(
    Capabilities,
)
Anatomy_strategy = st.builds(
    Anatomy,
)
Hardware_strategy = st.builds(
    Hardware,
)
Functions_strategy = st.builds(
    Functions,
)
oaam_common_OaamBaseElementA_strategy = st.builds(
    oaam_common_OaamBaseElementA,
    id=
        safe_text,
    traceLink=
        safe_text,
    modified=
        st.dates(),
    documentation=
        safe_text,
    modifier=
        safe_text,
    style=
        safe_text,
    name=
        safe_text
)
Library_strategy = st.builds(
    Library,
)
OaamBaseElementA_strategy = st.builds(
    OaamBaseElementA,
)
oaam_library_PowerSource_strategy = st.builds(
    oaam_library_PowerSource,
)
oaam_library_DeviceTypeDissimilarity_strategy = st.builds(
    oaam_library_DeviceTypeDissimilarity,
    percentageOfCommonHardware=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_library_Resource_strategy = st.builds(
    oaam_library_Resource,
    count=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_library_ResourceTypeModifier_strategy = st.builds(
    oaam_library_ResourceTypeModifier,
)
oaam_library_IoGroup_strategy = st.builds(
    oaam_library_IoGroup,
)
oaam_systems_SystemsContainerA_strategy = st.builds(
    oaam_systems_SystemsContainerA,
)
oaam_hardware_HardwareContainerA_strategy = st.builds(
    oaam_hardware_HardwareContainerA,
)
oaam_scenario_ScenarioContainerA_strategy = st.builds(
    oaam_scenario_ScenarioContainerA,
)
oaam_scenario_OperationModeReference_strategy = st.builds(
    oaam_scenario_OperationModeReference,
    activeProbability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_systems_InputSegregation_strategy = st.builds(
    oaam_systems_InputSegregation,
    dissimilarSource=
        st.booleans(),
    dissimilarTechnology=
        st.booleans(),
    dissimilarRoute=
        st.booleans()
)
oaam_restrictions_RestrictionsContainerA_strategy = st.builds(
    oaam_restrictions_RestrictionsContainerA,
)
oaam_library_ResourceAlternatives_strategy = st.builds(
    oaam_library_ResourceAlternatives,
)
oaam_library_DuctOpeningDeclaration_strategy = st.builds(
    oaam_library_DuctOpeningDeclaration,
)
oaam_common_DataTypeA_strategy = st.builds(
    oaam_common_DataTypeA,
)
oaam_library_TaskOutputTrigger_strategy = st.builds(
    oaam_library_TaskOutputTrigger,
    isFixedRate=
        st.booleans(),
    fixedRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_library_ResourceTypeDissimilarity_strategy = st.builds(
    oaam_library_ResourceTypeDissimilarity,
)
oaam_library_ResourceTypeModifierReference_strategy = st.builds(
    oaam_library_ResourceTypeModifierReference,
)
oaam_capabilities_CapabilitiesContainerA_strategy = st.builds(
    oaam_capabilities_CapabilitiesContainerA,
)
oaam_library_ResourceLink_strategy = st.builds(
    oaam_library_ResourceLink,
)
oaam_library_DeviceTypeSymmetry_strategy = st.builds(
    oaam_library_DeviceTypeSymmetry,
)
oaam_library_WireType_strategy = st.builds(
    oaam_library_WireType,
    nConductors=
        st.integers(),
    mtbf=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    specificPrice=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    specificWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    nShields=
        st.integers(),
    minBendingRadius=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_library_LibraryContainerA_strategy = st.builds(
    oaam_library_LibraryContainerA,
)
oaam_library_TaskTypeDissimilarity_strategy = st.builds(
    oaam_library_TaskTypeDissimilarity,
    percentageOfCommonCode=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_library_InputDeclaration_strategy = st.builds(
    oaam_library_InputDeclaration,
    unit=
        safe_text,
    range=
        safe_text,
    upperBound=
        st.integers(),
    lowerBound=
        st.integers(),
    precondition=
        safe_text
)
oaam_library_FaultPropagation_strategy = st.builds(
    oaam_library_FaultPropagation,
    outputState=
        safe_text
)
oaam_common_AttributeA_strategy = st.builds(
    oaam_common_AttributeA,
)
oaam_allocations_AllocationsContainerA_strategy = st.builds(
    oaam_allocations_AllocationsContainerA,
)
oaam_anatomy_AnatomyContainerA_strategy = st.builds(
    oaam_anatomy_AnatomyContainerA,
)
oaam_functions_TaskParameter_strategy = st.builds(
    oaam_functions_TaskParameter,
    value=
        safe_text
)
oaam_library_AttributeDefinition_strategy = st.builds(
    oaam_library_AttributeDefinition,
    target=
        safe_text,
    dataType=
        safe_text
)
oaam_library_IoDeclaration_strategy = st.builds(
    oaam_library_IoDeclaration,
)
oaam_library_TaskParameterDeclaration_strategy = st.builds(
    oaam_library_TaskParameterDeclaration,
)
oaam_capabilities_ResourceConsumption_strategy = st.builds(
    oaam_capabilities_ResourceConsumption,
    count=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam_library_ResourceGroup_strategy = st.builds(
    oaam_library_ResourceGroup,
)
oaam_library_OutputDeclaration_strategy = st.builds(
    oaam_library_OutputDeclaration,
    lowerBound=
        st.integers(),
    unit=
        safe_text,
    range=
        safe_text,
    postcondition=
        safe_text,
    upperBound=
        st.integers()
)
oaam_library_TaskStateDeclaration_strategy = st.builds(
    oaam_library_TaskStateDeclaration,
)
oaam_library_IoType_strategy = st.builds(
    oaam_library_IoType,
    direction=
        safe_text
)
oaam_Architecture_strategy = st.builds(
    oaam_Architecture,
)
Systems_strategy = st.builds(
    Systems,
)
Scenario_strategy = st.builds(
    Scenario,
)

@given(instance=oaam_allocations_SignalToMessageAssignment_strategy)
@settings(max_examples=50)
def test_oaam_allocations_signaltomessageassignment_instantiation(instance):
    assert isinstance(instance, oaam_allocations_SignalToMessageAssignment)



@given(instance=oaam_allocations_SignalToMessageAssignment_strategy)
def test_oaam_allocations_signaltomessageassignment_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=allocations_AllocationsContainerA_strategy)
@settings(max_examples=50)
def test_allocations_allocationscontainera_instantiation(instance):
    assert isinstance(instance, allocations_AllocationsContainerA)

@given(instance=AllocationsContainerA_strategy)
@settings(max_examples=50)
def test_allocationscontainera_instantiation(instance):
    assert isinstance(instance, AllocationsContainerA)

@given(instance=oaam_allocations_Allocations_strategy)
@settings(max_examples=50)
def test_oaam_allocations_allocations_instantiation(instance):
    assert isinstance(instance, oaam_allocations_Allocations)

@given(instance=MessageSegment_strategy)
@settings(max_examples=50)
def test_messagesegment_instantiation(instance):
    assert isinstance(instance, MessageSegment)

@given(instance=SignalToMessageAssignment_strategy)
@settings(max_examples=50)
def test_signaltomessageassignment_instantiation(instance):
    assert isinstance(instance, SignalToMessageAssignment)

@given(instance=Submessage_strategy)
@settings(max_examples=50)
def test_submessage_instantiation(instance):
    assert isinstance(instance, Submessage)

@given(instance=MessageA_strategy)
@settings(max_examples=50)
def test_messagea_instantiation(instance):
    assert isinstance(instance, MessageA)

@given(instance=oaam_allocations_Submessage_strategy)
@settings(max_examples=50)
def test_oaam_allocations_submessage_instantiation(instance):
    assert isinstance(instance, oaam_allocations_Submessage)



@given(instance=oaam_allocations_Submessage_strategy)
def test_oaam_allocations_submessage_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=oaam_allocations_Message_strategy)
@settings(max_examples=50)
def test_oaam_allocations_message_instantiation(instance):
    assert isinstance(instance, oaam_allocations_Message)

@given(instance=ScheduledTime_strategy)
@settings(max_examples=50)
def test_scheduledtime_instantiation(instance):
    assert isinstance(instance, ScheduledTime)

@given(instance=ConnectionAssignmentSegment_strategy)
@settings(max_examples=50)
def test_connectionassignmentsegment_instantiation(instance):
    assert isinstance(instance, ConnectionAssignmentSegment)

@given(instance=Area_strategy)
@settings(max_examples=50)
def test_area_instantiation(instance):
    assert isinstance(instance, Area)

@given(instance=Duct_strategy)
@settings(max_examples=50)
def test_duct_instantiation(instance):
    assert isinstance(instance, Duct)

@given(instance=LocationSymmetry_strategy)
@settings(max_examples=50)
def test_locationsymmetry_instantiation(instance):
    assert isinstance(instance, LocationSymmetry)

@given(instance=Position3D_strategy)
@settings(max_examples=50)
def test_position3d_instantiation(instance):
    assert isinstance(instance, Position3D)

@given(instance=AreaSymmetry_strategy)
@settings(max_examples=50)
def test_areasymmetry_instantiation(instance):
    assert isinstance(instance, AreaSymmetry)

@given(instance=Subanatomy_strategy)
@settings(max_examples=50)
def test_subanatomy_instantiation(instance):
    assert isinstance(instance, Subanatomy)

@given(instance=hardware_HardwareContainerA_strategy)
@settings(max_examples=50)
def test_hardware_hardwarecontainera_instantiation(instance):
    assert isinstance(instance, hardware_HardwareContainerA)

@given(instance=library_ResourceProviderInstanceA_strategy)
@settings(max_examples=50)
def test_library_resourceproviderinstancea_instantiation(instance):
    assert isinstance(instance, library_ResourceProviderInstanceA)

@given(instance=Bus_strategy)
@settings(max_examples=50)
def test_bus_instantiation(instance):
    assert isinstance(instance, Bus)

@given(instance=Subhardware_strategy)
@settings(max_examples=50)
def test_subhardware_instantiation(instance):
    assert isinstance(instance, Subhardware)

@given(instance=DeviceSymmetry_strategy)
@settings(max_examples=50)
def test_devicesymmetry_instantiation(instance):
    assert isinstance(instance, DeviceSymmetry)

@given(instance=Location_strategy)
@settings(max_examples=50)
def test_location_instantiation(instance):
    assert isinstance(instance, Location)

@given(instance=Connection_strategy)
@settings(max_examples=50)
def test_connection_instantiation(instance):
    assert isinstance(instance, Connection)

@given(instance=ExternalOutputLink_strategy)
@settings(max_examples=50)
def test_externaloutputlink_instantiation(instance):
    assert isinstance(instance, ExternalOutputLink)

@given(instance=Io_strategy)
@settings(max_examples=50)
def test_io_instantiation(instance):
    assert isinstance(instance, Io)

@given(instance=OutputIntegrityState_strategy)
@settings(max_examples=50)
def test_outputintegritystate_instantiation(instance):
    assert isinstance(instance, OutputIntegrityState)

@given(instance=Output_strategy)
@settings(max_examples=50)
def test_output_instantiation(instance):
    assert isinstance(instance, Output)

@given(instance=Input_strategy)
@settings(max_examples=50)
def test_input_instantiation(instance):
    assert isinstance(instance, Input)

@given(instance=Subfunctions_strategy)
@settings(max_examples=50)
def test_subfunctions_instantiation(instance):
    assert isinstance(instance, Subfunctions)

@given(instance=FailureCondition_strategy)
@settings(max_examples=50)
def test_failurecondition_instantiation(instance):
    assert isinstance(instance, FailureCondition)

@given(instance=TaskParameter_strategy)
@settings(max_examples=50)
def test_taskparameter_instantiation(instance):
    assert isinstance(instance, TaskParameter)

@given(instance=Device_strategy)
@settings(max_examples=50)
def test_device_instantiation(instance):
    assert isinstance(instance, Device)

@given(instance=ExternalTaskLink_strategy)
@settings(max_examples=50)
def test_externaltasklink_instantiation(instance):
    assert isinstance(instance, ExternalTaskLink)

@given(instance=Task_strategy)
@settings(max_examples=50)
def test_task_instantiation(instance):
    assert isinstance(instance, Task)

@given(instance=FunctionsContainerA_strategy)
@settings(max_examples=50)
def test_functionscontainera_instantiation(instance):
    assert isinstance(instance, FunctionsContainerA)

@given(instance=oaam_functions_Subfunctions_strategy)
@settings(max_examples=50)
def test_oaam_functions_subfunctions_instantiation(instance):
    assert isinstance(instance, oaam_functions_Subfunctions)



@given(instance=oaam_functions_Subfunctions_strategy)
def test_oaam_functions_subfunctions_multiplicityMax_setter(instance):
    original = instance.multiplicityMax
    instance.multiplicityMax = original
    assert instance.multiplicityMax == original



@given(instance=oaam_functions_Subfunctions_strategy)
def test_oaam_functions_subfunctions_multiplicityMin_setter(instance):
    original = instance.multiplicityMin
    instance.multiplicityMin = original
    assert instance.multiplicityMin == original

@given(instance=oaam_functions_Functions_strategy)
@settings(max_examples=50)
def test_oaam_functions_functions_instantiation(instance):
    assert isinstance(instance, oaam_functions_Functions)

@given(instance=SignalGroup_strategy)
@settings(max_examples=50)
def test_signalgroup_instantiation(instance):
    assert isinstance(instance, SignalGroup)

@given(instance=Signal_strategy)
@settings(max_examples=50)
def test_signal_instantiation(instance):
    assert isinstance(instance, Signal)

@given(instance=TaskRedundancy_strategy)
@settings(max_examples=50)
def test_taskredundancy_instantiation(instance):
    assert isinstance(instance, TaskRedundancy)

@given(instance=TaskSymmetry_strategy)
@settings(max_examples=50)
def test_tasksymmetry_instantiation(instance):
    assert isinstance(instance, TaskSymmetry)

@given(instance=TaskGroup_strategy)
@settings(max_examples=50)
def test_taskgroup_instantiation(instance):
    assert isinstance(instance, TaskGroup)

@given(instance=InformationPower_strategy)
@settings(max_examples=50)
def test_informationpower_instantiation(instance):
    assert isinstance(instance, InformationPower)

@given(instance=oaam_systems_HydraulicPower_strategy)
@settings(max_examples=50)
def test_oaam_systems_hydraulicpower_instantiation(instance):
    assert isinstance(instance, oaam_systems_HydraulicPower)



@given(instance=oaam_systems_HydraulicPower_strategy)
def test_oaam_systems_hydraulicpower_massFlowRate_setter(instance):
    original = instance.massFlowRate
    instance.massFlowRate = original
    assert instance.massFlowRate == original



@given(instance=oaam_systems_HydraulicPower_strategy)
def test_oaam_systems_hydraulicpower_pressure_setter(instance):
    original = instance.pressure
    instance.pressure = original
    assert instance.pressure == original

@given(instance=oaam_systems_RotaryPower_strategy)
@settings(max_examples=50)
def test_oaam_systems_rotarypower_instantiation(instance):
    assert isinstance(instance, oaam_systems_RotaryPower)



@given(instance=oaam_systems_RotaryPower_strategy)
def test_oaam_systems_rotarypower_momentum_setter(instance):
    original = instance.momentum
    instance.momentum = original
    assert instance.momentum == original



@given(instance=oaam_systems_RotaryPower_strategy)
def test_oaam_systems_rotarypower_angularVelocity_setter(instance):
    original = instance.angularVelocity
    instance.angularVelocity = original
    assert instance.angularVelocity == original

@given(instance=oaam_systems_ElectricPower_strategy)
@settings(max_examples=50)
def test_oaam_systems_electricpower_instantiation(instance):
    assert isinstance(instance, oaam_systems_ElectricPower)



@given(instance=oaam_systems_ElectricPower_strategy)
def test_oaam_systems_electricpower_voltage_setter(instance):
    original = instance.voltage
    instance.voltage = original
    assert instance.voltage == original



@given(instance=oaam_systems_ElectricPower_strategy)
def test_oaam_systems_electricpower_nPhases_setter(instance):
    original = instance.nPhases
    instance.nPhases = original
    assert instance.nPhases == original



@given(instance=oaam_systems_ElectricPower_strategy)
def test_oaam_systems_electricpower_frequency_setter(instance):
    original = instance.frequency
    instance.frequency = original
    assert instance.frequency == original



@given(instance=oaam_systems_ElectricPower_strategy)
def test_oaam_systems_electricpower_current_setter(instance):
    original = instance.current
    instance.current = original
    assert instance.current == original

@given(instance=oaam_systems_LinearPower_strategy)
@settings(max_examples=50)
def test_oaam_systems_linearpower_instantiation(instance):
    assert isinstance(instance, oaam_systems_LinearPower)



@given(instance=oaam_systems_LinearPower_strategy)
def test_oaam_systems_linearpower_velocity_setter(instance):
    original = instance.velocity
    instance.velocity = original
    assert instance.velocity == original



@given(instance=oaam_systems_LinearPower_strategy)
def test_oaam_systems_linearpower_force_setter(instance):
    original = instance.force
    instance.force = original
    assert instance.force == original

@given(instance=systems_RequiredInformationA_strategy)
@settings(max_examples=50)
def test_systems_requiredinformationa_instantiation(instance):
    assert isinstance(instance, systems_RequiredInformationA)

@given(instance=systems_ProvidedInformationA_strategy)
@settings(max_examples=50)
def test_systems_providedinformationa_instantiation(instance):
    assert isinstance(instance, systems_ProvidedInformationA)

@given(instance=oaam_systems_ProvidedInformationA_strategy)
@settings(max_examples=50)
def test_oaam_systems_providedinformationa_instantiation(instance):
    assert isinstance(instance, oaam_systems_ProvidedInformationA)

@given(instance=oaam_systems_RequiredInformationA_strategy)
@settings(max_examples=50)
def test_oaam_systems_requiredinformationa_instantiation(instance):
    assert isinstance(instance, oaam_systems_RequiredInformationA)

@given(instance=RequiredInformationA_strategy)
@settings(max_examples=50)
def test_requiredinformationa_instantiation(instance):
    assert isinstance(instance, RequiredInformationA)

@given(instance=Subsystem_strategy)
@settings(max_examples=50)
def test_subsystem_instantiation(instance):
    assert isinstance(instance, Subsystem)

@given(instance=InputSegregation_strategy)
@settings(max_examples=50)
def test_inputsegregation_instantiation(instance):
    assert isinstance(instance, InputSegregation)

@given(instance=InformationFlow_strategy)
@settings(max_examples=50)
def test_informationflow_instantiation(instance):
    assert isinstance(instance, InformationFlow)

@given(instance=System_strategy)
@settings(max_examples=50)
def test_system_instantiation(instance):
    assert isinstance(instance, System)

@given(instance=ScenarioContainerA_strategy)
@settings(max_examples=50)
def test_scenariocontainera_instantiation(instance):
    assert isinstance(instance, ScenarioContainerA)

@given(instance=oaam_scenario_Subscenario_strategy)
@settings(max_examples=50)
def test_oaam_scenario_subscenario_instantiation(instance):
    assert isinstance(instance, oaam_scenario_Subscenario)

@given(instance=oaam_scenario_Scenario_strategy)
@settings(max_examples=50)
def test_oaam_scenario_scenario_instantiation(instance):
    assert isinstance(instance, oaam_scenario_Scenario)

@given(instance=ProvidedInformationA_strategy)
@settings(max_examples=50)
def test_providedinformationa_instantiation(instance):
    assert isinstance(instance, ProvidedInformationA)

@given(instance=systems_SystemsContainerA_strategy)
@settings(max_examples=50)
def test_systems_systemscontainera_instantiation(instance):
    assert isinstance(instance, systems_SystemsContainerA)

@given(instance=SystemsContainerA_strategy)
@settings(max_examples=50)
def test_systemscontainera_instantiation(instance):
    assert isinstance(instance, SystemsContainerA)

@given(instance=oaam_systems_Systems_strategy)
@settings(max_examples=50)
def test_oaam_systems_systems_instantiation(instance):
    assert isinstance(instance, oaam_systems_Systems)

@given(instance=scenario_ScenarioParameterA_strategy)
@settings(max_examples=50)
def test_scenario_scenarioparametera_instantiation(instance):
    assert isinstance(instance, scenario_ScenarioParameterA)

@given(instance=Subscenario_strategy)
@settings(max_examples=50)
def test_subscenario_instantiation(instance):
    assert isinstance(instance, Subscenario)

@given(instance=OperationMode_strategy)
@settings(max_examples=50)
def test_operationmode_instantiation(instance):
    assert isinstance(instance, OperationMode)

@given(instance=scenario_VariantDependentElementA_strategy)
@settings(max_examples=50)
def test_scenario_variantdependentelementa_instantiation(instance):
    assert isinstance(instance, scenario_VariantDependentElementA)

@given(instance=scenario_ModeDependentElementA_strategy)
@settings(max_examples=50)
def test_scenario_modedependentelementa_instantiation(instance):
    assert isinstance(instance, scenario_ModeDependentElementA)

@given(instance=oaam_systems_Subsystem_strategy)
@settings(max_examples=50)
def test_oaam_systems_subsystem_instantiation(instance):
    assert isinstance(instance, oaam_systems_Subsystem)

@given(instance=oaam_hardware_Subhardware_strategy)
@settings(max_examples=50)
def test_oaam_hardware_subhardware_instantiation(instance):
    assert isinstance(instance, oaam_hardware_Subhardware)

@given(instance=oaam_hardware_Hardware_strategy)
@settings(max_examples=50)
def test_oaam_hardware_hardware_instantiation(instance):
    assert isinstance(instance, oaam_hardware_Hardware)

@given(instance=oaam_allocations_Suballocations_strategy)
@settings(max_examples=50)
def test_oaam_allocations_suballocations_instantiation(instance):
    assert isinstance(instance, oaam_allocations_Suballocations)

@given(instance=oaam_scenario_ScenarioParameterA_strategy)
@settings(max_examples=50)
def test_oaam_scenario_scenarioparametera_instantiation(instance):
    assert isinstance(instance, oaam_scenario_ScenarioParameterA)

@given(instance=LibraryContainerA_strategy)
@settings(max_examples=50)
def test_librarycontainera_instantiation(instance):
    assert isinstance(instance, LibraryContainerA)

@given(instance=oaam_library_Sublibrary_strategy)
@settings(max_examples=50)
def test_oaam_library_sublibrary_instantiation(instance):
    assert isinstance(instance, oaam_library_Sublibrary)

@given(instance=oaam_library_Library_strategy)
@settings(max_examples=50)
def test_oaam_library_library_instantiation(instance):
    assert isinstance(instance, oaam_library_Library)

@given(instance=ScenarioParameterA_strategy)
@settings(max_examples=50)
def test_scenarioparametera_instantiation(instance):
    assert isinstance(instance, ScenarioParameterA)

@given(instance=Variant_strategy)
@settings(max_examples=50)
def test_variant_instantiation(instance):
    assert isinstance(instance, Variant)

@given(instance=oaam_scenario_VariantDependentElementA_strategy)
@settings(max_examples=50)
def test_oaam_scenario_variantdependentelementa_instantiation(instance):
    assert isinstance(instance, oaam_scenario_VariantDependentElementA)

@given(instance=OperationModeReference_strategy)
@settings(max_examples=50)
def test_operationmodereference_instantiation(instance):
    assert isinstance(instance, OperationModeReference)

@given(instance=oaam_scenario_ModeDependentElementA_strategy)
@settings(max_examples=50)
def test_oaam_scenario_modedependentelementa_instantiation(instance):
    assert isinstance(instance, oaam_scenario_ModeDependentElementA)

@given(instance=TaskInputTrigger_strategy)
@settings(max_examples=50)
def test_taskinputtrigger_instantiation(instance):
    assert isinstance(instance, TaskInputTrigger)

@given(instance=TaskInputState_strategy)
@settings(max_examples=50)
def test_taskinputstate_instantiation(instance):
    assert isinstance(instance, TaskInputState)

@given(instance=BoolNot_strategy)
@settings(max_examples=50)
def test_boolnot_instantiation(instance):
    assert isinstance(instance, BoolNot)

@given(instance=BoolOperation_strategy)
@settings(max_examples=50)
def test_booloperation_instantiation(instance):
    assert isinstance(instance, BoolOperation)

@given(instance=FaultPropagation_strategy)
@settings(max_examples=50)
def test_faultpropagation_instantiation(instance):
    assert isinstance(instance, FaultPropagation)

@given(instance=TaskOutputTrigger_strategy)
@settings(max_examples=50)
def test_taskoutputtrigger_instantiation(instance):
    assert isinstance(instance, TaskOutputTrigger)

@given(instance=DuctOpeningDeclaration_strategy)
@settings(max_examples=50)
def test_ductopeningdeclaration_instantiation(instance):
    assert isinstance(instance, DuctOpeningDeclaration)

@given(instance=IoGroup_strategy)
@settings(max_examples=50)
def test_iogroup_instantiation(instance):
    assert isinstance(instance, IoGroup)

@given(instance=TaskParameterDeclaration_strategy)
@settings(max_examples=50)
def test_taskparameterdeclaration_instantiation(instance):
    assert isinstance(instance, TaskParameterDeclaration)

@given(instance=TaskStateDeclaration_strategy)
@settings(max_examples=50)
def test_taskstatedeclaration_instantiation(instance):
    assert isinstance(instance, TaskStateDeclaration)

@given(instance=InputDeclaration_strategy)
@settings(max_examples=50)
def test_inputdeclaration_instantiation(instance):
    assert isinstance(instance, InputDeclaration)

@given(instance=OutputDeclaration_strategy)
@settings(max_examples=50)
def test_outputdeclaration_instantiation(instance):
    assert isinstance(instance, OutputDeclaration)

@given(instance=IoDeclaration_strategy)
@settings(max_examples=50)
def test_iodeclaration_instantiation(instance):
    assert isinstance(instance, IoDeclaration)

@given(instance=library_ResourceProviderA_strategy)
@settings(max_examples=50)
def test_library_resourceprovidera_instantiation(instance):
    assert isinstance(instance, library_ResourceProviderA)

@given(instance=ResourceAlternatives_strategy)
@settings(max_examples=50)
def test_resourcealternatives_instantiation(instance):
    assert isinstance(instance, ResourceAlternatives)

@given(instance=ResourceTypeModifierReference_strategy)
@settings(max_examples=50)
def test_resourcetypemodifierreference_instantiation(instance):
    assert isinstance(instance, ResourceTypeModifierReference)

@given(instance=library_ResourceConsumerA_strategy)
@settings(max_examples=50)
def test_library_resourceconsumera_instantiation(instance):
    assert isinstance(instance, library_ResourceConsumerA)

@given(instance=MessageType_strategy)
@settings(max_examples=50)
def test_messagetype_instantiation(instance):
    assert isinstance(instance, MessageType)

@given(instance=BusType_strategy)
@settings(max_examples=50)
def test_bustype_instantiation(instance):
    assert isinstance(instance, BusType)

@given(instance=IoType_strategy)
@settings(max_examples=50)
def test_iotype_instantiation(instance):
    assert isinstance(instance, IoType)

@given(instance=LocationType_strategy)
@settings(max_examples=50)
def test_locationtype_instantiation(instance):
    assert isinstance(instance, LocationType)

@given(instance=WireType_strategy)
@settings(max_examples=50)
def test_wiretype_instantiation(instance):
    assert isinstance(instance, WireType)

@given(instance=ConnectionType_strategy)
@settings(max_examples=50)
def test_connectiontype_instantiation(instance):
    assert isinstance(instance, ConnectionType)

@given(instance=DeviceTypeDissimilarity_strategy)
@settings(max_examples=50)
def test_devicetypedissimilarity_instantiation(instance):
    assert isinstance(instance, DeviceTypeDissimilarity)

@given(instance=Sublibrary_strategy)
@settings(max_examples=50)
def test_sublibrary_instantiation(instance):
    assert isinstance(instance, Sublibrary)

@given(instance=Message_strategy)
@settings(max_examples=50)
def test_message_instantiation(instance):
    assert isinstance(instance, Message)

@given(instance=SubconnectionAssignment_strategy)
@settings(max_examples=50)
def test_subconnectionassignment_instantiation(instance):
    assert isinstance(instance, SubconnectionAssignment)

@given(instance=SignalAssignmentSegment_strategy)
@settings(max_examples=50)
def test_signalassignmentsegment_instantiation(instance):
    assert isinstance(instance, SignalAssignmentSegment)

@given(instance=Schedule_strategy)
@settings(max_examples=50)
def test_schedule_instantiation(instance):
    assert isinstance(instance, Schedule)

@given(instance=SubdeviceAssignment_strategy)
@settings(max_examples=50)
def test_subdeviceassignment_instantiation(instance):
    assert isinstance(instance, SubdeviceAssignment)

@given(instance=DeviceAssignment_strategy)
@settings(max_examples=50)
def test_deviceassignment_instantiation(instance):
    assert isinstance(instance, DeviceAssignment)

@given(instance=Suballocations_strategy)
@settings(max_examples=50)
def test_suballocations_instantiation(instance):
    assert isinstance(instance, Suballocations)

@given(instance=SignalAssignment_strategy)
@settings(max_examples=50)
def test_signalassignment_instantiation(instance):
    assert isinstance(instance, SignalAssignment)

@given(instance=TaskAssignment_strategy)
@settings(max_examples=50)
def test_taskassignment_instantiation(instance):
    assert isinstance(instance, TaskAssignment)

@given(instance=ConnectionAssignment_strategy)
@settings(max_examples=50)
def test_connectionassignment_instantiation(instance):
    assert isinstance(instance, ConnectionAssignment)

@given(instance=restrictions_RestrictionsContainerA_strategy)
@settings(max_examples=50)
def test_restrictions_restrictionscontainera_instantiation(instance):
    assert isinstance(instance, restrictions_RestrictionsContainerA)

@given(instance=oaam_restrictions_Subrestrictions_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_subrestrictions_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_Subrestrictions)

@given(instance=restrictions_ConnectionRestrinctionA_strategy)
@settings(max_examples=50)
def test_restrictions_connectionrestrinctiona_instantiation(instance):
    assert isinstance(instance, restrictions_ConnectionRestrinctionA)

@given(instance=restrictions_DeviceRestrictionA_strategy)
@settings(max_examples=50)
def test_restrictions_devicerestrictiona_instantiation(instance):
    assert isinstance(instance, restrictions_DeviceRestrictionA)

@given(instance=restrictions_SubfunctionRestrictionA_strategy)
@settings(max_examples=50)
def test_restrictions_subfunctionrestrictiona_instantiation(instance):
    assert isinstance(instance, restrictions_SubfunctionRestrictionA)

@given(instance=restrictions_SignalGroupRestrictionA_strategy)
@settings(max_examples=50)
def test_restrictions_signalgrouprestrictiona_instantiation(instance):
    assert isinstance(instance, restrictions_SignalGroupRestrictionA)

@given(instance=restrictions_SignalRestrictionA_strategy)
@settings(max_examples=50)
def test_restrictions_signalrestrictiona_instantiation(instance):
    assert isinstance(instance, restrictions_SignalRestrictionA)

@given(instance=restrictions_TaskGroupRestrictionA_strategy)
@settings(max_examples=50)
def test_restrictions_taskgrouprestrictiona_instantiation(instance):
    assert isinstance(instance, restrictions_TaskGroupRestrictionA)

@given(instance=restrictions_TaskRestrictionA_strategy)
@settings(max_examples=50)
def test_restrictions_taskrestrictiona_instantiation(instance):
    assert isinstance(instance, restrictions_TaskRestrictionA)

@given(instance=oaam_restrictions_SignalGroupRestrictionA_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_signalgrouprestrictiona_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_SignalGroupRestrictionA)

@given(instance=oaam_restrictions_TaskGroupRestrictionA_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_taskgrouprestrictiona_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_TaskGroupRestrictionA)

@given(instance=oaam_restrictions_SubfunctionRestrictionA_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_subfunctionrestrictiona_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_SubfunctionRestrictionA)

@given(instance=oaam_restrictions_DeviceRestrictionA_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_devicerestrictiona_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_DeviceRestrictionA)

@given(instance=RestrictionsContainerA_strategy)
@settings(max_examples=50)
def test_restrictionscontainera_instantiation(instance):
    assert isinstance(instance, RestrictionsContainerA)

@given(instance=oaam_restrictions_Restrictions_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_restrictions_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_Restrictions)

@given(instance=TimeDelayRestriction_strategy)
@settings(max_examples=50)
def test_timedelayrestriction_instantiation(instance):
    assert isinstance(instance, TimeDelayRestriction)

@given(instance=Subrestrictions_strategy)
@settings(max_examples=50)
def test_subrestrictions_instantiation(instance):
    assert isinstance(instance, Subrestrictions)

@given(instance=SegregationRestriction_strategy)
@settings(max_examples=50)
def test_segregationrestriction_instantiation(instance):
    assert isinstance(instance, SegregationRestriction)

@given(instance=ConnectionTypeRestriction_strategy)
@settings(max_examples=50)
def test_connectiontyperestriction_instantiation(instance):
    assert isinstance(instance, ConnectionTypeRestriction)

@given(instance=ConnectionRestriction_strategy)
@settings(max_examples=50)
def test_connectionrestriction_instantiation(instance):
    assert isinstance(instance, ConnectionRestriction)

@given(instance=oaam_restrictions_SignalRestrictionA_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_signalrestrictiona_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_SignalRestrictionA)

@given(instance=oaam_restrictions_TaskRestrictionA_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_taskrestrictiona_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_TaskRestrictionA)

@given(instance=oaam_restrictions_ConnectionRestrinctionA_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_connectionrestrinctiona_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_ConnectionRestrinctionA)

@given(instance=PowerSourceRestriction_strategy)
@settings(max_examples=50)
def test_powersourcerestriction_instantiation(instance):
    assert isinstance(instance, PowerSourceRestriction)

@given(instance=AreaRestriction_strategy)
@settings(max_examples=50)
def test_arearestriction_instantiation(instance):
    assert isinstance(instance, AreaRestriction)

@given(instance=LocationRestriction_strategy)
@settings(max_examples=50)
def test_locationrestriction_instantiation(instance):
    assert isinstance(instance, LocationRestriction)

@given(instance=DeviceRestriction_strategy)
@settings(max_examples=50)
def test_devicerestriction_instantiation(instance):
    assert isinstance(instance, DeviceRestriction)

@given(instance=DeviceTypeRestriction_strategy)
@settings(max_examples=50)
def test_devicetyperestriction_instantiation(instance):
    assert isinstance(instance, DeviceTypeRestriction)

@given(instance=SynchronicityRestriction_strategy)
@settings(max_examples=50)
def test_synchronicityrestriction_instantiation(instance):
    assert isinstance(instance, SynchronicityRestriction)

@given(instance=TaskSymmetryRestriction_strategy)
@settings(max_examples=50)
def test_tasksymmetryrestriction_instantiation(instance):
    assert isinstance(instance, TaskSymmetryRestriction)

@given(instance=TaskAtomicRestriction_strategy)
@settings(max_examples=50)
def test_taskatomicrestriction_instantiation(instance):
    assert isinstance(instance, TaskAtomicRestriction)

@given(instance=capabilities_CapabilitiesContainerA_strategy)
@settings(max_examples=50)
def test_capabilities_capabilitiescontainera_instantiation(instance):
    assert isinstance(instance, capabilities_CapabilitiesContainerA)

@given(instance=oaam_capabilities_Subcapabilities_strategy)
@settings(max_examples=50)
def test_oaam_capabilities_subcapabilities_instantiation(instance):
    assert isinstance(instance, oaam_capabilities_Subcapabilities)

@given(instance=CapabilitiesContainerA_strategy)
@settings(max_examples=50)
def test_capabilitiescontainera_instantiation(instance):
    assert isinstance(instance, CapabilitiesContainerA)

@given(instance=oaam_capabilities_Capabilities_strategy)
@settings(max_examples=50)
def test_oaam_capabilities_capabilities_instantiation(instance):
    assert isinstance(instance, oaam_capabilities_Capabilities)

@given(instance=capabilities_CapabilityA_strategy)
@settings(max_examples=50)
def test_capabilities_capabilitya_instantiation(instance):
    assert isinstance(instance, capabilities_CapabilityA)

@given(instance=MessageOnConnectionOrDeviceCapability_strategy)
@settings(max_examples=50)
def test_messageonconnectionordevicecapability_instantiation(instance):
    assert isinstance(instance, MessageOnConnectionOrDeviceCapability)

@given(instance=Subcapabilities_strategy)
@settings(max_examples=50)
def test_subcapabilities_instantiation(instance):
    assert isinstance(instance, Subcapabilities)

@given(instance=ConnectionInDuctOrLocationCapability_strategy)
@settings(max_examples=50)
def test_connectioninductorlocationcapability_instantiation(instance):
    assert isinstance(instance, ConnectionInDuctOrLocationCapability)

@given(instance=SubdeviceInDeviceCapability_strategy)
@settings(max_examples=50)
def test_subdeviceindevicecapability_instantiation(instance):
    assert isinstance(instance, SubdeviceInDeviceCapability)

@given(instance=DeviceInLocationCapability_strategy)
@settings(max_examples=50)
def test_deviceinlocationcapability_instantiation(instance):
    assert isinstance(instance, DeviceInLocationCapability)

@given(instance=SignalOnConnectionOrDeviceCapability_strategy)
@settings(max_examples=50)
def test_signalonconnectionordevicecapability_instantiation(instance):
    assert isinstance(instance, SignalOnConnectionOrDeviceCapability)

@given(instance=TaskOnDeviceCapability_strategy)
@settings(max_examples=50)
def test_taskondevicecapability_instantiation(instance):
    assert isinstance(instance, TaskOnDeviceCapability)

@given(instance=ResourceConsumption_strategy)
@settings(max_examples=50)
def test_resourceconsumption_instantiation(instance):
    assert isinstance(instance, ResourceConsumption)

@given(instance=oaam_capabilities_CapabilityA_strategy)
@settings(max_examples=50)
def test_oaam_capabilities_capabilitya_instantiation(instance):
    assert isinstance(instance, oaam_capabilities_CapabilityA)

@given(instance=SignalInMessageCapability_strategy)
@settings(max_examples=50)
def test_signalinmessagecapability_instantiation(instance):
    assert isinstance(instance, SignalInMessageCapability)

@given(instance=SubmessageInMessageCapability_strategy)
@settings(max_examples=50)
def test_submessageinmessagecapability_instantiation(instance):
    assert isinstance(instance, SubmessageInMessageCapability)

@given(instance=MessageOnBusCapability_strategy)
@settings(max_examples=50)
def test_messageonbuscapability_instantiation(instance):
    assert isinstance(instance, MessageOnBusCapability)

@given(instance=SubconnectionInDeviceCapability_strategy)
@settings(max_examples=50)
def test_subconnectionindevicecapability_instantiation(instance):
    assert isinstance(instance, SubconnectionInDeviceCapability)

@given(instance=AnatomyContainerA_strategy)
@settings(max_examples=50)
def test_anatomycontainera_instantiation(instance):
    assert isinstance(instance, AnatomyContainerA)

@given(instance=oaam_anatomy_Anatomy_strategy)
@settings(max_examples=50)
def test_oaam_anatomy_anatomy_instantiation(instance):
    assert isinstance(instance, oaam_anatomy_Anatomy)

@given(instance=anatomy_AnatomyContainerA_strategy)
@settings(max_examples=50)
def test_anatomy_anatomycontainera_instantiation(instance):
    assert isinstance(instance, anatomy_AnatomyContainerA)

@given(instance=oaam_anatomy_Subanatomy_strategy)
@settings(max_examples=50)
def test_oaam_anatomy_subanatomy_instantiation(instance):
    assert isinstance(instance, oaam_anatomy_Subanatomy)

@given(instance=DuctOpening_strategy)
@settings(max_examples=50)
def test_ductopening_instantiation(instance):
    assert isinstance(instance, DuctOpening)

@given(instance=DeviceTypeSymmetry_strategy)
@settings(max_examples=50)
def test_devicetypesymmetry_instantiation(instance):
    assert isinstance(instance, DeviceTypeSymmetry)

@given(instance=PowerSource_strategy)
@settings(max_examples=50)
def test_powersource_instantiation(instance):
    assert isinstance(instance, PowerSource)

@given(instance=AttributeDefinition_strategy)
@settings(max_examples=50)
def test_attributedefinition_instantiation(instance):
    assert isinstance(instance, AttributeDefinition)

@given(instance=DuctType_strategy)
@settings(max_examples=50)
def test_ducttype_instantiation(instance):
    assert isinstance(instance, DuctType)

@given(instance=TaskTypeDissimilarity_strategy)
@settings(max_examples=50)
def test_tasktypedissimilarity_instantiation(instance):
    assert isinstance(instance, TaskTypeDissimilarity)

@given(instance=TaskType_strategy)
@settings(max_examples=50)
def test_tasktype_instantiation(instance):
    assert isinstance(instance, TaskType)

@given(instance=ResourceTypeDissimilarity_strategy)
@settings(max_examples=50)
def test_resourcetypedissimilarity_instantiation(instance):
    assert isinstance(instance, ResourceTypeDissimilarity)

@given(instance=ResourceTypeModifier_strategy)
@settings(max_examples=50)
def test_resourcetypemodifier_instantiation(instance):
    assert isinstance(instance, ResourceTypeModifier)

@given(instance=DeviceType_strategy)
@settings(max_examples=50)
def test_devicetype_instantiation(instance):
    assert isinstance(instance, DeviceType)

@given(instance=SignalType_strategy)
@settings(max_examples=50)
def test_signaltype_instantiation(instance):
    assert isinstance(instance, SignalType)

@given(instance=ResourceTypeModifierLevel_strategy)
@settings(max_examples=50)
def test_resourcetypemodifierlevel_instantiation(instance):
    assert isinstance(instance, ResourceTypeModifierLevel)

@given(instance=oaam_library_ResourceProviderInstanceA_strategy)
@settings(max_examples=50)
def test_oaam_library_resourceproviderinstancea_instantiation(instance):
    assert isinstance(instance, oaam_library_ResourceProviderInstanceA)

@given(instance=ResourceLink_strategy)
@settings(max_examples=50)
def test_resourcelink_instantiation(instance):
    assert isinstance(instance, ResourceLink)

@given(instance=ResourceType_strategy)
@settings(max_examples=50)
def test_resourcetype_instantiation(instance):
    assert isinstance(instance, ResourceType)

@given(instance=ResourceBundle_strategy)
@settings(max_examples=50)
def test_resourcebundle_instantiation(instance):
    assert isinstance(instance, ResourceBundle)

@given(instance=oaam_library_ResourceProviderA_strategy)
@settings(max_examples=50)
def test_oaam_library_resourceprovidera_instantiation(instance):
    assert isinstance(instance, oaam_library_ResourceProviderA)

@given(instance=oaam_library_ResourceConsumerA_strategy)
@settings(max_examples=50)
def test_oaam_library_resourceconsumera_instantiation(instance):
    assert isinstance(instance, oaam_library_ResourceConsumerA)

@given(instance=ResourceGroup_strategy)
@settings(max_examples=50)
def test_resourcegroup_instantiation(instance):
    assert isinstance(instance, ResourceGroup)

@given(instance=Resource_strategy)
@settings(max_examples=50)
def test_resource_instantiation(instance):
    assert isinstance(instance, Resource)

@given(instance=Struct_strategy)
@settings(max_examples=50)
def test_struct_instantiation(instance):
    assert isinstance(instance, Struct)

@given(instance=DataTypeA_strategy)
@settings(max_examples=50)
def test_datatypea_instantiation(instance):
    assert isinstance(instance, DataTypeA)

@given(instance=oaam_common_Array_strategy)
@settings(max_examples=50)
def test_oaam_common_array_instantiation(instance):
    assert isinstance(instance, oaam_common_Array)



@given(instance=oaam_common_Array_strategy)
def test_oaam_common_array_nElements_setter(instance):
    original = instance.nElements
    instance.nElements = original
    assert instance.nElements == original



@given(instance=oaam_common_Array_strategy)
def test_oaam_common_array_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=oaam_common_Byte_strategy)
@settings(max_examples=50)
def test_oaam_common_byte_instantiation(instance):
    assert isinstance(instance, oaam_common_Byte)



@given(instance=oaam_common_Byte_strategy)
def test_oaam_common_byte_nBits_setter(instance):
    original = instance.nBits
    instance.nBits = original
    assert instance.nBits == original

@given(instance=oaam_common_Character_strategy)
@settings(max_examples=50)
def test_oaam_common_character_instantiation(instance):
    assert isinstance(instance, oaam_common_Character)



@given(instance=oaam_common_Character_strategy)
def test_oaam_common_character_nBits_setter(instance):
    original = instance.nBits
    instance.nBits = original
    assert instance.nBits == original



@given(instance=oaam_common_Character_strategy)
def test_oaam_common_character_encoding_setter(instance):
    original = instance.encoding
    instance.encoding = original
    assert instance.encoding == original

@given(instance=oaam_common_Boolean_strategy)
@settings(max_examples=50)
def test_oaam_common_boolean_instantiation(instance):
    assert isinstance(instance, oaam_common_Boolean)



@given(instance=oaam_common_Boolean_strategy)
def test_oaam_common_boolean_nBits_setter(instance):
    original = instance.nBits
    instance.nBits = original
    assert instance.nBits == original

@given(instance=oaam_common_Struct_strategy)
@settings(max_examples=50)
def test_oaam_common_struct_instantiation(instance):
    assert isinstance(instance, oaam_common_Struct)



@given(instance=oaam_common_Struct_strategy)
def test_oaam_common_struct_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original



@given(instance=oaam_common_Struct_strategy)
def test_oaam_common_struct_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=oaam_common_FloatingPoint_strategy)
@settings(max_examples=50)
def test_oaam_common_floatingpoint_instantiation(instance):
    assert isinstance(instance, oaam_common_FloatingPoint)



@given(instance=oaam_common_FloatingPoint_strategy)
def test_oaam_common_floatingpoint_endianess_setter(instance):
    original = instance.endianess
    instance.endianess = original
    assert instance.endianess == original



@given(instance=oaam_common_FloatingPoint_strategy)
def test_oaam_common_floatingpoint_nBits_setter(instance):
    original = instance.nBits
    instance.nBits = original
    assert instance.nBits == original

@given(instance=oaam_common_Integer_strategy)
@settings(max_examples=50)
def test_oaam_common_integer_instantiation(instance):
    assert isinstance(instance, oaam_common_Integer)



@given(instance=oaam_common_Integer_strategy)
def test_oaam_common_integer_nBits_setter(instance):
    original = instance.nBits
    instance.nBits = original
    assert instance.nBits == original



@given(instance=oaam_common_Integer_strategy)
def test_oaam_common_integer_signed_setter(instance):
    original = instance.signed
    instance.signed = original
    assert instance.signed == original



@given(instance=oaam_common_Integer_strategy)
def test_oaam_common_integer_endianess_setter(instance):
    original = instance.endianess
    instance.endianess = original
    assert instance.endianess == original

@given(instance=BoolA_strategy)
@settings(max_examples=50)
def test_boola_instantiation(instance):
    assert isinstance(instance, BoolA)

@given(instance=common_OaamBaseElementA_strategy)
@settings(max_examples=50)
def test_common_oaambaseelementa_instantiation(instance):
    assert isinstance(instance, common_OaamBaseElementA)

@given(instance=oaam_allocations_DeviceAssignment_strategy)
@settings(max_examples=50)
def test_oaam_allocations_deviceassignment_instantiation(instance):
    assert isinstance(instance, oaam_allocations_DeviceAssignment)

@given(instance=oaam_functions_Signal_strategy)
@settings(max_examples=50)
def test_oaam_functions_signal_instantiation(instance):
    assert isinstance(instance, oaam_functions_Signal)



@given(instance=oaam_functions_Signal_strategy)
def test_oaam_functions_signal_outIndex_setter(instance):
    original = instance.outIndex
    instance.outIndex = original
    assert instance.outIndex == original



@given(instance=oaam_functions_Signal_strategy)
def test_oaam_functions_signal_inIndex_setter(instance):
    original = instance.inIndex
    instance.inIndex = original
    assert instance.inIndex == original

@given(instance=oaam_restrictions_ConnectionRestriction_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_connectionrestriction_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_ConnectionRestriction)



@given(instance=oaam_restrictions_ConnectionRestriction_strategy)
def test_oaam_restrictions_connectionrestriction_isForbidden_setter(instance):
    original = instance.isForbidden
    instance.isForbidden = original
    assert instance.isForbidden == original



@given(instance=oaam_restrictions_ConnectionRestriction_strategy)
def test_oaam_restrictions_connectionrestriction_connectionName_setter(instance):
    original = instance.connectionName
    instance.connectionName = original
    assert instance.connectionName == original

@given(instance=oaam_capabilities_MessageOnBusCapability_strategy)
@settings(max_examples=50)
def test_oaam_capabilities_messageonbuscapability_instantiation(instance):
    assert isinstance(instance, oaam_capabilities_MessageOnBusCapability)

@given(instance=oaam_anatomy_DuctOpening_strategy)
@settings(max_examples=50)
def test_oaam_anatomy_ductopening_instantiation(instance):
    assert isinstance(instance, oaam_anatomy_DuctOpening)

@given(instance=oaam_hardware_Connection_strategy)
@settings(max_examples=50)
def test_oaam_hardware_connection_instantiation(instance):
    assert isinstance(instance, oaam_hardware_Connection)

@given(instance=oaam_allocations_Schedule_strategy)
@settings(max_examples=50)
def test_oaam_allocations_schedule_instantiation(instance):
    assert isinstance(instance, oaam_allocations_Schedule)



@given(instance=oaam_allocations_Schedule_strategy)
def test_oaam_allocations_schedule_isPeriodic_setter(instance):
    original = instance.isPeriodic
    instance.isPeriodic = original
    assert instance.isPeriodic == original



@given(instance=oaam_allocations_Schedule_strategy)
def test_oaam_allocations_schedule_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=oaam_allocations_Schedule_strategy)
def test_oaam_allocations_schedule_rate_setter(instance):
    original = instance.rate
    instance.rate = original
    assert instance.rate == original

@given(instance=oaam_scenario_OperationMode_strategy)
@settings(max_examples=50)
def test_oaam_scenario_operationmode_instantiation(instance):
    assert isinstance(instance, oaam_scenario_OperationMode)

@given(instance=oaam_library_ResourceTypeModifierLevel_strategy)
@settings(max_examples=50)
def test_oaam_library_resourcetypemodifierlevel_instantiation(instance):
    assert isinstance(instance, oaam_library_ResourceTypeModifierLevel)

@given(instance=oaam_library_TaskType_strategy)
@settings(max_examples=50)
def test_oaam_library_tasktype_instantiation(instance):
    assert isinstance(instance, oaam_library_TaskType)



@given(instance=oaam_library_TaskType_strategy)
def test_oaam_library_tasktype_preferredExecutionRate_setter(instance):
    original = instance.preferredExecutionRate
    instance.preferredExecutionRate = original
    assert instance.preferredExecutionRate == original



@given(instance=oaam_library_TaskType_strategy)
def test_oaam_library_tasktype_isDeterministic_setter(instance):
    original = instance.isDeterministic
    instance.isDeterministic = original
    assert instance.isDeterministic == original

@given(instance=oaam_anatomy_Location_strategy)
@settings(max_examples=50)
def test_oaam_anatomy_location_instantiation(instance):
    assert isinstance(instance, oaam_anatomy_Location)



@given(instance=oaam_anatomy_Location_strategy)
def test_oaam_anatomy_location_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=oaam_capabilities_SubconnectionInDeviceCapability_strategy)
@settings(max_examples=50)
def test_oaam_capabilities_subconnectionindevicecapability_instantiation(instance):
    assert isinstance(instance, oaam_capabilities_SubconnectionInDeviceCapability)

@given(instance=oaam_restrictions_ConnectionTypeRestriction_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_connectiontyperestriction_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_ConnectionTypeRestriction)



@given(instance=oaam_restrictions_ConnectionTypeRestriction_strategy)
def test_oaam_restrictions_connectiontyperestriction_connectionTypeName_setter(instance):
    original = instance.connectionTypeName
    instance.connectionTypeName = original
    assert instance.connectionTypeName == original



@given(instance=oaam_restrictions_ConnectionTypeRestriction_strategy)
def test_oaam_restrictions_connectiontyperestriction_isForbidden_setter(instance):
    original = instance.isForbidden
    instance.isForbidden = original
    assert instance.isForbidden == original

@given(instance=oaam_hardware_Device_strategy)
@settings(max_examples=50)
def test_oaam_hardware_device_instantiation(instance):
    assert isinstance(instance, oaam_hardware_Device)

@given(instance=oaam_allocations_ScheduledTime_strategy)
@settings(max_examples=50)
def test_oaam_allocations_scheduledtime_instantiation(instance):
    assert isinstance(instance, oaam_allocations_ScheduledTime)



@given(instance=oaam_allocations_ScheduledTime_strategy)
def test_oaam_allocations_scheduledtime_restart_setter(instance):
    original = instance.restart
    instance.restart = original
    assert instance.restart == original



@given(instance=oaam_allocations_ScheduledTime_strategy)
def test_oaam_allocations_scheduledtime_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=oaam_allocations_ScheduledTime_strategy)
def test_oaam_allocations_scheduledtime_cycle_setter(instance):
    original = instance.cycle
    instance.cycle = original
    assert instance.cycle == original



@given(instance=oaam_allocations_ScheduledTime_strategy)
def test_oaam_allocations_scheduledtime_startTime_setter(instance):
    original = instance.startTime
    instance.startTime = original
    assert instance.startTime == original

@given(instance=oaam_functions_Task_strategy)
@settings(max_examples=50)
def test_oaam_functions_task_instantiation(instance):
    assert isinstance(instance, oaam_functions_Task)



@given(instance=oaam_functions_Task_strategy)
def test_oaam_functions_task_fixedRate_setter(instance):
    original = instance.fixedRate
    instance.fixedRate = original
    assert instance.fixedRate == original



@given(instance=oaam_functions_Task_strategy)
def test_oaam_functions_task_nParallels_setter(instance):
    original = instance.nParallels
    instance.nParallels = original
    assert instance.nParallels == original

@given(instance=oaam_systems_InformationPower_strategy)
@settings(max_examples=50)
def test_oaam_systems_informationpower_instantiation(instance):
    assert isinstance(instance, oaam_systems_InformationPower)



@given(instance=oaam_systems_InformationPower_strategy)
def test_oaam_systems_informationpower_power_setter(instance):
    original = instance.power
    instance.power = original
    assert instance.power == original

@given(instance=oaam_allocations_MessageSegment_strategy)
@settings(max_examples=50)
def test_oaam_allocations_messagesegment_instantiation(instance):
    assert isinstance(instance, oaam_allocations_MessageSegment)

@given(instance=oaam_capabilities_DeviceInLocationCapability_strategy)
@settings(max_examples=50)
def test_oaam_capabilities_deviceinlocationcapability_instantiation(instance):
    assert isinstance(instance, oaam_capabilities_DeviceInLocationCapability)

@given(instance=oaam_scenario_ScenarioParameterNumeric_strategy)
@settings(max_examples=50)
def test_oaam_scenario_scenarioparameternumeric_instantiation(instance):
    assert isinstance(instance, oaam_scenario_ScenarioParameterNumeric)



@given(instance=oaam_scenario_ScenarioParameterNumeric_strategy)
def test_oaam_scenario_scenarioparameternumeric_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oaam_systems_InformationMaterial_strategy)
@settings(max_examples=50)
def test_oaam_systems_informationmaterial_instantiation(instance):
    assert isinstance(instance, oaam_systems_InformationMaterial)



@given(instance=oaam_systems_InformationMaterial_strategy)
def test_oaam_systems_informationmaterial_density_setter(instance):
    original = instance.density
    instance.density = original
    assert instance.density == original



@given(instance=oaam_systems_InformationMaterial_strategy)
def test_oaam_systems_informationmaterial_velocity_setter(instance):
    original = instance.velocity
    instance.velocity = original
    assert instance.velocity == original

@given(instance=oaam_systems_System_strategy)
@settings(max_examples=50)
def test_oaam_systems_system_instantiation(instance):
    assert isinstance(instance, oaam_systems_System)

@given(instance=oaam_restrictions_DeviceRestriction_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_devicerestriction_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_DeviceRestriction)



@given(instance=oaam_restrictions_DeviceRestriction_strategy)
def test_oaam_restrictions_devicerestriction_deviceName_setter(instance):
    original = instance.deviceName
    instance.deviceName = original
    assert instance.deviceName == original



@given(instance=oaam_restrictions_DeviceRestriction_strategy)
def test_oaam_restrictions_devicerestriction_isForbidden_setter(instance):
    original = instance.isForbidden
    instance.isForbidden = original
    assert instance.isForbidden == original

@given(instance=oaam_functions_TaskGroup_strategy)
@settings(max_examples=50)
def test_oaam_functions_taskgroup_instantiation(instance):
    assert isinstance(instance, oaam_functions_TaskGroup)

@given(instance=oaam_capabilities_SubdeviceInDeviceCapability_strategy)
@settings(max_examples=50)
def test_oaam_capabilities_subdeviceindevicecapability_instantiation(instance):
    assert isinstance(instance, oaam_capabilities_SubdeviceInDeviceCapability)

@given(instance=oaam_scenario_Variant_strategy)
@settings(max_examples=50)
def test_oaam_scenario_variant_instantiation(instance):
    assert isinstance(instance, oaam_scenario_Variant)

@given(instance=oaam_hardware_Io_strategy)
@settings(max_examples=50)
def test_oaam_hardware_io_instantiation(instance):
    assert isinstance(instance, oaam_hardware_Io)

@given(instance=oaam_systems_InformationSignal_strategy)
@settings(max_examples=50)
def test_oaam_systems_informationsignal_instantiation(instance):
    assert isinstance(instance, oaam_systems_InformationSignal)



@given(instance=oaam_systems_InformationSignal_strategy)
def test_oaam_systems_informationsignal_rate_setter(instance):
    original = instance.rate
    instance.rate = original
    assert instance.rate == original



@given(instance=oaam_systems_InformationSignal_strategy)
def test_oaam_systems_informationsignal_resolution_setter(instance):
    original = instance.resolution
    instance.resolution = original
    assert instance.resolution == original



@given(instance=oaam_systems_InformationSignal_strategy)
def test_oaam_systems_informationsignal_latency_setter(instance):
    original = instance.latency
    instance.latency = original
    assert instance.latency == original



@given(instance=oaam_systems_InformationSignal_strategy)
def test_oaam_systems_informationsignal_accuracy_setter(instance):
    original = instance.accuracy
    instance.accuracy = original
    assert instance.accuracy == original



@given(instance=oaam_systems_InformationSignal_strategy)
def test_oaam_systems_informationsignal_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=oaam_allocations_ConnectionAssignment_strategy)
@settings(max_examples=50)
def test_oaam_allocations_connectionassignment_instantiation(instance):
    assert isinstance(instance, oaam_allocations_ConnectionAssignment)

@given(instance=oaam_restrictions_SynchronicityRestriction_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_synchronicityrestriction_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_SynchronicityRestriction)



@given(instance=oaam_restrictions_SynchronicityRestriction_strategy)
def test_oaam_restrictions_synchronicityrestriction_maxJitter_setter(instance):
    original = instance.maxJitter
    instance.maxJitter = original
    assert instance.maxJitter == original

@given(instance=oaam_functions_ExternalTaskLink_strategy)
@settings(max_examples=50)
def test_oaam_functions_externaltasklink_instantiation(instance):
    assert isinstance(instance, oaam_functions_ExternalTaskLink)



@given(instance=oaam_functions_ExternalTaskLink_strategy)
def test_oaam_functions_externaltasklink_filter_setter(instance):
    original = instance.filter
    instance.filter = original
    assert instance.filter == original

@given(instance=oaam_library_MessageType_strategy)
@settings(max_examples=50)
def test_oaam_library_messagetype_instantiation(instance):
    assert isinstance(instance, oaam_library_MessageType)



@given(instance=oaam_library_MessageType_strategy)
def test_oaam_library_messagetype_minLength_setter(instance):
    original = instance.minLength
    instance.minLength = original
    assert instance.minLength == original



@given(instance=oaam_library_MessageType_strategy)
def test_oaam_library_messagetype_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original



@given(instance=oaam_library_MessageType_strategy)
def test_oaam_library_messagetype_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=oaam_functions_FunctionsContainerA_strategy)
@settings(max_examples=50)
def test_oaam_functions_functionscontainera_instantiation(instance):
    assert isinstance(instance, oaam_functions_FunctionsContainerA)

@given(instance=oaam_allocations_SignalAssignment_strategy)
@settings(max_examples=50)
def test_oaam_allocations_signalassignment_instantiation(instance):
    assert isinstance(instance, oaam_allocations_SignalAssignment)

@given(instance=oaam_anatomy_AreaSymmetry_strategy)
@settings(max_examples=50)
def test_oaam_anatomy_areasymmetry_instantiation(instance):
    assert isinstance(instance, oaam_anatomy_AreaSymmetry)

@given(instance=oaam_anatomy_Area_strategy)
@settings(max_examples=50)
def test_oaam_anatomy_area_instantiation(instance):
    assert isinstance(instance, oaam_anatomy_Area)

@given(instance=oaam_hardware_Bus_strategy)
@settings(max_examples=50)
def test_oaam_hardware_bus_instantiation(instance):
    assert isinstance(instance, oaam_hardware_Bus)

@given(instance=oaam_restrictions_LocationRestriction_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_locationrestriction_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_LocationRestriction)



@given(instance=oaam_restrictions_LocationRestriction_strategy)
def test_oaam_restrictions_locationrestriction_isForbidden_setter(instance):
    original = instance.isForbidden
    instance.isForbidden = original
    assert instance.isForbidden == original



@given(instance=oaam_restrictions_LocationRestriction_strategy)
def test_oaam_restrictions_locationrestriction_locationName_setter(instance):
    original = instance.locationName
    instance.locationName = original
    assert instance.locationName == original

@given(instance=oaam_allocations_SubconnectionAssignment_strategy)
@settings(max_examples=50)
def test_oaam_allocations_subconnectionassignment_instantiation(instance):
    assert isinstance(instance, oaam_allocations_SubconnectionAssignment)

@given(instance=oaam_hardware_DeviceSymmetry_strategy)
@settings(max_examples=50)
def test_oaam_hardware_devicesymmetry_instantiation(instance):
    assert isinstance(instance, oaam_hardware_DeviceSymmetry)

@given(instance=oaam_library_LocationType_strategy)
@settings(max_examples=50)
def test_oaam_library_locationtype_instantiation(instance):
    assert isinstance(instance, oaam_library_LocationType)



@given(instance=oaam_library_LocationType_strategy)
def test_oaam_library_locationtype_isJoint_setter(instance):
    original = instance.isJoint
    instance.isJoint = original
    assert instance.isJoint == original

@given(instance=oaam_capabilities_SignalOnConnectionOrDeviceCapability_strategy)
@settings(max_examples=50)
def test_oaam_capabilities_signalonconnectionordevicecapability_instantiation(instance):
    assert isinstance(instance, oaam_capabilities_SignalOnConnectionOrDeviceCapability)



@given(instance=oaam_capabilities_SignalOnConnectionOrDeviceCapability_strategy)
def test_oaam_capabilities_signalonconnectionordevicecapability_worstCaseTransmissionTime_setter(instance):
    original = instance.worstCaseTransmissionTime
    instance.worstCaseTransmissionTime = original
    assert instance.worstCaseTransmissionTime == original

@given(instance=oaam_capabilities_TaskOnDeviceCapability_strategy)
@settings(max_examples=50)
def test_oaam_capabilities_taskondevicecapability_instantiation(instance):
    assert isinstance(instance, oaam_capabilities_TaskOnDeviceCapability)



@given(instance=oaam_capabilities_TaskOnDeviceCapability_strategy)
def test_oaam_capabilities_taskondevicecapability_worstCaseExecutionTime_setter(instance):
    original = instance.worstCaseExecutionTime
    instance.worstCaseExecutionTime = original
    assert instance.worstCaseExecutionTime == original



@given(instance=oaam_capabilities_TaskOnDeviceCapability_strategy)
def test_oaam_capabilities_taskondevicecapability_failureProbability_setter(instance):
    original = instance.failureProbability
    instance.failureProbability = original
    assert instance.failureProbability == original

@given(instance=oaam_library_DeviceType_strategy)
@settings(max_examples=50)
def test_oaam_library_devicetype_instantiation(instance):
    assert isinstance(instance, oaam_library_DeviceType)



@given(instance=oaam_library_DeviceType_strategy)
def test_oaam_library_devicetype_isSubdevice_setter(instance):
    original = instance.isSubdevice
    instance.isSubdevice = original
    assert instance.isSubdevice == original



@given(instance=oaam_library_DeviceType_strategy)
def test_oaam_library_devicetype_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original



@given(instance=oaam_library_DeviceType_strategy)
def test_oaam_library_devicetype_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=oaam_library_DeviceType_strategy)
def test_oaam_library_devicetype_mtbf_setter(instance):
    original = instance.mtbf
    instance.mtbf = original
    assert instance.mtbf == original



@given(instance=oaam_library_DeviceType_strategy)
def test_oaam_library_devicetype_canHaveSubdevices_setter(instance):
    original = instance.canHaveSubdevices
    instance.canHaveSubdevices = original
    assert instance.canHaveSubdevices == original



@given(instance=oaam_library_DeviceType_strategy)
def test_oaam_library_devicetype_isSelfManaging_setter(instance):
    original = instance.isSelfManaging
    instance.isSelfManaging = original
    assert instance.isSelfManaging == original

@given(instance=oaam_restrictions_TaskAtomicRestriction_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_taskatomicrestriction_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_TaskAtomicRestriction)

@given(instance=oaam_functions_Input_strategy)
@settings(max_examples=50)
def test_oaam_functions_input_instantiation(instance):
    assert isinstance(instance, oaam_functions_Input)



@given(instance=oaam_functions_Input_strategy)
def test_oaam_functions_input_queueLength_setter(instance):
    original = instance.queueLength
    instance.queueLength = original
    assert instance.queueLength == original

@given(instance=oaam_capabilities_SubmessageInMessageCapability_strategy)
@settings(max_examples=50)
def test_oaam_capabilities_submessageinmessagecapability_instantiation(instance):
    assert isinstance(instance, oaam_capabilities_SubmessageInMessageCapability)

@given(instance=oaam_restrictions_DeviceTypeRestriction_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_devicetyperestriction_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_DeviceTypeRestriction)



@given(instance=oaam_restrictions_DeviceTypeRestriction_strategy)
def test_oaam_restrictions_devicetyperestriction_isForbidden_setter(instance):
    original = instance.isForbidden
    instance.isForbidden = original
    assert instance.isForbidden == original



@given(instance=oaam_restrictions_DeviceTypeRestriction_strategy)
def test_oaam_restrictions_devicetyperestriction_deviceTypeName_setter(instance):
    original = instance.deviceTypeName
    instance.deviceTypeName = original
    assert instance.deviceTypeName == original

@given(instance=oaam_functions_ExternalOutputLink_strategy)
@settings(max_examples=50)
def test_oaam_functions_externaloutputlink_instantiation(instance):
    assert isinstance(instance, oaam_functions_ExternalOutputLink)



@given(instance=oaam_functions_ExternalOutputLink_strategy)
def test_oaam_functions_externaloutputlink_filter_setter(instance):
    original = instance.filter
    instance.filter = original
    assert instance.filter == original

@given(instance=oaam_anatomy_Position3D_strategy)
@settings(max_examples=50)
def test_oaam_anatomy_position3d_instantiation(instance):
    assert isinstance(instance, oaam_anatomy_Position3D)



@given(instance=oaam_anatomy_Position3D_strategy)
def test_oaam_anatomy_position3d_z_setter(instance):
    original = instance.z
    instance.z = original
    assert instance.z == original



@given(instance=oaam_anatomy_Position3D_strategy)
def test_oaam_anatomy_position3d_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=oaam_anatomy_Position3D_strategy)
def test_oaam_anatomy_position3d_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=oaam_library_ConnectionType_strategy)
@settings(max_examples=50)
def test_oaam_library_connectiontype_instantiation(instance):
    assert isinstance(instance, oaam_library_ConnectionType)



@given(instance=oaam_library_ConnectionType_strategy)
def test_oaam_library_connectiontype_nEndPoints_setter(instance):
    original = instance.nEndPoints
    instance.nEndPoints = original
    assert instance.nEndPoints == original



@given(instance=oaam_library_ConnectionType_strategy)
def test_oaam_library_connectiontype_nJoints_setter(instance):
    original = instance.nJoints
    instance.nJoints = original
    assert instance.nJoints == original



@given(instance=oaam_library_ConnectionType_strategy)
def test_oaam_library_connectiontype_isPower_setter(instance):
    original = instance.isPower
    instance.isPower = original
    assert instance.isPower == original



@given(instance=oaam_library_ConnectionType_strategy)
def test_oaam_library_connectiontype_maxInterfaceToJointDistance_setter(instance):
    original = instance.maxInterfaceToJointDistance
    instance.maxInterfaceToJointDistance = original
    assert instance.maxInterfaceToJointDistance == original



@given(instance=oaam_library_ConnectionType_strategy)
def test_oaam_library_connectiontype_requiresMaster_setter(instance):
    original = instance.requiresMaster
    instance.requiresMaster = original
    assert instance.requiresMaster == original



@given(instance=oaam_library_ConnectionType_strategy)
def test_oaam_library_connectiontype_maxJointBranches_setter(instance):
    original = instance.maxJointBranches
    instance.maxJointBranches = original
    assert instance.maxJointBranches == original



@given(instance=oaam_library_ConnectionType_strategy)
def test_oaam_library_connectiontype_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original



@given(instance=oaam_library_ConnectionType_strategy)
def test_oaam_library_connectiontype_isInformation_setter(instance):
    original = instance.isInformation
    instance.isInformation = original
    assert instance.isInformation == original



@given(instance=oaam_library_ConnectionType_strategy)
def test_oaam_library_connectiontype_nStartingPoints_setter(instance):
    original = instance.nStartingPoints
    instance.nStartingPoints = original
    assert instance.nStartingPoints == original



@given(instance=oaam_library_ConnectionType_strategy)
def test_oaam_library_connectiontype_isSwitched_setter(instance):
    original = instance.isSwitched
    instance.isSwitched = original
    assert instance.isSwitched == original



@given(instance=oaam_library_ConnectionType_strategy)
def test_oaam_library_connectiontype_isWireless_setter(instance):
    original = instance.isWireless
    instance.isWireless = original
    assert instance.isWireless == original



@given(instance=oaam_library_ConnectionType_strategy)
def test_oaam_library_connectiontype_allowsCircles_setter(instance):
    original = instance.allowsCircles
    instance.allowsCircles = original
    assert instance.allowsCircles == original



@given(instance=oaam_library_ConnectionType_strategy)
def test_oaam_library_connectiontype_isUnidirectional_setter(instance):
    original = instance.isUnidirectional
    instance.isUnidirectional = original
    assert instance.isUnidirectional == original



@given(instance=oaam_library_ConnectionType_strategy)
def test_oaam_library_connectiontype_directConnectionsAllowed_setter(instance):
    original = instance.directConnectionsAllowed
    instance.directConnectionsAllowed = original
    assert instance.directConnectionsAllowed == original

@given(instance=oaam_allocations_MessageA_strategy)
@settings(max_examples=50)
def test_oaam_allocations_messagea_instantiation(instance):
    assert isinstance(instance, oaam_allocations_MessageA)



@given(instance=oaam_allocations_MessageA_strategy)
def test_oaam_allocations_messagea_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=oaam_allocations_MessageA_strategy)
def test_oaam_allocations_messagea_isPersistent_setter(instance):
    original = instance.isPersistent
    instance.isPersistent = original
    assert instance.isPersistent == original

@given(instance=oaam_functions_TaskRedundancy_strategy)
@settings(max_examples=50)
def test_oaam_functions_taskredundancy_instantiation(instance):
    assert isinstance(instance, oaam_functions_TaskRedundancy)

@given(instance=oaam_library_BusType_strategy)
@settings(max_examples=50)
def test_oaam_library_bustype_instantiation(instance):
    assert isinstance(instance, oaam_library_BusType)



@given(instance=oaam_library_BusType_strategy)
def test_oaam_library_bustype_isSelfManaging_setter(instance):
    original = instance.isSelfManaging
    instance.isSelfManaging = original
    assert instance.isSelfManaging == original



@given(instance=oaam_library_BusType_strategy)
def test_oaam_library_bustype_requiresMaster_setter(instance):
    original = instance.requiresMaster
    instance.requiresMaster = original
    assert instance.requiresMaster == original



@given(instance=oaam_library_BusType_strategy)
def test_oaam_library_bustype_mtbf_setter(instance):
    original = instance.mtbf
    instance.mtbf = original
    assert instance.mtbf == original

@given(instance=oaam_capabilities_ConnectionInDuctOrLocationCapability_strategy)
@settings(max_examples=50)
def test_oaam_capabilities_connectioninductorlocationcapability_instantiation(instance):
    assert isinstance(instance, oaam_capabilities_ConnectionInDuctOrLocationCapability)

@given(instance=oaam_scenario_ScenarioParameterBool_strategy)
@settings(max_examples=50)
def test_oaam_scenario_scenarioparameterbool_instantiation(instance):
    assert isinstance(instance, oaam_scenario_ScenarioParameterBool)



@given(instance=oaam_scenario_ScenarioParameterBool_strategy)
def test_oaam_scenario_scenarioparameterbool_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oaam_functions_Output_strategy)
@settings(max_examples=50)
def test_oaam_functions_output_instantiation(instance):
    assert isinstance(instance, oaam_functions_Output)



@given(instance=oaam_functions_Output_strategy)
def test_oaam_functions_output_fixedRate_setter(instance):
    original = instance.fixedRate
    instance.fixedRate = original
    assert instance.fixedRate == original

@given(instance=oaam_allocations_SignalAssignmentSegment_strategy)
@settings(max_examples=50)
def test_oaam_allocations_signalassignmentsegment_instantiation(instance):
    assert isinstance(instance, oaam_allocations_SignalAssignmentSegment)

@given(instance=oaam_allocations_ConnectionAssignmentSegment_strategy)
@settings(max_examples=50)
def test_oaam_allocations_connectionassignmentsegment_instantiation(instance):
    assert isinstance(instance, oaam_allocations_ConnectionAssignmentSegment)

@given(instance=oaam_restrictions_TimeDelayRestriction_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_timedelayrestriction_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_TimeDelayRestriction)



@given(instance=oaam_restrictions_TimeDelayRestriction_strategy)
def test_oaam_restrictions_timedelayrestriction_delay_setter(instance):
    original = instance.delay
    instance.delay = original
    assert instance.delay == original

@given(instance=oaam_allocations_SubdeviceAssignment_strategy)
@settings(max_examples=50)
def test_oaam_allocations_subdeviceassignment_instantiation(instance):
    assert isinstance(instance, oaam_allocations_SubdeviceAssignment)

@given(instance=oaam_functions_TaskSymmetry_strategy)
@settings(max_examples=50)
def test_oaam_functions_tasksymmetry_instantiation(instance):
    assert isinstance(instance, oaam_functions_TaskSymmetry)

@given(instance=oaam_library_DuctType_strategy)
@settings(max_examples=50)
def test_oaam_library_ducttype_instantiation(instance):
    assert isinstance(instance, oaam_library_DuctType)

@given(instance=oaam_library_SignalType_strategy)
@settings(max_examples=50)
def test_oaam_library_signaltype_instantiation(instance):
    assert isinstance(instance, oaam_library_SignalType)

@given(instance=oaam_restrictions_TaskSymmetryRestriction_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_tasksymmetryrestriction_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_TaskSymmetryRestriction)



@given(instance=oaam_restrictions_TaskSymmetryRestriction_strategy)
def test_oaam_restrictions_tasksymmetryrestriction_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=oaam_library_ResourceBundle_strategy)
@settings(max_examples=50)
def test_oaam_library_resourcebundle_instantiation(instance):
    assert isinstance(instance, oaam_library_ResourceBundle)



@given(instance=oaam_library_ResourceBundle_strategy)
def test_oaam_library_resourcebundle_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original



@given(instance=oaam_library_ResourceBundle_strategy)
def test_oaam_library_resourcebundle_mtbf_setter(instance):
    original = instance.mtbf
    instance.mtbf = original
    assert instance.mtbf == original



@given(instance=oaam_library_ResourceBundle_strategy)
def test_oaam_library_resourcebundle_mass_setter(instance):
    original = instance.mass
    instance.mass = original
    assert instance.mass == original

@given(instance=oaam_restrictions_PowerSourceRestriction_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_powersourcerestriction_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_PowerSourceRestriction)



@given(instance=oaam_restrictions_PowerSourceRestriction_strategy)
def test_oaam_restrictions_powersourcerestriction_isForbidden_setter(instance):
    original = instance.isForbidden
    instance.isForbidden = original
    assert instance.isForbidden == original



@given(instance=oaam_restrictions_PowerSourceRestriction_strategy)
def test_oaam_restrictions_powersourcerestriction_powerSourceName_setter(instance):
    original = instance.powerSourceName
    instance.powerSourceName = original
    assert instance.powerSourceName == original

@given(instance=oaam_functions_SignalGroup_strategy)
@settings(max_examples=50)
def test_oaam_functions_signalgroup_instantiation(instance):
    assert isinstance(instance, oaam_functions_SignalGroup)

@given(instance=oaam_systems_InformationFlow_strategy)
@settings(max_examples=50)
def test_oaam_systems_informationflow_instantiation(instance):
    assert isinstance(instance, oaam_systems_InformationFlow)

@given(instance=oaam_allocations_TaskAssignment_strategy)
@settings(max_examples=50)
def test_oaam_allocations_taskassignment_instantiation(instance):
    assert isinstance(instance, oaam_allocations_TaskAssignment)

@given(instance=oaam_anatomy_Duct_strategy)
@settings(max_examples=50)
def test_oaam_anatomy_duct_instantiation(instance):
    assert isinstance(instance, oaam_anatomy_Duct)



@given(instance=oaam_anatomy_Duct_strategy)
def test_oaam_anatomy_duct_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=oaam_restrictions_SegregationRestriction_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_segregationrestriction_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_SegregationRestriction)



@given(instance=oaam_restrictions_SegregationRestriction_strategy)
def test_oaam_restrictions_segregationrestriction_dissimilarLocation_setter(instance):
    original = instance.dissimilarLocation
    instance.dissimilarLocation = original
    assert instance.dissimilarLocation == original



@given(instance=oaam_restrictions_SegregationRestriction_strategy)
def test_oaam_restrictions_segregationrestriction_dissimilarPowerSource_setter(instance):
    original = instance.dissimilarPowerSource
    instance.dissimilarPowerSource = original
    assert instance.dissimilarPowerSource == original



@given(instance=oaam_restrictions_SegregationRestriction_strategy)
def test_oaam_restrictions_segregationrestriction_dissimilarArea_setter(instance):
    original = instance.dissimilarArea
    instance.dissimilarArea = original
    assert instance.dissimilarArea == original



@given(instance=oaam_restrictions_SegregationRestriction_strategy)
def test_oaam_restrictions_segregationrestriction_dissimilarTechnology_setter(instance):
    original = instance.dissimilarTechnology
    instance.dissimilarTechnology = original
    assert instance.dissimilarTechnology == original

@given(instance=oaam_anatomy_LocationSymmetry_strategy)
@settings(max_examples=50)
def test_oaam_anatomy_locationsymmetry_instantiation(instance):
    assert isinstance(instance, oaam_anatomy_LocationSymmetry)

@given(instance=oaam_restrictions_AreaRestriction_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_arearestriction_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_AreaRestriction)



@given(instance=oaam_restrictions_AreaRestriction_strategy)
def test_oaam_restrictions_arearestriction_areaName_setter(instance):
    original = instance.areaName
    instance.areaName = original
    assert instance.areaName == original



@given(instance=oaam_restrictions_AreaRestriction_strategy)
def test_oaam_restrictions_arearestriction_isForbidden_setter(instance):
    original = instance.isForbidden
    instance.isForbidden = original
    assert instance.isForbidden == original

@given(instance=oaam_capabilities_MessageOnConnectionOrDeviceCapability_strategy)
@settings(max_examples=50)
def test_oaam_capabilities_messageonconnectionordevicecapability_instantiation(instance):
    assert isinstance(instance, oaam_capabilities_MessageOnConnectionOrDeviceCapability)



@given(instance=oaam_capabilities_MessageOnConnectionOrDeviceCapability_strategy)
def test_oaam_capabilities_messageonconnectionordevicecapability_worstCaseTransmissionTime_setter(instance):
    original = instance.worstCaseTransmissionTime
    instance.worstCaseTransmissionTime = original
    assert instance.worstCaseTransmissionTime == original

@given(instance=oaam_library_ResourceType_strategy)
@settings(max_examples=50)
def test_oaam_library_resourcetype_instantiation(instance):
    assert isinstance(instance, oaam_library_ResourceType)



@given(instance=oaam_library_ResourceType_strategy)
def test_oaam_library_resourcetype_isConfigurable_setter(instance):
    original = instance.isConfigurable
    instance.isConfigurable = original
    assert instance.isConfigurable == original



@given(instance=oaam_library_ResourceType_strategy)
def test_oaam_library_resourcetype_isIo_setter(instance):
    original = instance.isIo
    instance.isIo = original
    assert instance.isIo == original



@given(instance=oaam_library_ResourceType_strategy)
def test_oaam_library_resourcetype_isDistinguishable_setter(instance):
    original = instance.isDistinguishable
    instance.isDistinguishable = original
    assert instance.isDistinguishable == original



@given(instance=oaam_library_ResourceType_strategy)
def test_oaam_library_resourcetype_isPropagated_setter(instance):
    original = instance.isPropagated
    instance.isPropagated = original
    assert instance.isPropagated == original



@given(instance=oaam_library_ResourceType_strategy)
def test_oaam_library_resourcetype_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original



@given(instance=oaam_library_ResourceType_strategy)
def test_oaam_library_resourcetype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=oaam_library_ResourceType_strategy)
def test_oaam_library_resourcetype_isConsumed_setter(instance):
    original = instance.isConsumed
    instance.isConsumed = original
    assert instance.isConsumed == original

@given(instance=oaam_functions_FailureCondition_strategy)
@settings(max_examples=50)
def test_oaam_functions_failurecondition_instantiation(instance):
    assert isinstance(instance, oaam_functions_FailureCondition)



@given(instance=oaam_functions_FailureCondition_strategy)
def test_oaam_functions_failurecondition_noSingleFailure_setter(instance):
    original = instance.noSingleFailure
    instance.noSingleFailure = original
    assert instance.noSingleFailure == original



@given(instance=oaam_functions_FailureCondition_strategy)
def test_oaam_functions_failurecondition_maxOccurrenceProbability_setter(instance):
    original = instance.maxOccurrenceProbability
    instance.maxOccurrenceProbability = original
    assert instance.maxOccurrenceProbability == original

@given(instance=oaam_capabilities_SignalInMessageCapability_strategy)
@settings(max_examples=50)
def test_oaam_capabilities_signalinmessagecapability_instantiation(instance):
    assert isinstance(instance, oaam_capabilities_SignalInMessageCapability)

@given(instance=common_BoolA_strategy)
@settings(max_examples=50)
def test_common_boola_instantiation(instance):
    assert isinstance(instance, common_BoolA)

@given(instance=oaam_library_TaskInputState_strategy)
@settings(max_examples=50)
def test_oaam_library_taskinputstate_instantiation(instance):
    assert isinstance(instance, oaam_library_TaskInputState)



@given(instance=oaam_library_TaskInputState_strategy)
def test_oaam_library_taskinputstate_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=oaam_functions_OutputIntegrityState_strategy)
@settings(max_examples=50)
def test_oaam_functions_outputintegritystate_instantiation(instance):
    assert isinstance(instance, oaam_functions_OutputIntegrityState)



@given(instance=oaam_functions_OutputIntegrityState_strategy)
def test_oaam_functions_outputintegritystate_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=oaam_library_TaskInputTrigger_strategy)
@settings(max_examples=50)
def test_oaam_library_taskinputtrigger_instantiation(instance):
    assert isinstance(instance, oaam_library_TaskInputTrigger)

@given(instance=oaam_common_BoolNot_strategy)
@settings(max_examples=50)
def test_oaam_common_boolnot_instantiation(instance):
    assert isinstance(instance, oaam_common_BoolNot)

@given(instance=oaam_common_BoolOperation_strategy)
@settings(max_examples=50)
def test_oaam_common_booloperation_instantiation(instance):
    assert isinstance(instance, oaam_common_BoolOperation)



@given(instance=oaam_common_BoolOperation_strategy)
def test_oaam_common_booloperation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=oaam_common_BoolA_strategy)
@settings(max_examples=50)
def test_oaam_common_boola_instantiation(instance):
    assert isinstance(instance, oaam_common_BoolA)

@given(instance=AttributeA_strategy)
@settings(max_examples=50)
def test_attributea_instantiation(instance):
    assert isinstance(instance, AttributeA)

@given(instance=oaam_common_AttributeNumeric_strategy)
@settings(max_examples=50)
def test_oaam_common_attributenumeric_instantiation(instance):
    assert isinstance(instance, oaam_common_AttributeNumeric)



@given(instance=oaam_common_AttributeNumeric_strategy)
def test_oaam_common_attributenumeric_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oaam_common_AttributeString_strategy)
@settings(max_examples=50)
def test_oaam_common_attributestring_instantiation(instance):
    assert isinstance(instance, oaam_common_AttributeString)



@given(instance=oaam_common_AttributeString_strategy)
def test_oaam_common_attributestring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oaam_common_AttributeReference_strategy)
@settings(max_examples=50)
def test_oaam_common_attributereference_instantiation(instance):
    assert isinstance(instance, oaam_common_AttributeReference)

@given(instance=oaam_common_AttributeContainment_strategy)
@settings(max_examples=50)
def test_oaam_common_attributecontainment_instantiation(instance):
    assert isinstance(instance, oaam_common_AttributeContainment)

@given(instance=Allocations_strategy)
@settings(max_examples=50)
def test_allocations_instantiation(instance):
    assert isinstance(instance, Allocations)

@given(instance=Restrictions_strategy)
@settings(max_examples=50)
def test_restrictions_instantiation(instance):
    assert isinstance(instance, Restrictions)

@given(instance=Capabilities_strategy)
@settings(max_examples=50)
def test_capabilities_instantiation(instance):
    assert isinstance(instance, Capabilities)

@given(instance=Anatomy_strategy)
@settings(max_examples=50)
def test_anatomy_instantiation(instance):
    assert isinstance(instance, Anatomy)

@given(instance=Hardware_strategy)
@settings(max_examples=50)
def test_hardware_instantiation(instance):
    assert isinstance(instance, Hardware)

@given(instance=Functions_strategy)
@settings(max_examples=50)
def test_functions_instantiation(instance):
    assert isinstance(instance, Functions)

@given(instance=oaam_common_OaamBaseElementA_strategy)
@settings(max_examples=50)
def test_oaam_common_oaambaseelementa_instantiation(instance):
    assert isinstance(instance, oaam_common_OaamBaseElementA)



@given(instance=oaam_common_OaamBaseElementA_strategy)
def test_oaam_common_oaambaseelementa_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=oaam_common_OaamBaseElementA_strategy)
def test_oaam_common_oaambaseelementa_traceLink_setter(instance):
    original = instance.traceLink
    instance.traceLink = original
    assert instance.traceLink == original



@given(instance=oaam_common_OaamBaseElementA_strategy)
def test_oaam_common_oaambaseelementa_modified_setter(instance):
    original = instance.modified
    instance.modified = original
    assert instance.modified == original



@given(instance=oaam_common_OaamBaseElementA_strategy)
def test_oaam_common_oaambaseelementa_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original



@given(instance=oaam_common_OaamBaseElementA_strategy)
def test_oaam_common_oaambaseelementa_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original



@given(instance=oaam_common_OaamBaseElementA_strategy)
def test_oaam_common_oaambaseelementa_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=oaam_common_OaamBaseElementA_strategy)
def test_oaam_common_oaambaseelementa_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Library_strategy)
@settings(max_examples=50)
def test_library_instantiation(instance):
    assert isinstance(instance, Library)

@given(instance=OaamBaseElementA_strategy)
@settings(max_examples=50)
def test_oaambaseelementa_instantiation(instance):
    assert isinstance(instance, OaamBaseElementA)

@given(instance=oaam_library_PowerSource_strategy)
@settings(max_examples=50)
def test_oaam_library_powersource_instantiation(instance):
    assert isinstance(instance, oaam_library_PowerSource)

@given(instance=oaam_library_DeviceTypeDissimilarity_strategy)
@settings(max_examples=50)
def test_oaam_library_devicetypedissimilarity_instantiation(instance):
    assert isinstance(instance, oaam_library_DeviceTypeDissimilarity)



@given(instance=oaam_library_DeviceTypeDissimilarity_strategy)
def test_oaam_library_devicetypedissimilarity_percentageOfCommonHardware_setter(instance):
    original = instance.percentageOfCommonHardware
    instance.percentageOfCommonHardware = original
    assert instance.percentageOfCommonHardware == original

@given(instance=oaam_library_Resource_strategy)
@settings(max_examples=50)
def test_oaam_library_resource_instantiation(instance):
    assert isinstance(instance, oaam_library_Resource)



@given(instance=oaam_library_Resource_strategy)
def test_oaam_library_resource_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=oaam_library_ResourceTypeModifier_strategy)
@settings(max_examples=50)
def test_oaam_library_resourcetypemodifier_instantiation(instance):
    assert isinstance(instance, oaam_library_ResourceTypeModifier)

@given(instance=oaam_library_IoGroup_strategy)
@settings(max_examples=50)
def test_oaam_library_iogroup_instantiation(instance):
    assert isinstance(instance, oaam_library_IoGroup)

@given(instance=oaam_systems_SystemsContainerA_strategy)
@settings(max_examples=50)
def test_oaam_systems_systemscontainera_instantiation(instance):
    assert isinstance(instance, oaam_systems_SystemsContainerA)

@given(instance=oaam_hardware_HardwareContainerA_strategy)
@settings(max_examples=50)
def test_oaam_hardware_hardwarecontainera_instantiation(instance):
    assert isinstance(instance, oaam_hardware_HardwareContainerA)

@given(instance=oaam_scenario_ScenarioContainerA_strategy)
@settings(max_examples=50)
def test_oaam_scenario_scenariocontainera_instantiation(instance):
    assert isinstance(instance, oaam_scenario_ScenarioContainerA)

@given(instance=oaam_scenario_OperationModeReference_strategy)
@settings(max_examples=50)
def test_oaam_scenario_operationmodereference_instantiation(instance):
    assert isinstance(instance, oaam_scenario_OperationModeReference)



@given(instance=oaam_scenario_OperationModeReference_strategy)
def test_oaam_scenario_operationmodereference_activeProbability_setter(instance):
    original = instance.activeProbability
    instance.activeProbability = original
    assert instance.activeProbability == original

@given(instance=oaam_systems_InputSegregation_strategy)
@settings(max_examples=50)
def test_oaam_systems_inputsegregation_instantiation(instance):
    assert isinstance(instance, oaam_systems_InputSegregation)



@given(instance=oaam_systems_InputSegregation_strategy)
def test_oaam_systems_inputsegregation_dissimilarSource_setter(instance):
    original = instance.dissimilarSource
    instance.dissimilarSource = original
    assert instance.dissimilarSource == original



@given(instance=oaam_systems_InputSegregation_strategy)
def test_oaam_systems_inputsegregation_dissimilarTechnology_setter(instance):
    original = instance.dissimilarTechnology
    instance.dissimilarTechnology = original
    assert instance.dissimilarTechnology == original



@given(instance=oaam_systems_InputSegregation_strategy)
def test_oaam_systems_inputsegregation_dissimilarRoute_setter(instance):
    original = instance.dissimilarRoute
    instance.dissimilarRoute = original
    assert instance.dissimilarRoute == original

@given(instance=oaam_restrictions_RestrictionsContainerA_strategy)
@settings(max_examples=50)
def test_oaam_restrictions_restrictionscontainera_instantiation(instance):
    assert isinstance(instance, oaam_restrictions_RestrictionsContainerA)

@given(instance=oaam_library_ResourceAlternatives_strategy)
@settings(max_examples=50)
def test_oaam_library_resourcealternatives_instantiation(instance):
    assert isinstance(instance, oaam_library_ResourceAlternatives)

@given(instance=oaam_library_DuctOpeningDeclaration_strategy)
@settings(max_examples=50)
def test_oaam_library_ductopeningdeclaration_instantiation(instance):
    assert isinstance(instance, oaam_library_DuctOpeningDeclaration)

@given(instance=oaam_common_DataTypeA_strategy)
@settings(max_examples=50)
def test_oaam_common_datatypea_instantiation(instance):
    assert isinstance(instance, oaam_common_DataTypeA)

@given(instance=oaam_library_TaskOutputTrigger_strategy)
@settings(max_examples=50)
def test_oaam_library_taskoutputtrigger_instantiation(instance):
    assert isinstance(instance, oaam_library_TaskOutputTrigger)



@given(instance=oaam_library_TaskOutputTrigger_strategy)
def test_oaam_library_taskoutputtrigger_isFixedRate_setter(instance):
    original = instance.isFixedRate
    instance.isFixedRate = original
    assert instance.isFixedRate == original



@given(instance=oaam_library_TaskOutputTrigger_strategy)
def test_oaam_library_taskoutputtrigger_fixedRate_setter(instance):
    original = instance.fixedRate
    instance.fixedRate = original
    assert instance.fixedRate == original

@given(instance=oaam_library_ResourceTypeDissimilarity_strategy)
@settings(max_examples=50)
def test_oaam_library_resourcetypedissimilarity_instantiation(instance):
    assert isinstance(instance, oaam_library_ResourceTypeDissimilarity)

@given(instance=oaam_library_ResourceTypeModifierReference_strategy)
@settings(max_examples=50)
def test_oaam_library_resourcetypemodifierreference_instantiation(instance):
    assert isinstance(instance, oaam_library_ResourceTypeModifierReference)

@given(instance=oaam_capabilities_CapabilitiesContainerA_strategy)
@settings(max_examples=50)
def test_oaam_capabilities_capabilitiescontainera_instantiation(instance):
    assert isinstance(instance, oaam_capabilities_CapabilitiesContainerA)

@given(instance=oaam_library_ResourceLink_strategy)
@settings(max_examples=50)
def test_oaam_library_resourcelink_instantiation(instance):
    assert isinstance(instance, oaam_library_ResourceLink)

@given(instance=oaam_library_DeviceTypeSymmetry_strategy)
@settings(max_examples=50)
def test_oaam_library_devicetypesymmetry_instantiation(instance):
    assert isinstance(instance, oaam_library_DeviceTypeSymmetry)

@given(instance=oaam_library_WireType_strategy)
@settings(max_examples=50)
def test_oaam_library_wiretype_instantiation(instance):
    assert isinstance(instance, oaam_library_WireType)



@given(instance=oaam_library_WireType_strategy)
def test_oaam_library_wiretype_nConductors_setter(instance):
    original = instance.nConductors
    instance.nConductors = original
    assert instance.nConductors == original



@given(instance=oaam_library_WireType_strategy)
def test_oaam_library_wiretype_mtbf_setter(instance):
    original = instance.mtbf
    instance.mtbf = original
    assert instance.mtbf == original



@given(instance=oaam_library_WireType_strategy)
def test_oaam_library_wiretype_specificPrice_setter(instance):
    original = instance.specificPrice
    instance.specificPrice = original
    assert instance.specificPrice == original



@given(instance=oaam_library_WireType_strategy)
def test_oaam_library_wiretype_specificWeight_setter(instance):
    original = instance.specificWeight
    instance.specificWeight = original
    assert instance.specificWeight == original



@given(instance=oaam_library_WireType_strategy)
def test_oaam_library_wiretype_nShields_setter(instance):
    original = instance.nShields
    instance.nShields = original
    assert instance.nShields == original



@given(instance=oaam_library_WireType_strategy)
def test_oaam_library_wiretype_minBendingRadius_setter(instance):
    original = instance.minBendingRadius
    instance.minBendingRadius = original
    assert instance.minBendingRadius == original

@given(instance=oaam_library_LibraryContainerA_strategy)
@settings(max_examples=50)
def test_oaam_library_librarycontainera_instantiation(instance):
    assert isinstance(instance, oaam_library_LibraryContainerA)

@given(instance=oaam_library_TaskTypeDissimilarity_strategy)
@settings(max_examples=50)
def test_oaam_library_tasktypedissimilarity_instantiation(instance):
    assert isinstance(instance, oaam_library_TaskTypeDissimilarity)



@given(instance=oaam_library_TaskTypeDissimilarity_strategy)
def test_oaam_library_tasktypedissimilarity_percentageOfCommonCode_setter(instance):
    original = instance.percentageOfCommonCode
    instance.percentageOfCommonCode = original
    assert instance.percentageOfCommonCode == original

@given(instance=oaam_library_InputDeclaration_strategy)
@settings(max_examples=50)
def test_oaam_library_inputdeclaration_instantiation(instance):
    assert isinstance(instance, oaam_library_InputDeclaration)



@given(instance=oaam_library_InputDeclaration_strategy)
def test_oaam_library_inputdeclaration_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original



@given(instance=oaam_library_InputDeclaration_strategy)
def test_oaam_library_inputdeclaration_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original



@given(instance=oaam_library_InputDeclaration_strategy)
def test_oaam_library_inputdeclaration_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original



@given(instance=oaam_library_InputDeclaration_strategy)
def test_oaam_library_inputdeclaration_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=oaam_library_InputDeclaration_strategy)
def test_oaam_library_inputdeclaration_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original

@given(instance=oaam_library_FaultPropagation_strategy)
@settings(max_examples=50)
def test_oaam_library_faultpropagation_instantiation(instance):
    assert isinstance(instance, oaam_library_FaultPropagation)



@given(instance=oaam_library_FaultPropagation_strategy)
def test_oaam_library_faultpropagation_outputState_setter(instance):
    original = instance.outputState
    instance.outputState = original
    assert instance.outputState == original

@given(instance=oaam_common_AttributeA_strategy)
@settings(max_examples=50)
def test_oaam_common_attributea_instantiation(instance):
    assert isinstance(instance, oaam_common_AttributeA)

@given(instance=oaam_allocations_AllocationsContainerA_strategy)
@settings(max_examples=50)
def test_oaam_allocations_allocationscontainera_instantiation(instance):
    assert isinstance(instance, oaam_allocations_AllocationsContainerA)

@given(instance=oaam_anatomy_AnatomyContainerA_strategy)
@settings(max_examples=50)
def test_oaam_anatomy_anatomycontainera_instantiation(instance):
    assert isinstance(instance, oaam_anatomy_AnatomyContainerA)

@given(instance=oaam_functions_TaskParameter_strategy)
@settings(max_examples=50)
def test_oaam_functions_taskparameter_instantiation(instance):
    assert isinstance(instance, oaam_functions_TaskParameter)



@given(instance=oaam_functions_TaskParameter_strategy)
def test_oaam_functions_taskparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oaam_library_AttributeDefinition_strategy)
@settings(max_examples=50)
def test_oaam_library_attributedefinition_instantiation(instance):
    assert isinstance(instance, oaam_library_AttributeDefinition)



@given(instance=oaam_library_AttributeDefinition_strategy)
def test_oaam_library_attributedefinition_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=oaam_library_AttributeDefinition_strategy)
def test_oaam_library_attributedefinition_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=oaam_library_IoDeclaration_strategy)
@settings(max_examples=50)
def test_oaam_library_iodeclaration_instantiation(instance):
    assert isinstance(instance, oaam_library_IoDeclaration)

@given(instance=oaam_library_TaskParameterDeclaration_strategy)
@settings(max_examples=50)
def test_oaam_library_taskparameterdeclaration_instantiation(instance):
    assert isinstance(instance, oaam_library_TaskParameterDeclaration)

@given(instance=oaam_capabilities_ResourceConsumption_strategy)
@settings(max_examples=50)
def test_oaam_capabilities_resourceconsumption_instantiation(instance):
    assert isinstance(instance, oaam_capabilities_ResourceConsumption)



@given(instance=oaam_capabilities_ResourceConsumption_strategy)
def test_oaam_capabilities_resourceconsumption_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=oaam_library_ResourceGroup_strategy)
@settings(max_examples=50)
def test_oaam_library_resourcegroup_instantiation(instance):
    assert isinstance(instance, oaam_library_ResourceGroup)

@given(instance=oaam_library_OutputDeclaration_strategy)
@settings(max_examples=50)
def test_oaam_library_outputdeclaration_instantiation(instance):
    assert isinstance(instance, oaam_library_OutputDeclaration)



@given(instance=oaam_library_OutputDeclaration_strategy)
def test_oaam_library_outputdeclaration_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=oaam_library_OutputDeclaration_strategy)
def test_oaam_library_outputdeclaration_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original



@given(instance=oaam_library_OutputDeclaration_strategy)
def test_oaam_library_outputdeclaration_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original



@given(instance=oaam_library_OutputDeclaration_strategy)
def test_oaam_library_outputdeclaration_postcondition_setter(instance):
    original = instance.postcondition
    instance.postcondition = original
    assert instance.postcondition == original



@given(instance=oaam_library_OutputDeclaration_strategy)
def test_oaam_library_outputdeclaration_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=oaam_library_TaskStateDeclaration_strategy)
@settings(max_examples=50)
def test_oaam_library_taskstatedeclaration_instantiation(instance):
    assert isinstance(instance, oaam_library_TaskStateDeclaration)

@given(instance=oaam_library_IoType_strategy)
@settings(max_examples=50)
def test_oaam_library_iotype_instantiation(instance):
    assert isinstance(instance, oaam_library_IoType)



@given(instance=oaam_library_IoType_strategy)
def test_oaam_library_iotype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=oaam_Architecture_strategy)
@settings(max_examples=50)
def test_oaam_architecture_instantiation(instance):
    assert isinstance(instance, oaam_Architecture)

@given(instance=Systems_strategy)
@settings(max_examples=50)
def test_systems_instantiation(instance):
    assert isinstance(instance, Systems)

@given(instance=Scenario_strategy)
@settings(max_examples=50)
def test_scenario_instantiation(instance):
    assert isinstance(instance, Scenario)
