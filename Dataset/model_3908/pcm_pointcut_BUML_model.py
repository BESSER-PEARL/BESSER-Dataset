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
            EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="BOOL"),
			EnumerationLiteral(name="DOUBLE"),
			EnumerationLiteral(name="CHAR"),
			EnumerationLiteral(name="BYTE"),
			EnumerationLiteral(name="LONG")
    }
)

VariableCharacterisationType: Enumeration = Enumeration(
    name="VariableCharacterisationType",
    literals={
            EnumerationLiteral(name="BYTESIZE"),
			EnumerationLiteral(name="TYPE"),
			EnumerationLiteral(name="STRUCTURE"),
			EnumerationLiteral(name="NUMBER_OF_ELEMENTS"),
			EnumerationLiteral(name="VALUE")
    }
)

# Classes
pcm_pc_DummyClass = Class(name="pcm::pc::DummyClass")
pcm_pc_Pointcut = Class(name="pcm::pc::Pointcut")
pcm_pc_EObject = Class(name="pcm::pc::EObject")
pcm_pc_core_pc_PCMRandomVariable = Class(name="pcm::pc::core::pc::PCMRandomVariable")
RandomVariable = Class(name="RandomVariable")
composition_pc_AssemblyEventConnector = Class(name="composition::pc::AssemblyEventConnector")
ClosedWorkload = Class(name="ClosedWorkload")
PassiveResource = Class(name="PassiveResource")
VariableCharacterisation = Class(name="VariableCharacterisation")
seff_performance_pc_InfrastructureCall = Class(name="seff::performance::pc::InfrastructureCall")
seff_performance_pc_ResourceCall = Class(name="seff::performance::pc::ResourceCall")
seff_performance_pc_ParametricResourceDemand = Class(name="seff::performance::pc::ParametricResourceDemand")
LoopAction = Class(name="LoopAction")
GuardedBranchTransition = Class(name="GuardedBranchTransition")
qos_performance_pc_SpecifiedExecutionTime = Class(name="qos::performance::pc::SpecifiedExecutionTime")
composition_pc_EventChannelSinkConnector = Class(name="composition::pc::EventChannelSinkConnector")
pcm_pc_entity_pc_ResourceInterfaceRequiringEntity = Class(name="pcm::pc::entity::pc::ResourceInterfaceRequiringEntity")
entity_pc_ResourceRequiredRole = Class(name="entity::pc::ResourceRequiredRole")
pcm_pc_entity_pc_ResourceRequiredRole = Class(name="pcm::pc::entity::pc::ResourceRequiredRole")
Loop = Class(name="Loop")
OpenWorkload = Class(name="OpenWorkload")
Delay = Class(name="Delay")
CommunicationLinkResourceSpecification = Class(name="CommunicationLinkResourceSpecification")
ProcessingResourceSpecification = Class(name="ProcessingResourceSpecification")
pcm_pc_entity_pc_ResourceProvidedRole = Class(name="pcm::pc::entity::pc::ResourceProvidedRole")
Role = Class(name="Role")
entity_pc_ResourceInterfaceProvidingEntity = Class(name="entity::pc::ResourceInterfaceProvidingEntity")
ResourceInterface = Class(name="ResourceInterface")
pcm_pc_entity_pc_InterfaceProvidingRequiringEntity = Class(name="pcm::pc::entity::pc::InterfaceProvidingRequiringEntity")
entity_pc_InterfaceProvidingEntity = Class(name="entity::pc::InterfaceProvidingEntity")
entity_pc_InterfaceRequiringEntity = Class(name="entity::pc::InterfaceRequiringEntity")
pcm_pc_entity_pc_InterfaceProvidingEntity = Class(name="pcm::pc::entity::pc::InterfaceProvidingEntity")
Entity = Class(name="Entity")
ProvidedRole = Class(name="ProvidedRole")
pcm_pc_entity_pc_InterfaceRequiringEntity = Class(name="pcm::pc::entity::pc::InterfaceRequiringEntity")
entity_pc_Entity = Class(name="entity::pc::Entity")
entity_pc_ResourceInterfaceRequiringEntity = Class(name="entity::pc::ResourceInterfaceRequiringEntity")
RequiredRole = Class(name="RequiredRole")
pcm_pc_entity_pc_ResourceInterfaceProvidingEntity = Class(name="pcm::pc::entity::pc::ResourceInterfaceProvidingEntity")
entity_pc_ResourceProvidedRole = Class(name="entity::pc::ResourceProvidedRole")
pcm_pc_entity_pc_ComposedProvidingRequiringEntity = Class(name="pcm::pc::entity::pc::ComposedProvidingRequiringEntity")
composition_pc_ComposedStructure = Class(name="composition::pc::ComposedStructure")
entity_pc_InterfaceProvidingRequiringEntity = Class(name="entity::pc::InterfaceProvidingRequiringEntity")
pcm_pc_entity_pc_NamedElement = Class(name="pcm::pc::entity::pc::NamedElement")
pcm_pc_entity_pc_ResourceInterfaceProvidingRequiringEntity = Class(name="pcm::pc::entity::pc::ResourceInterfaceProvidingRequiringEntity")
pcm_pc_entity_pc_Entity = Class(name="pcm::pc::entity::pc::Entity")
Identifier = Class(name="Identifier")
entity_pc_NamedElement = Class(name="entity::pc::NamedElement")
pcm_pc_composition_pc_DelegationConnector = Class(name="pcm::pc::composition::pc::DelegationConnector")
Connector = Class(name="Connector")
pcm_pc_composition_pc_Connector = Class(name="pcm::pc::composition::pc::Connector")
pcm_pc_composition_pc_ComposedStructure = Class(name="pcm::pc::composition::pc::ComposedStructure")
pcm_pc_composition_pc_ProvidedDelegationConnector = Class(name="pcm::pc::composition::pc::ProvidedDelegationConnector")
DelegationConnector = Class(name="DelegationConnector")
composition_pc_AssemblyContext = Class(name="composition::pc::AssemblyContext")
composition_pc_ResourceRequiredDelegationConnector = Class(name="composition::pc::ResourceRequiredDelegationConnector")
composition_pc_EventChannel = Class(name="composition::pc::EventChannel")
composition_pc_Connector = Class(name="composition::pc::Connector")
pcm_pc_composition_pc_ResourceRequiredDelegationConnector = Class(name="pcm::pc::composition::pc::ResourceRequiredDelegationConnector")
pcm_pc_composition_pc_EventChannel = Class(name="pcm::pc::composition::pc::EventChannel")
EventGroup = Class(name="EventGroup")
composition_pc_EventChannelSourceConnector = Class(name="composition::pc::EventChannelSourceConnector")
pcm_pc_composition_pc_EventChannelSourceConnector = Class(name="pcm::pc::composition::pc::EventChannelSourceConnector")
SourceRole = Class(name="SourceRole")
pcm_pc_composition_pc_EventChannelSinkConnector = Class(name="pcm::pc::composition::pc::EventChannelSinkConnector")
SinkRole = Class(name="SinkRole")
PCMRandomVariable = Class(name="PCMRandomVariable")
OperationRequiredRole = Class(name="OperationRequiredRole")
pcm_pc_composition_pc_AssemblyConnector = Class(name="pcm::pc::composition::pc::AssemblyConnector")
OperationProvidedRole = Class(name="OperationProvidedRole")
pcm_pc_composition_pc_RequiredDelegationConnector = Class(name="pcm::pc::composition::pc::RequiredDelegationConnector")
pcm_pc_composition_pc_SourceDelegationConnector = Class(name="pcm::pc::composition::pc::SourceDelegationConnector")
pcm_pc_composition_pc_AssemblyEventConnector = Class(name="pcm::pc::composition::pc::AssemblyEventConnector")
pcm_pc_composition_pc_RequiredResourceDelegationConnector = Class(name="pcm::pc::composition::pc::RequiredResourceDelegationConnector")
pcm_pc_composition_pc_SinkDelegationConnector = Class(name="pcm::pc::composition::pc::SinkDelegationConnector")
pcm_pc_composition_pc_AssemblyContext = Class(name="pcm::pc::composition::pc::AssemblyContext")
RepositoryComponent = Class(name="RepositoryComponent")
VariableUsage = Class(name="VariableUsage")
pcm_pc_composition_pc_AssemblyInfrastructureConnector = Class(name="pcm::pc::composition::pc::AssemblyInfrastructureConnector")
InfrastructureProvidedRole = Class(name="InfrastructureProvidedRole")
InfrastructureRequiredRole = Class(name="InfrastructureRequiredRole")
pcm_pc_usagemodel_pc_Workload = Class(name="pcm::pc::usagemodel::pc::Workload")
pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector = Class(name="pcm::pc::composition::pc::ProvidedInfrastructureDelegationConnector")
pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector = Class(name="pcm::pc::composition::pc::RequiredInfrastructureDelegationConnector")
pcm_pc_usagemodel_pc_UsageModel = Class(name="pcm::pc::usagemodel::pc::UsageModel")
UserData = Class(name="UserData")
pcm_pc_usagemodel_pc_EntryLevelSystemCall = Class(name="pcm::pc::usagemodel::pc::EntryLevelSystemCall")
AbstractUserAction = Class(name="AbstractUserAction")
OperationSignature = Class(name="OperationSignature")
UsageScenario = Class(name="UsageScenario")
pcm_pc_usagemodel_pc_UsageScenario = Class(name="pcm::pc::usagemodel::pc::UsageScenario")
UsageModel = Class(name="UsageModel")
ScenarioBehaviour = Class(name="ScenarioBehaviour")
Workload = Class(name="Workload")
pcm_pc_usagemodel_pc_UserData = Class(name="pcm::pc::usagemodel::pc::UserData")
BranchTransition = Class(name="BranchTransition")
pcm_pc_usagemodel_pc_BranchTransition = Class(name="pcm::pc::usagemodel::pc::BranchTransition")
Branch = Class(name="Branch")
pcm_pc_usagemodel_pc_Branch = Class(name="pcm::pc::usagemodel::pc::Branch")
pcm_pc_usagemodel_pc_AbstractUserAction = Class(name="pcm::pc::usagemodel::pc::AbstractUserAction")
pcm_pc_usagemodel_pc_ScenarioBehaviour = Class(name="pcm::pc::usagemodel::pc::ScenarioBehaviour")
pcm_pc_usagemodel_pc_Loop = Class(name="pcm::pc::usagemodel::pc::Loop")
pcm_pc_usagemodel_pc_Stop = Class(name="pcm::pc::usagemodel::pc::Stop")
pcm_pc_usagemodel_pc_Start = Class(name="pcm::pc::usagemodel::pc::Start")
pcm_pc_usagemodel_pc_OpenWorkload = Class(name="pcm::pc::usagemodel::pc::OpenWorkload")
pcm_pc_repository_pc_PassiveResource = Class(name="pcm::pc::repository::pc::PassiveResource")
BasicComponent = Class(name="BasicComponent")
ResourceTimeoutFailureType = Class(name="ResourceTimeoutFailureType")
pcm_pc_repository_pc_BasicComponent = Class(name="pcm::pc::repository::pc::BasicComponent")
ImplementationComponentType = Class(name="ImplementationComponentType")
pcm_pc_usagemodel_pc_Delay = Class(name="pcm::pc::usagemodel::pc::Delay")
pcm_pc_usagemodel_pc_ClosedWorkload = Class(name="pcm::pc::usagemodel::pc::ClosedWorkload")
pcm_pc_repository_pc_ImplementationComponentType = Class(name="pcm::pc::repository::pc::ImplementationComponentType")
CompleteComponentType = Class(name="CompleteComponentType")
ServiceEffectSpecification = Class(name="ServiceEffectSpecification")
EventType = Class(name="EventType")
ResourceSignature = Class(name="ResourceSignature")
pcm_pc_repository_pc_DataType = Class(name="pcm::pc::repository::pc::DataType")
pcm_pc_repository_pc_Repository = Class(name="pcm::pc::repository::pc::Repository")
Interface = Class(name="Interface")
FailureType = Class(name="FailureType")
pcm_pc_repository_pc_RepositoryComponent = Class(name="pcm::pc::repository::pc::RepositoryComponent")
InterfaceProvidingRequiringEntity = Class(name="InterfaceProvidingRequiringEntity")
Repository = Class(name="Repository")
pcm_pc_repository_pc_ProvidedRole = Class(name="pcm::pc::repository::pc::ProvidedRole")
pcm_pc_repository_pc_Parameter = Class(name="pcm::pc::repository::pc::Parameter")
DataType = Class(name="DataType")
InfrastructureSignature = Class(name="InfrastructureSignature")
RequiredCharacterisation = Class(name="RequiredCharacterisation")
pcm_pc_repository_pc_RequiredCharacterisation = Class(name="pcm::pc::repository::pc::RequiredCharacterisation")
Parameter_ = Class(name="Parameter")
pcm_pc_repository_pc_EventGroup = Class(name="pcm::pc::repository::pc::EventGroup")
pcm_pc_repository_pc_EventType = Class(name="pcm::pc::repository::pc::EventType")
Signature = Class(name="Signature")
pcm_pc_repository_pc_Signature = Class(name="pcm::pc::repository::pc::Signature")
pcm_pc_repository_pc_Interface = Class(name="pcm::pc::repository::pc::Interface")
Protocol = Class(name="Protocol")
pcm_pc_repository_pc_InfrastructureRequiredRole = Class(name="pcm::pc::repository::pc::InfrastructureRequiredRole")
pcm_pc_repository_pc_RequiredRole = Class(name="pcm::pc::repository::pc::RequiredRole")
pcm_pc_repository_pc_OperationSignature = Class(name="pcm::pc::repository::pc::OperationSignature")
OperationInterface = Class(name="OperationInterface")
ExceptionType = Class(name="ExceptionType")
pcm_pc_repository_pc_ExceptionType = Class(name="pcm::pc::repository::pc::ExceptionType")
pcm_pc_repository_pc_InfrastructureSignature = Class(name="pcm::pc::repository::pc::InfrastructureSignature")
InfrastructureInterface = Class(name="InfrastructureInterface")
pcm_pc_repository_pc_InfrastructureInterface = Class(name="pcm::pc::repository::pc::InfrastructureInterface")
pcm_pc_repository_pc_OperationRequiredRole = Class(name="pcm::pc::repository::pc::OperationRequiredRole")
pcm_pc_repository_pc_SourceRole = Class(name="pcm::pc::repository::pc::SourceRole")
pcm_pc_repository_pc_SinkRole = Class(name="pcm::pc::repository::pc::SinkRole")
pcm_pc_repository_pc_OperationProvidedRole = Class(name="pcm::pc::repository::pc::OperationProvidedRole")
pcm_pc_repository_pc_InfrastructureProvidedRole = Class(name="pcm::pc::repository::pc::InfrastructureProvidedRole")
pcm_pc_repository_pc_OperationInterface = Class(name="pcm::pc::repository::pc::OperationInterface")
ProvidesComponentType = Class(name="ProvidesComponentType")
pcm_pc_repository_pc_ProvidesComponentType = Class(name="pcm::pc::repository::pc::ProvidesComponentType")
pcm_pc_repository_pc_CompositeComponent = Class(name="pcm::pc::repository::pc::CompositeComponent")
entity_pc_ComposedProvidingRequiringEntity = Class(name="entity::pc::ComposedProvidingRequiringEntity")
repository_pc_ImplementationComponentType = Class(name="repository::pc::ImplementationComponentType")
pcm_pc_repository_pc_CompleteComponentType = Class(name="pcm::pc::repository::pc::CompleteComponentType")
pcm_pc_repository_pc_CollectionDataType = Class(name="pcm::pc::repository::pc::CollectionDataType")
repository_pc_DataType = Class(name="repository::pc::DataType")
pcm_pc_repository_pc_CompositeDataType = Class(name="pcm::pc::repository::pc::CompositeDataType")
CompositeDataType = Class(name="CompositeDataType")
InnerDeclaration = Class(name="InnerDeclaration")
pcm_pc_repository_pc_InnerDeclaration = Class(name="pcm::pc::repository::pc::InnerDeclaration")
NamedElement = Class(name="NamedElement")
pcm_pc_repository_pc_PrimitiveDataType = Class(name="pcm::pc::repository::pc::PrimitiveDataType")
pcm_pc_resourcetype_pc_ProcessingResourceType = Class(name="pcm::pc::resourcetype::pc::ProcessingResourceType")
ResourceType = Class(name="ResourceType")
HardwareInducedFailureType = Class(name="HardwareInducedFailureType")
pcm_pc_resourcetype_pc_ResourceType = Class(name="pcm::pc::resourcetype::pc::ResourceType")
UnitCarryingElement = Class(name="UnitCarryingElement")
ResourceRepository = Class(name="ResourceRepository")
pcm_pc_resourcetype_pc_ResourceRepository = Class(name="pcm::pc::resourcetype::pc::ResourceRepository")
SchedulingPolicy = Class(name="SchedulingPolicy")
pcm_pc_resourcetype_pc_SchedulingPolicy = Class(name="pcm::pc::resourcetype::pc::SchedulingPolicy")
pcm_pc_resourcetype_pc_CommunicationLinkResourceType = Class(name="pcm::pc::resourcetype::pc::CommunicationLinkResourceType")
NetworkInducedFailureType = Class(name="NetworkInducedFailureType")
pcm_pc_resourcetype_pc_ResourceInterface = Class(name="pcm::pc::resourcetype::pc::ResourceInterface")
pcm_pc_repository_pc_Role = Class(name="pcm::pc::repository::pc::Role")
pcm_pc_resourcetype_pc_ResourceSignature = Class(name="pcm::pc::resourcetype::pc::ResourceSignature")
CallAction = Class(name="CallAction")
SynchronisationPoint = Class(name="SynchronisationPoint")
CallReturnAction = Class(name="CallReturnAction")
SetVariableAction = Class(name="SetVariableAction")
SpecifiedOutputParameterAbstraction = Class(name="SpecifiedOutputParameterAbstraction")
EntryLevelSystemCall = Class(name="EntryLevelSystemCall")
parameter_pc_pcm_pc_AbstractNamedReference = Class(name="parameter::pc::pcm::pc::AbstractNamedReference")
pcm_pc_parameter_pc_VariableCharacterisation = Class(name="pcm::pc::parameter::pc::VariableCharacterisation")
pcm_pc_protocol_pc_Protocol = Class(name="pcm::pc::protocol::pc::Protocol")
pcm_pc_parameter_pc_VariableUsage = Class(name="pcm::pc::parameter::pc::VariableUsage")
pcm_pc_reliability_pc_FailureOccurrenceDescription = Class(name="pcm::pc::reliability::pc::FailureOccurrenceDescription")
pcm_pc_reliability_pc_HardwareInducedFailureType = Class(name="pcm::pc::reliability::pc::HardwareInducedFailureType")
ProcessingResourceType = Class(name="ProcessingResourceType")
pcm_pc_reliability_pc_SoftwareInducedFailureType = Class(name="pcm::pc::reliability::pc::SoftwareInducedFailureType")
InternalFailureOccurrenceDescription = Class(name="InternalFailureOccurrenceDescription")
pcm_pc_parameter_pc_CharacterisedVariable = Class(name="pcm::pc::parameter::pc::CharacterisedVariable")
Variable = Class(name="Variable")
InternalAction = Class(name="InternalAction")
pcm_pc_reliability_pc_InternalFailureOccurrenceDescription = Class(name="pcm::pc::reliability::pc::InternalFailureOccurrenceDescription")
FailureOccurrenceDescription = Class(name="FailureOccurrenceDescription")
qos_reliability_pc_SpecifiedReliabilityAnnotation = Class(name="qos::reliability::pc::SpecifiedReliabilityAnnotation")
pcm_pc_reliability_pc_ResourceTimeoutFailureType = Class(name="pcm::pc::reliability::pc::ResourceTimeoutFailureType")
pcm_pc_reliability_pc_FailureType = Class(name="pcm::pc::reliability::pc::FailureType")
pcm_pc_seff_pc_StopAction = Class(name="pcm::pc::seff::pc::StopAction")
AbstractInternalControlFlowAction = Class(name="AbstractInternalControlFlowAction")
SoftwareInducedFailureType = Class(name="SoftwareInducedFailureType")
pcm_pc_reliability_pc_NetworkInducedFailureType = Class(name="pcm::pc::reliability::pc::NetworkInducedFailureType")
CommunicationLinkResourceType = Class(name="CommunicationLinkResourceType")
pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription = Class(name="pcm::pc::reliability::pc::ExternalFailureOccurrenceDescription")
AbstractLoopAction = Class(name="AbstractLoopAction")
pcm_pc_seff_pc_AbstractInternalControlFlowAction = Class(name="pcm::pc::seff::pc::AbstractInternalControlFlowAction")
AbstractAction = Class(name="AbstractAction")
AbstractBranchTransition = Class(name="AbstractBranchTransition")
pcm_pc_seff_pc_AbstractLoopAction = Class(name="pcm::pc::seff::pc::AbstractLoopAction")
pcm_pc_seff_pc_AbstractBranchTransition = Class(name="pcm::pc::seff::pc::AbstractBranchTransition")
BranchAction = Class(name="BranchAction")
pcm_pc_seff_pc_AbstractAction = Class(name="pcm::pc::seff::pc::AbstractAction")
ResourceDemandingBehaviour = Class(name="ResourceDemandingBehaviour")
pcm_pc_seff_pc_ResourceDemandingBehaviour = Class(name="pcm::pc::seff::pc::ResourceDemandingBehaviour")
pcm_pc_seff_pc_CallAction = Class(name="pcm::pc::seff::pc::CallAction")
pcm_pc_seff_pc_StartAction = Class(name="pcm::pc::seff::pc::StartAction")
pcm_pc_seff_pc_ServiceEffectSpecification = Class(name="pcm::pc::seff::pc::ServiceEffectSpecification")
pcm_pc_seff_pc_ResourceDemandingSEFF = Class(name="pcm::pc::seff::pc::ResourceDemandingSEFF")
seff_pc_ServiceEffectSpecification = Class(name="seff::pc::ServiceEffectSpecification")
seff_pc_ResourceDemandingBehaviour = Class(name="seff::pc::ResourceDemandingBehaviour")
pcm_pc_seff_pc_BranchAction = Class(name="pcm::pc::seff::pc::BranchAction")
ResourceDemandingSEFF = Class(name="ResourceDemandingSEFF")
pcm_pc_seff_pc_ReleaseAction = Class(name="pcm::pc::seff::pc::ReleaseAction")
pcm_pc_seff_pc_LoopAction = Class(name="pcm::pc::seff::pc::LoopAction")
pcm_pc_seff_pc_ForkAction = Class(name="pcm::pc::seff::pc::ForkAction")
ForkedBehaviour = Class(name="ForkedBehaviour")
ResourceDemandingInternalBehaviour = Class(name="ResourceDemandingInternalBehaviour")
pcm_pc_seff_pc_ForkedBehaviour = Class(name="pcm::pc::seff::pc::ForkedBehaviour")
pcm_pc_seff_pc_ResourceDemandingInternalBehaviour = Class(name="pcm::pc::seff::pc::ResourceDemandingInternalBehaviour")
ForkAction = Class(name="ForkAction")
pcm_pc_seff_pc_SynchronisationPoint = Class(name="pcm::pc::seff::pc::SynchronisationPoint")
pcm_pc_seff_pc_ExternalCallAction = Class(name="pcm::pc::seff::pc::ExternalCallAction")
seff_pc_AbstractAction = Class(name="seff::pc::AbstractAction")
seff_pc_CallReturnAction = Class(name="seff::pc::CallReturnAction")
seff_reliability_pc_FailureHandlingEntity = Class(name="seff::reliability::pc::FailureHandlingEntity")
pcm_pc_seff_pc_CallReturnAction = Class(name="pcm::pc::seff::pc::CallReturnAction")
pcm_pc_seff_pc_ProbabilisticBranchTransition = Class(name="pcm::pc::seff::pc::ProbabilisticBranchTransition")
pcm_pc_seff_pc_AcquireAction = Class(name="pcm::pc::seff::pc::AcquireAction")
pcm_pc_seff_pc_CollectionIteratorAction = Class(name="pcm::pc::seff::pc::CollectionIteratorAction")
pcm_pc_seff_pc_SetVariableAction = Class(name="pcm::pc::seff::pc::SetVariableAction")
pcm_pc_seff_pc_InternalCallAction = Class(name="pcm::pc::seff::pc::InternalCallAction")
seff_pc_CallAction = Class(name="seff::pc::CallAction")
seff_pc_AbstractInternalControlFlowAction = Class(name="seff::pc::AbstractInternalControlFlowAction")
pcm_pc_seff_pc_EmitEventAction = Class(name="pcm::pc::seff::pc::EmitEventAction")
pcm_pc_seff_pc_GuardedBranchTransition = Class(name="pcm::pc::seff::pc::GuardedBranchTransition")
pcm_pc_seff_pc_InternalAction = Class(name="pcm::pc::seff::pc::InternalAction")
pcm_pc_seff_performance_pc_ResourceCall = Class(name="pcm::pc::seff::performance::pc::ResourceCall")
pcm_pc_seff_performance_pc_InfrastructureCall = Class(name="pcm::pc::seff::performance::pc::InfrastructureCall")
pcm_pc_seff_performance_pc_ParametricResourceDemand = Class(name="pcm::pc::seff::performance::pc::ParametricResourceDemand")
seff_reliability_pc_RecoveryActionBehaviour = Class(name="seff::reliability::pc::RecoveryActionBehaviour")
pcm_pc_seff_reliability_pc_RecoveryActionBehaviour = Class(name="pcm::pc::seff::reliability::pc::RecoveryActionBehaviour")
pcm_pc_qosannotations_pc_SpecifiedQoSAnnotation = Class(name="pcm::pc::qosannotations::pc::SpecifiedQoSAnnotation")
QoSAnnotations = Class(name="QoSAnnotations")
seff_reliability_pc_RecoveryAction = Class(name="seff::reliability::pc::RecoveryAction")
pcm_pc_seff_reliability_pc_RecoveryAction = Class(name="pcm::pc::seff::reliability::pc::RecoveryAction")
pcm_pc_seff_reliability_pc_FailureHandlingEntity = Class(name="pcm::pc::seff::reliability::pc::FailureHandlingEntity")
pcm_pc_qos_performance_pc_SystemSpecifiedExecutionTime = Class(name="pcm::pc::qos::performance::pc::SystemSpecifiedExecutionTime")
SpecifiedExecutionTime = Class(name="SpecifiedExecutionTime")
pcm_pc_qos_performance_pc_SpecifiedExecutionTime = Class(name="pcm::pc::qos::performance::pc::SpecifiedExecutionTime")
pcm_pc_qosannotations_pc_QoSAnnotations = Class(name="pcm::pc::qosannotations::pc::QoSAnnotations")
System = Class(name="System")
SpecifiedQoSAnnotation = Class(name="SpecifiedQoSAnnotation")
pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction = Class(name="pcm::pc::qosannotations::pc::SpecifiedOutputParameterAbstraction")
ExternalFailureOccurrenceDescription = Class(name="ExternalFailureOccurrenceDescription")
pcm_pc_qos_performance_pc_ComponentSpecifiedExecutionTime = Class(name="pcm::pc::qos::performance::pc::ComponentSpecifiedExecutionTime")
pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation = Class(name="pcm::pc::qos::reliability::pc::SpecifiedReliabilityAnnotation")
pcm_pc_resourceenvironment_pc_ResourceEnvironment = Class(name="pcm::pc::resourceenvironment::pc::ResourceEnvironment")
LinkingResource = Class(name="LinkingResource")
ResourceContainer = Class(name="ResourceContainer")
pcm_pc_resourceenvironment_pc_LinkingResource = Class(name="pcm::pc::resourceenvironment::pc::LinkingResource")
ResourceEnvironment = Class(name="ResourceEnvironment")
pcm_pc_resourceenvironment_pc_ResourceContainer = Class(name="pcm::pc::resourceenvironment::pc::ResourceContainer")
pcm_pc_system_pc_System = Class(name="pcm::pc::system::pc::System")
pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification = Class(name="pcm::pc::resourceenvironment::pc::CommunicationLinkResourceSpecification")
pcm_pc_allocation_pc_AllocationContext = Class(name="pcm::pc::allocation::pc::AllocationContext")
pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification = Class(name="pcm::pc::resourceenvironment::pc::ProcessingResourceSpecification")
pcm_pc_allocation_pc_Allocation = Class(name="pcm::pc::allocation::pc::Allocation")
AllocationContext = Class(name="AllocationContext")
pcm_pc_subsystem_pc_SubSystem = Class(name="pcm::pc::subsystem::pc::SubSystem")
repository_pc_RepositoryComponent = Class(name="repository::pc::RepositoryComponent")
pcm_pc_completions_pc_Completion = Class(name="pcm::pc::completions::pc::Completion")
Allocation = Class(name="Allocation")
pcm_pc_completions_pc_CompletionRepository = Class(name="pcm::pc::completions::pc::CompletionRepository")
Completion = Class(name="Completion")
pcm_pc_completions_pc_DelegatingExternalCallAction = Class(name="pcm::pc::completions::pc::DelegatingExternalCallAction")
ExternalCallAction = Class(name="ExternalCallAction")
pcm_pc_completions_pc_NetworkDemandParametricResourceDemand = Class(name="pcm::pc::completions::pc::NetworkDemandParametricResourceDemand")
ParametricResourceDemand = Class(name="ParametricResourceDemand")

# pcm_pc_DummyClass class attributes and methods

# pcm_pc_Pointcut class attributes and methods

# pcm_pc_EObject class attributes and methods

# pcm_pc_core_pc_PCMRandomVariable class attributes and methods
pcm_pc_core_pc_PCMRandomVariable_m_SpecificationMustNotBeNULL: Method = Method(name="SpecificationMustNotBeNULL", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_core_pc_PCMRandomVariable.methods={pcm_pc_core_pc_PCMRandomVariable_m_SpecificationMustNotBeNULL}

# RandomVariable class attributes and methods

# composition_pc_AssemblyEventConnector class attributes and methods

# ClosedWorkload class attributes and methods

# PassiveResource class attributes and methods

# VariableCharacterisation class attributes and methods

# seff_performance_pc_InfrastructureCall class attributes and methods

# seff_performance_pc_ResourceCall class attributes and methods

# seff_performance_pc_ParametricResourceDemand class attributes and methods

# LoopAction class attributes and methods

# GuardedBranchTransition class attributes and methods

# qos_performance_pc_SpecifiedExecutionTime class attributes and methods

# composition_pc_EventChannelSinkConnector class attributes and methods

# pcm_pc_entity_pc_ResourceInterfaceRequiringEntity class attributes and methods

# entity_pc_ResourceRequiredRole class attributes and methods

# pcm_pc_entity_pc_ResourceRequiredRole class attributes and methods

# Loop class attributes and methods

# OpenWorkload class attributes and methods

# Delay class attributes and methods

# CommunicationLinkResourceSpecification class attributes and methods

# ProcessingResourceSpecification class attributes and methods

# pcm_pc_entity_pc_ResourceProvidedRole class attributes and methods

# Role class attributes and methods

# entity_pc_ResourceInterfaceProvidingEntity class attributes and methods

# ResourceInterface class attributes and methods

# pcm_pc_entity_pc_InterfaceProvidingRequiringEntity class attributes and methods

# entity_pc_InterfaceProvidingEntity class attributes and methods

# entity_pc_InterfaceRequiringEntity class attributes and methods

# pcm_pc_entity_pc_InterfaceProvidingEntity class attributes and methods

# Entity class attributes and methods

# ProvidedRole class attributes and methods

# pcm_pc_entity_pc_InterfaceRequiringEntity class attributes and methods

# entity_pc_Entity class attributes and methods

# entity_pc_ResourceInterfaceRequiringEntity class attributes and methods

# RequiredRole class attributes and methods

# pcm_pc_entity_pc_ResourceInterfaceProvidingEntity class attributes and methods

# entity_pc_ResourceProvidedRole class attributes and methods

# pcm_pc_entity_pc_ComposedProvidingRequiringEntity class attributes and methods
pcm_pc_entity_pc_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound: Method = Method(name="ProvidedRolesMustBeBound", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_entity_pc_ComposedProvidingRequiringEntity.methods={pcm_pc_entity_pc_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound}

# composition_pc_ComposedStructure class attributes and methods

# entity_pc_InterfaceProvidingRequiringEntity class attributes and methods

# pcm_pc_entity_pc_NamedElement class attributes and methods
pcm_pc_entity_pc_NamedElement_entityName: Property = Property(name="entityName", type=StringType)
pcm_pc_entity_pc_NamedElement.attributes={pcm_pc_entity_pc_NamedElement_entityName}

# pcm_pc_entity_pc_ResourceInterfaceProvidingRequiringEntity class attributes and methods

# pcm_pc_entity_pc_Entity class attributes and methods

# Identifier class attributes and methods

# entity_pc_NamedElement class attributes and methods

# pcm_pc_composition_pc_DelegationConnector class attributes and methods

# Connector class attributes and methods

# pcm_pc_composition_pc_Connector class attributes and methods

# pcm_pc_composition_pc_ComposedStructure class attributes and methods
pcm_pc_composition_pc_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors: Method = Method(name="MultipleConnectorsConstraintForAssemblyConnectors", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_composition_pc_ComposedStructure_m_MultipleConnectorsConstraint: Method = Method(name="MultipleConnectorsConstraint", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_composition_pc_ComposedStructure.methods={pcm_pc_composition_pc_ComposedStructure_m_MultipleConnectorsConstraint, pcm_pc_composition_pc_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors}

# pcm_pc_composition_pc_ProvidedDelegationConnector class attributes and methods
pcm_pc_composition_pc_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_composition_pc_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_composition_pc_ProvidedDelegationConnector.methods={pcm_pc_composition_pc_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame, pcm_pc_composition_pc_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure}

# DelegationConnector class attributes and methods

# composition_pc_AssemblyContext class attributes and methods

# composition_pc_ResourceRequiredDelegationConnector class attributes and methods

# composition_pc_EventChannel class attributes and methods

# composition_pc_Connector class attributes and methods

# pcm_pc_composition_pc_ResourceRequiredDelegationConnector class attributes and methods

# pcm_pc_composition_pc_EventChannel class attributes and methods

# EventGroup class attributes and methods

# composition_pc_EventChannelSourceConnector class attributes and methods

# pcm_pc_composition_pc_EventChannelSourceConnector class attributes and methods

# SourceRole class attributes and methods

# pcm_pc_composition_pc_EventChannelSinkConnector class attributes and methods

# SinkRole class attributes and methods

# PCMRandomVariable class attributes and methods

# OperationRequiredRole class attributes and methods

# pcm_pc_composition_pc_AssemblyConnector class attributes and methods
pcm_pc_composition_pc_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_composition_pc_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_composition_pc_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch: Method = Method(name="AssemblyConnectorsReferencedInterfacesMustMatch", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_composition_pc_AssemblyConnector.methods={pcm_pc_composition_pc_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch, pcm_pc_composition_pc_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch, pcm_pc_composition_pc_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch}

# OperationProvidedRole class attributes and methods

# pcm_pc_composition_pc_RequiredDelegationConnector class attributes and methods
pcm_pc_composition_pc_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_composition_pc_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_composition_pc_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector: Method = Method(name="RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_composition_pc_RequiredDelegationConnector.methods={pcm_pc_composition_pc_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector, pcm_pc_composition_pc_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure, pcm_pc_composition_pc_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame}

# pcm_pc_composition_pc_SourceDelegationConnector class attributes and methods

# pcm_pc_composition_pc_AssemblyEventConnector class attributes and methods

# pcm_pc_composition_pc_RequiredResourceDelegationConnector class attributes and methods

# pcm_pc_composition_pc_SinkDelegationConnector class attributes and methods

# pcm_pc_composition_pc_AssemblyContext class attributes and methods

# RepositoryComponent class attributes and methods

# VariableUsage class attributes and methods

# pcm_pc_composition_pc_AssemblyInfrastructureConnector class attributes and methods

# InfrastructureProvidedRole class attributes and methods

# InfrastructureRequiredRole class attributes and methods

# pcm_pc_usagemodel_pc_Workload class attributes and methods

# pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector class attributes and methods

# pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector class attributes and methods

# pcm_pc_usagemodel_pc_UsageModel class attributes and methods

# UserData class attributes and methods

# pcm_pc_usagemodel_pc_EntryLevelSystemCall class attributes and methods
pcm_pc_usagemodel_pc_EntryLevelSystemCall_priority: Property = Property(name="priority", type=IntegerType)
pcm_pc_usagemodel_pc_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem: Method = Method(name="EntryLevelSystemCallMustReferenceProvidedRoleOfASystem", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_usagemodel_pc_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole: Method = Method(name="EntryLevelSystemCallSignatureMustMatchItsProvidedRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_usagemodel_pc_EntryLevelSystemCall.attributes={pcm_pc_usagemodel_pc_EntryLevelSystemCall_priority}
pcm_pc_usagemodel_pc_EntryLevelSystemCall.methods={pcm_pc_usagemodel_pc_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole, pcm_pc_usagemodel_pc_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem}

# AbstractUserAction class attributes and methods

# OperationSignature class attributes and methods

# UsageScenario class attributes and methods

# pcm_pc_usagemodel_pc_UsageScenario class attributes and methods

# UsageModel class attributes and methods

# ScenarioBehaviour class attributes and methods

# Workload class attributes and methods

# pcm_pc_usagemodel_pc_UserData class attributes and methods

# BranchTransition class attributes and methods

# pcm_pc_usagemodel_pc_BranchTransition class attributes and methods
pcm_pc_usagemodel_pc_BranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_pc_usagemodel_pc_BranchTransition.attributes={pcm_pc_usagemodel_pc_BranchTransition_branchProbability}

# Branch class attributes and methods

# pcm_pc_usagemodel_pc_Branch class attributes and methods
pcm_pc_usagemodel_pc_Branch_m_AllBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_usagemodel_pc_Branch.methods={pcm_pc_usagemodel_pc_Branch_m_AllBranchProbabilitiesMustSumUpTo1}

# pcm_pc_usagemodel_pc_AbstractUserAction class attributes and methods

# pcm_pc_usagemodel_pc_ScenarioBehaviour class attributes and methods
pcm_pc_usagemodel_pc_ScenarioBehaviour_m_Exactlyonestop: Method = Method(name="Exactlyonestop", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_usagemodel_pc_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor: Method = Method(name="EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_usagemodel_pc_ScenarioBehaviour_m_Exactlyonestart: Method = Method(name="Exactlyonestart", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_usagemodel_pc_ScenarioBehaviour.methods={pcm_pc_usagemodel_pc_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor, pcm_pc_usagemodel_pc_ScenarioBehaviour_m_Exactlyonestart, pcm_pc_usagemodel_pc_ScenarioBehaviour_m_Exactlyonestop}

# pcm_pc_usagemodel_pc_Loop class attributes and methods

# pcm_pc_usagemodel_pc_Stop class attributes and methods
pcm_pc_usagemodel_pc_Stop_m_StopHasNoSuccessor: Method = Method(name="StopHasNoSuccessor", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_usagemodel_pc_Stop.methods={pcm_pc_usagemodel_pc_Stop_m_StopHasNoSuccessor}

# pcm_pc_usagemodel_pc_Start class attributes and methods
pcm_pc_usagemodel_pc_Start_m_StartHasNoPredecessor: Method = Method(name="StartHasNoPredecessor", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_usagemodel_pc_Start.methods={pcm_pc_usagemodel_pc_Start_m_StartHasNoPredecessor}

# pcm_pc_usagemodel_pc_OpenWorkload class attributes and methods
pcm_pc_usagemodel_pc_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified: Method = Method(name="InterArrivalTimeInOpenWorkloadNeedsToBeSpecified", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_usagemodel_pc_OpenWorkload.methods={pcm_pc_usagemodel_pc_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified}

# pcm_pc_repository_pc_PassiveResource class attributes and methods

# BasicComponent class attributes and methods

# ResourceTimeoutFailureType class attributes and methods

# pcm_pc_repository_pc_BasicComponent class attributes and methods
pcm_pc_repository_pc_BasicComponent_m_NoSeffTypeUsedTwice: Method = Method(name="NoSeffTypeUsedTwice", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_repository_pc_BasicComponent_m_ProvideSameInterfacesAsImplementationType: Method = Method(name="ProvideSameInterfacesAsImplementationType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_repository_pc_BasicComponent_m_RequireSameInterfacesAsImplementationType: Method = Method(name="RequireSameInterfacesAsImplementationType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_repository_pc_BasicComponent.methods={pcm_pc_repository_pc_BasicComponent_m_ProvideSameInterfacesAsImplementationType, pcm_pc_repository_pc_BasicComponent_m_NoSeffTypeUsedTwice, pcm_pc_repository_pc_BasicComponent_m_RequireSameInterfacesAsImplementationType}

# ImplementationComponentType class attributes and methods

# pcm_pc_usagemodel_pc_Delay class attributes and methods

# pcm_pc_usagemodel_pc_ClosedWorkload class attributes and methods
pcm_pc_usagemodel_pc_ClosedWorkload_population: Property = Property(name="population", type=IntegerType)
pcm_pc_usagemodel_pc_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified: Method = Method(name="ThinkTimeInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_usagemodel_pc_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified: Method = Method(name="PopulationInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_usagemodel_pc_ClosedWorkload.attributes={pcm_pc_usagemodel_pc_ClosedWorkload_population}
pcm_pc_usagemodel_pc_ClosedWorkload.methods={pcm_pc_usagemodel_pc_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified, pcm_pc_usagemodel_pc_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified}

# pcm_pc_repository_pc_ImplementationComponentType class attributes and methods
pcm_pc_repository_pc_ImplementationComponentType_componentType: Property = Property(name="componentType", type=StringType)
pcm_pc_repository_pc_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType: Method = Method(name="RequiredInterfacesHaveToConformToCompleteType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_repository_pc_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType: Method = Method(name="providedInterfacesHaveToConformToCompleteType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_repository_pc_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType: Method = Method(name="ProvidedInterfaceHaveToConformToComponentType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_repository_pc_ImplementationComponentType.attributes={pcm_pc_repository_pc_ImplementationComponentType_componentType}
pcm_pc_repository_pc_ImplementationComponentType.methods={pcm_pc_repository_pc_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType, pcm_pc_repository_pc_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType, pcm_pc_repository_pc_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType}

# CompleteComponentType class attributes and methods

# ServiceEffectSpecification class attributes and methods

# EventType class attributes and methods

# ResourceSignature class attributes and methods

# pcm_pc_repository_pc_DataType class attributes and methods

# pcm_pc_repository_pc_Repository class attributes and methods
pcm_pc_repository_pc_Repository_repositoryDescription: Property = Property(name="repositoryDescription", type=StringType)
pcm_pc_repository_pc_Repository.attributes={pcm_pc_repository_pc_Repository_repositoryDescription}

# Interface class attributes and methods

# FailureType class attributes and methods

# pcm_pc_repository_pc_RepositoryComponent class attributes and methods

# InterfaceProvidingRequiringEntity class attributes and methods

# Repository class attributes and methods

# pcm_pc_repository_pc_ProvidedRole class attributes and methods

# pcm_pc_repository_pc_Parameter class attributes and methods
pcm_pc_repository_pc_Parameter_parameterName: Property = Property(name="parameterName", type=StringType)
pcm_pc_repository_pc_Parameter_modifier__Parameter: Property = Property(name="modifier__Parameter", type=StringType)
pcm_pc_repository_pc_Parameter.attributes={pcm_pc_repository_pc_Parameter_parameterName, pcm_pc_repository_pc_Parameter_modifier__Parameter}

# DataType class attributes and methods

# InfrastructureSignature class attributes and methods

# RequiredCharacterisation class attributes and methods

# pcm_pc_repository_pc_RequiredCharacterisation class attributes and methods
pcm_pc_repository_pc_RequiredCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_pc_repository_pc_RequiredCharacterisation.attributes={pcm_pc_repository_pc_RequiredCharacterisation_type}

# Parameter class attributes and methods

# pcm_pc_repository_pc_EventGroup class attributes and methods

# pcm_pc_repository_pc_EventType class attributes and methods

# Signature class attributes and methods

# pcm_pc_repository_pc_Signature class attributes and methods

# pcm_pc_repository_pc_Interface class attributes and methods
pcm_pc_repository_pc_Interface_m_NoProtocolTypeIDUsedTwice: Method = Method(name="NoProtocolTypeIDUsedTwice", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_repository_pc_Interface.methods={pcm_pc_repository_pc_Interface_m_NoProtocolTypeIDUsedTwice}

# Protocol class attributes and methods

# pcm_pc_repository_pc_InfrastructureRequiredRole class attributes and methods

# pcm_pc_repository_pc_RequiredRole class attributes and methods

# pcm_pc_repository_pc_OperationSignature class attributes and methods
pcm_pc_repository_pc_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature: Method = Method(name="ParameterNamesHaveToBeUniqueForASignature", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_repository_pc_OperationSignature.methods={pcm_pc_repository_pc_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature}

# OperationInterface class attributes and methods

# ExceptionType class attributes and methods

# pcm_pc_repository_pc_ExceptionType class attributes and methods
pcm_pc_repository_pc_ExceptionType_exceptionName: Property = Property(name="exceptionName", type=StringType)
pcm_pc_repository_pc_ExceptionType_exceptionMessage: Property = Property(name="exceptionMessage", type=StringType)
pcm_pc_repository_pc_ExceptionType.attributes={pcm_pc_repository_pc_ExceptionType_exceptionName, pcm_pc_repository_pc_ExceptionType_exceptionMessage}

# pcm_pc_repository_pc_InfrastructureSignature class attributes and methods

# InfrastructureInterface class attributes and methods

# pcm_pc_repository_pc_InfrastructureInterface class attributes and methods

# pcm_pc_repository_pc_OperationRequiredRole class attributes and methods

# pcm_pc_repository_pc_SourceRole class attributes and methods

# pcm_pc_repository_pc_SinkRole class attributes and methods

# pcm_pc_repository_pc_OperationProvidedRole class attributes and methods

# pcm_pc_repository_pc_InfrastructureProvidedRole class attributes and methods

# pcm_pc_repository_pc_OperationInterface class attributes and methods
pcm_pc_repository_pc_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface: Method = Method(name="SignaturesHaveToBeUniqueForAnInterface", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_repository_pc_OperationInterface.methods={pcm_pc_repository_pc_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface}

# ProvidesComponentType class attributes and methods

# pcm_pc_repository_pc_ProvidesComponentType class attributes and methods
pcm_pc_repository_pc_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_repository_pc_ProvidesComponentType.methods={pcm_pc_repository_pc_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType}

# pcm_pc_repository_pc_CompositeComponent class attributes and methods
pcm_pc_repository_pc_CompositeComponent_m_ProvideSameInterfaces: Method = Method(name="ProvideSameInterfaces", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_repository_pc_CompositeComponent_m_RequireSameInterfaces: Method = Method(name="RequireSameInterfaces", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_repository_pc_CompositeComponent.methods={pcm_pc_repository_pc_CompositeComponent_m_ProvideSameInterfaces, pcm_pc_repository_pc_CompositeComponent_m_RequireSameInterfaces}

# entity_pc_ComposedProvidingRequiringEntity class attributes and methods

# repository_pc_ImplementationComponentType class attributes and methods

# pcm_pc_repository_pc_CompleteComponentType class attributes and methods
pcm_pc_repository_pc_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_repository_pc_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2: Method = Method(name="providedInterfacesHaveToConformToProvidedType2", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_repository_pc_CompleteComponentType.methods={pcm_pc_repository_pc_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2, pcm_pc_repository_pc_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType}

# pcm_pc_repository_pc_CollectionDataType class attributes and methods

# repository_pc_DataType class attributes and methods

# pcm_pc_repository_pc_CompositeDataType class attributes and methods

# CompositeDataType class attributes and methods

# InnerDeclaration class attributes and methods

# pcm_pc_repository_pc_InnerDeclaration class attributes and methods

# NamedElement class attributes and methods

# pcm_pc_repository_pc_PrimitiveDataType class attributes and methods
pcm_pc_repository_pc_PrimitiveDataType_type: Property = Property(name="type", type=StringType)
pcm_pc_repository_pc_PrimitiveDataType.attributes={pcm_pc_repository_pc_PrimitiveDataType_type}

# pcm_pc_resourcetype_pc_ProcessingResourceType class attributes and methods

# ResourceType class attributes and methods

# HardwareInducedFailureType class attributes and methods

# pcm_pc_resourcetype_pc_ResourceType class attributes and methods

# UnitCarryingElement class attributes and methods

# ResourceRepository class attributes and methods

# pcm_pc_resourcetype_pc_ResourceRepository class attributes and methods

# SchedulingPolicy class attributes and methods

# pcm_pc_resourcetype_pc_SchedulingPolicy class attributes and methods

# pcm_pc_resourcetype_pc_CommunicationLinkResourceType class attributes and methods

# NetworkInducedFailureType class attributes and methods

# pcm_pc_resourcetype_pc_ResourceInterface class attributes and methods

# pcm_pc_repository_pc_Role class attributes and methods

# pcm_pc_resourcetype_pc_ResourceSignature class attributes and methods
pcm_pc_resourcetype_pc_ResourceSignature_resourceServiceId: Property = Property(name="resourceServiceId", type=IntegerType)
pcm_pc_resourcetype_pc_ResourceSignature.attributes={pcm_pc_resourcetype_pc_ResourceSignature_resourceServiceId}

# CallAction class attributes and methods

# SynchronisationPoint class attributes and methods

# CallReturnAction class attributes and methods

# SetVariableAction class attributes and methods

# SpecifiedOutputParameterAbstraction class attributes and methods

# EntryLevelSystemCall class attributes and methods

# parameter_pc_pcm_pc_AbstractNamedReference class attributes and methods

# pcm_pc_parameter_pc_VariableCharacterisation class attributes and methods
pcm_pc_parameter_pc_VariableCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_pc_parameter_pc_VariableCharacterisation.attributes={pcm_pc_parameter_pc_VariableCharacterisation_type}

# pcm_pc_protocol_pc_Protocol class attributes and methods
pcm_pc_protocol_pc_Protocol_protocolTypeID: Property = Property(name="protocolTypeID", type=StringType)
pcm_pc_protocol_pc_Protocol.attributes={pcm_pc_protocol_pc_Protocol_protocolTypeID}

# pcm_pc_parameter_pc_VariableUsage class attributes and methods

# pcm_pc_reliability_pc_FailureOccurrenceDescription class attributes and methods
pcm_pc_reliability_pc_FailureOccurrenceDescription_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_pc_reliability_pc_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange: Method = Method(name="EnsureValidFailureProbabilityRange", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_reliability_pc_FailureOccurrenceDescription.attributes={pcm_pc_reliability_pc_FailureOccurrenceDescription_failureProbability}
pcm_pc_reliability_pc_FailureOccurrenceDescription.methods={pcm_pc_reliability_pc_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange}

# pcm_pc_reliability_pc_HardwareInducedFailureType class attributes and methods
pcm_pc_reliability_pc_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType: Method = Method(name="HardwareInducedFailureTypeHasProcessingResourceType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_reliability_pc_HardwareInducedFailureType.methods={pcm_pc_reliability_pc_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType}

# ProcessingResourceType class attributes and methods

# pcm_pc_reliability_pc_SoftwareInducedFailureType class attributes and methods

# InternalFailureOccurrenceDescription class attributes and methods

# pcm_pc_parameter_pc_CharacterisedVariable class attributes and methods
pcm_pc_parameter_pc_CharacterisedVariable_characterisationType: Property = Property(name="characterisationType", type=StringType)
pcm_pc_parameter_pc_CharacterisedVariable.attributes={pcm_pc_parameter_pc_CharacterisedVariable_characterisationType}

# Variable class attributes and methods

# InternalAction class attributes and methods

# pcm_pc_reliability_pc_InternalFailureOccurrenceDescription class attributes and methods
pcm_pc_reliability_pc_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_reliability_pc_InternalFailureOccurrenceDescription.methods={pcm_pc_reliability_pc_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription}

# FailureOccurrenceDescription class attributes and methods

# qos_reliability_pc_SpecifiedReliabilityAnnotation class attributes and methods

# pcm_pc_reliability_pc_ResourceTimeoutFailureType class attributes and methods

# pcm_pc_reliability_pc_FailureType class attributes and methods

# pcm_pc_seff_pc_StopAction class attributes and methods
pcm_pc_seff_pc_StopAction_m_StopActionSuccessorMustNotBeDefined: Method = Method(name="StopActionSuccessorMustNotBeDefined", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_seff_pc_StopAction.methods={pcm_pc_seff_pc_StopAction_m_StopActionSuccessorMustNotBeDefined}

# AbstractInternalControlFlowAction class attributes and methods

# SoftwareInducedFailureType class attributes and methods

# pcm_pc_reliability_pc_NetworkInducedFailureType class attributes and methods
pcm_pc_reliability_pc_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType: Method = Method(name="NetworkInducedFailureTypeHasCommunicationLinkResourceType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_reliability_pc_NetworkInducedFailureType.methods={pcm_pc_reliability_pc_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType}

# CommunicationLinkResourceType class attributes and methods

# pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription class attributes and methods
pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription.methods={pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription}

# AbstractLoopAction class attributes and methods

# pcm_pc_seff_pc_AbstractInternalControlFlowAction class attributes and methods

# AbstractAction class attributes and methods

# AbstractBranchTransition class attributes and methods

# pcm_pc_seff_pc_AbstractLoopAction class attributes and methods

# pcm_pc_seff_pc_AbstractBranchTransition class attributes and methods

# BranchAction class attributes and methods

# pcm_pc_seff_pc_AbstractAction class attributes and methods

# ResourceDemandingBehaviour class attributes and methods

# pcm_pc_seff_pc_ResourceDemandingBehaviour class attributes and methods
pcm_pc_seff_pc_ResourceDemandingBehaviour_m_ExactlyOneStartAction: Method = Method(name="ExactlyOneStartAction", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_seff_pc_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor: Method = Method(name="EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_seff_pc_ResourceDemandingBehaviour_m_ExactlyOneStopAction: Method = Method(name="ExactlyOneStopAction", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_seff_pc_ResourceDemandingBehaviour.methods={pcm_pc_seff_pc_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor, pcm_pc_seff_pc_ResourceDemandingBehaviour_m_ExactlyOneStopAction, pcm_pc_seff_pc_ResourceDemandingBehaviour_m_ExactlyOneStartAction}

# pcm_pc_seff_pc_CallAction class attributes and methods

# pcm_pc_seff_pc_StartAction class attributes and methods
pcm_pc_seff_pc_StartAction_m_StartActionPredecessorMustNotBeDefined: Method = Method(name="StartActionPredecessorMustNotBeDefined", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_seff_pc_StartAction.methods={pcm_pc_seff_pc_StartAction_m_StartActionPredecessorMustNotBeDefined}

# pcm_pc_seff_pc_ServiceEffectSpecification class attributes and methods
pcm_pc_seff_pc_ServiceEffectSpecification_seffTypeID: Property = Property(name="seffTypeID", type=StringType)
pcm_pc_seff_pc_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole: Method = Method(name="ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_seff_pc_ServiceEffectSpecification.attributes={pcm_pc_seff_pc_ServiceEffectSpecification_seffTypeID}
pcm_pc_seff_pc_ServiceEffectSpecification.methods={pcm_pc_seff_pc_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole}

# pcm_pc_seff_pc_ResourceDemandingSEFF class attributes and methods

# seff_pc_ServiceEffectSpecification class attributes and methods

# seff_pc_ResourceDemandingBehaviour class attributes and methods

# pcm_pc_seff_pc_BranchAction class attributes and methods
pcm_pc_seff_pc_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions: Method = Method(name="EitherGuardedBranchesOrProbabilisiticBranchTransitions", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_seff_pc_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllProbabilisticBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_seff_pc_BranchAction.methods={pcm_pc_seff_pc_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions, pcm_pc_seff_pc_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1}

# ResourceDemandingSEFF class attributes and methods

# pcm_pc_seff_pc_ReleaseAction class attributes and methods

# pcm_pc_seff_pc_LoopAction class attributes and methods

# pcm_pc_seff_pc_ForkAction class attributes and methods

# ForkedBehaviour class attributes and methods

# ResourceDemandingInternalBehaviour class attributes and methods

# pcm_pc_seff_pc_ForkedBehaviour class attributes and methods

# pcm_pc_seff_pc_ResourceDemandingInternalBehaviour class attributes and methods

# ForkAction class attributes and methods

# pcm_pc_seff_pc_SynchronisationPoint class attributes and methods

# pcm_pc_seff_pc_ExternalCallAction class attributes and methods
pcm_pc_seff_pc_ExternalCallAction_retryCount: Property = Property(name="retryCount", type=IntegerType)
pcm_pc_seff_pc_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer: Method = Method(name="OperationRequiredRoleMustBeReferencedByContainer", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_seff_pc_ExternalCallAction_m_SignatureBelongsToRole: Method = Method(name="SignatureBelongsToRole", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_seff_pc_ExternalCallAction.attributes={pcm_pc_seff_pc_ExternalCallAction_retryCount}
pcm_pc_seff_pc_ExternalCallAction.methods={pcm_pc_seff_pc_ExternalCallAction_m_SignatureBelongsToRole, pcm_pc_seff_pc_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer}

# seff_pc_AbstractAction class attributes and methods

# seff_pc_CallReturnAction class attributes and methods

# seff_reliability_pc_FailureHandlingEntity class attributes and methods

# pcm_pc_seff_pc_CallReturnAction class attributes and methods

# pcm_pc_seff_pc_ProbabilisticBranchTransition class attributes and methods
pcm_pc_seff_pc_ProbabilisticBranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_pc_seff_pc_ProbabilisticBranchTransition.attributes={pcm_pc_seff_pc_ProbabilisticBranchTransition_branchProbability}

# pcm_pc_seff_pc_AcquireAction class attributes and methods
pcm_pc_seff_pc_AcquireAction_timeout: Property = Property(name="timeout", type=BooleanType)
pcm_pc_seff_pc_AcquireAction_timeoutValue: Property = Property(name="timeoutValue", type=FloatType)
pcm_pc_seff_pc_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative: Method = Method(name="TimeoutValueOfAcquireActionMustNotBeNegative", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_seff_pc_AcquireAction.attributes={pcm_pc_seff_pc_AcquireAction_timeoutValue, pcm_pc_seff_pc_AcquireAction_timeout}
pcm_pc_seff_pc_AcquireAction.methods={pcm_pc_seff_pc_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative}

# pcm_pc_seff_pc_CollectionIteratorAction class attributes and methods

# pcm_pc_seff_pc_SetVariableAction class attributes and methods

# pcm_pc_seff_pc_InternalCallAction class attributes and methods

# seff_pc_CallAction class attributes and methods

# seff_pc_AbstractInternalControlFlowAction class attributes and methods

# pcm_pc_seff_pc_EmitEventAction class attributes and methods

# pcm_pc_seff_pc_GuardedBranchTransition class attributes and methods

# pcm_pc_seff_pc_InternalAction class attributes and methods
pcm_pc_seff_pc_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_seff_pc_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfInternalActionFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_seff_pc_InternalAction.methods={pcm_pc_seff_pc_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed, pcm_pc_seff_pc_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1}

# pcm_pc_seff_performance_pc_ResourceCall class attributes and methods
pcm_pc_seff_performance_pc_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole: Method = Method(name="ResourceSignatureBelongsToResourceRequiredRole", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_seff_performance_pc_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent: Method = Method(name="ResourceRequiredRoleMustBeReferencedByComponent", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_seff_performance_pc_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_seff_performance_pc_ResourceCall.methods={pcm_pc_seff_performance_pc_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction, pcm_pc_seff_performance_pc_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole, pcm_pc_seff_performance_pc_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent}

# pcm_pc_seff_performance_pc_InfrastructureCall class attributes and methods
pcm_pc_seff_performance_pc_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent: Method = Method(name="ReferencedRequiredRoleMustBeRequiredByComponent", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_seff_performance_pc_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_seff_performance_pc_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole: Method = Method(name="SignatureMustBelongToUsedRequiredRole", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_seff_performance_pc_InfrastructureCall.methods={pcm_pc_seff_performance_pc_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent, pcm_pc_seff_performance_pc_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole, pcm_pc_seff_performance_pc_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction}

# pcm_pc_seff_performance_pc_ParametricResourceDemand class attributes and methods
pcm_pc_seff_performance_pc_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_seff_performance_pc_ParametricResourceDemand.methods={pcm_pc_seff_performance_pc_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction}

# seff_reliability_pc_RecoveryActionBehaviour class attributes and methods

# pcm_pc_seff_reliability_pc_RecoveryActionBehaviour class attributes and methods
pcm_pc_seff_reliability_pc_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes: Method = Method(name="SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_seff_reliability_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor: Method = Method(name="RecoveryActionBehaviourHasOnlyOnePredecessor", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_seff_reliability_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself: Method = Method(name="RecoveryActionBehaviourIsNotSuccessorOfItself", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_seff_reliability_pc_RecoveryActionBehaviour.methods={pcm_pc_seff_reliability_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor, pcm_pc_seff_reliability_pc_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes, pcm_pc_seff_reliability_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself}

# pcm_pc_qosannotations_pc_SpecifiedQoSAnnotation class attributes and methods

# QoSAnnotations class attributes and methods

# seff_reliability_pc_RecoveryAction class attributes and methods

# pcm_pc_seff_reliability_pc_RecoveryAction class attributes and methods
pcm_pc_seff_reliability_pc_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet: Method = Method(name="PrimaryBehaviourOfRecoveryActionMustBeSet", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_seff_reliability_pc_RecoveryAction.methods={pcm_pc_seff_reliability_pc_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet}

# pcm_pc_seff_reliability_pc_FailureHandlingEntity class attributes and methods

# pcm_pc_qos_performance_pc_SystemSpecifiedExecutionTime class attributes and methods
pcm_pc_qos_performance_pc_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem: Method = Method(name="SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_qos_performance_pc_SystemSpecifiedExecutionTime.methods={pcm_pc_qos_performance_pc_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem}

# SpecifiedExecutionTime class attributes and methods

# pcm_pc_qos_performance_pc_SpecifiedExecutionTime class attributes and methods

# pcm_pc_qosannotations_pc_QoSAnnotations class attributes and methods
pcm_pc_qosannotations_pc_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed: Method = Method(name="MultipleReliabilityAnnotationsPerExternalCallNotAllowed", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_qosannotations_pc_QoSAnnotations.methods={pcm_pc_qosannotations_pc_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed}

# System class attributes and methods

# SpecifiedQoSAnnotation class attributes and methods

# pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction class attributes and methods

# ExternalFailureOccurrenceDescription class attributes and methods

# pcm_pc_qos_performance_pc_ComponentSpecifiedExecutionTime class attributes and methods

# pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation class attributes and methods
pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem: Method = Method(name="SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation.methods={pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed, pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1, pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem}

# pcm_pc_resourceenvironment_pc_ResourceEnvironment class attributes and methods

# LinkingResource class attributes and methods

# ResourceContainer class attributes and methods

# pcm_pc_resourceenvironment_pc_LinkingResource class attributes and methods

# ResourceEnvironment class attributes and methods

# pcm_pc_resourceenvironment_pc_ResourceContainer class attributes and methods

# pcm_pc_system_pc_System class attributes and methods
pcm_pc_system_pc_System_m_SystemMustHaveAtLeastOneProvidedRole: Method = Method(name="SystemMustHaveAtLeastOneProvidedRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_system_pc_System.methods={pcm_pc_system_pc_System_m_SystemMustHaveAtLeastOneProvidedRole}

# pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification class attributes and methods
pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification.attributes={pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification_failureProbability}

# pcm_pc_allocation_pc_AllocationContext class attributes and methods
pcm_pc_allocation_pc_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred: Method = Method(name="OneAssemblyContextOrOneEventChannelShouldBeReferred", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_allocation_pc_AllocationContext.methods={pcm_pc_allocation_pc_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred}

# pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification class attributes and methods
pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification_requiredByContainer: Property = Property(name="requiredByContainer", type=BooleanType)
pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification_numberOfReplicas: Property = Property(name="numberOfReplicas", type=IntegerType)
pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification_MTTR: Property = Property(name="MTTR", type=FloatType)
pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification_MTTF: Property = Property(name="MTTF", type=FloatType)
pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification.attributes={pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification_MTTF, pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification_requiredByContainer, pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification_numberOfReplicas, pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification_MTTR}

# pcm_pc_allocation_pc_Allocation class attributes and methods
pcm_pc_allocation_pc_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce: Method = Method(name="EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_allocation_pc_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource: Method = Method(name="CommunicatingServersHaveToBeConnectedByLinkingResource", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_allocation_pc_Allocation.methods={pcm_pc_allocation_pc_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource, pcm_pc_allocation_pc_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce}

# AllocationContext class attributes and methods

# pcm_pc_subsystem_pc_SubSystem class attributes and methods

# repository_pc_RepositoryComponent class attributes and methods

# pcm_pc_completions_pc_Completion class attributes and methods

# Allocation class attributes and methods

# pcm_pc_completions_pc_CompletionRepository class attributes and methods

# Completion class attributes and methods

# pcm_pc_completions_pc_DelegatingExternalCallAction class attributes and methods

# ExternalCallAction class attributes and methods

# pcm_pc_completions_pc_NetworkDemandParametricResourceDemand class attributes and methods

# ParametricResourceDemand class attributes and methods

# Relationships
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="pcm_pc_EObject", type=pcm_pc_Pointcut, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_Pointcut", type=pcm_pc_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventChannelSinkConnector__FilterCondition16: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__FilterCondition16",
    ends={
        Property(name="core_pc", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc", type=composition_pc_EventChannelSinkConnector, multiplicity=Multiplicity(0, 1))
    }
)
assemblyEventConnector__FilterCondition17: BinaryAssociation = BinaryAssociation(
    name="assemblyEventConnector__FilterCondition17",
    ends={
        Property(name="core_pc19", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc18", type=composition_pc_AssemblyEventConnector, multiplicity=Multiplicity(0, 1))
    }
)
closedWorkload_PCMRandomVariable1: BinaryAssociation = BinaryAssociation(
    name="closedWorkload_PCMRandomVariable1",
    ends={
        Property(name="usagemodel_pc", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ClosedWorkload", type=ClosedWorkload, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_capacity_PCMRandomVariable2: BinaryAssociation = BinaryAssociation(
    name="passiveResource_capacity_PCMRandomVariable2",
    ends={
        Property(name="repository_pc", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
variableCharacterisation_Specification3: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_Specification3",
    ends={
        Property(name="parameter_pc", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableCharacterisation", type=VariableCharacterisation, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureCall__PCMRandomVariable4: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__PCMRandomVariable4",
    ends={
        Property(name="seff_pc", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_pc", type=seff_performance_pc_InfrastructureCall, multiplicity=Multiplicity(0, 1))
    }
)
resourceCall__PCMRandomVariable5: BinaryAssociation = BinaryAssociation(
    name="resourceCall__PCMRandomVariable5",
    ends={
        Property(name="seff_pc7", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_pc6", type=seff_performance_pc_ResourceCall, multiplicity=Multiplicity(0, 1))
    }
)
parametricResourceDemand_PCMRandomVariable8: BinaryAssociation = BinaryAssociation(
    name="parametricResourceDemand_PCMRandomVariable8",
    ends={
        Property(name="seff_pc10", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_pc9", type=seff_performance_pc_ParametricResourceDemand, multiplicity=Multiplicity(0, 1))
    }
)
loopAction_PCMRandomVariable11: BinaryAssociation = BinaryAssociation(
    name="loopAction_PCMRandomVariable11",
    ends={
        Property(name="seff_pc12", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopAction", type=LoopAction, multiplicity=Multiplicity(0, 1))
    }
)
guardedBranchTransition_PCMRandomVariable13: BinaryAssociation = BinaryAssociation(
    name="guardedBranchTransition_PCMRandomVariable13",
    ends={
        Property(name="seff_pc14", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="GuardedBranchTransition", type=GuardedBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
specifiedExecutionTime_PCMRandomVariable15: BinaryAssociation = BinaryAssociation(
    name="specifiedExecutionTime_PCMRandomVariable15",
    ends={
        Property(name="qosannotations_pc", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="qos_performance_pc", type=qos_performance_pc_SpecifiedExecutionTime, multiplicity=Multiplicity(0, 1))
    }
)
resourceRequiredRoles__ResourceInterfaceRequiringEntity39: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRoles__ResourceInterfaceRequiringEntity39",
    ends={
        Property(name="core_pc41", type=pcm_pc_entity_pc_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_pc40", type=entity_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredResourceInterface__ResourceRequiredRole42: BinaryAssociation = BinaryAssociation(
    name="requiredResourceInterface__ResourceRequiredRole42",
    ends={
        Property(name="ResourceInterface43", type=pcm_pc_entity_pc_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_entity_pc_ResourceRequiredRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
loop_LoopIteration20: BinaryAssociation = BinaryAssociation(
    name="loop_LoopIteration20",
    ends={
        Property(name="usagemodel_pc21", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Loop", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
openWorkload_PCMRandomVariable22: BinaryAssociation = BinaryAssociation(
    name="openWorkload_PCMRandomVariable22",
    ends={
        Property(name="usagemodel_pc23", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="OpenWorkload", type=OpenWorkload, multiplicity=Multiplicity(0, 1))
    }
)
delay_TimeSpecification24: BinaryAssociation = BinaryAssociation(
    name="delay_TimeSpecification24",
    ends={
        Property(name="usagemodel_pc25", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Delay", type=Delay, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecifcation_throughput_PCMRandomVariable26: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifcation_throughput_PCMRandomVariable26",
    ends={
        Property(name="resourceenvironment_pc", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceSpecification_processingRate_PCMRandomVariable27: BinaryAssociation = BinaryAssociation(
    name="processingResourceSpecification_processingRate_PCMRandomVariable27",
    ends={
        Property(name="resourceenvironment_pc28", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcessingResourceSpecification", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecification_latency_PCMRandomVariable29: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecification_latency_PCMRandomVariable29",
    ends={
        Property(name="resourceenvironment_pc31", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceSpecification30", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaceProvidingEntity__ResourceProvidedRole32: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceProvidingEntity__ResourceProvidedRole32",
    ends={
        Property(name="core_pc33", type=pcm_pc_entity_pc_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_pc", type=entity_pc_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
providedResourceInterface__ResourceProvidedRole34: BinaryAssociation = BinaryAssociation(
    name="providedResourceInterface__ResourceProvidedRole34",
    ends={
        Property(name="ResourceInterface", type=pcm_pc_entity_pc_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_entity_pc_ResourceProvidedRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedRoles_InterfaceProvidingEntity35: BinaryAssociation = BinaryAssociation(
    name="providedRoles_InterfaceProvidingEntity35",
    ends={
        Property(name="repository_pc36", type=pcm_pc_entity_pc_InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="ProvidedRole", type=ProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredRoles_InterfaceRequiringEntity37: BinaryAssociation = BinaryAssociation(
    name="requiredRoles_InterfaceRequiringEntity37",
    ends={
        Property(name="repository_pc38", type=pcm_pc_entity_pc_InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="RequiredRole", type=RequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceInterfaceRequiringEntity__ResourceRequiredRole44: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceRequiringEntity__ResourceRequiredRole44",
    ends={
        Property(name="core_pc46", type=pcm_pc_entity_pc_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_pc45", type=entity_pc_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
resourceProvidedRoles__ResourceInterfaceProvidingEntity47: BinaryAssociation = BinaryAssociation(
    name="resourceProvidedRoles__ResourceInterfaceProvidingEntity47",
    ends={
        Property(name="core_pc49", type=pcm_pc_entity_pc_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_pc48", type=entity_pc_ResourceProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentStructure__Connector50: BinaryAssociation = BinaryAssociation(
    name="parentStructure__Connector50",
    ends={
        Property(name="core_pc52", type=pcm_pc_composition_pc_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc51", type=composition_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__EventChannelSinkConnector91: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSinkConnector91",
    ends={
        Property(name="composition_pc_AssemblyContext93", type=pcm_pc_composition_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_EventChannelSinkConnector92", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSinkConnector94: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSinkConnector94",
    ends={
        Property(name="core_pc96", type=pcm_pc_composition_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc95", type=composition_pc_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContexts__ComposedStructure53: BinaryAssociation = BinaryAssociation(
    name="assemblyContexts__ComposedStructure53",
    ends={
        Property(name="core_pc55", type=pcm_pc_composition_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc54", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredDelegationConnectors_ComposedStructure56: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredDelegationConnectors_ComposedStructure56",
    ends={
        Property(name="core_pc58", type=pcm_pc_composition_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc57", type=composition_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventChannel__ComposedStructure59: BinaryAssociation = BinaryAssociation(
    name="eventChannel__ComposedStructure59",
    ends={
        Property(name="core_pc61", type=pcm_pc_composition_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc60", type=composition_pc_EventChannel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectors__ComposedStructure62: BinaryAssociation = BinaryAssociation(
    name="connectors__ComposedStructure62",
    ends={
        Property(name="core_pc64", type=pcm_pc_composition_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc63", type=composition_pc_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerResourceRequiredRole_ResourceRequiredDelegationConnector65: BinaryAssociation = BinaryAssociation(
    name="innerResourceRequiredRole_ResourceRequiredDelegationConnector65",
    ends={
        Property(name="entity_pc_ResourceRequiredRole", type=pcm_pc_composition_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_ResourceRequiredDelegationConnector", type=entity_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerResourceRequiredRole_ResourceRequiredDelegationConnector66: BinaryAssociation = BinaryAssociation(
    name="outerResourceRequiredRole_ResourceRequiredDelegationConnector66",
    ends={
        Property(name="entity_pc_ResourceRequiredRole68", type=pcm_pc_composition_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_ResourceRequiredDelegationConnector67", type=entity_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure_ResourceRequiredDelegationConnector69: BinaryAssociation = BinaryAssociation(
    name="parentStructure_ResourceRequiredDelegationConnector69",
    ends={
        Property(name="core_pc71", type=pcm_pc_composition_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc70", type=composition_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__EventChannel72: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventChannel72",
    ends={
        Property(name="EventGroup", type=pcm_pc_composition_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_EventChannel", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSourceConnector__EventChannel73: BinaryAssociation = BinaryAssociation(
    name="eventChannelSourceConnector__EventChannel73",
    ends={
        Property(name="core_pc75", type=pcm_pc_composition_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc74", type=composition_pc_EventChannelSourceConnector, multiplicity=Multiplicity(0, 9999))
    }
)
eventChannelSinkConnector__EventChannel76: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__EventChannel76",
    ends={
        Property(name="core_pc78", type=pcm_pc_composition_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc77", type=composition_pc_EventChannelSinkConnector, multiplicity=Multiplicity(0, 9999))
    }
)
parentStructure__EventChannel79: BinaryAssociation = BinaryAssociation(
    name="parentStructure__EventChannel79",
    ends={
        Property(name="core_pc81", type=pcm_pc_composition_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc80", type=composition_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EventChannelSourceRole82: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EventChannelSourceRole82",
    ends={
        Property(name="SourceRole", type=pcm_pc_composition_pc_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_EventChannelSourceConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__EventChannelSourceConnector83: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSourceConnector83",
    ends={
        Property(name="composition_pc_AssemblyContext", type=pcm_pc_composition_pc_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_EventChannelSourceConnector84", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSourceConnector85: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSourceConnector85",
    ends={
        Property(name="core_pc87", type=pcm_pc_composition_pc_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc86", type=composition_pc_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__EventChannelSinkConnector88: BinaryAssociation = BinaryAssociation(
    name="sinkRole__EventChannelSinkConnector88",
    ends={
        Property(name="SinkRole", type=pcm_pc_composition_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_EventChannelSinkConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__EventChannelSinkConnector89: BinaryAssociation = BinaryAssociation(
    name="filterCondition__EventChannelSinkConnector89",
    ends={
        Property(name="core_pc90", type=pcm_pc_composition_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
innerRequiredRole_RequiredDelegationConnector104: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole_RequiredDelegationConnector104",
    ends={
        Property(name="OperationRequiredRole", type=pcm_pc_composition_pc_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_RequiredDelegationConnector", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole_RequiredDelegationConnector105: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole_RequiredDelegationConnector105",
    ends={
        Property(name="OperationRequiredRole107", type=pcm_pc_composition_pc_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_RequiredDelegationConnector106", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_RequiredDelegationConnector108: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_RequiredDelegationConnector108",
    ends={
        Property(name="composition_pc_AssemblyContext110", type=pcm_pc_composition_pc_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_RequiredDelegationConnector109", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole_ProvidedDelegationConnector97: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole_ProvidedDelegationConnector97",
    ends={
        Property(name="OperationProvidedRole", type=pcm_pc_composition_pc_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_ProvidedDelegationConnector", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole_ProvidedDelegationConnector98: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole_ProvidedDelegationConnector98",
    ends={
        Property(name="OperationProvidedRole100", type=pcm_pc_composition_pc_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_ProvidedDelegationConnector99", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_ProvidedDelegationConnector101: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ProvidedDelegationConnector101",
    ends={
        Property(name="composition_pc_AssemblyContext103", type=pcm_pc_composition_pc_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_ProvidedDelegationConnector102", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__AssemblyEventConnector133: BinaryAssociation = BinaryAssociation(
    name="filterCondition__AssemblyEventConnector133",
    ends={
        Property(name="core_pc135", type=pcm_pc_composition_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable134", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
innerSourceRole__SourceRole136: BinaryAssociation = BinaryAssociation(
    name="innerSourceRole__SourceRole136",
    ends={
        Property(name="SourceRole137", type=pcm_pc_composition_pc_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_SourceDelegationConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSourceRole__SourceRole138: BinaryAssociation = BinaryAssociation(
    name="outerSourceRole__SourceRole138",
    ends={
        Property(name="SourceRole140", type=pcm_pc_composition_pc_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_SourceDelegationConnector139", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SourceDelegationConnector141: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SourceDelegationConnector141",
    ends={
        Property(name="composition_pc_AssemblyContext143", type=pcm_pc_composition_pc_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_SourceDelegationConnector142", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext_AssemblyConnector111: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext_AssemblyConnector111",
    ends={
        Property(name="composition_pc_AssemblyContext112", type=pcm_pc_composition_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyConnector", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext_AssemblyConnector113: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext_AssemblyConnector113",
    ends={
        Property(name="composition_pc_AssemblyContext115", type=pcm_pc_composition_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyConnector114", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providedRole_AssemblyConnector116: BinaryAssociation = BinaryAssociation(
    name="providedRole_AssemblyConnector116",
    ends={
        Property(name="OperationProvidedRole118", type=pcm_pc_composition_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyConnector117", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole_AssemblyConnector119: BinaryAssociation = BinaryAssociation(
    name="requiredRole_AssemblyConnector119",
    ends={
        Property(name="OperationRequiredRole121", type=pcm_pc_composition_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyConnector120", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__AssemblyEventConnector122: BinaryAssociation = BinaryAssociation(
    name="sinkRole__AssemblyEventConnector122",
    ends={
        Property(name="SinkRole123", type=pcm_pc_composition_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyEventConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__AssemblyEventConnector124: BinaryAssociation = BinaryAssociation(
    name="sourceRole__AssemblyEventConnector124",
    ends={
        Property(name="SourceRole126", type=pcm_pc_composition_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyEventConnector125", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkAssemblyContext__AssemblyEventConnector127: BinaryAssociation = BinaryAssociation(
    name="sinkAssemblyContext__AssemblyEventConnector127",
    ends={
        Property(name="composition_pc_AssemblyContext129", type=pcm_pc_composition_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyEventConnector128", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
sourceAssemblyContext__AssemblyEventConnector130: BinaryAssociation = BinaryAssociation(
    name="sourceAssemblyContext__AssemblyEventConnector130",
    ends={
        Property(name="composition_pc_AssemblyContext132", type=pcm_pc_composition_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyEventConnector131", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredInfrastructureDelegationConnector174: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredInfrastructureDelegationConnector174",
    ends={
        Property(name="composition_pc_AssemblyContext176", type=pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector175", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredResourceDelegationConnector177: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredResourceDelegationConnector177",
    ends={
        Property(name="composition_pc_AssemblyContext178", type=pcm_pc_composition_pc_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_RequiredResourceDelegationConnector", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole__RequiredResourceDelegationConnector179: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredResourceDelegationConnector179",
    ends={
        Property(name="entity_pc_ResourceRequiredRole181", type=pcm_pc_composition_pc_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_RequiredResourceDelegationConnector180", type=entity_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredResourceDelegationConnector182: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredResourceDelegationConnector182",
    ends={
        Property(name="entity_pc_ResourceRequiredRole184", type=pcm_pc_composition_pc_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_RequiredResourceDelegationConnector183", type=entity_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure__AssemblyContext185: BinaryAssociation = BinaryAssociation(
    name="parentStructure__AssemblyContext185",
    ends={
        Property(name="core_pc187", type=pcm_pc_composition_pc_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc186", type=composition_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SinkDelegationConnector144: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SinkDelegationConnector144",
    ends={
        Property(name="composition_pc_AssemblyContext145", type=pcm_pc_composition_pc_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_SinkDelegationConnector", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
encapsulatedComponent__AssemblyContext188: BinaryAssociation = BinaryAssociation(
    name="encapsulatedComponent__AssemblyContext188",
    ends={
        Property(name="RepositoryComponent", type=pcm_pc_composition_pc_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyContext", type=RepositoryComponent, multiplicity=Multiplicity(0, 1))
    }
)
innerSinkRole__SinkRole146: BinaryAssociation = BinaryAssociation(
    name="innerSinkRole__SinkRole146",
    ends={
        Property(name="SinkRole148", type=pcm_pc_composition_pc_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_SinkDelegationConnector147", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSinkRole__SinkRole149: BinaryAssociation = BinaryAssociation(
    name="outerSinkRole__SinkRole149",
    ends={
        Property(name="SinkRole151", type=pcm_pc_composition_pc_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_SinkDelegationConnector150", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
configParameterUsages__AssemblyContext189: BinaryAssociation = BinaryAssociation(
    name="configParameterUsages__AssemblyContext189",
    ends={
        Property(name="parameter_pc190", type=pcm_pc_composition_pc_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedRole__AssemblyInfrastructureConnector152: BinaryAssociation = BinaryAssociation(
    name="providedRole__AssemblyInfrastructureConnector152",
    ends={
        Property(name="InfrastructureProvidedRole", type=pcm_pc_composition_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyInfrastructureConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__AssemblyInfrastructureConnector153: BinaryAssociation = BinaryAssociation(
    name="requiredRole__AssemblyInfrastructureConnector153",
    ends={
        Property(name="InfrastructureRequiredRole", type=pcm_pc_composition_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyInfrastructureConnector154", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext__AssemblyInfrastructureConnector155: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext__AssemblyInfrastructureConnector155",
    ends={
        Property(name="composition_pc_AssemblyContext157", type=pcm_pc_composition_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyInfrastructureConnector156", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext__AssemblyInfrastructureConnector158: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext__AssemblyInfrastructureConnector158",
    ends={
        Property(name="composition_pc_AssemblyContext160", type=pcm_pc_composition_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyInfrastructureConnector159", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole__ProvidedInfrastructureDelegationConnector161: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole__ProvidedInfrastructureDelegationConnector161",
    ends={
        Property(name="InfrastructureProvidedRole162", type=pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole__ProvidedInfrastructureDelegationConnector163: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole__ProvidedInfrastructureDelegationConnector163",
    ends={
        Property(name="InfrastructureProvidedRole165", type=pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector164", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__ProvidedInfrastructureDelegationConnector166: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__ProvidedInfrastructureDelegationConnector166",
    ends={
        Property(name="composition_pc_AssemblyContext168", type=pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector167", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole__RequiredInfrastructureDelegationConnector169: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredInfrastructureDelegationConnector169",
    ends={
        Property(name="InfrastructureRequiredRole170", type=pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredInfrastructureDelegationConnector171: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredInfrastructureDelegationConnector171",
    ends={
        Property(name="InfrastructureRequiredRole173", type=pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector172", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UserData201: BinaryAssociation = BinaryAssociation(
    name="usageModel_UserData201",
    ends={
        Property(name="usagemodel_pc203", type=pcm_pc_usagemodel_pc_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageModel202", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
userDataParameterUsages_UserData204: BinaryAssociation = BinaryAssociation(
    name="userDataParameterUsages_UserData204",
    ends={
        Property(name="parameter_pc206", type=pcm_pc_usagemodel_pc_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage205", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_UsageModel207: BinaryAssociation = BinaryAssociation(
    name="usageScenario_UsageModel207",
    ends={
        Property(name="usagemodel_pc209", type=pcm_pc_usagemodel_pc_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageScenario208", type=UsageScenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_UsageModel210: BinaryAssociation = BinaryAssociation(
    name="userData_UsageModel210",
    ends={
        Property(name="usagemodel_pc211", type=pcm_pc_usagemodel_pc_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="UserData", type=UserData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedRole_EntryLevelSystemCall212: BinaryAssociation = BinaryAssociation(
    name="providedRole_EntryLevelSystemCall212",
    ends={
        Property(name="OperationProvidedRole213", type=pcm_pc_usagemodel_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_usagemodel_pc_EntryLevelSystemCall", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__EntryLevelSystemCall214: BinaryAssociation = BinaryAssociation(
    name="operationSignature__EntryLevelSystemCall214",
    ends={
        Property(name="OperationSignature", type=pcm_pc_usagemodel_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_usagemodel_pc_EntryLevelSystemCall215", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
outputParameterUsages_EntryLevelSystemCall216: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsages_EntryLevelSystemCall216",
    ends={
        Property(name="parameter_pc218", type=pcm_pc_usagemodel_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage217", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_Workload191: BinaryAssociation = BinaryAssociation(
    name="usageScenario_Workload191",
    ends={
        Property(name="usagemodel_pc192", type=pcm_pc_usagemodel_pc_Workload, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
inputParameterUsages_EntryLevelSystemCall219: BinaryAssociation = BinaryAssociation(
    name="inputParameterUsages_EntryLevelSystemCall219",
    ends={
        Property(name="parameter_pc221", type=pcm_pc_usagemodel_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage220", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageModel_UsageScenario193: BinaryAssociation = BinaryAssociation(
    name="usageModel_UsageScenario193",
    ends={
        Property(name="usagemodel_pc194", type=pcm_pc_usagemodel_pc_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageModel", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_UsageScenario195: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_UsageScenario195",
    ends={
        Property(name="usagemodel_pc196", type=pcm_pc_usagemodel_pc_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
workload_UsageScenario197: BinaryAssociation = BinaryAssociation(
    name="workload_UsageScenario197",
    ends={
        Property(name="usagemodel_pc198", type=pcm_pc_usagemodel_pc_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="Workload", type=Workload, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext_userData199: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_userData199",
    ends={
        Property(name="composition_pc_AssemblyContext200", type=pcm_pc_usagemodel_pc_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_usagemodel_pc_UserData", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
usageScenario_SenarioBehaviour230: BinaryAssociation = BinaryAssociation(
    name="usageScenario_SenarioBehaviour230",
    ends={
        Property(name="usagemodel_pc232", type=pcm_pc_usagemodel_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageScenario231", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
branchTransition_ScenarioBehaviour233: BinaryAssociation = BinaryAssociation(
    name="branchTransition_ScenarioBehaviour233",
    ends={
        Property(name="usagemodel_pc234", type=pcm_pc_usagemodel_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="BranchTransition", type=BranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
loop_ScenarioBehaviour235: BinaryAssociation = BinaryAssociation(
    name="loop_ScenarioBehaviour235",
    ends={
        Property(name="usagemodel_pc237", type=pcm_pc_usagemodel_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="Loop236", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
actions_ScenarioBehaviour238: BinaryAssociation = BinaryAssociation(
    name="actions_ScenarioBehaviour238",
    ends={
        Property(name="usagemodel_pc240", type=pcm_pc_usagemodel_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction239", type=AbstractUserAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branch_BranchTransition241: BinaryAssociation = BinaryAssociation(
    name="branch_BranchTransition241",
    ends={
        Property(name="usagemodel_pc242", type=pcm_pc_usagemodel_pc_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="Branch", type=Branch, multiplicity=Multiplicity(0, 1))
    }
)
branchedBehaviour_BranchTransition243: BinaryAssociation = BinaryAssociation(
    name="branchedBehaviour_BranchTransition243",
    ends={
        Property(name="usagemodel_pc245", type=pcm_pc_usagemodel_pc_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour244", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
successor222: BinaryAssociation = BinaryAssociation(
    name="successor222",
    ends={
        Property(name="usagemodel_pc223", type=pcm_pc_usagemodel_pc_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
predecessor224: BinaryAssociation = BinaryAssociation(
    name="predecessor224",
    ends={
        Property(name="usagemodel_pc226", type=pcm_pc_usagemodel_pc_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction225", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_AbstractUserAction227: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_AbstractUserAction227",
    ends={
        Property(name="usagemodel_pc229", type=pcm_pc_usagemodel_pc_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour228", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
loopIteration_Loop249: BinaryAssociation = BinaryAssociation(
    name="loopIteration_Loop249",
    ends={
        Property(name="core_pc251", type=pcm_pc_usagemodel_pc_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable250", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyBehaviour_Loop252: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop252",
    ends={
        Property(name="usagemodel_pc254", type=pcm_pc_usagemodel_pc_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour253", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchTransitions_Branch246: BinaryAssociation = BinaryAssociation(
    name="branchTransitions_Branch246",
    ends={
        Property(name="usagemodel_pc248", type=pcm_pc_usagemodel_pc_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="BranchTransition247", type=BranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thinkTime_ClosedWorkload261: BinaryAssociation = BinaryAssociation(
    name="thinkTime_ClosedWorkload261",
    ends={
        Property(name="core_pc263", type=pcm_pc_usagemodel_pc_ClosedWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable262", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capacity_PassiveResource264: BinaryAssociation = BinaryAssociation(
    name="capacity_PassiveResource264",
    ends={
        Property(name="core_pc266", type=pcm_pc_repository_pc_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable265", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicComponent_PassiveResource267: BinaryAssociation = BinaryAssociation(
    name="basicComponent_PassiveResource267",
    ends={
        Property(name="repository_pc268", type=pcm_pc_repository_pc_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="BasicComponent", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
resourceTimeoutFailureType__PassiveResource269: BinaryAssociation = BinaryAssociation(
    name="resourceTimeoutFailureType__PassiveResource269",
    ends={
        Property(name="reliability_pc", type=pcm_pc_repository_pc_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceTimeoutFailureType", type=ResourceTimeoutFailureType, multiplicity=Multiplicity(0, 1))
    }
)
interArrivalTime_OpenWorkload255: BinaryAssociation = BinaryAssociation(
    name="interArrivalTime_OpenWorkload255",
    ends={
        Property(name="core_pc257", type=pcm_pc_usagemodel_pc_OpenWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable256", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeSpecification_Delay258: BinaryAssociation = BinaryAssociation(
    name="timeSpecification_Delay258",
    ends={
        Property(name="core_pc260", type=pcm_pc_usagemodel_pc_Delay, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable259", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serviceEffectSpecifications__BasicComponent270: BinaryAssociation = BinaryAssociation(
    name="serviceEffectSpecifications__BasicComponent270",
    ends={
        Property(name="ServiceEffectSpecification", type=ServiceEffectSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="seff_pc271", type=pcm_pc_repository_pc_BasicComponent, multiplicity=Multiplicity(1, 1))
    }
)
passiveResource_BasicComponent272: BinaryAssociation = BinaryAssociation(
    name="passiveResource_BasicComponent272",
    ends={
        Property(name="repository_pc274", type=pcm_pc_repository_pc_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="PassiveResource273", type=PassiveResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentCompleteComponentTypes275: BinaryAssociation = BinaryAssociation(
    name="parentCompleteComponentTypes275",
    ends={
        Property(name="CompleteComponentType", type=pcm_pc_repository_pc_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_ImplementationComponentType", type=CompleteComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
infrastructureSignature__Parameter285: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignature__Parameter285",
    ends={
        Property(name="repository_pc286", type=pcm_pc_repository_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="InfrastructureSignature", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__Parameter287: BinaryAssociation = BinaryAssociation(
    name="operationSignature__Parameter287",
    ends={
        Property(name="repository_pc289", type=pcm_pc_repository_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationSignature288", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
eventType__Parameter290: BinaryAssociation = BinaryAssociation(
    name="eventType__Parameter290",
    ends={
        Property(name="repository_pc291", type=pcm_pc_repository_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="EventType", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
resourceSignature__Parameter292: BinaryAssociation = BinaryAssociation(
    name="resourceSignature__Parameter292",
    ends={
        Property(name="resourcetype_pc", type=pcm_pc_repository_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceSignature", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
repository__DataType293: BinaryAssociation = BinaryAssociation(
    name="repository__DataType293",
    ends={
        Property(name="repository_pc295", type=pcm_pc_repository_pc_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository294", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
components__Repository296: BinaryAssociation = BinaryAssociation(
    name="components__Repository296",
    ends={
        Property(name="repository_pc298", type=pcm_pc_repository_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="RepositoryComponent297", type=RepositoryComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaces__Repository299: BinaryAssociation = BinaryAssociation(
    name="interfaces__Repository299",
    ends={
        Property(name="repository_pc300", type=pcm_pc_repository_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="Interface", type=Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentParameterUsage_ImplementationComponentType276: BinaryAssociation = BinaryAssociation(
    name="componentParameterUsage_ImplementationComponentType276",
    ends={
        Property(name="VariableUsage278", type=pcm_pc_repository_pc_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_ImplementationComponentType277", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository__RepositoryComponent279: BinaryAssociation = BinaryAssociation(
    name="repository__RepositoryComponent279",
    ends={
        Property(name="repository_pc280", type=pcm_pc_repository_pc_RepositoryComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
providingEntity_ProvidedRole281: BinaryAssociation = BinaryAssociation(
    name="providingEntity_ProvidedRole281",
    ends={
        Property(name="core_pc283", type=pcm_pc_repository_pc_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_pc282", type=entity_pc_InterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
dataType__Parameter284: BinaryAssociation = BinaryAssociation(
    name="dataType__Parameter284",
    ends={
        Property(name="DataType", type=pcm_pc_repository_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_Parameter", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
protocols__Interface308: BinaryAssociation = BinaryAssociation(
    name="protocols__Interface308",
    ends={
        Property(name="pcm_pc_repository_pc_Interface309", type=Protocol, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Protocol", type=pcm_pc_repository_pc_Interface, multiplicity=Multiplicity(1, 1))
    }
)
requiredCharacterisations310: BinaryAssociation = BinaryAssociation(
    name="requiredCharacterisations310",
    ends={
        Property(name="repository_pc311", type=pcm_pc_repository_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="RequiredCharacterisation", type=RequiredCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository__Interface312: BinaryAssociation = BinaryAssociation(
    name="repository__Interface312",
    ends={
        Property(name="repository_pc314", type=pcm_pc_repository_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository313", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
parameter315: BinaryAssociation = BinaryAssociation(
    name="parameter315",
    ends={
        Property(name="Parameter", type=pcm_pc_repository_pc_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_RequiredCharacterisation", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
interface_RequiredCharacterisation316: BinaryAssociation = BinaryAssociation(
    name="interface_RequiredCharacterisation316",
    ends={
        Property(name="repository_pc318", type=pcm_pc_repository_pc_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="Interface317", type=Interface, multiplicity=Multiplicity(0, 1))
    }
)
eventTypes__EventGroup319: BinaryAssociation = BinaryAssociation(
    name="eventTypes__EventGroup319",
    ends={
        Property(name="repository_pc321", type=pcm_pc_repository_pc_EventGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="EventType320", type=EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter__EventType322: BinaryAssociation = BinaryAssociation(
    name="parameter__EventType322",
    ends={
        Property(name="repository_pc324", type=pcm_pc_repository_pc_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter323", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventGroup__EventType325: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventType325",
    ends={
        Property(name="repository_pc327", type=pcm_pc_repository_pc_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="EventGroup326", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
failureTypes__Repository301: BinaryAssociation = BinaryAssociation(
    name="failureTypes__Repository301",
    ends={
        Property(name="reliability_pc302", type=pcm_pc_repository_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="FailureType", type=FailureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes__Repository303: BinaryAssociation = BinaryAssociation(
    name="dataTypes__Repository303",
    ends={
        Property(name="repository_pc305", type=pcm_pc_repository_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="DataType304", type=DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentInterfaces__Interface306: BinaryAssociation = BinaryAssociation(
    name="parentInterfaces__Interface306",
    ends={
        Property(name="Interface307", type=pcm_pc_repository_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_Interface", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
infrastructureSignatures__InfrastructureInterface337: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignatures__InfrastructureInterface337",
    ends={
        Property(name="repository_pc339", type=pcm_pc_repository_pc_InfrastructureInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="InfrastructureSignature338", type=InfrastructureSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterface__InfrastructureRequiredRole340: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__InfrastructureRequiredRole340",
    ends={
        Property(name="InfrastructureInterface341", type=pcm_pc_repository_pc_InfrastructureRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_InfrastructureRequiredRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
requiringEntity_RequiredRole342: BinaryAssociation = BinaryAssociation(
    name="requiringEntity_RequiredRole342",
    ends={
        Property(name="core_pc344", type=pcm_pc_repository_pc_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_pc343", type=entity_pc_InterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
interface__OperationSignature345: BinaryAssociation = BinaryAssociation(
    name="interface__OperationSignature345",
    ends={
        Property(name="repository_pc346", type=pcm_pc_repository_pc_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationInterface", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
parameters__OperationSignature347: BinaryAssociation = BinaryAssociation(
    name="parameters__OperationSignature347",
    ends={
        Property(name="repository_pc349", type=pcm_pc_repository_pc_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter348", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptions__Signature328: BinaryAssociation = BinaryAssociation(
    name="exceptions__Signature328",
    ends={
        Property(name="ExceptionType", type=pcm_pc_repository_pc_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_Signature", type=ExceptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureType329: BinaryAssociation = BinaryAssociation(
    name="failureType329",
    ends={
        Property(name="FailureType331", type=pcm_pc_repository_pc_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_Signature330", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
parameters__InfrastructureSignature332: BinaryAssociation = BinaryAssociation(
    name="parameters__InfrastructureSignature332",
    ends={
        Property(name="repository_pc334", type=pcm_pc_repository_pc_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter333", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureInterface__InfrastructureSignature335: BinaryAssociation = BinaryAssociation(
    name="infrastructureInterface__InfrastructureSignature335",
    ends={
        Property(name="repository_pc336", type=pcm_pc_repository_pc_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="InfrastructureInterface", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
requiredInterface__OperationRequiredRole355: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__OperationRequiredRole355",
    ends={
        Property(name="OperationInterface356", type=pcm_pc_repository_pc_OperationRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_OperationRequiredRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SourceRole357: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SourceRole357",
    ends={
        Property(name="EventGroup358", type=pcm_pc_repository_pc_SourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_SourceRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SinkRole359: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SinkRole359",
    ends={
        Property(name="EventGroup360", type=pcm_pc_repository_pc_SinkRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_SinkRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface__OperationProvidedRole361: BinaryAssociation = BinaryAssociation(
    name="providedInterface__OperationProvidedRole361",
    ends={
        Property(name="OperationInterface362", type=pcm_pc_repository_pc_OperationProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_OperationProvidedRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface__InfrastructureProvidedRole363: BinaryAssociation = BinaryAssociation(
    name="providedInterface__InfrastructureProvidedRole363",
    ends={
        Property(name="InfrastructureInterface364", type=pcm_pc_repository_pc_InfrastructureProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_InfrastructureProvidedRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
returnType__OperationSignature350: BinaryAssociation = BinaryAssociation(
    name="returnType__OperationSignature350",
    ends={
        Property(name="DataType351", type=pcm_pc_repository_pc_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_OperationSignature", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
signatures__OperationInterface352: BinaryAssociation = BinaryAssociation(
    name="signatures__OperationInterface352",
    ends={
        Property(name="repository_pc354", type=pcm_pc_repository_pc_OperationInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationSignature353", type=OperationSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentProvidesComponentTypes365: BinaryAssociation = BinaryAssociation(
    name="parentProvidesComponentTypes365",
    ends={
        Property(name="ProvidesComponentType", type=pcm_pc_repository_pc_CompleteComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_CompleteComponentType", type=ProvidesComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
innerType_CollectionDataType366: BinaryAssociation = BinaryAssociation(
    name="innerType_CollectionDataType366",
    ends={
        Property(name="DataType367", type=pcm_pc_repository_pc_CollectionDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_CollectionDataType", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
parentType_CompositeDataType368: BinaryAssociation = BinaryAssociation(
    name="parentType_CompositeDataType368",
    ends={
        Property(name="CompositeDataType", type=pcm_pc_repository_pc_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 9999))
    }
)
innerDeclaration_CompositeDataType369: BinaryAssociation = BinaryAssociation(
    name="innerDeclaration_CompositeDataType369",
    ends={
        Property(name="repository_pc370", type=pcm_pc_repository_pc_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="InnerDeclaration", type=InnerDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceInterface__ResourceSignature379: BinaryAssociation = BinaryAssociation(
    name="resourceInterface__ResourceSignature379",
    ends={
        Property(name="resourcetype_pc381", type=pcm_pc_resourcetype_pc_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceInterface380", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
hardwareInducedFailureType__ProcessingResourceType382: BinaryAssociation = BinaryAssociation(
    name="hardwareInducedFailureType__ProcessingResourceType382",
    ends={
        Property(name="reliability_pc383", type=pcm_pc_resourcetype_pc_ProcessingResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="HardwareInducedFailureType", type=HardwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
resourceRepository_ResourceType384: BinaryAssociation = BinaryAssociation(
    name="resourceRepository_ResourceType384",
    ends={
        Property(name="resourcetype_pc385", type=pcm_pc_resourcetype_pc_ResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaces__ResourceRepository386: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaces__ResourceRepository386",
    ends={
        Property(name="resourcetype_pc388", type=pcm_pc_resourcetype_pc_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceInterface387", type=ResourceInterface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schedulingPolicies__ResourceRepository389: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicies__ResourceRepository389",
    ends={
        Property(name="resourcetype_pc390", type=pcm_pc_resourcetype_pc_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="SchedulingPolicy", type=SchedulingPolicy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
availableResourceTypes_ResourceRepository391: BinaryAssociation = BinaryAssociation(
    name="availableResourceTypes_ResourceRepository391",
    ends={
        Property(name="resourcetype_pc392", type=pcm_pc_resourcetype_pc_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceType", type=ResourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRepository__SchedulingPolicy393: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__SchedulingPolicy393",
    ends={
        Property(name="resourcetype_pc395", type=pcm_pc_resourcetype_pc_SchedulingPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceRepository394", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
networkInducedFailureType__CommunicationLinkResourceType396: BinaryAssociation = BinaryAssociation(
    name="networkInducedFailureType__CommunicationLinkResourceType396",
    ends={
        Property(name="reliability_pc397", type=pcm_pc_resourcetype_pc_CommunicationLinkResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="NetworkInducedFailureType", type=NetworkInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
datatype_InnerDeclaration371: BinaryAssociation = BinaryAssociation(
    name="datatype_InnerDeclaration371",
    ends={
        Property(name="DataType372", type=pcm_pc_repository_pc_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_InnerDeclaration", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
compositeDataType_InnerDeclaration373: BinaryAssociation = BinaryAssociation(
    name="compositeDataType_InnerDeclaration373",
    ends={
        Property(name="repository_pc375", type=pcm_pc_repository_pc_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="CompositeDataType374", type=CompositeDataType, multiplicity=Multiplicity(0, 1))
    }
)
parameter__ResourceSignature376: BinaryAssociation = BinaryAssociation(
    name="parameter__ResourceSignature376",
    ends={
        Property(name="repository_pc378", type=pcm_pc_resourcetype_pc_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter377", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableCharacterisation_VariableUsage404: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_VariableUsage404",
    ends={
        Property(name="parameter_pc406", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableCharacterisation405", type=VariableCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_VariableUsage407: BinaryAssociation = BinaryAssociation(
    name="userData_VariableUsage407",
    ends={
        Property(name="usagemodel_pc409", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="UserData408", type=UserData, multiplicity=Multiplicity(0, 1))
    }
)
callAction__VariableUsage410: BinaryAssociation = BinaryAssociation(
    name="callAction__VariableUsage410",
    ends={
        Property(name="seff_pc411", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="CallAction", type=CallAction, multiplicity=Multiplicity(0, 1))
    }
)
synchronisationPoint_VariableUsage412: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_VariableUsage412",
    ends={
        Property(name="seff_pc413", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
callReturnAction__VariableUsage414: BinaryAssociation = BinaryAssociation(
    name="callReturnAction__VariableUsage414",
    ends={
        Property(name="seff_pc415", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="CallReturnAction", type=CallReturnAction, multiplicity=Multiplicity(0, 1))
    }
)
setVariableAction_VariableUsage416: BinaryAssociation = BinaryAssociation(
    name="setVariableAction_VariableUsage416",
    ends={
        Property(name="seff_pc417", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="SetVariableAction", type=SetVariableAction, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage418: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage418",
    ends={
        Property(name="qosannotations_pc419", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="SpecifiedOutputParameterAbstraction", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__VariableUsage420: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__VariableUsage420",
    ends={
        Property(name="core_pc422", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc421", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_InputParameterUsage423: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_InputParameterUsage423",
    ends={
        Property(name="usagemodel_pc424", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="EntryLevelSystemCall", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_OutputParameterUsage425: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_OutputParameterUsage425",
    ends={
        Property(name="usagemodel_pc427", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="EntryLevelSystemCall426", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
namedReference__VariableUsage428: BinaryAssociation = BinaryAssociation(
    name="namedReference__VariableUsage428",
    ends={
        Property(name="parameter_pc_pcm_pc_AbstractNamedReference", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_parameter_pc_VariableUsage", type=parameter_pc_pcm_pc_AbstractNamedReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification_VariableCharacterisation429: BinaryAssociation = BinaryAssociation(
    name="specification_VariableCharacterisation429",
    ends={
        Property(name="core_pc431", type=pcm_pc_parameter_pc_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable430", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceRepository__ResourceInterface398: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__ResourceInterface398",
    ends={
        Property(name="resourcetype_pc400", type=pcm_pc_resourcetype_pc_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceRepository399", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
resourceSignatures__ResourceInterface401: BinaryAssociation = BinaryAssociation(
    name="resourceSignatures__ResourceInterface401",
    ends={
        Property(name="resourcetype_pc403", type=pcm_pc_resourcetype_pc_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceSignature402", type=ResourceSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processingResourceType__HardwareInducedFailureType435: BinaryAssociation = BinaryAssociation(
    name="processingResourceType__HardwareInducedFailureType435",
    ends={
        Property(name="resourcetype_pc436", type=pcm_pc_reliability_pc_HardwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcessingResourceType", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
internalFailureOccurrenceDescriptions__SoftwareInducedFailureType437: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__SoftwareInducedFailureType437",
    ends={
        Property(name="reliability_pc438", type=pcm_pc_reliability_pc_SoftwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="InternalFailureOccurrenceDescription", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999))
    }
)
variableUsage_VariableCharacterisation432: BinaryAssociation = BinaryAssociation(
    name="variableUsage_VariableCharacterisation432",
    ends={
        Property(name="parameter_pc434", type=pcm_pc_parameter_pc_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage433", type=VariableUsage, multiplicity=Multiplicity(0, 1))
    }
)
specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription445: BinaryAssociation = BinaryAssociation(
    name="specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription445",
    ends={
        Property(name="qosannotations_pc446", type=pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="qos_reliability_pc", type=qos_reliability_pc_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(0, 1))
    }
)
failureType__ExternalFailureOccurrenceDescription447: BinaryAssociation = BinaryAssociation(
    name="failureType__ExternalFailureOccurrenceDescription447",
    ends={
        Property(name="FailureType448", type=pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription", type=FailureType, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource__ResourceTimeoutFailureType449: BinaryAssociation = BinaryAssociation(
    name="passiveResource__ResourceTimeoutFailureType449",
    ends={
        Property(name="repository_pc451", type=pcm_pc_reliability_pc_ResourceTimeoutFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="PassiveResource450", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
repository__FailureType452: BinaryAssociation = BinaryAssociation(
    name="repository__FailureType452",
    ends={
        Property(name="repository_pc454", type=pcm_pc_reliability_pc_FailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository453", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
internalAction__InternalFailureOccurrenceDescription439: BinaryAssociation = BinaryAssociation(
    name="internalAction__InternalFailureOccurrenceDescription439",
    ends={
        Property(name="seff_pc440", type=pcm_pc_reliability_pc_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="InternalAction", type=InternalAction, multiplicity=Multiplicity(0, 1))
    }
)
softwareInducedFailureType__InternalFailureOccurrenceDescription441: BinaryAssociation = BinaryAssociation(
    name="softwareInducedFailureType__InternalFailureOccurrenceDescription441",
    ends={
        Property(name="reliability_pc442", type=pcm_pc_reliability_pc_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="SoftwareInducedFailureType", type=SoftwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceType__NetworkInducedFailureType443: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType__NetworkInducedFailureType443",
    ends={
        Property(name="resourcetype_pc444", type=pcm_pc_reliability_pc_NetworkInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceType", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
abstractLoopAction_ResourceDemandingBehaviour471: BinaryAssociation = BinaryAssociation(
    name="abstractLoopAction_ResourceDemandingBehaviour471",
    ends={
        Property(name="seff_pc472", type=pcm_pc_seff_pc_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractLoopAction", type=AbstractLoopAction, multiplicity=Multiplicity(0, 1))
    }
)
abstractBranchTransition_ResourceDemandingBehaviour473: BinaryAssociation = BinaryAssociation(
    name="abstractBranchTransition_ResourceDemandingBehaviour473",
    ends={
        Property(name="seff_pc474", type=pcm_pc_seff_pc_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractBranchTransition", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
steps_Behaviour475: BinaryAssociation = BinaryAssociation(
    name="steps_Behaviour475",
    ends={
        Property(name="seff_pc477", type=pcm_pc_seff_pc_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction476", type=AbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceDemand_Action455: BinaryAssociation = BinaryAssociation(
    name="resourceDemand_Action455",
    ends={
        Property(name="seff_pc457", type=pcm_pc_seff_pc_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_pc456", type=seff_performance_pc_ParametricResourceDemand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyBehaviour_Loop478: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop478",
    ends={
        Property(name="seff_pc480", type=pcm_pc_seff_pc_AbstractLoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingBehaviour479", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchAction_AbstractBranchTransition481: BinaryAssociation = BinaryAssociation(
    name="branchAction_AbstractBranchTransition481",
    ends={
        Property(name="seff_pc482", type=pcm_pc_seff_pc_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="BranchAction", type=BranchAction, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureCall__Action458: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__Action458",
    ends={
        Property(name="seff_pc460", type=pcm_pc_seff_pc_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_pc459", type=seff_performance_pc_InfrastructureCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceCall__Action461: BinaryAssociation = BinaryAssociation(
    name="resourceCall__Action461",
    ends={
        Property(name="seff_pc463", type=pcm_pc_seff_pc_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_pc462", type=seff_performance_pc_ResourceCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor_AbstractAction464: BinaryAssociation = BinaryAssociation(
    name="predecessor_AbstractAction464",
    ends={
        Property(name="seff_pc465", type=pcm_pc_seff_pc_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
successor_AbstractAction466: BinaryAssociation = BinaryAssociation(
    name="successor_AbstractAction466",
    ends={
        Property(name="seff_pc468", type=pcm_pc_seff_pc_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction467", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemandingBehaviour_AbstractAction469: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingBehaviour_AbstractAction469",
    ends={
        Property(name="seff_pc470", type=pcm_pc_seff_pc_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingBehaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
branches_Branch486: BinaryAssociation = BinaryAssociation(
    name="branches_Branch486",
    ends={
        Property(name="seff_pc488", type=pcm_pc_seff_pc_BranchAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractBranchTransition487", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputVariableUsages__CallAction489: BinaryAssociation = BinaryAssociation(
    name="inputVariableUsages__CallAction489",
    ends={
        Property(name="parameter_pc491", type=pcm_pc_seff_pc_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage490", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
describedService__SEFF492: BinaryAssociation = BinaryAssociation(
    name="describedService__SEFF492",
    ends={
        Property(name="Signature", type=pcm_pc_seff_pc_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_pc_ServiceEffectSpecification", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
basicComponent_ServiceEffectSpecification493: BinaryAssociation = BinaryAssociation(
    name="basicComponent_ServiceEffectSpecification493",
    ends={
        Property(name="repository_pc495", type=pcm_pc_seff_pc_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BasicComponent494", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
branchBehaviour_BranchTransition483: BinaryAssociation = BinaryAssociation(
    name="branchBehaviour_BranchTransition483",
    ends={
        Property(name="seff_pc485", type=pcm_pc_seff_pc_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingBehaviour484", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceDemandingSEFF_ResourceDemandingInternalBehaviour498: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingSEFF_ResourceDemandingInternalBehaviour498",
    ends={
        Property(name="seff_pc499", type=pcm_pc_seff_pc_ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingSEFF", type=ResourceDemandingSEFF, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_ReleaseAction500: BinaryAssociation = BinaryAssociation(
    name="passiveResource_ReleaseAction500",
    ends={
        Property(name="PassiveResource501", type=pcm_pc_seff_pc_ReleaseAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_pc_ReleaseAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
iterationCount_LoopAction502: BinaryAssociation = BinaryAssociation(
    name="iterationCount_LoopAction502",
    ends={
        Property(name="core_pc504", type=pcm_pc_seff_pc_LoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable503", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
asynchronousForkedBehaviours_ForkAction505: BinaryAssociation = BinaryAssociation(
    name="asynchronousForkedBehaviours_ForkAction505",
    ends={
        Property(name="seff_pc506", type=pcm_pc_seff_pc_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedBehaviour", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronisingBehaviours_ForkAction507: BinaryAssociation = BinaryAssociation(
    name="synchronisingBehaviours_ForkAction507",
    ends={
        Property(name="seff_pc509", type=pcm_pc_seff_pc_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="SynchronisationPoint508", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceDemandingInternalBehaviours496: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingInternalBehaviours496",
    ends={
        Property(name="seff_pc497", type=pcm_pc_seff_pc_ResourceDemandingSEFF, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingInternalBehaviour", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronisationPoint_ForkedBehaviour510: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_ForkedBehaviour510",
    ends={
        Property(name="seff_pc512", type=pcm_pc_seff_pc_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="SynchronisationPoint511", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
forkAction_ForkedBehaivour513: BinaryAssociation = BinaryAssociation(
    name="forkAction_ForkedBehaivour513",
    ends={
        Property(name="seff_pc514", type=pcm_pc_seff_pc_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkAction", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
outputParameterUsage_SynchronisationPoint515: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsage_SynchronisationPoint515",
    ends={
        Property(name="parameter_pc517", type=pcm_pc_seff_pc_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage516", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forkAction_SynchronisationPoint518: BinaryAssociation = BinaryAssociation(
    name="forkAction_SynchronisationPoint518",
    ends={
        Property(name="seff_pc520", type=pcm_pc_seff_pc_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkAction519", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
calledService_ExternalService524: BinaryAssociation = BinaryAssociation(
    name="calledService_ExternalService524",
    ends={
        Property(name="OperationSignature525", type=pcm_pc_seff_pc_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_pc_ExternalCallAction", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
synchronousForkedBehaviours_SynchronisationPoint521: BinaryAssociation = BinaryAssociation(
    name="synchronousForkedBehaviours_SynchronisationPoint521",
    ends={
        Property(name="seff_pc523", type=pcm_pc_seff_pc_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedBehaviour522", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
role_ExternalService526: BinaryAssociation = BinaryAssociation(
    name="role_ExternalService526",
    ends={
        Property(name="OperationRequiredRole528", type=pcm_pc_seff_pc_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_pc_ExternalCallAction527", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
returnVariableUsage__CallReturnAction529: BinaryAssociation = BinaryAssociation(
    name="returnVariableUsage__CallReturnAction529",
    ends={
        Property(name="parameter_pc531", type=pcm_pc_seff_pc_CallReturnAction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage530", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveresource_AcquireAction532: BinaryAssociation = BinaryAssociation(
    name="passiveresource_AcquireAction532",
    ends={
        Property(name="PassiveResource533", type=pcm_pc_seff_pc_AcquireAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_pc_AcquireAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
localVariableUsages_SetVariableAction539: BinaryAssociation = BinaryAssociation(
    name="localVariableUsages_SetVariableAction539",
    ends={
        Property(name="parameter_pc541", type=pcm_pc_seff_pc_SetVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage540", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledResourceDemandingInternalBehaviour542: BinaryAssociation = BinaryAssociation(
    name="calledResourceDemandingInternalBehaviour542",
    ends={
        Property(name="ResourceDemandingInternalBehaviour543", type=pcm_pc_seff_pc_InternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_pc_InternalCallAction", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
parameter_CollectionIteratorAction534: BinaryAssociation = BinaryAssociation(
    name="parameter_CollectionIteratorAction534",
    ends={
        Property(name="Parameter535", type=pcm_pc_seff_pc_CollectionIteratorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_pc_CollectionIteratorAction", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
eventType__EmitEventAction544: BinaryAssociation = BinaryAssociation(
    name="eventType__EmitEventAction544",
    ends={
        Property(name="EventType545", type=pcm_pc_seff_pc_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_pc_EmitEventAction", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EmitEventAction546: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EmitEventAction546",
    ends={
        Property(name="SourceRole548", type=pcm_pc_seff_pc_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_pc_EmitEventAction547", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
branchCondition_GuardedBranchTransition536: BinaryAssociation = BinaryAssociation(
    name="branchCondition_GuardedBranchTransition536",
    ends={
        Property(name="core_pc538", type=pcm_pc_seff_pc_GuardedBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable537", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
internalFailureOccurrenceDescriptions__InternalAction549: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__InternalAction549",
    ends={
        Property(name="reliability_pc551", type=pcm_pc_seff_pc_InternalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="InternalFailureOccurrenceDescription550", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature__InfrastructureCall552: BinaryAssociation = BinaryAssociation(
    name="signature__InfrastructureCall552",
    ends={
        Property(name="InfrastructureSignature553", type=pcm_pc_seff_performance_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_performance_pc_InfrastructureCall", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__InfrastructureCall554: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__InfrastructureCall554",
    ends={
        Property(name="core_pc556", type=pcm_pc_seff_performance_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable555", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action__InfrastructureCall557: BinaryAssociation = BinaryAssociation(
    name="action__InfrastructureCall557",
    ends={
        Property(name="seff_pc558", type=pcm_pc_seff_performance_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractInternalControlFlowAction", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__InfrastructureCall559: BinaryAssociation = BinaryAssociation(
    name="requiredRole__InfrastructureCall559",
    ends={
        Property(name="InfrastructureRequiredRole561", type=pcm_pc_seff_performance_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_performance_pc_InfrastructureCall560", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
action__ResourceCall562: BinaryAssociation = BinaryAssociation(
    name="action__ResourceCall562",
    ends={
        Property(name="seff_pc564", type=pcm_pc_seff_performance_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractInternalControlFlowAction563", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceRequiredRole__ResourceCall565: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRole__ResourceCall565",
    ends={
        Property(name="entity_pc_ResourceRequiredRole566", type=pcm_pc_seff_performance_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_performance_pc_ResourceCall", type=entity_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
signature__ResourceCall567: BinaryAssociation = BinaryAssociation(
    name="signature__ResourceCall567",
    ends={
        Property(name="ResourceSignature569", type=pcm_pc_seff_performance_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_performance_pc_ResourceCall568", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__ResourceCall570: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__ResourceCall570",
    ends={
        Property(name="core_pc572", type=pcm_pc_seff_performance_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable571", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
failureHandlingAlternatives__RecoveryActionBehaviour581: BinaryAssociation = BinaryAssociation(
    name="failureHandlingAlternatives__RecoveryActionBehaviour581",
    ends={
        Property(name="seff_reliability_pc_RecoveryActionBehaviour", type=pcm_pc_seff_reliability_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_reliability_pc_RecoveryActionBehaviour", type=seff_reliability_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999))
    }
)
specification_ParametericResourceDemand573: BinaryAssociation = BinaryAssociation(
    name="specification_ParametericResourceDemand573",
    ends={
        Property(name="core_pc575", type=pcm_pc_seff_performance_pc_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable574", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredResource_ParametricResourceDemand576: BinaryAssociation = BinaryAssociation(
    name="requiredResource_ParametricResourceDemand576",
    ends={
        Property(name="ProcessingResourceType577", type=pcm_pc_seff_performance_pc_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_performance_pc_ParametricResourceDemand", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
action_ParametricResourceDemand578: BinaryAssociation = BinaryAssociation(
    name="action_ParametricResourceDemand578",
    ends={
        Property(name="seff_pc580", type=pcm_pc_seff_performance_pc_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractInternalControlFlowAction579", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
failureTypes_FailureHandlingEntity589: BinaryAssociation = BinaryAssociation(
    name="failureTypes_FailureHandlingEntity589",
    ends={
        Property(name="FailureType590", type=pcm_pc_seff_reliability_pc_FailureHandlingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_reliability_pc_FailureHandlingEntity", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
signature_SpecifiedQoSAnnation591: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedQoSAnnation591",
    ends={
        Property(name="Signature592", type=pcm_pc_qosannotations_pc_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_qosannotations_pc_SpecifiedQoSAnnotation", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedQoSAnnotation593: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedQoSAnnotation593",
    ends={
        Property(name="Role", type=pcm_pc_qosannotations_pc_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_qosannotations_pc_SpecifiedQoSAnnotation594", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
qosAnnotations_SpecifiedQoSAnnotation595: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedQoSAnnotation595",
    ends={
        Property(name="qosannotations_pc596", type=pcm_pc_qosannotations_pc_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
recoveryAction__RecoveryActionBehaviour582: BinaryAssociation = BinaryAssociation(
    name="recoveryAction__RecoveryActionBehaviour582",
    ends={
        Property(name="seff_pc583", type=pcm_pc_seff_reliability_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_reliability_pc", type=seff_reliability_pc_RecoveryAction, multiplicity=Multiplicity(0, 1))
    }
)
primaryBehaviour__RecoveryAction584: BinaryAssociation = BinaryAssociation(
    name="primaryBehaviour__RecoveryAction584",
    ends={
        Property(name="seff_reliability_pc_RecoveryActionBehaviour585", type=pcm_pc_seff_reliability_pc_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_reliability_pc_RecoveryAction", type=seff_reliability_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
recoveryActionBehaviours__RecoveryAction586: BinaryAssociation = BinaryAssociation(
    name="recoveryActionBehaviours__RecoveryAction586",
    ends={
        Property(name="seff_pc588", type=pcm_pc_seff_reliability_pc_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_reliability_pc587", type=seff_reliability_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
role_SpecifiedOutputParameterAbstraction605: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedOutputParameterAbstraction605",
    ends={
        Property(name="Role607", type=pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction606", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
expectedExternalOutputs_SpecifiedOutputParameterAbstraction608: BinaryAssociation = BinaryAssociation(
    name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction608",
    ends={
        Property(name="parameter_pc610", type=pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage609", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qosAnnotations_SpecifiedOutputParameterAbstraction611: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedOutputParameterAbstraction611",
    ends={
        Property(name="qosannotations_pc613", type=pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="QoSAnnotations612", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstractions_QoSAnnotations597: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstractions_QoSAnnotations597",
    ends={
        Property(name="qosannotations_pc599", type=pcm_pc_qosannotations_pc_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="SpecifiedOutputParameterAbstraction598", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
system_QoSAnnotations600: BinaryAssociation = BinaryAssociation(
    name="system_QoSAnnotations600",
    ends={
        Property(name="system_pc", type=pcm_pc_qosannotations_pc_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="System", type=System, multiplicity=Multiplicity(0, 1))
    }
)
specifiedQoSAnnotations_QoSAnnotations601: BinaryAssociation = BinaryAssociation(
    name="specifiedQoSAnnotations_QoSAnnotations601",
    ends={
        Property(name="qosannotations_pc602", type=pcm_pc_qosannotations_pc_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="SpecifiedQoSAnnotation", type=SpecifiedQoSAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature_SpecifiedOutputParameterAbstraction603: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedOutputParameterAbstraction603",
    ends={
        Property(name="Signature604", type=pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
specification_SpecifiedExecutionTime614: BinaryAssociation = BinaryAssociation(
    name="specification_SpecifiedExecutionTime614",
    ends={
        Property(name="core_pc616", type=pcm_pc_qos_performance_pc_SpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable615", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation619: BinaryAssociation = BinaryAssociation(
    name="externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation619",
    ends={
        Property(name="reliability_pc620", type=pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ExternalFailureOccurrenceDescription", type=ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assemblyContext_ComponentSpecifiedExecutionTime617: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ComponentSpecifiedExecutionTime617",
    ends={
        Property(name="composition_pc_AssemblyContext618", type=pcm_pc_qos_performance_pc_ComponentSpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_qos_performance_pc_ComponentSpecifiedExecutionTime", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
qosAnnotations_System621: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_System621",
    ends={
        Property(name="qosannotations_pc623", type=pcm_pc_system_pc_System, multiplicity=Multiplicity(1, 1)),
        Property(name="QoSAnnotations622", type=QoSAnnotations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkingResources__ResourceEnvironment624: BinaryAssociation = BinaryAssociation(
    name="linkingResources__ResourceEnvironment624",
    ends={
        Property(name="resourceenvironment_pc625", type=pcm_pc_resourceenvironment_pc_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="LinkingResource", type=LinkingResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_ResourceEnvironment626: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ResourceEnvironment626",
    ends={
        Property(name="resourceenvironment_pc627", type=pcm_pc_resourceenvironment_pc_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectedResourceContainers_LinkingResource628: BinaryAssociation = BinaryAssociation(
    name="connectedResourceContainers_LinkingResource628",
    ends={
        Property(name="ResourceContainer629", type=pcm_pc_resourceenvironment_pc_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_resourceenvironment_pc_LinkingResource", type=ResourceContainer, multiplicity=Multiplicity(0, 9999))
    }
)
communicationLinkResourceSpecifications_LinkingResource630: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifications_LinkingResource630",
    ends={
        Property(name="resourceenvironment_pc632", type=pcm_pc_resourceenvironment_pc_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceSpecification631", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceEnvironment_LinkingResource633: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_LinkingResource633",
    ends={
        Property(name="resourceenvironment_pc634", type=pcm_pc_resourceenvironment_pc_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceEnvironment", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceSpecifications_ResourceContainer635: BinaryAssociation = BinaryAssociation(
    name="activeResourceSpecifications_ResourceContainer635",
    ends={
        Property(name="resourceenvironment_pc637", type=pcm_pc_resourceenvironment_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcessingResourceSpecification636", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceEnvironment_ResourceContainer638: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_ResourceContainer638",
    ends={
        Property(name="resourceenvironment_pc640", type=pcm_pc_resourceenvironment_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceEnvironment639", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
schedulingPolicy647: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicy647",
    ends={
        Property(name="SchedulingPolicy648", type=pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification", type=SchedulingPolicy, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceType_ActiveResourceSpecification649: BinaryAssociation = BinaryAssociation(
    name="activeResourceType_ActiveResourceSpecification649",
    ends={
        Property(name="ProcessingResourceType651", type=pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification650", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
processingRate_ProcessingResourceSpecification652: BinaryAssociation = BinaryAssociation(
    name="processingRate_ProcessingResourceSpecification652",
    ends={
        Property(name="core_pc654", type=pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable653", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceContainer_ProcessingResourceSpecification655: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ProcessingResourceSpecification655",
    ends={
        Property(name="resourceenvironment_pc657", type=pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer656", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
linkingResource_CommunicationLinkResourceSpecification658: BinaryAssociation = BinaryAssociation(
    name="linkingResource_CommunicationLinkResourceSpecification658",
    ends={
        Property(name="resourceenvironment_pc660", type=pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="LinkingResource659", type=LinkingResource, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceType_CommunicationLinkResourceSpecification661: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType_CommunicationLinkResourceSpecification661",
    ends={
        Property(name="CommunicationLinkResourceType662", type=pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
latency_CommunicationLinkResourceSpecification663: BinaryAssociation = BinaryAssociation(
    name="latency_CommunicationLinkResourceSpecification663",
    ends={
        Property(name="core_pc665", type=pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable664", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throughput_CommunicationLinkResourceSpecification666: BinaryAssociation = BinaryAssociation(
    name="throughput_CommunicationLinkResourceSpecification666",
    ends={
        Property(name="core_pc668", type=pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable667", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nestedResourceContainers__ResourceContainer641: BinaryAssociation = BinaryAssociation(
    name="nestedResourceContainers__ResourceContainer641",
    ends={
        Property(name="resourceenvironment_pc643", type=pcm_pc_resourceenvironment_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer642", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentResourceContainer__ResourceContainer644: BinaryAssociation = BinaryAssociation(
    name="parentResourceContainer__ResourceContainer644",
    ends={
        Property(name="resourceenvironment_pc646", type=pcm_pc_resourceenvironment_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer645", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__AllocationContext675: BinaryAssociation = BinaryAssociation(
    name="eventChannel__AllocationContext675",
    ends={
        Property(name="composition_pc_EventChannel", type=pcm_pc_allocation_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_allocation_pc_AllocationContext676", type=composition_pc_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
targetResourceEnvironment_Allocation677: BinaryAssociation = BinaryAssociation(
    name="targetResourceEnvironment_Allocation677",
    ends={
        Property(name="ResourceEnvironment678", type=pcm_pc_allocation_pc_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_allocation_pc_Allocation", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
system_Allocation679: BinaryAssociation = BinaryAssociation(
    name="system_Allocation679",
    ends={
        Property(name="System681", type=pcm_pc_allocation_pc_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_allocation_pc_Allocation680", type=System, multiplicity=Multiplicity(0, 1))
    }
)
allocationContexts_Allocation682: BinaryAssociation = BinaryAssociation(
    name="allocationContexts_Allocation682",
    ends={
        Property(name="allocation_pc683", type=pcm_pc_allocation_pc_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="AllocationContext", type=AllocationContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_AllocationContext669: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_AllocationContext669",
    ends={
        Property(name="ResourceContainer670", type=pcm_pc_allocation_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_allocation_pc_AllocationContext", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_AllocationContext671: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_AllocationContext671",
    ends={
        Property(name="composition_pc_AssemblyContext673", type=pcm_pc_allocation_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_allocation_pc_AllocationContext672", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
allocation_AllocationContext674: BinaryAssociation = BinaryAssociation(
    name="allocation_AllocationContext674",
    ends={
        Property(name="allocation_pc", type=pcm_pc_allocation_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="Allocation", type=Allocation, multiplicity=Multiplicity(0, 1))
    }
)
completions_CompletionRepository684: BinaryAssociation = BinaryAssociation(
    name="completions_CompletionRepository684",
    ends={
        Property(name="Completion", type=pcm_pc_completions_pc_CompletionRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_completions_pc_CompletionRepository", type=Completion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCommunicationLinkResource_ParametricResourceDemand685: BinaryAssociation = BinaryAssociation(
    name="requiredCommunicationLinkResource_ParametricResourceDemand685",
    ends={
        Property(name="CommunicationLinkResourceType686", type=pcm_pc_completions_pc_NetworkDemandParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_completions_pc_NetworkDemandParametricResourceDemand", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_pcm_pc_core_pc_PCMRandomVariable_RandomVariable = Generalization(general=RandomVariable, specific=pcm_pc_core_pc_PCMRandomVariable)
gen_pcm_pc_entity_pc_ResourceInterfaceRequiringEntity_Entity = Generalization(general=Entity, specific=pcm_pc_entity_pc_ResourceInterfaceRequiringEntity)
gen_pcm_pc_entity_pc_ResourceRequiredRole_Role = Generalization(general=Role, specific=pcm_pc_entity_pc_ResourceRequiredRole)
gen_pcm_pc_entity_pc_ResourceProvidedRole_Role = Generalization(general=Role, specific=pcm_pc_entity_pc_ResourceProvidedRole)
gen_pcm_pc_entity_pc_InterfaceProvidingRequiringEntity_entity_pc_InterfaceProvidingEntity = Generalization(general=entity_pc_InterfaceProvidingEntity, specific=pcm_pc_entity_pc_InterfaceProvidingRequiringEntity)
gen_pcm_pc_entity_pc_InterfaceProvidingRequiringEntity_entity_pc_InterfaceRequiringEntity = Generalization(general=entity_pc_InterfaceRequiringEntity, specific=pcm_pc_entity_pc_InterfaceProvidingRequiringEntity)
gen_pcm_pc_entity_pc_InterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_pc_entity_pc_InterfaceProvidingEntity)
gen_pcm_pc_entity_pc_InterfaceRequiringEntity_entity_pc_Entity = Generalization(general=entity_pc_Entity, specific=pcm_pc_entity_pc_InterfaceRequiringEntity)
gen_pcm_pc_entity_pc_InterfaceRequiringEntity_entity_pc_ResourceInterfaceRequiringEntity = Generalization(general=entity_pc_ResourceInterfaceRequiringEntity, specific=pcm_pc_entity_pc_InterfaceRequiringEntity)
gen_pcm_pc_entity_pc_ResourceInterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_pc_entity_pc_ResourceInterfaceProvidingEntity)
gen_pcm_pc_entity_pc_ComposedProvidingRequiringEntity_composition_pc_ComposedStructure = Generalization(general=composition_pc_ComposedStructure, specific=pcm_pc_entity_pc_ComposedProvidingRequiringEntity)
gen_pcm_pc_entity_pc_ComposedProvidingRequiringEntity_entity_pc_InterfaceProvidingRequiringEntity = Generalization(general=entity_pc_InterfaceProvidingRequiringEntity, specific=pcm_pc_entity_pc_ComposedProvidingRequiringEntity)
gen_pcm_pc_entity_pc_ResourceInterfaceProvidingRequiringEntity_entity_pc_ResourceInterfaceRequiringEntity = Generalization(general=entity_pc_ResourceInterfaceRequiringEntity, specific=pcm_pc_entity_pc_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_pc_entity_pc_ResourceInterfaceProvidingRequiringEntity_entity_pc_ResourceInterfaceProvidingEntity = Generalization(general=entity_pc_ResourceInterfaceProvidingEntity, specific=pcm_pc_entity_pc_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_pc_entity_pc_Entity_Identifier = Generalization(general=Identifier, specific=pcm_pc_entity_pc_Entity)
gen_pcm_pc_entity_pc_Entity_entity_pc_NamedElement = Generalization(general=entity_pc_NamedElement, specific=pcm_pc_entity_pc_Entity)
gen_pcm_pc_composition_pc_DelegationConnector_Connector = Generalization(general=Connector, specific=pcm_pc_composition_pc_DelegationConnector)
gen_pcm_pc_composition_pc_Connector_Entity = Generalization(general=Entity, specific=pcm_pc_composition_pc_Connector)
gen_pcm_pc_composition_pc_ComposedStructure_Entity = Generalization(general=Entity, specific=pcm_pc_composition_pc_ComposedStructure)
gen_pcm_pc_composition_pc_ProvidedDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_composition_pc_ProvidedDelegationConnector)
gen_pcm_pc_composition_pc_EventChannel_Entity = Generalization(general=Entity, specific=pcm_pc_composition_pc_EventChannel)
gen_pcm_pc_composition_pc_EventChannelSourceConnector_Connector = Generalization(general=Connector, specific=pcm_pc_composition_pc_EventChannelSourceConnector)
gen_pcm_pc_composition_pc_EventChannelSinkConnector_Connector = Generalization(general=Connector, specific=pcm_pc_composition_pc_EventChannelSinkConnector)
gen_pcm_pc_composition_pc_AssemblyConnector_Connector = Generalization(general=Connector, specific=pcm_pc_composition_pc_AssemblyConnector)
gen_pcm_pc_composition_pc_RequiredDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_composition_pc_RequiredDelegationConnector)
gen_pcm_pc_composition_pc_SourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_composition_pc_SourceDelegationConnector)
gen_pcm_pc_composition_pc_AssemblyEventConnector_Connector = Generalization(general=Connector, specific=pcm_pc_composition_pc_AssemblyEventConnector)
gen_pcm_pc_composition_pc_RequiredResourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_composition_pc_RequiredResourceDelegationConnector)
gen_pcm_pc_composition_pc_SinkDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_composition_pc_SinkDelegationConnector)
gen_pcm_pc_composition_pc_AssemblyContext_Entity = Generalization(general=Entity, specific=pcm_pc_composition_pc_AssemblyContext)
gen_pcm_pc_composition_pc_AssemblyInfrastructureConnector_Connector = Generalization(general=Connector, specific=pcm_pc_composition_pc_AssemblyInfrastructureConnector)
gen_pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector)
gen_pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector)
gen_pcm_pc_usagemodel_pc_EntryLevelSystemCall_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_usagemodel_pc_EntryLevelSystemCall)
gen_pcm_pc_usagemodel_pc_UsageScenario_Entity = Generalization(general=Entity, specific=pcm_pc_usagemodel_pc_UsageScenario)
gen_pcm_pc_usagemodel_pc_Branch_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_usagemodel_pc_Branch)
gen_pcm_pc_usagemodel_pc_AbstractUserAction_Entity = Generalization(general=Entity, specific=pcm_pc_usagemodel_pc_AbstractUserAction)
gen_pcm_pc_usagemodel_pc_ScenarioBehaviour_Entity = Generalization(general=Entity, specific=pcm_pc_usagemodel_pc_ScenarioBehaviour)
gen_pcm_pc_usagemodel_pc_Loop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_usagemodel_pc_Loop)
gen_pcm_pc_usagemodel_pc_Stop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_usagemodel_pc_Stop)
gen_pcm_pc_usagemodel_pc_Start_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_usagemodel_pc_Start)
gen_pcm_pc_usagemodel_pc_OpenWorkload_Workload = Generalization(general=Workload, specific=pcm_pc_usagemodel_pc_OpenWorkload)
gen_pcm_pc_repository_pc_PassiveResource_Entity = Generalization(general=Entity, specific=pcm_pc_repository_pc_PassiveResource)
gen_pcm_pc_repository_pc_BasicComponent_ImplementationComponentType = Generalization(general=ImplementationComponentType, specific=pcm_pc_repository_pc_BasicComponent)
gen_pcm_pc_usagemodel_pc_Delay_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_usagemodel_pc_Delay)
gen_pcm_pc_usagemodel_pc_ClosedWorkload_Workload = Generalization(general=Workload, specific=pcm_pc_usagemodel_pc_ClosedWorkload)
gen_pcm_pc_repository_pc_ImplementationComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_pc_repository_pc_ImplementationComponentType)
gen_pcm_pc_repository_pc_Repository_Entity = Generalization(general=Entity, specific=pcm_pc_repository_pc_Repository)
gen_pcm_pc_repository_pc_RepositoryComponent_InterfaceProvidingRequiringEntity = Generalization(general=InterfaceProvidingRequiringEntity, specific=pcm_pc_repository_pc_RepositoryComponent)
gen_pcm_pc_repository_pc_ProvidedRole_Role = Generalization(general=Role, specific=pcm_pc_repository_pc_ProvidedRole)
gen_pcm_pc_repository_pc_EventGroup_Interface = Generalization(general=Interface, specific=pcm_pc_repository_pc_EventGroup)
gen_pcm_pc_repository_pc_EventType_Signature = Generalization(general=Signature, specific=pcm_pc_repository_pc_EventType)
gen_pcm_pc_repository_pc_Signature_Entity = Generalization(general=Entity, specific=pcm_pc_repository_pc_Signature)
gen_pcm_pc_repository_pc_Interface_Entity = Generalization(general=Entity, specific=pcm_pc_repository_pc_Interface)
gen_pcm_pc_repository_pc_InfrastructureRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_pc_repository_pc_InfrastructureRequiredRole)
gen_pcm_pc_repository_pc_RequiredRole_Role = Generalization(general=Role, specific=pcm_pc_repository_pc_RequiredRole)
gen_pcm_pc_repository_pc_OperationSignature_Signature = Generalization(general=Signature, specific=pcm_pc_repository_pc_OperationSignature)
gen_pcm_pc_repository_pc_InfrastructureSignature_Signature = Generalization(general=Signature, specific=pcm_pc_repository_pc_InfrastructureSignature)
gen_pcm_pc_repository_pc_InfrastructureInterface_Interface = Generalization(general=Interface, specific=pcm_pc_repository_pc_InfrastructureInterface)
gen_pcm_pc_repository_pc_OperationRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_pc_repository_pc_OperationRequiredRole)
gen_pcm_pc_repository_pc_SourceRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_pc_repository_pc_SourceRole)
gen_pcm_pc_repository_pc_SinkRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_pc_repository_pc_SinkRole)
gen_pcm_pc_repository_pc_OperationProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_pc_repository_pc_OperationProvidedRole)
gen_pcm_pc_repository_pc_InfrastructureProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_pc_repository_pc_InfrastructureProvidedRole)
gen_pcm_pc_repository_pc_OperationInterface_Interface = Generalization(general=Interface, specific=pcm_pc_repository_pc_OperationInterface)
gen_pcm_pc_repository_pc_ProvidesComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_pc_repository_pc_ProvidesComponentType)
gen_pcm_pc_repository_pc_CompositeComponent_entity_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_ComposedProvidingRequiringEntity, specific=pcm_pc_repository_pc_CompositeComponent)
gen_pcm_pc_repository_pc_CompositeComponent_repository_pc_ImplementationComponentType = Generalization(general=repository_pc_ImplementationComponentType, specific=pcm_pc_repository_pc_CompositeComponent)
gen_pcm_pc_repository_pc_CompleteComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_pc_repository_pc_CompleteComponentType)
gen_pcm_pc_repository_pc_CollectionDataType_entity_pc_Entity = Generalization(general=entity_pc_Entity, specific=pcm_pc_repository_pc_CollectionDataType)
gen_pcm_pc_repository_pc_CollectionDataType_repository_pc_DataType = Generalization(general=repository_pc_DataType, specific=pcm_pc_repository_pc_CollectionDataType)
gen_pcm_pc_repository_pc_CompositeDataType_entity_pc_Entity = Generalization(general=entity_pc_Entity, specific=pcm_pc_repository_pc_CompositeDataType)
gen_pcm_pc_repository_pc_CompositeDataType_repository_pc_DataType = Generalization(general=repository_pc_DataType, specific=pcm_pc_repository_pc_CompositeDataType)
gen_pcm_pc_repository_pc_InnerDeclaration_NamedElement = Generalization(general=NamedElement, specific=pcm_pc_repository_pc_InnerDeclaration)
gen_pcm_pc_repository_pc_PrimitiveDataType_DataType = Generalization(general=DataType, specific=pcm_pc_repository_pc_PrimitiveDataType)
gen_pcm_pc_resourcetype_pc_ProcessingResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_pc_resourcetype_pc_ProcessingResourceType)
gen_pcm_pc_resourcetype_pc_ResourceType_entity_pc_Entity = Generalization(general=entity_pc_Entity, specific=pcm_pc_resourcetype_pc_ResourceType)
gen_pcm_pc_resourcetype_pc_ResourceType_UnitCarryingElement = Generalization(general=UnitCarryingElement, specific=pcm_pc_resourcetype_pc_ResourceType)
gen_pcm_pc_resourcetype_pc_ResourceType_entity_pc_ResourceInterfaceProvidingEntity = Generalization(general=entity_pc_ResourceInterfaceProvidingEntity, specific=pcm_pc_resourcetype_pc_ResourceType)
gen_pcm_pc_resourcetype_pc_SchedulingPolicy_Entity = Generalization(general=Entity, specific=pcm_pc_resourcetype_pc_SchedulingPolicy)
gen_pcm_pc_resourcetype_pc_CommunicationLinkResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_pc_resourcetype_pc_CommunicationLinkResourceType)
gen_pcm_pc_resourcetype_pc_ResourceInterface_Entity = Generalization(general=Entity, specific=pcm_pc_resourcetype_pc_ResourceInterface)
gen_pcm_pc_repository_pc_Role_Entity = Generalization(general=Entity, specific=pcm_pc_repository_pc_Role)
gen_pcm_pc_resourcetype_pc_ResourceSignature_Entity = Generalization(general=Entity, specific=pcm_pc_resourcetype_pc_ResourceSignature)
gen_pcm_pc_reliability_pc_HardwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_pc_reliability_pc_HardwareInducedFailureType)
gen_pcm_pc_reliability_pc_SoftwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_pc_reliability_pc_SoftwareInducedFailureType)
gen_pcm_pc_parameter_pc_CharacterisedVariable_Variable = Generalization(general=Variable, specific=pcm_pc_parameter_pc_CharacterisedVariable)
gen_pcm_pc_reliability_pc_InternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_pc_reliability_pc_InternalFailureOccurrenceDescription)
gen_pcm_pc_reliability_pc_ResourceTimeoutFailureType_SoftwareInducedFailureType = Generalization(general=SoftwareInducedFailureType, specific=pcm_pc_reliability_pc_ResourceTimeoutFailureType)
gen_pcm_pc_reliability_pc_FailureType_Entity = Generalization(general=Entity, specific=pcm_pc_reliability_pc_FailureType)
gen_pcm_pc_seff_pc_StopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_seff_pc_StopAction)
gen_pcm_pc_reliability_pc_NetworkInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_pc_reliability_pc_NetworkInducedFailureType)
gen_pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription)
gen_pcm_pc_seff_pc_AbstractInternalControlFlowAction_AbstractAction = Generalization(general=AbstractAction, specific=pcm_pc_seff_pc_AbstractInternalControlFlowAction)
gen_pcm_pc_seff_pc_AbstractLoopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_seff_pc_AbstractLoopAction)
gen_pcm_pc_seff_pc_AbstractBranchTransition_Entity = Generalization(general=Entity, specific=pcm_pc_seff_pc_AbstractBranchTransition)
gen_pcm_pc_seff_pc_AbstractAction_Entity = Generalization(general=Entity, specific=pcm_pc_seff_pc_AbstractAction)
gen_pcm_pc_seff_pc_ResourceDemandingBehaviour_Identifier = Generalization(general=Identifier, specific=pcm_pc_seff_pc_ResourceDemandingBehaviour)
gen_pcm_pc_seff_pc_StartAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_seff_pc_StartAction)
gen_pcm_pc_seff_pc_ResourceDemandingSEFF_Identifier = Generalization(general=Identifier, specific=pcm_pc_seff_pc_ResourceDemandingSEFF)
gen_pcm_pc_seff_pc_ResourceDemandingSEFF_seff_pc_ServiceEffectSpecification = Generalization(general=seff_pc_ServiceEffectSpecification, specific=pcm_pc_seff_pc_ResourceDemandingSEFF)
gen_pcm_pc_seff_pc_ResourceDemandingSEFF_seff_pc_ResourceDemandingBehaviour = Generalization(general=seff_pc_ResourceDemandingBehaviour, specific=pcm_pc_seff_pc_ResourceDemandingSEFF)
gen_pcm_pc_seff_pc_BranchAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_seff_pc_BranchAction)
gen_pcm_pc_seff_pc_ReleaseAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_seff_pc_ReleaseAction)
gen_pcm_pc_seff_pc_LoopAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_pc_seff_pc_LoopAction)
gen_pcm_pc_seff_pc_ForkAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_seff_pc_ForkAction)
gen_pcm_pc_seff_pc_ForkedBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_pc_seff_pc_ForkedBehaviour)
gen_pcm_pc_seff_pc_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_pc_seff_pc_ResourceDemandingInternalBehaviour)
gen_pcm_pc_seff_pc_ExternalCallAction_seff_pc_AbstractAction = Generalization(general=seff_pc_AbstractAction, specific=pcm_pc_seff_pc_ExternalCallAction)
gen_pcm_pc_seff_pc_ExternalCallAction_seff_pc_CallReturnAction = Generalization(general=seff_pc_CallReturnAction, specific=pcm_pc_seff_pc_ExternalCallAction)
gen_pcm_pc_seff_pc_ExternalCallAction_seff_reliability_pc_FailureHandlingEntity = Generalization(general=seff_reliability_pc_FailureHandlingEntity, specific=pcm_pc_seff_pc_ExternalCallAction)
gen_pcm_pc_seff_pc_CallReturnAction_CallAction = Generalization(general=CallAction, specific=pcm_pc_seff_pc_CallReturnAction)
gen_pcm_pc_seff_pc_ProbabilisticBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_pc_seff_pc_ProbabilisticBranchTransition)
gen_pcm_pc_seff_pc_AcquireAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_seff_pc_AcquireAction)
gen_pcm_pc_seff_pc_CollectionIteratorAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_pc_seff_pc_CollectionIteratorAction)
gen_pcm_pc_seff_pc_SetVariableAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_seff_pc_SetVariableAction)
gen_pcm_pc_seff_pc_InternalCallAction_seff_pc_CallAction = Generalization(general=seff_pc_CallAction, specific=pcm_pc_seff_pc_InternalCallAction)
gen_pcm_pc_seff_pc_InternalCallAction_seff_pc_AbstractInternalControlFlowAction = Generalization(general=seff_pc_AbstractInternalControlFlowAction, specific=pcm_pc_seff_pc_InternalCallAction)
gen_pcm_pc_seff_pc_EmitEventAction_seff_pc_AbstractAction = Generalization(general=seff_pc_AbstractAction, specific=pcm_pc_seff_pc_EmitEventAction)
gen_pcm_pc_seff_pc_EmitEventAction_seff_pc_CallAction = Generalization(general=seff_pc_CallAction, specific=pcm_pc_seff_pc_EmitEventAction)
gen_pcm_pc_seff_pc_GuardedBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_pc_seff_pc_GuardedBranchTransition)
gen_pcm_pc_seff_pc_InternalAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_seff_pc_InternalAction)
gen_pcm_pc_seff_performance_pc_ResourceCall_CallAction = Generalization(general=CallAction, specific=pcm_pc_seff_performance_pc_ResourceCall)
gen_pcm_pc_seff_performance_pc_InfrastructureCall_CallAction = Generalization(general=CallAction, specific=pcm_pc_seff_performance_pc_InfrastructureCall)
gen_pcm_pc_seff_reliability_pc_RecoveryActionBehaviour_seff_reliability_pc_FailureHandlingEntity = Generalization(general=seff_reliability_pc_FailureHandlingEntity, specific=pcm_pc_seff_reliability_pc_RecoveryActionBehaviour)
gen_pcm_pc_seff_reliability_pc_RecoveryActionBehaviour_seff_pc_ResourceDemandingBehaviour = Generalization(general=seff_pc_ResourceDemandingBehaviour, specific=pcm_pc_seff_reliability_pc_RecoveryActionBehaviour)
gen_pcm_pc_seff_reliability_pc_RecoveryAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_seff_reliability_pc_RecoveryAction)
gen_pcm_pc_seff_reliability_pc_FailureHandlingEntity_Entity = Generalization(general=Entity, specific=pcm_pc_seff_reliability_pc_FailureHandlingEntity)
gen_pcm_pc_qos_performance_pc_SystemSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_pc_qos_performance_pc_SystemSpecifiedExecutionTime)
gen_pcm_pc_qos_performance_pc_SpecifiedExecutionTime_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_pc_qos_performance_pc_SpecifiedExecutionTime)
gen_pcm_pc_qosannotations_pc_QoSAnnotations_Entity = Generalization(general=Entity, specific=pcm_pc_qosannotations_pc_QoSAnnotations)
gen_pcm_pc_qos_performance_pc_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_pc_qos_performance_pc_ComponentSpecifiedExecutionTime)
gen_pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation)
gen_pcm_pc_resourceenvironment_pc_ResourceEnvironment_NamedElement = Generalization(general=NamedElement, specific=pcm_pc_resourceenvironment_pc_ResourceEnvironment)
gen_pcm_pc_resourceenvironment_pc_LinkingResource_Entity = Generalization(general=Entity, specific=pcm_pc_resourceenvironment_pc_LinkingResource)
gen_pcm_pc_resourceenvironment_pc_ResourceContainer_Entity = Generalization(general=Entity, specific=pcm_pc_resourceenvironment_pc_ResourceContainer)
gen_pcm_pc_system_pc_System_entity_pc_Entity = Generalization(general=entity_pc_Entity, specific=pcm_pc_system_pc_System)
gen_pcm_pc_system_pc_System_entity_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_ComposedProvidingRequiringEntity, specific=pcm_pc_system_pc_System)
gen_pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification)
gen_pcm_pc_allocation_pc_AllocationContext_Entity = Generalization(general=Entity, specific=pcm_pc_allocation_pc_AllocationContext)
gen_pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification)
gen_pcm_pc_allocation_pc_Allocation_Entity = Generalization(general=Entity, specific=pcm_pc_allocation_pc_Allocation)
gen_pcm_pc_subsystem_pc_SubSystem_entity_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_ComposedProvidingRequiringEntity, specific=pcm_pc_subsystem_pc_SubSystem)
gen_pcm_pc_subsystem_pc_SubSystem_repository_pc_RepositoryComponent = Generalization(general=repository_pc_RepositoryComponent, specific=pcm_pc_subsystem_pc_SubSystem)
gen_pcm_pc_completions_pc_Completion_entity_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_ComposedProvidingRequiringEntity, specific=pcm_pc_completions_pc_Completion)
gen_pcm_pc_completions_pc_Completion_repository_pc_ImplementationComponentType = Generalization(general=repository_pc_ImplementationComponentType, specific=pcm_pc_completions_pc_Completion)
gen_pcm_pc_completions_pc_DelegatingExternalCallAction_ExternalCallAction = Generalization(general=ExternalCallAction, specific=pcm_pc_completions_pc_DelegatingExternalCallAction)
gen_pcm_pc_completions_pc_NetworkDemandParametricResourceDemand_ParametricResourceDemand = Generalization(general=ParametricResourceDemand, specific=pcm_pc_completions_pc_NetworkDemandParametricResourceDemand)

# Domain Model
domain_model = DomainModel(
    name="pcm_pc",
    types={pcm_pc_DummyClass, pcm_pc_Pointcut, pcm_pc_EObject, pcm_pc_core_pc_PCMRandomVariable, RandomVariable, composition_pc_AssemblyEventConnector, ClosedWorkload, PassiveResource, VariableCharacterisation, seff_performance_pc_InfrastructureCall, seff_performance_pc_ResourceCall, seff_performance_pc_ParametricResourceDemand, LoopAction, GuardedBranchTransition, qos_performance_pc_SpecifiedExecutionTime, composition_pc_EventChannelSinkConnector, pcm_pc_entity_pc_ResourceInterfaceRequiringEntity, entity_pc_ResourceRequiredRole, pcm_pc_entity_pc_ResourceRequiredRole, Loop, OpenWorkload, Delay, CommunicationLinkResourceSpecification, ProcessingResourceSpecification, pcm_pc_entity_pc_ResourceProvidedRole, Role, entity_pc_ResourceInterfaceProvidingEntity, ResourceInterface, pcm_pc_entity_pc_InterfaceProvidingRequiringEntity, entity_pc_InterfaceProvidingEntity, entity_pc_InterfaceRequiringEntity, pcm_pc_entity_pc_InterfaceProvidingEntity, Entity, ProvidedRole, pcm_pc_entity_pc_InterfaceRequiringEntity, entity_pc_Entity, entity_pc_ResourceInterfaceRequiringEntity, RequiredRole, pcm_pc_entity_pc_ResourceInterfaceProvidingEntity, entity_pc_ResourceProvidedRole, pcm_pc_entity_pc_ComposedProvidingRequiringEntity, composition_pc_ComposedStructure, entity_pc_InterfaceProvidingRequiringEntity, pcm_pc_entity_pc_NamedElement, pcm_pc_entity_pc_ResourceInterfaceProvidingRequiringEntity, pcm_pc_entity_pc_Entity, Identifier, entity_pc_NamedElement, pcm_pc_composition_pc_DelegationConnector, Connector, pcm_pc_composition_pc_Connector, pcm_pc_composition_pc_ComposedStructure, pcm_pc_composition_pc_ProvidedDelegationConnector, DelegationConnector, composition_pc_AssemblyContext, composition_pc_ResourceRequiredDelegationConnector, composition_pc_EventChannel, composition_pc_Connector, pcm_pc_composition_pc_ResourceRequiredDelegationConnector, pcm_pc_composition_pc_EventChannel, EventGroup, composition_pc_EventChannelSourceConnector, pcm_pc_composition_pc_EventChannelSourceConnector, SourceRole, pcm_pc_composition_pc_EventChannelSinkConnector, SinkRole, PCMRandomVariable, OperationRequiredRole, pcm_pc_composition_pc_AssemblyConnector, OperationProvidedRole, pcm_pc_composition_pc_RequiredDelegationConnector, pcm_pc_composition_pc_SourceDelegationConnector, pcm_pc_composition_pc_AssemblyEventConnector, pcm_pc_composition_pc_RequiredResourceDelegationConnector, pcm_pc_composition_pc_SinkDelegationConnector, pcm_pc_composition_pc_AssemblyContext, RepositoryComponent, VariableUsage, pcm_pc_composition_pc_AssemblyInfrastructureConnector, InfrastructureProvidedRole, InfrastructureRequiredRole, pcm_pc_usagemodel_pc_Workload, pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector, pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector, pcm_pc_usagemodel_pc_UsageModel, UserData, pcm_pc_usagemodel_pc_EntryLevelSystemCall, AbstractUserAction, OperationSignature, UsageScenario, pcm_pc_usagemodel_pc_UsageScenario, UsageModel, ScenarioBehaviour, Workload, pcm_pc_usagemodel_pc_UserData, BranchTransition, pcm_pc_usagemodel_pc_BranchTransition, Branch, pcm_pc_usagemodel_pc_Branch, pcm_pc_usagemodel_pc_AbstractUserAction, pcm_pc_usagemodel_pc_ScenarioBehaviour, pcm_pc_usagemodel_pc_Loop, pcm_pc_usagemodel_pc_Stop, pcm_pc_usagemodel_pc_Start, pcm_pc_usagemodel_pc_OpenWorkload, pcm_pc_repository_pc_PassiveResource, BasicComponent, ResourceTimeoutFailureType, pcm_pc_repository_pc_BasicComponent, ImplementationComponentType, pcm_pc_usagemodel_pc_Delay, pcm_pc_usagemodel_pc_ClosedWorkload, pcm_pc_repository_pc_ImplementationComponentType, CompleteComponentType, ServiceEffectSpecification, EventType, ResourceSignature, pcm_pc_repository_pc_DataType, pcm_pc_repository_pc_Repository, Interface, FailureType, pcm_pc_repository_pc_RepositoryComponent, InterfaceProvidingRequiringEntity, Repository, pcm_pc_repository_pc_ProvidedRole, pcm_pc_repository_pc_Parameter, DataType, InfrastructureSignature, RequiredCharacterisation, pcm_pc_repository_pc_RequiredCharacterisation, Parameter_, pcm_pc_repository_pc_EventGroup, pcm_pc_repository_pc_EventType, Signature, pcm_pc_repository_pc_Signature, pcm_pc_repository_pc_Interface, Protocol, pcm_pc_repository_pc_InfrastructureRequiredRole, pcm_pc_repository_pc_RequiredRole, pcm_pc_repository_pc_OperationSignature, OperationInterface, ExceptionType, pcm_pc_repository_pc_ExceptionType, pcm_pc_repository_pc_InfrastructureSignature, InfrastructureInterface, pcm_pc_repository_pc_InfrastructureInterface, pcm_pc_repository_pc_OperationRequiredRole, pcm_pc_repository_pc_SourceRole, pcm_pc_repository_pc_SinkRole, pcm_pc_repository_pc_OperationProvidedRole, pcm_pc_repository_pc_InfrastructureProvidedRole, pcm_pc_repository_pc_OperationInterface, ProvidesComponentType, pcm_pc_repository_pc_ProvidesComponentType, pcm_pc_repository_pc_CompositeComponent, entity_pc_ComposedProvidingRequiringEntity, repository_pc_ImplementationComponentType, pcm_pc_repository_pc_CompleteComponentType, pcm_pc_repository_pc_CollectionDataType, repository_pc_DataType, pcm_pc_repository_pc_CompositeDataType, CompositeDataType, InnerDeclaration, pcm_pc_repository_pc_InnerDeclaration, NamedElement, pcm_pc_repository_pc_PrimitiveDataType, pcm_pc_resourcetype_pc_ProcessingResourceType, ResourceType, HardwareInducedFailureType, pcm_pc_resourcetype_pc_ResourceType, UnitCarryingElement, ResourceRepository, pcm_pc_resourcetype_pc_ResourceRepository, SchedulingPolicy, pcm_pc_resourcetype_pc_SchedulingPolicy, pcm_pc_resourcetype_pc_CommunicationLinkResourceType, NetworkInducedFailureType, pcm_pc_resourcetype_pc_ResourceInterface, pcm_pc_repository_pc_Role, pcm_pc_resourcetype_pc_ResourceSignature, CallAction, SynchronisationPoint, CallReturnAction, SetVariableAction, SpecifiedOutputParameterAbstraction, EntryLevelSystemCall, parameter_pc_pcm_pc_AbstractNamedReference, pcm_pc_parameter_pc_VariableCharacterisation, pcm_pc_protocol_pc_Protocol, pcm_pc_parameter_pc_VariableUsage, pcm_pc_reliability_pc_FailureOccurrenceDescription, pcm_pc_reliability_pc_HardwareInducedFailureType, ProcessingResourceType, pcm_pc_reliability_pc_SoftwareInducedFailureType, InternalFailureOccurrenceDescription, pcm_pc_parameter_pc_CharacterisedVariable, Variable, InternalAction, pcm_pc_reliability_pc_InternalFailureOccurrenceDescription, FailureOccurrenceDescription, qos_reliability_pc_SpecifiedReliabilityAnnotation, pcm_pc_reliability_pc_ResourceTimeoutFailureType, pcm_pc_reliability_pc_FailureType, pcm_pc_seff_pc_StopAction, AbstractInternalControlFlowAction, SoftwareInducedFailureType, pcm_pc_reliability_pc_NetworkInducedFailureType, CommunicationLinkResourceType, pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription, AbstractLoopAction, pcm_pc_seff_pc_AbstractInternalControlFlowAction, AbstractAction, AbstractBranchTransition, pcm_pc_seff_pc_AbstractLoopAction, pcm_pc_seff_pc_AbstractBranchTransition, BranchAction, pcm_pc_seff_pc_AbstractAction, ResourceDemandingBehaviour, pcm_pc_seff_pc_ResourceDemandingBehaviour, pcm_pc_seff_pc_CallAction, pcm_pc_seff_pc_StartAction, pcm_pc_seff_pc_ServiceEffectSpecification, pcm_pc_seff_pc_ResourceDemandingSEFF, seff_pc_ServiceEffectSpecification, seff_pc_ResourceDemandingBehaviour, pcm_pc_seff_pc_BranchAction, ResourceDemandingSEFF, pcm_pc_seff_pc_ReleaseAction, pcm_pc_seff_pc_LoopAction, pcm_pc_seff_pc_ForkAction, ForkedBehaviour, ResourceDemandingInternalBehaviour, pcm_pc_seff_pc_ForkedBehaviour, pcm_pc_seff_pc_ResourceDemandingInternalBehaviour, ForkAction, pcm_pc_seff_pc_SynchronisationPoint, pcm_pc_seff_pc_ExternalCallAction, seff_pc_AbstractAction, seff_pc_CallReturnAction, seff_reliability_pc_FailureHandlingEntity, pcm_pc_seff_pc_CallReturnAction, pcm_pc_seff_pc_ProbabilisticBranchTransition, pcm_pc_seff_pc_AcquireAction, pcm_pc_seff_pc_CollectionIteratorAction, pcm_pc_seff_pc_SetVariableAction, pcm_pc_seff_pc_InternalCallAction, seff_pc_CallAction, seff_pc_AbstractInternalControlFlowAction, pcm_pc_seff_pc_EmitEventAction, pcm_pc_seff_pc_GuardedBranchTransition, pcm_pc_seff_pc_InternalAction, pcm_pc_seff_performance_pc_ResourceCall, pcm_pc_seff_performance_pc_InfrastructureCall, pcm_pc_seff_performance_pc_ParametricResourceDemand, seff_reliability_pc_RecoveryActionBehaviour, pcm_pc_seff_reliability_pc_RecoveryActionBehaviour, pcm_pc_qosannotations_pc_SpecifiedQoSAnnotation, QoSAnnotations, seff_reliability_pc_RecoveryAction, pcm_pc_seff_reliability_pc_RecoveryAction, pcm_pc_seff_reliability_pc_FailureHandlingEntity, pcm_pc_qos_performance_pc_SystemSpecifiedExecutionTime, SpecifiedExecutionTime, pcm_pc_qos_performance_pc_SpecifiedExecutionTime, pcm_pc_qosannotations_pc_QoSAnnotations, System, SpecifiedQoSAnnotation, pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction, ExternalFailureOccurrenceDescription, pcm_pc_qos_performance_pc_ComponentSpecifiedExecutionTime, pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation, pcm_pc_resourceenvironment_pc_ResourceEnvironment, LinkingResource, ResourceContainer, pcm_pc_resourceenvironment_pc_LinkingResource, ResourceEnvironment, pcm_pc_resourceenvironment_pc_ResourceContainer, pcm_pc_system_pc_System, pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification, pcm_pc_allocation_pc_AllocationContext, pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification, pcm_pc_allocation_pc_Allocation, AllocationContext, pcm_pc_subsystem_pc_SubSystem, repository_pc_RepositoryComponent, pcm_pc_completions_pc_Completion, Allocation, pcm_pc_completions_pc_CompletionRepository, Completion, pcm_pc_completions_pc_DelegatingExternalCallAction, ExternalCallAction, pcm_pc_completions_pc_NetworkDemandParametricResourceDemand, ParametricResourceDemand, ParameterModifier, ComponentType, PrimitiveTypeEnum, VariableCharacterisationType},
    associations={children0, eventChannelSinkConnector__FilterCondition16, assemblyEventConnector__FilterCondition17, closedWorkload_PCMRandomVariable1, passiveResource_capacity_PCMRandomVariable2, variableCharacterisation_Specification3, infrastructureCall__PCMRandomVariable4, resourceCall__PCMRandomVariable5, parametricResourceDemand_PCMRandomVariable8, loopAction_PCMRandomVariable11, guardedBranchTransition_PCMRandomVariable13, specifiedExecutionTime_PCMRandomVariable15, resourceRequiredRoles__ResourceInterfaceRequiringEntity39, requiredResourceInterface__ResourceRequiredRole42, loop_LoopIteration20, openWorkload_PCMRandomVariable22, delay_TimeSpecification24, communicationLinkResourceSpecifcation_throughput_PCMRandomVariable26, processingResourceSpecification_processingRate_PCMRandomVariable27, communicationLinkResourceSpecification_latency_PCMRandomVariable29, resourceInterfaceProvidingEntity__ResourceProvidedRole32, providedResourceInterface__ResourceProvidedRole34, providedRoles_InterfaceProvidingEntity35, requiredRoles_InterfaceRequiringEntity37, resourceInterfaceRequiringEntity__ResourceRequiredRole44, resourceProvidedRoles__ResourceInterfaceProvidingEntity47, parentStructure__Connector50, assemblyContext__EventChannelSinkConnector91, eventChannel__EventChannelSinkConnector94, assemblyContexts__ComposedStructure53, resourceRequiredDelegationConnectors_ComposedStructure56, eventChannel__ComposedStructure59, connectors__ComposedStructure62, innerResourceRequiredRole_ResourceRequiredDelegationConnector65, outerResourceRequiredRole_ResourceRequiredDelegationConnector66, parentStructure_ResourceRequiredDelegationConnector69, eventGroup__EventChannel72, eventChannelSourceConnector__EventChannel73, eventChannelSinkConnector__EventChannel76, parentStructure__EventChannel79, sourceRole__EventChannelSourceRole82, assemblyContext__EventChannelSourceConnector83, eventChannel__EventChannelSourceConnector85, sinkRole__EventChannelSinkConnector88, filterCondition__EventChannelSinkConnector89, innerRequiredRole_RequiredDelegationConnector104, outerRequiredRole_RequiredDelegationConnector105, assemblyContext_RequiredDelegationConnector108, innerProvidedRole_ProvidedDelegationConnector97, outerProvidedRole_ProvidedDelegationConnector98, assemblyContext_ProvidedDelegationConnector101, filterCondition__AssemblyEventConnector133, innerSourceRole__SourceRole136, outerSourceRole__SourceRole138, assemblyContext__SourceDelegationConnector141, requiringAssemblyContext_AssemblyConnector111, providingAssemblyContext_AssemblyConnector113, providedRole_AssemblyConnector116, requiredRole_AssemblyConnector119, sinkRole__AssemblyEventConnector122, sourceRole__AssemblyEventConnector124, sinkAssemblyContext__AssemblyEventConnector127, sourceAssemblyContext__AssemblyEventConnector130, assemblyContext__RequiredInfrastructureDelegationConnector174, assemblyContext__RequiredResourceDelegationConnector177, innerRequiredRole__RequiredResourceDelegationConnector179, outerRequiredRole__RequiredResourceDelegationConnector182, parentStructure__AssemblyContext185, assemblyContext__SinkDelegationConnector144, encapsulatedComponent__AssemblyContext188, innerSinkRole__SinkRole146, outerSinkRole__SinkRole149, configParameterUsages__AssemblyContext189, providedRole__AssemblyInfrastructureConnector152, requiredRole__AssemblyInfrastructureConnector153, providingAssemblyContext__AssemblyInfrastructureConnector155, requiringAssemblyContext__AssemblyInfrastructureConnector158, innerProvidedRole__ProvidedInfrastructureDelegationConnector161, outerProvidedRole__ProvidedInfrastructureDelegationConnector163, assemblyContext__ProvidedInfrastructureDelegationConnector166, innerRequiredRole__RequiredInfrastructureDelegationConnector169, outerRequiredRole__RequiredInfrastructureDelegationConnector171, usageModel_UserData201, userDataParameterUsages_UserData204, usageScenario_UsageModel207, userData_UsageModel210, providedRole_EntryLevelSystemCall212, operationSignature__EntryLevelSystemCall214, outputParameterUsages_EntryLevelSystemCall216, usageScenario_Workload191, inputParameterUsages_EntryLevelSystemCall219, usageModel_UsageScenario193, scenarioBehaviour_UsageScenario195, workload_UsageScenario197, assemblyContext_userData199, usageScenario_SenarioBehaviour230, branchTransition_ScenarioBehaviour233, loop_ScenarioBehaviour235, actions_ScenarioBehaviour238, branch_BranchTransition241, branchedBehaviour_BranchTransition243, successor222, predecessor224, scenarioBehaviour_AbstractUserAction227, loopIteration_Loop249, bodyBehaviour_Loop252, branchTransitions_Branch246, thinkTime_ClosedWorkload261, capacity_PassiveResource264, basicComponent_PassiveResource267, resourceTimeoutFailureType__PassiveResource269, interArrivalTime_OpenWorkload255, timeSpecification_Delay258, serviceEffectSpecifications__BasicComponent270, passiveResource_BasicComponent272, parentCompleteComponentTypes275, infrastructureSignature__Parameter285, operationSignature__Parameter287, eventType__Parameter290, resourceSignature__Parameter292, repository__DataType293, components__Repository296, interfaces__Repository299, componentParameterUsage_ImplementationComponentType276, repository__RepositoryComponent279, providingEntity_ProvidedRole281, dataType__Parameter284, protocols__Interface308, requiredCharacterisations310, repository__Interface312, parameter315, interface_RequiredCharacterisation316, eventTypes__EventGroup319, parameter__EventType322, eventGroup__EventType325, failureTypes__Repository301, dataTypes__Repository303, parentInterfaces__Interface306, infrastructureSignatures__InfrastructureInterface337, requiredInterface__InfrastructureRequiredRole340, requiringEntity_RequiredRole342, interface__OperationSignature345, parameters__OperationSignature347, exceptions__Signature328, failureType329, parameters__InfrastructureSignature332, infrastructureInterface__InfrastructureSignature335, requiredInterface__OperationRequiredRole355, eventGroup__SourceRole357, eventGroup__SinkRole359, providedInterface__OperationProvidedRole361, providedInterface__InfrastructureProvidedRole363, returnType__OperationSignature350, signatures__OperationInterface352, parentProvidesComponentTypes365, innerType_CollectionDataType366, parentType_CompositeDataType368, innerDeclaration_CompositeDataType369, resourceInterface__ResourceSignature379, hardwareInducedFailureType__ProcessingResourceType382, resourceRepository_ResourceType384, resourceInterfaces__ResourceRepository386, schedulingPolicies__ResourceRepository389, availableResourceTypes_ResourceRepository391, resourceRepository__SchedulingPolicy393, networkInducedFailureType__CommunicationLinkResourceType396, datatype_InnerDeclaration371, compositeDataType_InnerDeclaration373, parameter__ResourceSignature376, variableCharacterisation_VariableUsage404, userData_VariableUsage407, callAction__VariableUsage410, synchronisationPoint_VariableUsage412, callReturnAction__VariableUsage414, setVariableAction_VariableUsage416, specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage418, assemblyContext__VariableUsage420, entryLevelSystemCall_InputParameterUsage423, entryLevelSystemCall_OutputParameterUsage425, namedReference__VariableUsage428, specification_VariableCharacterisation429, resourceRepository__ResourceInterface398, resourceSignatures__ResourceInterface401, processingResourceType__HardwareInducedFailureType435, internalFailureOccurrenceDescriptions__SoftwareInducedFailureType437, variableUsage_VariableCharacterisation432, specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription445, failureType__ExternalFailureOccurrenceDescription447, passiveResource__ResourceTimeoutFailureType449, repository__FailureType452, internalAction__InternalFailureOccurrenceDescription439, softwareInducedFailureType__InternalFailureOccurrenceDescription441, communicationLinkResourceType__NetworkInducedFailureType443, abstractLoopAction_ResourceDemandingBehaviour471, abstractBranchTransition_ResourceDemandingBehaviour473, steps_Behaviour475, resourceDemand_Action455, bodyBehaviour_Loop478, branchAction_AbstractBranchTransition481, infrastructureCall__Action458, resourceCall__Action461, predecessor_AbstractAction464, successor_AbstractAction466, resourceDemandingBehaviour_AbstractAction469, branches_Branch486, inputVariableUsages__CallAction489, describedService__SEFF492, basicComponent_ServiceEffectSpecification493, branchBehaviour_BranchTransition483, resourceDemandingSEFF_ResourceDemandingInternalBehaviour498, passiveResource_ReleaseAction500, iterationCount_LoopAction502, asynchronousForkedBehaviours_ForkAction505, synchronisingBehaviours_ForkAction507, resourceDemandingInternalBehaviours496, synchronisationPoint_ForkedBehaviour510, forkAction_ForkedBehaivour513, outputParameterUsage_SynchronisationPoint515, forkAction_SynchronisationPoint518, calledService_ExternalService524, synchronousForkedBehaviours_SynchronisationPoint521, role_ExternalService526, returnVariableUsage__CallReturnAction529, passiveresource_AcquireAction532, localVariableUsages_SetVariableAction539, calledResourceDemandingInternalBehaviour542, parameter_CollectionIteratorAction534, eventType__EmitEventAction544, sourceRole__EmitEventAction546, branchCondition_GuardedBranchTransition536, internalFailureOccurrenceDescriptions__InternalAction549, signature__InfrastructureCall552, numberOfCalls__InfrastructureCall554, action__InfrastructureCall557, requiredRole__InfrastructureCall559, action__ResourceCall562, resourceRequiredRole__ResourceCall565, signature__ResourceCall567, numberOfCalls__ResourceCall570, failureHandlingAlternatives__RecoveryActionBehaviour581, specification_ParametericResourceDemand573, requiredResource_ParametricResourceDemand576, action_ParametricResourceDemand578, failureTypes_FailureHandlingEntity589, signature_SpecifiedQoSAnnation591, role_SpecifiedQoSAnnotation593, qosAnnotations_SpecifiedQoSAnnotation595, recoveryAction__RecoveryActionBehaviour582, primaryBehaviour__RecoveryAction584, recoveryActionBehaviours__RecoveryAction586, role_SpecifiedOutputParameterAbstraction605, expectedExternalOutputs_SpecifiedOutputParameterAbstraction608, qosAnnotations_SpecifiedOutputParameterAbstraction611, specifiedOutputParameterAbstractions_QoSAnnotations597, system_QoSAnnotations600, specifiedQoSAnnotations_QoSAnnotations601, signature_SpecifiedOutputParameterAbstraction603, specification_SpecifiedExecutionTime614, externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation619, assemblyContext_ComponentSpecifiedExecutionTime617, qosAnnotations_System621, linkingResources__ResourceEnvironment624, resourceContainer_ResourceEnvironment626, connectedResourceContainers_LinkingResource628, communicationLinkResourceSpecifications_LinkingResource630, resourceEnvironment_LinkingResource633, activeResourceSpecifications_ResourceContainer635, resourceEnvironment_ResourceContainer638, schedulingPolicy647, activeResourceType_ActiveResourceSpecification649, processingRate_ProcessingResourceSpecification652, resourceContainer_ProcessingResourceSpecification655, linkingResource_CommunicationLinkResourceSpecification658, communicationLinkResourceType_CommunicationLinkResourceSpecification661, latency_CommunicationLinkResourceSpecification663, throughput_CommunicationLinkResourceSpecification666, nestedResourceContainers__ResourceContainer641, parentResourceContainer__ResourceContainer644, eventChannel__AllocationContext675, targetResourceEnvironment_Allocation677, system_Allocation679, allocationContexts_Allocation682, resourceContainer_AllocationContext669, assemblyContext_AllocationContext671, allocation_AllocationContext674, completions_CompletionRepository684, requiredCommunicationLinkResource_ParametricResourceDemand685},
    generalizations={gen_pcm_pc_core_pc_PCMRandomVariable_RandomVariable, gen_pcm_pc_entity_pc_ResourceInterfaceRequiringEntity_Entity, gen_pcm_pc_entity_pc_ResourceRequiredRole_Role, gen_pcm_pc_entity_pc_ResourceProvidedRole_Role, gen_pcm_pc_entity_pc_InterfaceProvidingRequiringEntity_entity_pc_InterfaceProvidingEntity, gen_pcm_pc_entity_pc_InterfaceProvidingRequiringEntity_entity_pc_InterfaceRequiringEntity, gen_pcm_pc_entity_pc_InterfaceProvidingEntity_Entity, gen_pcm_pc_entity_pc_InterfaceRequiringEntity_entity_pc_Entity, gen_pcm_pc_entity_pc_InterfaceRequiringEntity_entity_pc_ResourceInterfaceRequiringEntity, gen_pcm_pc_entity_pc_ResourceInterfaceProvidingEntity_Entity, gen_pcm_pc_entity_pc_ComposedProvidingRequiringEntity_composition_pc_ComposedStructure, gen_pcm_pc_entity_pc_ComposedProvidingRequiringEntity_entity_pc_InterfaceProvidingRequiringEntity, gen_pcm_pc_entity_pc_ResourceInterfaceProvidingRequiringEntity_entity_pc_ResourceInterfaceRequiringEntity, gen_pcm_pc_entity_pc_ResourceInterfaceProvidingRequiringEntity_entity_pc_ResourceInterfaceProvidingEntity, gen_pcm_pc_entity_pc_Entity_Identifier, gen_pcm_pc_entity_pc_Entity_entity_pc_NamedElement, gen_pcm_pc_composition_pc_DelegationConnector_Connector, gen_pcm_pc_composition_pc_Connector_Entity, gen_pcm_pc_composition_pc_ComposedStructure_Entity, gen_pcm_pc_composition_pc_ProvidedDelegationConnector_DelegationConnector, gen_pcm_pc_composition_pc_EventChannel_Entity, gen_pcm_pc_composition_pc_EventChannelSourceConnector_Connector, gen_pcm_pc_composition_pc_EventChannelSinkConnector_Connector, gen_pcm_pc_composition_pc_AssemblyConnector_Connector, gen_pcm_pc_composition_pc_RequiredDelegationConnector_DelegationConnector, gen_pcm_pc_composition_pc_SourceDelegationConnector_DelegationConnector, gen_pcm_pc_composition_pc_AssemblyEventConnector_Connector, gen_pcm_pc_composition_pc_RequiredResourceDelegationConnector_DelegationConnector, gen_pcm_pc_composition_pc_SinkDelegationConnector_DelegationConnector, gen_pcm_pc_composition_pc_AssemblyContext_Entity, gen_pcm_pc_composition_pc_AssemblyInfrastructureConnector_Connector, gen_pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector_DelegationConnector, gen_pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector_DelegationConnector, gen_pcm_pc_usagemodel_pc_EntryLevelSystemCall_AbstractUserAction, gen_pcm_pc_usagemodel_pc_UsageScenario_Entity, gen_pcm_pc_usagemodel_pc_Branch_AbstractUserAction, gen_pcm_pc_usagemodel_pc_AbstractUserAction_Entity, gen_pcm_pc_usagemodel_pc_ScenarioBehaviour_Entity, gen_pcm_pc_usagemodel_pc_Loop_AbstractUserAction, gen_pcm_pc_usagemodel_pc_Stop_AbstractUserAction, gen_pcm_pc_usagemodel_pc_Start_AbstractUserAction, gen_pcm_pc_usagemodel_pc_OpenWorkload_Workload, gen_pcm_pc_repository_pc_PassiveResource_Entity, gen_pcm_pc_repository_pc_BasicComponent_ImplementationComponentType, gen_pcm_pc_usagemodel_pc_Delay_AbstractUserAction, gen_pcm_pc_usagemodel_pc_ClosedWorkload_Workload, gen_pcm_pc_repository_pc_ImplementationComponentType_RepositoryComponent, gen_pcm_pc_repository_pc_Repository_Entity, gen_pcm_pc_repository_pc_RepositoryComponent_InterfaceProvidingRequiringEntity, gen_pcm_pc_repository_pc_ProvidedRole_Role, gen_pcm_pc_repository_pc_EventGroup_Interface, gen_pcm_pc_repository_pc_EventType_Signature, gen_pcm_pc_repository_pc_Signature_Entity, gen_pcm_pc_repository_pc_Interface_Entity, gen_pcm_pc_repository_pc_InfrastructureRequiredRole_RequiredRole, gen_pcm_pc_repository_pc_RequiredRole_Role, gen_pcm_pc_repository_pc_OperationSignature_Signature, gen_pcm_pc_repository_pc_InfrastructureSignature_Signature, gen_pcm_pc_repository_pc_InfrastructureInterface_Interface, gen_pcm_pc_repository_pc_OperationRequiredRole_RequiredRole, gen_pcm_pc_repository_pc_SourceRole_RequiredRole, gen_pcm_pc_repository_pc_SinkRole_ProvidedRole, gen_pcm_pc_repository_pc_OperationProvidedRole_ProvidedRole, gen_pcm_pc_repository_pc_InfrastructureProvidedRole_ProvidedRole, gen_pcm_pc_repository_pc_OperationInterface_Interface, gen_pcm_pc_repository_pc_ProvidesComponentType_RepositoryComponent, gen_pcm_pc_repository_pc_CompositeComponent_entity_pc_ComposedProvidingRequiringEntity, gen_pcm_pc_repository_pc_CompositeComponent_repository_pc_ImplementationComponentType, gen_pcm_pc_repository_pc_CompleteComponentType_RepositoryComponent, gen_pcm_pc_repository_pc_CollectionDataType_entity_pc_Entity, gen_pcm_pc_repository_pc_CollectionDataType_repository_pc_DataType, gen_pcm_pc_repository_pc_CompositeDataType_entity_pc_Entity, gen_pcm_pc_repository_pc_CompositeDataType_repository_pc_DataType, gen_pcm_pc_repository_pc_InnerDeclaration_NamedElement, gen_pcm_pc_repository_pc_PrimitiveDataType_DataType, gen_pcm_pc_resourcetype_pc_ProcessingResourceType_ResourceType, gen_pcm_pc_resourcetype_pc_ResourceType_entity_pc_Entity, gen_pcm_pc_resourcetype_pc_ResourceType_UnitCarryingElement, gen_pcm_pc_resourcetype_pc_ResourceType_entity_pc_ResourceInterfaceProvidingEntity, gen_pcm_pc_resourcetype_pc_SchedulingPolicy_Entity, gen_pcm_pc_resourcetype_pc_CommunicationLinkResourceType_ResourceType, gen_pcm_pc_resourcetype_pc_ResourceInterface_Entity, gen_pcm_pc_repository_pc_Role_Entity, gen_pcm_pc_resourcetype_pc_ResourceSignature_Entity, gen_pcm_pc_reliability_pc_HardwareInducedFailureType_FailureType, gen_pcm_pc_reliability_pc_SoftwareInducedFailureType_FailureType, gen_pcm_pc_parameter_pc_CharacterisedVariable_Variable, gen_pcm_pc_reliability_pc_InternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_pc_reliability_pc_ResourceTimeoutFailureType_SoftwareInducedFailureType, gen_pcm_pc_reliability_pc_FailureType_Entity, gen_pcm_pc_seff_pc_StopAction_AbstractInternalControlFlowAction, gen_pcm_pc_reliability_pc_NetworkInducedFailureType_FailureType, gen_pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_pc_seff_pc_AbstractInternalControlFlowAction_AbstractAction, gen_pcm_pc_seff_pc_AbstractLoopAction_AbstractInternalControlFlowAction, gen_pcm_pc_seff_pc_AbstractBranchTransition_Entity, gen_pcm_pc_seff_pc_AbstractAction_Entity, gen_pcm_pc_seff_pc_ResourceDemandingBehaviour_Identifier, gen_pcm_pc_seff_pc_StartAction_AbstractInternalControlFlowAction, gen_pcm_pc_seff_pc_ResourceDemandingSEFF_Identifier, gen_pcm_pc_seff_pc_ResourceDemandingSEFF_seff_pc_ServiceEffectSpecification, gen_pcm_pc_seff_pc_ResourceDemandingSEFF_seff_pc_ResourceDemandingBehaviour, gen_pcm_pc_seff_pc_BranchAction_AbstractInternalControlFlowAction, gen_pcm_pc_seff_pc_ReleaseAction_AbstractInternalControlFlowAction, gen_pcm_pc_seff_pc_LoopAction_AbstractLoopAction, gen_pcm_pc_seff_pc_ForkAction_AbstractInternalControlFlowAction, gen_pcm_pc_seff_pc_ForkedBehaviour_ResourceDemandingBehaviour, gen_pcm_pc_seff_pc_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour, gen_pcm_pc_seff_pc_ExternalCallAction_seff_pc_AbstractAction, gen_pcm_pc_seff_pc_ExternalCallAction_seff_pc_CallReturnAction, gen_pcm_pc_seff_pc_ExternalCallAction_seff_reliability_pc_FailureHandlingEntity, gen_pcm_pc_seff_pc_CallReturnAction_CallAction, gen_pcm_pc_seff_pc_ProbabilisticBranchTransition_AbstractBranchTransition, gen_pcm_pc_seff_pc_AcquireAction_AbstractInternalControlFlowAction, gen_pcm_pc_seff_pc_CollectionIteratorAction_AbstractLoopAction, gen_pcm_pc_seff_pc_SetVariableAction_AbstractInternalControlFlowAction, gen_pcm_pc_seff_pc_InternalCallAction_seff_pc_CallAction, gen_pcm_pc_seff_pc_InternalCallAction_seff_pc_AbstractInternalControlFlowAction, gen_pcm_pc_seff_pc_EmitEventAction_seff_pc_AbstractAction, gen_pcm_pc_seff_pc_EmitEventAction_seff_pc_CallAction, gen_pcm_pc_seff_pc_GuardedBranchTransition_AbstractBranchTransition, gen_pcm_pc_seff_pc_InternalAction_AbstractInternalControlFlowAction, gen_pcm_pc_seff_performance_pc_ResourceCall_CallAction, gen_pcm_pc_seff_performance_pc_InfrastructureCall_CallAction, gen_pcm_pc_seff_reliability_pc_RecoveryActionBehaviour_seff_reliability_pc_FailureHandlingEntity, gen_pcm_pc_seff_reliability_pc_RecoveryActionBehaviour_seff_pc_ResourceDemandingBehaviour, gen_pcm_pc_seff_reliability_pc_RecoveryAction_AbstractInternalControlFlowAction, gen_pcm_pc_seff_reliability_pc_FailureHandlingEntity_Entity, gen_pcm_pc_qos_performance_pc_SystemSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_pc_qos_performance_pc_SpecifiedExecutionTime_SpecifiedQoSAnnotation, gen_pcm_pc_qosannotations_pc_QoSAnnotations_Entity, gen_pcm_pc_qos_performance_pc_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation, gen_pcm_pc_resourceenvironment_pc_ResourceEnvironment_NamedElement, gen_pcm_pc_resourceenvironment_pc_LinkingResource_Entity, gen_pcm_pc_resourceenvironment_pc_ResourceContainer_Entity, gen_pcm_pc_system_pc_System_entity_pc_Entity, gen_pcm_pc_system_pc_System_entity_pc_ComposedProvidingRequiringEntity, gen_pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification_Identifier, gen_pcm_pc_allocation_pc_AllocationContext_Entity, gen_pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification_Identifier, gen_pcm_pc_allocation_pc_Allocation_Entity, gen_pcm_pc_subsystem_pc_SubSystem_entity_pc_ComposedProvidingRequiringEntity, gen_pcm_pc_subsystem_pc_SubSystem_repository_pc_RepositoryComponent, gen_pcm_pc_completions_pc_Completion_entity_pc_ComposedProvidingRequiringEntity, gen_pcm_pc_completions_pc_Completion_repository_pc_ImplementationComponentType, gen_pcm_pc_completions_pc_DelegatingExternalCallAction_ExternalCallAction, gen_pcm_pc_completions_pc_NetworkDemandParametricResourceDemand_ParametricResourceDemand},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)