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
            EnumerationLiteral(name="STRUCTURE"),
			EnumerationLiteral(name="NUMBER_OF_ELEMENTS"),
			EnumerationLiteral(name="VALUE"),
			EnumerationLiteral(name="BYTESIZE"),
			EnumerationLiteral(name="TYPE")
    }
)

# Classes
pcm_av_av_DummyClass = Class(name="pcm::av::av::DummyClass")
pcm_av_av_AdviceAdvice = Class(name="pcm::av::av::AdviceAdvice")
pcm_av_av_EObject = Class(name="pcm::av::av::EObject")
pcm_av_av_GlobalScopeGlobalScope = Class(name="pcm::av::av::GlobalScopeGlobalScope")
pcm_av_av_PerJoinPointScopePerJoinPointScope = Class(name="pcm::av::av::PerJoinPointScopePerJoinPointScope")
pcm_av_av_Advice = Class(name="pcm::av::av::Advice")
ClosedWorkload = Class(name="ClosedWorkload")
PassiveResource = Class(name="PassiveResource")
VariableCharacterisation = Class(name="VariableCharacterisation")
seff_performance_av_av_InfrastructureCall = Class(name="seff::performance::av::av::InfrastructureCall")
seff_performance_av_av_ResourceCall = Class(name="seff::performance::av::av::ResourceCall")
seff_performance_av_av_ParametricResourceDemand = Class(name="seff::performance::av::av::ParametricResourceDemand")
LoopAction = Class(name="LoopAction")
GuardedBranchTransition = Class(name="GuardedBranchTransition")
qos_performance_av_av_SpecifiedExecutionTime = Class(name="qos::performance::av::av::SpecifiedExecutionTime")
composition_av_av_EventChannelSinkConnector = Class(name="composition::av::av::EventChannelSinkConnector")
composition_av_av_AssemblyEventConnector = Class(name="composition::av::av::AssemblyEventConnector")
Loop = Class(name="Loop")
OpenWorkload = Class(name="OpenWorkload")
pcm_av_av_GlobalScope = Class(name="pcm::av::av::GlobalScope")
pcm_av_av_PerJoinPointScope = Class(name="pcm::av::av::PerJoinPointScope")
pcm_av_av_core_av_av_PCMRandomVariable = Class(name="pcm::av::av::core::av::av::PCMRandomVariable")
RandomVariable = Class(name="RandomVariable")
ResourceInterface = Class(name="ResourceInterface")
pcm_av_av_entity_av_av_InterfaceProvidingRequiringEntity = Class(name="pcm::av::av::entity::av::av::InterfaceProvidingRequiringEntity")
entity_av_av_InterfaceProvidingEntity = Class(name="entity::av::av::InterfaceProvidingEntity")
entity_av_av_InterfaceRequiringEntity = Class(name="entity::av::av::InterfaceRequiringEntity")
pcm_av_av_entity_av_av_InterfaceProvidingEntity = Class(name="pcm::av::av::entity::av::av::InterfaceProvidingEntity")
Entity = Class(name="Entity")
ProvidedRole = Class(name="ProvidedRole")
pcm_av_av_entity_av_av_InterfaceRequiringEntity = Class(name="pcm::av::av::entity::av::av::InterfaceRequiringEntity")
entity_av_av_Entity = Class(name="entity::av::av::Entity")
entity_av_av_ResourceInterfaceRequiringEntity = Class(name="entity::av::av::ResourceInterfaceRequiringEntity")
RequiredRole = Class(name="RequiredRole")
pcm_av_av_entity_av_av_ResourceInterfaceRequiringEntity = Class(name="pcm::av::av::entity::av::av::ResourceInterfaceRequiringEntity")
entity_av_av_ResourceRequiredRole = Class(name="entity::av::av::ResourceRequiredRole")
pcm_av_av_entity_av_av_ResourceRequiredRole = Class(name="pcm::av::av::entity::av::av::ResourceRequiredRole")
pcm_av_av_entity_av_av_ResourceInterfaceProvidingEntity = Class(name="pcm::av::av::entity::av::av::ResourceInterfaceProvidingEntity")
entity_av_av_ResourceProvidedRole = Class(name="entity::av::av::ResourceProvidedRole")
Delay = Class(name="Delay")
CommunicationLinkResourceSpecification = Class(name="CommunicationLinkResourceSpecification")
ProcessingResourceSpecification = Class(name="ProcessingResourceSpecification")
pcm_av_av_entity_av_av_ResourceProvidedRole = Class(name="pcm::av::av::entity::av::av::ResourceProvidedRole")
Role = Class(name="Role")
entity_av_av_ResourceInterfaceProvidingEntity = Class(name="entity::av::av::ResourceInterfaceProvidingEntity")
pcm_av_av_composition_av_av_DelegationConnector = Class(name="pcm::av::av::composition::av::av::DelegationConnector")
Connector = Class(name="Connector")
pcm_av_av_composition_av_av_Connector = Class(name="pcm::av::av::composition::av::av::Connector")
pcm_av_av_composition_av_av_ComposedStructure = Class(name="pcm::av::av::composition::av::av::ComposedStructure")
composition_av_av_AssemblyContext = Class(name="composition::av::av::AssemblyContext")
composition_av_av_ResourceRequiredDelegationConnector = Class(name="composition::av::av::ResourceRequiredDelegationConnector")
composition_av_av_EventChannel = Class(name="composition::av::av::EventChannel")
pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity = Class(name="pcm::av::av::entity::av::av::ComposedProvidingRequiringEntity")
composition_av_av_ComposedStructure = Class(name="composition::av::av::ComposedStructure")
entity_av_av_InterfaceProvidingRequiringEntity = Class(name="entity::av::av::InterfaceProvidingRequiringEntity")
pcm_av_av_entity_av_av_NamedElement = Class(name="pcm::av::av::entity::av::av::NamedElement")
pcm_av_av_entity_av_av_ResourceInterfaceProvidingRequiringEntity = Class(name="pcm::av::av::entity::av::av::ResourceInterfaceProvidingRequiringEntity")
pcm_av_av_entity_av_av_Entity = Class(name="pcm::av::av::entity::av::av::Entity")
Identifier = Class(name="Identifier")
entity_av_av_NamedElement = Class(name="entity::av::av::NamedElement")
pcm_av_av_composition_av_av_ResourceRequiredDelegationConnector = Class(name="pcm::av::av::composition::av::av::ResourceRequiredDelegationConnector")
pcm_av_av_composition_av_av_EventChannel = Class(name="pcm::av::av::composition::av::av::EventChannel")
EventGroup = Class(name="EventGroup")
composition_av_av_EventChannelSourceConnector = Class(name="composition::av::av::EventChannelSourceConnector")
pcm_av_av_composition_av_av_EventChannelSourceConnector = Class(name="pcm::av::av::composition::av::av::EventChannelSourceConnector")
SourceRole = Class(name="SourceRole")
pcm_av_av_composition_av_av_EventChannelSinkConnector = Class(name="pcm::av::av::composition::av::av::EventChannelSinkConnector")
composition_av_av_Connector = Class(name="composition::av::av::Connector")
OperationProvidedRole = Class(name="OperationProvidedRole")
pcm_av_av_composition_av_av_RequiredDelegationConnector = Class(name="pcm::av::av::composition::av::av::RequiredDelegationConnector")
SinkRole = Class(name="SinkRole")
PCMRandomVariable = Class(name="PCMRandomVariable")
pcm_av_av_composition_av_av_ProvidedDelegationConnector = Class(name="pcm::av::av::composition::av::av::ProvidedDelegationConnector")
DelegationConnector = Class(name="DelegationConnector")
pcm_av_av_composition_av_av_AssemblyEventConnector = Class(name="pcm::av::av::composition::av::av::AssemblyEventConnector")
OperationRequiredRole = Class(name="OperationRequiredRole")
pcm_av_av_composition_av_av_AssemblyConnector = Class(name="pcm::av::av::composition::av::av::AssemblyConnector")
pcm_av_av_composition_av_av_AssemblyInfrastructureConnector = Class(name="pcm::av::av::composition::av::av::AssemblyInfrastructureConnector")
InfrastructureProvidedRole = Class(name="InfrastructureProvidedRole")
InfrastructureRequiredRole = Class(name="InfrastructureRequiredRole")
pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector = Class(name="pcm::av::av::composition::av::av::ProvidedInfrastructureDelegationConnector")
pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector = Class(name="pcm::av::av::composition::av::av::RequiredInfrastructureDelegationConnector")
pcm_av_av_composition_av_av_RequiredResourceDelegationConnector = Class(name="pcm::av::av::composition::av::av::RequiredResourceDelegationConnector")
pcm_av_av_composition_av_av_SourceDelegationConnector = Class(name="pcm::av::av::composition::av::av::SourceDelegationConnector")
pcm_av_av_composition_av_av_SinkDelegationConnector = Class(name="pcm::av::av::composition::av::av::SinkDelegationConnector")
VariableUsage = Class(name="VariableUsage")
pcm_av_av_usagemodel_av_av_Workload = Class(name="pcm::av::av::usagemodel::av::av::Workload")
UsageScenario = Class(name="UsageScenario")
pcm_av_av_usagemodel_av_av_UsageScenario = Class(name="pcm::av::av::usagemodel::av::av::UsageScenario")
UsageModel = Class(name="UsageModel")
ScenarioBehaviour = Class(name="ScenarioBehaviour")
Workload = Class(name="Workload")
pcm_av_av_usagemodel_av_av_UserData = Class(name="pcm::av::av::usagemodel::av::av::UserData")
pcm_av_av_usagemodel_av_av_UsageModel = Class(name="pcm::av::av::usagemodel::av::av::UsageModel")
pcm_av_av_composition_av_av_AssemblyContext = Class(name="pcm::av::av::composition::av::av::AssemblyContext")
RepositoryComponent = Class(name="RepositoryComponent")
UserData = Class(name="UserData")
pcm_av_av_usagemodel_av_av_EntryLevelSystemCall = Class(name="pcm::av::av::usagemodel::av::av::EntryLevelSystemCall")
AbstractUserAction = Class(name="AbstractUserAction")
OperationSignature = Class(name="OperationSignature")
BranchTransition = Class(name="BranchTransition")
pcm_av_av_usagemodel_av_av_BranchTransition = Class(name="pcm::av::av::usagemodel::av::av::BranchTransition")
pcm_av_av_usagemodel_av_av_AbstractUserAction = Class(name="pcm::av::av::usagemodel::av::av::AbstractUserAction")
pcm_av_av_usagemodel_av_av_ScenarioBehaviour = Class(name="pcm::av::av::usagemodel::av::av::ScenarioBehaviour")
pcm_av_av_usagemodel_av_av_Stop = Class(name="pcm::av::av::usagemodel::av::av::Stop")
pcm_av_av_usagemodel_av_av_Start = Class(name="pcm::av::av::usagemodel::av::av::Start")
pcm_av_av_usagemodel_av_av_OpenWorkload = Class(name="pcm::av::av::usagemodel::av::av::OpenWorkload")
Branch = Class(name="Branch")
pcm_av_av_usagemodel_av_av_Branch = Class(name="pcm::av::av::usagemodel::av::av::Branch")
pcm_av_av_usagemodel_av_av_Loop = Class(name="pcm::av::av::usagemodel::av::av::Loop")
pcm_av_av_repository_av_av_PassiveResource = Class(name="pcm::av::av::repository::av::av::PassiveResource")
BasicComponent = Class(name="BasicComponent")
ResourceTimeoutFailureType = Class(name="ResourceTimeoutFailureType")
pcm_av_av_repository_av_av_BasicComponent = Class(name="pcm::av::av::repository::av::av::BasicComponent")
ImplementationComponentType = Class(name="ImplementationComponentType")
pcm_av_av_usagemodel_av_av_Delay = Class(name="pcm::av::av::usagemodel::av::av::Delay")
pcm_av_av_usagemodel_av_av_ClosedWorkload = Class(name="pcm::av::av::usagemodel::av::av::ClosedWorkload")
pcm_av_av_repository_av_av_ImplementationComponentType = Class(name="pcm::av::av::repository::av::av::ImplementationComponentType")
CompleteComponentType = Class(name="CompleteComponentType")
ServiceEffectSpecification = Class(name="ServiceEffectSpecification")
InfrastructureSignature = Class(name="InfrastructureSignature")
EventType = Class(name="EventType")
ResourceSignature = Class(name="ResourceSignature")
pcm_av_av_repository_av_av_DataType = Class(name="pcm::av::av::repository::av::av::DataType")
pcm_av_av_repository_av_av_Repository = Class(name="pcm::av::av::repository::av::av::Repository")
Interface = Class(name="Interface")
pcm_av_av_repository_av_av_RepositoryComponent = Class(name="pcm::av::av::repository::av::av::RepositoryComponent")
InterfaceProvidingRequiringEntity = Class(name="InterfaceProvidingRequiringEntity")
Repository = Class(name="Repository")
pcm_av_av_repository_av_av_ProvidedRole = Class(name="pcm::av::av::repository::av::av::ProvidedRole")
pcm_av_av_repository_av_av_Parameter = Class(name="pcm::av::av::repository::av::av::Parameter")
DataType = Class(name="DataType")
pcm_av_av_repository_av_av_Interface = Class(name="pcm::av::av::repository::av::av::Interface")
Protocol = Class(name="Protocol")
FailureType = Class(name="FailureType")
pcm_av_av_repository_av_av_EventGroup = Class(name="pcm::av::av::repository::av::av::EventGroup")
pcm_av_av_repository_av_av_EventType = Class(name="pcm::av::av::repository::av::av::EventType")
Signature = Class(name="Signature")
pcm_av_av_repository_av_av_Signature = Class(name="pcm::av::av::repository::av::av::Signature")
ExceptionType = Class(name="ExceptionType")
pcm_av_av_repository_av_av_ExceptionType = Class(name="pcm::av::av::repository::av::av::ExceptionType")
RequiredCharacterisation = Class(name="RequiredCharacterisation")
pcm_av_av_repository_av_av_RequiredCharacterisation = Class(name="pcm::av::av::repository::av::av::RequiredCharacterisation")
Parameter_ = Class(name="Parameter")
pcm_av_av_repository_av_av_OperationSignature = Class(name="pcm::av::av::repository::av::av::OperationSignature")
OperationInterface = Class(name="OperationInterface")
pcm_av_av_repository_av_av_OperationInterface = Class(name="pcm::av::av::repository::av::av::OperationInterface")
pcm_av_av_repository_av_av_InfrastructureSignature = Class(name="pcm::av::av::repository::av::av::InfrastructureSignature")
InfrastructureInterface = Class(name="InfrastructureInterface")
pcm_av_av_repository_av_av_InfrastructureInterface = Class(name="pcm::av::av::repository::av::av::InfrastructureInterface")
pcm_av_av_repository_av_av_InfrastructureRequiredRole = Class(name="pcm::av::av::repository::av::av::InfrastructureRequiredRole")
pcm_av_av_repository_av_av_RequiredRole = Class(name="pcm::av::av::repository::av::av::RequiredRole")
pcm_av_av_repository_av_av_SinkRole = Class(name="pcm::av::av::repository::av::av::SinkRole")
pcm_av_av_repository_av_av_OperationProvidedRole = Class(name="pcm::av::av::repository::av::av::OperationProvidedRole")
pcm_av_av_repository_av_av_InfrastructureProvidedRole = Class(name="pcm::av::av::repository::av::av::InfrastructureProvidedRole")
pcm_av_av_repository_av_av_CompleteComponentType = Class(name="pcm::av::av::repository::av::av::CompleteComponentType")
pcm_av_av_repository_av_av_OperationRequiredRole = Class(name="pcm::av::av::repository::av::av::OperationRequiredRole")
pcm_av_av_repository_av_av_SourceRole = Class(name="pcm::av::av::repository::av::av::SourceRole")
pcm_av_av_repository_av_av_ProvidesComponentType = Class(name="pcm::av::av::repository::av::av::ProvidesComponentType")
pcm_av_av_repository_av_av_CompositeComponent = Class(name="pcm::av::av::repository::av::av::CompositeComponent")
entity_av_av_ComposedProvidingRequiringEntity = Class(name="entity::av::av::ComposedProvidingRequiringEntity")
repository_av_av_ImplementationComponentType = Class(name="repository::av::av::ImplementationComponentType")
pcm_av_av_repository_av_av_PrimitiveDataType = Class(name="pcm::av::av::repository::av::av::PrimitiveDataType")
ProvidesComponentType = Class(name="ProvidesComponentType")
CompositeDataType = Class(name="CompositeDataType")
InnerDeclaration = Class(name="InnerDeclaration")
pcm_av_av_repository_av_av_InnerDeclaration = Class(name="pcm::av::av::repository::av::av::InnerDeclaration")
NamedElement = Class(name="NamedElement")
pcm_av_av_repository_av_av_Role = Class(name="pcm::av::av::repository::av::av::Role")
pcm_av_av_resourcetype_av_av_ResourceSignature = Class(name="pcm::av::av::resourcetype::av::av::ResourceSignature")
pcm_av_av_resourcetype_av_av_ProcessingResourceType = Class(name="pcm::av::av::resourcetype::av::av::ProcessingResourceType")
ResourceType = Class(name="ResourceType")
HardwareInducedFailureType = Class(name="HardwareInducedFailureType")
pcm_av_av_resourcetype_av_av_ResourceType = Class(name="pcm::av::av::resourcetype::av::av::ResourceType")
UnitCarryingElement = Class(name="UnitCarryingElement")
pcm_av_av_repository_av_av_CollectionDataType = Class(name="pcm::av::av::repository::av::av::CollectionDataType")
repository_av_av_DataType = Class(name="repository::av::av::DataType")
pcm_av_av_repository_av_av_CompositeDataType = Class(name="pcm::av::av::repository::av::av::CompositeDataType")
pcm_av_av_resourcetype_av_av_CommunicationLinkResourceType = Class(name="pcm::av::av::resourcetype::av::av::CommunicationLinkResourceType")
NetworkInducedFailureType = Class(name="NetworkInducedFailureType")
pcm_av_av_resourcetype_av_av_ResourceInterface = Class(name="pcm::av::av::resourcetype::av::av::ResourceInterface")
pcm_av_av_protocol_av_av_Protocol = Class(name="pcm::av::av::protocol::av::av::Protocol")
pcm_av_av_parameter_av_av_VariableUsage = Class(name="pcm::av::av::parameter::av::av::VariableUsage")
CallAction = Class(name="CallAction")
SynchronisationPoint = Class(name="SynchronisationPoint")
CallReturnAction = Class(name="CallReturnAction")
ResourceRepository = Class(name="ResourceRepository")
pcm_av_av_resourcetype_av_av_ResourceRepository = Class(name="pcm::av::av::resourcetype::av::av::ResourceRepository")
SchedulingPolicy = Class(name="SchedulingPolicy")
pcm_av_av_resourcetype_av_av_SchedulingPolicy = Class(name="pcm::av::av::resourcetype::av::av::SchedulingPolicy")
pcm_av_av_parameter_av_av_CharacterisedVariable = Class(name="pcm::av::av::parameter::av::av::CharacterisedVariable")
Variable = Class(name="Variable")
pcm_av_av_reliability_av_av_FailureOccurrenceDescription = Class(name="pcm::av::av::reliability::av::av::FailureOccurrenceDescription")
SetVariableAction = Class(name="SetVariableAction")
SpecifiedOutputParameterAbstraction = Class(name="SpecifiedOutputParameterAbstraction")
EntryLevelSystemCall = Class(name="EntryLevelSystemCall")
parameter_av_av_pcm_av_av_AbstractNamedReference = Class(name="parameter::av::av::pcm::av::av::AbstractNamedReference")
pcm_av_av_parameter_av_av_VariableCharacterisation = Class(name="pcm::av::av::parameter::av::av::VariableCharacterisation")
ProcessingResourceType = Class(name="ProcessingResourceType")
pcm_av_av_reliability_av_av_SoftwareInducedFailureType = Class(name="pcm::av::av::reliability::av::av::SoftwareInducedFailureType")
InternalFailureOccurrenceDescription = Class(name="InternalFailureOccurrenceDescription")
pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription = Class(name="pcm::av::av::reliability::av::av::InternalFailureOccurrenceDescription")
FailureOccurrenceDescription = Class(name="FailureOccurrenceDescription")
InternalAction = Class(name="InternalAction")
SoftwareInducedFailureType = Class(name="SoftwareInducedFailureType")
pcm_av_av_reliability_av_av_NetworkInducedFailureType = Class(name="pcm::av::av::reliability::av::av::NetworkInducedFailureType")
pcm_av_av_reliability_av_av_HardwareInducedFailureType = Class(name="pcm::av::av::reliability::av::av::HardwareInducedFailureType")
qos_reliability_av_av_SpecifiedReliabilityAnnotation = Class(name="qos::reliability::av::av::SpecifiedReliabilityAnnotation")
pcm_av_av_reliability_av_av_ResourceTimeoutFailureType = Class(name="pcm::av::av::reliability::av::av::ResourceTimeoutFailureType")
pcm_av_av_reliability_av_av_FailureType = Class(name="pcm::av::av::reliability::av::av::FailureType")
pcm_av_av_seff_av_av_StopAction = Class(name="pcm::av::av::seff::av::av::StopAction")
AbstractInternalControlFlowAction = Class(name="AbstractInternalControlFlowAction")
CommunicationLinkResourceType = Class(name="CommunicationLinkResourceType")
pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription = Class(name="pcm::av::av::reliability::av::av::ExternalFailureOccurrenceDescription")
ResourceDemandingBehaviour = Class(name="ResourceDemandingBehaviour")
pcm_av_av_seff_av_av_ResourceDemandingBehaviour = Class(name="pcm::av::av::seff::av::av::ResourceDemandingBehaviour")
AbstractLoopAction = Class(name="AbstractLoopAction")
AbstractBranchTransition = Class(name="AbstractBranchTransition")
pcm_av_av_seff_av_av_AbstractInternalControlFlowAction = Class(name="pcm::av::av::seff::av::av::AbstractInternalControlFlowAction")
AbstractAction = Class(name="AbstractAction")
pcm_av_av_seff_av_av_AbstractAction = Class(name="pcm::av::av::seff::av::av::AbstractAction")
pcm_av_av_seff_av_av_CallAction = Class(name="pcm::av::av::seff::av::av::CallAction")
pcm_av_av_seff_av_av_StartAction = Class(name="pcm::av::av::seff::av::av::StartAction")
pcm_av_av_seff_av_av_ServiceEffectSpecification = Class(name="pcm::av::av::seff::av::av::ServiceEffectSpecification")
pcm_av_av_seff_av_av_AbstractLoopAction = Class(name="pcm::av::av::seff::av::av::AbstractLoopAction")
pcm_av_av_seff_av_av_AbstractBranchTransition = Class(name="pcm::av::av::seff::av::av::AbstractBranchTransition")
BranchAction = Class(name="BranchAction")
pcm_av_av_seff_av_av_BranchAction = Class(name="pcm::av::av::seff::av::av::BranchAction")
pcm_av_av_seff_av_av_ResourceDemandingInternalBehaviour = Class(name="pcm::av::av::seff::av::av::ResourceDemandingInternalBehaviour")
ResourceDemandingSEFF = Class(name="ResourceDemandingSEFF")
pcm_av_av_seff_av_av_ReleaseAction = Class(name="pcm::av::av::seff::av::av::ReleaseAction")
pcm_av_av_seff_av_av_LoopAction = Class(name="pcm::av::av::seff::av::av::LoopAction")
pcm_av_av_seff_av_av_ForkAction = Class(name="pcm::av::av::seff::av::av::ForkAction")
ForkedBehaviour = Class(name="ForkedBehaviour")
pcm_av_av_seff_av_av_ForkedBehaviour = Class(name="pcm::av::av::seff::av::av::ForkedBehaviour")
ForkAction = Class(name="ForkAction")
pcm_av_av_seff_av_av_SynchronisationPoint = Class(name="pcm::av::av::seff::av::av::SynchronisationPoint")
pcm_av_av_seff_av_av_ResourceDemandingSEFF = Class(name="pcm::av::av::seff::av::av::ResourceDemandingSEFF")
seff_av_av_ServiceEffectSpecification = Class(name="seff::av::av::ServiceEffectSpecification")
seff_av_av_ResourceDemandingBehaviour = Class(name="seff::av::av::ResourceDemandingBehaviour")
ResourceDemandingInternalBehaviour = Class(name="ResourceDemandingInternalBehaviour")
pcm_av_av_seff_av_av_CallReturnAction = Class(name="pcm::av::av::seff::av::av::CallReturnAction")
pcm_av_av_seff_av_av_ProbabilisticBranchTransition = Class(name="pcm::av::av::seff::av::av::ProbabilisticBranchTransition")
pcm_av_av_seff_av_av_AcquireAction = Class(name="pcm::av::av::seff::av::av::AcquireAction")
pcm_av_av_seff_av_av_ExternalCallAction = Class(name="pcm::av::av::seff::av::av::ExternalCallAction")
seff_av_av_AbstractAction = Class(name="seff::av::av::AbstractAction")
seff_av_av_CallReturnAction = Class(name="seff::av::av::CallReturnAction")
seff_reliability_av_av_FailureHandlingEntity = Class(name="seff::reliability::av::av::FailureHandlingEntity")
pcm_av_av_seff_av_av_SetVariableAction = Class(name="pcm::av::av::seff::av::av::SetVariableAction")
pcm_av_av_seff_av_av_InternalCallAction = Class(name="pcm::av::av::seff::av::av::InternalCallAction")
seff_av_av_CallAction = Class(name="seff::av::av::CallAction")
seff_av_av_AbstractInternalControlFlowAction = Class(name="seff::av::av::AbstractInternalControlFlowAction")
pcm_av_av_seff_av_av_EmitEventAction = Class(name="pcm::av::av::seff::av::av::EmitEventAction")
pcm_av_av_seff_av_av_InternalAction = Class(name="pcm::av::av::seff::av::av::InternalAction")
pcm_av_av_seff_av_av_CollectionIteratorAction = Class(name="pcm::av::av::seff::av::av::CollectionIteratorAction")
pcm_av_av_seff_av_av_GuardedBranchTransition = Class(name="pcm::av::av::seff::av::av::GuardedBranchTransition")
pcm_av_av_seff_performance_av_av_ResourceCall = Class(name="pcm::av::av::seff::performance::av::av::ResourceCall")
pcm_av_av_seff_performance_av_av_InfrastructureCall = Class(name="pcm::av::av::seff::performance::av::av::InfrastructureCall")
pcm_av_av_seff_performance_av_av_ParametricResourceDemand = Class(name="pcm::av::av::seff::performance::av::av::ParametricResourceDemand")
pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour = Class(name="pcm::av::av::seff::reliability::av::av::RecoveryActionBehaviour")
seff_reliability_av_av_RecoveryActionBehaviour = Class(name="seff::reliability::av::av::RecoveryActionBehaviour")
seff_reliability_av_av_RecoveryAction = Class(name="seff::reliability::av::av::RecoveryAction")
pcm_av_av_seff_reliability_av_av_RecoveryAction = Class(name="pcm::av::av::seff::reliability::av::av::RecoveryAction")
pcm_av_av_seff_reliability_av_av_FailureHandlingEntity = Class(name="pcm::av::av::seff::reliability::av::av::FailureHandlingEntity")
pcm_av_av_qosannotations_av_av_SpecifiedQoSAnnotation = Class(name="pcm::av::av::qosannotations::av::av::SpecifiedQoSAnnotation")
System = Class(name="System")
SpecifiedQoSAnnotation = Class(name="SpecifiedQoSAnnotation")
pcm_av_av_qosannotations_av_av_SpecifiedOutputParameterAbstraction = Class(name="pcm::av::av::qosannotations::av::av::SpecifiedOutputParameterAbstraction")
pcm_av_av_qos_performance_av_av_SystemSpecifiedExecutionTime = Class(name="pcm::av::av::qos::performance::av::av::SystemSpecifiedExecutionTime")
SpecifiedExecutionTime = Class(name="SpecifiedExecutionTime")
QoSAnnotations = Class(name="QoSAnnotations")
pcm_av_av_qosannotations_av_av_QoSAnnotations = Class(name="pcm::av::av::qosannotations::av::av::QoSAnnotations")
pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation = Class(name="pcm::av::av::qos::reliability::av::av::SpecifiedReliabilityAnnotation")
ExternalFailureOccurrenceDescription = Class(name="ExternalFailureOccurrenceDescription")
pcm_av_av_system_av_av_System = Class(name="pcm::av::av::system::av::av::System")
pcm_av_av_qos_performance_av_av_SpecifiedExecutionTime = Class(name="pcm::av::av::qos::performance::av::av::SpecifiedExecutionTime")
pcm_av_av_qos_performance_av_av_ComponentSpecifiedExecutionTime = Class(name="pcm::av::av::qos::performance::av::av::ComponentSpecifiedExecutionTime")
LinkingResource = Class(name="LinkingResource")
ResourceContainer = Class(name="ResourceContainer")
pcm_av_av_resourceenvironment_av_av_LinkingResource = Class(name="pcm::av::av::resourceenvironment::av::av::LinkingResource")
ResourceEnvironment = Class(name="ResourceEnvironment")
pcm_av_av_resourceenvironment_av_av_ResourceContainer = Class(name="pcm::av::av::resourceenvironment::av::av::ResourceContainer")
pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification = Class(name="pcm::av::av::resourceenvironment::av::av::ProcessingResourceSpecification")
pcm_av_av_resourceenvironment_av_av_ResourceEnvironment = Class(name="pcm::av::av::resourceenvironment::av::av::ResourceEnvironment")
pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification = Class(name="pcm::av::av::resourceenvironment::av::av::CommunicationLinkResourceSpecification")
pcm_av_av_allocation_av_av_AllocationContext = Class(name="pcm::av::av::allocation::av::av::AllocationContext")
AllocationContext = Class(name="AllocationContext")
pcm_av_av_subsystem_av_av_SubSystem = Class(name="pcm::av::av::subsystem::av::av::SubSystem")
repository_av_av_RepositoryComponent = Class(name="repository::av::av::RepositoryComponent")
pcm_av_av_completions_av_av_Completion = Class(name="pcm::av::av::completions::av::av::Completion")
pcm_av_av_completions_av_av_CompletionRepository = Class(name="pcm::av::av::completions::av::av::CompletionRepository")
Allocation = Class(name="Allocation")
pcm_av_av_allocation_av_av_Allocation = Class(name="pcm::av::av::allocation::av::av::Allocation")
Completion = Class(name="Completion")
pcm_av_av_completions_av_av_DelegatingExternalCallAction = Class(name="pcm::av::av::completions::av::av::DelegatingExternalCallAction")
ExternalCallAction = Class(name="ExternalCallAction")
pcm_av_av_completions_av_av_NetworkDemandParametricResourceDemand = Class(name="pcm::av::av::completions::av::av::NetworkDemandParametricResourceDemand")
ParametricResourceDemand = Class(name="ParametricResourceDemand")

# pcm_av_av_DummyClass class attributes and methods

# pcm_av_av_AdviceAdvice class attributes and methods

# pcm_av_av_EObject class attributes and methods

# pcm_av_av_GlobalScopeGlobalScope class attributes and methods

# pcm_av_av_PerJoinPointScopePerJoinPointScope class attributes and methods

# pcm_av_av_Advice class attributes and methods

# ClosedWorkload class attributes and methods

# PassiveResource class attributes and methods

# VariableCharacterisation class attributes and methods

# seff_performance_av_av_InfrastructureCall class attributes and methods

# seff_performance_av_av_ResourceCall class attributes and methods

# seff_performance_av_av_ParametricResourceDemand class attributes and methods

# LoopAction class attributes and methods

# GuardedBranchTransition class attributes and methods

# qos_performance_av_av_SpecifiedExecutionTime class attributes and methods

# composition_av_av_EventChannelSinkConnector class attributes and methods

# composition_av_av_AssemblyEventConnector class attributes and methods

# Loop class attributes and methods

# OpenWorkload class attributes and methods

# pcm_av_av_GlobalScope class attributes and methods

# pcm_av_av_PerJoinPointScope class attributes and methods

# pcm_av_av_core_av_av_PCMRandomVariable class attributes and methods
pcm_av_av_core_av_av_PCMRandomVariable_m_SpecificationMustNotBeNULL: Method = Method(name="SpecificationMustNotBeNULL", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_core_av_av_PCMRandomVariable.methods={pcm_av_av_core_av_av_PCMRandomVariable_m_SpecificationMustNotBeNULL}

# RandomVariable class attributes and methods

# ResourceInterface class attributes and methods

# pcm_av_av_entity_av_av_InterfaceProvidingRequiringEntity class attributes and methods

# entity_av_av_InterfaceProvidingEntity class attributes and methods

# entity_av_av_InterfaceRequiringEntity class attributes and methods

# pcm_av_av_entity_av_av_InterfaceProvidingEntity class attributes and methods

# Entity class attributes and methods

# ProvidedRole class attributes and methods

# pcm_av_av_entity_av_av_InterfaceRequiringEntity class attributes and methods

# entity_av_av_Entity class attributes and methods

# entity_av_av_ResourceInterfaceRequiringEntity class attributes and methods

# RequiredRole class attributes and methods

# pcm_av_av_entity_av_av_ResourceInterfaceRequiringEntity class attributes and methods

# entity_av_av_ResourceRequiredRole class attributes and methods

# pcm_av_av_entity_av_av_ResourceRequiredRole class attributes and methods

# pcm_av_av_entity_av_av_ResourceInterfaceProvidingEntity class attributes and methods

# entity_av_av_ResourceProvidedRole class attributes and methods

# Delay class attributes and methods

# CommunicationLinkResourceSpecification class attributes and methods

# ProcessingResourceSpecification class attributes and methods

# pcm_av_av_entity_av_av_ResourceProvidedRole class attributes and methods

# Role class attributes and methods

# entity_av_av_ResourceInterfaceProvidingEntity class attributes and methods

# pcm_av_av_composition_av_av_DelegationConnector class attributes and methods

# Connector class attributes and methods

# pcm_av_av_composition_av_av_Connector class attributes and methods

# pcm_av_av_composition_av_av_ComposedStructure class attributes and methods
pcm_av_av_composition_av_av_ComposedStructure_m_MultipleConnectorsConstraint: Method = Method(name="MultipleConnectorsConstraint", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_composition_av_av_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors: Method = Method(name="MultipleConnectorsConstraintForAssemblyConnectors", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_composition_av_av_ComposedStructure.methods={pcm_av_av_composition_av_av_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors, pcm_av_av_composition_av_av_ComposedStructure_m_MultipleConnectorsConstraint}

# composition_av_av_AssemblyContext class attributes and methods

# composition_av_av_ResourceRequiredDelegationConnector class attributes and methods

# composition_av_av_EventChannel class attributes and methods

# pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity class attributes and methods
pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound: Method = Method(name="ProvidedRolesMustBeBound", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity.methods={pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound}

# composition_av_av_ComposedStructure class attributes and methods

# entity_av_av_InterfaceProvidingRequiringEntity class attributes and methods

# pcm_av_av_entity_av_av_NamedElement class attributes and methods
pcm_av_av_entity_av_av_NamedElement_entityName: Property = Property(name="entityName", type=StringType)
pcm_av_av_entity_av_av_NamedElement.attributes={pcm_av_av_entity_av_av_NamedElement_entityName}

# pcm_av_av_entity_av_av_ResourceInterfaceProvidingRequiringEntity class attributes and methods

# pcm_av_av_entity_av_av_Entity class attributes and methods

# Identifier class attributes and methods

# entity_av_av_NamedElement class attributes and methods

# pcm_av_av_composition_av_av_ResourceRequiredDelegationConnector class attributes and methods

# pcm_av_av_composition_av_av_EventChannel class attributes and methods

# EventGroup class attributes and methods

# composition_av_av_EventChannelSourceConnector class attributes and methods

# pcm_av_av_composition_av_av_EventChannelSourceConnector class attributes and methods

# SourceRole class attributes and methods

# pcm_av_av_composition_av_av_EventChannelSinkConnector class attributes and methods

# composition_av_av_Connector class attributes and methods

# OperationProvidedRole class attributes and methods

# pcm_av_av_composition_av_av_RequiredDelegationConnector class attributes and methods
pcm_av_av_composition_av_av_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_composition_av_av_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_composition_av_av_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector: Method = Method(name="RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_composition_av_av_RequiredDelegationConnector.methods={pcm_av_av_composition_av_av_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure, pcm_av_av_composition_av_av_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector, pcm_av_av_composition_av_av_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame}

# SinkRole class attributes and methods

# PCMRandomVariable class attributes and methods

# pcm_av_av_composition_av_av_ProvidedDelegationConnector class attributes and methods
pcm_av_av_composition_av_av_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_composition_av_av_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_composition_av_av_ProvidedDelegationConnector.methods={pcm_av_av_composition_av_av_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame, pcm_av_av_composition_av_av_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure}

# DelegationConnector class attributes and methods

# pcm_av_av_composition_av_av_AssemblyEventConnector class attributes and methods

# OperationRequiredRole class attributes and methods

# pcm_av_av_composition_av_av_AssemblyConnector class attributes and methods
pcm_av_av_composition_av_av_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_composition_av_av_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch: Method = Method(name="AssemblyConnectorsReferencedInterfacesMustMatch", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_composition_av_av_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_composition_av_av_AssemblyConnector.methods={pcm_av_av_composition_av_av_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch, pcm_av_av_composition_av_av_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch, pcm_av_av_composition_av_av_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch}

# pcm_av_av_composition_av_av_AssemblyInfrastructureConnector class attributes and methods

# InfrastructureProvidedRole class attributes and methods

# InfrastructureRequiredRole class attributes and methods

# pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector class attributes and methods

# pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector class attributes and methods

# pcm_av_av_composition_av_av_RequiredResourceDelegationConnector class attributes and methods

# pcm_av_av_composition_av_av_SourceDelegationConnector class attributes and methods

# pcm_av_av_composition_av_av_SinkDelegationConnector class attributes and methods

# VariableUsage class attributes and methods

# pcm_av_av_usagemodel_av_av_Workload class attributes and methods

# UsageScenario class attributes and methods

# pcm_av_av_usagemodel_av_av_UsageScenario class attributes and methods

# UsageModel class attributes and methods

# ScenarioBehaviour class attributes and methods

# Workload class attributes and methods

# pcm_av_av_usagemodel_av_av_UserData class attributes and methods

# pcm_av_av_usagemodel_av_av_UsageModel class attributes and methods

# pcm_av_av_composition_av_av_AssemblyContext class attributes and methods

# RepositoryComponent class attributes and methods

# UserData class attributes and methods

# pcm_av_av_usagemodel_av_av_EntryLevelSystemCall class attributes and methods
pcm_av_av_usagemodel_av_av_EntryLevelSystemCall_priority: Property = Property(name="priority", type=IntegerType)
pcm_av_av_usagemodel_av_av_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem: Method = Method(name="EntryLevelSystemCallMustReferenceProvidedRoleOfASystem", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_usagemodel_av_av_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole: Method = Method(name="EntryLevelSystemCallSignatureMustMatchItsProvidedRole", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_usagemodel_av_av_EntryLevelSystemCall.attributes={pcm_av_av_usagemodel_av_av_EntryLevelSystemCall_priority}
pcm_av_av_usagemodel_av_av_EntryLevelSystemCall.methods={pcm_av_av_usagemodel_av_av_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem, pcm_av_av_usagemodel_av_av_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole}

# AbstractUserAction class attributes and methods

# OperationSignature class attributes and methods

# BranchTransition class attributes and methods

# pcm_av_av_usagemodel_av_av_BranchTransition class attributes and methods
pcm_av_av_usagemodel_av_av_BranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_av_av_usagemodel_av_av_BranchTransition.attributes={pcm_av_av_usagemodel_av_av_BranchTransition_branchProbability}

# pcm_av_av_usagemodel_av_av_AbstractUserAction class attributes and methods

# pcm_av_av_usagemodel_av_av_ScenarioBehaviour class attributes and methods
pcm_av_av_usagemodel_av_av_ScenarioBehaviour_m_Exactlyonestart: Method = Method(name="Exactlyonestart", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_usagemodel_av_av_ScenarioBehaviour_m_Exactlyonestop: Method = Method(name="Exactlyonestop", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_usagemodel_av_av_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor: Method = Method(name="EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_usagemodel_av_av_ScenarioBehaviour.methods={pcm_av_av_usagemodel_av_av_ScenarioBehaviour_m_Exactlyonestop, pcm_av_av_usagemodel_av_av_ScenarioBehaviour_m_Exactlyonestart, pcm_av_av_usagemodel_av_av_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor}

# pcm_av_av_usagemodel_av_av_Stop class attributes and methods
pcm_av_av_usagemodel_av_av_Stop_m_StopHasNoSuccessor: Method = Method(name="StopHasNoSuccessor", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_usagemodel_av_av_Stop.methods={pcm_av_av_usagemodel_av_av_Stop_m_StopHasNoSuccessor}

# pcm_av_av_usagemodel_av_av_Start class attributes and methods
pcm_av_av_usagemodel_av_av_Start_m_StartHasNoPredecessor: Method = Method(name="StartHasNoPredecessor", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_usagemodel_av_av_Start.methods={pcm_av_av_usagemodel_av_av_Start_m_StartHasNoPredecessor}

# pcm_av_av_usagemodel_av_av_OpenWorkload class attributes and methods
pcm_av_av_usagemodel_av_av_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified: Method = Method(name="InterArrivalTimeInOpenWorkloadNeedsToBeSpecified", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_usagemodel_av_av_OpenWorkload.methods={pcm_av_av_usagemodel_av_av_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified}

# Branch class attributes and methods

# pcm_av_av_usagemodel_av_av_Branch class attributes and methods
pcm_av_av_usagemodel_av_av_Branch_m_AllBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_usagemodel_av_av_Branch.methods={pcm_av_av_usagemodel_av_av_Branch_m_AllBranchProbabilitiesMustSumUpTo1}

# pcm_av_av_usagemodel_av_av_Loop class attributes and methods

# pcm_av_av_repository_av_av_PassiveResource class attributes and methods

# BasicComponent class attributes and methods

# ResourceTimeoutFailureType class attributes and methods

# pcm_av_av_repository_av_av_BasicComponent class attributes and methods
pcm_av_av_repository_av_av_BasicComponent_m_NoSeffTypeUsedTwice: Method = Method(name="NoSeffTypeUsedTwice", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_repository_av_av_BasicComponent_m_ProvideSameInterfacesAsImplementationType: Method = Method(name="ProvideSameInterfacesAsImplementationType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_repository_av_av_BasicComponent_m_RequireSameInterfacesAsImplementationType: Method = Method(name="RequireSameInterfacesAsImplementationType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_repository_av_av_BasicComponent.methods={pcm_av_av_repository_av_av_BasicComponent_m_NoSeffTypeUsedTwice, pcm_av_av_repository_av_av_BasicComponent_m_ProvideSameInterfacesAsImplementationType, pcm_av_av_repository_av_av_BasicComponent_m_RequireSameInterfacesAsImplementationType}

# ImplementationComponentType class attributes and methods

# pcm_av_av_usagemodel_av_av_Delay class attributes and methods

# pcm_av_av_usagemodel_av_av_ClosedWorkload class attributes and methods
pcm_av_av_usagemodel_av_av_ClosedWorkload_population: Property = Property(name="population", type=IntegerType)
pcm_av_av_usagemodel_av_av_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified: Method = Method(name="ThinkTimeInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_usagemodel_av_av_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified: Method = Method(name="PopulationInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_usagemodel_av_av_ClosedWorkload.attributes={pcm_av_av_usagemodel_av_av_ClosedWorkload_population}
pcm_av_av_usagemodel_av_av_ClosedWorkload.methods={pcm_av_av_usagemodel_av_av_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified, pcm_av_av_usagemodel_av_av_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified}

# pcm_av_av_repository_av_av_ImplementationComponentType class attributes and methods
pcm_av_av_repository_av_av_ImplementationComponentType_componentType: Property = Property(name="componentType", type=StringType)
pcm_av_av_repository_av_av_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType: Method = Method(name="RequiredInterfacesHaveToConformToCompleteType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_repository_av_av_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType: Method = Method(name="providedInterfacesHaveToConformToCompleteType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_repository_av_av_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType: Method = Method(name="ProvidedInterfaceHaveToConformToComponentType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_repository_av_av_ImplementationComponentType.attributes={pcm_av_av_repository_av_av_ImplementationComponentType_componentType}
pcm_av_av_repository_av_av_ImplementationComponentType.methods={pcm_av_av_repository_av_av_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType, pcm_av_av_repository_av_av_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType, pcm_av_av_repository_av_av_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType}

# CompleteComponentType class attributes and methods

# ServiceEffectSpecification class attributes and methods

# InfrastructureSignature class attributes and methods

# EventType class attributes and methods

# ResourceSignature class attributes and methods

# pcm_av_av_repository_av_av_DataType class attributes and methods

# pcm_av_av_repository_av_av_Repository class attributes and methods
pcm_av_av_repository_av_av_Repository_repositoryDescription: Property = Property(name="repositoryDescription", type=StringType)
pcm_av_av_repository_av_av_Repository.attributes={pcm_av_av_repository_av_av_Repository_repositoryDescription}

# Interface class attributes and methods

# pcm_av_av_repository_av_av_RepositoryComponent class attributes and methods

# InterfaceProvidingRequiringEntity class attributes and methods

# Repository class attributes and methods

# pcm_av_av_repository_av_av_ProvidedRole class attributes and methods

# pcm_av_av_repository_av_av_Parameter class attributes and methods
pcm_av_av_repository_av_av_Parameter_parameterName: Property = Property(name="parameterName", type=StringType)
pcm_av_av_repository_av_av_Parameter_modifier__Parameter: Property = Property(name="modifier__Parameter", type=StringType)
pcm_av_av_repository_av_av_Parameter.attributes={pcm_av_av_repository_av_av_Parameter_parameterName, pcm_av_av_repository_av_av_Parameter_modifier__Parameter}

# DataType class attributes and methods

# pcm_av_av_repository_av_av_Interface class attributes and methods
pcm_av_av_repository_av_av_Interface_m_NoProtocolTypeIDUsedTwice: Method = Method(name="NoProtocolTypeIDUsedTwice", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_repository_av_av_Interface.methods={pcm_av_av_repository_av_av_Interface_m_NoProtocolTypeIDUsedTwice}

# Protocol class attributes and methods

# FailureType class attributes and methods

# pcm_av_av_repository_av_av_EventGroup class attributes and methods

# pcm_av_av_repository_av_av_EventType class attributes and methods

# Signature class attributes and methods

# pcm_av_av_repository_av_av_Signature class attributes and methods

# ExceptionType class attributes and methods

# pcm_av_av_repository_av_av_ExceptionType class attributes and methods
pcm_av_av_repository_av_av_ExceptionType_exceptionName: Property = Property(name="exceptionName", type=StringType)
pcm_av_av_repository_av_av_ExceptionType_exceptionMessage: Property = Property(name="exceptionMessage", type=StringType)
pcm_av_av_repository_av_av_ExceptionType.attributes={pcm_av_av_repository_av_av_ExceptionType_exceptionName, pcm_av_av_repository_av_av_ExceptionType_exceptionMessage}

# RequiredCharacterisation class attributes and methods

# pcm_av_av_repository_av_av_RequiredCharacterisation class attributes and methods
pcm_av_av_repository_av_av_RequiredCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_av_av_repository_av_av_RequiredCharacterisation.attributes={pcm_av_av_repository_av_av_RequiredCharacterisation_type}

# Parameter class attributes and methods

# pcm_av_av_repository_av_av_OperationSignature class attributes and methods
pcm_av_av_repository_av_av_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature: Method = Method(name="ParameterNamesHaveToBeUniqueForASignature", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_repository_av_av_OperationSignature.methods={pcm_av_av_repository_av_av_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature}

# OperationInterface class attributes and methods

# pcm_av_av_repository_av_av_OperationInterface class attributes and methods
pcm_av_av_repository_av_av_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface: Method = Method(name="SignaturesHaveToBeUniqueForAnInterface", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_repository_av_av_OperationInterface.methods={pcm_av_av_repository_av_av_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface}

# pcm_av_av_repository_av_av_InfrastructureSignature class attributes and methods

# InfrastructureInterface class attributes and methods

# pcm_av_av_repository_av_av_InfrastructureInterface class attributes and methods

# pcm_av_av_repository_av_av_InfrastructureRequiredRole class attributes and methods

# pcm_av_av_repository_av_av_RequiredRole class attributes and methods

# pcm_av_av_repository_av_av_SinkRole class attributes and methods

# pcm_av_av_repository_av_av_OperationProvidedRole class attributes and methods

# pcm_av_av_repository_av_av_InfrastructureProvidedRole class attributes and methods

# pcm_av_av_repository_av_av_CompleteComponentType class attributes and methods
pcm_av_av_repository_av_av_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_repository_av_av_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2: Method = Method(name="providedInterfacesHaveToConformToProvidedType2", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_repository_av_av_CompleteComponentType.methods={pcm_av_av_repository_av_av_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2, pcm_av_av_repository_av_av_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType}

# pcm_av_av_repository_av_av_OperationRequiredRole class attributes and methods

# pcm_av_av_repository_av_av_SourceRole class attributes and methods

# pcm_av_av_repository_av_av_ProvidesComponentType class attributes and methods
pcm_av_av_repository_av_av_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_repository_av_av_ProvidesComponentType.methods={pcm_av_av_repository_av_av_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType}

# pcm_av_av_repository_av_av_CompositeComponent class attributes and methods
pcm_av_av_repository_av_av_CompositeComponent_m_ProvideSameInterfaces: Method = Method(name="ProvideSameInterfaces", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_repository_av_av_CompositeComponent_m_RequireSameInterfaces: Method = Method(name="RequireSameInterfaces", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_repository_av_av_CompositeComponent.methods={pcm_av_av_repository_av_av_CompositeComponent_m_ProvideSameInterfaces, pcm_av_av_repository_av_av_CompositeComponent_m_RequireSameInterfaces}

# entity_av_av_ComposedProvidingRequiringEntity class attributes and methods

# repository_av_av_ImplementationComponentType class attributes and methods

# pcm_av_av_repository_av_av_PrimitiveDataType class attributes and methods
pcm_av_av_repository_av_av_PrimitiveDataType_type: Property = Property(name="type", type=StringType)
pcm_av_av_repository_av_av_PrimitiveDataType.attributes={pcm_av_av_repository_av_av_PrimitiveDataType_type}

# ProvidesComponentType class attributes and methods

# CompositeDataType class attributes and methods

# InnerDeclaration class attributes and methods

# pcm_av_av_repository_av_av_InnerDeclaration class attributes and methods

# NamedElement class attributes and methods

# pcm_av_av_repository_av_av_Role class attributes and methods

# pcm_av_av_resourcetype_av_av_ResourceSignature class attributes and methods
pcm_av_av_resourcetype_av_av_ResourceSignature_resourceServiceId: Property = Property(name="resourceServiceId", type=IntegerType)
pcm_av_av_resourcetype_av_av_ResourceSignature.attributes={pcm_av_av_resourcetype_av_av_ResourceSignature_resourceServiceId}

# pcm_av_av_resourcetype_av_av_ProcessingResourceType class attributes and methods

# ResourceType class attributes and methods

# HardwareInducedFailureType class attributes and methods

# pcm_av_av_resourcetype_av_av_ResourceType class attributes and methods

# UnitCarryingElement class attributes and methods

# pcm_av_av_repository_av_av_CollectionDataType class attributes and methods

# repository_av_av_DataType class attributes and methods

# pcm_av_av_repository_av_av_CompositeDataType class attributes and methods

# pcm_av_av_resourcetype_av_av_CommunicationLinkResourceType class attributes and methods

# NetworkInducedFailureType class attributes and methods

# pcm_av_av_resourcetype_av_av_ResourceInterface class attributes and methods

# pcm_av_av_protocol_av_av_Protocol class attributes and methods
pcm_av_av_protocol_av_av_Protocol_protocolTypeID: Property = Property(name="protocolTypeID", type=StringType)
pcm_av_av_protocol_av_av_Protocol.attributes={pcm_av_av_protocol_av_av_Protocol_protocolTypeID}

# pcm_av_av_parameter_av_av_VariableUsage class attributes and methods

# CallAction class attributes and methods

# SynchronisationPoint class attributes and methods

# CallReturnAction class attributes and methods

# ResourceRepository class attributes and methods

# pcm_av_av_resourcetype_av_av_ResourceRepository class attributes and methods

# SchedulingPolicy class attributes and methods

# pcm_av_av_resourcetype_av_av_SchedulingPolicy class attributes and methods

# pcm_av_av_parameter_av_av_CharacterisedVariable class attributes and methods
pcm_av_av_parameter_av_av_CharacterisedVariable_characterisationType: Property = Property(name="characterisationType", type=StringType)
pcm_av_av_parameter_av_av_CharacterisedVariable.attributes={pcm_av_av_parameter_av_av_CharacterisedVariable_characterisationType}

# Variable class attributes and methods

# pcm_av_av_reliability_av_av_FailureOccurrenceDescription class attributes and methods
pcm_av_av_reliability_av_av_FailureOccurrenceDescription_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_av_av_reliability_av_av_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange: Method = Method(name="EnsureValidFailureProbabilityRange", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_reliability_av_av_FailureOccurrenceDescription.attributes={pcm_av_av_reliability_av_av_FailureOccurrenceDescription_failureProbability}
pcm_av_av_reliability_av_av_FailureOccurrenceDescription.methods={pcm_av_av_reliability_av_av_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange}

# SetVariableAction class attributes and methods

# SpecifiedOutputParameterAbstraction class attributes and methods

# EntryLevelSystemCall class attributes and methods

# parameter_av_av_pcm_av_av_AbstractNamedReference class attributes and methods

# pcm_av_av_parameter_av_av_VariableCharacterisation class attributes and methods
pcm_av_av_parameter_av_av_VariableCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_av_av_parameter_av_av_VariableCharacterisation.attributes={pcm_av_av_parameter_av_av_VariableCharacterisation_type}

# ProcessingResourceType class attributes and methods

# pcm_av_av_reliability_av_av_SoftwareInducedFailureType class attributes and methods

# InternalFailureOccurrenceDescription class attributes and methods

# pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription class attributes and methods
pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription.methods={pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription}

# FailureOccurrenceDescription class attributes and methods

# InternalAction class attributes and methods

# SoftwareInducedFailureType class attributes and methods

# pcm_av_av_reliability_av_av_NetworkInducedFailureType class attributes and methods
pcm_av_av_reliability_av_av_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType: Method = Method(name="NetworkInducedFailureTypeHasCommunicationLinkResourceType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_reliability_av_av_NetworkInducedFailureType.methods={pcm_av_av_reliability_av_av_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType}

# pcm_av_av_reliability_av_av_HardwareInducedFailureType class attributes and methods
pcm_av_av_reliability_av_av_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType: Method = Method(name="HardwareInducedFailureTypeHasProcessingResourceType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_reliability_av_av_HardwareInducedFailureType.methods={pcm_av_av_reliability_av_av_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType}

# qos_reliability_av_av_SpecifiedReliabilityAnnotation class attributes and methods

# pcm_av_av_reliability_av_av_ResourceTimeoutFailureType class attributes and methods

# pcm_av_av_reliability_av_av_FailureType class attributes and methods

# pcm_av_av_seff_av_av_StopAction class attributes and methods
pcm_av_av_seff_av_av_StopAction_m_StopActionSuccessorMustNotBeDefined: Method = Method(name="StopActionSuccessorMustNotBeDefined", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_seff_av_av_StopAction.methods={pcm_av_av_seff_av_av_StopAction_m_StopActionSuccessorMustNotBeDefined}

# AbstractInternalControlFlowAction class attributes and methods

# CommunicationLinkResourceType class attributes and methods

# pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription class attributes and methods
pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription.methods={pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription}

# ResourceDemandingBehaviour class attributes and methods

# pcm_av_av_seff_av_av_ResourceDemandingBehaviour class attributes and methods
pcm_av_av_seff_av_av_ResourceDemandingBehaviour_m_ExactlyOneStopAction: Method = Method(name="ExactlyOneStopAction", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_seff_av_av_ResourceDemandingBehaviour_m_ExactlyOneStartAction: Method = Method(name="ExactlyOneStartAction", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_seff_av_av_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor: Method = Method(name="EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_seff_av_av_ResourceDemandingBehaviour.methods={pcm_av_av_seff_av_av_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor, pcm_av_av_seff_av_av_ResourceDemandingBehaviour_m_ExactlyOneStartAction, pcm_av_av_seff_av_av_ResourceDemandingBehaviour_m_ExactlyOneStopAction}

# AbstractLoopAction class attributes and methods

# AbstractBranchTransition class attributes and methods

# pcm_av_av_seff_av_av_AbstractInternalControlFlowAction class attributes and methods

# AbstractAction class attributes and methods

# pcm_av_av_seff_av_av_AbstractAction class attributes and methods

# pcm_av_av_seff_av_av_CallAction class attributes and methods

# pcm_av_av_seff_av_av_StartAction class attributes and methods
pcm_av_av_seff_av_av_StartAction_m_StartActionPredecessorMustNotBeDefined: Method = Method(name="StartActionPredecessorMustNotBeDefined", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_seff_av_av_StartAction.methods={pcm_av_av_seff_av_av_StartAction_m_StartActionPredecessorMustNotBeDefined}

# pcm_av_av_seff_av_av_ServiceEffectSpecification class attributes and methods
pcm_av_av_seff_av_av_ServiceEffectSpecification_seffTypeID: Property = Property(name="seffTypeID", type=StringType)
pcm_av_av_seff_av_av_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole: Method = Method(name="ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_seff_av_av_ServiceEffectSpecification.attributes={pcm_av_av_seff_av_av_ServiceEffectSpecification_seffTypeID}
pcm_av_av_seff_av_av_ServiceEffectSpecification.methods={pcm_av_av_seff_av_av_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole}

# pcm_av_av_seff_av_av_AbstractLoopAction class attributes and methods

# pcm_av_av_seff_av_av_AbstractBranchTransition class attributes and methods

# BranchAction class attributes and methods

# pcm_av_av_seff_av_av_BranchAction class attributes and methods
pcm_av_av_seff_av_av_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions: Method = Method(name="EitherGuardedBranchesOrProbabilisiticBranchTransitions", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_seff_av_av_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllProbabilisticBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_seff_av_av_BranchAction.methods={pcm_av_av_seff_av_av_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1, pcm_av_av_seff_av_av_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions}

# pcm_av_av_seff_av_av_ResourceDemandingInternalBehaviour class attributes and methods

# ResourceDemandingSEFF class attributes and methods

# pcm_av_av_seff_av_av_ReleaseAction class attributes and methods

# pcm_av_av_seff_av_av_LoopAction class attributes and methods

# pcm_av_av_seff_av_av_ForkAction class attributes and methods

# ForkedBehaviour class attributes and methods

# pcm_av_av_seff_av_av_ForkedBehaviour class attributes and methods

# ForkAction class attributes and methods

# pcm_av_av_seff_av_av_SynchronisationPoint class attributes and methods

# pcm_av_av_seff_av_av_ResourceDemandingSEFF class attributes and methods

# seff_av_av_ServiceEffectSpecification class attributes and methods

# seff_av_av_ResourceDemandingBehaviour class attributes and methods

# ResourceDemandingInternalBehaviour class attributes and methods

# pcm_av_av_seff_av_av_CallReturnAction class attributes and methods

# pcm_av_av_seff_av_av_ProbabilisticBranchTransition class attributes and methods
pcm_av_av_seff_av_av_ProbabilisticBranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_av_av_seff_av_av_ProbabilisticBranchTransition.attributes={pcm_av_av_seff_av_av_ProbabilisticBranchTransition_branchProbability}

# pcm_av_av_seff_av_av_AcquireAction class attributes and methods
pcm_av_av_seff_av_av_AcquireAction_timeout: Property = Property(name="timeout", type=BooleanType)
pcm_av_av_seff_av_av_AcquireAction_timeoutValue: Property = Property(name="timeoutValue", type=FloatType)
pcm_av_av_seff_av_av_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative: Method = Method(name="TimeoutValueOfAcquireActionMustNotBeNegative", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_seff_av_av_AcquireAction.attributes={pcm_av_av_seff_av_av_AcquireAction_timeout, pcm_av_av_seff_av_av_AcquireAction_timeoutValue}
pcm_av_av_seff_av_av_AcquireAction.methods={pcm_av_av_seff_av_av_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative}

# pcm_av_av_seff_av_av_ExternalCallAction class attributes and methods
pcm_av_av_seff_av_av_ExternalCallAction_retryCount: Property = Property(name="retryCount", type=IntegerType)
pcm_av_av_seff_av_av_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer: Method = Method(name="OperationRequiredRoleMustBeReferencedByContainer", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_seff_av_av_ExternalCallAction_m_SignatureBelongsToRole: Method = Method(name="SignatureBelongsToRole", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_seff_av_av_ExternalCallAction.attributes={pcm_av_av_seff_av_av_ExternalCallAction_retryCount}
pcm_av_av_seff_av_av_ExternalCallAction.methods={pcm_av_av_seff_av_av_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer, pcm_av_av_seff_av_av_ExternalCallAction_m_SignatureBelongsToRole}

# seff_av_av_AbstractAction class attributes and methods

# seff_av_av_CallReturnAction class attributes and methods

# seff_reliability_av_av_FailureHandlingEntity class attributes and methods

# pcm_av_av_seff_av_av_SetVariableAction class attributes and methods

# pcm_av_av_seff_av_av_InternalCallAction class attributes and methods

# seff_av_av_CallAction class attributes and methods

# seff_av_av_AbstractInternalControlFlowAction class attributes and methods

# pcm_av_av_seff_av_av_EmitEventAction class attributes and methods

# pcm_av_av_seff_av_av_InternalAction class attributes and methods
pcm_av_av_seff_av_av_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_seff_av_av_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfInternalActionFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_seff_av_av_InternalAction.methods={pcm_av_av_seff_av_av_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1, pcm_av_av_seff_av_av_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed}

# pcm_av_av_seff_av_av_CollectionIteratorAction class attributes and methods

# pcm_av_av_seff_av_av_GuardedBranchTransition class attributes and methods

# pcm_av_av_seff_performance_av_av_ResourceCall class attributes and methods
pcm_av_av_seff_performance_av_av_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole: Method = Method(name="ResourceSignatureBelongsToResourceRequiredRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_seff_performance_av_av_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent: Method = Method(name="ResourceRequiredRoleMustBeReferencedByComponent", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_seff_performance_av_av_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_seff_performance_av_av_ResourceCall.methods={pcm_av_av_seff_performance_av_av_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole, pcm_av_av_seff_performance_av_av_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent, pcm_av_av_seff_performance_av_av_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction}

# pcm_av_av_seff_performance_av_av_InfrastructureCall class attributes and methods
pcm_av_av_seff_performance_av_av_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_seff_performance_av_av_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole: Method = Method(name="SignatureMustBelongToUsedRequiredRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_seff_performance_av_av_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent: Method = Method(name="ReferencedRequiredRoleMustBeRequiredByComponent", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_seff_performance_av_av_InfrastructureCall.methods={pcm_av_av_seff_performance_av_av_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction, pcm_av_av_seff_performance_av_av_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent, pcm_av_av_seff_performance_av_av_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole}

# pcm_av_av_seff_performance_av_av_ParametricResourceDemand class attributes and methods
pcm_av_av_seff_performance_av_av_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_seff_performance_av_av_ParametricResourceDemand.methods={pcm_av_av_seff_performance_av_av_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction}

# pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour class attributes and methods
pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor: Method = Method(name="RecoveryActionBehaviourHasOnlyOnePredecessor", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself: Method = Method(name="RecoveryActionBehaviourIsNotSuccessorOfItself", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes: Method = Method(name="SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour.methods={pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes, pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself, pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor}

# seff_reliability_av_av_RecoveryActionBehaviour class attributes and methods

# seff_reliability_av_av_RecoveryAction class attributes and methods

# pcm_av_av_seff_reliability_av_av_RecoveryAction class attributes and methods
pcm_av_av_seff_reliability_av_av_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet: Method = Method(name="PrimaryBehaviourOfRecoveryActionMustBeSet", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_seff_reliability_av_av_RecoveryAction.methods={pcm_av_av_seff_reliability_av_av_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet}

# pcm_av_av_seff_reliability_av_av_FailureHandlingEntity class attributes and methods

# pcm_av_av_qosannotations_av_av_SpecifiedQoSAnnotation class attributes and methods

# System class attributes and methods

# SpecifiedQoSAnnotation class attributes and methods

# pcm_av_av_qosannotations_av_av_SpecifiedOutputParameterAbstraction class attributes and methods

# pcm_av_av_qos_performance_av_av_SystemSpecifiedExecutionTime class attributes and methods
pcm_av_av_qos_performance_av_av_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem: Method = Method(name="SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_qos_performance_av_av_SystemSpecifiedExecutionTime.methods={pcm_av_av_qos_performance_av_av_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem}

# SpecifiedExecutionTime class attributes and methods

# QoSAnnotations class attributes and methods

# pcm_av_av_qosannotations_av_av_QoSAnnotations class attributes and methods
pcm_av_av_qosannotations_av_av_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed: Method = Method(name="MultipleReliabilityAnnotationsPerExternalCallNotAllowed", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_qosannotations_av_av_QoSAnnotations.methods={pcm_av_av_qosannotations_av_av_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed}

# pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation class attributes and methods
pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem: Method = Method(name="SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation.methods={pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1, pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed, pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem}

# ExternalFailureOccurrenceDescription class attributes and methods

# pcm_av_av_system_av_av_System class attributes and methods
pcm_av_av_system_av_av_System_m_SystemMustHaveAtLeastOneProvidedRole: Method = Method(name="SystemMustHaveAtLeastOneProvidedRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_av_system_av_av_System.methods={pcm_av_av_system_av_av_System_m_SystemMustHaveAtLeastOneProvidedRole}

# pcm_av_av_qos_performance_av_av_SpecifiedExecutionTime class attributes and methods

# pcm_av_av_qos_performance_av_av_ComponentSpecifiedExecutionTime class attributes and methods

# LinkingResource class attributes and methods

# ResourceContainer class attributes and methods

# pcm_av_av_resourceenvironment_av_av_LinkingResource class attributes and methods

# ResourceEnvironment class attributes and methods

# pcm_av_av_resourceenvironment_av_av_ResourceContainer class attributes and methods

# pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification class attributes and methods
pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification_MTTR: Property = Property(name="MTTR", type=FloatType)
pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification_MTTF: Property = Property(name="MTTF", type=FloatType)
pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification_requiredByContainer: Property = Property(name="requiredByContainer", type=BooleanType)
pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification_numberOfReplicas: Property = Property(name="numberOfReplicas", type=IntegerType)
pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification.attributes={pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification_MTTR, pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification_numberOfReplicas, pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification_requiredByContainer, pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification_MTTF}

# pcm_av_av_resourceenvironment_av_av_ResourceEnvironment class attributes and methods

# pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification class attributes and methods
pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification.attributes={pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification_failureProbability}

# pcm_av_av_allocation_av_av_AllocationContext class attributes and methods
pcm_av_av_allocation_av_av_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred: Method = Method(name="OneAssemblyContextOrOneEventChannelShouldBeReferred", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_allocation_av_av_AllocationContext.methods={pcm_av_av_allocation_av_av_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred}

# AllocationContext class attributes and methods

# pcm_av_av_subsystem_av_av_SubSystem class attributes and methods

# repository_av_av_RepositoryComponent class attributes and methods

# pcm_av_av_completions_av_av_Completion class attributes and methods

# pcm_av_av_completions_av_av_CompletionRepository class attributes and methods

# Allocation class attributes and methods

# pcm_av_av_allocation_av_av_Allocation class attributes and methods
pcm_av_av_allocation_av_av_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce: Method = Method(name="EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_allocation_av_av_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource: Method = Method(name="CommunicatingServersHaveToBeConnectedByLinkingResource", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_av_allocation_av_av_Allocation.methods={pcm_av_av_allocation_av_av_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce, pcm_av_av_allocation_av_av_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource}

# Completion class attributes and methods

# pcm_av_av_completions_av_av_DelegatingExternalCallAction class attributes and methods

# ExternalCallAction class attributes and methods

# pcm_av_av_completions_av_av_NetworkDemandParametricResourceDemand class attributes and methods

# ParametricResourceDemand class attributes and methods

# Relationships
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="pcm_av_av_EObject", type=pcm_av_av_AdviceAdvice, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_AdviceAdvice", type=pcm_av_av_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scopedObject1: BinaryAssociation = BinaryAssociation(
    name="scopedObject1",
    ends={
        Property(name="pcm_av_av_EObject2", type=pcm_av_av_GlobalScopeGlobalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_GlobalScopeGlobalScope", type=pcm_av_av_EObject, multiplicity=Multiplicity(0, 1))
    }
)
scopedObject3: BinaryAssociation = BinaryAssociation(
    name="scopedObject3",
    ends={
        Property(name="pcm_av_av_EObject4", type=pcm_av_av_PerJoinPointScopePerJoinPointScope, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_PerJoinPointScopePerJoinPointScope", type=pcm_av_av_EObject, multiplicity=Multiplicity(0, 1))
    }
)
children5: BinaryAssociation = BinaryAssociation(
    name="children5",
    ends={
        Property(name="pcm_av_av_EObject6", type=pcm_av_av_Advice, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_Advice", type=pcm_av_av_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
closedWorkload_PCMRandomVariable11: BinaryAssociation = BinaryAssociation(
    name="closedWorkload_PCMRandomVariable11",
    ends={
        Property(name="usagemodel_av_av", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ClosedWorkload", type=ClosedWorkload, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_capacity_PCMRandomVariable12: BinaryAssociation = BinaryAssociation(
    name="passiveResource_capacity_PCMRandomVariable12",
    ends={
        Property(name="repository_av_av", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
variableCharacterisation_Specification13: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_Specification13",
    ends={
        Property(name="parameter_av_av", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableCharacterisation", type=VariableCharacterisation, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureCall__PCMRandomVariable14: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__PCMRandomVariable14",
    ends={
        Property(name="seff_av_av", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_av_av", type=seff_performance_av_av_InfrastructureCall, multiplicity=Multiplicity(0, 1))
    }
)
resourceCall__PCMRandomVariable15: BinaryAssociation = BinaryAssociation(
    name="resourceCall__PCMRandomVariable15",
    ends={
        Property(name="seff_av_av17", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_av_av16", type=seff_performance_av_av_ResourceCall, multiplicity=Multiplicity(0, 1))
    }
)
parametricResourceDemand_PCMRandomVariable18: BinaryAssociation = BinaryAssociation(
    name="parametricResourceDemand_PCMRandomVariable18",
    ends={
        Property(name="seff_av_av20", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_av_av19", type=seff_performance_av_av_ParametricResourceDemand, multiplicity=Multiplicity(0, 1))
    }
)
loopAction_PCMRandomVariable21: BinaryAssociation = BinaryAssociation(
    name="loopAction_PCMRandomVariable21",
    ends={
        Property(name="seff_av_av22", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopAction", type=LoopAction, multiplicity=Multiplicity(0, 1))
    }
)
guardedBranchTransition_PCMRandomVariable23: BinaryAssociation = BinaryAssociation(
    name="guardedBranchTransition_PCMRandomVariable23",
    ends={
        Property(name="seff_av_av24", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="GuardedBranchTransition", type=GuardedBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
specifiedExecutionTime_PCMRandomVariable25: BinaryAssociation = BinaryAssociation(
    name="specifiedExecutionTime_PCMRandomVariable25",
    ends={
        Property(name="qosannotations_av_av", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="qos_performance_av_av", type=qos_performance_av_av_SpecifiedExecutionTime, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSinkConnector__FilterCondition26: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__FilterCondition26",
    ends={
        Property(name="core_av_av", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_av", type=composition_av_av_EventChannelSinkConnector, multiplicity=Multiplicity(0, 1))
    }
)
assemblyEventConnector__FilterCondition27: BinaryAssociation = BinaryAssociation(
    name="assemblyEventConnector__FilterCondition27",
    ends={
        Property(name="core_av_av29", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_av28", type=composition_av_av_AssemblyEventConnector, multiplicity=Multiplicity(0, 1))
    }
)
loop_LoopIteration30: BinaryAssociation = BinaryAssociation(
    name="loop_LoopIteration30",
    ends={
        Property(name="usagemodel_av_av31", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Loop", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
scopedObject7: BinaryAssociation = BinaryAssociation(
    name="scopedObject7",
    ends={
        Property(name="pcm_av_av_EObject8", type=pcm_av_av_GlobalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_GlobalScope", type=pcm_av_av_EObject, multiplicity=Multiplicity(1, 1))
    }
)
scopedObject9: BinaryAssociation = BinaryAssociation(
    name="scopedObject9",
    ends={
        Property(name="pcm_av_av_EObject10", type=pcm_av_av_PerJoinPointScope, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_PerJoinPointScope", type=pcm_av_av_EObject, multiplicity=Multiplicity(1, 1))
    }
)
resourceInterfaceProvidingEntity__ResourceProvidedRole42: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceProvidingEntity__ResourceProvidedRole42",
    ends={
        Property(name="core_av_av43", type=pcm_av_av_entity_av_av_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_av_av", type=entity_av_av_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
providedResourceInterface__ResourceProvidedRole44: BinaryAssociation = BinaryAssociation(
    name="providedResourceInterface__ResourceProvidedRole44",
    ends={
        Property(name="ResourceInterface", type=pcm_av_av_entity_av_av_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_entity_av_av_ResourceProvidedRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedRoles_InterfaceProvidingEntity45: BinaryAssociation = BinaryAssociation(
    name="providedRoles_InterfaceProvidingEntity45",
    ends={
        Property(name="repository_av_av46", type=pcm_av_av_entity_av_av_InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="ProvidedRole", type=ProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredRoles_InterfaceRequiringEntity47: BinaryAssociation = BinaryAssociation(
    name="requiredRoles_InterfaceRequiringEntity47",
    ends={
        Property(name="repository_av_av48", type=pcm_av_av_entity_av_av_InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="RequiredRole", type=RequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredRoles__ResourceInterfaceRequiringEntity49: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRoles__ResourceInterfaceRequiringEntity49",
    ends={
        Property(name="core_av_av51", type=pcm_av_av_entity_av_av_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_av_av50", type=entity_av_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredResourceInterface__ResourceRequiredRole52: BinaryAssociation = BinaryAssociation(
    name="requiredResourceInterface__ResourceRequiredRole52",
    ends={
        Property(name="ResourceInterface53", type=pcm_av_av_entity_av_av_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_entity_av_av_ResourceRequiredRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaceRequiringEntity__ResourceRequiredRole54: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceRequiringEntity__ResourceRequiredRole54",
    ends={
        Property(name="core_av_av56", type=pcm_av_av_entity_av_av_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_av_av55", type=entity_av_av_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
resourceProvidedRoles__ResourceInterfaceProvidingEntity57: BinaryAssociation = BinaryAssociation(
    name="resourceProvidedRoles__ResourceInterfaceProvidingEntity57",
    ends={
        Property(name="core_av_av59", type=pcm_av_av_entity_av_av_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_av_av58", type=entity_av_av_ResourceProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
openWorkload_PCMRandomVariable32: BinaryAssociation = BinaryAssociation(
    name="openWorkload_PCMRandomVariable32",
    ends={
        Property(name="usagemodel_av_av33", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="OpenWorkload", type=OpenWorkload, multiplicity=Multiplicity(0, 1))
    }
)
delay_TimeSpecification34: BinaryAssociation = BinaryAssociation(
    name="delay_TimeSpecification34",
    ends={
        Property(name="usagemodel_av_av35", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Delay", type=Delay, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecifcation_throughput_PCMRandomVariable36: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifcation_throughput_PCMRandomVariable36",
    ends={
        Property(name="resourceenvironment_av_av", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceSpecification_processingRate_PCMRandomVariable37: BinaryAssociation = BinaryAssociation(
    name="processingResourceSpecification_processingRate_PCMRandomVariable37",
    ends={
        Property(name="resourceenvironment_av_av38", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcessingResourceSpecification", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecification_latency_PCMRandomVariable39: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecification_latency_PCMRandomVariable39",
    ends={
        Property(name="resourceenvironment_av_av41", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceSpecification40", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure__Connector60: BinaryAssociation = BinaryAssociation(
    name="parentStructure__Connector60",
    ends={
        Property(name="core_av_av62", type=pcm_av_av_composition_av_av_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_av61", type=composition_av_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContexts__ComposedStructure63: BinaryAssociation = BinaryAssociation(
    name="assemblyContexts__ComposedStructure63",
    ends={
        Property(name="core_av_av65", type=pcm_av_av_composition_av_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_av64", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredDelegationConnectors_ComposedStructure66: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredDelegationConnectors_ComposedStructure66",
    ends={
        Property(name="core_av_av68", type=pcm_av_av_composition_av_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_av67", type=composition_av_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventChannel__ComposedStructure69: BinaryAssociation = BinaryAssociation(
    name="eventChannel__ComposedStructure69",
    ends={
        Property(name="core_av_av71", type=pcm_av_av_composition_av_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_av70", type=composition_av_av_EventChannel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerResourceRequiredRole_ResourceRequiredDelegationConnector75: BinaryAssociation = BinaryAssociation(
    name="innerResourceRequiredRole_ResourceRequiredDelegationConnector75",
    ends={
        Property(name="entity_av_av_ResourceRequiredRole", type=pcm_av_av_composition_av_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_ResourceRequiredDelegationConnector", type=entity_av_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerResourceRequiredRole_ResourceRequiredDelegationConnector76: BinaryAssociation = BinaryAssociation(
    name="outerResourceRequiredRole_ResourceRequiredDelegationConnector76",
    ends={
        Property(name="entity_av_av_ResourceRequiredRole78", type=pcm_av_av_composition_av_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_ResourceRequiredDelegationConnector77", type=entity_av_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure_ResourceRequiredDelegationConnector79: BinaryAssociation = BinaryAssociation(
    name="parentStructure_ResourceRequiredDelegationConnector79",
    ends={
        Property(name="core_av_av81", type=pcm_av_av_composition_av_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_av80", type=composition_av_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__EventChannel82: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventChannel82",
    ends={
        Property(name="EventGroup", type=pcm_av_av_composition_av_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_EventChannel", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSourceConnector__EventChannel83: BinaryAssociation = BinaryAssociation(
    name="eventChannelSourceConnector__EventChannel83",
    ends={
        Property(name="core_av_av85", type=pcm_av_av_composition_av_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_av84", type=composition_av_av_EventChannelSourceConnector, multiplicity=Multiplicity(0, 9999))
    }
)
eventChannelSinkConnector__EventChannel86: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__EventChannel86",
    ends={
        Property(name="core_av_av88", type=pcm_av_av_composition_av_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_av87", type=composition_av_av_EventChannelSinkConnector, multiplicity=Multiplicity(0, 9999))
    }
)
parentStructure__EventChannel89: BinaryAssociation = BinaryAssociation(
    name="parentStructure__EventChannel89",
    ends={
        Property(name="core_av_av91", type=pcm_av_av_composition_av_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_av90", type=composition_av_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EventChannelSourceRole92: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EventChannelSourceRole92",
    ends={
        Property(name="SourceRole", type=pcm_av_av_composition_av_av_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_EventChannelSourceConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__EventChannelSourceConnector93: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSourceConnector93",
    ends={
        Property(name="composition_av_av_AssemblyContext", type=pcm_av_av_composition_av_av_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_EventChannelSourceConnector94", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSourceConnector95: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSourceConnector95",
    ends={
        Property(name="core_av_av97", type=pcm_av_av_composition_av_av_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_av96", type=composition_av_av_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
connectors__ComposedStructure72: BinaryAssociation = BinaryAssociation(
    name="connectors__ComposedStructure72",
    ends={
        Property(name="core_av_av74", type=pcm_av_av_composition_av_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_av73", type=composition_av_av_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerProvidedRole_ProvidedDelegationConnector107: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole_ProvidedDelegationConnector107",
    ends={
        Property(name="OperationProvidedRole", type=pcm_av_av_composition_av_av_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_ProvidedDelegationConnector", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole_ProvidedDelegationConnector108: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole_ProvidedDelegationConnector108",
    ends={
        Property(name="OperationProvidedRole110", type=pcm_av_av_composition_av_av_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_ProvidedDelegationConnector109", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_ProvidedDelegationConnector111: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ProvidedDelegationConnector111",
    ends={
        Property(name="composition_av_av_AssemblyContext113", type=pcm_av_av_composition_av_av_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_ProvidedDelegationConnector112", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__EventChannelSinkConnector98: BinaryAssociation = BinaryAssociation(
    name="sinkRole__EventChannelSinkConnector98",
    ends={
        Property(name="SinkRole", type=pcm_av_av_composition_av_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_EventChannelSinkConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__EventChannelSinkConnector99: BinaryAssociation = BinaryAssociation(
    name="filterCondition__EventChannelSinkConnector99",
    ends={
        Property(name="core_av_av100", type=pcm_av_av_composition_av_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext__EventChannelSinkConnector101: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSinkConnector101",
    ends={
        Property(name="composition_av_av_AssemblyContext103", type=pcm_av_av_composition_av_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_EventChannelSinkConnector102", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSinkConnector104: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSinkConnector104",
    ends={
        Property(name="core_av_av106", type=pcm_av_av_composition_av_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_av105", type=composition_av_av_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext_AssemblyConnector121: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext_AssemblyConnector121",
    ends={
        Property(name="composition_av_av_AssemblyContext122", type=pcm_av_av_composition_av_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyConnector", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext_AssemblyConnector123: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext_AssemblyConnector123",
    ends={
        Property(name="composition_av_av_AssemblyContext125", type=pcm_av_av_composition_av_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyConnector124", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providedRole_AssemblyConnector126: BinaryAssociation = BinaryAssociation(
    name="providedRole_AssemblyConnector126",
    ends={
        Property(name="OperationProvidedRole128", type=pcm_av_av_composition_av_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyConnector127", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole_AssemblyConnector129: BinaryAssociation = BinaryAssociation(
    name="requiredRole_AssemblyConnector129",
    ends={
        Property(name="OperationRequiredRole131", type=pcm_av_av_composition_av_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyConnector130", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__AssemblyEventConnector132: BinaryAssociation = BinaryAssociation(
    name="sinkRole__AssemblyEventConnector132",
    ends={
        Property(name="SinkRole133", type=pcm_av_av_composition_av_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyEventConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__AssemblyEventConnector134: BinaryAssociation = BinaryAssociation(
    name="sourceRole__AssemblyEventConnector134",
    ends={
        Property(name="SourceRole136", type=pcm_av_av_composition_av_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyEventConnector135", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole_RequiredDelegationConnector114: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole_RequiredDelegationConnector114",
    ends={
        Property(name="OperationRequiredRole", type=pcm_av_av_composition_av_av_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_RequiredDelegationConnector", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole_RequiredDelegationConnector115: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole_RequiredDelegationConnector115",
    ends={
        Property(name="OperationRequiredRole117", type=pcm_av_av_composition_av_av_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_RequiredDelegationConnector116", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_RequiredDelegationConnector118: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_RequiredDelegationConnector118",
    ends={
        Property(name="composition_av_av_AssemblyContext120", type=pcm_av_av_composition_av_av_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_RequiredDelegationConnector119", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerSinkRole__SinkRole156: BinaryAssociation = BinaryAssociation(
    name="innerSinkRole__SinkRole156",
    ends={
        Property(name="SinkRole158", type=pcm_av_av_composition_av_av_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_SinkDelegationConnector157", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSinkRole__SinkRole159: BinaryAssociation = BinaryAssociation(
    name="outerSinkRole__SinkRole159",
    ends={
        Property(name="SinkRole161", type=pcm_av_av_composition_av_av_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_SinkDelegationConnector160", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
providedRole__AssemblyInfrastructureConnector162: BinaryAssociation = BinaryAssociation(
    name="providedRole__AssemblyInfrastructureConnector162",
    ends={
        Property(name="InfrastructureProvidedRole", type=pcm_av_av_composition_av_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyInfrastructureConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__AssemblyInfrastructureConnector163: BinaryAssociation = BinaryAssociation(
    name="requiredRole__AssemblyInfrastructureConnector163",
    ends={
        Property(name="InfrastructureRequiredRole", type=pcm_av_av_composition_av_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyInfrastructureConnector164", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext__AssemblyInfrastructureConnector165: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext__AssemblyInfrastructureConnector165",
    ends={
        Property(name="composition_av_av_AssemblyContext167", type=pcm_av_av_composition_av_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyInfrastructureConnector166", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext__AssemblyInfrastructureConnector168: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext__AssemblyInfrastructureConnector168",
    ends={
        Property(name="composition_av_av_AssemblyContext170", type=pcm_av_av_composition_av_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyInfrastructureConnector169", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole__ProvidedInfrastructureDelegationConnector171: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole__ProvidedInfrastructureDelegationConnector171",
    ends={
        Property(name="InfrastructureProvidedRole172", type=pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole__ProvidedInfrastructureDelegationConnector173: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole__ProvidedInfrastructureDelegationConnector173",
    ends={
        Property(name="InfrastructureProvidedRole175", type=pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector174", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__ProvidedInfrastructureDelegationConnector176: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__ProvidedInfrastructureDelegationConnector176",
    ends={
        Property(name="composition_av_av_AssemblyContext178", type=pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector177", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole__RequiredInfrastructureDelegationConnector179: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredInfrastructureDelegationConnector179",
    ends={
        Property(name="InfrastructureRequiredRole180", type=pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredInfrastructureDelegationConnector181: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredInfrastructureDelegationConnector181",
    ends={
        Property(name="InfrastructureRequiredRole183", type=pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector182", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredInfrastructureDelegationConnector184: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredInfrastructureDelegationConnector184",
    ends={
        Property(name="composition_av_av_AssemblyContext186", type=pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector185", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredResourceDelegationConnector187: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredResourceDelegationConnector187",
    ends={
        Property(name="composition_av_av_AssemblyContext188", type=pcm_av_av_composition_av_av_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_RequiredResourceDelegationConnector", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
sinkAssemblyContext__AssemblyEventConnector137: BinaryAssociation = BinaryAssociation(
    name="sinkAssemblyContext__AssemblyEventConnector137",
    ends={
        Property(name="composition_av_av_AssemblyContext139", type=pcm_av_av_composition_av_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyEventConnector138", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
sourceAssemblyContext__AssemblyEventConnector140: BinaryAssociation = BinaryAssociation(
    name="sourceAssemblyContext__AssemblyEventConnector140",
    ends={
        Property(name="composition_av_av_AssemblyContext142", type=pcm_av_av_composition_av_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyEventConnector141", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__AssemblyEventConnector143: BinaryAssociation = BinaryAssociation(
    name="filterCondition__AssemblyEventConnector143",
    ends={
        Property(name="core_av_av145", type=pcm_av_av_composition_av_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable144", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
innerSourceRole__SourceRole146: BinaryAssociation = BinaryAssociation(
    name="innerSourceRole__SourceRole146",
    ends={
        Property(name="SourceRole147", type=pcm_av_av_composition_av_av_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_SourceDelegationConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSourceRole__SourceRole148: BinaryAssociation = BinaryAssociation(
    name="outerSourceRole__SourceRole148",
    ends={
        Property(name="SourceRole150", type=pcm_av_av_composition_av_av_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_SourceDelegationConnector149", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SourceDelegationConnector151: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SourceDelegationConnector151",
    ends={
        Property(name="composition_av_av_AssemblyContext153", type=pcm_av_av_composition_av_av_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_SourceDelegationConnector152", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SinkDelegationConnector154: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SinkDelegationConnector154",
    ends={
        Property(name="composition_av_av_AssemblyContext155", type=pcm_av_av_composition_av_av_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_SinkDelegationConnector", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
configParameterUsages__AssemblyContext199: BinaryAssociation = BinaryAssociation(
    name="configParameterUsages__AssemblyContext199",
    ends={
        Property(name="parameter_av_av200", type=pcm_av_av_composition_av_av_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_Workload201: BinaryAssociation = BinaryAssociation(
    name="usageScenario_Workload201",
    ends={
        Property(name="usagemodel_av_av202", type=pcm_av_av_usagemodel_av_av_Workload, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UsageScenario203: BinaryAssociation = BinaryAssociation(
    name="usageModel_UsageScenario203",
    ends={
        Property(name="usagemodel_av_av204", type=pcm_av_av_usagemodel_av_av_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageModel", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_UsageScenario205: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_UsageScenario205",
    ends={
        Property(name="usagemodel_av_av206", type=pcm_av_av_usagemodel_av_av_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
workload_UsageScenario207: BinaryAssociation = BinaryAssociation(
    name="workload_UsageScenario207",
    ends={
        Property(name="usagemodel_av_av208", type=pcm_av_av_usagemodel_av_av_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="Workload", type=Workload, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext_userData209: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_userData209",
    ends={
        Property(name="composition_av_av_AssemblyContext210", type=pcm_av_av_usagemodel_av_av_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_usagemodel_av_av_UserData", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UserData211: BinaryAssociation = BinaryAssociation(
    name="usageModel_UserData211",
    ends={
        Property(name="usagemodel_av_av213", type=pcm_av_av_usagemodel_av_av_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageModel212", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
userDataParameterUsages_UserData214: BinaryAssociation = BinaryAssociation(
    name="userDataParameterUsages_UserData214",
    ends={
        Property(name="parameter_av_av216", type=pcm_av_av_usagemodel_av_av_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage215", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerRequiredRole__RequiredResourceDelegationConnector189: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredResourceDelegationConnector189",
    ends={
        Property(name="entity_av_av_ResourceRequiredRole191", type=pcm_av_av_composition_av_av_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_RequiredResourceDelegationConnector190", type=entity_av_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredResourceDelegationConnector192: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredResourceDelegationConnector192",
    ends={
        Property(name="entity_av_av_ResourceRequiredRole194", type=pcm_av_av_composition_av_av_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_RequiredResourceDelegationConnector193", type=entity_av_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure__AssemblyContext195: BinaryAssociation = BinaryAssociation(
    name="parentStructure__AssemblyContext195",
    ends={
        Property(name="core_av_av197", type=pcm_av_av_composition_av_av_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_av196", type=composition_av_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
encapsulatedComponent__AssemblyContext198: BinaryAssociation = BinaryAssociation(
    name="encapsulatedComponent__AssemblyContext198",
    ends={
        Property(name="RepositoryComponent", type=pcm_av_av_composition_av_av_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyContext", type=RepositoryComponent, multiplicity=Multiplicity(0, 1))
    }
)
userData_UsageModel220: BinaryAssociation = BinaryAssociation(
    name="userData_UsageModel220",
    ends={
        Property(name="usagemodel_av_av221", type=pcm_av_av_usagemodel_av_av_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="UserData", type=UserData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedRole_EntryLevelSystemCall222: BinaryAssociation = BinaryAssociation(
    name="providedRole_EntryLevelSystemCall222",
    ends={
        Property(name="OperationProvidedRole223", type=pcm_av_av_usagemodel_av_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_usagemodel_av_av_EntryLevelSystemCall", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__EntryLevelSystemCall224: BinaryAssociation = BinaryAssociation(
    name="operationSignature__EntryLevelSystemCall224",
    ends={
        Property(name="OperationSignature", type=pcm_av_av_usagemodel_av_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_usagemodel_av_av_EntryLevelSystemCall225", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
outputParameterUsages_EntryLevelSystemCall226: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsages_EntryLevelSystemCall226",
    ends={
        Property(name="parameter_av_av228", type=pcm_av_av_usagemodel_av_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage227", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_UsageModel217: BinaryAssociation = BinaryAssociation(
    name="usageScenario_UsageModel217",
    ends={
        Property(name="usagemodel_av_av219", type=pcm_av_av_usagemodel_av_av_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageScenario218", type=UsageScenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_SenarioBehaviour240: BinaryAssociation = BinaryAssociation(
    name="usageScenario_SenarioBehaviour240",
    ends={
        Property(name="usagemodel_av_av242", type=pcm_av_av_usagemodel_av_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageScenario241", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
branchTransition_ScenarioBehaviour243: BinaryAssociation = BinaryAssociation(
    name="branchTransition_ScenarioBehaviour243",
    ends={
        Property(name="usagemodel_av_av244", type=pcm_av_av_usagemodel_av_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="BranchTransition", type=BranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
loop_ScenarioBehaviour245: BinaryAssociation = BinaryAssociation(
    name="loop_ScenarioBehaviour245",
    ends={
        Property(name="usagemodel_av_av247", type=pcm_av_av_usagemodel_av_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="Loop246", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
actions_ScenarioBehaviour248: BinaryAssociation = BinaryAssociation(
    name="actions_ScenarioBehaviour248",
    ends={
        Property(name="usagemodel_av_av250", type=pcm_av_av_usagemodel_av_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction249", type=AbstractUserAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputParameterUsages_EntryLevelSystemCall229: BinaryAssociation = BinaryAssociation(
    name="inputParameterUsages_EntryLevelSystemCall229",
    ends={
        Property(name="parameter_av_av231", type=pcm_av_av_usagemodel_av_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage230", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
successor232: BinaryAssociation = BinaryAssociation(
    name="successor232",
    ends={
        Property(name="usagemodel_av_av233", type=pcm_av_av_usagemodel_av_av_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
predecessor234: BinaryAssociation = BinaryAssociation(
    name="predecessor234",
    ends={
        Property(name="usagemodel_av_av236", type=pcm_av_av_usagemodel_av_av_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction235", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_AbstractUserAction237: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_AbstractUserAction237",
    ends={
        Property(name="usagemodel_av_av239", type=pcm_av_av_usagemodel_av_av_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour238", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
loopIteration_Loop259: BinaryAssociation = BinaryAssociation(
    name="loopIteration_Loop259",
    ends={
        Property(name="core_av_av261", type=pcm_av_av_usagemodel_av_av_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable260", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyBehaviour_Loop262: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop262",
    ends={
        Property(name="usagemodel_av_av264", type=pcm_av_av_usagemodel_av_av_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour263", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branch_BranchTransition251: BinaryAssociation = BinaryAssociation(
    name="branch_BranchTransition251",
    ends={
        Property(name="usagemodel_av_av252", type=pcm_av_av_usagemodel_av_av_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="Branch", type=Branch, multiplicity=Multiplicity(0, 1))
    }
)
branchedBehaviour_BranchTransition253: BinaryAssociation = BinaryAssociation(
    name="branchedBehaviour_BranchTransition253",
    ends={
        Property(name="usagemodel_av_av255", type=pcm_av_av_usagemodel_av_av_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour254", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchTransitions_Branch256: BinaryAssociation = BinaryAssociation(
    name="branchTransitions_Branch256",
    ends={
        Property(name="usagemodel_av_av258", type=pcm_av_av_usagemodel_av_av_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="BranchTransition257", type=BranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thinkTime_ClosedWorkload271: BinaryAssociation = BinaryAssociation(
    name="thinkTime_ClosedWorkload271",
    ends={
        Property(name="core_av_av273", type=pcm_av_av_usagemodel_av_av_ClosedWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable272", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capacity_PassiveResource274: BinaryAssociation = BinaryAssociation(
    name="capacity_PassiveResource274",
    ends={
        Property(name="core_av_av276", type=pcm_av_av_repository_av_av_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable275", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicComponent_PassiveResource277: BinaryAssociation = BinaryAssociation(
    name="basicComponent_PassiveResource277",
    ends={
        Property(name="repository_av_av278", type=pcm_av_av_repository_av_av_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="BasicComponent", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
resourceTimeoutFailureType__PassiveResource279: BinaryAssociation = BinaryAssociation(
    name="resourceTimeoutFailureType__PassiveResource279",
    ends={
        Property(name="reliability_av_av", type=pcm_av_av_repository_av_av_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceTimeoutFailureType", type=ResourceTimeoutFailureType, multiplicity=Multiplicity(0, 1))
    }
)
interArrivalTime_OpenWorkload265: BinaryAssociation = BinaryAssociation(
    name="interArrivalTime_OpenWorkload265",
    ends={
        Property(name="core_av_av267", type=pcm_av_av_usagemodel_av_av_OpenWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable266", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeSpecification_Delay268: BinaryAssociation = BinaryAssociation(
    name="timeSpecification_Delay268",
    ends={
        Property(name="core_av_av270", type=pcm_av_av_usagemodel_av_av_Delay, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable269", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
passiveResource_BasicComponent282: BinaryAssociation = BinaryAssociation(
    name="passiveResource_BasicComponent282",
    ends={
        Property(name="repository_av_av284", type=pcm_av_av_repository_av_av_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="PassiveResource283", type=PassiveResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentCompleteComponentTypes285: BinaryAssociation = BinaryAssociation(
    name="parentCompleteComponentTypes285",
    ends={
        Property(name="CompleteComponentType", type=pcm_av_av_repository_av_av_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_ImplementationComponentType", type=CompleteComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
componentParameterUsage_ImplementationComponentType286: BinaryAssociation = BinaryAssociation(
    name="componentParameterUsage_ImplementationComponentType286",
    ends={
        Property(name="VariableUsage288", type=pcm_av_av_repository_av_av_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_ImplementationComponentType287", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceEffectSpecifications__BasicComponent280: BinaryAssociation = BinaryAssociation(
    name="serviceEffectSpecifications__BasicComponent280",
    ends={
        Property(name="seff_av_av281", type=pcm_av_av_repository_av_av_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ServiceEffectSpecification", type=ServiceEffectSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureSignature__Parameter295: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignature__Parameter295",
    ends={
        Property(name="repository_av_av296", type=pcm_av_av_repository_av_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="InfrastructureSignature", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__Parameter297: BinaryAssociation = BinaryAssociation(
    name="operationSignature__Parameter297",
    ends={
        Property(name="repository_av_av299", type=pcm_av_av_repository_av_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationSignature298", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
eventType__Parameter300: BinaryAssociation = BinaryAssociation(
    name="eventType__Parameter300",
    ends={
        Property(name="repository_av_av301", type=pcm_av_av_repository_av_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="EventType", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
resourceSignature__Parameter302: BinaryAssociation = BinaryAssociation(
    name="resourceSignature__Parameter302",
    ends={
        Property(name="resourcetype_av_av", type=pcm_av_av_repository_av_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceSignature", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
repository__DataType303: BinaryAssociation = BinaryAssociation(
    name="repository__DataType303",
    ends={
        Property(name="repository_av_av305", type=pcm_av_av_repository_av_av_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository304", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
components__Repository306: BinaryAssociation = BinaryAssociation(
    name="components__Repository306",
    ends={
        Property(name="repository_av_av308", type=pcm_av_av_repository_av_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="RepositoryComponent307", type=RepositoryComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaces__Repository309: BinaryAssociation = BinaryAssociation(
    name="interfaces__Repository309",
    ends={
        Property(name="repository_av_av310", type=pcm_av_av_repository_av_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="Interface", type=Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository__RepositoryComponent289: BinaryAssociation = BinaryAssociation(
    name="repository__RepositoryComponent289",
    ends={
        Property(name="repository_av_av290", type=pcm_av_av_repository_av_av_RepositoryComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
providingEntity_ProvidedRole291: BinaryAssociation = BinaryAssociation(
    name="providingEntity_ProvidedRole291",
    ends={
        Property(name="core_av_av293", type=pcm_av_av_repository_av_av_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_av_av292", type=entity_av_av_InterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
dataType__Parameter294: BinaryAssociation = BinaryAssociation(
    name="dataType__Parameter294",
    ends={
        Property(name="DataType", type=pcm_av_av_repository_av_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_Parameter", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
dataTypes__Repository313: BinaryAssociation = BinaryAssociation(
    name="dataTypes__Repository313",
    ends={
        Property(name="repository_av_av315", type=pcm_av_av_repository_av_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="DataType314", type=DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentInterfaces__Interface316: BinaryAssociation = BinaryAssociation(
    name="parentInterfaces__Interface316",
    ends={
        Property(name="Interface317", type=pcm_av_av_repository_av_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_Interface", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
protocols__Interface318: BinaryAssociation = BinaryAssociation(
    name="protocols__Interface318",
    ends={
        Property(name="Protocol", type=pcm_av_av_repository_av_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_Interface319", type=Protocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureTypes__Repository311: BinaryAssociation = BinaryAssociation(
    name="failureTypes__Repository311",
    ends={
        Property(name="reliability_av_av312", type=pcm_av_av_repository_av_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="FailureType", type=FailureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter325: BinaryAssociation = BinaryAssociation(
    name="parameter325",
    ends={
        Property(name="pcm_av_av_repository_av_av_RequiredCharacterisation", type=Parameter_, multiplicity=Multiplicity(0, 1)),
        Property(name="Parameter", type=pcm_av_av_repository_av_av_RequiredCharacterisation, multiplicity=Multiplicity(1, 1))
    }
)
interface_RequiredCharacterisation326: BinaryAssociation = BinaryAssociation(
    name="interface_RequiredCharacterisation326",
    ends={
        Property(name="repository_av_av328", type=pcm_av_av_repository_av_av_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="Interface327", type=Interface, multiplicity=Multiplicity(0, 1))
    }
)
eventTypes__EventGroup329: BinaryAssociation = BinaryAssociation(
    name="eventTypes__EventGroup329",
    ends={
        Property(name="repository_av_av331", type=pcm_av_av_repository_av_av_EventGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="EventType330", type=EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter__EventType332: BinaryAssociation = BinaryAssociation(
    name="parameter__EventType332",
    ends={
        Property(name="repository_av_av334", type=pcm_av_av_repository_av_av_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter333", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventGroup__EventType335: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventType335",
    ends={
        Property(name="repository_av_av337", type=pcm_av_av_repository_av_av_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="EventGroup336", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
exceptions__Signature338: BinaryAssociation = BinaryAssociation(
    name="exceptions__Signature338",
    ends={
        Property(name="ExceptionType", type=pcm_av_av_repository_av_av_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_Signature", type=ExceptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureType339: BinaryAssociation = BinaryAssociation(
    name="failureType339",
    ends={
        Property(name="FailureType341", type=pcm_av_av_repository_av_av_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_Signature340", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
requiredCharacterisations320: BinaryAssociation = BinaryAssociation(
    name="requiredCharacterisations320",
    ends={
        Property(name="repository_av_av321", type=pcm_av_av_repository_av_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="RequiredCharacterisation", type=RequiredCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository__Interface322: BinaryAssociation = BinaryAssociation(
    name="repository__Interface322",
    ends={
        Property(name="repository_av_av324", type=pcm_av_av_repository_av_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository323", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
requiringEntity_RequiredRole352: BinaryAssociation = BinaryAssociation(
    name="requiringEntity_RequiredRole352",
    ends={
        Property(name="core_av_av354", type=pcm_av_av_repository_av_av_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_av_av353", type=entity_av_av_InterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
interface__OperationSignature355: BinaryAssociation = BinaryAssociation(
    name="interface__OperationSignature355",
    ends={
        Property(name="repository_av_av356", type=pcm_av_av_repository_av_av_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationInterface", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
parameters__OperationSignature357: BinaryAssociation = BinaryAssociation(
    name="parameters__OperationSignature357",
    ends={
        Property(name="repository_av_av359", type=pcm_av_av_repository_av_av_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter358", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType__OperationSignature360: BinaryAssociation = BinaryAssociation(
    name="returnType__OperationSignature360",
    ends={
        Property(name="DataType361", type=pcm_av_av_repository_av_av_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_OperationSignature", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
parameters__InfrastructureSignature342: BinaryAssociation = BinaryAssociation(
    name="parameters__InfrastructureSignature342",
    ends={
        Property(name="repository_av_av344", type=pcm_av_av_repository_av_av_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter343", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureInterface__InfrastructureSignature345: BinaryAssociation = BinaryAssociation(
    name="infrastructureInterface__InfrastructureSignature345",
    ends={
        Property(name="repository_av_av346", type=pcm_av_av_repository_av_av_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="InfrastructureInterface", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureSignatures__InfrastructureInterface347: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignatures__InfrastructureInterface347",
    ends={
        Property(name="repository_av_av349", type=pcm_av_av_repository_av_av_InfrastructureInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="InfrastructureSignature348", type=InfrastructureSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterface__InfrastructureRequiredRole350: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__InfrastructureRequiredRole350",
    ends={
        Property(name="InfrastructureInterface351", type=pcm_av_av_repository_av_av_InfrastructureRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_InfrastructureRequiredRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SourceRole367: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SourceRole367",
    ends={
        Property(name="EventGroup368", type=pcm_av_av_repository_av_av_SourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_SourceRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SinkRole369: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SinkRole369",
    ends={
        Property(name="EventGroup370", type=pcm_av_av_repository_av_av_SinkRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_SinkRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface__OperationProvidedRole371: BinaryAssociation = BinaryAssociation(
    name="providedInterface__OperationProvidedRole371",
    ends={
        Property(name="OperationInterface372", type=pcm_av_av_repository_av_av_OperationProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_OperationProvidedRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface__InfrastructureProvidedRole373: BinaryAssociation = BinaryAssociation(
    name="providedInterface__InfrastructureProvidedRole373",
    ends={
        Property(name="InfrastructureInterface374", type=pcm_av_av_repository_av_av_InfrastructureProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_InfrastructureProvidedRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
signatures__OperationInterface362: BinaryAssociation = BinaryAssociation(
    name="signatures__OperationInterface362",
    ends={
        Property(name="repository_av_av364", type=pcm_av_av_repository_av_av_OperationInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationSignature363", type=OperationSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterface__OperationRequiredRole365: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__OperationRequiredRole365",
    ends={
        Property(name="OperationInterface366", type=pcm_av_av_repository_av_av_OperationRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_OperationRequiredRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
parentProvidesComponentTypes375: BinaryAssociation = BinaryAssociation(
    name="parentProvidesComponentTypes375",
    ends={
        Property(name="ProvidesComponentType", type=pcm_av_av_repository_av_av_CompleteComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_CompleteComponentType", type=ProvidesComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
parentType_CompositeDataType378: BinaryAssociation = BinaryAssociation(
    name="parentType_CompositeDataType378",
    ends={
        Property(name="CompositeDataType", type=pcm_av_av_repository_av_av_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 9999))
    }
)
innerDeclaration_CompositeDataType379: BinaryAssociation = BinaryAssociation(
    name="innerDeclaration_CompositeDataType379",
    ends={
        Property(name="repository_av_av380", type=pcm_av_av_repository_av_av_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="InnerDeclaration", type=InnerDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype_InnerDeclaration381: BinaryAssociation = BinaryAssociation(
    name="datatype_InnerDeclaration381",
    ends={
        Property(name="DataType382", type=pcm_av_av_repository_av_av_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_InnerDeclaration", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
compositeDataType_InnerDeclaration383: BinaryAssociation = BinaryAssociation(
    name="compositeDataType_InnerDeclaration383",
    ends={
        Property(name="repository_av_av385", type=pcm_av_av_repository_av_av_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="CompositeDataType384", type=CompositeDataType, multiplicity=Multiplicity(0, 1))
    }
)
parameter__ResourceSignature386: BinaryAssociation = BinaryAssociation(
    name="parameter__ResourceSignature386",
    ends={
        Property(name="repository_av_av388", type=pcm_av_av_resourcetype_av_av_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter387", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceInterface__ResourceSignature389: BinaryAssociation = BinaryAssociation(
    name="resourceInterface__ResourceSignature389",
    ends={
        Property(name="resourcetype_av_av391", type=pcm_av_av_resourcetype_av_av_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceInterface390", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
hardwareInducedFailureType__ProcessingResourceType392: BinaryAssociation = BinaryAssociation(
    name="hardwareInducedFailureType__ProcessingResourceType392",
    ends={
        Property(name="reliability_av_av393", type=pcm_av_av_resourcetype_av_av_ProcessingResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="HardwareInducedFailureType", type=HardwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
innerType_CollectionDataType376: BinaryAssociation = BinaryAssociation(
    name="innerType_CollectionDataType376",
    ends={
        Property(name="DataType377", type=pcm_av_av_repository_av_av_CollectionDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_CollectionDataType", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
networkInducedFailureType__CommunicationLinkResourceType406: BinaryAssociation = BinaryAssociation(
    name="networkInducedFailureType__CommunicationLinkResourceType406",
    ends={
        Property(name="reliability_av_av407", type=pcm_av_av_resourcetype_av_av_CommunicationLinkResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="NetworkInducedFailureType", type=NetworkInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
resourceRepository__ResourceInterface408: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__ResourceInterface408",
    ends={
        Property(name="resourcetype_av_av410", type=pcm_av_av_resourcetype_av_av_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceRepository409", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
resourceSignatures__ResourceInterface411: BinaryAssociation = BinaryAssociation(
    name="resourceSignatures__ResourceInterface411",
    ends={
        Property(name="resourcetype_av_av413", type=pcm_av_av_resourcetype_av_av_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceSignature412", type=ResourceSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableCharacterisation_VariableUsage414: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_VariableUsage414",
    ends={
        Property(name="parameter_av_av416", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableCharacterisation415", type=VariableCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_VariableUsage417: BinaryAssociation = BinaryAssociation(
    name="userData_VariableUsage417",
    ends={
        Property(name="usagemodel_av_av419", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="UserData418", type=UserData, multiplicity=Multiplicity(0, 1))
    }
)
callAction__VariableUsage420: BinaryAssociation = BinaryAssociation(
    name="callAction__VariableUsage420",
    ends={
        Property(name="seff_av_av421", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="CallAction", type=CallAction, multiplicity=Multiplicity(0, 1))
    }
)
synchronisationPoint_VariableUsage422: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_VariableUsage422",
    ends={
        Property(name="seff_av_av423", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
resourceRepository_ResourceType394: BinaryAssociation = BinaryAssociation(
    name="resourceRepository_ResourceType394",
    ends={
        Property(name="resourcetype_av_av395", type=pcm_av_av_resourcetype_av_av_ResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaces__ResourceRepository396: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaces__ResourceRepository396",
    ends={
        Property(name="resourcetype_av_av398", type=pcm_av_av_resourcetype_av_av_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceInterface397", type=ResourceInterface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schedulingPolicies__ResourceRepository399: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicies__ResourceRepository399",
    ends={
        Property(name="resourcetype_av_av400", type=pcm_av_av_resourcetype_av_av_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="SchedulingPolicy", type=SchedulingPolicy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
availableResourceTypes_ResourceRepository401: BinaryAssociation = BinaryAssociation(
    name="availableResourceTypes_ResourceRepository401",
    ends={
        Property(name="resourcetype_av_av402", type=pcm_av_av_resourcetype_av_av_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceType", type=ResourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRepository__SchedulingPolicy403: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__SchedulingPolicy403",
    ends={
        Property(name="resourcetype_av_av405", type=pcm_av_av_resourcetype_av_av_SchedulingPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceRepository404", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
specification_VariableCharacterisation439: BinaryAssociation = BinaryAssociation(
    name="specification_VariableCharacterisation439",
    ends={
        Property(name="core_av_av441", type=pcm_av_av_parameter_av_av_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable440", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableUsage_VariableCharacterisation442: BinaryAssociation = BinaryAssociation(
    name="variableUsage_VariableCharacterisation442",
    ends={
        Property(name="parameter_av_av444", type=pcm_av_av_parameter_av_av_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage443", type=VariableUsage, multiplicity=Multiplicity(0, 1))
    }
)
callReturnAction__VariableUsage424: BinaryAssociation = BinaryAssociation(
    name="callReturnAction__VariableUsage424",
    ends={
        Property(name="seff_av_av425", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="CallReturnAction", type=CallReturnAction, multiplicity=Multiplicity(0, 1))
    }
)
setVariableAction_VariableUsage426: BinaryAssociation = BinaryAssociation(
    name="setVariableAction_VariableUsage426",
    ends={
        Property(name="seff_av_av427", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="SetVariableAction", type=SetVariableAction, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage428: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage428",
    ends={
        Property(name="qosannotations_av_av429", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="SpecifiedOutputParameterAbstraction", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__VariableUsage430: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__VariableUsage430",
    ends={
        Property(name="core_av_av432", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_av431", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_InputParameterUsage433: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_InputParameterUsage433",
    ends={
        Property(name="usagemodel_av_av434", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="EntryLevelSystemCall", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_OutputParameterUsage435: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_OutputParameterUsage435",
    ends={
        Property(name="usagemodel_av_av437", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="EntryLevelSystemCall436", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
namedReference__VariableUsage438: BinaryAssociation = BinaryAssociation(
    name="namedReference__VariableUsage438",
    ends={
        Property(name="parameter_av_av_pcm_av_av_AbstractNamedReference", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_parameter_av_av_VariableUsage", type=parameter_av_av_pcm_av_av_AbstractNamedReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
processingResourceType__HardwareInducedFailureType445: BinaryAssociation = BinaryAssociation(
    name="processingResourceType__HardwareInducedFailureType445",
    ends={
        Property(name="resourcetype_av_av446", type=pcm_av_av_reliability_av_av_HardwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcessingResourceType", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
internalFailureOccurrenceDescriptions__SoftwareInducedFailureType447: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__SoftwareInducedFailureType447",
    ends={
        Property(name="reliability_av_av448", type=pcm_av_av_reliability_av_av_SoftwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="InternalFailureOccurrenceDescription", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999))
    }
)
internalAction__InternalFailureOccurrenceDescription449: BinaryAssociation = BinaryAssociation(
    name="internalAction__InternalFailureOccurrenceDescription449",
    ends={
        Property(name="seff_av_av450", type=pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="InternalAction", type=InternalAction, multiplicity=Multiplicity(0, 1))
    }
)
softwareInducedFailureType__InternalFailureOccurrenceDescription451: BinaryAssociation = BinaryAssociation(
    name="softwareInducedFailureType__InternalFailureOccurrenceDescription451",
    ends={
        Property(name="reliability_av_av452", type=pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="SoftwareInducedFailureType", type=SoftwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription455: BinaryAssociation = BinaryAssociation(
    name="specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription455",
    ends={
        Property(name="qosannotations_av_av456", type=pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="qos_reliability_av_av", type=qos_reliability_av_av_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(0, 1))
    }
)
failureType__ExternalFailureOccurrenceDescription457: BinaryAssociation = BinaryAssociation(
    name="failureType__ExternalFailureOccurrenceDescription457",
    ends={
        Property(name="FailureType458", type=pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription", type=FailureType, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource__ResourceTimeoutFailureType459: BinaryAssociation = BinaryAssociation(
    name="passiveResource__ResourceTimeoutFailureType459",
    ends={
        Property(name="repository_av_av461", type=pcm_av_av_reliability_av_av_ResourceTimeoutFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="PassiveResource460", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
repository__FailureType462: BinaryAssociation = BinaryAssociation(
    name="repository__FailureType462",
    ends={
        Property(name="repository_av_av464", type=pcm_av_av_reliability_av_av_FailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository463", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceType__NetworkInducedFailureType453: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType__NetworkInducedFailureType453",
    ends={
        Property(name="resourcetype_av_av454", type=pcm_av_av_reliability_av_av_NetworkInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceType", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
predecessor_AbstractAction474: BinaryAssociation = BinaryAssociation(
    name="predecessor_AbstractAction474",
    ends={
        Property(name="AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1)),
        Property(name="seff_av_av475", type=pcm_av_av_seff_av_av_AbstractAction, multiplicity=Multiplicity(1, 1))
    }
)
successor_AbstractAction476: BinaryAssociation = BinaryAssociation(
    name="successor_AbstractAction476",
    ends={
        Property(name="seff_av_av478", type=pcm_av_av_seff_av_av_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction477", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemandingBehaviour_AbstractAction479: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingBehaviour_AbstractAction479",
    ends={
        Property(name="seff_av_av480", type=pcm_av_av_seff_av_av_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingBehaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
abstractLoopAction_ResourceDemandingBehaviour481: BinaryAssociation = BinaryAssociation(
    name="abstractLoopAction_ResourceDemandingBehaviour481",
    ends={
        Property(name="seff_av_av482", type=pcm_av_av_seff_av_av_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractLoopAction", type=AbstractLoopAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemand_Action465: BinaryAssociation = BinaryAssociation(
    name="resourceDemand_Action465",
    ends={
        Property(name="seff_av_av467", type=pcm_av_av_seff_av_av_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_av_av466", type=seff_performance_av_av_ParametricResourceDemand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureCall__Action468: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__Action468",
    ends={
        Property(name="seff_av_av470", type=pcm_av_av_seff_av_av_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_av_av469", type=seff_performance_av_av_InfrastructureCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceCall__Action471: BinaryAssociation = BinaryAssociation(
    name="resourceCall__Action471",
    ends={
        Property(name="seff_av_av473", type=pcm_av_av_seff_av_av_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_av_av472", type=seff_performance_av_av_ResourceCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branches_Branch496: BinaryAssociation = BinaryAssociation(
    name="branches_Branch496",
    ends={
        Property(name="seff_av_av498", type=pcm_av_av_seff_av_av_BranchAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractBranchTransition497", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputVariableUsages__CallAction499: BinaryAssociation = BinaryAssociation(
    name="inputVariableUsages__CallAction499",
    ends={
        Property(name="parameter_av_av501", type=pcm_av_av_seff_av_av_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage500", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abstractBranchTransition_ResourceDemandingBehaviour483: BinaryAssociation = BinaryAssociation(
    name="abstractBranchTransition_ResourceDemandingBehaviour483",
    ends={
        Property(name="seff_av_av484", type=pcm_av_av_seff_av_av_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractBranchTransition", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
steps_Behaviour485: BinaryAssociation = BinaryAssociation(
    name="steps_Behaviour485",
    ends={
        Property(name="seff_av_av487", type=pcm_av_av_seff_av_av_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction486", type=AbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyBehaviour_Loop488: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop488",
    ends={
        Property(name="seff_av_av490", type=pcm_av_av_seff_av_av_AbstractLoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingBehaviour489", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchAction_AbstractBranchTransition491: BinaryAssociation = BinaryAssociation(
    name="branchAction_AbstractBranchTransition491",
    ends={
        Property(name="seff_av_av492", type=pcm_av_av_seff_av_av_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="BranchAction", type=BranchAction, multiplicity=Multiplicity(0, 1))
    }
)
branchBehaviour_BranchTransition493: BinaryAssociation = BinaryAssociation(
    name="branchBehaviour_BranchTransition493",
    ends={
        Property(name="seff_av_av495", type=pcm_av_av_seff_av_av_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingBehaviour494", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceDemandingSEFF_ResourceDemandingInternalBehaviour508: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingSEFF_ResourceDemandingInternalBehaviour508",
    ends={
        Property(name="seff_av_av509", type=pcm_av_av_seff_av_av_ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingSEFF", type=ResourceDemandingSEFF, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_ReleaseAction510: BinaryAssociation = BinaryAssociation(
    name="passiveResource_ReleaseAction510",
    ends={
        Property(name="PassiveResource511", type=pcm_av_av_seff_av_av_ReleaseAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_av_av_ReleaseAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
iterationCount_LoopAction512: BinaryAssociation = BinaryAssociation(
    name="iterationCount_LoopAction512",
    ends={
        Property(name="core_av_av514", type=pcm_av_av_seff_av_av_LoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable513", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
asynchronousForkedBehaviours_ForkAction515: BinaryAssociation = BinaryAssociation(
    name="asynchronousForkedBehaviours_ForkAction515",
    ends={
        Property(name="seff_av_av516", type=pcm_av_av_seff_av_av_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedBehaviour", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronisingBehaviours_ForkAction517: BinaryAssociation = BinaryAssociation(
    name="synchronisingBehaviours_ForkAction517",
    ends={
        Property(name="seff_av_av519", type=pcm_av_av_seff_av_av_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="SynchronisationPoint518", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
synchronisationPoint_ForkedBehaviour520: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_ForkedBehaviour520",
    ends={
        Property(name="seff_av_av522", type=pcm_av_av_seff_av_av_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="SynchronisationPoint521", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
forkAction_ForkedBehaivour523: BinaryAssociation = BinaryAssociation(
    name="forkAction_ForkedBehaivour523",
    ends={
        Property(name="seff_av_av524", type=pcm_av_av_seff_av_av_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkAction", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
outputParameterUsage_SynchronisationPoint525: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsage_SynchronisationPoint525",
    ends={
        Property(name="parameter_av_av527", type=pcm_av_av_seff_av_av_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage526", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
describedService__SEFF502: BinaryAssociation = BinaryAssociation(
    name="describedService__SEFF502",
    ends={
        Property(name="Signature", type=pcm_av_av_seff_av_av_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_av_av_ServiceEffectSpecification", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
basicComponent_ServiceEffectSpecification503: BinaryAssociation = BinaryAssociation(
    name="basicComponent_ServiceEffectSpecification503",
    ends={
        Property(name="repository_av_av505", type=pcm_av_av_seff_av_av_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BasicComponent504", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemandingInternalBehaviours506: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingInternalBehaviours506",
    ends={
        Property(name="seff_av_av507", type=pcm_av_av_seff_av_av_ResourceDemandingSEFF, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingInternalBehaviour", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledService_ExternalService534: BinaryAssociation = BinaryAssociation(
    name="calledService_ExternalService534",
    ends={
        Property(name="OperationSignature535", type=pcm_av_av_seff_av_av_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_av_av_ExternalCallAction", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
role_ExternalService536: BinaryAssociation = BinaryAssociation(
    name="role_ExternalService536",
    ends={
        Property(name="OperationRequiredRole538", type=pcm_av_av_seff_av_av_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_av_av_ExternalCallAction537", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
returnVariableUsage__CallReturnAction539: BinaryAssociation = BinaryAssociation(
    name="returnVariableUsage__CallReturnAction539",
    ends={
        Property(name="parameter_av_av541", type=pcm_av_av_seff_av_av_CallReturnAction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage540", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forkAction_SynchronisationPoint528: BinaryAssociation = BinaryAssociation(
    name="forkAction_SynchronisationPoint528",
    ends={
        Property(name="seff_av_av530", type=pcm_av_av_seff_av_av_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkAction529", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
synchronousForkedBehaviours_SynchronisationPoint531: BinaryAssociation = BinaryAssociation(
    name="synchronousForkedBehaviours_SynchronisationPoint531",
    ends={
        Property(name="seff_av_av533", type=pcm_av_av_seff_av_av_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedBehaviour532", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branchCondition_GuardedBranchTransition546: BinaryAssociation = BinaryAssociation(
    name="branchCondition_GuardedBranchTransition546",
    ends={
        Property(name="core_av_av548", type=pcm_av_av_seff_av_av_GuardedBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable547", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localVariableUsages_SetVariableAction549: BinaryAssociation = BinaryAssociation(
    name="localVariableUsages_SetVariableAction549",
    ends={
        Property(name="parameter_av_av551", type=pcm_av_av_seff_av_av_SetVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage550", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledResourceDemandingInternalBehaviour552: BinaryAssociation = BinaryAssociation(
    name="calledResourceDemandingInternalBehaviour552",
    ends={
        Property(name="ResourceDemandingInternalBehaviour553", type=pcm_av_av_seff_av_av_InternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_av_av_InternalCallAction", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
eventType__EmitEventAction554: BinaryAssociation = BinaryAssociation(
    name="eventType__EmitEventAction554",
    ends={
        Property(name="EventType555", type=pcm_av_av_seff_av_av_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_av_av_EmitEventAction", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EmitEventAction556: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EmitEventAction556",
    ends={
        Property(name="SourceRole558", type=pcm_av_av_seff_av_av_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_av_av_EmitEventAction557", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
passiveresource_AcquireAction542: BinaryAssociation = BinaryAssociation(
    name="passiveresource_AcquireAction542",
    ends={
        Property(name="PassiveResource543", type=pcm_av_av_seff_av_av_AcquireAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_av_av_AcquireAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
parameter_CollectionIteratorAction544: BinaryAssociation = BinaryAssociation(
    name="parameter_CollectionIteratorAction544",
    ends={
        Property(name="Parameter545", type=pcm_av_av_seff_av_av_CollectionIteratorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_av_av_CollectionIteratorAction", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
signature__InfrastructureCall562: BinaryAssociation = BinaryAssociation(
    name="signature__InfrastructureCall562",
    ends={
        Property(name="InfrastructureSignature563", type=pcm_av_av_seff_performance_av_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_performance_av_av_InfrastructureCall", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__InfrastructureCall564: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__InfrastructureCall564",
    ends={
        Property(name="core_av_av566", type=pcm_av_av_seff_performance_av_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable565", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action__InfrastructureCall567: BinaryAssociation = BinaryAssociation(
    name="action__InfrastructureCall567",
    ends={
        Property(name="seff_av_av568", type=pcm_av_av_seff_performance_av_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractInternalControlFlowAction", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__InfrastructureCall569: BinaryAssociation = BinaryAssociation(
    name="requiredRole__InfrastructureCall569",
    ends={
        Property(name="InfrastructureRequiredRole571", type=pcm_av_av_seff_performance_av_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_performance_av_av_InfrastructureCall570", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
internalFailureOccurrenceDescriptions__InternalAction559: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__InternalAction559",
    ends={
        Property(name="reliability_av_av561", type=pcm_av_av_seff_av_av_InternalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="InternalFailureOccurrenceDescription560", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification_ParametericResourceDemand583: BinaryAssociation = BinaryAssociation(
    name="specification_ParametericResourceDemand583",
    ends={
        Property(name="core_av_av585", type=pcm_av_av_seff_performance_av_av_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable584", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredResource_ParametricResourceDemand586: BinaryAssociation = BinaryAssociation(
    name="requiredResource_ParametricResourceDemand586",
    ends={
        Property(name="ProcessingResourceType587", type=pcm_av_av_seff_performance_av_av_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_performance_av_av_ParametricResourceDemand", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
action_ParametricResourceDemand588: BinaryAssociation = BinaryAssociation(
    name="action_ParametricResourceDemand588",
    ends={
        Property(name="seff_av_av590", type=pcm_av_av_seff_performance_av_av_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractInternalControlFlowAction589", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
action__ResourceCall572: BinaryAssociation = BinaryAssociation(
    name="action__ResourceCall572",
    ends={
        Property(name="seff_av_av574", type=pcm_av_av_seff_performance_av_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractInternalControlFlowAction573", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceRequiredRole__ResourceCall575: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRole__ResourceCall575",
    ends={
        Property(name="entity_av_av_ResourceRequiredRole576", type=pcm_av_av_seff_performance_av_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_performance_av_av_ResourceCall", type=entity_av_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
signature__ResourceCall577: BinaryAssociation = BinaryAssociation(
    name="signature__ResourceCall577",
    ends={
        Property(name="ResourceSignature579", type=pcm_av_av_seff_performance_av_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_performance_av_av_ResourceCall578", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__ResourceCall580: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__ResourceCall580",
    ends={
        Property(name="core_av_av582", type=pcm_av_av_seff_performance_av_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable581", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
failureHandlingAlternatives__RecoveryActionBehaviour591: BinaryAssociation = BinaryAssociation(
    name="failureHandlingAlternatives__RecoveryActionBehaviour591",
    ends={
        Property(name="seff_reliability_av_av_RecoveryActionBehaviour", type=pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour", type=seff_reliability_av_av_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999))
    }
)
recoveryAction__RecoveryActionBehaviour592: BinaryAssociation = BinaryAssociation(
    name="recoveryAction__RecoveryActionBehaviour592",
    ends={
        Property(name="seff_av_av593", type=pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_reliability_av_av", type=seff_reliability_av_av_RecoveryAction, multiplicity=Multiplicity(0, 1))
    }
)
primaryBehaviour__RecoveryAction594: BinaryAssociation = BinaryAssociation(
    name="primaryBehaviour__RecoveryAction594",
    ends={
        Property(name="seff_reliability_av_av_RecoveryActionBehaviour595", type=pcm_av_av_seff_reliability_av_av_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_reliability_av_av_RecoveryAction", type=seff_reliability_av_av_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
recoveryActionBehaviours__RecoveryAction596: BinaryAssociation = BinaryAssociation(
    name="recoveryActionBehaviours__RecoveryAction596",
    ends={
        Property(name="seff_av_av598", type=pcm_av_av_seff_reliability_av_av_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_reliability_av_av597", type=seff_reliability_av_av_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureTypes_FailureHandlingEntity599: BinaryAssociation = BinaryAssociation(
    name="failureTypes_FailureHandlingEntity599",
    ends={
        Property(name="FailureType600", type=pcm_av_av_seff_reliability_av_av_FailureHandlingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_reliability_av_av_FailureHandlingEntity", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
signature_SpecifiedQoSAnnation601: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedQoSAnnation601",
    ends={
        Property(name="Signature602", type=pcm_av_av_qosannotations_av_av_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_qosannotations_av_av_SpecifiedQoSAnnotation", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
system_QoSAnnotations610: BinaryAssociation = BinaryAssociation(
    name="system_QoSAnnotations610",
    ends={
        Property(name="system_av_av", type=pcm_av_av_qosannotations_av_av_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="System", type=System, multiplicity=Multiplicity(0, 1))
    }
)
specifiedQoSAnnotations_QoSAnnotations611: BinaryAssociation = BinaryAssociation(
    name="specifiedQoSAnnotations_QoSAnnotations611",
    ends={
        Property(name="qosannotations_av_av612", type=pcm_av_av_qosannotations_av_av_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="SpecifiedQoSAnnotation", type=SpecifiedQoSAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature_SpecifiedOutputParameterAbstraction613: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedOutputParameterAbstraction613",
    ends={
        Property(name="Signature614", type=pcm_av_av_qosannotations_av_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_qosannotations_av_av_SpecifiedOutputParameterAbstraction", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedOutputParameterAbstraction615: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedOutputParameterAbstraction615",
    ends={
        Property(name="Role617", type=pcm_av_av_qosannotations_av_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_qosannotations_av_av_SpecifiedOutputParameterAbstraction616", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
expectedExternalOutputs_SpecifiedOutputParameterAbstraction618: BinaryAssociation = BinaryAssociation(
    name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction618",
    ends={
        Property(name="parameter_av_av620", type=pcm_av_av_qosannotations_av_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage619", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qosAnnotations_SpecifiedOutputParameterAbstraction621: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedOutputParameterAbstraction621",
    ends={
        Property(name="qosannotations_av_av623", type=pcm_av_av_qosannotations_av_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="QoSAnnotations622", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedQoSAnnotation603: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedQoSAnnotation603",
    ends={
        Property(name="Role", type=pcm_av_av_qosannotations_av_av_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_qosannotations_av_av_SpecifiedQoSAnnotation604", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
qosAnnotations_SpecifiedQoSAnnotation605: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedQoSAnnotation605",
    ends={
        Property(name="qosannotations_av_av606", type=pcm_av_av_qosannotations_av_av_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstractions_QoSAnnotations607: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstractions_QoSAnnotations607",
    ends={
        Property(name="qosannotations_av_av609", type=pcm_av_av_qosannotations_av_av_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="SpecifiedOutputParameterAbstraction608", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation629: BinaryAssociation = BinaryAssociation(
    name="externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation629",
    ends={
        Property(name="reliability_av_av630", type=pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ExternalFailureOccurrenceDescription", type=ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification_SpecifiedExecutionTime624: BinaryAssociation = BinaryAssociation(
    name="specification_SpecifiedExecutionTime624",
    ends={
        Property(name="core_av_av626", type=pcm_av_av_qos_performance_av_av_SpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable625", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext_ComponentSpecifiedExecutionTime627: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ComponentSpecifiedExecutionTime627",
    ends={
        Property(name="composition_av_av_AssemblyContext628", type=pcm_av_av_qos_performance_av_av_ComponentSpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_qos_performance_av_av_ComponentSpecifiedExecutionTime", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
linkingResources__ResourceEnvironment634: BinaryAssociation = BinaryAssociation(
    name="linkingResources__ResourceEnvironment634",
    ends={
        Property(name="resourceenvironment_av_av635", type=pcm_av_av_resourceenvironment_av_av_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="LinkingResource", type=LinkingResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_ResourceEnvironment636: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ResourceEnvironment636",
    ends={
        Property(name="resourceenvironment_av_av637", type=pcm_av_av_resourceenvironment_av_av_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectedResourceContainers_LinkingResource638: BinaryAssociation = BinaryAssociation(
    name="connectedResourceContainers_LinkingResource638",
    ends={
        Property(name="ResourceContainer639", type=pcm_av_av_resourceenvironment_av_av_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_resourceenvironment_av_av_LinkingResource", type=ResourceContainer, multiplicity=Multiplicity(0, 9999))
    }
)
communicationLinkResourceSpecifications_LinkingResource640: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifications_LinkingResource640",
    ends={
        Property(name="resourceenvironment_av_av642", type=pcm_av_av_resourceenvironment_av_av_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceSpecification641", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceEnvironment_LinkingResource643: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_LinkingResource643",
    ends={
        Property(name="resourceenvironment_av_av644", type=pcm_av_av_resourceenvironment_av_av_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceEnvironment", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceSpecifications_ResourceContainer645: BinaryAssociation = BinaryAssociation(
    name="activeResourceSpecifications_ResourceContainer645",
    ends={
        Property(name="resourceenvironment_av_av647", type=pcm_av_av_resourceenvironment_av_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcessingResourceSpecification646", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceEnvironment_ResourceContainer648: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_ResourceContainer648",
    ends={
        Property(name="resourceenvironment_av_av650", type=pcm_av_av_resourceenvironment_av_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceEnvironment649", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
nestedResourceContainers__ResourceContainer651: BinaryAssociation = BinaryAssociation(
    name="nestedResourceContainers__ResourceContainer651",
    ends={
        Property(name="resourceenvironment_av_av653", type=pcm_av_av_resourceenvironment_av_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer652", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentResourceContainer__ResourceContainer654: BinaryAssociation = BinaryAssociation(
    name="parentResourceContainer__ResourceContainer654",
    ends={
        Property(name="resourceenvironment_av_av656", type=pcm_av_av_resourceenvironment_av_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer655", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
qosAnnotations_System631: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_System631",
    ends={
        Property(name="qosannotations_av_av633", type=pcm_av_av_system_av_av_System, multiplicity=Multiplicity(1, 1)),
        Property(name="QoSAnnotations632", type=QoSAnnotations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_ProcessingResourceSpecification665: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ProcessingResourceSpecification665",
    ends={
        Property(name="resourceenvironment_av_av667", type=pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer666", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
linkingResource_CommunicationLinkResourceSpecification668: BinaryAssociation = BinaryAssociation(
    name="linkingResource_CommunicationLinkResourceSpecification668",
    ends={
        Property(name="resourceenvironment_av_av670", type=pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="LinkingResource669", type=LinkingResource, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceType_CommunicationLinkResourceSpecification671: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType_CommunicationLinkResourceSpecification671",
    ends={
        Property(name="CommunicationLinkResourceType672", type=pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
latency_CommunicationLinkResourceSpecification673: BinaryAssociation = BinaryAssociation(
    name="latency_CommunicationLinkResourceSpecification673",
    ends={
        Property(name="core_av_av675", type=pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable674", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throughput_CommunicationLinkResourceSpecification676: BinaryAssociation = BinaryAssociation(
    name="throughput_CommunicationLinkResourceSpecification676",
    ends={
        Property(name="core_av_av678", type=pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable677", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schedulingPolicy657: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicy657",
    ends={
        Property(name="SchedulingPolicy658", type=pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification", type=SchedulingPolicy, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceType_ActiveResourceSpecification659: BinaryAssociation = BinaryAssociation(
    name="activeResourceType_ActiveResourceSpecification659",
    ends={
        Property(name="ProcessingResourceType661", type=pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification660", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
processingRate_ProcessingResourceSpecification662: BinaryAssociation = BinaryAssociation(
    name="processingRate_ProcessingResourceSpecification662",
    ends={
        Property(name="core_av_av664", type=pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable663", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetResourceEnvironment_Allocation687: BinaryAssociation = BinaryAssociation(
    name="targetResourceEnvironment_Allocation687",
    ends={
        Property(name="ResourceEnvironment688", type=pcm_av_av_allocation_av_av_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_allocation_av_av_Allocation", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
system_Allocation689: BinaryAssociation = BinaryAssociation(
    name="system_Allocation689",
    ends={
        Property(name="System691", type=pcm_av_av_allocation_av_av_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_allocation_av_av_Allocation690", type=System, multiplicity=Multiplicity(0, 1))
    }
)
allocationContexts_Allocation692: BinaryAssociation = BinaryAssociation(
    name="allocationContexts_Allocation692",
    ends={
        Property(name="allocation_av_av693", type=pcm_av_av_allocation_av_av_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="AllocationContext", type=AllocationContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_AllocationContext679: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_AllocationContext679",
    ends={
        Property(name="ResourceContainer680", type=pcm_av_av_allocation_av_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_allocation_av_av_AllocationContext", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_AllocationContext681: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_AllocationContext681",
    ends={
        Property(name="composition_av_av_AssemblyContext683", type=pcm_av_av_allocation_av_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_allocation_av_av_AllocationContext682", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
allocation_AllocationContext684: BinaryAssociation = BinaryAssociation(
    name="allocation_AllocationContext684",
    ends={
        Property(name="allocation_av_av", type=pcm_av_av_allocation_av_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="Allocation", type=Allocation, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__AllocationContext685: BinaryAssociation = BinaryAssociation(
    name="eventChannel__AllocationContext685",
    ends={
        Property(name="composition_av_av_EventChannel", type=pcm_av_av_allocation_av_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_allocation_av_av_AllocationContext686", type=composition_av_av_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
completions_CompletionRepository694: BinaryAssociation = BinaryAssociation(
    name="completions_CompletionRepository694",
    ends={
        Property(name="Completion", type=pcm_av_av_completions_av_av_CompletionRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_completions_av_av_CompletionRepository", type=Completion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCommunicationLinkResource_ParametricResourceDemand695: BinaryAssociation = BinaryAssociation(
    name="requiredCommunicationLinkResource_ParametricResourceDemand695",
    ends={
        Property(name="CommunicationLinkResourceType696", type=pcm_av_av_completions_av_av_NetworkDemandParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_completions_av_av_NetworkDemandParametricResourceDemand", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_pcm_av_av_core_av_av_PCMRandomVariable_RandomVariable = Generalization(general=RandomVariable, specific=pcm_av_av_core_av_av_PCMRandomVariable)
gen_pcm_av_av_entity_av_av_InterfaceProvidingRequiringEntity_entity_av_av_InterfaceProvidingEntity = Generalization(general=entity_av_av_InterfaceProvidingEntity, specific=pcm_av_av_entity_av_av_InterfaceProvidingRequiringEntity)
gen_pcm_av_av_entity_av_av_InterfaceProvidingRequiringEntity_entity_av_av_InterfaceRequiringEntity = Generalization(general=entity_av_av_InterfaceRequiringEntity, specific=pcm_av_av_entity_av_av_InterfaceProvidingRequiringEntity)
gen_pcm_av_av_entity_av_av_InterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_av_av_entity_av_av_InterfaceProvidingEntity)
gen_pcm_av_av_entity_av_av_InterfaceRequiringEntity_entity_av_av_Entity = Generalization(general=entity_av_av_Entity, specific=pcm_av_av_entity_av_av_InterfaceRequiringEntity)
gen_pcm_av_av_entity_av_av_InterfaceRequiringEntity_entity_av_av_ResourceInterfaceRequiringEntity = Generalization(general=entity_av_av_ResourceInterfaceRequiringEntity, specific=pcm_av_av_entity_av_av_InterfaceRequiringEntity)
gen_pcm_av_av_entity_av_av_ResourceInterfaceRequiringEntity_Entity = Generalization(general=Entity, specific=pcm_av_av_entity_av_av_ResourceInterfaceRequiringEntity)
gen_pcm_av_av_entity_av_av_ResourceRequiredRole_Role = Generalization(general=Role, specific=pcm_av_av_entity_av_av_ResourceRequiredRole)
gen_pcm_av_av_entity_av_av_ResourceInterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_av_av_entity_av_av_ResourceInterfaceProvidingEntity)
gen_pcm_av_av_entity_av_av_ResourceProvidedRole_Role = Generalization(general=Role, specific=pcm_av_av_entity_av_av_ResourceProvidedRole)
gen_pcm_av_av_composition_av_av_DelegationConnector_Connector = Generalization(general=Connector, specific=pcm_av_av_composition_av_av_DelegationConnector)
gen_pcm_av_av_composition_av_av_Connector_Entity = Generalization(general=Entity, specific=pcm_av_av_composition_av_av_Connector)
gen_pcm_av_av_composition_av_av_ComposedStructure_Entity = Generalization(general=Entity, specific=pcm_av_av_composition_av_av_ComposedStructure)
gen_pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity_composition_av_av_ComposedStructure = Generalization(general=composition_av_av_ComposedStructure, specific=pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity)
gen_pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity_entity_av_av_InterfaceProvidingRequiringEntity = Generalization(general=entity_av_av_InterfaceProvidingRequiringEntity, specific=pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity)
gen_pcm_av_av_entity_av_av_ResourceInterfaceProvidingRequiringEntity_entity_av_av_ResourceInterfaceRequiringEntity = Generalization(general=entity_av_av_ResourceInterfaceRequiringEntity, specific=pcm_av_av_entity_av_av_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_av_av_entity_av_av_ResourceInterfaceProvidingRequiringEntity_entity_av_av_ResourceInterfaceProvidingEntity = Generalization(general=entity_av_av_ResourceInterfaceProvidingEntity, specific=pcm_av_av_entity_av_av_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_av_av_entity_av_av_Entity_Identifier = Generalization(general=Identifier, specific=pcm_av_av_entity_av_av_Entity)
gen_pcm_av_av_entity_av_av_Entity_entity_av_av_NamedElement = Generalization(general=entity_av_av_NamedElement, specific=pcm_av_av_entity_av_av_Entity)
gen_pcm_av_av_composition_av_av_EventChannel_Entity = Generalization(general=Entity, specific=pcm_av_av_composition_av_av_EventChannel)
gen_pcm_av_av_composition_av_av_EventChannelSourceConnector_Connector = Generalization(general=Connector, specific=pcm_av_av_composition_av_av_EventChannelSourceConnector)
gen_pcm_av_av_composition_av_av_EventChannelSinkConnector_Connector = Generalization(general=Connector, specific=pcm_av_av_composition_av_av_EventChannelSinkConnector)
gen_pcm_av_av_composition_av_av_RequiredDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_av_composition_av_av_RequiredDelegationConnector)
gen_pcm_av_av_composition_av_av_ProvidedDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_av_composition_av_av_ProvidedDelegationConnector)
gen_pcm_av_av_composition_av_av_AssemblyEventConnector_Connector = Generalization(general=Connector, specific=pcm_av_av_composition_av_av_AssemblyEventConnector)
gen_pcm_av_av_composition_av_av_AssemblyConnector_Connector = Generalization(general=Connector, specific=pcm_av_av_composition_av_av_AssemblyConnector)
gen_pcm_av_av_composition_av_av_AssemblyInfrastructureConnector_Connector = Generalization(general=Connector, specific=pcm_av_av_composition_av_av_AssemblyInfrastructureConnector)
gen_pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector)
gen_pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector)
gen_pcm_av_av_composition_av_av_RequiredResourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_av_composition_av_av_RequiredResourceDelegationConnector)
gen_pcm_av_av_composition_av_av_SourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_av_composition_av_av_SourceDelegationConnector)
gen_pcm_av_av_composition_av_av_SinkDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_av_composition_av_av_SinkDelegationConnector)
gen_pcm_av_av_usagemodel_av_av_UsageScenario_Entity = Generalization(general=Entity, specific=pcm_av_av_usagemodel_av_av_UsageScenario)
gen_pcm_av_av_composition_av_av_AssemblyContext_Entity = Generalization(general=Entity, specific=pcm_av_av_composition_av_av_AssemblyContext)
gen_pcm_av_av_usagemodel_av_av_EntryLevelSystemCall_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_av_usagemodel_av_av_EntryLevelSystemCall)
gen_pcm_av_av_usagemodel_av_av_AbstractUserAction_Entity = Generalization(general=Entity, specific=pcm_av_av_usagemodel_av_av_AbstractUserAction)
gen_pcm_av_av_usagemodel_av_av_ScenarioBehaviour_Entity = Generalization(general=Entity, specific=pcm_av_av_usagemodel_av_av_ScenarioBehaviour)
gen_pcm_av_av_usagemodel_av_av_Stop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_av_usagemodel_av_av_Stop)
gen_pcm_av_av_usagemodel_av_av_Start_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_av_usagemodel_av_av_Start)
gen_pcm_av_av_usagemodel_av_av_OpenWorkload_Workload = Generalization(general=Workload, specific=pcm_av_av_usagemodel_av_av_OpenWorkload)
gen_pcm_av_av_usagemodel_av_av_Branch_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_av_usagemodel_av_av_Branch)
gen_pcm_av_av_usagemodel_av_av_Loop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_av_usagemodel_av_av_Loop)
gen_pcm_av_av_repository_av_av_PassiveResource_Entity = Generalization(general=Entity, specific=pcm_av_av_repository_av_av_PassiveResource)
gen_pcm_av_av_repository_av_av_BasicComponent_ImplementationComponentType = Generalization(general=ImplementationComponentType, specific=pcm_av_av_repository_av_av_BasicComponent)
gen_pcm_av_av_usagemodel_av_av_Delay_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_av_usagemodel_av_av_Delay)
gen_pcm_av_av_usagemodel_av_av_ClosedWorkload_Workload = Generalization(general=Workload, specific=pcm_av_av_usagemodel_av_av_ClosedWorkload)
gen_pcm_av_av_repository_av_av_ImplementationComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_av_av_repository_av_av_ImplementationComponentType)
gen_pcm_av_av_repository_av_av_Repository_Entity = Generalization(general=Entity, specific=pcm_av_av_repository_av_av_Repository)
gen_pcm_av_av_repository_av_av_RepositoryComponent_InterfaceProvidingRequiringEntity = Generalization(general=InterfaceProvidingRequiringEntity, specific=pcm_av_av_repository_av_av_RepositoryComponent)
gen_pcm_av_av_repository_av_av_ProvidedRole_Role = Generalization(general=Role, specific=pcm_av_av_repository_av_av_ProvidedRole)
gen_pcm_av_av_repository_av_av_Interface_Entity = Generalization(general=Entity, specific=pcm_av_av_repository_av_av_Interface)
gen_pcm_av_av_repository_av_av_EventGroup_Interface = Generalization(general=Interface, specific=pcm_av_av_repository_av_av_EventGroup)
gen_pcm_av_av_repository_av_av_EventType_Signature = Generalization(general=Signature, specific=pcm_av_av_repository_av_av_EventType)
gen_pcm_av_av_repository_av_av_Signature_Entity = Generalization(general=Entity, specific=pcm_av_av_repository_av_av_Signature)
gen_pcm_av_av_repository_av_av_OperationSignature_Signature = Generalization(general=Signature, specific=pcm_av_av_repository_av_av_OperationSignature)
gen_pcm_av_av_repository_av_av_OperationInterface_Interface = Generalization(general=Interface, specific=pcm_av_av_repository_av_av_OperationInterface)
gen_pcm_av_av_repository_av_av_InfrastructureSignature_Signature = Generalization(general=Signature, specific=pcm_av_av_repository_av_av_InfrastructureSignature)
gen_pcm_av_av_repository_av_av_InfrastructureInterface_Interface = Generalization(general=Interface, specific=pcm_av_av_repository_av_av_InfrastructureInterface)
gen_pcm_av_av_repository_av_av_InfrastructureRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_av_av_repository_av_av_InfrastructureRequiredRole)
gen_pcm_av_av_repository_av_av_SourceRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_av_av_repository_av_av_SourceRole)
gen_pcm_av_av_repository_av_av_RequiredRole_Role = Generalization(general=Role, specific=pcm_av_av_repository_av_av_RequiredRole)
gen_pcm_av_av_repository_av_av_SinkRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_av_av_repository_av_av_SinkRole)
gen_pcm_av_av_repository_av_av_OperationProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_av_av_repository_av_av_OperationProvidedRole)
gen_pcm_av_av_repository_av_av_InfrastructureProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_av_av_repository_av_av_InfrastructureProvidedRole)
gen_pcm_av_av_repository_av_av_CompleteComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_av_av_repository_av_av_CompleteComponentType)
gen_pcm_av_av_repository_av_av_OperationRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_av_av_repository_av_av_OperationRequiredRole)
gen_pcm_av_av_repository_av_av_ProvidesComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_av_av_repository_av_av_ProvidesComponentType)
gen_pcm_av_av_repository_av_av_CompositeComponent_entity_av_av_ComposedProvidingRequiringEntity = Generalization(general=entity_av_av_ComposedProvidingRequiringEntity, specific=pcm_av_av_repository_av_av_CompositeComponent)
gen_pcm_av_av_repository_av_av_CompositeComponent_repository_av_av_ImplementationComponentType = Generalization(general=repository_av_av_ImplementationComponentType, specific=pcm_av_av_repository_av_av_CompositeComponent)
gen_pcm_av_av_repository_av_av_PrimitiveDataType_DataType = Generalization(general=DataType, specific=pcm_av_av_repository_av_av_PrimitiveDataType)
gen_pcm_av_av_repository_av_av_InnerDeclaration_NamedElement = Generalization(general=NamedElement, specific=pcm_av_av_repository_av_av_InnerDeclaration)
gen_pcm_av_av_repository_av_av_Role_Entity = Generalization(general=Entity, specific=pcm_av_av_repository_av_av_Role)
gen_pcm_av_av_resourcetype_av_av_ResourceSignature_Entity = Generalization(general=Entity, specific=pcm_av_av_resourcetype_av_av_ResourceSignature)
gen_pcm_av_av_resourcetype_av_av_ProcessingResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_av_av_resourcetype_av_av_ProcessingResourceType)
gen_pcm_av_av_resourcetype_av_av_ResourceType_entity_av_av_Entity = Generalization(general=entity_av_av_Entity, specific=pcm_av_av_resourcetype_av_av_ResourceType)
gen_pcm_av_av_resourcetype_av_av_ResourceType_UnitCarryingElement = Generalization(general=UnitCarryingElement, specific=pcm_av_av_resourcetype_av_av_ResourceType)
gen_pcm_av_av_resourcetype_av_av_ResourceType_entity_av_av_ResourceInterfaceProvidingEntity = Generalization(general=entity_av_av_ResourceInterfaceProvidingEntity, specific=pcm_av_av_resourcetype_av_av_ResourceType)
gen_pcm_av_av_repository_av_av_CollectionDataType_entity_av_av_Entity = Generalization(general=entity_av_av_Entity, specific=pcm_av_av_repository_av_av_CollectionDataType)
gen_pcm_av_av_repository_av_av_CollectionDataType_repository_av_av_DataType = Generalization(general=repository_av_av_DataType, specific=pcm_av_av_repository_av_av_CollectionDataType)
gen_pcm_av_av_repository_av_av_CompositeDataType_entity_av_av_Entity = Generalization(general=entity_av_av_Entity, specific=pcm_av_av_repository_av_av_CompositeDataType)
gen_pcm_av_av_repository_av_av_CompositeDataType_repository_av_av_DataType = Generalization(general=repository_av_av_DataType, specific=pcm_av_av_repository_av_av_CompositeDataType)
gen_pcm_av_av_resourcetype_av_av_CommunicationLinkResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_av_av_resourcetype_av_av_CommunicationLinkResourceType)
gen_pcm_av_av_resourcetype_av_av_ResourceInterface_Entity = Generalization(general=Entity, specific=pcm_av_av_resourcetype_av_av_ResourceInterface)
gen_pcm_av_av_resourcetype_av_av_SchedulingPolicy_Entity = Generalization(general=Entity, specific=pcm_av_av_resourcetype_av_av_SchedulingPolicy)
gen_pcm_av_av_parameter_av_av_CharacterisedVariable_Variable = Generalization(general=Variable, specific=pcm_av_av_parameter_av_av_CharacterisedVariable)
gen_pcm_av_av_reliability_av_av_SoftwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_av_av_reliability_av_av_SoftwareInducedFailureType)
gen_pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription)
gen_pcm_av_av_reliability_av_av_NetworkInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_av_av_reliability_av_av_NetworkInducedFailureType)
gen_pcm_av_av_reliability_av_av_HardwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_av_av_reliability_av_av_HardwareInducedFailureType)
gen_pcm_av_av_reliability_av_av_ResourceTimeoutFailureType_SoftwareInducedFailureType = Generalization(general=SoftwareInducedFailureType, specific=pcm_av_av_reliability_av_av_ResourceTimeoutFailureType)
gen_pcm_av_av_reliability_av_av_FailureType_Entity = Generalization(general=Entity, specific=pcm_av_av_reliability_av_av_FailureType)
gen_pcm_av_av_seff_av_av_StopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_av_seff_av_av_StopAction)
gen_pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription)
gen_pcm_av_av_seff_av_av_ResourceDemandingBehaviour_Identifier = Generalization(general=Identifier, specific=pcm_av_av_seff_av_av_ResourceDemandingBehaviour)
gen_pcm_av_av_seff_av_av_AbstractInternalControlFlowAction_AbstractAction = Generalization(general=AbstractAction, specific=pcm_av_av_seff_av_av_AbstractInternalControlFlowAction)
gen_pcm_av_av_seff_av_av_AbstractAction_Entity = Generalization(general=Entity, specific=pcm_av_av_seff_av_av_AbstractAction)
gen_pcm_av_av_seff_av_av_StartAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_av_seff_av_av_StartAction)
gen_pcm_av_av_seff_av_av_AbstractLoopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_av_seff_av_av_AbstractLoopAction)
gen_pcm_av_av_seff_av_av_AbstractBranchTransition_Entity = Generalization(general=Entity, specific=pcm_av_av_seff_av_av_AbstractBranchTransition)
gen_pcm_av_av_seff_av_av_BranchAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_av_seff_av_av_BranchAction)
gen_pcm_av_av_seff_av_av_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_av_av_seff_av_av_ResourceDemandingInternalBehaviour)
gen_pcm_av_av_seff_av_av_ReleaseAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_av_seff_av_av_ReleaseAction)
gen_pcm_av_av_seff_av_av_LoopAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_av_av_seff_av_av_LoopAction)
gen_pcm_av_av_seff_av_av_ForkAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_av_seff_av_av_ForkAction)
gen_pcm_av_av_seff_av_av_ForkedBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_av_av_seff_av_av_ForkedBehaviour)
gen_pcm_av_av_seff_av_av_ResourceDemandingSEFF_Identifier = Generalization(general=Identifier, specific=pcm_av_av_seff_av_av_ResourceDemandingSEFF)
gen_pcm_av_av_seff_av_av_ResourceDemandingSEFF_seff_av_av_ServiceEffectSpecification = Generalization(general=seff_av_av_ServiceEffectSpecification, specific=pcm_av_av_seff_av_av_ResourceDemandingSEFF)
gen_pcm_av_av_seff_av_av_ResourceDemandingSEFF_seff_av_av_ResourceDemandingBehaviour = Generalization(general=seff_av_av_ResourceDemandingBehaviour, specific=pcm_av_av_seff_av_av_ResourceDemandingSEFF)
gen_pcm_av_av_seff_av_av_CallReturnAction_CallAction = Generalization(general=CallAction, specific=pcm_av_av_seff_av_av_CallReturnAction)
gen_pcm_av_av_seff_av_av_ProbabilisticBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_av_av_seff_av_av_ProbabilisticBranchTransition)
gen_pcm_av_av_seff_av_av_AcquireAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_av_seff_av_av_AcquireAction)
gen_pcm_av_av_seff_av_av_ExternalCallAction_seff_av_av_AbstractAction = Generalization(general=seff_av_av_AbstractAction, specific=pcm_av_av_seff_av_av_ExternalCallAction)
gen_pcm_av_av_seff_av_av_ExternalCallAction_seff_av_av_CallReturnAction = Generalization(general=seff_av_av_CallReturnAction, specific=pcm_av_av_seff_av_av_ExternalCallAction)
gen_pcm_av_av_seff_av_av_ExternalCallAction_seff_reliability_av_av_FailureHandlingEntity = Generalization(general=seff_reliability_av_av_FailureHandlingEntity, specific=pcm_av_av_seff_av_av_ExternalCallAction)
gen_pcm_av_av_seff_av_av_SetVariableAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_av_seff_av_av_SetVariableAction)
gen_pcm_av_av_seff_av_av_InternalCallAction_seff_av_av_CallAction = Generalization(general=seff_av_av_CallAction, specific=pcm_av_av_seff_av_av_InternalCallAction)
gen_pcm_av_av_seff_av_av_InternalCallAction_seff_av_av_AbstractInternalControlFlowAction = Generalization(general=seff_av_av_AbstractInternalControlFlowAction, specific=pcm_av_av_seff_av_av_InternalCallAction)
gen_pcm_av_av_seff_av_av_EmitEventAction_seff_av_av_AbstractAction = Generalization(general=seff_av_av_AbstractAction, specific=pcm_av_av_seff_av_av_EmitEventAction)
gen_pcm_av_av_seff_av_av_EmitEventAction_seff_av_av_CallAction = Generalization(general=seff_av_av_CallAction, specific=pcm_av_av_seff_av_av_EmitEventAction)
gen_pcm_av_av_seff_av_av_InternalAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_av_seff_av_av_InternalAction)
gen_pcm_av_av_seff_av_av_CollectionIteratorAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_av_av_seff_av_av_CollectionIteratorAction)
gen_pcm_av_av_seff_av_av_GuardedBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_av_av_seff_av_av_GuardedBranchTransition)
gen_pcm_av_av_seff_performance_av_av_ResourceCall_CallAction = Generalization(general=CallAction, specific=pcm_av_av_seff_performance_av_av_ResourceCall)
gen_pcm_av_av_seff_performance_av_av_InfrastructureCall_CallAction = Generalization(general=CallAction, specific=pcm_av_av_seff_performance_av_av_InfrastructureCall)
gen_pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour_seff_reliability_av_av_FailureHandlingEntity = Generalization(general=seff_reliability_av_av_FailureHandlingEntity, specific=pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour)
gen_pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour_seff_av_av_ResourceDemandingBehaviour = Generalization(general=seff_av_av_ResourceDemandingBehaviour, specific=pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour)
gen_pcm_av_av_seff_reliability_av_av_RecoveryAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_av_seff_reliability_av_av_RecoveryAction)
gen_pcm_av_av_seff_reliability_av_av_FailureHandlingEntity_Entity = Generalization(general=Entity, specific=pcm_av_av_seff_reliability_av_av_FailureHandlingEntity)
gen_pcm_av_av_qos_performance_av_av_SystemSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_av_av_qos_performance_av_av_SystemSpecifiedExecutionTime)
gen_pcm_av_av_qosannotations_av_av_QoSAnnotations_Entity = Generalization(general=Entity, specific=pcm_av_av_qosannotations_av_av_QoSAnnotations)
gen_pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation)
gen_pcm_av_av_system_av_av_System_entity_av_av_Entity = Generalization(general=entity_av_av_Entity, specific=pcm_av_av_system_av_av_System)
gen_pcm_av_av_system_av_av_System_entity_av_av_ComposedProvidingRequiringEntity = Generalization(general=entity_av_av_ComposedProvidingRequiringEntity, specific=pcm_av_av_system_av_av_System)
gen_pcm_av_av_qos_performance_av_av_SpecifiedExecutionTime_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_av_av_qos_performance_av_av_SpecifiedExecutionTime)
gen_pcm_av_av_qos_performance_av_av_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_av_av_qos_performance_av_av_ComponentSpecifiedExecutionTime)
gen_pcm_av_av_resourceenvironment_av_av_LinkingResource_Entity = Generalization(general=Entity, specific=pcm_av_av_resourceenvironment_av_av_LinkingResource)
gen_pcm_av_av_resourceenvironment_av_av_ResourceContainer_Entity = Generalization(general=Entity, specific=pcm_av_av_resourceenvironment_av_av_ResourceContainer)
gen_pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification)
gen_pcm_av_av_resourceenvironment_av_av_ResourceEnvironment_NamedElement = Generalization(general=NamedElement, specific=pcm_av_av_resourceenvironment_av_av_ResourceEnvironment)
gen_pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification)
gen_pcm_av_av_allocation_av_av_AllocationContext_Entity = Generalization(general=Entity, specific=pcm_av_av_allocation_av_av_AllocationContext)
gen_pcm_av_av_subsystem_av_av_SubSystem_entity_av_av_ComposedProvidingRequiringEntity = Generalization(general=entity_av_av_ComposedProvidingRequiringEntity, specific=pcm_av_av_subsystem_av_av_SubSystem)
gen_pcm_av_av_subsystem_av_av_SubSystem_repository_av_av_RepositoryComponent = Generalization(general=repository_av_av_RepositoryComponent, specific=pcm_av_av_subsystem_av_av_SubSystem)
gen_pcm_av_av_completions_av_av_Completion_entity_av_av_ComposedProvidingRequiringEntity = Generalization(general=entity_av_av_ComposedProvidingRequiringEntity, specific=pcm_av_av_completions_av_av_Completion)
gen_pcm_av_av_completions_av_av_Completion_repository_av_av_ImplementationComponentType = Generalization(general=repository_av_av_ImplementationComponentType, specific=pcm_av_av_completions_av_av_Completion)
gen_pcm_av_av_allocation_av_av_Allocation_Entity = Generalization(general=Entity, specific=pcm_av_av_allocation_av_av_Allocation)
gen_pcm_av_av_completions_av_av_DelegatingExternalCallAction_ExternalCallAction = Generalization(general=ExternalCallAction, specific=pcm_av_av_completions_av_av_DelegatingExternalCallAction)
gen_pcm_av_av_completions_av_av_NetworkDemandParametricResourceDemand_ParametricResourceDemand = Generalization(general=ParametricResourceDemand, specific=pcm_av_av_completions_av_av_NetworkDemandParametricResourceDemand)

# Domain Model
domain_model = DomainModel(
    name="pcm_av_av",
    types={pcm_av_av_DummyClass, pcm_av_av_AdviceAdvice, pcm_av_av_EObject, pcm_av_av_GlobalScopeGlobalScope, pcm_av_av_PerJoinPointScopePerJoinPointScope, pcm_av_av_Advice, ClosedWorkload, PassiveResource, VariableCharacterisation, seff_performance_av_av_InfrastructureCall, seff_performance_av_av_ResourceCall, seff_performance_av_av_ParametricResourceDemand, LoopAction, GuardedBranchTransition, qos_performance_av_av_SpecifiedExecutionTime, composition_av_av_EventChannelSinkConnector, composition_av_av_AssemblyEventConnector, Loop, OpenWorkload, pcm_av_av_GlobalScope, pcm_av_av_PerJoinPointScope, pcm_av_av_core_av_av_PCMRandomVariable, RandomVariable, ResourceInterface, pcm_av_av_entity_av_av_InterfaceProvidingRequiringEntity, entity_av_av_InterfaceProvidingEntity, entity_av_av_InterfaceRequiringEntity, pcm_av_av_entity_av_av_InterfaceProvidingEntity, Entity, ProvidedRole, pcm_av_av_entity_av_av_InterfaceRequiringEntity, entity_av_av_Entity, entity_av_av_ResourceInterfaceRequiringEntity, RequiredRole, pcm_av_av_entity_av_av_ResourceInterfaceRequiringEntity, entity_av_av_ResourceRequiredRole, pcm_av_av_entity_av_av_ResourceRequiredRole, pcm_av_av_entity_av_av_ResourceInterfaceProvidingEntity, entity_av_av_ResourceProvidedRole, Delay, CommunicationLinkResourceSpecification, ProcessingResourceSpecification, pcm_av_av_entity_av_av_ResourceProvidedRole, Role, entity_av_av_ResourceInterfaceProvidingEntity, pcm_av_av_composition_av_av_DelegationConnector, Connector, pcm_av_av_composition_av_av_Connector, pcm_av_av_composition_av_av_ComposedStructure, composition_av_av_AssemblyContext, composition_av_av_ResourceRequiredDelegationConnector, composition_av_av_EventChannel, pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity, composition_av_av_ComposedStructure, entity_av_av_InterfaceProvidingRequiringEntity, pcm_av_av_entity_av_av_NamedElement, pcm_av_av_entity_av_av_ResourceInterfaceProvidingRequiringEntity, pcm_av_av_entity_av_av_Entity, Identifier, entity_av_av_NamedElement, pcm_av_av_composition_av_av_ResourceRequiredDelegationConnector, pcm_av_av_composition_av_av_EventChannel, EventGroup, composition_av_av_EventChannelSourceConnector, pcm_av_av_composition_av_av_EventChannelSourceConnector, SourceRole, pcm_av_av_composition_av_av_EventChannelSinkConnector, composition_av_av_Connector, OperationProvidedRole, pcm_av_av_composition_av_av_RequiredDelegationConnector, SinkRole, PCMRandomVariable, pcm_av_av_composition_av_av_ProvidedDelegationConnector, DelegationConnector, pcm_av_av_composition_av_av_AssemblyEventConnector, OperationRequiredRole, pcm_av_av_composition_av_av_AssemblyConnector, pcm_av_av_composition_av_av_AssemblyInfrastructureConnector, InfrastructureProvidedRole, InfrastructureRequiredRole, pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector, pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector, pcm_av_av_composition_av_av_RequiredResourceDelegationConnector, pcm_av_av_composition_av_av_SourceDelegationConnector, pcm_av_av_composition_av_av_SinkDelegationConnector, VariableUsage, pcm_av_av_usagemodel_av_av_Workload, UsageScenario, pcm_av_av_usagemodel_av_av_UsageScenario, UsageModel, ScenarioBehaviour, Workload, pcm_av_av_usagemodel_av_av_UserData, pcm_av_av_usagemodel_av_av_UsageModel, pcm_av_av_composition_av_av_AssemblyContext, RepositoryComponent, UserData, pcm_av_av_usagemodel_av_av_EntryLevelSystemCall, AbstractUserAction, OperationSignature, BranchTransition, pcm_av_av_usagemodel_av_av_BranchTransition, pcm_av_av_usagemodel_av_av_AbstractUserAction, pcm_av_av_usagemodel_av_av_ScenarioBehaviour, pcm_av_av_usagemodel_av_av_Stop, pcm_av_av_usagemodel_av_av_Start, pcm_av_av_usagemodel_av_av_OpenWorkload, Branch, pcm_av_av_usagemodel_av_av_Branch, pcm_av_av_usagemodel_av_av_Loop, pcm_av_av_repository_av_av_PassiveResource, BasicComponent, ResourceTimeoutFailureType, pcm_av_av_repository_av_av_BasicComponent, ImplementationComponentType, pcm_av_av_usagemodel_av_av_Delay, pcm_av_av_usagemodel_av_av_ClosedWorkload, pcm_av_av_repository_av_av_ImplementationComponentType, CompleteComponentType, ServiceEffectSpecification, InfrastructureSignature, EventType, ResourceSignature, pcm_av_av_repository_av_av_DataType, pcm_av_av_repository_av_av_Repository, Interface, pcm_av_av_repository_av_av_RepositoryComponent, InterfaceProvidingRequiringEntity, Repository, pcm_av_av_repository_av_av_ProvidedRole, pcm_av_av_repository_av_av_Parameter, DataType, pcm_av_av_repository_av_av_Interface, Protocol, FailureType, pcm_av_av_repository_av_av_EventGroup, pcm_av_av_repository_av_av_EventType, Signature, pcm_av_av_repository_av_av_Signature, ExceptionType, pcm_av_av_repository_av_av_ExceptionType, RequiredCharacterisation, pcm_av_av_repository_av_av_RequiredCharacterisation, Parameter_, pcm_av_av_repository_av_av_OperationSignature, OperationInterface, pcm_av_av_repository_av_av_OperationInterface, pcm_av_av_repository_av_av_InfrastructureSignature, InfrastructureInterface, pcm_av_av_repository_av_av_InfrastructureInterface, pcm_av_av_repository_av_av_InfrastructureRequiredRole, pcm_av_av_repository_av_av_RequiredRole, pcm_av_av_repository_av_av_SinkRole, pcm_av_av_repository_av_av_OperationProvidedRole, pcm_av_av_repository_av_av_InfrastructureProvidedRole, pcm_av_av_repository_av_av_CompleteComponentType, pcm_av_av_repository_av_av_OperationRequiredRole, pcm_av_av_repository_av_av_SourceRole, pcm_av_av_repository_av_av_ProvidesComponentType, pcm_av_av_repository_av_av_CompositeComponent, entity_av_av_ComposedProvidingRequiringEntity, repository_av_av_ImplementationComponentType, pcm_av_av_repository_av_av_PrimitiveDataType, ProvidesComponentType, CompositeDataType, InnerDeclaration, pcm_av_av_repository_av_av_InnerDeclaration, NamedElement, pcm_av_av_repository_av_av_Role, pcm_av_av_resourcetype_av_av_ResourceSignature, pcm_av_av_resourcetype_av_av_ProcessingResourceType, ResourceType, HardwareInducedFailureType, pcm_av_av_resourcetype_av_av_ResourceType, UnitCarryingElement, pcm_av_av_repository_av_av_CollectionDataType, repository_av_av_DataType, pcm_av_av_repository_av_av_CompositeDataType, pcm_av_av_resourcetype_av_av_CommunicationLinkResourceType, NetworkInducedFailureType, pcm_av_av_resourcetype_av_av_ResourceInterface, pcm_av_av_protocol_av_av_Protocol, pcm_av_av_parameter_av_av_VariableUsage, CallAction, SynchronisationPoint, CallReturnAction, ResourceRepository, pcm_av_av_resourcetype_av_av_ResourceRepository, SchedulingPolicy, pcm_av_av_resourcetype_av_av_SchedulingPolicy, pcm_av_av_parameter_av_av_CharacterisedVariable, Variable, pcm_av_av_reliability_av_av_FailureOccurrenceDescription, SetVariableAction, SpecifiedOutputParameterAbstraction, EntryLevelSystemCall, parameter_av_av_pcm_av_av_AbstractNamedReference, pcm_av_av_parameter_av_av_VariableCharacterisation, ProcessingResourceType, pcm_av_av_reliability_av_av_SoftwareInducedFailureType, InternalFailureOccurrenceDescription, pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription, FailureOccurrenceDescription, InternalAction, SoftwareInducedFailureType, pcm_av_av_reliability_av_av_NetworkInducedFailureType, pcm_av_av_reliability_av_av_HardwareInducedFailureType, qos_reliability_av_av_SpecifiedReliabilityAnnotation, pcm_av_av_reliability_av_av_ResourceTimeoutFailureType, pcm_av_av_reliability_av_av_FailureType, pcm_av_av_seff_av_av_StopAction, AbstractInternalControlFlowAction, CommunicationLinkResourceType, pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription, ResourceDemandingBehaviour, pcm_av_av_seff_av_av_ResourceDemandingBehaviour, AbstractLoopAction, AbstractBranchTransition, pcm_av_av_seff_av_av_AbstractInternalControlFlowAction, AbstractAction, pcm_av_av_seff_av_av_AbstractAction, pcm_av_av_seff_av_av_CallAction, pcm_av_av_seff_av_av_StartAction, pcm_av_av_seff_av_av_ServiceEffectSpecification, pcm_av_av_seff_av_av_AbstractLoopAction, pcm_av_av_seff_av_av_AbstractBranchTransition, BranchAction, pcm_av_av_seff_av_av_BranchAction, pcm_av_av_seff_av_av_ResourceDemandingInternalBehaviour, ResourceDemandingSEFF, pcm_av_av_seff_av_av_ReleaseAction, pcm_av_av_seff_av_av_LoopAction, pcm_av_av_seff_av_av_ForkAction, ForkedBehaviour, pcm_av_av_seff_av_av_ForkedBehaviour, ForkAction, pcm_av_av_seff_av_av_SynchronisationPoint, pcm_av_av_seff_av_av_ResourceDemandingSEFF, seff_av_av_ServiceEffectSpecification, seff_av_av_ResourceDemandingBehaviour, ResourceDemandingInternalBehaviour, pcm_av_av_seff_av_av_CallReturnAction, pcm_av_av_seff_av_av_ProbabilisticBranchTransition, pcm_av_av_seff_av_av_AcquireAction, pcm_av_av_seff_av_av_ExternalCallAction, seff_av_av_AbstractAction, seff_av_av_CallReturnAction, seff_reliability_av_av_FailureHandlingEntity, pcm_av_av_seff_av_av_SetVariableAction, pcm_av_av_seff_av_av_InternalCallAction, seff_av_av_CallAction, seff_av_av_AbstractInternalControlFlowAction, pcm_av_av_seff_av_av_EmitEventAction, pcm_av_av_seff_av_av_InternalAction, pcm_av_av_seff_av_av_CollectionIteratorAction, pcm_av_av_seff_av_av_GuardedBranchTransition, pcm_av_av_seff_performance_av_av_ResourceCall, pcm_av_av_seff_performance_av_av_InfrastructureCall, pcm_av_av_seff_performance_av_av_ParametricResourceDemand, pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour, seff_reliability_av_av_RecoveryActionBehaviour, seff_reliability_av_av_RecoveryAction, pcm_av_av_seff_reliability_av_av_RecoveryAction, pcm_av_av_seff_reliability_av_av_FailureHandlingEntity, pcm_av_av_qosannotations_av_av_SpecifiedQoSAnnotation, System, SpecifiedQoSAnnotation, pcm_av_av_qosannotations_av_av_SpecifiedOutputParameterAbstraction, pcm_av_av_qos_performance_av_av_SystemSpecifiedExecutionTime, SpecifiedExecutionTime, QoSAnnotations, pcm_av_av_qosannotations_av_av_QoSAnnotations, pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation, ExternalFailureOccurrenceDescription, pcm_av_av_system_av_av_System, pcm_av_av_qos_performance_av_av_SpecifiedExecutionTime, pcm_av_av_qos_performance_av_av_ComponentSpecifiedExecutionTime, LinkingResource, ResourceContainer, pcm_av_av_resourceenvironment_av_av_LinkingResource, ResourceEnvironment, pcm_av_av_resourceenvironment_av_av_ResourceContainer, pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification, pcm_av_av_resourceenvironment_av_av_ResourceEnvironment, pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification, pcm_av_av_allocation_av_av_AllocationContext, AllocationContext, pcm_av_av_subsystem_av_av_SubSystem, repository_av_av_RepositoryComponent, pcm_av_av_completions_av_av_Completion, pcm_av_av_completions_av_av_CompletionRepository, Allocation, pcm_av_av_allocation_av_av_Allocation, Completion, pcm_av_av_completions_av_av_DelegatingExternalCallAction, ExternalCallAction, pcm_av_av_completions_av_av_NetworkDemandParametricResourceDemand, ParametricResourceDemand, ParameterModifier, ComponentType, PrimitiveTypeEnum, VariableCharacterisationType},
    associations={children0, scopedObject1, scopedObject3, children5, closedWorkload_PCMRandomVariable11, passiveResource_capacity_PCMRandomVariable12, variableCharacterisation_Specification13, infrastructureCall__PCMRandomVariable14, resourceCall__PCMRandomVariable15, parametricResourceDemand_PCMRandomVariable18, loopAction_PCMRandomVariable21, guardedBranchTransition_PCMRandomVariable23, specifiedExecutionTime_PCMRandomVariable25, eventChannelSinkConnector__FilterCondition26, assemblyEventConnector__FilterCondition27, loop_LoopIteration30, scopedObject7, scopedObject9, resourceInterfaceProvidingEntity__ResourceProvidedRole42, providedResourceInterface__ResourceProvidedRole44, providedRoles_InterfaceProvidingEntity45, requiredRoles_InterfaceRequiringEntity47, resourceRequiredRoles__ResourceInterfaceRequiringEntity49, requiredResourceInterface__ResourceRequiredRole52, resourceInterfaceRequiringEntity__ResourceRequiredRole54, resourceProvidedRoles__ResourceInterfaceProvidingEntity57, openWorkload_PCMRandomVariable32, delay_TimeSpecification34, communicationLinkResourceSpecifcation_throughput_PCMRandomVariable36, processingResourceSpecification_processingRate_PCMRandomVariable37, communicationLinkResourceSpecification_latency_PCMRandomVariable39, parentStructure__Connector60, assemblyContexts__ComposedStructure63, resourceRequiredDelegationConnectors_ComposedStructure66, eventChannel__ComposedStructure69, innerResourceRequiredRole_ResourceRequiredDelegationConnector75, outerResourceRequiredRole_ResourceRequiredDelegationConnector76, parentStructure_ResourceRequiredDelegationConnector79, eventGroup__EventChannel82, eventChannelSourceConnector__EventChannel83, eventChannelSinkConnector__EventChannel86, parentStructure__EventChannel89, sourceRole__EventChannelSourceRole92, assemblyContext__EventChannelSourceConnector93, eventChannel__EventChannelSourceConnector95, connectors__ComposedStructure72, innerProvidedRole_ProvidedDelegationConnector107, outerProvidedRole_ProvidedDelegationConnector108, assemblyContext_ProvidedDelegationConnector111, sinkRole__EventChannelSinkConnector98, filterCondition__EventChannelSinkConnector99, assemblyContext__EventChannelSinkConnector101, eventChannel__EventChannelSinkConnector104, requiringAssemblyContext_AssemblyConnector121, providingAssemblyContext_AssemblyConnector123, providedRole_AssemblyConnector126, requiredRole_AssemblyConnector129, sinkRole__AssemblyEventConnector132, sourceRole__AssemblyEventConnector134, innerRequiredRole_RequiredDelegationConnector114, outerRequiredRole_RequiredDelegationConnector115, assemblyContext_RequiredDelegationConnector118, innerSinkRole__SinkRole156, outerSinkRole__SinkRole159, providedRole__AssemblyInfrastructureConnector162, requiredRole__AssemblyInfrastructureConnector163, providingAssemblyContext__AssemblyInfrastructureConnector165, requiringAssemblyContext__AssemblyInfrastructureConnector168, innerProvidedRole__ProvidedInfrastructureDelegationConnector171, outerProvidedRole__ProvidedInfrastructureDelegationConnector173, assemblyContext__ProvidedInfrastructureDelegationConnector176, innerRequiredRole__RequiredInfrastructureDelegationConnector179, outerRequiredRole__RequiredInfrastructureDelegationConnector181, assemblyContext__RequiredInfrastructureDelegationConnector184, assemblyContext__RequiredResourceDelegationConnector187, sinkAssemblyContext__AssemblyEventConnector137, sourceAssemblyContext__AssemblyEventConnector140, filterCondition__AssemblyEventConnector143, innerSourceRole__SourceRole146, outerSourceRole__SourceRole148, assemblyContext__SourceDelegationConnector151, assemblyContext__SinkDelegationConnector154, configParameterUsages__AssemblyContext199, usageScenario_Workload201, usageModel_UsageScenario203, scenarioBehaviour_UsageScenario205, workload_UsageScenario207, assemblyContext_userData209, usageModel_UserData211, userDataParameterUsages_UserData214, innerRequiredRole__RequiredResourceDelegationConnector189, outerRequiredRole__RequiredResourceDelegationConnector192, parentStructure__AssemblyContext195, encapsulatedComponent__AssemblyContext198, userData_UsageModel220, providedRole_EntryLevelSystemCall222, operationSignature__EntryLevelSystemCall224, outputParameterUsages_EntryLevelSystemCall226, usageScenario_UsageModel217, usageScenario_SenarioBehaviour240, branchTransition_ScenarioBehaviour243, loop_ScenarioBehaviour245, actions_ScenarioBehaviour248, inputParameterUsages_EntryLevelSystemCall229, successor232, predecessor234, scenarioBehaviour_AbstractUserAction237, loopIteration_Loop259, bodyBehaviour_Loop262, branch_BranchTransition251, branchedBehaviour_BranchTransition253, branchTransitions_Branch256, thinkTime_ClosedWorkload271, capacity_PassiveResource274, basicComponent_PassiveResource277, resourceTimeoutFailureType__PassiveResource279, interArrivalTime_OpenWorkload265, timeSpecification_Delay268, passiveResource_BasicComponent282, parentCompleteComponentTypes285, componentParameterUsage_ImplementationComponentType286, serviceEffectSpecifications__BasicComponent280, infrastructureSignature__Parameter295, operationSignature__Parameter297, eventType__Parameter300, resourceSignature__Parameter302, repository__DataType303, components__Repository306, interfaces__Repository309, repository__RepositoryComponent289, providingEntity_ProvidedRole291, dataType__Parameter294, dataTypes__Repository313, parentInterfaces__Interface316, protocols__Interface318, failureTypes__Repository311, parameter325, interface_RequiredCharacterisation326, eventTypes__EventGroup329, parameter__EventType332, eventGroup__EventType335, exceptions__Signature338, failureType339, requiredCharacterisations320, repository__Interface322, requiringEntity_RequiredRole352, interface__OperationSignature355, parameters__OperationSignature357, returnType__OperationSignature360, parameters__InfrastructureSignature342, infrastructureInterface__InfrastructureSignature345, infrastructureSignatures__InfrastructureInterface347, requiredInterface__InfrastructureRequiredRole350, eventGroup__SourceRole367, eventGroup__SinkRole369, providedInterface__OperationProvidedRole371, providedInterface__InfrastructureProvidedRole373, signatures__OperationInterface362, requiredInterface__OperationRequiredRole365, parentProvidesComponentTypes375, parentType_CompositeDataType378, innerDeclaration_CompositeDataType379, datatype_InnerDeclaration381, compositeDataType_InnerDeclaration383, parameter__ResourceSignature386, resourceInterface__ResourceSignature389, hardwareInducedFailureType__ProcessingResourceType392, innerType_CollectionDataType376, networkInducedFailureType__CommunicationLinkResourceType406, resourceRepository__ResourceInterface408, resourceSignatures__ResourceInterface411, variableCharacterisation_VariableUsage414, userData_VariableUsage417, callAction__VariableUsage420, synchronisationPoint_VariableUsage422, resourceRepository_ResourceType394, resourceInterfaces__ResourceRepository396, schedulingPolicies__ResourceRepository399, availableResourceTypes_ResourceRepository401, resourceRepository__SchedulingPolicy403, specification_VariableCharacterisation439, variableUsage_VariableCharacterisation442, callReturnAction__VariableUsage424, setVariableAction_VariableUsage426, specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage428, assemblyContext__VariableUsage430, entryLevelSystemCall_InputParameterUsage433, entryLevelSystemCall_OutputParameterUsage435, namedReference__VariableUsage438, processingResourceType__HardwareInducedFailureType445, internalFailureOccurrenceDescriptions__SoftwareInducedFailureType447, internalAction__InternalFailureOccurrenceDescription449, softwareInducedFailureType__InternalFailureOccurrenceDescription451, specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription455, failureType__ExternalFailureOccurrenceDescription457, passiveResource__ResourceTimeoutFailureType459, repository__FailureType462, communicationLinkResourceType__NetworkInducedFailureType453, predecessor_AbstractAction474, successor_AbstractAction476, resourceDemandingBehaviour_AbstractAction479, abstractLoopAction_ResourceDemandingBehaviour481, resourceDemand_Action465, infrastructureCall__Action468, resourceCall__Action471, branches_Branch496, inputVariableUsages__CallAction499, abstractBranchTransition_ResourceDemandingBehaviour483, steps_Behaviour485, bodyBehaviour_Loop488, branchAction_AbstractBranchTransition491, branchBehaviour_BranchTransition493, resourceDemandingSEFF_ResourceDemandingInternalBehaviour508, passiveResource_ReleaseAction510, iterationCount_LoopAction512, asynchronousForkedBehaviours_ForkAction515, synchronisingBehaviours_ForkAction517, synchronisationPoint_ForkedBehaviour520, forkAction_ForkedBehaivour523, outputParameterUsage_SynchronisationPoint525, describedService__SEFF502, basicComponent_ServiceEffectSpecification503, resourceDemandingInternalBehaviours506, calledService_ExternalService534, role_ExternalService536, returnVariableUsage__CallReturnAction539, forkAction_SynchronisationPoint528, synchronousForkedBehaviours_SynchronisationPoint531, branchCondition_GuardedBranchTransition546, localVariableUsages_SetVariableAction549, calledResourceDemandingInternalBehaviour552, eventType__EmitEventAction554, sourceRole__EmitEventAction556, passiveresource_AcquireAction542, parameter_CollectionIteratorAction544, signature__InfrastructureCall562, numberOfCalls__InfrastructureCall564, action__InfrastructureCall567, requiredRole__InfrastructureCall569, internalFailureOccurrenceDescriptions__InternalAction559, specification_ParametericResourceDemand583, requiredResource_ParametricResourceDemand586, action_ParametricResourceDemand588, action__ResourceCall572, resourceRequiredRole__ResourceCall575, signature__ResourceCall577, numberOfCalls__ResourceCall580, failureHandlingAlternatives__RecoveryActionBehaviour591, recoveryAction__RecoveryActionBehaviour592, primaryBehaviour__RecoveryAction594, recoveryActionBehaviours__RecoveryAction596, failureTypes_FailureHandlingEntity599, signature_SpecifiedQoSAnnation601, system_QoSAnnotations610, specifiedQoSAnnotations_QoSAnnotations611, signature_SpecifiedOutputParameterAbstraction613, role_SpecifiedOutputParameterAbstraction615, expectedExternalOutputs_SpecifiedOutputParameterAbstraction618, qosAnnotations_SpecifiedOutputParameterAbstraction621, role_SpecifiedQoSAnnotation603, qosAnnotations_SpecifiedQoSAnnotation605, specifiedOutputParameterAbstractions_QoSAnnotations607, externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation629, specification_SpecifiedExecutionTime624, assemblyContext_ComponentSpecifiedExecutionTime627, linkingResources__ResourceEnvironment634, resourceContainer_ResourceEnvironment636, connectedResourceContainers_LinkingResource638, communicationLinkResourceSpecifications_LinkingResource640, resourceEnvironment_LinkingResource643, activeResourceSpecifications_ResourceContainer645, resourceEnvironment_ResourceContainer648, nestedResourceContainers__ResourceContainer651, parentResourceContainer__ResourceContainer654, qosAnnotations_System631, resourceContainer_ProcessingResourceSpecification665, linkingResource_CommunicationLinkResourceSpecification668, communicationLinkResourceType_CommunicationLinkResourceSpecification671, latency_CommunicationLinkResourceSpecification673, throughput_CommunicationLinkResourceSpecification676, schedulingPolicy657, activeResourceType_ActiveResourceSpecification659, processingRate_ProcessingResourceSpecification662, targetResourceEnvironment_Allocation687, system_Allocation689, allocationContexts_Allocation692, resourceContainer_AllocationContext679, assemblyContext_AllocationContext681, allocation_AllocationContext684, eventChannel__AllocationContext685, completions_CompletionRepository694, requiredCommunicationLinkResource_ParametricResourceDemand695},
    generalizations={gen_pcm_av_av_core_av_av_PCMRandomVariable_RandomVariable, gen_pcm_av_av_entity_av_av_InterfaceProvidingRequiringEntity_entity_av_av_InterfaceProvidingEntity, gen_pcm_av_av_entity_av_av_InterfaceProvidingRequiringEntity_entity_av_av_InterfaceRequiringEntity, gen_pcm_av_av_entity_av_av_InterfaceProvidingEntity_Entity, gen_pcm_av_av_entity_av_av_InterfaceRequiringEntity_entity_av_av_Entity, gen_pcm_av_av_entity_av_av_InterfaceRequiringEntity_entity_av_av_ResourceInterfaceRequiringEntity, gen_pcm_av_av_entity_av_av_ResourceInterfaceRequiringEntity_Entity, gen_pcm_av_av_entity_av_av_ResourceRequiredRole_Role, gen_pcm_av_av_entity_av_av_ResourceInterfaceProvidingEntity_Entity, gen_pcm_av_av_entity_av_av_ResourceProvidedRole_Role, gen_pcm_av_av_composition_av_av_DelegationConnector_Connector, gen_pcm_av_av_composition_av_av_Connector_Entity, gen_pcm_av_av_composition_av_av_ComposedStructure_Entity, gen_pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity_composition_av_av_ComposedStructure, gen_pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity_entity_av_av_InterfaceProvidingRequiringEntity, gen_pcm_av_av_entity_av_av_ResourceInterfaceProvidingRequiringEntity_entity_av_av_ResourceInterfaceRequiringEntity, gen_pcm_av_av_entity_av_av_ResourceInterfaceProvidingRequiringEntity_entity_av_av_ResourceInterfaceProvidingEntity, gen_pcm_av_av_entity_av_av_Entity_Identifier, gen_pcm_av_av_entity_av_av_Entity_entity_av_av_NamedElement, gen_pcm_av_av_composition_av_av_EventChannel_Entity, gen_pcm_av_av_composition_av_av_EventChannelSourceConnector_Connector, gen_pcm_av_av_composition_av_av_EventChannelSinkConnector_Connector, gen_pcm_av_av_composition_av_av_RequiredDelegationConnector_DelegationConnector, gen_pcm_av_av_composition_av_av_ProvidedDelegationConnector_DelegationConnector, gen_pcm_av_av_composition_av_av_AssemblyEventConnector_Connector, gen_pcm_av_av_composition_av_av_AssemblyConnector_Connector, gen_pcm_av_av_composition_av_av_AssemblyInfrastructureConnector_Connector, gen_pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector_DelegationConnector, gen_pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector_DelegationConnector, gen_pcm_av_av_composition_av_av_RequiredResourceDelegationConnector_DelegationConnector, gen_pcm_av_av_composition_av_av_SourceDelegationConnector_DelegationConnector, gen_pcm_av_av_composition_av_av_SinkDelegationConnector_DelegationConnector, gen_pcm_av_av_usagemodel_av_av_UsageScenario_Entity, gen_pcm_av_av_composition_av_av_AssemblyContext_Entity, gen_pcm_av_av_usagemodel_av_av_EntryLevelSystemCall_AbstractUserAction, gen_pcm_av_av_usagemodel_av_av_AbstractUserAction_Entity, gen_pcm_av_av_usagemodel_av_av_ScenarioBehaviour_Entity, gen_pcm_av_av_usagemodel_av_av_Stop_AbstractUserAction, gen_pcm_av_av_usagemodel_av_av_Start_AbstractUserAction, gen_pcm_av_av_usagemodel_av_av_OpenWorkload_Workload, gen_pcm_av_av_usagemodel_av_av_Branch_AbstractUserAction, gen_pcm_av_av_usagemodel_av_av_Loop_AbstractUserAction, gen_pcm_av_av_repository_av_av_PassiveResource_Entity, gen_pcm_av_av_repository_av_av_BasicComponent_ImplementationComponentType, gen_pcm_av_av_usagemodel_av_av_Delay_AbstractUserAction, gen_pcm_av_av_usagemodel_av_av_ClosedWorkload_Workload, gen_pcm_av_av_repository_av_av_ImplementationComponentType_RepositoryComponent, gen_pcm_av_av_repository_av_av_Repository_Entity, gen_pcm_av_av_repository_av_av_RepositoryComponent_InterfaceProvidingRequiringEntity, gen_pcm_av_av_repository_av_av_ProvidedRole_Role, gen_pcm_av_av_repository_av_av_Interface_Entity, gen_pcm_av_av_repository_av_av_EventGroup_Interface, gen_pcm_av_av_repository_av_av_EventType_Signature, gen_pcm_av_av_repository_av_av_Signature_Entity, gen_pcm_av_av_repository_av_av_OperationSignature_Signature, gen_pcm_av_av_repository_av_av_OperationInterface_Interface, gen_pcm_av_av_repository_av_av_InfrastructureSignature_Signature, gen_pcm_av_av_repository_av_av_InfrastructureInterface_Interface, gen_pcm_av_av_repository_av_av_InfrastructureRequiredRole_RequiredRole, gen_pcm_av_av_repository_av_av_SourceRole_RequiredRole, gen_pcm_av_av_repository_av_av_RequiredRole_Role, gen_pcm_av_av_repository_av_av_SinkRole_ProvidedRole, gen_pcm_av_av_repository_av_av_OperationProvidedRole_ProvidedRole, gen_pcm_av_av_repository_av_av_InfrastructureProvidedRole_ProvidedRole, gen_pcm_av_av_repository_av_av_CompleteComponentType_RepositoryComponent, gen_pcm_av_av_repository_av_av_OperationRequiredRole_RequiredRole, gen_pcm_av_av_repository_av_av_ProvidesComponentType_RepositoryComponent, gen_pcm_av_av_repository_av_av_CompositeComponent_entity_av_av_ComposedProvidingRequiringEntity, gen_pcm_av_av_repository_av_av_CompositeComponent_repository_av_av_ImplementationComponentType, gen_pcm_av_av_repository_av_av_PrimitiveDataType_DataType, gen_pcm_av_av_repository_av_av_InnerDeclaration_NamedElement, gen_pcm_av_av_repository_av_av_Role_Entity, gen_pcm_av_av_resourcetype_av_av_ResourceSignature_Entity, gen_pcm_av_av_resourcetype_av_av_ProcessingResourceType_ResourceType, gen_pcm_av_av_resourcetype_av_av_ResourceType_entity_av_av_Entity, gen_pcm_av_av_resourcetype_av_av_ResourceType_UnitCarryingElement, gen_pcm_av_av_resourcetype_av_av_ResourceType_entity_av_av_ResourceInterfaceProvidingEntity, gen_pcm_av_av_repository_av_av_CollectionDataType_entity_av_av_Entity, gen_pcm_av_av_repository_av_av_CollectionDataType_repository_av_av_DataType, gen_pcm_av_av_repository_av_av_CompositeDataType_entity_av_av_Entity, gen_pcm_av_av_repository_av_av_CompositeDataType_repository_av_av_DataType, gen_pcm_av_av_resourcetype_av_av_CommunicationLinkResourceType_ResourceType, gen_pcm_av_av_resourcetype_av_av_ResourceInterface_Entity, gen_pcm_av_av_resourcetype_av_av_SchedulingPolicy_Entity, gen_pcm_av_av_parameter_av_av_CharacterisedVariable_Variable, gen_pcm_av_av_reliability_av_av_SoftwareInducedFailureType_FailureType, gen_pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_av_av_reliability_av_av_NetworkInducedFailureType_FailureType, gen_pcm_av_av_reliability_av_av_HardwareInducedFailureType_FailureType, gen_pcm_av_av_reliability_av_av_ResourceTimeoutFailureType_SoftwareInducedFailureType, gen_pcm_av_av_reliability_av_av_FailureType_Entity, gen_pcm_av_av_seff_av_av_StopAction_AbstractInternalControlFlowAction, gen_pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_av_av_seff_av_av_ResourceDemandingBehaviour_Identifier, gen_pcm_av_av_seff_av_av_AbstractInternalControlFlowAction_AbstractAction, gen_pcm_av_av_seff_av_av_AbstractAction_Entity, gen_pcm_av_av_seff_av_av_StartAction_AbstractInternalControlFlowAction, gen_pcm_av_av_seff_av_av_AbstractLoopAction_AbstractInternalControlFlowAction, gen_pcm_av_av_seff_av_av_AbstractBranchTransition_Entity, gen_pcm_av_av_seff_av_av_BranchAction_AbstractInternalControlFlowAction, gen_pcm_av_av_seff_av_av_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour, gen_pcm_av_av_seff_av_av_ReleaseAction_AbstractInternalControlFlowAction, gen_pcm_av_av_seff_av_av_LoopAction_AbstractLoopAction, gen_pcm_av_av_seff_av_av_ForkAction_AbstractInternalControlFlowAction, gen_pcm_av_av_seff_av_av_ForkedBehaviour_ResourceDemandingBehaviour, gen_pcm_av_av_seff_av_av_ResourceDemandingSEFF_Identifier, gen_pcm_av_av_seff_av_av_ResourceDemandingSEFF_seff_av_av_ServiceEffectSpecification, gen_pcm_av_av_seff_av_av_ResourceDemandingSEFF_seff_av_av_ResourceDemandingBehaviour, gen_pcm_av_av_seff_av_av_CallReturnAction_CallAction, gen_pcm_av_av_seff_av_av_ProbabilisticBranchTransition_AbstractBranchTransition, gen_pcm_av_av_seff_av_av_AcquireAction_AbstractInternalControlFlowAction, gen_pcm_av_av_seff_av_av_ExternalCallAction_seff_av_av_AbstractAction, gen_pcm_av_av_seff_av_av_ExternalCallAction_seff_av_av_CallReturnAction, gen_pcm_av_av_seff_av_av_ExternalCallAction_seff_reliability_av_av_FailureHandlingEntity, gen_pcm_av_av_seff_av_av_SetVariableAction_AbstractInternalControlFlowAction, gen_pcm_av_av_seff_av_av_InternalCallAction_seff_av_av_CallAction, gen_pcm_av_av_seff_av_av_InternalCallAction_seff_av_av_AbstractInternalControlFlowAction, gen_pcm_av_av_seff_av_av_EmitEventAction_seff_av_av_AbstractAction, gen_pcm_av_av_seff_av_av_EmitEventAction_seff_av_av_CallAction, gen_pcm_av_av_seff_av_av_InternalAction_AbstractInternalControlFlowAction, gen_pcm_av_av_seff_av_av_CollectionIteratorAction_AbstractLoopAction, gen_pcm_av_av_seff_av_av_GuardedBranchTransition_AbstractBranchTransition, gen_pcm_av_av_seff_performance_av_av_ResourceCall_CallAction, gen_pcm_av_av_seff_performance_av_av_InfrastructureCall_CallAction, gen_pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour_seff_reliability_av_av_FailureHandlingEntity, gen_pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour_seff_av_av_ResourceDemandingBehaviour, gen_pcm_av_av_seff_reliability_av_av_RecoveryAction_AbstractInternalControlFlowAction, gen_pcm_av_av_seff_reliability_av_av_FailureHandlingEntity_Entity, gen_pcm_av_av_qos_performance_av_av_SystemSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_av_av_qosannotations_av_av_QoSAnnotations_Entity, gen_pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation, gen_pcm_av_av_system_av_av_System_entity_av_av_Entity, gen_pcm_av_av_system_av_av_System_entity_av_av_ComposedProvidingRequiringEntity, gen_pcm_av_av_qos_performance_av_av_SpecifiedExecutionTime_SpecifiedQoSAnnotation, gen_pcm_av_av_qos_performance_av_av_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_av_av_resourceenvironment_av_av_LinkingResource_Entity, gen_pcm_av_av_resourceenvironment_av_av_ResourceContainer_Entity, gen_pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification_Identifier, gen_pcm_av_av_resourceenvironment_av_av_ResourceEnvironment_NamedElement, gen_pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification_Identifier, gen_pcm_av_av_allocation_av_av_AllocationContext_Entity, gen_pcm_av_av_subsystem_av_av_SubSystem_entity_av_av_ComposedProvidingRequiringEntity, gen_pcm_av_av_subsystem_av_av_SubSystem_repository_av_av_RepositoryComponent, gen_pcm_av_av_completions_av_av_Completion_entity_av_av_ComposedProvidingRequiringEntity, gen_pcm_av_av_completions_av_av_Completion_repository_av_av_ImplementationComponentType, gen_pcm_av_av_allocation_av_av_Allocation_Entity, gen_pcm_av_av_completions_av_av_DelegatingExternalCallAction_ExternalCallAction, gen_pcm_av_av_completions_av_av_NetworkDemandParametricResourceDemand_ParametricResourceDemand},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)