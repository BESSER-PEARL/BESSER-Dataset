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
ParameterModifier: Enumeration = Enumeration(
    name="ParameterModifier",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="in"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="inout")
    }
)

ComponentType: Enumeration = Enumeration(
    name="ComponentType",
    literals={
            EnumerationLiteral(name="BUSINESS_COMPONENT"),
			EnumerationLiteral(name="INFRASTRUCTURE_COMPONENT")
    }
)

PrimitiveTypeEnum: Enumeration = Enumeration(
    name="PrimitiveTypeEnum",
    literals={
            EnumerationLiteral(name="DOUBLE"),
			EnumerationLiteral(name="CHAR"),
			EnumerationLiteral(name="BYTE"),
			EnumerationLiteral(name="LONG"),
			EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="BOOL")
    }
)

VariableCharacterisationType: Enumeration = Enumeration(
    name="VariableCharacterisationType",
    literals={
            EnumerationLiteral(name="STRUCTURE"),
			EnumerationLiteral(name="NUMBER_OF_ELEMENTS"),
			EnumerationLiteral(name="VALUE"),
			EnumerationLiteral(name="BYTESIZE"),
			EnumerationLiteral(name="TYPE")
    }
)

# Classes
pcm_av_DummyClass = Class(name="pcm::av::DummyClass")
pcm_av_Advice = Class(name="pcm::av::Advice")
pcm_av_EObject = Class(name="pcm::av::EObject")
pcm_av_GlobalScope = Class(name="pcm::av::GlobalScope")
pcm_av_PerJoinPointScope = Class(name="pcm::av::PerJoinPointScope")
pcm_av_core_av_PCMRandomVariable = Class(name="pcm::av::core::av::PCMRandomVariable")
RandomVariable = Class(name="RandomVariable")
ClosedWorkload = Class(name="ClosedWorkload")
PassiveResource = Class(name="PassiveResource")
VariableCharacterisation = Class(name="VariableCharacterisation")
seff_performance_av_InfrastructureCall = Class(name="seff::performance::av::InfrastructureCall")
seff_performance_av_ResourceCall = Class(name="seff::performance::av::ResourceCall")
seff_performance_av_ParametricResourceDemand = Class(name="seff::performance::av::ParametricResourceDemand")
LoopAction = Class(name="LoopAction")
GuardedBranchTransition = Class(name="GuardedBranchTransition")
qos_performance_av_SpecifiedExecutionTime = Class(name="qos::performance::av::SpecifiedExecutionTime")
composition_av_EventChannelSinkConnector = Class(name="composition::av::EventChannelSinkConnector")
OpenWorkload = Class(name="OpenWorkload")
Delay = Class(name="Delay")
CommunicationLinkResourceSpecification = Class(name="CommunicationLinkResourceSpecification")
ProcessingResourceSpecification = Class(name="ProcessingResourceSpecification")
pcm_av_entity_av_ResourceProvidedRole = Class(name="pcm::av::entity::av::ResourceProvidedRole")
Role = Class(name="Role")
entity_av_ResourceInterfaceProvidingEntity = Class(name="entity::av::ResourceInterfaceProvidingEntity")
ResourceInterface = Class(name="ResourceInterface")
pcm_av_entity_av_InterfaceProvidingRequiringEntity = Class(name="pcm::av::entity::av::InterfaceProvidingRequiringEntity")
entity_av_InterfaceProvidingEntity = Class(name="entity::av::InterfaceProvidingEntity")
entity_av_InterfaceRequiringEntity = Class(name="entity::av::InterfaceRequiringEntity")
pcm_av_entity_av_InterfaceProvidingEntity = Class(name="pcm::av::entity::av::InterfaceProvidingEntity")
Entity = Class(name="Entity")
ProvidedRole = Class(name="ProvidedRole")
pcm_av_entity_av_InterfaceRequiringEntity = Class(name="pcm::av::entity::av::InterfaceRequiringEntity")
entity_av_Entity = Class(name="entity::av::Entity")
entity_av_ResourceInterfaceRequiringEntity = Class(name="entity::av::ResourceInterfaceRequiringEntity")
RequiredRole = Class(name="RequiredRole")
pcm_av_entity_av_ResourceInterfaceRequiringEntity = Class(name="pcm::av::entity::av::ResourceInterfaceRequiringEntity")
entity_av_ResourceRequiredRole = Class(name="entity::av::ResourceRequiredRole")
pcm_av_entity_av_ResourceRequiredRole = Class(name="pcm::av::entity::av::ResourceRequiredRole")
pcm_av_entity_av_ResourceInterfaceProvidingEntity = Class(name="pcm::av::entity::av::ResourceInterfaceProvidingEntity")
composition_av_AssemblyEventConnector = Class(name="composition::av::AssemblyEventConnector")
Loop = Class(name="Loop")
pcm_av_entity_av_NamedElement = Class(name="pcm::av::entity::av::NamedElement")
pcm_av_entity_av_ResourceInterfaceProvidingRequiringEntity = Class(name="pcm::av::entity::av::ResourceInterfaceProvidingRequiringEntity")
pcm_av_entity_av_Entity = Class(name="pcm::av::entity::av::Entity")
Identifier = Class(name="Identifier")
entity_av_NamedElement = Class(name="entity::av::NamedElement")
pcm_av_composition_av_DelegationConnector = Class(name="pcm::av::composition::av::DelegationConnector")
Connector = Class(name="Connector")
pcm_av_composition_av_Connector = Class(name="pcm::av::composition::av::Connector")
pcm_av_composition_av_ComposedStructure = Class(name="pcm::av::composition::av::ComposedStructure")
composition_av_AssemblyContext = Class(name="composition::av::AssemblyContext")
composition_av_ResourceRequiredDelegationConnector = Class(name="composition::av::ResourceRequiredDelegationConnector")
entity_av_ResourceProvidedRole = Class(name="entity::av::ResourceProvidedRole")
pcm_av_entity_av_ComposedProvidingRequiringEntity = Class(name="pcm::av::entity::av::ComposedProvidingRequiringEntity")
composition_av_ComposedStructure = Class(name="composition::av::ComposedStructure")
entity_av_InterfaceProvidingRequiringEntity = Class(name="entity::av::InterfaceProvidingRequiringEntity")
pcm_av_composition_av_ResourceRequiredDelegationConnector = Class(name="pcm::av::composition::av::ResourceRequiredDelegationConnector")
pcm_av_composition_av_EventChannel = Class(name="pcm::av::composition::av::EventChannel")
EventGroup = Class(name="EventGroup")
composition_av_EventChannelSourceConnector = Class(name="composition::av::EventChannelSourceConnector")
pcm_av_composition_av_EventChannelSourceConnector = Class(name="pcm::av::composition::av::EventChannelSourceConnector")
SourceRole = Class(name="SourceRole")
pcm_av_composition_av_EventChannelSinkConnector = Class(name="pcm::av::composition::av::EventChannelSinkConnector")
SinkRole = Class(name="SinkRole")
PCMRandomVariable = Class(name="PCMRandomVariable")
pcm_av_composition_av_ProvidedDelegationConnector = Class(name="pcm::av::composition::av::ProvidedDelegationConnector")
DelegationConnector = Class(name="DelegationConnector")
composition_av_EventChannel = Class(name="composition::av::EventChannel")
OperationProvidedRole = Class(name="OperationProvidedRole")
composition_av_Connector = Class(name="composition::av::Connector")
pcm_av_composition_av_RequiredDelegationConnector = Class(name="pcm::av::composition::av::RequiredDelegationConnector")
OperationRequiredRole = Class(name="OperationRequiredRole")
pcm_av_composition_av_AssemblyConnector = Class(name="pcm::av::composition::av::AssemblyConnector")
pcm_av_composition_av_AssemblyEventConnector = Class(name="pcm::av::composition::av::AssemblyEventConnector")
pcm_av_composition_av_SourceDelegationConnector = Class(name="pcm::av::composition::av::SourceDelegationConnector")
pcm_av_composition_av_AssemblyInfrastructureConnector = Class(name="pcm::av::composition::av::AssemblyInfrastructureConnector")
InfrastructureProvidedRole = Class(name="InfrastructureProvidedRole")
InfrastructureRequiredRole = Class(name="InfrastructureRequiredRole")
pcm_av_composition_av_ProvidedInfrastructureDelegationConnector = Class(name="pcm::av::composition::av::ProvidedInfrastructureDelegationConnector")
pcm_av_composition_av_RequiredInfrastructureDelegationConnector = Class(name="pcm::av::composition::av::RequiredInfrastructureDelegationConnector")
pcm_av_composition_av_RequiredResourceDelegationConnector = Class(name="pcm::av::composition::av::RequiredResourceDelegationConnector")
pcm_av_composition_av_SinkDelegationConnector = Class(name="pcm::av::composition::av::SinkDelegationConnector")
pcm_av_usagemodel_av_Workload = Class(name="pcm::av::usagemodel::av::Workload")
UsageScenario = Class(name="UsageScenario")
pcm_av_usagemodel_av_UsageScenario = Class(name="pcm::av::usagemodel::av::UsageScenario")
UsageModel = Class(name="UsageModel")
ScenarioBehaviour = Class(name="ScenarioBehaviour")
Workload = Class(name="Workload")
pcm_av_usagemodel_av_UserData = Class(name="pcm::av::usagemodel::av::UserData")
pcm_av_usagemodel_av_UsageModel = Class(name="pcm::av::usagemodel::av::UsageModel")
UserData = Class(name="UserData")
pcm_av_composition_av_AssemblyContext = Class(name="pcm::av::composition::av::AssemblyContext")
RepositoryComponent = Class(name="RepositoryComponent")
VariableUsage = Class(name="VariableUsage")
OperationSignature = Class(name="OperationSignature")
pcm_av_usagemodel_av_AbstractUserAction = Class(name="pcm::av::usagemodel::av::AbstractUserAction")
pcm_av_usagemodel_av_ScenarioBehaviour = Class(name="pcm::av::usagemodel::av::ScenarioBehaviour")
pcm_av_usagemodel_av_EntryLevelSystemCall = Class(name="pcm::av::usagemodel::av::EntryLevelSystemCall")
AbstractUserAction = Class(name="AbstractUserAction")
BranchTransition = Class(name="BranchTransition")
pcm_av_usagemodel_av_BranchTransition = Class(name="pcm::av::usagemodel::av::BranchTransition")
Branch = Class(name="Branch")
pcm_av_usagemodel_av_Branch = Class(name="pcm::av::usagemodel::av::Branch")
pcm_av_usagemodel_av_Loop = Class(name="pcm::av::usagemodel::av::Loop")
pcm_av_usagemodel_av_Start = Class(name="pcm::av::usagemodel::av::Start")
pcm_av_usagemodel_av_OpenWorkload = Class(name="pcm::av::usagemodel::av::OpenWorkload")
pcm_av_usagemodel_av_Delay = Class(name="pcm::av::usagemodel::av::Delay")
pcm_av_usagemodel_av_ClosedWorkload = Class(name="pcm::av::usagemodel::av::ClosedWorkload")
pcm_av_usagemodel_av_Stop = Class(name="pcm::av::usagemodel::av::Stop")
pcm_av_repository_av_PassiveResource = Class(name="pcm::av::repository::av::PassiveResource")
BasicComponent = Class(name="BasicComponent")
ResourceTimeoutFailureType = Class(name="ResourceTimeoutFailureType")
pcm_av_repository_av_BasicComponent = Class(name="pcm::av::repository::av::BasicComponent")
ImplementationComponentType = Class(name="ImplementationComponentType")
ServiceEffectSpecification = Class(name="ServiceEffectSpecification")
CompleteComponentType = Class(name="CompleteComponentType")
pcm_av_repository_av_RepositoryComponent = Class(name="pcm::av::repository::av::RepositoryComponent")
InterfaceProvidingRequiringEntity = Class(name="InterfaceProvidingRequiringEntity")
Repository = Class(name="Repository")
pcm_av_repository_av_ProvidedRole = Class(name="pcm::av::repository::av::ProvidedRole")
pcm_av_repository_av_ImplementationComponentType = Class(name="pcm::av::repository::av::ImplementationComponentType")
EventType = Class(name="EventType")
ResourceSignature = Class(name="ResourceSignature")
pcm_av_repository_av_DataType = Class(name="pcm::av::repository::av::DataType")
pcm_av_repository_av_Repository = Class(name="pcm::av::repository::av::Repository")
Interface = Class(name="Interface")
FailureType = Class(name="FailureType")
pcm_av_repository_av_Interface = Class(name="pcm::av::repository::av::Interface")
pcm_av_repository_av_Parameter = Class(name="pcm::av::repository::av::Parameter")
DataType = Class(name="DataType")
InfrastructureSignature = Class(name="InfrastructureSignature")
Protocol = Class(name="Protocol")
RequiredCharacterisation = Class(name="RequiredCharacterisation")
pcm_av_repository_av_RequiredCharacterisation = Class(name="pcm::av::repository::av::RequiredCharacterisation")
Parameter_ = Class(name="Parameter")
pcm_av_repository_av_EventGroup = Class(name="pcm::av::repository::av::EventGroup")
pcm_av_repository_av_Signature = Class(name="pcm::av::repository::av::Signature")
ExceptionType = Class(name="ExceptionType")
pcm_av_repository_av_ExceptionType = Class(name="pcm::av::repository::av::ExceptionType")
pcm_av_repository_av_InfrastructureSignature = Class(name="pcm::av::repository::av::InfrastructureSignature")
InfrastructureInterface = Class(name="InfrastructureInterface")
pcm_av_repository_av_InfrastructureInterface = Class(name="pcm::av::repository::av::InfrastructureInterface")
pcm_av_repository_av_EventType = Class(name="pcm::av::repository::av::EventType")
Signature = Class(name="Signature")
pcm_av_repository_av_InfrastructureRequiredRole = Class(name="pcm::av::repository::av::InfrastructureRequiredRole")
pcm_av_repository_av_RequiredRole = Class(name="pcm::av::repository::av::RequiredRole")
pcm_av_repository_av_OperationSignature = Class(name="pcm::av::repository::av::OperationSignature")
OperationInterface = Class(name="OperationInterface")
pcm_av_repository_av_OperationRequiredRole = Class(name="pcm::av::repository::av::OperationRequiredRole")
pcm_av_repository_av_SourceRole = Class(name="pcm::av::repository::av::SourceRole")
pcm_av_repository_av_SinkRole = Class(name="pcm::av::repository::av::SinkRole")
pcm_av_repository_av_OperationProvidedRole = Class(name="pcm::av::repository::av::OperationProvidedRole")
pcm_av_repository_av_InfrastructureProvidedRole = Class(name="pcm::av::repository::av::InfrastructureProvidedRole")
pcm_av_repository_av_CompleteComponentType = Class(name="pcm::av::repository::av::CompleteComponentType")
pcm_av_repository_av_OperationInterface = Class(name="pcm::av::repository::av::OperationInterface")
ProvidesComponentType = Class(name="ProvidesComponentType")
pcm_av_repository_av_ProvidesComponentType = Class(name="pcm::av::repository::av::ProvidesComponentType")
pcm_av_repository_av_CompositeComponent = Class(name="pcm::av::repository::av::CompositeComponent")
entity_av_ComposedProvidingRequiringEntity = Class(name="entity::av::ComposedProvidingRequiringEntity")
repository_av_ImplementationComponentType = Class(name="repository::av::ImplementationComponentType")
pcm_av_repository_av_PrimitiveDataType = Class(name="pcm::av::repository::av::PrimitiveDataType")
pcm_av_repository_av_CollectionDataType = Class(name="pcm::av::repository::av::CollectionDataType")
repository_av_DataType = Class(name="repository::av::DataType")
pcm_av_repository_av_CompositeDataType = Class(name="pcm::av::repository::av::CompositeDataType")
CompositeDataType = Class(name="CompositeDataType")
InnerDeclaration = Class(name="InnerDeclaration")
pcm_av_repository_av_InnerDeclaration = Class(name="pcm::av::repository::av::InnerDeclaration")
NamedElement = Class(name="NamedElement")
pcm_av_repository_av_Role = Class(name="pcm::av::repository::av::Role")
pcm_av_resourcetype_av_ResourceSignature = Class(name="pcm::av::resourcetype::av::ResourceSignature")
ResourceRepository = Class(name="ResourceRepository")
pcm_av_resourcetype_av_ResourceRepository = Class(name="pcm::av::resourcetype::av::ResourceRepository")
SchedulingPolicy = Class(name="SchedulingPolicy")
pcm_av_resourcetype_av_SchedulingPolicy = Class(name="pcm::av::resourcetype::av::SchedulingPolicy")
pcm_av_resourcetype_av_CommunicationLinkResourceType = Class(name="pcm::av::resourcetype::av::CommunicationLinkResourceType")
NetworkInducedFailureType = Class(name="NetworkInducedFailureType")
pcm_av_resourcetype_av_ResourceInterface = Class(name="pcm::av::resourcetype::av::ResourceInterface")
pcm_av_protocol_av_Protocol = Class(name="pcm::av::protocol::av::Protocol")
pcm_av_parameter_av_VariableUsage = Class(name="pcm::av::parameter::av::VariableUsage")
pcm_av_resourcetype_av_ProcessingResourceType = Class(name="pcm::av::resourcetype::av::ProcessingResourceType")
ResourceType = Class(name="ResourceType")
HardwareInducedFailureType = Class(name="HardwareInducedFailureType")
pcm_av_resourcetype_av_ResourceType = Class(name="pcm::av::resourcetype::av::ResourceType")
UnitCarryingElement = Class(name="UnitCarryingElement")
SpecifiedOutputParameterAbstraction = Class(name="SpecifiedOutputParameterAbstraction")
EntryLevelSystemCall = Class(name="EntryLevelSystemCall")
parameter_av_pcm_av_AbstractNamedReference = Class(name="parameter::av::pcm::av::AbstractNamedReference")
pcm_av_parameter_av_VariableCharacterisation = Class(name="pcm::av::parameter::av::VariableCharacterisation")
pcm_av_parameter_av_CharacterisedVariable = Class(name="pcm::av::parameter::av::CharacterisedVariable")
Variable = Class(name="Variable")
pcm_av_reliability_av_FailureOccurrenceDescription = Class(name="pcm::av::reliability::av::FailureOccurrenceDescription")
CallAction = Class(name="CallAction")
SynchronisationPoint = Class(name="SynchronisationPoint")
CallReturnAction = Class(name="CallReturnAction")
SetVariableAction = Class(name="SetVariableAction")
pcm_av_reliability_av_HardwareInducedFailureType = Class(name="pcm::av::reliability::av::HardwareInducedFailureType")
ProcessingResourceType = Class(name="ProcessingResourceType")
pcm_av_reliability_av_SoftwareInducedFailureType = Class(name="pcm::av::reliability::av::SoftwareInducedFailureType")
InternalFailureOccurrenceDescription = Class(name="InternalFailureOccurrenceDescription")
pcm_av_reliability_av_InternalFailureOccurrenceDescription = Class(name="pcm::av::reliability::av::InternalFailureOccurrenceDescription")
FailureOccurrenceDescription = Class(name="FailureOccurrenceDescription")
InternalAction = Class(name="InternalAction")
SoftwareInducedFailureType = Class(name="SoftwareInducedFailureType")
pcm_av_reliability_av_NetworkInducedFailureType = Class(name="pcm::av::reliability::av::NetworkInducedFailureType")
qos_reliability_av_SpecifiedReliabilityAnnotation = Class(name="qos::reliability::av::SpecifiedReliabilityAnnotation")
pcm_av_reliability_av_ResourceTimeoutFailureType = Class(name="pcm::av::reliability::av::ResourceTimeoutFailureType")
pcm_av_reliability_av_FailureType = Class(name="pcm::av::reliability::av::FailureType")
pcm_av_seff_av_StopAction = Class(name="pcm::av::seff::av::StopAction")
AbstractInternalControlFlowAction = Class(name="AbstractInternalControlFlowAction")
pcm_av_seff_av_AbstractInternalControlFlowAction = Class(name="pcm::av::seff::av::AbstractInternalControlFlowAction")
AbstractAction = Class(name="AbstractAction")
pcm_av_seff_av_AbstractAction = Class(name="pcm::av::seff::av::AbstractAction")
CommunicationLinkResourceType = Class(name="CommunicationLinkResourceType")
pcm_av_reliability_av_ExternalFailureOccurrenceDescription = Class(name="pcm::av::reliability::av::ExternalFailureOccurrenceDescription")
AbstractLoopAction = Class(name="AbstractLoopAction")
AbstractBranchTransition = Class(name="AbstractBranchTransition")
pcm_av_seff_av_AbstractLoopAction = Class(name="pcm::av::seff::av::AbstractLoopAction")
pcm_av_seff_av_AbstractBranchTransition = Class(name="pcm::av::seff::av::AbstractBranchTransition")
BranchAction = Class(name="BranchAction")
pcm_av_seff_av_BranchAction = Class(name="pcm::av::seff::av::BranchAction")
ResourceDemandingBehaviour = Class(name="ResourceDemandingBehaviour")
pcm_av_seff_av_ResourceDemandingBehaviour = Class(name="pcm::av::seff::av::ResourceDemandingBehaviour")
pcm_av_seff_av_CallAction = Class(name="pcm::av::seff::av::CallAction")
pcm_av_seff_av_StartAction = Class(name="pcm::av::seff::av::StartAction")
pcm_av_seff_av_ServiceEffectSpecification = Class(name="pcm::av::seff::av::ServiceEffectSpecification")
pcm_av_seff_av_ResourceDemandingSEFF = Class(name="pcm::av::seff::av::ResourceDemandingSEFF")
seff_av_ServiceEffectSpecification = Class(name="seff::av::ServiceEffectSpecification")
seff_av_ResourceDemandingBehaviour = Class(name="seff::av::ResourceDemandingBehaviour")
pcm_av_seff_av_ReleaseAction = Class(name="pcm::av::seff::av::ReleaseAction")
pcm_av_seff_av_LoopAction = Class(name="pcm::av::seff::av::LoopAction")
pcm_av_seff_av_ForkAction = Class(name="pcm::av::seff::av::ForkAction")
ForkedBehaviour = Class(name="ForkedBehaviour")
pcm_av_seff_av_ForkedBehaviour = Class(name="pcm::av::seff::av::ForkedBehaviour")
ForkAction = Class(name="ForkAction")
pcm_av_seff_av_SynchronisationPoint = Class(name="pcm::av::seff::av::SynchronisationPoint")
pcm_av_seff_av_ExternalCallAction = Class(name="pcm::av::seff::av::ExternalCallAction")
seff_av_AbstractAction = Class(name="seff::av::AbstractAction")
seff_av_CallReturnAction = Class(name="seff::av::CallReturnAction")
seff_reliability_av_FailureHandlingEntity = Class(name="seff::reliability::av::FailureHandlingEntity")
ResourceDemandingInternalBehaviour = Class(name="ResourceDemandingInternalBehaviour")
pcm_av_seff_av_ResourceDemandingInternalBehaviour = Class(name="pcm::av::seff::av::ResourceDemandingInternalBehaviour")
ResourceDemandingSEFF = Class(name="ResourceDemandingSEFF")
pcm_av_seff_av_CallReturnAction = Class(name="pcm::av::seff::av::CallReturnAction")
pcm_av_seff_av_ProbabilisticBranchTransition = Class(name="pcm::av::seff::av::ProbabilisticBranchTransition")
pcm_av_seff_av_AcquireAction = Class(name="pcm::av::seff::av::AcquireAction")
pcm_av_seff_av_CollectionIteratorAction = Class(name="pcm::av::seff::av::CollectionIteratorAction")
pcm_av_seff_av_GuardedBranchTransition = Class(name="pcm::av::seff::av::GuardedBranchTransition")
pcm_av_seff_av_SetVariableAction = Class(name="pcm::av::seff::av::SetVariableAction")
pcm_av_seff_av_InternalCallAction = Class(name="pcm::av::seff::av::InternalCallAction")
seff_av_CallAction = Class(name="seff::av::CallAction")
seff_av_AbstractInternalControlFlowAction = Class(name="seff::av::AbstractInternalControlFlowAction")
pcm_av_seff_av_EmitEventAction = Class(name="pcm::av::seff::av::EmitEventAction")
pcm_av_seff_av_InternalAction = Class(name="pcm::av::seff::av::InternalAction")
pcm_av_seff_performance_av_InfrastructureCall = Class(name="pcm::av::seff::performance::av::InfrastructureCall")
pcm_av_seff_performance_av_ResourceCall = Class(name="pcm::av::seff::performance::av::ResourceCall")
pcm_av_seff_performance_av_ParametricResourceDemand = Class(name="pcm::av::seff::performance::av::ParametricResourceDemand")
pcm_av_seff_reliability_av_RecoveryActionBehaviour = Class(name="pcm::av::seff::reliability::av::RecoveryActionBehaviour")
seff_reliability_av_RecoveryAction = Class(name="seff::reliability::av::RecoveryAction")
pcm_av_seff_reliability_av_RecoveryAction = Class(name="pcm::av::seff::reliability::av::RecoveryAction")
pcm_av_seff_reliability_av_FailureHandlingEntity = Class(name="pcm::av::seff::reliability::av::FailureHandlingEntity")
pcm_av_qosannotations_av_SpecifiedQoSAnnotation = Class(name="pcm::av::qosannotations::av::SpecifiedQoSAnnotation")
QoSAnnotations = Class(name="QoSAnnotations")
pcm_av_qosannotations_av_QoSAnnotations = Class(name="pcm::av::qosannotations::av::QoSAnnotations")
seff_reliability_av_RecoveryActionBehaviour = Class(name="seff::reliability::av::RecoveryActionBehaviour")
SpecifiedQoSAnnotation = Class(name="SpecifiedQoSAnnotation")
pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction = Class(name="pcm::av::qosannotations::av::SpecifiedOutputParameterAbstraction")
pcm_av_qos_performance_av_SystemSpecifiedExecutionTime = Class(name="pcm::av::qos::performance::av::SystemSpecifiedExecutionTime")
SpecifiedExecutionTime = Class(name="SpecifiedExecutionTime")
pcm_av_qos_performance_av_SpecifiedExecutionTime = Class(name="pcm::av::qos::performance::av::SpecifiedExecutionTime")
pcm_av_qos_performance_av_ComponentSpecifiedExecutionTime = Class(name="pcm::av::qos::performance::av::ComponentSpecifiedExecutionTime")
System = Class(name="System")
ExternalFailureOccurrenceDescription = Class(name="ExternalFailureOccurrenceDescription")
pcm_av_system_av_System = Class(name="pcm::av::system::av::System")
pcm_av_resourceenvironment_av_ResourceEnvironment = Class(name="pcm::av::resourceenvironment::av::ResourceEnvironment")
pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation = Class(name="pcm::av::qos::reliability::av::SpecifiedReliabilityAnnotation")
ResourceContainer = Class(name="ResourceContainer")
pcm_av_resourceenvironment_av_LinkingResource = Class(name="pcm::av::resourceenvironment::av::LinkingResource")
ResourceEnvironment = Class(name="ResourceEnvironment")
pcm_av_resourceenvironment_av_ResourceContainer = Class(name="pcm::av::resourceenvironment::av::ResourceContainer")
pcm_av_resourceenvironment_av_ProcessingResourceSpecification = Class(name="pcm::av::resourceenvironment::av::ProcessingResourceSpecification")
LinkingResource = Class(name="LinkingResource")
pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification = Class(name="pcm::av::resourceenvironment::av::CommunicationLinkResourceSpecification")
pcm_av_allocation_av_AllocationContext = Class(name="pcm::av::allocation::av::AllocationContext")
pcm_av_allocation_av_Allocation = Class(name="pcm::av::allocation::av::Allocation")
AllocationContext = Class(name="AllocationContext")
pcm_av_subsystem_av_SubSystem = Class(name="pcm::av::subsystem::av::SubSystem")
repository_av_RepositoryComponent = Class(name="repository::av::RepositoryComponent")
pcm_av_completions_av_Completion = Class(name="pcm::av::completions::av::Completion")
pcm_av_completions_av_CompletionRepository = Class(name="pcm::av::completions::av::CompletionRepository")
Completion = Class(name="Completion")
Allocation = Class(name="Allocation")
pcm_av_completions_av_DelegatingExternalCallAction = Class(name="pcm::av::completions::av::DelegatingExternalCallAction")
ExternalCallAction = Class(name="ExternalCallAction")
pcm_av_completions_av_NetworkDemandParametricResourceDemand = Class(name="pcm::av::completions::av::NetworkDemandParametricResourceDemand")
ParametricResourceDemand = Class(name="ParametricResourceDemand")

# pcm_av_DummyClass class attributes and methods

# pcm_av_Advice class attributes and methods

# pcm_av_EObject class attributes and methods

# pcm_av_GlobalScope class attributes and methods

# pcm_av_PerJoinPointScope class attributes and methods

# pcm_av_core_av_PCMRandomVariable class attributes and methods
pcm_av_core_av_PCMRandomVariable_m_SpecificationMustNotBeNULL: Method = Method(name="SpecificationMustNotBeNULL", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_core_av_PCMRandomVariable.methods={pcm_av_core_av_PCMRandomVariable_m_SpecificationMustNotBeNULL}

# RandomVariable class attributes and methods

# ClosedWorkload class attributes and methods

# PassiveResource class attributes and methods

# VariableCharacterisation class attributes and methods

# seff_performance_av_InfrastructureCall class attributes and methods

# seff_performance_av_ResourceCall class attributes and methods

# seff_performance_av_ParametricResourceDemand class attributes and methods

# LoopAction class attributes and methods

# GuardedBranchTransition class attributes and methods

# qos_performance_av_SpecifiedExecutionTime class attributes and methods

# composition_av_EventChannelSinkConnector class attributes and methods

# OpenWorkload class attributes and methods

# Delay class attributes and methods

# CommunicationLinkResourceSpecification class attributes and methods

# ProcessingResourceSpecification class attributes and methods

# pcm_av_entity_av_ResourceProvidedRole class attributes and methods

# Role class attributes and methods

# entity_av_ResourceInterfaceProvidingEntity class attributes and methods

# ResourceInterface class attributes and methods

# pcm_av_entity_av_InterfaceProvidingRequiringEntity class attributes and methods

# entity_av_InterfaceProvidingEntity class attributes and methods

# entity_av_InterfaceRequiringEntity class attributes and methods

# pcm_av_entity_av_InterfaceProvidingEntity class attributes and methods

# Entity class attributes and methods

# ProvidedRole class attributes and methods

# pcm_av_entity_av_InterfaceRequiringEntity class attributes and methods

# entity_av_Entity class attributes and methods

# entity_av_ResourceInterfaceRequiringEntity class attributes and methods

# RequiredRole class attributes and methods

# pcm_av_entity_av_ResourceInterfaceRequiringEntity class attributes and methods

# entity_av_ResourceRequiredRole class attributes and methods

# pcm_av_entity_av_ResourceRequiredRole class attributes and methods

# pcm_av_entity_av_ResourceInterfaceProvidingEntity class attributes and methods

# composition_av_AssemblyEventConnector class attributes and methods

# Loop class attributes and methods

# pcm_av_entity_av_NamedElement class attributes and methods
pcm_av_entity_av_NamedElement_entityName: Property = Property(name="entityName", type=StringType)
pcm_av_entity_av_NamedElement.attributes={pcm_av_entity_av_NamedElement_entityName}

# pcm_av_entity_av_ResourceInterfaceProvidingRequiringEntity class attributes and methods

# pcm_av_entity_av_Entity class attributes and methods

# Identifier class attributes and methods

# entity_av_NamedElement class attributes and methods

# pcm_av_composition_av_DelegationConnector class attributes and methods

# Connector class attributes and methods

# pcm_av_composition_av_Connector class attributes and methods

# pcm_av_composition_av_ComposedStructure class attributes and methods
pcm_av_composition_av_ComposedStructure_m_MultipleConnectorsConstraint: Method = Method(name="MultipleConnectorsConstraint", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_composition_av_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors: Method = Method(name="MultipleConnectorsConstraintForAssemblyConnectors", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_composition_av_ComposedStructure.methods={pcm_av_composition_av_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors, pcm_av_composition_av_ComposedStructure_m_MultipleConnectorsConstraint}

# composition_av_AssemblyContext class attributes and methods

# composition_av_ResourceRequiredDelegationConnector class attributes and methods

# entity_av_ResourceProvidedRole class attributes and methods

# pcm_av_entity_av_ComposedProvidingRequiringEntity class attributes and methods
pcm_av_entity_av_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound: Method = Method(name="ProvidedRolesMustBeBound", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_entity_av_ComposedProvidingRequiringEntity.methods={pcm_av_entity_av_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound}

# composition_av_ComposedStructure class attributes and methods

# entity_av_InterfaceProvidingRequiringEntity class attributes and methods

# pcm_av_composition_av_ResourceRequiredDelegationConnector class attributes and methods

# pcm_av_composition_av_EventChannel class attributes and methods

# EventGroup class attributes and methods

# composition_av_EventChannelSourceConnector class attributes and methods

# pcm_av_composition_av_EventChannelSourceConnector class attributes and methods

# SourceRole class attributes and methods

# pcm_av_composition_av_EventChannelSinkConnector class attributes and methods

# SinkRole class attributes and methods

# PCMRandomVariable class attributes and methods

# pcm_av_composition_av_ProvidedDelegationConnector class attributes and methods
pcm_av_composition_av_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_composition_av_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_composition_av_ProvidedDelegationConnector.methods={pcm_av_composition_av_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure, pcm_av_composition_av_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame}

# DelegationConnector class attributes and methods

# composition_av_EventChannel class attributes and methods

# OperationProvidedRole class attributes and methods

# composition_av_Connector class attributes and methods

# pcm_av_composition_av_RequiredDelegationConnector class attributes and methods
pcm_av_composition_av_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_composition_av_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_composition_av_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector: Method = Method(name="RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_composition_av_RequiredDelegationConnector.methods={pcm_av_composition_av_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector, pcm_av_composition_av_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame, pcm_av_composition_av_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure}

# OperationRequiredRole class attributes and methods

# pcm_av_composition_av_AssemblyConnector class attributes and methods
pcm_av_composition_av_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_composition_av_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch: Method = Method(name="AssemblyConnectorsReferencedInterfacesMustMatch", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_composition_av_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_composition_av_AssemblyConnector.methods={pcm_av_composition_av_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch, pcm_av_composition_av_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch, pcm_av_composition_av_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch}

# pcm_av_composition_av_AssemblyEventConnector class attributes and methods

# pcm_av_composition_av_SourceDelegationConnector class attributes and methods

# pcm_av_composition_av_AssemblyInfrastructureConnector class attributes and methods

# InfrastructureProvidedRole class attributes and methods

# InfrastructureRequiredRole class attributes and methods

# pcm_av_composition_av_ProvidedInfrastructureDelegationConnector class attributes and methods

# pcm_av_composition_av_RequiredInfrastructureDelegationConnector class attributes and methods

# pcm_av_composition_av_RequiredResourceDelegationConnector class attributes and methods

# pcm_av_composition_av_SinkDelegationConnector class attributes and methods

# pcm_av_usagemodel_av_Workload class attributes and methods

# UsageScenario class attributes and methods

# pcm_av_usagemodel_av_UsageScenario class attributes and methods

# UsageModel class attributes and methods

# ScenarioBehaviour class attributes and methods

# Workload class attributes and methods

# pcm_av_usagemodel_av_UserData class attributes and methods

# pcm_av_usagemodel_av_UsageModel class attributes and methods

# UserData class attributes and methods

# pcm_av_composition_av_AssemblyContext class attributes and methods

# RepositoryComponent class attributes and methods

# VariableUsage class attributes and methods

# OperationSignature class attributes and methods

# pcm_av_usagemodel_av_AbstractUserAction class attributes and methods

# pcm_av_usagemodel_av_ScenarioBehaviour class attributes and methods
pcm_av_usagemodel_av_ScenarioBehaviour_m_Exactlyonestart: Method = Method(name="Exactlyonestart", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_usagemodel_av_ScenarioBehaviour_m_Exactlyonestop: Method = Method(name="Exactlyonestop", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_usagemodel_av_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor: Method = Method(name="EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_usagemodel_av_ScenarioBehaviour.methods={pcm_av_usagemodel_av_ScenarioBehaviour_m_Exactlyonestart, pcm_av_usagemodel_av_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor, pcm_av_usagemodel_av_ScenarioBehaviour_m_Exactlyonestop}

# pcm_av_usagemodel_av_EntryLevelSystemCall class attributes and methods
pcm_av_usagemodel_av_EntryLevelSystemCall_priority: Property = Property(name="priority", type=IntegerType)
pcm_av_usagemodel_av_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole: Method = Method(name="EntryLevelSystemCallSignatureMustMatchItsProvidedRole", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_usagemodel_av_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem: Method = Method(name="EntryLevelSystemCallMustReferenceProvidedRoleOfASystem", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_usagemodel_av_EntryLevelSystemCall.attributes={pcm_av_usagemodel_av_EntryLevelSystemCall_priority}
pcm_av_usagemodel_av_EntryLevelSystemCall.methods={pcm_av_usagemodel_av_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem, pcm_av_usagemodel_av_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole}

# AbstractUserAction class attributes and methods

# BranchTransition class attributes and methods

# pcm_av_usagemodel_av_BranchTransition class attributes and methods
pcm_av_usagemodel_av_BranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_av_usagemodel_av_BranchTransition.attributes={pcm_av_usagemodel_av_BranchTransition_branchProbability}

# Branch class attributes and methods

# pcm_av_usagemodel_av_Branch class attributes and methods
pcm_av_usagemodel_av_Branch_m_AllBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_usagemodel_av_Branch.methods={pcm_av_usagemodel_av_Branch_m_AllBranchProbabilitiesMustSumUpTo1}

# pcm_av_usagemodel_av_Loop class attributes and methods

# pcm_av_usagemodel_av_Start class attributes and methods
pcm_av_usagemodel_av_Start_m_StartHasNoPredecessor: Method = Method(name="StartHasNoPredecessor", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_usagemodel_av_Start.methods={pcm_av_usagemodel_av_Start_m_StartHasNoPredecessor}

# pcm_av_usagemodel_av_OpenWorkload class attributes and methods
pcm_av_usagemodel_av_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified: Method = Method(name="InterArrivalTimeInOpenWorkloadNeedsToBeSpecified", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_usagemodel_av_OpenWorkload.methods={pcm_av_usagemodel_av_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified}

# pcm_av_usagemodel_av_Delay class attributes and methods

# pcm_av_usagemodel_av_ClosedWorkload class attributes and methods
pcm_av_usagemodel_av_ClosedWorkload_population: Property = Property(name="population", type=IntegerType)
pcm_av_usagemodel_av_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified: Method = Method(name="PopulationInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_usagemodel_av_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified: Method = Method(name="ThinkTimeInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_usagemodel_av_ClosedWorkload.attributes={pcm_av_usagemodel_av_ClosedWorkload_population}
pcm_av_usagemodel_av_ClosedWorkload.methods={pcm_av_usagemodel_av_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified, pcm_av_usagemodel_av_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified}

# pcm_av_usagemodel_av_Stop class attributes and methods
pcm_av_usagemodel_av_Stop_m_StopHasNoSuccessor: Method = Method(name="StopHasNoSuccessor", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_usagemodel_av_Stop.methods={pcm_av_usagemodel_av_Stop_m_StopHasNoSuccessor}

# pcm_av_repository_av_PassiveResource class attributes and methods

# BasicComponent class attributes and methods

# ResourceTimeoutFailureType class attributes and methods

# pcm_av_repository_av_BasicComponent class attributes and methods
pcm_av_repository_av_BasicComponent_m_NoSeffTypeUsedTwice: Method = Method(name="NoSeffTypeUsedTwice", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_repository_av_BasicComponent_m_ProvideSameInterfacesAsImplementationType: Method = Method(name="ProvideSameInterfacesAsImplementationType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_repository_av_BasicComponent_m_RequireSameInterfacesAsImplementationType: Method = Method(name="RequireSameInterfacesAsImplementationType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_repository_av_BasicComponent.methods={pcm_av_repository_av_BasicComponent_m_NoSeffTypeUsedTwice, pcm_av_repository_av_BasicComponent_m_RequireSameInterfacesAsImplementationType, pcm_av_repository_av_BasicComponent_m_ProvideSameInterfacesAsImplementationType}

# ImplementationComponentType class attributes and methods

# ServiceEffectSpecification class attributes and methods

# CompleteComponentType class attributes and methods

# pcm_av_repository_av_RepositoryComponent class attributes and methods

# InterfaceProvidingRequiringEntity class attributes and methods

# Repository class attributes and methods

# pcm_av_repository_av_ProvidedRole class attributes and methods

# pcm_av_repository_av_ImplementationComponentType class attributes and methods
pcm_av_repository_av_ImplementationComponentType_componentType: Property = Property(name="componentType", type=StringType)
pcm_av_repository_av_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType: Method = Method(name="RequiredInterfacesHaveToConformToCompleteType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_repository_av_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType: Method = Method(name="providedInterfacesHaveToConformToCompleteType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_repository_av_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType: Method = Method(name="ProvidedInterfaceHaveToConformToComponentType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_repository_av_ImplementationComponentType.attributes={pcm_av_repository_av_ImplementationComponentType_componentType}
pcm_av_repository_av_ImplementationComponentType.methods={pcm_av_repository_av_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType, pcm_av_repository_av_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType, pcm_av_repository_av_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType}

# EventType class attributes and methods

# ResourceSignature class attributes and methods

# pcm_av_repository_av_DataType class attributes and methods

# pcm_av_repository_av_Repository class attributes and methods
pcm_av_repository_av_Repository_repositoryDescription: Property = Property(name="repositoryDescription", type=StringType)
pcm_av_repository_av_Repository.attributes={pcm_av_repository_av_Repository_repositoryDescription}

# Interface class attributes and methods

# FailureType class attributes and methods

# pcm_av_repository_av_Interface class attributes and methods
pcm_av_repository_av_Interface_m_NoProtocolTypeIDUsedTwice: Method = Method(name="NoProtocolTypeIDUsedTwice", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_repository_av_Interface.methods={pcm_av_repository_av_Interface_m_NoProtocolTypeIDUsedTwice}

# pcm_av_repository_av_Parameter class attributes and methods
pcm_av_repository_av_Parameter_parameterName: Property = Property(name="parameterName", type=StringType)
pcm_av_repository_av_Parameter_modifier__Parameter: Property = Property(name="modifier__Parameter", type=StringType)
pcm_av_repository_av_Parameter.attributes={pcm_av_repository_av_Parameter_parameterName, pcm_av_repository_av_Parameter_modifier__Parameter}

# DataType class attributes and methods

# InfrastructureSignature class attributes and methods

# Protocol class attributes and methods

# RequiredCharacterisation class attributes and methods

# pcm_av_repository_av_RequiredCharacterisation class attributes and methods
pcm_av_repository_av_RequiredCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_av_repository_av_RequiredCharacterisation.attributes={pcm_av_repository_av_RequiredCharacterisation_type}

# Parameter class attributes and methods

# pcm_av_repository_av_EventGroup class attributes and methods

# pcm_av_repository_av_Signature class attributes and methods

# ExceptionType class attributes and methods

# pcm_av_repository_av_ExceptionType class attributes and methods
pcm_av_repository_av_ExceptionType_exceptionName: Property = Property(name="exceptionName", type=StringType)
pcm_av_repository_av_ExceptionType_exceptionMessage: Property = Property(name="exceptionMessage", type=StringType)
pcm_av_repository_av_ExceptionType.attributes={pcm_av_repository_av_ExceptionType_exceptionName, pcm_av_repository_av_ExceptionType_exceptionMessage}

# pcm_av_repository_av_InfrastructureSignature class attributes and methods

# InfrastructureInterface class attributes and methods

# pcm_av_repository_av_InfrastructureInterface class attributes and methods

# pcm_av_repository_av_EventType class attributes and methods

# Signature class attributes and methods

# pcm_av_repository_av_InfrastructureRequiredRole class attributes and methods

# pcm_av_repository_av_RequiredRole class attributes and methods

# pcm_av_repository_av_OperationSignature class attributes and methods
pcm_av_repository_av_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature: Method = Method(name="ParameterNamesHaveToBeUniqueForASignature", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_repository_av_OperationSignature.methods={pcm_av_repository_av_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature}

# OperationInterface class attributes and methods

# pcm_av_repository_av_OperationRequiredRole class attributes and methods

# pcm_av_repository_av_SourceRole class attributes and methods

# pcm_av_repository_av_SinkRole class attributes and methods

# pcm_av_repository_av_OperationProvidedRole class attributes and methods

# pcm_av_repository_av_InfrastructureProvidedRole class attributes and methods

# pcm_av_repository_av_CompleteComponentType class attributes and methods
pcm_av_repository_av_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_repository_av_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2: Method = Method(name="providedInterfacesHaveToConformToProvidedType2", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_repository_av_CompleteComponentType.methods={pcm_av_repository_av_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2, pcm_av_repository_av_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType}

# pcm_av_repository_av_OperationInterface class attributes and methods
pcm_av_repository_av_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface: Method = Method(name="SignaturesHaveToBeUniqueForAnInterface", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_repository_av_OperationInterface.methods={pcm_av_repository_av_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface}

# ProvidesComponentType class attributes and methods

# pcm_av_repository_av_ProvidesComponentType class attributes and methods
pcm_av_repository_av_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_repository_av_ProvidesComponentType.methods={pcm_av_repository_av_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType}

# pcm_av_repository_av_CompositeComponent class attributes and methods
pcm_av_repository_av_CompositeComponent_m_ProvideSameInterfaces: Method = Method(name="ProvideSameInterfaces", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_repository_av_CompositeComponent_m_RequireSameInterfaces: Method = Method(name="RequireSameInterfaces", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_repository_av_CompositeComponent.methods={pcm_av_repository_av_CompositeComponent_m_RequireSameInterfaces, pcm_av_repository_av_CompositeComponent_m_ProvideSameInterfaces}

# entity_av_ComposedProvidingRequiringEntity class attributes and methods

# repository_av_ImplementationComponentType class attributes and methods

# pcm_av_repository_av_PrimitiveDataType class attributes and methods
pcm_av_repository_av_PrimitiveDataType_type: Property = Property(name="type", type=StringType)
pcm_av_repository_av_PrimitiveDataType.attributes={pcm_av_repository_av_PrimitiveDataType_type}

# pcm_av_repository_av_CollectionDataType class attributes and methods

# repository_av_DataType class attributes and methods

# pcm_av_repository_av_CompositeDataType class attributes and methods

# CompositeDataType class attributes and methods

# InnerDeclaration class attributes and methods

# pcm_av_repository_av_InnerDeclaration class attributes and methods

# NamedElement class attributes and methods

# pcm_av_repository_av_Role class attributes and methods

# pcm_av_resourcetype_av_ResourceSignature class attributes and methods
pcm_av_resourcetype_av_ResourceSignature_resourceServiceId: Property = Property(name="resourceServiceId", type=IntegerType)
pcm_av_resourcetype_av_ResourceSignature.attributes={pcm_av_resourcetype_av_ResourceSignature_resourceServiceId}

# ResourceRepository class attributes and methods

# pcm_av_resourcetype_av_ResourceRepository class attributes and methods

# SchedulingPolicy class attributes and methods

# pcm_av_resourcetype_av_SchedulingPolicy class attributes and methods

# pcm_av_resourcetype_av_CommunicationLinkResourceType class attributes and methods

# NetworkInducedFailureType class attributes and methods

# pcm_av_resourcetype_av_ResourceInterface class attributes and methods

# pcm_av_protocol_av_Protocol class attributes and methods
pcm_av_protocol_av_Protocol_protocolTypeID: Property = Property(name="protocolTypeID", type=StringType)
pcm_av_protocol_av_Protocol.attributes={pcm_av_protocol_av_Protocol_protocolTypeID}

# pcm_av_parameter_av_VariableUsage class attributes and methods

# pcm_av_resourcetype_av_ProcessingResourceType class attributes and methods

# ResourceType class attributes and methods

# HardwareInducedFailureType class attributes and methods

# pcm_av_resourcetype_av_ResourceType class attributes and methods

# UnitCarryingElement class attributes and methods

# SpecifiedOutputParameterAbstraction class attributes and methods

# EntryLevelSystemCall class attributes and methods

# parameter_av_pcm_av_AbstractNamedReference class attributes and methods

# pcm_av_parameter_av_VariableCharacterisation class attributes and methods
pcm_av_parameter_av_VariableCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_av_parameter_av_VariableCharacterisation.attributes={pcm_av_parameter_av_VariableCharacterisation_type}

# pcm_av_parameter_av_CharacterisedVariable class attributes and methods
pcm_av_parameter_av_CharacterisedVariable_characterisationType: Property = Property(name="characterisationType", type=StringType)
pcm_av_parameter_av_CharacterisedVariable.attributes={pcm_av_parameter_av_CharacterisedVariable_characterisationType}

# Variable class attributes and methods

# pcm_av_reliability_av_FailureOccurrenceDescription class attributes and methods
pcm_av_reliability_av_FailureOccurrenceDescription_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_av_reliability_av_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange: Method = Method(name="EnsureValidFailureProbabilityRange", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_reliability_av_FailureOccurrenceDescription.attributes={pcm_av_reliability_av_FailureOccurrenceDescription_failureProbability}
pcm_av_reliability_av_FailureOccurrenceDescription.methods={pcm_av_reliability_av_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange}

# CallAction class attributes and methods

# SynchronisationPoint class attributes and methods

# CallReturnAction class attributes and methods

# SetVariableAction class attributes and methods

# pcm_av_reliability_av_HardwareInducedFailureType class attributes and methods
pcm_av_reliability_av_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType: Method = Method(name="HardwareInducedFailureTypeHasProcessingResourceType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_reliability_av_HardwareInducedFailureType.methods={pcm_av_reliability_av_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType}

# ProcessingResourceType class attributes and methods

# pcm_av_reliability_av_SoftwareInducedFailureType class attributes and methods

# InternalFailureOccurrenceDescription class attributes and methods

# pcm_av_reliability_av_InternalFailureOccurrenceDescription class attributes and methods
pcm_av_reliability_av_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_reliability_av_InternalFailureOccurrenceDescription.methods={pcm_av_reliability_av_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription}

# FailureOccurrenceDescription class attributes and methods

# InternalAction class attributes and methods

# SoftwareInducedFailureType class attributes and methods

# pcm_av_reliability_av_NetworkInducedFailureType class attributes and methods
pcm_av_reliability_av_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType: Method = Method(name="NetworkInducedFailureTypeHasCommunicationLinkResourceType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_reliability_av_NetworkInducedFailureType.methods={pcm_av_reliability_av_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType}

# qos_reliability_av_SpecifiedReliabilityAnnotation class attributes and methods

# pcm_av_reliability_av_ResourceTimeoutFailureType class attributes and methods

# pcm_av_reliability_av_FailureType class attributes and methods

# pcm_av_seff_av_StopAction class attributes and methods
pcm_av_seff_av_StopAction_m_StopActionSuccessorMustNotBeDefined: Method = Method(name="StopActionSuccessorMustNotBeDefined", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_seff_av_StopAction.methods={pcm_av_seff_av_StopAction_m_StopActionSuccessorMustNotBeDefined}

# AbstractInternalControlFlowAction class attributes and methods

# pcm_av_seff_av_AbstractInternalControlFlowAction class attributes and methods

# AbstractAction class attributes and methods

# pcm_av_seff_av_AbstractAction class attributes and methods

# CommunicationLinkResourceType class attributes and methods

# pcm_av_reliability_av_ExternalFailureOccurrenceDescription class attributes and methods
pcm_av_reliability_av_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_reliability_av_ExternalFailureOccurrenceDescription.methods={pcm_av_reliability_av_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription}

# AbstractLoopAction class attributes and methods

# AbstractBranchTransition class attributes and methods

# pcm_av_seff_av_AbstractLoopAction class attributes and methods

# pcm_av_seff_av_AbstractBranchTransition class attributes and methods

# BranchAction class attributes and methods

# pcm_av_seff_av_BranchAction class attributes and methods
pcm_av_seff_av_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllProbabilisticBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_seff_av_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions: Method = Method(name="EitherGuardedBranchesOrProbabilisiticBranchTransitions", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_seff_av_BranchAction.methods={pcm_av_seff_av_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions, pcm_av_seff_av_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1}

# ResourceDemandingBehaviour class attributes and methods

# pcm_av_seff_av_ResourceDemandingBehaviour class attributes and methods
pcm_av_seff_av_ResourceDemandingBehaviour_m_ExactlyOneStopAction: Method = Method(name="ExactlyOneStopAction", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_seff_av_ResourceDemandingBehaviour_m_ExactlyOneStartAction: Method = Method(name="ExactlyOneStartAction", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_seff_av_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor: Method = Method(name="EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_seff_av_ResourceDemandingBehaviour.methods={pcm_av_seff_av_ResourceDemandingBehaviour_m_ExactlyOneStopAction, pcm_av_seff_av_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor, pcm_av_seff_av_ResourceDemandingBehaviour_m_ExactlyOneStartAction}

# pcm_av_seff_av_CallAction class attributes and methods

# pcm_av_seff_av_StartAction class attributes and methods
pcm_av_seff_av_StartAction_m_StartActionPredecessorMustNotBeDefined: Method = Method(name="StartActionPredecessorMustNotBeDefined", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_seff_av_StartAction.methods={pcm_av_seff_av_StartAction_m_StartActionPredecessorMustNotBeDefined}

# pcm_av_seff_av_ServiceEffectSpecification class attributes and methods
pcm_av_seff_av_ServiceEffectSpecification_seffTypeID: Property = Property(name="seffTypeID", type=StringType)
pcm_av_seff_av_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole: Method = Method(name="ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_seff_av_ServiceEffectSpecification.attributes={pcm_av_seff_av_ServiceEffectSpecification_seffTypeID}
pcm_av_seff_av_ServiceEffectSpecification.methods={pcm_av_seff_av_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole}

# pcm_av_seff_av_ResourceDemandingSEFF class attributes and methods

# seff_av_ServiceEffectSpecification class attributes and methods

# seff_av_ResourceDemandingBehaviour class attributes and methods

# pcm_av_seff_av_ReleaseAction class attributes and methods

# pcm_av_seff_av_LoopAction class attributes and methods

# pcm_av_seff_av_ForkAction class attributes and methods

# ForkedBehaviour class attributes and methods

# pcm_av_seff_av_ForkedBehaviour class attributes and methods

# ForkAction class attributes and methods

# pcm_av_seff_av_SynchronisationPoint class attributes and methods

# pcm_av_seff_av_ExternalCallAction class attributes and methods
pcm_av_seff_av_ExternalCallAction_retryCount: Property = Property(name="retryCount", type=IntegerType)
pcm_av_seff_av_ExternalCallAction_m_SignatureBelongsToRole: Method = Method(name="SignatureBelongsToRole", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_seff_av_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer: Method = Method(name="OperationRequiredRoleMustBeReferencedByContainer", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_seff_av_ExternalCallAction.attributes={pcm_av_seff_av_ExternalCallAction_retryCount}
pcm_av_seff_av_ExternalCallAction.methods={pcm_av_seff_av_ExternalCallAction_m_SignatureBelongsToRole, pcm_av_seff_av_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer}

# seff_av_AbstractAction class attributes and methods

# seff_av_CallReturnAction class attributes and methods

# seff_reliability_av_FailureHandlingEntity class attributes and methods

# ResourceDemandingInternalBehaviour class attributes and methods

# pcm_av_seff_av_ResourceDemandingInternalBehaviour class attributes and methods

# ResourceDemandingSEFF class attributes and methods

# pcm_av_seff_av_CallReturnAction class attributes and methods

# pcm_av_seff_av_ProbabilisticBranchTransition class attributes and methods
pcm_av_seff_av_ProbabilisticBranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_av_seff_av_ProbabilisticBranchTransition.attributes={pcm_av_seff_av_ProbabilisticBranchTransition_branchProbability}

# pcm_av_seff_av_AcquireAction class attributes and methods
pcm_av_seff_av_AcquireAction_timeout: Property = Property(name="timeout", type=BooleanType)
pcm_av_seff_av_AcquireAction_timeoutValue: Property = Property(name="timeoutValue", type=FloatType)
pcm_av_seff_av_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative: Method = Method(name="TimeoutValueOfAcquireActionMustNotBeNegative", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_seff_av_AcquireAction.attributes={pcm_av_seff_av_AcquireAction_timeout, pcm_av_seff_av_AcquireAction_timeoutValue}
pcm_av_seff_av_AcquireAction.methods={pcm_av_seff_av_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative}

# pcm_av_seff_av_CollectionIteratorAction class attributes and methods

# pcm_av_seff_av_GuardedBranchTransition class attributes and methods

# pcm_av_seff_av_SetVariableAction class attributes and methods

# pcm_av_seff_av_InternalCallAction class attributes and methods

# seff_av_CallAction class attributes and methods

# seff_av_AbstractInternalControlFlowAction class attributes and methods

# pcm_av_seff_av_EmitEventAction class attributes and methods

# pcm_av_seff_av_InternalAction class attributes and methods
pcm_av_seff_av_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_seff_av_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfInternalActionFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_seff_av_InternalAction.methods={pcm_av_seff_av_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed, pcm_av_seff_av_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1}

# pcm_av_seff_performance_av_InfrastructureCall class attributes and methods
pcm_av_seff_performance_av_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent: Method = Method(name="ReferencedRequiredRoleMustBeRequiredByComponent", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_seff_performance_av_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_seff_performance_av_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole: Method = Method(name="SignatureMustBelongToUsedRequiredRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_seff_performance_av_InfrastructureCall.methods={pcm_av_seff_performance_av_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent, pcm_av_seff_performance_av_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction, pcm_av_seff_performance_av_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole}

# pcm_av_seff_performance_av_ResourceCall class attributes and methods
pcm_av_seff_performance_av_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole: Method = Method(name="ResourceSignatureBelongsToResourceRequiredRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_seff_performance_av_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent: Method = Method(name="ResourceRequiredRoleMustBeReferencedByComponent", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_seff_performance_av_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_seff_performance_av_ResourceCall.methods={pcm_av_seff_performance_av_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent, pcm_av_seff_performance_av_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole, pcm_av_seff_performance_av_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction}

# pcm_av_seff_performance_av_ParametricResourceDemand class attributes and methods
pcm_av_seff_performance_av_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_seff_performance_av_ParametricResourceDemand.methods={pcm_av_seff_performance_av_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction}

# pcm_av_seff_reliability_av_RecoveryActionBehaviour class attributes and methods
pcm_av_seff_reliability_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor: Method = Method(name="RecoveryActionBehaviourHasOnlyOnePredecessor", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_seff_reliability_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself: Method = Method(name="RecoveryActionBehaviourIsNotSuccessorOfItself", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_seff_reliability_av_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes: Method = Method(name="SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_seff_reliability_av_RecoveryActionBehaviour.methods={pcm_av_seff_reliability_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself, pcm_av_seff_reliability_av_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes, pcm_av_seff_reliability_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor}

# seff_reliability_av_RecoveryAction class attributes and methods

# pcm_av_seff_reliability_av_RecoveryAction class attributes and methods
pcm_av_seff_reliability_av_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet: Method = Method(name="PrimaryBehaviourOfRecoveryActionMustBeSet", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_seff_reliability_av_RecoveryAction.methods={pcm_av_seff_reliability_av_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet}

# pcm_av_seff_reliability_av_FailureHandlingEntity class attributes and methods

# pcm_av_qosannotations_av_SpecifiedQoSAnnotation class attributes and methods

# QoSAnnotations class attributes and methods

# pcm_av_qosannotations_av_QoSAnnotations class attributes and methods
pcm_av_qosannotations_av_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed: Method = Method(name="MultipleReliabilityAnnotationsPerExternalCallNotAllowed", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_qosannotations_av_QoSAnnotations.methods={pcm_av_qosannotations_av_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed}

# seff_reliability_av_RecoveryActionBehaviour class attributes and methods

# SpecifiedQoSAnnotation class attributes and methods

# pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction class attributes and methods

# pcm_av_qos_performance_av_SystemSpecifiedExecutionTime class attributes and methods
pcm_av_qos_performance_av_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem: Method = Method(name="SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_qos_performance_av_SystemSpecifiedExecutionTime.methods={pcm_av_qos_performance_av_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem}

# SpecifiedExecutionTime class attributes and methods

# pcm_av_qos_performance_av_SpecifiedExecutionTime class attributes and methods

# pcm_av_qos_performance_av_ComponentSpecifiedExecutionTime class attributes and methods

# System class attributes and methods

# ExternalFailureOccurrenceDescription class attributes and methods

# pcm_av_system_av_System class attributes and methods
pcm_av_system_av_System_m_SystemMustHaveAtLeastOneProvidedRole: Method = Method(name="SystemMustHaveAtLeastOneProvidedRole", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_system_av_System.methods={pcm_av_system_av_System_m_SystemMustHaveAtLeastOneProvidedRole}

# pcm_av_resourceenvironment_av_ResourceEnvironment class attributes and methods

# pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation class attributes and methods
pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem: Method = Method(name="SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation.methods={pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed, pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem, pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1}

# ResourceContainer class attributes and methods

# pcm_av_resourceenvironment_av_LinkingResource class attributes and methods

# ResourceEnvironment class attributes and methods

# pcm_av_resourceenvironment_av_ResourceContainer class attributes and methods

# pcm_av_resourceenvironment_av_ProcessingResourceSpecification class attributes and methods
pcm_av_resourceenvironment_av_ProcessingResourceSpecification_MTTR: Property = Property(name="MTTR", type=FloatType)
pcm_av_resourceenvironment_av_ProcessingResourceSpecification_MTTF: Property = Property(name="MTTF", type=FloatType)
pcm_av_resourceenvironment_av_ProcessingResourceSpecification_requiredByContainer: Property = Property(name="requiredByContainer", type=BooleanType)
pcm_av_resourceenvironment_av_ProcessingResourceSpecification_numberOfReplicas: Property = Property(name="numberOfReplicas", type=IntegerType)
pcm_av_resourceenvironment_av_ProcessingResourceSpecification.attributes={pcm_av_resourceenvironment_av_ProcessingResourceSpecification_MTTR, pcm_av_resourceenvironment_av_ProcessingResourceSpecification_requiredByContainer, pcm_av_resourceenvironment_av_ProcessingResourceSpecification_numberOfReplicas, pcm_av_resourceenvironment_av_ProcessingResourceSpecification_MTTF}

# LinkingResource class attributes and methods

# pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification class attributes and methods
pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification.attributes={pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification_failureProbability}

# pcm_av_allocation_av_AllocationContext class attributes and methods
pcm_av_allocation_av_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred: Method = Method(name="OneAssemblyContextOrOneEventChannelShouldBeReferred", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_allocation_av_AllocationContext.methods={pcm_av_allocation_av_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred}

# pcm_av_allocation_av_Allocation class attributes and methods
pcm_av_allocation_av_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce: Method = Method(name="EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_allocation_av_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource: Method = Method(name="CommunicatingServersHaveToBeConnectedByLinkingResource", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_allocation_av_Allocation.methods={pcm_av_allocation_av_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce, pcm_av_allocation_av_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource}

# AllocationContext class attributes and methods

# pcm_av_subsystem_av_SubSystem class attributes and methods

# repository_av_RepositoryComponent class attributes and methods

# pcm_av_completions_av_Completion class attributes and methods

# pcm_av_completions_av_CompletionRepository class attributes and methods

# Completion class attributes and methods

# Allocation class attributes and methods

# pcm_av_completions_av_DelegatingExternalCallAction class attributes and methods

# ExternalCallAction class attributes and methods

# pcm_av_completions_av_NetworkDemandParametricResourceDemand class attributes and methods

# ParametricResourceDemand class attributes and methods

# Relationships
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="pcm_av_EObject", type=pcm_av_Advice, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_Advice", type=pcm_av_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scopedObject1: BinaryAssociation = BinaryAssociation(
    name="scopedObject1",
    ends={
        Property(name="pcm_av_EObject2", type=pcm_av_GlobalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_GlobalScope", type=pcm_av_EObject, multiplicity=Multiplicity(1, 1))
    }
)
scopedObject3: BinaryAssociation = BinaryAssociation(
    name="scopedObject3",
    ends={
        Property(name="pcm_av_EObject4", type=pcm_av_PerJoinPointScope, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_PerJoinPointScope", type=pcm_av_EObject, multiplicity=Multiplicity(1, 1))
    }
)
closedWorkload_PCMRandomVariable5: BinaryAssociation = BinaryAssociation(
    name="closedWorkload_PCMRandomVariable5",
    ends={
        Property(name="usagemodel_av", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ClosedWorkload", type=ClosedWorkload, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_capacity_PCMRandomVariable6: BinaryAssociation = BinaryAssociation(
    name="passiveResource_capacity_PCMRandomVariable6",
    ends={
        Property(name="repository_av", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
variableCharacterisation_Specification7: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_Specification7",
    ends={
        Property(name="parameter_av", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableCharacterisation", type=VariableCharacterisation, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureCall__PCMRandomVariable8: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__PCMRandomVariable8",
    ends={
        Property(name="seff_av", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_av", type=seff_performance_av_InfrastructureCall, multiplicity=Multiplicity(0, 1))
    }
)
resourceCall__PCMRandomVariable9: BinaryAssociation = BinaryAssociation(
    name="resourceCall__PCMRandomVariable9",
    ends={
        Property(name="seff_av11", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_av10", type=seff_performance_av_ResourceCall, multiplicity=Multiplicity(0, 1))
    }
)
parametricResourceDemand_PCMRandomVariable12: BinaryAssociation = BinaryAssociation(
    name="parametricResourceDemand_PCMRandomVariable12",
    ends={
        Property(name="seff_av14", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_av13", type=seff_performance_av_ParametricResourceDemand, multiplicity=Multiplicity(0, 1))
    }
)
loopAction_PCMRandomVariable15: BinaryAssociation = BinaryAssociation(
    name="loopAction_PCMRandomVariable15",
    ends={
        Property(name="seff_av16", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopAction", type=LoopAction, multiplicity=Multiplicity(0, 1))
    }
)
guardedBranchTransition_PCMRandomVariable17: BinaryAssociation = BinaryAssociation(
    name="guardedBranchTransition_PCMRandomVariable17",
    ends={
        Property(name="seff_av18", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="GuardedBranchTransition", type=GuardedBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
specifiedExecutionTime_PCMRandomVariable19: BinaryAssociation = BinaryAssociation(
    name="specifiedExecutionTime_PCMRandomVariable19",
    ends={
        Property(name="qosannotations_av", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="qos_performance_av", type=qos_performance_av_SpecifiedExecutionTime, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSinkConnector__FilterCondition20: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__FilterCondition20",
    ends={
        Property(name="core_av", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av", type=composition_av_EventChannelSinkConnector, multiplicity=Multiplicity(0, 1))
    }
)
openWorkload_PCMRandomVariable26: BinaryAssociation = BinaryAssociation(
    name="openWorkload_PCMRandomVariable26",
    ends={
        Property(name="usagemodel_av27", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="OpenWorkload", type=OpenWorkload, multiplicity=Multiplicity(0, 1))
    }
)
delay_TimeSpecification28: BinaryAssociation = BinaryAssociation(
    name="delay_TimeSpecification28",
    ends={
        Property(name="usagemodel_av29", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Delay", type=Delay, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecifcation_throughput_PCMRandomVariable30: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifcation_throughput_PCMRandomVariable30",
    ends={
        Property(name="resourceenvironment_av", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceSpecification_processingRate_PCMRandomVariable31: BinaryAssociation = BinaryAssociation(
    name="processingResourceSpecification_processingRate_PCMRandomVariable31",
    ends={
        Property(name="resourceenvironment_av32", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcessingResourceSpecification", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecification_latency_PCMRandomVariable33: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecification_latency_PCMRandomVariable33",
    ends={
        Property(name="resourceenvironment_av35", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceSpecification34", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaceProvidingEntity__ResourceProvidedRole36: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceProvidingEntity__ResourceProvidedRole36",
    ends={
        Property(name="core_av37", type=pcm_av_entity_av_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_av", type=entity_av_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
providedResourceInterface__ResourceProvidedRole38: BinaryAssociation = BinaryAssociation(
    name="providedResourceInterface__ResourceProvidedRole38",
    ends={
        Property(name="ResourceInterface", type=pcm_av_entity_av_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_entity_av_ResourceProvidedRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedRoles_InterfaceProvidingEntity39: BinaryAssociation = BinaryAssociation(
    name="providedRoles_InterfaceProvidingEntity39",
    ends={
        Property(name="repository_av40", type=pcm_av_entity_av_InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="ProvidedRole", type=ProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredRoles_InterfaceRequiringEntity41: BinaryAssociation = BinaryAssociation(
    name="requiredRoles_InterfaceRequiringEntity41",
    ends={
        Property(name="repository_av42", type=pcm_av_entity_av_InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="RequiredRole", type=RequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredRoles__ResourceInterfaceRequiringEntity43: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRoles__ResourceInterfaceRequiringEntity43",
    ends={
        Property(name="core_av45", type=pcm_av_entity_av_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_av44", type=entity_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredResourceInterface__ResourceRequiredRole46: BinaryAssociation = BinaryAssociation(
    name="requiredResourceInterface__ResourceRequiredRole46",
    ends={
        Property(name="ResourceInterface47", type=pcm_av_entity_av_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_entity_av_ResourceRequiredRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaceRequiringEntity__ResourceRequiredRole48: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceRequiringEntity__ResourceRequiredRole48",
    ends={
        Property(name="core_av50", type=pcm_av_entity_av_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_av49", type=entity_av_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
assemblyEventConnector__FilterCondition21: BinaryAssociation = BinaryAssociation(
    name="assemblyEventConnector__FilterCondition21",
    ends={
        Property(name="core_av23", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av22", type=composition_av_AssemblyEventConnector, multiplicity=Multiplicity(0, 1))
    }
)
loop_LoopIteration24: BinaryAssociation = BinaryAssociation(
    name="loop_LoopIteration24",
    ends={
        Property(name="usagemodel_av25", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Loop", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure__Connector54: BinaryAssociation = BinaryAssociation(
    name="parentStructure__Connector54",
    ends={
        Property(name="core_av56", type=pcm_av_composition_av_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av55", type=composition_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContexts__ComposedStructure57: BinaryAssociation = BinaryAssociation(
    name="assemblyContexts__ComposedStructure57",
    ends={
        Property(name="core_av59", type=pcm_av_composition_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av58", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredDelegationConnectors_ComposedStructure60: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredDelegationConnectors_ComposedStructure60",
    ends={
        Property(name="core_av62", type=pcm_av_composition_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av61", type=composition_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceProvidedRoles__ResourceInterfaceProvidingEntity51: BinaryAssociation = BinaryAssociation(
    name="resourceProvidedRoles__ResourceInterfaceProvidingEntity51",
    ends={
        Property(name="core_av53", type=pcm_av_entity_av_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_av52", type=entity_av_ResourceProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectors__ComposedStructure66: BinaryAssociation = BinaryAssociation(
    name="connectors__ComposedStructure66",
    ends={
        Property(name="core_av68", type=pcm_av_composition_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av67", type=composition_av_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerResourceRequiredRole_ResourceRequiredDelegationConnector69: BinaryAssociation = BinaryAssociation(
    name="innerResourceRequiredRole_ResourceRequiredDelegationConnector69",
    ends={
        Property(name="entity_av_ResourceRequiredRole", type=pcm_av_composition_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_ResourceRequiredDelegationConnector", type=entity_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerResourceRequiredRole_ResourceRequiredDelegationConnector70: BinaryAssociation = BinaryAssociation(
    name="outerResourceRequiredRole_ResourceRequiredDelegationConnector70",
    ends={
        Property(name="entity_av_ResourceRequiredRole72", type=pcm_av_composition_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_ResourceRequiredDelegationConnector71", type=entity_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure_ResourceRequiredDelegationConnector73: BinaryAssociation = BinaryAssociation(
    name="parentStructure_ResourceRequiredDelegationConnector73",
    ends={
        Property(name="core_av75", type=pcm_av_composition_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av74", type=composition_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__EventChannel76: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventChannel76",
    ends={
        Property(name="EventGroup", type=pcm_av_composition_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_EventChannel", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSourceConnector__EventChannel77: BinaryAssociation = BinaryAssociation(
    name="eventChannelSourceConnector__EventChannel77",
    ends={
        Property(name="core_av79", type=pcm_av_composition_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av78", type=composition_av_EventChannelSourceConnector, multiplicity=Multiplicity(0, 9999))
    }
)
eventChannelSinkConnector__EventChannel80: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__EventChannel80",
    ends={
        Property(name="core_av82", type=pcm_av_composition_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av81", type=composition_av_EventChannelSinkConnector, multiplicity=Multiplicity(0, 9999))
    }
)
parentStructure__EventChannel83: BinaryAssociation = BinaryAssociation(
    name="parentStructure__EventChannel83",
    ends={
        Property(name="core_av85", type=pcm_av_composition_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av84", type=composition_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EventChannelSourceRole86: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EventChannelSourceRole86",
    ends={
        Property(name="SourceRole", type=pcm_av_composition_av_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_EventChannelSourceConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__EventChannelSourceConnector87: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSourceConnector87",
    ends={
        Property(name="composition_av_AssemblyContext", type=pcm_av_composition_av_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_EventChannelSourceConnector88", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSourceConnector89: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSourceConnector89",
    ends={
        Property(name="core_av91", type=pcm_av_composition_av_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av90", type=composition_av_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__EventChannelSinkConnector92: BinaryAssociation = BinaryAssociation(
    name="sinkRole__EventChannelSinkConnector92",
    ends={
        Property(name="SinkRole", type=pcm_av_composition_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_EventChannelSinkConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__EventChannelSinkConnector93: BinaryAssociation = BinaryAssociation(
    name="filterCondition__EventChannelSinkConnector93",
    ends={
        Property(name="core_av94", type=pcm_av_composition_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext__EventChannelSinkConnector95: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSinkConnector95",
    ends={
        Property(name="composition_av_AssemblyContext97", type=pcm_av_composition_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_EventChannelSinkConnector96", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSinkConnector98: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSinkConnector98",
    ends={
        Property(name="core_av100", type=pcm_av_composition_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av99", type=composition_av_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__ComposedStructure63: BinaryAssociation = BinaryAssociation(
    name="eventChannel__ComposedStructure63",
    ends={
        Property(name="core_av65", type=pcm_av_composition_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av64", type=composition_av_EventChannel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerProvidedRole_ProvidedDelegationConnector101: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole_ProvidedDelegationConnector101",
    ends={
        Property(name="OperationProvidedRole", type=pcm_av_composition_av_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_ProvidedDelegationConnector", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole_ProvidedDelegationConnector102: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole_ProvidedDelegationConnector102",
    ends={
        Property(name="OperationProvidedRole104", type=pcm_av_composition_av_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_ProvidedDelegationConnector103", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_ProvidedDelegationConnector105: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ProvidedDelegationConnector105",
    ends={
        Property(name="composition_av_AssemblyContext107", type=pcm_av_composition_av_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_ProvidedDelegationConnector106", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole_RequiredDelegationConnector108: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole_RequiredDelegationConnector108",
    ends={
        Property(name="OperationRequiredRole", type=pcm_av_composition_av_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_RequiredDelegationConnector", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole_RequiredDelegationConnector109: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole_RequiredDelegationConnector109",
    ends={
        Property(name="OperationRequiredRole111", type=pcm_av_composition_av_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_RequiredDelegationConnector110", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_RequiredDelegationConnector112: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_RequiredDelegationConnector112",
    ends={
        Property(name="composition_av_AssemblyContext114", type=pcm_av_composition_av_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_RequiredDelegationConnector113", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext_AssemblyConnector115: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext_AssemblyConnector115",
    ends={
        Property(name="composition_av_AssemblyContext116", type=pcm_av_composition_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyConnector", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext_AssemblyConnector117: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext_AssemblyConnector117",
    ends={
        Property(name="composition_av_AssemblyContext119", type=pcm_av_composition_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyConnector118", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providedRole_AssemblyConnector120: BinaryAssociation = BinaryAssociation(
    name="providedRole_AssemblyConnector120",
    ends={
        Property(name="OperationProvidedRole122", type=pcm_av_composition_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyConnector121", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole_AssemblyConnector123: BinaryAssociation = BinaryAssociation(
    name="requiredRole_AssemblyConnector123",
    ends={
        Property(name="OperationRequiredRole125", type=pcm_av_composition_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyConnector124", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__AssemblyEventConnector126: BinaryAssociation = BinaryAssociation(
    name="sinkRole__AssemblyEventConnector126",
    ends={
        Property(name="SinkRole127", type=pcm_av_composition_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyEventConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__AssemblyEventConnector128: BinaryAssociation = BinaryAssociation(
    name="sourceRole__AssemblyEventConnector128",
    ends={
        Property(name="SourceRole130", type=pcm_av_composition_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyEventConnector129", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkAssemblyContext__AssemblyEventConnector131: BinaryAssociation = BinaryAssociation(
    name="sinkAssemblyContext__AssemblyEventConnector131",
    ends={
        Property(name="composition_av_AssemblyContext133", type=pcm_av_composition_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyEventConnector132", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
sourceAssemblyContext__AssemblyEventConnector134: BinaryAssociation = BinaryAssociation(
    name="sourceAssemblyContext__AssemblyEventConnector134",
    ends={
        Property(name="composition_av_AssemblyContext136", type=pcm_av_composition_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyEventConnector135", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__AssemblyEventConnector137: BinaryAssociation = BinaryAssociation(
    name="filterCondition__AssemblyEventConnector137",
    ends={
        Property(name="core_av139", type=pcm_av_composition_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable138", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
innerSourceRole__SourceRole140: BinaryAssociation = BinaryAssociation(
    name="innerSourceRole__SourceRole140",
    ends={
        Property(name="SourceRole141", type=pcm_av_composition_av_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_SourceDelegationConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSourceRole__SourceRole142: BinaryAssociation = BinaryAssociation(
    name="outerSourceRole__SourceRole142",
    ends={
        Property(name="SourceRole144", type=pcm_av_composition_av_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_SourceDelegationConnector143", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSinkRole__SinkRole153: BinaryAssociation = BinaryAssociation(
    name="outerSinkRole__SinkRole153",
    ends={
        Property(name="SinkRole155", type=pcm_av_composition_av_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_SinkDelegationConnector154", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
providedRole__AssemblyInfrastructureConnector156: BinaryAssociation = BinaryAssociation(
    name="providedRole__AssemblyInfrastructureConnector156",
    ends={
        Property(name="InfrastructureProvidedRole", type=pcm_av_composition_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyInfrastructureConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__AssemblyInfrastructureConnector157: BinaryAssociation = BinaryAssociation(
    name="requiredRole__AssemblyInfrastructureConnector157",
    ends={
        Property(name="InfrastructureRequiredRole", type=pcm_av_composition_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyInfrastructureConnector158", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext__AssemblyInfrastructureConnector159: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext__AssemblyInfrastructureConnector159",
    ends={
        Property(name="composition_av_AssemblyContext161", type=pcm_av_composition_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyInfrastructureConnector160", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext__AssemblyInfrastructureConnector162: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext__AssemblyInfrastructureConnector162",
    ends={
        Property(name="composition_av_AssemblyContext164", type=pcm_av_composition_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyInfrastructureConnector163", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole__ProvidedInfrastructureDelegationConnector165: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole__ProvidedInfrastructureDelegationConnector165",
    ends={
        Property(name="InfrastructureProvidedRole166", type=pcm_av_composition_av_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_ProvidedInfrastructureDelegationConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole__ProvidedInfrastructureDelegationConnector167: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole__ProvidedInfrastructureDelegationConnector167",
    ends={
        Property(name="InfrastructureProvidedRole169", type=pcm_av_composition_av_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_ProvidedInfrastructureDelegationConnector168", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__ProvidedInfrastructureDelegationConnector170: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__ProvidedInfrastructureDelegationConnector170",
    ends={
        Property(name="composition_av_AssemblyContext172", type=pcm_av_composition_av_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_ProvidedInfrastructureDelegationConnector171", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole__RequiredInfrastructureDelegationConnector173: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredInfrastructureDelegationConnector173",
    ends={
        Property(name="InfrastructureRequiredRole174", type=pcm_av_composition_av_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_RequiredInfrastructureDelegationConnector", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredInfrastructureDelegationConnector175: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredInfrastructureDelegationConnector175",
    ends={
        Property(name="InfrastructureRequiredRole177", type=pcm_av_composition_av_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_RequiredInfrastructureDelegationConnector176", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredInfrastructureDelegationConnector178: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredInfrastructureDelegationConnector178",
    ends={
        Property(name="composition_av_AssemblyContext180", type=pcm_av_composition_av_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_RequiredInfrastructureDelegationConnector179", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredResourceDelegationConnector181: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredResourceDelegationConnector181",
    ends={
        Property(name="composition_av_AssemblyContext182", type=pcm_av_composition_av_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_RequiredResourceDelegationConnector", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole__RequiredResourceDelegationConnector183: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredResourceDelegationConnector183",
    ends={
        Property(name="entity_av_ResourceRequiredRole185", type=pcm_av_composition_av_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_RequiredResourceDelegationConnector184", type=entity_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredResourceDelegationConnector186: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredResourceDelegationConnector186",
    ends={
        Property(name="entity_av_ResourceRequiredRole188", type=pcm_av_composition_av_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_RequiredResourceDelegationConnector187", type=entity_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SourceDelegationConnector145: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SourceDelegationConnector145",
    ends={
        Property(name="composition_av_AssemblyContext147", type=pcm_av_composition_av_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_SourceDelegationConnector146", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SinkDelegationConnector148: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SinkDelegationConnector148",
    ends={
        Property(name="composition_av_AssemblyContext149", type=pcm_av_composition_av_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_SinkDelegationConnector", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerSinkRole__SinkRole150: BinaryAssociation = BinaryAssociation(
    name="innerSinkRole__SinkRole150",
    ends={
        Property(name="SinkRole152", type=pcm_av_composition_av_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_SinkDelegationConnector151", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
usageScenario_Workload195: BinaryAssociation = BinaryAssociation(
    name="usageScenario_Workload195",
    ends={
        Property(name="usagemodel_av196", type=pcm_av_usagemodel_av_Workload, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UsageScenario197: BinaryAssociation = BinaryAssociation(
    name="usageModel_UsageScenario197",
    ends={
        Property(name="usagemodel_av198", type=pcm_av_usagemodel_av_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageModel", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_UsageScenario199: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_UsageScenario199",
    ends={
        Property(name="usagemodel_av200", type=pcm_av_usagemodel_av_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
workload_UsageScenario201: BinaryAssociation = BinaryAssociation(
    name="workload_UsageScenario201",
    ends={
        Property(name="usagemodel_av202", type=pcm_av_usagemodel_av_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="Workload", type=Workload, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext_userData203: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_userData203",
    ends={
        Property(name="composition_av_AssemblyContext204", type=pcm_av_usagemodel_av_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_usagemodel_av_UserData", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UserData205: BinaryAssociation = BinaryAssociation(
    name="usageModel_UserData205",
    ends={
        Property(name="usagemodel_av207", type=pcm_av_usagemodel_av_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageModel206", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
userDataParameterUsages_UserData208: BinaryAssociation = BinaryAssociation(
    name="userDataParameterUsages_UserData208",
    ends={
        Property(name="parameter_av210", type=pcm_av_usagemodel_av_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage209", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_UsageModel211: BinaryAssociation = BinaryAssociation(
    name="usageScenario_UsageModel211",
    ends={
        Property(name="usagemodel_av213", type=pcm_av_usagemodel_av_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageScenario212", type=UsageScenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentStructure__AssemblyContext189: BinaryAssociation = BinaryAssociation(
    name="parentStructure__AssemblyContext189",
    ends={
        Property(name="core_av191", type=pcm_av_composition_av_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av190", type=composition_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
encapsulatedComponent__AssemblyContext192: BinaryAssociation = BinaryAssociation(
    name="encapsulatedComponent__AssemblyContext192",
    ends={
        Property(name="RepositoryComponent", type=pcm_av_composition_av_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyContext", type=RepositoryComponent, multiplicity=Multiplicity(0, 1))
    }
)
configParameterUsages__AssemblyContext193: BinaryAssociation = BinaryAssociation(
    name="configParameterUsages__AssemblyContext193",
    ends={
        Property(name="parameter_av194", type=pcm_av_composition_av_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedRole_EntryLevelSystemCall216: BinaryAssociation = BinaryAssociation(
    name="providedRole_EntryLevelSystemCall216",
    ends={
        Property(name="OperationProvidedRole217", type=pcm_av_usagemodel_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_usagemodel_av_EntryLevelSystemCall", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__EntryLevelSystemCall218: BinaryAssociation = BinaryAssociation(
    name="operationSignature__EntryLevelSystemCall218",
    ends={
        Property(name="OperationSignature", type=pcm_av_usagemodel_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_usagemodel_av_EntryLevelSystemCall219", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
outputParameterUsages_EntryLevelSystemCall220: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsages_EntryLevelSystemCall220",
    ends={
        Property(name="parameter_av222", type=pcm_av_usagemodel_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage221", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputParameterUsages_EntryLevelSystemCall223: BinaryAssociation = BinaryAssociation(
    name="inputParameterUsages_EntryLevelSystemCall223",
    ends={
        Property(name="parameter_av225", type=pcm_av_usagemodel_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage224", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
successor226: BinaryAssociation = BinaryAssociation(
    name="successor226",
    ends={
        Property(name="usagemodel_av227", type=pcm_av_usagemodel_av_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
predecessor228: BinaryAssociation = BinaryAssociation(
    name="predecessor228",
    ends={
        Property(name="usagemodel_av230", type=pcm_av_usagemodel_av_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction229", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_AbstractUserAction231: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_AbstractUserAction231",
    ends={
        Property(name="usagemodel_av233", type=pcm_av_usagemodel_av_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour232", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
userData_UsageModel214: BinaryAssociation = BinaryAssociation(
    name="userData_UsageModel214",
    ends={
        Property(name="usagemodel_av215", type=pcm_av_usagemodel_av_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="UserData", type=UserData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_SenarioBehaviour234: BinaryAssociation = BinaryAssociation(
    name="usageScenario_SenarioBehaviour234",
    ends={
        Property(name="usagemodel_av236", type=pcm_av_usagemodel_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageScenario235", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
branchTransition_ScenarioBehaviour237: BinaryAssociation = BinaryAssociation(
    name="branchTransition_ScenarioBehaviour237",
    ends={
        Property(name="usagemodel_av238", type=pcm_av_usagemodel_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="BranchTransition", type=BranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
loop_ScenarioBehaviour239: BinaryAssociation = BinaryAssociation(
    name="loop_ScenarioBehaviour239",
    ends={
        Property(name="usagemodel_av241", type=pcm_av_usagemodel_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="Loop240", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
actions_ScenarioBehaviour242: BinaryAssociation = BinaryAssociation(
    name="actions_ScenarioBehaviour242",
    ends={
        Property(name="usagemodel_av244", type=pcm_av_usagemodel_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction243", type=AbstractUserAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branch_BranchTransition245: BinaryAssociation = BinaryAssociation(
    name="branch_BranchTransition245",
    ends={
        Property(name="usagemodel_av246", type=pcm_av_usagemodel_av_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="Branch", type=Branch, multiplicity=Multiplicity(0, 1))
    }
)
branchedBehaviour_BranchTransition247: BinaryAssociation = BinaryAssociation(
    name="branchedBehaviour_BranchTransition247",
    ends={
        Property(name="usagemodel_av249", type=pcm_av_usagemodel_av_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour248", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchTransitions_Branch250: BinaryAssociation = BinaryAssociation(
    name="branchTransitions_Branch250",
    ends={
        Property(name="usagemodel_av252", type=pcm_av_usagemodel_av_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="BranchTransition251", type=BranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopIteration_Loop253: BinaryAssociation = BinaryAssociation(
    name="loopIteration_Loop253",
    ends={
        Property(name="core_av255", type=pcm_av_usagemodel_av_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable254", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interArrivalTime_OpenWorkload259: BinaryAssociation = BinaryAssociation(
    name="interArrivalTime_OpenWorkload259",
    ends={
        Property(name="core_av261", type=pcm_av_usagemodel_av_OpenWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable260", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeSpecification_Delay262: BinaryAssociation = BinaryAssociation(
    name="timeSpecification_Delay262",
    ends={
        Property(name="core_av264", type=pcm_av_usagemodel_av_Delay, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable263", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyBehaviour_Loop256: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop256",
    ends={
        Property(name="usagemodel_av258", type=pcm_av_usagemodel_av_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour257", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thinkTime_ClosedWorkload265: BinaryAssociation = BinaryAssociation(
    name="thinkTime_ClosedWorkload265",
    ends={
        Property(name="core_av267", type=pcm_av_usagemodel_av_ClosedWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable266", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capacity_PassiveResource268: BinaryAssociation = BinaryAssociation(
    name="capacity_PassiveResource268",
    ends={
        Property(name="core_av270", type=pcm_av_repository_av_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable269", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicComponent_PassiveResource271: BinaryAssociation = BinaryAssociation(
    name="basicComponent_PassiveResource271",
    ends={
        Property(name="repository_av272", type=pcm_av_repository_av_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="BasicComponent", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
resourceTimeoutFailureType__PassiveResource273: BinaryAssociation = BinaryAssociation(
    name="resourceTimeoutFailureType__PassiveResource273",
    ends={
        Property(name="reliability_av", type=pcm_av_repository_av_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceTimeoutFailureType", type=ResourceTimeoutFailureType, multiplicity=Multiplicity(0, 1))
    }
)
parentCompleteComponentTypes279: BinaryAssociation = BinaryAssociation(
    name="parentCompleteComponentTypes279",
    ends={
        Property(name="CompleteComponentType", type=pcm_av_repository_av_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_ImplementationComponentType", type=CompleteComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
componentParameterUsage_ImplementationComponentType280: BinaryAssociation = BinaryAssociation(
    name="componentParameterUsage_ImplementationComponentType280",
    ends={
        Property(name="VariableUsage282", type=pcm_av_repository_av_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_ImplementationComponentType281", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository__RepositoryComponent283: BinaryAssociation = BinaryAssociation(
    name="repository__RepositoryComponent283",
    ends={
        Property(name="repository_av284", type=pcm_av_repository_av_RepositoryComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
providingEntity_ProvidedRole285: BinaryAssociation = BinaryAssociation(
    name="providingEntity_ProvidedRole285",
    ends={
        Property(name="core_av287", type=pcm_av_repository_av_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_av286", type=entity_av_InterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
serviceEffectSpecifications__BasicComponent274: BinaryAssociation = BinaryAssociation(
    name="serviceEffectSpecifications__BasicComponent274",
    ends={
        Property(name="seff_av275", type=pcm_av_repository_av_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ServiceEffectSpecification", type=ServiceEffectSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveResource_BasicComponent276: BinaryAssociation = BinaryAssociation(
    name="passiveResource_BasicComponent276",
    ends={
        Property(name="repository_av278", type=pcm_av_repository_av_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="PassiveResource277", type=PassiveResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operationSignature__Parameter291: BinaryAssociation = BinaryAssociation(
    name="operationSignature__Parameter291",
    ends={
        Property(name="repository_av293", type=pcm_av_repository_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationSignature292", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
eventType__Parameter294: BinaryAssociation = BinaryAssociation(
    name="eventType__Parameter294",
    ends={
        Property(name="repository_av295", type=pcm_av_repository_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="EventType", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
resourceSignature__Parameter296: BinaryAssociation = BinaryAssociation(
    name="resourceSignature__Parameter296",
    ends={
        Property(name="resourcetype_av", type=pcm_av_repository_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceSignature", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
repository__DataType297: BinaryAssociation = BinaryAssociation(
    name="repository__DataType297",
    ends={
        Property(name="repository_av299", type=pcm_av_repository_av_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository298", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
components__Repository300: BinaryAssociation = BinaryAssociation(
    name="components__Repository300",
    ends={
        Property(name="repository_av302", type=pcm_av_repository_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="RepositoryComponent301", type=RepositoryComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaces__Repository303: BinaryAssociation = BinaryAssociation(
    name="interfaces__Repository303",
    ends={
        Property(name="repository_av304", type=pcm_av_repository_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="Interface", type=Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureTypes__Repository305: BinaryAssociation = BinaryAssociation(
    name="failureTypes__Repository305",
    ends={
        Property(name="reliability_av306", type=pcm_av_repository_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="FailureType", type=FailureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes__Repository307: BinaryAssociation = BinaryAssociation(
    name="dataTypes__Repository307",
    ends={
        Property(name="repository_av309", type=pcm_av_repository_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="DataType308", type=DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataType__Parameter288: BinaryAssociation = BinaryAssociation(
    name="dataType__Parameter288",
    ends={
        Property(name="DataType", type=pcm_av_repository_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_Parameter", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureSignature__Parameter289: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignature__Parameter289",
    ends={
        Property(name="repository_av290", type=pcm_av_repository_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="InfrastructureSignature", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
parentInterfaces__Interface310: BinaryAssociation = BinaryAssociation(
    name="parentInterfaces__Interface310",
    ends={
        Property(name="Interface311", type=pcm_av_repository_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_Interface", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
protocols__Interface312: BinaryAssociation = BinaryAssociation(
    name="protocols__Interface312",
    ends={
        Property(name="Protocol", type=pcm_av_repository_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_Interface313", type=Protocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCharacterisations314: BinaryAssociation = BinaryAssociation(
    name="requiredCharacterisations314",
    ends={
        Property(name="repository_av315", type=pcm_av_repository_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="RequiredCharacterisation", type=RequiredCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository__Interface316: BinaryAssociation = BinaryAssociation(
    name="repository__Interface316",
    ends={
        Property(name="repository_av318", type=pcm_av_repository_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository317", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
parameter319: BinaryAssociation = BinaryAssociation(
    name="parameter319",
    ends={
        Property(name="Parameter", type=pcm_av_repository_av_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_RequiredCharacterisation", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
interface_RequiredCharacterisation320: BinaryAssociation = BinaryAssociation(
    name="interface_RequiredCharacterisation320",
    ends={
        Property(name="repository_av322", type=pcm_av_repository_av_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="Interface321", type=Interface, multiplicity=Multiplicity(0, 1))
    }
)
parameter__EventType326: BinaryAssociation = BinaryAssociation(
    name="parameter__EventType326",
    ends={
        Property(name="repository_av328", type=pcm_av_repository_av_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter327", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventGroup__EventType329: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventType329",
    ends={
        Property(name="repository_av331", type=pcm_av_repository_av_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="EventGroup330", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
exceptions__Signature332: BinaryAssociation = BinaryAssociation(
    name="exceptions__Signature332",
    ends={
        Property(name="ExceptionType", type=pcm_av_repository_av_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_Signature", type=ExceptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureType333: BinaryAssociation = BinaryAssociation(
    name="failureType333",
    ends={
        Property(name="FailureType335", type=pcm_av_repository_av_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_Signature334", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
parameters__InfrastructureSignature336: BinaryAssociation = BinaryAssociation(
    name="parameters__InfrastructureSignature336",
    ends={
        Property(name="repository_av338", type=pcm_av_repository_av_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter337", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureInterface__InfrastructureSignature339: BinaryAssociation = BinaryAssociation(
    name="infrastructureInterface__InfrastructureSignature339",
    ends={
        Property(name="repository_av340", type=pcm_av_repository_av_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="InfrastructureInterface", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureSignatures__InfrastructureInterface341: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignatures__InfrastructureInterface341",
    ends={
        Property(name="repository_av343", type=pcm_av_repository_av_InfrastructureInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="InfrastructureSignature342", type=InfrastructureSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventTypes__EventGroup323: BinaryAssociation = BinaryAssociation(
    name="eventTypes__EventGroup323",
    ends={
        Property(name="repository_av325", type=pcm_av_repository_av_EventGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="EventType324", type=EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterface__InfrastructureRequiredRole344: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__InfrastructureRequiredRole344",
    ends={
        Property(name="InfrastructureInterface345", type=pcm_av_repository_av_InfrastructureRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_InfrastructureRequiredRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
requiringEntity_RequiredRole346: BinaryAssociation = BinaryAssociation(
    name="requiringEntity_RequiredRole346",
    ends={
        Property(name="core_av348", type=pcm_av_repository_av_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_av347", type=entity_av_InterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
interface__OperationSignature349: BinaryAssociation = BinaryAssociation(
    name="interface__OperationSignature349",
    ends={
        Property(name="repository_av350", type=pcm_av_repository_av_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationInterface", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
parameters__OperationSignature351: BinaryAssociation = BinaryAssociation(
    name="parameters__OperationSignature351",
    ends={
        Property(name="repository_av353", type=pcm_av_repository_av_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter352", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType__OperationSignature354: BinaryAssociation = BinaryAssociation(
    name="returnType__OperationSignature354",
    ends={
        Property(name="DataType355", type=pcm_av_repository_av_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_OperationSignature", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
signatures__OperationInterface356: BinaryAssociation = BinaryAssociation(
    name="signatures__OperationInterface356",
    ends={
        Property(name="repository_av358", type=pcm_av_repository_av_OperationInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationSignature357", type=OperationSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterface__OperationRequiredRole359: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__OperationRequiredRole359",
    ends={
        Property(name="OperationInterface360", type=pcm_av_repository_av_OperationRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_OperationRequiredRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SourceRole361: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SourceRole361",
    ends={
        Property(name="EventGroup362", type=pcm_av_repository_av_SourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_SourceRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SinkRole363: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SinkRole363",
    ends={
        Property(name="EventGroup364", type=pcm_av_repository_av_SinkRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_SinkRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface__OperationProvidedRole365: BinaryAssociation = BinaryAssociation(
    name="providedInterface__OperationProvidedRole365",
    ends={
        Property(name="OperationInterface366", type=pcm_av_repository_av_OperationProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_OperationProvidedRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface__InfrastructureProvidedRole367: BinaryAssociation = BinaryAssociation(
    name="providedInterface__InfrastructureProvidedRole367",
    ends={
        Property(name="InfrastructureInterface368", type=pcm_av_repository_av_InfrastructureProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_InfrastructureProvidedRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
parentProvidesComponentTypes369: BinaryAssociation = BinaryAssociation(
    name="parentProvidesComponentTypes369",
    ends={
        Property(name="ProvidesComponentType", type=pcm_av_repository_av_CompleteComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_CompleteComponentType", type=ProvidesComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
innerType_CollectionDataType370: BinaryAssociation = BinaryAssociation(
    name="innerType_CollectionDataType370",
    ends={
        Property(name="DataType371", type=pcm_av_repository_av_CollectionDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_CollectionDataType", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
parentType_CompositeDataType372: BinaryAssociation = BinaryAssociation(
    name="parentType_CompositeDataType372",
    ends={
        Property(name="CompositeDataType", type=pcm_av_repository_av_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 9999))
    }
)
innerDeclaration_CompositeDataType373: BinaryAssociation = BinaryAssociation(
    name="innerDeclaration_CompositeDataType373",
    ends={
        Property(name="repository_av374", type=pcm_av_repository_av_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="InnerDeclaration", type=InnerDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype_InnerDeclaration375: BinaryAssociation = BinaryAssociation(
    name="datatype_InnerDeclaration375",
    ends={
        Property(name="DataType376", type=pcm_av_repository_av_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_InnerDeclaration", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
compositeDataType_InnerDeclaration377: BinaryAssociation = BinaryAssociation(
    name="compositeDataType_InnerDeclaration377",
    ends={
        Property(name="repository_av379", type=pcm_av_repository_av_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="CompositeDataType378", type=CompositeDataType, multiplicity=Multiplicity(0, 1))
    }
)
parameter__ResourceSignature380: BinaryAssociation = BinaryAssociation(
    name="parameter__ResourceSignature380",
    ends={
        Property(name="repository_av382", type=pcm_av_resourcetype_av_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter381", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceRepository_ResourceType388: BinaryAssociation = BinaryAssociation(
    name="resourceRepository_ResourceType388",
    ends={
        Property(name="resourcetype_av389", type=pcm_av_resourcetype_av_ResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaces__ResourceRepository390: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaces__ResourceRepository390",
    ends={
        Property(name="resourcetype_av392", type=pcm_av_resourcetype_av_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceInterface391", type=ResourceInterface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schedulingPolicies__ResourceRepository393: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicies__ResourceRepository393",
    ends={
        Property(name="resourcetype_av394", type=pcm_av_resourcetype_av_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="SchedulingPolicy", type=SchedulingPolicy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
availableResourceTypes_ResourceRepository395: BinaryAssociation = BinaryAssociation(
    name="availableResourceTypes_ResourceRepository395",
    ends={
        Property(name="resourcetype_av396", type=pcm_av_resourcetype_av_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceType", type=ResourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRepository__SchedulingPolicy397: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__SchedulingPolicy397",
    ends={
        Property(name="resourcetype_av399", type=pcm_av_resourcetype_av_SchedulingPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceRepository398", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
networkInducedFailureType__CommunicationLinkResourceType400: BinaryAssociation = BinaryAssociation(
    name="networkInducedFailureType__CommunicationLinkResourceType400",
    ends={
        Property(name="reliability_av401", type=pcm_av_resourcetype_av_CommunicationLinkResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="NetworkInducedFailureType", type=NetworkInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
resourceRepository__ResourceInterface402: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__ResourceInterface402",
    ends={
        Property(name="resourcetype_av404", type=pcm_av_resourcetype_av_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceRepository403", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
resourceSignatures__ResourceInterface405: BinaryAssociation = BinaryAssociation(
    name="resourceSignatures__ResourceInterface405",
    ends={
        Property(name="resourcetype_av407", type=pcm_av_resourcetype_av_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceSignature406", type=ResourceSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableCharacterisation_VariableUsage408: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_VariableUsage408",
    ends={
        Property(name="parameter_av410", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableCharacterisation409", type=VariableCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceInterface__ResourceSignature383: BinaryAssociation = BinaryAssociation(
    name="resourceInterface__ResourceSignature383",
    ends={
        Property(name="resourcetype_av385", type=pcm_av_resourcetype_av_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceInterface384", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
hardwareInducedFailureType__ProcessingResourceType386: BinaryAssociation = BinaryAssociation(
    name="hardwareInducedFailureType__ProcessingResourceType386",
    ends={
        Property(name="reliability_av387", type=pcm_av_resourcetype_av_ProcessingResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="HardwareInducedFailureType", type=HardwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage422: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage422",
    ends={
        Property(name="qosannotations_av423", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="SpecifiedOutputParameterAbstraction", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__VariableUsage424: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__VariableUsage424",
    ends={
        Property(name="core_av426", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av425", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_InputParameterUsage427: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_InputParameterUsage427",
    ends={
        Property(name="usagemodel_av428", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="EntryLevelSystemCall", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_OutputParameterUsage429: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_OutputParameterUsage429",
    ends={
        Property(name="usagemodel_av431", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="EntryLevelSystemCall430", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
namedReference__VariableUsage432: BinaryAssociation = BinaryAssociation(
    name="namedReference__VariableUsage432",
    ends={
        Property(name="parameter_av_pcm_av_AbstractNamedReference", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_parameter_av_VariableUsage", type=parameter_av_pcm_av_AbstractNamedReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification_VariableCharacterisation433: BinaryAssociation = BinaryAssociation(
    name="specification_VariableCharacterisation433",
    ends={
        Property(name="core_av435", type=pcm_av_parameter_av_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable434", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableUsage_VariableCharacterisation436: BinaryAssociation = BinaryAssociation(
    name="variableUsage_VariableCharacterisation436",
    ends={
        Property(name="parameter_av438", type=pcm_av_parameter_av_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage437", type=VariableUsage, multiplicity=Multiplicity(0, 1))
    }
)
userData_VariableUsage411: BinaryAssociation = BinaryAssociation(
    name="userData_VariableUsage411",
    ends={
        Property(name="usagemodel_av413", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="UserData412", type=UserData, multiplicity=Multiplicity(0, 1))
    }
)
callAction__VariableUsage414: BinaryAssociation = BinaryAssociation(
    name="callAction__VariableUsage414",
    ends={
        Property(name="seff_av415", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="CallAction", type=CallAction, multiplicity=Multiplicity(0, 1))
    }
)
synchronisationPoint_VariableUsage416: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_VariableUsage416",
    ends={
        Property(name="seff_av417", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
callReturnAction__VariableUsage418: BinaryAssociation = BinaryAssociation(
    name="callReturnAction__VariableUsage418",
    ends={
        Property(name="seff_av419", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="CallReturnAction", type=CallReturnAction, multiplicity=Multiplicity(0, 1))
    }
)
setVariableAction_VariableUsage420: BinaryAssociation = BinaryAssociation(
    name="setVariableAction_VariableUsage420",
    ends={
        Property(name="seff_av421", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="SetVariableAction", type=SetVariableAction, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceType__HardwareInducedFailureType439: BinaryAssociation = BinaryAssociation(
    name="processingResourceType__HardwareInducedFailureType439",
    ends={
        Property(name="resourcetype_av440", type=pcm_av_reliability_av_HardwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcessingResourceType", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
internalFailureOccurrenceDescriptions__SoftwareInducedFailureType441: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__SoftwareInducedFailureType441",
    ends={
        Property(name="reliability_av442", type=pcm_av_reliability_av_SoftwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="InternalFailureOccurrenceDescription", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999))
    }
)
internalAction__InternalFailureOccurrenceDescription443: BinaryAssociation = BinaryAssociation(
    name="internalAction__InternalFailureOccurrenceDescription443",
    ends={
        Property(name="seff_av444", type=pcm_av_reliability_av_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="InternalAction", type=InternalAction, multiplicity=Multiplicity(0, 1))
    }
)
softwareInducedFailureType__InternalFailureOccurrenceDescription445: BinaryAssociation = BinaryAssociation(
    name="softwareInducedFailureType__InternalFailureOccurrenceDescription445",
    ends={
        Property(name="reliability_av446", type=pcm_av_reliability_av_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="SoftwareInducedFailureType", type=SoftwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription449: BinaryAssociation = BinaryAssociation(
    name="specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription449",
    ends={
        Property(name="qosannotations_av450", type=pcm_av_reliability_av_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="qos_reliability_av", type=qos_reliability_av_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(0, 1))
    }
)
failureType__ExternalFailureOccurrenceDescription451: BinaryAssociation = BinaryAssociation(
    name="failureType__ExternalFailureOccurrenceDescription451",
    ends={
        Property(name="FailureType452", type=pcm_av_reliability_av_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_reliability_av_ExternalFailureOccurrenceDescription", type=FailureType, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource__ResourceTimeoutFailureType453: BinaryAssociation = BinaryAssociation(
    name="passiveResource__ResourceTimeoutFailureType453",
    ends={
        Property(name="repository_av455", type=pcm_av_reliability_av_ResourceTimeoutFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="PassiveResource454", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
repository__FailureType456: BinaryAssociation = BinaryAssociation(
    name="repository__FailureType456",
    ends={
        Property(name="repository_av458", type=pcm_av_reliability_av_FailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository457", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemand_Action459: BinaryAssociation = BinaryAssociation(
    name="resourceDemand_Action459",
    ends={
        Property(name="seff_av461", type=pcm_av_seff_av_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_av460", type=seff_performance_av_ParametricResourceDemand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureCall__Action462: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__Action462",
    ends={
        Property(name="seff_av464", type=pcm_av_seff_av_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_av463", type=seff_performance_av_InfrastructureCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceCall__Action465: BinaryAssociation = BinaryAssociation(
    name="resourceCall__Action465",
    ends={
        Property(name="seff_av467", type=pcm_av_seff_av_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_av466", type=seff_performance_av_ResourceCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
communicationLinkResourceType__NetworkInducedFailureType447: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType__NetworkInducedFailureType447",
    ends={
        Property(name="resourcetype_av448", type=pcm_av_reliability_av_NetworkInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceType", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
abstractLoopAction_ResourceDemandingBehaviour475: BinaryAssociation = BinaryAssociation(
    name="abstractLoopAction_ResourceDemandingBehaviour475",
    ends={
        Property(name="seff_av476", type=pcm_av_seff_av_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractLoopAction", type=AbstractLoopAction, multiplicity=Multiplicity(0, 1))
    }
)
abstractBranchTransition_ResourceDemandingBehaviour477: BinaryAssociation = BinaryAssociation(
    name="abstractBranchTransition_ResourceDemandingBehaviour477",
    ends={
        Property(name="seff_av478", type=pcm_av_seff_av_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractBranchTransition", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
steps_Behaviour479: BinaryAssociation = BinaryAssociation(
    name="steps_Behaviour479",
    ends={
        Property(name="seff_av481", type=pcm_av_seff_av_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction480", type=AbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyBehaviour_Loop482: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop482",
    ends={
        Property(name="seff_av484", type=pcm_av_seff_av_AbstractLoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingBehaviour483", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchAction_AbstractBranchTransition485: BinaryAssociation = BinaryAssociation(
    name="branchAction_AbstractBranchTransition485",
    ends={
        Property(name="seff_av486", type=pcm_av_seff_av_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="BranchAction", type=BranchAction, multiplicity=Multiplicity(0, 1))
    }
)
branchBehaviour_BranchTransition487: BinaryAssociation = BinaryAssociation(
    name="branchBehaviour_BranchTransition487",
    ends={
        Property(name="seff_av489", type=pcm_av_seff_av_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingBehaviour488", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
predecessor_AbstractAction468: BinaryAssociation = BinaryAssociation(
    name="predecessor_AbstractAction468",
    ends={
        Property(name="seff_av469", type=pcm_av_seff_av_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
successor_AbstractAction470: BinaryAssociation = BinaryAssociation(
    name="successor_AbstractAction470",
    ends={
        Property(name="seff_av472", type=pcm_av_seff_av_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction471", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemandingBehaviour_AbstractAction473: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingBehaviour_AbstractAction473",
    ends={
        Property(name="seff_av474", type=pcm_av_seff_av_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingBehaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
branches_Branch490: BinaryAssociation = BinaryAssociation(
    name="branches_Branch490",
    ends={
        Property(name="seff_av492", type=pcm_av_seff_av_BranchAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractBranchTransition491", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputVariableUsages__CallAction493: BinaryAssociation = BinaryAssociation(
    name="inputVariableUsages__CallAction493",
    ends={
        Property(name="parameter_av495", type=pcm_av_seff_av_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage494", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
describedService__SEFF496: BinaryAssociation = BinaryAssociation(
    name="describedService__SEFF496",
    ends={
        Property(name="Signature", type=pcm_av_seff_av_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_av_ServiceEffectSpecification", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
basicComponent_ServiceEffectSpecification497: BinaryAssociation = BinaryAssociation(
    name="basicComponent_ServiceEffectSpecification497",
    ends={
        Property(name="repository_av499", type=pcm_av_seff_av_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BasicComponent498", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_ReleaseAction504: BinaryAssociation = BinaryAssociation(
    name="passiveResource_ReleaseAction504",
    ends={
        Property(name="PassiveResource505", type=pcm_av_seff_av_ReleaseAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_av_ReleaseAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
iterationCount_LoopAction506: BinaryAssociation = BinaryAssociation(
    name="iterationCount_LoopAction506",
    ends={
        Property(name="core_av508", type=pcm_av_seff_av_LoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable507", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
asynchronousForkedBehaviours_ForkAction509: BinaryAssociation = BinaryAssociation(
    name="asynchronousForkedBehaviours_ForkAction509",
    ends={
        Property(name="seff_av510", type=pcm_av_seff_av_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedBehaviour", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronisingBehaviours_ForkAction511: BinaryAssociation = BinaryAssociation(
    name="synchronisingBehaviours_ForkAction511",
    ends={
        Property(name="seff_av513", type=pcm_av_seff_av_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="SynchronisationPoint512", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
synchronisationPoint_ForkedBehaviour514: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_ForkedBehaviour514",
    ends={
        Property(name="seff_av516", type=pcm_av_seff_av_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="SynchronisationPoint515", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
forkAction_ForkedBehaivour517: BinaryAssociation = BinaryAssociation(
    name="forkAction_ForkedBehaivour517",
    ends={
        Property(name="seff_av518", type=pcm_av_seff_av_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkAction", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
outputParameterUsage_SynchronisationPoint519: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsage_SynchronisationPoint519",
    ends={
        Property(name="parameter_av521", type=pcm_av_seff_av_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage520", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forkAction_SynchronisationPoint522: BinaryAssociation = BinaryAssociation(
    name="forkAction_SynchronisationPoint522",
    ends={
        Property(name="seff_av524", type=pcm_av_seff_av_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkAction523", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
synchronousForkedBehaviours_SynchronisationPoint525: BinaryAssociation = BinaryAssociation(
    name="synchronousForkedBehaviours_SynchronisationPoint525",
    ends={
        Property(name="seff_av527", type=pcm_av_seff_av_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedBehaviour526", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceDemandingInternalBehaviours500: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingInternalBehaviours500",
    ends={
        Property(name="seff_av501", type=pcm_av_seff_av_ResourceDemandingSEFF, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingInternalBehaviour", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceDemandingSEFF_ResourceDemandingInternalBehaviour502: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingSEFF_ResourceDemandingInternalBehaviour502",
    ends={
        Property(name="seff_av503", type=pcm_av_seff_av_ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingSEFF", type=ResourceDemandingSEFF, multiplicity=Multiplicity(0, 1))
    }
)
calledService_ExternalService528: BinaryAssociation = BinaryAssociation(
    name="calledService_ExternalService528",
    ends={
        Property(name="OperationSignature529", type=pcm_av_seff_av_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_av_ExternalCallAction", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
role_ExternalService530: BinaryAssociation = BinaryAssociation(
    name="role_ExternalService530",
    ends={
        Property(name="OperationRequiredRole532", type=pcm_av_seff_av_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_av_ExternalCallAction531", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
returnVariableUsage__CallReturnAction533: BinaryAssociation = BinaryAssociation(
    name="returnVariableUsage__CallReturnAction533",
    ends={
        Property(name="parameter_av535", type=pcm_av_seff_av_CallReturnAction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage534", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveresource_AcquireAction536: BinaryAssociation = BinaryAssociation(
    name="passiveresource_AcquireAction536",
    ends={
        Property(name="PassiveResource537", type=pcm_av_seff_av_AcquireAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_av_AcquireAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
parameter_CollectionIteratorAction538: BinaryAssociation = BinaryAssociation(
    name="parameter_CollectionIteratorAction538",
    ends={
        Property(name="Parameter539", type=pcm_av_seff_av_CollectionIteratorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_av_CollectionIteratorAction", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
localVariableUsages_SetVariableAction543: BinaryAssociation = BinaryAssociation(
    name="localVariableUsages_SetVariableAction543",
    ends={
        Property(name="parameter_av545", type=pcm_av_seff_av_SetVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage544", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledResourceDemandingInternalBehaviour546: BinaryAssociation = BinaryAssociation(
    name="calledResourceDemandingInternalBehaviour546",
    ends={
        Property(name="ResourceDemandingInternalBehaviour547", type=pcm_av_seff_av_InternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_av_InternalCallAction", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
eventType__EmitEventAction548: BinaryAssociation = BinaryAssociation(
    name="eventType__EmitEventAction548",
    ends={
        Property(name="EventType549", type=pcm_av_seff_av_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_av_EmitEventAction", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EmitEventAction550: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EmitEventAction550",
    ends={
        Property(name="SourceRole552", type=pcm_av_seff_av_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_av_EmitEventAction551", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
internalFailureOccurrenceDescriptions__InternalAction553: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__InternalAction553",
    ends={
        Property(name="reliability_av555", type=pcm_av_seff_av_InternalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="InternalFailureOccurrenceDescription554", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branchCondition_GuardedBranchTransition540: BinaryAssociation = BinaryAssociation(
    name="branchCondition_GuardedBranchTransition540",
    ends={
        Property(name="core_av542", type=pcm_av_seff_av_GuardedBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable541", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signature__InfrastructureCall556: BinaryAssociation = BinaryAssociation(
    name="signature__InfrastructureCall556",
    ends={
        Property(name="InfrastructureSignature557", type=pcm_av_seff_performance_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_performance_av_InfrastructureCall", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__InfrastructureCall558: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__InfrastructureCall558",
    ends={
        Property(name="core_av560", type=pcm_av_seff_performance_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable559", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action__InfrastructureCall561: BinaryAssociation = BinaryAssociation(
    name="action__InfrastructureCall561",
    ends={
        Property(name="seff_av562", type=pcm_av_seff_performance_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractInternalControlFlowAction", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__InfrastructureCall563: BinaryAssociation = BinaryAssociation(
    name="requiredRole__InfrastructureCall563",
    ends={
        Property(name="InfrastructureRequiredRole565", type=pcm_av_seff_performance_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_performance_av_InfrastructureCall564", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
action__ResourceCall566: BinaryAssociation = BinaryAssociation(
    name="action__ResourceCall566",
    ends={
        Property(name="seff_av568", type=pcm_av_seff_performance_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractInternalControlFlowAction567", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceRequiredRole__ResourceCall569: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRole__ResourceCall569",
    ends={
        Property(name="entity_av_ResourceRequiredRole570", type=pcm_av_seff_performance_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_performance_av_ResourceCall", type=entity_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
signature__ResourceCall571: BinaryAssociation = BinaryAssociation(
    name="signature__ResourceCall571",
    ends={
        Property(name="ResourceSignature573", type=pcm_av_seff_performance_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_performance_av_ResourceCall572", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__ResourceCall574: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__ResourceCall574",
    ends={
        Property(name="core_av576", type=pcm_av_seff_performance_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable575", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification_ParametericResourceDemand577: BinaryAssociation = BinaryAssociation(
    name="specification_ParametericResourceDemand577",
    ends={
        Property(name="core_av579", type=pcm_av_seff_performance_av_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable578", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredResource_ParametricResourceDemand580: BinaryAssociation = BinaryAssociation(
    name="requiredResource_ParametricResourceDemand580",
    ends={
        Property(name="ProcessingResourceType581", type=pcm_av_seff_performance_av_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_performance_av_ParametricResourceDemand", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
action_ParametricResourceDemand582: BinaryAssociation = BinaryAssociation(
    name="action_ParametricResourceDemand582",
    ends={
        Property(name="seff_av584", type=pcm_av_seff_performance_av_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractInternalControlFlowAction583", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
recoveryAction__RecoveryActionBehaviour586: BinaryAssociation = BinaryAssociation(
    name="recoveryAction__RecoveryActionBehaviour586",
    ends={
        Property(name="seff_av587", type=pcm_av_seff_reliability_av_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_reliability_av", type=seff_reliability_av_RecoveryAction, multiplicity=Multiplicity(0, 1))
    }
)
primaryBehaviour__RecoveryAction588: BinaryAssociation = BinaryAssociation(
    name="primaryBehaviour__RecoveryAction588",
    ends={
        Property(name="seff_reliability_av_RecoveryActionBehaviour589", type=pcm_av_seff_reliability_av_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_reliability_av_RecoveryAction", type=seff_reliability_av_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
recoveryActionBehaviours__RecoveryAction590: BinaryAssociation = BinaryAssociation(
    name="recoveryActionBehaviours__RecoveryAction590",
    ends={
        Property(name="seff_av592", type=pcm_av_seff_reliability_av_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_reliability_av591", type=seff_reliability_av_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureTypes_FailureHandlingEntity593: BinaryAssociation = BinaryAssociation(
    name="failureTypes_FailureHandlingEntity593",
    ends={
        Property(name="FailureType594", type=pcm_av_seff_reliability_av_FailureHandlingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_reliability_av_FailureHandlingEntity", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
signature_SpecifiedQoSAnnation595: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedQoSAnnation595",
    ends={
        Property(name="Signature596", type=pcm_av_qosannotations_av_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_qosannotations_av_SpecifiedQoSAnnotation", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedQoSAnnotation597: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedQoSAnnotation597",
    ends={
        Property(name="Role", type=pcm_av_qosannotations_av_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_qosannotations_av_SpecifiedQoSAnnotation598", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
qosAnnotations_SpecifiedQoSAnnotation599: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedQoSAnnotation599",
    ends={
        Property(name="qosannotations_av600", type=pcm_av_qosannotations_av_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
failureHandlingAlternatives__RecoveryActionBehaviour585: BinaryAssociation = BinaryAssociation(
    name="failureHandlingAlternatives__RecoveryActionBehaviour585",
    ends={
        Property(name="seff_reliability_av_RecoveryActionBehaviour", type=pcm_av_seff_reliability_av_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_reliability_av_RecoveryActionBehaviour", type=seff_reliability_av_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999))
    }
)
system_QoSAnnotations604: BinaryAssociation = BinaryAssociation(
    name="system_QoSAnnotations604",
    ends={
        Property(name="system_av", type=pcm_av_qosannotations_av_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="System", type=System, multiplicity=Multiplicity(0, 1))
    }
)
specifiedQoSAnnotations_QoSAnnotations605: BinaryAssociation = BinaryAssociation(
    name="specifiedQoSAnnotations_QoSAnnotations605",
    ends={
        Property(name="qosannotations_av606", type=pcm_av_qosannotations_av_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="SpecifiedQoSAnnotation", type=SpecifiedQoSAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature_SpecifiedOutputParameterAbstraction607: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedOutputParameterAbstraction607",
    ends={
        Property(name="Signature608", type=pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedOutputParameterAbstraction609: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedOutputParameterAbstraction609",
    ends={
        Property(name="Role611", type=pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction610", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
expectedExternalOutputs_SpecifiedOutputParameterAbstraction612: BinaryAssociation = BinaryAssociation(
    name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction612",
    ends={
        Property(name="parameter_av614", type=pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage613", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qosAnnotations_SpecifiedOutputParameterAbstraction615: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedOutputParameterAbstraction615",
    ends={
        Property(name="qosannotations_av617", type=pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="QoSAnnotations616", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
specification_SpecifiedExecutionTime618: BinaryAssociation = BinaryAssociation(
    name="specification_SpecifiedExecutionTime618",
    ends={
        Property(name="core_av620", type=pcm_av_qos_performance_av_SpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable619", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext_ComponentSpecifiedExecutionTime621: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ComponentSpecifiedExecutionTime621",
    ends={
        Property(name="composition_av_AssemblyContext622", type=pcm_av_qos_performance_av_ComponentSpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_qos_performance_av_ComponentSpecifiedExecutionTime", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstractions_QoSAnnotations601: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstractions_QoSAnnotations601",
    ends={
        Property(name="qosannotations_av603", type=pcm_av_qosannotations_av_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="SpecifiedOutputParameterAbstraction602", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation623: BinaryAssociation = BinaryAssociation(
    name="externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation623",
    ends={
        Property(name="reliability_av624", type=pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ExternalFailureOccurrenceDescription", type=ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qosAnnotations_System625: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_System625",
    ends={
        Property(name="qosannotations_av627", type=pcm_av_system_av_System, multiplicity=Multiplicity(1, 1)),
        Property(name="QoSAnnotations626", type=QoSAnnotations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_ResourceEnvironment630: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ResourceEnvironment630",
    ends={
        Property(name="resourceenvironment_av631", type=pcm_av_resourceenvironment_av_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectedResourceContainers_LinkingResource632: BinaryAssociation = BinaryAssociation(
    name="connectedResourceContainers_LinkingResource632",
    ends={
        Property(name="ResourceContainer633", type=pcm_av_resourceenvironment_av_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_resourceenvironment_av_LinkingResource", type=ResourceContainer, multiplicity=Multiplicity(0, 9999))
    }
)
communicationLinkResourceSpecifications_LinkingResource634: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifications_LinkingResource634",
    ends={
        Property(name="resourceenvironment_av636", type=pcm_av_resourceenvironment_av_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceSpecification635", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceEnvironment_LinkingResource637: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_LinkingResource637",
    ends={
        Property(name="resourceenvironment_av638", type=pcm_av_resourceenvironment_av_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceEnvironment", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceSpecifications_ResourceContainer639: BinaryAssociation = BinaryAssociation(
    name="activeResourceSpecifications_ResourceContainer639",
    ends={
        Property(name="resourceenvironment_av641", type=pcm_av_resourceenvironment_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcessingResourceSpecification640", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceEnvironment_ResourceContainer642: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_ResourceContainer642",
    ends={
        Property(name="resourceenvironment_av644", type=pcm_av_resourceenvironment_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceEnvironment643", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
nestedResourceContainers__ResourceContainer645: BinaryAssociation = BinaryAssociation(
    name="nestedResourceContainers__ResourceContainer645",
    ends={
        Property(name="resourceenvironment_av647", type=pcm_av_resourceenvironment_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer646", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentResourceContainer__ResourceContainer648: BinaryAssociation = BinaryAssociation(
    name="parentResourceContainer__ResourceContainer648",
    ends={
        Property(name="resourceenvironment_av650", type=pcm_av_resourceenvironment_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer649", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
schedulingPolicy651: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicy651",
    ends={
        Property(name="SchedulingPolicy652", type=pcm_av_resourceenvironment_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_resourceenvironment_av_ProcessingResourceSpecification", type=SchedulingPolicy, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceType_ActiveResourceSpecification653: BinaryAssociation = BinaryAssociation(
    name="activeResourceType_ActiveResourceSpecification653",
    ends={
        Property(name="ProcessingResourceType655", type=pcm_av_resourceenvironment_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_resourceenvironment_av_ProcessingResourceSpecification654", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
processingRate_ProcessingResourceSpecification656: BinaryAssociation = BinaryAssociation(
    name="processingRate_ProcessingResourceSpecification656",
    ends={
        Property(name="core_av658", type=pcm_av_resourceenvironment_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable657", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
linkingResources__ResourceEnvironment628: BinaryAssociation = BinaryAssociation(
    name="linkingResources__ResourceEnvironment628",
    ends={
        Property(name="resourceenvironment_av629", type=pcm_av_resourceenvironment_av_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="LinkingResource", type=LinkingResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_ProcessingResourceSpecification659: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ProcessingResourceSpecification659",
    ends={
        Property(name="resourceenvironment_av661", type=pcm_av_resourceenvironment_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer660", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
linkingResource_CommunicationLinkResourceSpecification662: BinaryAssociation = BinaryAssociation(
    name="linkingResource_CommunicationLinkResourceSpecification662",
    ends={
        Property(name="resourceenvironment_av664", type=pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="LinkingResource663", type=LinkingResource, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceType_CommunicationLinkResourceSpecification665: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType_CommunicationLinkResourceSpecification665",
    ends={
        Property(name="CommunicationLinkResourceType666", type=pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
latency_CommunicationLinkResourceSpecification667: BinaryAssociation = BinaryAssociation(
    name="latency_CommunicationLinkResourceSpecification667",
    ends={
        Property(name="core_av669", type=pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable668", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throughput_CommunicationLinkResourceSpecification670: BinaryAssociation = BinaryAssociation(
    name="throughput_CommunicationLinkResourceSpecification670",
    ends={
        Property(name="core_av672", type=pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable671", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceContainer_AllocationContext673: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_AllocationContext673",
    ends={
        Property(name="ResourceContainer674", type=pcm_av_allocation_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_allocation_av_AllocationContext", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_AllocationContext675: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_AllocationContext675",
    ends={
        Property(name="composition_av_AssemblyContext677", type=pcm_av_allocation_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_allocation_av_AllocationContext676", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__AllocationContext679: BinaryAssociation = BinaryAssociation(
    name="eventChannel__AllocationContext679",
    ends={
        Property(name="composition_av_EventChannel", type=pcm_av_allocation_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_allocation_av_AllocationContext680", type=composition_av_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
targetResourceEnvironment_Allocation681: BinaryAssociation = BinaryAssociation(
    name="targetResourceEnvironment_Allocation681",
    ends={
        Property(name="ResourceEnvironment682", type=pcm_av_allocation_av_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_allocation_av_Allocation", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
system_Allocation683: BinaryAssociation = BinaryAssociation(
    name="system_Allocation683",
    ends={
        Property(name="System685", type=pcm_av_allocation_av_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_allocation_av_Allocation684", type=System, multiplicity=Multiplicity(0, 1))
    }
)
allocationContexts_Allocation686: BinaryAssociation = BinaryAssociation(
    name="allocationContexts_Allocation686",
    ends={
        Property(name="allocation_av687", type=pcm_av_allocation_av_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="AllocationContext", type=AllocationContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
completions_CompletionRepository688: BinaryAssociation = BinaryAssociation(
    name="completions_CompletionRepository688",
    ends={
        Property(name="Completion", type=pcm_av_completions_av_CompletionRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_completions_av_CompletionRepository", type=Completion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allocation_AllocationContext678: BinaryAssociation = BinaryAssociation(
    name="allocation_AllocationContext678",
    ends={
        Property(name="allocation_av", type=pcm_av_allocation_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="Allocation", type=Allocation, multiplicity=Multiplicity(0, 1))
    }
)
requiredCommunicationLinkResource_ParametricResourceDemand689: BinaryAssociation = BinaryAssociation(
    name="requiredCommunicationLinkResource_ParametricResourceDemand689",
    ends={
        Property(name="pcm_av_completions_av_NetworkDemandParametricResourceDemand", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1)),
        Property(name="CommunicationLinkResourceType690", type=pcm_av_completions_av_NetworkDemandParametricResourceDemand, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_pcm_av_core_av_PCMRandomVariable_RandomVariable = Generalization(general=RandomVariable, specific=pcm_av_core_av_PCMRandomVariable)
gen_pcm_av_entity_av_ResourceProvidedRole_Role = Generalization(general=Role, specific=pcm_av_entity_av_ResourceProvidedRole)
gen_pcm_av_entity_av_InterfaceProvidingRequiringEntity_entity_av_InterfaceProvidingEntity = Generalization(general=entity_av_InterfaceProvidingEntity, specific=pcm_av_entity_av_InterfaceProvidingRequiringEntity)
gen_pcm_av_entity_av_InterfaceProvidingRequiringEntity_entity_av_InterfaceRequiringEntity = Generalization(general=entity_av_InterfaceRequiringEntity, specific=pcm_av_entity_av_InterfaceProvidingRequiringEntity)
gen_pcm_av_entity_av_InterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_av_entity_av_InterfaceProvidingEntity)
gen_pcm_av_entity_av_InterfaceRequiringEntity_entity_av_Entity = Generalization(general=entity_av_Entity, specific=pcm_av_entity_av_InterfaceRequiringEntity)
gen_pcm_av_entity_av_InterfaceRequiringEntity_entity_av_ResourceInterfaceRequiringEntity = Generalization(general=entity_av_ResourceInterfaceRequiringEntity, specific=pcm_av_entity_av_InterfaceRequiringEntity)
gen_pcm_av_entity_av_ResourceInterfaceRequiringEntity_Entity = Generalization(general=Entity, specific=pcm_av_entity_av_ResourceInterfaceRequiringEntity)
gen_pcm_av_entity_av_ResourceRequiredRole_Role = Generalization(general=Role, specific=pcm_av_entity_av_ResourceRequiredRole)
gen_pcm_av_entity_av_ResourceInterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_av_entity_av_ResourceInterfaceProvidingEntity)
gen_pcm_av_entity_av_ResourceInterfaceProvidingRequiringEntity_entity_av_ResourceInterfaceRequiringEntity = Generalization(general=entity_av_ResourceInterfaceRequiringEntity, specific=pcm_av_entity_av_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_av_entity_av_ResourceInterfaceProvidingRequiringEntity_entity_av_ResourceInterfaceProvidingEntity = Generalization(general=entity_av_ResourceInterfaceProvidingEntity, specific=pcm_av_entity_av_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_av_entity_av_Entity_Identifier = Generalization(general=Identifier, specific=pcm_av_entity_av_Entity)
gen_pcm_av_entity_av_Entity_entity_av_NamedElement = Generalization(general=entity_av_NamedElement, specific=pcm_av_entity_av_Entity)
gen_pcm_av_composition_av_DelegationConnector_Connector = Generalization(general=Connector, specific=pcm_av_composition_av_DelegationConnector)
gen_pcm_av_composition_av_Connector_Entity = Generalization(general=Entity, specific=pcm_av_composition_av_Connector)
gen_pcm_av_composition_av_ComposedStructure_Entity = Generalization(general=Entity, specific=pcm_av_composition_av_ComposedStructure)
gen_pcm_av_entity_av_ComposedProvidingRequiringEntity_composition_av_ComposedStructure = Generalization(general=composition_av_ComposedStructure, specific=pcm_av_entity_av_ComposedProvidingRequiringEntity)
gen_pcm_av_entity_av_ComposedProvidingRequiringEntity_entity_av_InterfaceProvidingRequiringEntity = Generalization(general=entity_av_InterfaceProvidingRequiringEntity, specific=pcm_av_entity_av_ComposedProvidingRequiringEntity)
gen_pcm_av_composition_av_EventChannel_Entity = Generalization(general=Entity, specific=pcm_av_composition_av_EventChannel)
gen_pcm_av_composition_av_EventChannelSourceConnector_Connector = Generalization(general=Connector, specific=pcm_av_composition_av_EventChannelSourceConnector)
gen_pcm_av_composition_av_EventChannelSinkConnector_Connector = Generalization(general=Connector, specific=pcm_av_composition_av_EventChannelSinkConnector)
gen_pcm_av_composition_av_ProvidedDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_composition_av_ProvidedDelegationConnector)
gen_pcm_av_composition_av_RequiredDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_composition_av_RequiredDelegationConnector)
gen_pcm_av_composition_av_AssemblyConnector_Connector = Generalization(general=Connector, specific=pcm_av_composition_av_AssemblyConnector)
gen_pcm_av_composition_av_AssemblyEventConnector_Connector = Generalization(general=Connector, specific=pcm_av_composition_av_AssemblyEventConnector)
gen_pcm_av_composition_av_SourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_composition_av_SourceDelegationConnector)
gen_pcm_av_composition_av_AssemblyInfrastructureConnector_Connector = Generalization(general=Connector, specific=pcm_av_composition_av_AssemblyInfrastructureConnector)
gen_pcm_av_composition_av_ProvidedInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_composition_av_ProvidedInfrastructureDelegationConnector)
gen_pcm_av_composition_av_RequiredInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_composition_av_RequiredInfrastructureDelegationConnector)
gen_pcm_av_composition_av_RequiredResourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_composition_av_RequiredResourceDelegationConnector)
gen_pcm_av_composition_av_SinkDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_composition_av_SinkDelegationConnector)
gen_pcm_av_usagemodel_av_UsageScenario_Entity = Generalization(general=Entity, specific=pcm_av_usagemodel_av_UsageScenario)
gen_pcm_av_composition_av_AssemblyContext_Entity = Generalization(general=Entity, specific=pcm_av_composition_av_AssemblyContext)
gen_pcm_av_usagemodel_av_AbstractUserAction_Entity = Generalization(general=Entity, specific=pcm_av_usagemodel_av_AbstractUserAction)
gen_pcm_av_usagemodel_av_ScenarioBehaviour_Entity = Generalization(general=Entity, specific=pcm_av_usagemodel_av_ScenarioBehaviour)
gen_pcm_av_usagemodel_av_EntryLevelSystemCall_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_usagemodel_av_EntryLevelSystemCall)
gen_pcm_av_usagemodel_av_Branch_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_usagemodel_av_Branch)
gen_pcm_av_usagemodel_av_Loop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_usagemodel_av_Loop)
gen_pcm_av_usagemodel_av_Start_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_usagemodel_av_Start)
gen_pcm_av_usagemodel_av_OpenWorkload_Workload = Generalization(general=Workload, specific=pcm_av_usagemodel_av_OpenWorkload)
gen_pcm_av_usagemodel_av_Delay_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_usagemodel_av_Delay)
gen_pcm_av_usagemodel_av_ClosedWorkload_Workload = Generalization(general=Workload, specific=pcm_av_usagemodel_av_ClosedWorkload)
gen_pcm_av_usagemodel_av_Stop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_usagemodel_av_Stop)
gen_pcm_av_repository_av_PassiveResource_Entity = Generalization(general=Entity, specific=pcm_av_repository_av_PassiveResource)
gen_pcm_av_repository_av_BasicComponent_ImplementationComponentType = Generalization(general=ImplementationComponentType, specific=pcm_av_repository_av_BasicComponent)
gen_pcm_av_repository_av_RepositoryComponent_InterfaceProvidingRequiringEntity = Generalization(general=InterfaceProvidingRequiringEntity, specific=pcm_av_repository_av_RepositoryComponent)
gen_pcm_av_repository_av_ProvidedRole_Role = Generalization(general=Role, specific=pcm_av_repository_av_ProvidedRole)
gen_pcm_av_repository_av_ImplementationComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_av_repository_av_ImplementationComponentType)
gen_pcm_av_repository_av_Repository_Entity = Generalization(general=Entity, specific=pcm_av_repository_av_Repository)
gen_pcm_av_repository_av_Interface_Entity = Generalization(general=Entity, specific=pcm_av_repository_av_Interface)
gen_pcm_av_repository_av_EventGroup_Interface = Generalization(general=Interface, specific=pcm_av_repository_av_EventGroup)
gen_pcm_av_repository_av_Signature_Entity = Generalization(general=Entity, specific=pcm_av_repository_av_Signature)
gen_pcm_av_repository_av_InfrastructureSignature_Signature = Generalization(general=Signature, specific=pcm_av_repository_av_InfrastructureSignature)
gen_pcm_av_repository_av_InfrastructureInterface_Interface = Generalization(general=Interface, specific=pcm_av_repository_av_InfrastructureInterface)
gen_pcm_av_repository_av_EventType_Signature = Generalization(general=Signature, specific=pcm_av_repository_av_EventType)
gen_pcm_av_repository_av_InfrastructureRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_av_repository_av_InfrastructureRequiredRole)
gen_pcm_av_repository_av_RequiredRole_Role = Generalization(general=Role, specific=pcm_av_repository_av_RequiredRole)
gen_pcm_av_repository_av_OperationSignature_Signature = Generalization(general=Signature, specific=pcm_av_repository_av_OperationSignature)
gen_pcm_av_repository_av_OperationRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_av_repository_av_OperationRequiredRole)
gen_pcm_av_repository_av_SourceRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_av_repository_av_SourceRole)
gen_pcm_av_repository_av_SinkRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_av_repository_av_SinkRole)
gen_pcm_av_repository_av_OperationProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_av_repository_av_OperationProvidedRole)
gen_pcm_av_repository_av_InfrastructureProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_av_repository_av_InfrastructureProvidedRole)
gen_pcm_av_repository_av_CompleteComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_av_repository_av_CompleteComponentType)
gen_pcm_av_repository_av_OperationInterface_Interface = Generalization(general=Interface, specific=pcm_av_repository_av_OperationInterface)
gen_pcm_av_repository_av_ProvidesComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_av_repository_av_ProvidesComponentType)
gen_pcm_av_repository_av_CompositeComponent_entity_av_ComposedProvidingRequiringEntity = Generalization(general=entity_av_ComposedProvidingRequiringEntity, specific=pcm_av_repository_av_CompositeComponent)
gen_pcm_av_repository_av_CompositeComponent_repository_av_ImplementationComponentType = Generalization(general=repository_av_ImplementationComponentType, specific=pcm_av_repository_av_CompositeComponent)
gen_pcm_av_repository_av_PrimitiveDataType_DataType = Generalization(general=DataType, specific=pcm_av_repository_av_PrimitiveDataType)
gen_pcm_av_repository_av_CollectionDataType_entity_av_Entity = Generalization(general=entity_av_Entity, specific=pcm_av_repository_av_CollectionDataType)
gen_pcm_av_repository_av_CollectionDataType_repository_av_DataType = Generalization(general=repository_av_DataType, specific=pcm_av_repository_av_CollectionDataType)
gen_pcm_av_repository_av_CompositeDataType_entity_av_Entity = Generalization(general=entity_av_Entity, specific=pcm_av_repository_av_CompositeDataType)
gen_pcm_av_repository_av_CompositeDataType_repository_av_DataType = Generalization(general=repository_av_DataType, specific=pcm_av_repository_av_CompositeDataType)
gen_pcm_av_repository_av_InnerDeclaration_NamedElement = Generalization(general=NamedElement, specific=pcm_av_repository_av_InnerDeclaration)
gen_pcm_av_repository_av_Role_Entity = Generalization(general=Entity, specific=pcm_av_repository_av_Role)
gen_pcm_av_resourcetype_av_ResourceSignature_Entity = Generalization(general=Entity, specific=pcm_av_resourcetype_av_ResourceSignature)
gen_pcm_av_resourcetype_av_SchedulingPolicy_Entity = Generalization(general=Entity, specific=pcm_av_resourcetype_av_SchedulingPolicy)
gen_pcm_av_resourcetype_av_CommunicationLinkResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_av_resourcetype_av_CommunicationLinkResourceType)
gen_pcm_av_resourcetype_av_ResourceInterface_Entity = Generalization(general=Entity, specific=pcm_av_resourcetype_av_ResourceInterface)
gen_pcm_av_resourcetype_av_ProcessingResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_av_resourcetype_av_ProcessingResourceType)
gen_pcm_av_resourcetype_av_ResourceType_entity_av_Entity = Generalization(general=entity_av_Entity, specific=pcm_av_resourcetype_av_ResourceType)
gen_pcm_av_resourcetype_av_ResourceType_UnitCarryingElement = Generalization(general=UnitCarryingElement, specific=pcm_av_resourcetype_av_ResourceType)
gen_pcm_av_resourcetype_av_ResourceType_entity_av_ResourceInterfaceProvidingEntity = Generalization(general=entity_av_ResourceInterfaceProvidingEntity, specific=pcm_av_resourcetype_av_ResourceType)
gen_pcm_av_parameter_av_CharacterisedVariable_Variable = Generalization(general=Variable, specific=pcm_av_parameter_av_CharacterisedVariable)
gen_pcm_av_reliability_av_HardwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_av_reliability_av_HardwareInducedFailureType)
gen_pcm_av_reliability_av_SoftwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_av_reliability_av_SoftwareInducedFailureType)
gen_pcm_av_reliability_av_InternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_av_reliability_av_InternalFailureOccurrenceDescription)
gen_pcm_av_reliability_av_NetworkInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_av_reliability_av_NetworkInducedFailureType)
gen_pcm_av_reliability_av_ResourceTimeoutFailureType_SoftwareInducedFailureType = Generalization(general=SoftwareInducedFailureType, specific=pcm_av_reliability_av_ResourceTimeoutFailureType)
gen_pcm_av_reliability_av_FailureType_Entity = Generalization(general=Entity, specific=pcm_av_reliability_av_FailureType)
gen_pcm_av_seff_av_StopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_seff_av_StopAction)
gen_pcm_av_seff_av_AbstractInternalControlFlowAction_AbstractAction = Generalization(general=AbstractAction, specific=pcm_av_seff_av_AbstractInternalControlFlowAction)
gen_pcm_av_seff_av_AbstractAction_Entity = Generalization(general=Entity, specific=pcm_av_seff_av_AbstractAction)
gen_pcm_av_reliability_av_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_av_reliability_av_ExternalFailureOccurrenceDescription)
gen_pcm_av_seff_av_AbstractLoopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_seff_av_AbstractLoopAction)
gen_pcm_av_seff_av_AbstractBranchTransition_Entity = Generalization(general=Entity, specific=pcm_av_seff_av_AbstractBranchTransition)
gen_pcm_av_seff_av_ResourceDemandingBehaviour_Identifier = Generalization(general=Identifier, specific=pcm_av_seff_av_ResourceDemandingBehaviour)
gen_pcm_av_seff_av_StartAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_seff_av_StartAction)
gen_pcm_av_seff_av_ResourceDemandingSEFF_Identifier = Generalization(general=Identifier, specific=pcm_av_seff_av_ResourceDemandingSEFF)
gen_pcm_av_seff_av_ResourceDemandingSEFF_seff_av_ServiceEffectSpecification = Generalization(general=seff_av_ServiceEffectSpecification, specific=pcm_av_seff_av_ResourceDemandingSEFF)
gen_pcm_av_seff_av_ResourceDemandingSEFF_seff_av_ResourceDemandingBehaviour = Generalization(general=seff_av_ResourceDemandingBehaviour, specific=pcm_av_seff_av_ResourceDemandingSEFF)
gen_pcm_av_seff_av_BranchAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_seff_av_BranchAction)
gen_pcm_av_seff_av_ReleaseAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_seff_av_ReleaseAction)
gen_pcm_av_seff_av_LoopAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_av_seff_av_LoopAction)
gen_pcm_av_seff_av_ForkAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_seff_av_ForkAction)
gen_pcm_av_seff_av_ForkedBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_av_seff_av_ForkedBehaviour)
gen_pcm_av_seff_av_ExternalCallAction_seff_av_AbstractAction = Generalization(general=seff_av_AbstractAction, specific=pcm_av_seff_av_ExternalCallAction)
gen_pcm_av_seff_av_ExternalCallAction_seff_av_CallReturnAction = Generalization(general=seff_av_CallReturnAction, specific=pcm_av_seff_av_ExternalCallAction)
gen_pcm_av_seff_av_ExternalCallAction_seff_reliability_av_FailureHandlingEntity = Generalization(general=seff_reliability_av_FailureHandlingEntity, specific=pcm_av_seff_av_ExternalCallAction)
gen_pcm_av_seff_av_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_av_seff_av_ResourceDemandingInternalBehaviour)
gen_pcm_av_seff_av_CallReturnAction_CallAction = Generalization(general=CallAction, specific=pcm_av_seff_av_CallReturnAction)
gen_pcm_av_seff_av_ProbabilisticBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_av_seff_av_ProbabilisticBranchTransition)
gen_pcm_av_seff_av_AcquireAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_seff_av_AcquireAction)
gen_pcm_av_seff_av_CollectionIteratorAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_av_seff_av_CollectionIteratorAction)
gen_pcm_av_seff_av_GuardedBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_av_seff_av_GuardedBranchTransition)
gen_pcm_av_seff_av_SetVariableAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_seff_av_SetVariableAction)
gen_pcm_av_seff_av_InternalCallAction_seff_av_CallAction = Generalization(general=seff_av_CallAction, specific=pcm_av_seff_av_InternalCallAction)
gen_pcm_av_seff_av_InternalCallAction_seff_av_AbstractInternalControlFlowAction = Generalization(general=seff_av_AbstractInternalControlFlowAction, specific=pcm_av_seff_av_InternalCallAction)
gen_pcm_av_seff_av_EmitEventAction_seff_av_AbstractAction = Generalization(general=seff_av_AbstractAction, specific=pcm_av_seff_av_EmitEventAction)
gen_pcm_av_seff_av_EmitEventAction_seff_av_CallAction = Generalization(general=seff_av_CallAction, specific=pcm_av_seff_av_EmitEventAction)
gen_pcm_av_seff_av_InternalAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_seff_av_InternalAction)
gen_pcm_av_seff_performance_av_InfrastructureCall_CallAction = Generalization(general=CallAction, specific=pcm_av_seff_performance_av_InfrastructureCall)
gen_pcm_av_seff_performance_av_ResourceCall_CallAction = Generalization(general=CallAction, specific=pcm_av_seff_performance_av_ResourceCall)
gen_pcm_av_seff_reliability_av_RecoveryActionBehaviour_seff_reliability_av_FailureHandlingEntity = Generalization(general=seff_reliability_av_FailureHandlingEntity, specific=pcm_av_seff_reliability_av_RecoveryActionBehaviour)
gen_pcm_av_seff_reliability_av_RecoveryActionBehaviour_seff_av_ResourceDemandingBehaviour = Generalization(general=seff_av_ResourceDemandingBehaviour, specific=pcm_av_seff_reliability_av_RecoveryActionBehaviour)
gen_pcm_av_seff_reliability_av_RecoveryAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_seff_reliability_av_RecoveryAction)
gen_pcm_av_seff_reliability_av_FailureHandlingEntity_Entity = Generalization(general=Entity, specific=pcm_av_seff_reliability_av_FailureHandlingEntity)
gen_pcm_av_qosannotations_av_QoSAnnotations_Entity = Generalization(general=Entity, specific=pcm_av_qosannotations_av_QoSAnnotations)
gen_pcm_av_qos_performance_av_SystemSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_av_qos_performance_av_SystemSpecifiedExecutionTime)
gen_pcm_av_qos_performance_av_SpecifiedExecutionTime_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_av_qos_performance_av_SpecifiedExecutionTime)
gen_pcm_av_qos_performance_av_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_av_qos_performance_av_ComponentSpecifiedExecutionTime)
gen_pcm_av_system_av_System_entity_av_Entity = Generalization(general=entity_av_Entity, specific=pcm_av_system_av_System)
gen_pcm_av_system_av_System_entity_av_ComposedProvidingRequiringEntity = Generalization(general=entity_av_ComposedProvidingRequiringEntity, specific=pcm_av_system_av_System)
gen_pcm_av_resourceenvironment_av_ResourceEnvironment_NamedElement = Generalization(general=NamedElement, specific=pcm_av_resourceenvironment_av_ResourceEnvironment)
gen_pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation)
gen_pcm_av_resourceenvironment_av_LinkingResource_Entity = Generalization(general=Entity, specific=pcm_av_resourceenvironment_av_LinkingResource)
gen_pcm_av_resourceenvironment_av_ResourceContainer_Entity = Generalization(general=Entity, specific=pcm_av_resourceenvironment_av_ResourceContainer)
gen_pcm_av_resourceenvironment_av_ProcessingResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_av_resourceenvironment_av_ProcessingResourceSpecification)
gen_pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification)
gen_pcm_av_allocation_av_AllocationContext_Entity = Generalization(general=Entity, specific=pcm_av_allocation_av_AllocationContext)
gen_pcm_av_allocation_av_Allocation_Entity = Generalization(general=Entity, specific=pcm_av_allocation_av_Allocation)
gen_pcm_av_subsystem_av_SubSystem_entity_av_ComposedProvidingRequiringEntity = Generalization(general=entity_av_ComposedProvidingRequiringEntity, specific=pcm_av_subsystem_av_SubSystem)
gen_pcm_av_subsystem_av_SubSystem_repository_av_RepositoryComponent = Generalization(general=repository_av_RepositoryComponent, specific=pcm_av_subsystem_av_SubSystem)
gen_pcm_av_completions_av_Completion_entity_av_ComposedProvidingRequiringEntity = Generalization(general=entity_av_ComposedProvidingRequiringEntity, specific=pcm_av_completions_av_Completion)
gen_pcm_av_completions_av_Completion_repository_av_ImplementationComponentType = Generalization(general=repository_av_ImplementationComponentType, specific=pcm_av_completions_av_Completion)
gen_pcm_av_completions_av_DelegatingExternalCallAction_ExternalCallAction = Generalization(general=ExternalCallAction, specific=pcm_av_completions_av_DelegatingExternalCallAction)
gen_pcm_av_completions_av_NetworkDemandParametricResourceDemand_ParametricResourceDemand = Generalization(general=ParametricResourceDemand, specific=pcm_av_completions_av_NetworkDemandParametricResourceDemand)

# Domain Model
domain_model = DomainModel(
    name="pcm_av",
    types={pcm_av_DummyClass, pcm_av_Advice, pcm_av_EObject, pcm_av_GlobalScope, pcm_av_PerJoinPointScope, pcm_av_core_av_PCMRandomVariable, RandomVariable, ClosedWorkload, PassiveResource, VariableCharacterisation, seff_performance_av_InfrastructureCall, seff_performance_av_ResourceCall, seff_performance_av_ParametricResourceDemand, LoopAction, GuardedBranchTransition, qos_performance_av_SpecifiedExecutionTime, composition_av_EventChannelSinkConnector, OpenWorkload, Delay, CommunicationLinkResourceSpecification, ProcessingResourceSpecification, pcm_av_entity_av_ResourceProvidedRole, Role, entity_av_ResourceInterfaceProvidingEntity, ResourceInterface, pcm_av_entity_av_InterfaceProvidingRequiringEntity, entity_av_InterfaceProvidingEntity, entity_av_InterfaceRequiringEntity, pcm_av_entity_av_InterfaceProvidingEntity, Entity, ProvidedRole, pcm_av_entity_av_InterfaceRequiringEntity, entity_av_Entity, entity_av_ResourceInterfaceRequiringEntity, RequiredRole, pcm_av_entity_av_ResourceInterfaceRequiringEntity, entity_av_ResourceRequiredRole, pcm_av_entity_av_ResourceRequiredRole, pcm_av_entity_av_ResourceInterfaceProvidingEntity, composition_av_AssemblyEventConnector, Loop, pcm_av_entity_av_NamedElement, pcm_av_entity_av_ResourceInterfaceProvidingRequiringEntity, pcm_av_entity_av_Entity, Identifier, entity_av_NamedElement, pcm_av_composition_av_DelegationConnector, Connector, pcm_av_composition_av_Connector, pcm_av_composition_av_ComposedStructure, composition_av_AssemblyContext, composition_av_ResourceRequiredDelegationConnector, entity_av_ResourceProvidedRole, pcm_av_entity_av_ComposedProvidingRequiringEntity, composition_av_ComposedStructure, entity_av_InterfaceProvidingRequiringEntity, pcm_av_composition_av_ResourceRequiredDelegationConnector, pcm_av_composition_av_EventChannel, EventGroup, composition_av_EventChannelSourceConnector, pcm_av_composition_av_EventChannelSourceConnector, SourceRole, pcm_av_composition_av_EventChannelSinkConnector, SinkRole, PCMRandomVariable, pcm_av_composition_av_ProvidedDelegationConnector, DelegationConnector, composition_av_EventChannel, OperationProvidedRole, composition_av_Connector, pcm_av_composition_av_RequiredDelegationConnector, OperationRequiredRole, pcm_av_composition_av_AssemblyConnector, pcm_av_composition_av_AssemblyEventConnector, pcm_av_composition_av_SourceDelegationConnector, pcm_av_composition_av_AssemblyInfrastructureConnector, InfrastructureProvidedRole, InfrastructureRequiredRole, pcm_av_composition_av_ProvidedInfrastructureDelegationConnector, pcm_av_composition_av_RequiredInfrastructureDelegationConnector, pcm_av_composition_av_RequiredResourceDelegationConnector, pcm_av_composition_av_SinkDelegationConnector, pcm_av_usagemodel_av_Workload, UsageScenario, pcm_av_usagemodel_av_UsageScenario, UsageModel, ScenarioBehaviour, Workload, pcm_av_usagemodel_av_UserData, pcm_av_usagemodel_av_UsageModel, UserData, pcm_av_composition_av_AssemblyContext, RepositoryComponent, VariableUsage, OperationSignature, pcm_av_usagemodel_av_AbstractUserAction, pcm_av_usagemodel_av_ScenarioBehaviour, pcm_av_usagemodel_av_EntryLevelSystemCall, AbstractUserAction, BranchTransition, pcm_av_usagemodel_av_BranchTransition, Branch, pcm_av_usagemodel_av_Branch, pcm_av_usagemodel_av_Loop, pcm_av_usagemodel_av_Start, pcm_av_usagemodel_av_OpenWorkload, pcm_av_usagemodel_av_Delay, pcm_av_usagemodel_av_ClosedWorkload, pcm_av_usagemodel_av_Stop, pcm_av_repository_av_PassiveResource, BasicComponent, ResourceTimeoutFailureType, pcm_av_repository_av_BasicComponent, ImplementationComponentType, ServiceEffectSpecification, CompleteComponentType, pcm_av_repository_av_RepositoryComponent, InterfaceProvidingRequiringEntity, Repository, pcm_av_repository_av_ProvidedRole, pcm_av_repository_av_ImplementationComponentType, EventType, ResourceSignature, pcm_av_repository_av_DataType, pcm_av_repository_av_Repository, Interface, FailureType, pcm_av_repository_av_Interface, pcm_av_repository_av_Parameter, DataType, InfrastructureSignature, Protocol, RequiredCharacterisation, pcm_av_repository_av_RequiredCharacterisation, Parameter_, pcm_av_repository_av_EventGroup, pcm_av_repository_av_Signature, ExceptionType, pcm_av_repository_av_ExceptionType, pcm_av_repository_av_InfrastructureSignature, InfrastructureInterface, pcm_av_repository_av_InfrastructureInterface, pcm_av_repository_av_EventType, Signature, pcm_av_repository_av_InfrastructureRequiredRole, pcm_av_repository_av_RequiredRole, pcm_av_repository_av_OperationSignature, OperationInterface, pcm_av_repository_av_OperationRequiredRole, pcm_av_repository_av_SourceRole, pcm_av_repository_av_SinkRole, pcm_av_repository_av_OperationProvidedRole, pcm_av_repository_av_InfrastructureProvidedRole, pcm_av_repository_av_CompleteComponentType, pcm_av_repository_av_OperationInterface, ProvidesComponentType, pcm_av_repository_av_ProvidesComponentType, pcm_av_repository_av_CompositeComponent, entity_av_ComposedProvidingRequiringEntity, repository_av_ImplementationComponentType, pcm_av_repository_av_PrimitiveDataType, pcm_av_repository_av_CollectionDataType, repository_av_DataType, pcm_av_repository_av_CompositeDataType, CompositeDataType, InnerDeclaration, pcm_av_repository_av_InnerDeclaration, NamedElement, pcm_av_repository_av_Role, pcm_av_resourcetype_av_ResourceSignature, ResourceRepository, pcm_av_resourcetype_av_ResourceRepository, SchedulingPolicy, pcm_av_resourcetype_av_SchedulingPolicy, pcm_av_resourcetype_av_CommunicationLinkResourceType, NetworkInducedFailureType, pcm_av_resourcetype_av_ResourceInterface, pcm_av_protocol_av_Protocol, pcm_av_parameter_av_VariableUsage, pcm_av_resourcetype_av_ProcessingResourceType, ResourceType, HardwareInducedFailureType, pcm_av_resourcetype_av_ResourceType, UnitCarryingElement, SpecifiedOutputParameterAbstraction, EntryLevelSystemCall, parameter_av_pcm_av_AbstractNamedReference, pcm_av_parameter_av_VariableCharacterisation, pcm_av_parameter_av_CharacterisedVariable, Variable, pcm_av_reliability_av_FailureOccurrenceDescription, CallAction, SynchronisationPoint, CallReturnAction, SetVariableAction, pcm_av_reliability_av_HardwareInducedFailureType, ProcessingResourceType, pcm_av_reliability_av_SoftwareInducedFailureType, InternalFailureOccurrenceDescription, pcm_av_reliability_av_InternalFailureOccurrenceDescription, FailureOccurrenceDescription, InternalAction, SoftwareInducedFailureType, pcm_av_reliability_av_NetworkInducedFailureType, qos_reliability_av_SpecifiedReliabilityAnnotation, pcm_av_reliability_av_ResourceTimeoutFailureType, pcm_av_reliability_av_FailureType, pcm_av_seff_av_StopAction, AbstractInternalControlFlowAction, pcm_av_seff_av_AbstractInternalControlFlowAction, AbstractAction, pcm_av_seff_av_AbstractAction, CommunicationLinkResourceType, pcm_av_reliability_av_ExternalFailureOccurrenceDescription, AbstractLoopAction, AbstractBranchTransition, pcm_av_seff_av_AbstractLoopAction, pcm_av_seff_av_AbstractBranchTransition, BranchAction, pcm_av_seff_av_BranchAction, ResourceDemandingBehaviour, pcm_av_seff_av_ResourceDemandingBehaviour, pcm_av_seff_av_CallAction, pcm_av_seff_av_StartAction, pcm_av_seff_av_ServiceEffectSpecification, pcm_av_seff_av_ResourceDemandingSEFF, seff_av_ServiceEffectSpecification, seff_av_ResourceDemandingBehaviour, pcm_av_seff_av_ReleaseAction, pcm_av_seff_av_LoopAction, pcm_av_seff_av_ForkAction, ForkedBehaviour, pcm_av_seff_av_ForkedBehaviour, ForkAction, pcm_av_seff_av_SynchronisationPoint, pcm_av_seff_av_ExternalCallAction, seff_av_AbstractAction, seff_av_CallReturnAction, seff_reliability_av_FailureHandlingEntity, ResourceDemandingInternalBehaviour, pcm_av_seff_av_ResourceDemandingInternalBehaviour, ResourceDemandingSEFF, pcm_av_seff_av_CallReturnAction, pcm_av_seff_av_ProbabilisticBranchTransition, pcm_av_seff_av_AcquireAction, pcm_av_seff_av_CollectionIteratorAction, pcm_av_seff_av_GuardedBranchTransition, pcm_av_seff_av_SetVariableAction, pcm_av_seff_av_InternalCallAction, seff_av_CallAction, seff_av_AbstractInternalControlFlowAction, pcm_av_seff_av_EmitEventAction, pcm_av_seff_av_InternalAction, pcm_av_seff_performance_av_InfrastructureCall, pcm_av_seff_performance_av_ResourceCall, pcm_av_seff_performance_av_ParametricResourceDemand, pcm_av_seff_reliability_av_RecoveryActionBehaviour, seff_reliability_av_RecoveryAction, pcm_av_seff_reliability_av_RecoveryAction, pcm_av_seff_reliability_av_FailureHandlingEntity, pcm_av_qosannotations_av_SpecifiedQoSAnnotation, QoSAnnotations, pcm_av_qosannotations_av_QoSAnnotations, seff_reliability_av_RecoveryActionBehaviour, SpecifiedQoSAnnotation, pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction, pcm_av_qos_performance_av_SystemSpecifiedExecutionTime, SpecifiedExecutionTime, pcm_av_qos_performance_av_SpecifiedExecutionTime, pcm_av_qos_performance_av_ComponentSpecifiedExecutionTime, System, ExternalFailureOccurrenceDescription, pcm_av_system_av_System, pcm_av_resourceenvironment_av_ResourceEnvironment, pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation, ResourceContainer, pcm_av_resourceenvironment_av_LinkingResource, ResourceEnvironment, pcm_av_resourceenvironment_av_ResourceContainer, pcm_av_resourceenvironment_av_ProcessingResourceSpecification, LinkingResource, pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification, pcm_av_allocation_av_AllocationContext, pcm_av_allocation_av_Allocation, AllocationContext, pcm_av_subsystem_av_SubSystem, repository_av_RepositoryComponent, pcm_av_completions_av_Completion, pcm_av_completions_av_CompletionRepository, Completion, Allocation, pcm_av_completions_av_DelegatingExternalCallAction, ExternalCallAction, pcm_av_completions_av_NetworkDemandParametricResourceDemand, ParametricResourceDemand, ParameterModifier, ComponentType, PrimitiveTypeEnum, VariableCharacterisationType},
    associations={children0, scopedObject1, scopedObject3, closedWorkload_PCMRandomVariable5, passiveResource_capacity_PCMRandomVariable6, variableCharacterisation_Specification7, infrastructureCall__PCMRandomVariable8, resourceCall__PCMRandomVariable9, parametricResourceDemand_PCMRandomVariable12, loopAction_PCMRandomVariable15, guardedBranchTransition_PCMRandomVariable17, specifiedExecutionTime_PCMRandomVariable19, eventChannelSinkConnector__FilterCondition20, openWorkload_PCMRandomVariable26, delay_TimeSpecification28, communicationLinkResourceSpecifcation_throughput_PCMRandomVariable30, processingResourceSpecification_processingRate_PCMRandomVariable31, communicationLinkResourceSpecification_latency_PCMRandomVariable33, resourceInterfaceProvidingEntity__ResourceProvidedRole36, providedResourceInterface__ResourceProvidedRole38, providedRoles_InterfaceProvidingEntity39, requiredRoles_InterfaceRequiringEntity41, resourceRequiredRoles__ResourceInterfaceRequiringEntity43, requiredResourceInterface__ResourceRequiredRole46, resourceInterfaceRequiringEntity__ResourceRequiredRole48, assemblyEventConnector__FilterCondition21, loop_LoopIteration24, parentStructure__Connector54, assemblyContexts__ComposedStructure57, resourceRequiredDelegationConnectors_ComposedStructure60, resourceProvidedRoles__ResourceInterfaceProvidingEntity51, connectors__ComposedStructure66, innerResourceRequiredRole_ResourceRequiredDelegationConnector69, outerResourceRequiredRole_ResourceRequiredDelegationConnector70, parentStructure_ResourceRequiredDelegationConnector73, eventGroup__EventChannel76, eventChannelSourceConnector__EventChannel77, eventChannelSinkConnector__EventChannel80, parentStructure__EventChannel83, sourceRole__EventChannelSourceRole86, assemblyContext__EventChannelSourceConnector87, eventChannel__EventChannelSourceConnector89, sinkRole__EventChannelSinkConnector92, filterCondition__EventChannelSinkConnector93, assemblyContext__EventChannelSinkConnector95, eventChannel__EventChannelSinkConnector98, eventChannel__ComposedStructure63, innerProvidedRole_ProvidedDelegationConnector101, outerProvidedRole_ProvidedDelegationConnector102, assemblyContext_ProvidedDelegationConnector105, innerRequiredRole_RequiredDelegationConnector108, outerRequiredRole_RequiredDelegationConnector109, assemblyContext_RequiredDelegationConnector112, requiringAssemblyContext_AssemblyConnector115, providingAssemblyContext_AssemblyConnector117, providedRole_AssemblyConnector120, requiredRole_AssemblyConnector123, sinkRole__AssemblyEventConnector126, sourceRole__AssemblyEventConnector128, sinkAssemblyContext__AssemblyEventConnector131, sourceAssemblyContext__AssemblyEventConnector134, filterCondition__AssemblyEventConnector137, innerSourceRole__SourceRole140, outerSourceRole__SourceRole142, outerSinkRole__SinkRole153, providedRole__AssemblyInfrastructureConnector156, requiredRole__AssemblyInfrastructureConnector157, providingAssemblyContext__AssemblyInfrastructureConnector159, requiringAssemblyContext__AssemblyInfrastructureConnector162, innerProvidedRole__ProvidedInfrastructureDelegationConnector165, outerProvidedRole__ProvidedInfrastructureDelegationConnector167, assemblyContext__ProvidedInfrastructureDelegationConnector170, innerRequiredRole__RequiredInfrastructureDelegationConnector173, outerRequiredRole__RequiredInfrastructureDelegationConnector175, assemblyContext__RequiredInfrastructureDelegationConnector178, assemblyContext__RequiredResourceDelegationConnector181, innerRequiredRole__RequiredResourceDelegationConnector183, outerRequiredRole__RequiredResourceDelegationConnector186, assemblyContext__SourceDelegationConnector145, assemblyContext__SinkDelegationConnector148, innerSinkRole__SinkRole150, usageScenario_Workload195, usageModel_UsageScenario197, scenarioBehaviour_UsageScenario199, workload_UsageScenario201, assemblyContext_userData203, usageModel_UserData205, userDataParameterUsages_UserData208, usageScenario_UsageModel211, parentStructure__AssemblyContext189, encapsulatedComponent__AssemblyContext192, configParameterUsages__AssemblyContext193, providedRole_EntryLevelSystemCall216, operationSignature__EntryLevelSystemCall218, outputParameterUsages_EntryLevelSystemCall220, inputParameterUsages_EntryLevelSystemCall223, successor226, predecessor228, scenarioBehaviour_AbstractUserAction231, userData_UsageModel214, usageScenario_SenarioBehaviour234, branchTransition_ScenarioBehaviour237, loop_ScenarioBehaviour239, actions_ScenarioBehaviour242, branch_BranchTransition245, branchedBehaviour_BranchTransition247, branchTransitions_Branch250, loopIteration_Loop253, interArrivalTime_OpenWorkload259, timeSpecification_Delay262, bodyBehaviour_Loop256, thinkTime_ClosedWorkload265, capacity_PassiveResource268, basicComponent_PassiveResource271, resourceTimeoutFailureType__PassiveResource273, parentCompleteComponentTypes279, componentParameterUsage_ImplementationComponentType280, repository__RepositoryComponent283, providingEntity_ProvidedRole285, serviceEffectSpecifications__BasicComponent274, passiveResource_BasicComponent276, operationSignature__Parameter291, eventType__Parameter294, resourceSignature__Parameter296, repository__DataType297, components__Repository300, interfaces__Repository303, failureTypes__Repository305, dataTypes__Repository307, dataType__Parameter288, infrastructureSignature__Parameter289, parentInterfaces__Interface310, protocols__Interface312, requiredCharacterisations314, repository__Interface316, parameter319, interface_RequiredCharacterisation320, parameter__EventType326, eventGroup__EventType329, exceptions__Signature332, failureType333, parameters__InfrastructureSignature336, infrastructureInterface__InfrastructureSignature339, infrastructureSignatures__InfrastructureInterface341, eventTypes__EventGroup323, requiredInterface__InfrastructureRequiredRole344, requiringEntity_RequiredRole346, interface__OperationSignature349, parameters__OperationSignature351, returnType__OperationSignature354, signatures__OperationInterface356, requiredInterface__OperationRequiredRole359, eventGroup__SourceRole361, eventGroup__SinkRole363, providedInterface__OperationProvidedRole365, providedInterface__InfrastructureProvidedRole367, parentProvidesComponentTypes369, innerType_CollectionDataType370, parentType_CompositeDataType372, innerDeclaration_CompositeDataType373, datatype_InnerDeclaration375, compositeDataType_InnerDeclaration377, parameter__ResourceSignature380, resourceRepository_ResourceType388, resourceInterfaces__ResourceRepository390, schedulingPolicies__ResourceRepository393, availableResourceTypes_ResourceRepository395, resourceRepository__SchedulingPolicy397, networkInducedFailureType__CommunicationLinkResourceType400, resourceRepository__ResourceInterface402, resourceSignatures__ResourceInterface405, variableCharacterisation_VariableUsage408, resourceInterface__ResourceSignature383, hardwareInducedFailureType__ProcessingResourceType386, specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage422, assemblyContext__VariableUsage424, entryLevelSystemCall_InputParameterUsage427, entryLevelSystemCall_OutputParameterUsage429, namedReference__VariableUsage432, specification_VariableCharacterisation433, variableUsage_VariableCharacterisation436, userData_VariableUsage411, callAction__VariableUsage414, synchronisationPoint_VariableUsage416, callReturnAction__VariableUsage418, setVariableAction_VariableUsage420, processingResourceType__HardwareInducedFailureType439, internalFailureOccurrenceDescriptions__SoftwareInducedFailureType441, internalAction__InternalFailureOccurrenceDescription443, softwareInducedFailureType__InternalFailureOccurrenceDescription445, specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription449, failureType__ExternalFailureOccurrenceDescription451, passiveResource__ResourceTimeoutFailureType453, repository__FailureType456, resourceDemand_Action459, infrastructureCall__Action462, resourceCall__Action465, communicationLinkResourceType__NetworkInducedFailureType447, abstractLoopAction_ResourceDemandingBehaviour475, abstractBranchTransition_ResourceDemandingBehaviour477, steps_Behaviour479, bodyBehaviour_Loop482, branchAction_AbstractBranchTransition485, branchBehaviour_BranchTransition487, predecessor_AbstractAction468, successor_AbstractAction470, resourceDemandingBehaviour_AbstractAction473, branches_Branch490, inputVariableUsages__CallAction493, describedService__SEFF496, basicComponent_ServiceEffectSpecification497, passiveResource_ReleaseAction504, iterationCount_LoopAction506, asynchronousForkedBehaviours_ForkAction509, synchronisingBehaviours_ForkAction511, synchronisationPoint_ForkedBehaviour514, forkAction_ForkedBehaivour517, outputParameterUsage_SynchronisationPoint519, forkAction_SynchronisationPoint522, synchronousForkedBehaviours_SynchronisationPoint525, resourceDemandingInternalBehaviours500, resourceDemandingSEFF_ResourceDemandingInternalBehaviour502, calledService_ExternalService528, role_ExternalService530, returnVariableUsage__CallReturnAction533, passiveresource_AcquireAction536, parameter_CollectionIteratorAction538, localVariableUsages_SetVariableAction543, calledResourceDemandingInternalBehaviour546, eventType__EmitEventAction548, sourceRole__EmitEventAction550, internalFailureOccurrenceDescriptions__InternalAction553, branchCondition_GuardedBranchTransition540, signature__InfrastructureCall556, numberOfCalls__InfrastructureCall558, action__InfrastructureCall561, requiredRole__InfrastructureCall563, action__ResourceCall566, resourceRequiredRole__ResourceCall569, signature__ResourceCall571, numberOfCalls__ResourceCall574, specification_ParametericResourceDemand577, requiredResource_ParametricResourceDemand580, action_ParametricResourceDemand582, recoveryAction__RecoveryActionBehaviour586, primaryBehaviour__RecoveryAction588, recoveryActionBehaviours__RecoveryAction590, failureTypes_FailureHandlingEntity593, signature_SpecifiedQoSAnnation595, role_SpecifiedQoSAnnotation597, qosAnnotations_SpecifiedQoSAnnotation599, failureHandlingAlternatives__RecoveryActionBehaviour585, system_QoSAnnotations604, specifiedQoSAnnotations_QoSAnnotations605, signature_SpecifiedOutputParameterAbstraction607, role_SpecifiedOutputParameterAbstraction609, expectedExternalOutputs_SpecifiedOutputParameterAbstraction612, qosAnnotations_SpecifiedOutputParameterAbstraction615, specification_SpecifiedExecutionTime618, assemblyContext_ComponentSpecifiedExecutionTime621, specifiedOutputParameterAbstractions_QoSAnnotations601, externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation623, qosAnnotations_System625, resourceContainer_ResourceEnvironment630, connectedResourceContainers_LinkingResource632, communicationLinkResourceSpecifications_LinkingResource634, resourceEnvironment_LinkingResource637, activeResourceSpecifications_ResourceContainer639, resourceEnvironment_ResourceContainer642, nestedResourceContainers__ResourceContainer645, parentResourceContainer__ResourceContainer648, schedulingPolicy651, activeResourceType_ActiveResourceSpecification653, processingRate_ProcessingResourceSpecification656, linkingResources__ResourceEnvironment628, resourceContainer_ProcessingResourceSpecification659, linkingResource_CommunicationLinkResourceSpecification662, communicationLinkResourceType_CommunicationLinkResourceSpecification665, latency_CommunicationLinkResourceSpecification667, throughput_CommunicationLinkResourceSpecification670, resourceContainer_AllocationContext673, assemblyContext_AllocationContext675, eventChannel__AllocationContext679, targetResourceEnvironment_Allocation681, system_Allocation683, allocationContexts_Allocation686, completions_CompletionRepository688, allocation_AllocationContext678, requiredCommunicationLinkResource_ParametricResourceDemand689},
    generalizations={gen_pcm_av_core_av_PCMRandomVariable_RandomVariable, gen_pcm_av_entity_av_ResourceProvidedRole_Role, gen_pcm_av_entity_av_InterfaceProvidingRequiringEntity_entity_av_InterfaceProvidingEntity, gen_pcm_av_entity_av_InterfaceProvidingRequiringEntity_entity_av_InterfaceRequiringEntity, gen_pcm_av_entity_av_InterfaceProvidingEntity_Entity, gen_pcm_av_entity_av_InterfaceRequiringEntity_entity_av_Entity, gen_pcm_av_entity_av_InterfaceRequiringEntity_entity_av_ResourceInterfaceRequiringEntity, gen_pcm_av_entity_av_ResourceInterfaceRequiringEntity_Entity, gen_pcm_av_entity_av_ResourceRequiredRole_Role, gen_pcm_av_entity_av_ResourceInterfaceProvidingEntity_Entity, gen_pcm_av_entity_av_ResourceInterfaceProvidingRequiringEntity_entity_av_ResourceInterfaceRequiringEntity, gen_pcm_av_entity_av_ResourceInterfaceProvidingRequiringEntity_entity_av_ResourceInterfaceProvidingEntity, gen_pcm_av_entity_av_Entity_Identifier, gen_pcm_av_entity_av_Entity_entity_av_NamedElement, gen_pcm_av_composition_av_DelegationConnector_Connector, gen_pcm_av_composition_av_Connector_Entity, gen_pcm_av_composition_av_ComposedStructure_Entity, gen_pcm_av_entity_av_ComposedProvidingRequiringEntity_composition_av_ComposedStructure, gen_pcm_av_entity_av_ComposedProvidingRequiringEntity_entity_av_InterfaceProvidingRequiringEntity, gen_pcm_av_composition_av_EventChannel_Entity, gen_pcm_av_composition_av_EventChannelSourceConnector_Connector, gen_pcm_av_composition_av_EventChannelSinkConnector_Connector, gen_pcm_av_composition_av_ProvidedDelegationConnector_DelegationConnector, gen_pcm_av_composition_av_RequiredDelegationConnector_DelegationConnector, gen_pcm_av_composition_av_AssemblyConnector_Connector, gen_pcm_av_composition_av_AssemblyEventConnector_Connector, gen_pcm_av_composition_av_SourceDelegationConnector_DelegationConnector, gen_pcm_av_composition_av_AssemblyInfrastructureConnector_Connector, gen_pcm_av_composition_av_ProvidedInfrastructureDelegationConnector_DelegationConnector, gen_pcm_av_composition_av_RequiredInfrastructureDelegationConnector_DelegationConnector, gen_pcm_av_composition_av_RequiredResourceDelegationConnector_DelegationConnector, gen_pcm_av_composition_av_SinkDelegationConnector_DelegationConnector, gen_pcm_av_usagemodel_av_UsageScenario_Entity, gen_pcm_av_composition_av_AssemblyContext_Entity, gen_pcm_av_usagemodel_av_AbstractUserAction_Entity, gen_pcm_av_usagemodel_av_ScenarioBehaviour_Entity, gen_pcm_av_usagemodel_av_EntryLevelSystemCall_AbstractUserAction, gen_pcm_av_usagemodel_av_Branch_AbstractUserAction, gen_pcm_av_usagemodel_av_Loop_AbstractUserAction, gen_pcm_av_usagemodel_av_Start_AbstractUserAction, gen_pcm_av_usagemodel_av_OpenWorkload_Workload, gen_pcm_av_usagemodel_av_Delay_AbstractUserAction, gen_pcm_av_usagemodel_av_ClosedWorkload_Workload, gen_pcm_av_usagemodel_av_Stop_AbstractUserAction, gen_pcm_av_repository_av_PassiveResource_Entity, gen_pcm_av_repository_av_BasicComponent_ImplementationComponentType, gen_pcm_av_repository_av_RepositoryComponent_InterfaceProvidingRequiringEntity, gen_pcm_av_repository_av_ProvidedRole_Role, gen_pcm_av_repository_av_ImplementationComponentType_RepositoryComponent, gen_pcm_av_repository_av_Repository_Entity, gen_pcm_av_repository_av_Interface_Entity, gen_pcm_av_repository_av_EventGroup_Interface, gen_pcm_av_repository_av_Signature_Entity, gen_pcm_av_repository_av_InfrastructureSignature_Signature, gen_pcm_av_repository_av_InfrastructureInterface_Interface, gen_pcm_av_repository_av_EventType_Signature, gen_pcm_av_repository_av_InfrastructureRequiredRole_RequiredRole, gen_pcm_av_repository_av_RequiredRole_Role, gen_pcm_av_repository_av_OperationSignature_Signature, gen_pcm_av_repository_av_OperationRequiredRole_RequiredRole, gen_pcm_av_repository_av_SourceRole_RequiredRole, gen_pcm_av_repository_av_SinkRole_ProvidedRole, gen_pcm_av_repository_av_OperationProvidedRole_ProvidedRole, gen_pcm_av_repository_av_InfrastructureProvidedRole_ProvidedRole, gen_pcm_av_repository_av_CompleteComponentType_RepositoryComponent, gen_pcm_av_repository_av_OperationInterface_Interface, gen_pcm_av_repository_av_ProvidesComponentType_RepositoryComponent, gen_pcm_av_repository_av_CompositeComponent_entity_av_ComposedProvidingRequiringEntity, gen_pcm_av_repository_av_CompositeComponent_repository_av_ImplementationComponentType, gen_pcm_av_repository_av_PrimitiveDataType_DataType, gen_pcm_av_repository_av_CollectionDataType_entity_av_Entity, gen_pcm_av_repository_av_CollectionDataType_repository_av_DataType, gen_pcm_av_repository_av_CompositeDataType_entity_av_Entity, gen_pcm_av_repository_av_CompositeDataType_repository_av_DataType, gen_pcm_av_repository_av_InnerDeclaration_NamedElement, gen_pcm_av_repository_av_Role_Entity, gen_pcm_av_resourcetype_av_ResourceSignature_Entity, gen_pcm_av_resourcetype_av_SchedulingPolicy_Entity, gen_pcm_av_resourcetype_av_CommunicationLinkResourceType_ResourceType, gen_pcm_av_resourcetype_av_ResourceInterface_Entity, gen_pcm_av_resourcetype_av_ProcessingResourceType_ResourceType, gen_pcm_av_resourcetype_av_ResourceType_entity_av_Entity, gen_pcm_av_resourcetype_av_ResourceType_UnitCarryingElement, gen_pcm_av_resourcetype_av_ResourceType_entity_av_ResourceInterfaceProvidingEntity, gen_pcm_av_parameter_av_CharacterisedVariable_Variable, gen_pcm_av_reliability_av_HardwareInducedFailureType_FailureType, gen_pcm_av_reliability_av_SoftwareInducedFailureType_FailureType, gen_pcm_av_reliability_av_InternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_av_reliability_av_NetworkInducedFailureType_FailureType, gen_pcm_av_reliability_av_ResourceTimeoutFailureType_SoftwareInducedFailureType, gen_pcm_av_reliability_av_FailureType_Entity, gen_pcm_av_seff_av_StopAction_AbstractInternalControlFlowAction, gen_pcm_av_seff_av_AbstractInternalControlFlowAction_AbstractAction, gen_pcm_av_seff_av_AbstractAction_Entity, gen_pcm_av_reliability_av_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_av_seff_av_AbstractLoopAction_AbstractInternalControlFlowAction, gen_pcm_av_seff_av_AbstractBranchTransition_Entity, gen_pcm_av_seff_av_ResourceDemandingBehaviour_Identifier, gen_pcm_av_seff_av_StartAction_AbstractInternalControlFlowAction, gen_pcm_av_seff_av_ResourceDemandingSEFF_Identifier, gen_pcm_av_seff_av_ResourceDemandingSEFF_seff_av_ServiceEffectSpecification, gen_pcm_av_seff_av_ResourceDemandingSEFF_seff_av_ResourceDemandingBehaviour, gen_pcm_av_seff_av_BranchAction_AbstractInternalControlFlowAction, gen_pcm_av_seff_av_ReleaseAction_AbstractInternalControlFlowAction, gen_pcm_av_seff_av_LoopAction_AbstractLoopAction, gen_pcm_av_seff_av_ForkAction_AbstractInternalControlFlowAction, gen_pcm_av_seff_av_ForkedBehaviour_ResourceDemandingBehaviour, gen_pcm_av_seff_av_ExternalCallAction_seff_av_AbstractAction, gen_pcm_av_seff_av_ExternalCallAction_seff_av_CallReturnAction, gen_pcm_av_seff_av_ExternalCallAction_seff_reliability_av_FailureHandlingEntity, gen_pcm_av_seff_av_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour, gen_pcm_av_seff_av_CallReturnAction_CallAction, gen_pcm_av_seff_av_ProbabilisticBranchTransition_AbstractBranchTransition, gen_pcm_av_seff_av_AcquireAction_AbstractInternalControlFlowAction, gen_pcm_av_seff_av_CollectionIteratorAction_AbstractLoopAction, gen_pcm_av_seff_av_GuardedBranchTransition_AbstractBranchTransition, gen_pcm_av_seff_av_SetVariableAction_AbstractInternalControlFlowAction, gen_pcm_av_seff_av_InternalCallAction_seff_av_CallAction, gen_pcm_av_seff_av_InternalCallAction_seff_av_AbstractInternalControlFlowAction, gen_pcm_av_seff_av_EmitEventAction_seff_av_AbstractAction, gen_pcm_av_seff_av_EmitEventAction_seff_av_CallAction, gen_pcm_av_seff_av_InternalAction_AbstractInternalControlFlowAction, gen_pcm_av_seff_performance_av_InfrastructureCall_CallAction, gen_pcm_av_seff_performance_av_ResourceCall_CallAction, gen_pcm_av_seff_reliability_av_RecoveryActionBehaviour_seff_reliability_av_FailureHandlingEntity, gen_pcm_av_seff_reliability_av_RecoveryActionBehaviour_seff_av_ResourceDemandingBehaviour, gen_pcm_av_seff_reliability_av_RecoveryAction_AbstractInternalControlFlowAction, gen_pcm_av_seff_reliability_av_FailureHandlingEntity_Entity, gen_pcm_av_qosannotations_av_QoSAnnotations_Entity, gen_pcm_av_qos_performance_av_SystemSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_av_qos_performance_av_SpecifiedExecutionTime_SpecifiedQoSAnnotation, gen_pcm_av_qos_performance_av_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_av_system_av_System_entity_av_Entity, gen_pcm_av_system_av_System_entity_av_ComposedProvidingRequiringEntity, gen_pcm_av_resourceenvironment_av_ResourceEnvironment_NamedElement, gen_pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation, gen_pcm_av_resourceenvironment_av_LinkingResource_Entity, gen_pcm_av_resourceenvironment_av_ResourceContainer_Entity, gen_pcm_av_resourceenvironment_av_ProcessingResourceSpecification_Identifier, gen_pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification_Identifier, gen_pcm_av_allocation_av_AllocationContext_Entity, gen_pcm_av_allocation_av_Allocation_Entity, gen_pcm_av_subsystem_av_SubSystem_entity_av_ComposedProvidingRequiringEntity, gen_pcm_av_subsystem_av_SubSystem_repository_av_RepositoryComponent, gen_pcm_av_completions_av_Completion_entity_av_ComposedProvidingRequiringEntity, gen_pcm_av_completions_av_Completion_repository_av_ImplementationComponentType, gen_pcm_av_completions_av_DelegatingExternalCallAction_ExternalCallAction, gen_pcm_av_completions_av_NetworkDemandParametricResourceDemand_ParametricResourceDemand},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)