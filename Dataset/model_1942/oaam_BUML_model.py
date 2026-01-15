####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
BoolOperationTypesE: Enumeration = Enumeration(
    name="BoolOperationTypesE",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="XOR")
    }
)

IntegretyStateE: Enumeration = Enumeration(
    name="IntegretyStateE",
    literals={
            EnumerationLiteral(name="FAILED"),
			EnumerationLiteral(name="UNKNOWN"),
			EnumerationLiteral(name="OK")
    }
)

EndianessE: Enumeration = Enumeration(
    name="EndianessE",
    literals={
            EnumerationLiteral(name="BIG"),
			EnumerationLiteral(name="LITTLE")
    }
)

AttributeTargetsE: Enumeration = Enumeration(
    name="AttributeTargetsE",
    literals={
            EnumerationLiteral(name="DEVICE_TYPE"),
			EnumerationLiteral(name="DEVICE"),
			EnumerationLiteral(name="TASK_TYPE"),
			EnumerationLiteral(name="TASK"),
			EnumerationLiteral(name="CONNECTION_TYPE"),
			EnumerationLiteral(name="CONNECTION"),
			EnumerationLiteral(name="LOCATION_TYPE"),
			EnumerationLiteral(name="LOCATION"),
			EnumerationLiteral(name="WIRE_TYPE"),
			EnumerationLiteral(name="DUCT_TYPE"),
			EnumerationLiteral(name="RESOURCE_TYPE"),
			EnumerationLiteral(name="RESOURCE"),
			EnumerationLiteral(name="SIGNAL_TYPE"),
			EnumerationLiteral(name="SIGNAL"),
			EnumerationLiteral(name="DUCT"),
			EnumerationLiteral(name="RESOURCE_BUNDLE"),
			EnumerationLiteral(name="RESOURCE_ALTERNATIVE"),
			EnumerationLiteral(name="RESOURCE_GROUP"),
			EnumerationLiteral(name="AREA"),
			EnumerationLiteral(name="VARIANT")
    }
)

IoDirectionE: Enumeration = Enumeration(
    name="IoDirectionE",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="OUT"),
			EnumerationLiteral(name="BOTH")
    }
)

AttributeTypesE: Enumeration = Enumeration(
    name="AttributeTypesE",
    literals={
            EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="NUMERIC"),
			EnumerationLiteral(name="BOOL")
    }
)

SymmetryTypesE: Enumeration = Enumeration(
    name="SymmetryTypesE",
    literals={
            EnumerationLiteral(name="LOCATION"),
			EnumerationLiteral(name="DEVICE"),
			EnumerationLiteral(name="AREA"),
			EnumerationLiteral(name="DEVICE_TYPE")
    }
)

# Classes
oaam_Architecture = Class(name="oaam::Architecture")
OaamBaseElementA = Class(name="OaamBaseElementA")
Anatomy = Class(name="Anatomy")
Capabilities = Class(name="Capabilities")
Library = Class(name="Library")
Scenario = Class(name="Scenario")
Systems = Class(name="Systems")
Functions = Class(name="Functions")
Hardware = Class(name="Hardware")
oaam_common_OaamBaseElementA = Class(name="oaam::common::OaamBaseElementA", is_abstract=True)
Restrictions = Class(name="Restrictions")
Allocations = Class(name="Allocations")
oaam_common_AttributeA = Class(name="oaam::common::AttributeA", is_abstract=True)
oaam_common_AttributeString = Class(name="oaam::common::AttributeString")
AttributeA = Class(name="AttributeA")
oaam_common_BoolA = Class(name="oaam::common::BoolA", is_abstract=True)
oaam_common_BoolOperation = Class(name="oaam::common::BoolOperation")
common_BoolA = Class(name="common::BoolA")
common_OaamBaseElementA = Class(name="common::OaamBaseElementA")
BoolA = Class(name="BoolA")
oaam_common_AttributeNumeric = Class(name="oaam::common::AttributeNumeric")
oaam_common_AttributeContainment = Class(name="oaam::common::AttributeContainment")
oaam_common_AttributeReference = Class(name="oaam::common::AttributeReference")
oaam_common_Array = Class(name="oaam::common::Array")
oaam_common_BoolNot = Class(name="oaam::common::BoolNot")
oaam_common_DataTypeA = Class(name="oaam::common::DataTypeA", is_abstract=True)
oaam_common_Integer = Class(name="oaam::common::Integer")
DataTypeA = Class(name="DataTypeA")
oaam_common_FloatingPoint = Class(name="oaam::common::FloatingPoint")
oaam_common_Struct = Class(name="oaam::common::Struct")
Struct = Class(name="Struct")
oaam_common_Boolean = Class(name="oaam::common::Boolean")
oaam_common_Byte = Class(name="oaam::common::Byte")
oaam_common_Character = Class(name="oaam::common::Character")
ResourceGroup = Class(name="ResourceGroup")
oaam_library_ResourceProviderA = Class(name="oaam::library::ResourceProviderA", is_abstract=True)
ResourceBundle = Class(name="ResourceBundle")
ResourceType = Class(name="ResourceType")
ResourceLink = Class(name="ResourceLink")
oaam_library_ResourceProviderInstanceA = Class(name="oaam::library::ResourceProviderInstanceA", is_abstract=True)
oaam_library_ResourceConsumerA = Class(name="oaam::library::ResourceConsumerA", is_abstract=True)
Resource = Class(name="Resource")
oaam_library_LibraryContainerA = Class(name="oaam::library::LibraryContainerA", is_abstract=True)
ResourceTypeModifier = Class(name="ResourceTypeModifier")
ResourceTypeDissimilarity = Class(name="ResourceTypeDissimilarity")
TaskType = Class(name="TaskType")
TaskTypeDissimilarity = Class(name="TaskTypeDissimilarity")
SignalType = Class(name="SignalType")
ResourceTypeModifierLevel = Class(name="ResourceTypeModifierLevel")
IoType = Class(name="IoType")
DeviceTypeDissimilarity = Class(name="DeviceTypeDissimilarity")
BusType = Class(name="BusType")
ConnectionType = Class(name="ConnectionType")
WireType = Class(name="WireType")
LocationType = Class(name="LocationType")
DuctType = Class(name="DuctType")
AttributeDefinition = Class(name="AttributeDefinition")
PowerSource = Class(name="PowerSource")
DeviceType = Class(name="DeviceType")
Sublibrary = Class(name="Sublibrary")
DeviceTypeSymmetry = Class(name="DeviceTypeSymmetry")
ResourceAlternatives = Class(name="ResourceAlternatives")
oaam_library_Resource = Class(name="oaam::library::Resource")
MessageType = Class(name="MessageType")
oaam_library_ResourceType = Class(name="oaam::library::ResourceType")
library_ResourceConsumerA = Class(name="library::ResourceConsumerA")
ResourceTypeModifierReference = Class(name="ResourceTypeModifierReference")
TaskStateDeclaration = Class(name="TaskStateDeclaration")
oaam_library_ResourceAlternatives = Class(name="oaam::library::ResourceAlternatives")
oaam_library_ResourceBundle = Class(name="oaam::library::ResourceBundle")
oaam_library_TaskType = Class(name="oaam::library::TaskType")
OutputDeclaration = Class(name="OutputDeclaration")
InputDeclaration = Class(name="InputDeclaration")
TaskParameterDeclaration = Class(name="TaskParameterDeclaration")
oaam_library_SignalType = Class(name="oaam::library::SignalType")
oaam_library_DeviceType = Class(name="oaam::library::DeviceType")
library_ResourceProviderA = Class(name="library::ResourceProviderA")
IoDeclaration = Class(name="IoDeclaration")
IoGroup = Class(name="IoGroup")
oaam_library_ConnectionType = Class(name="oaam::library::ConnectionType")
oaam_library_LocationType = Class(name="oaam::library::LocationType")
oaam_library_IoType = Class(name="oaam::library::IoType")
DuctOpeningDeclaration = Class(name="DuctOpeningDeclaration")
oaam_library_DuctType = Class(name="oaam::library::DuctType")
oaam_library_WireType = Class(name="oaam::library::WireType")
TaskOutputTrigger = Class(name="TaskOutputTrigger")
oaam_library_InputDeclaration = Class(name="oaam::library::InputDeclaration")
oaam_library_OutputDeclaration = Class(name="oaam::library::OutputDeclaration")
oaam_library_ResourceGroup = Class(name="oaam::library::ResourceGroup")
oaam_library_DeviceTypeSymmetry = Class(name="oaam::library::DeviceTypeSymmetry")
FaultPropagation = Class(name="FaultPropagation")
oaam_library_IoDeclaration = Class(name="oaam::library::IoDeclaration")
oaam_library_DuctOpeningDeclaration = Class(name="oaam::library::DuctOpeningDeclaration")
BoolOperation = Class(name="BoolOperation")
oaam_library_IoGroup = Class(name="oaam::library::IoGroup")
oaam_library_AttributeDefinition = Class(name="oaam::library::AttributeDefinition")
oaam_library_FaultPropagation = Class(name="oaam::library::FaultPropagation")
oaam_library_ResourceTypeModifier = Class(name="oaam::library::ResourceTypeModifier")
BoolNot = Class(name="BoolNot")
TaskInputState = Class(name="TaskInputState")
oaam_library_TaskInputState = Class(name="oaam::library::TaskInputState")
oaam_library_PowerSource = Class(name="oaam::library::PowerSource")
oaam_library_ResourceLink = Class(name="oaam::library::ResourceLink")
oaam_library_TaskTypeDissimilarity = Class(name="oaam::library::TaskTypeDissimilarity")
oaam_library_ResourceTypeModifierLevel = Class(name="oaam::library::ResourceTypeModifierLevel")
oaam_library_ResourceTypeModifierReference = Class(name="oaam::library::ResourceTypeModifierReference")
oaam_library_TaskOutputTrigger = Class(name="oaam::library::TaskOutputTrigger")
oaam_library_DeviceTypeDissimilarity = Class(name="oaam::library::DeviceTypeDissimilarity")
oaam_library_ResourceTypeDissimilarity = Class(name="oaam::library::ResourceTypeDissimilarity")
oaam_library_TaskInputTrigger = Class(name="oaam::library::TaskInputTrigger")
TaskInputTrigger = Class(name="TaskInputTrigger")
oaam_library_BusType = Class(name="oaam::library::BusType")
oaam_library_TaskStateDeclaration = Class(name="oaam::library::TaskStateDeclaration")
oaam_library_TaskParameterDeclaration = Class(name="oaam::library::TaskParameterDeclaration")
oaam_library_MessageType = Class(name="oaam::library::MessageType")
oaam_library_Library = Class(name="oaam::library::Library")
LibraryContainerA = Class(name="LibraryContainerA")
oaam_library_Sublibrary = Class(name="oaam::library::Sublibrary")
oaam_scenario_VariantDependentElementA = Class(name="oaam::scenario::VariantDependentElementA", is_abstract=True)
Variant = Class(name="Variant")
oaam_scenario_ScenarioParameterA = Class(name="oaam::scenario::ScenarioParameterA", is_abstract=True)
scenario_ModeDependentElementA = Class(name="scenario::ModeDependentElementA")
scenario_VariantDependentElementA = Class(name="scenario::VariantDependentElementA")
oaam_scenario_ModeDependentElementA = Class(name="oaam::scenario::ModeDependentElementA", is_abstract=True)
OperationModeReference = Class(name="OperationModeReference")
oaam_scenario_OperationMode = Class(name="oaam::scenario::OperationMode")
oaam_scenario_ScenarioParameterNumeric = Class(name="oaam::scenario::ScenarioParameterNumeric")
scenario_ScenarioParameterA = Class(name="scenario::ScenarioParameterA")
oaam_scenario_ScenarioContainerA = Class(name="oaam::scenario::ScenarioContainerA", is_abstract=True)
ScenarioParameterA = Class(name="ScenarioParameterA")
OperationMode = Class(name="OperationMode")
Subscenario = Class(name="Subscenario")
oaam_scenario_Scenario = Class(name="oaam::scenario::Scenario")
ScenarioContainerA = Class(name="ScenarioContainerA")
oaam_scenario_Subscenario = Class(name="oaam::scenario::Subscenario")
oaam_scenario_ScenarioParameterBool = Class(name="oaam::scenario::ScenarioParameterBool")
oaam_scenario_Variant = Class(name="oaam::scenario::Variant")
oaam_scenario_OperationModeReference = Class(name="oaam::scenario::OperationModeReference")
oaam_systems_Systems = Class(name="oaam::systems::Systems")
SystemsContainerA = Class(name="SystemsContainerA")
oaam_systems_Subsystem = Class(name="oaam::systems::Subsystem")
systems_SystemsContainerA = Class(name="systems::SystemsContainerA")
oaam_systems_SystemsContainerA = Class(name="oaam::systems::SystemsContainerA", is_abstract=True)
System = Class(name="System")
InformationFlow = Class(name="InformationFlow")
InputSegregation = Class(name="InputSegregation")
Subsystem = Class(name="Subsystem")
oaam_systems_System = Class(name="oaam::systems::System")
ProvidedInformationA = Class(name="ProvidedInformationA")
RequiredInformationA = Class(name="RequiredInformationA")
oaam_systems_RequiredInformationA = Class(name="oaam::systems::RequiredInformationA", is_abstract=True)
oaam_systems_ProvidedInformationA = Class(name="oaam::systems::ProvidedInformationA", is_abstract=True)
oaam_systems_InformationFlow = Class(name="oaam::systems::InformationFlow")
oaam_systems_InformationMaterial = Class(name="oaam::systems::InformationMaterial")
oaam_systems_InformationSignal = Class(name="oaam::systems::InformationSignal")
systems_ProvidedInformationA = Class(name="systems::ProvidedInformationA")
systems_RequiredInformationA = Class(name="systems::RequiredInformationA")
oaam_systems_HydraulicPower = Class(name="oaam::systems::HydraulicPower")
oaam_systems_InformationPower = Class(name="oaam::systems::InformationPower")
oaam_systems_ElectricPower = Class(name="oaam::systems::ElectricPower")
InformationPower = Class(name="InformationPower")
oaam_systems_RotaryPower = Class(name="oaam::systems::RotaryPower")
oaam_systems_LinearPower = Class(name="oaam::systems::LinearPower")
oaam_systems_InputSegregation = Class(name="oaam::systems::InputSegregation")
ExternalTaskLink = Class(name="ExternalTaskLink")
TaskGroup = Class(name="TaskGroup")
oaam_functions_Functions = Class(name="oaam::functions::Functions")
FunctionsContainerA = Class(name="FunctionsContainerA")
oaam_functions_FunctionsContainerA = Class(name="oaam::functions::FunctionsContainerA", is_abstract=True)
Task = Class(name="Task")
FailureCondition = Class(name="FailureCondition")
Subfunctions = Class(name="Subfunctions")
TaskSymmetry = Class(name="TaskSymmetry")
TaskRedundancy = Class(name="TaskRedundancy")
Signal = Class(name="Signal")
SignalGroup = Class(name="SignalGroup")
Output = Class(name="Output")
oaam_functions_Task = Class(name="oaam::functions::Task")
Input = Class(name="Input")
Device = Class(name="Device")
TaskParameter = Class(name="TaskParameter")
oaam_functions_ExternalTaskLink = Class(name="oaam::functions::ExternalTaskLink")
oaam_functions_TaskGroup = Class(name="oaam::functions::TaskGroup")
oaam_functions_TaskSymmetry = Class(name="oaam::functions::TaskSymmetry")
oaam_functions_TaskRedundancy = Class(name="oaam::functions::TaskRedundancy")
oaam_functions_FailureCondition = Class(name="oaam::functions::FailureCondition")
OutputIntegrityState = Class(name="OutputIntegrityState")
oaam_functions_OutputIntegrityState = Class(name="oaam::functions::OutputIntegrityState")
oaam_functions_Signal = Class(name="oaam::functions::Signal")
oaam_functions_Input = Class(name="oaam::functions::Input")
Connection = Class(name="Connection")
oaam_functions_SignalGroup = Class(name="oaam::functions::SignalGroup")
Io = Class(name="Io")
ExternalOutputLink = Class(name="ExternalOutputLink")
oaam_functions_Output = Class(name="oaam::functions::Output")
oaam_functions_Subfunctions = Class(name="oaam::functions::Subfunctions")
oaam_functions_TaskParameter = Class(name="oaam::functions::TaskParameter")
oaam_functions_ExternalOutputLink = Class(name="oaam::functions::ExternalOutputLink")
Subhardware = Class(name="Subhardware")
oaam_hardware_HardwareContainerA = Class(name="oaam::hardware::HardwareContainerA", is_abstract=True)
DeviceSymmetry = Class(name="DeviceSymmetry")
Location = Class(name="Location")
Bus = Class(name="Bus")
oaam_hardware_Device = Class(name="oaam::hardware::Device")
library_ResourceProviderInstanceA = Class(name="library::ResourceProviderInstanceA")
oaam_hardware_Connection = Class(name="oaam::hardware::Connection")
oaam_hardware_Hardware = Class(name="oaam::hardware::Hardware")
hardware_HardwareContainerA = Class(name="hardware::HardwareContainerA")
oaam_hardware_Io = Class(name="oaam::hardware::Io")
oaam_hardware_DeviceSymmetry = Class(name="oaam::hardware::DeviceSymmetry")
oaam_anatomy_AnatomyContainerA = Class(name="oaam::anatomy::AnatomyContainerA", is_abstract=True)
oaam_hardware_Subhardware = Class(name="oaam::hardware::Subhardware")
oaam_hardware_Bus = Class(name="oaam::hardware::Bus")
AreaSymmetry = Class(name="AreaSymmetry")
oaam_anatomy_Location = Class(name="oaam::anatomy::Location")
LocationSymmetry = Class(name="LocationSymmetry")
Duct = Class(name="Duct")
Area = Class(name="Area")
Subanatomy = Class(name="Subanatomy")
DuctOpening = Class(name="DuctOpening")
Position3D = Class(name="Position3D")
oaam_anatomy_Area = Class(name="oaam::anatomy::Area")
oaam_anatomy_Duct = Class(name="oaam::anatomy::Duct")
oaam_anatomy_DuctOpening = Class(name="oaam::anatomy::DuctOpening")
oaam_anatomy_Position3D = Class(name="oaam::anatomy::Position3D")
oaam_anatomy_AreaSymmetry = Class(name="oaam::anatomy::AreaSymmetry")
oaam_anatomy_LocationSymmetry = Class(name="oaam::anatomy::LocationSymmetry")
oaam_capabilities_CapabilitiesContainerA = Class(name="oaam::capabilities::CapabilitiesContainerA", is_abstract=True)
TaskOnDeviceCapability = Class(name="TaskOnDeviceCapability")
oaam_anatomy_Subanatomy = Class(name="oaam::anatomy::Subanatomy")
anatomy_AnatomyContainerA = Class(name="anatomy::AnatomyContainerA")
oaam_anatomy_Anatomy = Class(name="oaam::anatomy::Anatomy")
AnatomyContainerA = Class(name="AnatomyContainerA")
oaam_capabilities_CapabilityA = Class(name="oaam::capabilities::CapabilityA", is_abstract=True)
ResourceConsumption = Class(name="ResourceConsumption")
ConnectionInDuctOrLocationCapability = Class(name="ConnectionInDuctOrLocationCapability")
Subcapabilities = Class(name="Subcapabilities")
SignalOnConnectionOrDeviceCapability = Class(name="SignalOnConnectionOrDeviceCapability")
DeviceInLocationCapability = Class(name="DeviceInLocationCapability")
SubdeviceInDeviceCapability = Class(name="SubdeviceInDeviceCapability")
MessageOnConnectionOrDeviceCapability = Class(name="MessageOnConnectionOrDeviceCapability")
oaam_capabilities_TaskOnDeviceCapability = Class(name="oaam::capabilities::TaskOnDeviceCapability")
capabilities_CapabilityA = Class(name="capabilities::CapabilityA")
SubconnectionInDeviceCapability = Class(name="SubconnectionInDeviceCapability")
MessageOnBusCapability = Class(name="MessageOnBusCapability")
SubmessageInMessageCapability = Class(name="SubmessageInMessageCapability")
SignalInMessageCapability = Class(name="SignalInMessageCapability")
oaam_capabilities_DeviceInLocationCapability = Class(name="oaam::capabilities::DeviceInLocationCapability")
oaam_capabilities_SignalOnConnectionOrDeviceCapability = Class(name="oaam::capabilities::SignalOnConnectionOrDeviceCapability")
oaam_capabilities_ConnectionInDuctOrLocationCapability = Class(name="oaam::capabilities::ConnectionInDuctOrLocationCapability")
oaam_capabilities_SubdeviceInDeviceCapability = Class(name="oaam::capabilities::SubdeviceInDeviceCapability")
oaam_capabilities_ResourceConsumption = Class(name="oaam::capabilities::ResourceConsumption")
oaam_capabilities_SubconnectionInDeviceCapability = Class(name="oaam::capabilities::SubconnectionInDeviceCapability")
oaam_capabilities_MessageOnConnectionOrDeviceCapability = Class(name="oaam::capabilities::MessageOnConnectionOrDeviceCapability")
oaam_capabilities_MessageOnBusCapability = Class(name="oaam::capabilities::MessageOnBusCapability")
oaam_capabilities_SubmessageInMessageCapability = Class(name="oaam::capabilities::SubmessageInMessageCapability")
oaam_capabilities_Capabilities = Class(name="oaam::capabilities::Capabilities")
CapabilitiesContainerA = Class(name="CapabilitiesContainerA")
oaam_capabilities_Subcapabilities = Class(name="oaam::capabilities::Subcapabilities")
capabilities_CapabilitiesContainerA = Class(name="capabilities::CapabilitiesContainerA")
oaam_capabilities_SignalInMessageCapability = Class(name="oaam::capabilities::SignalInMessageCapability")
AreaRestriction = Class(name="AreaRestriction")
PowerSourceRestriction = Class(name="PowerSourceRestriction")
TaskAtomicRestriction = Class(name="TaskAtomicRestriction")
oaam_restrictions_RestrictionsContainerA = Class(name="oaam::restrictions::RestrictionsContainerA", is_abstract=True)
DeviceTypeRestriction = Class(name="DeviceTypeRestriction")
DeviceRestriction = Class(name="DeviceRestriction")
LocationRestriction = Class(name="LocationRestriction")
SegregationRestriction = Class(name="SegregationRestriction")
Subrestrictions = Class(name="Subrestrictions")
TaskSymmetryRestriction = Class(name="TaskSymmetryRestriction")
SynchronicityRestriction = Class(name="SynchronicityRestriction")
ConnectionRestriction = Class(name="ConnectionRestriction")
ConnectionTypeRestriction = Class(name="ConnectionTypeRestriction")
oaam_restrictions_ConnectionRestrinctionA = Class(name="oaam::restrictions::ConnectionRestrinctionA", is_abstract=True)
TimeDelayRestriction = Class(name="TimeDelayRestriction")
oaam_restrictions_Restrictions = Class(name="oaam::restrictions::Restrictions")
RestrictionsContainerA = Class(name="RestrictionsContainerA")
oaam_restrictions_DeviceRestrictionA = Class(name="oaam::restrictions::DeviceRestrictionA", is_abstract=True)
oaam_restrictions_TaskGroupRestrictionA = Class(name="oaam::restrictions::TaskGroupRestrictionA", is_abstract=True)
oaam_restrictions_TaskRestrictionA = Class(name="oaam::restrictions::TaskRestrictionA", is_abstract=True)
oaam_restrictions_SignalRestrictionA = Class(name="oaam::restrictions::SignalRestrictionA", is_abstract=True)
oaam_restrictions_SubfunctionRestrictionA = Class(name="oaam::restrictions::SubfunctionRestrictionA", is_abstract=True)
oaam_restrictions_SignalGroupRestrictionA = Class(name="oaam::restrictions::SignalGroupRestrictionA", is_abstract=True)
oaam_restrictions_LocationRestriction = Class(name="oaam::restrictions::LocationRestriction")
restrictions_TaskRestrictionA = Class(name="restrictions::TaskRestrictionA")
restrictions_TaskGroupRestrictionA = Class(name="restrictions::TaskGroupRestrictionA")
restrictions_SignalRestrictionA = Class(name="restrictions::SignalRestrictionA")
restrictions_SignalGroupRestrictionA = Class(name="restrictions::SignalGroupRestrictionA")
restrictions_SubfunctionRestrictionA = Class(name="restrictions::SubfunctionRestrictionA")
restrictions_DeviceRestrictionA = Class(name="restrictions::DeviceRestrictionA")
restrictions_ConnectionRestrinctionA = Class(name="restrictions::ConnectionRestrinctionA")
oaam_restrictions_AreaRestriction = Class(name="oaam::restrictions::AreaRestriction")
oaam_restrictions_DeviceTypeRestriction = Class(name="oaam::restrictions::DeviceTypeRestriction")
oaam_restrictions_PowerSourceRestriction = Class(name="oaam::restrictions::PowerSourceRestriction")
oaam_restrictions_DeviceRestriction = Class(name="oaam::restrictions::DeviceRestriction")
oaam_restrictions_SegregationRestriction = Class(name="oaam::restrictions::SegregationRestriction")
oaam_restrictions_ConnectionTypeRestriction = Class(name="oaam::restrictions::ConnectionTypeRestriction")
oaam_restrictions_ConnectionRestriction = Class(name="oaam::restrictions::ConnectionRestriction")
oaam_restrictions_TaskSymmetryRestriction = Class(name="oaam::restrictions::TaskSymmetryRestriction")
oaam_restrictions_TimeDelayRestriction = Class(name="oaam::restrictions::TimeDelayRestriction")
oaam_restrictions_SynchronicityRestriction = Class(name="oaam::restrictions::SynchronicityRestriction")
oaam_restrictions_TaskAtomicRestriction = Class(name="oaam::restrictions::TaskAtomicRestriction")
oaam_allocations_AllocationsContainerA = Class(name="oaam::allocations::AllocationsContainerA", is_abstract=True)
oaam_restrictions_Subrestrictions = Class(name="oaam::restrictions::Subrestrictions")
restrictions_RestrictionsContainerA = Class(name="restrictions::RestrictionsContainerA")
SignalAssignment = Class(name="SignalAssignment")
Suballocations = Class(name="Suballocations")
SubconnectionAssignment = Class(name="SubconnectionAssignment")
Message = Class(name="Message")
DeviceAssignment = Class(name="DeviceAssignment")
SubdeviceAssignment = Class(name="SubdeviceAssignment")
ConnectionAssignment = Class(name="ConnectionAssignment")
TaskAssignment = Class(name="TaskAssignment")
Schedule = Class(name="Schedule")
oaam_allocations_SignalAssignment = Class(name="oaam::allocations::SignalAssignment")
SignalAssignmentSegment = Class(name="SignalAssignmentSegment")
oaam_allocations_TaskAssignment = Class(name="oaam::allocations::TaskAssignment")
oaam_allocations_SignalAssignmentSegment = Class(name="oaam::allocations::SignalAssignmentSegment")
oaam_allocations_ConnectionAssignment = Class(name="oaam::allocations::ConnectionAssignment")
ConnectionAssignmentSegment = Class(name="ConnectionAssignmentSegment")
oaam_allocations_DeviceAssignment = Class(name="oaam::allocations::DeviceAssignment")
oaam_allocations_SubdeviceAssignment = Class(name="oaam::allocations::SubdeviceAssignment")
oaam_allocations_ConnectionAssignmentSegment = Class(name="oaam::allocations::ConnectionAssignmentSegment")
oaam_allocations_Schedule = Class(name="oaam::allocations::Schedule")
oaam_allocations_SubconnectionAssignment = Class(name="oaam::allocations::SubconnectionAssignment")
oaam_allocations_MessageA = Class(name="oaam::allocations::MessageA", is_abstract=True)
ScheduledTime = Class(name="ScheduledTime")
oaam_allocations_ScheduledTime = Class(name="oaam::allocations::ScheduledTime")
MessageSegment = Class(name="MessageSegment")
Submessage = Class(name="Submessage")
SignalToMessageAssignment = Class(name="SignalToMessageAssignment")
oaam_allocations_MessageSegment = Class(name="oaam::allocations::MessageSegment")
oaam_allocations_Message = Class(name="oaam::allocations::Message")
MessageA = Class(name="MessageA")
oaam_allocations_Submessage = Class(name="oaam::allocations::Submessage")
oaam_allocations_SignalToMessageAssignment = Class(name="oaam::allocations::SignalToMessageAssignment")
oaam_allocations_Allocations = Class(name="oaam::allocations::Allocations")
AllocationsContainerA = Class(name="AllocationsContainerA")
oaam_allocations_Suballocations = Class(name="oaam::allocations::Suballocations")
allocations_AllocationsContainerA = Class(name="allocations::AllocationsContainerA")

# oaam_Architecture class attributes and methods

# OaamBaseElementA class attributes and methods

# Anatomy class attributes and methods

# Capabilities class attributes and methods

# Library class attributes and methods

# Scenario class attributes and methods

# Systems class attributes and methods

# Functions class attributes and methods

# Hardware class attributes and methods

# oaam_common_OaamBaseElementA class attributes and methods
oaam_common_OaamBaseElementA_id: Property = Property(name="id", type=StringType)
oaam_common_OaamBaseElementA_name: Property = Property(name="name", type=StringType)
oaam_common_OaamBaseElementA_style: Property = Property(name="style", type=StringType)
oaam_common_OaamBaseElementA_documentation: Property = Property(name="documentation", type=StringType)
oaam_common_OaamBaseElementA_modified: Property = Property(name="modified", type=DateType)
oaam_common_OaamBaseElementA_modifier: Property = Property(name="modifier", type=StringType)
oaam_common_OaamBaseElementA_traceLink: Property = Property(name="traceLink", type=StringType)
oaam_common_OaamBaseElementA.attributes={oaam_common_OaamBaseElementA_style, oaam_common_OaamBaseElementA_modifier, oaam_common_OaamBaseElementA_id, oaam_common_OaamBaseElementA_modified, oaam_common_OaamBaseElementA_traceLink, oaam_common_OaamBaseElementA_documentation, oaam_common_OaamBaseElementA_name}

# Restrictions class attributes and methods

# Allocations class attributes and methods

# oaam_common_AttributeA class attributes and methods

# oaam_common_AttributeString class attributes and methods
oaam_common_AttributeString_value: Property = Property(name="value", type=StringType)
oaam_common_AttributeString.attributes={oaam_common_AttributeString_value}

# AttributeA class attributes and methods

# oaam_common_BoolA class attributes and methods

# oaam_common_BoolOperation class attributes and methods
oaam_common_BoolOperation_type: Property = Property(name="type", type=StringType)
oaam_common_BoolOperation.attributes={oaam_common_BoolOperation_type}

# common_BoolA class attributes and methods

# common_OaamBaseElementA class attributes and methods

# BoolA class attributes and methods

# oaam_common_AttributeNumeric class attributes and methods
oaam_common_AttributeNumeric_value: Property = Property(name="value", type=FloatType)
oaam_common_AttributeNumeric.attributes={oaam_common_AttributeNumeric_value}

# oaam_common_AttributeContainment class attributes and methods

# oaam_common_AttributeReference class attributes and methods

# oaam_common_Array class attributes and methods
oaam_common_Array_nElements: Property = Property(name="nElements", type=IntegerType)
oaam_common_Array_alignment: Property = Property(name="alignment", type=IntegerType)
oaam_common_Array.attributes={oaam_common_Array_alignment, oaam_common_Array_nElements}

# oaam_common_BoolNot class attributes and methods

# oaam_common_DataTypeA class attributes and methods

# oaam_common_Integer class attributes and methods
oaam_common_Integer_nBits: Property = Property(name="nBits", type=IntegerType)
oaam_common_Integer_endianess: Property = Property(name="endianess", type=StringType)
oaam_common_Integer_signed: Property = Property(name="signed", type=BooleanType)
oaam_common_Integer.attributes={oaam_common_Integer_nBits, oaam_common_Integer_endianess, oaam_common_Integer_signed}

# DataTypeA class attributes and methods

# oaam_common_FloatingPoint class attributes and methods
oaam_common_FloatingPoint_nBits: Property = Property(name="nBits", type=IntegerType)
oaam_common_FloatingPoint_endianess: Property = Property(name="endianess", type=StringType)
oaam_common_FloatingPoint.attributes={oaam_common_FloatingPoint_endianess, oaam_common_FloatingPoint_nBits}

# oaam_common_Struct class attributes and methods
oaam_common_Struct_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
oaam_common_Struct_alignment: Property = Property(name="alignment", type=IntegerType)
oaam_common_Struct.attributes={oaam_common_Struct_alignment, oaam_common_Struct_isAbstract}

# Struct class attributes and methods

# oaam_common_Boolean class attributes and methods
oaam_common_Boolean_nBits: Property = Property(name="nBits", type=IntegerType)
oaam_common_Boolean.attributes={oaam_common_Boolean_nBits}

# oaam_common_Byte class attributes and methods
oaam_common_Byte_nBits: Property = Property(name="nBits", type=IntegerType)
oaam_common_Byte.attributes={oaam_common_Byte_nBits}

# oaam_common_Character class attributes and methods
oaam_common_Character_encoding: Property = Property(name="encoding", type=StringType)
oaam_common_Character_nBits: Property = Property(name="nBits", type=IntegerType)
oaam_common_Character.attributes={oaam_common_Character_nBits, oaam_common_Character_encoding}

# ResourceGroup class attributes and methods

# oaam_library_ResourceProviderA class attributes and methods

# ResourceBundle class attributes and methods

# ResourceType class attributes and methods

# ResourceLink class attributes and methods

# oaam_library_ResourceProviderInstanceA class attributes and methods

# oaam_library_ResourceConsumerA class attributes and methods

# Resource class attributes and methods

# oaam_library_LibraryContainerA class attributes and methods

# ResourceTypeModifier class attributes and methods

# ResourceTypeDissimilarity class attributes and methods

# TaskType class attributes and methods

# TaskTypeDissimilarity class attributes and methods

# SignalType class attributes and methods

# ResourceTypeModifierLevel class attributes and methods

# IoType class attributes and methods

# DeviceTypeDissimilarity class attributes and methods

# BusType class attributes and methods

# ConnectionType class attributes and methods

# WireType class attributes and methods

# LocationType class attributes and methods

# DuctType class attributes and methods

# AttributeDefinition class attributes and methods

# PowerSource class attributes and methods

# DeviceType class attributes and methods

# Sublibrary class attributes and methods

# DeviceTypeSymmetry class attributes and methods

# ResourceAlternatives class attributes and methods

# oaam_library_Resource class attributes and methods
oaam_library_Resource_count: Property = Property(name="count", type=FloatType)
oaam_library_Resource.attributes={oaam_library_Resource_count}

# MessageType class attributes and methods

# oaam_library_ResourceType class attributes and methods
oaam_library_ResourceType_unit: Property = Property(name="unit", type=StringType)
oaam_library_ResourceType_isConsumed: Property = Property(name="isConsumed", type=BooleanType)
oaam_library_ResourceType_isDistinguishable: Property = Property(name="isDistinguishable", type=BooleanType)
oaam_library_ResourceType_isPropagated: Property = Property(name="isPropagated", type=BooleanType)
oaam_library_ResourceType_direction: Property = Property(name="direction", type=StringType)
oaam_library_ResourceType_isIo: Property = Property(name="isIo", type=BooleanType)
oaam_library_ResourceType_isConfigurable: Property = Property(name="isConfigurable", type=BooleanType)
oaam_library_ResourceType.attributes={oaam_library_ResourceType_isPropagated, oaam_library_ResourceType_isConsumed, oaam_library_ResourceType_isConfigurable, oaam_library_ResourceType_isDistinguishable, oaam_library_ResourceType_unit, oaam_library_ResourceType_isIo, oaam_library_ResourceType_direction}

# library_ResourceConsumerA class attributes and methods

# ResourceTypeModifierReference class attributes and methods

# TaskStateDeclaration class attributes and methods

# oaam_library_ResourceAlternatives class attributes and methods

# oaam_library_ResourceBundle class attributes and methods
oaam_library_ResourceBundle_mtbf: Property = Property(name="mtbf", type=FloatType)
oaam_library_ResourceBundle_cost: Property = Property(name="cost", type=FloatType)
oaam_library_ResourceBundle_mass: Property = Property(name="mass", type=FloatType)
oaam_library_ResourceBundle.attributes={oaam_library_ResourceBundle_mtbf, oaam_library_ResourceBundle_cost, oaam_library_ResourceBundle_mass}

# oaam_library_TaskType class attributes and methods
oaam_library_TaskType_isDeterministic: Property = Property(name="isDeterministic", type=BooleanType)
oaam_library_TaskType_preferredExecutionRate: Property = Property(name="preferredExecutionRate", type=FloatType)
oaam_library_TaskType.attributes={oaam_library_TaskType_preferredExecutionRate, oaam_library_TaskType_isDeterministic}

# OutputDeclaration class attributes and methods

# InputDeclaration class attributes and methods

# TaskParameterDeclaration class attributes and methods

# oaam_library_SignalType class attributes and methods

# oaam_library_DeviceType class attributes and methods
oaam_library_DeviceType_mtbf: Property = Property(name="mtbf", type=FloatType)
oaam_library_DeviceType_weight: Property = Property(name="weight", type=FloatType)
oaam_library_DeviceType_cost: Property = Property(name="cost", type=FloatType)
oaam_library_DeviceType_isSubdevice: Property = Property(name="isSubdevice", type=BooleanType)
oaam_library_DeviceType_canHaveSubdevices: Property = Property(name="canHaveSubdevices", type=BooleanType)
oaam_library_DeviceType_isSelfManaging: Property = Property(name="isSelfManaging", type=BooleanType)
oaam_library_DeviceType.attributes={oaam_library_DeviceType_cost, oaam_library_DeviceType_isSubdevice, oaam_library_DeviceType_isSelfManaging, oaam_library_DeviceType_mtbf, oaam_library_DeviceType_canHaveSubdevices, oaam_library_DeviceType_weight}

# library_ResourceProviderA class attributes and methods

# IoDeclaration class attributes and methods

# IoGroup class attributes and methods

# oaam_library_ConnectionType class attributes and methods
oaam_library_ConnectionType_nEndPoints: Property = Property(name="nEndPoints", type=IntegerType)
oaam_library_ConnectionType_isInformation: Property = Property(name="isInformation", type=BooleanType)
oaam_library_ConnectionType_isPower: Property = Property(name="isPower", type=BooleanType)
oaam_library_ConnectionType_isWireless: Property = Property(name="isWireless", type=BooleanType)
oaam_library_ConnectionType_allowsCircles: Property = Property(name="allowsCircles", type=BooleanType)
oaam_library_ConnectionType_nStartingPoints: Property = Property(name="nStartingPoints", type=IntegerType)
oaam_library_ConnectionType_nJoints: Property = Property(name="nJoints", type=IntegerType)
oaam_library_ConnectionType_maxJointBranches: Property = Property(name="maxJointBranches", type=IntegerType)
oaam_library_ConnectionType_maxInterfaceToJointDistance: Property = Property(name="maxInterfaceToJointDistance", type=FloatType)
oaam_library_ConnectionType_isSwitched: Property = Property(name="isSwitched", type=BooleanType)
oaam_library_ConnectionType_directConnectionsAllowed: Property = Property(name="directConnectionsAllowed", type=BooleanType)
oaam_library_ConnectionType_maxLength: Property = Property(name="maxLength", type=FloatType)
oaam_library_ConnectionType_isUnidirectional: Property = Property(name="isUnidirectional", type=BooleanType)
oaam_library_ConnectionType_requiresMaster: Property = Property(name="requiresMaster", type=BooleanType)
oaam_library_ConnectionType.attributes={oaam_library_ConnectionType_isPower, oaam_library_ConnectionType_isInformation, oaam_library_ConnectionType_isSwitched, oaam_library_ConnectionType_isWireless, oaam_library_ConnectionType_maxLength, oaam_library_ConnectionType_nJoints, oaam_library_ConnectionType_directConnectionsAllowed, oaam_library_ConnectionType_requiresMaster, oaam_library_ConnectionType_maxInterfaceToJointDistance, oaam_library_ConnectionType_nEndPoints, oaam_library_ConnectionType_isUnidirectional, oaam_library_ConnectionType_allowsCircles, oaam_library_ConnectionType_nStartingPoints, oaam_library_ConnectionType_maxJointBranches}

# oaam_library_LocationType class attributes and methods
oaam_library_LocationType_isJoint: Property = Property(name="isJoint", type=BooleanType)
oaam_library_LocationType.attributes={oaam_library_LocationType_isJoint}

# oaam_library_IoType class attributes and methods
oaam_library_IoType_direction: Property = Property(name="direction", type=StringType)
oaam_library_IoType.attributes={oaam_library_IoType_direction}

# DuctOpeningDeclaration class attributes and methods

# oaam_library_DuctType class attributes and methods

# oaam_library_WireType class attributes and methods
oaam_library_WireType_specificWeight: Property = Property(name="specificWeight", type=FloatType)
oaam_library_WireType_specificPrice: Property = Property(name="specificPrice", type=FloatType)
oaam_library_WireType_nConductors: Property = Property(name="nConductors", type=IntegerType)
oaam_library_WireType_minBendingRadius: Property = Property(name="minBendingRadius", type=FloatType)
oaam_library_WireType_nShields: Property = Property(name="nShields", type=IntegerType)
oaam_library_WireType_mtbf: Property = Property(name="mtbf", type=FloatType)
oaam_library_WireType.attributes={oaam_library_WireType_minBendingRadius, oaam_library_WireType_nShields, oaam_library_WireType_mtbf, oaam_library_WireType_specificPrice, oaam_library_WireType_specificWeight, oaam_library_WireType_nConductors}

# TaskOutputTrigger class attributes and methods

# oaam_library_InputDeclaration class attributes and methods
oaam_library_InputDeclaration_unit: Property = Property(name="unit", type=StringType)
oaam_library_InputDeclaration_precondition: Property = Property(name="precondition", type=StringType)
oaam_library_InputDeclaration_range: Property = Property(name="range", type=StringType)
oaam_library_InputDeclaration_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
oaam_library_InputDeclaration_upperBound: Property = Property(name="upperBound", type=IntegerType)
oaam_library_InputDeclaration.attributes={oaam_library_InputDeclaration_precondition, oaam_library_InputDeclaration_lowerBound, oaam_library_InputDeclaration_upperBound, oaam_library_InputDeclaration_unit, oaam_library_InputDeclaration_range}

# oaam_library_OutputDeclaration class attributes and methods
oaam_library_OutputDeclaration_range: Property = Property(name="range", type=StringType)
oaam_library_OutputDeclaration_unit: Property = Property(name="unit", type=StringType)
oaam_library_OutputDeclaration_postcondition: Property = Property(name="postcondition", type=StringType)
oaam_library_OutputDeclaration_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
oaam_library_OutputDeclaration_upperBound: Property = Property(name="upperBound", type=IntegerType)
oaam_library_OutputDeclaration.attributes={oaam_library_OutputDeclaration_lowerBound, oaam_library_OutputDeclaration_range, oaam_library_OutputDeclaration_postcondition, oaam_library_OutputDeclaration_upperBound, oaam_library_OutputDeclaration_unit}

# oaam_library_ResourceGroup class attributes and methods

# oaam_library_DeviceTypeSymmetry class attributes and methods

# FaultPropagation class attributes and methods

# oaam_library_IoDeclaration class attributes and methods

# oaam_library_DuctOpeningDeclaration class attributes and methods

# BoolOperation class attributes and methods

# oaam_library_IoGroup class attributes and methods

# oaam_library_AttributeDefinition class attributes and methods
oaam_library_AttributeDefinition_dataType: Property = Property(name="dataType", type=StringType)
oaam_library_AttributeDefinition_target: Property = Property(name="target", type=StringType)
oaam_library_AttributeDefinition.attributes={oaam_library_AttributeDefinition_dataType, oaam_library_AttributeDefinition_target}

# oaam_library_FaultPropagation class attributes and methods
oaam_library_FaultPropagation_outputState: Property = Property(name="outputState", type=StringType)
oaam_library_FaultPropagation.attributes={oaam_library_FaultPropagation_outputState}

# oaam_library_ResourceTypeModifier class attributes and methods

# BoolNot class attributes and methods

# TaskInputState class attributes and methods

# oaam_library_TaskInputState class attributes and methods
oaam_library_TaskInputState_state: Property = Property(name="state", type=StringType)
oaam_library_TaskInputState.attributes={oaam_library_TaskInputState_state}

# oaam_library_PowerSource class attributes and methods

# oaam_library_ResourceLink class attributes and methods

# oaam_library_TaskTypeDissimilarity class attributes and methods
oaam_library_TaskTypeDissimilarity_percentageOfCommonCode: Property = Property(name="percentageOfCommonCode", type=FloatType)
oaam_library_TaskTypeDissimilarity.attributes={oaam_library_TaskTypeDissimilarity_percentageOfCommonCode}

# oaam_library_ResourceTypeModifierLevel class attributes and methods

# oaam_library_ResourceTypeModifierReference class attributes and methods

# oaam_library_TaskOutputTrigger class attributes and methods
oaam_library_TaskOutputTrigger_fixedRate: Property = Property(name="fixedRate", type=FloatType)
oaam_library_TaskOutputTrigger_isFixedRate: Property = Property(name="isFixedRate", type=BooleanType)
oaam_library_TaskOutputTrigger.attributes={oaam_library_TaskOutputTrigger_isFixedRate, oaam_library_TaskOutputTrigger_fixedRate}

# oaam_library_DeviceTypeDissimilarity class attributes and methods
oaam_library_DeviceTypeDissimilarity_percentageOfCommonHardware: Property = Property(name="percentageOfCommonHardware", type=FloatType)
oaam_library_DeviceTypeDissimilarity.attributes={oaam_library_DeviceTypeDissimilarity_percentageOfCommonHardware}

# oaam_library_ResourceTypeDissimilarity class attributes and methods

# oaam_library_TaskInputTrigger class attributes and methods

# TaskInputTrigger class attributes and methods

# oaam_library_BusType class attributes and methods
oaam_library_BusType_requiresMaster: Property = Property(name="requiresMaster", type=BooleanType)
oaam_library_BusType_mtbf: Property = Property(name="mtbf", type=FloatType)
oaam_library_BusType_isSelfManaging: Property = Property(name="isSelfManaging", type=BooleanType)
oaam_library_BusType.attributes={oaam_library_BusType_requiresMaster, oaam_library_BusType_mtbf, oaam_library_BusType_isSelfManaging}

# oaam_library_TaskStateDeclaration class attributes and methods

# oaam_library_TaskParameterDeclaration class attributes and methods

# oaam_library_MessageType class attributes and methods
oaam_library_MessageType_maxLength: Property = Property(name="maxLength", type=IntegerType)
oaam_library_MessageType_minLength: Property = Property(name="minLength", type=IntegerType)
oaam_library_MessageType_alignment: Property = Property(name="alignment", type=IntegerType)
oaam_library_MessageType.attributes={oaam_library_MessageType_maxLength, oaam_library_MessageType_minLength, oaam_library_MessageType_alignment}

# oaam_library_Library class attributes and methods

# LibraryContainerA class attributes and methods

# oaam_library_Sublibrary class attributes and methods

# oaam_scenario_VariantDependentElementA class attributes and methods

# Variant class attributes and methods

# oaam_scenario_ScenarioParameterA class attributes and methods

# scenario_ModeDependentElementA class attributes and methods

# scenario_VariantDependentElementA class attributes and methods

# oaam_scenario_ModeDependentElementA class attributes and methods

# OperationModeReference class attributes and methods

# oaam_scenario_OperationMode class attributes and methods

# oaam_scenario_ScenarioParameterNumeric class attributes and methods
oaam_scenario_ScenarioParameterNumeric_value: Property = Property(name="value", type=FloatType)
oaam_scenario_ScenarioParameterNumeric.attributes={oaam_scenario_ScenarioParameterNumeric_value}

# scenario_ScenarioParameterA class attributes and methods

# oaam_scenario_ScenarioContainerA class attributes and methods

# ScenarioParameterA class attributes and methods

# OperationMode class attributes and methods

# Subscenario class attributes and methods

# oaam_scenario_Scenario class attributes and methods

# ScenarioContainerA class attributes and methods

# oaam_scenario_Subscenario class attributes and methods

# oaam_scenario_ScenarioParameterBool class attributes and methods
oaam_scenario_ScenarioParameterBool_value: Property = Property(name="value", type=BooleanType)
oaam_scenario_ScenarioParameterBool.attributes={oaam_scenario_ScenarioParameterBool_value}

# oaam_scenario_Variant class attributes and methods

# oaam_scenario_OperationModeReference class attributes and methods
oaam_scenario_OperationModeReference_activeProbability: Property = Property(name="activeProbability", type=FloatType)
oaam_scenario_OperationModeReference.attributes={oaam_scenario_OperationModeReference_activeProbability}

# oaam_systems_Systems class attributes and methods

# SystemsContainerA class attributes and methods

# oaam_systems_Subsystem class attributes and methods

# systems_SystemsContainerA class attributes and methods

# oaam_systems_SystemsContainerA class attributes and methods

# System class attributes and methods

# InformationFlow class attributes and methods

# InputSegregation class attributes and methods

# Subsystem class attributes and methods

# oaam_systems_System class attributes and methods

# ProvidedInformationA class attributes and methods

# RequiredInformationA class attributes and methods

# oaam_systems_RequiredInformationA class attributes and methods

# oaam_systems_ProvidedInformationA class attributes and methods

# oaam_systems_InformationFlow class attributes and methods

# oaam_systems_InformationMaterial class attributes and methods
oaam_systems_InformationMaterial_density: Property = Property(name="density", type=FloatType)
oaam_systems_InformationMaterial_velocity: Property = Property(name="velocity", type=FloatType)
oaam_systems_InformationMaterial.attributes={oaam_systems_InformationMaterial_velocity, oaam_systems_InformationMaterial_density}

# oaam_systems_InformationSignal class attributes and methods
oaam_systems_InformationSignal_rate: Property = Property(name="rate", type=FloatType)
oaam_systems_InformationSignal_latency: Property = Property(name="latency", type=FloatType)
oaam_systems_InformationSignal_accuracy: Property = Property(name="accuracy", type=FloatType)
oaam_systems_InformationSignal_resolution: Property = Property(name="resolution", type=FloatType)
oaam_systems_InformationSignal_unit: Property = Property(name="unit", type=StringType)
oaam_systems_InformationSignal.attributes={oaam_systems_InformationSignal_rate, oaam_systems_InformationSignal_latency, oaam_systems_InformationSignal_resolution, oaam_systems_InformationSignal_unit, oaam_systems_InformationSignal_accuracy}

# systems_ProvidedInformationA class attributes and methods

# systems_RequiredInformationA class attributes and methods

# oaam_systems_HydraulicPower class attributes and methods
oaam_systems_HydraulicPower_pressure: Property = Property(name="pressure", type=FloatType)
oaam_systems_HydraulicPower_massFlowRate: Property = Property(name="massFlowRate", type=FloatType)
oaam_systems_HydraulicPower.attributes={oaam_systems_HydraulicPower_massFlowRate, oaam_systems_HydraulicPower_pressure}

# oaam_systems_InformationPower class attributes and methods
oaam_systems_InformationPower_power: Property = Property(name="power", type=FloatType)
oaam_systems_InformationPower.attributes={oaam_systems_InformationPower_power}

# oaam_systems_ElectricPower class attributes and methods
oaam_systems_ElectricPower_current: Property = Property(name="current", type=FloatType)
oaam_systems_ElectricPower_frequency: Property = Property(name="frequency", type=FloatType)
oaam_systems_ElectricPower_nPhases: Property = Property(name="nPhases", type=IntegerType)
oaam_systems_ElectricPower_voltage: Property = Property(name="voltage", type=FloatType)
oaam_systems_ElectricPower.attributes={oaam_systems_ElectricPower_current, oaam_systems_ElectricPower_voltage, oaam_systems_ElectricPower_frequency, oaam_systems_ElectricPower_nPhases}

# InformationPower class attributes and methods

# oaam_systems_RotaryPower class attributes and methods
oaam_systems_RotaryPower_momentum: Property = Property(name="momentum", type=FloatType)
oaam_systems_RotaryPower_angularVelocity: Property = Property(name="angularVelocity", type=FloatType)
oaam_systems_RotaryPower.attributes={oaam_systems_RotaryPower_angularVelocity, oaam_systems_RotaryPower_momentum}

# oaam_systems_LinearPower class attributes and methods
oaam_systems_LinearPower_force: Property = Property(name="force", type=FloatType)
oaam_systems_LinearPower_velocity: Property = Property(name="velocity", type=FloatType)
oaam_systems_LinearPower.attributes={oaam_systems_LinearPower_force, oaam_systems_LinearPower_velocity}

# oaam_systems_InputSegregation class attributes and methods
oaam_systems_InputSegregation_dissimilarSource: Property = Property(name="dissimilarSource", type=BooleanType)
oaam_systems_InputSegregation_dissimilarRoute: Property = Property(name="dissimilarRoute", type=BooleanType)
oaam_systems_InputSegregation_dissimilarTechnology: Property = Property(name="dissimilarTechnology", type=BooleanType)
oaam_systems_InputSegregation.attributes={oaam_systems_InputSegregation_dissimilarTechnology, oaam_systems_InputSegregation_dissimilarRoute, oaam_systems_InputSegregation_dissimilarSource}

# ExternalTaskLink class attributes and methods

# TaskGroup class attributes and methods

# oaam_functions_Functions class attributes and methods

# FunctionsContainerA class attributes and methods

# oaam_functions_FunctionsContainerA class attributes and methods

# Task class attributes and methods

# FailureCondition class attributes and methods

# Subfunctions class attributes and methods

# TaskSymmetry class attributes and methods

# TaskRedundancy class attributes and methods

# Signal class attributes and methods

# SignalGroup class attributes and methods

# Output class attributes and methods

# oaam_functions_Task class attributes and methods
oaam_functions_Task_nParallels: Property = Property(name="nParallels", type=IntegerType)
oaam_functions_Task_fixedRate: Property = Property(name="fixedRate", type=FloatType)
oaam_functions_Task.attributes={oaam_functions_Task_nParallels, oaam_functions_Task_fixedRate}

# Input class attributes and methods

# Device class attributes and methods

# TaskParameter class attributes and methods

# oaam_functions_ExternalTaskLink class attributes and methods
oaam_functions_ExternalTaskLink_filter: Property = Property(name="filter", type=StringType)
oaam_functions_ExternalTaskLink.attributes={oaam_functions_ExternalTaskLink_filter}

# oaam_functions_TaskGroup class attributes and methods

# oaam_functions_TaskSymmetry class attributes and methods

# oaam_functions_TaskRedundancy class attributes and methods

# oaam_functions_FailureCondition class attributes and methods
oaam_functions_FailureCondition_maxOccurrenceProbability: Property = Property(name="maxOccurrenceProbability", type=FloatType)
oaam_functions_FailureCondition_noSingleFailure: Property = Property(name="noSingleFailure", type=BooleanType)
oaam_functions_FailureCondition.attributes={oaam_functions_FailureCondition_maxOccurrenceProbability, oaam_functions_FailureCondition_noSingleFailure}

# OutputIntegrityState class attributes and methods

# oaam_functions_OutputIntegrityState class attributes and methods
oaam_functions_OutputIntegrityState_state: Property = Property(name="state", type=StringType)
oaam_functions_OutputIntegrityState.attributes={oaam_functions_OutputIntegrityState_state}

# oaam_functions_Signal class attributes and methods
oaam_functions_Signal_inIndex: Property = Property(name="inIndex", type=IntegerType)
oaam_functions_Signal_outIndex: Property = Property(name="outIndex", type=IntegerType)
oaam_functions_Signal.attributes={oaam_functions_Signal_outIndex, oaam_functions_Signal_inIndex}

# oaam_functions_Input class attributes and methods
oaam_functions_Input_queueLength: Property = Property(name="queueLength", type=IntegerType)
oaam_functions_Input.attributes={oaam_functions_Input_queueLength}

# Connection class attributes and methods

# oaam_functions_SignalGroup class attributes and methods

# Io class attributes and methods

# ExternalOutputLink class attributes and methods

# oaam_functions_Output class attributes and methods
oaam_functions_Output_fixedRate: Property = Property(name="fixedRate", type=FloatType)
oaam_functions_Output.attributes={oaam_functions_Output_fixedRate}

# oaam_functions_Subfunctions class attributes and methods
oaam_functions_Subfunctions_multiplicityMin: Property = Property(name="multiplicityMin", type=IntegerType)
oaam_functions_Subfunctions_multiplicityMax: Property = Property(name="multiplicityMax", type=IntegerType)
oaam_functions_Subfunctions.attributes={oaam_functions_Subfunctions_multiplicityMin, oaam_functions_Subfunctions_multiplicityMax}

# oaam_functions_TaskParameter class attributes and methods
oaam_functions_TaskParameter_value: Property = Property(name="value", type=StringType)
oaam_functions_TaskParameter.attributes={oaam_functions_TaskParameter_value}

# oaam_functions_ExternalOutputLink class attributes and methods
oaam_functions_ExternalOutputLink_filter: Property = Property(name="filter", type=StringType)
oaam_functions_ExternalOutputLink.attributes={oaam_functions_ExternalOutputLink_filter}

# Subhardware class attributes and methods

# oaam_hardware_HardwareContainerA class attributes and methods

# DeviceSymmetry class attributes and methods

# Location class attributes and methods

# Bus class attributes and methods

# oaam_hardware_Device class attributes and methods

# library_ResourceProviderInstanceA class attributes and methods

# oaam_hardware_Connection class attributes and methods

# oaam_hardware_Hardware class attributes and methods

# hardware_HardwareContainerA class attributes and methods

# oaam_hardware_Io class attributes and methods

# oaam_hardware_DeviceSymmetry class attributes and methods

# oaam_anatomy_AnatomyContainerA class attributes and methods

# oaam_hardware_Subhardware class attributes and methods

# oaam_hardware_Bus class attributes and methods

# AreaSymmetry class attributes and methods

# oaam_anatomy_Location class attributes and methods
oaam_anatomy_Location_length: Property = Property(name="length", type=FloatType)
oaam_anatomy_Location.attributes={oaam_anatomy_Location_length}

# LocationSymmetry class attributes and methods

# Duct class attributes and methods

# Area class attributes and methods

# Subanatomy class attributes and methods

# DuctOpening class attributes and methods

# Position3D class attributes and methods

# oaam_anatomy_Area class attributes and methods

# oaam_anatomy_Duct class attributes and methods
oaam_anatomy_Duct_length: Property = Property(name="length", type=FloatType)
oaam_anatomy_Duct.attributes={oaam_anatomy_Duct_length}

# oaam_anatomy_DuctOpening class attributes and methods

# oaam_anatomy_Position3D class attributes and methods
oaam_anatomy_Position3D_x: Property = Property(name="x", type=FloatType)
oaam_anatomy_Position3D_y: Property = Property(name="y", type=FloatType)
oaam_anatomy_Position3D_z: Property = Property(name="z", type=FloatType)
oaam_anatomy_Position3D.attributes={oaam_anatomy_Position3D_x, oaam_anatomy_Position3D_z, oaam_anatomy_Position3D_y}

# oaam_anatomy_AreaSymmetry class attributes and methods

# oaam_anatomy_LocationSymmetry class attributes and methods

# oaam_capabilities_CapabilitiesContainerA class attributes and methods

# TaskOnDeviceCapability class attributes and methods

# oaam_anatomy_Subanatomy class attributes and methods

# anatomy_AnatomyContainerA class attributes and methods

# oaam_anatomy_Anatomy class attributes and methods

# AnatomyContainerA class attributes and methods

# oaam_capabilities_CapabilityA class attributes and methods

# ResourceConsumption class attributes and methods

# ConnectionInDuctOrLocationCapability class attributes and methods

# Subcapabilities class attributes and methods

# SignalOnConnectionOrDeviceCapability class attributes and methods

# DeviceInLocationCapability class attributes and methods

# SubdeviceInDeviceCapability class attributes and methods

# MessageOnConnectionOrDeviceCapability class attributes and methods

# oaam_capabilities_TaskOnDeviceCapability class attributes and methods
oaam_capabilities_TaskOnDeviceCapability_worstCaseExecutionTime: Property = Property(name="worstCaseExecutionTime", type=FloatType)
oaam_capabilities_TaskOnDeviceCapability_failureProbability: Property = Property(name="failureProbability", type=FloatType)
oaam_capabilities_TaskOnDeviceCapability.attributes={oaam_capabilities_TaskOnDeviceCapability_worstCaseExecutionTime, oaam_capabilities_TaskOnDeviceCapability_failureProbability}

# capabilities_CapabilityA class attributes and methods

# SubconnectionInDeviceCapability class attributes and methods

# MessageOnBusCapability class attributes and methods

# SubmessageInMessageCapability class attributes and methods

# SignalInMessageCapability class attributes and methods

# oaam_capabilities_DeviceInLocationCapability class attributes and methods

# oaam_capabilities_SignalOnConnectionOrDeviceCapability class attributes and methods
oaam_capabilities_SignalOnConnectionOrDeviceCapability_worstCaseTransmissionTime: Property = Property(name="worstCaseTransmissionTime", type=FloatType)
oaam_capabilities_SignalOnConnectionOrDeviceCapability.attributes={oaam_capabilities_SignalOnConnectionOrDeviceCapability_worstCaseTransmissionTime}

# oaam_capabilities_ConnectionInDuctOrLocationCapability class attributes and methods

# oaam_capabilities_SubdeviceInDeviceCapability class attributes and methods

# oaam_capabilities_ResourceConsumption class attributes and methods
oaam_capabilities_ResourceConsumption_count: Property = Property(name="count", type=FloatType)
oaam_capabilities_ResourceConsumption.attributes={oaam_capabilities_ResourceConsumption_count}

# oaam_capabilities_SubconnectionInDeviceCapability class attributes and methods

# oaam_capabilities_MessageOnConnectionOrDeviceCapability class attributes and methods
oaam_capabilities_MessageOnConnectionOrDeviceCapability_worstCaseTransmissionTime: Property = Property(name="worstCaseTransmissionTime", type=FloatType)
oaam_capabilities_MessageOnConnectionOrDeviceCapability.attributes={oaam_capabilities_MessageOnConnectionOrDeviceCapability_worstCaseTransmissionTime}

# oaam_capabilities_MessageOnBusCapability class attributes and methods

# oaam_capabilities_SubmessageInMessageCapability class attributes and methods

# oaam_capabilities_Capabilities class attributes and methods

# CapabilitiesContainerA class attributes and methods

# oaam_capabilities_Subcapabilities class attributes and methods

# capabilities_CapabilitiesContainerA class attributes and methods

# oaam_capabilities_SignalInMessageCapability class attributes and methods

# AreaRestriction class attributes and methods

# PowerSourceRestriction class attributes and methods

# TaskAtomicRestriction class attributes and methods

# oaam_restrictions_RestrictionsContainerA class attributes and methods

# DeviceTypeRestriction class attributes and methods

# DeviceRestriction class attributes and methods

# LocationRestriction class attributes and methods

# SegregationRestriction class attributes and methods

# Subrestrictions class attributes and methods

# TaskSymmetryRestriction class attributes and methods

# SynchronicityRestriction class attributes and methods

# ConnectionRestriction class attributes and methods

# ConnectionTypeRestriction class attributes and methods

# oaam_restrictions_ConnectionRestrinctionA class attributes and methods

# TimeDelayRestriction class attributes and methods

# oaam_restrictions_Restrictions class attributes and methods

# RestrictionsContainerA class attributes and methods

# oaam_restrictions_DeviceRestrictionA class attributes and methods

# oaam_restrictions_TaskGroupRestrictionA class attributes and methods

# oaam_restrictions_TaskRestrictionA class attributes and methods

# oaam_restrictions_SignalRestrictionA class attributes and methods

# oaam_restrictions_SubfunctionRestrictionA class attributes and methods

# oaam_restrictions_SignalGroupRestrictionA class attributes and methods

# oaam_restrictions_LocationRestriction class attributes and methods
oaam_restrictions_LocationRestriction_locationName: Property = Property(name="locationName", type=StringType)
oaam_restrictions_LocationRestriction_isForbidden: Property = Property(name="isForbidden", type=BooleanType)
oaam_restrictions_LocationRestriction.attributes={oaam_restrictions_LocationRestriction_isForbidden, oaam_restrictions_LocationRestriction_locationName}

# restrictions_TaskRestrictionA class attributes and methods

# restrictions_TaskGroupRestrictionA class attributes and methods

# restrictions_SignalRestrictionA class attributes and methods

# restrictions_SignalGroupRestrictionA class attributes and methods

# restrictions_SubfunctionRestrictionA class attributes and methods

# restrictions_DeviceRestrictionA class attributes and methods

# restrictions_ConnectionRestrinctionA class attributes and methods

# oaam_restrictions_AreaRestriction class attributes and methods
oaam_restrictions_AreaRestriction_areaName: Property = Property(name="areaName", type=StringType)
oaam_restrictions_AreaRestriction_isForbidden: Property = Property(name="isForbidden", type=BooleanType)
oaam_restrictions_AreaRestriction.attributes={oaam_restrictions_AreaRestriction_isForbidden, oaam_restrictions_AreaRestriction_areaName}

# oaam_restrictions_DeviceTypeRestriction class attributes and methods
oaam_restrictions_DeviceTypeRestriction_deviceTypeName: Property = Property(name="deviceTypeName", type=StringType)
oaam_restrictions_DeviceTypeRestriction_isForbidden: Property = Property(name="isForbidden", type=BooleanType)
oaam_restrictions_DeviceTypeRestriction.attributes={oaam_restrictions_DeviceTypeRestriction_deviceTypeName, oaam_restrictions_DeviceTypeRestriction_isForbidden}

# oaam_restrictions_PowerSourceRestriction class attributes and methods
oaam_restrictions_PowerSourceRestriction_powerSourceName: Property = Property(name="powerSourceName", type=StringType)
oaam_restrictions_PowerSourceRestriction_isForbidden: Property = Property(name="isForbidden", type=BooleanType)
oaam_restrictions_PowerSourceRestriction.attributes={oaam_restrictions_PowerSourceRestriction_isForbidden, oaam_restrictions_PowerSourceRestriction_powerSourceName}

# oaam_restrictions_DeviceRestriction class attributes and methods
oaam_restrictions_DeviceRestriction_deviceName: Property = Property(name="deviceName", type=StringType)
oaam_restrictions_DeviceRestriction_isForbidden: Property = Property(name="isForbidden", type=BooleanType)
oaam_restrictions_DeviceRestriction.attributes={oaam_restrictions_DeviceRestriction_isForbidden, oaam_restrictions_DeviceRestriction_deviceName}

# oaam_restrictions_SegregationRestriction class attributes and methods
oaam_restrictions_SegregationRestriction_dissimilarArea: Property = Property(name="dissimilarArea", type=BooleanType)
oaam_restrictions_SegregationRestriction_dissimilarPowerSource: Property = Property(name="dissimilarPowerSource", type=BooleanType)
oaam_restrictions_SegregationRestriction_dissimilarTechnology: Property = Property(name="dissimilarTechnology", type=BooleanType)
oaam_restrictions_SegregationRestriction_dissimilarLocation: Property = Property(name="dissimilarLocation", type=BooleanType)
oaam_restrictions_SegregationRestriction.attributes={oaam_restrictions_SegregationRestriction_dissimilarPowerSource, oaam_restrictions_SegregationRestriction_dissimilarArea, oaam_restrictions_SegregationRestriction_dissimilarTechnology, oaam_restrictions_SegregationRestriction_dissimilarLocation}

# oaam_restrictions_ConnectionTypeRestriction class attributes and methods
oaam_restrictions_ConnectionTypeRestriction_connectionTypeName: Property = Property(name="connectionTypeName", type=StringType)
oaam_restrictions_ConnectionTypeRestriction_isForbidden: Property = Property(name="isForbidden", type=BooleanType)
oaam_restrictions_ConnectionTypeRestriction.attributes={oaam_restrictions_ConnectionTypeRestriction_connectionTypeName, oaam_restrictions_ConnectionTypeRestriction_isForbidden}

# oaam_restrictions_ConnectionRestriction class attributes and methods
oaam_restrictions_ConnectionRestriction_connectionName: Property = Property(name="connectionName", type=StringType)
oaam_restrictions_ConnectionRestriction_isForbidden: Property = Property(name="isForbidden", type=BooleanType)
oaam_restrictions_ConnectionRestriction.attributes={oaam_restrictions_ConnectionRestriction_connectionName, oaam_restrictions_ConnectionRestriction_isForbidden}

# oaam_restrictions_TaskSymmetryRestriction class attributes and methods
oaam_restrictions_TaskSymmetryRestriction_type: Property = Property(name="type", type=StringType)
oaam_restrictions_TaskSymmetryRestriction.attributes={oaam_restrictions_TaskSymmetryRestriction_type}

# oaam_restrictions_TimeDelayRestriction class attributes and methods
oaam_restrictions_TimeDelayRestriction_delay: Property = Property(name="delay", type=FloatType)
oaam_restrictions_TimeDelayRestriction.attributes={oaam_restrictions_TimeDelayRestriction_delay}

# oaam_restrictions_SynchronicityRestriction class attributes and methods
oaam_restrictions_SynchronicityRestriction_maxJitter: Property = Property(name="maxJitter", type=FloatType)
oaam_restrictions_SynchronicityRestriction.attributes={oaam_restrictions_SynchronicityRestriction_maxJitter}

# oaam_restrictions_TaskAtomicRestriction class attributes and methods

# oaam_allocations_AllocationsContainerA class attributes and methods

# oaam_restrictions_Subrestrictions class attributes and methods

# restrictions_RestrictionsContainerA class attributes and methods

# SignalAssignment class attributes and methods

# Suballocations class attributes and methods

# SubconnectionAssignment class attributes and methods

# Message class attributes and methods

# DeviceAssignment class attributes and methods

# SubdeviceAssignment class attributes and methods

# ConnectionAssignment class attributes and methods

# TaskAssignment class attributes and methods

# Schedule class attributes and methods

# oaam_allocations_SignalAssignment class attributes and methods

# SignalAssignmentSegment class attributes and methods

# oaam_allocations_TaskAssignment class attributes and methods

# oaam_allocations_SignalAssignmentSegment class attributes and methods

# oaam_allocations_ConnectionAssignment class attributes and methods

# ConnectionAssignmentSegment class attributes and methods

# oaam_allocations_DeviceAssignment class attributes and methods

# oaam_allocations_SubdeviceAssignment class attributes and methods

# oaam_allocations_ConnectionAssignmentSegment class attributes and methods

# oaam_allocations_Schedule class attributes and methods
oaam_allocations_Schedule_rate: Property = Property(name="rate", type=FloatType)
oaam_allocations_Schedule_isPeriodic: Property = Property(name="isPeriodic", type=BooleanType)
oaam_allocations_Schedule_priority: Property = Property(name="priority", type=IntegerType)
oaam_allocations_Schedule.attributes={oaam_allocations_Schedule_rate, oaam_allocations_Schedule_isPeriodic, oaam_allocations_Schedule_priority}

# oaam_allocations_SubconnectionAssignment class attributes and methods

# oaam_allocations_MessageA class attributes and methods
oaam_allocations_MessageA_isPersistent: Property = Property(name="isPersistent", type=BooleanType)
oaam_allocations_MessageA_length: Property = Property(name="length", type=IntegerType)
oaam_allocations_MessageA.attributes={oaam_allocations_MessageA_length, oaam_allocations_MessageA_isPersistent}

# ScheduledTime class attributes and methods

# oaam_allocations_ScheduledTime class attributes and methods
oaam_allocations_ScheduledTime_startTime: Property = Property(name="startTime", type=FloatType)
oaam_allocations_ScheduledTime_duration: Property = Property(name="duration", type=FloatType)
oaam_allocations_ScheduledTime_restart: Property = Property(name="restart", type=BooleanType)
oaam_allocations_ScheduledTime_cycle: Property = Property(name="cycle", type=IntegerType)
oaam_allocations_ScheduledTime.attributes={oaam_allocations_ScheduledTime_restart, oaam_allocations_ScheduledTime_duration, oaam_allocations_ScheduledTime_startTime, oaam_allocations_ScheduledTime_cycle}

# MessageSegment class attributes and methods

# Submessage class attributes and methods

# SignalToMessageAssignment class attributes and methods

# oaam_allocations_MessageSegment class attributes and methods

# oaam_allocations_Message class attributes and methods

# MessageA class attributes and methods

# oaam_allocations_Submessage class attributes and methods
oaam_allocations_Submessage_position: Property = Property(name="position", type=IntegerType)
oaam_allocations_Submessage.attributes={oaam_allocations_Submessage_position}

# oaam_allocations_SignalToMessageAssignment class attributes and methods
oaam_allocations_SignalToMessageAssignment_position: Property = Property(name="position", type=IntegerType)
oaam_allocations_SignalToMessageAssignment.attributes={oaam_allocations_SignalToMessageAssignment_position}

# oaam_allocations_Allocations class attributes and methods

# AllocationsContainerA class attributes and methods

# oaam_allocations_Suballocations class attributes and methods

# allocations_AllocationsContainerA class attributes and methods

# Relationships
include1: BinaryAssociation = BinaryAssociation(
    name="include1",
    ends={
        Property(name="oaam_Architecture", type=oaam_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_Architecture0", type=oaam_Architecture, multiplicity=Multiplicity(0, 9999))
    }
)
anatomy12: BinaryAssociation = BinaryAssociation(
    name="anatomy12",
    ends={
        Property(name="Anatomy", type=oaam_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_Architecture13", type=Anatomy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capabilities14: BinaryAssociation = BinaryAssociation(
    name="capabilities14",
    ends={
        Property(name="Capabilities", type=oaam_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_Architecture15", type=Capabilities, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
library2: BinaryAssociation = BinaryAssociation(
    name="library2",
    ends={
        Property(name="Library", type=oaam_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_Architecture3", type=Library, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scenario4: BinaryAssociation = BinaryAssociation(
    name="scenario4",
    ends={
        Property(name="Scenario", type=oaam_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_Architecture5", type=Scenario, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
systems6: BinaryAssociation = BinaryAssociation(
    name="systems6",
    ends={
        Property(name="Systems", type=oaam_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_Architecture7", type=Systems, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functions8: BinaryAssociation = BinaryAssociation(
    name="functions8",
    ends={
        Property(name="Functions", type=oaam_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_Architecture9", type=Functions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hardware10: BinaryAssociation = BinaryAssociation(
    name="hardware10",
    ends={
        Property(name="Hardware", type=oaam_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_Architecture11", type=Hardware, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
restrictions16: BinaryAssociation = BinaryAssociation(
    name="restrictions16",
    ends={
        Property(name="Restrictions", type=oaam_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_Architecture17", type=Restrictions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
allocations18: BinaryAssociation = BinaryAssociation(
    name="allocations18",
    ends={
        Property(name="Allocations", type=oaam_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_Architecture19", type=Allocations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes20: BinaryAssociation = BinaryAssociation(
    name="attributes20",
    ends={
        Property(name="AttributeA", type=oaam_common_OaamBaseElementA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_common_OaamBaseElementA", type=AttributeA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value21: BinaryAssociation = BinaryAssociation(
    name="value21",
    ends={
        Property(name="OaamBaseElementA", type=oaam_common_AttributeContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_common_AttributeContainment", type=OaamBaseElementA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value22: BinaryAssociation = BinaryAssociation(
    name="value22",
    ends={
        Property(name="OaamBaseElementA23", type=oaam_common_AttributeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_common_AttributeReference", type=OaamBaseElementA, multiplicity=Multiplicity(0, 9999))
    }
)
left24: BinaryAssociation = BinaryAssociation(
    name="left24",
    ends={
        Property(name="BoolA", type=oaam_common_BoolOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_common_BoolOperation", type=BoolA, multiplicity=Multiplicity(1, 1))
    }
)
right25: BinaryAssociation = BinaryAssociation(
    name="right25",
    ends={
        Property(name="BoolA27", type=oaam_common_BoolOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_common_BoolOperation26", type=BoolA, multiplicity=Multiplicity(1, 1))
    }
)
in28: BinaryAssociation = BinaryAssociation(
    name="in28",
    ends={
        Property(name="BoolA29", type=oaam_common_BoolNot, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_common_BoolNot", type=BoolA, multiplicity=Multiplicity(1, 1))
    }
)
type30: BinaryAssociation = BinaryAssociation(
    name="type30",
    ends={
        Property(name="DataTypeA", type=oaam_common_Array, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_common_Array", type=DataTypeA, multiplicity=Multiplicity(1, 1))
    }
)
fields31: BinaryAssociation = BinaryAssociation(
    name="fields31",
    ends={
        Property(name="DataTypeA32", type=oaam_common_Struct, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_common_Struct", type=DataTypeA, multiplicity=Multiplicity(1, 9999))
    }
)
inheritsFrom33: BinaryAssociation = BinaryAssociation(
    name="inheritsFrom33",
    ends={
        Property(name="Struct", type=oaam_common_Struct, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_common_Struct34", type=Struct, multiplicity=Multiplicity(0, 1))
    }
)
consumedGroups36: BinaryAssociation = BinaryAssociation(
    name="consumedGroups36",
    ends={
        Property(name="ResourceGroup", type=oaam_library_ResourceConsumerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ResourceConsumerA37", type=ResourceGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedBundles38: BinaryAssociation = BinaryAssociation(
    name="providedBundles38",
    ends={
        Property(name="ResourceBundle", type=oaam_library_ResourceProviderA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ResourceProviderA", type=ResourceBundle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
possibleResourceProvisions39: BinaryAssociation = BinaryAssociation(
    name="possibleResourceProvisions39",
    ends={
        Property(name="ResourceType", type=oaam_library_ResourceProviderA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ResourceProviderA40", type=ResourceType, multiplicity=Multiplicity(0, 9999))
    }
)
providedGroups41: BinaryAssociation = BinaryAssociation(
    name="providedGroups41",
    ends={
        Property(name="ResourceGroup43", type=oaam_library_ResourceProviderA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ResourceProviderA42", type=ResourceGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceLinks44: BinaryAssociation = BinaryAssociation(
    name="resourceLinks44",
    ends={
        Property(name="ResourceLink", type=oaam_library_ResourceProviderA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ResourceProviderA45", type=ResourceLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredResources35: BinaryAssociation = BinaryAssociation(
    name="requiredResources35",
    ends={
        Property(name="Resource", type=oaam_library_ResourceConsumerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ResourceConsumerA", type=Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes47: BinaryAssociation = BinaryAssociation(
    name="dataTypes47",
    ends={
        Property(name="DataTypeA48", type=oaam_library_LibraryContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_LibraryContainerA", type=DataTypeA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceTypes49: BinaryAssociation = BinaryAssociation(
    name="resourceTypes49",
    ends={
        Property(name="ResourceType51", type=oaam_library_LibraryContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_LibraryContainerA50", type=ResourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceBundles52: BinaryAssociation = BinaryAssociation(
    name="resourceBundles52",
    ends={
        Property(name="ResourceBundle54", type=oaam_library_LibraryContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_LibraryContainerA53", type=ResourceBundle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceModifiers55: BinaryAssociation = BinaryAssociation(
    name="resourceModifiers55",
    ends={
        Property(name="ResourceTypeModifier", type=oaam_library_LibraryContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_LibraryContainerA56", type=ResourceTypeModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceTypeDissimilarities57: BinaryAssociation = BinaryAssociation(
    name="resourceTypeDissimilarities57",
    ends={
        Property(name="ResourceTypeDissimilarity", type=oaam_library_LibraryContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_LibraryContainerA58", type=ResourceTypeDissimilarity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskTypes59: BinaryAssociation = BinaryAssociation(
    name="taskTypes59",
    ends={
        Property(name="TaskType", type=oaam_library_LibraryContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_LibraryContainerA60", type=TaskType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskTypeDissimilarity61: BinaryAssociation = BinaryAssociation(
    name="taskTypeDissimilarity61",
    ends={
        Property(name="TaskTypeDissimilarity", type=oaam_library_LibraryContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_LibraryContainerA62", type=TaskTypeDissimilarity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signalTypes63: BinaryAssociation = BinaryAssociation(
    name="signalTypes63",
    ends={
        Property(name="SignalType", type=oaam_library_LibraryContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_LibraryContainerA64", type=SignalType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredModifiers46: BinaryAssociation = BinaryAssociation(
    name="requiredModifiers46",
    ends={
        Property(name="ResourceTypeModifierLevel", type=oaam_library_ResourceProviderInstanceA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ResourceProviderInstanceA", type=ResourceTypeModifierLevel, multiplicity=Multiplicity(0, 9999))
    }
)
deviceTypeSymmetries67: BinaryAssociation = BinaryAssociation(
    name="deviceTypeSymmetries67",
    ends={
        Property(name="oaam_library_LibraryContainerA68", type=DeviceTypeSymmetry, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="DeviceTypeSymmetry", type=oaam_library_LibraryContainerA, multiplicity=Multiplicity(1, 1))
    }
)
ioTypes85: BinaryAssociation = BinaryAssociation(
    name="ioTypes85",
    ends={
        Property(name="IoType", type=oaam_library_LibraryContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_LibraryContainerA86", type=IoType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deviceTypeDissimilarities69: BinaryAssociation = BinaryAssociation(
    name="deviceTypeDissimilarities69",
    ends={
        Property(name="DeviceTypeDissimilarity", type=oaam_library_LibraryContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_LibraryContainerA70", type=DeviceTypeDissimilarity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hardwareGroupTypes87: BinaryAssociation = BinaryAssociation(
    name="hardwareGroupTypes87",
    ends={
        Property(name="BusType", type=oaam_library_LibraryContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_LibraryContainerA88", type=BusType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectionTypes71: BinaryAssociation = BinaryAssociation(
    name="connectionTypes71",
    ends={
        Property(name="ConnectionType", type=oaam_library_LibraryContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_LibraryContainerA72", type=ConnectionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wireTypes73: BinaryAssociation = BinaryAssociation(
    name="wireTypes73",
    ends={
        Property(name="WireType", type=oaam_library_LibraryContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_LibraryContainerA74", type=WireType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locationTypes75: BinaryAssociation = BinaryAssociation(
    name="locationTypes75",
    ends={
        Property(name="LocationType", type=oaam_library_LibraryContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_LibraryContainerA76", type=LocationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ductTypes77: BinaryAssociation = BinaryAssociation(
    name="ductTypes77",
    ends={
        Property(name="DuctType", type=oaam_library_LibraryContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_LibraryContainerA78", type=DuctType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
genericAttributes79: BinaryAssociation = BinaryAssociation(
    name="genericAttributes79",
    ends={
        Property(name="AttributeDefinition", type=oaam_library_LibraryContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_LibraryContainerA80", type=AttributeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
powerSources81: BinaryAssociation = BinaryAssociation(
    name="powerSources81",
    ends={
        Property(name="PowerSource", type=oaam_library_LibraryContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_LibraryContainerA82", type=PowerSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deviceTypes65: BinaryAssociation = BinaryAssociation(
    name="deviceTypes65",
    ends={
        Property(name="DeviceType", type=oaam_library_LibraryContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_LibraryContainerA66", type=DeviceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sublibraries83: BinaryAssociation = BinaryAssociation(
    name="sublibraries83",
    ends={
        Property(name="Sublibrary", type=oaam_library_LibraryContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_LibraryContainerA84", type=Sublibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alternatives95: BinaryAssociation = BinaryAssociation(
    name="alternatives95",
    ends={
        Property(name="ResourceAlternatives", type=oaam_library_ResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ResourceType96", type=ResourceAlternatives, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type97: BinaryAssociation = BinaryAssociation(
    name="type97",
    ends={
        Property(name="ResourceType98", type=oaam_library_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_Resource", type=ResourceType, multiplicity=Multiplicity(1, 1))
    }
)
messageTypes89: BinaryAssociation = BinaryAssociation(
    name="messageTypes89",
    ends={
        Property(name="MessageType", type=oaam_library_LibraryContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_LibraryContainerA90", type=MessageType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propagetedResources91: BinaryAssociation = BinaryAssociation(
    name="propagetedResources91",
    ends={
        Property(name="Resource92", type=oaam_library_ResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ResourceType", type=Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allowedModifiers93: BinaryAssociation = BinaryAssociation(
    name="allowedModifiers93",
    ends={
        Property(name="ResourceTypeModifierReference", type=oaam_library_ResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ResourceType94", type=ResourceTypeModifierReference, multiplicity=Multiplicity(0, 9999))
    }
)
stateDeclarations109: BinaryAssociation = BinaryAssociation(
    name="stateDeclarations109",
    ends={
        Property(name="TaskStateDeclaration", type=oaam_library_TaskType, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_TaskType110", type=TaskStateDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers99: BinaryAssociation = BinaryAssociation(
    name="modifiers99",
    ends={
        Property(name="ResourceTypeModifierLevel101", type=oaam_library_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_Resource100", type=ResourceTypeModifierLevel, multiplicity=Multiplicity(0, 9999))
    }
)
resources102: BinaryAssociation = BinaryAssociation(
    name="resources102",
    ends={
        Property(name="Resource103", type=oaam_library_ResourceAlternatives, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ResourceAlternatives", type=Resource, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
resources104: BinaryAssociation = BinaryAssociation(
    name="resources104",
    ends={
        Property(name="Resource105", type=oaam_library_ResourceBundle, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ResourceBundle", type=Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputDeclarations106: BinaryAssociation = BinaryAssociation(
    name="outputDeclarations106",
    ends={
        Property(name="OutputDeclaration", type=oaam_library_TaskType, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_TaskType", type=OutputDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputDeclarations107: BinaryAssociation = BinaryAssociation(
    name="inputDeclarations107",
    ends={
        Property(name="InputDeclaration", type=oaam_library_TaskType, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_TaskType108", type=InputDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterDeclarations111: BinaryAssociation = BinaryAssociation(
    name="parameterDeclarations111",
    ends={
        Property(name="TaskParameterDeclaration", type=oaam_library_TaskType, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_TaskType112", type=TaskParameterDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type113: BinaryAssociation = BinaryAssociation(
    name="type113",
    ends={
        Property(name="DataTypeA114", type=oaam_library_SignalType, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_SignalType", type=DataTypeA, multiplicity=Multiplicity(1, 1))
    }
)
ioDeclarations115: BinaryAssociation = BinaryAssociation(
    name="ioDeclarations115",
    ends={
        Property(name="IoDeclaration", type=oaam_library_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_DeviceType", type=IoDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startingPointResourceTypes120: BinaryAssociation = BinaryAssociation(
    name="startingPointResourceTypes120",
    ends={
        Property(name="ResourceType122", type=oaam_library_ConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ConnectionType121", type=ResourceType, multiplicity=Multiplicity(0, 9999))
    }
)
ioGroups116: BinaryAssociation = BinaryAssociation(
    name="ioGroups116",
    ends={
        Property(name="IoGroup", type=oaam_library_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_DeviceType117", type=IoGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wireTypes118: BinaryAssociation = BinaryAssociation(
    name="wireTypes118",
    ends={
        Property(name="WireType119", type=oaam_library_ConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ConnectionType", type=WireType, multiplicity=Multiplicity(0, 9999))
    }
)
messageType129: BinaryAssociation = BinaryAssociation(
    name="messageType129",
    ends={
        Property(name="MessageType131", type=oaam_library_ConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ConnectionType130", type=MessageType, multiplicity=Multiplicity(0, 1))
    }
)
endPointResourceTypes123: BinaryAssociation = BinaryAssociation(
    name="endPointResourceTypes123",
    ends={
        Property(name="ResourceType125", type=oaam_library_ConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ConnectionType124", type=ResourceType, multiplicity=Multiplicity(0, 9999))
    }
)
switchTypes126: BinaryAssociation = BinaryAssociation(
    name="switchTypes126",
    ends={
        Property(name="DeviceType128", type=oaam_library_ConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ConnectionType127", type=DeviceType, multiplicity=Multiplicity(0, 9999))
    }
)
ductOpeningDeclarations132: BinaryAssociation = BinaryAssociation(
    name="ductOpeningDeclarations132",
    ends={
        Property(name="DuctOpeningDeclaration", type=oaam_library_LocationType, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_LocationType", type=DuctOpeningDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger135: BinaryAssociation = BinaryAssociation(
    name="trigger135",
    ends={
        Property(name="TaskOutputTrigger", type=oaam_library_OutputDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_OutputDeclaration", type=TaskOutputTrigger, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type133: BinaryAssociation = BinaryAssociation(
    name="type133",
    ends={
        Property(name="DataTypeA134", type=oaam_library_InputDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_InputDeclaration", type=DataTypeA, multiplicity=Multiplicity(1, 1))
    }
)
resources146: BinaryAssociation = BinaryAssociation(
    name="resources146",
    ends={
        Property(name="Resource147", type=oaam_library_ResourceGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ResourceGroup", type=Resource, multiplicity=Multiplicity(0, 9999))
    }
)
type136: BinaryAssociation = BinaryAssociation(
    name="type136",
    ends={
        Property(name="DataTypeA138", type=oaam_library_OutputDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_OutputDeclaration137", type=DataTypeA, multiplicity=Multiplicity(1, 1))
    }
)
faultPropagations139: BinaryAssociation = BinaryAssociation(
    name="faultPropagations139",
    ends={
        Property(name="FaultPropagation", type=oaam_library_OutputDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_OutputDeclaration140", type=FaultPropagation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources141: BinaryAssociation = BinaryAssociation(
    name="resources141",
    ends={
        Property(name="Resource142", type=oaam_library_IoDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_IoDeclaration", type=Resource, multiplicity=Multiplicity(1, 9999))
    }
)
type143: BinaryAssociation = BinaryAssociation(
    name="type143",
    ends={
        Property(name="IoType145", type=oaam_library_IoDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_IoDeclaration144", type=IoType, multiplicity=Multiplicity(1, 1))
    }
)
condition152: BinaryAssociation = BinaryAssociation(
    name="condition152",
    ends={
        Property(name="BoolA153", type=oaam_library_FaultPropagation, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_FaultPropagation", type=BoolA, multiplicity=Multiplicity(1, 1))
    }
)
booleanOperations154: BinaryAssociation = BinaryAssociation(
    name="booleanOperations154",
    ends={
        Property(name="BoolOperation", type=oaam_library_FaultPropagation, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_FaultPropagation155", type=BoolOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deviceTypes148: BinaryAssociation = BinaryAssociation(
    name="deviceTypes148",
    ends={
        Property(name="DeviceType149", type=oaam_library_DeviceTypeSymmetry, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_DeviceTypeSymmetry", type=DeviceType, multiplicity=Multiplicity(2, 9999))
    }
)
ios150: BinaryAssociation = BinaryAssociation(
    name="ios150",
    ends={
        Property(name="IoDeclaration151", type=oaam_library_IoGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_IoGroup", type=IoDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
out164: BinaryAssociation = BinaryAssociation(
    name="out164",
    ends={
        Property(name="Resource166", type=oaam_library_ResourceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ResourceLink165", type=Resource, multiplicity=Multiplicity(1, 9999))
    }
)
booleanNots156: BinaryAssociation = BinaryAssociation(
    name="booleanNots156",
    ends={
        Property(name="BoolNot", type=oaam_library_FaultPropagation, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_FaultPropagation157", type=BoolNot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskInputStates158: BinaryAssociation = BinaryAssociation(
    name="taskInputStates158",
    ends={
        Property(name="TaskInputState", type=oaam_library_FaultPropagation, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_FaultPropagation159", type=TaskInputState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input160: BinaryAssociation = BinaryAssociation(
    name="input160",
    ends={
        Property(name="InputDeclaration161", type=oaam_library_TaskInputState, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_TaskInputState", type=InputDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
in162: BinaryAssociation = BinaryAssociation(
    name="in162",
    ends={
        Property(name="Resource163", type=oaam_library_ResourceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ResourceLink", type=Resource, multiplicity=Multiplicity(1, 9999))
    }
)
tasks179: BinaryAssociation = BinaryAssociation(
    name="tasks179",
    ends={
        Property(name="TaskType180", type=oaam_library_TaskTypeDissimilarity, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_TaskTypeDissimilarity", type=TaskType, multiplicity=Multiplicity(0, 9999))
    }
)
levels167: BinaryAssociation = BinaryAssociation(
    name="levels167",
    ends={
        Property(name="ResourceTypeModifierLevel168", type=oaam_library_ResourceTypeModifier, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ResourceTypeModifier", type=ResourceTypeModifierLevel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
equalAlternatives169: BinaryAssociation = BinaryAssociation(
    name="equalAlternatives169",
    ends={
        Property(name="ResourceTypeModifierLevel170", type=oaam_library_ResourceTypeModifierLevel, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ResourceTypeModifierLevel", type=ResourceTypeModifierLevel, multiplicity=Multiplicity(0, 9999))
    }
)
betterAlternative171: BinaryAssociation = BinaryAssociation(
    name="betterAlternative171",
    ends={
        Property(name="ResourceTypeModifierLevel173", type=oaam_library_ResourceTypeModifierLevel, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ResourceTypeModifierLevel172", type=ResourceTypeModifierLevel, multiplicity=Multiplicity(0, 1))
    }
)
type174: BinaryAssociation = BinaryAssociation(
    name="type174",
    ends={
        Property(name="ResourceTypeModifier175", type=oaam_library_ResourceTypeModifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ResourceTypeModifierReference", type=ResourceTypeModifier, multiplicity=Multiplicity(1, 1))
    }
)
allowedLevels176: BinaryAssociation = BinaryAssociation(
    name="allowedLevels176",
    ends={
        Property(name="ResourceTypeModifierLevel178", type=oaam_library_ResourceTypeModifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ResourceTypeModifierReference177", type=ResourceTypeModifierLevel, multiplicity=Multiplicity(1, 9999))
    }
)
resourceTypes183: BinaryAssociation = BinaryAssociation(
    name="resourceTypes183",
    ends={
        Property(name="ResourceType184", type=oaam_library_ResourceTypeDissimilarity, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_ResourceTypeDissimilarity", type=ResourceType, multiplicity=Multiplicity(0, 9999))
    }
)
devices181: BinaryAssociation = BinaryAssociation(
    name="devices181",
    ends={
        Property(name="DeviceType182", type=oaam_library_DeviceTypeDissimilarity, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_DeviceTypeDissimilarity", type=DeviceType, multiplicity=Multiplicity(0, 9999))
    }
)
input195: BinaryAssociation = BinaryAssociation(
    name="input195",
    ends={
        Property(name="InputDeclaration196", type=oaam_library_TaskInputTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_TaskInputTrigger", type=InputDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
condition185: BinaryAssociation = BinaryAssociation(
    name="condition185",
    ends={
        Property(name="BoolA186", type=oaam_library_TaskOutputTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_TaskOutputTrigger", type=BoolA, multiplicity=Multiplicity(0, 1))
    }
)
booleanOperations187: BinaryAssociation = BinaryAssociation(
    name="booleanOperations187",
    ends={
        Property(name="BoolOperation189", type=oaam_library_TaskOutputTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_TaskOutputTrigger188", type=BoolOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
booleanNots190: BinaryAssociation = BinaryAssociation(
    name="booleanNots190",
    ends={
        Property(name="BoolNot192", type=oaam_library_TaskOutputTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_TaskOutputTrigger191", type=BoolNot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskInputTriggers193: BinaryAssociation = BinaryAssociation(
    name="taskInputTriggers193",
    ends={
        Property(name="TaskInputTrigger", type=oaam_library_TaskOutputTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_TaskOutputTrigger194", type=TaskInputTrigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type197: BinaryAssociation = BinaryAssociation(
    name="type197",
    ends={
        Property(name="DataTypeA198", type=oaam_library_TaskStateDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_TaskStateDeclaration", type=DataTypeA, multiplicity=Multiplicity(1, 1))
    }
)
type199: BinaryAssociation = BinaryAssociation(
    name="type199",
    ends={
        Property(name="DataTypeA200", type=oaam_library_TaskParameterDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_TaskParameterDeclaration", type=DataTypeA, multiplicity=Multiplicity(1, 1))
    }
)
deviceTypes201: BinaryAssociation = BinaryAssociation(
    name="deviceTypes201",
    ends={
        Property(name="DeviceType202", type=oaam_library_BusType, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_BusType", type=DeviceType, multiplicity=Multiplicity(0, 9999))
    }
)
connectionTypes203: BinaryAssociation = BinaryAssociation(
    name="connectionTypes203",
    ends={
        Property(name="ConnectionType205", type=oaam_library_BusType, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_BusType204", type=ConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
messagetypes206: BinaryAssociation = BinaryAssociation(
    name="messagetypes206",
    ends={
        Property(name="MessageType208", type=oaam_library_BusType, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_BusType207", type=MessageType, multiplicity=Multiplicity(0, 9999))
    }
)
headerDefinition209: BinaryAssociation = BinaryAssociation(
    name="headerDefinition209",
    ends={
        Property(name="DataTypeA210", type=oaam_library_MessageType, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_MessageType", type=DataTypeA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trailerDefinition211: BinaryAssociation = BinaryAssociation(
    name="trailerDefinition211",
    ends={
        Property(name="DataTypeA213", type=oaam_library_MessageType, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_library_MessageType212", type=DataTypeA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variants215: BinaryAssociation = BinaryAssociation(
    name="variants215",
    ends={
        Property(name="Variant", type=oaam_scenario_VariantDependentElementA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_scenario_VariantDependentElementA", type=Variant, multiplicity=Multiplicity(0, 9999))
    }
)
operationModes214: BinaryAssociation = BinaryAssociation(
    name="operationModes214",
    ends={
        Property(name="OperationModeReference", type=oaam_scenario_ModeDependentElementA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_scenario_ModeDependentElementA", type=OperationModeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters216: BinaryAssociation = BinaryAssociation(
    name="parameters216",
    ends={
        Property(name="ScenarioParameterA", type=oaam_scenario_ScenarioContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_scenario_ScenarioContainerA", type=ScenarioParameterA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variants217: BinaryAssociation = BinaryAssociation(
    name="variants217",
    ends={
        Property(name="Variant219", type=oaam_scenario_ScenarioContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_scenario_ScenarioContainerA218", type=Variant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operationModes220: BinaryAssociation = BinaryAssociation(
    name="operationModes220",
    ends={
        Property(name="OperationMode", type=oaam_scenario_ScenarioContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_scenario_ScenarioContainerA221", type=OperationMode, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
subscenarios222: BinaryAssociation = BinaryAssociation(
    name="subscenarios222",
    ends={
        Property(name="Subscenario", type=oaam_scenario_ScenarioContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_scenario_ScenarioContainerA223", type=Subscenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operationMode224: BinaryAssociation = BinaryAssociation(
    name="operationMode224",
    ends={
        Property(name="OperationMode225", type=oaam_scenario_OperationModeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_scenario_OperationModeReference", type=OperationMode, multiplicity=Multiplicity(1, 1))
    }
)
systems226: BinaryAssociation = BinaryAssociation(
    name="systems226",
    ends={
        Property(name="System", type=oaam_systems_SystemsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_systems_SystemsContainerA", type=System, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
informationFlows227: BinaryAssociation = BinaryAssociation(
    name="informationFlows227",
    ends={
        Property(name="InformationFlow", type=oaam_systems_SystemsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_systems_SystemsContainerA228", type=InformationFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputSegregations229: BinaryAssociation = BinaryAssociation(
    name="inputSegregations229",
    ends={
        Property(name="InputSegregation", type=oaam_systems_SystemsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_systems_SystemsContainerA230", type=InputSegregation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subsystems231: BinaryAssociation = BinaryAssociation(
    name="subsystems231",
    ends={
        Property(name="Subsystem", type=oaam_systems_SystemsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_systems_SystemsContainerA232", type=Subsystem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from236: BinaryAssociation = BinaryAssociation(
    name="from236",
    ends={
        Property(name="ProvidedInformationA237", type=oaam_systems_InformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_systems_InformationFlow", type=ProvidedInformationA, multiplicity=Multiplicity(1, 1))
    }
)
to238: BinaryAssociation = BinaryAssociation(
    name="to238",
    ends={
        Property(name="RequiredInformationA240", type=oaam_systems_InformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_systems_InformationFlow239", type=RequiredInformationA, multiplicity=Multiplicity(1, 1))
    }
)
providedOutputs233: BinaryAssociation = BinaryAssociation(
    name="providedOutputs233",
    ends={
        Property(name="ProvidedInformationA", type=oaam_systems_System, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_systems_System", type=ProvidedInformationA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInputs234: BinaryAssociation = BinaryAssociation(
    name="requiredInputs234",
    ends={
        Property(name="RequiredInformationA", type=oaam_systems_System, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_systems_System235", type=RequiredInformationA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tasks246: BinaryAssociation = BinaryAssociation(
    name="tasks246",
    ends={
        Property(name="Task", type=oaam_functions_FunctionsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_FunctionsContainerA", type=Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskLinks247: BinaryAssociation = BinaryAssociation(
    name="taskLinks247",
    ends={
        Property(name="ExternalTaskLink", type=oaam_functions_FunctionsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_FunctionsContainerA248", type=ExternalTaskLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskGroups249: BinaryAssociation = BinaryAssociation(
    name="taskGroups249",
    ends={
        Property(name="TaskGroup", type=oaam_functions_FunctionsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_FunctionsContainerA250", type=TaskGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groupA241: BinaryAssociation = BinaryAssociation(
    name="groupA241",
    ends={
        Property(name="RequiredInformationA242", type=oaam_systems_InputSegregation, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_systems_InputSegregation", type=RequiredInformationA, multiplicity=Multiplicity(1, 9999))
    }
)
groupB243: BinaryAssociation = BinaryAssociation(
    name="groupB243",
    ends={
        Property(name="RequiredInformationA245", type=oaam_systems_InputSegregation, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_systems_InputSegregation244", type=RequiredInformationA, multiplicity=Multiplicity(1, 9999))
    }
)
failureConditions259: BinaryAssociation = BinaryAssociation(
    name="failureConditions259",
    ends={
        Property(name="FailureCondition", type=oaam_functions_FunctionsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_FunctionsContainerA260", type=FailureCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subfunctions261: BinaryAssociation = BinaryAssociation(
    name="subfunctions261",
    ends={
        Property(name="Subfunctions", type=oaam_functions_FunctionsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_FunctionsContainerA262", type=Subfunctions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskSymmetries251: BinaryAssociation = BinaryAssociation(
    name="taskSymmetries251",
    ends={
        Property(name="TaskSymmetry", type=oaam_functions_FunctionsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_FunctionsContainerA252", type=TaskSymmetry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskRedundancies253: BinaryAssociation = BinaryAssociation(
    name="taskRedundancies253",
    ends={
        Property(name="TaskRedundancy", type=oaam_functions_FunctionsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_FunctionsContainerA254", type=TaskRedundancy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signals255: BinaryAssociation = BinaryAssociation(
    name="signals255",
    ends={
        Property(name="Signal", type=oaam_functions_FunctionsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_FunctionsContainerA256", type=Signal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signalGroups257: BinaryAssociation = BinaryAssociation(
    name="signalGroups257",
    ends={
        Property(name="SignalGroup", type=oaam_functions_FunctionsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_FunctionsContainerA258", type=SignalGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs267: BinaryAssociation = BinaryAssociation(
    name="outputs267",
    ends={
        Property(name="Output", type=oaam_functions_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_Task268", type=Output, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implements269: BinaryAssociation = BinaryAssociation(
    name="implements269",
    ends={
        Property(name="System271", type=oaam_functions_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_Task270", type=System, multiplicity=Multiplicity(0, 1))
    }
)
type263: BinaryAssociation = BinaryAssociation(
    name="type263",
    ends={
        Property(name="TaskType264", type=oaam_functions_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_Task", type=TaskType, multiplicity=Multiplicity(1, 1))
    }
)
inputs265: BinaryAssociation = BinaryAssociation(
    name="inputs265",
    ends={
        Property(name="Input", type=oaam_functions_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_Task266", type=Input, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputs278: BinaryAssociation = BinaryAssociation(
    name="inputs278",
    ends={
        Property(name="Input280", type=oaam_functions_ExternalTaskLink, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_ExternalTaskLink279", type=Input, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs281: BinaryAssociation = BinaryAssociation(
    name="outputs281",
    ends={
        Property(name="Output283", type=oaam_functions_ExternalTaskLink, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_ExternalTaskLink282", type=Output, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deviceBinding272: BinaryAssociation = BinaryAssociation(
    name="deviceBinding272",
    ends={
        Property(name="Device", type=oaam_functions_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_Task273", type=Device, multiplicity=Multiplicity(0, 1))
    }
)
parameters274: BinaryAssociation = BinaryAssociation(
    name="parameters274",
    ends={
        Property(name="TaskParameter", type=oaam_functions_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_Task275", type=TaskParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type276: BinaryAssociation = BinaryAssociation(
    name="type276",
    ends={
        Property(name="TaskType277", type=oaam_functions_ExternalTaskLink, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_ExternalTaskLink", type=TaskType, multiplicity=Multiplicity(1, 1))
    }
)
tasks289: BinaryAssociation = BinaryAssociation(
    name="tasks289",
    ends={
        Property(name="Task290", type=oaam_functions_TaskSymmetry, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_TaskSymmetry", type=Task, multiplicity=Multiplicity(2, 9999))
    }
)
task284: BinaryAssociation = BinaryAssociation(
    name="task284",
    ends={
        Property(name="Task286", type=oaam_functions_ExternalTaskLink, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_ExternalTaskLink285", type=Task, multiplicity=Multiplicity(0, 1))
    }
)
tasks287: BinaryAssociation = BinaryAssociation(
    name="tasks287",
    ends={
        Property(name="Task288", type=oaam_functions_TaskGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_TaskGroup", type=Task, multiplicity=Multiplicity(1, 9999))
    }
)
condition293: BinaryAssociation = BinaryAssociation(
    name="condition293",
    ends={
        Property(name="BoolA294", type=oaam_functions_FailureCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_FailureCondition", type=BoolA, multiplicity=Multiplicity(1, 1))
    }
)
tasks291: BinaryAssociation = BinaryAssociation(
    name="tasks291",
    ends={
        Property(name="Task292", type=oaam_functions_TaskRedundancy, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_TaskRedundancy", type=Task, multiplicity=Multiplicity(2, 9999))
    }
)
booleanNots298: BinaryAssociation = BinaryAssociation(
    name="booleanNots298",
    ends={
        Property(name="BoolNot300", type=oaam_functions_FailureCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_FailureCondition299", type=BoolNot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
booleanOperations295: BinaryAssociation = BinaryAssociation(
    name="booleanOperations295",
    ends={
        Property(name="BoolOperation297", type=oaam_functions_FailureCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_FailureCondition296", type=BoolOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
output303: BinaryAssociation = BinaryAssociation(
    name="output303",
    ends={
        Property(name="Output304", type=oaam_functions_OutputIntegrityState, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_OutputIntegrityState", type=Output, multiplicity=Multiplicity(1, 1))
    }
)
outputIntegrityStates301: BinaryAssociation = BinaryAssociation(
    name="outputIntegrityStates301",
    ends={
        Property(name="OutputIntegrityState", type=oaam_functions_FailureCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_FailureCondition302", type=OutputIntegrityState, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type310: BinaryAssociation = BinaryAssociation(
    name="type310",
    ends={
        Property(name="oaam_functions_Signal311", type=SignalType, multiplicity=Multiplicity(1, 1)),
        Property(name="SignalType312", type=oaam_functions_Signal, multiplicity=Multiplicity(1, 1))
    }
)
source305: BinaryAssociation = BinaryAssociation(
    name="source305",
    ends={
        Property(name="Output306", type=oaam_functions_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_Signal", type=Output, multiplicity=Multiplicity(1, 1))
    }
)
target307: BinaryAssociation = BinaryAssociation(
    name="target307",
    ends={
        Property(name="Input309", type=oaam_functions_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_Signal308", type=Input, multiplicity=Multiplicity(1, 1))
    }
)
declaration317: BinaryAssociation = BinaryAssociation(
    name="declaration317",
    ends={
        Property(name="InputDeclaration318", type=oaam_functions_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_Input", type=InputDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
connectionBinding313: BinaryAssociation = BinaryAssociation(
    name="connectionBinding313",
    ends={
        Property(name="Connection", type=oaam_functions_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_Signal314", type=Connection, multiplicity=Multiplicity(0, 1))
    }
)
signals315: BinaryAssociation = BinaryAssociation(
    name="signals315",
    ends={
        Property(name="Signal316", type=oaam_functions_SignalGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_SignalGroup", type=Signal, multiplicity=Multiplicity(1, 9999))
    }
)
implements326: BinaryAssociation = BinaryAssociation(
    name="implements326",
    ends={
        Property(name="ProvidedInformationA327", type=oaam_functions_Output, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_Output", type=ProvidedInformationA, multiplicity=Multiplicity(0, 1))
    }
)
declaration328: BinaryAssociation = BinaryAssociation(
    name="declaration328",
    ends={
        Property(name="OutputDeclaration330", type=oaam_functions_Output, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_Output329", type=OutputDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
implements319: BinaryAssociation = BinaryAssociation(
    name="implements319",
    ends={
        Property(name="RequiredInformationA321", type=oaam_functions_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_Input320", type=RequiredInformationA, multiplicity=Multiplicity(0, 1))
    }
)
ioBindings322: BinaryAssociation = BinaryAssociation(
    name="ioBindings322",
    ends={
        Property(name="Io", type=oaam_functions_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_Input323", type=Io, multiplicity=Multiplicity(0, 9999))
    }
)
outputLink324: BinaryAssociation = BinaryAssociation(
    name="outputLink324",
    ends={
        Property(name="ExternalOutputLink", type=oaam_functions_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_Input325", type=ExternalOutputLink, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ioBindings331: BinaryAssociation = BinaryAssociation(
    name="ioBindings331",
    ends={
        Property(name="Io333", type=oaam_functions_Output, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_Output332", type=Io, multiplicity=Multiplicity(0, 9999))
    }
)
output334: BinaryAssociation = BinaryAssociation(
    name="output334",
    ends={
        Property(name="Output335", type=oaam_functions_ExternalOutputLink, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_ExternalOutputLink", type=Output, multiplicity=Multiplicity(0, 1))
    }
)
deviceSymmetries340: BinaryAssociation = BinaryAssociation(
    name="deviceSymmetries340",
    ends={
        Property(name="DeviceSymmetry", type=oaam_hardware_HardwareContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_hardware_HardwareContainerA341", type=DeviceSymmetry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections342: BinaryAssociation = BinaryAssociation(
    name="connections342",
    ends={
        Property(name="Connection344", type=oaam_hardware_HardwareContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_hardware_HardwareContainerA343", type=Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subhardware345: BinaryAssociation = BinaryAssociation(
    name="subhardware345",
    ends={
        Property(name="Subhardware", type=oaam_hardware_HardwareContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_hardware_HardwareContainerA346", type=Subhardware, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definition336: BinaryAssociation = BinaryAssociation(
    name="definition336",
    ends={
        Property(name="TaskParameterDeclaration337", type=oaam_functions_TaskParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_functions_TaskParameter", type=TaskParameterDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
devices338: BinaryAssociation = BinaryAssociation(
    name="devices338",
    ends={
        Property(name="Device339", type=oaam_hardware_HardwareContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_hardware_HardwareContainerA", type=Device, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subdevices354: BinaryAssociation = BinaryAssociation(
    name="subdevices354",
    ends={
        Property(name="Device356", type=oaam_hardware_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_hardware_Device355", type=Device, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locationBinding357: BinaryAssociation = BinaryAssociation(
    name="locationBinding357",
    ends={
        Property(name="Location", type=oaam_hardware_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_hardware_Device358", type=Location, multiplicity=Multiplicity(0, 1))
    }
)
buses347: BinaryAssociation = BinaryAssociation(
    name="buses347",
    ends={
        Property(name="Bus", type=oaam_hardware_HardwareContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_hardware_HardwareContainerA348", type=Bus, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type349: BinaryAssociation = BinaryAssociation(
    name="type349",
    ends={
        Property(name="DeviceType350", type=oaam_hardware_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_hardware_Device", type=DeviceType, multiplicity=Multiplicity(0, 1))
    }
)
ios351: BinaryAssociation = BinaryAssociation(
    name="ios351",
    ends={
        Property(name="Io353", type=oaam_hardware_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_hardware_Device352", type=Io, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startingPoints367: BinaryAssociation = BinaryAssociation(
    name="startingPoints367",
    ends={
        Property(name="Io369", type=oaam_hardware_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_hardware_Connection368", type=Io, multiplicity=Multiplicity(0, 9999))
    }
)
endPoints370: BinaryAssociation = BinaryAssociation(
    name="endPoints370",
    ends={
        Property(name="Io372", type=oaam_hardware_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_hardware_Connection371", type=Io, multiplicity=Multiplicity(0, 9999))
    }
)
powerSources359: BinaryAssociation = BinaryAssociation(
    name="powerSources359",
    ends={
        Property(name="PowerSource361", type=oaam_hardware_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_hardware_Device360", type=PowerSource, multiplicity=Multiplicity(0, 9999))
    }
)
subconnections362: BinaryAssociation = BinaryAssociation(
    name="subconnections362",
    ends={
        Property(name="Connection364", type=oaam_hardware_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_hardware_Device363", type=Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type365: BinaryAssociation = BinaryAssociation(
    name="type365",
    ends={
        Property(name="ConnectionType366", type=oaam_hardware_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_hardware_Connection", type=ConnectionType, multiplicity=Multiplicity(0, 1))
    }
)
devices378: BinaryAssociation = BinaryAssociation(
    name="devices378",
    ends={
        Property(name="Device379", type=oaam_hardware_DeviceSymmetry, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_hardware_DeviceSymmetry", type=Device, multiplicity=Multiplicity(2, 9999))
    }
)
masters373: BinaryAssociation = BinaryAssociation(
    name="masters373",
    ends={
        Property(name="Io375", type=oaam_hardware_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_hardware_Connection374", type=Io, multiplicity=Multiplicity(0, 9999))
    }
)
declaration376: BinaryAssociation = BinaryAssociation(
    name="declaration376",
    ends={
        Property(name="IoDeclaration377", type=oaam_hardware_Io, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_hardware_Io", type=IoDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
type380: BinaryAssociation = BinaryAssociation(
    name="type380",
    ends={
        Property(name="BusType381", type=oaam_hardware_Bus, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_hardware_Bus", type=BusType, multiplicity=Multiplicity(0, 1))
    }
)
connections382: BinaryAssociation = BinaryAssociation(
    name="connections382",
    ends={
        Property(name="Connection384", type=oaam_hardware_Bus, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_hardware_Bus383", type=Connection, multiplicity=Multiplicity(0, 9999))
    }
)
devices385: BinaryAssociation = BinaryAssociation(
    name="devices385",
    ends={
        Property(name="Device387", type=oaam_hardware_Bus, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_hardware_Bus386", type=Device, multiplicity=Multiplicity(0, 9999))
    }
)
areaSymmetries398: BinaryAssociation = BinaryAssociation(
    name="areaSymmetries398",
    ends={
        Property(name="AreaSymmetry", type=oaam_anatomy_AnatomyContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_anatomy_AnatomyContainerA399", type=AreaSymmetry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locations388: BinaryAssociation = BinaryAssociation(
    name="locations388",
    ends={
        Property(name="Location389", type=oaam_anatomy_AnatomyContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_anatomy_AnatomyContainerA", type=Location, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locationSymmetries390: BinaryAssociation = BinaryAssociation(
    name="locationSymmetries390",
    ends={
        Property(name="LocationSymmetry", type=oaam_anatomy_AnatomyContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_anatomy_AnatomyContainerA391", type=LocationSymmetry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ducts392: BinaryAssociation = BinaryAssociation(
    name="ducts392",
    ends={
        Property(name="Duct", type=oaam_anatomy_AnatomyContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_anatomy_AnatomyContainerA393", type=Duct, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
areas394: BinaryAssociation = BinaryAssociation(
    name="areas394",
    ends={
        Property(name="Area", type=oaam_anatomy_AnatomyContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_anatomy_AnatomyContainerA395", type=Area, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subanatomies396: BinaryAssociation = BinaryAssociation(
    name="subanatomies396",
    ends={
        Property(name="Subanatomy", type=oaam_anatomy_AnatomyContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_anatomy_AnatomyContainerA397", type=Subanatomy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ductOpenings404: BinaryAssociation = BinaryAssociation(
    name="ductOpenings404",
    ends={
        Property(name="DuctOpening", type=oaam_anatomy_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_anatomy_Location405", type=DuctOpening, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type400: BinaryAssociation = BinaryAssociation(
    name="type400",
    ends={
        Property(name="LocationType401", type=oaam_anatomy_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_anatomy_Location", type=LocationType, multiplicity=Multiplicity(1, 1))
    }
)
position402: BinaryAssociation = BinaryAssociation(
    name="position402",
    ends={
        Property(name="Position3D", type=oaam_anatomy_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_anatomy_Location403", type=Position3D, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type411: BinaryAssociation = BinaryAssociation(
    name="type411",
    ends={
        Property(name="DuctType412", type=oaam_anatomy_Duct, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_anatomy_Duct", type=DuctType, multiplicity=Multiplicity(1, 1))
    }
)
startingPoint413: BinaryAssociation = BinaryAssociation(
    name="startingPoint413",
    ends={
        Property(name="DuctOpening415", type=oaam_anatomy_Duct, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_anatomy_Duct414", type=DuctOpening, multiplicity=Multiplicity(1, 1))
    }
)
locations406: BinaryAssociation = BinaryAssociation(
    name="locations406",
    ends={
        Property(name="Location407", type=oaam_anatomy_Area, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_anatomy_Area", type=Location, multiplicity=Multiplicity(0, 9999))
    }
)
ducts408: BinaryAssociation = BinaryAssociation(
    name="ducts408",
    ends={
        Property(name="Duct410", type=oaam_anatomy_Area, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_anatomy_Area409", type=Duct, multiplicity=Multiplicity(0, 9999))
    }
)
endPoint416: BinaryAssociation = BinaryAssociation(
    name="endPoint416",
    ends={
        Property(name="DuctOpening418", type=oaam_anatomy_Duct, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_anatomy_Duct417", type=DuctOpening, multiplicity=Multiplicity(1, 1))
    }
)
relativPosition419: BinaryAssociation = BinaryAssociation(
    name="relativPosition419",
    ends={
        Property(name="Position3D420", type=oaam_anatomy_DuctOpening, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_anatomy_DuctOpening", type=Position3D, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration421: BinaryAssociation = BinaryAssociation(
    name="declaration421",
    ends={
        Property(name="DuctOpeningDeclaration423", type=oaam_anatomy_DuctOpening, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_anatomy_DuctOpening422", type=DuctOpeningDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
areas426: BinaryAssociation = BinaryAssociation(
    name="areas426",
    ends={
        Property(name="Area427", type=oaam_anatomy_AreaSymmetry, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_anatomy_AreaSymmetry", type=Area, multiplicity=Multiplicity(0, 9999))
    }
)
locations424: BinaryAssociation = BinaryAssociation(
    name="locations424",
    ends={
        Property(name="Location425", type=oaam_anatomy_LocationSymmetry, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_anatomy_LocationSymmetry", type=Location, multiplicity=Multiplicity(0, 9999))
    }
)
taskOnDeviceCapabilities429: BinaryAssociation = BinaryAssociation(
    name="taskOnDeviceCapabilities429",
    ends={
        Property(name="TaskOnDeviceCapability", type=oaam_capabilities_CapabilitiesContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_CapabilitiesContainerA", type=TaskOnDeviceCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceConsumptions428: BinaryAssociation = BinaryAssociation(
    name="resourceConsumptions428",
    ends={
        Property(name="ResourceConsumption", type=oaam_capabilities_CapabilityA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_CapabilityA", type=ResourceConsumption, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectionInDuctOrLocationCapabilities436: BinaryAssociation = BinaryAssociation(
    name="connectionInDuctOrLocationCapabilities436",
    ends={
        Property(name="ConnectionInDuctOrLocationCapability", type=oaam_capabilities_CapabilitiesContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_CapabilitiesContainerA437", type=ConnectionInDuctOrLocationCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subcapabilities438: BinaryAssociation = BinaryAssociation(
    name="subcapabilities438",
    ends={
        Property(name="Subcapabilities", type=oaam_capabilities_CapabilitiesContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_CapabilitiesContainerA439", type=Subcapabilities, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signalOnConnectionOrDeviceCapabilities430: BinaryAssociation = BinaryAssociation(
    name="signalOnConnectionOrDeviceCapabilities430",
    ends={
        Property(name="SignalOnConnectionOrDeviceCapability", type=oaam_capabilities_CapabilitiesContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_CapabilitiesContainerA431", type=SignalOnConnectionOrDeviceCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deviceInLocationCapabilities432: BinaryAssociation = BinaryAssociation(
    name="deviceInLocationCapabilities432",
    ends={
        Property(name="DeviceInLocationCapability", type=oaam_capabilities_CapabilitiesContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_CapabilitiesContainerA433", type=DeviceInLocationCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subdeviceInDeviceCapabilities434: BinaryAssociation = BinaryAssociation(
    name="subdeviceInDeviceCapabilities434",
    ends={
        Property(name="SubdeviceInDeviceCapability", type=oaam_capabilities_CapabilitiesContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_CapabilitiesContainerA435", type=SubdeviceInDeviceCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signalInMessageCapabilities446: BinaryAssociation = BinaryAssociation(
    name="signalInMessageCapabilities446",
    ends={
        Property(name="oaam_capabilities_CapabilitiesContainerA447", type=SignalInMessageCapability, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="SignalInMessageCapability", type=oaam_capabilities_CapabilitiesContainerA, multiplicity=Multiplicity(1, 1))
    }
)
messageOnConnectionOrDeviceCapabilities448: BinaryAssociation = BinaryAssociation(
    name="messageOnConnectionOrDeviceCapabilities448",
    ends={
        Property(name="MessageOnConnectionOrDeviceCapability", type=oaam_capabilities_CapabilitiesContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_CapabilitiesContainerA449", type=MessageOnConnectionOrDeviceCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subconnectionInDeviceCapabilities440: BinaryAssociation = BinaryAssociation(
    name="subconnectionInDeviceCapabilities440",
    ends={
        Property(name="SubconnectionInDeviceCapability", type=oaam_capabilities_CapabilitiesContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_CapabilitiesContainerA441", type=SubconnectionInDeviceCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageOnBusCapabilities442: BinaryAssociation = BinaryAssociation(
    name="messageOnBusCapabilities442",
    ends={
        Property(name="MessageOnBusCapability", type=oaam_capabilities_CapabilitiesContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_CapabilitiesContainerA443", type=MessageOnBusCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
submessageInMessageCapabilities444: BinaryAssociation = BinaryAssociation(
    name="submessageInMessageCapabilities444",
    ends={
        Property(name="SubmessageInMessageCapability", type=oaam_capabilities_CapabilitiesContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_CapabilitiesContainerA445", type=SubmessageInMessageCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deviceType455: BinaryAssociation = BinaryAssociation(
    name="deviceType455",
    ends={
        Property(name="DeviceType456", type=oaam_capabilities_DeviceInLocationCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_DeviceInLocationCapability", type=DeviceType, multiplicity=Multiplicity(1, 1))
    }
)
taskType450: BinaryAssociation = BinaryAssociation(
    name="taskType450",
    ends={
        Property(name="TaskType451", type=oaam_capabilities_TaskOnDeviceCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_TaskOnDeviceCapability", type=TaskType, multiplicity=Multiplicity(1, 1))
    }
)
deviceType452: BinaryAssociation = BinaryAssociation(
    name="deviceType452",
    ends={
        Property(name="DeviceType454", type=oaam_capabilities_TaskOnDeviceCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_TaskOnDeviceCapability453", type=DeviceType, multiplicity=Multiplicity(1, 1))
    }
)
ductType465: BinaryAssociation = BinaryAssociation(
    name="ductType465",
    ends={
        Property(name="DuctType467", type=oaam_capabilities_ConnectionInDuctOrLocationCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_ConnectionInDuctOrLocationCapability466", type=DuctType, multiplicity=Multiplicity(0, 1))
    }
)
locationType457: BinaryAssociation = BinaryAssociation(
    name="locationType457",
    ends={
        Property(name="LocationType459", type=oaam_capabilities_DeviceInLocationCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_DeviceInLocationCapability458", type=LocationType, multiplicity=Multiplicity(1, 1))
    }
)
connectionType460: BinaryAssociation = BinaryAssociation(
    name="connectionType460",
    ends={
        Property(name="ConnectionType461", type=oaam_capabilities_ConnectionInDuctOrLocationCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_ConnectionInDuctOrLocationCapability", type=ConnectionType, multiplicity=Multiplicity(1, 1))
    }
)
locationType462: BinaryAssociation = BinaryAssociation(
    name="locationType462",
    ends={
        Property(name="LocationType464", type=oaam_capabilities_ConnectionInDuctOrLocationCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_ConnectionInDuctOrLocationCapability463", type=LocationType, multiplicity=Multiplicity(0, 1))
    }
)
subdeviceType476: BinaryAssociation = BinaryAssociation(
    name="subdeviceType476",
    ends={
        Property(name="DeviceType477", type=oaam_capabilities_SubdeviceInDeviceCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_SubdeviceInDeviceCapability", type=DeviceType, multiplicity=Multiplicity(1, 1))
    }
)
signalType468: BinaryAssociation = BinaryAssociation(
    name="signalType468",
    ends={
        Property(name="SignalType469", type=oaam_capabilities_SignalOnConnectionOrDeviceCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_SignalOnConnectionOrDeviceCapability", type=SignalType, multiplicity=Multiplicity(1, 1))
    }
)
deviceType470: BinaryAssociation = BinaryAssociation(
    name="deviceType470",
    ends={
        Property(name="DeviceType472", type=oaam_capabilities_SignalOnConnectionOrDeviceCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_SignalOnConnectionOrDeviceCapability471", type=DeviceType, multiplicity=Multiplicity(0, 1))
    }
)
connectionType473: BinaryAssociation = BinaryAssociation(
    name="connectionType473",
    ends={
        Property(name="ConnectionType475", type=oaam_capabilities_SignalOnConnectionOrDeviceCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_SignalOnConnectionOrDeviceCapability474", type=ConnectionType, multiplicity=Multiplicity(0, 1))
    }
)
targetDeviceType483: BinaryAssociation = BinaryAssociation(
    name="targetDeviceType483",
    ends={
        Property(name="DeviceType485", type=oaam_capabilities_SubconnectionInDeviceCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_SubconnectionInDeviceCapability484", type=DeviceType, multiplicity=Multiplicity(1, 1))
    }
)
targetDeviceType478: BinaryAssociation = BinaryAssociation(
    name="targetDeviceType478",
    ends={
        Property(name="DeviceType480", type=oaam_capabilities_SubdeviceInDeviceCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_SubdeviceInDeviceCapability479", type=DeviceType, multiplicity=Multiplicity(1, 1))
    }
)
subconnectionType481: BinaryAssociation = BinaryAssociation(
    name="subconnectionType481",
    ends={
        Property(name="ConnectionType482", type=oaam_capabilities_SubconnectionInDeviceCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_SubconnectionInDeviceCapability", type=ConnectionType, multiplicity=Multiplicity(1, 1))
    }
)
messageType493: BinaryAssociation = BinaryAssociation(
    name="messageType493",
    ends={
        Property(name="MessageType495", type=oaam_capabilities_MessageOnBusCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_MessageOnBusCapability494", type=MessageType, multiplicity=Multiplicity(1, 1))
    }
)
originalResource486: BinaryAssociation = BinaryAssociation(
    name="originalResource486",
    ends={
        Property(name="Resource487", type=oaam_capabilities_ResourceConsumption, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_ResourceConsumption", type=Resource, multiplicity=Multiplicity(0, 9999))
    }
)
type488: BinaryAssociation = BinaryAssociation(
    name="type488",
    ends={
        Property(name="ResourceType490", type=oaam_capabilities_ResourceConsumption, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_ResourceConsumption489", type=ResourceType, multiplicity=Multiplicity(1, 1))
    }
)
busType491: BinaryAssociation = BinaryAssociation(
    name="busType491",
    ends={
        Property(name="BusType492", type=oaam_capabilities_MessageOnBusCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_MessageOnBusCapability", type=BusType, multiplicity=Multiplicity(1, 1))
    }
)
messageType504: BinaryAssociation = BinaryAssociation(
    name="messageType504",
    ends={
        Property(name="MessageType505", type=oaam_capabilities_SubmessageInMessageCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_SubmessageInMessageCapability", type=MessageType, multiplicity=Multiplicity(1, 1))
    }
)
messageType496: BinaryAssociation = BinaryAssociation(
    name="messageType496",
    ends={
        Property(name="MessageType497", type=oaam_capabilities_MessageOnConnectionOrDeviceCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_MessageOnConnectionOrDeviceCapability", type=MessageType, multiplicity=Multiplicity(1, 1))
    }
)
deviceType498: BinaryAssociation = BinaryAssociation(
    name="deviceType498",
    ends={
        Property(name="DeviceType500", type=oaam_capabilities_MessageOnConnectionOrDeviceCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_MessageOnConnectionOrDeviceCapability499", type=DeviceType, multiplicity=Multiplicity(0, 1))
    }
)
connectionType501: BinaryAssociation = BinaryAssociation(
    name="connectionType501",
    ends={
        Property(name="ConnectionType503", type=oaam_capabilities_MessageOnConnectionOrDeviceCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_MessageOnConnectionOrDeviceCapability502", type=ConnectionType, multiplicity=Multiplicity(0, 1))
    }
)
submessageType506: BinaryAssociation = BinaryAssociation(
    name="submessageType506",
    ends={
        Property(name="MessageType508", type=oaam_capabilities_SubmessageInMessageCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_SubmessageInMessageCapability507", type=MessageType, multiplicity=Multiplicity(1, 1))
    }
)
messageType509: BinaryAssociation = BinaryAssociation(
    name="messageType509",
    ends={
        Property(name="MessageType510", type=oaam_capabilities_SignalInMessageCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_SignalInMessageCapability", type=MessageType, multiplicity=Multiplicity(1, 1))
    }
)
signalType511: BinaryAssociation = BinaryAssociation(
    name="signalType511",
    ends={
        Property(name="SignalType513", type=oaam_capabilities_SignalInMessageCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_capabilities_SignalInMessageCapability512", type=SignalType, multiplicity=Multiplicity(1, 1))
    }
)
areaRestrictions519: BinaryAssociation = BinaryAssociation(
    name="areaRestrictions519",
    ends={
        Property(name="AreaRestriction", type=oaam_restrictions_RestrictionsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_RestrictionsContainerA520", type=AreaRestriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
powerSourceRestrictions521: BinaryAssociation = BinaryAssociation(
    name="powerSourceRestrictions521",
    ends={
        Property(name="PowerSourceRestriction", type=oaam_restrictions_RestrictionsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_RestrictionsContainerA522", type=PowerSourceRestriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deviceTypeRestrictions514: BinaryAssociation = BinaryAssociation(
    name="deviceTypeRestrictions514",
    ends={
        Property(name="DeviceTypeRestriction", type=oaam_restrictions_RestrictionsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_RestrictionsContainerA", type=DeviceTypeRestriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deviceRestrictions515: BinaryAssociation = BinaryAssociation(
    name="deviceRestrictions515",
    ends={
        Property(name="DeviceRestriction", type=oaam_restrictions_RestrictionsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_RestrictionsContainerA516", type=DeviceRestriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locationRestrictions517: BinaryAssociation = BinaryAssociation(
    name="locationRestrictions517",
    ends={
        Property(name="LocationRestriction", type=oaam_restrictions_RestrictionsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_RestrictionsContainerA518", type=LocationRestriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectionTypeRestrictions531: BinaryAssociation = BinaryAssociation(
    name="connectionTypeRestrictions531",
    ends={
        Property(name="oaam_restrictions_RestrictionsContainerA532", type=ConnectionTypeRestriction, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="ConnectionTypeRestriction", type=oaam_restrictions_RestrictionsContainerA, multiplicity=Multiplicity(1, 1))
    }
)
segregationRestrictions533: BinaryAssociation = BinaryAssociation(
    name="segregationRestrictions533",
    ends={
        Property(name="SegregationRestriction", type=oaam_restrictions_RestrictionsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_RestrictionsContainerA534", type=SegregationRestriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskAtomicRestrictions523: BinaryAssociation = BinaryAssociation(
    name="taskAtomicRestrictions523",
    ends={
        Property(name="TaskAtomicRestriction", type=oaam_restrictions_RestrictionsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_RestrictionsContainerA524", type=TaskAtomicRestriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskSymmetryRestrictions525: BinaryAssociation = BinaryAssociation(
    name="taskSymmetryRestrictions525",
    ends={
        Property(name="TaskSymmetryRestriction", type=oaam_restrictions_RestrictionsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_RestrictionsContainerA526", type=TaskSymmetryRestriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronicityRestriction527: BinaryAssociation = BinaryAssociation(
    name="synchronicityRestriction527",
    ends={
        Property(name="SynchronicityRestriction", type=oaam_restrictions_RestrictionsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_RestrictionsContainerA528", type=SynchronicityRestriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectionRestrictions529: BinaryAssociation = BinaryAssociation(
    name="connectionRestrictions529",
    ends={
        Property(name="ConnectionRestriction", type=oaam_restrictions_RestrictionsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_RestrictionsContainerA530", type=ConnectionRestriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
devices539: BinaryAssociation = BinaryAssociation(
    name="devices539",
    ends={
        Property(name="Device540", type=oaam_restrictions_DeviceRestrictionA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_DeviceRestrictionA", type=Device, multiplicity=Multiplicity(0, 1))
    }
)
subrestrictions535: BinaryAssociation = BinaryAssociation(
    name="subrestrictions535",
    ends={
        Property(name="Subrestrictions", type=oaam_restrictions_RestrictionsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_RestrictionsContainerA536", type=Subrestrictions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timeDelayRestrictions537: BinaryAssociation = BinaryAssociation(
    name="timeDelayRestrictions537",
    ends={
        Property(name="TimeDelayRestriction", type=oaam_restrictions_RestrictionsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_RestrictionsContainerA538", type=TimeDelayRestriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections541: BinaryAssociation = BinaryAssociation(
    name="connections541",
    ends={
        Property(name="Connection542", type=oaam_restrictions_ConnectionRestrinctionA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_ConnectionRestrinctionA", type=Connection, multiplicity=Multiplicity(0, 9999))
    }
)
tasks543: BinaryAssociation = BinaryAssociation(
    name="tasks543",
    ends={
        Property(name="Task544", type=oaam_restrictions_TaskRestrictionA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_TaskRestrictionA", type=Task, multiplicity=Multiplicity(0, 9999))
    }
)
signals545: BinaryAssociation = BinaryAssociation(
    name="signals545",
    ends={
        Property(name="Signal546", type=oaam_restrictions_SignalRestrictionA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_SignalRestrictionA", type=Signal, multiplicity=Multiplicity(0, 9999))
    }
)
subfunctions547: BinaryAssociation = BinaryAssociation(
    name="subfunctions547",
    ends={
        Property(name="Subfunctions548", type=oaam_restrictions_SubfunctionRestrictionA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_SubfunctionRestrictionA", type=Subfunctions, multiplicity=Multiplicity(0, 9999))
    }
)
taskGroups549: BinaryAssociation = BinaryAssociation(
    name="taskGroups549",
    ends={
        Property(name="TaskGroup550", type=oaam_restrictions_TaskGroupRestrictionA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_TaskGroupRestrictionA", type=TaskGroup, multiplicity=Multiplicity(0, 9999))
    }
)
signalGroups551: BinaryAssociation = BinaryAssociation(
    name="signalGroups551",
    ends={
        Property(name="SignalGroup552", type=oaam_restrictions_SignalGroupRestrictionA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_SignalGroupRestrictionA", type=SignalGroup, multiplicity=Multiplicity(0, 9999))
    }
)
locations553: BinaryAssociation = BinaryAssociation(
    name="locations553",
    ends={
        Property(name="Location554", type=oaam_restrictions_LocationRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_LocationRestriction", type=Location, multiplicity=Multiplicity(0, 9999))
    }
)
devices559: BinaryAssociation = BinaryAssociation(
    name="devices559",
    ends={
        Property(name="Device560", type=oaam_restrictions_DeviceRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_DeviceRestriction", type=Device, multiplicity=Multiplicity(0, 9999))
    }
)
areas555: BinaryAssociation = BinaryAssociation(
    name="areas555",
    ends={
        Property(name="Area556", type=oaam_restrictions_AreaRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_AreaRestriction", type=Area, multiplicity=Multiplicity(0, 9999))
    }
)
powerSources557: BinaryAssociation = BinaryAssociation(
    name="powerSources557",
    ends={
        Property(name="PowerSource558", type=oaam_restrictions_PowerSourceRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_PowerSourceRestriction", type=PowerSource, multiplicity=Multiplicity(0, 9999))
    }
)
connections565: BinaryAssociation = BinaryAssociation(
    name="connections565",
    ends={
        Property(name="Connection566", type=oaam_restrictions_ConnectionRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_ConnectionRestriction", type=Connection, multiplicity=Multiplicity(0, 9999))
    }
)
tasksA567: BinaryAssociation = BinaryAssociation(
    name="tasksA567",
    ends={
        Property(name="Task568", type=oaam_restrictions_SegregationRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_SegregationRestriction", type=Task, multiplicity=Multiplicity(1, 9999))
    }
)
deviceTypes561: BinaryAssociation = BinaryAssociation(
    name="deviceTypes561",
    ends={
        Property(name="DeviceType562", type=oaam_restrictions_DeviceTypeRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_DeviceTypeRestriction", type=DeviceType, multiplicity=Multiplicity(0, 9999))
    }
)
connectionTypes563: BinaryAssociation = BinaryAssociation(
    name="connectionTypes563",
    ends={
        Property(name="ConnectionType564", type=oaam_restrictions_ConnectionTypeRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_ConnectionTypeRestriction", type=ConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
signalsA577: BinaryAssociation = BinaryAssociation(
    name="signalsA577",
    ends={
        Property(name="Signal579", type=oaam_restrictions_SegregationRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_SegregationRestriction578", type=Signal, multiplicity=Multiplicity(0, 9999))
    }
)
signalsB580: BinaryAssociation = BinaryAssociation(
    name="signalsB580",
    ends={
        Property(name="Signal582", type=oaam_restrictions_SegregationRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_SegregationRestriction581", type=Signal, multiplicity=Multiplicity(0, 9999))
    }
)
tasksB569: BinaryAssociation = BinaryAssociation(
    name="tasksB569",
    ends={
        Property(name="Task571", type=oaam_restrictions_SegregationRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_SegregationRestriction570", type=Task, multiplicity=Multiplicity(1, 9999))
    }
)
subfunctionsA572: BinaryAssociation = BinaryAssociation(
    name="subfunctionsA572",
    ends={
        Property(name="FunctionsContainerA", type=oaam_restrictions_SegregationRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_SegregationRestriction573", type=FunctionsContainerA, multiplicity=Multiplicity(0, 9999))
    }
)
subfunctionsB574: BinaryAssociation = BinaryAssociation(
    name="subfunctionsB574",
    ends={
        Property(name="FunctionsContainerA576", type=oaam_restrictions_SegregationRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_SegregationRestriction575", type=FunctionsContainerA, multiplicity=Multiplicity(0, 9999))
    }
)
devicesA595: BinaryAssociation = BinaryAssociation(
    name="devicesA595",
    ends={
        Property(name="Device597", type=oaam_restrictions_SegregationRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_SegregationRestriction596", type=Device, multiplicity=Multiplicity(0, 9999))
    }
)
devicesB598: BinaryAssociation = BinaryAssociation(
    name="devicesB598",
    ends={
        Property(name="Device600", type=oaam_restrictions_SegregationRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_SegregationRestriction599", type=Device, multiplicity=Multiplicity(0, 9999))
    }
)
connectionsA601: BinaryAssociation = BinaryAssociation(
    name="connectionsA601",
    ends={
        Property(name="Connection603", type=oaam_restrictions_SegregationRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_SegregationRestriction602", type=Connection, multiplicity=Multiplicity(0, 9999))
    }
)
taskGroupsA583: BinaryAssociation = BinaryAssociation(
    name="taskGroupsA583",
    ends={
        Property(name="TaskGroup585", type=oaam_restrictions_SegregationRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_SegregationRestriction584", type=TaskGroup, multiplicity=Multiplicity(0, 9999))
    }
)
taskGroupsB586: BinaryAssociation = BinaryAssociation(
    name="taskGroupsB586",
    ends={
        Property(name="TaskGroup588", type=oaam_restrictions_SegregationRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_SegregationRestriction587", type=TaskGroup, multiplicity=Multiplicity(0, 9999))
    }
)
signalGroupsB589: BinaryAssociation = BinaryAssociation(
    name="signalGroupsB589",
    ends={
        Property(name="SignalGroup591", type=oaam_restrictions_SegregationRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_SegregationRestriction590", type=SignalGroup, multiplicity=Multiplicity(0, 9999))
    }
)
signalGroupsA592: BinaryAssociation = BinaryAssociation(
    name="signalGroupsA592",
    ends={
        Property(name="SignalGroup594", type=oaam_restrictions_SegregationRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_SegregationRestriction593", type=SignalGroup, multiplicity=Multiplicity(0, 9999))
    }
)
connectionsB604: BinaryAssociation = BinaryAssociation(
    name="connectionsB604",
    ends={
        Property(name="Connection606", type=oaam_restrictions_SegregationRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_SegregationRestriction605", type=Connection, multiplicity=Multiplicity(0, 9999))
    }
)
startTask607: BinaryAssociation = BinaryAssociation(
    name="startTask607",
    ends={
        Property(name="Task608", type=oaam_restrictions_TimeDelayRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_TimeDelayRestriction", type=Task, multiplicity=Multiplicity(1, 1))
    }
)
endTask609: BinaryAssociation = BinaryAssociation(
    name="endTask609",
    ends={
        Property(name="Task611", type=oaam_restrictions_TimeDelayRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_restrictions_TimeDelayRestriction610", type=Task, multiplicity=Multiplicity(1, 1))
    }
)
signalAssignments619: BinaryAssociation = BinaryAssociation(
    name="signalAssignments619",
    ends={
        Property(name="SignalAssignment", type=oaam_allocations_AllocationsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_AllocationsContainerA620", type=SignalAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
suballocations621: BinaryAssociation = BinaryAssociation(
    name="suballocations621",
    ends={
        Property(name="Suballocations", type=oaam_allocations_AllocationsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_AllocationsContainerA622", type=Suballocations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subconnectionAssignments623: BinaryAssociation = BinaryAssociation(
    name="subconnectionAssignments623",
    ends={
        Property(name="SubconnectionAssignment", type=oaam_allocations_AllocationsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_AllocationsContainerA624", type=SubconnectionAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deviceAssignments612: BinaryAssociation = BinaryAssociation(
    name="deviceAssignments612",
    ends={
        Property(name="DeviceAssignment", type=oaam_allocations_AllocationsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_AllocationsContainerA", type=DeviceAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subdeviceAssignments613: BinaryAssociation = BinaryAssociation(
    name="subdeviceAssignments613",
    ends={
        Property(name="SubdeviceAssignment", type=oaam_allocations_AllocationsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_AllocationsContainerA614", type=SubdeviceAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectionAssignments615: BinaryAssociation = BinaryAssociation(
    name="connectionAssignments615",
    ends={
        Property(name="ConnectionAssignment", type=oaam_allocations_AllocationsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_AllocationsContainerA616", type=ConnectionAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskAssignments617: BinaryAssociation = BinaryAssociation(
    name="taskAssignments617",
    ends={
        Property(name="TaskAssignment", type=oaam_allocations_AllocationsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_AllocationsContainerA618", type=TaskAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
device632: BinaryAssociation = BinaryAssociation(
    name="device632",
    ends={
        Property(name="Device634", type=oaam_allocations_TaskAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_TaskAssignment633", type=Device, multiplicity=Multiplicity(1, 1))
    }
)
schedules635: BinaryAssociation = BinaryAssociation(
    name="schedules635",
    ends={
        Property(name="Schedule", type=oaam_allocations_TaskAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_TaskAssignment636", type=Schedule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messages625: BinaryAssociation = BinaryAssociation(
    name="messages625",
    ends={
        Property(name="Message", type=oaam_allocations_AllocationsContainerA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_AllocationsContainerA626", type=Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
capability627: BinaryAssociation = BinaryAssociation(
    name="capability627",
    ends={
        Property(name="TaskOnDeviceCapability628", type=oaam_allocations_TaskAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_TaskAssignment", type=TaskOnDeviceCapability, multiplicity=Multiplicity(1, 1))
    }
)
task629: BinaryAssociation = BinaryAssociation(
    name="task629",
    ends={
        Property(name="Task631", type=oaam_allocations_TaskAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_TaskAssignment630", type=Task, multiplicity=Multiplicity(1, 1))
    }
)
connection642: BinaryAssociation = BinaryAssociation(
    name="connection642",
    ends={
        Property(name="Connection644", type=oaam_allocations_ConnectionAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_ConnectionAssignment643", type=Connection, multiplicity=Multiplicity(1, 1))
    }
)
capability645: BinaryAssociation = BinaryAssociation(
    name="capability645",
    ends={
        Property(name="SignalOnConnectionOrDeviceCapability646", type=oaam_allocations_SignalAssignmentSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_SignalAssignmentSegment", type=SignalOnConnectionOrDeviceCapability, multiplicity=Multiplicity(1, 1))
    }
)
segments637: BinaryAssociation = BinaryAssociation(
    name="segments637",
    ends={
        Property(name="SignalAssignmentSegment", type=oaam_allocations_SignalAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_SignalAssignment", type=SignalAssignmentSegment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signal638: BinaryAssociation = BinaryAssociation(
    name="signal638",
    ends={
        Property(name="Signal640", type=oaam_allocations_SignalAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_SignalAssignment639", type=Signal, multiplicity=Multiplicity(1, 1))
    }
)
segments641: BinaryAssociation = BinaryAssociation(
    name="segments641",
    ends={
        Property(name="ConnectionAssignmentSegment", type=oaam_allocations_ConnectionAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_ConnectionAssignment", type=ConnectionAssignmentSegment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
device656: BinaryAssociation = BinaryAssociation(
    name="device656",
    ends={
        Property(name="Device657", type=oaam_allocations_DeviceAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_DeviceAssignment", type=Device, multiplicity=Multiplicity(1, 1))
    }
)
location658: BinaryAssociation = BinaryAssociation(
    name="location658",
    ends={
        Property(name="Location660", type=oaam_allocations_DeviceAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_DeviceAssignment659", type=Location, multiplicity=Multiplicity(1, 1))
    }
)
capability661: BinaryAssociation = BinaryAssociation(
    name="capability661",
    ends={
        Property(name="DeviceInLocationCapability663", type=oaam_allocations_DeviceAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_DeviceAssignment662", type=DeviceInLocationCapability, multiplicity=Multiplicity(1, 1))
    }
)
device647: BinaryAssociation = BinaryAssociation(
    name="device647",
    ends={
        Property(name="Device649", type=oaam_allocations_SignalAssignmentSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_SignalAssignmentSegment648", type=Device, multiplicity=Multiplicity(0, 1))
    }
)
connection650: BinaryAssociation = BinaryAssociation(
    name="connection650",
    ends={
        Property(name="Connection652", type=oaam_allocations_SignalAssignmentSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_SignalAssignmentSegment651", type=Connection, multiplicity=Multiplicity(0, 1))
    }
)
schedules653: BinaryAssociation = BinaryAssociation(
    name="schedules653",
    ends={
        Property(name="Schedule655", type=oaam_allocations_SignalAssignmentSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_SignalAssignmentSegment654", type=Schedule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
capability672: BinaryAssociation = BinaryAssociation(
    name="capability672",
    ends={
        Property(name="SubdeviceInDeviceCapability673", type=oaam_allocations_SubdeviceAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_SubdeviceAssignment", type=SubdeviceInDeviceCapability, multiplicity=Multiplicity(1, 1))
    }
)
subdevice674: BinaryAssociation = BinaryAssociation(
    name="subdevice674",
    ends={
        Property(name="Device676", type=oaam_allocations_SubdeviceAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_SubdeviceAssignment675", type=Device, multiplicity=Multiplicity(1, 1))
    }
)
capability664: BinaryAssociation = BinaryAssociation(
    name="capability664",
    ends={
        Property(name="ConnectionInDuctOrLocationCapability665", type=oaam_allocations_ConnectionAssignmentSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_ConnectionAssignmentSegment", type=ConnectionInDuctOrLocationCapability, multiplicity=Multiplicity(1, 1))
    }
)
location666: BinaryAssociation = BinaryAssociation(
    name="location666",
    ends={
        Property(name="Location668", type=oaam_allocations_ConnectionAssignmentSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_ConnectionAssignmentSegment667", type=Location, multiplicity=Multiplicity(0, 1))
    }
)
duct669: BinaryAssociation = BinaryAssociation(
    name="duct669",
    ends={
        Property(name="Duct671", type=oaam_allocations_ConnectionAssignmentSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_ConnectionAssignmentSegment670", type=Duct, multiplicity=Multiplicity(0, 1))
    }
)
targetDevice685: BinaryAssociation = BinaryAssociation(
    name="targetDevice685",
    ends={
        Property(name="Device687", type=oaam_allocations_SubconnectionAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_SubconnectionAssignment686", type=Device, multiplicity=Multiplicity(1, 1))
    }
)
targetDevice677: BinaryAssociation = BinaryAssociation(
    name="targetDevice677",
    ends={
        Property(name="Device679", type=oaam_allocations_SubdeviceAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_SubdeviceAssignment678", type=Device, multiplicity=Multiplicity(1, 1))
    }
)
capability680: BinaryAssociation = BinaryAssociation(
    name="capability680",
    ends={
        Property(name="SubconnectionInDeviceCapability681", type=oaam_allocations_SubconnectionAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_SubconnectionAssignment", type=SubconnectionInDeviceCapability, multiplicity=Multiplicity(1, 1))
    }
)
subconnection682: BinaryAssociation = BinaryAssociation(
    name="subconnection682",
    ends={
        Property(name="Connection684", type=oaam_allocations_SubconnectionAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_SubconnectionAssignment683", type=Connection, multiplicity=Multiplicity(1, 1))
    }
)
schedules689: BinaryAssociation = BinaryAssociation(
    name="schedules689",
    ends={
        Property(name="Schedule690", type=oaam_allocations_MessageA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_MessageA", type=Schedule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scheduledTimes688: BinaryAssociation = BinaryAssociation(
    name="scheduledTimes688",
    ends={
        Property(name="ScheduledTime", type=oaam_allocations_Schedule, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_Schedule", type=ScheduledTime, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
segments695: BinaryAssociation = BinaryAssociation(
    name="segments695",
    ends={
        Property(name="MessageSegment", type=oaam_allocations_MessageA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_MessageA696", type=MessageSegment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type697: BinaryAssociation = BinaryAssociation(
    name="type697",
    ends={
        Property(name="MessageType699", type=oaam_allocations_MessageA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_MessageA698", type=MessageType, multiplicity=Multiplicity(0, 1))
    }
)
submessages691: BinaryAssociation = BinaryAssociation(
    name="submessages691",
    ends={
        Property(name="Submessage", type=oaam_allocations_MessageA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_MessageA692", type=Submessage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bus710: BinaryAssociation = BinaryAssociation(
    name="bus710",
    ends={
        Property(name="Bus712", type=oaam_allocations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_Message711", type=Bus, multiplicity=Multiplicity(1, 1))
    }
)
signalToMessageAssignments693: BinaryAssociation = BinaryAssociation(
    name="signalToMessageAssignments693",
    ends={
        Property(name="SignalToMessageAssignment", type=oaam_allocations_MessageA, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_MessageA694", type=SignalToMessageAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceDevices713: BinaryAssociation = BinaryAssociation(
    name="sourceDevices713",
    ends={
        Property(name="Device715", type=oaam_allocations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_Message714", type=Device, multiplicity=Multiplicity(0, 9999))
    }
)
destinationDevices716: BinaryAssociation = BinaryAssociation(
    name="destinationDevices716",
    ends={
        Property(name="Device718", type=oaam_allocations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_Message717", type=Device, multiplicity=Multiplicity(0, 9999))
    }
)
capability700: BinaryAssociation = BinaryAssociation(
    name="capability700",
    ends={
        Property(name="MessageOnConnectionOrDeviceCapability701", type=oaam_allocations_MessageSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_MessageSegment", type=MessageOnConnectionOrDeviceCapability, multiplicity=Multiplicity(1, 1))
    }
)
device702: BinaryAssociation = BinaryAssociation(
    name="device702",
    ends={
        Property(name="Device704", type=oaam_allocations_MessageSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_MessageSegment703", type=Device, multiplicity=Multiplicity(0, 1))
    }
)
connection705: BinaryAssociation = BinaryAssociation(
    name="connection705",
    ends={
        Property(name="Connection707", type=oaam_allocations_MessageSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_MessageSegment706", type=Connection, multiplicity=Multiplicity(0, 1))
    }
)
capability708: BinaryAssociation = BinaryAssociation(
    name="capability708",
    ends={
        Property(name="MessageOnBusCapability709", type=oaam_allocations_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_Message", type=MessageOnBusCapability, multiplicity=Multiplicity(1, 1))
    }
)
operationModes729: BinaryAssociation = BinaryAssociation(
    name="operationModes729",
    ends={
        Property(name="OperationModeReference731", type=oaam_allocations_SignalToMessageAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_SignalToMessageAssignment730", type=OperationModeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataType732: BinaryAssociation = BinaryAssociation(
    name="dataType732",
    ends={
        Property(name="DataTypeA734", type=oaam_allocations_SignalToMessageAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_SignalToMessageAssignment733", type=DataTypeA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capability719: BinaryAssociation = BinaryAssociation(
    name="capability719",
    ends={
        Property(name="SubmessageInMessageCapability720", type=oaam_allocations_Submessage, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_Submessage", type=SubmessageInMessageCapability, multiplicity=Multiplicity(1, 1))
    }
)
signal721: BinaryAssociation = BinaryAssociation(
    name="signal721",
    ends={
        Property(name="Signal722", type=oaam_allocations_SignalToMessageAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_SignalToMessageAssignment", type=Signal, multiplicity=Multiplicity(1, 1))
    }
)
attributes723: BinaryAssociation = BinaryAssociation(
    name="attributes723",
    ends={
        Property(name="AttributeA725", type=oaam_allocations_SignalToMessageAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_SignalToMessageAssignment724", type=AttributeA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variants726: BinaryAssociation = BinaryAssociation(
    name="variants726",
    ends={
        Property(name="Variant728", type=oaam_allocations_SignalToMessageAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_SignalToMessageAssignment727", type=Variant, multiplicity=Multiplicity(0, 9999))
    }
)
capability735: BinaryAssociation = BinaryAssociation(
    name="capability735",
    ends={
        Property(name="SignalInMessageCapability737", type=oaam_allocations_SignalToMessageAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="oaam_allocations_SignalToMessageAssignment736", type=SignalInMessageCapability, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_oaam_Architecture_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_Architecture)
gen_oaam_common_AttributeA_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_common_AttributeA)
gen_oaam_common_AttributeString_AttributeA = Generalization(general=AttributeA, specific=oaam_common_AttributeString)
gen_oaam_common_BoolOperation_common_BoolA = Generalization(general=common_BoolA, specific=oaam_common_BoolOperation)
gen_oaam_common_BoolOperation_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_common_BoolOperation)
gen_oaam_common_AttributeNumeric_AttributeA = Generalization(general=AttributeA, specific=oaam_common_AttributeNumeric)
gen_oaam_common_AttributeContainment_AttributeA = Generalization(general=AttributeA, specific=oaam_common_AttributeContainment)
gen_oaam_common_AttributeReference_AttributeA = Generalization(general=AttributeA, specific=oaam_common_AttributeReference)
gen_oaam_common_Array_DataTypeA = Generalization(general=DataTypeA, specific=oaam_common_Array)
gen_oaam_common_BoolNot_common_BoolA = Generalization(general=common_BoolA, specific=oaam_common_BoolNot)
gen_oaam_common_BoolNot_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_common_BoolNot)
gen_oaam_common_DataTypeA_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_common_DataTypeA)
gen_oaam_common_Integer_DataTypeA = Generalization(general=DataTypeA, specific=oaam_common_Integer)
gen_oaam_common_FloatingPoint_DataTypeA = Generalization(general=DataTypeA, specific=oaam_common_FloatingPoint)
gen_oaam_common_Struct_DataTypeA = Generalization(general=DataTypeA, specific=oaam_common_Struct)
gen_oaam_common_Boolean_DataTypeA = Generalization(general=DataTypeA, specific=oaam_common_Boolean)
gen_oaam_common_Byte_DataTypeA = Generalization(general=DataTypeA, specific=oaam_common_Byte)
gen_oaam_common_Character_DataTypeA = Generalization(general=DataTypeA, specific=oaam_common_Character)
gen_oaam_library_LibraryContainerA_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_LibraryContainerA)
gen_oaam_library_Resource_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_Resource)
gen_oaam_library_ResourceType_library_ResourceConsumerA = Generalization(general=library_ResourceConsumerA, specific=oaam_library_ResourceType)
gen_oaam_library_ResourceType_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_library_ResourceType)
gen_oaam_library_ResourceAlternatives_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_ResourceAlternatives)
gen_oaam_library_ResourceBundle_library_ResourceConsumerA = Generalization(general=library_ResourceConsumerA, specific=oaam_library_ResourceBundle)
gen_oaam_library_ResourceBundle_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_library_ResourceBundle)
gen_oaam_library_TaskType_library_ResourceConsumerA = Generalization(general=library_ResourceConsumerA, specific=oaam_library_TaskType)
gen_oaam_library_TaskType_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_library_TaskType)
gen_oaam_library_SignalType_library_ResourceConsumerA = Generalization(general=library_ResourceConsumerA, specific=oaam_library_SignalType)
gen_oaam_library_SignalType_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_library_SignalType)
gen_oaam_library_DeviceType_library_ResourceConsumerA = Generalization(general=library_ResourceConsumerA, specific=oaam_library_DeviceType)
gen_oaam_library_DeviceType_library_ResourceProviderA = Generalization(general=library_ResourceProviderA, specific=oaam_library_DeviceType)
gen_oaam_library_DeviceType_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_library_DeviceType)
gen_oaam_library_ConnectionType_library_ResourceProviderA = Generalization(general=library_ResourceProviderA, specific=oaam_library_ConnectionType)
gen_oaam_library_ConnectionType_library_ResourceConsumerA = Generalization(general=library_ResourceConsumerA, specific=oaam_library_ConnectionType)
gen_oaam_library_ConnectionType_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_library_ConnectionType)
gen_oaam_library_LocationType_library_ResourceProviderA = Generalization(general=library_ResourceProviderA, specific=oaam_library_LocationType)
gen_oaam_library_LocationType_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_library_LocationType)
gen_oaam_library_IoType_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_IoType)
gen_oaam_library_DuctType_library_ResourceProviderA = Generalization(general=library_ResourceProviderA, specific=oaam_library_DuctType)
gen_oaam_library_DuctType_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_library_DuctType)
gen_oaam_library_WireType_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_WireType)
gen_oaam_library_InputDeclaration_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_InputDeclaration)
gen_oaam_library_OutputDeclaration_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_OutputDeclaration)
gen_oaam_library_ResourceGroup_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_ResourceGroup)
gen_oaam_library_DeviceTypeSymmetry_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_DeviceTypeSymmetry)
gen_oaam_library_IoDeclaration_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_IoDeclaration)
gen_oaam_library_DuctOpeningDeclaration_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_DuctOpeningDeclaration)
gen_oaam_library_IoGroup_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_IoGroup)
gen_oaam_library_AttributeDefinition_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_AttributeDefinition)
gen_oaam_library_FaultPropagation_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_FaultPropagation)
gen_oaam_library_ResourceTypeModifier_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_ResourceTypeModifier)
gen_oaam_library_TaskInputState_common_BoolA = Generalization(general=common_BoolA, specific=oaam_library_TaskInputState)
gen_oaam_library_TaskInputState_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_library_TaskInputState)
gen_oaam_library_PowerSource_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_PowerSource)
gen_oaam_library_ResourceLink_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_ResourceLink)
gen_oaam_library_TaskTypeDissimilarity_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_TaskTypeDissimilarity)
gen_oaam_library_ResourceTypeModifierLevel_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_library_ResourceTypeModifierLevel)
gen_oaam_library_ResourceTypeModifierLevel_library_ResourceConsumerA = Generalization(general=library_ResourceConsumerA, specific=oaam_library_ResourceTypeModifierLevel)
gen_oaam_library_ResourceTypeModifierReference_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_ResourceTypeModifierReference)
gen_oaam_library_TaskOutputTrigger_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_TaskOutputTrigger)
gen_oaam_library_DeviceTypeDissimilarity_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_DeviceTypeDissimilarity)
gen_oaam_library_ResourceTypeDissimilarity_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_ResourceTypeDissimilarity)
gen_oaam_library_TaskInputTrigger_common_BoolA = Generalization(general=common_BoolA, specific=oaam_library_TaskInputTrigger)
gen_oaam_library_TaskInputTrigger_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_library_TaskInputTrigger)
gen_oaam_library_BusType_library_ResourceProviderA = Generalization(general=library_ResourceProviderA, specific=oaam_library_BusType)
gen_oaam_library_BusType_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_library_BusType)
gen_oaam_library_TaskStateDeclaration_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_TaskStateDeclaration)
gen_oaam_library_TaskParameterDeclaration_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_library_TaskParameterDeclaration)
gen_oaam_library_MessageType_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_library_MessageType)
gen_oaam_library_MessageType_library_ResourceConsumerA = Generalization(general=library_ResourceConsumerA, specific=oaam_library_MessageType)
gen_oaam_library_MessageType_library_ResourceProviderA = Generalization(general=library_ResourceProviderA, specific=oaam_library_MessageType)
gen_oaam_library_Library_LibraryContainerA = Generalization(general=LibraryContainerA, specific=oaam_library_Library)
gen_oaam_library_Sublibrary_LibraryContainerA = Generalization(general=LibraryContainerA, specific=oaam_library_Sublibrary)
gen_oaam_scenario_ScenarioParameterA_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_scenario_ScenarioParameterA)
gen_oaam_scenario_ScenarioParameterA_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_scenario_ScenarioParameterA)
gen_oaam_scenario_OperationMode_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_scenario_OperationMode)
gen_oaam_scenario_OperationMode_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_scenario_OperationMode)
gen_oaam_scenario_ScenarioParameterNumeric_scenario_ScenarioParameterA = Generalization(general=scenario_ScenarioParameterA, specific=oaam_scenario_ScenarioParameterNumeric)
gen_oaam_scenario_ScenarioParameterNumeric_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_scenario_ScenarioParameterNumeric)
gen_oaam_scenario_ScenarioContainerA_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_scenario_ScenarioContainerA)
gen_oaam_scenario_Scenario_ScenarioContainerA = Generalization(general=ScenarioContainerA, specific=oaam_scenario_Scenario)
gen_oaam_scenario_Subscenario_ScenarioContainerA = Generalization(general=ScenarioContainerA, specific=oaam_scenario_Subscenario)
gen_oaam_scenario_ScenarioParameterBool_scenario_ScenarioParameterA = Generalization(general=scenario_ScenarioParameterA, specific=oaam_scenario_ScenarioParameterBool)
gen_oaam_scenario_ScenarioParameterBool_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_scenario_ScenarioParameterBool)
gen_oaam_scenario_Variant_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_scenario_Variant)
gen_oaam_scenario_Variant_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_scenario_Variant)
gen_oaam_scenario_OperationModeReference_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_scenario_OperationModeReference)
gen_oaam_systems_Systems_SystemsContainerA = Generalization(general=SystemsContainerA, specific=oaam_systems_Systems)
gen_oaam_systems_Subsystem_systems_SystemsContainerA = Generalization(general=systems_SystemsContainerA, specific=oaam_systems_Subsystem)
gen_oaam_systems_Subsystem_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_systems_Subsystem)
gen_oaam_systems_Subsystem_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_systems_Subsystem)
gen_oaam_systems_SystemsContainerA_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_systems_SystemsContainerA)
gen_oaam_systems_InformationFlow_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_systems_InformationFlow)
gen_oaam_systems_InformationFlow_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_systems_InformationFlow)
gen_oaam_systems_System_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_systems_System)
gen_oaam_systems_System_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_systems_System)
gen_oaam_systems_System_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_systems_System)
gen_oaam_systems_InformationFlow_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_systems_InformationFlow)
gen_oaam_systems_InformationMaterial_systems_ProvidedInformationA = Generalization(general=systems_ProvidedInformationA, specific=oaam_systems_InformationMaterial)
gen_oaam_systems_InformationMaterial_systems_RequiredInformationA = Generalization(general=systems_RequiredInformationA, specific=oaam_systems_InformationMaterial)
gen_oaam_systems_InformationMaterial_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_systems_InformationMaterial)
gen_oaam_systems_InformationMaterial_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_systems_InformationMaterial)
gen_oaam_systems_InformationMaterial_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_systems_InformationMaterial)
gen_oaam_systems_InformationSignal_systems_ProvidedInformationA = Generalization(general=systems_ProvidedInformationA, specific=oaam_systems_InformationSignal)
gen_oaam_systems_InformationSignal_systems_RequiredInformationA = Generalization(general=systems_RequiredInformationA, specific=oaam_systems_InformationSignal)
gen_oaam_systems_InformationSignal_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_systems_InformationSignal)
gen_oaam_systems_InformationSignal_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_systems_InformationSignal)
gen_oaam_systems_InformationSignal_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_systems_InformationSignal)
gen_oaam_systems_HydraulicPower_InformationPower = Generalization(general=InformationPower, specific=oaam_systems_HydraulicPower)
gen_oaam_systems_InformationPower_systems_ProvidedInformationA = Generalization(general=systems_ProvidedInformationA, specific=oaam_systems_InformationPower)
gen_oaam_systems_InformationPower_systems_RequiredInformationA = Generalization(general=systems_RequiredInformationA, specific=oaam_systems_InformationPower)
gen_oaam_systems_InformationPower_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_systems_InformationPower)
gen_oaam_systems_InformationPower_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_systems_InformationPower)
gen_oaam_systems_InformationPower_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_systems_InformationPower)
gen_oaam_systems_ElectricPower_InformationPower = Generalization(general=InformationPower, specific=oaam_systems_ElectricPower)
gen_oaam_systems_RotaryPower_InformationPower = Generalization(general=InformationPower, specific=oaam_systems_RotaryPower)
gen_oaam_systems_LinearPower_InformationPower = Generalization(general=InformationPower, specific=oaam_systems_LinearPower)
gen_oaam_systems_InputSegregation_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_systems_InputSegregation)
gen_oaam_functions_Functions_FunctionsContainerA = Generalization(general=FunctionsContainerA, specific=oaam_functions_Functions)
gen_oaam_functions_FunctionsContainerA_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_functions_FunctionsContainerA)
gen_oaam_functions_FunctionsContainerA_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_functions_FunctionsContainerA)
gen_oaam_functions_FunctionsContainerA_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_functions_FunctionsContainerA)
gen_oaam_functions_Task_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_functions_Task)
gen_oaam_functions_Task_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_functions_Task)
gen_oaam_functions_Task_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_functions_Task)
gen_oaam_functions_ExternalTaskLink_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_functions_ExternalTaskLink)
gen_oaam_functions_ExternalTaskLink_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_functions_ExternalTaskLink)
gen_oaam_functions_ExternalTaskLink_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_functions_ExternalTaskLink)
gen_oaam_functions_TaskGroup_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_functions_TaskGroup)
gen_oaam_functions_TaskGroup_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_functions_TaskGroup)
gen_oaam_functions_TaskGroup_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_functions_TaskGroup)
gen_oaam_functions_TaskSymmetry_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_functions_TaskSymmetry)
gen_oaam_functions_TaskSymmetry_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_functions_TaskSymmetry)
gen_oaam_functions_TaskSymmetry_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_functions_TaskSymmetry)
gen_oaam_functions_FailureCondition_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_functions_FailureCondition)
gen_oaam_functions_FailureCondition_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_functions_FailureCondition)
gen_oaam_functions_FailureCondition_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_functions_FailureCondition)
gen_oaam_functions_TaskRedundancy_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_functions_TaskRedundancy)
gen_oaam_functions_TaskRedundancy_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_functions_TaskRedundancy)
gen_oaam_functions_TaskRedundancy_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_functions_TaskRedundancy)
gen_oaam_functions_OutputIntegrityState_common_BoolA = Generalization(general=common_BoolA, specific=oaam_functions_OutputIntegrityState)
gen_oaam_functions_OutputIntegrityState_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_functions_OutputIntegrityState)
gen_oaam_functions_OutputIntegrityState_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_functions_OutputIntegrityState)
gen_oaam_functions_OutputIntegrityState_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_functions_OutputIntegrityState)
gen_oaam_functions_Signal_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_functions_Signal)
gen_oaam_functions_Signal_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_functions_Signal)
gen_oaam_functions_Signal_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_functions_Signal)
gen_oaam_functions_Input_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_functions_Input)
gen_oaam_functions_Input_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_functions_Input)
gen_oaam_functions_Input_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_functions_Input)
gen_oaam_functions_SignalGroup_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_functions_SignalGroup)
gen_oaam_functions_SignalGroup_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_functions_SignalGroup)
gen_oaam_functions_SignalGroup_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_functions_SignalGroup)
gen_oaam_functions_Output_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_functions_Output)
gen_oaam_functions_Output_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_functions_Output)
gen_oaam_functions_Output_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_functions_Output)
gen_oaam_functions_Subfunctions_FunctionsContainerA = Generalization(general=FunctionsContainerA, specific=oaam_functions_Subfunctions)
gen_oaam_functions_ExternalOutputLink_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_functions_ExternalOutputLink)
gen_oaam_functions_ExternalOutputLink_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_functions_ExternalOutputLink)
gen_oaam_functions_ExternalOutputLink_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_functions_ExternalOutputLink)
gen_oaam_functions_TaskParameter_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_functions_TaskParameter)
gen_oaam_hardware_HardwareContainerA_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_hardware_HardwareContainerA)
gen_oaam_hardware_Device_library_ResourceProviderInstanceA = Generalization(general=library_ResourceProviderInstanceA, specific=oaam_hardware_Device)
gen_oaam_hardware_Device_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_hardware_Device)
gen_oaam_hardware_Device_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_hardware_Device)
gen_oaam_hardware_Device_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_hardware_Device)
gen_oaam_hardware_Connection_library_ResourceProviderInstanceA = Generalization(general=library_ResourceProviderInstanceA, specific=oaam_hardware_Connection)
gen_oaam_hardware_Connection_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_hardware_Connection)
gen_oaam_hardware_Connection_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_hardware_Connection)
gen_oaam_hardware_Connection_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_hardware_Connection)
gen_oaam_hardware_Hardware_hardware_HardwareContainerA = Generalization(general=hardware_HardwareContainerA, specific=oaam_hardware_Hardware)
gen_oaam_hardware_Hardware_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_hardware_Hardware)
gen_oaam_hardware_Hardware_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_hardware_Hardware)
gen_oaam_hardware_Io_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_hardware_Io)
gen_oaam_hardware_Io_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_hardware_Io)
gen_oaam_hardware_Io_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_hardware_Io)
gen_oaam_hardware_DeviceSymmetry_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_hardware_DeviceSymmetry)
gen_oaam_hardware_DeviceSymmetry_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_hardware_DeviceSymmetry)
gen_oaam_hardware_DeviceSymmetry_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_hardware_DeviceSymmetry)
gen_oaam_anatomy_AnatomyContainerA_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_anatomy_AnatomyContainerA)
gen_oaam_hardware_Subhardware_hardware_HardwareContainerA = Generalization(general=hardware_HardwareContainerA, specific=oaam_hardware_Subhardware)
gen_oaam_hardware_Subhardware_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_hardware_Subhardware)
gen_oaam_hardware_Subhardware_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_hardware_Subhardware)
gen_oaam_hardware_Bus_library_ResourceProviderInstanceA = Generalization(general=library_ResourceProviderInstanceA, specific=oaam_hardware_Bus)
gen_oaam_hardware_Bus_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_hardware_Bus)
gen_oaam_hardware_Bus_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_hardware_Bus)
gen_oaam_hardware_Bus_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_hardware_Bus)
gen_oaam_anatomy_Location_library_ResourceProviderInstanceA = Generalization(general=library_ResourceProviderInstanceA, specific=oaam_anatomy_Location)
gen_oaam_anatomy_Location_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_anatomy_Location)
gen_oaam_anatomy_Location_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_anatomy_Location)
gen_oaam_anatomy_Location_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_anatomy_Location)
gen_oaam_anatomy_Area_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_anatomy_Area)
gen_oaam_anatomy_Area_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_anatomy_Area)
gen_oaam_anatomy_Area_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_anatomy_Area)
gen_oaam_anatomy_Duct_library_ResourceProviderInstanceA = Generalization(general=library_ResourceProviderInstanceA, specific=oaam_anatomy_Duct)
gen_oaam_anatomy_Duct_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_anatomy_Duct)
gen_oaam_anatomy_Duct_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_anatomy_Duct)
gen_oaam_anatomy_Duct_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_anatomy_Duct)
gen_oaam_anatomy_Position3D_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_anatomy_Position3D)
gen_oaam_anatomy_DuctOpening_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_anatomy_DuctOpening)
gen_oaam_anatomy_DuctOpening_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_anatomy_DuctOpening)
gen_oaam_anatomy_DuctOpening_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_anatomy_DuctOpening)
gen_oaam_anatomy_Position3D_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_anatomy_Position3D)
gen_oaam_anatomy_Position3D_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_anatomy_Position3D)
gen_oaam_anatomy_AreaSymmetry_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_anatomy_AreaSymmetry)
gen_oaam_anatomy_AreaSymmetry_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_anatomy_AreaSymmetry)
gen_oaam_anatomy_AreaSymmetry_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_anatomy_AreaSymmetry)
gen_oaam_anatomy_LocationSymmetry_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_anatomy_LocationSymmetry)
gen_oaam_anatomy_LocationSymmetry_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_anatomy_LocationSymmetry)
gen_oaam_anatomy_LocationSymmetry_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_anatomy_LocationSymmetry)
gen_oaam_capabilities_CapabilitiesContainerA_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_capabilities_CapabilitiesContainerA)
gen_oaam_anatomy_Subanatomy_anatomy_AnatomyContainerA = Generalization(general=anatomy_AnatomyContainerA, specific=oaam_anatomy_Subanatomy)
gen_oaam_anatomy_Subanatomy_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_anatomy_Subanatomy)
gen_oaam_anatomy_Subanatomy_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_anatomy_Subanatomy)
gen_oaam_anatomy_Anatomy_AnatomyContainerA = Generalization(general=AnatomyContainerA, specific=oaam_anatomy_Anatomy)
gen_oaam_capabilities_TaskOnDeviceCapability_capabilities_CapabilityA = Generalization(general=capabilities_CapabilityA, specific=oaam_capabilities_TaskOnDeviceCapability)
gen_oaam_capabilities_DeviceInLocationCapability_capabilities_CapabilityA = Generalization(general=capabilities_CapabilityA, specific=oaam_capabilities_DeviceInLocationCapability)
gen_oaam_capabilities_DeviceInLocationCapability_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_capabilities_DeviceInLocationCapability)
gen_oaam_capabilities_DeviceInLocationCapability_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_capabilities_DeviceInLocationCapability)
gen_oaam_capabilities_DeviceInLocationCapability_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_capabilities_DeviceInLocationCapability)
gen_oaam_capabilities_TaskOnDeviceCapability_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_capabilities_TaskOnDeviceCapability)
gen_oaam_capabilities_TaskOnDeviceCapability_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_capabilities_TaskOnDeviceCapability)
gen_oaam_capabilities_TaskOnDeviceCapability_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_capabilities_TaskOnDeviceCapability)
gen_oaam_capabilities_SignalOnConnectionOrDeviceCapability_capabilities_CapabilityA = Generalization(general=capabilities_CapabilityA, specific=oaam_capabilities_SignalOnConnectionOrDeviceCapability)
gen_oaam_capabilities_SignalOnConnectionOrDeviceCapability_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_capabilities_SignalOnConnectionOrDeviceCapability)
gen_oaam_capabilities_ConnectionInDuctOrLocationCapability_capabilities_CapabilityA = Generalization(general=capabilities_CapabilityA, specific=oaam_capabilities_ConnectionInDuctOrLocationCapability)
gen_oaam_capabilities_ConnectionInDuctOrLocationCapability_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_capabilities_ConnectionInDuctOrLocationCapability)
gen_oaam_capabilities_ConnectionInDuctOrLocationCapability_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_capabilities_ConnectionInDuctOrLocationCapability)
gen_oaam_capabilities_ConnectionInDuctOrLocationCapability_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_capabilities_ConnectionInDuctOrLocationCapability)
gen_oaam_capabilities_SubdeviceInDeviceCapability_capabilities_CapabilityA = Generalization(general=capabilities_CapabilityA, specific=oaam_capabilities_SubdeviceInDeviceCapability)
gen_oaam_capabilities_SubdeviceInDeviceCapability_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_capabilities_SubdeviceInDeviceCapability)
gen_oaam_capabilities_SubdeviceInDeviceCapability_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_capabilities_SubdeviceInDeviceCapability)
gen_oaam_capabilities_SubdeviceInDeviceCapability_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_capabilities_SubdeviceInDeviceCapability)
gen_oaam_capabilities_SignalOnConnectionOrDeviceCapability_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_capabilities_SignalOnConnectionOrDeviceCapability)
gen_oaam_capabilities_SignalOnConnectionOrDeviceCapability_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_capabilities_SignalOnConnectionOrDeviceCapability)
gen_oaam_capabilities_ResourceConsumption_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_capabilities_ResourceConsumption)
gen_oaam_capabilities_SubconnectionInDeviceCapability_capabilities_CapabilityA = Generalization(general=capabilities_CapabilityA, specific=oaam_capabilities_SubconnectionInDeviceCapability)
gen_oaam_capabilities_SubconnectionInDeviceCapability_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_capabilities_SubconnectionInDeviceCapability)
gen_oaam_capabilities_SubconnectionInDeviceCapability_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_capabilities_SubconnectionInDeviceCapability)
gen_oaam_capabilities_SubconnectionInDeviceCapability_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_capabilities_SubconnectionInDeviceCapability)
gen_oaam_capabilities_MessageOnConnectionOrDeviceCapability_capabilities_CapabilityA = Generalization(general=capabilities_CapabilityA, specific=oaam_capabilities_MessageOnConnectionOrDeviceCapability)
gen_oaam_capabilities_MessageOnConnectionOrDeviceCapability_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_capabilities_MessageOnConnectionOrDeviceCapability)
gen_oaam_capabilities_MessageOnConnectionOrDeviceCapability_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_capabilities_MessageOnConnectionOrDeviceCapability)
gen_oaam_capabilities_MessageOnConnectionOrDeviceCapability_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_capabilities_MessageOnConnectionOrDeviceCapability)
gen_oaam_capabilities_MessageOnBusCapability_capabilities_CapabilityA = Generalization(general=capabilities_CapabilityA, specific=oaam_capabilities_MessageOnBusCapability)
gen_oaam_capabilities_MessageOnBusCapability_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_capabilities_MessageOnBusCapability)
gen_oaam_capabilities_MessageOnBusCapability_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_capabilities_MessageOnBusCapability)
gen_oaam_capabilities_MessageOnBusCapability_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_capabilities_MessageOnBusCapability)
gen_oaam_capabilities_SubmessageInMessageCapability_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_capabilities_SubmessageInMessageCapability)
gen_oaam_capabilities_SubmessageInMessageCapability_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_capabilities_SubmessageInMessageCapability)
gen_oaam_capabilities_SubmessageInMessageCapability_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_capabilities_SubmessageInMessageCapability)
gen_oaam_capabilities_SubmessageInMessageCapability_capabilities_CapabilityA = Generalization(general=capabilities_CapabilityA, specific=oaam_capabilities_SubmessageInMessageCapability)
gen_oaam_capabilities_Capabilities_CapabilitiesContainerA = Generalization(general=CapabilitiesContainerA, specific=oaam_capabilities_Capabilities)
gen_oaam_capabilities_Subcapabilities_capabilities_CapabilitiesContainerA = Generalization(general=capabilities_CapabilitiesContainerA, specific=oaam_capabilities_Subcapabilities)
gen_oaam_capabilities_Subcapabilities_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_capabilities_Subcapabilities)
gen_oaam_capabilities_Subcapabilities_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_capabilities_Subcapabilities)
gen_oaam_capabilities_SignalInMessageCapability_capabilities_CapabilityA = Generalization(general=capabilities_CapabilityA, specific=oaam_capabilities_SignalInMessageCapability)
gen_oaam_capabilities_SignalInMessageCapability_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_capabilities_SignalInMessageCapability)
gen_oaam_capabilities_SignalInMessageCapability_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_capabilities_SignalInMessageCapability)
gen_oaam_capabilities_SignalInMessageCapability_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_capabilities_SignalInMessageCapability)
gen_oaam_restrictions_RestrictionsContainerA_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_restrictions_RestrictionsContainerA)
gen_oaam_restrictions_Restrictions_RestrictionsContainerA = Generalization(general=RestrictionsContainerA, specific=oaam_restrictions_Restrictions)
gen_oaam_restrictions_AreaRestriction_restrictions_TaskRestrictionA = Generalization(general=restrictions_TaskRestrictionA, specific=oaam_restrictions_AreaRestriction)
gen_oaam_restrictions_AreaRestriction_restrictions_TaskGroupRestrictionA = Generalization(general=restrictions_TaskGroupRestrictionA, specific=oaam_restrictions_AreaRestriction)
gen_oaam_restrictions_AreaRestriction_restrictions_SignalRestrictionA = Generalization(general=restrictions_SignalRestrictionA, specific=oaam_restrictions_AreaRestriction)
gen_oaam_restrictions_AreaRestriction_restrictions_SignalGroupRestrictionA = Generalization(general=restrictions_SignalGroupRestrictionA, specific=oaam_restrictions_AreaRestriction)
gen_oaam_restrictions_AreaRestriction_restrictions_SubfunctionRestrictionA = Generalization(general=restrictions_SubfunctionRestrictionA, specific=oaam_restrictions_AreaRestriction)
gen_oaam_restrictions_AreaRestriction_restrictions_DeviceRestrictionA = Generalization(general=restrictions_DeviceRestrictionA, specific=oaam_restrictions_AreaRestriction)
gen_oaam_restrictions_AreaRestriction_restrictions_ConnectionRestrinctionA = Generalization(general=restrictions_ConnectionRestrinctionA, specific=oaam_restrictions_AreaRestriction)
gen_oaam_restrictions_AreaRestriction_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_restrictions_AreaRestriction)
gen_oaam_restrictions_AreaRestriction_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_restrictions_AreaRestriction)
gen_oaam_restrictions_AreaRestriction_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_restrictions_AreaRestriction)
gen_oaam_restrictions_LocationRestriction_restrictions_TaskRestrictionA = Generalization(general=restrictions_TaskRestrictionA, specific=oaam_restrictions_LocationRestriction)
gen_oaam_restrictions_LocationRestriction_restrictions_TaskGroupRestrictionA = Generalization(general=restrictions_TaskGroupRestrictionA, specific=oaam_restrictions_LocationRestriction)
gen_oaam_restrictions_LocationRestriction_restrictions_SignalRestrictionA = Generalization(general=restrictions_SignalRestrictionA, specific=oaam_restrictions_LocationRestriction)
gen_oaam_restrictions_LocationRestriction_restrictions_SignalGroupRestrictionA = Generalization(general=restrictions_SignalGroupRestrictionA, specific=oaam_restrictions_LocationRestriction)
gen_oaam_restrictions_LocationRestriction_restrictions_SubfunctionRestrictionA = Generalization(general=restrictions_SubfunctionRestrictionA, specific=oaam_restrictions_LocationRestriction)
gen_oaam_restrictions_LocationRestriction_restrictions_DeviceRestrictionA = Generalization(general=restrictions_DeviceRestrictionA, specific=oaam_restrictions_LocationRestriction)
gen_oaam_restrictions_LocationRestriction_restrictions_ConnectionRestrinctionA = Generalization(general=restrictions_ConnectionRestrinctionA, specific=oaam_restrictions_LocationRestriction)
gen_oaam_restrictions_LocationRestriction_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_restrictions_LocationRestriction)
gen_oaam_restrictions_LocationRestriction_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_restrictions_LocationRestriction)
gen_oaam_restrictions_LocationRestriction_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_restrictions_LocationRestriction)
gen_oaam_restrictions_DeviceTypeRestriction_restrictions_TaskRestrictionA = Generalization(general=restrictions_TaskRestrictionA, specific=oaam_restrictions_DeviceTypeRestriction)
gen_oaam_restrictions_DeviceTypeRestriction_restrictions_TaskGroupRestrictionA = Generalization(general=restrictions_TaskGroupRestrictionA, specific=oaam_restrictions_DeviceTypeRestriction)
gen_oaam_restrictions_DeviceTypeRestriction_restrictions_SignalRestrictionA = Generalization(general=restrictions_SignalRestrictionA, specific=oaam_restrictions_DeviceTypeRestriction)
gen_oaam_restrictions_DeviceTypeRestriction_restrictions_SignalGroupRestrictionA = Generalization(general=restrictions_SignalGroupRestrictionA, specific=oaam_restrictions_DeviceTypeRestriction)
gen_oaam_restrictions_DeviceTypeRestriction_restrictions_SubfunctionRestrictionA = Generalization(general=restrictions_SubfunctionRestrictionA, specific=oaam_restrictions_DeviceTypeRestriction)
gen_oaam_restrictions_DeviceTypeRestriction_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_restrictions_DeviceTypeRestriction)
gen_oaam_restrictions_DeviceTypeRestriction_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_restrictions_DeviceTypeRestriction)
gen_oaam_restrictions_DeviceTypeRestriction_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_restrictions_DeviceTypeRestriction)
gen_oaam_restrictions_PowerSourceRestriction_restrictions_TaskRestrictionA = Generalization(general=restrictions_TaskRestrictionA, specific=oaam_restrictions_PowerSourceRestriction)
gen_oaam_restrictions_PowerSourceRestriction_restrictions_TaskGroupRestrictionA = Generalization(general=restrictions_TaskGroupRestrictionA, specific=oaam_restrictions_PowerSourceRestriction)
gen_oaam_restrictions_PowerSourceRestriction_restrictions_SignalRestrictionA = Generalization(general=restrictions_SignalRestrictionA, specific=oaam_restrictions_PowerSourceRestriction)
gen_oaam_restrictions_PowerSourceRestriction_restrictions_SignalGroupRestrictionA = Generalization(general=restrictions_SignalGroupRestrictionA, specific=oaam_restrictions_PowerSourceRestriction)
gen_oaam_restrictions_PowerSourceRestriction_restrictions_SubfunctionRestrictionA = Generalization(general=restrictions_SubfunctionRestrictionA, specific=oaam_restrictions_PowerSourceRestriction)
gen_oaam_restrictions_PowerSourceRestriction_restrictions_DeviceRestrictionA = Generalization(general=restrictions_DeviceRestrictionA, specific=oaam_restrictions_PowerSourceRestriction)
gen_oaam_restrictions_PowerSourceRestriction_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_restrictions_PowerSourceRestriction)
gen_oaam_restrictions_PowerSourceRestriction_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_restrictions_PowerSourceRestriction)
gen_oaam_restrictions_PowerSourceRestriction_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_restrictions_PowerSourceRestriction)
gen_oaam_restrictions_DeviceRestriction_restrictions_TaskRestrictionA = Generalization(general=restrictions_TaskRestrictionA, specific=oaam_restrictions_DeviceRestriction)
gen_oaam_restrictions_DeviceRestriction_restrictions_TaskGroupRestrictionA = Generalization(general=restrictions_TaskGroupRestrictionA, specific=oaam_restrictions_DeviceRestriction)
gen_oaam_restrictions_DeviceRestriction_restrictions_SignalRestrictionA = Generalization(general=restrictions_SignalRestrictionA, specific=oaam_restrictions_DeviceRestriction)
gen_oaam_restrictions_DeviceRestriction_restrictions_SignalGroupRestrictionA = Generalization(general=restrictions_SignalGroupRestrictionA, specific=oaam_restrictions_DeviceRestriction)
gen_oaam_restrictions_DeviceRestriction_restrictions_SubfunctionRestrictionA = Generalization(general=restrictions_SubfunctionRestrictionA, specific=oaam_restrictions_DeviceRestriction)
gen_oaam_restrictions_DeviceRestriction_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_restrictions_DeviceRestriction)
gen_oaam_restrictions_DeviceRestriction_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_restrictions_DeviceRestriction)
gen_oaam_restrictions_DeviceRestriction_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_restrictions_DeviceRestriction)
gen_oaam_restrictions_SegregationRestriction_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_restrictions_SegregationRestriction)
gen_oaam_restrictions_SegregationRestriction_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_restrictions_SegregationRestriction)
gen_oaam_restrictions_SegregationRestriction_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_restrictions_SegregationRestriction)
gen_oaam_restrictions_ConnectionTypeRestriction_restrictions_SignalRestrictionA = Generalization(general=restrictions_SignalRestrictionA, specific=oaam_restrictions_ConnectionTypeRestriction)
gen_oaam_restrictions_ConnectionTypeRestriction_restrictions_SignalGroupRestrictionA = Generalization(general=restrictions_SignalGroupRestrictionA, specific=oaam_restrictions_ConnectionTypeRestriction)
gen_oaam_restrictions_ConnectionTypeRestriction_restrictions_SubfunctionRestrictionA = Generalization(general=restrictions_SubfunctionRestrictionA, specific=oaam_restrictions_ConnectionTypeRestriction)
gen_oaam_restrictions_ConnectionTypeRestriction_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_restrictions_ConnectionTypeRestriction)
gen_oaam_restrictions_ConnectionTypeRestriction_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_restrictions_ConnectionTypeRestriction)
gen_oaam_restrictions_ConnectionTypeRestriction_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_restrictions_ConnectionTypeRestriction)
gen_oaam_restrictions_ConnectionRestriction_restrictions_SignalRestrictionA = Generalization(general=restrictions_SignalRestrictionA, specific=oaam_restrictions_ConnectionRestriction)
gen_oaam_restrictions_ConnectionRestriction_restrictions_SignalGroupRestrictionA = Generalization(general=restrictions_SignalGroupRestrictionA, specific=oaam_restrictions_ConnectionRestriction)
gen_oaam_restrictions_ConnectionRestriction_restrictions_SubfunctionRestrictionA = Generalization(general=restrictions_SubfunctionRestrictionA, specific=oaam_restrictions_ConnectionRestriction)
gen_oaam_restrictions_ConnectionRestriction_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_restrictions_ConnectionRestriction)
gen_oaam_restrictions_ConnectionRestriction_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_restrictions_ConnectionRestriction)
gen_oaam_restrictions_ConnectionRestriction_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_restrictions_ConnectionRestriction)
gen_oaam_restrictions_TaskAtomicRestriction_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_restrictions_TaskAtomicRestriction)
gen_oaam_restrictions_TaskAtomicRestriction_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_restrictions_TaskAtomicRestriction)
gen_oaam_restrictions_TaskSymmetryRestriction_restrictions_TaskRestrictionA = Generalization(general=restrictions_TaskRestrictionA, specific=oaam_restrictions_TaskSymmetryRestriction)
gen_oaam_restrictions_TaskSymmetryRestriction_restrictions_TaskGroupRestrictionA = Generalization(general=restrictions_TaskGroupRestrictionA, specific=oaam_restrictions_TaskSymmetryRestriction)
gen_oaam_restrictions_TaskSymmetryRestriction_restrictions_SubfunctionRestrictionA = Generalization(general=restrictions_SubfunctionRestrictionA, specific=oaam_restrictions_TaskSymmetryRestriction)
gen_oaam_restrictions_TaskSymmetryRestriction_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_restrictions_TaskSymmetryRestriction)
gen_oaam_restrictions_TaskSymmetryRestriction_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_restrictions_TaskSymmetryRestriction)
gen_oaam_restrictions_TaskSymmetryRestriction_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_restrictions_TaskSymmetryRestriction)
gen_oaam_restrictions_TimeDelayRestriction_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_restrictions_TimeDelayRestriction)
gen_oaam_restrictions_SynchronicityRestriction_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_restrictions_SynchronicityRestriction)
gen_oaam_restrictions_SynchronicityRestriction_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_restrictions_SynchronicityRestriction)
gen_oaam_restrictions_SynchronicityRestriction_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_restrictions_SynchronicityRestriction)
gen_oaam_restrictions_SynchronicityRestriction_restrictions_TaskRestrictionA = Generalization(general=restrictions_TaskRestrictionA, specific=oaam_restrictions_SynchronicityRestriction)
gen_oaam_restrictions_TaskAtomicRestriction_restrictions_TaskRestrictionA = Generalization(general=restrictions_TaskRestrictionA, specific=oaam_restrictions_TaskAtomicRestriction)
gen_oaam_restrictions_TaskAtomicRestriction_restrictions_TaskGroupRestrictionA = Generalization(general=restrictions_TaskGroupRestrictionA, specific=oaam_restrictions_TaskAtomicRestriction)
gen_oaam_restrictions_TaskAtomicRestriction_restrictions_SubfunctionRestrictionA = Generalization(general=restrictions_SubfunctionRestrictionA, specific=oaam_restrictions_TaskAtomicRestriction)
gen_oaam_restrictions_TaskAtomicRestriction_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_restrictions_TaskAtomicRestriction)
gen_oaam_restrictions_TimeDelayRestriction_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_restrictions_TimeDelayRestriction)
gen_oaam_restrictions_TimeDelayRestriction_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_restrictions_TimeDelayRestriction)
gen_oaam_restrictions_Subrestrictions_restrictions_RestrictionsContainerA = Generalization(general=restrictions_RestrictionsContainerA, specific=oaam_restrictions_Subrestrictions)
gen_oaam_restrictions_Subrestrictions_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_restrictions_Subrestrictions)
gen_oaam_restrictions_Subrestrictions_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_restrictions_Subrestrictions)
gen_oaam_allocations_AllocationsContainerA_OaamBaseElementA = Generalization(general=OaamBaseElementA, specific=oaam_allocations_AllocationsContainerA)
gen_oaam_allocations_SignalAssignment_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_allocations_SignalAssignment)
gen_oaam_allocations_SignalAssignment_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_allocations_SignalAssignment)
gen_oaam_allocations_SignalAssignment_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_allocations_SignalAssignment)
gen_oaam_allocations_TaskAssignment_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_allocations_TaskAssignment)
gen_oaam_allocations_TaskAssignment_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_allocations_TaskAssignment)
gen_oaam_allocations_TaskAssignment_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_allocations_TaskAssignment)
gen_oaam_allocations_SignalAssignmentSegment_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_allocations_SignalAssignmentSegment)
gen_oaam_allocations_SignalAssignmentSegment_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_allocations_SignalAssignmentSegment)
gen_oaam_allocations_SignalAssignmentSegment_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_allocations_SignalAssignmentSegment)
gen_oaam_allocations_ConnectionAssignment_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_allocations_ConnectionAssignment)
gen_oaam_allocations_ConnectionAssignment_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_allocations_ConnectionAssignment)
gen_oaam_allocations_ConnectionAssignment_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_allocations_ConnectionAssignment)
gen_oaam_allocations_DeviceAssignment_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_allocations_DeviceAssignment)
gen_oaam_allocations_DeviceAssignment_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_allocations_DeviceAssignment)
gen_oaam_allocations_DeviceAssignment_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_allocations_DeviceAssignment)
gen_oaam_allocations_SubdeviceAssignment_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_allocations_SubdeviceAssignment)
gen_oaam_allocations_SubdeviceAssignment_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_allocations_SubdeviceAssignment)
gen_oaam_allocations_SubdeviceAssignment_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_allocations_SubdeviceAssignment)
gen_oaam_allocations_ConnectionAssignmentSegment_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_allocations_ConnectionAssignmentSegment)
gen_oaam_allocations_ConnectionAssignmentSegment_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_allocations_ConnectionAssignmentSegment)
gen_oaam_allocations_ConnectionAssignmentSegment_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_allocations_ConnectionAssignmentSegment)
gen_oaam_allocations_Schedule_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_allocations_Schedule)
gen_oaam_allocations_Schedule_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_allocations_Schedule)
gen_oaam_allocations_Schedule_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_allocations_Schedule)
gen_oaam_allocations_SubconnectionAssignment_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_allocations_SubconnectionAssignment)
gen_oaam_allocations_SubconnectionAssignment_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_allocations_SubconnectionAssignment)
gen_oaam_allocations_SubconnectionAssignment_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_allocations_SubconnectionAssignment)
gen_oaam_allocations_MessageA_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_allocations_MessageA)
gen_oaam_allocations_MessageA_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_allocations_MessageA)
gen_oaam_allocations_MessageA_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_allocations_MessageA)
gen_oaam_allocations_ScheduledTime_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_allocations_ScheduledTime)
gen_oaam_allocations_ScheduledTime_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_allocations_ScheduledTime)
gen_oaam_allocations_ScheduledTime_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_allocations_ScheduledTime)
gen_oaam_allocations_MessageSegment_common_OaamBaseElementA = Generalization(general=common_OaamBaseElementA, specific=oaam_allocations_MessageSegment)
gen_oaam_allocations_MessageSegment_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_allocations_MessageSegment)
gen_oaam_allocations_MessageSegment_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_allocations_MessageSegment)
gen_oaam_allocations_Message_MessageA = Generalization(general=MessageA, specific=oaam_allocations_Message)
gen_oaam_allocations_Submessage_MessageA = Generalization(general=MessageA, specific=oaam_allocations_Submessage)
gen_oaam_allocations_Allocations_AllocationsContainerA = Generalization(general=AllocationsContainerA, specific=oaam_allocations_Allocations)
gen_oaam_allocations_Suballocations_allocations_AllocationsContainerA = Generalization(general=allocations_AllocationsContainerA, specific=oaam_allocations_Suballocations)
gen_oaam_allocations_Suballocations_scenario_ModeDependentElementA = Generalization(general=scenario_ModeDependentElementA, specific=oaam_allocations_Suballocations)
gen_oaam_allocations_Suballocations_scenario_VariantDependentElementA = Generalization(general=scenario_VariantDependentElementA, specific=oaam_allocations_Suballocations)

# Domain Model
domain_model = DomainModel(
    name="oaam",
    types={oaam_Architecture, OaamBaseElementA, Anatomy, Capabilities, Library, Scenario, Systems, Functions, Hardware, oaam_common_OaamBaseElementA, Restrictions, Allocations, oaam_common_AttributeA, oaam_common_AttributeString, AttributeA, oaam_common_BoolA, oaam_common_BoolOperation, common_BoolA, common_OaamBaseElementA, BoolA, oaam_common_AttributeNumeric, oaam_common_AttributeContainment, oaam_common_AttributeReference, oaam_common_Array, oaam_common_BoolNot, oaam_common_DataTypeA, oaam_common_Integer, DataTypeA, oaam_common_FloatingPoint, oaam_common_Struct, Struct, oaam_common_Boolean, oaam_common_Byte, oaam_common_Character, ResourceGroup, oaam_library_ResourceProviderA, ResourceBundle, ResourceType, ResourceLink, oaam_library_ResourceProviderInstanceA, oaam_library_ResourceConsumerA, Resource, oaam_library_LibraryContainerA, ResourceTypeModifier, ResourceTypeDissimilarity, TaskType, TaskTypeDissimilarity, SignalType, ResourceTypeModifierLevel, IoType, DeviceTypeDissimilarity, BusType, ConnectionType, WireType, LocationType, DuctType, AttributeDefinition, PowerSource, DeviceType, Sublibrary, DeviceTypeSymmetry, ResourceAlternatives, oaam_library_Resource, MessageType, oaam_library_ResourceType, library_ResourceConsumerA, ResourceTypeModifierReference, TaskStateDeclaration, oaam_library_ResourceAlternatives, oaam_library_ResourceBundle, oaam_library_TaskType, OutputDeclaration, InputDeclaration, TaskParameterDeclaration, oaam_library_SignalType, oaam_library_DeviceType, library_ResourceProviderA, IoDeclaration, IoGroup, oaam_library_ConnectionType, oaam_library_LocationType, oaam_library_IoType, DuctOpeningDeclaration, oaam_library_DuctType, oaam_library_WireType, TaskOutputTrigger, oaam_library_InputDeclaration, oaam_library_OutputDeclaration, oaam_library_ResourceGroup, oaam_library_DeviceTypeSymmetry, FaultPropagation, oaam_library_IoDeclaration, oaam_library_DuctOpeningDeclaration, BoolOperation, oaam_library_IoGroup, oaam_library_AttributeDefinition, oaam_library_FaultPropagation, oaam_library_ResourceTypeModifier, BoolNot, TaskInputState, oaam_library_TaskInputState, oaam_library_PowerSource, oaam_library_ResourceLink, oaam_library_TaskTypeDissimilarity, oaam_library_ResourceTypeModifierLevel, oaam_library_ResourceTypeModifierReference, oaam_library_TaskOutputTrigger, oaam_library_DeviceTypeDissimilarity, oaam_library_ResourceTypeDissimilarity, oaam_library_TaskInputTrigger, TaskInputTrigger, oaam_library_BusType, oaam_library_TaskStateDeclaration, oaam_library_TaskParameterDeclaration, oaam_library_MessageType, oaam_library_Library, LibraryContainerA, oaam_library_Sublibrary, oaam_scenario_VariantDependentElementA, Variant, oaam_scenario_ScenarioParameterA, scenario_ModeDependentElementA, scenario_VariantDependentElementA, oaam_scenario_ModeDependentElementA, OperationModeReference, oaam_scenario_OperationMode, oaam_scenario_ScenarioParameterNumeric, scenario_ScenarioParameterA, oaam_scenario_ScenarioContainerA, ScenarioParameterA, OperationMode, Subscenario, oaam_scenario_Scenario, ScenarioContainerA, oaam_scenario_Subscenario, oaam_scenario_ScenarioParameterBool, oaam_scenario_Variant, oaam_scenario_OperationModeReference, oaam_systems_Systems, SystemsContainerA, oaam_systems_Subsystem, systems_SystemsContainerA, oaam_systems_SystemsContainerA, System, InformationFlow, InputSegregation, Subsystem, oaam_systems_System, ProvidedInformationA, RequiredInformationA, oaam_systems_RequiredInformationA, oaam_systems_ProvidedInformationA, oaam_systems_InformationFlow, oaam_systems_InformationMaterial, oaam_systems_InformationSignal, systems_ProvidedInformationA, systems_RequiredInformationA, oaam_systems_HydraulicPower, oaam_systems_InformationPower, oaam_systems_ElectricPower, InformationPower, oaam_systems_RotaryPower, oaam_systems_LinearPower, oaam_systems_InputSegregation, ExternalTaskLink, TaskGroup, oaam_functions_Functions, FunctionsContainerA, oaam_functions_FunctionsContainerA, Task, FailureCondition, Subfunctions, TaskSymmetry, TaskRedundancy, Signal, SignalGroup, Output, oaam_functions_Task, Input, Device, TaskParameter, oaam_functions_ExternalTaskLink, oaam_functions_TaskGroup, oaam_functions_TaskSymmetry, oaam_functions_TaskRedundancy, oaam_functions_FailureCondition, OutputIntegrityState, oaam_functions_OutputIntegrityState, oaam_functions_Signal, oaam_functions_Input, Connection, oaam_functions_SignalGroup, Io, ExternalOutputLink, oaam_functions_Output, oaam_functions_Subfunctions, oaam_functions_TaskParameter, oaam_functions_ExternalOutputLink, Subhardware, oaam_hardware_HardwareContainerA, DeviceSymmetry, Location, Bus, oaam_hardware_Device, library_ResourceProviderInstanceA, oaam_hardware_Connection, oaam_hardware_Hardware, hardware_HardwareContainerA, oaam_hardware_Io, oaam_hardware_DeviceSymmetry, oaam_anatomy_AnatomyContainerA, oaam_hardware_Subhardware, oaam_hardware_Bus, AreaSymmetry, oaam_anatomy_Location, LocationSymmetry, Duct, Area, Subanatomy, DuctOpening, Position3D, oaam_anatomy_Area, oaam_anatomy_Duct, oaam_anatomy_DuctOpening, oaam_anatomy_Position3D, oaam_anatomy_AreaSymmetry, oaam_anatomy_LocationSymmetry, oaam_capabilities_CapabilitiesContainerA, TaskOnDeviceCapability, oaam_anatomy_Subanatomy, anatomy_AnatomyContainerA, oaam_anatomy_Anatomy, AnatomyContainerA, oaam_capabilities_CapabilityA, ResourceConsumption, ConnectionInDuctOrLocationCapability, Subcapabilities, SignalOnConnectionOrDeviceCapability, DeviceInLocationCapability, SubdeviceInDeviceCapability, MessageOnConnectionOrDeviceCapability, oaam_capabilities_TaskOnDeviceCapability, capabilities_CapabilityA, SubconnectionInDeviceCapability, MessageOnBusCapability, SubmessageInMessageCapability, SignalInMessageCapability, oaam_capabilities_DeviceInLocationCapability, oaam_capabilities_SignalOnConnectionOrDeviceCapability, oaam_capabilities_ConnectionInDuctOrLocationCapability, oaam_capabilities_SubdeviceInDeviceCapability, oaam_capabilities_ResourceConsumption, oaam_capabilities_SubconnectionInDeviceCapability, oaam_capabilities_MessageOnConnectionOrDeviceCapability, oaam_capabilities_MessageOnBusCapability, oaam_capabilities_SubmessageInMessageCapability, oaam_capabilities_Capabilities, CapabilitiesContainerA, oaam_capabilities_Subcapabilities, capabilities_CapabilitiesContainerA, oaam_capabilities_SignalInMessageCapability, AreaRestriction, PowerSourceRestriction, TaskAtomicRestriction, oaam_restrictions_RestrictionsContainerA, DeviceTypeRestriction, DeviceRestriction, LocationRestriction, SegregationRestriction, Subrestrictions, TaskSymmetryRestriction, SynchronicityRestriction, ConnectionRestriction, ConnectionTypeRestriction, oaam_restrictions_ConnectionRestrinctionA, TimeDelayRestriction, oaam_restrictions_Restrictions, RestrictionsContainerA, oaam_restrictions_DeviceRestrictionA, oaam_restrictions_TaskGroupRestrictionA, oaam_restrictions_TaskRestrictionA, oaam_restrictions_SignalRestrictionA, oaam_restrictions_SubfunctionRestrictionA, oaam_restrictions_SignalGroupRestrictionA, oaam_restrictions_LocationRestriction, restrictions_TaskRestrictionA, restrictions_TaskGroupRestrictionA, restrictions_SignalRestrictionA, restrictions_SignalGroupRestrictionA, restrictions_SubfunctionRestrictionA, restrictions_DeviceRestrictionA, restrictions_ConnectionRestrinctionA, oaam_restrictions_AreaRestriction, oaam_restrictions_DeviceTypeRestriction, oaam_restrictions_PowerSourceRestriction, oaam_restrictions_DeviceRestriction, oaam_restrictions_SegregationRestriction, oaam_restrictions_ConnectionTypeRestriction, oaam_restrictions_ConnectionRestriction, oaam_restrictions_TaskSymmetryRestriction, oaam_restrictions_TimeDelayRestriction, oaam_restrictions_SynchronicityRestriction, oaam_restrictions_TaskAtomicRestriction, oaam_allocations_AllocationsContainerA, oaam_restrictions_Subrestrictions, restrictions_RestrictionsContainerA, SignalAssignment, Suballocations, SubconnectionAssignment, Message, DeviceAssignment, SubdeviceAssignment, ConnectionAssignment, TaskAssignment, Schedule, oaam_allocations_SignalAssignment, SignalAssignmentSegment, oaam_allocations_TaskAssignment, oaam_allocations_SignalAssignmentSegment, oaam_allocations_ConnectionAssignment, ConnectionAssignmentSegment, oaam_allocations_DeviceAssignment, oaam_allocations_SubdeviceAssignment, oaam_allocations_ConnectionAssignmentSegment, oaam_allocations_Schedule, oaam_allocations_SubconnectionAssignment, oaam_allocations_MessageA, ScheduledTime, oaam_allocations_ScheduledTime, MessageSegment, Submessage, SignalToMessageAssignment, oaam_allocations_MessageSegment, oaam_allocations_Message, MessageA, oaam_allocations_Submessage, oaam_allocations_SignalToMessageAssignment, oaam_allocations_Allocations, AllocationsContainerA, oaam_allocations_Suballocations, allocations_AllocationsContainerA, BoolOperationTypesE, IntegretyStateE, EndianessE, AttributeTargetsE, IoDirectionE, AttributeTypesE, SymmetryTypesE},
    associations={include1, anatomy12, capabilities14, library2, scenario4, systems6, functions8, hardware10, restrictions16, allocations18, attributes20, value21, value22, left24, right25, in28, type30, fields31, inheritsFrom33, consumedGroups36, providedBundles38, possibleResourceProvisions39, providedGroups41, resourceLinks44, requiredResources35, dataTypes47, resourceTypes49, resourceBundles52, resourceModifiers55, resourceTypeDissimilarities57, taskTypes59, taskTypeDissimilarity61, signalTypes63, requiredModifiers46, deviceTypeSymmetries67, ioTypes85, deviceTypeDissimilarities69, hardwareGroupTypes87, connectionTypes71, wireTypes73, locationTypes75, ductTypes77, genericAttributes79, powerSources81, deviceTypes65, sublibraries83, alternatives95, type97, messageTypes89, propagetedResources91, allowedModifiers93, stateDeclarations109, modifiers99, resources102, resources104, outputDeclarations106, inputDeclarations107, parameterDeclarations111, type113, ioDeclarations115, startingPointResourceTypes120, ioGroups116, wireTypes118, messageType129, endPointResourceTypes123, switchTypes126, ductOpeningDeclarations132, trigger135, type133, resources146, type136, faultPropagations139, resources141, type143, condition152, booleanOperations154, deviceTypes148, ios150, out164, booleanNots156, taskInputStates158, input160, in162, tasks179, levels167, equalAlternatives169, betterAlternative171, type174, allowedLevels176, resourceTypes183, devices181, input195, condition185, booleanOperations187, booleanNots190, taskInputTriggers193, type197, type199, deviceTypes201, connectionTypes203, messagetypes206, headerDefinition209, trailerDefinition211, variants215, operationModes214, parameters216, variants217, operationModes220, subscenarios222, operationMode224, systems226, informationFlows227, inputSegregations229, subsystems231, from236, to238, providedOutputs233, requiredInputs234, tasks246, taskLinks247, taskGroups249, groupA241, groupB243, failureConditions259, subfunctions261, taskSymmetries251, taskRedundancies253, signals255, signalGroups257, outputs267, implements269, type263, inputs265, inputs278, outputs281, deviceBinding272, parameters274, type276, tasks289, task284, tasks287, condition293, tasks291, booleanNots298, booleanOperations295, output303, outputIntegrityStates301, type310, source305, target307, declaration317, connectionBinding313, signals315, implements326, declaration328, implements319, ioBindings322, outputLink324, ioBindings331, output334, deviceSymmetries340, connections342, subhardware345, definition336, devices338, subdevices354, locationBinding357, buses347, type349, ios351, startingPoints367, endPoints370, powerSources359, subconnections362, type365, devices378, masters373, declaration376, type380, connections382, devices385, areaSymmetries398, locations388, locationSymmetries390, ducts392, areas394, subanatomies396, ductOpenings404, type400, position402, type411, startingPoint413, locations406, ducts408, endPoint416, relativPosition419, declaration421, areas426, locations424, taskOnDeviceCapabilities429, resourceConsumptions428, connectionInDuctOrLocationCapabilities436, subcapabilities438, signalOnConnectionOrDeviceCapabilities430, deviceInLocationCapabilities432, subdeviceInDeviceCapabilities434, signalInMessageCapabilities446, messageOnConnectionOrDeviceCapabilities448, subconnectionInDeviceCapabilities440, messageOnBusCapabilities442, submessageInMessageCapabilities444, deviceType455, taskType450, deviceType452, ductType465, locationType457, connectionType460, locationType462, subdeviceType476, signalType468, deviceType470, connectionType473, targetDeviceType483, targetDeviceType478, subconnectionType481, messageType493, originalResource486, type488, busType491, messageType504, messageType496, deviceType498, connectionType501, submessageType506, messageType509, signalType511, areaRestrictions519, powerSourceRestrictions521, deviceTypeRestrictions514, deviceRestrictions515, locationRestrictions517, connectionTypeRestrictions531, segregationRestrictions533, taskAtomicRestrictions523, taskSymmetryRestrictions525, synchronicityRestriction527, connectionRestrictions529, devices539, subrestrictions535, timeDelayRestrictions537, connections541, tasks543, signals545, subfunctions547, taskGroups549, signalGroups551, locations553, devices559, areas555, powerSources557, connections565, tasksA567, deviceTypes561, connectionTypes563, signalsA577, signalsB580, tasksB569, subfunctionsA572, subfunctionsB574, devicesA595, devicesB598, connectionsA601, taskGroupsA583, taskGroupsB586, signalGroupsB589, signalGroupsA592, connectionsB604, startTask607, endTask609, signalAssignments619, suballocations621, subconnectionAssignments623, deviceAssignments612, subdeviceAssignments613, connectionAssignments615, taskAssignments617, device632, schedules635, messages625, capability627, task629, connection642, capability645, segments637, signal638, segments641, device656, location658, capability661, device647, connection650, schedules653, capability672, subdevice674, capability664, location666, duct669, targetDevice685, targetDevice677, capability680, subconnection682, schedules689, scheduledTimes688, segments695, type697, submessages691, bus710, signalToMessageAssignments693, sourceDevices713, destinationDevices716, capability700, device702, connection705, capability708, operationModes729, dataType732, capability719, signal721, attributes723, variants726, capability735},
    generalizations={gen_oaam_Architecture_OaamBaseElementA, gen_oaam_common_AttributeA_OaamBaseElementA, gen_oaam_common_AttributeString_AttributeA, gen_oaam_common_BoolOperation_common_BoolA, gen_oaam_common_BoolOperation_common_OaamBaseElementA, gen_oaam_common_AttributeNumeric_AttributeA, gen_oaam_common_AttributeContainment_AttributeA, gen_oaam_common_AttributeReference_AttributeA, gen_oaam_common_Array_DataTypeA, gen_oaam_common_BoolNot_common_BoolA, gen_oaam_common_BoolNot_common_OaamBaseElementA, gen_oaam_common_DataTypeA_OaamBaseElementA, gen_oaam_common_Integer_DataTypeA, gen_oaam_common_FloatingPoint_DataTypeA, gen_oaam_common_Struct_DataTypeA, gen_oaam_common_Boolean_DataTypeA, gen_oaam_common_Byte_DataTypeA, gen_oaam_common_Character_DataTypeA, gen_oaam_library_LibraryContainerA_OaamBaseElementA, gen_oaam_library_Resource_OaamBaseElementA, gen_oaam_library_ResourceType_library_ResourceConsumerA, gen_oaam_library_ResourceType_common_OaamBaseElementA, gen_oaam_library_ResourceAlternatives_OaamBaseElementA, gen_oaam_library_ResourceBundle_library_ResourceConsumerA, gen_oaam_library_ResourceBundle_common_OaamBaseElementA, gen_oaam_library_TaskType_library_ResourceConsumerA, gen_oaam_library_TaskType_common_OaamBaseElementA, gen_oaam_library_SignalType_library_ResourceConsumerA, gen_oaam_library_SignalType_common_OaamBaseElementA, gen_oaam_library_DeviceType_library_ResourceConsumerA, gen_oaam_library_DeviceType_library_ResourceProviderA, gen_oaam_library_DeviceType_common_OaamBaseElementA, gen_oaam_library_ConnectionType_library_ResourceProviderA, gen_oaam_library_ConnectionType_library_ResourceConsumerA, gen_oaam_library_ConnectionType_common_OaamBaseElementA, gen_oaam_library_LocationType_library_ResourceProviderA, gen_oaam_library_LocationType_common_OaamBaseElementA, gen_oaam_library_IoType_OaamBaseElementA, gen_oaam_library_DuctType_library_ResourceProviderA, gen_oaam_library_DuctType_common_OaamBaseElementA, gen_oaam_library_WireType_OaamBaseElementA, gen_oaam_library_InputDeclaration_OaamBaseElementA, gen_oaam_library_OutputDeclaration_OaamBaseElementA, gen_oaam_library_ResourceGroup_OaamBaseElementA, gen_oaam_library_DeviceTypeSymmetry_OaamBaseElementA, gen_oaam_library_IoDeclaration_OaamBaseElementA, gen_oaam_library_DuctOpeningDeclaration_OaamBaseElementA, gen_oaam_library_IoGroup_OaamBaseElementA, gen_oaam_library_AttributeDefinition_OaamBaseElementA, gen_oaam_library_FaultPropagation_OaamBaseElementA, gen_oaam_library_ResourceTypeModifier_OaamBaseElementA, gen_oaam_library_TaskInputState_common_BoolA, gen_oaam_library_TaskInputState_common_OaamBaseElementA, gen_oaam_library_PowerSource_OaamBaseElementA, gen_oaam_library_ResourceLink_OaamBaseElementA, gen_oaam_library_TaskTypeDissimilarity_OaamBaseElementA, gen_oaam_library_ResourceTypeModifierLevel_common_OaamBaseElementA, gen_oaam_library_ResourceTypeModifierLevel_library_ResourceConsumerA, gen_oaam_library_ResourceTypeModifierReference_OaamBaseElementA, gen_oaam_library_TaskOutputTrigger_OaamBaseElementA, gen_oaam_library_DeviceTypeDissimilarity_OaamBaseElementA, gen_oaam_library_ResourceTypeDissimilarity_OaamBaseElementA, gen_oaam_library_TaskInputTrigger_common_BoolA, gen_oaam_library_TaskInputTrigger_common_OaamBaseElementA, gen_oaam_library_BusType_library_ResourceProviderA, gen_oaam_library_BusType_common_OaamBaseElementA, gen_oaam_library_TaskStateDeclaration_OaamBaseElementA, gen_oaam_library_TaskParameterDeclaration_OaamBaseElementA, gen_oaam_library_MessageType_common_OaamBaseElementA, gen_oaam_library_MessageType_library_ResourceConsumerA, gen_oaam_library_MessageType_library_ResourceProviderA, gen_oaam_library_Library_LibraryContainerA, gen_oaam_library_Sublibrary_LibraryContainerA, gen_oaam_scenario_ScenarioParameterA_scenario_ModeDependentElementA, gen_oaam_scenario_ScenarioParameterA_scenario_VariantDependentElementA, gen_oaam_scenario_OperationMode_common_OaamBaseElementA, gen_oaam_scenario_OperationMode_scenario_VariantDependentElementA, gen_oaam_scenario_ScenarioParameterNumeric_scenario_ScenarioParameterA, gen_oaam_scenario_ScenarioParameterNumeric_common_OaamBaseElementA, gen_oaam_scenario_ScenarioContainerA_OaamBaseElementA, gen_oaam_scenario_Scenario_ScenarioContainerA, gen_oaam_scenario_Subscenario_ScenarioContainerA, gen_oaam_scenario_ScenarioParameterBool_scenario_ScenarioParameterA, gen_oaam_scenario_ScenarioParameterBool_common_OaamBaseElementA, gen_oaam_scenario_Variant_common_OaamBaseElementA, gen_oaam_scenario_Variant_scenario_ModeDependentElementA, gen_oaam_scenario_OperationModeReference_OaamBaseElementA, gen_oaam_systems_Systems_SystemsContainerA, gen_oaam_systems_Subsystem_systems_SystemsContainerA, gen_oaam_systems_Subsystem_scenario_ModeDependentElementA, gen_oaam_systems_Subsystem_scenario_VariantDependentElementA, gen_oaam_systems_SystemsContainerA_OaamBaseElementA, gen_oaam_systems_InformationFlow_scenario_ModeDependentElementA, gen_oaam_systems_InformationFlow_scenario_VariantDependentElementA, gen_oaam_systems_System_common_OaamBaseElementA, gen_oaam_systems_System_scenario_VariantDependentElementA, gen_oaam_systems_System_scenario_ModeDependentElementA, gen_oaam_systems_InformationFlow_common_OaamBaseElementA, gen_oaam_systems_InformationMaterial_systems_ProvidedInformationA, gen_oaam_systems_InformationMaterial_systems_RequiredInformationA, gen_oaam_systems_InformationMaterial_common_OaamBaseElementA, gen_oaam_systems_InformationMaterial_scenario_ModeDependentElementA, gen_oaam_systems_InformationMaterial_scenario_VariantDependentElementA, gen_oaam_systems_InformationSignal_systems_ProvidedInformationA, gen_oaam_systems_InformationSignal_systems_RequiredInformationA, gen_oaam_systems_InformationSignal_common_OaamBaseElementA, gen_oaam_systems_InformationSignal_scenario_ModeDependentElementA, gen_oaam_systems_InformationSignal_scenario_VariantDependentElementA, gen_oaam_systems_HydraulicPower_InformationPower, gen_oaam_systems_InformationPower_systems_ProvidedInformationA, gen_oaam_systems_InformationPower_systems_RequiredInformationA, gen_oaam_systems_InformationPower_common_OaamBaseElementA, gen_oaam_systems_InformationPower_scenario_VariantDependentElementA, gen_oaam_systems_InformationPower_scenario_ModeDependentElementA, gen_oaam_systems_ElectricPower_InformationPower, gen_oaam_systems_RotaryPower_InformationPower, gen_oaam_systems_LinearPower_InformationPower, gen_oaam_systems_InputSegregation_OaamBaseElementA, gen_oaam_functions_Functions_FunctionsContainerA, gen_oaam_functions_FunctionsContainerA_common_OaamBaseElementA, gen_oaam_functions_FunctionsContainerA_scenario_VariantDependentElementA, gen_oaam_functions_FunctionsContainerA_scenario_ModeDependentElementA, gen_oaam_functions_Task_common_OaamBaseElementA, gen_oaam_functions_Task_scenario_VariantDependentElementA, gen_oaam_functions_Task_scenario_ModeDependentElementA, gen_oaam_functions_ExternalTaskLink_common_OaamBaseElementA, gen_oaam_functions_ExternalTaskLink_scenario_ModeDependentElementA, gen_oaam_functions_ExternalTaskLink_scenario_VariantDependentElementA, gen_oaam_functions_TaskGroup_common_OaamBaseElementA, gen_oaam_functions_TaskGroup_scenario_ModeDependentElementA, gen_oaam_functions_TaskGroup_scenario_VariantDependentElementA, gen_oaam_functions_TaskSymmetry_common_OaamBaseElementA, gen_oaam_functions_TaskSymmetry_scenario_ModeDependentElementA, gen_oaam_functions_TaskSymmetry_scenario_VariantDependentElementA, gen_oaam_functions_FailureCondition_common_OaamBaseElementA, gen_oaam_functions_FailureCondition_scenario_ModeDependentElementA, gen_oaam_functions_FailureCondition_scenario_VariantDependentElementA, gen_oaam_functions_TaskRedundancy_common_OaamBaseElementA, gen_oaam_functions_TaskRedundancy_scenario_ModeDependentElementA, gen_oaam_functions_TaskRedundancy_scenario_VariantDependentElementA, gen_oaam_functions_OutputIntegrityState_common_BoolA, gen_oaam_functions_OutputIntegrityState_common_OaamBaseElementA, gen_oaam_functions_OutputIntegrityState_scenario_ModeDependentElementA, gen_oaam_functions_OutputIntegrityState_scenario_VariantDependentElementA, gen_oaam_functions_Signal_common_OaamBaseElementA, gen_oaam_functions_Signal_scenario_VariantDependentElementA, gen_oaam_functions_Signal_scenario_ModeDependentElementA, gen_oaam_functions_Input_common_OaamBaseElementA, gen_oaam_functions_Input_scenario_VariantDependentElementA, gen_oaam_functions_Input_scenario_ModeDependentElementA, gen_oaam_functions_SignalGroup_common_OaamBaseElementA, gen_oaam_functions_SignalGroup_scenario_ModeDependentElementA, gen_oaam_functions_SignalGroup_scenario_VariantDependentElementA, gen_oaam_functions_Output_scenario_ModeDependentElementA, gen_oaam_functions_Output_common_OaamBaseElementA, gen_oaam_functions_Output_scenario_VariantDependentElementA, gen_oaam_functions_Subfunctions_FunctionsContainerA, gen_oaam_functions_ExternalOutputLink_common_OaamBaseElementA, gen_oaam_functions_ExternalOutputLink_scenario_ModeDependentElementA, gen_oaam_functions_ExternalOutputLink_scenario_VariantDependentElementA, gen_oaam_functions_TaskParameter_OaamBaseElementA, gen_oaam_hardware_HardwareContainerA_OaamBaseElementA, gen_oaam_hardware_Device_library_ResourceProviderInstanceA, gen_oaam_hardware_Device_common_OaamBaseElementA, gen_oaam_hardware_Device_scenario_VariantDependentElementA, gen_oaam_hardware_Device_scenario_ModeDependentElementA, gen_oaam_hardware_Connection_library_ResourceProviderInstanceA, gen_oaam_hardware_Connection_common_OaamBaseElementA, gen_oaam_hardware_Connection_scenario_VariantDependentElementA, gen_oaam_hardware_Connection_scenario_ModeDependentElementA, gen_oaam_hardware_Hardware_hardware_HardwareContainerA, gen_oaam_hardware_Hardware_scenario_VariantDependentElementA, gen_oaam_hardware_Hardware_scenario_ModeDependentElementA, gen_oaam_hardware_Io_common_OaamBaseElementA, gen_oaam_hardware_Io_scenario_VariantDependentElementA, gen_oaam_hardware_Io_scenario_ModeDependentElementA, gen_oaam_hardware_DeviceSymmetry_common_OaamBaseElementA, gen_oaam_hardware_DeviceSymmetry_scenario_VariantDependentElementA, gen_oaam_hardware_DeviceSymmetry_scenario_ModeDependentElementA, gen_oaam_anatomy_AnatomyContainerA_OaamBaseElementA, gen_oaam_hardware_Subhardware_hardware_HardwareContainerA, gen_oaam_hardware_Subhardware_scenario_VariantDependentElementA, gen_oaam_hardware_Subhardware_scenario_ModeDependentElementA, gen_oaam_hardware_Bus_library_ResourceProviderInstanceA, gen_oaam_hardware_Bus_common_OaamBaseElementA, gen_oaam_hardware_Bus_scenario_VariantDependentElementA, gen_oaam_hardware_Bus_scenario_ModeDependentElementA, gen_oaam_anatomy_Location_library_ResourceProviderInstanceA, gen_oaam_anatomy_Location_common_OaamBaseElementA, gen_oaam_anatomy_Location_scenario_VariantDependentElementA, gen_oaam_anatomy_Location_scenario_ModeDependentElementA, gen_oaam_anatomy_Area_common_OaamBaseElementA, gen_oaam_anatomy_Area_scenario_VariantDependentElementA, gen_oaam_anatomy_Area_scenario_ModeDependentElementA, gen_oaam_anatomy_Duct_library_ResourceProviderInstanceA, gen_oaam_anatomy_Duct_common_OaamBaseElementA, gen_oaam_anatomy_Duct_scenario_VariantDependentElementA, gen_oaam_anatomy_Duct_scenario_ModeDependentElementA, gen_oaam_anatomy_Position3D_scenario_ModeDependentElementA, gen_oaam_anatomy_DuctOpening_common_OaamBaseElementA, gen_oaam_anatomy_DuctOpening_scenario_VariantDependentElementA, gen_oaam_anatomy_DuctOpening_scenario_ModeDependentElementA, gen_oaam_anatomy_Position3D_common_OaamBaseElementA, gen_oaam_anatomy_Position3D_scenario_VariantDependentElementA, gen_oaam_anatomy_AreaSymmetry_common_OaamBaseElementA, gen_oaam_anatomy_AreaSymmetry_scenario_ModeDependentElementA, gen_oaam_anatomy_AreaSymmetry_scenario_VariantDependentElementA, gen_oaam_anatomy_LocationSymmetry_common_OaamBaseElementA, gen_oaam_anatomy_LocationSymmetry_scenario_ModeDependentElementA, gen_oaam_anatomy_LocationSymmetry_scenario_VariantDependentElementA, gen_oaam_capabilities_CapabilitiesContainerA_OaamBaseElementA, gen_oaam_anatomy_Subanatomy_anatomy_AnatomyContainerA, gen_oaam_anatomy_Subanatomy_scenario_VariantDependentElementA, gen_oaam_anatomy_Subanatomy_scenario_ModeDependentElementA, gen_oaam_anatomy_Anatomy_AnatomyContainerA, gen_oaam_capabilities_TaskOnDeviceCapability_capabilities_CapabilityA, gen_oaam_capabilities_DeviceInLocationCapability_capabilities_CapabilityA, gen_oaam_capabilities_DeviceInLocationCapability_common_OaamBaseElementA, gen_oaam_capabilities_DeviceInLocationCapability_scenario_VariantDependentElementA, gen_oaam_capabilities_DeviceInLocationCapability_scenario_ModeDependentElementA, gen_oaam_capabilities_TaskOnDeviceCapability_common_OaamBaseElementA, gen_oaam_capabilities_TaskOnDeviceCapability_scenario_VariantDependentElementA, gen_oaam_capabilities_TaskOnDeviceCapability_scenario_ModeDependentElementA, gen_oaam_capabilities_SignalOnConnectionOrDeviceCapability_capabilities_CapabilityA, gen_oaam_capabilities_SignalOnConnectionOrDeviceCapability_common_OaamBaseElementA, gen_oaam_capabilities_ConnectionInDuctOrLocationCapability_capabilities_CapabilityA, gen_oaam_capabilities_ConnectionInDuctOrLocationCapability_common_OaamBaseElementA, gen_oaam_capabilities_ConnectionInDuctOrLocationCapability_scenario_VariantDependentElementA, gen_oaam_capabilities_ConnectionInDuctOrLocationCapability_scenario_ModeDependentElementA, gen_oaam_capabilities_SubdeviceInDeviceCapability_capabilities_CapabilityA, gen_oaam_capabilities_SubdeviceInDeviceCapability_common_OaamBaseElementA, gen_oaam_capabilities_SubdeviceInDeviceCapability_scenario_VariantDependentElementA, gen_oaam_capabilities_SubdeviceInDeviceCapability_scenario_ModeDependentElementA, gen_oaam_capabilities_SignalOnConnectionOrDeviceCapability_scenario_VariantDependentElementA, gen_oaam_capabilities_SignalOnConnectionOrDeviceCapability_scenario_ModeDependentElementA, gen_oaam_capabilities_ResourceConsumption_OaamBaseElementA, gen_oaam_capabilities_SubconnectionInDeviceCapability_capabilities_CapabilityA, gen_oaam_capabilities_SubconnectionInDeviceCapability_common_OaamBaseElementA, gen_oaam_capabilities_SubconnectionInDeviceCapability_scenario_VariantDependentElementA, gen_oaam_capabilities_SubconnectionInDeviceCapability_scenario_ModeDependentElementA, gen_oaam_capabilities_MessageOnConnectionOrDeviceCapability_capabilities_CapabilityA, gen_oaam_capabilities_MessageOnConnectionOrDeviceCapability_common_OaamBaseElementA, gen_oaam_capabilities_MessageOnConnectionOrDeviceCapability_scenario_VariantDependentElementA, gen_oaam_capabilities_MessageOnConnectionOrDeviceCapability_scenario_ModeDependentElementA, gen_oaam_capabilities_MessageOnBusCapability_capabilities_CapabilityA, gen_oaam_capabilities_MessageOnBusCapability_common_OaamBaseElementA, gen_oaam_capabilities_MessageOnBusCapability_scenario_VariantDependentElementA, gen_oaam_capabilities_MessageOnBusCapability_scenario_ModeDependentElementA, gen_oaam_capabilities_SubmessageInMessageCapability_common_OaamBaseElementA, gen_oaam_capabilities_SubmessageInMessageCapability_scenario_VariantDependentElementA, gen_oaam_capabilities_SubmessageInMessageCapability_scenario_ModeDependentElementA, gen_oaam_capabilities_SubmessageInMessageCapability_capabilities_CapabilityA, gen_oaam_capabilities_Capabilities_CapabilitiesContainerA, gen_oaam_capabilities_Subcapabilities_capabilities_CapabilitiesContainerA, gen_oaam_capabilities_Subcapabilities_scenario_ModeDependentElementA, gen_oaam_capabilities_Subcapabilities_scenario_VariantDependentElementA, gen_oaam_capabilities_SignalInMessageCapability_capabilities_CapabilityA, gen_oaam_capabilities_SignalInMessageCapability_common_OaamBaseElementA, gen_oaam_capabilities_SignalInMessageCapability_scenario_VariantDependentElementA, gen_oaam_capabilities_SignalInMessageCapability_scenario_ModeDependentElementA, gen_oaam_restrictions_RestrictionsContainerA_OaamBaseElementA, gen_oaam_restrictions_Restrictions_RestrictionsContainerA, gen_oaam_restrictions_AreaRestriction_restrictions_TaskRestrictionA, gen_oaam_restrictions_AreaRestriction_restrictions_TaskGroupRestrictionA, gen_oaam_restrictions_AreaRestriction_restrictions_SignalRestrictionA, gen_oaam_restrictions_AreaRestriction_restrictions_SignalGroupRestrictionA, gen_oaam_restrictions_AreaRestriction_restrictions_SubfunctionRestrictionA, gen_oaam_restrictions_AreaRestriction_restrictions_DeviceRestrictionA, gen_oaam_restrictions_AreaRestriction_restrictions_ConnectionRestrinctionA, gen_oaam_restrictions_AreaRestriction_common_OaamBaseElementA, gen_oaam_restrictions_AreaRestriction_scenario_VariantDependentElementA, gen_oaam_restrictions_AreaRestriction_scenario_ModeDependentElementA, gen_oaam_restrictions_LocationRestriction_restrictions_TaskRestrictionA, gen_oaam_restrictions_LocationRestriction_restrictions_TaskGroupRestrictionA, gen_oaam_restrictions_LocationRestriction_restrictions_SignalRestrictionA, gen_oaam_restrictions_LocationRestriction_restrictions_SignalGroupRestrictionA, gen_oaam_restrictions_LocationRestriction_restrictions_SubfunctionRestrictionA, gen_oaam_restrictions_LocationRestriction_restrictions_DeviceRestrictionA, gen_oaam_restrictions_LocationRestriction_restrictions_ConnectionRestrinctionA, gen_oaam_restrictions_LocationRestriction_common_OaamBaseElementA, gen_oaam_restrictions_LocationRestriction_scenario_VariantDependentElementA, gen_oaam_restrictions_LocationRestriction_scenario_ModeDependentElementA, gen_oaam_restrictions_DeviceTypeRestriction_restrictions_TaskRestrictionA, gen_oaam_restrictions_DeviceTypeRestriction_restrictions_TaskGroupRestrictionA, gen_oaam_restrictions_DeviceTypeRestriction_restrictions_SignalRestrictionA, gen_oaam_restrictions_DeviceTypeRestriction_restrictions_SignalGroupRestrictionA, gen_oaam_restrictions_DeviceTypeRestriction_restrictions_SubfunctionRestrictionA, gen_oaam_restrictions_DeviceTypeRestriction_common_OaamBaseElementA, gen_oaam_restrictions_DeviceTypeRestriction_scenario_VariantDependentElementA, gen_oaam_restrictions_DeviceTypeRestriction_scenario_ModeDependentElementA, gen_oaam_restrictions_PowerSourceRestriction_restrictions_TaskRestrictionA, gen_oaam_restrictions_PowerSourceRestriction_restrictions_TaskGroupRestrictionA, gen_oaam_restrictions_PowerSourceRestriction_restrictions_SignalRestrictionA, gen_oaam_restrictions_PowerSourceRestriction_restrictions_SignalGroupRestrictionA, gen_oaam_restrictions_PowerSourceRestriction_restrictions_SubfunctionRestrictionA, gen_oaam_restrictions_PowerSourceRestriction_restrictions_DeviceRestrictionA, gen_oaam_restrictions_PowerSourceRestriction_common_OaamBaseElementA, gen_oaam_restrictions_PowerSourceRestriction_scenario_VariantDependentElementA, gen_oaam_restrictions_PowerSourceRestriction_scenario_ModeDependentElementA, gen_oaam_restrictions_DeviceRestriction_restrictions_TaskRestrictionA, gen_oaam_restrictions_DeviceRestriction_restrictions_TaskGroupRestrictionA, gen_oaam_restrictions_DeviceRestriction_restrictions_SignalRestrictionA, gen_oaam_restrictions_DeviceRestriction_restrictions_SignalGroupRestrictionA, gen_oaam_restrictions_DeviceRestriction_restrictions_SubfunctionRestrictionA, gen_oaam_restrictions_DeviceRestriction_common_OaamBaseElementA, gen_oaam_restrictions_DeviceRestriction_scenario_VariantDependentElementA, gen_oaam_restrictions_DeviceRestriction_scenario_ModeDependentElementA, gen_oaam_restrictions_SegregationRestriction_common_OaamBaseElementA, gen_oaam_restrictions_SegregationRestriction_scenario_ModeDependentElementA, gen_oaam_restrictions_SegregationRestriction_scenario_VariantDependentElementA, gen_oaam_restrictions_ConnectionTypeRestriction_restrictions_SignalRestrictionA, gen_oaam_restrictions_ConnectionTypeRestriction_restrictions_SignalGroupRestrictionA, gen_oaam_restrictions_ConnectionTypeRestriction_restrictions_SubfunctionRestrictionA, gen_oaam_restrictions_ConnectionTypeRestriction_common_OaamBaseElementA, gen_oaam_restrictions_ConnectionTypeRestriction_scenario_VariantDependentElementA, gen_oaam_restrictions_ConnectionTypeRestriction_scenario_ModeDependentElementA, gen_oaam_restrictions_ConnectionRestriction_restrictions_SignalRestrictionA, gen_oaam_restrictions_ConnectionRestriction_restrictions_SignalGroupRestrictionA, gen_oaam_restrictions_ConnectionRestriction_restrictions_SubfunctionRestrictionA, gen_oaam_restrictions_ConnectionRestriction_common_OaamBaseElementA, gen_oaam_restrictions_ConnectionRestriction_scenario_VariantDependentElementA, gen_oaam_restrictions_ConnectionRestriction_scenario_ModeDependentElementA, gen_oaam_restrictions_TaskAtomicRestriction_scenario_ModeDependentElementA, gen_oaam_restrictions_TaskAtomicRestriction_scenario_VariantDependentElementA, gen_oaam_restrictions_TaskSymmetryRestriction_restrictions_TaskRestrictionA, gen_oaam_restrictions_TaskSymmetryRestriction_restrictions_TaskGroupRestrictionA, gen_oaam_restrictions_TaskSymmetryRestriction_restrictions_SubfunctionRestrictionA, gen_oaam_restrictions_TaskSymmetryRestriction_common_OaamBaseElementA, gen_oaam_restrictions_TaskSymmetryRestriction_scenario_ModeDependentElementA, gen_oaam_restrictions_TaskSymmetryRestriction_scenario_VariantDependentElementA, gen_oaam_restrictions_TimeDelayRestriction_common_OaamBaseElementA, gen_oaam_restrictions_SynchronicityRestriction_common_OaamBaseElementA, gen_oaam_restrictions_SynchronicityRestriction_scenario_ModeDependentElementA, gen_oaam_restrictions_SynchronicityRestriction_scenario_VariantDependentElementA, gen_oaam_restrictions_SynchronicityRestriction_restrictions_TaskRestrictionA, gen_oaam_restrictions_TaskAtomicRestriction_restrictions_TaskRestrictionA, gen_oaam_restrictions_TaskAtomicRestriction_restrictions_TaskGroupRestrictionA, gen_oaam_restrictions_TaskAtomicRestriction_restrictions_SubfunctionRestrictionA, gen_oaam_restrictions_TaskAtomicRestriction_common_OaamBaseElementA, gen_oaam_restrictions_TimeDelayRestriction_scenario_ModeDependentElementA, gen_oaam_restrictions_TimeDelayRestriction_scenario_VariantDependentElementA, gen_oaam_restrictions_Subrestrictions_restrictions_RestrictionsContainerA, gen_oaam_restrictions_Subrestrictions_scenario_VariantDependentElementA, gen_oaam_restrictions_Subrestrictions_scenario_ModeDependentElementA, gen_oaam_allocations_AllocationsContainerA_OaamBaseElementA, gen_oaam_allocations_SignalAssignment_common_OaamBaseElementA, gen_oaam_allocations_SignalAssignment_scenario_VariantDependentElementA, gen_oaam_allocations_SignalAssignment_scenario_ModeDependentElementA, gen_oaam_allocations_TaskAssignment_common_OaamBaseElementA, gen_oaam_allocations_TaskAssignment_scenario_VariantDependentElementA, gen_oaam_allocations_TaskAssignment_scenario_ModeDependentElementA, gen_oaam_allocations_SignalAssignmentSegment_common_OaamBaseElementA, gen_oaam_allocations_SignalAssignmentSegment_scenario_VariantDependentElementA, gen_oaam_allocations_SignalAssignmentSegment_scenario_ModeDependentElementA, gen_oaam_allocations_ConnectionAssignment_common_OaamBaseElementA, gen_oaam_allocations_ConnectionAssignment_scenario_VariantDependentElementA, gen_oaam_allocations_ConnectionAssignment_scenario_ModeDependentElementA, gen_oaam_allocations_DeviceAssignment_common_OaamBaseElementA, gen_oaam_allocations_DeviceAssignment_scenario_VariantDependentElementA, gen_oaam_allocations_DeviceAssignment_scenario_ModeDependentElementA, gen_oaam_allocations_SubdeviceAssignment_common_OaamBaseElementA, gen_oaam_allocations_SubdeviceAssignment_scenario_VariantDependentElementA, gen_oaam_allocations_SubdeviceAssignment_scenario_ModeDependentElementA, gen_oaam_allocations_ConnectionAssignmentSegment_common_OaamBaseElementA, gen_oaam_allocations_ConnectionAssignmentSegment_scenario_VariantDependentElementA, gen_oaam_allocations_ConnectionAssignmentSegment_scenario_ModeDependentElementA, gen_oaam_allocations_Schedule_common_OaamBaseElementA, gen_oaam_allocations_Schedule_scenario_ModeDependentElementA, gen_oaam_allocations_Schedule_scenario_VariantDependentElementA, gen_oaam_allocations_SubconnectionAssignment_common_OaamBaseElementA, gen_oaam_allocations_SubconnectionAssignment_scenario_VariantDependentElementA, gen_oaam_allocations_SubconnectionAssignment_scenario_ModeDependentElementA, gen_oaam_allocations_MessageA_common_OaamBaseElementA, gen_oaam_allocations_MessageA_scenario_VariantDependentElementA, gen_oaam_allocations_MessageA_scenario_ModeDependentElementA, gen_oaam_allocations_ScheduledTime_common_OaamBaseElementA, gen_oaam_allocations_ScheduledTime_scenario_ModeDependentElementA, gen_oaam_allocations_ScheduledTime_scenario_VariantDependentElementA, gen_oaam_allocations_MessageSegment_common_OaamBaseElementA, gen_oaam_allocations_MessageSegment_scenario_VariantDependentElementA, gen_oaam_allocations_MessageSegment_scenario_ModeDependentElementA, gen_oaam_allocations_Message_MessageA, gen_oaam_allocations_Submessage_MessageA, gen_oaam_allocations_Allocations_AllocationsContainerA, gen_oaam_allocations_Suballocations_allocations_AllocationsContainerA, gen_oaam_allocations_Suballocations_scenario_ModeDependentElementA, gen_oaam_allocations_Suballocations_scenario_VariantDependentElementA},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)