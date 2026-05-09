import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    InputSegregation,
    InformationFlow,
    System,
    ScenarioContainerA,
    oaam::scenario::Subscenario,
    oaam::scenario::Scenario,
    ProvidedInformationA,
    systems::SystemsContainerA,
    SystemsContainerA,
    oaam::systems::Systems,
    scenario::ScenarioParameterA,
    Subscenario,
    OperationMode,
    scenario::VariantDependentElementA,
    scenario::ModeDependentElementA,
    oaam::systems::Subsystem,
    oaam::scenario::ScenarioParameterA,
    LibraryContainerA,
    oaam::library::Sublibrary,
    oaam::library::Library,
    ScenarioParameterA,
    Variant,
    oaam::scenario::VariantDependentElementA,
    OperationModeReference,
    oaam::scenario::ModeDependentElementA,
    oaam::allocations::SignalToMessageAssignment,
    allocations::AllocationsContainerA,
    oaam::allocations::Suballocations,
    AllocationsContainerA,
    oaam::allocations::Allocations,
    MessageSegment,
    SignalToMessageAssignment,
    Submessage,
    MessageA,
    oaam::allocations::Submessage,
    oaam::allocations::Message,
    ScheduledTime,
    ConnectionAssignmentSegment,
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
    restrictions::RestrictionsContainerA,
    oaam::restrictions::Subrestrictions,
    restrictions::ConnectionRestrinctionA,
    restrictions::DeviceRestrictionA,
    restrictions::SubfunctionRestrictionA,
    restrictions::SignalGroupRestrictionA,
    restrictions::SignalRestrictionA,
    restrictions::TaskGroupRestrictionA,
    restrictions::TaskRestrictionA,
    oaam::restrictions::SignalGroupRestrictionA,
    oaam::restrictions::TaskGroupRestrictionA,
    oaam::restrictions::SubfunctionRestrictionA,
    oaam::restrictions::DeviceRestrictionA,
    RestrictionsContainerA,
    oaam::restrictions::Restrictions,
    TimeDelayRestriction,
    Subrestrictions,
    SegregationRestriction,
    ConnectionTypeRestriction,
    ConnectionRestriction,
    oaam::restrictions::SignalRestrictionA,
    oaam::restrictions::TaskRestrictionA,
    oaam::restrictions::ConnectionRestrinctionA,
    PowerSourceRestriction,
    AreaRestriction,
    LocationRestriction,
    DeviceRestriction,
    DeviceTypeRestriction,
    SynchronicityRestriction,
    TaskSymmetryRestriction,
    TaskAtomicRestriction,
    capabilities::CapabilitiesContainerA,
    oaam::capabilities::Subcapabilities,
    CapabilitiesContainerA,
    oaam::capabilities::Capabilities,
    capabilities::CapabilityA,
    MessageOnConnectionOrDeviceCapability,
    Subcapabilities,
    ConnectionInDuctOrLocationCapability,
    SubdeviceInDeviceCapability,
    DeviceInLocationCapability,
    SignalOnConnectionOrDeviceCapability,
    TaskOnDeviceCapability,
    ResourceConsumption,
    oaam::capabilities::CapabilityA,
    SignalInMessageCapability,
    SubmessageInMessageCapability,
    MessageOnBusCapability,
    SubconnectionInDeviceCapability,
    AnatomyContainerA,
    oaam::anatomy::Anatomy,
    anatomy::AnatomyContainerA,
    oaam::anatomy::Subanatomy,
    DuctOpening,
    Area,
    Duct,
    LocationSymmetry,
    Position3D,
    AreaSymmetry,
    Subanatomy,
    hardware::HardwareContainerA,
    oaam::hardware::Subhardware,
    oaam::hardware::Hardware,
    library::ResourceProviderInstanceA,
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
    oaam::functions::Subfunctions,
    oaam::functions::Functions,
    SignalGroup,
    Signal,
    TaskRedundancy,
    TaskSymmetry,
    TaskGroup,
    InformationPower,
    oaam::systems::HydraulicPower,
    oaam::systems::RotaryPower,
    oaam::systems::ElectricPower,
    oaam::systems::LinearPower,
    systems::RequiredInformationA,
    systems::ProvidedInformationA,
    oaam::systems::ProvidedInformationA,
    oaam::systems::RequiredInformationA,
    RequiredInformationA,
    Subsystem,
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
    library::ResourceProviderA,
    ResourceAlternatives,
    ResourceTypeModifierReference,
    library::ResourceConsumerA,
    MessageType,
    BusType,
    IoType,
    LocationType,
    WireType,
    ConnectionType,
    DeviceTypeDissimilarity,
    Sublibrary,
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
    oaam::library::ResourceProviderInstanceA,
    ResourceLink,
    ResourceType,
    ResourceBundle,
    oaam::library::ResourceProviderA,
    oaam::library::ResourceConsumerA,
    ResourceGroup,
    Resource,
    Struct,
    DataTypeA,
    oaam::common::FloatingPoint,
    oaam::common::Character,
    oaam::common::Byte,
    oaam::common::Boolean,
    oaam::common::Struct,
    oaam::common::Array,
    oaam::common::Integer,
    BoolA,
    common::OaamBaseElementA,
    oaam::capabilities::TaskOnDeviceCapability,
    oaam::library::MessageType,
    oaam::anatomy::Duct,
    oaam::hardware::DeviceSymmetry,
    oaam::restrictions::AreaRestriction,
    oaam::anatomy::AreaSymmetry,
    oaam::anatomy::Area,
    oaam::library::ResourceType,
    oaam::restrictions::TaskAtomicRestriction,
    oaam::restrictions::LocationRestriction,
    oaam::allocations::SignalAssignmentSegment,
    oaam::systems::InformationMaterial,
    oaam::functions::TaskGroup,
    oaam::functions::Task,
    oaam::capabilities::SubconnectionInDeviceCapability,
    oaam::allocations::ScheduledTime,
    oaam::library::SignalType,
    oaam::capabilities::DeviceInLocationCapability,
    oaam::library::TaskType,
    oaam::capabilities::MessageOnBusCapability,
    oaam::allocations::ConnectionAssignment,
    oaam::allocations::DeviceAssignment,
    oaam::capabilities::SubmessageInMessageCapability,
    oaam::functions::Output,
    oaam::hardware::Io,
    oaam::scenario::Variant,
    oaam::functions::ExternalTaskLink,
    oaam::capabilities::ConnectionInDuctOrLocationCapability,
    oaam::allocations::MessageSegment,
    oaam::functions::TaskSymmetry,
    oaam::allocations::SubconnectionAssignment,
    oaam::scenario::ScenarioParameterBool,
    oaam::allocations::TaskAssignment,
    oaam::functions::Signal,
    oaam::functions::ExternalOutputLink,
    oaam::hardware::Bus,
    oaam::hardware::Connection,
    oaam::functions::TaskRedundancy,
    oaam::library::BusType,
    oaam::library::LocationType,
    oaam::capabilities::SignalInMessageCapability,
    oaam::anatomy::LocationSymmetry,
    oaam::allocations::MessageA,
    oaam::anatomy::Location,
    oaam::functions::FunctionsContainerA,
    oaam::library::DeviceType,
    oaam::restrictions::SegregationRestriction,
    oaam::scenario::ScenarioParameterNumeric,
    oaam::library::ResourceTypeModifierLevel,
    oaam::restrictions::DeviceTypeRestriction,
    oaam::restrictions::ConnectionTypeRestriction,
    oaam::scenario::OperationMode,
    oaam::hardware::Device,
    oaam::restrictions::DeviceRestriction,
    oaam::allocations::Schedule,
    oaam::systems::InformationPower,
    oaam::restrictions::TimeDelayRestriction,
    oaam::library::ResourceBundle,
    oaam::library::DuctType,
    oaam::restrictions::PowerSourceRestriction,
    oaam::capabilities::SignalOnConnectionOrDeviceCapability,
    oaam::functions::Input,
    oaam::systems::System,
    oaam::anatomy::DuctOpening,
    oaam::allocations::ConnectionAssignmentSegment,
    oaam::functions::FailureCondition,
    oaam::restrictions::TaskSymmetryRestriction,
    oaam::allocations::SubdeviceAssignment,
    oaam::library::ConnectionType,
    oaam::anatomy::Position3D,
    oaam::restrictions::SynchronicityRestriction,
    oaam::restrictions::ConnectionRestriction,
    oaam::systems::InformationFlow,
    oaam::capabilities::SubdeviceInDeviceCapability,
    oaam::systems::InformationSignal,
    oaam::allocations::SignalAssignment,
    oaam::capabilities::MessageOnConnectionOrDeviceCapability,
    oaam::functions::SignalGroup,
    common::BoolA,
    oaam::library::TaskInputState,
    oaam::functions::OutputIntegrityState,
    oaam::common::BoolNot,
    oaam::library::TaskInputTrigger,
    oaam::common::BoolOperation,
    oaam::common::BoolA,
    AttributeA,
    oaam::common::AttributeReference,
    oaam::common::AttributeNumeric,
    oaam::common::AttributeString,
    oaam::common::AttributeContainment,
    Allocations,
    Restrictions,
    Capabilities,
    Anatomy,
    Hardware,
    Functions,
    oaam::common::OaamBaseElementA,
    Library,
    OaamBaseElementA,
    oaam::library::ResourceTypeModifier,
    oaam::library::TaskStateDeclaration,
    oaam::library::DuctOpeningDeclaration,
    oaam::library::ResourceGroup,
    oaam::scenario::ScenarioContainerA,
    oaam::library::DeviceTypeDissimilarity,
    oaam::common::AttributeA,
    oaam::library::WireType,
    oaam::library::InputDeclaration,
    oaam::library::LibraryContainerA,
    oaam::library::AttributeDefinition,
    oaam::library::ResourceLink,
    oaam::library::IoDeclaration,
    oaam::library::ResourceTypeModifierReference,
    oaam::systems::InputSegregation,
    oaam::functions::TaskParameter,
    oaam::library::FaultPropagation,
    oaam::library::Resource,
    oaam::systems::SystemsContainerA,
    oaam::hardware::HardwareContainerA,
    oaam::restrictions::RestrictionsContainerA,
    oaam::capabilities::CapabilitiesContainerA,
    oaam::library::TaskTypeDissimilarity,
    oaam::scenario::OperationModeReference,
    oaam::allocations::AllocationsContainerA,
    oaam::capabilities::ResourceConsumption,
    oaam::library::IoGroup,
    oaam::library::OutputDeclaration,
    oaam::library::ResourceAlternatives,
    oaam::library::TaskOutputTrigger,
    oaam::library::IoType,
    oaam::library::PowerSource,
    oaam::library::DeviceTypeSymmetry,
    oaam::common::DataTypeA,
    oaam::library::TaskParameterDeclaration,
    oaam::library::ResourceTypeDissimilarity,
    oaam::anatomy::AnatomyContainerA,
    oaam::Architecture,
    Systems,
    Scenario,
    SymmetryTypesE,
    IoDirectionE,
    BoolOperationTypesE,
    AttributeTargetsE,
    AttributeTypesE,
    IntegretyStateE,
    EndianessE,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_oaam::scenario::subscenario_is_not_abstract():
    assert not inspect.isabstract(oaam::scenario::Subscenario)


def test_oaam::scenario::subscenario_constructor_exists():
    assert callable(oaam::scenario::Subscenario.__init__)


def test_oaam::scenario::subscenario_constructor_args():
    sig = inspect.signature(oaam::scenario::Subscenario.__init__)
    params = list(sig.parameters.keys())



def test_oaam::scenario::scenario_is_not_abstract():
    assert not inspect.isabstract(oaam::scenario::Scenario)


def test_oaam::scenario::scenario_constructor_exists():
    assert callable(oaam::scenario::Scenario.__init__)


def test_oaam::scenario::scenario_constructor_args():
    sig = inspect.signature(oaam::scenario::Scenario.__init__)
    params = list(sig.parameters.keys())



def test_providedinformationa_is_not_abstract():
    assert not inspect.isabstract(ProvidedInformationA)


def test_providedinformationa_constructor_exists():
    assert callable(ProvidedInformationA.__init__)


def test_providedinformationa_constructor_args():
    sig = inspect.signature(ProvidedInformationA.__init__)
    params = list(sig.parameters.keys())



def test_systems::systemscontainera_is_not_abstract():
    assert not inspect.isabstract(systems::SystemsContainerA)


def test_systems::systemscontainera_constructor_exists():
    assert callable(systems::SystemsContainerA.__init__)


def test_systems::systemscontainera_constructor_args():
    sig = inspect.signature(systems::SystemsContainerA.__init__)
    params = list(sig.parameters.keys())



def test_systemscontainera_is_not_abstract():
    assert not inspect.isabstract(SystemsContainerA)


def test_systemscontainera_constructor_exists():
    assert callable(SystemsContainerA.__init__)


def test_systemscontainera_constructor_args():
    sig = inspect.signature(SystemsContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::systems::systems_is_not_abstract():
    assert not inspect.isabstract(oaam::systems::Systems)


def test_oaam::systems::systems_constructor_exists():
    assert callable(oaam::systems::Systems.__init__)


def test_oaam::systems::systems_constructor_args():
    sig = inspect.signature(oaam::systems::Systems.__init__)
    params = list(sig.parameters.keys())



def test_scenario::scenarioparametera_is_not_abstract():
    assert not inspect.isabstract(scenario::ScenarioParameterA)


def test_scenario::scenarioparametera_constructor_exists():
    assert callable(scenario::ScenarioParameterA.__init__)


def test_scenario::scenarioparametera_constructor_args():
    sig = inspect.signature(scenario::ScenarioParameterA.__init__)
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



def test_scenario::variantdependentelementa_is_not_abstract():
    assert not inspect.isabstract(scenario::VariantDependentElementA)


def test_scenario::variantdependentelementa_constructor_exists():
    assert callable(scenario::VariantDependentElementA.__init__)


def test_scenario::variantdependentelementa_constructor_args():
    sig = inspect.signature(scenario::VariantDependentElementA.__init__)
    params = list(sig.parameters.keys())



def test_scenario::modedependentelementa_is_not_abstract():
    assert not inspect.isabstract(scenario::ModeDependentElementA)


def test_scenario::modedependentelementa_constructor_exists():
    assert callable(scenario::ModeDependentElementA.__init__)


def test_scenario::modedependentelementa_constructor_args():
    sig = inspect.signature(scenario::ModeDependentElementA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::systems::subsystem_is_not_abstract():
    assert not inspect.isabstract(oaam::systems::Subsystem)


def test_oaam::systems::subsystem_constructor_exists():
    assert callable(oaam::systems::Subsystem.__init__)


def test_oaam::systems::subsystem_constructor_args():
    sig = inspect.signature(oaam::systems::Subsystem.__init__)
    params = list(sig.parameters.keys())



def test_oaam::scenario::scenarioparametera_is_not_abstract():
    assert not inspect.isabstract(oaam::scenario::ScenarioParameterA)


def test_oaam::scenario::scenarioparametera_constructor_exists():
    assert callable(oaam::scenario::ScenarioParameterA.__init__)


def test_oaam::scenario::scenarioparametera_constructor_args():
    sig = inspect.signature(oaam::scenario::ScenarioParameterA.__init__)
    params = list(sig.parameters.keys())



def test_librarycontainera_is_not_abstract():
    assert not inspect.isabstract(LibraryContainerA)


def test_librarycontainera_constructor_exists():
    assert callable(LibraryContainerA.__init__)


def test_librarycontainera_constructor_args():
    sig = inspect.signature(LibraryContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::sublibrary_is_not_abstract():
    assert not inspect.isabstract(oaam::library::Sublibrary)


def test_oaam::library::sublibrary_constructor_exists():
    assert callable(oaam::library::Sublibrary.__init__)


def test_oaam::library::sublibrary_constructor_args():
    sig = inspect.signature(oaam::library::Sublibrary.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::library_is_not_abstract():
    assert not inspect.isabstract(oaam::library::Library)


def test_oaam::library::library_constructor_exists():
    assert callable(oaam::library::Library.__init__)


def test_oaam::library::library_constructor_args():
    sig = inspect.signature(oaam::library::Library.__init__)
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



def test_oaam::scenario::variantdependentelementa_is_not_abstract():
    assert not inspect.isabstract(oaam::scenario::VariantDependentElementA)


def test_oaam::scenario::variantdependentelementa_constructor_exists():
    assert callable(oaam::scenario::VariantDependentElementA.__init__)


def test_oaam::scenario::variantdependentelementa_constructor_args():
    sig = inspect.signature(oaam::scenario::VariantDependentElementA.__init__)
    params = list(sig.parameters.keys())



def test_operationmodereference_is_not_abstract():
    assert not inspect.isabstract(OperationModeReference)


def test_operationmodereference_constructor_exists():
    assert callable(OperationModeReference.__init__)


def test_operationmodereference_constructor_args():
    sig = inspect.signature(OperationModeReference.__init__)
    params = list(sig.parameters.keys())



def test_oaam::scenario::modedependentelementa_is_not_abstract():
    assert not inspect.isabstract(oaam::scenario::ModeDependentElementA)


def test_oaam::scenario::modedependentelementa_constructor_exists():
    assert callable(oaam::scenario::ModeDependentElementA.__init__)


def test_oaam::scenario::modedependentelementa_constructor_args():
    sig = inspect.signature(oaam::scenario::ModeDependentElementA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::allocations::signaltomessageassignment_is_not_abstract():
    assert not inspect.isabstract(oaam::allocations::SignalToMessageAssignment)


def test_oaam::allocations::signaltomessageassignment_constructor_exists():
    assert callable(oaam::allocations::SignalToMessageAssignment.__init__)


def test_oaam::allocations::signaltomessageassignment_constructor_args():
    sig = inspect.signature(oaam::allocations::SignalToMessageAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_oaam::allocations::signaltomessageassignment_has_position():
    assert hasattr(oaam::allocations::SignalToMessageAssignment, "position")
    descriptor = None
    for klass in oaam::allocations::SignalToMessageAssignment.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_allocations::allocationscontainera_is_not_abstract():
    assert not inspect.isabstract(allocations::AllocationsContainerA)


def test_allocations::allocationscontainera_constructor_exists():
    assert callable(allocations::AllocationsContainerA.__init__)


def test_allocations::allocationscontainera_constructor_args():
    sig = inspect.signature(allocations::AllocationsContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::allocations::suballocations_is_not_abstract():
    assert not inspect.isabstract(oaam::allocations::Suballocations)


def test_oaam::allocations::suballocations_constructor_exists():
    assert callable(oaam::allocations::Suballocations.__init__)


def test_oaam::allocations::suballocations_constructor_args():
    sig = inspect.signature(oaam::allocations::Suballocations.__init__)
    params = list(sig.parameters.keys())



def test_allocationscontainera_is_not_abstract():
    assert not inspect.isabstract(AllocationsContainerA)


def test_allocationscontainera_constructor_exists():
    assert callable(AllocationsContainerA.__init__)


def test_allocationscontainera_constructor_args():
    sig = inspect.signature(AllocationsContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::allocations::allocations_is_not_abstract():
    assert not inspect.isabstract(oaam::allocations::Allocations)


def test_oaam::allocations::allocations_constructor_exists():
    assert callable(oaam::allocations::Allocations.__init__)


def test_oaam::allocations::allocations_constructor_args():
    sig = inspect.signature(oaam::allocations::Allocations.__init__)
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



def test_oaam::allocations::submessage_is_not_abstract():
    assert not inspect.isabstract(oaam::allocations::Submessage)


def test_oaam::allocations::submessage_constructor_exists():
    assert callable(oaam::allocations::Submessage.__init__)


def test_oaam::allocations::submessage_constructor_args():
    sig = inspect.signature(oaam::allocations::Submessage.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_oaam::allocations::submessage_has_position():
    assert hasattr(oaam::allocations::Submessage, "position")
    descriptor = None
    for klass in oaam::allocations::Submessage.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_oaam::allocations::message_is_not_abstract():
    assert not inspect.isabstract(oaam::allocations::Message)


def test_oaam::allocations::message_constructor_exists():
    assert callable(oaam::allocations::Message.__init__)


def test_oaam::allocations::message_constructor_args():
    sig = inspect.signature(oaam::allocations::Message.__init__)
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



def test_restrictions::restrictionscontainera_is_not_abstract():
    assert not inspect.isabstract(restrictions::RestrictionsContainerA)


def test_restrictions::restrictionscontainera_constructor_exists():
    assert callable(restrictions::RestrictionsContainerA.__init__)


def test_restrictions::restrictionscontainera_constructor_args():
    sig = inspect.signature(restrictions::RestrictionsContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::restrictions::subrestrictions_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::Subrestrictions)


def test_oaam::restrictions::subrestrictions_constructor_exists():
    assert callable(oaam::restrictions::Subrestrictions.__init__)


def test_oaam::restrictions::subrestrictions_constructor_args():
    sig = inspect.signature(oaam::restrictions::Subrestrictions.__init__)
    params = list(sig.parameters.keys())



def test_restrictions::connectionrestrinctiona_is_not_abstract():
    assert not inspect.isabstract(restrictions::ConnectionRestrinctionA)


def test_restrictions::connectionrestrinctiona_constructor_exists():
    assert callable(restrictions::ConnectionRestrinctionA.__init__)


def test_restrictions::connectionrestrinctiona_constructor_args():
    sig = inspect.signature(restrictions::ConnectionRestrinctionA.__init__)
    params = list(sig.parameters.keys())



def test_restrictions::devicerestrictiona_is_not_abstract():
    assert not inspect.isabstract(restrictions::DeviceRestrictionA)


def test_restrictions::devicerestrictiona_constructor_exists():
    assert callable(restrictions::DeviceRestrictionA.__init__)


def test_restrictions::devicerestrictiona_constructor_args():
    sig = inspect.signature(restrictions::DeviceRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_restrictions::subfunctionrestrictiona_is_not_abstract():
    assert not inspect.isabstract(restrictions::SubfunctionRestrictionA)


def test_restrictions::subfunctionrestrictiona_constructor_exists():
    assert callable(restrictions::SubfunctionRestrictionA.__init__)


def test_restrictions::subfunctionrestrictiona_constructor_args():
    sig = inspect.signature(restrictions::SubfunctionRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_restrictions::signalgrouprestrictiona_is_not_abstract():
    assert not inspect.isabstract(restrictions::SignalGroupRestrictionA)


def test_restrictions::signalgrouprestrictiona_constructor_exists():
    assert callable(restrictions::SignalGroupRestrictionA.__init__)


def test_restrictions::signalgrouprestrictiona_constructor_args():
    sig = inspect.signature(restrictions::SignalGroupRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_restrictions::signalrestrictiona_is_not_abstract():
    assert not inspect.isabstract(restrictions::SignalRestrictionA)


def test_restrictions::signalrestrictiona_constructor_exists():
    assert callable(restrictions::SignalRestrictionA.__init__)


def test_restrictions::signalrestrictiona_constructor_args():
    sig = inspect.signature(restrictions::SignalRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_restrictions::taskgrouprestrictiona_is_not_abstract():
    assert not inspect.isabstract(restrictions::TaskGroupRestrictionA)


def test_restrictions::taskgrouprestrictiona_constructor_exists():
    assert callable(restrictions::TaskGroupRestrictionA.__init__)


def test_restrictions::taskgrouprestrictiona_constructor_args():
    sig = inspect.signature(restrictions::TaskGroupRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_restrictions::taskrestrictiona_is_not_abstract():
    assert not inspect.isabstract(restrictions::TaskRestrictionA)


def test_restrictions::taskrestrictiona_constructor_exists():
    assert callable(restrictions::TaskRestrictionA.__init__)


def test_restrictions::taskrestrictiona_constructor_args():
    sig = inspect.signature(restrictions::TaskRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::restrictions::signalgrouprestrictiona_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::SignalGroupRestrictionA)


def test_oaam::restrictions::signalgrouprestrictiona_constructor_exists():
    assert callable(oaam::restrictions::SignalGroupRestrictionA.__init__)


def test_oaam::restrictions::signalgrouprestrictiona_constructor_args():
    sig = inspect.signature(oaam::restrictions::SignalGroupRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::restrictions::taskgrouprestrictiona_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::TaskGroupRestrictionA)


def test_oaam::restrictions::taskgrouprestrictiona_constructor_exists():
    assert callable(oaam::restrictions::TaskGroupRestrictionA.__init__)


def test_oaam::restrictions::taskgrouprestrictiona_constructor_args():
    sig = inspect.signature(oaam::restrictions::TaskGroupRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::restrictions::subfunctionrestrictiona_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::SubfunctionRestrictionA)


def test_oaam::restrictions::subfunctionrestrictiona_constructor_exists():
    assert callable(oaam::restrictions::SubfunctionRestrictionA.__init__)


def test_oaam::restrictions::subfunctionrestrictiona_constructor_args():
    sig = inspect.signature(oaam::restrictions::SubfunctionRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::restrictions::devicerestrictiona_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::DeviceRestrictionA)


def test_oaam::restrictions::devicerestrictiona_constructor_exists():
    assert callable(oaam::restrictions::DeviceRestrictionA.__init__)


def test_oaam::restrictions::devicerestrictiona_constructor_args():
    sig = inspect.signature(oaam::restrictions::DeviceRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_restrictionscontainera_is_not_abstract():
    assert not inspect.isabstract(RestrictionsContainerA)


def test_restrictionscontainera_constructor_exists():
    assert callable(RestrictionsContainerA.__init__)


def test_restrictionscontainera_constructor_args():
    sig = inspect.signature(RestrictionsContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::restrictions::restrictions_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::Restrictions)


def test_oaam::restrictions::restrictions_constructor_exists():
    assert callable(oaam::restrictions::Restrictions.__init__)


def test_oaam::restrictions::restrictions_constructor_args():
    sig = inspect.signature(oaam::restrictions::Restrictions.__init__)
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



def test_oaam::restrictions::signalrestrictiona_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::SignalRestrictionA)


def test_oaam::restrictions::signalrestrictiona_constructor_exists():
    assert callable(oaam::restrictions::SignalRestrictionA.__init__)


def test_oaam::restrictions::signalrestrictiona_constructor_args():
    sig = inspect.signature(oaam::restrictions::SignalRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::restrictions::taskrestrictiona_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::TaskRestrictionA)


def test_oaam::restrictions::taskrestrictiona_constructor_exists():
    assert callable(oaam::restrictions::TaskRestrictionA.__init__)


def test_oaam::restrictions::taskrestrictiona_constructor_args():
    sig = inspect.signature(oaam::restrictions::TaskRestrictionA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::restrictions::connectionrestrinctiona_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::ConnectionRestrinctionA)


def test_oaam::restrictions::connectionrestrinctiona_constructor_exists():
    assert callable(oaam::restrictions::ConnectionRestrinctionA.__init__)


def test_oaam::restrictions::connectionrestrinctiona_constructor_args():
    sig = inspect.signature(oaam::restrictions::ConnectionRestrinctionA.__init__)
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



def test_capabilities::capabilitiescontainera_is_not_abstract():
    assert not inspect.isabstract(capabilities::CapabilitiesContainerA)


def test_capabilities::capabilitiescontainera_constructor_exists():
    assert callable(capabilities::CapabilitiesContainerA.__init__)


def test_capabilities::capabilitiescontainera_constructor_args():
    sig = inspect.signature(capabilities::CapabilitiesContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::capabilities::subcapabilities_is_not_abstract():
    assert not inspect.isabstract(oaam::capabilities::Subcapabilities)


def test_oaam::capabilities::subcapabilities_constructor_exists():
    assert callable(oaam::capabilities::Subcapabilities.__init__)


def test_oaam::capabilities::subcapabilities_constructor_args():
    sig = inspect.signature(oaam::capabilities::Subcapabilities.__init__)
    params = list(sig.parameters.keys())



def test_capabilitiescontainera_is_not_abstract():
    assert not inspect.isabstract(CapabilitiesContainerA)


def test_capabilitiescontainera_constructor_exists():
    assert callable(CapabilitiesContainerA.__init__)


def test_capabilitiescontainera_constructor_args():
    sig = inspect.signature(CapabilitiesContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::capabilities::capabilities_is_not_abstract():
    assert not inspect.isabstract(oaam::capabilities::Capabilities)


def test_oaam::capabilities::capabilities_constructor_exists():
    assert callable(oaam::capabilities::Capabilities.__init__)


def test_oaam::capabilities::capabilities_constructor_args():
    sig = inspect.signature(oaam::capabilities::Capabilities.__init__)
    params = list(sig.parameters.keys())



def test_capabilities::capabilitya_is_not_abstract():
    assert not inspect.isabstract(capabilities::CapabilityA)


def test_capabilities::capabilitya_constructor_exists():
    assert callable(capabilities::CapabilityA.__init__)


def test_capabilities::capabilitya_constructor_args():
    sig = inspect.signature(capabilities::CapabilityA.__init__)
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



def test_oaam::capabilities::capabilitya_is_not_abstract():
    assert not inspect.isabstract(oaam::capabilities::CapabilityA)


def test_oaam::capabilities::capabilitya_constructor_exists():
    assert callable(oaam::capabilities::CapabilityA.__init__)


def test_oaam::capabilities::capabilitya_constructor_args():
    sig = inspect.signature(oaam::capabilities::CapabilityA.__init__)
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



def test_oaam::anatomy::anatomy_is_not_abstract():
    assert not inspect.isabstract(oaam::anatomy::Anatomy)


def test_oaam::anatomy::anatomy_constructor_exists():
    assert callable(oaam::anatomy::Anatomy.__init__)


def test_oaam::anatomy::anatomy_constructor_args():
    sig = inspect.signature(oaam::anatomy::Anatomy.__init__)
    params = list(sig.parameters.keys())



def test_anatomy::anatomycontainera_is_not_abstract():
    assert not inspect.isabstract(anatomy::AnatomyContainerA)


def test_anatomy::anatomycontainera_constructor_exists():
    assert callable(anatomy::AnatomyContainerA.__init__)


def test_anatomy::anatomycontainera_constructor_args():
    sig = inspect.signature(anatomy::AnatomyContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::anatomy::subanatomy_is_not_abstract():
    assert not inspect.isabstract(oaam::anatomy::Subanatomy)


def test_oaam::anatomy::subanatomy_constructor_exists():
    assert callable(oaam::anatomy::Subanatomy.__init__)


def test_oaam::anatomy::subanatomy_constructor_args():
    sig = inspect.signature(oaam::anatomy::Subanatomy.__init__)
    params = list(sig.parameters.keys())



def test_ductopening_is_not_abstract():
    assert not inspect.isabstract(DuctOpening)


def test_ductopening_constructor_exists():
    assert callable(DuctOpening.__init__)


def test_ductopening_constructor_args():
    sig = inspect.signature(DuctOpening.__init__)
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



def test_hardware::hardwarecontainera_is_not_abstract():
    assert not inspect.isabstract(hardware::HardwareContainerA)


def test_hardware::hardwarecontainera_constructor_exists():
    assert callable(hardware::HardwareContainerA.__init__)


def test_hardware::hardwarecontainera_constructor_args():
    sig = inspect.signature(hardware::HardwareContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::hardware::subhardware_is_not_abstract():
    assert not inspect.isabstract(oaam::hardware::Subhardware)


def test_oaam::hardware::subhardware_constructor_exists():
    assert callable(oaam::hardware::Subhardware.__init__)


def test_oaam::hardware::subhardware_constructor_args():
    sig = inspect.signature(oaam::hardware::Subhardware.__init__)
    params = list(sig.parameters.keys())



def test_oaam::hardware::hardware_is_not_abstract():
    assert not inspect.isabstract(oaam::hardware::Hardware)


def test_oaam::hardware::hardware_constructor_exists():
    assert callable(oaam::hardware::Hardware.__init__)


def test_oaam::hardware::hardware_constructor_args():
    sig = inspect.signature(oaam::hardware::Hardware.__init__)
    params = list(sig.parameters.keys())



def test_library::resourceproviderinstancea_is_not_abstract():
    assert not inspect.isabstract(library::ResourceProviderInstanceA)


def test_library::resourceproviderinstancea_constructor_exists():
    assert callable(library::ResourceProviderInstanceA.__init__)


def test_library::resourceproviderinstancea_constructor_args():
    sig = inspect.signature(library::ResourceProviderInstanceA.__init__)
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



def test_oaam::functions::subfunctions_is_not_abstract():
    assert not inspect.isabstract(oaam::functions::Subfunctions)


def test_oaam::functions::subfunctions_constructor_exists():
    assert callable(oaam::functions::Subfunctions.__init__)


def test_oaam::functions::subfunctions_constructor_args():
    sig = inspect.signature(oaam::functions::Subfunctions.__init__)
    params = list(sig.parameters.keys())
    assert "multiplicityMax" in params, "Missing parameter 'multiplicityMax'"
    assert "multiplicityMin" in params, "Missing parameter 'multiplicityMin'"

def test_oaam::functions::subfunctions_has_multiplicityMax():
    assert hasattr(oaam::functions::Subfunctions, "multiplicityMax")
    descriptor = None
    for klass in oaam::functions::Subfunctions.__mro__:
        if "multiplicityMax" in klass.__dict__:
            descriptor = klass.__dict__["multiplicityMax"]
            break
    assert isinstance(descriptor, property)

def test_oaam::functions::subfunctions_has_multiplicityMin():
    assert hasattr(oaam::functions::Subfunctions, "multiplicityMin")
    descriptor = None
    for klass in oaam::functions::Subfunctions.__mro__:
        if "multiplicityMin" in klass.__dict__:
            descriptor = klass.__dict__["multiplicityMin"]
            break
    assert isinstance(descriptor, property)



def test_oaam::functions::functions_is_not_abstract():
    assert not inspect.isabstract(oaam::functions::Functions)


def test_oaam::functions::functions_constructor_exists():
    assert callable(oaam::functions::Functions.__init__)


def test_oaam::functions::functions_constructor_args():
    sig = inspect.signature(oaam::functions::Functions.__init__)
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



def test_oaam::systems::hydraulicpower_is_not_abstract():
    assert not inspect.isabstract(oaam::systems::HydraulicPower)


def test_oaam::systems::hydraulicpower_constructor_exists():
    assert callable(oaam::systems::HydraulicPower.__init__)


def test_oaam::systems::hydraulicpower_constructor_args():
    sig = inspect.signature(oaam::systems::HydraulicPower.__init__)
    params = list(sig.parameters.keys())
    assert "massFlowRate" in params, "Missing parameter 'massFlowRate'"
    assert "pressure" in params, "Missing parameter 'pressure'"

def test_oaam::systems::hydraulicpower_has_massFlowRate():
    assert hasattr(oaam::systems::HydraulicPower, "massFlowRate")
    descriptor = None
    for klass in oaam::systems::HydraulicPower.__mro__:
        if "massFlowRate" in klass.__dict__:
            descriptor = klass.__dict__["massFlowRate"]
            break
    assert isinstance(descriptor, property)

def test_oaam::systems::hydraulicpower_has_pressure():
    assert hasattr(oaam::systems::HydraulicPower, "pressure")
    descriptor = None
    for klass in oaam::systems::HydraulicPower.__mro__:
        if "pressure" in klass.__dict__:
            descriptor = klass.__dict__["pressure"]
            break
    assert isinstance(descriptor, property)



def test_oaam::systems::rotarypower_is_not_abstract():
    assert not inspect.isabstract(oaam::systems::RotaryPower)


def test_oaam::systems::rotarypower_constructor_exists():
    assert callable(oaam::systems::RotaryPower.__init__)


def test_oaam::systems::rotarypower_constructor_args():
    sig = inspect.signature(oaam::systems::RotaryPower.__init__)
    params = list(sig.parameters.keys())
    assert "angularVelocity" in params, "Missing parameter 'angularVelocity'"
    assert "momentum" in params, "Missing parameter 'momentum'"

def test_oaam::systems::rotarypower_has_angularVelocity():
    assert hasattr(oaam::systems::RotaryPower, "angularVelocity")
    descriptor = None
    for klass in oaam::systems::RotaryPower.__mro__:
        if "angularVelocity" in klass.__dict__:
            descriptor = klass.__dict__["angularVelocity"]
            break
    assert isinstance(descriptor, property)

def test_oaam::systems::rotarypower_has_momentum():
    assert hasattr(oaam::systems::RotaryPower, "momentum")
    descriptor = None
    for klass in oaam::systems::RotaryPower.__mro__:
        if "momentum" in klass.__dict__:
            descriptor = klass.__dict__["momentum"]
            break
    assert isinstance(descriptor, property)



def test_oaam::systems::electricpower_is_not_abstract():
    assert not inspect.isabstract(oaam::systems::ElectricPower)


def test_oaam::systems::electricpower_constructor_exists():
    assert callable(oaam::systems::ElectricPower.__init__)


def test_oaam::systems::electricpower_constructor_args():
    sig = inspect.signature(oaam::systems::ElectricPower.__init__)
    params = list(sig.parameters.keys())
    assert "nPhases" in params, "Missing parameter 'nPhases'"
    assert "voltage" in params, "Missing parameter 'voltage'"
    assert "current" in params, "Missing parameter 'current'"
    assert "frequency" in params, "Missing parameter 'frequency'"

def test_oaam::systems::electricpower_has_nPhases():
    assert hasattr(oaam::systems::ElectricPower, "nPhases")
    descriptor = None
    for klass in oaam::systems::ElectricPower.__mro__:
        if "nPhases" in klass.__dict__:
            descriptor = klass.__dict__["nPhases"]
            break
    assert isinstance(descriptor, property)

def test_oaam::systems::electricpower_has_voltage():
    assert hasattr(oaam::systems::ElectricPower, "voltage")
    descriptor = None
    for klass in oaam::systems::ElectricPower.__mro__:
        if "voltage" in klass.__dict__:
            descriptor = klass.__dict__["voltage"]
            break
    assert isinstance(descriptor, property)

def test_oaam::systems::electricpower_has_current():
    assert hasattr(oaam::systems::ElectricPower, "current")
    descriptor = None
    for klass in oaam::systems::ElectricPower.__mro__:
        if "current" in klass.__dict__:
            descriptor = klass.__dict__["current"]
            break
    assert isinstance(descriptor, property)

def test_oaam::systems::electricpower_has_frequency():
    assert hasattr(oaam::systems::ElectricPower, "frequency")
    descriptor = None
    for klass in oaam::systems::ElectricPower.__mro__:
        if "frequency" in klass.__dict__:
            descriptor = klass.__dict__["frequency"]
            break
    assert isinstance(descriptor, property)



def test_oaam::systems::linearpower_is_not_abstract():
    assert not inspect.isabstract(oaam::systems::LinearPower)


def test_oaam::systems::linearpower_constructor_exists():
    assert callable(oaam::systems::LinearPower.__init__)


def test_oaam::systems::linearpower_constructor_args():
    sig = inspect.signature(oaam::systems::LinearPower.__init__)
    params = list(sig.parameters.keys())
    assert "force" in params, "Missing parameter 'force'"
    assert "velocity" in params, "Missing parameter 'velocity'"

def test_oaam::systems::linearpower_has_force():
    assert hasattr(oaam::systems::LinearPower, "force")
    descriptor = None
    for klass in oaam::systems::LinearPower.__mro__:
        if "force" in klass.__dict__:
            descriptor = klass.__dict__["force"]
            break
    assert isinstance(descriptor, property)

def test_oaam::systems::linearpower_has_velocity():
    assert hasattr(oaam::systems::LinearPower, "velocity")
    descriptor = None
    for klass in oaam::systems::LinearPower.__mro__:
        if "velocity" in klass.__dict__:
            descriptor = klass.__dict__["velocity"]
            break
    assert isinstance(descriptor, property)



def test_systems::requiredinformationa_is_not_abstract():
    assert not inspect.isabstract(systems::RequiredInformationA)


def test_systems::requiredinformationa_constructor_exists():
    assert callable(systems::RequiredInformationA.__init__)


def test_systems::requiredinformationa_constructor_args():
    sig = inspect.signature(systems::RequiredInformationA.__init__)
    params = list(sig.parameters.keys())



def test_systems::providedinformationa_is_not_abstract():
    assert not inspect.isabstract(systems::ProvidedInformationA)


def test_systems::providedinformationa_constructor_exists():
    assert callable(systems::ProvidedInformationA.__init__)


def test_systems::providedinformationa_constructor_args():
    sig = inspect.signature(systems::ProvidedInformationA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::systems::providedinformationa_is_not_abstract():
    assert not inspect.isabstract(oaam::systems::ProvidedInformationA)


def test_oaam::systems::providedinformationa_constructor_exists():
    assert callable(oaam::systems::ProvidedInformationA.__init__)


def test_oaam::systems::providedinformationa_constructor_args():
    sig = inspect.signature(oaam::systems::ProvidedInformationA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::systems::requiredinformationa_is_not_abstract():
    assert not inspect.isabstract(oaam::systems::RequiredInformationA)


def test_oaam::systems::requiredinformationa_constructor_exists():
    assert callable(oaam::systems::RequiredInformationA.__init__)


def test_oaam::systems::requiredinformationa_constructor_args():
    sig = inspect.signature(oaam::systems::RequiredInformationA.__init__)
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



def test_library::resourceprovidera_is_not_abstract():
    assert not inspect.isabstract(library::ResourceProviderA)


def test_library::resourceprovidera_constructor_exists():
    assert callable(library::ResourceProviderA.__init__)


def test_library::resourceprovidera_constructor_args():
    sig = inspect.signature(library::ResourceProviderA.__init__)
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



def test_library::resourceconsumera_is_not_abstract():
    assert not inspect.isabstract(library::ResourceConsumerA)


def test_library::resourceconsumera_constructor_exists():
    assert callable(library::ResourceConsumerA.__init__)


def test_library::resourceconsumera_constructor_args():
    sig = inspect.signature(library::ResourceConsumerA.__init__)
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



def test_oaam::library::resourceproviderinstancea_is_not_abstract():
    assert not inspect.isabstract(oaam::library::ResourceProviderInstanceA)


def test_oaam::library::resourceproviderinstancea_constructor_exists():
    assert callable(oaam::library::ResourceProviderInstanceA.__init__)


def test_oaam::library::resourceproviderinstancea_constructor_args():
    sig = inspect.signature(oaam::library::ResourceProviderInstanceA.__init__)
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



def test_oaam::library::resourceprovidera_is_not_abstract():
    assert not inspect.isabstract(oaam::library::ResourceProviderA)


def test_oaam::library::resourceprovidera_constructor_exists():
    assert callable(oaam::library::ResourceProviderA.__init__)


def test_oaam::library::resourceprovidera_constructor_args():
    sig = inspect.signature(oaam::library::ResourceProviderA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::resourceconsumera_is_not_abstract():
    assert not inspect.isabstract(oaam::library::ResourceConsumerA)


def test_oaam::library::resourceconsumera_constructor_exists():
    assert callable(oaam::library::ResourceConsumerA.__init__)


def test_oaam::library::resourceconsumera_constructor_args():
    sig = inspect.signature(oaam::library::ResourceConsumerA.__init__)
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



def test_oaam::common::floatingpoint_is_not_abstract():
    assert not inspect.isabstract(oaam::common::FloatingPoint)


def test_oaam::common::floatingpoint_constructor_exists():
    assert callable(oaam::common::FloatingPoint.__init__)


def test_oaam::common::floatingpoint_constructor_args():
    sig = inspect.signature(oaam::common::FloatingPoint.__init__)
    params = list(sig.parameters.keys())
    assert "nBits" in params, "Missing parameter 'nBits'"
    assert "endianess" in params, "Missing parameter 'endianess'"

def test_oaam::common::floatingpoint_has_nBits():
    assert hasattr(oaam::common::FloatingPoint, "nBits")
    descriptor = None
    for klass in oaam::common::FloatingPoint.__mro__:
        if "nBits" in klass.__dict__:
            descriptor = klass.__dict__["nBits"]
            break
    assert isinstance(descriptor, property)

def test_oaam::common::floatingpoint_has_endianess():
    assert hasattr(oaam::common::FloatingPoint, "endianess")
    descriptor = None
    for klass in oaam::common::FloatingPoint.__mro__:
        if "endianess" in klass.__dict__:
            descriptor = klass.__dict__["endianess"]
            break
    assert isinstance(descriptor, property)



def test_oaam::common::character_is_not_abstract():
    assert not inspect.isabstract(oaam::common::Character)


def test_oaam::common::character_constructor_exists():
    assert callable(oaam::common::Character.__init__)


def test_oaam::common::character_constructor_args():
    sig = inspect.signature(oaam::common::Character.__init__)
    params = list(sig.parameters.keys())
    assert "encoding" in params, "Missing parameter 'encoding'"
    assert "nBits" in params, "Missing parameter 'nBits'"

def test_oaam::common::character_has_encoding():
    assert hasattr(oaam::common::Character, "encoding")
    descriptor = None
    for klass in oaam::common::Character.__mro__:
        if "encoding" in klass.__dict__:
            descriptor = klass.__dict__["encoding"]
            break
    assert isinstance(descriptor, property)

def test_oaam::common::character_has_nBits():
    assert hasattr(oaam::common::Character, "nBits")
    descriptor = None
    for klass in oaam::common::Character.__mro__:
        if "nBits" in klass.__dict__:
            descriptor = klass.__dict__["nBits"]
            break
    assert isinstance(descriptor, property)



def test_oaam::common::byte_is_not_abstract():
    assert not inspect.isabstract(oaam::common::Byte)


def test_oaam::common::byte_constructor_exists():
    assert callable(oaam::common::Byte.__init__)


def test_oaam::common::byte_constructor_args():
    sig = inspect.signature(oaam::common::Byte.__init__)
    params = list(sig.parameters.keys())
    assert "nBits" in params, "Missing parameter 'nBits'"

def test_oaam::common::byte_has_nBits():
    assert hasattr(oaam::common::Byte, "nBits")
    descriptor = None
    for klass in oaam::common::Byte.__mro__:
        if "nBits" in klass.__dict__:
            descriptor = klass.__dict__["nBits"]
            break
    assert isinstance(descriptor, property)



def test_oaam::common::boolean_is_not_abstract():
    assert not inspect.isabstract(oaam::common::Boolean)


def test_oaam::common::boolean_constructor_exists():
    assert callable(oaam::common::Boolean.__init__)


def test_oaam::common::boolean_constructor_args():
    sig = inspect.signature(oaam::common::Boolean.__init__)
    params = list(sig.parameters.keys())
    assert "nBits" in params, "Missing parameter 'nBits'"

def test_oaam::common::boolean_has_nBits():
    assert hasattr(oaam::common::Boolean, "nBits")
    descriptor = None
    for klass in oaam::common::Boolean.__mro__:
        if "nBits" in klass.__dict__:
            descriptor = klass.__dict__["nBits"]
            break
    assert isinstance(descriptor, property)



def test_oaam::common::struct_is_not_abstract():
    assert not inspect.isabstract(oaam::common::Struct)


def test_oaam::common::struct_constructor_exists():
    assert callable(oaam::common::Struct.__init__)


def test_oaam::common::struct_constructor_args():
    sig = inspect.signature(oaam::common::Struct.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_oaam::common::struct_has_alignment():
    assert hasattr(oaam::common::Struct, "alignment")
    descriptor = None
    for klass in oaam::common::Struct.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)

def test_oaam::common::struct_has_isAbstract():
    assert hasattr(oaam::common::Struct, "isAbstract")
    descriptor = None
    for klass in oaam::common::Struct.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_oaam::common::array_is_not_abstract():
    assert not inspect.isabstract(oaam::common::Array)


def test_oaam::common::array_constructor_exists():
    assert callable(oaam::common::Array.__init__)


def test_oaam::common::array_constructor_args():
    sig = inspect.signature(oaam::common::Array.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"
    assert "nElements" in params, "Missing parameter 'nElements'"

def test_oaam::common::array_has_alignment():
    assert hasattr(oaam::common::Array, "alignment")
    descriptor = None
    for klass in oaam::common::Array.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)

def test_oaam::common::array_has_nElements():
    assert hasattr(oaam::common::Array, "nElements")
    descriptor = None
    for klass in oaam::common::Array.__mro__:
        if "nElements" in klass.__dict__:
            descriptor = klass.__dict__["nElements"]
            break
    assert isinstance(descriptor, property)



def test_oaam::common::integer_is_not_abstract():
    assert not inspect.isabstract(oaam::common::Integer)


def test_oaam::common::integer_constructor_exists():
    assert callable(oaam::common::Integer.__init__)


def test_oaam::common::integer_constructor_args():
    sig = inspect.signature(oaam::common::Integer.__init__)
    params = list(sig.parameters.keys())
    assert "endianess" in params, "Missing parameter 'endianess'"
    assert "nBits" in params, "Missing parameter 'nBits'"
    assert "signed" in params, "Missing parameter 'signed'"

def test_oaam::common::integer_has_endianess():
    assert hasattr(oaam::common::Integer, "endianess")
    descriptor = None
    for klass in oaam::common::Integer.__mro__:
        if "endianess" in klass.__dict__:
            descriptor = klass.__dict__["endianess"]
            break
    assert isinstance(descriptor, property)

def test_oaam::common::integer_has_nBits():
    assert hasattr(oaam::common::Integer, "nBits")
    descriptor = None
    for klass in oaam::common::Integer.__mro__:
        if "nBits" in klass.__dict__:
            descriptor = klass.__dict__["nBits"]
            break
    assert isinstance(descriptor, property)

def test_oaam::common::integer_has_signed():
    assert hasattr(oaam::common::Integer, "signed")
    descriptor = None
    for klass in oaam::common::Integer.__mro__:
        if "signed" in klass.__dict__:
            descriptor = klass.__dict__["signed"]
            break
    assert isinstance(descriptor, property)



def test_boola_is_not_abstract():
    assert not inspect.isabstract(BoolA)


def test_boola_constructor_exists():
    assert callable(BoolA.__init__)


def test_boola_constructor_args():
    sig = inspect.signature(BoolA.__init__)
    params = list(sig.parameters.keys())



def test_common::oaambaseelementa_is_not_abstract():
    assert not inspect.isabstract(common::OaamBaseElementA)


def test_common::oaambaseelementa_constructor_exists():
    assert callable(common::OaamBaseElementA.__init__)


def test_common::oaambaseelementa_constructor_args():
    sig = inspect.signature(common::OaamBaseElementA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::capabilities::taskondevicecapability_is_not_abstract():
    assert not inspect.isabstract(oaam::capabilities::TaskOnDeviceCapability)


def test_oaam::capabilities::taskondevicecapability_constructor_exists():
    assert callable(oaam::capabilities::TaskOnDeviceCapability.__init__)


def test_oaam::capabilities::taskondevicecapability_constructor_args():
    sig = inspect.signature(oaam::capabilities::TaskOnDeviceCapability.__init__)
    params = list(sig.parameters.keys())
    assert "failureProbability" in params, "Missing parameter 'failureProbability'"
    assert "worstCaseExecutionTime" in params, "Missing parameter 'worstCaseExecutionTime'"

def test_oaam::capabilities::taskondevicecapability_has_failureProbability():
    assert hasattr(oaam::capabilities::TaskOnDeviceCapability, "failureProbability")
    descriptor = None
    for klass in oaam::capabilities::TaskOnDeviceCapability.__mro__:
        if "failureProbability" in klass.__dict__:
            descriptor = klass.__dict__["failureProbability"]
            break
    assert isinstance(descriptor, property)

def test_oaam::capabilities::taskondevicecapability_has_worstCaseExecutionTime():
    assert hasattr(oaam::capabilities::TaskOnDeviceCapability, "worstCaseExecutionTime")
    descriptor = None
    for klass in oaam::capabilities::TaskOnDeviceCapability.__mro__:
        if "worstCaseExecutionTime" in klass.__dict__:
            descriptor = klass.__dict__["worstCaseExecutionTime"]
            break
    assert isinstance(descriptor, property)



def test_oaam::library::messagetype_is_not_abstract():
    assert not inspect.isabstract(oaam::library::MessageType)


def test_oaam::library::messagetype_constructor_exists():
    assert callable(oaam::library::MessageType.__init__)


def test_oaam::library::messagetype_constructor_args():
    sig = inspect.signature(oaam::library::MessageType.__init__)
    params = list(sig.parameters.keys())
    assert "minLength" in params, "Missing parameter 'minLength'"
    assert "maxLength" in params, "Missing parameter 'maxLength'"
    assert "alignment" in params, "Missing parameter 'alignment'"

def test_oaam::library::messagetype_has_minLength():
    assert hasattr(oaam::library::MessageType, "minLength")
    descriptor = None
    for klass in oaam::library::MessageType.__mro__:
        if "minLength" in klass.__dict__:
            descriptor = klass.__dict__["minLength"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::messagetype_has_maxLength():
    assert hasattr(oaam::library::MessageType, "maxLength")
    descriptor = None
    for klass in oaam::library::MessageType.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::messagetype_has_alignment():
    assert hasattr(oaam::library::MessageType, "alignment")
    descriptor = None
    for klass in oaam::library::MessageType.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)



def test_oaam::anatomy::duct_is_not_abstract():
    assert not inspect.isabstract(oaam::anatomy::Duct)


def test_oaam::anatomy::duct_constructor_exists():
    assert callable(oaam::anatomy::Duct.__init__)


def test_oaam::anatomy::duct_constructor_args():
    sig = inspect.signature(oaam::anatomy::Duct.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_oaam::anatomy::duct_has_length():
    assert hasattr(oaam::anatomy::Duct, "length")
    descriptor = None
    for klass in oaam::anatomy::Duct.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_oaam::hardware::devicesymmetry_is_not_abstract():
    assert not inspect.isabstract(oaam::hardware::DeviceSymmetry)


def test_oaam::hardware::devicesymmetry_constructor_exists():
    assert callable(oaam::hardware::DeviceSymmetry.__init__)


def test_oaam::hardware::devicesymmetry_constructor_args():
    sig = inspect.signature(oaam::hardware::DeviceSymmetry.__init__)
    params = list(sig.parameters.keys())



def test_oaam::restrictions::arearestriction_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::AreaRestriction)


def test_oaam::restrictions::arearestriction_constructor_exists():
    assert callable(oaam::restrictions::AreaRestriction.__init__)


def test_oaam::restrictions::arearestriction_constructor_args():
    sig = inspect.signature(oaam::restrictions::AreaRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "isForbidden" in params, "Missing parameter 'isForbidden'"
    assert "areaName" in params, "Missing parameter 'areaName'"

def test_oaam::restrictions::arearestriction_has_isForbidden():
    assert hasattr(oaam::restrictions::AreaRestriction, "isForbidden")
    descriptor = None
    for klass in oaam::restrictions::AreaRestriction.__mro__:
        if "isForbidden" in klass.__dict__:
            descriptor = klass.__dict__["isForbidden"]
            break
    assert isinstance(descriptor, property)

def test_oaam::restrictions::arearestriction_has_areaName():
    assert hasattr(oaam::restrictions::AreaRestriction, "areaName")
    descriptor = None
    for klass in oaam::restrictions::AreaRestriction.__mro__:
        if "areaName" in klass.__dict__:
            descriptor = klass.__dict__["areaName"]
            break
    assert isinstance(descriptor, property)



def test_oaam::anatomy::areasymmetry_is_not_abstract():
    assert not inspect.isabstract(oaam::anatomy::AreaSymmetry)


def test_oaam::anatomy::areasymmetry_constructor_exists():
    assert callable(oaam::anatomy::AreaSymmetry.__init__)


def test_oaam::anatomy::areasymmetry_constructor_args():
    sig = inspect.signature(oaam::anatomy::AreaSymmetry.__init__)
    params = list(sig.parameters.keys())



def test_oaam::anatomy::area_is_not_abstract():
    assert not inspect.isabstract(oaam::anatomy::Area)


def test_oaam::anatomy::area_constructor_exists():
    assert callable(oaam::anatomy::Area.__init__)


def test_oaam::anatomy::area_constructor_args():
    sig = inspect.signature(oaam::anatomy::Area.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::resourcetype_is_not_abstract():
    assert not inspect.isabstract(oaam::library::ResourceType)


def test_oaam::library::resourcetype_constructor_exists():
    assert callable(oaam::library::ResourceType.__init__)


def test_oaam::library::resourcetype_constructor_args():
    sig = inspect.signature(oaam::library::ResourceType.__init__)
    params = list(sig.parameters.keys())
    assert "isConsumed" in params, "Missing parameter 'isConsumed'"
    assert "isConfigurable" in params, "Missing parameter 'isConfigurable'"
    assert "isDistinguishable" in params, "Missing parameter 'isDistinguishable'"
    assert "isIo" in params, "Missing parameter 'isIo'"
    assert "isPropagated" in params, "Missing parameter 'isPropagated'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_oaam::library::resourcetype_has_isConsumed():
    assert hasattr(oaam::library::ResourceType, "isConsumed")
    descriptor = None
    for klass in oaam::library::ResourceType.__mro__:
        if "isConsumed" in klass.__dict__:
            descriptor = klass.__dict__["isConsumed"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::resourcetype_has_isConfigurable():
    assert hasattr(oaam::library::ResourceType, "isConfigurable")
    descriptor = None
    for klass in oaam::library::ResourceType.__mro__:
        if "isConfigurable" in klass.__dict__:
            descriptor = klass.__dict__["isConfigurable"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::resourcetype_has_isDistinguishable():
    assert hasattr(oaam::library::ResourceType, "isDistinguishable")
    descriptor = None
    for klass in oaam::library::ResourceType.__mro__:
        if "isDistinguishable" in klass.__dict__:
            descriptor = klass.__dict__["isDistinguishable"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::resourcetype_has_isIo():
    assert hasattr(oaam::library::ResourceType, "isIo")
    descriptor = None
    for klass in oaam::library::ResourceType.__mro__:
        if "isIo" in klass.__dict__:
            descriptor = klass.__dict__["isIo"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::resourcetype_has_isPropagated():
    assert hasattr(oaam::library::ResourceType, "isPropagated")
    descriptor = None
    for klass in oaam::library::ResourceType.__mro__:
        if "isPropagated" in klass.__dict__:
            descriptor = klass.__dict__["isPropagated"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::resourcetype_has_direction():
    assert hasattr(oaam::library::ResourceType, "direction")
    descriptor = None
    for klass in oaam::library::ResourceType.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::resourcetype_has_unit():
    assert hasattr(oaam::library::ResourceType, "unit")
    descriptor = None
    for klass in oaam::library::ResourceType.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_oaam::restrictions::taskatomicrestriction_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::TaskAtomicRestriction)


def test_oaam::restrictions::taskatomicrestriction_constructor_exists():
    assert callable(oaam::restrictions::TaskAtomicRestriction.__init__)


def test_oaam::restrictions::taskatomicrestriction_constructor_args():
    sig = inspect.signature(oaam::restrictions::TaskAtomicRestriction.__init__)
    params = list(sig.parameters.keys())



def test_oaam::restrictions::locationrestriction_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::LocationRestriction)


def test_oaam::restrictions::locationrestriction_constructor_exists():
    assert callable(oaam::restrictions::LocationRestriction.__init__)


def test_oaam::restrictions::locationrestriction_constructor_args():
    sig = inspect.signature(oaam::restrictions::LocationRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "isForbidden" in params, "Missing parameter 'isForbidden'"
    assert "locationName" in params, "Missing parameter 'locationName'"

def test_oaam::restrictions::locationrestriction_has_isForbidden():
    assert hasattr(oaam::restrictions::LocationRestriction, "isForbidden")
    descriptor = None
    for klass in oaam::restrictions::LocationRestriction.__mro__:
        if "isForbidden" in klass.__dict__:
            descriptor = klass.__dict__["isForbidden"]
            break
    assert isinstance(descriptor, property)

def test_oaam::restrictions::locationrestriction_has_locationName():
    assert hasattr(oaam::restrictions::LocationRestriction, "locationName")
    descriptor = None
    for klass in oaam::restrictions::LocationRestriction.__mro__:
        if "locationName" in klass.__dict__:
            descriptor = klass.__dict__["locationName"]
            break
    assert isinstance(descriptor, property)



def test_oaam::allocations::signalassignmentsegment_is_not_abstract():
    assert not inspect.isabstract(oaam::allocations::SignalAssignmentSegment)


def test_oaam::allocations::signalassignmentsegment_constructor_exists():
    assert callable(oaam::allocations::SignalAssignmentSegment.__init__)


def test_oaam::allocations::signalassignmentsegment_constructor_args():
    sig = inspect.signature(oaam::allocations::SignalAssignmentSegment.__init__)
    params = list(sig.parameters.keys())



def test_oaam::systems::informationmaterial_is_not_abstract():
    assert not inspect.isabstract(oaam::systems::InformationMaterial)


def test_oaam::systems::informationmaterial_constructor_exists():
    assert callable(oaam::systems::InformationMaterial.__init__)


def test_oaam::systems::informationmaterial_constructor_args():
    sig = inspect.signature(oaam::systems::InformationMaterial.__init__)
    params = list(sig.parameters.keys())
    assert "velocity" in params, "Missing parameter 'velocity'"
    assert "density" in params, "Missing parameter 'density'"

def test_oaam::systems::informationmaterial_has_velocity():
    assert hasattr(oaam::systems::InformationMaterial, "velocity")
    descriptor = None
    for klass in oaam::systems::InformationMaterial.__mro__:
        if "velocity" in klass.__dict__:
            descriptor = klass.__dict__["velocity"]
            break
    assert isinstance(descriptor, property)

def test_oaam::systems::informationmaterial_has_density():
    assert hasattr(oaam::systems::InformationMaterial, "density")
    descriptor = None
    for klass in oaam::systems::InformationMaterial.__mro__:
        if "density" in klass.__dict__:
            descriptor = klass.__dict__["density"]
            break
    assert isinstance(descriptor, property)



def test_oaam::functions::taskgroup_is_not_abstract():
    assert not inspect.isabstract(oaam::functions::TaskGroup)


def test_oaam::functions::taskgroup_constructor_exists():
    assert callable(oaam::functions::TaskGroup.__init__)


def test_oaam::functions::taskgroup_constructor_args():
    sig = inspect.signature(oaam::functions::TaskGroup.__init__)
    params = list(sig.parameters.keys())



def test_oaam::functions::task_is_not_abstract():
    assert not inspect.isabstract(oaam::functions::Task)


def test_oaam::functions::task_constructor_exists():
    assert callable(oaam::functions::Task.__init__)


def test_oaam::functions::task_constructor_args():
    sig = inspect.signature(oaam::functions::Task.__init__)
    params = list(sig.parameters.keys())
    assert "nParallels" in params, "Missing parameter 'nParallels'"
    assert "fixedRate" in params, "Missing parameter 'fixedRate'"

def test_oaam::functions::task_has_nParallels():
    assert hasattr(oaam::functions::Task, "nParallels")
    descriptor = None
    for klass in oaam::functions::Task.__mro__:
        if "nParallels" in klass.__dict__:
            descriptor = klass.__dict__["nParallels"]
            break
    assert isinstance(descriptor, property)

def test_oaam::functions::task_has_fixedRate():
    assert hasattr(oaam::functions::Task, "fixedRate")
    descriptor = None
    for klass in oaam::functions::Task.__mro__:
        if "fixedRate" in klass.__dict__:
            descriptor = klass.__dict__["fixedRate"]
            break
    assert isinstance(descriptor, property)



def test_oaam::capabilities::subconnectionindevicecapability_is_not_abstract():
    assert not inspect.isabstract(oaam::capabilities::SubconnectionInDeviceCapability)


def test_oaam::capabilities::subconnectionindevicecapability_constructor_exists():
    assert callable(oaam::capabilities::SubconnectionInDeviceCapability.__init__)


def test_oaam::capabilities::subconnectionindevicecapability_constructor_args():
    sig = inspect.signature(oaam::capabilities::SubconnectionInDeviceCapability.__init__)
    params = list(sig.parameters.keys())



def test_oaam::allocations::scheduledtime_is_not_abstract():
    assert not inspect.isabstract(oaam::allocations::ScheduledTime)


def test_oaam::allocations::scheduledtime_constructor_exists():
    assert callable(oaam::allocations::ScheduledTime.__init__)


def test_oaam::allocations::scheduledtime_constructor_args():
    sig = inspect.signature(oaam::allocations::ScheduledTime.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"
    assert "restart" in params, "Missing parameter 'restart'"
    assert "startTime" in params, "Missing parameter 'startTime'"
    assert "cycle" in params, "Missing parameter 'cycle'"

def test_oaam::allocations::scheduledtime_has_duration():
    assert hasattr(oaam::allocations::ScheduledTime, "duration")
    descriptor = None
    for klass in oaam::allocations::ScheduledTime.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_oaam::allocations::scheduledtime_has_restart():
    assert hasattr(oaam::allocations::ScheduledTime, "restart")
    descriptor = None
    for klass in oaam::allocations::ScheduledTime.__mro__:
        if "restart" in klass.__dict__:
            descriptor = klass.__dict__["restart"]
            break
    assert isinstance(descriptor, property)

def test_oaam::allocations::scheduledtime_has_startTime():
    assert hasattr(oaam::allocations::ScheduledTime, "startTime")
    descriptor = None
    for klass in oaam::allocations::ScheduledTime.__mro__:
        if "startTime" in klass.__dict__:
            descriptor = klass.__dict__["startTime"]
            break
    assert isinstance(descriptor, property)

def test_oaam::allocations::scheduledtime_has_cycle():
    assert hasattr(oaam::allocations::ScheduledTime, "cycle")
    descriptor = None
    for klass in oaam::allocations::ScheduledTime.__mro__:
        if "cycle" in klass.__dict__:
            descriptor = klass.__dict__["cycle"]
            break
    assert isinstance(descriptor, property)



def test_oaam::library::signaltype_is_not_abstract():
    assert not inspect.isabstract(oaam::library::SignalType)


def test_oaam::library::signaltype_constructor_exists():
    assert callable(oaam::library::SignalType.__init__)


def test_oaam::library::signaltype_constructor_args():
    sig = inspect.signature(oaam::library::SignalType.__init__)
    params = list(sig.parameters.keys())



def test_oaam::capabilities::deviceinlocationcapability_is_not_abstract():
    assert not inspect.isabstract(oaam::capabilities::DeviceInLocationCapability)


def test_oaam::capabilities::deviceinlocationcapability_constructor_exists():
    assert callable(oaam::capabilities::DeviceInLocationCapability.__init__)


def test_oaam::capabilities::deviceinlocationcapability_constructor_args():
    sig = inspect.signature(oaam::capabilities::DeviceInLocationCapability.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::tasktype_is_not_abstract():
    assert not inspect.isabstract(oaam::library::TaskType)


def test_oaam::library::tasktype_constructor_exists():
    assert callable(oaam::library::TaskType.__init__)


def test_oaam::library::tasktype_constructor_args():
    sig = inspect.signature(oaam::library::TaskType.__init__)
    params = list(sig.parameters.keys())
    assert "isDeterministic" in params, "Missing parameter 'isDeterministic'"
    assert "preferredExecutionRate" in params, "Missing parameter 'preferredExecutionRate'"

def test_oaam::library::tasktype_has_isDeterministic():
    assert hasattr(oaam::library::TaskType, "isDeterministic")
    descriptor = None
    for klass in oaam::library::TaskType.__mro__:
        if "isDeterministic" in klass.__dict__:
            descriptor = klass.__dict__["isDeterministic"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::tasktype_has_preferredExecutionRate():
    assert hasattr(oaam::library::TaskType, "preferredExecutionRate")
    descriptor = None
    for klass in oaam::library::TaskType.__mro__:
        if "preferredExecutionRate" in klass.__dict__:
            descriptor = klass.__dict__["preferredExecutionRate"]
            break
    assert isinstance(descriptor, property)



def test_oaam::capabilities::messageonbuscapability_is_not_abstract():
    assert not inspect.isabstract(oaam::capabilities::MessageOnBusCapability)


def test_oaam::capabilities::messageonbuscapability_constructor_exists():
    assert callable(oaam::capabilities::MessageOnBusCapability.__init__)


def test_oaam::capabilities::messageonbuscapability_constructor_args():
    sig = inspect.signature(oaam::capabilities::MessageOnBusCapability.__init__)
    params = list(sig.parameters.keys())



def test_oaam::allocations::connectionassignment_is_not_abstract():
    assert not inspect.isabstract(oaam::allocations::ConnectionAssignment)


def test_oaam::allocations::connectionassignment_constructor_exists():
    assert callable(oaam::allocations::ConnectionAssignment.__init__)


def test_oaam::allocations::connectionassignment_constructor_args():
    sig = inspect.signature(oaam::allocations::ConnectionAssignment.__init__)
    params = list(sig.parameters.keys())



def test_oaam::allocations::deviceassignment_is_not_abstract():
    assert not inspect.isabstract(oaam::allocations::DeviceAssignment)


def test_oaam::allocations::deviceassignment_constructor_exists():
    assert callable(oaam::allocations::DeviceAssignment.__init__)


def test_oaam::allocations::deviceassignment_constructor_args():
    sig = inspect.signature(oaam::allocations::DeviceAssignment.__init__)
    params = list(sig.parameters.keys())



def test_oaam::capabilities::submessageinmessagecapability_is_not_abstract():
    assert not inspect.isabstract(oaam::capabilities::SubmessageInMessageCapability)


def test_oaam::capabilities::submessageinmessagecapability_constructor_exists():
    assert callable(oaam::capabilities::SubmessageInMessageCapability.__init__)


def test_oaam::capabilities::submessageinmessagecapability_constructor_args():
    sig = inspect.signature(oaam::capabilities::SubmessageInMessageCapability.__init__)
    params = list(sig.parameters.keys())



def test_oaam::functions::output_is_not_abstract():
    assert not inspect.isabstract(oaam::functions::Output)


def test_oaam::functions::output_constructor_exists():
    assert callable(oaam::functions::Output.__init__)


def test_oaam::functions::output_constructor_args():
    sig = inspect.signature(oaam::functions::Output.__init__)
    params = list(sig.parameters.keys())
    assert "fixedRate" in params, "Missing parameter 'fixedRate'"

def test_oaam::functions::output_has_fixedRate():
    assert hasattr(oaam::functions::Output, "fixedRate")
    descriptor = None
    for klass in oaam::functions::Output.__mro__:
        if "fixedRate" in klass.__dict__:
            descriptor = klass.__dict__["fixedRate"]
            break
    assert isinstance(descriptor, property)



def test_oaam::hardware::io_is_not_abstract():
    assert not inspect.isabstract(oaam::hardware::Io)


def test_oaam::hardware::io_constructor_exists():
    assert callable(oaam::hardware::Io.__init__)


def test_oaam::hardware::io_constructor_args():
    sig = inspect.signature(oaam::hardware::Io.__init__)
    params = list(sig.parameters.keys())



def test_oaam::scenario::variant_is_not_abstract():
    assert not inspect.isabstract(oaam::scenario::Variant)


def test_oaam::scenario::variant_constructor_exists():
    assert callable(oaam::scenario::Variant.__init__)


def test_oaam::scenario::variant_constructor_args():
    sig = inspect.signature(oaam::scenario::Variant.__init__)
    params = list(sig.parameters.keys())



def test_oaam::functions::externaltasklink_is_not_abstract():
    assert not inspect.isabstract(oaam::functions::ExternalTaskLink)


def test_oaam::functions::externaltasklink_constructor_exists():
    assert callable(oaam::functions::ExternalTaskLink.__init__)


def test_oaam::functions::externaltasklink_constructor_args():
    sig = inspect.signature(oaam::functions::ExternalTaskLink.__init__)
    params = list(sig.parameters.keys())
    assert "filter" in params, "Missing parameter 'filter'"

def test_oaam::functions::externaltasklink_has_filter():
    assert hasattr(oaam::functions::ExternalTaskLink, "filter")
    descriptor = None
    for klass in oaam::functions::ExternalTaskLink.__mro__:
        if "filter" in klass.__dict__:
            descriptor = klass.__dict__["filter"]
            break
    assert isinstance(descriptor, property)



def test_oaam::capabilities::connectioninductorlocationcapability_is_not_abstract():
    assert not inspect.isabstract(oaam::capabilities::ConnectionInDuctOrLocationCapability)


def test_oaam::capabilities::connectioninductorlocationcapability_constructor_exists():
    assert callable(oaam::capabilities::ConnectionInDuctOrLocationCapability.__init__)


def test_oaam::capabilities::connectioninductorlocationcapability_constructor_args():
    sig = inspect.signature(oaam::capabilities::ConnectionInDuctOrLocationCapability.__init__)
    params = list(sig.parameters.keys())



def test_oaam::allocations::messagesegment_is_not_abstract():
    assert not inspect.isabstract(oaam::allocations::MessageSegment)


def test_oaam::allocations::messagesegment_constructor_exists():
    assert callable(oaam::allocations::MessageSegment.__init__)


def test_oaam::allocations::messagesegment_constructor_args():
    sig = inspect.signature(oaam::allocations::MessageSegment.__init__)
    params = list(sig.parameters.keys())



def test_oaam::functions::tasksymmetry_is_not_abstract():
    assert not inspect.isabstract(oaam::functions::TaskSymmetry)


def test_oaam::functions::tasksymmetry_constructor_exists():
    assert callable(oaam::functions::TaskSymmetry.__init__)


def test_oaam::functions::tasksymmetry_constructor_args():
    sig = inspect.signature(oaam::functions::TaskSymmetry.__init__)
    params = list(sig.parameters.keys())



def test_oaam::allocations::subconnectionassignment_is_not_abstract():
    assert not inspect.isabstract(oaam::allocations::SubconnectionAssignment)


def test_oaam::allocations::subconnectionassignment_constructor_exists():
    assert callable(oaam::allocations::SubconnectionAssignment.__init__)


def test_oaam::allocations::subconnectionassignment_constructor_args():
    sig = inspect.signature(oaam::allocations::SubconnectionAssignment.__init__)
    params = list(sig.parameters.keys())



def test_oaam::scenario::scenarioparameterbool_is_not_abstract():
    assert not inspect.isabstract(oaam::scenario::ScenarioParameterBool)


def test_oaam::scenario::scenarioparameterbool_constructor_exists():
    assert callable(oaam::scenario::ScenarioParameterBool.__init__)


def test_oaam::scenario::scenarioparameterbool_constructor_args():
    sig = inspect.signature(oaam::scenario::ScenarioParameterBool.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oaam::scenario::scenarioparameterbool_has_value():
    assert hasattr(oaam::scenario::ScenarioParameterBool, "value")
    descriptor = None
    for klass in oaam::scenario::ScenarioParameterBool.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oaam::allocations::taskassignment_is_not_abstract():
    assert not inspect.isabstract(oaam::allocations::TaskAssignment)


def test_oaam::allocations::taskassignment_constructor_exists():
    assert callable(oaam::allocations::TaskAssignment.__init__)


def test_oaam::allocations::taskassignment_constructor_args():
    sig = inspect.signature(oaam::allocations::TaskAssignment.__init__)
    params = list(sig.parameters.keys())



def test_oaam::functions::signal_is_not_abstract():
    assert not inspect.isabstract(oaam::functions::Signal)


def test_oaam::functions::signal_constructor_exists():
    assert callable(oaam::functions::Signal.__init__)


def test_oaam::functions::signal_constructor_args():
    sig = inspect.signature(oaam::functions::Signal.__init__)
    params = list(sig.parameters.keys())
    assert "inIndex" in params, "Missing parameter 'inIndex'"
    assert "outIndex" in params, "Missing parameter 'outIndex'"

def test_oaam::functions::signal_has_inIndex():
    assert hasattr(oaam::functions::Signal, "inIndex")
    descriptor = None
    for klass in oaam::functions::Signal.__mro__:
        if "inIndex" in klass.__dict__:
            descriptor = klass.__dict__["inIndex"]
            break
    assert isinstance(descriptor, property)

def test_oaam::functions::signal_has_outIndex():
    assert hasattr(oaam::functions::Signal, "outIndex")
    descriptor = None
    for klass in oaam::functions::Signal.__mro__:
        if "outIndex" in klass.__dict__:
            descriptor = klass.__dict__["outIndex"]
            break
    assert isinstance(descriptor, property)



def test_oaam::functions::externaloutputlink_is_not_abstract():
    assert not inspect.isabstract(oaam::functions::ExternalOutputLink)


def test_oaam::functions::externaloutputlink_constructor_exists():
    assert callable(oaam::functions::ExternalOutputLink.__init__)


def test_oaam::functions::externaloutputlink_constructor_args():
    sig = inspect.signature(oaam::functions::ExternalOutputLink.__init__)
    params = list(sig.parameters.keys())
    assert "filter" in params, "Missing parameter 'filter'"

def test_oaam::functions::externaloutputlink_has_filter():
    assert hasattr(oaam::functions::ExternalOutputLink, "filter")
    descriptor = None
    for klass in oaam::functions::ExternalOutputLink.__mro__:
        if "filter" in klass.__dict__:
            descriptor = klass.__dict__["filter"]
            break
    assert isinstance(descriptor, property)



def test_oaam::hardware::bus_is_not_abstract():
    assert not inspect.isabstract(oaam::hardware::Bus)


def test_oaam::hardware::bus_constructor_exists():
    assert callable(oaam::hardware::Bus.__init__)


def test_oaam::hardware::bus_constructor_args():
    sig = inspect.signature(oaam::hardware::Bus.__init__)
    params = list(sig.parameters.keys())



def test_oaam::hardware::connection_is_not_abstract():
    assert not inspect.isabstract(oaam::hardware::Connection)


def test_oaam::hardware::connection_constructor_exists():
    assert callable(oaam::hardware::Connection.__init__)


def test_oaam::hardware::connection_constructor_args():
    sig = inspect.signature(oaam::hardware::Connection.__init__)
    params = list(sig.parameters.keys())



def test_oaam::functions::taskredundancy_is_not_abstract():
    assert not inspect.isabstract(oaam::functions::TaskRedundancy)


def test_oaam::functions::taskredundancy_constructor_exists():
    assert callable(oaam::functions::TaskRedundancy.__init__)


def test_oaam::functions::taskredundancy_constructor_args():
    sig = inspect.signature(oaam::functions::TaskRedundancy.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::bustype_is_not_abstract():
    assert not inspect.isabstract(oaam::library::BusType)


def test_oaam::library::bustype_constructor_exists():
    assert callable(oaam::library::BusType.__init__)


def test_oaam::library::bustype_constructor_args():
    sig = inspect.signature(oaam::library::BusType.__init__)
    params = list(sig.parameters.keys())
    assert "isSelfManaging" in params, "Missing parameter 'isSelfManaging'"
    assert "mtbf" in params, "Missing parameter 'mtbf'"
    assert "requiresMaster" in params, "Missing parameter 'requiresMaster'"

def test_oaam::library::bustype_has_isSelfManaging():
    assert hasattr(oaam::library::BusType, "isSelfManaging")
    descriptor = None
    for klass in oaam::library::BusType.__mro__:
        if "isSelfManaging" in klass.__dict__:
            descriptor = klass.__dict__["isSelfManaging"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::bustype_has_mtbf():
    assert hasattr(oaam::library::BusType, "mtbf")
    descriptor = None
    for klass in oaam::library::BusType.__mro__:
        if "mtbf" in klass.__dict__:
            descriptor = klass.__dict__["mtbf"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::bustype_has_requiresMaster():
    assert hasattr(oaam::library::BusType, "requiresMaster")
    descriptor = None
    for klass in oaam::library::BusType.__mro__:
        if "requiresMaster" in klass.__dict__:
            descriptor = klass.__dict__["requiresMaster"]
            break
    assert isinstance(descriptor, property)



def test_oaam::library::locationtype_is_not_abstract():
    assert not inspect.isabstract(oaam::library::LocationType)


def test_oaam::library::locationtype_constructor_exists():
    assert callable(oaam::library::LocationType.__init__)


def test_oaam::library::locationtype_constructor_args():
    sig = inspect.signature(oaam::library::LocationType.__init__)
    params = list(sig.parameters.keys())
    assert "isJoint" in params, "Missing parameter 'isJoint'"

def test_oaam::library::locationtype_has_isJoint():
    assert hasattr(oaam::library::LocationType, "isJoint")
    descriptor = None
    for klass in oaam::library::LocationType.__mro__:
        if "isJoint" in klass.__dict__:
            descriptor = klass.__dict__["isJoint"]
            break
    assert isinstance(descriptor, property)



def test_oaam::capabilities::signalinmessagecapability_is_not_abstract():
    assert not inspect.isabstract(oaam::capabilities::SignalInMessageCapability)


def test_oaam::capabilities::signalinmessagecapability_constructor_exists():
    assert callable(oaam::capabilities::SignalInMessageCapability.__init__)


def test_oaam::capabilities::signalinmessagecapability_constructor_args():
    sig = inspect.signature(oaam::capabilities::SignalInMessageCapability.__init__)
    params = list(sig.parameters.keys())



def test_oaam::anatomy::locationsymmetry_is_not_abstract():
    assert not inspect.isabstract(oaam::anatomy::LocationSymmetry)


def test_oaam::anatomy::locationsymmetry_constructor_exists():
    assert callable(oaam::anatomy::LocationSymmetry.__init__)


def test_oaam::anatomy::locationsymmetry_constructor_args():
    sig = inspect.signature(oaam::anatomy::LocationSymmetry.__init__)
    params = list(sig.parameters.keys())



def test_oaam::allocations::messagea_is_not_abstract():
    assert not inspect.isabstract(oaam::allocations::MessageA)


def test_oaam::allocations::messagea_constructor_exists():
    assert callable(oaam::allocations::MessageA.__init__)


def test_oaam::allocations::messagea_constructor_args():
    sig = inspect.signature(oaam::allocations::MessageA.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "isPersistent" in params, "Missing parameter 'isPersistent'"

def test_oaam::allocations::messagea_has_length():
    assert hasattr(oaam::allocations::MessageA, "length")
    descriptor = None
    for klass in oaam::allocations::MessageA.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_oaam::allocations::messagea_has_isPersistent():
    assert hasattr(oaam::allocations::MessageA, "isPersistent")
    descriptor = None
    for klass in oaam::allocations::MessageA.__mro__:
        if "isPersistent" in klass.__dict__:
            descriptor = klass.__dict__["isPersistent"]
            break
    assert isinstance(descriptor, property)



def test_oaam::anatomy::location_is_not_abstract():
    assert not inspect.isabstract(oaam::anatomy::Location)


def test_oaam::anatomy::location_constructor_exists():
    assert callable(oaam::anatomy::Location.__init__)


def test_oaam::anatomy::location_constructor_args():
    sig = inspect.signature(oaam::anatomy::Location.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_oaam::anatomy::location_has_length():
    assert hasattr(oaam::anatomy::Location, "length")
    descriptor = None
    for klass in oaam::anatomy::Location.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_oaam::functions::functionscontainera_is_not_abstract():
    assert not inspect.isabstract(oaam::functions::FunctionsContainerA)


def test_oaam::functions::functionscontainera_constructor_exists():
    assert callable(oaam::functions::FunctionsContainerA.__init__)


def test_oaam::functions::functionscontainera_constructor_args():
    sig = inspect.signature(oaam::functions::FunctionsContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::devicetype_is_not_abstract():
    assert not inspect.isabstract(oaam::library::DeviceType)


def test_oaam::library::devicetype_constructor_exists():
    assert callable(oaam::library::DeviceType.__init__)


def test_oaam::library::devicetype_constructor_args():
    sig = inspect.signature(oaam::library::DeviceType.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "canHaveSubdevices" in params, "Missing parameter 'canHaveSubdevices'"
    assert "mtbf" in params, "Missing parameter 'mtbf'"
    assert "isSelfManaging" in params, "Missing parameter 'isSelfManaging'"
    assert "isSubdevice" in params, "Missing parameter 'isSubdevice'"
    assert "cost" in params, "Missing parameter 'cost'"

def test_oaam::library::devicetype_has_weight():
    assert hasattr(oaam::library::DeviceType, "weight")
    descriptor = None
    for klass in oaam::library::DeviceType.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::devicetype_has_canHaveSubdevices():
    assert hasattr(oaam::library::DeviceType, "canHaveSubdevices")
    descriptor = None
    for klass in oaam::library::DeviceType.__mro__:
        if "canHaveSubdevices" in klass.__dict__:
            descriptor = klass.__dict__["canHaveSubdevices"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::devicetype_has_mtbf():
    assert hasattr(oaam::library::DeviceType, "mtbf")
    descriptor = None
    for klass in oaam::library::DeviceType.__mro__:
        if "mtbf" in klass.__dict__:
            descriptor = klass.__dict__["mtbf"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::devicetype_has_isSelfManaging():
    assert hasattr(oaam::library::DeviceType, "isSelfManaging")
    descriptor = None
    for klass in oaam::library::DeviceType.__mro__:
        if "isSelfManaging" in klass.__dict__:
            descriptor = klass.__dict__["isSelfManaging"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::devicetype_has_isSubdevice():
    assert hasattr(oaam::library::DeviceType, "isSubdevice")
    descriptor = None
    for klass in oaam::library::DeviceType.__mro__:
        if "isSubdevice" in klass.__dict__:
            descriptor = klass.__dict__["isSubdevice"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::devicetype_has_cost():
    assert hasattr(oaam::library::DeviceType, "cost")
    descriptor = None
    for klass in oaam::library::DeviceType.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)



def test_oaam::restrictions::segregationrestriction_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::SegregationRestriction)


def test_oaam::restrictions::segregationrestriction_constructor_exists():
    assert callable(oaam::restrictions::SegregationRestriction.__init__)


def test_oaam::restrictions::segregationrestriction_constructor_args():
    sig = inspect.signature(oaam::restrictions::SegregationRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "dissimilarTechnology" in params, "Missing parameter 'dissimilarTechnology'"
    assert "dissimilarArea" in params, "Missing parameter 'dissimilarArea'"
    assert "dissimilarPowerSource" in params, "Missing parameter 'dissimilarPowerSource'"
    assert "dissimilarLocation" in params, "Missing parameter 'dissimilarLocation'"

def test_oaam::restrictions::segregationrestriction_has_dissimilarTechnology():
    assert hasattr(oaam::restrictions::SegregationRestriction, "dissimilarTechnology")
    descriptor = None
    for klass in oaam::restrictions::SegregationRestriction.__mro__:
        if "dissimilarTechnology" in klass.__dict__:
            descriptor = klass.__dict__["dissimilarTechnology"]
            break
    assert isinstance(descriptor, property)

def test_oaam::restrictions::segregationrestriction_has_dissimilarArea():
    assert hasattr(oaam::restrictions::SegregationRestriction, "dissimilarArea")
    descriptor = None
    for klass in oaam::restrictions::SegregationRestriction.__mro__:
        if "dissimilarArea" in klass.__dict__:
            descriptor = klass.__dict__["dissimilarArea"]
            break
    assert isinstance(descriptor, property)

def test_oaam::restrictions::segregationrestriction_has_dissimilarPowerSource():
    assert hasattr(oaam::restrictions::SegregationRestriction, "dissimilarPowerSource")
    descriptor = None
    for klass in oaam::restrictions::SegregationRestriction.__mro__:
        if "dissimilarPowerSource" in klass.__dict__:
            descriptor = klass.__dict__["dissimilarPowerSource"]
            break
    assert isinstance(descriptor, property)

def test_oaam::restrictions::segregationrestriction_has_dissimilarLocation():
    assert hasattr(oaam::restrictions::SegregationRestriction, "dissimilarLocation")
    descriptor = None
    for klass in oaam::restrictions::SegregationRestriction.__mro__:
        if "dissimilarLocation" in klass.__dict__:
            descriptor = klass.__dict__["dissimilarLocation"]
            break
    assert isinstance(descriptor, property)



def test_oaam::scenario::scenarioparameternumeric_is_not_abstract():
    assert not inspect.isabstract(oaam::scenario::ScenarioParameterNumeric)


def test_oaam::scenario::scenarioparameternumeric_constructor_exists():
    assert callable(oaam::scenario::ScenarioParameterNumeric.__init__)


def test_oaam::scenario::scenarioparameternumeric_constructor_args():
    sig = inspect.signature(oaam::scenario::ScenarioParameterNumeric.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oaam::scenario::scenarioparameternumeric_has_value():
    assert hasattr(oaam::scenario::ScenarioParameterNumeric, "value")
    descriptor = None
    for klass in oaam::scenario::ScenarioParameterNumeric.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oaam::library::resourcetypemodifierlevel_is_not_abstract():
    assert not inspect.isabstract(oaam::library::ResourceTypeModifierLevel)


def test_oaam::library::resourcetypemodifierlevel_constructor_exists():
    assert callable(oaam::library::ResourceTypeModifierLevel.__init__)


def test_oaam::library::resourcetypemodifierlevel_constructor_args():
    sig = inspect.signature(oaam::library::ResourceTypeModifierLevel.__init__)
    params = list(sig.parameters.keys())



def test_oaam::restrictions::devicetyperestriction_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::DeviceTypeRestriction)


def test_oaam::restrictions::devicetyperestriction_constructor_exists():
    assert callable(oaam::restrictions::DeviceTypeRestriction.__init__)


def test_oaam::restrictions::devicetyperestriction_constructor_args():
    sig = inspect.signature(oaam::restrictions::DeviceTypeRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "deviceTypeName" in params, "Missing parameter 'deviceTypeName'"
    assert "isForbidden" in params, "Missing parameter 'isForbidden'"

def test_oaam::restrictions::devicetyperestriction_has_deviceTypeName():
    assert hasattr(oaam::restrictions::DeviceTypeRestriction, "deviceTypeName")
    descriptor = None
    for klass in oaam::restrictions::DeviceTypeRestriction.__mro__:
        if "deviceTypeName" in klass.__dict__:
            descriptor = klass.__dict__["deviceTypeName"]
            break
    assert isinstance(descriptor, property)

def test_oaam::restrictions::devicetyperestriction_has_isForbidden():
    assert hasattr(oaam::restrictions::DeviceTypeRestriction, "isForbidden")
    descriptor = None
    for klass in oaam::restrictions::DeviceTypeRestriction.__mro__:
        if "isForbidden" in klass.__dict__:
            descriptor = klass.__dict__["isForbidden"]
            break
    assert isinstance(descriptor, property)



def test_oaam::restrictions::connectiontyperestriction_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::ConnectionTypeRestriction)


def test_oaam::restrictions::connectiontyperestriction_constructor_exists():
    assert callable(oaam::restrictions::ConnectionTypeRestriction.__init__)


def test_oaam::restrictions::connectiontyperestriction_constructor_args():
    sig = inspect.signature(oaam::restrictions::ConnectionTypeRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "connectionTypeName" in params, "Missing parameter 'connectionTypeName'"
    assert "isForbidden" in params, "Missing parameter 'isForbidden'"

def test_oaam::restrictions::connectiontyperestriction_has_connectionTypeName():
    assert hasattr(oaam::restrictions::ConnectionTypeRestriction, "connectionTypeName")
    descriptor = None
    for klass in oaam::restrictions::ConnectionTypeRestriction.__mro__:
        if "connectionTypeName" in klass.__dict__:
            descriptor = klass.__dict__["connectionTypeName"]
            break
    assert isinstance(descriptor, property)

def test_oaam::restrictions::connectiontyperestriction_has_isForbidden():
    assert hasattr(oaam::restrictions::ConnectionTypeRestriction, "isForbidden")
    descriptor = None
    for klass in oaam::restrictions::ConnectionTypeRestriction.__mro__:
        if "isForbidden" in klass.__dict__:
            descriptor = klass.__dict__["isForbidden"]
            break
    assert isinstance(descriptor, property)



def test_oaam::scenario::operationmode_is_not_abstract():
    assert not inspect.isabstract(oaam::scenario::OperationMode)


def test_oaam::scenario::operationmode_constructor_exists():
    assert callable(oaam::scenario::OperationMode.__init__)


def test_oaam::scenario::operationmode_constructor_args():
    sig = inspect.signature(oaam::scenario::OperationMode.__init__)
    params = list(sig.parameters.keys())



def test_oaam::hardware::device_is_not_abstract():
    assert not inspect.isabstract(oaam::hardware::Device)


def test_oaam::hardware::device_constructor_exists():
    assert callable(oaam::hardware::Device.__init__)


def test_oaam::hardware::device_constructor_args():
    sig = inspect.signature(oaam::hardware::Device.__init__)
    params = list(sig.parameters.keys())



def test_oaam::restrictions::devicerestriction_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::DeviceRestriction)


def test_oaam::restrictions::devicerestriction_constructor_exists():
    assert callable(oaam::restrictions::DeviceRestriction.__init__)


def test_oaam::restrictions::devicerestriction_constructor_args():
    sig = inspect.signature(oaam::restrictions::DeviceRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "isForbidden" in params, "Missing parameter 'isForbidden'"
    assert "deviceName" in params, "Missing parameter 'deviceName'"

def test_oaam::restrictions::devicerestriction_has_isForbidden():
    assert hasattr(oaam::restrictions::DeviceRestriction, "isForbidden")
    descriptor = None
    for klass in oaam::restrictions::DeviceRestriction.__mro__:
        if "isForbidden" in klass.__dict__:
            descriptor = klass.__dict__["isForbidden"]
            break
    assert isinstance(descriptor, property)

def test_oaam::restrictions::devicerestriction_has_deviceName():
    assert hasattr(oaam::restrictions::DeviceRestriction, "deviceName")
    descriptor = None
    for klass in oaam::restrictions::DeviceRestriction.__mro__:
        if "deviceName" in klass.__dict__:
            descriptor = klass.__dict__["deviceName"]
            break
    assert isinstance(descriptor, property)



def test_oaam::allocations::schedule_is_not_abstract():
    assert not inspect.isabstract(oaam::allocations::Schedule)


def test_oaam::allocations::schedule_constructor_exists():
    assert callable(oaam::allocations::Schedule.__init__)


def test_oaam::allocations::schedule_constructor_args():
    sig = inspect.signature(oaam::allocations::Schedule.__init__)
    params = list(sig.parameters.keys())
    assert "rate" in params, "Missing parameter 'rate'"
    assert "isPeriodic" in params, "Missing parameter 'isPeriodic'"
    assert "priority" in params, "Missing parameter 'priority'"

def test_oaam::allocations::schedule_has_rate():
    assert hasattr(oaam::allocations::Schedule, "rate")
    descriptor = None
    for klass in oaam::allocations::Schedule.__mro__:
        if "rate" in klass.__dict__:
            descriptor = klass.__dict__["rate"]
            break
    assert isinstance(descriptor, property)

def test_oaam::allocations::schedule_has_isPeriodic():
    assert hasattr(oaam::allocations::Schedule, "isPeriodic")
    descriptor = None
    for klass in oaam::allocations::Schedule.__mro__:
        if "isPeriodic" in klass.__dict__:
            descriptor = klass.__dict__["isPeriodic"]
            break
    assert isinstance(descriptor, property)

def test_oaam::allocations::schedule_has_priority():
    assert hasattr(oaam::allocations::Schedule, "priority")
    descriptor = None
    for klass in oaam::allocations::Schedule.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_oaam::systems::informationpower_is_not_abstract():
    assert not inspect.isabstract(oaam::systems::InformationPower)


def test_oaam::systems::informationpower_constructor_exists():
    assert callable(oaam::systems::InformationPower.__init__)


def test_oaam::systems::informationpower_constructor_args():
    sig = inspect.signature(oaam::systems::InformationPower.__init__)
    params = list(sig.parameters.keys())
    assert "power" in params, "Missing parameter 'power'"

def test_oaam::systems::informationpower_has_power():
    assert hasattr(oaam::systems::InformationPower, "power")
    descriptor = None
    for klass in oaam::systems::InformationPower.__mro__:
        if "power" in klass.__dict__:
            descriptor = klass.__dict__["power"]
            break
    assert isinstance(descriptor, property)



def test_oaam::restrictions::timedelayrestriction_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::TimeDelayRestriction)


def test_oaam::restrictions::timedelayrestriction_constructor_exists():
    assert callable(oaam::restrictions::TimeDelayRestriction.__init__)


def test_oaam::restrictions::timedelayrestriction_constructor_args():
    sig = inspect.signature(oaam::restrictions::TimeDelayRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "delay" in params, "Missing parameter 'delay'"

def test_oaam::restrictions::timedelayrestriction_has_delay():
    assert hasattr(oaam::restrictions::TimeDelayRestriction, "delay")
    descriptor = None
    for klass in oaam::restrictions::TimeDelayRestriction.__mro__:
        if "delay" in klass.__dict__:
            descriptor = klass.__dict__["delay"]
            break
    assert isinstance(descriptor, property)



def test_oaam::library::resourcebundle_is_not_abstract():
    assert not inspect.isabstract(oaam::library::ResourceBundle)


def test_oaam::library::resourcebundle_constructor_exists():
    assert callable(oaam::library::ResourceBundle.__init__)


def test_oaam::library::resourcebundle_constructor_args():
    sig = inspect.signature(oaam::library::ResourceBundle.__init__)
    params = list(sig.parameters.keys())
    assert "mtbf" in params, "Missing parameter 'mtbf'"
    assert "mass" in params, "Missing parameter 'mass'"
    assert "cost" in params, "Missing parameter 'cost'"

def test_oaam::library::resourcebundle_has_mtbf():
    assert hasattr(oaam::library::ResourceBundle, "mtbf")
    descriptor = None
    for klass in oaam::library::ResourceBundle.__mro__:
        if "mtbf" in klass.__dict__:
            descriptor = klass.__dict__["mtbf"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::resourcebundle_has_mass():
    assert hasattr(oaam::library::ResourceBundle, "mass")
    descriptor = None
    for klass in oaam::library::ResourceBundle.__mro__:
        if "mass" in klass.__dict__:
            descriptor = klass.__dict__["mass"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::resourcebundle_has_cost():
    assert hasattr(oaam::library::ResourceBundle, "cost")
    descriptor = None
    for klass in oaam::library::ResourceBundle.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)



def test_oaam::library::ducttype_is_not_abstract():
    assert not inspect.isabstract(oaam::library::DuctType)


def test_oaam::library::ducttype_constructor_exists():
    assert callable(oaam::library::DuctType.__init__)


def test_oaam::library::ducttype_constructor_args():
    sig = inspect.signature(oaam::library::DuctType.__init__)
    params = list(sig.parameters.keys())



def test_oaam::restrictions::powersourcerestriction_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::PowerSourceRestriction)


def test_oaam::restrictions::powersourcerestriction_constructor_exists():
    assert callable(oaam::restrictions::PowerSourceRestriction.__init__)


def test_oaam::restrictions::powersourcerestriction_constructor_args():
    sig = inspect.signature(oaam::restrictions::PowerSourceRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "powerSourceName" in params, "Missing parameter 'powerSourceName'"
    assert "isForbidden" in params, "Missing parameter 'isForbidden'"

def test_oaam::restrictions::powersourcerestriction_has_powerSourceName():
    assert hasattr(oaam::restrictions::PowerSourceRestriction, "powerSourceName")
    descriptor = None
    for klass in oaam::restrictions::PowerSourceRestriction.__mro__:
        if "powerSourceName" in klass.__dict__:
            descriptor = klass.__dict__["powerSourceName"]
            break
    assert isinstance(descriptor, property)

def test_oaam::restrictions::powersourcerestriction_has_isForbidden():
    assert hasattr(oaam::restrictions::PowerSourceRestriction, "isForbidden")
    descriptor = None
    for klass in oaam::restrictions::PowerSourceRestriction.__mro__:
        if "isForbidden" in klass.__dict__:
            descriptor = klass.__dict__["isForbidden"]
            break
    assert isinstance(descriptor, property)



def test_oaam::capabilities::signalonconnectionordevicecapability_is_not_abstract():
    assert not inspect.isabstract(oaam::capabilities::SignalOnConnectionOrDeviceCapability)


def test_oaam::capabilities::signalonconnectionordevicecapability_constructor_exists():
    assert callable(oaam::capabilities::SignalOnConnectionOrDeviceCapability.__init__)


def test_oaam::capabilities::signalonconnectionordevicecapability_constructor_args():
    sig = inspect.signature(oaam::capabilities::SignalOnConnectionOrDeviceCapability.__init__)
    params = list(sig.parameters.keys())
    assert "worstCaseTransmissionTime" in params, "Missing parameter 'worstCaseTransmissionTime'"

def test_oaam::capabilities::signalonconnectionordevicecapability_has_worstCaseTransmissionTime():
    assert hasattr(oaam::capabilities::SignalOnConnectionOrDeviceCapability, "worstCaseTransmissionTime")
    descriptor = None
    for klass in oaam::capabilities::SignalOnConnectionOrDeviceCapability.__mro__:
        if "worstCaseTransmissionTime" in klass.__dict__:
            descriptor = klass.__dict__["worstCaseTransmissionTime"]
            break
    assert isinstance(descriptor, property)



def test_oaam::functions::input_is_not_abstract():
    assert not inspect.isabstract(oaam::functions::Input)


def test_oaam::functions::input_constructor_exists():
    assert callable(oaam::functions::Input.__init__)


def test_oaam::functions::input_constructor_args():
    sig = inspect.signature(oaam::functions::Input.__init__)
    params = list(sig.parameters.keys())
    assert "queueLength" in params, "Missing parameter 'queueLength'"

def test_oaam::functions::input_has_queueLength():
    assert hasattr(oaam::functions::Input, "queueLength")
    descriptor = None
    for klass in oaam::functions::Input.__mro__:
        if "queueLength" in klass.__dict__:
            descriptor = klass.__dict__["queueLength"]
            break
    assert isinstance(descriptor, property)



def test_oaam::systems::system_is_not_abstract():
    assert not inspect.isabstract(oaam::systems::System)


def test_oaam::systems::system_constructor_exists():
    assert callable(oaam::systems::System.__init__)


def test_oaam::systems::system_constructor_args():
    sig = inspect.signature(oaam::systems::System.__init__)
    params = list(sig.parameters.keys())



def test_oaam::anatomy::ductopening_is_not_abstract():
    assert not inspect.isabstract(oaam::anatomy::DuctOpening)


def test_oaam::anatomy::ductopening_constructor_exists():
    assert callable(oaam::anatomy::DuctOpening.__init__)


def test_oaam::anatomy::ductopening_constructor_args():
    sig = inspect.signature(oaam::anatomy::DuctOpening.__init__)
    params = list(sig.parameters.keys())



def test_oaam::allocations::connectionassignmentsegment_is_not_abstract():
    assert not inspect.isabstract(oaam::allocations::ConnectionAssignmentSegment)


def test_oaam::allocations::connectionassignmentsegment_constructor_exists():
    assert callable(oaam::allocations::ConnectionAssignmentSegment.__init__)


def test_oaam::allocations::connectionassignmentsegment_constructor_args():
    sig = inspect.signature(oaam::allocations::ConnectionAssignmentSegment.__init__)
    params = list(sig.parameters.keys())



def test_oaam::functions::failurecondition_is_not_abstract():
    assert not inspect.isabstract(oaam::functions::FailureCondition)


def test_oaam::functions::failurecondition_constructor_exists():
    assert callable(oaam::functions::FailureCondition.__init__)


def test_oaam::functions::failurecondition_constructor_args():
    sig = inspect.signature(oaam::functions::FailureCondition.__init__)
    params = list(sig.parameters.keys())
    assert "maxOccurrenceProbability" in params, "Missing parameter 'maxOccurrenceProbability'"
    assert "noSingleFailure" in params, "Missing parameter 'noSingleFailure'"

def test_oaam::functions::failurecondition_has_maxOccurrenceProbability():
    assert hasattr(oaam::functions::FailureCondition, "maxOccurrenceProbability")
    descriptor = None
    for klass in oaam::functions::FailureCondition.__mro__:
        if "maxOccurrenceProbability" in klass.__dict__:
            descriptor = klass.__dict__["maxOccurrenceProbability"]
            break
    assert isinstance(descriptor, property)

def test_oaam::functions::failurecondition_has_noSingleFailure():
    assert hasattr(oaam::functions::FailureCondition, "noSingleFailure")
    descriptor = None
    for klass in oaam::functions::FailureCondition.__mro__:
        if "noSingleFailure" in klass.__dict__:
            descriptor = klass.__dict__["noSingleFailure"]
            break
    assert isinstance(descriptor, property)



def test_oaam::restrictions::tasksymmetryrestriction_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::TaskSymmetryRestriction)


def test_oaam::restrictions::tasksymmetryrestriction_constructor_exists():
    assert callable(oaam::restrictions::TaskSymmetryRestriction.__init__)


def test_oaam::restrictions::tasksymmetryrestriction_constructor_args():
    sig = inspect.signature(oaam::restrictions::TaskSymmetryRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_oaam::restrictions::tasksymmetryrestriction_has_type():
    assert hasattr(oaam::restrictions::TaskSymmetryRestriction, "type")
    descriptor = None
    for klass in oaam::restrictions::TaskSymmetryRestriction.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_oaam::allocations::subdeviceassignment_is_not_abstract():
    assert not inspect.isabstract(oaam::allocations::SubdeviceAssignment)


def test_oaam::allocations::subdeviceassignment_constructor_exists():
    assert callable(oaam::allocations::SubdeviceAssignment.__init__)


def test_oaam::allocations::subdeviceassignment_constructor_args():
    sig = inspect.signature(oaam::allocations::SubdeviceAssignment.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::connectiontype_is_not_abstract():
    assert not inspect.isabstract(oaam::library::ConnectionType)


def test_oaam::library::connectiontype_constructor_exists():
    assert callable(oaam::library::ConnectionType.__init__)


def test_oaam::library::connectiontype_constructor_args():
    sig = inspect.signature(oaam::library::ConnectionType.__init__)
    params = list(sig.parameters.keys())
    assert "maxInterfaceToJointDistance" in params, "Missing parameter 'maxInterfaceToJointDistance'"
    assert "isPower" in params, "Missing parameter 'isPower'"
    assert "isSwitched" in params, "Missing parameter 'isSwitched'"
    assert "nJoints" in params, "Missing parameter 'nJoints'"
    assert "allowsCircles" in params, "Missing parameter 'allowsCircles'"
    assert "maxJointBranches" in params, "Missing parameter 'maxJointBranches'"
    assert "isUnidirectional" in params, "Missing parameter 'isUnidirectional'"
    assert "isWireless" in params, "Missing parameter 'isWireless'"
    assert "nStartingPoints" in params, "Missing parameter 'nStartingPoints'"
    assert "directConnectionsAllowed" in params, "Missing parameter 'directConnectionsAllowed'"
    assert "maxLength" in params, "Missing parameter 'maxLength'"
    assert "requiresMaster" in params, "Missing parameter 'requiresMaster'"
    assert "isInformation" in params, "Missing parameter 'isInformation'"
    assert "nEndPoints" in params, "Missing parameter 'nEndPoints'"

def test_oaam::library::connectiontype_has_maxInterfaceToJointDistance():
    assert hasattr(oaam::library::ConnectionType, "maxInterfaceToJointDistance")
    descriptor = None
    for klass in oaam::library::ConnectionType.__mro__:
        if "maxInterfaceToJointDistance" in klass.__dict__:
            descriptor = klass.__dict__["maxInterfaceToJointDistance"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::connectiontype_has_isPower():
    assert hasattr(oaam::library::ConnectionType, "isPower")
    descriptor = None
    for klass in oaam::library::ConnectionType.__mro__:
        if "isPower" in klass.__dict__:
            descriptor = klass.__dict__["isPower"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::connectiontype_has_isSwitched():
    assert hasattr(oaam::library::ConnectionType, "isSwitched")
    descriptor = None
    for klass in oaam::library::ConnectionType.__mro__:
        if "isSwitched" in klass.__dict__:
            descriptor = klass.__dict__["isSwitched"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::connectiontype_has_nJoints():
    assert hasattr(oaam::library::ConnectionType, "nJoints")
    descriptor = None
    for klass in oaam::library::ConnectionType.__mro__:
        if "nJoints" in klass.__dict__:
            descriptor = klass.__dict__["nJoints"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::connectiontype_has_allowsCircles():
    assert hasattr(oaam::library::ConnectionType, "allowsCircles")
    descriptor = None
    for klass in oaam::library::ConnectionType.__mro__:
        if "allowsCircles" in klass.__dict__:
            descriptor = klass.__dict__["allowsCircles"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::connectiontype_has_maxJointBranches():
    assert hasattr(oaam::library::ConnectionType, "maxJointBranches")
    descriptor = None
    for klass in oaam::library::ConnectionType.__mro__:
        if "maxJointBranches" in klass.__dict__:
            descriptor = klass.__dict__["maxJointBranches"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::connectiontype_has_isUnidirectional():
    assert hasattr(oaam::library::ConnectionType, "isUnidirectional")
    descriptor = None
    for klass in oaam::library::ConnectionType.__mro__:
        if "isUnidirectional" in klass.__dict__:
            descriptor = klass.__dict__["isUnidirectional"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::connectiontype_has_isWireless():
    assert hasattr(oaam::library::ConnectionType, "isWireless")
    descriptor = None
    for klass in oaam::library::ConnectionType.__mro__:
        if "isWireless" in klass.__dict__:
            descriptor = klass.__dict__["isWireless"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::connectiontype_has_nStartingPoints():
    assert hasattr(oaam::library::ConnectionType, "nStartingPoints")
    descriptor = None
    for klass in oaam::library::ConnectionType.__mro__:
        if "nStartingPoints" in klass.__dict__:
            descriptor = klass.__dict__["nStartingPoints"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::connectiontype_has_directConnectionsAllowed():
    assert hasattr(oaam::library::ConnectionType, "directConnectionsAllowed")
    descriptor = None
    for klass in oaam::library::ConnectionType.__mro__:
        if "directConnectionsAllowed" in klass.__dict__:
            descriptor = klass.__dict__["directConnectionsAllowed"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::connectiontype_has_maxLength():
    assert hasattr(oaam::library::ConnectionType, "maxLength")
    descriptor = None
    for klass in oaam::library::ConnectionType.__mro__:
        if "maxLength" in klass.__dict__:
            descriptor = klass.__dict__["maxLength"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::connectiontype_has_requiresMaster():
    assert hasattr(oaam::library::ConnectionType, "requiresMaster")
    descriptor = None
    for klass in oaam::library::ConnectionType.__mro__:
        if "requiresMaster" in klass.__dict__:
            descriptor = klass.__dict__["requiresMaster"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::connectiontype_has_isInformation():
    assert hasattr(oaam::library::ConnectionType, "isInformation")
    descriptor = None
    for klass in oaam::library::ConnectionType.__mro__:
        if "isInformation" in klass.__dict__:
            descriptor = klass.__dict__["isInformation"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::connectiontype_has_nEndPoints():
    assert hasattr(oaam::library::ConnectionType, "nEndPoints")
    descriptor = None
    for klass in oaam::library::ConnectionType.__mro__:
        if "nEndPoints" in klass.__dict__:
            descriptor = klass.__dict__["nEndPoints"]
            break
    assert isinstance(descriptor, property)



def test_oaam::anatomy::position3d_is_not_abstract():
    assert not inspect.isabstract(oaam::anatomy::Position3D)


def test_oaam::anatomy::position3d_constructor_exists():
    assert callable(oaam::anatomy::Position3D.__init__)


def test_oaam::anatomy::position3d_constructor_args():
    sig = inspect.signature(oaam::anatomy::Position3D.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "z" in params, "Missing parameter 'z'"

def test_oaam::anatomy::position3d_has_x():
    assert hasattr(oaam::anatomy::Position3D, "x")
    descriptor = None
    for klass in oaam::anatomy::Position3D.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_oaam::anatomy::position3d_has_y():
    assert hasattr(oaam::anatomy::Position3D, "y")
    descriptor = None
    for klass in oaam::anatomy::Position3D.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_oaam::anatomy::position3d_has_z():
    assert hasattr(oaam::anatomy::Position3D, "z")
    descriptor = None
    for klass in oaam::anatomy::Position3D.__mro__:
        if "z" in klass.__dict__:
            descriptor = klass.__dict__["z"]
            break
    assert isinstance(descriptor, property)



def test_oaam::restrictions::synchronicityrestriction_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::SynchronicityRestriction)


def test_oaam::restrictions::synchronicityrestriction_constructor_exists():
    assert callable(oaam::restrictions::SynchronicityRestriction.__init__)


def test_oaam::restrictions::synchronicityrestriction_constructor_args():
    sig = inspect.signature(oaam::restrictions::SynchronicityRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "maxJitter" in params, "Missing parameter 'maxJitter'"

def test_oaam::restrictions::synchronicityrestriction_has_maxJitter():
    assert hasattr(oaam::restrictions::SynchronicityRestriction, "maxJitter")
    descriptor = None
    for klass in oaam::restrictions::SynchronicityRestriction.__mro__:
        if "maxJitter" in klass.__dict__:
            descriptor = klass.__dict__["maxJitter"]
            break
    assert isinstance(descriptor, property)



def test_oaam::restrictions::connectionrestriction_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::ConnectionRestriction)


def test_oaam::restrictions::connectionrestriction_constructor_exists():
    assert callable(oaam::restrictions::ConnectionRestriction.__init__)


def test_oaam::restrictions::connectionrestriction_constructor_args():
    sig = inspect.signature(oaam::restrictions::ConnectionRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "isForbidden" in params, "Missing parameter 'isForbidden'"
    assert "connectionName" in params, "Missing parameter 'connectionName'"

def test_oaam::restrictions::connectionrestriction_has_isForbidden():
    assert hasattr(oaam::restrictions::ConnectionRestriction, "isForbidden")
    descriptor = None
    for klass in oaam::restrictions::ConnectionRestriction.__mro__:
        if "isForbidden" in klass.__dict__:
            descriptor = klass.__dict__["isForbidden"]
            break
    assert isinstance(descriptor, property)

def test_oaam::restrictions::connectionrestriction_has_connectionName():
    assert hasattr(oaam::restrictions::ConnectionRestriction, "connectionName")
    descriptor = None
    for klass in oaam::restrictions::ConnectionRestriction.__mro__:
        if "connectionName" in klass.__dict__:
            descriptor = klass.__dict__["connectionName"]
            break
    assert isinstance(descriptor, property)



def test_oaam::systems::informationflow_is_not_abstract():
    assert not inspect.isabstract(oaam::systems::InformationFlow)


def test_oaam::systems::informationflow_constructor_exists():
    assert callable(oaam::systems::InformationFlow.__init__)


def test_oaam::systems::informationflow_constructor_args():
    sig = inspect.signature(oaam::systems::InformationFlow.__init__)
    params = list(sig.parameters.keys())



def test_oaam::capabilities::subdeviceindevicecapability_is_not_abstract():
    assert not inspect.isabstract(oaam::capabilities::SubdeviceInDeviceCapability)


def test_oaam::capabilities::subdeviceindevicecapability_constructor_exists():
    assert callable(oaam::capabilities::SubdeviceInDeviceCapability.__init__)


def test_oaam::capabilities::subdeviceindevicecapability_constructor_args():
    sig = inspect.signature(oaam::capabilities::SubdeviceInDeviceCapability.__init__)
    params = list(sig.parameters.keys())



def test_oaam::systems::informationsignal_is_not_abstract():
    assert not inspect.isabstract(oaam::systems::InformationSignal)


def test_oaam::systems::informationsignal_constructor_exists():
    assert callable(oaam::systems::InformationSignal.__init__)


def test_oaam::systems::informationsignal_constructor_args():
    sig = inspect.signature(oaam::systems::InformationSignal.__init__)
    params = list(sig.parameters.keys())
    assert "latency" in params, "Missing parameter 'latency'"
    assert "rate" in params, "Missing parameter 'rate'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "accuracy" in params, "Missing parameter 'accuracy'"
    assert "resolution" in params, "Missing parameter 'resolution'"

def test_oaam::systems::informationsignal_has_latency():
    assert hasattr(oaam::systems::InformationSignal, "latency")
    descriptor = None
    for klass in oaam::systems::InformationSignal.__mro__:
        if "latency" in klass.__dict__:
            descriptor = klass.__dict__["latency"]
            break
    assert isinstance(descriptor, property)

def test_oaam::systems::informationsignal_has_rate():
    assert hasattr(oaam::systems::InformationSignal, "rate")
    descriptor = None
    for klass in oaam::systems::InformationSignal.__mro__:
        if "rate" in klass.__dict__:
            descriptor = klass.__dict__["rate"]
            break
    assert isinstance(descriptor, property)

def test_oaam::systems::informationsignal_has_unit():
    assert hasattr(oaam::systems::InformationSignal, "unit")
    descriptor = None
    for klass in oaam::systems::InformationSignal.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_oaam::systems::informationsignal_has_accuracy():
    assert hasattr(oaam::systems::InformationSignal, "accuracy")
    descriptor = None
    for klass in oaam::systems::InformationSignal.__mro__:
        if "accuracy" in klass.__dict__:
            descriptor = klass.__dict__["accuracy"]
            break
    assert isinstance(descriptor, property)

def test_oaam::systems::informationsignal_has_resolution():
    assert hasattr(oaam::systems::InformationSignal, "resolution")
    descriptor = None
    for klass in oaam::systems::InformationSignal.__mro__:
        if "resolution" in klass.__dict__:
            descriptor = klass.__dict__["resolution"]
            break
    assert isinstance(descriptor, property)



def test_oaam::allocations::signalassignment_is_not_abstract():
    assert not inspect.isabstract(oaam::allocations::SignalAssignment)


def test_oaam::allocations::signalassignment_constructor_exists():
    assert callable(oaam::allocations::SignalAssignment.__init__)


def test_oaam::allocations::signalassignment_constructor_args():
    sig = inspect.signature(oaam::allocations::SignalAssignment.__init__)
    params = list(sig.parameters.keys())



def test_oaam::capabilities::messageonconnectionordevicecapability_is_not_abstract():
    assert not inspect.isabstract(oaam::capabilities::MessageOnConnectionOrDeviceCapability)


def test_oaam::capabilities::messageonconnectionordevicecapability_constructor_exists():
    assert callable(oaam::capabilities::MessageOnConnectionOrDeviceCapability.__init__)


def test_oaam::capabilities::messageonconnectionordevicecapability_constructor_args():
    sig = inspect.signature(oaam::capabilities::MessageOnConnectionOrDeviceCapability.__init__)
    params = list(sig.parameters.keys())
    assert "worstCaseTransmissionTime" in params, "Missing parameter 'worstCaseTransmissionTime'"

def test_oaam::capabilities::messageonconnectionordevicecapability_has_worstCaseTransmissionTime():
    assert hasattr(oaam::capabilities::MessageOnConnectionOrDeviceCapability, "worstCaseTransmissionTime")
    descriptor = None
    for klass in oaam::capabilities::MessageOnConnectionOrDeviceCapability.__mro__:
        if "worstCaseTransmissionTime" in klass.__dict__:
            descriptor = klass.__dict__["worstCaseTransmissionTime"]
            break
    assert isinstance(descriptor, property)



def test_oaam::functions::signalgroup_is_not_abstract():
    assert not inspect.isabstract(oaam::functions::SignalGroup)


def test_oaam::functions::signalgroup_constructor_exists():
    assert callable(oaam::functions::SignalGroup.__init__)


def test_oaam::functions::signalgroup_constructor_args():
    sig = inspect.signature(oaam::functions::SignalGroup.__init__)
    params = list(sig.parameters.keys())



def test_common::boola_is_not_abstract():
    assert not inspect.isabstract(common::BoolA)


def test_common::boola_constructor_exists():
    assert callable(common::BoolA.__init__)


def test_common::boola_constructor_args():
    sig = inspect.signature(common::BoolA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::taskinputstate_is_not_abstract():
    assert not inspect.isabstract(oaam::library::TaskInputState)


def test_oaam::library::taskinputstate_constructor_exists():
    assert callable(oaam::library::TaskInputState.__init__)


def test_oaam::library::taskinputstate_constructor_args():
    sig = inspect.signature(oaam::library::TaskInputState.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"

def test_oaam::library::taskinputstate_has_state():
    assert hasattr(oaam::library::TaskInputState, "state")
    descriptor = None
    for klass in oaam::library::TaskInputState.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)



def test_oaam::functions::outputintegritystate_is_not_abstract():
    assert not inspect.isabstract(oaam::functions::OutputIntegrityState)


def test_oaam::functions::outputintegritystate_constructor_exists():
    assert callable(oaam::functions::OutputIntegrityState.__init__)


def test_oaam::functions::outputintegritystate_constructor_args():
    sig = inspect.signature(oaam::functions::OutputIntegrityState.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"

def test_oaam::functions::outputintegritystate_has_state():
    assert hasattr(oaam::functions::OutputIntegrityState, "state")
    descriptor = None
    for klass in oaam::functions::OutputIntegrityState.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)



def test_oaam::common::boolnot_is_not_abstract():
    assert not inspect.isabstract(oaam::common::BoolNot)


def test_oaam::common::boolnot_constructor_exists():
    assert callable(oaam::common::BoolNot.__init__)


def test_oaam::common::boolnot_constructor_args():
    sig = inspect.signature(oaam::common::BoolNot.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::taskinputtrigger_is_not_abstract():
    assert not inspect.isabstract(oaam::library::TaskInputTrigger)


def test_oaam::library::taskinputtrigger_constructor_exists():
    assert callable(oaam::library::TaskInputTrigger.__init__)


def test_oaam::library::taskinputtrigger_constructor_args():
    sig = inspect.signature(oaam::library::TaskInputTrigger.__init__)
    params = list(sig.parameters.keys())



def test_oaam::common::booloperation_is_not_abstract():
    assert not inspect.isabstract(oaam::common::BoolOperation)


def test_oaam::common::booloperation_constructor_exists():
    assert callable(oaam::common::BoolOperation.__init__)


def test_oaam::common::booloperation_constructor_args():
    sig = inspect.signature(oaam::common::BoolOperation.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_oaam::common::booloperation_has_type():
    assert hasattr(oaam::common::BoolOperation, "type")
    descriptor = None
    for klass in oaam::common::BoolOperation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_oaam::common::boola_is_not_abstract():
    assert not inspect.isabstract(oaam::common::BoolA)


def test_oaam::common::boola_constructor_exists():
    assert callable(oaam::common::BoolA.__init__)


def test_oaam::common::boola_constructor_args():
    sig = inspect.signature(oaam::common::BoolA.__init__)
    params = list(sig.parameters.keys())



def test_attributea_is_not_abstract():
    assert not inspect.isabstract(AttributeA)


def test_attributea_constructor_exists():
    assert callable(AttributeA.__init__)


def test_attributea_constructor_args():
    sig = inspect.signature(AttributeA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::common::attributereference_is_not_abstract():
    assert not inspect.isabstract(oaam::common::AttributeReference)


def test_oaam::common::attributereference_constructor_exists():
    assert callable(oaam::common::AttributeReference.__init__)


def test_oaam::common::attributereference_constructor_args():
    sig = inspect.signature(oaam::common::AttributeReference.__init__)
    params = list(sig.parameters.keys())



def test_oaam::common::attributenumeric_is_not_abstract():
    assert not inspect.isabstract(oaam::common::AttributeNumeric)


def test_oaam::common::attributenumeric_constructor_exists():
    assert callable(oaam::common::AttributeNumeric.__init__)


def test_oaam::common::attributenumeric_constructor_args():
    sig = inspect.signature(oaam::common::AttributeNumeric.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oaam::common::attributenumeric_has_value():
    assert hasattr(oaam::common::AttributeNumeric, "value")
    descriptor = None
    for klass in oaam::common::AttributeNumeric.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oaam::common::attributestring_is_not_abstract():
    assert not inspect.isabstract(oaam::common::AttributeString)


def test_oaam::common::attributestring_constructor_exists():
    assert callable(oaam::common::AttributeString.__init__)


def test_oaam::common::attributestring_constructor_args():
    sig = inspect.signature(oaam::common::AttributeString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oaam::common::attributestring_has_value():
    assert hasattr(oaam::common::AttributeString, "value")
    descriptor = None
    for klass in oaam::common::AttributeString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oaam::common::attributecontainment_is_not_abstract():
    assert not inspect.isabstract(oaam::common::AttributeContainment)


def test_oaam::common::attributecontainment_constructor_exists():
    assert callable(oaam::common::AttributeContainment.__init__)


def test_oaam::common::attributecontainment_constructor_args():
    sig = inspect.signature(oaam::common::AttributeContainment.__init__)
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



def test_oaam::common::oaambaseelementa_is_not_abstract():
    assert not inspect.isabstract(oaam::common::OaamBaseElementA)


def test_oaam::common::oaambaseelementa_constructor_exists():
    assert callable(oaam::common::OaamBaseElementA.__init__)


def test_oaam::common::oaambaseelementa_constructor_args():
    sig = inspect.signature(oaam::common::OaamBaseElementA.__init__)
    params = list(sig.parameters.keys())
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "id" in params, "Missing parameter 'id'"
    assert "modified" in params, "Missing parameter 'modified'"
    assert "style" in params, "Missing parameter 'style'"
    assert "name" in params, "Missing parameter 'name'"
    assert "modifier" in params, "Missing parameter 'modifier'"
    assert "traceLink" in params, "Missing parameter 'traceLink'"

def test_oaam::common::oaambaseelementa_has_documentation():
    assert hasattr(oaam::common::OaamBaseElementA, "documentation")
    descriptor = None
    for klass in oaam::common::OaamBaseElementA.__mro__:
        if "documentation" in klass.__dict__:
            descriptor = klass.__dict__["documentation"]
            break
    assert isinstance(descriptor, property)

def test_oaam::common::oaambaseelementa_has_id():
    assert hasattr(oaam::common::OaamBaseElementA, "id")
    descriptor = None
    for klass in oaam::common::OaamBaseElementA.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_oaam::common::oaambaseelementa_has_modified():
    assert hasattr(oaam::common::OaamBaseElementA, "modified")
    descriptor = None
    for klass in oaam::common::OaamBaseElementA.__mro__:
        if "modified" in klass.__dict__:
            descriptor = klass.__dict__["modified"]
            break
    assert isinstance(descriptor, property)

def test_oaam::common::oaambaseelementa_has_style():
    assert hasattr(oaam::common::OaamBaseElementA, "style")
    descriptor = None
    for klass in oaam::common::OaamBaseElementA.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_oaam::common::oaambaseelementa_has_name():
    assert hasattr(oaam::common::OaamBaseElementA, "name")
    descriptor = None
    for klass in oaam::common::OaamBaseElementA.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_oaam::common::oaambaseelementa_has_modifier():
    assert hasattr(oaam::common::OaamBaseElementA, "modifier")
    descriptor = None
    for klass in oaam::common::OaamBaseElementA.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)

def test_oaam::common::oaambaseelementa_has_traceLink():
    assert hasattr(oaam::common::OaamBaseElementA, "traceLink")
    descriptor = None
    for klass in oaam::common::OaamBaseElementA.__mro__:
        if "traceLink" in klass.__dict__:
            descriptor = klass.__dict__["traceLink"]
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



def test_oaam::library::resourcetypemodifier_is_not_abstract():
    assert not inspect.isabstract(oaam::library::ResourceTypeModifier)


def test_oaam::library::resourcetypemodifier_constructor_exists():
    assert callable(oaam::library::ResourceTypeModifier.__init__)


def test_oaam::library::resourcetypemodifier_constructor_args():
    sig = inspect.signature(oaam::library::ResourceTypeModifier.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::taskstatedeclaration_is_not_abstract():
    assert not inspect.isabstract(oaam::library::TaskStateDeclaration)


def test_oaam::library::taskstatedeclaration_constructor_exists():
    assert callable(oaam::library::TaskStateDeclaration.__init__)


def test_oaam::library::taskstatedeclaration_constructor_args():
    sig = inspect.signature(oaam::library::TaskStateDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::ductopeningdeclaration_is_not_abstract():
    assert not inspect.isabstract(oaam::library::DuctOpeningDeclaration)


def test_oaam::library::ductopeningdeclaration_constructor_exists():
    assert callable(oaam::library::DuctOpeningDeclaration.__init__)


def test_oaam::library::ductopeningdeclaration_constructor_args():
    sig = inspect.signature(oaam::library::DuctOpeningDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::resourcegroup_is_not_abstract():
    assert not inspect.isabstract(oaam::library::ResourceGroup)


def test_oaam::library::resourcegroup_constructor_exists():
    assert callable(oaam::library::ResourceGroup.__init__)


def test_oaam::library::resourcegroup_constructor_args():
    sig = inspect.signature(oaam::library::ResourceGroup.__init__)
    params = list(sig.parameters.keys())



def test_oaam::scenario::scenariocontainera_is_not_abstract():
    assert not inspect.isabstract(oaam::scenario::ScenarioContainerA)


def test_oaam::scenario::scenariocontainera_constructor_exists():
    assert callable(oaam::scenario::ScenarioContainerA.__init__)


def test_oaam::scenario::scenariocontainera_constructor_args():
    sig = inspect.signature(oaam::scenario::ScenarioContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::devicetypedissimilarity_is_not_abstract():
    assert not inspect.isabstract(oaam::library::DeviceTypeDissimilarity)


def test_oaam::library::devicetypedissimilarity_constructor_exists():
    assert callable(oaam::library::DeviceTypeDissimilarity.__init__)


def test_oaam::library::devicetypedissimilarity_constructor_args():
    sig = inspect.signature(oaam::library::DeviceTypeDissimilarity.__init__)
    params = list(sig.parameters.keys())
    assert "percentageOfCommonHardware" in params, "Missing parameter 'percentageOfCommonHardware'"

def test_oaam::library::devicetypedissimilarity_has_percentageOfCommonHardware():
    assert hasattr(oaam::library::DeviceTypeDissimilarity, "percentageOfCommonHardware")
    descriptor = None
    for klass in oaam::library::DeviceTypeDissimilarity.__mro__:
        if "percentageOfCommonHardware" in klass.__dict__:
            descriptor = klass.__dict__["percentageOfCommonHardware"]
            break
    assert isinstance(descriptor, property)



def test_oaam::common::attributea_is_not_abstract():
    assert not inspect.isabstract(oaam::common::AttributeA)


def test_oaam::common::attributea_constructor_exists():
    assert callable(oaam::common::AttributeA.__init__)


def test_oaam::common::attributea_constructor_args():
    sig = inspect.signature(oaam::common::AttributeA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::wiretype_is_not_abstract():
    assert not inspect.isabstract(oaam::library::WireType)


def test_oaam::library::wiretype_constructor_exists():
    assert callable(oaam::library::WireType.__init__)


def test_oaam::library::wiretype_constructor_args():
    sig = inspect.signature(oaam::library::WireType.__init__)
    params = list(sig.parameters.keys())
    assert "specificWeight" in params, "Missing parameter 'specificWeight'"
    assert "mtbf" in params, "Missing parameter 'mtbf'"
    assert "specificPrice" in params, "Missing parameter 'specificPrice'"
    assert "minBendingRadius" in params, "Missing parameter 'minBendingRadius'"
    assert "nShields" in params, "Missing parameter 'nShields'"
    assert "nConductors" in params, "Missing parameter 'nConductors'"

def test_oaam::library::wiretype_has_specificWeight():
    assert hasattr(oaam::library::WireType, "specificWeight")
    descriptor = None
    for klass in oaam::library::WireType.__mro__:
        if "specificWeight" in klass.__dict__:
            descriptor = klass.__dict__["specificWeight"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::wiretype_has_mtbf():
    assert hasattr(oaam::library::WireType, "mtbf")
    descriptor = None
    for klass in oaam::library::WireType.__mro__:
        if "mtbf" in klass.__dict__:
            descriptor = klass.__dict__["mtbf"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::wiretype_has_specificPrice():
    assert hasattr(oaam::library::WireType, "specificPrice")
    descriptor = None
    for klass in oaam::library::WireType.__mro__:
        if "specificPrice" in klass.__dict__:
            descriptor = klass.__dict__["specificPrice"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::wiretype_has_minBendingRadius():
    assert hasattr(oaam::library::WireType, "minBendingRadius")
    descriptor = None
    for klass in oaam::library::WireType.__mro__:
        if "minBendingRadius" in klass.__dict__:
            descriptor = klass.__dict__["minBendingRadius"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::wiretype_has_nShields():
    assert hasattr(oaam::library::WireType, "nShields")
    descriptor = None
    for klass in oaam::library::WireType.__mro__:
        if "nShields" in klass.__dict__:
            descriptor = klass.__dict__["nShields"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::wiretype_has_nConductors():
    assert hasattr(oaam::library::WireType, "nConductors")
    descriptor = None
    for klass in oaam::library::WireType.__mro__:
        if "nConductors" in klass.__dict__:
            descriptor = klass.__dict__["nConductors"]
            break
    assert isinstance(descriptor, property)



def test_oaam::library::inputdeclaration_is_not_abstract():
    assert not inspect.isabstract(oaam::library::InputDeclaration)


def test_oaam::library::inputdeclaration_constructor_exists():
    assert callable(oaam::library::InputDeclaration.__init__)


def test_oaam::library::inputdeclaration_constructor_args():
    sig = inspect.signature(oaam::library::InputDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "range" in params, "Missing parameter 'range'"

def test_oaam::library::inputdeclaration_has_precondition():
    assert hasattr(oaam::library::InputDeclaration, "precondition")
    descriptor = None
    for klass in oaam::library::InputDeclaration.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::inputdeclaration_has_unit():
    assert hasattr(oaam::library::InputDeclaration, "unit")
    descriptor = None
    for klass in oaam::library::InputDeclaration.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::inputdeclaration_has_lowerBound():
    assert hasattr(oaam::library::InputDeclaration, "lowerBound")
    descriptor = None
    for klass in oaam::library::InputDeclaration.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::inputdeclaration_has_upperBound():
    assert hasattr(oaam::library::InputDeclaration, "upperBound")
    descriptor = None
    for klass in oaam::library::InputDeclaration.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::inputdeclaration_has_range():
    assert hasattr(oaam::library::InputDeclaration, "range")
    descriptor = None
    for klass in oaam::library::InputDeclaration.__mro__:
        if "range" in klass.__dict__:
            descriptor = klass.__dict__["range"]
            break
    assert isinstance(descriptor, property)



def test_oaam::library::librarycontainera_is_not_abstract():
    assert not inspect.isabstract(oaam::library::LibraryContainerA)


def test_oaam::library::librarycontainera_constructor_exists():
    assert callable(oaam::library::LibraryContainerA.__init__)


def test_oaam::library::librarycontainera_constructor_args():
    sig = inspect.signature(oaam::library::LibraryContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::attributedefinition_is_not_abstract():
    assert not inspect.isabstract(oaam::library::AttributeDefinition)


def test_oaam::library::attributedefinition_constructor_exists():
    assert callable(oaam::library::AttributeDefinition.__init__)


def test_oaam::library::attributedefinition_constructor_args():
    sig = inspect.signature(oaam::library::AttributeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"
    assert "target" in params, "Missing parameter 'target'"

def test_oaam::library::attributedefinition_has_dataType():
    assert hasattr(oaam::library::AttributeDefinition, "dataType")
    descriptor = None
    for klass in oaam::library::AttributeDefinition.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::attributedefinition_has_target():
    assert hasattr(oaam::library::AttributeDefinition, "target")
    descriptor = None
    for klass in oaam::library::AttributeDefinition.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)



def test_oaam::library::resourcelink_is_not_abstract():
    assert not inspect.isabstract(oaam::library::ResourceLink)


def test_oaam::library::resourcelink_constructor_exists():
    assert callable(oaam::library::ResourceLink.__init__)


def test_oaam::library::resourcelink_constructor_args():
    sig = inspect.signature(oaam::library::ResourceLink.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::iodeclaration_is_not_abstract():
    assert not inspect.isabstract(oaam::library::IoDeclaration)


def test_oaam::library::iodeclaration_constructor_exists():
    assert callable(oaam::library::IoDeclaration.__init__)


def test_oaam::library::iodeclaration_constructor_args():
    sig = inspect.signature(oaam::library::IoDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::resourcetypemodifierreference_is_not_abstract():
    assert not inspect.isabstract(oaam::library::ResourceTypeModifierReference)


def test_oaam::library::resourcetypemodifierreference_constructor_exists():
    assert callable(oaam::library::ResourceTypeModifierReference.__init__)


def test_oaam::library::resourcetypemodifierreference_constructor_args():
    sig = inspect.signature(oaam::library::ResourceTypeModifierReference.__init__)
    params = list(sig.parameters.keys())



def test_oaam::systems::inputsegregation_is_not_abstract():
    assert not inspect.isabstract(oaam::systems::InputSegregation)


def test_oaam::systems::inputsegregation_constructor_exists():
    assert callable(oaam::systems::InputSegregation.__init__)


def test_oaam::systems::inputsegregation_constructor_args():
    sig = inspect.signature(oaam::systems::InputSegregation.__init__)
    params = list(sig.parameters.keys())
    assert "dissimilarRoute" in params, "Missing parameter 'dissimilarRoute'"
    assert "dissimilarSource" in params, "Missing parameter 'dissimilarSource'"
    assert "dissimilarTechnology" in params, "Missing parameter 'dissimilarTechnology'"

def test_oaam::systems::inputsegregation_has_dissimilarRoute():
    assert hasattr(oaam::systems::InputSegregation, "dissimilarRoute")
    descriptor = None
    for klass in oaam::systems::InputSegregation.__mro__:
        if "dissimilarRoute" in klass.__dict__:
            descriptor = klass.__dict__["dissimilarRoute"]
            break
    assert isinstance(descriptor, property)

def test_oaam::systems::inputsegregation_has_dissimilarSource():
    assert hasattr(oaam::systems::InputSegregation, "dissimilarSource")
    descriptor = None
    for klass in oaam::systems::InputSegregation.__mro__:
        if "dissimilarSource" in klass.__dict__:
            descriptor = klass.__dict__["dissimilarSource"]
            break
    assert isinstance(descriptor, property)

def test_oaam::systems::inputsegregation_has_dissimilarTechnology():
    assert hasattr(oaam::systems::InputSegregation, "dissimilarTechnology")
    descriptor = None
    for klass in oaam::systems::InputSegregation.__mro__:
        if "dissimilarTechnology" in klass.__dict__:
            descriptor = klass.__dict__["dissimilarTechnology"]
            break
    assert isinstance(descriptor, property)



def test_oaam::functions::taskparameter_is_not_abstract():
    assert not inspect.isabstract(oaam::functions::TaskParameter)


def test_oaam::functions::taskparameter_constructor_exists():
    assert callable(oaam::functions::TaskParameter.__init__)


def test_oaam::functions::taskparameter_constructor_args():
    sig = inspect.signature(oaam::functions::TaskParameter.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oaam::functions::taskparameter_has_value():
    assert hasattr(oaam::functions::TaskParameter, "value")
    descriptor = None
    for klass in oaam::functions::TaskParameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oaam::library::faultpropagation_is_not_abstract():
    assert not inspect.isabstract(oaam::library::FaultPropagation)


def test_oaam::library::faultpropagation_constructor_exists():
    assert callable(oaam::library::FaultPropagation.__init__)


def test_oaam::library::faultpropagation_constructor_args():
    sig = inspect.signature(oaam::library::FaultPropagation.__init__)
    params = list(sig.parameters.keys())
    assert "outputState" in params, "Missing parameter 'outputState'"

def test_oaam::library::faultpropagation_has_outputState():
    assert hasattr(oaam::library::FaultPropagation, "outputState")
    descriptor = None
    for klass in oaam::library::FaultPropagation.__mro__:
        if "outputState" in klass.__dict__:
            descriptor = klass.__dict__["outputState"]
            break
    assert isinstance(descriptor, property)



def test_oaam::library::resource_is_not_abstract():
    assert not inspect.isabstract(oaam::library::Resource)


def test_oaam::library::resource_constructor_exists():
    assert callable(oaam::library::Resource.__init__)


def test_oaam::library::resource_constructor_args():
    sig = inspect.signature(oaam::library::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_oaam::library::resource_has_count():
    assert hasattr(oaam::library::Resource, "count")
    descriptor = None
    for klass in oaam::library::Resource.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_oaam::systems::systemscontainera_is_not_abstract():
    assert not inspect.isabstract(oaam::systems::SystemsContainerA)


def test_oaam::systems::systemscontainera_constructor_exists():
    assert callable(oaam::systems::SystemsContainerA.__init__)


def test_oaam::systems::systemscontainera_constructor_args():
    sig = inspect.signature(oaam::systems::SystemsContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::hardware::hardwarecontainera_is_not_abstract():
    assert not inspect.isabstract(oaam::hardware::HardwareContainerA)


def test_oaam::hardware::hardwarecontainera_constructor_exists():
    assert callable(oaam::hardware::HardwareContainerA.__init__)


def test_oaam::hardware::hardwarecontainera_constructor_args():
    sig = inspect.signature(oaam::hardware::HardwareContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::restrictions::restrictionscontainera_is_not_abstract():
    assert not inspect.isabstract(oaam::restrictions::RestrictionsContainerA)


def test_oaam::restrictions::restrictionscontainera_constructor_exists():
    assert callable(oaam::restrictions::RestrictionsContainerA.__init__)


def test_oaam::restrictions::restrictionscontainera_constructor_args():
    sig = inspect.signature(oaam::restrictions::RestrictionsContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::capabilities::capabilitiescontainera_is_not_abstract():
    assert not inspect.isabstract(oaam::capabilities::CapabilitiesContainerA)


def test_oaam::capabilities::capabilitiescontainera_constructor_exists():
    assert callable(oaam::capabilities::CapabilitiesContainerA.__init__)


def test_oaam::capabilities::capabilitiescontainera_constructor_args():
    sig = inspect.signature(oaam::capabilities::CapabilitiesContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::tasktypedissimilarity_is_not_abstract():
    assert not inspect.isabstract(oaam::library::TaskTypeDissimilarity)


def test_oaam::library::tasktypedissimilarity_constructor_exists():
    assert callable(oaam::library::TaskTypeDissimilarity.__init__)


def test_oaam::library::tasktypedissimilarity_constructor_args():
    sig = inspect.signature(oaam::library::TaskTypeDissimilarity.__init__)
    params = list(sig.parameters.keys())
    assert "percentageOfCommonCode" in params, "Missing parameter 'percentageOfCommonCode'"

def test_oaam::library::tasktypedissimilarity_has_percentageOfCommonCode():
    assert hasattr(oaam::library::TaskTypeDissimilarity, "percentageOfCommonCode")
    descriptor = None
    for klass in oaam::library::TaskTypeDissimilarity.__mro__:
        if "percentageOfCommonCode" in klass.__dict__:
            descriptor = klass.__dict__["percentageOfCommonCode"]
            break
    assert isinstance(descriptor, property)



def test_oaam::scenario::operationmodereference_is_not_abstract():
    assert not inspect.isabstract(oaam::scenario::OperationModeReference)


def test_oaam::scenario::operationmodereference_constructor_exists():
    assert callable(oaam::scenario::OperationModeReference.__init__)


def test_oaam::scenario::operationmodereference_constructor_args():
    sig = inspect.signature(oaam::scenario::OperationModeReference.__init__)
    params = list(sig.parameters.keys())
    assert "activeProbability" in params, "Missing parameter 'activeProbability'"

def test_oaam::scenario::operationmodereference_has_activeProbability():
    assert hasattr(oaam::scenario::OperationModeReference, "activeProbability")
    descriptor = None
    for klass in oaam::scenario::OperationModeReference.__mro__:
        if "activeProbability" in klass.__dict__:
            descriptor = klass.__dict__["activeProbability"]
            break
    assert isinstance(descriptor, property)



def test_oaam::allocations::allocationscontainera_is_not_abstract():
    assert not inspect.isabstract(oaam::allocations::AllocationsContainerA)


def test_oaam::allocations::allocationscontainera_constructor_exists():
    assert callable(oaam::allocations::AllocationsContainerA.__init__)


def test_oaam::allocations::allocationscontainera_constructor_args():
    sig = inspect.signature(oaam::allocations::AllocationsContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::capabilities::resourceconsumption_is_not_abstract():
    assert not inspect.isabstract(oaam::capabilities::ResourceConsumption)


def test_oaam::capabilities::resourceconsumption_constructor_exists():
    assert callable(oaam::capabilities::ResourceConsumption.__init__)


def test_oaam::capabilities::resourceconsumption_constructor_args():
    sig = inspect.signature(oaam::capabilities::ResourceConsumption.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_oaam::capabilities::resourceconsumption_has_count():
    assert hasattr(oaam::capabilities::ResourceConsumption, "count")
    descriptor = None
    for klass in oaam::capabilities::ResourceConsumption.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_oaam::library::iogroup_is_not_abstract():
    assert not inspect.isabstract(oaam::library::IoGroup)


def test_oaam::library::iogroup_constructor_exists():
    assert callable(oaam::library::IoGroup.__init__)


def test_oaam::library::iogroup_constructor_args():
    sig = inspect.signature(oaam::library::IoGroup.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::outputdeclaration_is_not_abstract():
    assert not inspect.isabstract(oaam::library::OutputDeclaration)


def test_oaam::library::outputdeclaration_constructor_exists():
    assert callable(oaam::library::OutputDeclaration.__init__)


def test_oaam::library::outputdeclaration_constructor_args():
    sig = inspect.signature(oaam::library::OutputDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "postcondition" in params, "Missing parameter 'postcondition'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "range" in params, "Missing parameter 'range'"

def test_oaam::library::outputdeclaration_has_lowerBound():
    assert hasattr(oaam::library::OutputDeclaration, "lowerBound")
    descriptor = None
    for klass in oaam::library::OutputDeclaration.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::outputdeclaration_has_upperBound():
    assert hasattr(oaam::library::OutputDeclaration, "upperBound")
    descriptor = None
    for klass in oaam::library::OutputDeclaration.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::outputdeclaration_has_postcondition():
    assert hasattr(oaam::library::OutputDeclaration, "postcondition")
    descriptor = None
    for klass in oaam::library::OutputDeclaration.__mro__:
        if "postcondition" in klass.__dict__:
            descriptor = klass.__dict__["postcondition"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::outputdeclaration_has_unit():
    assert hasattr(oaam::library::OutputDeclaration, "unit")
    descriptor = None
    for klass in oaam::library::OutputDeclaration.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::outputdeclaration_has_range():
    assert hasattr(oaam::library::OutputDeclaration, "range")
    descriptor = None
    for klass in oaam::library::OutputDeclaration.__mro__:
        if "range" in klass.__dict__:
            descriptor = klass.__dict__["range"]
            break
    assert isinstance(descriptor, property)



def test_oaam::library::resourcealternatives_is_not_abstract():
    assert not inspect.isabstract(oaam::library::ResourceAlternatives)


def test_oaam::library::resourcealternatives_constructor_exists():
    assert callable(oaam::library::ResourceAlternatives.__init__)


def test_oaam::library::resourcealternatives_constructor_args():
    sig = inspect.signature(oaam::library::ResourceAlternatives.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::taskoutputtrigger_is_not_abstract():
    assert not inspect.isabstract(oaam::library::TaskOutputTrigger)


def test_oaam::library::taskoutputtrigger_constructor_exists():
    assert callable(oaam::library::TaskOutputTrigger.__init__)


def test_oaam::library::taskoutputtrigger_constructor_args():
    sig = inspect.signature(oaam::library::TaskOutputTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "fixedRate" in params, "Missing parameter 'fixedRate'"
    assert "isFixedRate" in params, "Missing parameter 'isFixedRate'"

def test_oaam::library::taskoutputtrigger_has_fixedRate():
    assert hasattr(oaam::library::TaskOutputTrigger, "fixedRate")
    descriptor = None
    for klass in oaam::library::TaskOutputTrigger.__mro__:
        if "fixedRate" in klass.__dict__:
            descriptor = klass.__dict__["fixedRate"]
            break
    assert isinstance(descriptor, property)

def test_oaam::library::taskoutputtrigger_has_isFixedRate():
    assert hasattr(oaam::library::TaskOutputTrigger, "isFixedRate")
    descriptor = None
    for klass in oaam::library::TaskOutputTrigger.__mro__:
        if "isFixedRate" in klass.__dict__:
            descriptor = klass.__dict__["isFixedRate"]
            break
    assert isinstance(descriptor, property)



def test_oaam::library::iotype_is_not_abstract():
    assert not inspect.isabstract(oaam::library::IoType)


def test_oaam::library::iotype_constructor_exists():
    assert callable(oaam::library::IoType.__init__)


def test_oaam::library::iotype_constructor_args():
    sig = inspect.signature(oaam::library::IoType.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_oaam::library::iotype_has_direction():
    assert hasattr(oaam::library::IoType, "direction")
    descriptor = None
    for klass in oaam::library::IoType.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_oaam::library::powersource_is_not_abstract():
    assert not inspect.isabstract(oaam::library::PowerSource)


def test_oaam::library::powersource_constructor_exists():
    assert callable(oaam::library::PowerSource.__init__)


def test_oaam::library::powersource_constructor_args():
    sig = inspect.signature(oaam::library::PowerSource.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::devicetypesymmetry_is_not_abstract():
    assert not inspect.isabstract(oaam::library::DeviceTypeSymmetry)


def test_oaam::library::devicetypesymmetry_constructor_exists():
    assert callable(oaam::library::DeviceTypeSymmetry.__init__)


def test_oaam::library::devicetypesymmetry_constructor_args():
    sig = inspect.signature(oaam::library::DeviceTypeSymmetry.__init__)
    params = list(sig.parameters.keys())



def test_oaam::common::datatypea_is_not_abstract():
    assert not inspect.isabstract(oaam::common::DataTypeA)


def test_oaam::common::datatypea_constructor_exists():
    assert callable(oaam::common::DataTypeA.__init__)


def test_oaam::common::datatypea_constructor_args():
    sig = inspect.signature(oaam::common::DataTypeA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::taskparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(oaam::library::TaskParameterDeclaration)


def test_oaam::library::taskparameterdeclaration_constructor_exists():
    assert callable(oaam::library::TaskParameterDeclaration.__init__)


def test_oaam::library::taskparameterdeclaration_constructor_args():
    sig = inspect.signature(oaam::library::TaskParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_oaam::library::resourcetypedissimilarity_is_not_abstract():
    assert not inspect.isabstract(oaam::library::ResourceTypeDissimilarity)


def test_oaam::library::resourcetypedissimilarity_constructor_exists():
    assert callable(oaam::library::ResourceTypeDissimilarity.__init__)


def test_oaam::library::resourcetypedissimilarity_constructor_args():
    sig = inspect.signature(oaam::library::ResourceTypeDissimilarity.__init__)
    params = list(sig.parameters.keys())



def test_oaam::anatomy::anatomycontainera_is_not_abstract():
    assert not inspect.isabstract(oaam::anatomy::AnatomyContainerA)


def test_oaam::anatomy::anatomycontainera_constructor_exists():
    assert callable(oaam::anatomy::AnatomyContainerA.__init__)


def test_oaam::anatomy::anatomycontainera_constructor_args():
    sig = inspect.signature(oaam::anatomy::AnatomyContainerA.__init__)
    params = list(sig.parameters.keys())



def test_oaam::architecture_is_not_abstract():
    assert not inspect.isabstract(oaam::Architecture)


def test_oaam::architecture_constructor_exists():
    assert callable(oaam::Architecture.__init__)


def test_oaam::architecture_constructor_args():
    sig = inspect.signature(oaam::Architecture.__init__)
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

def test_symmetrytypese_exists():
    # Check that the Enumeration exists
    assert SymmetryTypesE is not None

def test_symmetrytypese_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SymmetryTypesE]
    expected_literals = [
        "DEVICE",
        "AREA",
        "DEVICE_TYPE",
        "LOCATION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SymmetryTypesE"

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

def test_attributetargetse_exists():
    # Check that the Enumeration exists
    assert AttributeTargetsE is not None

def test_attributetargetse_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AttributeTargetsE]
    expected_literals = [
        "SIGNAL",
        "RESOURCE_BUNDLE",
        "RESOURCE",
        "SIGNAL_TYPE",
        "TASK_TYPE",
        "RESOURCE_TYPE",
        "AREA",
        "WIRE_TYPE",
        "DEVICE",
        "CONNECTION_TYPE",
        "CONNECTION",
        "LOCATION_TYPE",
        "RESOURCE_ALTERNATIVE",
        "RESOURCE_GROUP",
        "VARIANT",
        "TASK",
        "DUCT_TYPE",
        "LOCATION",
        "DEVICE_TYPE",
        "DUCT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AttributeTargetsE"

def test_attributetypese_exists():
    # Check that the Enumeration exists
    assert AttributeTypesE is not None

def test_attributetypese_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AttributeTypesE]
    expected_literals = [
        "STRING",
        "BOOL",
        "NUMERIC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AttributeTypesE"

def test_integretystatee_exists():
    # Check that the Enumeration exists
    assert IntegretyStateE is not None

def test_integretystatee_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntegretyStateE]
    expected_literals = [
        "OK",
        "UNKNOWN",
        "FAILED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntegretyStateE"

def test_endianesse_exists():
    # Check that the Enumeration exists
    assert EndianessE is not None

def test_endianesse_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EndianessE]
    expected_literals = [
        "BIG",
        "LITTLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EndianessE"


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
oaam::scenario::Subscenario_strategy = st.builds(
    oaam::scenario::Subscenario,
)
oaam::scenario::Scenario_strategy = st.builds(
    oaam::scenario::Scenario,
)
ProvidedInformationA_strategy = st.builds(
    ProvidedInformationA,
)
systems::SystemsContainerA_strategy = st.builds(
    systems::SystemsContainerA,
)
SystemsContainerA_strategy = st.builds(
    SystemsContainerA,
)
oaam::systems::Systems_strategy = st.builds(
    oaam::systems::Systems,
)
scenario::ScenarioParameterA_strategy = st.builds(
    scenario::ScenarioParameterA,
)
Subscenario_strategy = st.builds(
    Subscenario,
)
OperationMode_strategy = st.builds(
    OperationMode,
)
scenario::VariantDependentElementA_strategy = st.builds(
    scenario::VariantDependentElementA,
)
scenario::ModeDependentElementA_strategy = st.builds(
    scenario::ModeDependentElementA,
)
oaam::systems::Subsystem_strategy = st.builds(
    oaam::systems::Subsystem,
)
oaam::scenario::ScenarioParameterA_strategy = st.builds(
    oaam::scenario::ScenarioParameterA,
)
LibraryContainerA_strategy = st.builds(
    LibraryContainerA,
)
oaam::library::Sublibrary_strategy = st.builds(
    oaam::library::Sublibrary,
)
oaam::library::Library_strategy = st.builds(
    oaam::library::Library,
)
ScenarioParameterA_strategy = st.builds(
    ScenarioParameterA,
)
Variant_strategy = st.builds(
    Variant,
)
oaam::scenario::VariantDependentElementA_strategy = st.builds(
    oaam::scenario::VariantDependentElementA,
)
OperationModeReference_strategy = st.builds(
    OperationModeReference,
)
oaam::scenario::ModeDependentElementA_strategy = st.builds(
    oaam::scenario::ModeDependentElementA,
)
oaam::allocations::SignalToMessageAssignment_strategy = st.builds(
    oaam::allocations::SignalToMessageAssignment,
    position=
        st.integers()
)
allocations::AllocationsContainerA_strategy = st.builds(
    allocations::AllocationsContainerA,
)
oaam::allocations::Suballocations_strategy = st.builds(
    oaam::allocations::Suballocations,
)
AllocationsContainerA_strategy = st.builds(
    AllocationsContainerA,
)
oaam::allocations::Allocations_strategy = st.builds(
    oaam::allocations::Allocations,
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
oaam::allocations::Submessage_strategy = st.builds(
    oaam::allocations::Submessage,
    position=
        st.integers()
)
oaam::allocations::Message_strategy = st.builds(
    oaam::allocations::Message,
)
ScheduledTime_strategy = st.builds(
    ScheduledTime,
)
ConnectionAssignmentSegment_strategy = st.builds(
    ConnectionAssignmentSegment,
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
restrictions::RestrictionsContainerA_strategy = st.builds(
    restrictions::RestrictionsContainerA,
)
oaam::restrictions::Subrestrictions_strategy = st.builds(
    oaam::restrictions::Subrestrictions,
)
restrictions::ConnectionRestrinctionA_strategy = st.builds(
    restrictions::ConnectionRestrinctionA,
)
restrictions::DeviceRestrictionA_strategy = st.builds(
    restrictions::DeviceRestrictionA,
)
restrictions::SubfunctionRestrictionA_strategy = st.builds(
    restrictions::SubfunctionRestrictionA,
)
restrictions::SignalGroupRestrictionA_strategy = st.builds(
    restrictions::SignalGroupRestrictionA,
)
restrictions::SignalRestrictionA_strategy = st.builds(
    restrictions::SignalRestrictionA,
)
restrictions::TaskGroupRestrictionA_strategy = st.builds(
    restrictions::TaskGroupRestrictionA,
)
restrictions::TaskRestrictionA_strategy = st.builds(
    restrictions::TaskRestrictionA,
)
oaam::restrictions::SignalGroupRestrictionA_strategy = st.builds(
    oaam::restrictions::SignalGroupRestrictionA,
)
oaam::restrictions::TaskGroupRestrictionA_strategy = st.builds(
    oaam::restrictions::TaskGroupRestrictionA,
)
oaam::restrictions::SubfunctionRestrictionA_strategy = st.builds(
    oaam::restrictions::SubfunctionRestrictionA,
)
oaam::restrictions::DeviceRestrictionA_strategy = st.builds(
    oaam::restrictions::DeviceRestrictionA,
)
RestrictionsContainerA_strategy = st.builds(
    RestrictionsContainerA,
)
oaam::restrictions::Restrictions_strategy = st.builds(
    oaam::restrictions::Restrictions,
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
oaam::restrictions::SignalRestrictionA_strategy = st.builds(
    oaam::restrictions::SignalRestrictionA,
)
oaam::restrictions::TaskRestrictionA_strategy = st.builds(
    oaam::restrictions::TaskRestrictionA,
)
oaam::restrictions::ConnectionRestrinctionA_strategy = st.builds(
    oaam::restrictions::ConnectionRestrinctionA,
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
capabilities::CapabilitiesContainerA_strategy = st.builds(
    capabilities::CapabilitiesContainerA,
)
oaam::capabilities::Subcapabilities_strategy = st.builds(
    oaam::capabilities::Subcapabilities,
)
CapabilitiesContainerA_strategy = st.builds(
    CapabilitiesContainerA,
)
oaam::capabilities::Capabilities_strategy = st.builds(
    oaam::capabilities::Capabilities,
)
capabilities::CapabilityA_strategy = st.builds(
    capabilities::CapabilityA,
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
oaam::capabilities::CapabilityA_strategy = st.builds(
    oaam::capabilities::CapabilityA,
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
oaam::anatomy::Anatomy_strategy = st.builds(
    oaam::anatomy::Anatomy,
)
anatomy::AnatomyContainerA_strategy = st.builds(
    anatomy::AnatomyContainerA,
)
oaam::anatomy::Subanatomy_strategy = st.builds(
    oaam::anatomy::Subanatomy,
)
DuctOpening_strategy = st.builds(
    DuctOpening,
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
hardware::HardwareContainerA_strategy = st.builds(
    hardware::HardwareContainerA,
)
oaam::hardware::Subhardware_strategy = st.builds(
    oaam::hardware::Subhardware,
)
oaam::hardware::Hardware_strategy = st.builds(
    oaam::hardware::Hardware,
)
library::ResourceProviderInstanceA_strategy = st.builds(
    library::ResourceProviderInstanceA,
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
oaam::functions::Subfunctions_strategy = st.builds(
    oaam::functions::Subfunctions,
    multiplicityMax=
        st.integers(),
    multiplicityMin=
        st.integers()
)
oaam::functions::Functions_strategy = st.builds(
    oaam::functions::Functions,
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
oaam::systems::HydraulicPower_strategy = st.builds(
    oaam::systems::HydraulicPower,
    massFlowRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    pressure=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::systems::RotaryPower_strategy = st.builds(
    oaam::systems::RotaryPower,
    angularVelocity=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    momentum=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::systems::ElectricPower_strategy = st.builds(
    oaam::systems::ElectricPower,
    nPhases=
        st.integers(),
    voltage=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    current=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    frequency=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::systems::LinearPower_strategy = st.builds(
    oaam::systems::LinearPower,
    force=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    velocity=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
systems::RequiredInformationA_strategy = st.builds(
    systems::RequiredInformationA,
)
systems::ProvidedInformationA_strategy = st.builds(
    systems::ProvidedInformationA,
)
oaam::systems::ProvidedInformationA_strategy = st.builds(
    oaam::systems::ProvidedInformationA,
)
oaam::systems::RequiredInformationA_strategy = st.builds(
    oaam::systems::RequiredInformationA,
)
RequiredInformationA_strategy = st.builds(
    RequiredInformationA,
)
Subsystem_strategy = st.builds(
    Subsystem,
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
library::ResourceProviderA_strategy = st.builds(
    library::ResourceProviderA,
)
ResourceAlternatives_strategy = st.builds(
    ResourceAlternatives,
)
ResourceTypeModifierReference_strategy = st.builds(
    ResourceTypeModifierReference,
)
library::ResourceConsumerA_strategy = st.builds(
    library::ResourceConsumerA,
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
oaam::library::ResourceProviderInstanceA_strategy = st.builds(
    oaam::library::ResourceProviderInstanceA,
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
oaam::library::ResourceProviderA_strategy = st.builds(
    oaam::library::ResourceProviderA,
)
oaam::library::ResourceConsumerA_strategy = st.builds(
    oaam::library::ResourceConsumerA,
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
oaam::common::FloatingPoint_strategy = st.builds(
    oaam::common::FloatingPoint,
    nBits=
        st.integers(),
    endianess=
        safe_text
)
oaam::common::Character_strategy = st.builds(
    oaam::common::Character,
    encoding=
        safe_text,
    nBits=
        st.integers()
)
oaam::common::Byte_strategy = st.builds(
    oaam::common::Byte,
    nBits=
        st.integers()
)
oaam::common::Boolean_strategy = st.builds(
    oaam::common::Boolean,
    nBits=
        st.integers()
)
oaam::common::Struct_strategy = st.builds(
    oaam::common::Struct,
    alignment=
        st.integers(),
    isAbstract=
        st.booleans()
)
oaam::common::Array_strategy = st.builds(
    oaam::common::Array,
    alignment=
        st.integers(),
    nElements=
        st.integers()
)
oaam::common::Integer_strategy = st.builds(
    oaam::common::Integer,
    endianess=
        safe_text,
    nBits=
        st.integers(),
    signed=
        st.booleans()
)
BoolA_strategy = st.builds(
    BoolA,
)
common::OaamBaseElementA_strategy = st.builds(
    common::OaamBaseElementA,
)
oaam::capabilities::TaskOnDeviceCapability_strategy = st.builds(
    oaam::capabilities::TaskOnDeviceCapability,
    failureProbability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    worstCaseExecutionTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::library::MessageType_strategy = st.builds(
    oaam::library::MessageType,
    minLength=
        st.integers(),
    maxLength=
        st.integers(),
    alignment=
        st.integers()
)
oaam::anatomy::Duct_strategy = st.builds(
    oaam::anatomy::Duct,
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::hardware::DeviceSymmetry_strategy = st.builds(
    oaam::hardware::DeviceSymmetry,
)
oaam::restrictions::AreaRestriction_strategy = st.builds(
    oaam::restrictions::AreaRestriction,
    isForbidden=
        st.booleans(),
    areaName=
        safe_text
)
oaam::anatomy::AreaSymmetry_strategy = st.builds(
    oaam::anatomy::AreaSymmetry,
)
oaam::anatomy::Area_strategy = st.builds(
    oaam::anatomy::Area,
)
oaam::library::ResourceType_strategy = st.builds(
    oaam::library::ResourceType,
    isConsumed=
        st.booleans(),
    isConfigurable=
        st.booleans(),
    isDistinguishable=
        st.booleans(),
    isIo=
        st.booleans(),
    isPropagated=
        st.booleans(),
    direction=
        safe_text,
    unit=
        safe_text
)
oaam::restrictions::TaskAtomicRestriction_strategy = st.builds(
    oaam::restrictions::TaskAtomicRestriction,
)
oaam::restrictions::LocationRestriction_strategy = st.builds(
    oaam::restrictions::LocationRestriction,
    isForbidden=
        st.booleans(),
    locationName=
        safe_text
)
oaam::allocations::SignalAssignmentSegment_strategy = st.builds(
    oaam::allocations::SignalAssignmentSegment,
)
oaam::systems::InformationMaterial_strategy = st.builds(
    oaam::systems::InformationMaterial,
    velocity=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    density=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::functions::TaskGroup_strategy = st.builds(
    oaam::functions::TaskGroup,
)
oaam::functions::Task_strategy = st.builds(
    oaam::functions::Task,
    nParallels=
        st.integers(),
    fixedRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::capabilities::SubconnectionInDeviceCapability_strategy = st.builds(
    oaam::capabilities::SubconnectionInDeviceCapability,
)
oaam::allocations::ScheduledTime_strategy = st.builds(
    oaam::allocations::ScheduledTime,
    duration=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    restart=
        st.booleans(),
    startTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    cycle=
        st.integers()
)
oaam::library::SignalType_strategy = st.builds(
    oaam::library::SignalType,
)
oaam::capabilities::DeviceInLocationCapability_strategy = st.builds(
    oaam::capabilities::DeviceInLocationCapability,
)
oaam::library::TaskType_strategy = st.builds(
    oaam::library::TaskType,
    isDeterministic=
        st.booleans(),
    preferredExecutionRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::capabilities::MessageOnBusCapability_strategy = st.builds(
    oaam::capabilities::MessageOnBusCapability,
)
oaam::allocations::ConnectionAssignment_strategy = st.builds(
    oaam::allocations::ConnectionAssignment,
)
oaam::allocations::DeviceAssignment_strategy = st.builds(
    oaam::allocations::DeviceAssignment,
)
oaam::capabilities::SubmessageInMessageCapability_strategy = st.builds(
    oaam::capabilities::SubmessageInMessageCapability,
)
oaam::functions::Output_strategy = st.builds(
    oaam::functions::Output,
    fixedRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::hardware::Io_strategy = st.builds(
    oaam::hardware::Io,
)
oaam::scenario::Variant_strategy = st.builds(
    oaam::scenario::Variant,
)
oaam::functions::ExternalTaskLink_strategy = st.builds(
    oaam::functions::ExternalTaskLink,
    filter=
        safe_text
)
oaam::capabilities::ConnectionInDuctOrLocationCapability_strategy = st.builds(
    oaam::capabilities::ConnectionInDuctOrLocationCapability,
)
oaam::allocations::MessageSegment_strategy = st.builds(
    oaam::allocations::MessageSegment,
)
oaam::functions::TaskSymmetry_strategy = st.builds(
    oaam::functions::TaskSymmetry,
)
oaam::allocations::SubconnectionAssignment_strategy = st.builds(
    oaam::allocations::SubconnectionAssignment,
)
oaam::scenario::ScenarioParameterBool_strategy = st.builds(
    oaam::scenario::ScenarioParameterBool,
    value=
        st.booleans()
)
oaam::allocations::TaskAssignment_strategy = st.builds(
    oaam::allocations::TaskAssignment,
)
oaam::functions::Signal_strategy = st.builds(
    oaam::functions::Signal,
    inIndex=
        st.integers(),
    outIndex=
        st.integers()
)
oaam::functions::ExternalOutputLink_strategy = st.builds(
    oaam::functions::ExternalOutputLink,
    filter=
        safe_text
)
oaam::hardware::Bus_strategy = st.builds(
    oaam::hardware::Bus,
)
oaam::hardware::Connection_strategy = st.builds(
    oaam::hardware::Connection,
)
oaam::functions::TaskRedundancy_strategy = st.builds(
    oaam::functions::TaskRedundancy,
)
oaam::library::BusType_strategy = st.builds(
    oaam::library::BusType,
    isSelfManaging=
        st.booleans(),
    mtbf=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    requiresMaster=
        st.booleans()
)
oaam::library::LocationType_strategy = st.builds(
    oaam::library::LocationType,
    isJoint=
        st.booleans()
)
oaam::capabilities::SignalInMessageCapability_strategy = st.builds(
    oaam::capabilities::SignalInMessageCapability,
)
oaam::anatomy::LocationSymmetry_strategy = st.builds(
    oaam::anatomy::LocationSymmetry,
)
oaam::allocations::MessageA_strategy = st.builds(
    oaam::allocations::MessageA,
    length=
        st.integers(),
    isPersistent=
        st.booleans()
)
oaam::anatomy::Location_strategy = st.builds(
    oaam::anatomy::Location,
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::functions::FunctionsContainerA_strategy = st.builds(
    oaam::functions::FunctionsContainerA,
)
oaam::library::DeviceType_strategy = st.builds(
    oaam::library::DeviceType,
    weight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    canHaveSubdevices=
        st.booleans(),
    mtbf=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    isSelfManaging=
        st.booleans(),
    isSubdevice=
        st.booleans(),
    cost=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::restrictions::SegregationRestriction_strategy = st.builds(
    oaam::restrictions::SegregationRestriction,
    dissimilarTechnology=
        st.booleans(),
    dissimilarArea=
        st.booleans(),
    dissimilarPowerSource=
        st.booleans(),
    dissimilarLocation=
        st.booleans()
)
oaam::scenario::ScenarioParameterNumeric_strategy = st.builds(
    oaam::scenario::ScenarioParameterNumeric,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::library::ResourceTypeModifierLevel_strategy = st.builds(
    oaam::library::ResourceTypeModifierLevel,
)
oaam::restrictions::DeviceTypeRestriction_strategy = st.builds(
    oaam::restrictions::DeviceTypeRestriction,
    deviceTypeName=
        safe_text,
    isForbidden=
        st.booleans()
)
oaam::restrictions::ConnectionTypeRestriction_strategy = st.builds(
    oaam::restrictions::ConnectionTypeRestriction,
    connectionTypeName=
        safe_text,
    isForbidden=
        st.booleans()
)
oaam::scenario::OperationMode_strategy = st.builds(
    oaam::scenario::OperationMode,
)
oaam::hardware::Device_strategy = st.builds(
    oaam::hardware::Device,
)
oaam::restrictions::DeviceRestriction_strategy = st.builds(
    oaam::restrictions::DeviceRestriction,
    isForbidden=
        st.booleans(),
    deviceName=
        safe_text
)
oaam::allocations::Schedule_strategy = st.builds(
    oaam::allocations::Schedule,
    rate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    isPeriodic=
        st.booleans(),
    priority=
        st.integers()
)
oaam::systems::InformationPower_strategy = st.builds(
    oaam::systems::InformationPower,
    power=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::restrictions::TimeDelayRestriction_strategy = st.builds(
    oaam::restrictions::TimeDelayRestriction,
    delay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::library::ResourceBundle_strategy = st.builds(
    oaam::library::ResourceBundle,
    mtbf=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    mass=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    cost=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::library::DuctType_strategy = st.builds(
    oaam::library::DuctType,
)
oaam::restrictions::PowerSourceRestriction_strategy = st.builds(
    oaam::restrictions::PowerSourceRestriction,
    powerSourceName=
        safe_text,
    isForbidden=
        st.booleans()
)
oaam::capabilities::SignalOnConnectionOrDeviceCapability_strategy = st.builds(
    oaam::capabilities::SignalOnConnectionOrDeviceCapability,
    worstCaseTransmissionTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::functions::Input_strategy = st.builds(
    oaam::functions::Input,
    queueLength=
        st.integers()
)
oaam::systems::System_strategy = st.builds(
    oaam::systems::System,
)
oaam::anatomy::DuctOpening_strategy = st.builds(
    oaam::anatomy::DuctOpening,
)
oaam::allocations::ConnectionAssignmentSegment_strategy = st.builds(
    oaam::allocations::ConnectionAssignmentSegment,
)
oaam::functions::FailureCondition_strategy = st.builds(
    oaam::functions::FailureCondition,
    maxOccurrenceProbability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    noSingleFailure=
        st.booleans()
)
oaam::restrictions::TaskSymmetryRestriction_strategy = st.builds(
    oaam::restrictions::TaskSymmetryRestriction,
    type=
        safe_text
)
oaam::allocations::SubdeviceAssignment_strategy = st.builds(
    oaam::allocations::SubdeviceAssignment,
)
oaam::library::ConnectionType_strategy = st.builds(
    oaam::library::ConnectionType,
    maxInterfaceToJointDistance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    isPower=
        st.booleans(),
    isSwitched=
        st.booleans(),
    nJoints=
        st.integers(),
    allowsCircles=
        st.booleans(),
    maxJointBranches=
        st.integers(),
    isUnidirectional=
        st.booleans(),
    isWireless=
        st.booleans(),
    nStartingPoints=
        st.integers(),
    directConnectionsAllowed=
        st.booleans(),
    maxLength=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    requiresMaster=
        st.booleans(),
    isInformation=
        st.booleans(),
    nEndPoints=
        st.integers()
)
oaam::anatomy::Position3D_strategy = st.builds(
    oaam::anatomy::Position3D,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    z=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::restrictions::SynchronicityRestriction_strategy = st.builds(
    oaam::restrictions::SynchronicityRestriction,
    maxJitter=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::restrictions::ConnectionRestriction_strategy = st.builds(
    oaam::restrictions::ConnectionRestriction,
    isForbidden=
        st.booleans(),
    connectionName=
        safe_text
)
oaam::systems::InformationFlow_strategy = st.builds(
    oaam::systems::InformationFlow,
)
oaam::capabilities::SubdeviceInDeviceCapability_strategy = st.builds(
    oaam::capabilities::SubdeviceInDeviceCapability,
)
oaam::systems::InformationSignal_strategy = st.builds(
    oaam::systems::InformationSignal,
    latency=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    rate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    unit=
        safe_text,
    accuracy=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    resolution=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::allocations::SignalAssignment_strategy = st.builds(
    oaam::allocations::SignalAssignment,
)
oaam::capabilities::MessageOnConnectionOrDeviceCapability_strategy = st.builds(
    oaam::capabilities::MessageOnConnectionOrDeviceCapability,
    worstCaseTransmissionTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::functions::SignalGroup_strategy = st.builds(
    oaam::functions::SignalGroup,
)
common::BoolA_strategy = st.builds(
    common::BoolA,
)
oaam::library::TaskInputState_strategy = st.builds(
    oaam::library::TaskInputState,
    state=
        safe_text
)
oaam::functions::OutputIntegrityState_strategy = st.builds(
    oaam::functions::OutputIntegrityState,
    state=
        safe_text
)
oaam::common::BoolNot_strategy = st.builds(
    oaam::common::BoolNot,
)
oaam::library::TaskInputTrigger_strategy = st.builds(
    oaam::library::TaskInputTrigger,
)
oaam::common::BoolOperation_strategy = st.builds(
    oaam::common::BoolOperation,
    type=
        safe_text
)
oaam::common::BoolA_strategy = st.builds(
    oaam::common::BoolA,
)
AttributeA_strategy = st.builds(
    AttributeA,
)
oaam::common::AttributeReference_strategy = st.builds(
    oaam::common::AttributeReference,
)
oaam::common::AttributeNumeric_strategy = st.builds(
    oaam::common::AttributeNumeric,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::common::AttributeString_strategy = st.builds(
    oaam::common::AttributeString,
    value=
        safe_text
)
oaam::common::AttributeContainment_strategy = st.builds(
    oaam::common::AttributeContainment,
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
oaam::common::OaamBaseElementA_strategy = st.builds(
    oaam::common::OaamBaseElementA,
    documentation=
        safe_text,
    id=
        safe_text,
    modified=
        st.dates(),
    style=
        safe_text,
    name=
        safe_text,
    modifier=
        safe_text,
    traceLink=
        safe_text
)
Library_strategy = st.builds(
    Library,
)
OaamBaseElementA_strategy = st.builds(
    OaamBaseElementA,
)
oaam::library::ResourceTypeModifier_strategy = st.builds(
    oaam::library::ResourceTypeModifier,
)
oaam::library::TaskStateDeclaration_strategy = st.builds(
    oaam::library::TaskStateDeclaration,
)
oaam::library::DuctOpeningDeclaration_strategy = st.builds(
    oaam::library::DuctOpeningDeclaration,
)
oaam::library::ResourceGroup_strategy = st.builds(
    oaam::library::ResourceGroup,
)
oaam::scenario::ScenarioContainerA_strategy = st.builds(
    oaam::scenario::ScenarioContainerA,
)
oaam::library::DeviceTypeDissimilarity_strategy = st.builds(
    oaam::library::DeviceTypeDissimilarity,
    percentageOfCommonHardware=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::common::AttributeA_strategy = st.builds(
    oaam::common::AttributeA,
)
oaam::library::WireType_strategy = st.builds(
    oaam::library::WireType,
    specificWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    mtbf=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    specificPrice=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minBendingRadius=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    nShields=
        st.integers(),
    nConductors=
        st.integers()
)
oaam::library::InputDeclaration_strategy = st.builds(
    oaam::library::InputDeclaration,
    precondition=
        safe_text,
    unit=
        safe_text,
    lowerBound=
        st.integers(),
    upperBound=
        st.integers(),
    range=
        safe_text
)
oaam::library::LibraryContainerA_strategy = st.builds(
    oaam::library::LibraryContainerA,
)
oaam::library::AttributeDefinition_strategy = st.builds(
    oaam::library::AttributeDefinition,
    dataType=
        safe_text,
    target=
        safe_text
)
oaam::library::ResourceLink_strategy = st.builds(
    oaam::library::ResourceLink,
)
oaam::library::IoDeclaration_strategy = st.builds(
    oaam::library::IoDeclaration,
)
oaam::library::ResourceTypeModifierReference_strategy = st.builds(
    oaam::library::ResourceTypeModifierReference,
)
oaam::systems::InputSegregation_strategy = st.builds(
    oaam::systems::InputSegregation,
    dissimilarRoute=
        st.booleans(),
    dissimilarSource=
        st.booleans(),
    dissimilarTechnology=
        st.booleans()
)
oaam::functions::TaskParameter_strategy = st.builds(
    oaam::functions::TaskParameter,
    value=
        safe_text
)
oaam::library::FaultPropagation_strategy = st.builds(
    oaam::library::FaultPropagation,
    outputState=
        safe_text
)
oaam::library::Resource_strategy = st.builds(
    oaam::library::Resource,
    count=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::systems::SystemsContainerA_strategy = st.builds(
    oaam::systems::SystemsContainerA,
)
oaam::hardware::HardwareContainerA_strategy = st.builds(
    oaam::hardware::HardwareContainerA,
)
oaam::restrictions::RestrictionsContainerA_strategy = st.builds(
    oaam::restrictions::RestrictionsContainerA,
)
oaam::capabilities::CapabilitiesContainerA_strategy = st.builds(
    oaam::capabilities::CapabilitiesContainerA,
)
oaam::library::TaskTypeDissimilarity_strategy = st.builds(
    oaam::library::TaskTypeDissimilarity,
    percentageOfCommonCode=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::scenario::OperationModeReference_strategy = st.builds(
    oaam::scenario::OperationModeReference,
    activeProbability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::allocations::AllocationsContainerA_strategy = st.builds(
    oaam::allocations::AllocationsContainerA,
)
oaam::capabilities::ResourceConsumption_strategy = st.builds(
    oaam::capabilities::ResourceConsumption,
    count=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oaam::library::IoGroup_strategy = st.builds(
    oaam::library::IoGroup,
)
oaam::library::OutputDeclaration_strategy = st.builds(
    oaam::library::OutputDeclaration,
    lowerBound=
        st.integers(),
    upperBound=
        st.integers(),
    postcondition=
        safe_text,
    unit=
        safe_text,
    range=
        safe_text
)
oaam::library::ResourceAlternatives_strategy = st.builds(
    oaam::library::ResourceAlternatives,
)
oaam::library::TaskOutputTrigger_strategy = st.builds(
    oaam::library::TaskOutputTrigger,
    fixedRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    isFixedRate=
        st.booleans()
)
oaam::library::IoType_strategy = st.builds(
    oaam::library::IoType,
    direction=
        safe_text
)
oaam::library::PowerSource_strategy = st.builds(
    oaam::library::PowerSource,
)
oaam::library::DeviceTypeSymmetry_strategy = st.builds(
    oaam::library::DeviceTypeSymmetry,
)
oaam::common::DataTypeA_strategy = st.builds(
    oaam::common::DataTypeA,
)
oaam::library::TaskParameterDeclaration_strategy = st.builds(
    oaam::library::TaskParameterDeclaration,
)
oaam::library::ResourceTypeDissimilarity_strategy = st.builds(
    oaam::library::ResourceTypeDissimilarity,
)
oaam::anatomy::AnatomyContainerA_strategy = st.builds(
    oaam::anatomy::AnatomyContainerA,
)
oaam::Architecture_strategy = st.builds(
    oaam::Architecture,
)
Systems_strategy = st.builds(
    Systems,
)
Scenario_strategy = st.builds(
    Scenario,
)

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

@given(instance=oaam::scenario::Subscenario_strategy)
@settings(max_examples=50)
def test_oaam::scenario::subscenario_instantiation(instance):
    assert isinstance(instance, oaam::scenario::Subscenario)

@given(instance=oaam::scenario::Scenario_strategy)
@settings(max_examples=50)
def test_oaam::scenario::scenario_instantiation(instance):
    assert isinstance(instance, oaam::scenario::Scenario)

@given(instance=ProvidedInformationA_strategy)
@settings(max_examples=50)
def test_providedinformationa_instantiation(instance):
    assert isinstance(instance, ProvidedInformationA)

@given(instance=systems::SystemsContainerA_strategy)
@settings(max_examples=50)
def test_systems::systemscontainera_instantiation(instance):
    assert isinstance(instance, systems::SystemsContainerA)

@given(instance=SystemsContainerA_strategy)
@settings(max_examples=50)
def test_systemscontainera_instantiation(instance):
    assert isinstance(instance, SystemsContainerA)

@given(instance=oaam::systems::Systems_strategy)
@settings(max_examples=50)
def test_oaam::systems::systems_instantiation(instance):
    assert isinstance(instance, oaam::systems::Systems)

@given(instance=scenario::ScenarioParameterA_strategy)
@settings(max_examples=50)
def test_scenario::scenarioparametera_instantiation(instance):
    assert isinstance(instance, scenario::ScenarioParameterA)

@given(instance=Subscenario_strategy)
@settings(max_examples=50)
def test_subscenario_instantiation(instance):
    assert isinstance(instance, Subscenario)

@given(instance=OperationMode_strategy)
@settings(max_examples=50)
def test_operationmode_instantiation(instance):
    assert isinstance(instance, OperationMode)

@given(instance=scenario::VariantDependentElementA_strategy)
@settings(max_examples=50)
def test_scenario::variantdependentelementa_instantiation(instance):
    assert isinstance(instance, scenario::VariantDependentElementA)

@given(instance=scenario::ModeDependentElementA_strategy)
@settings(max_examples=50)
def test_scenario::modedependentelementa_instantiation(instance):
    assert isinstance(instance, scenario::ModeDependentElementA)

@given(instance=oaam::systems::Subsystem_strategy)
@settings(max_examples=50)
def test_oaam::systems::subsystem_instantiation(instance):
    assert isinstance(instance, oaam::systems::Subsystem)

@given(instance=oaam::scenario::ScenarioParameterA_strategy)
@settings(max_examples=50)
def test_oaam::scenario::scenarioparametera_instantiation(instance):
    assert isinstance(instance, oaam::scenario::ScenarioParameterA)

@given(instance=LibraryContainerA_strategy)
@settings(max_examples=50)
def test_librarycontainera_instantiation(instance):
    assert isinstance(instance, LibraryContainerA)

@given(instance=oaam::library::Sublibrary_strategy)
@settings(max_examples=50)
def test_oaam::library::sublibrary_instantiation(instance):
    assert isinstance(instance, oaam::library::Sublibrary)

@given(instance=oaam::library::Library_strategy)
@settings(max_examples=50)
def test_oaam::library::library_instantiation(instance):
    assert isinstance(instance, oaam::library::Library)

@given(instance=ScenarioParameterA_strategy)
@settings(max_examples=50)
def test_scenarioparametera_instantiation(instance):
    assert isinstance(instance, ScenarioParameterA)

@given(instance=Variant_strategy)
@settings(max_examples=50)
def test_variant_instantiation(instance):
    assert isinstance(instance, Variant)

@given(instance=oaam::scenario::VariantDependentElementA_strategy)
@settings(max_examples=50)
def test_oaam::scenario::variantdependentelementa_instantiation(instance):
    assert isinstance(instance, oaam::scenario::VariantDependentElementA)

@given(instance=OperationModeReference_strategy)
@settings(max_examples=50)
def test_operationmodereference_instantiation(instance):
    assert isinstance(instance, OperationModeReference)

@given(instance=oaam::scenario::ModeDependentElementA_strategy)
@settings(max_examples=50)
def test_oaam::scenario::modedependentelementa_instantiation(instance):
    assert isinstance(instance, oaam::scenario::ModeDependentElementA)

@given(instance=oaam::allocations::SignalToMessageAssignment_strategy)
@settings(max_examples=50)
def test_oaam::allocations::signaltomessageassignment_instantiation(instance):
    assert isinstance(instance, oaam::allocations::SignalToMessageAssignment)

@given(instance=oaam::allocations::SignalToMessageAssignment_strategy)
def test_oaam::allocations::signaltomessageassignment_position_type(instance):
    assert isinstance(instance.position, int)


@given(instance=oaam::allocations::SignalToMessageAssignment_strategy)
def test_oaam::allocations::signaltomessageassignment_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=allocations::AllocationsContainerA_strategy)
@settings(max_examples=50)
def test_allocations::allocationscontainera_instantiation(instance):
    assert isinstance(instance, allocations::AllocationsContainerA)

@given(instance=oaam::allocations::Suballocations_strategy)
@settings(max_examples=50)
def test_oaam::allocations::suballocations_instantiation(instance):
    assert isinstance(instance, oaam::allocations::Suballocations)

@given(instance=AllocationsContainerA_strategy)
@settings(max_examples=50)
def test_allocationscontainera_instantiation(instance):
    assert isinstance(instance, AllocationsContainerA)

@given(instance=oaam::allocations::Allocations_strategy)
@settings(max_examples=50)
def test_oaam::allocations::allocations_instantiation(instance):
    assert isinstance(instance, oaam::allocations::Allocations)

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

@given(instance=oaam::allocations::Submessage_strategy)
@settings(max_examples=50)
def test_oaam::allocations::submessage_instantiation(instance):
    assert isinstance(instance, oaam::allocations::Submessage)

@given(instance=oaam::allocations::Submessage_strategy)
def test_oaam::allocations::submessage_position_type(instance):
    assert isinstance(instance.position, int)


@given(instance=oaam::allocations::Submessage_strategy)
def test_oaam::allocations::submessage_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=oaam::allocations::Message_strategy)
@settings(max_examples=50)
def test_oaam::allocations::message_instantiation(instance):
    assert isinstance(instance, oaam::allocations::Message)

@given(instance=ScheduledTime_strategy)
@settings(max_examples=50)
def test_scheduledtime_instantiation(instance):
    assert isinstance(instance, ScheduledTime)

@given(instance=ConnectionAssignmentSegment_strategy)
@settings(max_examples=50)
def test_connectionassignmentsegment_instantiation(instance):
    assert isinstance(instance, ConnectionAssignmentSegment)

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

@given(instance=restrictions::RestrictionsContainerA_strategy)
@settings(max_examples=50)
def test_restrictions::restrictionscontainera_instantiation(instance):
    assert isinstance(instance, restrictions::RestrictionsContainerA)

@given(instance=oaam::restrictions::Subrestrictions_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::subrestrictions_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::Subrestrictions)

@given(instance=restrictions::ConnectionRestrinctionA_strategy)
@settings(max_examples=50)
def test_restrictions::connectionrestrinctiona_instantiation(instance):
    assert isinstance(instance, restrictions::ConnectionRestrinctionA)

@given(instance=restrictions::DeviceRestrictionA_strategy)
@settings(max_examples=50)
def test_restrictions::devicerestrictiona_instantiation(instance):
    assert isinstance(instance, restrictions::DeviceRestrictionA)

@given(instance=restrictions::SubfunctionRestrictionA_strategy)
@settings(max_examples=50)
def test_restrictions::subfunctionrestrictiona_instantiation(instance):
    assert isinstance(instance, restrictions::SubfunctionRestrictionA)

@given(instance=restrictions::SignalGroupRestrictionA_strategy)
@settings(max_examples=50)
def test_restrictions::signalgrouprestrictiona_instantiation(instance):
    assert isinstance(instance, restrictions::SignalGroupRestrictionA)

@given(instance=restrictions::SignalRestrictionA_strategy)
@settings(max_examples=50)
def test_restrictions::signalrestrictiona_instantiation(instance):
    assert isinstance(instance, restrictions::SignalRestrictionA)

@given(instance=restrictions::TaskGroupRestrictionA_strategy)
@settings(max_examples=50)
def test_restrictions::taskgrouprestrictiona_instantiation(instance):
    assert isinstance(instance, restrictions::TaskGroupRestrictionA)

@given(instance=restrictions::TaskRestrictionA_strategy)
@settings(max_examples=50)
def test_restrictions::taskrestrictiona_instantiation(instance):
    assert isinstance(instance, restrictions::TaskRestrictionA)

@given(instance=oaam::restrictions::SignalGroupRestrictionA_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::signalgrouprestrictiona_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::SignalGroupRestrictionA)

@given(instance=oaam::restrictions::TaskGroupRestrictionA_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::taskgrouprestrictiona_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::TaskGroupRestrictionA)

@given(instance=oaam::restrictions::SubfunctionRestrictionA_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::subfunctionrestrictiona_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::SubfunctionRestrictionA)

@given(instance=oaam::restrictions::DeviceRestrictionA_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::devicerestrictiona_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::DeviceRestrictionA)

@given(instance=RestrictionsContainerA_strategy)
@settings(max_examples=50)
def test_restrictionscontainera_instantiation(instance):
    assert isinstance(instance, RestrictionsContainerA)

@given(instance=oaam::restrictions::Restrictions_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::restrictions_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::Restrictions)

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

@given(instance=oaam::restrictions::SignalRestrictionA_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::signalrestrictiona_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::SignalRestrictionA)

@given(instance=oaam::restrictions::TaskRestrictionA_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::taskrestrictiona_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::TaskRestrictionA)

@given(instance=oaam::restrictions::ConnectionRestrinctionA_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::connectionrestrinctiona_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::ConnectionRestrinctionA)

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

@given(instance=capabilities::CapabilitiesContainerA_strategy)
@settings(max_examples=50)
def test_capabilities::capabilitiescontainera_instantiation(instance):
    assert isinstance(instance, capabilities::CapabilitiesContainerA)

@given(instance=oaam::capabilities::Subcapabilities_strategy)
@settings(max_examples=50)
def test_oaam::capabilities::subcapabilities_instantiation(instance):
    assert isinstance(instance, oaam::capabilities::Subcapabilities)

@given(instance=CapabilitiesContainerA_strategy)
@settings(max_examples=50)
def test_capabilitiescontainera_instantiation(instance):
    assert isinstance(instance, CapabilitiesContainerA)

@given(instance=oaam::capabilities::Capabilities_strategy)
@settings(max_examples=50)
def test_oaam::capabilities::capabilities_instantiation(instance):
    assert isinstance(instance, oaam::capabilities::Capabilities)

@given(instance=capabilities::CapabilityA_strategy)
@settings(max_examples=50)
def test_capabilities::capabilitya_instantiation(instance):
    assert isinstance(instance, capabilities::CapabilityA)

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

@given(instance=oaam::capabilities::CapabilityA_strategy)
@settings(max_examples=50)
def test_oaam::capabilities::capabilitya_instantiation(instance):
    assert isinstance(instance, oaam::capabilities::CapabilityA)

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

@given(instance=oaam::anatomy::Anatomy_strategy)
@settings(max_examples=50)
def test_oaam::anatomy::anatomy_instantiation(instance):
    assert isinstance(instance, oaam::anatomy::Anatomy)

@given(instance=anatomy::AnatomyContainerA_strategy)
@settings(max_examples=50)
def test_anatomy::anatomycontainera_instantiation(instance):
    assert isinstance(instance, anatomy::AnatomyContainerA)

@given(instance=oaam::anatomy::Subanatomy_strategy)
@settings(max_examples=50)
def test_oaam::anatomy::subanatomy_instantiation(instance):
    assert isinstance(instance, oaam::anatomy::Subanatomy)

@given(instance=DuctOpening_strategy)
@settings(max_examples=50)
def test_ductopening_instantiation(instance):
    assert isinstance(instance, DuctOpening)

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

@given(instance=hardware::HardwareContainerA_strategy)
@settings(max_examples=50)
def test_hardware::hardwarecontainera_instantiation(instance):
    assert isinstance(instance, hardware::HardwareContainerA)

@given(instance=oaam::hardware::Subhardware_strategy)
@settings(max_examples=50)
def test_oaam::hardware::subhardware_instantiation(instance):
    assert isinstance(instance, oaam::hardware::Subhardware)

@given(instance=oaam::hardware::Hardware_strategy)
@settings(max_examples=50)
def test_oaam::hardware::hardware_instantiation(instance):
    assert isinstance(instance, oaam::hardware::Hardware)

@given(instance=library::ResourceProviderInstanceA_strategy)
@settings(max_examples=50)
def test_library::resourceproviderinstancea_instantiation(instance):
    assert isinstance(instance, library::ResourceProviderInstanceA)

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

@given(instance=oaam::functions::Subfunctions_strategy)
@settings(max_examples=50)
def test_oaam::functions::subfunctions_instantiation(instance):
    assert isinstance(instance, oaam::functions::Subfunctions)

@given(instance=oaam::functions::Subfunctions_strategy)
def test_oaam::functions::subfunctions_multiplicityMax_type(instance):
    assert isinstance(instance.multiplicityMax, int)


@given(instance=oaam::functions::Subfunctions_strategy)
def test_oaam::functions::subfunctions_multiplicityMax_setter(instance):
    original = instance.multiplicityMax
    instance.multiplicityMax = original
    assert instance.multiplicityMax == original

@given(instance=oaam::functions::Subfunctions_strategy)
def test_oaam::functions::subfunctions_multiplicityMin_type(instance):
    assert isinstance(instance.multiplicityMin, int)


@given(instance=oaam::functions::Subfunctions_strategy)
def test_oaam::functions::subfunctions_multiplicityMin_setter(instance):
    original = instance.multiplicityMin
    instance.multiplicityMin = original
    assert instance.multiplicityMin == original

@given(instance=oaam::functions::Functions_strategy)
@settings(max_examples=50)
def test_oaam::functions::functions_instantiation(instance):
    assert isinstance(instance, oaam::functions::Functions)

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

@given(instance=oaam::systems::HydraulicPower_strategy)
@settings(max_examples=50)
def test_oaam::systems::hydraulicpower_instantiation(instance):
    assert isinstance(instance, oaam::systems::HydraulicPower)

@given(instance=oaam::systems::HydraulicPower_strategy)
def test_oaam::systems::hydraulicpower_massFlowRate_type(instance):
    assert isinstance(instance.massFlowRate, float)


@given(instance=oaam::systems::HydraulicPower_strategy)
def test_oaam::systems::hydraulicpower_massFlowRate_setter(instance):
    original = instance.massFlowRate
    instance.massFlowRate = original
    assert instance.massFlowRate == original

@given(instance=oaam::systems::HydraulicPower_strategy)
def test_oaam::systems::hydraulicpower_pressure_type(instance):
    assert isinstance(instance.pressure, float)


@given(instance=oaam::systems::HydraulicPower_strategy)
def test_oaam::systems::hydraulicpower_pressure_setter(instance):
    original = instance.pressure
    instance.pressure = original
    assert instance.pressure == original

@given(instance=oaam::systems::RotaryPower_strategy)
@settings(max_examples=50)
def test_oaam::systems::rotarypower_instantiation(instance):
    assert isinstance(instance, oaam::systems::RotaryPower)

@given(instance=oaam::systems::RotaryPower_strategy)
def test_oaam::systems::rotarypower_angularVelocity_type(instance):
    assert isinstance(instance.angularVelocity, float)


@given(instance=oaam::systems::RotaryPower_strategy)
def test_oaam::systems::rotarypower_angularVelocity_setter(instance):
    original = instance.angularVelocity
    instance.angularVelocity = original
    assert instance.angularVelocity == original

@given(instance=oaam::systems::RotaryPower_strategy)
def test_oaam::systems::rotarypower_momentum_type(instance):
    assert isinstance(instance.momentum, float)


@given(instance=oaam::systems::RotaryPower_strategy)
def test_oaam::systems::rotarypower_momentum_setter(instance):
    original = instance.momentum
    instance.momentum = original
    assert instance.momentum == original

@given(instance=oaam::systems::ElectricPower_strategy)
@settings(max_examples=50)
def test_oaam::systems::electricpower_instantiation(instance):
    assert isinstance(instance, oaam::systems::ElectricPower)

@given(instance=oaam::systems::ElectricPower_strategy)
def test_oaam::systems::electricpower_nPhases_type(instance):
    assert isinstance(instance.nPhases, int)


@given(instance=oaam::systems::ElectricPower_strategy)
def test_oaam::systems::electricpower_nPhases_setter(instance):
    original = instance.nPhases
    instance.nPhases = original
    assert instance.nPhases == original

@given(instance=oaam::systems::ElectricPower_strategy)
def test_oaam::systems::electricpower_voltage_type(instance):
    assert isinstance(instance.voltage, float)


@given(instance=oaam::systems::ElectricPower_strategy)
def test_oaam::systems::electricpower_voltage_setter(instance):
    original = instance.voltage
    instance.voltage = original
    assert instance.voltage == original

@given(instance=oaam::systems::ElectricPower_strategy)
def test_oaam::systems::electricpower_current_type(instance):
    assert isinstance(instance.current, float)


@given(instance=oaam::systems::ElectricPower_strategy)
def test_oaam::systems::electricpower_current_setter(instance):
    original = instance.current
    instance.current = original
    assert instance.current == original

@given(instance=oaam::systems::ElectricPower_strategy)
def test_oaam::systems::electricpower_frequency_type(instance):
    assert isinstance(instance.frequency, float)


@given(instance=oaam::systems::ElectricPower_strategy)
def test_oaam::systems::electricpower_frequency_setter(instance):
    original = instance.frequency
    instance.frequency = original
    assert instance.frequency == original

@given(instance=oaam::systems::LinearPower_strategy)
@settings(max_examples=50)
def test_oaam::systems::linearpower_instantiation(instance):
    assert isinstance(instance, oaam::systems::LinearPower)

@given(instance=oaam::systems::LinearPower_strategy)
def test_oaam::systems::linearpower_force_type(instance):
    assert isinstance(instance.force, float)


@given(instance=oaam::systems::LinearPower_strategy)
def test_oaam::systems::linearpower_force_setter(instance):
    original = instance.force
    instance.force = original
    assert instance.force == original

@given(instance=oaam::systems::LinearPower_strategy)
def test_oaam::systems::linearpower_velocity_type(instance):
    assert isinstance(instance.velocity, float)


@given(instance=oaam::systems::LinearPower_strategy)
def test_oaam::systems::linearpower_velocity_setter(instance):
    original = instance.velocity
    instance.velocity = original
    assert instance.velocity == original

@given(instance=systems::RequiredInformationA_strategy)
@settings(max_examples=50)
def test_systems::requiredinformationa_instantiation(instance):
    assert isinstance(instance, systems::RequiredInformationA)

@given(instance=systems::ProvidedInformationA_strategy)
@settings(max_examples=50)
def test_systems::providedinformationa_instantiation(instance):
    assert isinstance(instance, systems::ProvidedInformationA)

@given(instance=oaam::systems::ProvidedInformationA_strategy)
@settings(max_examples=50)
def test_oaam::systems::providedinformationa_instantiation(instance):
    assert isinstance(instance, oaam::systems::ProvidedInformationA)

@given(instance=oaam::systems::RequiredInformationA_strategy)
@settings(max_examples=50)
def test_oaam::systems::requiredinformationa_instantiation(instance):
    assert isinstance(instance, oaam::systems::RequiredInformationA)

@given(instance=RequiredInformationA_strategy)
@settings(max_examples=50)
def test_requiredinformationa_instantiation(instance):
    assert isinstance(instance, RequiredInformationA)

@given(instance=Subsystem_strategy)
@settings(max_examples=50)
def test_subsystem_instantiation(instance):
    assert isinstance(instance, Subsystem)

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

@given(instance=library::ResourceProviderA_strategy)
@settings(max_examples=50)
def test_library::resourceprovidera_instantiation(instance):
    assert isinstance(instance, library::ResourceProviderA)

@given(instance=ResourceAlternatives_strategy)
@settings(max_examples=50)
def test_resourcealternatives_instantiation(instance):
    assert isinstance(instance, ResourceAlternatives)

@given(instance=ResourceTypeModifierReference_strategy)
@settings(max_examples=50)
def test_resourcetypemodifierreference_instantiation(instance):
    assert isinstance(instance, ResourceTypeModifierReference)

@given(instance=library::ResourceConsumerA_strategy)
@settings(max_examples=50)
def test_library::resourceconsumera_instantiation(instance):
    assert isinstance(instance, library::ResourceConsumerA)

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

@given(instance=oaam::library::ResourceProviderInstanceA_strategy)
@settings(max_examples=50)
def test_oaam::library::resourceproviderinstancea_instantiation(instance):
    assert isinstance(instance, oaam::library::ResourceProviderInstanceA)

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

@given(instance=oaam::library::ResourceProviderA_strategy)
@settings(max_examples=50)
def test_oaam::library::resourceprovidera_instantiation(instance):
    assert isinstance(instance, oaam::library::ResourceProviderA)

@given(instance=oaam::library::ResourceConsumerA_strategy)
@settings(max_examples=50)
def test_oaam::library::resourceconsumera_instantiation(instance):
    assert isinstance(instance, oaam::library::ResourceConsumerA)

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

@given(instance=oaam::common::FloatingPoint_strategy)
@settings(max_examples=50)
def test_oaam::common::floatingpoint_instantiation(instance):
    assert isinstance(instance, oaam::common::FloatingPoint)

@given(instance=oaam::common::FloatingPoint_strategy)
def test_oaam::common::floatingpoint_nBits_type(instance):
    assert isinstance(instance.nBits, int)


@given(instance=oaam::common::FloatingPoint_strategy)
def test_oaam::common::floatingpoint_nBits_setter(instance):
    original = instance.nBits
    instance.nBits = original
    assert instance.nBits == original

@given(instance=oaam::common::FloatingPoint_strategy)
def test_oaam::common::floatingpoint_endianess_type(instance):
    assert isinstance(instance.endianess, str)


@given(instance=oaam::common::FloatingPoint_strategy)
def test_oaam::common::floatingpoint_endianess_setter(instance):
    original = instance.endianess
    instance.endianess = original
    assert instance.endianess == original

@given(instance=oaam::common::Character_strategy)
@settings(max_examples=50)
def test_oaam::common::character_instantiation(instance):
    assert isinstance(instance, oaam::common::Character)

@given(instance=oaam::common::Character_strategy)
def test_oaam::common::character_encoding_type(instance):
    assert isinstance(instance.encoding, str)


@given(instance=oaam::common::Character_strategy)
def test_oaam::common::character_encoding_setter(instance):
    original = instance.encoding
    instance.encoding = original
    assert instance.encoding == original

@given(instance=oaam::common::Character_strategy)
def test_oaam::common::character_nBits_type(instance):
    assert isinstance(instance.nBits, int)


@given(instance=oaam::common::Character_strategy)
def test_oaam::common::character_nBits_setter(instance):
    original = instance.nBits
    instance.nBits = original
    assert instance.nBits == original

@given(instance=oaam::common::Byte_strategy)
@settings(max_examples=50)
def test_oaam::common::byte_instantiation(instance):
    assert isinstance(instance, oaam::common::Byte)

@given(instance=oaam::common::Byte_strategy)
def test_oaam::common::byte_nBits_type(instance):
    assert isinstance(instance.nBits, int)


@given(instance=oaam::common::Byte_strategy)
def test_oaam::common::byte_nBits_setter(instance):
    original = instance.nBits
    instance.nBits = original
    assert instance.nBits == original

@given(instance=oaam::common::Boolean_strategy)
@settings(max_examples=50)
def test_oaam::common::boolean_instantiation(instance):
    assert isinstance(instance, oaam::common::Boolean)

@given(instance=oaam::common::Boolean_strategy)
def test_oaam::common::boolean_nBits_type(instance):
    assert isinstance(instance.nBits, int)


@given(instance=oaam::common::Boolean_strategy)
def test_oaam::common::boolean_nBits_setter(instance):
    original = instance.nBits
    instance.nBits = original
    assert instance.nBits == original

@given(instance=oaam::common::Struct_strategy)
@settings(max_examples=50)
def test_oaam::common::struct_instantiation(instance):
    assert isinstance(instance, oaam::common::Struct)

@given(instance=oaam::common::Struct_strategy)
def test_oaam::common::struct_alignment_type(instance):
    assert isinstance(instance.alignment, int)


@given(instance=oaam::common::Struct_strategy)
def test_oaam::common::struct_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=oaam::common::Struct_strategy)
def test_oaam::common::struct_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=oaam::common::Struct_strategy)
def test_oaam::common::struct_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=oaam::common::Array_strategy)
@settings(max_examples=50)
def test_oaam::common::array_instantiation(instance):
    assert isinstance(instance, oaam::common::Array)

@given(instance=oaam::common::Array_strategy)
def test_oaam::common::array_alignment_type(instance):
    assert isinstance(instance.alignment, int)


@given(instance=oaam::common::Array_strategy)
def test_oaam::common::array_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=oaam::common::Array_strategy)
def test_oaam::common::array_nElements_type(instance):
    assert isinstance(instance.nElements, int)


@given(instance=oaam::common::Array_strategy)
def test_oaam::common::array_nElements_setter(instance):
    original = instance.nElements
    instance.nElements = original
    assert instance.nElements == original

@given(instance=oaam::common::Integer_strategy)
@settings(max_examples=50)
def test_oaam::common::integer_instantiation(instance):
    assert isinstance(instance, oaam::common::Integer)

@given(instance=oaam::common::Integer_strategy)
def test_oaam::common::integer_endianess_type(instance):
    assert isinstance(instance.endianess, str)


@given(instance=oaam::common::Integer_strategy)
def test_oaam::common::integer_endianess_setter(instance):
    original = instance.endianess
    instance.endianess = original
    assert instance.endianess == original

@given(instance=oaam::common::Integer_strategy)
def test_oaam::common::integer_nBits_type(instance):
    assert isinstance(instance.nBits, int)


@given(instance=oaam::common::Integer_strategy)
def test_oaam::common::integer_nBits_setter(instance):
    original = instance.nBits
    instance.nBits = original
    assert instance.nBits == original

@given(instance=oaam::common::Integer_strategy)
def test_oaam::common::integer_signed_type(instance):
    assert isinstance(instance.signed, bool)


@given(instance=oaam::common::Integer_strategy)
def test_oaam::common::integer_signed_setter(instance):
    original = instance.signed
    instance.signed = original
    assert instance.signed == original

@given(instance=BoolA_strategy)
@settings(max_examples=50)
def test_boola_instantiation(instance):
    assert isinstance(instance, BoolA)

@given(instance=common::OaamBaseElementA_strategy)
@settings(max_examples=50)
def test_common::oaambaseelementa_instantiation(instance):
    assert isinstance(instance, common::OaamBaseElementA)

@given(instance=oaam::capabilities::TaskOnDeviceCapability_strategy)
@settings(max_examples=50)
def test_oaam::capabilities::taskondevicecapability_instantiation(instance):
    assert isinstance(instance, oaam::capabilities::TaskOnDeviceCapability)

@given(instance=oaam::capabilities::TaskOnDeviceCapability_strategy)
def test_oaam::capabilities::taskondevicecapability_failureProbability_type(instance):
    assert isinstance(instance.failureProbability, float)


@given(instance=oaam::capabilities::TaskOnDeviceCapability_strategy)
def test_oaam::capabilities::taskondevicecapability_failureProbability_setter(instance):
    original = instance.failureProbability
    instance.failureProbability = original
    assert instance.failureProbability == original

@given(instance=oaam::capabilities::TaskOnDeviceCapability_strategy)
def test_oaam::capabilities::taskondevicecapability_worstCaseExecutionTime_type(instance):
    assert isinstance(instance.worstCaseExecutionTime, float)


@given(instance=oaam::capabilities::TaskOnDeviceCapability_strategy)
def test_oaam::capabilities::taskondevicecapability_worstCaseExecutionTime_setter(instance):
    original = instance.worstCaseExecutionTime
    instance.worstCaseExecutionTime = original
    assert instance.worstCaseExecutionTime == original

@given(instance=oaam::library::MessageType_strategy)
@settings(max_examples=50)
def test_oaam::library::messagetype_instantiation(instance):
    assert isinstance(instance, oaam::library::MessageType)

@given(instance=oaam::library::MessageType_strategy)
def test_oaam::library::messagetype_minLength_type(instance):
    assert isinstance(instance.minLength, int)


@given(instance=oaam::library::MessageType_strategy)
def test_oaam::library::messagetype_minLength_setter(instance):
    original = instance.minLength
    instance.minLength = original
    assert instance.minLength == original

@given(instance=oaam::library::MessageType_strategy)
def test_oaam::library::messagetype_maxLength_type(instance):
    assert isinstance(instance.maxLength, int)


@given(instance=oaam::library::MessageType_strategy)
def test_oaam::library::messagetype_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original

@given(instance=oaam::library::MessageType_strategy)
def test_oaam::library::messagetype_alignment_type(instance):
    assert isinstance(instance.alignment, int)


@given(instance=oaam::library::MessageType_strategy)
def test_oaam::library::messagetype_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=oaam::anatomy::Duct_strategy)
@settings(max_examples=50)
def test_oaam::anatomy::duct_instantiation(instance):
    assert isinstance(instance, oaam::anatomy::Duct)

@given(instance=oaam::anatomy::Duct_strategy)
def test_oaam::anatomy::duct_length_type(instance):
    assert isinstance(instance.length, float)


@given(instance=oaam::anatomy::Duct_strategy)
def test_oaam::anatomy::duct_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=oaam::hardware::DeviceSymmetry_strategy)
@settings(max_examples=50)
def test_oaam::hardware::devicesymmetry_instantiation(instance):
    assert isinstance(instance, oaam::hardware::DeviceSymmetry)

@given(instance=oaam::restrictions::AreaRestriction_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::arearestriction_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::AreaRestriction)

@given(instance=oaam::restrictions::AreaRestriction_strategy)
def test_oaam::restrictions::arearestriction_isForbidden_type(instance):
    assert isinstance(instance.isForbidden, bool)


@given(instance=oaam::restrictions::AreaRestriction_strategy)
def test_oaam::restrictions::arearestriction_isForbidden_setter(instance):
    original = instance.isForbidden
    instance.isForbidden = original
    assert instance.isForbidden == original

@given(instance=oaam::restrictions::AreaRestriction_strategy)
def test_oaam::restrictions::arearestriction_areaName_type(instance):
    assert isinstance(instance.areaName, str)


@given(instance=oaam::restrictions::AreaRestriction_strategy)
def test_oaam::restrictions::arearestriction_areaName_setter(instance):
    original = instance.areaName
    instance.areaName = original
    assert instance.areaName == original

@given(instance=oaam::anatomy::AreaSymmetry_strategy)
@settings(max_examples=50)
def test_oaam::anatomy::areasymmetry_instantiation(instance):
    assert isinstance(instance, oaam::anatomy::AreaSymmetry)

@given(instance=oaam::anatomy::Area_strategy)
@settings(max_examples=50)
def test_oaam::anatomy::area_instantiation(instance):
    assert isinstance(instance, oaam::anatomy::Area)

@given(instance=oaam::library::ResourceType_strategy)
@settings(max_examples=50)
def test_oaam::library::resourcetype_instantiation(instance):
    assert isinstance(instance, oaam::library::ResourceType)

@given(instance=oaam::library::ResourceType_strategy)
def test_oaam::library::resourcetype_isConsumed_type(instance):
    assert isinstance(instance.isConsumed, bool)


@given(instance=oaam::library::ResourceType_strategy)
def test_oaam::library::resourcetype_isConsumed_setter(instance):
    original = instance.isConsumed
    instance.isConsumed = original
    assert instance.isConsumed == original

@given(instance=oaam::library::ResourceType_strategy)
def test_oaam::library::resourcetype_isConfigurable_type(instance):
    assert isinstance(instance.isConfigurable, bool)


@given(instance=oaam::library::ResourceType_strategy)
def test_oaam::library::resourcetype_isConfigurable_setter(instance):
    original = instance.isConfigurable
    instance.isConfigurable = original
    assert instance.isConfigurable == original

@given(instance=oaam::library::ResourceType_strategy)
def test_oaam::library::resourcetype_isDistinguishable_type(instance):
    assert isinstance(instance.isDistinguishable, bool)


@given(instance=oaam::library::ResourceType_strategy)
def test_oaam::library::resourcetype_isDistinguishable_setter(instance):
    original = instance.isDistinguishable
    instance.isDistinguishable = original
    assert instance.isDistinguishable == original

@given(instance=oaam::library::ResourceType_strategy)
def test_oaam::library::resourcetype_isIo_type(instance):
    assert isinstance(instance.isIo, bool)


@given(instance=oaam::library::ResourceType_strategy)
def test_oaam::library::resourcetype_isIo_setter(instance):
    original = instance.isIo
    instance.isIo = original
    assert instance.isIo == original

@given(instance=oaam::library::ResourceType_strategy)
def test_oaam::library::resourcetype_isPropagated_type(instance):
    assert isinstance(instance.isPropagated, bool)


@given(instance=oaam::library::ResourceType_strategy)
def test_oaam::library::resourcetype_isPropagated_setter(instance):
    original = instance.isPropagated
    instance.isPropagated = original
    assert instance.isPropagated == original

@given(instance=oaam::library::ResourceType_strategy)
def test_oaam::library::resourcetype_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=oaam::library::ResourceType_strategy)
def test_oaam::library::resourcetype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=oaam::library::ResourceType_strategy)
def test_oaam::library::resourcetype_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=oaam::library::ResourceType_strategy)
def test_oaam::library::resourcetype_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=oaam::restrictions::TaskAtomicRestriction_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::taskatomicrestriction_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::TaskAtomicRestriction)

@given(instance=oaam::restrictions::LocationRestriction_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::locationrestriction_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::LocationRestriction)

@given(instance=oaam::restrictions::LocationRestriction_strategy)
def test_oaam::restrictions::locationrestriction_isForbidden_type(instance):
    assert isinstance(instance.isForbidden, bool)


@given(instance=oaam::restrictions::LocationRestriction_strategy)
def test_oaam::restrictions::locationrestriction_isForbidden_setter(instance):
    original = instance.isForbidden
    instance.isForbidden = original
    assert instance.isForbidden == original

@given(instance=oaam::restrictions::LocationRestriction_strategy)
def test_oaam::restrictions::locationrestriction_locationName_type(instance):
    assert isinstance(instance.locationName, str)


@given(instance=oaam::restrictions::LocationRestriction_strategy)
def test_oaam::restrictions::locationrestriction_locationName_setter(instance):
    original = instance.locationName
    instance.locationName = original
    assert instance.locationName == original

@given(instance=oaam::allocations::SignalAssignmentSegment_strategy)
@settings(max_examples=50)
def test_oaam::allocations::signalassignmentsegment_instantiation(instance):
    assert isinstance(instance, oaam::allocations::SignalAssignmentSegment)

@given(instance=oaam::systems::InformationMaterial_strategy)
@settings(max_examples=50)
def test_oaam::systems::informationmaterial_instantiation(instance):
    assert isinstance(instance, oaam::systems::InformationMaterial)

@given(instance=oaam::systems::InformationMaterial_strategy)
def test_oaam::systems::informationmaterial_velocity_type(instance):
    assert isinstance(instance.velocity, float)


@given(instance=oaam::systems::InformationMaterial_strategy)
def test_oaam::systems::informationmaterial_velocity_setter(instance):
    original = instance.velocity
    instance.velocity = original
    assert instance.velocity == original

@given(instance=oaam::systems::InformationMaterial_strategy)
def test_oaam::systems::informationmaterial_density_type(instance):
    assert isinstance(instance.density, float)


@given(instance=oaam::systems::InformationMaterial_strategy)
def test_oaam::systems::informationmaterial_density_setter(instance):
    original = instance.density
    instance.density = original
    assert instance.density == original

@given(instance=oaam::functions::TaskGroup_strategy)
@settings(max_examples=50)
def test_oaam::functions::taskgroup_instantiation(instance):
    assert isinstance(instance, oaam::functions::TaskGroup)

@given(instance=oaam::functions::Task_strategy)
@settings(max_examples=50)
def test_oaam::functions::task_instantiation(instance):
    assert isinstance(instance, oaam::functions::Task)

@given(instance=oaam::functions::Task_strategy)
def test_oaam::functions::task_nParallels_type(instance):
    assert isinstance(instance.nParallels, int)


@given(instance=oaam::functions::Task_strategy)
def test_oaam::functions::task_nParallels_setter(instance):
    original = instance.nParallels
    instance.nParallels = original
    assert instance.nParallels == original

@given(instance=oaam::functions::Task_strategy)
def test_oaam::functions::task_fixedRate_type(instance):
    assert isinstance(instance.fixedRate, float)


@given(instance=oaam::functions::Task_strategy)
def test_oaam::functions::task_fixedRate_setter(instance):
    original = instance.fixedRate
    instance.fixedRate = original
    assert instance.fixedRate == original

@given(instance=oaam::capabilities::SubconnectionInDeviceCapability_strategy)
@settings(max_examples=50)
def test_oaam::capabilities::subconnectionindevicecapability_instantiation(instance):
    assert isinstance(instance, oaam::capabilities::SubconnectionInDeviceCapability)

@given(instance=oaam::allocations::ScheduledTime_strategy)
@settings(max_examples=50)
def test_oaam::allocations::scheduledtime_instantiation(instance):
    assert isinstance(instance, oaam::allocations::ScheduledTime)

@given(instance=oaam::allocations::ScheduledTime_strategy)
def test_oaam::allocations::scheduledtime_duration_type(instance):
    assert isinstance(instance.duration, float)


@given(instance=oaam::allocations::ScheduledTime_strategy)
def test_oaam::allocations::scheduledtime_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=oaam::allocations::ScheduledTime_strategy)
def test_oaam::allocations::scheduledtime_restart_type(instance):
    assert isinstance(instance.restart, bool)


@given(instance=oaam::allocations::ScheduledTime_strategy)
def test_oaam::allocations::scheduledtime_restart_setter(instance):
    original = instance.restart
    instance.restart = original
    assert instance.restart == original

@given(instance=oaam::allocations::ScheduledTime_strategy)
def test_oaam::allocations::scheduledtime_startTime_type(instance):
    assert isinstance(instance.startTime, float)


@given(instance=oaam::allocations::ScheduledTime_strategy)
def test_oaam::allocations::scheduledtime_startTime_setter(instance):
    original = instance.startTime
    instance.startTime = original
    assert instance.startTime == original

@given(instance=oaam::allocations::ScheduledTime_strategy)
def test_oaam::allocations::scheduledtime_cycle_type(instance):
    assert isinstance(instance.cycle, int)


@given(instance=oaam::allocations::ScheduledTime_strategy)
def test_oaam::allocations::scheduledtime_cycle_setter(instance):
    original = instance.cycle
    instance.cycle = original
    assert instance.cycle == original

@given(instance=oaam::library::SignalType_strategy)
@settings(max_examples=50)
def test_oaam::library::signaltype_instantiation(instance):
    assert isinstance(instance, oaam::library::SignalType)

@given(instance=oaam::capabilities::DeviceInLocationCapability_strategy)
@settings(max_examples=50)
def test_oaam::capabilities::deviceinlocationcapability_instantiation(instance):
    assert isinstance(instance, oaam::capabilities::DeviceInLocationCapability)

@given(instance=oaam::library::TaskType_strategy)
@settings(max_examples=50)
def test_oaam::library::tasktype_instantiation(instance):
    assert isinstance(instance, oaam::library::TaskType)

@given(instance=oaam::library::TaskType_strategy)
def test_oaam::library::tasktype_isDeterministic_type(instance):
    assert isinstance(instance.isDeterministic, bool)


@given(instance=oaam::library::TaskType_strategy)
def test_oaam::library::tasktype_isDeterministic_setter(instance):
    original = instance.isDeterministic
    instance.isDeterministic = original
    assert instance.isDeterministic == original

@given(instance=oaam::library::TaskType_strategy)
def test_oaam::library::tasktype_preferredExecutionRate_type(instance):
    assert isinstance(instance.preferredExecutionRate, float)


@given(instance=oaam::library::TaskType_strategy)
def test_oaam::library::tasktype_preferredExecutionRate_setter(instance):
    original = instance.preferredExecutionRate
    instance.preferredExecutionRate = original
    assert instance.preferredExecutionRate == original

@given(instance=oaam::capabilities::MessageOnBusCapability_strategy)
@settings(max_examples=50)
def test_oaam::capabilities::messageonbuscapability_instantiation(instance):
    assert isinstance(instance, oaam::capabilities::MessageOnBusCapability)

@given(instance=oaam::allocations::ConnectionAssignment_strategy)
@settings(max_examples=50)
def test_oaam::allocations::connectionassignment_instantiation(instance):
    assert isinstance(instance, oaam::allocations::ConnectionAssignment)

@given(instance=oaam::allocations::DeviceAssignment_strategy)
@settings(max_examples=50)
def test_oaam::allocations::deviceassignment_instantiation(instance):
    assert isinstance(instance, oaam::allocations::DeviceAssignment)

@given(instance=oaam::capabilities::SubmessageInMessageCapability_strategy)
@settings(max_examples=50)
def test_oaam::capabilities::submessageinmessagecapability_instantiation(instance):
    assert isinstance(instance, oaam::capabilities::SubmessageInMessageCapability)

@given(instance=oaam::functions::Output_strategy)
@settings(max_examples=50)
def test_oaam::functions::output_instantiation(instance):
    assert isinstance(instance, oaam::functions::Output)

@given(instance=oaam::functions::Output_strategy)
def test_oaam::functions::output_fixedRate_type(instance):
    assert isinstance(instance.fixedRate, float)


@given(instance=oaam::functions::Output_strategy)
def test_oaam::functions::output_fixedRate_setter(instance):
    original = instance.fixedRate
    instance.fixedRate = original
    assert instance.fixedRate == original

@given(instance=oaam::hardware::Io_strategy)
@settings(max_examples=50)
def test_oaam::hardware::io_instantiation(instance):
    assert isinstance(instance, oaam::hardware::Io)

@given(instance=oaam::scenario::Variant_strategy)
@settings(max_examples=50)
def test_oaam::scenario::variant_instantiation(instance):
    assert isinstance(instance, oaam::scenario::Variant)

@given(instance=oaam::functions::ExternalTaskLink_strategy)
@settings(max_examples=50)
def test_oaam::functions::externaltasklink_instantiation(instance):
    assert isinstance(instance, oaam::functions::ExternalTaskLink)

@given(instance=oaam::functions::ExternalTaskLink_strategy)
def test_oaam::functions::externaltasklink_filter_type(instance):
    assert isinstance(instance.filter, str)


@given(instance=oaam::functions::ExternalTaskLink_strategy)
def test_oaam::functions::externaltasklink_filter_setter(instance):
    original = instance.filter
    instance.filter = original
    assert instance.filter == original

@given(instance=oaam::capabilities::ConnectionInDuctOrLocationCapability_strategy)
@settings(max_examples=50)
def test_oaam::capabilities::connectioninductorlocationcapability_instantiation(instance):
    assert isinstance(instance, oaam::capabilities::ConnectionInDuctOrLocationCapability)

@given(instance=oaam::allocations::MessageSegment_strategy)
@settings(max_examples=50)
def test_oaam::allocations::messagesegment_instantiation(instance):
    assert isinstance(instance, oaam::allocations::MessageSegment)

@given(instance=oaam::functions::TaskSymmetry_strategy)
@settings(max_examples=50)
def test_oaam::functions::tasksymmetry_instantiation(instance):
    assert isinstance(instance, oaam::functions::TaskSymmetry)

@given(instance=oaam::allocations::SubconnectionAssignment_strategy)
@settings(max_examples=50)
def test_oaam::allocations::subconnectionassignment_instantiation(instance):
    assert isinstance(instance, oaam::allocations::SubconnectionAssignment)

@given(instance=oaam::scenario::ScenarioParameterBool_strategy)
@settings(max_examples=50)
def test_oaam::scenario::scenarioparameterbool_instantiation(instance):
    assert isinstance(instance, oaam::scenario::ScenarioParameterBool)

@given(instance=oaam::scenario::ScenarioParameterBool_strategy)
def test_oaam::scenario::scenarioparameterbool_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=oaam::scenario::ScenarioParameterBool_strategy)
def test_oaam::scenario::scenarioparameterbool_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oaam::allocations::TaskAssignment_strategy)
@settings(max_examples=50)
def test_oaam::allocations::taskassignment_instantiation(instance):
    assert isinstance(instance, oaam::allocations::TaskAssignment)

@given(instance=oaam::functions::Signal_strategy)
@settings(max_examples=50)
def test_oaam::functions::signal_instantiation(instance):
    assert isinstance(instance, oaam::functions::Signal)

@given(instance=oaam::functions::Signal_strategy)
def test_oaam::functions::signal_inIndex_type(instance):
    assert isinstance(instance.inIndex, int)


@given(instance=oaam::functions::Signal_strategy)
def test_oaam::functions::signal_inIndex_setter(instance):
    original = instance.inIndex
    instance.inIndex = original
    assert instance.inIndex == original

@given(instance=oaam::functions::Signal_strategy)
def test_oaam::functions::signal_outIndex_type(instance):
    assert isinstance(instance.outIndex, int)


@given(instance=oaam::functions::Signal_strategy)
def test_oaam::functions::signal_outIndex_setter(instance):
    original = instance.outIndex
    instance.outIndex = original
    assert instance.outIndex == original

@given(instance=oaam::functions::ExternalOutputLink_strategy)
@settings(max_examples=50)
def test_oaam::functions::externaloutputlink_instantiation(instance):
    assert isinstance(instance, oaam::functions::ExternalOutputLink)

@given(instance=oaam::functions::ExternalOutputLink_strategy)
def test_oaam::functions::externaloutputlink_filter_type(instance):
    assert isinstance(instance.filter, str)


@given(instance=oaam::functions::ExternalOutputLink_strategy)
def test_oaam::functions::externaloutputlink_filter_setter(instance):
    original = instance.filter
    instance.filter = original
    assert instance.filter == original

@given(instance=oaam::hardware::Bus_strategy)
@settings(max_examples=50)
def test_oaam::hardware::bus_instantiation(instance):
    assert isinstance(instance, oaam::hardware::Bus)

@given(instance=oaam::hardware::Connection_strategy)
@settings(max_examples=50)
def test_oaam::hardware::connection_instantiation(instance):
    assert isinstance(instance, oaam::hardware::Connection)

@given(instance=oaam::functions::TaskRedundancy_strategy)
@settings(max_examples=50)
def test_oaam::functions::taskredundancy_instantiation(instance):
    assert isinstance(instance, oaam::functions::TaskRedundancy)

@given(instance=oaam::library::BusType_strategy)
@settings(max_examples=50)
def test_oaam::library::bustype_instantiation(instance):
    assert isinstance(instance, oaam::library::BusType)

@given(instance=oaam::library::BusType_strategy)
def test_oaam::library::bustype_isSelfManaging_type(instance):
    assert isinstance(instance.isSelfManaging, bool)


@given(instance=oaam::library::BusType_strategy)
def test_oaam::library::bustype_isSelfManaging_setter(instance):
    original = instance.isSelfManaging
    instance.isSelfManaging = original
    assert instance.isSelfManaging == original

@given(instance=oaam::library::BusType_strategy)
def test_oaam::library::bustype_mtbf_type(instance):
    assert isinstance(instance.mtbf, float)


@given(instance=oaam::library::BusType_strategy)
def test_oaam::library::bustype_mtbf_setter(instance):
    original = instance.mtbf
    instance.mtbf = original
    assert instance.mtbf == original

@given(instance=oaam::library::BusType_strategy)
def test_oaam::library::bustype_requiresMaster_type(instance):
    assert isinstance(instance.requiresMaster, bool)


@given(instance=oaam::library::BusType_strategy)
def test_oaam::library::bustype_requiresMaster_setter(instance):
    original = instance.requiresMaster
    instance.requiresMaster = original
    assert instance.requiresMaster == original

@given(instance=oaam::library::LocationType_strategy)
@settings(max_examples=50)
def test_oaam::library::locationtype_instantiation(instance):
    assert isinstance(instance, oaam::library::LocationType)

@given(instance=oaam::library::LocationType_strategy)
def test_oaam::library::locationtype_isJoint_type(instance):
    assert isinstance(instance.isJoint, bool)


@given(instance=oaam::library::LocationType_strategy)
def test_oaam::library::locationtype_isJoint_setter(instance):
    original = instance.isJoint
    instance.isJoint = original
    assert instance.isJoint == original

@given(instance=oaam::capabilities::SignalInMessageCapability_strategy)
@settings(max_examples=50)
def test_oaam::capabilities::signalinmessagecapability_instantiation(instance):
    assert isinstance(instance, oaam::capabilities::SignalInMessageCapability)

@given(instance=oaam::anatomy::LocationSymmetry_strategy)
@settings(max_examples=50)
def test_oaam::anatomy::locationsymmetry_instantiation(instance):
    assert isinstance(instance, oaam::anatomy::LocationSymmetry)

@given(instance=oaam::allocations::MessageA_strategy)
@settings(max_examples=50)
def test_oaam::allocations::messagea_instantiation(instance):
    assert isinstance(instance, oaam::allocations::MessageA)

@given(instance=oaam::allocations::MessageA_strategy)
def test_oaam::allocations::messagea_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=oaam::allocations::MessageA_strategy)
def test_oaam::allocations::messagea_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=oaam::allocations::MessageA_strategy)
def test_oaam::allocations::messagea_isPersistent_type(instance):
    assert isinstance(instance.isPersistent, bool)


@given(instance=oaam::allocations::MessageA_strategy)
def test_oaam::allocations::messagea_isPersistent_setter(instance):
    original = instance.isPersistent
    instance.isPersistent = original
    assert instance.isPersistent == original

@given(instance=oaam::anatomy::Location_strategy)
@settings(max_examples=50)
def test_oaam::anatomy::location_instantiation(instance):
    assert isinstance(instance, oaam::anatomy::Location)

@given(instance=oaam::anatomy::Location_strategy)
def test_oaam::anatomy::location_length_type(instance):
    assert isinstance(instance.length, float)


@given(instance=oaam::anatomy::Location_strategy)
def test_oaam::anatomy::location_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=oaam::functions::FunctionsContainerA_strategy)
@settings(max_examples=50)
def test_oaam::functions::functionscontainera_instantiation(instance):
    assert isinstance(instance, oaam::functions::FunctionsContainerA)

@given(instance=oaam::library::DeviceType_strategy)
@settings(max_examples=50)
def test_oaam::library::devicetype_instantiation(instance):
    assert isinstance(instance, oaam::library::DeviceType)

@given(instance=oaam::library::DeviceType_strategy)
def test_oaam::library::devicetype_weight_type(instance):
    assert isinstance(instance.weight, float)


@given(instance=oaam::library::DeviceType_strategy)
def test_oaam::library::devicetype_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=oaam::library::DeviceType_strategy)
def test_oaam::library::devicetype_canHaveSubdevices_type(instance):
    assert isinstance(instance.canHaveSubdevices, bool)


@given(instance=oaam::library::DeviceType_strategy)
def test_oaam::library::devicetype_canHaveSubdevices_setter(instance):
    original = instance.canHaveSubdevices
    instance.canHaveSubdevices = original
    assert instance.canHaveSubdevices == original

@given(instance=oaam::library::DeviceType_strategy)
def test_oaam::library::devicetype_mtbf_type(instance):
    assert isinstance(instance.mtbf, float)


@given(instance=oaam::library::DeviceType_strategy)
def test_oaam::library::devicetype_mtbf_setter(instance):
    original = instance.mtbf
    instance.mtbf = original
    assert instance.mtbf == original

@given(instance=oaam::library::DeviceType_strategy)
def test_oaam::library::devicetype_isSelfManaging_type(instance):
    assert isinstance(instance.isSelfManaging, bool)


@given(instance=oaam::library::DeviceType_strategy)
def test_oaam::library::devicetype_isSelfManaging_setter(instance):
    original = instance.isSelfManaging
    instance.isSelfManaging = original
    assert instance.isSelfManaging == original

@given(instance=oaam::library::DeviceType_strategy)
def test_oaam::library::devicetype_isSubdevice_type(instance):
    assert isinstance(instance.isSubdevice, bool)


@given(instance=oaam::library::DeviceType_strategy)
def test_oaam::library::devicetype_isSubdevice_setter(instance):
    original = instance.isSubdevice
    instance.isSubdevice = original
    assert instance.isSubdevice == original

@given(instance=oaam::library::DeviceType_strategy)
def test_oaam::library::devicetype_cost_type(instance):
    assert isinstance(instance.cost, float)


@given(instance=oaam::library::DeviceType_strategy)
def test_oaam::library::devicetype_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original

@given(instance=oaam::restrictions::SegregationRestriction_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::segregationrestriction_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::SegregationRestriction)

@given(instance=oaam::restrictions::SegregationRestriction_strategy)
def test_oaam::restrictions::segregationrestriction_dissimilarTechnology_type(instance):
    assert isinstance(instance.dissimilarTechnology, bool)


@given(instance=oaam::restrictions::SegregationRestriction_strategy)
def test_oaam::restrictions::segregationrestriction_dissimilarTechnology_setter(instance):
    original = instance.dissimilarTechnology
    instance.dissimilarTechnology = original
    assert instance.dissimilarTechnology == original

@given(instance=oaam::restrictions::SegregationRestriction_strategy)
def test_oaam::restrictions::segregationrestriction_dissimilarArea_type(instance):
    assert isinstance(instance.dissimilarArea, bool)


@given(instance=oaam::restrictions::SegregationRestriction_strategy)
def test_oaam::restrictions::segregationrestriction_dissimilarArea_setter(instance):
    original = instance.dissimilarArea
    instance.dissimilarArea = original
    assert instance.dissimilarArea == original

@given(instance=oaam::restrictions::SegregationRestriction_strategy)
def test_oaam::restrictions::segregationrestriction_dissimilarPowerSource_type(instance):
    assert isinstance(instance.dissimilarPowerSource, bool)


@given(instance=oaam::restrictions::SegregationRestriction_strategy)
def test_oaam::restrictions::segregationrestriction_dissimilarPowerSource_setter(instance):
    original = instance.dissimilarPowerSource
    instance.dissimilarPowerSource = original
    assert instance.dissimilarPowerSource == original

@given(instance=oaam::restrictions::SegregationRestriction_strategy)
def test_oaam::restrictions::segregationrestriction_dissimilarLocation_type(instance):
    assert isinstance(instance.dissimilarLocation, bool)


@given(instance=oaam::restrictions::SegregationRestriction_strategy)
def test_oaam::restrictions::segregationrestriction_dissimilarLocation_setter(instance):
    original = instance.dissimilarLocation
    instance.dissimilarLocation = original
    assert instance.dissimilarLocation == original

@given(instance=oaam::scenario::ScenarioParameterNumeric_strategy)
@settings(max_examples=50)
def test_oaam::scenario::scenarioparameternumeric_instantiation(instance):
    assert isinstance(instance, oaam::scenario::ScenarioParameterNumeric)

@given(instance=oaam::scenario::ScenarioParameterNumeric_strategy)
def test_oaam::scenario::scenarioparameternumeric_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=oaam::scenario::ScenarioParameterNumeric_strategy)
def test_oaam::scenario::scenarioparameternumeric_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oaam::library::ResourceTypeModifierLevel_strategy)
@settings(max_examples=50)
def test_oaam::library::resourcetypemodifierlevel_instantiation(instance):
    assert isinstance(instance, oaam::library::ResourceTypeModifierLevel)

@given(instance=oaam::restrictions::DeviceTypeRestriction_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::devicetyperestriction_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::DeviceTypeRestriction)

@given(instance=oaam::restrictions::DeviceTypeRestriction_strategy)
def test_oaam::restrictions::devicetyperestriction_deviceTypeName_type(instance):
    assert isinstance(instance.deviceTypeName, str)


@given(instance=oaam::restrictions::DeviceTypeRestriction_strategy)
def test_oaam::restrictions::devicetyperestriction_deviceTypeName_setter(instance):
    original = instance.deviceTypeName
    instance.deviceTypeName = original
    assert instance.deviceTypeName == original

@given(instance=oaam::restrictions::DeviceTypeRestriction_strategy)
def test_oaam::restrictions::devicetyperestriction_isForbidden_type(instance):
    assert isinstance(instance.isForbidden, bool)


@given(instance=oaam::restrictions::DeviceTypeRestriction_strategy)
def test_oaam::restrictions::devicetyperestriction_isForbidden_setter(instance):
    original = instance.isForbidden
    instance.isForbidden = original
    assert instance.isForbidden == original

@given(instance=oaam::restrictions::ConnectionTypeRestriction_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::connectiontyperestriction_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::ConnectionTypeRestriction)

@given(instance=oaam::restrictions::ConnectionTypeRestriction_strategy)
def test_oaam::restrictions::connectiontyperestriction_connectionTypeName_type(instance):
    assert isinstance(instance.connectionTypeName, str)


@given(instance=oaam::restrictions::ConnectionTypeRestriction_strategy)
def test_oaam::restrictions::connectiontyperestriction_connectionTypeName_setter(instance):
    original = instance.connectionTypeName
    instance.connectionTypeName = original
    assert instance.connectionTypeName == original

@given(instance=oaam::restrictions::ConnectionTypeRestriction_strategy)
def test_oaam::restrictions::connectiontyperestriction_isForbidden_type(instance):
    assert isinstance(instance.isForbidden, bool)


@given(instance=oaam::restrictions::ConnectionTypeRestriction_strategy)
def test_oaam::restrictions::connectiontyperestriction_isForbidden_setter(instance):
    original = instance.isForbidden
    instance.isForbidden = original
    assert instance.isForbidden == original

@given(instance=oaam::scenario::OperationMode_strategy)
@settings(max_examples=50)
def test_oaam::scenario::operationmode_instantiation(instance):
    assert isinstance(instance, oaam::scenario::OperationMode)

@given(instance=oaam::hardware::Device_strategy)
@settings(max_examples=50)
def test_oaam::hardware::device_instantiation(instance):
    assert isinstance(instance, oaam::hardware::Device)

@given(instance=oaam::restrictions::DeviceRestriction_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::devicerestriction_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::DeviceRestriction)

@given(instance=oaam::restrictions::DeviceRestriction_strategy)
def test_oaam::restrictions::devicerestriction_isForbidden_type(instance):
    assert isinstance(instance.isForbidden, bool)


@given(instance=oaam::restrictions::DeviceRestriction_strategy)
def test_oaam::restrictions::devicerestriction_isForbidden_setter(instance):
    original = instance.isForbidden
    instance.isForbidden = original
    assert instance.isForbidden == original

@given(instance=oaam::restrictions::DeviceRestriction_strategy)
def test_oaam::restrictions::devicerestriction_deviceName_type(instance):
    assert isinstance(instance.deviceName, str)


@given(instance=oaam::restrictions::DeviceRestriction_strategy)
def test_oaam::restrictions::devicerestriction_deviceName_setter(instance):
    original = instance.deviceName
    instance.deviceName = original
    assert instance.deviceName == original

@given(instance=oaam::allocations::Schedule_strategy)
@settings(max_examples=50)
def test_oaam::allocations::schedule_instantiation(instance):
    assert isinstance(instance, oaam::allocations::Schedule)

@given(instance=oaam::allocations::Schedule_strategy)
def test_oaam::allocations::schedule_rate_type(instance):
    assert isinstance(instance.rate, float)


@given(instance=oaam::allocations::Schedule_strategy)
def test_oaam::allocations::schedule_rate_setter(instance):
    original = instance.rate
    instance.rate = original
    assert instance.rate == original

@given(instance=oaam::allocations::Schedule_strategy)
def test_oaam::allocations::schedule_isPeriodic_type(instance):
    assert isinstance(instance.isPeriodic, bool)


@given(instance=oaam::allocations::Schedule_strategy)
def test_oaam::allocations::schedule_isPeriodic_setter(instance):
    original = instance.isPeriodic
    instance.isPeriodic = original
    assert instance.isPeriodic == original

@given(instance=oaam::allocations::Schedule_strategy)
def test_oaam::allocations::schedule_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=oaam::allocations::Schedule_strategy)
def test_oaam::allocations::schedule_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=oaam::systems::InformationPower_strategy)
@settings(max_examples=50)
def test_oaam::systems::informationpower_instantiation(instance):
    assert isinstance(instance, oaam::systems::InformationPower)

@given(instance=oaam::systems::InformationPower_strategy)
def test_oaam::systems::informationpower_power_type(instance):
    assert isinstance(instance.power, float)


@given(instance=oaam::systems::InformationPower_strategy)
def test_oaam::systems::informationpower_power_setter(instance):
    original = instance.power
    instance.power = original
    assert instance.power == original

@given(instance=oaam::restrictions::TimeDelayRestriction_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::timedelayrestriction_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::TimeDelayRestriction)

@given(instance=oaam::restrictions::TimeDelayRestriction_strategy)
def test_oaam::restrictions::timedelayrestriction_delay_type(instance):
    assert isinstance(instance.delay, float)


@given(instance=oaam::restrictions::TimeDelayRestriction_strategy)
def test_oaam::restrictions::timedelayrestriction_delay_setter(instance):
    original = instance.delay
    instance.delay = original
    assert instance.delay == original

@given(instance=oaam::library::ResourceBundle_strategy)
@settings(max_examples=50)
def test_oaam::library::resourcebundle_instantiation(instance):
    assert isinstance(instance, oaam::library::ResourceBundle)

@given(instance=oaam::library::ResourceBundle_strategy)
def test_oaam::library::resourcebundle_mtbf_type(instance):
    assert isinstance(instance.mtbf, float)


@given(instance=oaam::library::ResourceBundle_strategy)
def test_oaam::library::resourcebundle_mtbf_setter(instance):
    original = instance.mtbf
    instance.mtbf = original
    assert instance.mtbf == original

@given(instance=oaam::library::ResourceBundle_strategy)
def test_oaam::library::resourcebundle_mass_type(instance):
    assert isinstance(instance.mass, float)


@given(instance=oaam::library::ResourceBundle_strategy)
def test_oaam::library::resourcebundle_mass_setter(instance):
    original = instance.mass
    instance.mass = original
    assert instance.mass == original

@given(instance=oaam::library::ResourceBundle_strategy)
def test_oaam::library::resourcebundle_cost_type(instance):
    assert isinstance(instance.cost, float)


@given(instance=oaam::library::ResourceBundle_strategy)
def test_oaam::library::resourcebundle_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original

@given(instance=oaam::library::DuctType_strategy)
@settings(max_examples=50)
def test_oaam::library::ducttype_instantiation(instance):
    assert isinstance(instance, oaam::library::DuctType)

@given(instance=oaam::restrictions::PowerSourceRestriction_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::powersourcerestriction_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::PowerSourceRestriction)

@given(instance=oaam::restrictions::PowerSourceRestriction_strategy)
def test_oaam::restrictions::powersourcerestriction_powerSourceName_type(instance):
    assert isinstance(instance.powerSourceName, str)


@given(instance=oaam::restrictions::PowerSourceRestriction_strategy)
def test_oaam::restrictions::powersourcerestriction_powerSourceName_setter(instance):
    original = instance.powerSourceName
    instance.powerSourceName = original
    assert instance.powerSourceName == original

@given(instance=oaam::restrictions::PowerSourceRestriction_strategy)
def test_oaam::restrictions::powersourcerestriction_isForbidden_type(instance):
    assert isinstance(instance.isForbidden, bool)


@given(instance=oaam::restrictions::PowerSourceRestriction_strategy)
def test_oaam::restrictions::powersourcerestriction_isForbidden_setter(instance):
    original = instance.isForbidden
    instance.isForbidden = original
    assert instance.isForbidden == original

@given(instance=oaam::capabilities::SignalOnConnectionOrDeviceCapability_strategy)
@settings(max_examples=50)
def test_oaam::capabilities::signalonconnectionordevicecapability_instantiation(instance):
    assert isinstance(instance, oaam::capabilities::SignalOnConnectionOrDeviceCapability)

@given(instance=oaam::capabilities::SignalOnConnectionOrDeviceCapability_strategy)
def test_oaam::capabilities::signalonconnectionordevicecapability_worstCaseTransmissionTime_type(instance):
    assert isinstance(instance.worstCaseTransmissionTime, float)


@given(instance=oaam::capabilities::SignalOnConnectionOrDeviceCapability_strategy)
def test_oaam::capabilities::signalonconnectionordevicecapability_worstCaseTransmissionTime_setter(instance):
    original = instance.worstCaseTransmissionTime
    instance.worstCaseTransmissionTime = original
    assert instance.worstCaseTransmissionTime == original

@given(instance=oaam::functions::Input_strategy)
@settings(max_examples=50)
def test_oaam::functions::input_instantiation(instance):
    assert isinstance(instance, oaam::functions::Input)

@given(instance=oaam::functions::Input_strategy)
def test_oaam::functions::input_queueLength_type(instance):
    assert isinstance(instance.queueLength, int)


@given(instance=oaam::functions::Input_strategy)
def test_oaam::functions::input_queueLength_setter(instance):
    original = instance.queueLength
    instance.queueLength = original
    assert instance.queueLength == original

@given(instance=oaam::systems::System_strategy)
@settings(max_examples=50)
def test_oaam::systems::system_instantiation(instance):
    assert isinstance(instance, oaam::systems::System)

@given(instance=oaam::anatomy::DuctOpening_strategy)
@settings(max_examples=50)
def test_oaam::anatomy::ductopening_instantiation(instance):
    assert isinstance(instance, oaam::anatomy::DuctOpening)

@given(instance=oaam::allocations::ConnectionAssignmentSegment_strategy)
@settings(max_examples=50)
def test_oaam::allocations::connectionassignmentsegment_instantiation(instance):
    assert isinstance(instance, oaam::allocations::ConnectionAssignmentSegment)

@given(instance=oaam::functions::FailureCondition_strategy)
@settings(max_examples=50)
def test_oaam::functions::failurecondition_instantiation(instance):
    assert isinstance(instance, oaam::functions::FailureCondition)

@given(instance=oaam::functions::FailureCondition_strategy)
def test_oaam::functions::failurecondition_maxOccurrenceProbability_type(instance):
    assert isinstance(instance.maxOccurrenceProbability, float)


@given(instance=oaam::functions::FailureCondition_strategy)
def test_oaam::functions::failurecondition_maxOccurrenceProbability_setter(instance):
    original = instance.maxOccurrenceProbability
    instance.maxOccurrenceProbability = original
    assert instance.maxOccurrenceProbability == original

@given(instance=oaam::functions::FailureCondition_strategy)
def test_oaam::functions::failurecondition_noSingleFailure_type(instance):
    assert isinstance(instance.noSingleFailure, bool)


@given(instance=oaam::functions::FailureCondition_strategy)
def test_oaam::functions::failurecondition_noSingleFailure_setter(instance):
    original = instance.noSingleFailure
    instance.noSingleFailure = original
    assert instance.noSingleFailure == original

@given(instance=oaam::restrictions::TaskSymmetryRestriction_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::tasksymmetryrestriction_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::TaskSymmetryRestriction)

@given(instance=oaam::restrictions::TaskSymmetryRestriction_strategy)
def test_oaam::restrictions::tasksymmetryrestriction_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=oaam::restrictions::TaskSymmetryRestriction_strategy)
def test_oaam::restrictions::tasksymmetryrestriction_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=oaam::allocations::SubdeviceAssignment_strategy)
@settings(max_examples=50)
def test_oaam::allocations::subdeviceassignment_instantiation(instance):
    assert isinstance(instance, oaam::allocations::SubdeviceAssignment)

@given(instance=oaam::library::ConnectionType_strategy)
@settings(max_examples=50)
def test_oaam::library::connectiontype_instantiation(instance):
    assert isinstance(instance, oaam::library::ConnectionType)

@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_maxInterfaceToJointDistance_type(instance):
    assert isinstance(instance.maxInterfaceToJointDistance, float)


@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_maxInterfaceToJointDistance_setter(instance):
    original = instance.maxInterfaceToJointDistance
    instance.maxInterfaceToJointDistance = original
    assert instance.maxInterfaceToJointDistance == original

@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_isPower_type(instance):
    assert isinstance(instance.isPower, bool)


@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_isPower_setter(instance):
    original = instance.isPower
    instance.isPower = original
    assert instance.isPower == original

@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_isSwitched_type(instance):
    assert isinstance(instance.isSwitched, bool)


@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_isSwitched_setter(instance):
    original = instance.isSwitched
    instance.isSwitched = original
    assert instance.isSwitched == original

@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_nJoints_type(instance):
    assert isinstance(instance.nJoints, int)


@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_nJoints_setter(instance):
    original = instance.nJoints
    instance.nJoints = original
    assert instance.nJoints == original

@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_allowsCircles_type(instance):
    assert isinstance(instance.allowsCircles, bool)


@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_allowsCircles_setter(instance):
    original = instance.allowsCircles
    instance.allowsCircles = original
    assert instance.allowsCircles == original

@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_maxJointBranches_type(instance):
    assert isinstance(instance.maxJointBranches, int)


@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_maxJointBranches_setter(instance):
    original = instance.maxJointBranches
    instance.maxJointBranches = original
    assert instance.maxJointBranches == original

@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_isUnidirectional_type(instance):
    assert isinstance(instance.isUnidirectional, bool)


@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_isUnidirectional_setter(instance):
    original = instance.isUnidirectional
    instance.isUnidirectional = original
    assert instance.isUnidirectional == original

@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_isWireless_type(instance):
    assert isinstance(instance.isWireless, bool)


@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_isWireless_setter(instance):
    original = instance.isWireless
    instance.isWireless = original
    assert instance.isWireless == original

@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_nStartingPoints_type(instance):
    assert isinstance(instance.nStartingPoints, int)


@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_nStartingPoints_setter(instance):
    original = instance.nStartingPoints
    instance.nStartingPoints = original
    assert instance.nStartingPoints == original

@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_directConnectionsAllowed_type(instance):
    assert isinstance(instance.directConnectionsAllowed, bool)


@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_directConnectionsAllowed_setter(instance):
    original = instance.directConnectionsAllowed
    instance.directConnectionsAllowed = original
    assert instance.directConnectionsAllowed == original

@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_maxLength_type(instance):
    assert isinstance(instance.maxLength, float)


@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original

@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_requiresMaster_type(instance):
    assert isinstance(instance.requiresMaster, bool)


@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_requiresMaster_setter(instance):
    original = instance.requiresMaster
    instance.requiresMaster = original
    assert instance.requiresMaster == original

@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_isInformation_type(instance):
    assert isinstance(instance.isInformation, bool)


@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_isInformation_setter(instance):
    original = instance.isInformation
    instance.isInformation = original
    assert instance.isInformation == original

@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_nEndPoints_type(instance):
    assert isinstance(instance.nEndPoints, int)


@given(instance=oaam::library::ConnectionType_strategy)
def test_oaam::library::connectiontype_nEndPoints_setter(instance):
    original = instance.nEndPoints
    instance.nEndPoints = original
    assert instance.nEndPoints == original

@given(instance=oaam::anatomy::Position3D_strategy)
@settings(max_examples=50)
def test_oaam::anatomy::position3d_instantiation(instance):
    assert isinstance(instance, oaam::anatomy::Position3D)

@given(instance=oaam::anatomy::Position3D_strategy)
def test_oaam::anatomy::position3d_x_type(instance):
    assert isinstance(instance.x, float)


@given(instance=oaam::anatomy::Position3D_strategy)
def test_oaam::anatomy::position3d_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=oaam::anatomy::Position3D_strategy)
def test_oaam::anatomy::position3d_y_type(instance):
    assert isinstance(instance.y, float)


@given(instance=oaam::anatomy::Position3D_strategy)
def test_oaam::anatomy::position3d_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=oaam::anatomy::Position3D_strategy)
def test_oaam::anatomy::position3d_z_type(instance):
    assert isinstance(instance.z, float)


@given(instance=oaam::anatomy::Position3D_strategy)
def test_oaam::anatomy::position3d_z_setter(instance):
    original = instance.z
    instance.z = original
    assert instance.z == original

@given(instance=oaam::restrictions::SynchronicityRestriction_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::synchronicityrestriction_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::SynchronicityRestriction)

@given(instance=oaam::restrictions::SynchronicityRestriction_strategy)
def test_oaam::restrictions::synchronicityrestriction_maxJitter_type(instance):
    assert isinstance(instance.maxJitter, float)


@given(instance=oaam::restrictions::SynchronicityRestriction_strategy)
def test_oaam::restrictions::synchronicityrestriction_maxJitter_setter(instance):
    original = instance.maxJitter
    instance.maxJitter = original
    assert instance.maxJitter == original

@given(instance=oaam::restrictions::ConnectionRestriction_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::connectionrestriction_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::ConnectionRestriction)

@given(instance=oaam::restrictions::ConnectionRestriction_strategy)
def test_oaam::restrictions::connectionrestriction_isForbidden_type(instance):
    assert isinstance(instance.isForbidden, bool)


@given(instance=oaam::restrictions::ConnectionRestriction_strategy)
def test_oaam::restrictions::connectionrestriction_isForbidden_setter(instance):
    original = instance.isForbidden
    instance.isForbidden = original
    assert instance.isForbidden == original

@given(instance=oaam::restrictions::ConnectionRestriction_strategy)
def test_oaam::restrictions::connectionrestriction_connectionName_type(instance):
    assert isinstance(instance.connectionName, str)


@given(instance=oaam::restrictions::ConnectionRestriction_strategy)
def test_oaam::restrictions::connectionrestriction_connectionName_setter(instance):
    original = instance.connectionName
    instance.connectionName = original
    assert instance.connectionName == original

@given(instance=oaam::systems::InformationFlow_strategy)
@settings(max_examples=50)
def test_oaam::systems::informationflow_instantiation(instance):
    assert isinstance(instance, oaam::systems::InformationFlow)

@given(instance=oaam::capabilities::SubdeviceInDeviceCapability_strategy)
@settings(max_examples=50)
def test_oaam::capabilities::subdeviceindevicecapability_instantiation(instance):
    assert isinstance(instance, oaam::capabilities::SubdeviceInDeviceCapability)

@given(instance=oaam::systems::InformationSignal_strategy)
@settings(max_examples=50)
def test_oaam::systems::informationsignal_instantiation(instance):
    assert isinstance(instance, oaam::systems::InformationSignal)

@given(instance=oaam::systems::InformationSignal_strategy)
def test_oaam::systems::informationsignal_latency_type(instance):
    assert isinstance(instance.latency, float)


@given(instance=oaam::systems::InformationSignal_strategy)
def test_oaam::systems::informationsignal_latency_setter(instance):
    original = instance.latency
    instance.latency = original
    assert instance.latency == original

@given(instance=oaam::systems::InformationSignal_strategy)
def test_oaam::systems::informationsignal_rate_type(instance):
    assert isinstance(instance.rate, float)


@given(instance=oaam::systems::InformationSignal_strategy)
def test_oaam::systems::informationsignal_rate_setter(instance):
    original = instance.rate
    instance.rate = original
    assert instance.rate == original

@given(instance=oaam::systems::InformationSignal_strategy)
def test_oaam::systems::informationsignal_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=oaam::systems::InformationSignal_strategy)
def test_oaam::systems::informationsignal_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=oaam::systems::InformationSignal_strategy)
def test_oaam::systems::informationsignal_accuracy_type(instance):
    assert isinstance(instance.accuracy, float)


@given(instance=oaam::systems::InformationSignal_strategy)
def test_oaam::systems::informationsignal_accuracy_setter(instance):
    original = instance.accuracy
    instance.accuracy = original
    assert instance.accuracy == original

@given(instance=oaam::systems::InformationSignal_strategy)
def test_oaam::systems::informationsignal_resolution_type(instance):
    assert isinstance(instance.resolution, float)


@given(instance=oaam::systems::InformationSignal_strategy)
def test_oaam::systems::informationsignal_resolution_setter(instance):
    original = instance.resolution
    instance.resolution = original
    assert instance.resolution == original

@given(instance=oaam::allocations::SignalAssignment_strategy)
@settings(max_examples=50)
def test_oaam::allocations::signalassignment_instantiation(instance):
    assert isinstance(instance, oaam::allocations::SignalAssignment)

@given(instance=oaam::capabilities::MessageOnConnectionOrDeviceCapability_strategy)
@settings(max_examples=50)
def test_oaam::capabilities::messageonconnectionordevicecapability_instantiation(instance):
    assert isinstance(instance, oaam::capabilities::MessageOnConnectionOrDeviceCapability)

@given(instance=oaam::capabilities::MessageOnConnectionOrDeviceCapability_strategy)
def test_oaam::capabilities::messageonconnectionordevicecapability_worstCaseTransmissionTime_type(instance):
    assert isinstance(instance.worstCaseTransmissionTime, float)


@given(instance=oaam::capabilities::MessageOnConnectionOrDeviceCapability_strategy)
def test_oaam::capabilities::messageonconnectionordevicecapability_worstCaseTransmissionTime_setter(instance):
    original = instance.worstCaseTransmissionTime
    instance.worstCaseTransmissionTime = original
    assert instance.worstCaseTransmissionTime == original

@given(instance=oaam::functions::SignalGroup_strategy)
@settings(max_examples=50)
def test_oaam::functions::signalgroup_instantiation(instance):
    assert isinstance(instance, oaam::functions::SignalGroup)

@given(instance=common::BoolA_strategy)
@settings(max_examples=50)
def test_common::boola_instantiation(instance):
    assert isinstance(instance, common::BoolA)

@given(instance=oaam::library::TaskInputState_strategy)
@settings(max_examples=50)
def test_oaam::library::taskinputstate_instantiation(instance):
    assert isinstance(instance, oaam::library::TaskInputState)

@given(instance=oaam::library::TaskInputState_strategy)
def test_oaam::library::taskinputstate_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=oaam::library::TaskInputState_strategy)
def test_oaam::library::taskinputstate_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=oaam::functions::OutputIntegrityState_strategy)
@settings(max_examples=50)
def test_oaam::functions::outputintegritystate_instantiation(instance):
    assert isinstance(instance, oaam::functions::OutputIntegrityState)

@given(instance=oaam::functions::OutputIntegrityState_strategy)
def test_oaam::functions::outputintegritystate_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=oaam::functions::OutputIntegrityState_strategy)
def test_oaam::functions::outputintegritystate_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=oaam::common::BoolNot_strategy)
@settings(max_examples=50)
def test_oaam::common::boolnot_instantiation(instance):
    assert isinstance(instance, oaam::common::BoolNot)

@given(instance=oaam::library::TaskInputTrigger_strategy)
@settings(max_examples=50)
def test_oaam::library::taskinputtrigger_instantiation(instance):
    assert isinstance(instance, oaam::library::TaskInputTrigger)

@given(instance=oaam::common::BoolOperation_strategy)
@settings(max_examples=50)
def test_oaam::common::booloperation_instantiation(instance):
    assert isinstance(instance, oaam::common::BoolOperation)

@given(instance=oaam::common::BoolOperation_strategy)
def test_oaam::common::booloperation_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=oaam::common::BoolOperation_strategy)
def test_oaam::common::booloperation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=oaam::common::BoolA_strategy)
@settings(max_examples=50)
def test_oaam::common::boola_instantiation(instance):
    assert isinstance(instance, oaam::common::BoolA)

@given(instance=AttributeA_strategy)
@settings(max_examples=50)
def test_attributea_instantiation(instance):
    assert isinstance(instance, AttributeA)

@given(instance=oaam::common::AttributeReference_strategy)
@settings(max_examples=50)
def test_oaam::common::attributereference_instantiation(instance):
    assert isinstance(instance, oaam::common::AttributeReference)

@given(instance=oaam::common::AttributeNumeric_strategy)
@settings(max_examples=50)
def test_oaam::common::attributenumeric_instantiation(instance):
    assert isinstance(instance, oaam::common::AttributeNumeric)

@given(instance=oaam::common::AttributeNumeric_strategy)
def test_oaam::common::attributenumeric_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=oaam::common::AttributeNumeric_strategy)
def test_oaam::common::attributenumeric_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oaam::common::AttributeString_strategy)
@settings(max_examples=50)
def test_oaam::common::attributestring_instantiation(instance):
    assert isinstance(instance, oaam::common::AttributeString)

@given(instance=oaam::common::AttributeString_strategy)
def test_oaam::common::attributestring_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=oaam::common::AttributeString_strategy)
def test_oaam::common::attributestring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oaam::common::AttributeContainment_strategy)
@settings(max_examples=50)
def test_oaam::common::attributecontainment_instantiation(instance):
    assert isinstance(instance, oaam::common::AttributeContainment)

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

@given(instance=oaam::common::OaamBaseElementA_strategy)
@settings(max_examples=50)
def test_oaam::common::oaambaseelementa_instantiation(instance):
    assert isinstance(instance, oaam::common::OaamBaseElementA)

@given(instance=oaam::common::OaamBaseElementA_strategy)
def test_oaam::common::oaambaseelementa_documentation_type(instance):
    assert isinstance(instance.documentation, str)


@given(instance=oaam::common::OaamBaseElementA_strategy)
def test_oaam::common::oaambaseelementa_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original

@given(instance=oaam::common::OaamBaseElementA_strategy)
def test_oaam::common::oaambaseelementa_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=oaam::common::OaamBaseElementA_strategy)
def test_oaam::common::oaambaseelementa_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=oaam::common::OaamBaseElementA_strategy)
def test_oaam::common::oaambaseelementa_modified_type(instance):
    assert isinstance(instance.modified, date)


@given(instance=oaam::common::OaamBaseElementA_strategy)
def test_oaam::common::oaambaseelementa_modified_setter(instance):
    original = instance.modified
    instance.modified = original
    assert instance.modified == original

@given(instance=oaam::common::OaamBaseElementA_strategy)
def test_oaam::common::oaambaseelementa_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=oaam::common::OaamBaseElementA_strategy)
def test_oaam::common::oaambaseelementa_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=oaam::common::OaamBaseElementA_strategy)
def test_oaam::common::oaambaseelementa_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oaam::common::OaamBaseElementA_strategy)
def test_oaam::common::oaambaseelementa_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oaam::common::OaamBaseElementA_strategy)
def test_oaam::common::oaambaseelementa_modifier_type(instance):
    assert isinstance(instance.modifier, str)


@given(instance=oaam::common::OaamBaseElementA_strategy)
def test_oaam::common::oaambaseelementa_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=oaam::common::OaamBaseElementA_strategy)
def test_oaam::common::oaambaseelementa_traceLink_type(instance):
    assert isinstance(instance.traceLink, str)


@given(instance=oaam::common::OaamBaseElementA_strategy)
def test_oaam::common::oaambaseelementa_traceLink_setter(instance):
    original = instance.traceLink
    instance.traceLink = original
    assert instance.traceLink == original

@given(instance=Library_strategy)
@settings(max_examples=50)
def test_library_instantiation(instance):
    assert isinstance(instance, Library)

@given(instance=OaamBaseElementA_strategy)
@settings(max_examples=50)
def test_oaambaseelementa_instantiation(instance):
    assert isinstance(instance, OaamBaseElementA)

@given(instance=oaam::library::ResourceTypeModifier_strategy)
@settings(max_examples=50)
def test_oaam::library::resourcetypemodifier_instantiation(instance):
    assert isinstance(instance, oaam::library::ResourceTypeModifier)

@given(instance=oaam::library::TaskStateDeclaration_strategy)
@settings(max_examples=50)
def test_oaam::library::taskstatedeclaration_instantiation(instance):
    assert isinstance(instance, oaam::library::TaskStateDeclaration)

@given(instance=oaam::library::DuctOpeningDeclaration_strategy)
@settings(max_examples=50)
def test_oaam::library::ductopeningdeclaration_instantiation(instance):
    assert isinstance(instance, oaam::library::DuctOpeningDeclaration)

@given(instance=oaam::library::ResourceGroup_strategy)
@settings(max_examples=50)
def test_oaam::library::resourcegroup_instantiation(instance):
    assert isinstance(instance, oaam::library::ResourceGroup)

@given(instance=oaam::scenario::ScenarioContainerA_strategy)
@settings(max_examples=50)
def test_oaam::scenario::scenariocontainera_instantiation(instance):
    assert isinstance(instance, oaam::scenario::ScenarioContainerA)

@given(instance=oaam::library::DeviceTypeDissimilarity_strategy)
@settings(max_examples=50)
def test_oaam::library::devicetypedissimilarity_instantiation(instance):
    assert isinstance(instance, oaam::library::DeviceTypeDissimilarity)

@given(instance=oaam::library::DeviceTypeDissimilarity_strategy)
def test_oaam::library::devicetypedissimilarity_percentageOfCommonHardware_type(instance):
    assert isinstance(instance.percentageOfCommonHardware, float)


@given(instance=oaam::library::DeviceTypeDissimilarity_strategy)
def test_oaam::library::devicetypedissimilarity_percentageOfCommonHardware_setter(instance):
    original = instance.percentageOfCommonHardware
    instance.percentageOfCommonHardware = original
    assert instance.percentageOfCommonHardware == original

@given(instance=oaam::common::AttributeA_strategy)
@settings(max_examples=50)
def test_oaam::common::attributea_instantiation(instance):
    assert isinstance(instance, oaam::common::AttributeA)

@given(instance=oaam::library::WireType_strategy)
@settings(max_examples=50)
def test_oaam::library::wiretype_instantiation(instance):
    assert isinstance(instance, oaam::library::WireType)

@given(instance=oaam::library::WireType_strategy)
def test_oaam::library::wiretype_specificWeight_type(instance):
    assert isinstance(instance.specificWeight, float)


@given(instance=oaam::library::WireType_strategy)
def test_oaam::library::wiretype_specificWeight_setter(instance):
    original = instance.specificWeight
    instance.specificWeight = original
    assert instance.specificWeight == original

@given(instance=oaam::library::WireType_strategy)
def test_oaam::library::wiretype_mtbf_type(instance):
    assert isinstance(instance.mtbf, float)


@given(instance=oaam::library::WireType_strategy)
def test_oaam::library::wiretype_mtbf_setter(instance):
    original = instance.mtbf
    instance.mtbf = original
    assert instance.mtbf == original

@given(instance=oaam::library::WireType_strategy)
def test_oaam::library::wiretype_specificPrice_type(instance):
    assert isinstance(instance.specificPrice, float)


@given(instance=oaam::library::WireType_strategy)
def test_oaam::library::wiretype_specificPrice_setter(instance):
    original = instance.specificPrice
    instance.specificPrice = original
    assert instance.specificPrice == original

@given(instance=oaam::library::WireType_strategy)
def test_oaam::library::wiretype_minBendingRadius_type(instance):
    assert isinstance(instance.minBendingRadius, float)


@given(instance=oaam::library::WireType_strategy)
def test_oaam::library::wiretype_minBendingRadius_setter(instance):
    original = instance.minBendingRadius
    instance.minBendingRadius = original
    assert instance.minBendingRadius == original

@given(instance=oaam::library::WireType_strategy)
def test_oaam::library::wiretype_nShields_type(instance):
    assert isinstance(instance.nShields, int)


@given(instance=oaam::library::WireType_strategy)
def test_oaam::library::wiretype_nShields_setter(instance):
    original = instance.nShields
    instance.nShields = original
    assert instance.nShields == original

@given(instance=oaam::library::WireType_strategy)
def test_oaam::library::wiretype_nConductors_type(instance):
    assert isinstance(instance.nConductors, int)


@given(instance=oaam::library::WireType_strategy)
def test_oaam::library::wiretype_nConductors_setter(instance):
    original = instance.nConductors
    instance.nConductors = original
    assert instance.nConductors == original

@given(instance=oaam::library::InputDeclaration_strategy)
@settings(max_examples=50)
def test_oaam::library::inputdeclaration_instantiation(instance):
    assert isinstance(instance, oaam::library::InputDeclaration)

@given(instance=oaam::library::InputDeclaration_strategy)
def test_oaam::library::inputdeclaration_precondition_type(instance):
    assert isinstance(instance.precondition, str)


@given(instance=oaam::library::InputDeclaration_strategy)
def test_oaam::library::inputdeclaration_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original

@given(instance=oaam::library::InputDeclaration_strategy)
def test_oaam::library::inputdeclaration_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=oaam::library::InputDeclaration_strategy)
def test_oaam::library::inputdeclaration_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=oaam::library::InputDeclaration_strategy)
def test_oaam::library::inputdeclaration_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=oaam::library::InputDeclaration_strategy)
def test_oaam::library::inputdeclaration_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=oaam::library::InputDeclaration_strategy)
def test_oaam::library::inputdeclaration_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=oaam::library::InputDeclaration_strategy)
def test_oaam::library::inputdeclaration_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=oaam::library::InputDeclaration_strategy)
def test_oaam::library::inputdeclaration_range_type(instance):
    assert isinstance(instance.range, str)


@given(instance=oaam::library::InputDeclaration_strategy)
def test_oaam::library::inputdeclaration_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original

@given(instance=oaam::library::LibraryContainerA_strategy)
@settings(max_examples=50)
def test_oaam::library::librarycontainera_instantiation(instance):
    assert isinstance(instance, oaam::library::LibraryContainerA)

@given(instance=oaam::library::AttributeDefinition_strategy)
@settings(max_examples=50)
def test_oaam::library::attributedefinition_instantiation(instance):
    assert isinstance(instance, oaam::library::AttributeDefinition)

@given(instance=oaam::library::AttributeDefinition_strategy)
def test_oaam::library::attributedefinition_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=oaam::library::AttributeDefinition_strategy)
def test_oaam::library::attributedefinition_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=oaam::library::AttributeDefinition_strategy)
def test_oaam::library::attributedefinition_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=oaam::library::AttributeDefinition_strategy)
def test_oaam::library::attributedefinition_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=oaam::library::ResourceLink_strategy)
@settings(max_examples=50)
def test_oaam::library::resourcelink_instantiation(instance):
    assert isinstance(instance, oaam::library::ResourceLink)

@given(instance=oaam::library::IoDeclaration_strategy)
@settings(max_examples=50)
def test_oaam::library::iodeclaration_instantiation(instance):
    assert isinstance(instance, oaam::library::IoDeclaration)

@given(instance=oaam::library::ResourceTypeModifierReference_strategy)
@settings(max_examples=50)
def test_oaam::library::resourcetypemodifierreference_instantiation(instance):
    assert isinstance(instance, oaam::library::ResourceTypeModifierReference)

@given(instance=oaam::systems::InputSegregation_strategy)
@settings(max_examples=50)
def test_oaam::systems::inputsegregation_instantiation(instance):
    assert isinstance(instance, oaam::systems::InputSegregation)

@given(instance=oaam::systems::InputSegregation_strategy)
def test_oaam::systems::inputsegregation_dissimilarRoute_type(instance):
    assert isinstance(instance.dissimilarRoute, bool)


@given(instance=oaam::systems::InputSegregation_strategy)
def test_oaam::systems::inputsegregation_dissimilarRoute_setter(instance):
    original = instance.dissimilarRoute
    instance.dissimilarRoute = original
    assert instance.dissimilarRoute == original

@given(instance=oaam::systems::InputSegregation_strategy)
def test_oaam::systems::inputsegregation_dissimilarSource_type(instance):
    assert isinstance(instance.dissimilarSource, bool)


@given(instance=oaam::systems::InputSegregation_strategy)
def test_oaam::systems::inputsegregation_dissimilarSource_setter(instance):
    original = instance.dissimilarSource
    instance.dissimilarSource = original
    assert instance.dissimilarSource == original

@given(instance=oaam::systems::InputSegregation_strategy)
def test_oaam::systems::inputsegregation_dissimilarTechnology_type(instance):
    assert isinstance(instance.dissimilarTechnology, bool)


@given(instance=oaam::systems::InputSegregation_strategy)
def test_oaam::systems::inputsegregation_dissimilarTechnology_setter(instance):
    original = instance.dissimilarTechnology
    instance.dissimilarTechnology = original
    assert instance.dissimilarTechnology == original

@given(instance=oaam::functions::TaskParameter_strategy)
@settings(max_examples=50)
def test_oaam::functions::taskparameter_instantiation(instance):
    assert isinstance(instance, oaam::functions::TaskParameter)

@given(instance=oaam::functions::TaskParameter_strategy)
def test_oaam::functions::taskparameter_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=oaam::functions::TaskParameter_strategy)
def test_oaam::functions::taskparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oaam::library::FaultPropagation_strategy)
@settings(max_examples=50)
def test_oaam::library::faultpropagation_instantiation(instance):
    assert isinstance(instance, oaam::library::FaultPropagation)

@given(instance=oaam::library::FaultPropagation_strategy)
def test_oaam::library::faultpropagation_outputState_type(instance):
    assert isinstance(instance.outputState, str)


@given(instance=oaam::library::FaultPropagation_strategy)
def test_oaam::library::faultpropagation_outputState_setter(instance):
    original = instance.outputState
    instance.outputState = original
    assert instance.outputState == original

@given(instance=oaam::library::Resource_strategy)
@settings(max_examples=50)
def test_oaam::library::resource_instantiation(instance):
    assert isinstance(instance, oaam::library::Resource)

@given(instance=oaam::library::Resource_strategy)
def test_oaam::library::resource_count_type(instance):
    assert isinstance(instance.count, float)


@given(instance=oaam::library::Resource_strategy)
def test_oaam::library::resource_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=oaam::systems::SystemsContainerA_strategy)
@settings(max_examples=50)
def test_oaam::systems::systemscontainera_instantiation(instance):
    assert isinstance(instance, oaam::systems::SystemsContainerA)

@given(instance=oaam::hardware::HardwareContainerA_strategy)
@settings(max_examples=50)
def test_oaam::hardware::hardwarecontainera_instantiation(instance):
    assert isinstance(instance, oaam::hardware::HardwareContainerA)

@given(instance=oaam::restrictions::RestrictionsContainerA_strategy)
@settings(max_examples=50)
def test_oaam::restrictions::restrictionscontainera_instantiation(instance):
    assert isinstance(instance, oaam::restrictions::RestrictionsContainerA)

@given(instance=oaam::capabilities::CapabilitiesContainerA_strategy)
@settings(max_examples=50)
def test_oaam::capabilities::capabilitiescontainera_instantiation(instance):
    assert isinstance(instance, oaam::capabilities::CapabilitiesContainerA)

@given(instance=oaam::library::TaskTypeDissimilarity_strategy)
@settings(max_examples=50)
def test_oaam::library::tasktypedissimilarity_instantiation(instance):
    assert isinstance(instance, oaam::library::TaskTypeDissimilarity)

@given(instance=oaam::library::TaskTypeDissimilarity_strategy)
def test_oaam::library::tasktypedissimilarity_percentageOfCommonCode_type(instance):
    assert isinstance(instance.percentageOfCommonCode, float)


@given(instance=oaam::library::TaskTypeDissimilarity_strategy)
def test_oaam::library::tasktypedissimilarity_percentageOfCommonCode_setter(instance):
    original = instance.percentageOfCommonCode
    instance.percentageOfCommonCode = original
    assert instance.percentageOfCommonCode == original

@given(instance=oaam::scenario::OperationModeReference_strategy)
@settings(max_examples=50)
def test_oaam::scenario::operationmodereference_instantiation(instance):
    assert isinstance(instance, oaam::scenario::OperationModeReference)

@given(instance=oaam::scenario::OperationModeReference_strategy)
def test_oaam::scenario::operationmodereference_activeProbability_type(instance):
    assert isinstance(instance.activeProbability, float)


@given(instance=oaam::scenario::OperationModeReference_strategy)
def test_oaam::scenario::operationmodereference_activeProbability_setter(instance):
    original = instance.activeProbability
    instance.activeProbability = original
    assert instance.activeProbability == original

@given(instance=oaam::allocations::AllocationsContainerA_strategy)
@settings(max_examples=50)
def test_oaam::allocations::allocationscontainera_instantiation(instance):
    assert isinstance(instance, oaam::allocations::AllocationsContainerA)

@given(instance=oaam::capabilities::ResourceConsumption_strategy)
@settings(max_examples=50)
def test_oaam::capabilities::resourceconsumption_instantiation(instance):
    assert isinstance(instance, oaam::capabilities::ResourceConsumption)

@given(instance=oaam::capabilities::ResourceConsumption_strategy)
def test_oaam::capabilities::resourceconsumption_count_type(instance):
    assert isinstance(instance.count, float)


@given(instance=oaam::capabilities::ResourceConsumption_strategy)
def test_oaam::capabilities::resourceconsumption_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=oaam::library::IoGroup_strategy)
@settings(max_examples=50)
def test_oaam::library::iogroup_instantiation(instance):
    assert isinstance(instance, oaam::library::IoGroup)

@given(instance=oaam::library::OutputDeclaration_strategy)
@settings(max_examples=50)
def test_oaam::library::outputdeclaration_instantiation(instance):
    assert isinstance(instance, oaam::library::OutputDeclaration)

@given(instance=oaam::library::OutputDeclaration_strategy)
def test_oaam::library::outputdeclaration_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=oaam::library::OutputDeclaration_strategy)
def test_oaam::library::outputdeclaration_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=oaam::library::OutputDeclaration_strategy)
def test_oaam::library::outputdeclaration_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=oaam::library::OutputDeclaration_strategy)
def test_oaam::library::outputdeclaration_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=oaam::library::OutputDeclaration_strategy)
def test_oaam::library::outputdeclaration_postcondition_type(instance):
    assert isinstance(instance.postcondition, str)


@given(instance=oaam::library::OutputDeclaration_strategy)
def test_oaam::library::outputdeclaration_postcondition_setter(instance):
    original = instance.postcondition
    instance.postcondition = original
    assert instance.postcondition == original

@given(instance=oaam::library::OutputDeclaration_strategy)
def test_oaam::library::outputdeclaration_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=oaam::library::OutputDeclaration_strategy)
def test_oaam::library::outputdeclaration_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=oaam::library::OutputDeclaration_strategy)
def test_oaam::library::outputdeclaration_range_type(instance):
    assert isinstance(instance.range, str)


@given(instance=oaam::library::OutputDeclaration_strategy)
def test_oaam::library::outputdeclaration_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original

@given(instance=oaam::library::ResourceAlternatives_strategy)
@settings(max_examples=50)
def test_oaam::library::resourcealternatives_instantiation(instance):
    assert isinstance(instance, oaam::library::ResourceAlternatives)

@given(instance=oaam::library::TaskOutputTrigger_strategy)
@settings(max_examples=50)
def test_oaam::library::taskoutputtrigger_instantiation(instance):
    assert isinstance(instance, oaam::library::TaskOutputTrigger)

@given(instance=oaam::library::TaskOutputTrigger_strategy)
def test_oaam::library::taskoutputtrigger_fixedRate_type(instance):
    assert isinstance(instance.fixedRate, float)


@given(instance=oaam::library::TaskOutputTrigger_strategy)
def test_oaam::library::taskoutputtrigger_fixedRate_setter(instance):
    original = instance.fixedRate
    instance.fixedRate = original
    assert instance.fixedRate == original

@given(instance=oaam::library::TaskOutputTrigger_strategy)
def test_oaam::library::taskoutputtrigger_isFixedRate_type(instance):
    assert isinstance(instance.isFixedRate, bool)


@given(instance=oaam::library::TaskOutputTrigger_strategy)
def test_oaam::library::taskoutputtrigger_isFixedRate_setter(instance):
    original = instance.isFixedRate
    instance.isFixedRate = original
    assert instance.isFixedRate == original

@given(instance=oaam::library::IoType_strategy)
@settings(max_examples=50)
def test_oaam::library::iotype_instantiation(instance):
    assert isinstance(instance, oaam::library::IoType)

@given(instance=oaam::library::IoType_strategy)
def test_oaam::library::iotype_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=oaam::library::IoType_strategy)
def test_oaam::library::iotype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=oaam::library::PowerSource_strategy)
@settings(max_examples=50)
def test_oaam::library::powersource_instantiation(instance):
    assert isinstance(instance, oaam::library::PowerSource)

@given(instance=oaam::library::DeviceTypeSymmetry_strategy)
@settings(max_examples=50)
def test_oaam::library::devicetypesymmetry_instantiation(instance):
    assert isinstance(instance, oaam::library::DeviceTypeSymmetry)

@given(instance=oaam::common::DataTypeA_strategy)
@settings(max_examples=50)
def test_oaam::common::datatypea_instantiation(instance):
    assert isinstance(instance, oaam::common::DataTypeA)

@given(instance=oaam::library::TaskParameterDeclaration_strategy)
@settings(max_examples=50)
def test_oaam::library::taskparameterdeclaration_instantiation(instance):
    assert isinstance(instance, oaam::library::TaskParameterDeclaration)

@given(instance=oaam::library::ResourceTypeDissimilarity_strategy)
@settings(max_examples=50)
def test_oaam::library::resourcetypedissimilarity_instantiation(instance):
    assert isinstance(instance, oaam::library::ResourceTypeDissimilarity)

@given(instance=oaam::anatomy::AnatomyContainerA_strategy)
@settings(max_examples=50)
def test_oaam::anatomy::anatomycontainera_instantiation(instance):
    assert isinstance(instance, oaam::anatomy::AnatomyContainerA)

@given(instance=oaam::Architecture_strategy)
@settings(max_examples=50)
def test_oaam::architecture_instantiation(instance):
    assert isinstance(instance, oaam::Architecture)

@given(instance=Systems_strategy)
@settings(max_examples=50)
def test_systems_instantiation(instance):
    assert isinstance(instance, Systems)

@given(instance=Scenario_strategy)
@settings(max_examples=50)
def test_scenario_instantiation(instance):
    assert isinstance(instance, Scenario)
