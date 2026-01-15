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

ComponentType: Enumeration = Enumeration(
    name="ComponentType",
    literals={
            EnumerationLiteral(name="BUSINESS_COMPONENT"),
			EnumerationLiteral(name="INFRASTRUCTURE_COMPONENT")
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
pcm_av_pc_DummyClass = Class(name="pcm::av::pc::DummyClass")
pcm_av_pc_Advice = Class(name="pcm::av::pc::Advice")
pcm_av_pc_EObject = Class(name="pcm::av::pc::EObject")
pcm_av_pc_GlobalScope = Class(name="pcm::av::pc::GlobalScope")
pcm_av_pc_PerJoinPointScope = Class(name="pcm::av::pc::PerJoinPointScope")
pcm_av_pc_Pointcut = Class(name="pcm::av::pc::Pointcut")
pcm_av_pc_core_av_pc_PCMRandomVariable = Class(name="pcm::av::pc::core::av::pc::PCMRandomVariable")
RandomVariable = Class(name="RandomVariable")
pcm_av_pc_entity_av_pc_ResourceInterfaceRequiringEntity = Class(name="pcm::av::pc::entity::av::pc::ResourceInterfaceRequiringEntity")
seff_performance_av_pc_ResourceCall = Class(name="seff::performance::av::pc::ResourceCall")
entity_av_pc_ResourceRequiredRole = Class(name="entity::av::pc::ResourceRequiredRole")
pcm_av_pc_entity_av_pc_ResourceRequiredRole = Class(name="pcm::av::pc::entity::av::pc::ResourceRequiredRole")
seff_performance_av_pc_ParametricResourceDemand = Class(name="seff::performance::av::pc::ParametricResourceDemand")
LoopAction = Class(name="LoopAction")
GuardedBranchTransition = Class(name="GuardedBranchTransition")
pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingEntity = Class(name="pcm::av::pc::entity::av::pc::ResourceInterfaceProvidingEntity")
qos_performance_av_pc_SpecifiedExecutionTime = Class(name="qos::performance::av::pc::SpecifiedExecutionTime")
entity_av_pc_ResourceProvidedRole = Class(name="entity::av::pc::ResourceProvidedRole")
composition_av_pc_EventChannelSinkConnector = Class(name="composition::av::pc::EventChannelSinkConnector")
composition_av_pc_AssemblyEventConnector = Class(name="composition::av::pc::AssemblyEventConnector")
Loop = Class(name="Loop")
OpenWorkload = Class(name="OpenWorkload")
Delay = Class(name="Delay")
CommunicationLinkResourceSpecification = Class(name="CommunicationLinkResourceSpecification")
ProcessingResourceSpecification = Class(name="ProcessingResourceSpecification")
pcm_av_pc_entity_av_pc_ResourceProvidedRole = Class(name="pcm::av::pc::entity::av::pc::ResourceProvidedRole")
Role = Class(name="Role")
entity_av_pc_ResourceInterfaceProvidingEntity = Class(name="entity::av::pc::ResourceInterfaceProvidingEntity")
ResourceInterface = Class(name="ResourceInterface")
pcm_av_pc_entity_av_pc_InterfaceProvidingRequiringEntity = Class(name="pcm::av::pc::entity::av::pc::InterfaceProvidingRequiringEntity")
entity_av_pc_InterfaceProvidingEntity = Class(name="entity::av::pc::InterfaceProvidingEntity")
entity_av_pc_InterfaceRequiringEntity = Class(name="entity::av::pc::InterfaceRequiringEntity")
ClosedWorkload = Class(name="ClosedWorkload")
pcm_av_pc_entity_av_pc_InterfaceProvidingEntity = Class(name="pcm::av::pc::entity::av::pc::InterfaceProvidingEntity")
Entity = Class(name="Entity")
PassiveResource = Class(name="PassiveResource")
ProvidedRole = Class(name="ProvidedRole")
VariableCharacterisation = Class(name="VariableCharacterisation")
pcm_av_pc_entity_av_pc_InterfaceRequiringEntity = Class(name="pcm::av::pc::entity::av::pc::InterfaceRequiringEntity")
entity_av_pc_Entity = Class(name="entity::av::pc::Entity")
entity_av_pc_ResourceInterfaceRequiringEntity = Class(name="entity::av::pc::ResourceInterfaceRequiringEntity")
seff_performance_av_pc_InfrastructureCall = Class(name="seff::performance::av::pc::InfrastructureCall")
RequiredRole = Class(name="RequiredRole")
composition_av_pc_AssemblyContext = Class(name="composition::av::pc::AssemblyContext")
composition_av_pc_ResourceRequiredDelegationConnector = Class(name="composition::av::pc::ResourceRequiredDelegationConnector")
pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity = Class(name="pcm::av::pc::entity::av::pc::ComposedProvidingRequiringEntity")
composition_av_pc_ComposedStructure = Class(name="composition::av::pc::ComposedStructure")
entity_av_pc_InterfaceProvidingRequiringEntity = Class(name="entity::av::pc::InterfaceProvidingRequiringEntity")
composition_av_pc_EventChannel = Class(name="composition::av::pc::EventChannel")
composition_av_pc_Connector = Class(name="composition::av::pc::Connector")
pcm_av_pc_entity_av_pc_NamedElement = Class(name="pcm::av::pc::entity::av::pc::NamedElement")
pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingRequiringEntity = Class(name="pcm::av::pc::entity::av::pc::ResourceInterfaceProvidingRequiringEntity")
pcm_av_pc_entity_av_pc_Entity = Class(name="pcm::av::pc::entity::av::pc::Entity")
Identifier = Class(name="Identifier")
entity_av_pc_NamedElement = Class(name="entity::av::pc::NamedElement")
pcm_av_pc_composition_av_pc_DelegationConnector = Class(name="pcm::av::pc::composition::av::pc::DelegationConnector")
Connector = Class(name="Connector")
pcm_av_pc_composition_av_pc_Connector = Class(name="pcm::av::pc::composition::av::pc::Connector")
pcm_av_pc_composition_av_pc_ComposedStructure = Class(name="pcm::av::pc::composition::av::pc::ComposedStructure")
pcm_av_pc_composition_av_pc_EventChannelSourceConnector = Class(name="pcm::av::pc::composition::av::pc::EventChannelSourceConnector")
SourceRole = Class(name="SourceRole")
pcm_av_pc_composition_av_pc_EventChannelSinkConnector = Class(name="pcm::av::pc::composition::av::pc::EventChannelSinkConnector")
SinkRole = Class(name="SinkRole")
PCMRandomVariable = Class(name="PCMRandomVariable")
pcm_av_pc_composition_av_pc_ProvidedDelegationConnector = Class(name="pcm::av::pc::composition::av::pc::ProvidedDelegationConnector")
DelegationConnector = Class(name="DelegationConnector")
pcm_av_pc_composition_av_pc_ResourceRequiredDelegationConnector = Class(name="pcm::av::pc::composition::av::pc::ResourceRequiredDelegationConnector")
pcm_av_pc_composition_av_pc_EventChannel = Class(name="pcm::av::pc::composition::av::pc::EventChannel")
EventGroup = Class(name="EventGroup")
composition_av_pc_EventChannelSourceConnector = Class(name="composition::av::pc::EventChannelSourceConnector")
OperationRequiredRole = Class(name="OperationRequiredRole")
OperationProvidedRole = Class(name="OperationProvidedRole")
pcm_av_pc_composition_av_pc_RequiredDelegationConnector = Class(name="pcm::av::pc::composition::av::pc::RequiredDelegationConnector")
pcm_av_pc_composition_av_pc_AssemblyEventConnector = Class(name="pcm::av::pc::composition::av::pc::AssemblyEventConnector")
pcm_av_pc_composition_av_pc_SourceDelegationConnector = Class(name="pcm::av::pc::composition::av::pc::SourceDelegationConnector")
pcm_av_pc_composition_av_pc_AssemblyConnector = Class(name="pcm::av::pc::composition::av::pc::AssemblyConnector")
pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector = Class(name="pcm::av::pc::composition::av::pc::RequiredResourceDelegationConnector")
pcm_av_pc_composition_av_pc_AssemblyContext = Class(name="pcm::av::pc::composition::av::pc::AssemblyContext")
RepositoryComponent = Class(name="RepositoryComponent")
VariableUsage = Class(name="VariableUsage")
pcm_av_pc_composition_av_pc_SinkDelegationConnector = Class(name="pcm::av::pc::composition::av::pc::SinkDelegationConnector")
pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector = Class(name="pcm::av::pc::composition::av::pc::AssemblyInfrastructureConnector")
InfrastructureProvidedRole = Class(name="InfrastructureProvidedRole")
InfrastructureRequiredRole = Class(name="InfrastructureRequiredRole")
pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector = Class(name="pcm::av::pc::composition::av::pc::ProvidedInfrastructureDelegationConnector")
pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector = Class(name="pcm::av::pc::composition::av::pc::RequiredInfrastructureDelegationConnector")
OperationSignature = Class(name="OperationSignature")
pcm_av_pc_usagemodel_av_pc_Workload = Class(name="pcm::av::pc::usagemodel::av::pc::Workload")
UsageScenario = Class(name="UsageScenario")
pcm_av_pc_usagemodel_av_pc_UsageScenario = Class(name="pcm::av::pc::usagemodel::av::pc::UsageScenario")
UsageModel = Class(name="UsageModel")
ScenarioBehaviour = Class(name="ScenarioBehaviour")
Workload = Class(name="Workload")
pcm_av_pc_usagemodel_av_pc_UserData = Class(name="pcm::av::pc::usagemodel::av::pc::UserData")
pcm_av_pc_usagemodel_av_pc_UsageModel = Class(name="pcm::av::pc::usagemodel::av::pc::UsageModel")
UserData = Class(name="UserData")
pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall = Class(name="pcm::av::pc::usagemodel::av::pc::EntryLevelSystemCall")
AbstractUserAction = Class(name="AbstractUserAction")
BranchTransition = Class(name="BranchTransition")
pcm_av_pc_usagemodel_av_pc_AbstractUserAction = Class(name="pcm::av::pc::usagemodel::av::pc::AbstractUserAction")
pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour = Class(name="pcm::av::pc::usagemodel::av::pc::ScenarioBehaviour")
pcm_av_pc_usagemodel_av_pc_Start = Class(name="pcm::av::pc::usagemodel::av::pc::Start")
pcm_av_pc_usagemodel_av_pc_OpenWorkload = Class(name="pcm::av::pc::usagemodel::av::pc::OpenWorkload")
pcm_av_pc_usagemodel_av_pc_BranchTransition = Class(name="pcm::av::pc::usagemodel::av::pc::BranchTransition")
Branch = Class(name="Branch")
pcm_av_pc_usagemodel_av_pc_Branch = Class(name="pcm::av::pc::usagemodel::av::pc::Branch")
pcm_av_pc_usagemodel_av_pc_Loop = Class(name="pcm::av::pc::usagemodel::av::pc::Loop")
pcm_av_pc_usagemodel_av_pc_Stop = Class(name="pcm::av::pc::usagemodel::av::pc::Stop")
pcm_av_pc_repository_av_pc_PassiveResource = Class(name="pcm::av::pc::repository::av::pc::PassiveResource")
BasicComponent = Class(name="BasicComponent")
ResourceTimeoutFailureType = Class(name="ResourceTimeoutFailureType")
pcm_av_pc_repository_av_pc_BasicComponent = Class(name="pcm::av::pc::repository::av::pc::BasicComponent")
ImplementationComponentType = Class(name="ImplementationComponentType")
pcm_av_pc_usagemodel_av_pc_Delay = Class(name="pcm::av::pc::usagemodel::av::pc::Delay")
pcm_av_pc_usagemodel_av_pc_ClosedWorkload = Class(name="pcm::av::pc::usagemodel::av::pc::ClosedWorkload")
CompleteComponentType = Class(name="CompleteComponentType")
ServiceEffectSpecification = Class(name="ServiceEffectSpecification")
pcm_av_pc_repository_av_pc_ImplementationComponentType = Class(name="pcm::av::pc::repository::av::pc::ImplementationComponentType")
ResourceSignature = Class(name="ResourceSignature")
pcm_av_pc_repository_av_pc_DataType = Class(name="pcm::av::pc::repository::av::pc::DataType")
pcm_av_pc_repository_av_pc_Repository = Class(name="pcm::av::pc::repository::av::pc::Repository")
Interface = Class(name="Interface")
FailureType = Class(name="FailureType")
pcm_av_pc_repository_av_pc_RepositoryComponent = Class(name="pcm::av::pc::repository::av::pc::RepositoryComponent")
InterfaceProvidingRequiringEntity = Class(name="InterfaceProvidingRequiringEntity")
Repository = Class(name="Repository")
pcm_av_pc_repository_av_pc_ProvidedRole = Class(name="pcm::av::pc::repository::av::pc::ProvidedRole")
pcm_av_pc_repository_av_pc_Parameter = Class(name="pcm::av::pc::repository::av::pc::Parameter")
DataType = Class(name="DataType")
InfrastructureSignature = Class(name="InfrastructureSignature")
EventType = Class(name="EventType")
RequiredCharacterisation = Class(name="RequiredCharacterisation")
pcm_av_pc_repository_av_pc_InfrastructureRequiredRole = Class(name="pcm::av::pc::repository::av::pc::InfrastructureRequiredRole")
pcm_av_pc_repository_av_pc_Interface = Class(name="pcm::av::pc::repository::av::pc::Interface")
pcm_av_pc_repository_av_pc_RequiredRole = Class(name="pcm::av::pc::repository::av::pc::RequiredRole")
pcm_av_pc_repository_av_pc_RequiredCharacterisation = Class(name="pcm::av::pc::repository::av::pc::RequiredCharacterisation")
pcm_av_pc_repository_av_pc_OperationSignature = Class(name="pcm::av::pc::repository::av::pc::OperationSignature")
Parameter_ = Class(name="Parameter")
pcm_av_pc_repository_av_pc_EventGroup = Class(name="pcm::av::pc::repository::av::pc::EventGroup")
Protocol = Class(name="Protocol")
pcm_av_pc_repository_av_pc_EventType = Class(name="pcm::av::pc::repository::av::pc::EventType")
Signature = Class(name="Signature")
pcm_av_pc_repository_av_pc_Signature = Class(name="pcm::av::pc::repository::av::pc::Signature")
ExceptionType = Class(name="ExceptionType")
pcm_av_pc_repository_av_pc_ExceptionType = Class(name="pcm::av::pc::repository::av::pc::ExceptionType")
pcm_av_pc_repository_av_pc_InfrastructureSignature = Class(name="pcm::av::pc::repository::av::pc::InfrastructureSignature")
InfrastructureInterface = Class(name="InfrastructureInterface")
pcm_av_pc_repository_av_pc_InfrastructureInterface = Class(name="pcm::av::pc::repository::av::pc::InfrastructureInterface")
pcm_av_pc_repository_av_pc_OperationInterface = Class(name="pcm::av::pc::repository::av::pc::OperationInterface")
OperationInterface = Class(name="OperationInterface")
pcm_av_pc_repository_av_pc_InfrastructureProvidedRole = Class(name="pcm::av::pc::repository::av::pc::InfrastructureProvidedRole")
pcm_av_pc_repository_av_pc_CompleteComponentType = Class(name="pcm::av::pc::repository::av::pc::CompleteComponentType")
ProvidesComponentType = Class(name="ProvidesComponentType")
pcm_av_pc_repository_av_pc_OperationRequiredRole = Class(name="pcm::av::pc::repository::av::pc::OperationRequiredRole")
pcm_av_pc_repository_av_pc_SourceRole = Class(name="pcm::av::pc::repository::av::pc::SourceRole")
pcm_av_pc_repository_av_pc_SinkRole = Class(name="pcm::av::pc::repository::av::pc::SinkRole")
pcm_av_pc_repository_av_pc_OperationProvidedRole = Class(name="pcm::av::pc::repository::av::pc::OperationProvidedRole")
pcm_av_pc_repository_av_pc_CompositeComponent = Class(name="pcm::av::pc::repository::av::pc::CompositeComponent")
entity_av_pc_ComposedProvidingRequiringEntity = Class(name="entity::av::pc::ComposedProvidingRequiringEntity")
repository_av_pc_ImplementationComponentType = Class(name="repository::av::pc::ImplementationComponentType")
pcm_av_pc_repository_av_pc_PrimitiveDataType = Class(name="pcm::av::pc::repository::av::pc::PrimitiveDataType")
pcm_av_pc_repository_av_pc_CollectionDataType = Class(name="pcm::av::pc::repository::av::pc::CollectionDataType")
repository_av_pc_DataType = Class(name="repository::av::pc::DataType")
pcm_av_pc_repository_av_pc_ProvidesComponentType = Class(name="pcm::av::pc::repository::av::pc::ProvidesComponentType")
InnerDeclaration = Class(name="InnerDeclaration")
pcm_av_pc_repository_av_pc_InnerDeclaration = Class(name="pcm::av::pc::repository::av::pc::InnerDeclaration")
NamedElement = Class(name="NamedElement")
pcm_av_pc_repository_av_pc_Role = Class(name="pcm::av::pc::repository::av::pc::Role")
pcm_av_pc_resourcetype_av_pc_ResourceSignature = Class(name="pcm::av::pc::resourcetype::av::pc::ResourceSignature")
pcm_av_pc_resourcetype_av_pc_ProcessingResourceType = Class(name="pcm::av::pc::resourcetype::av::pc::ProcessingResourceType")
ResourceType = Class(name="ResourceType")
HardwareInducedFailureType = Class(name="HardwareInducedFailureType")
pcm_av_pc_resourcetype_av_pc_ResourceType = Class(name="pcm::av::pc::resourcetype::av::pc::ResourceType")
UnitCarryingElement = Class(name="UnitCarryingElement")
ResourceRepository = Class(name="ResourceRepository")
pcm_av_pc_resourcetype_av_pc_ResourceRepository = Class(name="pcm::av::pc::resourcetype::av::pc::ResourceRepository")
pcm_av_pc_repository_av_pc_CompositeDataType = Class(name="pcm::av::pc::repository::av::pc::CompositeDataType")
CompositeDataType = Class(name="CompositeDataType")
pcm_av_pc_resourcetype_av_pc_CommunicationLinkResourceType = Class(name="pcm::av::pc::resourcetype::av::pc::CommunicationLinkResourceType")
NetworkInducedFailureType = Class(name="NetworkInducedFailureType")
pcm_av_pc_resourcetype_av_pc_ResourceInterface = Class(name="pcm::av::pc::resourcetype::av::pc::ResourceInterface")
pcm_av_pc_protocol_av_pc_Protocol = Class(name="pcm::av::pc::protocol::av::pc::Protocol")
pcm_av_pc_parameter_av_pc_VariableUsage = Class(name="pcm::av::pc::parameter::av::pc::VariableUsage")
CallAction = Class(name="CallAction")
SynchronisationPoint = Class(name="SynchronisationPoint")
CallReturnAction = Class(name="CallReturnAction")
SetVariableAction = Class(name="SetVariableAction")
SpecifiedOutputParameterAbstraction = Class(name="SpecifiedOutputParameterAbstraction")
SchedulingPolicy = Class(name="SchedulingPolicy")
pcm_av_pc_resourcetype_av_pc_SchedulingPolicy = Class(name="pcm::av::pc::resourcetype::av::pc::SchedulingPolicy")
pcm_av_pc_parameter_av_pc_CharacterisedVariable = Class(name="pcm::av::pc::parameter::av::pc::CharacterisedVariable")
Variable = Class(name="Variable")
pcm_av_pc_reliability_av_pc_FailureOccurrenceDescription = Class(name="pcm::av::pc::reliability::av::pc::FailureOccurrenceDescription")
pcm_av_pc_reliability_av_pc_HardwareInducedFailureType = Class(name="pcm::av::pc::reliability::av::pc::HardwareInducedFailureType")
EntryLevelSystemCall = Class(name="EntryLevelSystemCall")
parameter_av_pc_pcm_av_pc_AbstractNamedReference = Class(name="parameter::av::pc::pcm::av::pc::AbstractNamedReference")
pcm_av_pc_parameter_av_pc_VariableCharacterisation = Class(name="pcm::av::pc::parameter::av::pc::VariableCharacterisation")
InternalAction = Class(name="InternalAction")
SoftwareInducedFailureType = Class(name="SoftwareInducedFailureType")
pcm_av_pc_reliability_av_pc_NetworkInducedFailureType = Class(name="pcm::av::pc::reliability::av::pc::NetworkInducedFailureType")
CommunicationLinkResourceType = Class(name="CommunicationLinkResourceType")
pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription = Class(name="pcm::av::pc::reliability::av::pc::ExternalFailureOccurrenceDescription")
qos_reliability_av_pc_SpecifiedReliabilityAnnotation = Class(name="qos::reliability::av::pc::SpecifiedReliabilityAnnotation")
ProcessingResourceType = Class(name="ProcessingResourceType")
pcm_av_pc_reliability_av_pc_SoftwareInducedFailureType = Class(name="pcm::av::pc::reliability::av::pc::SoftwareInducedFailureType")
InternalFailureOccurrenceDescription = Class(name="InternalFailureOccurrenceDescription")
pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription = Class(name="pcm::av::pc::reliability::av::pc::InternalFailureOccurrenceDescription")
FailureOccurrenceDescription = Class(name="FailureOccurrenceDescription")
pcm_av_pc_seff_av_pc_AbstractInternalControlFlowAction = Class(name="pcm::av::pc::seff::av::pc::AbstractInternalControlFlowAction")
AbstractAction = Class(name="AbstractAction")
pcm_av_pc_seff_av_pc_AbstractAction = Class(name="pcm::av::pc::seff::av::pc::AbstractAction")
ResourceDemandingBehaviour = Class(name="ResourceDemandingBehaviour")
pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour = Class(name="pcm::av::pc::seff::av::pc::ResourceDemandingBehaviour")
pcm_av_pc_reliability_av_pc_ResourceTimeoutFailureType = Class(name="pcm::av::pc::reliability::av::pc::ResourceTimeoutFailureType")
pcm_av_pc_reliability_av_pc_FailureType = Class(name="pcm::av::pc::reliability::av::pc::FailureType")
pcm_av_pc_seff_av_pc_StopAction = Class(name="pcm::av::pc::seff::av::pc::StopAction")
AbstractInternalControlFlowAction = Class(name="AbstractInternalControlFlowAction")
AbstractLoopAction = Class(name="AbstractLoopAction")
AbstractBranchTransition = Class(name="AbstractBranchTransition")
pcm_av_pc_seff_av_pc_AbstractLoopAction = Class(name="pcm::av::pc::seff::av::pc::AbstractLoopAction")
pcm_av_pc_seff_av_pc_AbstractBranchTransition = Class(name="pcm::av::pc::seff::av::pc::AbstractBranchTransition")
BranchAction = Class(name="BranchAction")
pcm_av_pc_seff_av_pc_BranchAction = Class(name="pcm::av::pc::seff::av::pc::BranchAction")
pcm_av_pc_seff_av_pc_ServiceEffectSpecification = Class(name="pcm::av::pc::seff::av::pc::ServiceEffectSpecification")
pcm_av_pc_seff_av_pc_ResourceDemandingSEFF = Class(name="pcm::av::pc::seff::av::pc::ResourceDemandingSEFF")
seff_av_pc_ServiceEffectSpecification = Class(name="seff::av::pc::ServiceEffectSpecification")
seff_av_pc_ResourceDemandingBehaviour = Class(name="seff::av::pc::ResourceDemandingBehaviour")
ResourceDemandingInternalBehaviour = Class(name="ResourceDemandingInternalBehaviour")
pcm_av_pc_seff_av_pc_ResourceDemandingInternalBehaviour = Class(name="pcm::av::pc::seff::av::pc::ResourceDemandingInternalBehaviour")
ResourceDemandingSEFF = Class(name="ResourceDemandingSEFF")
pcm_av_pc_seff_av_pc_ReleaseAction = Class(name="pcm::av::pc::seff::av::pc::ReleaseAction")
pcm_av_pc_seff_av_pc_CallAction = Class(name="pcm::av::pc::seff::av::pc::CallAction")
pcm_av_pc_seff_av_pc_StartAction = Class(name="pcm::av::pc::seff::av::pc::StartAction")
pcm_av_pc_seff_av_pc_LoopAction = Class(name="pcm::av::pc::seff::av::pc::LoopAction")
pcm_av_pc_seff_av_pc_ForkAction = Class(name="pcm::av::pc::seff::av::pc::ForkAction")
ForkedBehaviour = Class(name="ForkedBehaviour")
pcm_av_pc_seff_av_pc_ForkedBehaviour = Class(name="pcm::av::pc::seff::av::pc::ForkedBehaviour")
ForkAction = Class(name="ForkAction")
pcm_av_pc_seff_av_pc_SynchronisationPoint = Class(name="pcm::av::pc::seff::av::pc::SynchronisationPoint")
pcm_av_pc_seff_av_pc_CallReturnAction = Class(name="pcm::av::pc::seff::av::pc::CallReturnAction")
pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition = Class(name="pcm::av::pc::seff::av::pc::ProbabilisticBranchTransition")
pcm_av_pc_seff_av_pc_AcquireAction = Class(name="pcm::av::pc::seff::av::pc::AcquireAction")
pcm_av_pc_seff_av_pc_ExternalCallAction = Class(name="pcm::av::pc::seff::av::pc::ExternalCallAction")
seff_av_pc_AbstractAction = Class(name="seff::av::pc::AbstractAction")
seff_av_pc_CallReturnAction = Class(name="seff::av::pc::CallReturnAction")
seff_reliability_av_pc_FailureHandlingEntity = Class(name="seff::reliability::av::pc::FailureHandlingEntity")
pcm_av_pc_seff_av_pc_EmitEventAction = Class(name="pcm::av::pc::seff::av::pc::EmitEventAction")
pcm_av_pc_seff_av_pc_InternalAction = Class(name="pcm::av::pc::seff::av::pc::InternalAction")
pcm_av_pc_seff_performance_av_pc_InfrastructureCall = Class(name="pcm::av::pc::seff::performance::av::pc::InfrastructureCall")
pcm_av_pc_seff_av_pc_CollectionIteratorAction = Class(name="pcm::av::pc::seff::av::pc::CollectionIteratorAction")
pcm_av_pc_seff_av_pc_GuardedBranchTransition = Class(name="pcm::av::pc::seff::av::pc::GuardedBranchTransition")
pcm_av_pc_seff_av_pc_SetVariableAction = Class(name="pcm::av::pc::seff::av::pc::SetVariableAction")
pcm_av_pc_seff_av_pc_InternalCallAction = Class(name="pcm::av::pc::seff::av::pc::InternalCallAction")
seff_av_pc_CallAction = Class(name="seff::av::pc::CallAction")
seff_av_pc_AbstractInternalControlFlowAction = Class(name="seff::av::pc::AbstractInternalControlFlowAction")
pcm_av_pc_seff_performance_av_pc_ResourceCall = Class(name="pcm::av::pc::seff::performance::av::pc::ResourceCall")
pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour = Class(name="pcm::av::pc::seff::reliability::av::pc::RecoveryActionBehaviour")
pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand = Class(name="pcm::av::pc::seff::performance::av::pc::ParametricResourceDemand")
pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity = Class(name="pcm::av::pc::seff::reliability::av::pc::FailureHandlingEntity")
pcm_av_pc_qosannotations_av_pc_SpecifiedQoSAnnotation = Class(name="pcm::av::pc::qosannotations::av::pc::SpecifiedQoSAnnotation")
QoSAnnotations = Class(name="QoSAnnotations")
pcm_av_pc_qosannotations_av_pc_QoSAnnotations = Class(name="pcm::av::pc::qosannotations::av::pc::QoSAnnotations")
System = Class(name="System")
SpecifiedQoSAnnotation = Class(name="SpecifiedQoSAnnotation")
seff_reliability_av_pc_RecoveryActionBehaviour = Class(name="seff::reliability::av::pc::RecoveryActionBehaviour")
seff_reliability_av_pc_RecoveryAction = Class(name="seff::reliability::av::pc::RecoveryAction")
pcm_av_pc_seff_reliability_av_pc_RecoveryAction = Class(name="pcm::av::pc::seff::reliability::av::pc::RecoveryAction")
pcm_av_pc_qos_performance_av_pc_SystemSpecifiedExecutionTime = Class(name="pcm::av::pc::qos::performance::av::pc::SystemSpecifiedExecutionTime")
SpecifiedExecutionTime = Class(name="SpecifiedExecutionTime")
pcm_av_pc_qos_performance_av_pc_SpecifiedExecutionTime = Class(name="pcm::av::pc::qos::performance::av::pc::SpecifiedExecutionTime")
pcm_av_pc_qos_performance_av_pc_ComponentSpecifiedExecutionTime = Class(name="pcm::av::pc::qos::performance::av::pc::ComponentSpecifiedExecutionTime")
pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation = Class(name="pcm::av::pc::qos::reliability::av::pc::SpecifiedReliabilityAnnotation")
pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction = Class(name="pcm::av::pc::qosannotations::av::pc::SpecifiedOutputParameterAbstraction")
ExternalFailureOccurrenceDescription = Class(name="ExternalFailureOccurrenceDescription")
pcm_av_pc_system_av_pc_System = Class(name="pcm::av::pc::system::av::pc::System")
pcm_av_pc_resourceenvironment_av_pc_ResourceEnvironment = Class(name="pcm::av::pc::resourceenvironment::av::pc::ResourceEnvironment")
LinkingResource = Class(name="LinkingResource")
ResourceContainer = Class(name="ResourceContainer")
pcm_av_pc_resourceenvironment_av_pc_LinkingResource = Class(name="pcm::av::pc::resourceenvironment::av::pc::LinkingResource")
pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification = Class(name="pcm::av::pc::resourceenvironment::av::pc::ProcessingResourceSpecification")
pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification = Class(name="pcm::av::pc::resourceenvironment::av::pc::CommunicationLinkResourceSpecification")
ResourceEnvironment = Class(name="ResourceEnvironment")
pcm_av_pc_resourceenvironment_av_pc_ResourceContainer = Class(name="pcm::av::pc::resourceenvironment::av::pc::ResourceContainer")
pcm_av_pc_allocation_av_pc_AllocationContext = Class(name="pcm::av::pc::allocation::av::pc::AllocationContext")
Allocation = Class(name="Allocation")
pcm_av_pc_allocation_av_pc_Allocation = Class(name="pcm::av::pc::allocation::av::pc::Allocation")
pcm_av_pc_completions_av_pc_Completion = Class(name="pcm::av::pc::completions::av::pc::Completion")
pcm_av_pc_completions_av_pc_CompletionRepository = Class(name="pcm::av::pc::completions::av::pc::CompletionRepository")
Completion = Class(name="Completion")
pcm_av_pc_completions_av_pc_DelegatingExternalCallAction = Class(name="pcm::av::pc::completions::av::pc::DelegatingExternalCallAction")
ExternalCallAction = Class(name="ExternalCallAction")
pcm_av_pc_completions_av_pc_NetworkDemandParametricResourceDemand = Class(name="pcm::av::pc::completions::av::pc::NetworkDemandParametricResourceDemand")
ParametricResourceDemand = Class(name="ParametricResourceDemand")
AllocationContext = Class(name="AllocationContext")
pcm_av_pc_subsystem_av_pc_SubSystem = Class(name="pcm::av::pc::subsystem::av::pc::SubSystem")
repository_av_pc_RepositoryComponent = Class(name="repository::av::pc::RepositoryComponent")

# pcm_av_pc_DummyClass class attributes and methods

# pcm_av_pc_Advice class attributes and methods

# pcm_av_pc_EObject class attributes and methods

# pcm_av_pc_GlobalScope class attributes and methods

# pcm_av_pc_PerJoinPointScope class attributes and methods

# pcm_av_pc_Pointcut class attributes and methods

# pcm_av_pc_core_av_pc_PCMRandomVariable class attributes and methods
pcm_av_pc_core_av_pc_PCMRandomVariable_m_SpecificationMustNotBeNULL: Method = Method(name="SpecificationMustNotBeNULL", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_core_av_pc_PCMRandomVariable.methods={pcm_av_pc_core_av_pc_PCMRandomVariable_m_SpecificationMustNotBeNULL}

# RandomVariable class attributes and methods

# pcm_av_pc_entity_av_pc_ResourceInterfaceRequiringEntity class attributes and methods

# seff_performance_av_pc_ResourceCall class attributes and methods

# entity_av_pc_ResourceRequiredRole class attributes and methods

# pcm_av_pc_entity_av_pc_ResourceRequiredRole class attributes and methods

# seff_performance_av_pc_ParametricResourceDemand class attributes and methods

# LoopAction class attributes and methods

# GuardedBranchTransition class attributes and methods

# pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingEntity class attributes and methods

# qos_performance_av_pc_SpecifiedExecutionTime class attributes and methods

# entity_av_pc_ResourceProvidedRole class attributes and methods

# composition_av_pc_EventChannelSinkConnector class attributes and methods

# composition_av_pc_AssemblyEventConnector class attributes and methods

# Loop class attributes and methods

# OpenWorkload class attributes and methods

# Delay class attributes and methods

# CommunicationLinkResourceSpecification class attributes and methods

# ProcessingResourceSpecification class attributes and methods

# pcm_av_pc_entity_av_pc_ResourceProvidedRole class attributes and methods

# Role class attributes and methods

# entity_av_pc_ResourceInterfaceProvidingEntity class attributes and methods

# ResourceInterface class attributes and methods

# pcm_av_pc_entity_av_pc_InterfaceProvidingRequiringEntity class attributes and methods

# entity_av_pc_InterfaceProvidingEntity class attributes and methods

# entity_av_pc_InterfaceRequiringEntity class attributes and methods

# ClosedWorkload class attributes and methods

# pcm_av_pc_entity_av_pc_InterfaceProvidingEntity class attributes and methods

# Entity class attributes and methods

# PassiveResource class attributes and methods

# ProvidedRole class attributes and methods

# VariableCharacterisation class attributes and methods

# pcm_av_pc_entity_av_pc_InterfaceRequiringEntity class attributes and methods

# entity_av_pc_Entity class attributes and methods

# entity_av_pc_ResourceInterfaceRequiringEntity class attributes and methods

# seff_performance_av_pc_InfrastructureCall class attributes and methods

# RequiredRole class attributes and methods

# composition_av_pc_AssemblyContext class attributes and methods

# composition_av_pc_ResourceRequiredDelegationConnector class attributes and methods

# pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity class attributes and methods
pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound: Method = Method(name="ProvidedRolesMustBeBound", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity.methods={pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound}

# composition_av_pc_ComposedStructure class attributes and methods

# entity_av_pc_InterfaceProvidingRequiringEntity class attributes and methods

# composition_av_pc_EventChannel class attributes and methods

# composition_av_pc_Connector class attributes and methods

# pcm_av_pc_entity_av_pc_NamedElement class attributes and methods
pcm_av_pc_entity_av_pc_NamedElement_entityName: Property = Property(name="entityName", type=StringType)
pcm_av_pc_entity_av_pc_NamedElement.attributes={pcm_av_pc_entity_av_pc_NamedElement_entityName}

# pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingRequiringEntity class attributes and methods

# pcm_av_pc_entity_av_pc_Entity class attributes and methods

# Identifier class attributes and methods

# entity_av_pc_NamedElement class attributes and methods

# pcm_av_pc_composition_av_pc_DelegationConnector class attributes and methods

# Connector class attributes and methods

# pcm_av_pc_composition_av_pc_Connector class attributes and methods

# pcm_av_pc_composition_av_pc_ComposedStructure class attributes and methods
pcm_av_pc_composition_av_pc_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors: Method = Method(name="MultipleConnectorsConstraintForAssemblyConnectors", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_composition_av_pc_ComposedStructure_m_MultipleConnectorsConstraint: Method = Method(name="MultipleConnectorsConstraint", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_composition_av_pc_ComposedStructure.methods={pcm_av_pc_composition_av_pc_ComposedStructure_m_MultipleConnectorsConstraint, pcm_av_pc_composition_av_pc_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors}

# pcm_av_pc_composition_av_pc_EventChannelSourceConnector class attributes and methods

# SourceRole class attributes and methods

# pcm_av_pc_composition_av_pc_EventChannelSinkConnector class attributes and methods

# SinkRole class attributes and methods

# PCMRandomVariable class attributes and methods

# pcm_av_pc_composition_av_pc_ProvidedDelegationConnector class attributes and methods
pcm_av_pc_composition_av_pc_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_composition_av_pc_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_composition_av_pc_ProvidedDelegationConnector.methods={pcm_av_pc_composition_av_pc_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame, pcm_av_pc_composition_av_pc_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure}

# DelegationConnector class attributes and methods

# pcm_av_pc_composition_av_pc_ResourceRequiredDelegationConnector class attributes and methods

# pcm_av_pc_composition_av_pc_EventChannel class attributes and methods

# EventGroup class attributes and methods

# composition_av_pc_EventChannelSourceConnector class attributes and methods

# OperationRequiredRole class attributes and methods

# OperationProvidedRole class attributes and methods

# pcm_av_pc_composition_av_pc_RequiredDelegationConnector class attributes and methods
pcm_av_pc_composition_av_pc_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_composition_av_pc_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector: Method = Method(name="RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_composition_av_pc_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_composition_av_pc_RequiredDelegationConnector.methods={pcm_av_pc_composition_av_pc_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector, pcm_av_pc_composition_av_pc_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure, pcm_av_pc_composition_av_pc_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame}

# pcm_av_pc_composition_av_pc_AssemblyEventConnector class attributes and methods

# pcm_av_pc_composition_av_pc_SourceDelegationConnector class attributes and methods

# pcm_av_pc_composition_av_pc_AssemblyConnector class attributes and methods
pcm_av_pc_composition_av_pc_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_composition_av_pc_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_composition_av_pc_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch: Method = Method(name="AssemblyConnectorsReferencedInterfacesMustMatch", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_composition_av_pc_AssemblyConnector.methods={pcm_av_pc_composition_av_pc_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch, pcm_av_pc_composition_av_pc_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch, pcm_av_pc_composition_av_pc_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch}

# pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector class attributes and methods

# pcm_av_pc_composition_av_pc_AssemblyContext class attributes and methods

# RepositoryComponent class attributes and methods

# VariableUsage class attributes and methods

# pcm_av_pc_composition_av_pc_SinkDelegationConnector class attributes and methods

# pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector class attributes and methods

# InfrastructureProvidedRole class attributes and methods

# InfrastructureRequiredRole class attributes and methods

# pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector class attributes and methods

# pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector class attributes and methods

# OperationSignature class attributes and methods

# pcm_av_pc_usagemodel_av_pc_Workload class attributes and methods

# UsageScenario class attributes and methods

# pcm_av_pc_usagemodel_av_pc_UsageScenario class attributes and methods

# UsageModel class attributes and methods

# ScenarioBehaviour class attributes and methods

# Workload class attributes and methods

# pcm_av_pc_usagemodel_av_pc_UserData class attributes and methods

# pcm_av_pc_usagemodel_av_pc_UsageModel class attributes and methods

# UserData class attributes and methods

# pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall class attributes and methods
pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall_priority: Property = Property(name="priority", type=IntegerType)
pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem: Method = Method(name="EntryLevelSystemCallMustReferenceProvidedRoleOfASystem", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole: Method = Method(name="EntryLevelSystemCallSignatureMustMatchItsProvidedRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall.attributes={pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall_priority}
pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall.methods={pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem, pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole}

# AbstractUserAction class attributes and methods

# BranchTransition class attributes and methods

# pcm_av_pc_usagemodel_av_pc_AbstractUserAction class attributes and methods

# pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour class attributes and methods
pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour_m_Exactlyonestop: Method = Method(name="Exactlyonestop", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor: Method = Method(name="EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour_m_Exactlyonestart: Method = Method(name="Exactlyonestart", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour.methods={pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour_m_Exactlyonestop, pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour_m_Exactlyonestart, pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor}

# pcm_av_pc_usagemodel_av_pc_Start class attributes and methods
pcm_av_pc_usagemodel_av_pc_Start_m_StartHasNoPredecessor: Method = Method(name="StartHasNoPredecessor", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_Start.methods={pcm_av_pc_usagemodel_av_pc_Start_m_StartHasNoPredecessor}

# pcm_av_pc_usagemodel_av_pc_OpenWorkload class attributes and methods
pcm_av_pc_usagemodel_av_pc_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified: Method = Method(name="InterArrivalTimeInOpenWorkloadNeedsToBeSpecified", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_OpenWorkload.methods={pcm_av_pc_usagemodel_av_pc_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified}

# pcm_av_pc_usagemodel_av_pc_BranchTransition class attributes and methods
pcm_av_pc_usagemodel_av_pc_BranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_av_pc_usagemodel_av_pc_BranchTransition.attributes={pcm_av_pc_usagemodel_av_pc_BranchTransition_branchProbability}

# Branch class attributes and methods

# pcm_av_pc_usagemodel_av_pc_Branch class attributes and methods
pcm_av_pc_usagemodel_av_pc_Branch_m_AllBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_Branch.methods={pcm_av_pc_usagemodel_av_pc_Branch_m_AllBranchProbabilitiesMustSumUpTo1}

# pcm_av_pc_usagemodel_av_pc_Loop class attributes and methods

# pcm_av_pc_usagemodel_av_pc_Stop class attributes and methods
pcm_av_pc_usagemodel_av_pc_Stop_m_StopHasNoSuccessor: Method = Method(name="StopHasNoSuccessor", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_Stop.methods={pcm_av_pc_usagemodel_av_pc_Stop_m_StopHasNoSuccessor}

# pcm_av_pc_repository_av_pc_PassiveResource class attributes and methods

# BasicComponent class attributes and methods

# ResourceTimeoutFailureType class attributes and methods

# pcm_av_pc_repository_av_pc_BasicComponent class attributes and methods
pcm_av_pc_repository_av_pc_BasicComponent_m_NoSeffTypeUsedTwice: Method = Method(name="NoSeffTypeUsedTwice", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_repository_av_pc_BasicComponent_m_ProvideSameInterfacesAsImplementationType: Method = Method(name="ProvideSameInterfacesAsImplementationType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_repository_av_pc_BasicComponent_m_RequireSameInterfacesAsImplementationType: Method = Method(name="RequireSameInterfacesAsImplementationType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_repository_av_pc_BasicComponent.methods={pcm_av_pc_repository_av_pc_BasicComponent_m_RequireSameInterfacesAsImplementationType, pcm_av_pc_repository_av_pc_BasicComponent_m_NoSeffTypeUsedTwice, pcm_av_pc_repository_av_pc_BasicComponent_m_ProvideSameInterfacesAsImplementationType}

# ImplementationComponentType class attributes and methods

# pcm_av_pc_usagemodel_av_pc_Delay class attributes and methods

# pcm_av_pc_usagemodel_av_pc_ClosedWorkload class attributes and methods
pcm_av_pc_usagemodel_av_pc_ClosedWorkload_population: Property = Property(name="population", type=IntegerType)
pcm_av_pc_usagemodel_av_pc_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified: Method = Method(name="PopulationInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified: Method = Method(name="ThinkTimeInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_ClosedWorkload.attributes={pcm_av_pc_usagemodel_av_pc_ClosedWorkload_population}
pcm_av_pc_usagemodel_av_pc_ClosedWorkload.methods={pcm_av_pc_usagemodel_av_pc_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified, pcm_av_pc_usagemodel_av_pc_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified}

# CompleteComponentType class attributes and methods

# ServiceEffectSpecification class attributes and methods

# pcm_av_pc_repository_av_pc_ImplementationComponentType class attributes and methods
pcm_av_pc_repository_av_pc_ImplementationComponentType_componentType: Property = Property(name="componentType", type=StringType)
pcm_av_pc_repository_av_pc_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType: Method = Method(name="providedInterfacesHaveToConformToCompleteType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_repository_av_pc_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType: Method = Method(name="ProvidedInterfaceHaveToConformToComponentType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_repository_av_pc_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType: Method = Method(name="RequiredInterfacesHaveToConformToCompleteType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_repository_av_pc_ImplementationComponentType.attributes={pcm_av_pc_repository_av_pc_ImplementationComponentType_componentType}
pcm_av_pc_repository_av_pc_ImplementationComponentType.methods={pcm_av_pc_repository_av_pc_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType, pcm_av_pc_repository_av_pc_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType, pcm_av_pc_repository_av_pc_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType}

# ResourceSignature class attributes and methods

# pcm_av_pc_repository_av_pc_DataType class attributes and methods

# pcm_av_pc_repository_av_pc_Repository class attributes and methods
pcm_av_pc_repository_av_pc_Repository_repositoryDescription: Property = Property(name="repositoryDescription", type=StringType)
pcm_av_pc_repository_av_pc_Repository.attributes={pcm_av_pc_repository_av_pc_Repository_repositoryDescription}

# Interface class attributes and methods

# FailureType class attributes and methods

# pcm_av_pc_repository_av_pc_RepositoryComponent class attributes and methods

# InterfaceProvidingRequiringEntity class attributes and methods

# Repository class attributes and methods

# pcm_av_pc_repository_av_pc_ProvidedRole class attributes and methods

# pcm_av_pc_repository_av_pc_Parameter class attributes and methods
pcm_av_pc_repository_av_pc_Parameter_parameterName: Property = Property(name="parameterName", type=StringType)
pcm_av_pc_repository_av_pc_Parameter_modifier__Parameter: Property = Property(name="modifier__Parameter", type=StringType)
pcm_av_pc_repository_av_pc_Parameter.attributes={pcm_av_pc_repository_av_pc_Parameter_parameterName, pcm_av_pc_repository_av_pc_Parameter_modifier__Parameter}

# DataType class attributes and methods

# InfrastructureSignature class attributes and methods

# EventType class attributes and methods

# RequiredCharacterisation class attributes and methods

# pcm_av_pc_repository_av_pc_InfrastructureRequiredRole class attributes and methods

# pcm_av_pc_repository_av_pc_Interface class attributes and methods
pcm_av_pc_repository_av_pc_Interface_m_NoProtocolTypeIDUsedTwice: Method = Method(name="NoProtocolTypeIDUsedTwice", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_repository_av_pc_Interface.methods={pcm_av_pc_repository_av_pc_Interface_m_NoProtocolTypeIDUsedTwice}

# pcm_av_pc_repository_av_pc_RequiredRole class attributes and methods

# pcm_av_pc_repository_av_pc_RequiredCharacterisation class attributes and methods
pcm_av_pc_repository_av_pc_RequiredCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_av_pc_repository_av_pc_RequiredCharacterisation.attributes={pcm_av_pc_repository_av_pc_RequiredCharacterisation_type}

# pcm_av_pc_repository_av_pc_OperationSignature class attributes and methods
pcm_av_pc_repository_av_pc_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature: Method = Method(name="ParameterNamesHaveToBeUniqueForASignature", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_repository_av_pc_OperationSignature.methods={pcm_av_pc_repository_av_pc_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature}

# Parameter class attributes and methods

# pcm_av_pc_repository_av_pc_EventGroup class attributes and methods

# Protocol class attributes and methods

# pcm_av_pc_repository_av_pc_EventType class attributes and methods

# Signature class attributes and methods

# pcm_av_pc_repository_av_pc_Signature class attributes and methods

# ExceptionType class attributes and methods

# pcm_av_pc_repository_av_pc_ExceptionType class attributes and methods
pcm_av_pc_repository_av_pc_ExceptionType_exceptionName: Property = Property(name="exceptionName", type=StringType)
pcm_av_pc_repository_av_pc_ExceptionType_exceptionMessage: Property = Property(name="exceptionMessage", type=StringType)
pcm_av_pc_repository_av_pc_ExceptionType.attributes={pcm_av_pc_repository_av_pc_ExceptionType_exceptionMessage, pcm_av_pc_repository_av_pc_ExceptionType_exceptionName}

# pcm_av_pc_repository_av_pc_InfrastructureSignature class attributes and methods

# InfrastructureInterface class attributes and methods

# pcm_av_pc_repository_av_pc_InfrastructureInterface class attributes and methods

# pcm_av_pc_repository_av_pc_OperationInterface class attributes and methods
pcm_av_pc_repository_av_pc_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface: Method = Method(name="SignaturesHaveToBeUniqueForAnInterface", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_repository_av_pc_OperationInterface.methods={pcm_av_pc_repository_av_pc_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface}

# OperationInterface class attributes and methods

# pcm_av_pc_repository_av_pc_InfrastructureProvidedRole class attributes and methods

# pcm_av_pc_repository_av_pc_CompleteComponentType class attributes and methods
pcm_av_pc_repository_av_pc_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_repository_av_pc_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2: Method = Method(name="providedInterfacesHaveToConformToProvidedType2", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_repository_av_pc_CompleteComponentType.methods={pcm_av_pc_repository_av_pc_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2, pcm_av_pc_repository_av_pc_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType}

# ProvidesComponentType class attributes and methods

# pcm_av_pc_repository_av_pc_OperationRequiredRole class attributes and methods

# pcm_av_pc_repository_av_pc_SourceRole class attributes and methods

# pcm_av_pc_repository_av_pc_SinkRole class attributes and methods

# pcm_av_pc_repository_av_pc_OperationProvidedRole class attributes and methods

# pcm_av_pc_repository_av_pc_CompositeComponent class attributes and methods
pcm_av_pc_repository_av_pc_CompositeComponent_m_ProvideSameInterfaces: Method = Method(name="ProvideSameInterfaces", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_repository_av_pc_CompositeComponent_m_RequireSameInterfaces: Method = Method(name="RequireSameInterfaces", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_repository_av_pc_CompositeComponent.methods={pcm_av_pc_repository_av_pc_CompositeComponent_m_RequireSameInterfaces, pcm_av_pc_repository_av_pc_CompositeComponent_m_ProvideSameInterfaces}

# entity_av_pc_ComposedProvidingRequiringEntity class attributes and methods

# repository_av_pc_ImplementationComponentType class attributes and methods

# pcm_av_pc_repository_av_pc_PrimitiveDataType class attributes and methods
pcm_av_pc_repository_av_pc_PrimitiveDataType_type: Property = Property(name="type", type=StringType)
pcm_av_pc_repository_av_pc_PrimitiveDataType.attributes={pcm_av_pc_repository_av_pc_PrimitiveDataType_type}

# pcm_av_pc_repository_av_pc_CollectionDataType class attributes and methods

# repository_av_pc_DataType class attributes and methods

# pcm_av_pc_repository_av_pc_ProvidesComponentType class attributes and methods
pcm_av_pc_repository_av_pc_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_repository_av_pc_ProvidesComponentType.methods={pcm_av_pc_repository_av_pc_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType}

# InnerDeclaration class attributes and methods

# pcm_av_pc_repository_av_pc_InnerDeclaration class attributes and methods

# NamedElement class attributes and methods

# pcm_av_pc_repository_av_pc_Role class attributes and methods

# pcm_av_pc_resourcetype_av_pc_ResourceSignature class attributes and methods
pcm_av_pc_resourcetype_av_pc_ResourceSignature_resourceServiceId: Property = Property(name="resourceServiceId", type=IntegerType)
pcm_av_pc_resourcetype_av_pc_ResourceSignature.attributes={pcm_av_pc_resourcetype_av_pc_ResourceSignature_resourceServiceId}

# pcm_av_pc_resourcetype_av_pc_ProcessingResourceType class attributes and methods

# ResourceType class attributes and methods

# HardwareInducedFailureType class attributes and methods

# pcm_av_pc_resourcetype_av_pc_ResourceType class attributes and methods

# UnitCarryingElement class attributes and methods

# ResourceRepository class attributes and methods

# pcm_av_pc_resourcetype_av_pc_ResourceRepository class attributes and methods

# pcm_av_pc_repository_av_pc_CompositeDataType class attributes and methods

# CompositeDataType class attributes and methods

# pcm_av_pc_resourcetype_av_pc_CommunicationLinkResourceType class attributes and methods

# NetworkInducedFailureType class attributes and methods

# pcm_av_pc_resourcetype_av_pc_ResourceInterface class attributes and methods

# pcm_av_pc_protocol_av_pc_Protocol class attributes and methods
pcm_av_pc_protocol_av_pc_Protocol_protocolTypeID: Property = Property(name="protocolTypeID", type=StringType)
pcm_av_pc_protocol_av_pc_Protocol.attributes={pcm_av_pc_protocol_av_pc_Protocol_protocolTypeID}

# pcm_av_pc_parameter_av_pc_VariableUsage class attributes and methods

# CallAction class attributes and methods

# SynchronisationPoint class attributes and methods

# CallReturnAction class attributes and methods

# SetVariableAction class attributes and methods

# SpecifiedOutputParameterAbstraction class attributes and methods

# SchedulingPolicy class attributes and methods

# pcm_av_pc_resourcetype_av_pc_SchedulingPolicy class attributes and methods

# pcm_av_pc_parameter_av_pc_CharacterisedVariable class attributes and methods
pcm_av_pc_parameter_av_pc_CharacterisedVariable_characterisationType: Property = Property(name="characterisationType", type=StringType)
pcm_av_pc_parameter_av_pc_CharacterisedVariable.attributes={pcm_av_pc_parameter_av_pc_CharacterisedVariable_characterisationType}

# Variable class attributes and methods

# pcm_av_pc_reliability_av_pc_FailureOccurrenceDescription class attributes and methods
pcm_av_pc_reliability_av_pc_FailureOccurrenceDescription_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_av_pc_reliability_av_pc_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange: Method = Method(name="EnsureValidFailureProbabilityRange", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_reliability_av_pc_FailureOccurrenceDescription.attributes={pcm_av_pc_reliability_av_pc_FailureOccurrenceDescription_failureProbability}
pcm_av_pc_reliability_av_pc_FailureOccurrenceDescription.methods={pcm_av_pc_reliability_av_pc_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange}

# pcm_av_pc_reliability_av_pc_HardwareInducedFailureType class attributes and methods
pcm_av_pc_reliability_av_pc_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType: Method = Method(name="HardwareInducedFailureTypeHasProcessingResourceType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_reliability_av_pc_HardwareInducedFailureType.methods={pcm_av_pc_reliability_av_pc_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType}

# EntryLevelSystemCall class attributes and methods

# parameter_av_pc_pcm_av_pc_AbstractNamedReference class attributes and methods

# pcm_av_pc_parameter_av_pc_VariableCharacterisation class attributes and methods
pcm_av_pc_parameter_av_pc_VariableCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_av_pc_parameter_av_pc_VariableCharacterisation.attributes={pcm_av_pc_parameter_av_pc_VariableCharacterisation_type}

# InternalAction class attributes and methods

# SoftwareInducedFailureType class attributes and methods

# pcm_av_pc_reliability_av_pc_NetworkInducedFailureType class attributes and methods
pcm_av_pc_reliability_av_pc_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType: Method = Method(name="NetworkInducedFailureTypeHasCommunicationLinkResourceType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_reliability_av_pc_NetworkInducedFailureType.methods={pcm_av_pc_reliability_av_pc_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType}

# CommunicationLinkResourceType class attributes and methods

# pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription class attributes and methods
pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription.methods={pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription}

# qos_reliability_av_pc_SpecifiedReliabilityAnnotation class attributes and methods

# ProcessingResourceType class attributes and methods

# pcm_av_pc_reliability_av_pc_SoftwareInducedFailureType class attributes and methods

# InternalFailureOccurrenceDescription class attributes and methods

# pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription class attributes and methods
pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription.methods={pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription}

# FailureOccurrenceDescription class attributes and methods

# pcm_av_pc_seff_av_pc_AbstractInternalControlFlowAction class attributes and methods

# AbstractAction class attributes and methods

# pcm_av_pc_seff_av_pc_AbstractAction class attributes and methods

# ResourceDemandingBehaviour class attributes and methods

# pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour class attributes and methods
pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour_m_ExactlyOneStopAction: Method = Method(name="ExactlyOneStopAction", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour_m_ExactlyOneStartAction: Method = Method(name="ExactlyOneStartAction", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor: Method = Method(name="EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour.methods={pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor, pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour_m_ExactlyOneStopAction, pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour_m_ExactlyOneStartAction}

# pcm_av_pc_reliability_av_pc_ResourceTimeoutFailureType class attributes and methods

# pcm_av_pc_reliability_av_pc_FailureType class attributes and methods

# pcm_av_pc_seff_av_pc_StopAction class attributes and methods
pcm_av_pc_seff_av_pc_StopAction_m_StopActionSuccessorMustNotBeDefined: Method = Method(name="StopActionSuccessorMustNotBeDefined", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_seff_av_pc_StopAction.methods={pcm_av_pc_seff_av_pc_StopAction_m_StopActionSuccessorMustNotBeDefined}

# AbstractInternalControlFlowAction class attributes and methods

# AbstractLoopAction class attributes and methods

# AbstractBranchTransition class attributes and methods

# pcm_av_pc_seff_av_pc_AbstractLoopAction class attributes and methods

# pcm_av_pc_seff_av_pc_AbstractBranchTransition class attributes and methods

# BranchAction class attributes and methods

# pcm_av_pc_seff_av_pc_BranchAction class attributes and methods
pcm_av_pc_seff_av_pc_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions: Method = Method(name="EitherGuardedBranchesOrProbabilisiticBranchTransitions", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_seff_av_pc_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllProbabilisticBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_seff_av_pc_BranchAction.methods={pcm_av_pc_seff_av_pc_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1, pcm_av_pc_seff_av_pc_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions}

# pcm_av_pc_seff_av_pc_ServiceEffectSpecification class attributes and methods
pcm_av_pc_seff_av_pc_ServiceEffectSpecification_seffTypeID: Property = Property(name="seffTypeID", type=StringType)
pcm_av_pc_seff_av_pc_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole: Method = Method(name="ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_seff_av_pc_ServiceEffectSpecification.attributes={pcm_av_pc_seff_av_pc_ServiceEffectSpecification_seffTypeID}
pcm_av_pc_seff_av_pc_ServiceEffectSpecification.methods={pcm_av_pc_seff_av_pc_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole}

# pcm_av_pc_seff_av_pc_ResourceDemandingSEFF class attributes and methods

# seff_av_pc_ServiceEffectSpecification class attributes and methods

# seff_av_pc_ResourceDemandingBehaviour class attributes and methods

# ResourceDemandingInternalBehaviour class attributes and methods

# pcm_av_pc_seff_av_pc_ResourceDemandingInternalBehaviour class attributes and methods

# ResourceDemandingSEFF class attributes and methods

# pcm_av_pc_seff_av_pc_ReleaseAction class attributes and methods

# pcm_av_pc_seff_av_pc_CallAction class attributes and methods

# pcm_av_pc_seff_av_pc_StartAction class attributes and methods
pcm_av_pc_seff_av_pc_StartAction_m_StartActionPredecessorMustNotBeDefined: Method = Method(name="StartActionPredecessorMustNotBeDefined", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_seff_av_pc_StartAction.methods={pcm_av_pc_seff_av_pc_StartAction_m_StartActionPredecessorMustNotBeDefined}

# pcm_av_pc_seff_av_pc_LoopAction class attributes and methods

# pcm_av_pc_seff_av_pc_ForkAction class attributes and methods

# ForkedBehaviour class attributes and methods

# pcm_av_pc_seff_av_pc_ForkedBehaviour class attributes and methods

# ForkAction class attributes and methods

# pcm_av_pc_seff_av_pc_SynchronisationPoint class attributes and methods

# pcm_av_pc_seff_av_pc_CallReturnAction class attributes and methods

# pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition class attributes and methods
pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition.attributes={pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition_branchProbability}

# pcm_av_pc_seff_av_pc_AcquireAction class attributes and methods
pcm_av_pc_seff_av_pc_AcquireAction_timeout: Property = Property(name="timeout", type=BooleanType)
pcm_av_pc_seff_av_pc_AcquireAction_timeoutValue: Property = Property(name="timeoutValue", type=FloatType)
pcm_av_pc_seff_av_pc_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative: Method = Method(name="TimeoutValueOfAcquireActionMustNotBeNegative", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_seff_av_pc_AcquireAction.attributes={pcm_av_pc_seff_av_pc_AcquireAction_timeoutValue, pcm_av_pc_seff_av_pc_AcquireAction_timeout}
pcm_av_pc_seff_av_pc_AcquireAction.methods={pcm_av_pc_seff_av_pc_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative}

# pcm_av_pc_seff_av_pc_ExternalCallAction class attributes and methods
pcm_av_pc_seff_av_pc_ExternalCallAction_retryCount: Property = Property(name="retryCount", type=IntegerType)
pcm_av_pc_seff_av_pc_ExternalCallAction_m_SignatureBelongsToRole: Method = Method(name="SignatureBelongsToRole", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_seff_av_pc_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer: Method = Method(name="OperationRequiredRoleMustBeReferencedByContainer", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_seff_av_pc_ExternalCallAction.attributes={pcm_av_pc_seff_av_pc_ExternalCallAction_retryCount}
pcm_av_pc_seff_av_pc_ExternalCallAction.methods={pcm_av_pc_seff_av_pc_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer, pcm_av_pc_seff_av_pc_ExternalCallAction_m_SignatureBelongsToRole}

# seff_av_pc_AbstractAction class attributes and methods

# seff_av_pc_CallReturnAction class attributes and methods

# seff_reliability_av_pc_FailureHandlingEntity class attributes and methods

# pcm_av_pc_seff_av_pc_EmitEventAction class attributes and methods

# pcm_av_pc_seff_av_pc_InternalAction class attributes and methods
pcm_av_pc_seff_av_pc_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_seff_av_pc_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfInternalActionFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_seff_av_pc_InternalAction.methods={pcm_av_pc_seff_av_pc_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed, pcm_av_pc_seff_av_pc_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1}

# pcm_av_pc_seff_performance_av_pc_InfrastructureCall class attributes and methods
pcm_av_pc_seff_performance_av_pc_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole: Method = Method(name="SignatureMustBelongToUsedRequiredRole", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_seff_performance_av_pc_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent: Method = Method(name="ReferencedRequiredRoleMustBeRequiredByComponent", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_seff_performance_av_pc_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_seff_performance_av_pc_InfrastructureCall.methods={pcm_av_pc_seff_performance_av_pc_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole, pcm_av_pc_seff_performance_av_pc_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction, pcm_av_pc_seff_performance_av_pc_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent}

# pcm_av_pc_seff_av_pc_CollectionIteratorAction class attributes and methods

# pcm_av_pc_seff_av_pc_GuardedBranchTransition class attributes and methods

# pcm_av_pc_seff_av_pc_SetVariableAction class attributes and methods

# pcm_av_pc_seff_av_pc_InternalCallAction class attributes and methods

# seff_av_pc_CallAction class attributes and methods

# seff_av_pc_AbstractInternalControlFlowAction class attributes and methods

# pcm_av_pc_seff_performance_av_pc_ResourceCall class attributes and methods
pcm_av_pc_seff_performance_av_pc_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole: Method = Method(name="ResourceSignatureBelongsToResourceRequiredRole", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_seff_performance_av_pc_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent: Method = Method(name="ResourceRequiredRoleMustBeReferencedByComponent", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_seff_performance_av_pc_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_seff_performance_av_pc_ResourceCall.methods={pcm_av_pc_seff_performance_av_pc_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent, pcm_av_pc_seff_performance_av_pc_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole, pcm_av_pc_seff_performance_av_pc_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction}

# pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour class attributes and methods
pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor: Method = Method(name="RecoveryActionBehaviourHasOnlyOnePredecessor", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself: Method = Method(name="RecoveryActionBehaviourIsNotSuccessorOfItself", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes: Method = Method(name="SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour.methods={pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor, pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself, pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes}

# pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand class attributes and methods
pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand.methods={pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction}

# pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity class attributes and methods

# pcm_av_pc_qosannotations_av_pc_SpecifiedQoSAnnotation class attributes and methods

# QoSAnnotations class attributes and methods

# pcm_av_pc_qosannotations_av_pc_QoSAnnotations class attributes and methods
pcm_av_pc_qosannotations_av_pc_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed: Method = Method(name="MultipleReliabilityAnnotationsPerExternalCallNotAllowed", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_qosannotations_av_pc_QoSAnnotations.methods={pcm_av_pc_qosannotations_av_pc_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed}

# System class attributes and methods

# SpecifiedQoSAnnotation class attributes and methods

# seff_reliability_av_pc_RecoveryActionBehaviour class attributes and methods

# seff_reliability_av_pc_RecoveryAction class attributes and methods

# pcm_av_pc_seff_reliability_av_pc_RecoveryAction class attributes and methods
pcm_av_pc_seff_reliability_av_pc_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet: Method = Method(name="PrimaryBehaviourOfRecoveryActionMustBeSet", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_seff_reliability_av_pc_RecoveryAction.methods={pcm_av_pc_seff_reliability_av_pc_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet}

# pcm_av_pc_qos_performance_av_pc_SystemSpecifiedExecutionTime class attributes and methods
pcm_av_pc_qos_performance_av_pc_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem: Method = Method(name="SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_qos_performance_av_pc_SystemSpecifiedExecutionTime.methods={pcm_av_pc_qos_performance_av_pc_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem}

# SpecifiedExecutionTime class attributes and methods

# pcm_av_pc_qos_performance_av_pc_SpecifiedExecutionTime class attributes and methods

# pcm_av_pc_qos_performance_av_pc_ComponentSpecifiedExecutionTime class attributes and methods

# pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation class attributes and methods
pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem: Method = Method(name="SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation.methods={pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1, pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem, pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed}

# pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction class attributes and methods

# ExternalFailureOccurrenceDescription class attributes and methods

# pcm_av_pc_system_av_pc_System class attributes and methods
pcm_av_pc_system_av_pc_System_m_SystemMustHaveAtLeastOneProvidedRole: Method = Method(name="SystemMustHaveAtLeastOneProvidedRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_system_av_pc_System.methods={pcm_av_pc_system_av_pc_System_m_SystemMustHaveAtLeastOneProvidedRole}

# pcm_av_pc_resourceenvironment_av_pc_ResourceEnvironment class attributes and methods

# LinkingResource class attributes and methods

# ResourceContainer class attributes and methods

# pcm_av_pc_resourceenvironment_av_pc_LinkingResource class attributes and methods

# pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification class attributes and methods
pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification_MTTR: Property = Property(name="MTTR", type=FloatType)
pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification_MTTF: Property = Property(name="MTTF", type=FloatType)
pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification_requiredByContainer: Property = Property(name="requiredByContainer", type=BooleanType)
pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification_numberOfReplicas: Property = Property(name="numberOfReplicas", type=IntegerType)
pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification.attributes={pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification_requiredByContainer, pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification_MTTF, pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification_MTTR, pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification_numberOfReplicas}

# pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification class attributes and methods
pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification.attributes={pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification_failureProbability}

# ResourceEnvironment class attributes and methods

# pcm_av_pc_resourceenvironment_av_pc_ResourceContainer class attributes and methods

# pcm_av_pc_allocation_av_pc_AllocationContext class attributes and methods
pcm_av_pc_allocation_av_pc_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred: Method = Method(name="OneAssemblyContextOrOneEventChannelShouldBeReferred", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_allocation_av_pc_AllocationContext.methods={pcm_av_pc_allocation_av_pc_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred}

# Allocation class attributes and methods

# pcm_av_pc_allocation_av_pc_Allocation class attributes and methods
pcm_av_pc_allocation_av_pc_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce: Method = Method(name="EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_av_pc_allocation_av_pc_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource: Method = Method(name="CommunicatingServersHaveToBeConnectedByLinkingResource", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_av_pc_allocation_av_pc_Allocation.methods={pcm_av_pc_allocation_av_pc_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce, pcm_av_pc_allocation_av_pc_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource}

# pcm_av_pc_completions_av_pc_Completion class attributes and methods

# pcm_av_pc_completions_av_pc_CompletionRepository class attributes and methods

# Completion class attributes and methods

# pcm_av_pc_completions_av_pc_DelegatingExternalCallAction class attributes and methods

# ExternalCallAction class attributes and methods

# pcm_av_pc_completions_av_pc_NetworkDemandParametricResourceDemand class attributes and methods

# ParametricResourceDemand class attributes and methods

# AllocationContext class attributes and methods

# pcm_av_pc_subsystem_av_pc_SubSystem class attributes and methods

# repository_av_pc_RepositoryComponent class attributes and methods

# Relationships
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="pcm_av_pc_EObject", type=pcm_av_pc_Advice, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_Advice", type=pcm_av_pc_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scopedObject1: BinaryAssociation = BinaryAssociation(
    name="scopedObject1",
    ends={
        Property(name="pcm_av_pc_EObject2", type=pcm_av_pc_GlobalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_GlobalScope", type=pcm_av_pc_EObject, multiplicity=Multiplicity(0, 1))
    }
)
scopedObject3: BinaryAssociation = BinaryAssociation(
    name="scopedObject3",
    ends={
        Property(name="pcm_av_pc_EObject4", type=pcm_av_pc_PerJoinPointScope, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_PerJoinPointScope", type=pcm_av_pc_EObject, multiplicity=Multiplicity(0, 1))
    }
)
children5: BinaryAssociation = BinaryAssociation(
    name="children5",
    ends={
        Property(name="pcm_av_pc_EObject6", type=pcm_av_pc_Pointcut, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_Pointcut", type=pcm_av_pc_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredRoles_InterfaceRequiringEntity43: BinaryAssociation = BinaryAssociation(
    name="requiredRoles_InterfaceRequiringEntity43",
    ends={
        Property(name="RequiredRole", type=RequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="repository_av_pc44", type=pcm_av_pc_entity_av_pc_InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1))
    }
)
resourceCall__PCMRandomVariable11: BinaryAssociation = BinaryAssociation(
    name="resourceCall__PCMRandomVariable11",
    ends={
        Property(name="seff_av_pc13", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_av_pc12", type=seff_performance_av_pc_ResourceCall, multiplicity=Multiplicity(0, 1))
    }
)
resourceRequiredRoles__ResourceInterfaceRequiringEntity45: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRoles__ResourceInterfaceRequiringEntity45",
    ends={
        Property(name="core_av_pc47", type=pcm_av_pc_entity_av_pc_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_av_pc46", type=entity_av_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parametricResourceDemand_PCMRandomVariable14: BinaryAssociation = BinaryAssociation(
    name="parametricResourceDemand_PCMRandomVariable14",
    ends={
        Property(name="seff_av_pc16", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_av_pc15", type=seff_performance_av_pc_ParametricResourceDemand, multiplicity=Multiplicity(0, 1))
    }
)
loopAction_PCMRandomVariable17: BinaryAssociation = BinaryAssociation(
    name="loopAction_PCMRandomVariable17",
    ends={
        Property(name="seff_av_pc18", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopAction", type=LoopAction, multiplicity=Multiplicity(0, 1))
    }
)
requiredResourceInterface__ResourceRequiredRole48: BinaryAssociation = BinaryAssociation(
    name="requiredResourceInterface__ResourceRequiredRole48",
    ends={
        Property(name="ResourceInterface49", type=pcm_av_pc_entity_av_pc_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_entity_av_pc_ResourceRequiredRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaceRequiringEntity__ResourceRequiredRole50: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceRequiringEntity__ResourceRequiredRole50",
    ends={
        Property(name="core_av_pc52", type=pcm_av_pc_entity_av_pc_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_av_pc51", type=entity_av_pc_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
guardedBranchTransition_PCMRandomVariable19: BinaryAssociation = BinaryAssociation(
    name="guardedBranchTransition_PCMRandomVariable19",
    ends={
        Property(name="seff_av_pc20", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="GuardedBranchTransition", type=GuardedBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
specifiedExecutionTime_PCMRandomVariable21: BinaryAssociation = BinaryAssociation(
    name="specifiedExecutionTime_PCMRandomVariable21",
    ends={
        Property(name="qosannotations_av_pc", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="qos_performance_av_pc", type=qos_performance_av_pc_SpecifiedExecutionTime, multiplicity=Multiplicity(0, 1))
    }
)
resourceProvidedRoles__ResourceInterfaceProvidingEntity53: BinaryAssociation = BinaryAssociation(
    name="resourceProvidedRoles__ResourceInterfaceProvidingEntity53",
    ends={
        Property(name="core_av_pc55", type=pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_av_pc54", type=entity_av_pc_ResourceProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventChannelSinkConnector__FilterCondition22: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__FilterCondition22",
    ends={
        Property(name="core_av_pc", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_pc", type=composition_av_pc_EventChannelSinkConnector, multiplicity=Multiplicity(0, 1))
    }
)
assemblyEventConnector__FilterCondition23: BinaryAssociation = BinaryAssociation(
    name="assemblyEventConnector__FilterCondition23",
    ends={
        Property(name="core_av_pc25", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_pc24", type=composition_av_pc_AssemblyEventConnector, multiplicity=Multiplicity(0, 1))
    }
)
loop_LoopIteration26: BinaryAssociation = BinaryAssociation(
    name="loop_LoopIteration26",
    ends={
        Property(name="usagemodel_av_pc27", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Loop", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
openWorkload_PCMRandomVariable28: BinaryAssociation = BinaryAssociation(
    name="openWorkload_PCMRandomVariable28",
    ends={
        Property(name="usagemodel_av_pc29", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="OpenWorkload", type=OpenWorkload, multiplicity=Multiplicity(0, 1))
    }
)
delay_TimeSpecification30: BinaryAssociation = BinaryAssociation(
    name="delay_TimeSpecification30",
    ends={
        Property(name="usagemodel_av_pc31", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Delay", type=Delay, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecifcation_throughput_PCMRandomVariable32: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifcation_throughput_PCMRandomVariable32",
    ends={
        Property(name="resourceenvironment_av_pc", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceSpecification_processingRate_PCMRandomVariable33: BinaryAssociation = BinaryAssociation(
    name="processingResourceSpecification_processingRate_PCMRandomVariable33",
    ends={
        Property(name="resourceenvironment_av_pc34", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcessingResourceSpecification", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecification_latency_PCMRandomVariable35: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecification_latency_PCMRandomVariable35",
    ends={
        Property(name="resourceenvironment_av_pc37", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceSpecification36", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaceProvidingEntity__ResourceProvidedRole38: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceProvidingEntity__ResourceProvidedRole38",
    ends={
        Property(name="core_av_pc39", type=pcm_av_pc_entity_av_pc_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_av_pc", type=entity_av_pc_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
providedResourceInterface__ResourceProvidedRole40: BinaryAssociation = BinaryAssociation(
    name="providedResourceInterface__ResourceProvidedRole40",
    ends={
        Property(name="ResourceInterface", type=pcm_av_pc_entity_av_pc_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_entity_av_pc_ResourceProvidedRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
closedWorkload_PCMRandomVariable7: BinaryAssociation = BinaryAssociation(
    name="closedWorkload_PCMRandomVariable7",
    ends={
        Property(name="usagemodel_av_pc", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ClosedWorkload", type=ClosedWorkload, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_capacity_PCMRandomVariable8: BinaryAssociation = BinaryAssociation(
    name="passiveResource_capacity_PCMRandomVariable8",
    ends={
        Property(name="repository_av_pc", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
providedRoles_InterfaceProvidingEntity41: BinaryAssociation = BinaryAssociation(
    name="providedRoles_InterfaceProvidingEntity41",
    ends={
        Property(name="repository_av_pc42", type=pcm_av_pc_entity_av_pc_InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="ProvidedRole", type=ProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableCharacterisation_Specification9: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_Specification9",
    ends={
        Property(name="parameter_av_pc", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableCharacterisation", type=VariableCharacterisation, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureCall__PCMRandomVariable10: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__PCMRandomVariable10",
    ends={
        Property(name="seff_av_pc", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_av_pc", type=seff_performance_av_pc_InfrastructureCall, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContexts__ComposedStructure59: BinaryAssociation = BinaryAssociation(
    name="assemblyContexts__ComposedStructure59",
    ends={
        Property(name="core_av_pc61", type=pcm_av_pc_composition_av_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_pc60", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredDelegationConnectors_ComposedStructure62: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredDelegationConnectors_ComposedStructure62",
    ends={
        Property(name="core_av_pc64", type=pcm_av_pc_composition_av_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_pc63", type=composition_av_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventChannel__ComposedStructure65: BinaryAssociation = BinaryAssociation(
    name="eventChannel__ComposedStructure65",
    ends={
        Property(name="core_av_pc67", type=pcm_av_pc_composition_av_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_pc66", type=composition_av_pc_EventChannel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectors__ComposedStructure68: BinaryAssociation = BinaryAssociation(
    name="connectors__ComposedStructure68",
    ends={
        Property(name="core_av_pc70", type=pcm_av_pc_composition_av_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_pc69", type=composition_av_pc_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentStructure__Connector56: BinaryAssociation = BinaryAssociation(
    name="parentStructure__Connector56",
    ends={
        Property(name="core_av_pc58", type=pcm_av_pc_composition_av_pc_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_pc57", type=composition_av_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure__EventChannel85: BinaryAssociation = BinaryAssociation(
    name="parentStructure__EventChannel85",
    ends={
        Property(name="core_av_pc87", type=pcm_av_pc_composition_av_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_pc86", type=composition_av_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EventChannelSourceRole88: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EventChannelSourceRole88",
    ends={
        Property(name="SourceRole", type=pcm_av_pc_composition_av_pc_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_EventChannelSourceConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__EventChannelSourceConnector89: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSourceConnector89",
    ends={
        Property(name="composition_av_pc_AssemblyContext", type=pcm_av_pc_composition_av_pc_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_EventChannelSourceConnector90", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSourceConnector91: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSourceConnector91",
    ends={
        Property(name="core_av_pc93", type=pcm_av_pc_composition_av_pc_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_pc92", type=composition_av_pc_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__EventChannelSinkConnector94: BinaryAssociation = BinaryAssociation(
    name="sinkRole__EventChannelSinkConnector94",
    ends={
        Property(name="SinkRole", type=pcm_av_pc_composition_av_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_EventChannelSinkConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__EventChannelSinkConnector95: BinaryAssociation = BinaryAssociation(
    name="filterCondition__EventChannelSinkConnector95",
    ends={
        Property(name="core_av_pc96", type=pcm_av_pc_composition_av_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext__EventChannelSinkConnector97: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSinkConnector97",
    ends={
        Property(name="composition_av_pc_AssemblyContext99", type=pcm_av_pc_composition_av_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_EventChannelSinkConnector98", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSinkConnector100: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSinkConnector100",
    ends={
        Property(name="core_av_pc102", type=pcm_av_pc_composition_av_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_pc101", type=composition_av_pc_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
innerResourceRequiredRole_ResourceRequiredDelegationConnector71: BinaryAssociation = BinaryAssociation(
    name="innerResourceRequiredRole_ResourceRequiredDelegationConnector71",
    ends={
        Property(name="entity_av_pc_ResourceRequiredRole", type=pcm_av_pc_composition_av_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_ResourceRequiredDelegationConnector", type=entity_av_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerResourceRequiredRole_ResourceRequiredDelegationConnector72: BinaryAssociation = BinaryAssociation(
    name="outerResourceRequiredRole_ResourceRequiredDelegationConnector72",
    ends={
        Property(name="entity_av_pc_ResourceRequiredRole74", type=pcm_av_pc_composition_av_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_ResourceRequiredDelegationConnector73", type=entity_av_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure_ResourceRequiredDelegationConnector75: BinaryAssociation = BinaryAssociation(
    name="parentStructure_ResourceRequiredDelegationConnector75",
    ends={
        Property(name="core_av_pc77", type=pcm_av_pc_composition_av_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_pc76", type=composition_av_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__EventChannel78: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventChannel78",
    ends={
        Property(name="EventGroup", type=pcm_av_pc_composition_av_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_EventChannel", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSourceConnector__EventChannel79: BinaryAssociation = BinaryAssociation(
    name="eventChannelSourceConnector__EventChannel79",
    ends={
        Property(name="core_av_pc81", type=pcm_av_pc_composition_av_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_pc80", type=composition_av_pc_EventChannelSourceConnector, multiplicity=Multiplicity(0, 9999))
    }
)
eventChannelSinkConnector__EventChannel82: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__EventChannel82",
    ends={
        Property(name="core_av_pc84", type=pcm_av_pc_composition_av_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_pc83", type=composition_av_pc_EventChannelSinkConnector, multiplicity=Multiplicity(0, 9999))
    }
)
innerRequiredRole_RequiredDelegationConnector110: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole_RequiredDelegationConnector110",
    ends={
        Property(name="OperationRequiredRole", type=pcm_av_pc_composition_av_pc_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_RequiredDelegationConnector", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole_RequiredDelegationConnector111: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole_RequiredDelegationConnector111",
    ends={
        Property(name="OperationRequiredRole113", type=pcm_av_pc_composition_av_pc_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_RequiredDelegationConnector112", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_RequiredDelegationConnector114: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_RequiredDelegationConnector114",
    ends={
        Property(name="composition_av_pc_AssemblyContext116", type=pcm_av_pc_composition_av_pc_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_RequiredDelegationConnector115", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole_ProvidedDelegationConnector103: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole_ProvidedDelegationConnector103",
    ends={
        Property(name="OperationProvidedRole", type=pcm_av_pc_composition_av_pc_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_ProvidedDelegationConnector", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole_ProvidedDelegationConnector104: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole_ProvidedDelegationConnector104",
    ends={
        Property(name="OperationProvidedRole106", type=pcm_av_pc_composition_av_pc_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_ProvidedDelegationConnector105", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_ProvidedDelegationConnector107: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ProvidedDelegationConnector107",
    ends={
        Property(name="composition_av_pc_AssemblyContext109", type=pcm_av_pc_composition_av_pc_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_ProvidedDelegationConnector108", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providedRole_AssemblyConnector122: BinaryAssociation = BinaryAssociation(
    name="providedRole_AssemblyConnector122",
    ends={
        Property(name="OperationProvidedRole124", type=pcm_av_pc_composition_av_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyConnector123", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole_AssemblyConnector125: BinaryAssociation = BinaryAssociation(
    name="requiredRole_AssemblyConnector125",
    ends={
        Property(name="OperationRequiredRole127", type=pcm_av_pc_composition_av_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyConnector126", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__AssemblyEventConnector128: BinaryAssociation = BinaryAssociation(
    name="sinkRole__AssemblyEventConnector128",
    ends={
        Property(name="SinkRole129", type=pcm_av_pc_composition_av_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyEventConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__AssemblyEventConnector130: BinaryAssociation = BinaryAssociation(
    name="sourceRole__AssemblyEventConnector130",
    ends={
        Property(name="SourceRole132", type=pcm_av_pc_composition_av_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyEventConnector131", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkAssemblyContext__AssemblyEventConnector133: BinaryAssociation = BinaryAssociation(
    name="sinkAssemblyContext__AssemblyEventConnector133",
    ends={
        Property(name="composition_av_pc_AssemblyContext135", type=pcm_av_pc_composition_av_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyEventConnector134", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
sourceAssemblyContext__AssemblyEventConnector136: BinaryAssociation = BinaryAssociation(
    name="sourceAssemblyContext__AssemblyEventConnector136",
    ends={
        Property(name="composition_av_pc_AssemblyContext138", type=pcm_av_pc_composition_av_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyEventConnector137", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__AssemblyEventConnector139: BinaryAssociation = BinaryAssociation(
    name="filterCondition__AssemblyEventConnector139",
    ends={
        Property(name="core_av_pc141", type=pcm_av_pc_composition_av_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable140", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
innerSourceRole__SourceRole142: BinaryAssociation = BinaryAssociation(
    name="innerSourceRole__SourceRole142",
    ends={
        Property(name="SourceRole143", type=pcm_av_pc_composition_av_pc_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_SourceDelegationConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSourceRole__SourceRole144: BinaryAssociation = BinaryAssociation(
    name="outerSourceRole__SourceRole144",
    ends={
        Property(name="SourceRole146", type=pcm_av_pc_composition_av_pc_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_SourceDelegationConnector145", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext_AssemblyConnector117: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext_AssemblyConnector117",
    ends={
        Property(name="composition_av_pc_AssemblyContext118", type=pcm_av_pc_composition_av_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyConnector", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext_AssemblyConnector119: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext_AssemblyConnector119",
    ends={
        Property(name="composition_av_pc_AssemblyContext121", type=pcm_av_pc_composition_av_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyConnector120", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredInfrastructureDelegationConnector177: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredInfrastructureDelegationConnector177",
    ends={
        Property(name="pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector178", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1)),
        Property(name="InfrastructureRequiredRole179", type=pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1))
    }
)
assemblyContext__RequiredInfrastructureDelegationConnector180: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredInfrastructureDelegationConnector180",
    ends={
        Property(name="composition_av_pc_AssemblyContext182", type=pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector181", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredResourceDelegationConnector183: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredResourceDelegationConnector183",
    ends={
        Property(name="composition_av_pc_AssemblyContext184", type=pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole__RequiredResourceDelegationConnector185: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredResourceDelegationConnector185",
    ends={
        Property(name="entity_av_pc_ResourceRequiredRole187", type=pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector186", type=entity_av_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredResourceDelegationConnector188: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredResourceDelegationConnector188",
    ends={
        Property(name="entity_av_pc_ResourceRequiredRole190", type=pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector189", type=entity_av_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure__AssemblyContext191: BinaryAssociation = BinaryAssociation(
    name="parentStructure__AssemblyContext191",
    ends={
        Property(name="core_av_pc193", type=pcm_av_pc_composition_av_pc_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_pc192", type=composition_av_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
encapsulatedComponent__AssemblyContext194: BinaryAssociation = BinaryAssociation(
    name="encapsulatedComponent__AssemblyContext194",
    ends={
        Property(name="RepositoryComponent", type=pcm_av_pc_composition_av_pc_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyContext", type=RepositoryComponent, multiplicity=Multiplicity(0, 1))
    }
)
configParameterUsages__AssemblyContext195: BinaryAssociation = BinaryAssociation(
    name="configParameterUsages__AssemblyContext195",
    ends={
        Property(name="parameter_av_pc196", type=pcm_av_pc_composition_av_pc_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assemblyContext__SourceDelegationConnector147: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SourceDelegationConnector147",
    ends={
        Property(name="composition_av_pc_AssemblyContext149", type=pcm_av_pc_composition_av_pc_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_SourceDelegationConnector148", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SinkDelegationConnector150: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SinkDelegationConnector150",
    ends={
        Property(name="composition_av_pc_AssemblyContext151", type=pcm_av_pc_composition_av_pc_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_SinkDelegationConnector", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerSinkRole__SinkRole152: BinaryAssociation = BinaryAssociation(
    name="innerSinkRole__SinkRole152",
    ends={
        Property(name="SinkRole154", type=pcm_av_pc_composition_av_pc_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_SinkDelegationConnector153", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSinkRole__SinkRole155: BinaryAssociation = BinaryAssociation(
    name="outerSinkRole__SinkRole155",
    ends={
        Property(name="SinkRole157", type=pcm_av_pc_composition_av_pc_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_SinkDelegationConnector156", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
providedRole__AssemblyInfrastructureConnector158: BinaryAssociation = BinaryAssociation(
    name="providedRole__AssemblyInfrastructureConnector158",
    ends={
        Property(name="InfrastructureProvidedRole", type=pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__AssemblyInfrastructureConnector159: BinaryAssociation = BinaryAssociation(
    name="requiredRole__AssemblyInfrastructureConnector159",
    ends={
        Property(name="InfrastructureRequiredRole", type=pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector160", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext__AssemblyInfrastructureConnector161: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext__AssemblyInfrastructureConnector161",
    ends={
        Property(name="composition_av_pc_AssemblyContext163", type=pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector162", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext__AssemblyInfrastructureConnector164: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext__AssemblyInfrastructureConnector164",
    ends={
        Property(name="composition_av_pc_AssemblyContext166", type=pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector165", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole__ProvidedInfrastructureDelegationConnector167: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole__ProvidedInfrastructureDelegationConnector167",
    ends={
        Property(name="InfrastructureProvidedRole168", type=pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole__ProvidedInfrastructureDelegationConnector169: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole__ProvidedInfrastructureDelegationConnector169",
    ends={
        Property(name="InfrastructureProvidedRole171", type=pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector170", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__ProvidedInfrastructureDelegationConnector172: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__ProvidedInfrastructureDelegationConnector172",
    ends={
        Property(name="composition_av_pc_AssemblyContext174", type=pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector173", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole__RequiredInfrastructureDelegationConnector175: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredInfrastructureDelegationConnector175",
    ends={
        Property(name="InfrastructureRequiredRole176", type=pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
providedRole_EntryLevelSystemCall218: BinaryAssociation = BinaryAssociation(
    name="providedRole_EntryLevelSystemCall218",
    ends={
        Property(name="OperationProvidedRole219", type=pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__EntryLevelSystemCall220: BinaryAssociation = BinaryAssociation(
    name="operationSignature__EntryLevelSystemCall220",
    ends={
        Property(name="OperationSignature", type=pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall221", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
outputParameterUsages_EntryLevelSystemCall222: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsages_EntryLevelSystemCall222",
    ends={
        Property(name="parameter_av_pc224", type=pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage223", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_Workload197: BinaryAssociation = BinaryAssociation(
    name="usageScenario_Workload197",
    ends={
        Property(name="usagemodel_av_pc198", type=pcm_av_pc_usagemodel_av_pc_Workload, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UsageScenario199: BinaryAssociation = BinaryAssociation(
    name="usageModel_UsageScenario199",
    ends={
        Property(name="usagemodel_av_pc200", type=pcm_av_pc_usagemodel_av_pc_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageModel", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_UsageScenario201: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_UsageScenario201",
    ends={
        Property(name="usagemodel_av_pc202", type=pcm_av_pc_usagemodel_av_pc_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
workload_UsageScenario203: BinaryAssociation = BinaryAssociation(
    name="workload_UsageScenario203",
    ends={
        Property(name="usagemodel_av_pc204", type=pcm_av_pc_usagemodel_av_pc_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="Workload", type=Workload, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext_userData205: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_userData205",
    ends={
        Property(name="composition_av_pc_AssemblyContext206", type=pcm_av_pc_usagemodel_av_pc_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_usagemodel_av_pc_UserData", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UserData207: BinaryAssociation = BinaryAssociation(
    name="usageModel_UserData207",
    ends={
        Property(name="usagemodel_av_pc209", type=pcm_av_pc_usagemodel_av_pc_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageModel208", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
userDataParameterUsages_UserData210: BinaryAssociation = BinaryAssociation(
    name="userDataParameterUsages_UserData210",
    ends={
        Property(name="parameter_av_pc212", type=pcm_av_pc_usagemodel_av_pc_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage211", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_UsageModel213: BinaryAssociation = BinaryAssociation(
    name="usageScenario_UsageModel213",
    ends={
        Property(name="usagemodel_av_pc215", type=pcm_av_pc_usagemodel_av_pc_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageScenario214", type=UsageScenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_UsageModel216: BinaryAssociation = BinaryAssociation(
    name="userData_UsageModel216",
    ends={
        Property(name="usagemodel_av_pc217", type=pcm_av_pc_usagemodel_av_pc_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="UserData", type=UserData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_SenarioBehaviour236: BinaryAssociation = BinaryAssociation(
    name="usageScenario_SenarioBehaviour236",
    ends={
        Property(name="usagemodel_av_pc238", type=pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageScenario237", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
branchTransition_ScenarioBehaviour239: BinaryAssociation = BinaryAssociation(
    name="branchTransition_ScenarioBehaviour239",
    ends={
        Property(name="usagemodel_av_pc240", type=pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="BranchTransition", type=BranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
loop_ScenarioBehaviour241: BinaryAssociation = BinaryAssociation(
    name="loop_ScenarioBehaviour241",
    ends={
        Property(name="usagemodel_av_pc243", type=pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="Loop242", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
inputParameterUsages_EntryLevelSystemCall225: BinaryAssociation = BinaryAssociation(
    name="inputParameterUsages_EntryLevelSystemCall225",
    ends={
        Property(name="parameter_av_pc227", type=pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage226", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
successor228: BinaryAssociation = BinaryAssociation(
    name="successor228",
    ends={
        Property(name="usagemodel_av_pc229", type=pcm_av_pc_usagemodel_av_pc_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
predecessor230: BinaryAssociation = BinaryAssociation(
    name="predecessor230",
    ends={
        Property(name="usagemodel_av_pc232", type=pcm_av_pc_usagemodel_av_pc_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction231", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_AbstractUserAction233: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_AbstractUserAction233",
    ends={
        Property(name="usagemodel_av_pc235", type=pcm_av_pc_usagemodel_av_pc_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour234", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
actions_ScenarioBehaviour244: BinaryAssociation = BinaryAssociation(
    name="actions_ScenarioBehaviour244",
    ends={
        Property(name="usagemodel_av_pc246", type=pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction245", type=AbstractUserAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branch_BranchTransition247: BinaryAssociation = BinaryAssociation(
    name="branch_BranchTransition247",
    ends={
        Property(name="usagemodel_av_pc248", type=pcm_av_pc_usagemodel_av_pc_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="Branch", type=Branch, multiplicity=Multiplicity(0, 1))
    }
)
branchedBehaviour_BranchTransition249: BinaryAssociation = BinaryAssociation(
    name="branchedBehaviour_BranchTransition249",
    ends={
        Property(name="usagemodel_av_pc251", type=pcm_av_pc_usagemodel_av_pc_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour250", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchTransitions_Branch252: BinaryAssociation = BinaryAssociation(
    name="branchTransitions_Branch252",
    ends={
        Property(name="usagemodel_av_pc254", type=pcm_av_pc_usagemodel_av_pc_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="BranchTransition253", type=BranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopIteration_Loop255: BinaryAssociation = BinaryAssociation(
    name="loopIteration_Loop255",
    ends={
        Property(name="core_av_pc257", type=pcm_av_pc_usagemodel_av_pc_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable256", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyBehaviour_Loop258: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop258",
    ends={
        Property(name="usagemodel_av_pc260", type=pcm_av_pc_usagemodel_av_pc_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour259", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capacity_PassiveResource270: BinaryAssociation = BinaryAssociation(
    name="capacity_PassiveResource270",
    ends={
        Property(name="core_av_pc272", type=pcm_av_pc_repository_av_pc_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable271", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicComponent_PassiveResource273: BinaryAssociation = BinaryAssociation(
    name="basicComponent_PassiveResource273",
    ends={
        Property(name="repository_av_pc274", type=pcm_av_pc_repository_av_pc_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="BasicComponent", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
resourceTimeoutFailureType__PassiveResource275: BinaryAssociation = BinaryAssociation(
    name="resourceTimeoutFailureType__PassiveResource275",
    ends={
        Property(name="reliability_av_pc", type=pcm_av_pc_repository_av_pc_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceTimeoutFailureType", type=ResourceTimeoutFailureType, multiplicity=Multiplicity(0, 1))
    }
)
interArrivalTime_OpenWorkload261: BinaryAssociation = BinaryAssociation(
    name="interArrivalTime_OpenWorkload261",
    ends={
        Property(name="core_av_pc263", type=pcm_av_pc_usagemodel_av_pc_OpenWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable262", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeSpecification_Delay264: BinaryAssociation = BinaryAssociation(
    name="timeSpecification_Delay264",
    ends={
        Property(name="core_av_pc266", type=pcm_av_pc_usagemodel_av_pc_Delay, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable265", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thinkTime_ClosedWorkload267: BinaryAssociation = BinaryAssociation(
    name="thinkTime_ClosedWorkload267",
    ends={
        Property(name="core_av_pc269", type=pcm_av_pc_usagemodel_av_pc_ClosedWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable268", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parentCompleteComponentTypes281: BinaryAssociation = BinaryAssociation(
    name="parentCompleteComponentTypes281",
    ends={
        Property(name="CompleteComponentType", type=pcm_av_pc_repository_av_pc_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_ImplementationComponentType", type=CompleteComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
componentParameterUsage_ImplementationComponentType282: BinaryAssociation = BinaryAssociation(
    name="componentParameterUsage_ImplementationComponentType282",
    ends={
        Property(name="VariableUsage284", type=pcm_av_pc_repository_av_pc_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_ImplementationComponentType283", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceEffectSpecifications__BasicComponent276: BinaryAssociation = BinaryAssociation(
    name="serviceEffectSpecifications__BasicComponent276",
    ends={
        Property(name="seff_av_pc277", type=pcm_av_pc_repository_av_pc_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ServiceEffectSpecification", type=ServiceEffectSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveResource_BasicComponent278: BinaryAssociation = BinaryAssociation(
    name="passiveResource_BasicComponent278",
    ends={
        Property(name="repository_av_pc280", type=pcm_av_pc_repository_av_pc_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="PassiveResource279", type=PassiveResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceSignature__Parameter298: BinaryAssociation = BinaryAssociation(
    name="resourceSignature__Parameter298",
    ends={
        Property(name="resourcetype_av_pc", type=pcm_av_pc_repository_av_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceSignature", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
repository__DataType299: BinaryAssociation = BinaryAssociation(
    name="repository__DataType299",
    ends={
        Property(name="repository_av_pc301", type=pcm_av_pc_repository_av_pc_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository300", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
components__Repository302: BinaryAssociation = BinaryAssociation(
    name="components__Repository302",
    ends={
        Property(name="repository_av_pc304", type=pcm_av_pc_repository_av_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="RepositoryComponent303", type=RepositoryComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaces__Repository305: BinaryAssociation = BinaryAssociation(
    name="interfaces__Repository305",
    ends={
        Property(name="repository_av_pc306", type=pcm_av_pc_repository_av_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="Interface", type=Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureTypes__Repository307: BinaryAssociation = BinaryAssociation(
    name="failureTypes__Repository307",
    ends={
        Property(name="reliability_av_pc308", type=pcm_av_pc_repository_av_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="FailureType", type=FailureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository__RepositoryComponent285: BinaryAssociation = BinaryAssociation(
    name="repository__RepositoryComponent285",
    ends={
        Property(name="repository_av_pc286", type=pcm_av_pc_repository_av_pc_RepositoryComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
providingEntity_ProvidedRole287: BinaryAssociation = BinaryAssociation(
    name="providingEntity_ProvidedRole287",
    ends={
        Property(name="core_av_pc289", type=pcm_av_pc_repository_av_pc_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_av_pc288", type=entity_av_pc_InterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
dataType__Parameter290: BinaryAssociation = BinaryAssociation(
    name="dataType__Parameter290",
    ends={
        Property(name="DataType", type=pcm_av_pc_repository_av_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_Parameter", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureSignature__Parameter291: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignature__Parameter291",
    ends={
        Property(name="repository_av_pc292", type=pcm_av_pc_repository_av_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="InfrastructureSignature", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__Parameter293: BinaryAssociation = BinaryAssociation(
    name="operationSignature__Parameter293",
    ends={
        Property(name="repository_av_pc295", type=pcm_av_pc_repository_av_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationSignature294", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
eventType__Parameter296: BinaryAssociation = BinaryAssociation(
    name="eventType__Parameter296",
    ends={
        Property(name="repository_av_pc297", type=pcm_av_pc_repository_av_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="EventType", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
protocols__Interface314: BinaryAssociation = BinaryAssociation(
    name="protocols__Interface314",
    ends={
        Property(name="Protocol", type=pcm_av_pc_repository_av_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_Interface315", type=Protocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCharacterisations316: BinaryAssociation = BinaryAssociation(
    name="requiredCharacterisations316",
    ends={
        Property(name="repository_av_pc317", type=pcm_av_pc_repository_av_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="RequiredCharacterisation", type=RequiredCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureSignatures__InfrastructureInterface343: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignatures__InfrastructureInterface343",
    ends={
        Property(name="repository_av_pc345", type=pcm_av_pc_repository_av_pc_InfrastructureInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="InfrastructureSignature344", type=InfrastructureSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes__Repository309: BinaryAssociation = BinaryAssociation(
    name="dataTypes__Repository309",
    ends={
        Property(name="repository_av_pc311", type=pcm_av_pc_repository_av_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="DataType310", type=DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterface__InfrastructureRequiredRole346: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__InfrastructureRequiredRole346",
    ends={
        Property(name="InfrastructureInterface347", type=pcm_av_pc_repository_av_pc_InfrastructureRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_InfrastructureRequiredRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
repository__Interface318: BinaryAssociation = BinaryAssociation(
    name="repository__Interface318",
    ends={
        Property(name="repository_av_pc320", type=pcm_av_pc_repository_av_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository319", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
requiringEntity_RequiredRole348: BinaryAssociation = BinaryAssociation(
    name="requiringEntity_RequiredRole348",
    ends={
        Property(name="core_av_pc350", type=pcm_av_pc_repository_av_pc_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_av_pc349", type=entity_av_pc_InterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
parameter321: BinaryAssociation = BinaryAssociation(
    name="parameter321",
    ends={
        Property(name="Parameter", type=pcm_av_pc_repository_av_pc_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_RequiredCharacterisation", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
interface_RequiredCharacterisation322: BinaryAssociation = BinaryAssociation(
    name="interface_RequiredCharacterisation322",
    ends={
        Property(name="repository_av_pc324", type=pcm_av_pc_repository_av_pc_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="Interface323", type=Interface, multiplicity=Multiplicity(0, 1))
    }
)
parentInterfaces__Interface312: BinaryAssociation = BinaryAssociation(
    name="parentInterfaces__Interface312",
    ends={
        Property(name="Interface313", type=pcm_av_pc_repository_av_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_Interface", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
eventTypes__EventGroup325: BinaryAssociation = BinaryAssociation(
    name="eventTypes__EventGroup325",
    ends={
        Property(name="repository_av_pc327", type=pcm_av_pc_repository_av_pc_EventGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="EventType326", type=EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter__EventType328: BinaryAssociation = BinaryAssociation(
    name="parameter__EventType328",
    ends={
        Property(name="repository_av_pc330", type=pcm_av_pc_repository_av_pc_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter329", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventGroup__EventType331: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventType331",
    ends={
        Property(name="repository_av_pc333", type=pcm_av_pc_repository_av_pc_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="EventGroup332", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
exceptions__Signature334: BinaryAssociation = BinaryAssociation(
    name="exceptions__Signature334",
    ends={
        Property(name="ExceptionType", type=pcm_av_pc_repository_av_pc_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_Signature", type=ExceptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureType335: BinaryAssociation = BinaryAssociation(
    name="failureType335",
    ends={
        Property(name="FailureType337", type=pcm_av_pc_repository_av_pc_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_Signature336", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
parameters__InfrastructureSignature338: BinaryAssociation = BinaryAssociation(
    name="parameters__InfrastructureSignature338",
    ends={
        Property(name="repository_av_pc340", type=pcm_av_pc_repository_av_pc_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter339", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureInterface__InfrastructureSignature341: BinaryAssociation = BinaryAssociation(
    name="infrastructureInterface__InfrastructureSignature341",
    ends={
        Property(name="repository_av_pc342", type=pcm_av_pc_repository_av_pc_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="InfrastructureInterface", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
returnType__OperationSignature356: BinaryAssociation = BinaryAssociation(
    name="returnType__OperationSignature356",
    ends={
        Property(name="DataType357", type=pcm_av_pc_repository_av_pc_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_OperationSignature", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
signatures__OperationInterface358: BinaryAssociation = BinaryAssociation(
    name="signatures__OperationInterface358",
    ends={
        Property(name="repository_av_pc360", type=pcm_av_pc_repository_av_pc_OperationInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationSignature359", type=OperationSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interface__OperationSignature351: BinaryAssociation = BinaryAssociation(
    name="interface__OperationSignature351",
    ends={
        Property(name="repository_av_pc352", type=pcm_av_pc_repository_av_pc_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationInterface", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
parameters__OperationSignature353: BinaryAssociation = BinaryAssociation(
    name="parameters__OperationSignature353",
    ends={
        Property(name="repository_av_pc355", type=pcm_av_pc_repository_av_pc_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter354", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedInterface__OperationProvidedRole367: BinaryAssociation = BinaryAssociation(
    name="providedInterface__OperationProvidedRole367",
    ends={
        Property(name="OperationInterface368", type=pcm_av_pc_repository_av_pc_OperationProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_OperationProvidedRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface__InfrastructureProvidedRole369: BinaryAssociation = BinaryAssociation(
    name="providedInterface__InfrastructureProvidedRole369",
    ends={
        Property(name="InfrastructureInterface370", type=pcm_av_pc_repository_av_pc_InfrastructureProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_InfrastructureProvidedRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
requiredInterface__OperationRequiredRole361: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__OperationRequiredRole361",
    ends={
        Property(name="OperationInterface362", type=pcm_av_pc_repository_av_pc_OperationRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_OperationRequiredRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SourceRole363: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SourceRole363",
    ends={
        Property(name="EventGroup364", type=pcm_av_pc_repository_av_pc_SourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_SourceRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SinkRole365: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SinkRole365",
    ends={
        Property(name="EventGroup366", type=pcm_av_pc_repository_av_pc_SinkRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_SinkRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
innerType_CollectionDataType372: BinaryAssociation = BinaryAssociation(
    name="innerType_CollectionDataType372",
    ends={
        Property(name="DataType373", type=pcm_av_pc_repository_av_pc_CollectionDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_CollectionDataType", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
parentProvidesComponentTypes371: BinaryAssociation = BinaryAssociation(
    name="parentProvidesComponentTypes371",
    ends={
        Property(name="ProvidesComponentType", type=pcm_av_pc_repository_av_pc_CompleteComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_CompleteComponentType", type=ProvidesComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
innerDeclaration_CompositeDataType375: BinaryAssociation = BinaryAssociation(
    name="innerDeclaration_CompositeDataType375",
    ends={
        Property(name="repository_av_pc376", type=pcm_av_pc_repository_av_pc_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="InnerDeclaration", type=InnerDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype_InnerDeclaration377: BinaryAssociation = BinaryAssociation(
    name="datatype_InnerDeclaration377",
    ends={
        Property(name="DataType378", type=pcm_av_pc_repository_av_pc_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_InnerDeclaration", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
compositeDataType_InnerDeclaration379: BinaryAssociation = BinaryAssociation(
    name="compositeDataType_InnerDeclaration379",
    ends={
        Property(name="repository_av_pc381", type=pcm_av_pc_repository_av_pc_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="CompositeDataType380", type=CompositeDataType, multiplicity=Multiplicity(0, 1))
    }
)
parameter__ResourceSignature382: BinaryAssociation = BinaryAssociation(
    name="parameter__ResourceSignature382",
    ends={
        Property(name="repository_av_pc384", type=pcm_av_pc_resourcetype_av_pc_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter383", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceInterface__ResourceSignature385: BinaryAssociation = BinaryAssociation(
    name="resourceInterface__ResourceSignature385",
    ends={
        Property(name="resourcetype_av_pc387", type=pcm_av_pc_resourcetype_av_pc_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceInterface386", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
hardwareInducedFailureType__ProcessingResourceType388: BinaryAssociation = BinaryAssociation(
    name="hardwareInducedFailureType__ProcessingResourceType388",
    ends={
        Property(name="reliability_av_pc389", type=pcm_av_pc_resourcetype_av_pc_ProcessingResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="HardwareInducedFailureType", type=HardwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
resourceRepository_ResourceType390: BinaryAssociation = BinaryAssociation(
    name="resourceRepository_ResourceType390",
    ends={
        Property(name="resourcetype_av_pc391", type=pcm_av_pc_resourcetype_av_pc_ResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
parentType_CompositeDataType374: BinaryAssociation = BinaryAssociation(
    name="parentType_CompositeDataType374",
    ends={
        Property(name="CompositeDataType", type=pcm_av_pc_repository_av_pc_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 9999))
    }
)
networkInducedFailureType__CommunicationLinkResourceType402: BinaryAssociation = BinaryAssociation(
    name="networkInducedFailureType__CommunicationLinkResourceType402",
    ends={
        Property(name="reliability_av_pc403", type=pcm_av_pc_resourcetype_av_pc_CommunicationLinkResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="NetworkInducedFailureType", type=NetworkInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
resourceRepository__ResourceInterface404: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__ResourceInterface404",
    ends={
        Property(name="resourcetype_av_pc406", type=pcm_av_pc_resourcetype_av_pc_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceRepository405", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
resourceSignatures__ResourceInterface407: BinaryAssociation = BinaryAssociation(
    name="resourceSignatures__ResourceInterface407",
    ends={
        Property(name="resourcetype_av_pc409", type=pcm_av_pc_resourcetype_av_pc_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceSignature408", type=ResourceSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableCharacterisation_VariableUsage410: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_VariableUsage410",
    ends={
        Property(name="parameter_av_pc412", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableCharacterisation411", type=VariableCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_VariableUsage413: BinaryAssociation = BinaryAssociation(
    name="userData_VariableUsage413",
    ends={
        Property(name="usagemodel_av_pc415", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="UserData414", type=UserData, multiplicity=Multiplicity(0, 1))
    }
)
callAction__VariableUsage416: BinaryAssociation = BinaryAssociation(
    name="callAction__VariableUsage416",
    ends={
        Property(name="seff_av_pc417", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="CallAction", type=CallAction, multiplicity=Multiplicity(0, 1))
    }
)
synchronisationPoint_VariableUsage418: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_VariableUsage418",
    ends={
        Property(name="seff_av_pc419", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
callReturnAction__VariableUsage420: BinaryAssociation = BinaryAssociation(
    name="callReturnAction__VariableUsage420",
    ends={
        Property(name="seff_av_pc421", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="CallReturnAction", type=CallReturnAction, multiplicity=Multiplicity(0, 1))
    }
)
setVariableAction_VariableUsage422: BinaryAssociation = BinaryAssociation(
    name="setVariableAction_VariableUsage422",
    ends={
        Property(name="seff_av_pc423", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="SetVariableAction", type=SetVariableAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaces__ResourceRepository392: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaces__ResourceRepository392",
    ends={
        Property(name="resourcetype_av_pc394", type=pcm_av_pc_resourcetype_av_pc_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceInterface393", type=ResourceInterface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schedulingPolicies__ResourceRepository395: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicies__ResourceRepository395",
    ends={
        Property(name="resourcetype_av_pc396", type=pcm_av_pc_resourcetype_av_pc_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="SchedulingPolicy", type=SchedulingPolicy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
availableResourceTypes_ResourceRepository397: BinaryAssociation = BinaryAssociation(
    name="availableResourceTypes_ResourceRepository397",
    ends={
        Property(name="resourcetype_av_pc398", type=pcm_av_pc_resourcetype_av_pc_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceType", type=ResourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRepository__SchedulingPolicy399: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__SchedulingPolicy399",
    ends={
        Property(name="resourcetype_av_pc401", type=pcm_av_pc_resourcetype_av_pc_SchedulingPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceRepository400", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
specification_VariableCharacterisation435: BinaryAssociation = BinaryAssociation(
    name="specification_VariableCharacterisation435",
    ends={
        Property(name="core_av_pc437", type=pcm_av_pc_parameter_av_pc_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable436", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableUsage_VariableCharacterisation438: BinaryAssociation = BinaryAssociation(
    name="variableUsage_VariableCharacterisation438",
    ends={
        Property(name="parameter_av_pc440", type=pcm_av_pc_parameter_av_pc_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage439", type=VariableUsage, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage424: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage424",
    ends={
        Property(name="qosannotations_av_pc425", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="SpecifiedOutputParameterAbstraction", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__VariableUsage426: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__VariableUsage426",
    ends={
        Property(name="core_av_pc428", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_av_pc427", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_InputParameterUsage429: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_InputParameterUsage429",
    ends={
        Property(name="usagemodel_av_pc430", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="EntryLevelSystemCall", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_OutputParameterUsage431: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_OutputParameterUsage431",
    ends={
        Property(name="usagemodel_av_pc433", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="EntryLevelSystemCall432", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
namedReference__VariableUsage434: BinaryAssociation = BinaryAssociation(
    name="namedReference__VariableUsage434",
    ends={
        Property(name="parameter_av_pc_pcm_av_pc_AbstractNamedReference", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_parameter_av_pc_VariableUsage", type=parameter_av_pc_pcm_av_pc_AbstractNamedReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
internalAction__InternalFailureOccurrenceDescription445: BinaryAssociation = BinaryAssociation(
    name="internalAction__InternalFailureOccurrenceDescription445",
    ends={
        Property(name="seff_av_pc446", type=pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="InternalAction", type=InternalAction, multiplicity=Multiplicity(0, 1))
    }
)
softwareInducedFailureType__InternalFailureOccurrenceDescription447: BinaryAssociation = BinaryAssociation(
    name="softwareInducedFailureType__InternalFailureOccurrenceDescription447",
    ends={
        Property(name="reliability_av_pc448", type=pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="SoftwareInducedFailureType", type=SoftwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceType__NetworkInducedFailureType449: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType__NetworkInducedFailureType449",
    ends={
        Property(name="resourcetype_av_pc450", type=pcm_av_pc_reliability_av_pc_NetworkInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceType", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription451: BinaryAssociation = BinaryAssociation(
    name="specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription451",
    ends={
        Property(name="qosannotations_av_pc452", type=pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="qos_reliability_av_pc", type=qos_reliability_av_pc_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(0, 1))
    }
)
failureType__ExternalFailureOccurrenceDescription453: BinaryAssociation = BinaryAssociation(
    name="failureType__ExternalFailureOccurrenceDescription453",
    ends={
        Property(name="FailureType454", type=pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription", type=FailureType, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceType__HardwareInducedFailureType441: BinaryAssociation = BinaryAssociation(
    name="processingResourceType__HardwareInducedFailureType441",
    ends={
        Property(name="resourcetype_av_pc442", type=pcm_av_pc_reliability_av_pc_HardwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcessingResourceType", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
internalFailureOccurrenceDescriptions__SoftwareInducedFailureType443: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__SoftwareInducedFailureType443",
    ends={
        Property(name="reliability_av_pc444", type=pcm_av_pc_reliability_av_pc_SoftwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="InternalFailureOccurrenceDescription", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999))
    }
)
resourceDemand_Action461: BinaryAssociation = BinaryAssociation(
    name="resourceDemand_Action461",
    ends={
        Property(name="seff_av_pc463", type=pcm_av_pc_seff_av_pc_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_av_pc462", type=seff_performance_av_pc_ParametricResourceDemand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureCall__Action464: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__Action464",
    ends={
        Property(name="seff_av_pc466", type=pcm_av_pc_seff_av_pc_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_av_pc465", type=seff_performance_av_pc_InfrastructureCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceCall__Action467: BinaryAssociation = BinaryAssociation(
    name="resourceCall__Action467",
    ends={
        Property(name="seff_av_pc469", type=pcm_av_pc_seff_av_pc_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_av_pc468", type=seff_performance_av_pc_ResourceCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor_AbstractAction470: BinaryAssociation = BinaryAssociation(
    name="predecessor_AbstractAction470",
    ends={
        Property(name="seff_av_pc471", type=pcm_av_pc_seff_av_pc_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
successor_AbstractAction472: BinaryAssociation = BinaryAssociation(
    name="successor_AbstractAction472",
    ends={
        Property(name="seff_av_pc474", type=pcm_av_pc_seff_av_pc_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction473", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemandingBehaviour_AbstractAction475: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingBehaviour_AbstractAction475",
    ends={
        Property(name="seff_av_pc476", type=pcm_av_pc_seff_av_pc_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingBehaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource__ResourceTimeoutFailureType455: BinaryAssociation = BinaryAssociation(
    name="passiveResource__ResourceTimeoutFailureType455",
    ends={
        Property(name="repository_av_pc457", type=pcm_av_pc_reliability_av_pc_ResourceTimeoutFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="PassiveResource456", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
repository__FailureType458: BinaryAssociation = BinaryAssociation(
    name="repository__FailureType458",
    ends={
        Property(name="repository_av_pc460", type=pcm_av_pc_reliability_av_pc_FailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository459", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
abstractLoopAction_ResourceDemandingBehaviour477: BinaryAssociation = BinaryAssociation(
    name="abstractLoopAction_ResourceDemandingBehaviour477",
    ends={
        Property(name="seff_av_pc478", type=pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractLoopAction", type=AbstractLoopAction, multiplicity=Multiplicity(0, 1))
    }
)
abstractBranchTransition_ResourceDemandingBehaviour479: BinaryAssociation = BinaryAssociation(
    name="abstractBranchTransition_ResourceDemandingBehaviour479",
    ends={
        Property(name="seff_av_pc480", type=pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractBranchTransition", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
steps_Behaviour481: BinaryAssociation = BinaryAssociation(
    name="steps_Behaviour481",
    ends={
        Property(name="seff_av_pc483", type=pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction482", type=AbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyBehaviour_Loop484: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop484",
    ends={
        Property(name="seff_av_pc486", type=pcm_av_pc_seff_av_pc_AbstractLoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingBehaviour485", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchAction_AbstractBranchTransition487: BinaryAssociation = BinaryAssociation(
    name="branchAction_AbstractBranchTransition487",
    ends={
        Property(name="seff_av_pc488", type=pcm_av_pc_seff_av_pc_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="BranchAction", type=BranchAction, multiplicity=Multiplicity(0, 1))
    }
)
branchBehaviour_BranchTransition489: BinaryAssociation = BinaryAssociation(
    name="branchBehaviour_BranchTransition489",
    ends={
        Property(name="seff_av_pc491", type=pcm_av_pc_seff_av_pc_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingBehaviour490", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
describedService__SEFF498: BinaryAssociation = BinaryAssociation(
    name="describedService__SEFF498",
    ends={
        Property(name="Signature", type=pcm_av_pc_seff_av_pc_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_av_pc_ServiceEffectSpecification", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
basicComponent_ServiceEffectSpecification499: BinaryAssociation = BinaryAssociation(
    name="basicComponent_ServiceEffectSpecification499",
    ends={
        Property(name="repository_av_pc501", type=pcm_av_pc_seff_av_pc_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BasicComponent500", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemandingInternalBehaviours502: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingInternalBehaviours502",
    ends={
        Property(name="seff_av_pc503", type=pcm_av_pc_seff_av_pc_ResourceDemandingSEFF, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingInternalBehaviour", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceDemandingSEFF_ResourceDemandingInternalBehaviour504: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingSEFF_ResourceDemandingInternalBehaviour504",
    ends={
        Property(name="seff_av_pc505", type=pcm_av_pc_seff_av_pc_ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingSEFF", type=ResourceDemandingSEFF, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_ReleaseAction506: BinaryAssociation = BinaryAssociation(
    name="passiveResource_ReleaseAction506",
    ends={
        Property(name="PassiveResource507", type=pcm_av_pc_seff_av_pc_ReleaseAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_av_pc_ReleaseAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
branches_Branch492: BinaryAssociation = BinaryAssociation(
    name="branches_Branch492",
    ends={
        Property(name="seff_av_pc494", type=pcm_av_pc_seff_av_pc_BranchAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractBranchTransition493", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputVariableUsages__CallAction495: BinaryAssociation = BinaryAssociation(
    name="inputVariableUsages__CallAction495",
    ends={
        Property(name="parameter_av_pc497", type=pcm_av_pc_seff_av_pc_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage496", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterationCount_LoopAction508: BinaryAssociation = BinaryAssociation(
    name="iterationCount_LoopAction508",
    ends={
        Property(name="core_av_pc510", type=pcm_av_pc_seff_av_pc_LoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable509", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
asynchronousForkedBehaviours_ForkAction511: BinaryAssociation = BinaryAssociation(
    name="asynchronousForkedBehaviours_ForkAction511",
    ends={
        Property(name="seff_av_pc512", type=pcm_av_pc_seff_av_pc_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedBehaviour", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronisingBehaviours_ForkAction513: BinaryAssociation = BinaryAssociation(
    name="synchronisingBehaviours_ForkAction513",
    ends={
        Property(name="seff_av_pc515", type=pcm_av_pc_seff_av_pc_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="SynchronisationPoint514", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
synchronisationPoint_ForkedBehaviour516: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_ForkedBehaviour516",
    ends={
        Property(name="seff_av_pc518", type=pcm_av_pc_seff_av_pc_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="SynchronisationPoint517", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
forkAction_ForkedBehaivour519: BinaryAssociation = BinaryAssociation(
    name="forkAction_ForkedBehaivour519",
    ends={
        Property(name="seff_av_pc520", type=pcm_av_pc_seff_av_pc_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkAction", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
outputParameterUsage_SynchronisationPoint521: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsage_SynchronisationPoint521",
    ends={
        Property(name="parameter_av_pc523", type=pcm_av_pc_seff_av_pc_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage522", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledService_ExternalService530: BinaryAssociation = BinaryAssociation(
    name="calledService_ExternalService530",
    ends={
        Property(name="OperationSignature531", type=pcm_av_pc_seff_av_pc_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_av_pc_ExternalCallAction", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
role_ExternalService532: BinaryAssociation = BinaryAssociation(
    name="role_ExternalService532",
    ends={
        Property(name="OperationRequiredRole534", type=pcm_av_pc_seff_av_pc_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_av_pc_ExternalCallAction533", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
returnVariableUsage__CallReturnAction535: BinaryAssociation = BinaryAssociation(
    name="returnVariableUsage__CallReturnAction535",
    ends={
        Property(name="parameter_av_pc537", type=pcm_av_pc_seff_av_pc_CallReturnAction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage536", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveresource_AcquireAction538: BinaryAssociation = BinaryAssociation(
    name="passiveresource_AcquireAction538",
    ends={
        Property(name="PassiveResource539", type=pcm_av_pc_seff_av_pc_AcquireAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_av_pc_AcquireAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
forkAction_SynchronisationPoint524: BinaryAssociation = BinaryAssociation(
    name="forkAction_SynchronisationPoint524",
    ends={
        Property(name="seff_av_pc526", type=pcm_av_pc_seff_av_pc_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkAction525", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
synchronousForkedBehaviours_SynchronisationPoint527: BinaryAssociation = BinaryAssociation(
    name="synchronousForkedBehaviours_SynchronisationPoint527",
    ends={
        Property(name="seff_av_pc529", type=pcm_av_pc_seff_av_pc_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedBehaviour528", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledResourceDemandingInternalBehaviour548: BinaryAssociation = BinaryAssociation(
    name="calledResourceDemandingInternalBehaviour548",
    ends={
        Property(name="ResourceDemandingInternalBehaviour549", type=pcm_av_pc_seff_av_pc_InternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_av_pc_InternalCallAction", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
eventType__EmitEventAction550: BinaryAssociation = BinaryAssociation(
    name="eventType__EmitEventAction550",
    ends={
        Property(name="EventType551", type=pcm_av_pc_seff_av_pc_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_av_pc_EmitEventAction", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EmitEventAction552: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EmitEventAction552",
    ends={
        Property(name="SourceRole554", type=pcm_av_pc_seff_av_pc_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_av_pc_EmitEventAction553", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
internalFailureOccurrenceDescriptions__InternalAction555: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__InternalAction555",
    ends={
        Property(name="reliability_av_pc557", type=pcm_av_pc_seff_av_pc_InternalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="InternalFailureOccurrenceDescription556", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter_CollectionIteratorAction540: BinaryAssociation = BinaryAssociation(
    name="parameter_CollectionIteratorAction540",
    ends={
        Property(name="Parameter541", type=pcm_av_pc_seff_av_pc_CollectionIteratorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_av_pc_CollectionIteratorAction", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
branchCondition_GuardedBranchTransition542: BinaryAssociation = BinaryAssociation(
    name="branchCondition_GuardedBranchTransition542",
    ends={
        Property(name="core_av_pc544", type=pcm_av_pc_seff_av_pc_GuardedBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable543", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localVariableUsages_SetVariableAction545: BinaryAssociation = BinaryAssociation(
    name="localVariableUsages_SetVariableAction545",
    ends={
        Property(name="parameter_av_pc547", type=pcm_av_pc_seff_av_pc_SetVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage546", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature__InfrastructureCall558: BinaryAssociation = BinaryAssociation(
    name="signature__InfrastructureCall558",
    ends={
        Property(name="InfrastructureSignature559", type=pcm_av_pc_seff_performance_av_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_performance_av_pc_InfrastructureCall", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__InfrastructureCall560: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__InfrastructureCall560",
    ends={
        Property(name="core_av_pc562", type=pcm_av_pc_seff_performance_av_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable561", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action__InfrastructureCall563: BinaryAssociation = BinaryAssociation(
    name="action__InfrastructureCall563",
    ends={
        Property(name="seff_av_pc564", type=pcm_av_pc_seff_performance_av_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractInternalControlFlowAction", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__InfrastructureCall565: BinaryAssociation = BinaryAssociation(
    name="requiredRole__InfrastructureCall565",
    ends={
        Property(name="InfrastructureRequiredRole567", type=pcm_av_pc_seff_performance_av_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_performance_av_pc_InfrastructureCall566", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
action__ResourceCall568: BinaryAssociation = BinaryAssociation(
    name="action__ResourceCall568",
    ends={
        Property(name="seff_av_pc570", type=pcm_av_pc_seff_performance_av_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractInternalControlFlowAction569", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
specification_ParametericResourceDemand579: BinaryAssociation = BinaryAssociation(
    name="specification_ParametericResourceDemand579",
    ends={
        Property(name="core_av_pc581", type=pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable580", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredResource_ParametricResourceDemand582: BinaryAssociation = BinaryAssociation(
    name="requiredResource_ParametricResourceDemand582",
    ends={
        Property(name="ProcessingResourceType583", type=pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
action_ParametricResourceDemand584: BinaryAssociation = BinaryAssociation(
    name="action_ParametricResourceDemand584",
    ends={
        Property(name="seff_av_pc586", type=pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractInternalControlFlowAction585", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceRequiredRole__ResourceCall571: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRole__ResourceCall571",
    ends={
        Property(name="entity_av_pc_ResourceRequiredRole572", type=pcm_av_pc_seff_performance_av_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_performance_av_pc_ResourceCall", type=entity_av_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
signature__ResourceCall573: BinaryAssociation = BinaryAssociation(
    name="signature__ResourceCall573",
    ends={
        Property(name="ResourceSignature575", type=pcm_av_pc_seff_performance_av_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_performance_av_pc_ResourceCall574", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__ResourceCall576: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__ResourceCall576",
    ends={
        Property(name="core_av_pc578", type=pcm_av_pc_seff_performance_av_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable577", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primaryBehaviour__RecoveryAction590: BinaryAssociation = BinaryAssociation(
    name="primaryBehaviour__RecoveryAction590",
    ends={
        Property(name="seff_reliability_av_pc_RecoveryActionBehaviour591", type=pcm_av_pc_seff_reliability_av_pc_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_reliability_av_pc_RecoveryAction", type=seff_reliability_av_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
recoveryActionBehaviours__RecoveryAction592: BinaryAssociation = BinaryAssociation(
    name="recoveryActionBehaviours__RecoveryAction592",
    ends={
        Property(name="seff_av_pc594", type=pcm_av_pc_seff_reliability_av_pc_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_reliability_av_pc593", type=seff_reliability_av_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureTypes_FailureHandlingEntity595: BinaryAssociation = BinaryAssociation(
    name="failureTypes_FailureHandlingEntity595",
    ends={
        Property(name="FailureType596", type=pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
signature_SpecifiedQoSAnnation597: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedQoSAnnation597",
    ends={
        Property(name="Signature598", type=pcm_av_pc_qosannotations_av_pc_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_qosannotations_av_pc_SpecifiedQoSAnnotation", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedQoSAnnotation599: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedQoSAnnotation599",
    ends={
        Property(name="Role", type=pcm_av_pc_qosannotations_av_pc_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_qosannotations_av_pc_SpecifiedQoSAnnotation600", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
qosAnnotations_SpecifiedQoSAnnotation601: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedQoSAnnotation601",
    ends={
        Property(name="qosannotations_av_pc602", type=pcm_av_pc_qosannotations_av_pc_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstractions_QoSAnnotations603: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstractions_QoSAnnotations603",
    ends={
        Property(name="qosannotations_av_pc605", type=pcm_av_pc_qosannotations_av_pc_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="SpecifiedOutputParameterAbstraction604", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
system_QoSAnnotations606: BinaryAssociation = BinaryAssociation(
    name="system_QoSAnnotations606",
    ends={
        Property(name="system_av_pc", type=pcm_av_pc_qosannotations_av_pc_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="System", type=System, multiplicity=Multiplicity(0, 1))
    }
)
failureHandlingAlternatives__RecoveryActionBehaviour587: BinaryAssociation = BinaryAssociation(
    name="failureHandlingAlternatives__RecoveryActionBehaviour587",
    ends={
        Property(name="seff_reliability_av_pc_RecoveryActionBehaviour", type=pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour", type=seff_reliability_av_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999))
    }
)
recoveryAction__RecoveryActionBehaviour588: BinaryAssociation = BinaryAssociation(
    name="recoveryAction__RecoveryActionBehaviour588",
    ends={
        Property(name="seff_av_pc589", type=pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_reliability_av_pc", type=seff_reliability_av_pc_RecoveryAction, multiplicity=Multiplicity(0, 1))
    }
)
specification_SpecifiedExecutionTime620: BinaryAssociation = BinaryAssociation(
    name="specification_SpecifiedExecutionTime620",
    ends={
        Property(name="core_av_pc622", type=pcm_av_pc_qos_performance_av_pc_SpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable621", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext_ComponentSpecifiedExecutionTime623: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ComponentSpecifiedExecutionTime623",
    ends={
        Property(name="composition_av_pc_AssemblyContext624", type=pcm_av_pc_qos_performance_av_pc_ComponentSpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_qos_performance_av_pc_ComponentSpecifiedExecutionTime", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
specifiedQoSAnnotations_QoSAnnotations607: BinaryAssociation = BinaryAssociation(
    name="specifiedQoSAnnotations_QoSAnnotations607",
    ends={
        Property(name="qosannotations_av_pc608", type=pcm_av_pc_qosannotations_av_pc_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="SpecifiedQoSAnnotation", type=SpecifiedQoSAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature_SpecifiedOutputParameterAbstraction609: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedOutputParameterAbstraction609",
    ends={
        Property(name="Signature610", type=pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedOutputParameterAbstraction611: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedOutputParameterAbstraction611",
    ends={
        Property(name="Role613", type=pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction612", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation625: BinaryAssociation = BinaryAssociation(
    name="externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation625",
    ends={
        Property(name="reliability_av_pc626", type=pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ExternalFailureOccurrenceDescription", type=ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expectedExternalOutputs_SpecifiedOutputParameterAbstraction614: BinaryAssociation = BinaryAssociation(
    name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction614",
    ends={
        Property(name="parameter_av_pc616", type=pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage615", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qosAnnotations_SpecifiedOutputParameterAbstraction617: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedOutputParameterAbstraction617",
    ends={
        Property(name="qosannotations_av_pc619", type=pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="QoSAnnotations618", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
qosAnnotations_System627: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_System627",
    ends={
        Property(name="qosannotations_av_pc629", type=pcm_av_pc_system_av_pc_System, multiplicity=Multiplicity(1, 1)),
        Property(name="QoSAnnotations628", type=QoSAnnotations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkingResources__ResourceEnvironment630: BinaryAssociation = BinaryAssociation(
    name="linkingResources__ResourceEnvironment630",
    ends={
        Property(name="resourceenvironment_av_pc631", type=pcm_av_pc_resourceenvironment_av_pc_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="LinkingResource", type=LinkingResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_ResourceEnvironment632: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ResourceEnvironment632",
    ends={
        Property(name="resourceenvironment_av_pc633", type=pcm_av_pc_resourceenvironment_av_pc_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectedResourceContainers_LinkingResource634: BinaryAssociation = BinaryAssociation(
    name="connectedResourceContainers_LinkingResource634",
    ends={
        Property(name="ResourceContainer635", type=pcm_av_pc_resourceenvironment_av_pc_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_resourceenvironment_av_pc_LinkingResource", type=ResourceContainer, multiplicity=Multiplicity(0, 9999))
    }
)
resourceEnvironment_ResourceContainer644: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_ResourceContainer644",
    ends={
        Property(name="resourceenvironment_av_pc646", type=pcm_av_pc_resourceenvironment_av_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceEnvironment645", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
nestedResourceContainers__ResourceContainer647: BinaryAssociation = BinaryAssociation(
    name="nestedResourceContainers__ResourceContainer647",
    ends={
        Property(name="resourceenvironment_av_pc649", type=pcm_av_pc_resourceenvironment_av_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer648", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentResourceContainer__ResourceContainer650: BinaryAssociation = BinaryAssociation(
    name="parentResourceContainer__ResourceContainer650",
    ends={
        Property(name="resourceenvironment_av_pc652", type=pcm_av_pc_resourceenvironment_av_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer651", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
schedulingPolicy653: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicy653",
    ends={
        Property(name="SchedulingPolicy654", type=pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification", type=SchedulingPolicy, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceType_ActiveResourceSpecification655: BinaryAssociation = BinaryAssociation(
    name="activeResourceType_ActiveResourceSpecification655",
    ends={
        Property(name="ProcessingResourceType657", type=pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification656", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
processingRate_ProcessingResourceSpecification658: BinaryAssociation = BinaryAssociation(
    name="processingRate_ProcessingResourceSpecification658",
    ends={
        Property(name="core_av_pc660", type=pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable659", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceContainer_ProcessingResourceSpecification661: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ProcessingResourceSpecification661",
    ends={
        Property(name="resourceenvironment_av_pc663", type=pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer662", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
linkingResource_CommunicationLinkResourceSpecification664: BinaryAssociation = BinaryAssociation(
    name="linkingResource_CommunicationLinkResourceSpecification664",
    ends={
        Property(name="resourceenvironment_av_pc666", type=pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="LinkingResource665", type=LinkingResource, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceType_CommunicationLinkResourceSpecification667: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType_CommunicationLinkResourceSpecification667",
    ends={
        Property(name="CommunicationLinkResourceType668", type=pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecifications_LinkingResource636: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifications_LinkingResource636",
    ends={
        Property(name="resourceenvironment_av_pc638", type=pcm_av_pc_resourceenvironment_av_pc_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceSpecification637", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceEnvironment_LinkingResource639: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_LinkingResource639",
    ends={
        Property(name="resourceenvironment_av_pc640", type=pcm_av_pc_resourceenvironment_av_pc_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceEnvironment", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceSpecifications_ResourceContainer641: BinaryAssociation = BinaryAssociation(
    name="activeResourceSpecifications_ResourceContainer641",
    ends={
        Property(name="resourceenvironment_av_pc643", type=pcm_av_pc_resourceenvironment_av_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcessingResourceSpecification642", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_AllocationContext675: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_AllocationContext675",
    ends={
        Property(name="ResourceContainer676", type=pcm_av_pc_allocation_av_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_allocation_av_pc_AllocationContext", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_AllocationContext677: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_AllocationContext677",
    ends={
        Property(name="composition_av_pc_AssemblyContext679", type=pcm_av_pc_allocation_av_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_allocation_av_pc_AllocationContext678", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
allocation_AllocationContext680: BinaryAssociation = BinaryAssociation(
    name="allocation_AllocationContext680",
    ends={
        Property(name="allocation_av_pc", type=pcm_av_pc_allocation_av_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="Allocation", type=Allocation, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__AllocationContext681: BinaryAssociation = BinaryAssociation(
    name="eventChannel__AllocationContext681",
    ends={
        Property(name="composition_av_pc_EventChannel", type=pcm_av_pc_allocation_av_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_allocation_av_pc_AllocationContext682", type=composition_av_pc_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
latency_CommunicationLinkResourceSpecification669: BinaryAssociation = BinaryAssociation(
    name="latency_CommunicationLinkResourceSpecification669",
    ends={
        Property(name="core_av_pc671", type=pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable670", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throughput_CommunicationLinkResourceSpecification672: BinaryAssociation = BinaryAssociation(
    name="throughput_CommunicationLinkResourceSpecification672",
    ends={
        Property(name="core_av_pc674", type=pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable673", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
completions_CompletionRepository690: BinaryAssociation = BinaryAssociation(
    name="completions_CompletionRepository690",
    ends={
        Property(name="Completion", type=pcm_av_pc_completions_av_pc_CompletionRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_completions_av_pc_CompletionRepository", type=Completion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCommunicationLinkResource_ParametricResourceDemand691: BinaryAssociation = BinaryAssociation(
    name="requiredCommunicationLinkResource_ParametricResourceDemand691",
    ends={
        Property(name="CommunicationLinkResourceType692", type=pcm_av_pc_completions_av_pc_NetworkDemandParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_completions_av_pc_NetworkDemandParametricResourceDemand", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
targetResourceEnvironment_Allocation683: BinaryAssociation = BinaryAssociation(
    name="targetResourceEnvironment_Allocation683",
    ends={
        Property(name="ResourceEnvironment684", type=pcm_av_pc_allocation_av_pc_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_allocation_av_pc_Allocation", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
system_Allocation685: BinaryAssociation = BinaryAssociation(
    name="system_Allocation685",
    ends={
        Property(name="System687", type=pcm_av_pc_allocation_av_pc_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_allocation_av_pc_Allocation686", type=System, multiplicity=Multiplicity(0, 1))
    }
)
allocationContexts_Allocation688: BinaryAssociation = BinaryAssociation(
    name="allocationContexts_Allocation688",
    ends={
        Property(name="allocation_av_pc689", type=pcm_av_pc_allocation_av_pc_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="AllocationContext", type=AllocationContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_pcm_av_pc_core_av_pc_PCMRandomVariable_RandomVariable = Generalization(general=RandomVariable, specific=pcm_av_pc_core_av_pc_PCMRandomVariable)
gen_pcm_av_pc_entity_av_pc_ResourceInterfaceRequiringEntity_Entity = Generalization(general=Entity, specific=pcm_av_pc_entity_av_pc_ResourceInterfaceRequiringEntity)
gen_pcm_av_pc_entity_av_pc_ResourceRequiredRole_Role = Generalization(general=Role, specific=pcm_av_pc_entity_av_pc_ResourceRequiredRole)
gen_pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingEntity)
gen_pcm_av_pc_entity_av_pc_ResourceProvidedRole_Role = Generalization(general=Role, specific=pcm_av_pc_entity_av_pc_ResourceProvidedRole)
gen_pcm_av_pc_entity_av_pc_InterfaceProvidingRequiringEntity_entity_av_pc_InterfaceProvidingEntity = Generalization(general=entity_av_pc_InterfaceProvidingEntity, specific=pcm_av_pc_entity_av_pc_InterfaceProvidingRequiringEntity)
gen_pcm_av_pc_entity_av_pc_InterfaceProvidingRequiringEntity_entity_av_pc_InterfaceRequiringEntity = Generalization(general=entity_av_pc_InterfaceRequiringEntity, specific=pcm_av_pc_entity_av_pc_InterfaceProvidingRequiringEntity)
gen_pcm_av_pc_entity_av_pc_InterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_av_pc_entity_av_pc_InterfaceProvidingEntity)
gen_pcm_av_pc_entity_av_pc_InterfaceRequiringEntity_entity_av_pc_Entity = Generalization(general=entity_av_pc_Entity, specific=pcm_av_pc_entity_av_pc_InterfaceRequiringEntity)
gen_pcm_av_pc_entity_av_pc_InterfaceRequiringEntity_entity_av_pc_ResourceInterfaceRequiringEntity = Generalization(general=entity_av_pc_ResourceInterfaceRequiringEntity, specific=pcm_av_pc_entity_av_pc_InterfaceRequiringEntity)
gen_pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity_composition_av_pc_ComposedStructure = Generalization(general=composition_av_pc_ComposedStructure, specific=pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity)
gen_pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity_entity_av_pc_InterfaceProvidingRequiringEntity = Generalization(general=entity_av_pc_InterfaceProvidingRequiringEntity, specific=pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity)
gen_pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingRequiringEntity_entity_av_pc_ResourceInterfaceRequiringEntity = Generalization(general=entity_av_pc_ResourceInterfaceRequiringEntity, specific=pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingRequiringEntity_entity_av_pc_ResourceInterfaceProvidingEntity = Generalization(general=entity_av_pc_ResourceInterfaceProvidingEntity, specific=pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_av_pc_entity_av_pc_Entity_Identifier = Generalization(general=Identifier, specific=pcm_av_pc_entity_av_pc_Entity)
gen_pcm_av_pc_entity_av_pc_Entity_entity_av_pc_NamedElement = Generalization(general=entity_av_pc_NamedElement, specific=pcm_av_pc_entity_av_pc_Entity)
gen_pcm_av_pc_composition_av_pc_DelegationConnector_Connector = Generalization(general=Connector, specific=pcm_av_pc_composition_av_pc_DelegationConnector)
gen_pcm_av_pc_composition_av_pc_Connector_Entity = Generalization(general=Entity, specific=pcm_av_pc_composition_av_pc_Connector)
gen_pcm_av_pc_composition_av_pc_ComposedStructure_Entity = Generalization(general=Entity, specific=pcm_av_pc_composition_av_pc_ComposedStructure)
gen_pcm_av_pc_composition_av_pc_EventChannelSourceConnector_Connector = Generalization(general=Connector, specific=pcm_av_pc_composition_av_pc_EventChannelSourceConnector)
gen_pcm_av_pc_composition_av_pc_EventChannelSinkConnector_Connector = Generalization(general=Connector, specific=pcm_av_pc_composition_av_pc_EventChannelSinkConnector)
gen_pcm_av_pc_composition_av_pc_ProvidedDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_pc_composition_av_pc_ProvidedDelegationConnector)
gen_pcm_av_pc_composition_av_pc_EventChannel_Entity = Generalization(general=Entity, specific=pcm_av_pc_composition_av_pc_EventChannel)
gen_pcm_av_pc_composition_av_pc_RequiredDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_pc_composition_av_pc_RequiredDelegationConnector)
gen_pcm_av_pc_composition_av_pc_AssemblyEventConnector_Connector = Generalization(general=Connector, specific=pcm_av_pc_composition_av_pc_AssemblyEventConnector)
gen_pcm_av_pc_composition_av_pc_SourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_pc_composition_av_pc_SourceDelegationConnector)
gen_pcm_av_pc_composition_av_pc_AssemblyConnector_Connector = Generalization(general=Connector, specific=pcm_av_pc_composition_av_pc_AssemblyConnector)
gen_pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector)
gen_pcm_av_pc_composition_av_pc_AssemblyContext_Entity = Generalization(general=Entity, specific=pcm_av_pc_composition_av_pc_AssemblyContext)
gen_pcm_av_pc_composition_av_pc_SinkDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_pc_composition_av_pc_SinkDelegationConnector)
gen_pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector_Connector = Generalization(general=Connector, specific=pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector)
gen_pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector)
gen_pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector)
gen_pcm_av_pc_usagemodel_av_pc_UsageScenario_Entity = Generalization(general=Entity, specific=pcm_av_pc_usagemodel_av_pc_UsageScenario)
gen_pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall)
gen_pcm_av_pc_usagemodel_av_pc_AbstractUserAction_Entity = Generalization(general=Entity, specific=pcm_av_pc_usagemodel_av_pc_AbstractUserAction)
gen_pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour_Entity = Generalization(general=Entity, specific=pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour)
gen_pcm_av_pc_usagemodel_av_pc_Start_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_pc_usagemodel_av_pc_Start)
gen_pcm_av_pc_usagemodel_av_pc_OpenWorkload_Workload = Generalization(general=Workload, specific=pcm_av_pc_usagemodel_av_pc_OpenWorkload)
gen_pcm_av_pc_usagemodel_av_pc_Branch_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_pc_usagemodel_av_pc_Branch)
gen_pcm_av_pc_usagemodel_av_pc_Loop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_pc_usagemodel_av_pc_Loop)
gen_pcm_av_pc_usagemodel_av_pc_Stop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_pc_usagemodel_av_pc_Stop)
gen_pcm_av_pc_repository_av_pc_PassiveResource_Entity = Generalization(general=Entity, specific=pcm_av_pc_repository_av_pc_PassiveResource)
gen_pcm_av_pc_repository_av_pc_BasicComponent_ImplementationComponentType = Generalization(general=ImplementationComponentType, specific=pcm_av_pc_repository_av_pc_BasicComponent)
gen_pcm_av_pc_usagemodel_av_pc_Delay_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_pc_usagemodel_av_pc_Delay)
gen_pcm_av_pc_usagemodel_av_pc_ClosedWorkload_Workload = Generalization(general=Workload, specific=pcm_av_pc_usagemodel_av_pc_ClosedWorkload)
gen_pcm_av_pc_repository_av_pc_ImplementationComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_av_pc_repository_av_pc_ImplementationComponentType)
gen_pcm_av_pc_repository_av_pc_Repository_Entity = Generalization(general=Entity, specific=pcm_av_pc_repository_av_pc_Repository)
gen_pcm_av_pc_repository_av_pc_RepositoryComponent_InterfaceProvidingRequiringEntity = Generalization(general=InterfaceProvidingRequiringEntity, specific=pcm_av_pc_repository_av_pc_RepositoryComponent)
gen_pcm_av_pc_repository_av_pc_ProvidedRole_Role = Generalization(general=Role, specific=pcm_av_pc_repository_av_pc_ProvidedRole)
gen_pcm_av_pc_repository_av_pc_InfrastructureRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_av_pc_repository_av_pc_InfrastructureRequiredRole)
gen_pcm_av_pc_repository_av_pc_Interface_Entity = Generalization(general=Entity, specific=pcm_av_pc_repository_av_pc_Interface)
gen_pcm_av_pc_repository_av_pc_RequiredRole_Role = Generalization(general=Role, specific=pcm_av_pc_repository_av_pc_RequiredRole)
gen_pcm_av_pc_repository_av_pc_OperationSignature_Signature = Generalization(general=Signature, specific=pcm_av_pc_repository_av_pc_OperationSignature)
gen_pcm_av_pc_repository_av_pc_EventGroup_Interface = Generalization(general=Interface, specific=pcm_av_pc_repository_av_pc_EventGroup)
gen_pcm_av_pc_repository_av_pc_EventType_Signature = Generalization(general=Signature, specific=pcm_av_pc_repository_av_pc_EventType)
gen_pcm_av_pc_repository_av_pc_Signature_Entity = Generalization(general=Entity, specific=pcm_av_pc_repository_av_pc_Signature)
gen_pcm_av_pc_repository_av_pc_InfrastructureSignature_Signature = Generalization(general=Signature, specific=pcm_av_pc_repository_av_pc_InfrastructureSignature)
gen_pcm_av_pc_repository_av_pc_InfrastructureInterface_Interface = Generalization(general=Interface, specific=pcm_av_pc_repository_av_pc_InfrastructureInterface)
gen_pcm_av_pc_repository_av_pc_OperationInterface_Interface = Generalization(general=Interface, specific=pcm_av_pc_repository_av_pc_OperationInterface)
gen_pcm_av_pc_repository_av_pc_InfrastructureProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_av_pc_repository_av_pc_InfrastructureProvidedRole)
gen_pcm_av_pc_repository_av_pc_CompleteComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_av_pc_repository_av_pc_CompleteComponentType)
gen_pcm_av_pc_repository_av_pc_OperationRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_av_pc_repository_av_pc_OperationRequiredRole)
gen_pcm_av_pc_repository_av_pc_SourceRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_av_pc_repository_av_pc_SourceRole)
gen_pcm_av_pc_repository_av_pc_SinkRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_av_pc_repository_av_pc_SinkRole)
gen_pcm_av_pc_repository_av_pc_OperationProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_av_pc_repository_av_pc_OperationProvidedRole)
gen_pcm_av_pc_repository_av_pc_CompositeComponent_entity_av_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_av_pc_ComposedProvidingRequiringEntity, specific=pcm_av_pc_repository_av_pc_CompositeComponent)
gen_pcm_av_pc_repository_av_pc_CompositeComponent_repository_av_pc_ImplementationComponentType = Generalization(general=repository_av_pc_ImplementationComponentType, specific=pcm_av_pc_repository_av_pc_CompositeComponent)
gen_pcm_av_pc_repository_av_pc_PrimitiveDataType_DataType = Generalization(general=DataType, specific=pcm_av_pc_repository_av_pc_PrimitiveDataType)
gen_pcm_av_pc_repository_av_pc_CollectionDataType_entity_av_pc_Entity = Generalization(general=entity_av_pc_Entity, specific=pcm_av_pc_repository_av_pc_CollectionDataType)
gen_pcm_av_pc_repository_av_pc_CollectionDataType_repository_av_pc_DataType = Generalization(general=repository_av_pc_DataType, specific=pcm_av_pc_repository_av_pc_CollectionDataType)
gen_pcm_av_pc_repository_av_pc_ProvidesComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_av_pc_repository_av_pc_ProvidesComponentType)
gen_pcm_av_pc_repository_av_pc_InnerDeclaration_NamedElement = Generalization(general=NamedElement, specific=pcm_av_pc_repository_av_pc_InnerDeclaration)
gen_pcm_av_pc_repository_av_pc_Role_Entity = Generalization(general=Entity, specific=pcm_av_pc_repository_av_pc_Role)
gen_pcm_av_pc_resourcetype_av_pc_ResourceSignature_Entity = Generalization(general=Entity, specific=pcm_av_pc_resourcetype_av_pc_ResourceSignature)
gen_pcm_av_pc_resourcetype_av_pc_ProcessingResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_av_pc_resourcetype_av_pc_ProcessingResourceType)
gen_pcm_av_pc_resourcetype_av_pc_ResourceType_entity_av_pc_Entity = Generalization(general=entity_av_pc_Entity, specific=pcm_av_pc_resourcetype_av_pc_ResourceType)
gen_pcm_av_pc_resourcetype_av_pc_ResourceType_UnitCarryingElement = Generalization(general=UnitCarryingElement, specific=pcm_av_pc_resourcetype_av_pc_ResourceType)
gen_pcm_av_pc_resourcetype_av_pc_ResourceType_entity_av_pc_ResourceInterfaceProvidingEntity = Generalization(general=entity_av_pc_ResourceInterfaceProvidingEntity, specific=pcm_av_pc_resourcetype_av_pc_ResourceType)
gen_pcm_av_pc_repository_av_pc_CompositeDataType_entity_av_pc_Entity = Generalization(general=entity_av_pc_Entity, specific=pcm_av_pc_repository_av_pc_CompositeDataType)
gen_pcm_av_pc_repository_av_pc_CompositeDataType_repository_av_pc_DataType = Generalization(general=repository_av_pc_DataType, specific=pcm_av_pc_repository_av_pc_CompositeDataType)
gen_pcm_av_pc_resourcetype_av_pc_CommunicationLinkResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_av_pc_resourcetype_av_pc_CommunicationLinkResourceType)
gen_pcm_av_pc_resourcetype_av_pc_ResourceInterface_Entity = Generalization(general=Entity, specific=pcm_av_pc_resourcetype_av_pc_ResourceInterface)
gen_pcm_av_pc_resourcetype_av_pc_SchedulingPolicy_Entity = Generalization(general=Entity, specific=pcm_av_pc_resourcetype_av_pc_SchedulingPolicy)
gen_pcm_av_pc_parameter_av_pc_CharacterisedVariable_Variable = Generalization(general=Variable, specific=pcm_av_pc_parameter_av_pc_CharacterisedVariable)
gen_pcm_av_pc_reliability_av_pc_HardwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_av_pc_reliability_av_pc_HardwareInducedFailureType)
gen_pcm_av_pc_reliability_av_pc_NetworkInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_av_pc_reliability_av_pc_NetworkInducedFailureType)
gen_pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription)
gen_pcm_av_pc_reliability_av_pc_SoftwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_av_pc_reliability_av_pc_SoftwareInducedFailureType)
gen_pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription)
gen_pcm_av_pc_seff_av_pc_AbstractInternalControlFlowAction_AbstractAction = Generalization(general=AbstractAction, specific=pcm_av_pc_seff_av_pc_AbstractInternalControlFlowAction)
gen_pcm_av_pc_seff_av_pc_AbstractAction_Entity = Generalization(general=Entity, specific=pcm_av_pc_seff_av_pc_AbstractAction)
gen_pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour_Identifier = Generalization(general=Identifier, specific=pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour)
gen_pcm_av_pc_reliability_av_pc_ResourceTimeoutFailureType_SoftwareInducedFailureType = Generalization(general=SoftwareInducedFailureType, specific=pcm_av_pc_reliability_av_pc_ResourceTimeoutFailureType)
gen_pcm_av_pc_reliability_av_pc_FailureType_Entity = Generalization(general=Entity, specific=pcm_av_pc_reliability_av_pc_FailureType)
gen_pcm_av_pc_seff_av_pc_StopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_av_pc_StopAction)
gen_pcm_av_pc_seff_av_pc_AbstractLoopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_av_pc_AbstractLoopAction)
gen_pcm_av_pc_seff_av_pc_AbstractBranchTransition_Entity = Generalization(general=Entity, specific=pcm_av_pc_seff_av_pc_AbstractBranchTransition)
gen_pcm_av_pc_seff_av_pc_BranchAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_av_pc_BranchAction)
gen_pcm_av_pc_seff_av_pc_ResourceDemandingSEFF_Identifier = Generalization(general=Identifier, specific=pcm_av_pc_seff_av_pc_ResourceDemandingSEFF)
gen_pcm_av_pc_seff_av_pc_ResourceDemandingSEFF_seff_av_pc_ServiceEffectSpecification = Generalization(general=seff_av_pc_ServiceEffectSpecification, specific=pcm_av_pc_seff_av_pc_ResourceDemandingSEFF)
gen_pcm_av_pc_seff_av_pc_ResourceDemandingSEFF_seff_av_pc_ResourceDemandingBehaviour = Generalization(general=seff_av_pc_ResourceDemandingBehaviour, specific=pcm_av_pc_seff_av_pc_ResourceDemandingSEFF)
gen_pcm_av_pc_seff_av_pc_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_av_pc_seff_av_pc_ResourceDemandingInternalBehaviour)
gen_pcm_av_pc_seff_av_pc_ReleaseAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_av_pc_ReleaseAction)
gen_pcm_av_pc_seff_av_pc_StartAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_av_pc_StartAction)
gen_pcm_av_pc_seff_av_pc_LoopAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_av_pc_seff_av_pc_LoopAction)
gen_pcm_av_pc_seff_av_pc_ForkAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_av_pc_ForkAction)
gen_pcm_av_pc_seff_av_pc_ForkedBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_av_pc_seff_av_pc_ForkedBehaviour)
gen_pcm_av_pc_seff_av_pc_CallReturnAction_CallAction = Generalization(general=CallAction, specific=pcm_av_pc_seff_av_pc_CallReturnAction)
gen_pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition)
gen_pcm_av_pc_seff_av_pc_AcquireAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_av_pc_AcquireAction)
gen_pcm_av_pc_seff_av_pc_ExternalCallAction_seff_av_pc_AbstractAction = Generalization(general=seff_av_pc_AbstractAction, specific=pcm_av_pc_seff_av_pc_ExternalCallAction)
gen_pcm_av_pc_seff_av_pc_ExternalCallAction_seff_av_pc_CallReturnAction = Generalization(general=seff_av_pc_CallReturnAction, specific=pcm_av_pc_seff_av_pc_ExternalCallAction)
gen_pcm_av_pc_seff_av_pc_ExternalCallAction_seff_reliability_av_pc_FailureHandlingEntity = Generalization(general=seff_reliability_av_pc_FailureHandlingEntity, specific=pcm_av_pc_seff_av_pc_ExternalCallAction)
gen_pcm_av_pc_seff_av_pc_EmitEventAction_seff_av_pc_AbstractAction = Generalization(general=seff_av_pc_AbstractAction, specific=pcm_av_pc_seff_av_pc_EmitEventAction)
gen_pcm_av_pc_seff_av_pc_EmitEventAction_seff_av_pc_CallAction = Generalization(general=seff_av_pc_CallAction, specific=pcm_av_pc_seff_av_pc_EmitEventAction)
gen_pcm_av_pc_seff_av_pc_InternalAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_av_pc_InternalAction)
gen_pcm_av_pc_seff_performance_av_pc_InfrastructureCall_CallAction = Generalization(general=CallAction, specific=pcm_av_pc_seff_performance_av_pc_InfrastructureCall)
gen_pcm_av_pc_seff_av_pc_CollectionIteratorAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_av_pc_seff_av_pc_CollectionIteratorAction)
gen_pcm_av_pc_seff_av_pc_GuardedBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_av_pc_seff_av_pc_GuardedBranchTransition)
gen_pcm_av_pc_seff_av_pc_SetVariableAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_av_pc_SetVariableAction)
gen_pcm_av_pc_seff_av_pc_InternalCallAction_seff_av_pc_CallAction = Generalization(general=seff_av_pc_CallAction, specific=pcm_av_pc_seff_av_pc_InternalCallAction)
gen_pcm_av_pc_seff_av_pc_InternalCallAction_seff_av_pc_AbstractInternalControlFlowAction = Generalization(general=seff_av_pc_AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_av_pc_InternalCallAction)
gen_pcm_av_pc_seff_performance_av_pc_ResourceCall_CallAction = Generalization(general=CallAction, specific=pcm_av_pc_seff_performance_av_pc_ResourceCall)
gen_pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour_seff_reliability_av_pc_FailureHandlingEntity = Generalization(general=seff_reliability_av_pc_FailureHandlingEntity, specific=pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour)
gen_pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour_seff_av_pc_ResourceDemandingBehaviour = Generalization(general=seff_av_pc_ResourceDemandingBehaviour, specific=pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour)
gen_pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity_Entity = Generalization(general=Entity, specific=pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity)
gen_pcm_av_pc_qosannotations_av_pc_QoSAnnotations_Entity = Generalization(general=Entity, specific=pcm_av_pc_qosannotations_av_pc_QoSAnnotations)
gen_pcm_av_pc_seff_reliability_av_pc_RecoveryAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_reliability_av_pc_RecoveryAction)
gen_pcm_av_pc_qos_performance_av_pc_SystemSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_av_pc_qos_performance_av_pc_SystemSpecifiedExecutionTime)
gen_pcm_av_pc_qos_performance_av_pc_SpecifiedExecutionTime_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_av_pc_qos_performance_av_pc_SpecifiedExecutionTime)
gen_pcm_av_pc_qos_performance_av_pc_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_av_pc_qos_performance_av_pc_ComponentSpecifiedExecutionTime)
gen_pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation)
gen_pcm_av_pc_system_av_pc_System_entity_av_pc_Entity = Generalization(general=entity_av_pc_Entity, specific=pcm_av_pc_system_av_pc_System)
gen_pcm_av_pc_system_av_pc_System_entity_av_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_av_pc_ComposedProvidingRequiringEntity, specific=pcm_av_pc_system_av_pc_System)
gen_pcm_av_pc_resourceenvironment_av_pc_ResourceEnvironment_NamedElement = Generalization(general=NamedElement, specific=pcm_av_pc_resourceenvironment_av_pc_ResourceEnvironment)
gen_pcm_av_pc_resourceenvironment_av_pc_LinkingResource_Entity = Generalization(general=Entity, specific=pcm_av_pc_resourceenvironment_av_pc_LinkingResource)
gen_pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification)
gen_pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification)
gen_pcm_av_pc_resourceenvironment_av_pc_ResourceContainer_Entity = Generalization(general=Entity, specific=pcm_av_pc_resourceenvironment_av_pc_ResourceContainer)
gen_pcm_av_pc_allocation_av_pc_AllocationContext_Entity = Generalization(general=Entity, specific=pcm_av_pc_allocation_av_pc_AllocationContext)
gen_pcm_av_pc_allocation_av_pc_Allocation_Entity = Generalization(general=Entity, specific=pcm_av_pc_allocation_av_pc_Allocation)
gen_pcm_av_pc_completions_av_pc_Completion_entity_av_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_av_pc_ComposedProvidingRequiringEntity, specific=pcm_av_pc_completions_av_pc_Completion)
gen_pcm_av_pc_completions_av_pc_Completion_repository_av_pc_ImplementationComponentType = Generalization(general=repository_av_pc_ImplementationComponentType, specific=pcm_av_pc_completions_av_pc_Completion)
gen_pcm_av_pc_completions_av_pc_DelegatingExternalCallAction_ExternalCallAction = Generalization(general=ExternalCallAction, specific=pcm_av_pc_completions_av_pc_DelegatingExternalCallAction)
gen_pcm_av_pc_completions_av_pc_NetworkDemandParametricResourceDemand_ParametricResourceDemand = Generalization(general=ParametricResourceDemand, specific=pcm_av_pc_completions_av_pc_NetworkDemandParametricResourceDemand)
gen_pcm_av_pc_subsystem_av_pc_SubSystem_entity_av_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_av_pc_ComposedProvidingRequiringEntity, specific=pcm_av_pc_subsystem_av_pc_SubSystem)
gen_pcm_av_pc_subsystem_av_pc_SubSystem_repository_av_pc_RepositoryComponent = Generalization(general=repository_av_pc_RepositoryComponent, specific=pcm_av_pc_subsystem_av_pc_SubSystem)

# Domain Model
domain_model = DomainModel(
    name="pcm_av_pc",
    types={pcm_av_pc_DummyClass, pcm_av_pc_Advice, pcm_av_pc_EObject, pcm_av_pc_GlobalScope, pcm_av_pc_PerJoinPointScope, pcm_av_pc_Pointcut, pcm_av_pc_core_av_pc_PCMRandomVariable, RandomVariable, pcm_av_pc_entity_av_pc_ResourceInterfaceRequiringEntity, seff_performance_av_pc_ResourceCall, entity_av_pc_ResourceRequiredRole, pcm_av_pc_entity_av_pc_ResourceRequiredRole, seff_performance_av_pc_ParametricResourceDemand, LoopAction, GuardedBranchTransition, pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingEntity, qos_performance_av_pc_SpecifiedExecutionTime, entity_av_pc_ResourceProvidedRole, composition_av_pc_EventChannelSinkConnector, composition_av_pc_AssemblyEventConnector, Loop, OpenWorkload, Delay, CommunicationLinkResourceSpecification, ProcessingResourceSpecification, pcm_av_pc_entity_av_pc_ResourceProvidedRole, Role, entity_av_pc_ResourceInterfaceProvidingEntity, ResourceInterface, pcm_av_pc_entity_av_pc_InterfaceProvidingRequiringEntity, entity_av_pc_InterfaceProvidingEntity, entity_av_pc_InterfaceRequiringEntity, ClosedWorkload, pcm_av_pc_entity_av_pc_InterfaceProvidingEntity, Entity, PassiveResource, ProvidedRole, VariableCharacterisation, pcm_av_pc_entity_av_pc_InterfaceRequiringEntity, entity_av_pc_Entity, entity_av_pc_ResourceInterfaceRequiringEntity, seff_performance_av_pc_InfrastructureCall, RequiredRole, composition_av_pc_AssemblyContext, composition_av_pc_ResourceRequiredDelegationConnector, pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity, composition_av_pc_ComposedStructure, entity_av_pc_InterfaceProvidingRequiringEntity, composition_av_pc_EventChannel, composition_av_pc_Connector, pcm_av_pc_entity_av_pc_NamedElement, pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingRequiringEntity, pcm_av_pc_entity_av_pc_Entity, Identifier, entity_av_pc_NamedElement, pcm_av_pc_composition_av_pc_DelegationConnector, Connector, pcm_av_pc_composition_av_pc_Connector, pcm_av_pc_composition_av_pc_ComposedStructure, pcm_av_pc_composition_av_pc_EventChannelSourceConnector, SourceRole, pcm_av_pc_composition_av_pc_EventChannelSinkConnector, SinkRole, PCMRandomVariable, pcm_av_pc_composition_av_pc_ProvidedDelegationConnector, DelegationConnector, pcm_av_pc_composition_av_pc_ResourceRequiredDelegationConnector, pcm_av_pc_composition_av_pc_EventChannel, EventGroup, composition_av_pc_EventChannelSourceConnector, OperationRequiredRole, OperationProvidedRole, pcm_av_pc_composition_av_pc_RequiredDelegationConnector, pcm_av_pc_composition_av_pc_AssemblyEventConnector, pcm_av_pc_composition_av_pc_SourceDelegationConnector, pcm_av_pc_composition_av_pc_AssemblyConnector, pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector, pcm_av_pc_composition_av_pc_AssemblyContext, RepositoryComponent, VariableUsage, pcm_av_pc_composition_av_pc_SinkDelegationConnector, pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector, InfrastructureProvidedRole, InfrastructureRequiredRole, pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector, pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector, OperationSignature, pcm_av_pc_usagemodel_av_pc_Workload, UsageScenario, pcm_av_pc_usagemodel_av_pc_UsageScenario, UsageModel, ScenarioBehaviour, Workload, pcm_av_pc_usagemodel_av_pc_UserData, pcm_av_pc_usagemodel_av_pc_UsageModel, UserData, pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall, AbstractUserAction, BranchTransition, pcm_av_pc_usagemodel_av_pc_AbstractUserAction, pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour, pcm_av_pc_usagemodel_av_pc_Start, pcm_av_pc_usagemodel_av_pc_OpenWorkload, pcm_av_pc_usagemodel_av_pc_BranchTransition, Branch, pcm_av_pc_usagemodel_av_pc_Branch, pcm_av_pc_usagemodel_av_pc_Loop, pcm_av_pc_usagemodel_av_pc_Stop, pcm_av_pc_repository_av_pc_PassiveResource, BasicComponent, ResourceTimeoutFailureType, pcm_av_pc_repository_av_pc_BasicComponent, ImplementationComponentType, pcm_av_pc_usagemodel_av_pc_Delay, pcm_av_pc_usagemodel_av_pc_ClosedWorkload, CompleteComponentType, ServiceEffectSpecification, pcm_av_pc_repository_av_pc_ImplementationComponentType, ResourceSignature, pcm_av_pc_repository_av_pc_DataType, pcm_av_pc_repository_av_pc_Repository, Interface, FailureType, pcm_av_pc_repository_av_pc_RepositoryComponent, InterfaceProvidingRequiringEntity, Repository, pcm_av_pc_repository_av_pc_ProvidedRole, pcm_av_pc_repository_av_pc_Parameter, DataType, InfrastructureSignature, EventType, RequiredCharacterisation, pcm_av_pc_repository_av_pc_InfrastructureRequiredRole, pcm_av_pc_repository_av_pc_Interface, pcm_av_pc_repository_av_pc_RequiredRole, pcm_av_pc_repository_av_pc_RequiredCharacterisation, pcm_av_pc_repository_av_pc_OperationSignature, Parameter_, pcm_av_pc_repository_av_pc_EventGroup, Protocol, pcm_av_pc_repository_av_pc_EventType, Signature, pcm_av_pc_repository_av_pc_Signature, ExceptionType, pcm_av_pc_repository_av_pc_ExceptionType, pcm_av_pc_repository_av_pc_InfrastructureSignature, InfrastructureInterface, pcm_av_pc_repository_av_pc_InfrastructureInterface, pcm_av_pc_repository_av_pc_OperationInterface, OperationInterface, pcm_av_pc_repository_av_pc_InfrastructureProvidedRole, pcm_av_pc_repository_av_pc_CompleteComponentType, ProvidesComponentType, pcm_av_pc_repository_av_pc_OperationRequiredRole, pcm_av_pc_repository_av_pc_SourceRole, pcm_av_pc_repository_av_pc_SinkRole, pcm_av_pc_repository_av_pc_OperationProvidedRole, pcm_av_pc_repository_av_pc_CompositeComponent, entity_av_pc_ComposedProvidingRequiringEntity, repository_av_pc_ImplementationComponentType, pcm_av_pc_repository_av_pc_PrimitiveDataType, pcm_av_pc_repository_av_pc_CollectionDataType, repository_av_pc_DataType, pcm_av_pc_repository_av_pc_ProvidesComponentType, InnerDeclaration, pcm_av_pc_repository_av_pc_InnerDeclaration, NamedElement, pcm_av_pc_repository_av_pc_Role, pcm_av_pc_resourcetype_av_pc_ResourceSignature, pcm_av_pc_resourcetype_av_pc_ProcessingResourceType, ResourceType, HardwareInducedFailureType, pcm_av_pc_resourcetype_av_pc_ResourceType, UnitCarryingElement, ResourceRepository, pcm_av_pc_resourcetype_av_pc_ResourceRepository, pcm_av_pc_repository_av_pc_CompositeDataType, CompositeDataType, pcm_av_pc_resourcetype_av_pc_CommunicationLinkResourceType, NetworkInducedFailureType, pcm_av_pc_resourcetype_av_pc_ResourceInterface, pcm_av_pc_protocol_av_pc_Protocol, pcm_av_pc_parameter_av_pc_VariableUsage, CallAction, SynchronisationPoint, CallReturnAction, SetVariableAction, SpecifiedOutputParameterAbstraction, SchedulingPolicy, pcm_av_pc_resourcetype_av_pc_SchedulingPolicy, pcm_av_pc_parameter_av_pc_CharacterisedVariable, Variable, pcm_av_pc_reliability_av_pc_FailureOccurrenceDescription, pcm_av_pc_reliability_av_pc_HardwareInducedFailureType, EntryLevelSystemCall, parameter_av_pc_pcm_av_pc_AbstractNamedReference, pcm_av_pc_parameter_av_pc_VariableCharacterisation, InternalAction, SoftwareInducedFailureType, pcm_av_pc_reliability_av_pc_NetworkInducedFailureType, CommunicationLinkResourceType, pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription, qos_reliability_av_pc_SpecifiedReliabilityAnnotation, ProcessingResourceType, pcm_av_pc_reliability_av_pc_SoftwareInducedFailureType, InternalFailureOccurrenceDescription, pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription, FailureOccurrenceDescription, pcm_av_pc_seff_av_pc_AbstractInternalControlFlowAction, AbstractAction, pcm_av_pc_seff_av_pc_AbstractAction, ResourceDemandingBehaviour, pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour, pcm_av_pc_reliability_av_pc_ResourceTimeoutFailureType, pcm_av_pc_reliability_av_pc_FailureType, pcm_av_pc_seff_av_pc_StopAction, AbstractInternalControlFlowAction, AbstractLoopAction, AbstractBranchTransition, pcm_av_pc_seff_av_pc_AbstractLoopAction, pcm_av_pc_seff_av_pc_AbstractBranchTransition, BranchAction, pcm_av_pc_seff_av_pc_BranchAction, pcm_av_pc_seff_av_pc_ServiceEffectSpecification, pcm_av_pc_seff_av_pc_ResourceDemandingSEFF, seff_av_pc_ServiceEffectSpecification, seff_av_pc_ResourceDemandingBehaviour, ResourceDemandingInternalBehaviour, pcm_av_pc_seff_av_pc_ResourceDemandingInternalBehaviour, ResourceDemandingSEFF, pcm_av_pc_seff_av_pc_ReleaseAction, pcm_av_pc_seff_av_pc_CallAction, pcm_av_pc_seff_av_pc_StartAction, pcm_av_pc_seff_av_pc_LoopAction, pcm_av_pc_seff_av_pc_ForkAction, ForkedBehaviour, pcm_av_pc_seff_av_pc_ForkedBehaviour, ForkAction, pcm_av_pc_seff_av_pc_SynchronisationPoint, pcm_av_pc_seff_av_pc_CallReturnAction, pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition, pcm_av_pc_seff_av_pc_AcquireAction, pcm_av_pc_seff_av_pc_ExternalCallAction, seff_av_pc_AbstractAction, seff_av_pc_CallReturnAction, seff_reliability_av_pc_FailureHandlingEntity, pcm_av_pc_seff_av_pc_EmitEventAction, pcm_av_pc_seff_av_pc_InternalAction, pcm_av_pc_seff_performance_av_pc_InfrastructureCall, pcm_av_pc_seff_av_pc_CollectionIteratorAction, pcm_av_pc_seff_av_pc_GuardedBranchTransition, pcm_av_pc_seff_av_pc_SetVariableAction, pcm_av_pc_seff_av_pc_InternalCallAction, seff_av_pc_CallAction, seff_av_pc_AbstractInternalControlFlowAction, pcm_av_pc_seff_performance_av_pc_ResourceCall, pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour, pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand, pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity, pcm_av_pc_qosannotations_av_pc_SpecifiedQoSAnnotation, QoSAnnotations, pcm_av_pc_qosannotations_av_pc_QoSAnnotations, System, SpecifiedQoSAnnotation, seff_reliability_av_pc_RecoveryActionBehaviour, seff_reliability_av_pc_RecoveryAction, pcm_av_pc_seff_reliability_av_pc_RecoveryAction, pcm_av_pc_qos_performance_av_pc_SystemSpecifiedExecutionTime, SpecifiedExecutionTime, pcm_av_pc_qos_performance_av_pc_SpecifiedExecutionTime, pcm_av_pc_qos_performance_av_pc_ComponentSpecifiedExecutionTime, pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation, pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction, ExternalFailureOccurrenceDescription, pcm_av_pc_system_av_pc_System, pcm_av_pc_resourceenvironment_av_pc_ResourceEnvironment, LinkingResource, ResourceContainer, pcm_av_pc_resourceenvironment_av_pc_LinkingResource, pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification, pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification, ResourceEnvironment, pcm_av_pc_resourceenvironment_av_pc_ResourceContainer, pcm_av_pc_allocation_av_pc_AllocationContext, Allocation, pcm_av_pc_allocation_av_pc_Allocation, pcm_av_pc_completions_av_pc_Completion, pcm_av_pc_completions_av_pc_CompletionRepository, Completion, pcm_av_pc_completions_av_pc_DelegatingExternalCallAction, ExternalCallAction, pcm_av_pc_completions_av_pc_NetworkDemandParametricResourceDemand, ParametricResourceDemand, AllocationContext, pcm_av_pc_subsystem_av_pc_SubSystem, repository_av_pc_RepositoryComponent, ParameterModifier, PrimitiveTypeEnum, ComponentType, VariableCharacterisationType},
    associations={children0, scopedObject1, scopedObject3, children5, requiredRoles_InterfaceRequiringEntity43, resourceCall__PCMRandomVariable11, resourceRequiredRoles__ResourceInterfaceRequiringEntity45, parametricResourceDemand_PCMRandomVariable14, loopAction_PCMRandomVariable17, requiredResourceInterface__ResourceRequiredRole48, resourceInterfaceRequiringEntity__ResourceRequiredRole50, guardedBranchTransition_PCMRandomVariable19, specifiedExecutionTime_PCMRandomVariable21, resourceProvidedRoles__ResourceInterfaceProvidingEntity53, eventChannelSinkConnector__FilterCondition22, assemblyEventConnector__FilterCondition23, loop_LoopIteration26, openWorkload_PCMRandomVariable28, delay_TimeSpecification30, communicationLinkResourceSpecifcation_throughput_PCMRandomVariable32, processingResourceSpecification_processingRate_PCMRandomVariable33, communicationLinkResourceSpecification_latency_PCMRandomVariable35, resourceInterfaceProvidingEntity__ResourceProvidedRole38, providedResourceInterface__ResourceProvidedRole40, closedWorkload_PCMRandomVariable7, passiveResource_capacity_PCMRandomVariable8, providedRoles_InterfaceProvidingEntity41, variableCharacterisation_Specification9, infrastructureCall__PCMRandomVariable10, assemblyContexts__ComposedStructure59, resourceRequiredDelegationConnectors_ComposedStructure62, eventChannel__ComposedStructure65, connectors__ComposedStructure68, parentStructure__Connector56, parentStructure__EventChannel85, sourceRole__EventChannelSourceRole88, assemblyContext__EventChannelSourceConnector89, eventChannel__EventChannelSourceConnector91, sinkRole__EventChannelSinkConnector94, filterCondition__EventChannelSinkConnector95, assemblyContext__EventChannelSinkConnector97, eventChannel__EventChannelSinkConnector100, innerResourceRequiredRole_ResourceRequiredDelegationConnector71, outerResourceRequiredRole_ResourceRequiredDelegationConnector72, parentStructure_ResourceRequiredDelegationConnector75, eventGroup__EventChannel78, eventChannelSourceConnector__EventChannel79, eventChannelSinkConnector__EventChannel82, innerRequiredRole_RequiredDelegationConnector110, outerRequiredRole_RequiredDelegationConnector111, assemblyContext_RequiredDelegationConnector114, innerProvidedRole_ProvidedDelegationConnector103, outerProvidedRole_ProvidedDelegationConnector104, assemblyContext_ProvidedDelegationConnector107, providedRole_AssemblyConnector122, requiredRole_AssemblyConnector125, sinkRole__AssemblyEventConnector128, sourceRole__AssemblyEventConnector130, sinkAssemblyContext__AssemblyEventConnector133, sourceAssemblyContext__AssemblyEventConnector136, filterCondition__AssemblyEventConnector139, innerSourceRole__SourceRole142, outerSourceRole__SourceRole144, requiringAssemblyContext_AssemblyConnector117, providingAssemblyContext_AssemblyConnector119, outerRequiredRole__RequiredInfrastructureDelegationConnector177, assemblyContext__RequiredInfrastructureDelegationConnector180, assemblyContext__RequiredResourceDelegationConnector183, innerRequiredRole__RequiredResourceDelegationConnector185, outerRequiredRole__RequiredResourceDelegationConnector188, parentStructure__AssemblyContext191, encapsulatedComponent__AssemblyContext194, configParameterUsages__AssemblyContext195, assemblyContext__SourceDelegationConnector147, assemblyContext__SinkDelegationConnector150, innerSinkRole__SinkRole152, outerSinkRole__SinkRole155, providedRole__AssemblyInfrastructureConnector158, requiredRole__AssemblyInfrastructureConnector159, providingAssemblyContext__AssemblyInfrastructureConnector161, requiringAssemblyContext__AssemblyInfrastructureConnector164, innerProvidedRole__ProvidedInfrastructureDelegationConnector167, outerProvidedRole__ProvidedInfrastructureDelegationConnector169, assemblyContext__ProvidedInfrastructureDelegationConnector172, innerRequiredRole__RequiredInfrastructureDelegationConnector175, providedRole_EntryLevelSystemCall218, operationSignature__EntryLevelSystemCall220, outputParameterUsages_EntryLevelSystemCall222, usageScenario_Workload197, usageModel_UsageScenario199, scenarioBehaviour_UsageScenario201, workload_UsageScenario203, assemblyContext_userData205, usageModel_UserData207, userDataParameterUsages_UserData210, usageScenario_UsageModel213, userData_UsageModel216, usageScenario_SenarioBehaviour236, branchTransition_ScenarioBehaviour239, loop_ScenarioBehaviour241, inputParameterUsages_EntryLevelSystemCall225, successor228, predecessor230, scenarioBehaviour_AbstractUserAction233, actions_ScenarioBehaviour244, branch_BranchTransition247, branchedBehaviour_BranchTransition249, branchTransitions_Branch252, loopIteration_Loop255, bodyBehaviour_Loop258, capacity_PassiveResource270, basicComponent_PassiveResource273, resourceTimeoutFailureType__PassiveResource275, interArrivalTime_OpenWorkload261, timeSpecification_Delay264, thinkTime_ClosedWorkload267, parentCompleteComponentTypes281, componentParameterUsage_ImplementationComponentType282, serviceEffectSpecifications__BasicComponent276, passiveResource_BasicComponent278, resourceSignature__Parameter298, repository__DataType299, components__Repository302, interfaces__Repository305, failureTypes__Repository307, repository__RepositoryComponent285, providingEntity_ProvidedRole287, dataType__Parameter290, infrastructureSignature__Parameter291, operationSignature__Parameter293, eventType__Parameter296, protocols__Interface314, requiredCharacterisations316, infrastructureSignatures__InfrastructureInterface343, dataTypes__Repository309, requiredInterface__InfrastructureRequiredRole346, repository__Interface318, requiringEntity_RequiredRole348, parameter321, interface_RequiredCharacterisation322, parentInterfaces__Interface312, eventTypes__EventGroup325, parameter__EventType328, eventGroup__EventType331, exceptions__Signature334, failureType335, parameters__InfrastructureSignature338, infrastructureInterface__InfrastructureSignature341, returnType__OperationSignature356, signatures__OperationInterface358, interface__OperationSignature351, parameters__OperationSignature353, providedInterface__OperationProvidedRole367, providedInterface__InfrastructureProvidedRole369, requiredInterface__OperationRequiredRole361, eventGroup__SourceRole363, eventGroup__SinkRole365, innerType_CollectionDataType372, parentProvidesComponentTypes371, innerDeclaration_CompositeDataType375, datatype_InnerDeclaration377, compositeDataType_InnerDeclaration379, parameter__ResourceSignature382, resourceInterface__ResourceSignature385, hardwareInducedFailureType__ProcessingResourceType388, resourceRepository_ResourceType390, parentType_CompositeDataType374, networkInducedFailureType__CommunicationLinkResourceType402, resourceRepository__ResourceInterface404, resourceSignatures__ResourceInterface407, variableCharacterisation_VariableUsage410, userData_VariableUsage413, callAction__VariableUsage416, synchronisationPoint_VariableUsage418, callReturnAction__VariableUsage420, setVariableAction_VariableUsage422, resourceInterfaces__ResourceRepository392, schedulingPolicies__ResourceRepository395, availableResourceTypes_ResourceRepository397, resourceRepository__SchedulingPolicy399, specification_VariableCharacterisation435, variableUsage_VariableCharacterisation438, specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage424, assemblyContext__VariableUsage426, entryLevelSystemCall_InputParameterUsage429, entryLevelSystemCall_OutputParameterUsage431, namedReference__VariableUsage434, internalAction__InternalFailureOccurrenceDescription445, softwareInducedFailureType__InternalFailureOccurrenceDescription447, communicationLinkResourceType__NetworkInducedFailureType449, specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription451, failureType__ExternalFailureOccurrenceDescription453, processingResourceType__HardwareInducedFailureType441, internalFailureOccurrenceDescriptions__SoftwareInducedFailureType443, resourceDemand_Action461, infrastructureCall__Action464, resourceCall__Action467, predecessor_AbstractAction470, successor_AbstractAction472, resourceDemandingBehaviour_AbstractAction475, passiveResource__ResourceTimeoutFailureType455, repository__FailureType458, abstractLoopAction_ResourceDemandingBehaviour477, abstractBranchTransition_ResourceDemandingBehaviour479, steps_Behaviour481, bodyBehaviour_Loop484, branchAction_AbstractBranchTransition487, branchBehaviour_BranchTransition489, describedService__SEFF498, basicComponent_ServiceEffectSpecification499, resourceDemandingInternalBehaviours502, resourceDemandingSEFF_ResourceDemandingInternalBehaviour504, passiveResource_ReleaseAction506, branches_Branch492, inputVariableUsages__CallAction495, iterationCount_LoopAction508, asynchronousForkedBehaviours_ForkAction511, synchronisingBehaviours_ForkAction513, synchronisationPoint_ForkedBehaviour516, forkAction_ForkedBehaivour519, outputParameterUsage_SynchronisationPoint521, calledService_ExternalService530, role_ExternalService532, returnVariableUsage__CallReturnAction535, passiveresource_AcquireAction538, forkAction_SynchronisationPoint524, synchronousForkedBehaviours_SynchronisationPoint527, calledResourceDemandingInternalBehaviour548, eventType__EmitEventAction550, sourceRole__EmitEventAction552, internalFailureOccurrenceDescriptions__InternalAction555, parameter_CollectionIteratorAction540, branchCondition_GuardedBranchTransition542, localVariableUsages_SetVariableAction545, signature__InfrastructureCall558, numberOfCalls__InfrastructureCall560, action__InfrastructureCall563, requiredRole__InfrastructureCall565, action__ResourceCall568, specification_ParametericResourceDemand579, requiredResource_ParametricResourceDemand582, action_ParametricResourceDemand584, resourceRequiredRole__ResourceCall571, signature__ResourceCall573, numberOfCalls__ResourceCall576, primaryBehaviour__RecoveryAction590, recoveryActionBehaviours__RecoveryAction592, failureTypes_FailureHandlingEntity595, signature_SpecifiedQoSAnnation597, role_SpecifiedQoSAnnotation599, qosAnnotations_SpecifiedQoSAnnotation601, specifiedOutputParameterAbstractions_QoSAnnotations603, system_QoSAnnotations606, failureHandlingAlternatives__RecoveryActionBehaviour587, recoveryAction__RecoveryActionBehaviour588, specification_SpecifiedExecutionTime620, assemblyContext_ComponentSpecifiedExecutionTime623, specifiedQoSAnnotations_QoSAnnotations607, signature_SpecifiedOutputParameterAbstraction609, role_SpecifiedOutputParameterAbstraction611, externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation625, expectedExternalOutputs_SpecifiedOutputParameterAbstraction614, qosAnnotations_SpecifiedOutputParameterAbstraction617, qosAnnotations_System627, linkingResources__ResourceEnvironment630, resourceContainer_ResourceEnvironment632, connectedResourceContainers_LinkingResource634, resourceEnvironment_ResourceContainer644, nestedResourceContainers__ResourceContainer647, parentResourceContainer__ResourceContainer650, schedulingPolicy653, activeResourceType_ActiveResourceSpecification655, processingRate_ProcessingResourceSpecification658, resourceContainer_ProcessingResourceSpecification661, linkingResource_CommunicationLinkResourceSpecification664, communicationLinkResourceType_CommunicationLinkResourceSpecification667, communicationLinkResourceSpecifications_LinkingResource636, resourceEnvironment_LinkingResource639, activeResourceSpecifications_ResourceContainer641, resourceContainer_AllocationContext675, assemblyContext_AllocationContext677, allocation_AllocationContext680, eventChannel__AllocationContext681, latency_CommunicationLinkResourceSpecification669, throughput_CommunicationLinkResourceSpecification672, completions_CompletionRepository690, requiredCommunicationLinkResource_ParametricResourceDemand691, targetResourceEnvironment_Allocation683, system_Allocation685, allocationContexts_Allocation688},
    generalizations={gen_pcm_av_pc_core_av_pc_PCMRandomVariable_RandomVariable, gen_pcm_av_pc_entity_av_pc_ResourceInterfaceRequiringEntity_Entity, gen_pcm_av_pc_entity_av_pc_ResourceRequiredRole_Role, gen_pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingEntity_Entity, gen_pcm_av_pc_entity_av_pc_ResourceProvidedRole_Role, gen_pcm_av_pc_entity_av_pc_InterfaceProvidingRequiringEntity_entity_av_pc_InterfaceProvidingEntity, gen_pcm_av_pc_entity_av_pc_InterfaceProvidingRequiringEntity_entity_av_pc_InterfaceRequiringEntity, gen_pcm_av_pc_entity_av_pc_InterfaceProvidingEntity_Entity, gen_pcm_av_pc_entity_av_pc_InterfaceRequiringEntity_entity_av_pc_Entity, gen_pcm_av_pc_entity_av_pc_InterfaceRequiringEntity_entity_av_pc_ResourceInterfaceRequiringEntity, gen_pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity_composition_av_pc_ComposedStructure, gen_pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity_entity_av_pc_InterfaceProvidingRequiringEntity, gen_pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingRequiringEntity_entity_av_pc_ResourceInterfaceRequiringEntity, gen_pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingRequiringEntity_entity_av_pc_ResourceInterfaceProvidingEntity, gen_pcm_av_pc_entity_av_pc_Entity_Identifier, gen_pcm_av_pc_entity_av_pc_Entity_entity_av_pc_NamedElement, gen_pcm_av_pc_composition_av_pc_DelegationConnector_Connector, gen_pcm_av_pc_composition_av_pc_Connector_Entity, gen_pcm_av_pc_composition_av_pc_ComposedStructure_Entity, gen_pcm_av_pc_composition_av_pc_EventChannelSourceConnector_Connector, gen_pcm_av_pc_composition_av_pc_EventChannelSinkConnector_Connector, gen_pcm_av_pc_composition_av_pc_ProvidedDelegationConnector_DelegationConnector, gen_pcm_av_pc_composition_av_pc_EventChannel_Entity, gen_pcm_av_pc_composition_av_pc_RequiredDelegationConnector_DelegationConnector, gen_pcm_av_pc_composition_av_pc_AssemblyEventConnector_Connector, gen_pcm_av_pc_composition_av_pc_SourceDelegationConnector_DelegationConnector, gen_pcm_av_pc_composition_av_pc_AssemblyConnector_Connector, gen_pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector_DelegationConnector, gen_pcm_av_pc_composition_av_pc_AssemblyContext_Entity, gen_pcm_av_pc_composition_av_pc_SinkDelegationConnector_DelegationConnector, gen_pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector_Connector, gen_pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector_DelegationConnector, gen_pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector_DelegationConnector, gen_pcm_av_pc_usagemodel_av_pc_UsageScenario_Entity, gen_pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall_AbstractUserAction, gen_pcm_av_pc_usagemodel_av_pc_AbstractUserAction_Entity, gen_pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour_Entity, gen_pcm_av_pc_usagemodel_av_pc_Start_AbstractUserAction, gen_pcm_av_pc_usagemodel_av_pc_OpenWorkload_Workload, gen_pcm_av_pc_usagemodel_av_pc_Branch_AbstractUserAction, gen_pcm_av_pc_usagemodel_av_pc_Loop_AbstractUserAction, gen_pcm_av_pc_usagemodel_av_pc_Stop_AbstractUserAction, gen_pcm_av_pc_repository_av_pc_PassiveResource_Entity, gen_pcm_av_pc_repository_av_pc_BasicComponent_ImplementationComponentType, gen_pcm_av_pc_usagemodel_av_pc_Delay_AbstractUserAction, gen_pcm_av_pc_usagemodel_av_pc_ClosedWorkload_Workload, gen_pcm_av_pc_repository_av_pc_ImplementationComponentType_RepositoryComponent, gen_pcm_av_pc_repository_av_pc_Repository_Entity, gen_pcm_av_pc_repository_av_pc_RepositoryComponent_InterfaceProvidingRequiringEntity, gen_pcm_av_pc_repository_av_pc_ProvidedRole_Role, gen_pcm_av_pc_repository_av_pc_InfrastructureRequiredRole_RequiredRole, gen_pcm_av_pc_repository_av_pc_Interface_Entity, gen_pcm_av_pc_repository_av_pc_RequiredRole_Role, gen_pcm_av_pc_repository_av_pc_OperationSignature_Signature, gen_pcm_av_pc_repository_av_pc_EventGroup_Interface, gen_pcm_av_pc_repository_av_pc_EventType_Signature, gen_pcm_av_pc_repository_av_pc_Signature_Entity, gen_pcm_av_pc_repository_av_pc_InfrastructureSignature_Signature, gen_pcm_av_pc_repository_av_pc_InfrastructureInterface_Interface, gen_pcm_av_pc_repository_av_pc_OperationInterface_Interface, gen_pcm_av_pc_repository_av_pc_InfrastructureProvidedRole_ProvidedRole, gen_pcm_av_pc_repository_av_pc_CompleteComponentType_RepositoryComponent, gen_pcm_av_pc_repository_av_pc_OperationRequiredRole_RequiredRole, gen_pcm_av_pc_repository_av_pc_SourceRole_RequiredRole, gen_pcm_av_pc_repository_av_pc_SinkRole_ProvidedRole, gen_pcm_av_pc_repository_av_pc_OperationProvidedRole_ProvidedRole, gen_pcm_av_pc_repository_av_pc_CompositeComponent_entity_av_pc_ComposedProvidingRequiringEntity, gen_pcm_av_pc_repository_av_pc_CompositeComponent_repository_av_pc_ImplementationComponentType, gen_pcm_av_pc_repository_av_pc_PrimitiveDataType_DataType, gen_pcm_av_pc_repository_av_pc_CollectionDataType_entity_av_pc_Entity, gen_pcm_av_pc_repository_av_pc_CollectionDataType_repository_av_pc_DataType, gen_pcm_av_pc_repository_av_pc_ProvidesComponentType_RepositoryComponent, gen_pcm_av_pc_repository_av_pc_InnerDeclaration_NamedElement, gen_pcm_av_pc_repository_av_pc_Role_Entity, gen_pcm_av_pc_resourcetype_av_pc_ResourceSignature_Entity, gen_pcm_av_pc_resourcetype_av_pc_ProcessingResourceType_ResourceType, gen_pcm_av_pc_resourcetype_av_pc_ResourceType_entity_av_pc_Entity, gen_pcm_av_pc_resourcetype_av_pc_ResourceType_UnitCarryingElement, gen_pcm_av_pc_resourcetype_av_pc_ResourceType_entity_av_pc_ResourceInterfaceProvidingEntity, gen_pcm_av_pc_repository_av_pc_CompositeDataType_entity_av_pc_Entity, gen_pcm_av_pc_repository_av_pc_CompositeDataType_repository_av_pc_DataType, gen_pcm_av_pc_resourcetype_av_pc_CommunicationLinkResourceType_ResourceType, gen_pcm_av_pc_resourcetype_av_pc_ResourceInterface_Entity, gen_pcm_av_pc_resourcetype_av_pc_SchedulingPolicy_Entity, gen_pcm_av_pc_parameter_av_pc_CharacterisedVariable_Variable, gen_pcm_av_pc_reliability_av_pc_HardwareInducedFailureType_FailureType, gen_pcm_av_pc_reliability_av_pc_NetworkInducedFailureType_FailureType, gen_pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_av_pc_reliability_av_pc_SoftwareInducedFailureType_FailureType, gen_pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_av_pc_seff_av_pc_AbstractInternalControlFlowAction_AbstractAction, gen_pcm_av_pc_seff_av_pc_AbstractAction_Entity, gen_pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour_Identifier, gen_pcm_av_pc_reliability_av_pc_ResourceTimeoutFailureType_SoftwareInducedFailureType, gen_pcm_av_pc_reliability_av_pc_FailureType_Entity, gen_pcm_av_pc_seff_av_pc_StopAction_AbstractInternalControlFlowAction, gen_pcm_av_pc_seff_av_pc_AbstractLoopAction_AbstractInternalControlFlowAction, gen_pcm_av_pc_seff_av_pc_AbstractBranchTransition_Entity, gen_pcm_av_pc_seff_av_pc_BranchAction_AbstractInternalControlFlowAction, gen_pcm_av_pc_seff_av_pc_ResourceDemandingSEFF_Identifier, gen_pcm_av_pc_seff_av_pc_ResourceDemandingSEFF_seff_av_pc_ServiceEffectSpecification, gen_pcm_av_pc_seff_av_pc_ResourceDemandingSEFF_seff_av_pc_ResourceDemandingBehaviour, gen_pcm_av_pc_seff_av_pc_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour, gen_pcm_av_pc_seff_av_pc_ReleaseAction_AbstractInternalControlFlowAction, gen_pcm_av_pc_seff_av_pc_StartAction_AbstractInternalControlFlowAction, gen_pcm_av_pc_seff_av_pc_LoopAction_AbstractLoopAction, gen_pcm_av_pc_seff_av_pc_ForkAction_AbstractInternalControlFlowAction, gen_pcm_av_pc_seff_av_pc_ForkedBehaviour_ResourceDemandingBehaviour, gen_pcm_av_pc_seff_av_pc_CallReturnAction_CallAction, gen_pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition_AbstractBranchTransition, gen_pcm_av_pc_seff_av_pc_AcquireAction_AbstractInternalControlFlowAction, gen_pcm_av_pc_seff_av_pc_ExternalCallAction_seff_av_pc_AbstractAction, gen_pcm_av_pc_seff_av_pc_ExternalCallAction_seff_av_pc_CallReturnAction, gen_pcm_av_pc_seff_av_pc_ExternalCallAction_seff_reliability_av_pc_FailureHandlingEntity, gen_pcm_av_pc_seff_av_pc_EmitEventAction_seff_av_pc_AbstractAction, gen_pcm_av_pc_seff_av_pc_EmitEventAction_seff_av_pc_CallAction, gen_pcm_av_pc_seff_av_pc_InternalAction_AbstractInternalControlFlowAction, gen_pcm_av_pc_seff_performance_av_pc_InfrastructureCall_CallAction, gen_pcm_av_pc_seff_av_pc_CollectionIteratorAction_AbstractLoopAction, gen_pcm_av_pc_seff_av_pc_GuardedBranchTransition_AbstractBranchTransition, gen_pcm_av_pc_seff_av_pc_SetVariableAction_AbstractInternalControlFlowAction, gen_pcm_av_pc_seff_av_pc_InternalCallAction_seff_av_pc_CallAction, gen_pcm_av_pc_seff_av_pc_InternalCallAction_seff_av_pc_AbstractInternalControlFlowAction, gen_pcm_av_pc_seff_performance_av_pc_ResourceCall_CallAction, gen_pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour_seff_reliability_av_pc_FailureHandlingEntity, gen_pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour_seff_av_pc_ResourceDemandingBehaviour, gen_pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity_Entity, gen_pcm_av_pc_qosannotations_av_pc_QoSAnnotations_Entity, gen_pcm_av_pc_seff_reliability_av_pc_RecoveryAction_AbstractInternalControlFlowAction, gen_pcm_av_pc_qos_performance_av_pc_SystemSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_av_pc_qos_performance_av_pc_SpecifiedExecutionTime_SpecifiedQoSAnnotation, gen_pcm_av_pc_qos_performance_av_pc_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation, gen_pcm_av_pc_system_av_pc_System_entity_av_pc_Entity, gen_pcm_av_pc_system_av_pc_System_entity_av_pc_ComposedProvidingRequiringEntity, gen_pcm_av_pc_resourceenvironment_av_pc_ResourceEnvironment_NamedElement, gen_pcm_av_pc_resourceenvironment_av_pc_LinkingResource_Entity, gen_pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification_Identifier, gen_pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification_Identifier, gen_pcm_av_pc_resourceenvironment_av_pc_ResourceContainer_Entity, gen_pcm_av_pc_allocation_av_pc_AllocationContext_Entity, gen_pcm_av_pc_allocation_av_pc_Allocation_Entity, gen_pcm_av_pc_completions_av_pc_Completion_entity_av_pc_ComposedProvidingRequiringEntity, gen_pcm_av_pc_completions_av_pc_Completion_repository_av_pc_ImplementationComponentType, gen_pcm_av_pc_completions_av_pc_DelegatingExternalCallAction_ExternalCallAction, gen_pcm_av_pc_completions_av_pc_NetworkDemandParametricResourceDemand_ParametricResourceDemand, gen_pcm_av_pc_subsystem_av_pc_SubSystem_entity_av_pc_ComposedProvidingRequiringEntity, gen_pcm_av_pc_subsystem_av_pc_SubSystem_repository_av_pc_RepositoryComponent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)