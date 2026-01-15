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
            EnumerationLiteral(name="CHAR"),
			EnumerationLiteral(name="BYTE"),
			EnumerationLiteral(name="LONG"),
			EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="BOOL"),
			EnumerationLiteral(name="DOUBLE")
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
pcm_pc_av_PerJoinPointScope = Class(name="pcm::pc::av::PerJoinPointScope")
pcm_pc_av_core_pc_av_PCMRandomVariable = Class(name="pcm::pc::av::core::pc::av::PCMRandomVariable")
RandomVariable = Class(name="RandomVariable")
pcm_pc_av_DummyClass = Class(name="pcm::pc::av::DummyClass")
pcm_pc_av_Pointcut = Class(name="pcm::pc::av::Pointcut")
pcm_pc_av_EObject = Class(name="pcm::pc::av::EObject")
pcm_pc_av_Advice = Class(name="pcm::pc::av::Advice")
pcm_pc_av_GlobalScope = Class(name="pcm::pc::av::GlobalScope")
Loop = Class(name="Loop")
OpenWorkload = Class(name="OpenWorkload")
Delay = Class(name="Delay")
CommunicationLinkResourceSpecification = Class(name="CommunicationLinkResourceSpecification")
ProcessingResourceSpecification = Class(name="ProcessingResourceSpecification")
ClosedWorkload = Class(name="ClosedWorkload")
PassiveResource = Class(name="PassiveResource")
VariableCharacterisation = Class(name="VariableCharacterisation")
seff_performance_pc_av_InfrastructureCall = Class(name="seff::performance::pc::av::InfrastructureCall")
seff_performance_pc_av_ResourceCall = Class(name="seff::performance::pc::av::ResourceCall")
seff_performance_pc_av_ParametricResourceDemand = Class(name="seff::performance::pc::av::ParametricResourceDemand")
LoopAction = Class(name="LoopAction")
GuardedBranchTransition = Class(name="GuardedBranchTransition")
qos_performance_pc_av_SpecifiedExecutionTime = Class(name="qos::performance::pc::av::SpecifiedExecutionTime")
composition_pc_av_EventChannelSinkConnector = Class(name="composition::pc::av::EventChannelSinkConnector")
composition_pc_av_AssemblyEventConnector = Class(name="composition::pc::av::AssemblyEventConnector")
pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingEntity = Class(name="pcm::pc::av::entity::pc::av::ResourceInterfaceProvidingEntity")
entity_pc_av_ResourceProvidedRole = Class(name="entity::pc::av::ResourceProvidedRole")
pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity = Class(name="pcm::pc::av::entity::pc::av::ComposedProvidingRequiringEntity")
composition_pc_av_ComposedStructure = Class(name="composition::pc::av::ComposedStructure")
entity_pc_av_InterfaceProvidingRequiringEntity = Class(name="entity::pc::av::InterfaceProvidingRequiringEntity")
pcm_pc_av_entity_pc_av_ResourceProvidedRole = Class(name="pcm::pc::av::entity::pc::av::ResourceProvidedRole")
Role = Class(name="Role")
entity_pc_av_ResourceInterfaceProvidingEntity = Class(name="entity::pc::av::ResourceInterfaceProvidingEntity")
ResourceInterface = Class(name="ResourceInterface")
pcm_pc_av_entity_pc_av_InterfaceProvidingRequiringEntity = Class(name="pcm::pc::av::entity::pc::av::InterfaceProvidingRequiringEntity")
entity_pc_av_InterfaceProvidingEntity = Class(name="entity::pc::av::InterfaceProvidingEntity")
entity_pc_av_InterfaceRequiringEntity = Class(name="entity::pc::av::InterfaceRequiringEntity")
pcm_pc_av_entity_pc_av_InterfaceProvidingEntity = Class(name="pcm::pc::av::entity::pc::av::InterfaceProvidingEntity")
Entity = Class(name="Entity")
ProvidedRole = Class(name="ProvidedRole")
pcm_pc_av_entity_pc_av_InterfaceRequiringEntity = Class(name="pcm::pc::av::entity::pc::av::InterfaceRequiringEntity")
entity_pc_av_Entity = Class(name="entity::pc::av::Entity")
entity_pc_av_ResourceInterfaceRequiringEntity = Class(name="entity::pc::av::ResourceInterfaceRequiringEntity")
RequiredRole = Class(name="RequiredRole")
pcm_pc_av_entity_pc_av_ResourceInterfaceRequiringEntity = Class(name="pcm::pc::av::entity::pc::av::ResourceInterfaceRequiringEntity")
entity_pc_av_ResourceRequiredRole = Class(name="entity::pc::av::ResourceRequiredRole")
pcm_pc_av_entity_pc_av_ResourceRequiredRole = Class(name="pcm::pc::av::entity::pc::av::ResourceRequiredRole")
composition_pc_av_AssemblyContext = Class(name="composition::pc::av::AssemblyContext")
composition_pc_av_ResourceRequiredDelegationConnector = Class(name="composition::pc::av::ResourceRequiredDelegationConnector")
composition_pc_av_EventChannel = Class(name="composition::pc::av::EventChannel")
pcm_pc_av_entity_pc_av_NamedElement = Class(name="pcm::pc::av::entity::pc::av::NamedElement")
pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingRequiringEntity = Class(name="pcm::pc::av::entity::pc::av::ResourceInterfaceProvidingRequiringEntity")
pcm_pc_av_entity_pc_av_Entity = Class(name="pcm::pc::av::entity::pc::av::Entity")
Identifier = Class(name="Identifier")
entity_pc_av_NamedElement = Class(name="entity::pc::av::NamedElement")
pcm_pc_av_composition_pc_av_DelegationConnector = Class(name="pcm::pc::av::composition::pc::av::DelegationConnector")
Connector = Class(name="Connector")
pcm_pc_av_composition_pc_av_Connector = Class(name="pcm::pc::av::composition::pc::av::Connector")
pcm_pc_av_composition_pc_av_ComposedStructure = Class(name="pcm::pc::av::composition::pc::av::ComposedStructure")
SinkRole = Class(name="SinkRole")
PCMRandomVariable = Class(name="PCMRandomVariable")
pcm_pc_av_composition_pc_av_ProvidedDelegationConnector = Class(name="pcm::pc::av::composition::pc::av::ProvidedDelegationConnector")
DelegationConnector = Class(name="DelegationConnector")
composition_pc_av_Connector = Class(name="composition::pc::av::Connector")
pcm_pc_av_composition_pc_av_ResourceRequiredDelegationConnector = Class(name="pcm::pc::av::composition::pc::av::ResourceRequiredDelegationConnector")
pcm_pc_av_composition_pc_av_EventChannel = Class(name="pcm::pc::av::composition::pc::av::EventChannel")
EventGroup = Class(name="EventGroup")
composition_pc_av_EventChannelSourceConnector = Class(name="composition::pc::av::EventChannelSourceConnector")
pcm_pc_av_composition_pc_av_EventChannelSourceConnector = Class(name="pcm::pc::av::composition::pc::av::EventChannelSourceConnector")
SourceRole = Class(name="SourceRole")
pcm_pc_av_composition_pc_av_EventChannelSinkConnector = Class(name="pcm::pc::av::composition::pc::av::EventChannelSinkConnector")
OperationRequiredRole = Class(name="OperationRequiredRole")
pcm_pc_av_composition_pc_av_AssemblyConnector = Class(name="pcm::pc::av::composition::pc::av::AssemblyConnector")
OperationProvidedRole = Class(name="OperationProvidedRole")
pcm_pc_av_composition_pc_av_RequiredDelegationConnector = Class(name="pcm::pc::av::composition::pc::av::RequiredDelegationConnector")
pcm_pc_av_composition_pc_av_SourceDelegationConnector = Class(name="pcm::pc::av::composition::pc::av::SourceDelegationConnector")
pcm_pc_av_composition_pc_av_SinkDelegationConnector = Class(name="pcm::pc::av::composition::pc::av::SinkDelegationConnector")
pcm_pc_av_composition_pc_av_AssemblyEventConnector = Class(name="pcm::pc::av::composition::pc::av::AssemblyEventConnector")
pcm_pc_av_composition_pc_av_AssemblyContext = Class(name="pcm::pc::av::composition::pc::av::AssemblyContext")
RepositoryComponent = Class(name="RepositoryComponent")
VariableUsage = Class(name="VariableUsage")
pcm_pc_av_usagemodel_pc_av_Workload = Class(name="pcm::pc::av::usagemodel::pc::av::Workload")
UsageScenario = Class(name="UsageScenario")
pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector = Class(name="pcm::pc::av::composition::pc::av::AssemblyInfrastructureConnector")
InfrastructureProvidedRole = Class(name="InfrastructureProvidedRole")
InfrastructureRequiredRole = Class(name="InfrastructureRequiredRole")
pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector = Class(name="pcm::pc::av::composition::pc::av::ProvidedInfrastructureDelegationConnector")
pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector = Class(name="pcm::pc::av::composition::pc::av::RequiredInfrastructureDelegationConnector")
pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector = Class(name="pcm::pc::av::composition::pc::av::RequiredResourceDelegationConnector")
OperationSignature = Class(name="OperationSignature")
pcm_pc_av_usagemodel_pc_av_UsageScenario = Class(name="pcm::pc::av::usagemodel::pc::av::UsageScenario")
UsageModel = Class(name="UsageModel")
ScenarioBehaviour = Class(name="ScenarioBehaviour")
Workload = Class(name="Workload")
pcm_pc_av_usagemodel_pc_av_UserData = Class(name="pcm::pc::av::usagemodel::pc::av::UserData")
pcm_pc_av_usagemodel_pc_av_UsageModel = Class(name="pcm::pc::av::usagemodel::pc::av::UsageModel")
UserData = Class(name="UserData")
pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall = Class(name="pcm::pc::av::usagemodel::pc::av::EntryLevelSystemCall")
AbstractUserAction = Class(name="AbstractUserAction")
BranchTransition = Class(name="BranchTransition")
pcm_pc_av_usagemodel_pc_av_BranchTransition = Class(name="pcm::pc::av::usagemodel::pc::av::BranchTransition")
Branch = Class(name="Branch")
pcm_pc_av_usagemodel_pc_av_AbstractUserAction = Class(name="pcm::pc::av::usagemodel::pc::av::AbstractUserAction")
pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour = Class(name="pcm::pc::av::usagemodel::pc::av::ScenarioBehaviour")
pcm_pc_av_usagemodel_pc_av_Start = Class(name="pcm::pc::av::usagemodel::pc::av::Start")
pcm_pc_av_usagemodel_pc_av_OpenWorkload = Class(name="pcm::pc::av::usagemodel::pc::av::OpenWorkload")
pcm_pc_av_usagemodel_pc_av_Branch = Class(name="pcm::pc::av::usagemodel::pc::av::Branch")
pcm_pc_av_usagemodel_pc_av_Loop = Class(name="pcm::pc::av::usagemodel::pc::av::Loop")
pcm_pc_av_usagemodel_pc_av_Stop = Class(name="pcm::pc::av::usagemodel::pc::av::Stop")
pcm_pc_av_repository_pc_av_PassiveResource = Class(name="pcm::pc::av::repository::pc::av::PassiveResource")
BasicComponent = Class(name="BasicComponent")
ResourceTimeoutFailureType = Class(name="ResourceTimeoutFailureType")
pcm_pc_av_repository_pc_av_BasicComponent = Class(name="pcm::pc::av::repository::pc::av::BasicComponent")
ImplementationComponentType = Class(name="ImplementationComponentType")
pcm_pc_av_usagemodel_pc_av_Delay = Class(name="pcm::pc::av::usagemodel::pc::av::Delay")
pcm_pc_av_usagemodel_pc_av_ClosedWorkload = Class(name="pcm::pc::av::usagemodel::pc::av::ClosedWorkload")
CompleteComponentType = Class(name="CompleteComponentType")
ServiceEffectSpecification = Class(name="ServiceEffectSpecification")
pcm_pc_av_repository_pc_av_ImplementationComponentType = Class(name="pcm::pc::av::repository::pc::av::ImplementationComponentType")
ResourceSignature = Class(name="ResourceSignature")
pcm_pc_av_repository_pc_av_DataType = Class(name="pcm::pc::av::repository::pc::av::DataType")
pcm_pc_av_repository_pc_av_Repository = Class(name="pcm::pc::av::repository::pc::av::Repository")
pcm_pc_av_repository_pc_av_RepositoryComponent = Class(name="pcm::pc::av::repository::pc::av::RepositoryComponent")
InterfaceProvidingRequiringEntity = Class(name="InterfaceProvidingRequiringEntity")
Repository = Class(name="Repository")
pcm_pc_av_repository_pc_av_ProvidedRole = Class(name="pcm::pc::av::repository::pc::av::ProvidedRole")
pcm_pc_av_repository_pc_av_Parameter = Class(name="pcm::pc::av::repository::pc::av::Parameter")
DataType = Class(name="DataType")
InfrastructureSignature = Class(name="InfrastructureSignature")
EventType = Class(name="EventType")
Protocol = Class(name="Protocol")
RequiredCharacterisation = Class(name="RequiredCharacterisation")
pcm_pc_av_repository_pc_av_RequiredCharacterisation = Class(name="pcm::pc::av::repository::pc::av::RequiredCharacterisation")
Parameter_ = Class(name="Parameter")
Interface = Class(name="Interface")
FailureType = Class(name="FailureType")
pcm_pc_av_repository_pc_av_Interface = Class(name="pcm::pc::av::repository::pc::av::Interface")
pcm_pc_av_repository_pc_av_InfrastructureSignature = Class(name="pcm::pc::av::repository::pc::av::InfrastructureSignature")
InfrastructureInterface = Class(name="InfrastructureInterface")
pcm_pc_av_repository_pc_av_InfrastructureInterface = Class(name="pcm::pc::av::repository::pc::av::InfrastructureInterface")
pcm_pc_av_repository_pc_av_InfrastructureRequiredRole = Class(name="pcm::pc::av::repository::pc::av::InfrastructureRequiredRole")
pcm_pc_av_repository_pc_av_RequiredRole = Class(name="pcm::pc::av::repository::pc::av::RequiredRole")
pcm_pc_av_repository_pc_av_EventGroup = Class(name="pcm::pc::av::repository::pc::av::EventGroup")
pcm_pc_av_repository_pc_av_EventType = Class(name="pcm::pc::av::repository::pc::av::EventType")
Signature = Class(name="Signature")
pcm_pc_av_repository_pc_av_Signature = Class(name="pcm::pc::av::repository::pc::av::Signature")
ExceptionType = Class(name="ExceptionType")
pcm_pc_av_repository_pc_av_ExceptionType = Class(name="pcm::pc::av::repository::pc::av::ExceptionType")
pcm_pc_av_repository_pc_av_OperationRequiredRole = Class(name="pcm::pc::av::repository::pc::av::OperationRequiredRole")
pcm_pc_av_repository_pc_av_SourceRole = Class(name="pcm::pc::av::repository::pc::av::SourceRole")
pcm_pc_av_repository_pc_av_SinkRole = Class(name="pcm::pc::av::repository::pc::av::SinkRole")
pcm_pc_av_repository_pc_av_OperationSignature = Class(name="pcm::pc::av::repository::pc::av::OperationSignature")
OperationInterface = Class(name="OperationInterface")
pcm_pc_av_repository_pc_av_OperationInterface = Class(name="pcm::pc::av::repository::pc::av::OperationInterface")
ProvidesComponentType = Class(name="ProvidesComponentType")
pcm_pc_av_repository_pc_av_ProvidesComponentType = Class(name="pcm::pc::av::repository::pc::av::ProvidesComponentType")
pcm_pc_av_repository_pc_av_OperationProvidedRole = Class(name="pcm::pc::av::repository::pc::av::OperationProvidedRole")
pcm_pc_av_repository_pc_av_InfrastructureProvidedRole = Class(name="pcm::pc::av::repository::pc::av::InfrastructureProvidedRole")
pcm_pc_av_repository_pc_av_CompleteComponentType = Class(name="pcm::pc::av::repository::pc::av::CompleteComponentType")
pcm_pc_av_repository_pc_av_CollectionDataType = Class(name="pcm::pc::av::repository::pc::av::CollectionDataType")
repository_pc_av_DataType = Class(name="repository::pc::av::DataType")
pcm_pc_av_repository_pc_av_CompositeDataType = Class(name="pcm::pc::av::repository::pc::av::CompositeDataType")
CompositeDataType = Class(name="CompositeDataType")
InnerDeclaration = Class(name="InnerDeclaration")
pcm_pc_av_repository_pc_av_CompositeComponent = Class(name="pcm::pc::av::repository::pc::av::CompositeComponent")
entity_pc_av_ComposedProvidingRequiringEntity = Class(name="entity::pc::av::ComposedProvidingRequiringEntity")
repository_pc_av_ImplementationComponentType = Class(name="repository::pc::av::ImplementationComponentType")
pcm_pc_av_repository_pc_av_PrimitiveDataType = Class(name="pcm::pc::av::repository::pc::av::PrimitiveDataType")
HardwareInducedFailureType = Class(name="HardwareInducedFailureType")
pcm_pc_av_resourcetype_pc_av_ResourceType = Class(name="pcm::pc::av::resourcetype::pc::av::ResourceType")
UnitCarryingElement = Class(name="UnitCarryingElement")
ResourceRepository = Class(name="ResourceRepository")
pcm_pc_av_resourcetype_pc_av_ResourceRepository = Class(name="pcm::pc::av::resourcetype::pc::av::ResourceRepository")
SchedulingPolicy = Class(name="SchedulingPolicy")
pcm_pc_av_repository_pc_av_InnerDeclaration = Class(name="pcm::pc::av::repository::pc::av::InnerDeclaration")
NamedElement = Class(name="NamedElement")
pcm_pc_av_resourcetype_pc_av_SchedulingPolicy = Class(name="pcm::pc::av::resourcetype::pc::av::SchedulingPolicy")
pcm_pc_av_resourcetype_pc_av_CommunicationLinkResourceType = Class(name="pcm::pc::av::resourcetype::pc::av::CommunicationLinkResourceType")
pcm_pc_av_repository_pc_av_Role = Class(name="pcm::pc::av::repository::pc::av::Role")
NetworkInducedFailureType = Class(name="NetworkInducedFailureType")
pcm_pc_av_resourcetype_pc_av_ResourceInterface = Class(name="pcm::pc::av::resourcetype::pc::av::ResourceInterface")
pcm_pc_av_resourcetype_pc_av_ResourceSignature = Class(name="pcm::pc::av::resourcetype::pc::av::ResourceSignature")
pcm_pc_av_resourcetype_pc_av_ProcessingResourceType = Class(name="pcm::pc::av::resourcetype::pc::av::ProcessingResourceType")
ResourceType = Class(name="ResourceType")
pcm_pc_av_protocol_pc_av_Protocol = Class(name="pcm::pc::av::protocol::pc::av::Protocol")
pcm_pc_av_parameter_pc_av_VariableUsage = Class(name="pcm::pc::av::parameter::pc::av::VariableUsage")
CallAction = Class(name="CallAction")
SynchronisationPoint = Class(name="SynchronisationPoint")
CallReturnAction = Class(name="CallReturnAction")
SetVariableAction = Class(name="SetVariableAction")
SpecifiedOutputParameterAbstraction = Class(name="SpecifiedOutputParameterAbstraction")
parameter_pc_av_pcm_pc_av_AbstractNamedReference = Class(name="parameter::pc::av::pcm::pc::av::AbstractNamedReference")
pcm_pc_av_parameter_pc_av_VariableCharacterisation = Class(name="pcm::pc::av::parameter::pc::av::VariableCharacterisation")
pcm_pc_av_parameter_pc_av_CharacterisedVariable = Class(name="pcm::pc::av::parameter::pc::av::CharacterisedVariable")
Variable = Class(name="Variable")
pcm_pc_av_reliability_pc_av_FailureOccurrenceDescription = Class(name="pcm::pc::av::reliability::pc::av::FailureOccurrenceDescription")
EntryLevelSystemCall = Class(name="EntryLevelSystemCall")
ProcessingResourceType = Class(name="ProcessingResourceType")
pcm_pc_av_reliability_pc_av_SoftwareInducedFailureType = Class(name="pcm::pc::av::reliability::pc::av::SoftwareInducedFailureType")
InternalFailureOccurrenceDescription = Class(name="InternalFailureOccurrenceDescription")
pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription = Class(name="pcm::pc::av::reliability::pc::av::InternalFailureOccurrenceDescription")
FailureOccurrenceDescription = Class(name="FailureOccurrenceDescription")
InternalAction = Class(name="InternalAction")
SoftwareInducedFailureType = Class(name="SoftwareInducedFailureType")
pcm_pc_av_reliability_pc_av_NetworkInducedFailureType = Class(name="pcm::pc::av::reliability::pc::av::NetworkInducedFailureType")
CommunicationLinkResourceType = Class(name="CommunicationLinkResourceType")
pcm_pc_av_reliability_pc_av_HardwareInducedFailureType = Class(name="pcm::pc::av::reliability::pc::av::HardwareInducedFailureType")
qos_reliability_pc_av_SpecifiedReliabilityAnnotation = Class(name="qos::reliability::pc::av::SpecifiedReliabilityAnnotation")
pcm_pc_av_reliability_pc_av_ResourceTimeoutFailureType = Class(name="pcm::pc::av::reliability::pc::av::ResourceTimeoutFailureType")
pcm_pc_av_reliability_pc_av_FailureType = Class(name="pcm::pc::av::reliability::pc::av::FailureType")
pcm_pc_av_seff_pc_av_StopAction = Class(name="pcm::pc::av::seff::pc::av::StopAction")
AbstractInternalControlFlowAction = Class(name="AbstractInternalControlFlowAction")
pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction = Class(name="pcm::pc::av::seff::pc::av::AbstractInternalControlFlowAction")
AbstractAction = Class(name="AbstractAction")
pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription = Class(name="pcm::pc::av::reliability::pc::av::ExternalFailureOccurrenceDescription")
pcm_pc_av_seff_pc_av_AbstractAction = Class(name="pcm::pc::av::seff::pc::av::AbstractAction")
ResourceDemandingBehaviour = Class(name="ResourceDemandingBehaviour")
pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour = Class(name="pcm::pc::av::seff::pc::av::ResourceDemandingBehaviour")
AbstractLoopAction = Class(name="AbstractLoopAction")
pcm_pc_av_seff_pc_av_AbstractLoopAction = Class(name="pcm::pc::av::seff::pc::av::AbstractLoopAction")
pcm_pc_av_seff_pc_av_AbstractBranchTransition = Class(name="pcm::pc::av::seff::pc::av::AbstractBranchTransition")
BranchAction = Class(name="BranchAction")
pcm_pc_av_seff_pc_av_BranchAction = Class(name="pcm::pc::av::seff::pc::av::BranchAction")
pcm_pc_av_seff_pc_av_CallAction = Class(name="pcm::pc::av::seff::pc::av::CallAction")
pcm_pc_av_seff_pc_av_StartAction = Class(name="pcm::pc::av::seff::pc::av::StartAction")
AbstractBranchTransition = Class(name="AbstractBranchTransition")
pcm_pc_av_seff_pc_av_ServiceEffectSpecification = Class(name="pcm::pc::av::seff::pc::av::ServiceEffectSpecification")
pcm_pc_av_seff_pc_av_ResourceDemandingSEFF = Class(name="pcm::pc::av::seff::pc::av::ResourceDemandingSEFF")
seff_pc_av_ServiceEffectSpecification = Class(name="seff::pc::av::ServiceEffectSpecification")
seff_pc_av_ResourceDemandingBehaviour = Class(name="seff::pc::av::ResourceDemandingBehaviour")
ResourceDemandingInternalBehaviour = Class(name="ResourceDemandingInternalBehaviour")
pcm_pc_av_seff_pc_av_ResourceDemandingInternalBehaviour = Class(name="pcm::pc::av::seff::pc::av::ResourceDemandingInternalBehaviour")
pcm_pc_av_seff_pc_av_LoopAction = Class(name="pcm::pc::av::seff::pc::av::LoopAction")
pcm_pc_av_seff_pc_av_ForkAction = Class(name="pcm::pc::av::seff::pc::av::ForkAction")
ForkedBehaviour = Class(name="ForkedBehaviour")
pcm_pc_av_seff_pc_av_ForkedBehaviour = Class(name="pcm::pc::av::seff::pc::av::ForkedBehaviour")
ForkAction = Class(name="ForkAction")
pcm_pc_av_seff_pc_av_SynchronisationPoint = Class(name="pcm::pc::av::seff::pc::av::SynchronisationPoint")
pcm_pc_av_seff_pc_av_ExternalCallAction = Class(name="pcm::pc::av::seff::pc::av::ExternalCallAction")
seff_pc_av_AbstractAction = Class(name="seff::pc::av::AbstractAction")
seff_pc_av_CallReturnAction = Class(name="seff::pc::av::CallReturnAction")
ResourceDemandingSEFF = Class(name="ResourceDemandingSEFF")
seff_reliability_pc_av_FailureHandlingEntity = Class(name="seff::reliability::pc::av::FailureHandlingEntity")
pcm_pc_av_seff_pc_av_ReleaseAction = Class(name="pcm::pc::av::seff::pc::av::ReleaseAction")
pcm_pc_av_seff_pc_av_CollectionIteratorAction = Class(name="pcm::pc::av::seff::pc::av::CollectionIteratorAction")
pcm_pc_av_seff_pc_av_GuardedBranchTransition = Class(name="pcm::pc::av::seff::pc::av::GuardedBranchTransition")
pcm_pc_av_seff_pc_av_CallReturnAction = Class(name="pcm::pc::av::seff::pc::av::CallReturnAction")
pcm_pc_av_seff_pc_av_ProbabilisticBranchTransition = Class(name="pcm::pc::av::seff::pc::av::ProbabilisticBranchTransition")
pcm_pc_av_seff_pc_av_AcquireAction = Class(name="pcm::pc::av::seff::pc::av::AcquireAction")
pcm_pc_av_seff_pc_av_InternalAction = Class(name="pcm::pc::av::seff::pc::av::InternalAction")
pcm_pc_av_seff_pc_av_SetVariableAction = Class(name="pcm::pc::av::seff::pc::av::SetVariableAction")
pcm_pc_av_seff_pc_av_InternalCallAction = Class(name="pcm::pc::av::seff::pc::av::InternalCallAction")
seff_pc_av_CallAction = Class(name="seff::pc::av::CallAction")
seff_pc_av_AbstractInternalControlFlowAction = Class(name="seff::pc::av::AbstractInternalControlFlowAction")
pcm_pc_av_seff_pc_av_EmitEventAction = Class(name="pcm::pc::av::seff::pc::av::EmitEventAction")
pcm_pc_av_seff_performance_pc_av_InfrastructureCall = Class(name="pcm::pc::av::seff::performance::pc::av::InfrastructureCall")
pcm_pc_av_seff_performance_pc_av_ResourceCall = Class(name="pcm::pc::av::seff::performance::pc::av::ResourceCall")
pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand = Class(name="pcm::pc::av::seff::performance::pc::av::ParametricResourceDemand")
pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour = Class(name="pcm::pc::av::seff::reliability::pc::av::RecoveryActionBehaviour")
pcm_pc_av_seff_reliability_pc_av_FailureHandlingEntity = Class(name="pcm::pc::av::seff::reliability::pc::av::FailureHandlingEntity")
pcm_pc_av_qosannotations_pc_av_SpecifiedQoSAnnotation = Class(name="pcm::pc::av::qosannotations::pc::av::SpecifiedQoSAnnotation")
seff_reliability_pc_av_RecoveryActionBehaviour = Class(name="seff::reliability::pc::av::RecoveryActionBehaviour")
seff_reliability_pc_av_RecoveryAction = Class(name="seff::reliability::pc::av::RecoveryAction")
pcm_pc_av_seff_reliability_pc_av_RecoveryAction = Class(name="pcm::pc::av::seff::reliability::pc::av::RecoveryAction")
System = Class(name="System")
SpecifiedQoSAnnotation = Class(name="SpecifiedQoSAnnotation")
QoSAnnotations = Class(name="QoSAnnotations")
pcm_pc_av_qosannotations_pc_av_QoSAnnotations = Class(name="pcm::pc::av::qosannotations::pc::av::QoSAnnotations")
pcm_pc_av_qos_performance_pc_av_SystemSpecifiedExecutionTime = Class(name="pcm::pc::av::qos::performance::pc::av::SystemSpecifiedExecutionTime")
SpecifiedExecutionTime = Class(name="SpecifiedExecutionTime")
pcm_pc_av_qos_performance_pc_av_SpecifiedExecutionTime = Class(name="pcm::pc::av::qos::performance::pc::av::SpecifiedExecutionTime")
pcm_pc_av_qos_performance_pc_av_ComponentSpecifiedExecutionTime = Class(name="pcm::pc::av::qos::performance::pc::av::ComponentSpecifiedExecutionTime")
pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction = Class(name="pcm::pc::av::qosannotations::pc::av::SpecifiedOutputParameterAbstraction")
ExternalFailureOccurrenceDescription = Class(name="ExternalFailureOccurrenceDescription")
pcm_pc_av_system_pc_av_System = Class(name="pcm::pc::av::system::pc::av::System")
pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation = Class(name="pcm::pc::av::qos::reliability::pc::av::SpecifiedReliabilityAnnotation")
pcm_pc_av_resourceenvironment_pc_av_ResourceContainer = Class(name="pcm::pc::av::resourceenvironment::pc::av::ResourceContainer")
pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification = Class(name="pcm::pc::av::resourceenvironment::pc::av::ProcessingResourceSpecification")
pcm_pc_av_resourceenvironment_pc_av_ResourceEnvironment = Class(name="pcm::pc::av::resourceenvironment::pc::av::ResourceEnvironment")
LinkingResource = Class(name="LinkingResource")
ResourceContainer = Class(name="ResourceContainer")
pcm_pc_av_resourceenvironment_pc_av_LinkingResource = Class(name="pcm::pc::av::resourceenvironment::pc::av::LinkingResource")
ResourceEnvironment = Class(name="ResourceEnvironment")
pcm_pc_av_allocation_pc_av_AllocationContext = Class(name="pcm::pc::av::allocation::pc::av::AllocationContext")
Allocation = Class(name="Allocation")
pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification = Class(name="pcm::pc::av::resourceenvironment::pc::av::CommunicationLinkResourceSpecification")
AllocationContext = Class(name="AllocationContext")
pcm_pc_av_subsystem_pc_av_SubSystem = Class(name="pcm::pc::av::subsystem::pc::av::SubSystem")
repository_pc_av_RepositoryComponent = Class(name="repository::pc::av::RepositoryComponent")
pcm_pc_av_completions_pc_av_Completion = Class(name="pcm::pc::av::completions::pc::av::Completion")
pcm_pc_av_completions_pc_av_CompletionRepository = Class(name="pcm::pc::av::completions::pc::av::CompletionRepository")
pcm_pc_av_allocation_pc_av_Allocation = Class(name="pcm::pc::av::allocation::pc::av::Allocation")
Completion = Class(name="Completion")
pcm_pc_av_completions_pc_av_DelegatingExternalCallAction = Class(name="pcm::pc::av::completions::pc::av::DelegatingExternalCallAction")
ExternalCallAction = Class(name="ExternalCallAction")
pcm_pc_av_completions_pc_av_NetworkDemandParametricResourceDemand = Class(name="pcm::pc::av::completions::pc::av::NetworkDemandParametricResourceDemand")
ParametricResourceDemand = Class(name="ParametricResourceDemand")

# pcm_pc_av_PerJoinPointScope class attributes and methods

# pcm_pc_av_core_pc_av_PCMRandomVariable class attributes and methods
pcm_pc_av_core_pc_av_PCMRandomVariable_m_SpecificationMustNotBeNULL: Method = Method(name="SpecificationMustNotBeNULL", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_core_pc_av_PCMRandomVariable.methods={pcm_pc_av_core_pc_av_PCMRandomVariable_m_SpecificationMustNotBeNULL}

# RandomVariable class attributes and methods

# pcm_pc_av_DummyClass class attributes and methods

# pcm_pc_av_Pointcut class attributes and methods

# pcm_pc_av_EObject class attributes and methods

# pcm_pc_av_Advice class attributes and methods

# pcm_pc_av_GlobalScope class attributes and methods

# Loop class attributes and methods

# OpenWorkload class attributes and methods

# Delay class attributes and methods

# CommunicationLinkResourceSpecification class attributes and methods

# ProcessingResourceSpecification class attributes and methods

# ClosedWorkload class attributes and methods

# PassiveResource class attributes and methods

# VariableCharacterisation class attributes and methods

# seff_performance_pc_av_InfrastructureCall class attributes and methods

# seff_performance_pc_av_ResourceCall class attributes and methods

# seff_performance_pc_av_ParametricResourceDemand class attributes and methods

# LoopAction class attributes and methods

# GuardedBranchTransition class attributes and methods

# qos_performance_pc_av_SpecifiedExecutionTime class attributes and methods

# composition_pc_av_EventChannelSinkConnector class attributes and methods

# composition_pc_av_AssemblyEventConnector class attributes and methods

# pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingEntity class attributes and methods

# entity_pc_av_ResourceProvidedRole class attributes and methods

# pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity class attributes and methods
pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound: Method = Method(name="ProvidedRolesMustBeBound", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity.methods={pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound}

# composition_pc_av_ComposedStructure class attributes and methods

# entity_pc_av_InterfaceProvidingRequiringEntity class attributes and methods

# pcm_pc_av_entity_pc_av_ResourceProvidedRole class attributes and methods

# Role class attributes and methods

# entity_pc_av_ResourceInterfaceProvidingEntity class attributes and methods

# ResourceInterface class attributes and methods

# pcm_pc_av_entity_pc_av_InterfaceProvidingRequiringEntity class attributes and methods

# entity_pc_av_InterfaceProvidingEntity class attributes and methods

# entity_pc_av_InterfaceRequiringEntity class attributes and methods

# pcm_pc_av_entity_pc_av_InterfaceProvidingEntity class attributes and methods

# Entity class attributes and methods

# ProvidedRole class attributes and methods

# pcm_pc_av_entity_pc_av_InterfaceRequiringEntity class attributes and methods

# entity_pc_av_Entity class attributes and methods

# entity_pc_av_ResourceInterfaceRequiringEntity class attributes and methods

# RequiredRole class attributes and methods

# pcm_pc_av_entity_pc_av_ResourceInterfaceRequiringEntity class attributes and methods

# entity_pc_av_ResourceRequiredRole class attributes and methods

# pcm_pc_av_entity_pc_av_ResourceRequiredRole class attributes and methods

# composition_pc_av_AssemblyContext class attributes and methods

# composition_pc_av_ResourceRequiredDelegationConnector class attributes and methods

# composition_pc_av_EventChannel class attributes and methods

# pcm_pc_av_entity_pc_av_NamedElement class attributes and methods
pcm_pc_av_entity_pc_av_NamedElement_entityName: Property = Property(name="entityName", type=StringType)
pcm_pc_av_entity_pc_av_NamedElement.attributes={pcm_pc_av_entity_pc_av_NamedElement_entityName}

# pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingRequiringEntity class attributes and methods

# pcm_pc_av_entity_pc_av_Entity class attributes and methods

# Identifier class attributes and methods

# entity_pc_av_NamedElement class attributes and methods

# pcm_pc_av_composition_pc_av_DelegationConnector class attributes and methods

# Connector class attributes and methods

# pcm_pc_av_composition_pc_av_Connector class attributes and methods

# pcm_pc_av_composition_pc_av_ComposedStructure class attributes and methods
pcm_pc_av_composition_pc_av_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors: Method = Method(name="MultipleConnectorsConstraintForAssemblyConnectors", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_composition_pc_av_ComposedStructure_m_MultipleConnectorsConstraint: Method = Method(name="MultipleConnectorsConstraint", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_composition_pc_av_ComposedStructure.methods={pcm_pc_av_composition_pc_av_ComposedStructure_m_MultipleConnectorsConstraint, pcm_pc_av_composition_pc_av_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors}

# SinkRole class attributes and methods

# PCMRandomVariable class attributes and methods

# pcm_pc_av_composition_pc_av_ProvidedDelegationConnector class attributes and methods
pcm_pc_av_composition_pc_av_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_composition_pc_av_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_composition_pc_av_ProvidedDelegationConnector.methods={pcm_pc_av_composition_pc_av_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame, pcm_pc_av_composition_pc_av_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure}

# DelegationConnector class attributes and methods

# composition_pc_av_Connector class attributes and methods

# pcm_pc_av_composition_pc_av_ResourceRequiredDelegationConnector class attributes and methods

# pcm_pc_av_composition_pc_av_EventChannel class attributes and methods

# EventGroup class attributes and methods

# composition_pc_av_EventChannelSourceConnector class attributes and methods

# pcm_pc_av_composition_pc_av_EventChannelSourceConnector class attributes and methods

# SourceRole class attributes and methods

# pcm_pc_av_composition_pc_av_EventChannelSinkConnector class attributes and methods

# OperationRequiredRole class attributes and methods

# pcm_pc_av_composition_pc_av_AssemblyConnector class attributes and methods
pcm_pc_av_composition_pc_av_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_composition_pc_av_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_composition_pc_av_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch: Method = Method(name="AssemblyConnectorsReferencedInterfacesMustMatch", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_composition_pc_av_AssemblyConnector.methods={pcm_pc_av_composition_pc_av_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch, pcm_pc_av_composition_pc_av_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch, pcm_pc_av_composition_pc_av_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch}

# OperationProvidedRole class attributes and methods

# pcm_pc_av_composition_pc_av_RequiredDelegationConnector class attributes and methods
pcm_pc_av_composition_pc_av_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector: Method = Method(name="RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_composition_pc_av_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_composition_pc_av_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_composition_pc_av_RequiredDelegationConnector.methods={pcm_pc_av_composition_pc_av_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame, pcm_pc_av_composition_pc_av_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector, pcm_pc_av_composition_pc_av_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure}

# pcm_pc_av_composition_pc_av_SourceDelegationConnector class attributes and methods

# pcm_pc_av_composition_pc_av_SinkDelegationConnector class attributes and methods

# pcm_pc_av_composition_pc_av_AssemblyEventConnector class attributes and methods

# pcm_pc_av_composition_pc_av_AssemblyContext class attributes and methods

# RepositoryComponent class attributes and methods

# VariableUsage class attributes and methods

# pcm_pc_av_usagemodel_pc_av_Workload class attributes and methods

# UsageScenario class attributes and methods

# pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector class attributes and methods

# InfrastructureProvidedRole class attributes and methods

# InfrastructureRequiredRole class attributes and methods

# pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector class attributes and methods

# pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector class attributes and methods

# pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector class attributes and methods

# OperationSignature class attributes and methods

# pcm_pc_av_usagemodel_pc_av_UsageScenario class attributes and methods

# UsageModel class attributes and methods

# ScenarioBehaviour class attributes and methods

# Workload class attributes and methods

# pcm_pc_av_usagemodel_pc_av_UserData class attributes and methods

# pcm_pc_av_usagemodel_pc_av_UsageModel class attributes and methods

# UserData class attributes and methods

# pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall class attributes and methods
pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall_priority: Property = Property(name="priority", type=IntegerType)
pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole: Method = Method(name="EntryLevelSystemCallSignatureMustMatchItsProvidedRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem: Method = Method(name="EntryLevelSystemCallMustReferenceProvidedRoleOfASystem", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall.attributes={pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall_priority}
pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall.methods={pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem, pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole}

# AbstractUserAction class attributes and methods

# BranchTransition class attributes and methods

# pcm_pc_av_usagemodel_pc_av_BranchTransition class attributes and methods
pcm_pc_av_usagemodel_pc_av_BranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_pc_av_usagemodel_pc_av_BranchTransition.attributes={pcm_pc_av_usagemodel_pc_av_BranchTransition_branchProbability}

# Branch class attributes and methods

# pcm_pc_av_usagemodel_pc_av_AbstractUserAction class attributes and methods

# pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour class attributes and methods
pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour_m_Exactlyonestart: Method = Method(name="Exactlyonestart", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour_m_Exactlyonestop: Method = Method(name="Exactlyonestop", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor: Method = Method(name="EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour.methods={pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour_m_Exactlyonestop, pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor, pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour_m_Exactlyonestart}

# pcm_pc_av_usagemodel_pc_av_Start class attributes and methods
pcm_pc_av_usagemodel_pc_av_Start_m_StartHasNoPredecessor: Method = Method(name="StartHasNoPredecessor", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_Start.methods={pcm_pc_av_usagemodel_pc_av_Start_m_StartHasNoPredecessor}

# pcm_pc_av_usagemodel_pc_av_OpenWorkload class attributes and methods
pcm_pc_av_usagemodel_pc_av_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified: Method = Method(name="InterArrivalTimeInOpenWorkloadNeedsToBeSpecified", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_OpenWorkload.methods={pcm_pc_av_usagemodel_pc_av_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified}

# pcm_pc_av_usagemodel_pc_av_Branch class attributes and methods
pcm_pc_av_usagemodel_pc_av_Branch_m_AllBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_Branch.methods={pcm_pc_av_usagemodel_pc_av_Branch_m_AllBranchProbabilitiesMustSumUpTo1}

# pcm_pc_av_usagemodel_pc_av_Loop class attributes and methods

# pcm_pc_av_usagemodel_pc_av_Stop class attributes and methods
pcm_pc_av_usagemodel_pc_av_Stop_m_StopHasNoSuccessor: Method = Method(name="StopHasNoSuccessor", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_Stop.methods={pcm_pc_av_usagemodel_pc_av_Stop_m_StopHasNoSuccessor}

# pcm_pc_av_repository_pc_av_PassiveResource class attributes and methods

# BasicComponent class attributes and methods

# ResourceTimeoutFailureType class attributes and methods

# pcm_pc_av_repository_pc_av_BasicComponent class attributes and methods
pcm_pc_av_repository_pc_av_BasicComponent_m_NoSeffTypeUsedTwice: Method = Method(name="NoSeffTypeUsedTwice", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_repository_pc_av_BasicComponent_m_ProvideSameInterfacesAsImplementationType: Method = Method(name="ProvideSameInterfacesAsImplementationType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_repository_pc_av_BasicComponent_m_RequireSameInterfacesAsImplementationType: Method = Method(name="RequireSameInterfacesAsImplementationType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_repository_pc_av_BasicComponent.methods={pcm_pc_av_repository_pc_av_BasicComponent_m_NoSeffTypeUsedTwice, pcm_pc_av_repository_pc_av_BasicComponent_m_RequireSameInterfacesAsImplementationType, pcm_pc_av_repository_pc_av_BasicComponent_m_ProvideSameInterfacesAsImplementationType}

# ImplementationComponentType class attributes and methods

# pcm_pc_av_usagemodel_pc_av_Delay class attributes and methods

# pcm_pc_av_usagemodel_pc_av_ClosedWorkload class attributes and methods
pcm_pc_av_usagemodel_pc_av_ClosedWorkload_population: Property = Property(name="population", type=IntegerType)
pcm_pc_av_usagemodel_pc_av_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified: Method = Method(name="PopulationInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified: Method = Method(name="ThinkTimeInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_ClosedWorkload.attributes={pcm_pc_av_usagemodel_pc_av_ClosedWorkload_population}
pcm_pc_av_usagemodel_pc_av_ClosedWorkload.methods={pcm_pc_av_usagemodel_pc_av_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified, pcm_pc_av_usagemodel_pc_av_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified}

# CompleteComponentType class attributes and methods

# ServiceEffectSpecification class attributes and methods

# pcm_pc_av_repository_pc_av_ImplementationComponentType class attributes and methods
pcm_pc_av_repository_pc_av_ImplementationComponentType_componentType: Property = Property(name="componentType", type=StringType)
pcm_pc_av_repository_pc_av_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType: Method = Method(name="providedInterfacesHaveToConformToCompleteType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_repository_pc_av_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType: Method = Method(name="ProvidedInterfaceHaveToConformToComponentType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_repository_pc_av_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType: Method = Method(name="RequiredInterfacesHaveToConformToCompleteType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_repository_pc_av_ImplementationComponentType.attributes={pcm_pc_av_repository_pc_av_ImplementationComponentType_componentType}
pcm_pc_av_repository_pc_av_ImplementationComponentType.methods={pcm_pc_av_repository_pc_av_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType, pcm_pc_av_repository_pc_av_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType, pcm_pc_av_repository_pc_av_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType}

# ResourceSignature class attributes and methods

# pcm_pc_av_repository_pc_av_DataType class attributes and methods

# pcm_pc_av_repository_pc_av_Repository class attributes and methods
pcm_pc_av_repository_pc_av_Repository_repositoryDescription: Property = Property(name="repositoryDescription", type=StringType)
pcm_pc_av_repository_pc_av_Repository.attributes={pcm_pc_av_repository_pc_av_Repository_repositoryDescription}

# pcm_pc_av_repository_pc_av_RepositoryComponent class attributes and methods

# InterfaceProvidingRequiringEntity class attributes and methods

# Repository class attributes and methods

# pcm_pc_av_repository_pc_av_ProvidedRole class attributes and methods

# pcm_pc_av_repository_pc_av_Parameter class attributes and methods
pcm_pc_av_repository_pc_av_Parameter_modifier__Parameter: Property = Property(name="modifier__Parameter", type=StringType)
pcm_pc_av_repository_pc_av_Parameter_parameterName: Property = Property(name="parameterName", type=StringType)
pcm_pc_av_repository_pc_av_Parameter.attributes={pcm_pc_av_repository_pc_av_Parameter_parameterName, pcm_pc_av_repository_pc_av_Parameter_modifier__Parameter}

# DataType class attributes and methods

# InfrastructureSignature class attributes and methods

# EventType class attributes and methods

# Protocol class attributes and methods

# RequiredCharacterisation class attributes and methods

# pcm_pc_av_repository_pc_av_RequiredCharacterisation class attributes and methods
pcm_pc_av_repository_pc_av_RequiredCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_pc_av_repository_pc_av_RequiredCharacterisation.attributes={pcm_pc_av_repository_pc_av_RequiredCharacterisation_type}

# Parameter class attributes and methods

# Interface class attributes and methods

# FailureType class attributes and methods

# pcm_pc_av_repository_pc_av_Interface class attributes and methods
pcm_pc_av_repository_pc_av_Interface_m_NoProtocolTypeIDUsedTwice: Method = Method(name="NoProtocolTypeIDUsedTwice", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_repository_pc_av_Interface.methods={pcm_pc_av_repository_pc_av_Interface_m_NoProtocolTypeIDUsedTwice}

# pcm_pc_av_repository_pc_av_InfrastructureSignature class attributes and methods

# InfrastructureInterface class attributes and methods

# pcm_pc_av_repository_pc_av_InfrastructureInterface class attributes and methods

# pcm_pc_av_repository_pc_av_InfrastructureRequiredRole class attributes and methods

# pcm_pc_av_repository_pc_av_RequiredRole class attributes and methods

# pcm_pc_av_repository_pc_av_EventGroup class attributes and methods

# pcm_pc_av_repository_pc_av_EventType class attributes and methods

# Signature class attributes and methods

# pcm_pc_av_repository_pc_av_Signature class attributes and methods

# ExceptionType class attributes and methods

# pcm_pc_av_repository_pc_av_ExceptionType class attributes and methods
pcm_pc_av_repository_pc_av_ExceptionType_exceptionName: Property = Property(name="exceptionName", type=StringType)
pcm_pc_av_repository_pc_av_ExceptionType_exceptionMessage: Property = Property(name="exceptionMessage", type=StringType)
pcm_pc_av_repository_pc_av_ExceptionType.attributes={pcm_pc_av_repository_pc_av_ExceptionType_exceptionMessage, pcm_pc_av_repository_pc_av_ExceptionType_exceptionName}

# pcm_pc_av_repository_pc_av_OperationRequiredRole class attributes and methods

# pcm_pc_av_repository_pc_av_SourceRole class attributes and methods

# pcm_pc_av_repository_pc_av_SinkRole class attributes and methods

# pcm_pc_av_repository_pc_av_OperationSignature class attributes and methods
pcm_pc_av_repository_pc_av_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature: Method = Method(name="ParameterNamesHaveToBeUniqueForASignature", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_repository_pc_av_OperationSignature.methods={pcm_pc_av_repository_pc_av_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature}

# OperationInterface class attributes and methods

# pcm_pc_av_repository_pc_av_OperationInterface class attributes and methods
pcm_pc_av_repository_pc_av_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface: Method = Method(name="SignaturesHaveToBeUniqueForAnInterface", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_repository_pc_av_OperationInterface.methods={pcm_pc_av_repository_pc_av_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface}

# ProvidesComponentType class attributes and methods

# pcm_pc_av_repository_pc_av_ProvidesComponentType class attributes and methods
pcm_pc_av_repository_pc_av_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_repository_pc_av_ProvidesComponentType.methods={pcm_pc_av_repository_pc_av_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType}

# pcm_pc_av_repository_pc_av_OperationProvidedRole class attributes and methods

# pcm_pc_av_repository_pc_av_InfrastructureProvidedRole class attributes and methods

# pcm_pc_av_repository_pc_av_CompleteComponentType class attributes and methods
pcm_pc_av_repository_pc_av_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_repository_pc_av_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2: Method = Method(name="providedInterfacesHaveToConformToProvidedType2", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_repository_pc_av_CompleteComponentType.methods={pcm_pc_av_repository_pc_av_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType, pcm_pc_av_repository_pc_av_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2}

# pcm_pc_av_repository_pc_av_CollectionDataType class attributes and methods

# repository_pc_av_DataType class attributes and methods

# pcm_pc_av_repository_pc_av_CompositeDataType class attributes and methods

# CompositeDataType class attributes and methods

# InnerDeclaration class attributes and methods

# pcm_pc_av_repository_pc_av_CompositeComponent class attributes and methods
pcm_pc_av_repository_pc_av_CompositeComponent_m_ProvideSameInterfaces: Method = Method(name="ProvideSameInterfaces", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_repository_pc_av_CompositeComponent_m_RequireSameInterfaces: Method = Method(name="RequireSameInterfaces", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_repository_pc_av_CompositeComponent.methods={pcm_pc_av_repository_pc_av_CompositeComponent_m_RequireSameInterfaces, pcm_pc_av_repository_pc_av_CompositeComponent_m_ProvideSameInterfaces}

# entity_pc_av_ComposedProvidingRequiringEntity class attributes and methods

# repository_pc_av_ImplementationComponentType class attributes and methods

# pcm_pc_av_repository_pc_av_PrimitiveDataType class attributes and methods
pcm_pc_av_repository_pc_av_PrimitiveDataType_type: Property = Property(name="type", type=StringType)
pcm_pc_av_repository_pc_av_PrimitiveDataType.attributes={pcm_pc_av_repository_pc_av_PrimitiveDataType_type}

# HardwareInducedFailureType class attributes and methods

# pcm_pc_av_resourcetype_pc_av_ResourceType class attributes and methods

# UnitCarryingElement class attributes and methods

# ResourceRepository class attributes and methods

# pcm_pc_av_resourcetype_pc_av_ResourceRepository class attributes and methods

# SchedulingPolicy class attributes and methods

# pcm_pc_av_repository_pc_av_InnerDeclaration class attributes and methods

# NamedElement class attributes and methods

# pcm_pc_av_resourcetype_pc_av_SchedulingPolicy class attributes and methods

# pcm_pc_av_resourcetype_pc_av_CommunicationLinkResourceType class attributes and methods

# pcm_pc_av_repository_pc_av_Role class attributes and methods

# NetworkInducedFailureType class attributes and methods

# pcm_pc_av_resourcetype_pc_av_ResourceInterface class attributes and methods

# pcm_pc_av_resourcetype_pc_av_ResourceSignature class attributes and methods
pcm_pc_av_resourcetype_pc_av_ResourceSignature_resourceServiceId: Property = Property(name="resourceServiceId", type=IntegerType)
pcm_pc_av_resourcetype_pc_av_ResourceSignature.attributes={pcm_pc_av_resourcetype_pc_av_ResourceSignature_resourceServiceId}

# pcm_pc_av_resourcetype_pc_av_ProcessingResourceType class attributes and methods

# ResourceType class attributes and methods

# pcm_pc_av_protocol_pc_av_Protocol class attributes and methods
pcm_pc_av_protocol_pc_av_Protocol_protocolTypeID: Property = Property(name="protocolTypeID", type=StringType)
pcm_pc_av_protocol_pc_av_Protocol.attributes={pcm_pc_av_protocol_pc_av_Protocol_protocolTypeID}

# pcm_pc_av_parameter_pc_av_VariableUsage class attributes and methods

# CallAction class attributes and methods

# SynchronisationPoint class attributes and methods

# CallReturnAction class attributes and methods

# SetVariableAction class attributes and methods

# SpecifiedOutputParameterAbstraction class attributes and methods

# parameter_pc_av_pcm_pc_av_AbstractNamedReference class attributes and methods

# pcm_pc_av_parameter_pc_av_VariableCharacterisation class attributes and methods
pcm_pc_av_parameter_pc_av_VariableCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_pc_av_parameter_pc_av_VariableCharacterisation.attributes={pcm_pc_av_parameter_pc_av_VariableCharacterisation_type}

# pcm_pc_av_parameter_pc_av_CharacterisedVariable class attributes and methods
pcm_pc_av_parameter_pc_av_CharacterisedVariable_characterisationType: Property = Property(name="characterisationType", type=StringType)
pcm_pc_av_parameter_pc_av_CharacterisedVariable.attributes={pcm_pc_av_parameter_pc_av_CharacterisedVariable_characterisationType}

# Variable class attributes and methods

# pcm_pc_av_reliability_pc_av_FailureOccurrenceDescription class attributes and methods
pcm_pc_av_reliability_pc_av_FailureOccurrenceDescription_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_pc_av_reliability_pc_av_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange: Method = Method(name="EnsureValidFailureProbabilityRange", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_reliability_pc_av_FailureOccurrenceDescription.attributes={pcm_pc_av_reliability_pc_av_FailureOccurrenceDescription_failureProbability}
pcm_pc_av_reliability_pc_av_FailureOccurrenceDescription.methods={pcm_pc_av_reliability_pc_av_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange}

# EntryLevelSystemCall class attributes and methods

# ProcessingResourceType class attributes and methods

# pcm_pc_av_reliability_pc_av_SoftwareInducedFailureType class attributes and methods

# InternalFailureOccurrenceDescription class attributes and methods

# pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription class attributes and methods
pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription.methods={pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription}

# FailureOccurrenceDescription class attributes and methods

# InternalAction class attributes and methods

# SoftwareInducedFailureType class attributes and methods

# pcm_pc_av_reliability_pc_av_NetworkInducedFailureType class attributes and methods
pcm_pc_av_reliability_pc_av_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType: Method = Method(name="NetworkInducedFailureTypeHasCommunicationLinkResourceType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_reliability_pc_av_NetworkInducedFailureType.methods={pcm_pc_av_reliability_pc_av_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType}

# CommunicationLinkResourceType class attributes and methods

# pcm_pc_av_reliability_pc_av_HardwareInducedFailureType class attributes and methods
pcm_pc_av_reliability_pc_av_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType: Method = Method(name="HardwareInducedFailureTypeHasProcessingResourceType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_reliability_pc_av_HardwareInducedFailureType.methods={pcm_pc_av_reliability_pc_av_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType}

# qos_reliability_pc_av_SpecifiedReliabilityAnnotation class attributes and methods

# pcm_pc_av_reliability_pc_av_ResourceTimeoutFailureType class attributes and methods

# pcm_pc_av_reliability_pc_av_FailureType class attributes and methods

# pcm_pc_av_seff_pc_av_StopAction class attributes and methods
pcm_pc_av_seff_pc_av_StopAction_m_StopActionSuccessorMustNotBeDefined: Method = Method(name="StopActionSuccessorMustNotBeDefined", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_seff_pc_av_StopAction.methods={pcm_pc_av_seff_pc_av_StopAction_m_StopActionSuccessorMustNotBeDefined}

# AbstractInternalControlFlowAction class attributes and methods

# pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction class attributes and methods

# AbstractAction class attributes and methods

# pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription class attributes and methods
pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription.methods={pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription}

# pcm_pc_av_seff_pc_av_AbstractAction class attributes and methods

# ResourceDemandingBehaviour class attributes and methods

# pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour class attributes and methods
pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour_m_ExactlyOneStopAction: Method = Method(name="ExactlyOneStopAction", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour_m_ExactlyOneStartAction: Method = Method(name="ExactlyOneStartAction", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor: Method = Method(name="EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour.methods={pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor, pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour_m_ExactlyOneStartAction, pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour_m_ExactlyOneStopAction}

# AbstractLoopAction class attributes and methods

# pcm_pc_av_seff_pc_av_AbstractLoopAction class attributes and methods

# pcm_pc_av_seff_pc_av_AbstractBranchTransition class attributes and methods

# BranchAction class attributes and methods

# pcm_pc_av_seff_pc_av_BranchAction class attributes and methods
pcm_pc_av_seff_pc_av_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions: Method = Method(name="EitherGuardedBranchesOrProbabilisiticBranchTransitions", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_seff_pc_av_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllProbabilisticBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_seff_pc_av_BranchAction.methods={pcm_pc_av_seff_pc_av_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1, pcm_pc_av_seff_pc_av_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions}

# pcm_pc_av_seff_pc_av_CallAction class attributes and methods

# pcm_pc_av_seff_pc_av_StartAction class attributes and methods
pcm_pc_av_seff_pc_av_StartAction_m_StartActionPredecessorMustNotBeDefined: Method = Method(name="StartActionPredecessorMustNotBeDefined", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_seff_pc_av_StartAction.methods={pcm_pc_av_seff_pc_av_StartAction_m_StartActionPredecessorMustNotBeDefined}

# AbstractBranchTransition class attributes and methods

# pcm_pc_av_seff_pc_av_ServiceEffectSpecification class attributes and methods
pcm_pc_av_seff_pc_av_ServiceEffectSpecification_seffTypeID: Property = Property(name="seffTypeID", type=StringType)
pcm_pc_av_seff_pc_av_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole: Method = Method(name="ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_seff_pc_av_ServiceEffectSpecification.attributes={pcm_pc_av_seff_pc_av_ServiceEffectSpecification_seffTypeID}
pcm_pc_av_seff_pc_av_ServiceEffectSpecification.methods={pcm_pc_av_seff_pc_av_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole}

# pcm_pc_av_seff_pc_av_ResourceDemandingSEFF class attributes and methods

# seff_pc_av_ServiceEffectSpecification class attributes and methods

# seff_pc_av_ResourceDemandingBehaviour class attributes and methods

# ResourceDemandingInternalBehaviour class attributes and methods

# pcm_pc_av_seff_pc_av_ResourceDemandingInternalBehaviour class attributes and methods

# pcm_pc_av_seff_pc_av_LoopAction class attributes and methods

# pcm_pc_av_seff_pc_av_ForkAction class attributes and methods

# ForkedBehaviour class attributes and methods

# pcm_pc_av_seff_pc_av_ForkedBehaviour class attributes and methods

# ForkAction class attributes and methods

# pcm_pc_av_seff_pc_av_SynchronisationPoint class attributes and methods

# pcm_pc_av_seff_pc_av_ExternalCallAction class attributes and methods
pcm_pc_av_seff_pc_av_ExternalCallAction_retryCount: Property = Property(name="retryCount", type=IntegerType)
pcm_pc_av_seff_pc_av_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer: Method = Method(name="OperationRequiredRoleMustBeReferencedByContainer", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_seff_pc_av_ExternalCallAction_m_SignatureBelongsToRole: Method = Method(name="SignatureBelongsToRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_seff_pc_av_ExternalCallAction.attributes={pcm_pc_av_seff_pc_av_ExternalCallAction_retryCount}
pcm_pc_av_seff_pc_av_ExternalCallAction.methods={pcm_pc_av_seff_pc_av_ExternalCallAction_m_SignatureBelongsToRole, pcm_pc_av_seff_pc_av_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer}

# seff_pc_av_AbstractAction class attributes and methods

# seff_pc_av_CallReturnAction class attributes and methods

# ResourceDemandingSEFF class attributes and methods

# seff_reliability_pc_av_FailureHandlingEntity class attributes and methods

# pcm_pc_av_seff_pc_av_ReleaseAction class attributes and methods

# pcm_pc_av_seff_pc_av_CollectionIteratorAction class attributes and methods

# pcm_pc_av_seff_pc_av_GuardedBranchTransition class attributes and methods

# pcm_pc_av_seff_pc_av_CallReturnAction class attributes and methods

# pcm_pc_av_seff_pc_av_ProbabilisticBranchTransition class attributes and methods
pcm_pc_av_seff_pc_av_ProbabilisticBranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_pc_av_seff_pc_av_ProbabilisticBranchTransition.attributes={pcm_pc_av_seff_pc_av_ProbabilisticBranchTransition_branchProbability}

# pcm_pc_av_seff_pc_av_AcquireAction class attributes and methods
pcm_pc_av_seff_pc_av_AcquireAction_timeoutValue: Property = Property(name="timeoutValue", type=FloatType)
pcm_pc_av_seff_pc_av_AcquireAction_timeout: Property = Property(name="timeout", type=BooleanType)
pcm_pc_av_seff_pc_av_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative: Method = Method(name="TimeoutValueOfAcquireActionMustNotBeNegative", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_seff_pc_av_AcquireAction.attributes={pcm_pc_av_seff_pc_av_AcquireAction_timeout, pcm_pc_av_seff_pc_av_AcquireAction_timeoutValue}
pcm_pc_av_seff_pc_av_AcquireAction.methods={pcm_pc_av_seff_pc_av_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative}

# pcm_pc_av_seff_pc_av_InternalAction class attributes and methods
pcm_pc_av_seff_pc_av_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_seff_pc_av_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfInternalActionFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_seff_pc_av_InternalAction.methods={pcm_pc_av_seff_pc_av_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed, pcm_pc_av_seff_pc_av_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1}

# pcm_pc_av_seff_pc_av_SetVariableAction class attributes and methods

# pcm_pc_av_seff_pc_av_InternalCallAction class attributes and methods

# seff_pc_av_CallAction class attributes and methods

# seff_pc_av_AbstractInternalControlFlowAction class attributes and methods

# pcm_pc_av_seff_pc_av_EmitEventAction class attributes and methods

# pcm_pc_av_seff_performance_pc_av_InfrastructureCall class attributes and methods
pcm_pc_av_seff_performance_pc_av_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole: Method = Method(name="SignatureMustBelongToUsedRequiredRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_seff_performance_pc_av_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent: Method = Method(name="ReferencedRequiredRoleMustBeRequiredByComponent", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_seff_performance_pc_av_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_seff_performance_pc_av_InfrastructureCall.methods={pcm_pc_av_seff_performance_pc_av_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction, pcm_pc_av_seff_performance_pc_av_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole, pcm_pc_av_seff_performance_pc_av_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent}

# pcm_pc_av_seff_performance_pc_av_ResourceCall class attributes and methods
pcm_pc_av_seff_performance_pc_av_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole: Method = Method(name="ResourceSignatureBelongsToResourceRequiredRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_seff_performance_pc_av_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent: Method = Method(name="ResourceRequiredRoleMustBeReferencedByComponent", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_seff_performance_pc_av_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_seff_performance_pc_av_ResourceCall.methods={pcm_pc_av_seff_performance_pc_av_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent, pcm_pc_av_seff_performance_pc_av_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole, pcm_pc_av_seff_performance_pc_av_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction}

# pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand class attributes and methods
pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand.methods={pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction}

# pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour class attributes and methods
pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself: Method = Method(name="RecoveryActionBehaviourIsNotSuccessorOfItself", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes: Method = Method(name="SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor: Method = Method(name="RecoveryActionBehaviourHasOnlyOnePredecessor", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour.methods={pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes, pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself, pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor}

# pcm_pc_av_seff_reliability_pc_av_FailureHandlingEntity class attributes and methods

# pcm_pc_av_qosannotations_pc_av_SpecifiedQoSAnnotation class attributes and methods

# seff_reliability_pc_av_RecoveryActionBehaviour class attributes and methods

# seff_reliability_pc_av_RecoveryAction class attributes and methods

# pcm_pc_av_seff_reliability_pc_av_RecoveryAction class attributes and methods
pcm_pc_av_seff_reliability_pc_av_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet: Method = Method(name="PrimaryBehaviourOfRecoveryActionMustBeSet", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_seff_reliability_pc_av_RecoveryAction.methods={pcm_pc_av_seff_reliability_pc_av_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet}

# System class attributes and methods

# SpecifiedQoSAnnotation class attributes and methods

# QoSAnnotations class attributes and methods

# pcm_pc_av_qosannotations_pc_av_QoSAnnotations class attributes and methods
pcm_pc_av_qosannotations_pc_av_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed: Method = Method(name="MultipleReliabilityAnnotationsPerExternalCallNotAllowed", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_qosannotations_pc_av_QoSAnnotations.methods={pcm_pc_av_qosannotations_pc_av_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed}

# pcm_pc_av_qos_performance_pc_av_SystemSpecifiedExecutionTime class attributes and methods
pcm_pc_av_qos_performance_pc_av_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem: Method = Method(name="SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_qos_performance_pc_av_SystemSpecifiedExecutionTime.methods={pcm_pc_av_qos_performance_pc_av_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem}

# SpecifiedExecutionTime class attributes and methods

# pcm_pc_av_qos_performance_pc_av_SpecifiedExecutionTime class attributes and methods

# pcm_pc_av_qos_performance_pc_av_ComponentSpecifiedExecutionTime class attributes and methods

# pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction class attributes and methods

# ExternalFailureOccurrenceDescription class attributes and methods

# pcm_pc_av_system_pc_av_System class attributes and methods
pcm_pc_av_system_pc_av_System_m_SystemMustHaveAtLeastOneProvidedRole: Method = Method(name="SystemMustHaveAtLeastOneProvidedRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_system_pc_av_System.methods={pcm_pc_av_system_pc_av_System_m_SystemMustHaveAtLeastOneProvidedRole}

# pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation class attributes and methods
pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem: Method = Method(name="SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation.methods={pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1, pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed, pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem}

# pcm_pc_av_resourceenvironment_pc_av_ResourceContainer class attributes and methods

# pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification class attributes and methods
pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification_MTTR: Property = Property(name="MTTR", type=FloatType)
pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification_MTTF: Property = Property(name="MTTF", type=FloatType)
pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification_requiredByContainer: Property = Property(name="requiredByContainer", type=BooleanType)
pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification_numberOfReplicas: Property = Property(name="numberOfReplicas", type=IntegerType)
pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification.attributes={pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification_requiredByContainer, pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification_MTTF, pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification_numberOfReplicas, pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification_MTTR}

# pcm_pc_av_resourceenvironment_pc_av_ResourceEnvironment class attributes and methods

# LinkingResource class attributes and methods

# ResourceContainer class attributes and methods

# pcm_pc_av_resourceenvironment_pc_av_LinkingResource class attributes and methods

# ResourceEnvironment class attributes and methods

# pcm_pc_av_allocation_pc_av_AllocationContext class attributes and methods
pcm_pc_av_allocation_pc_av_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred: Method = Method(name="OneAssemblyContextOrOneEventChannelShouldBeReferred", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_av_allocation_pc_av_AllocationContext.methods={pcm_pc_av_allocation_pc_av_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred}

# Allocation class attributes and methods

# pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification class attributes and methods
pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification.attributes={pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification_failureProbability}

# AllocationContext class attributes and methods

# pcm_pc_av_subsystem_pc_av_SubSystem class attributes and methods

# repository_pc_av_RepositoryComponent class attributes and methods

# pcm_pc_av_completions_pc_av_Completion class attributes and methods

# pcm_pc_av_completions_pc_av_CompletionRepository class attributes and methods

# pcm_pc_av_allocation_pc_av_Allocation class attributes and methods
pcm_pc_av_allocation_pc_av_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce: Method = Method(name="EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_allocation_pc_av_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource: Method = Method(name="CommunicatingServersHaveToBeConnectedByLinkingResource", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_av_allocation_pc_av_Allocation.methods={pcm_pc_av_allocation_pc_av_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource, pcm_pc_av_allocation_pc_av_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce}

# Completion class attributes and methods

# pcm_pc_av_completions_pc_av_DelegatingExternalCallAction class attributes and methods

# ExternalCallAction class attributes and methods

# pcm_pc_av_completions_pc_av_NetworkDemandParametricResourceDemand class attributes and methods

# ParametricResourceDemand class attributes and methods

# Relationships
scopedObject5: BinaryAssociation = BinaryAssociation(
    name="scopedObject5",
    ends={
        Property(name="pcm_pc_av_EObject6", type=pcm_pc_av_PerJoinPointScope, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_PerJoinPointScope", type=pcm_pc_av_EObject, multiplicity=Multiplicity(1, 1))
    }
)
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="pcm_pc_av_EObject", type=pcm_pc_av_Pointcut, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_Pointcut", type=pcm_pc_av_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children1: BinaryAssociation = BinaryAssociation(
    name="children1",
    ends={
        Property(name="pcm_pc_av_EObject2", type=pcm_pc_av_Advice, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_Advice", type=pcm_pc_av_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scopedObject3: BinaryAssociation = BinaryAssociation(
    name="scopedObject3",
    ends={
        Property(name="pcm_pc_av_EObject4", type=pcm_pc_av_GlobalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_GlobalScope", type=pcm_pc_av_EObject, multiplicity=Multiplicity(1, 1))
    }
)
loop_LoopIteration26: BinaryAssociation = BinaryAssociation(
    name="loop_LoopIteration26",
    ends={
        Property(name="usagemodel_pc_av27", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Loop", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
openWorkload_PCMRandomVariable28: BinaryAssociation = BinaryAssociation(
    name="openWorkload_PCMRandomVariable28",
    ends={
        Property(name="usagemodel_pc_av29", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="OpenWorkload", type=OpenWorkload, multiplicity=Multiplicity(0, 1))
    }
)
delay_TimeSpecification30: BinaryAssociation = BinaryAssociation(
    name="delay_TimeSpecification30",
    ends={
        Property(name="usagemodel_pc_av31", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Delay", type=Delay, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecifcation_throughput_PCMRandomVariable32: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifcation_throughput_PCMRandomVariable32",
    ends={
        Property(name="resourceenvironment_pc_av", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceSpecification_processingRate_PCMRandomVariable33: BinaryAssociation = BinaryAssociation(
    name="processingResourceSpecification_processingRate_PCMRandomVariable33",
    ends={
        Property(name="resourceenvironment_pc_av34", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcessingResourceSpecification", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecification_latency_PCMRandomVariable35: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecification_latency_PCMRandomVariable35",
    ends={
        Property(name="resourceenvironment_pc_av37", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceSpecification36", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
closedWorkload_PCMRandomVariable7: BinaryAssociation = BinaryAssociation(
    name="closedWorkload_PCMRandomVariable7",
    ends={
        Property(name="usagemodel_pc_av", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ClosedWorkload", type=ClosedWorkload, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_capacity_PCMRandomVariable8: BinaryAssociation = BinaryAssociation(
    name="passiveResource_capacity_PCMRandomVariable8",
    ends={
        Property(name="repository_pc_av", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
variableCharacterisation_Specification9: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_Specification9",
    ends={
        Property(name="parameter_pc_av", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableCharacterisation", type=VariableCharacterisation, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureCall__PCMRandomVariable10: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__PCMRandomVariable10",
    ends={
        Property(name="seff_pc_av", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_pc_av", type=seff_performance_pc_av_InfrastructureCall, multiplicity=Multiplicity(0, 1))
    }
)
resourceCall__PCMRandomVariable11: BinaryAssociation = BinaryAssociation(
    name="resourceCall__PCMRandomVariable11",
    ends={
        Property(name="seff_pc_av13", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_pc_av12", type=seff_performance_pc_av_ResourceCall, multiplicity=Multiplicity(0, 1))
    }
)
parametricResourceDemand_PCMRandomVariable14: BinaryAssociation = BinaryAssociation(
    name="parametricResourceDemand_PCMRandomVariable14",
    ends={
        Property(name="seff_pc_av16", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_pc_av15", type=seff_performance_pc_av_ParametricResourceDemand, multiplicity=Multiplicity(0, 1))
    }
)
loopAction_PCMRandomVariable17: BinaryAssociation = BinaryAssociation(
    name="loopAction_PCMRandomVariable17",
    ends={
        Property(name="seff_pc_av18", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopAction", type=LoopAction, multiplicity=Multiplicity(0, 1))
    }
)
guardedBranchTransition_PCMRandomVariable19: BinaryAssociation = BinaryAssociation(
    name="guardedBranchTransition_PCMRandomVariable19",
    ends={
        Property(name="seff_pc_av20", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="GuardedBranchTransition", type=GuardedBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
specifiedExecutionTime_PCMRandomVariable21: BinaryAssociation = BinaryAssociation(
    name="specifiedExecutionTime_PCMRandomVariable21",
    ends={
        Property(name="qosannotations_pc_av", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="qos_performance_pc_av", type=qos_performance_pc_av_SpecifiedExecutionTime, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSinkConnector__FilterCondition22: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__FilterCondition22",
    ends={
        Property(name="core_pc_av", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_av", type=composition_pc_av_EventChannelSinkConnector, multiplicity=Multiplicity(0, 1))
    }
)
assemblyEventConnector__FilterCondition23: BinaryAssociation = BinaryAssociation(
    name="assemblyEventConnector__FilterCondition23",
    ends={
        Property(name="core_pc_av25", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_av24", type=composition_pc_av_AssemblyEventConnector, multiplicity=Multiplicity(0, 1))
    }
)
resourceProvidedRoles__ResourceInterfaceProvidingEntity53: BinaryAssociation = BinaryAssociation(
    name="resourceProvidedRoles__ResourceInterfaceProvidingEntity53",
    ends={
        Property(name="core_pc_av55", type=pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_pc_av54", type=entity_pc_av_ResourceProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceInterfaceProvidingEntity__ResourceProvidedRole38: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceProvidingEntity__ResourceProvidedRole38",
    ends={
        Property(name="core_pc_av39", type=pcm_pc_av_entity_pc_av_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_pc_av", type=entity_pc_av_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
providedResourceInterface__ResourceProvidedRole40: BinaryAssociation = BinaryAssociation(
    name="providedResourceInterface__ResourceProvidedRole40",
    ends={
        Property(name="ResourceInterface", type=pcm_pc_av_entity_pc_av_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_entity_pc_av_ResourceProvidedRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedRoles_InterfaceProvidingEntity41: BinaryAssociation = BinaryAssociation(
    name="providedRoles_InterfaceProvidingEntity41",
    ends={
        Property(name="repository_pc_av42", type=pcm_pc_av_entity_pc_av_InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="ProvidedRole", type=ProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredRoles_InterfaceRequiringEntity43: BinaryAssociation = BinaryAssociation(
    name="requiredRoles_InterfaceRequiringEntity43",
    ends={
        Property(name="repository_pc_av44", type=pcm_pc_av_entity_pc_av_InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="RequiredRole", type=RequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredRoles__ResourceInterfaceRequiringEntity45: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRoles__ResourceInterfaceRequiringEntity45",
    ends={
        Property(name="core_pc_av47", type=pcm_pc_av_entity_pc_av_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_pc_av46", type=entity_pc_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredResourceInterface__ResourceRequiredRole48: BinaryAssociation = BinaryAssociation(
    name="requiredResourceInterface__ResourceRequiredRole48",
    ends={
        Property(name="ResourceInterface49", type=pcm_pc_av_entity_pc_av_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_entity_pc_av_ResourceRequiredRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaceRequiringEntity__ResourceRequiredRole50: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceRequiringEntity__ResourceRequiredRole50",
    ends={
        Property(name="core_pc_av52", type=pcm_pc_av_entity_pc_av_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_pc_av51", type=entity_pc_av_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContexts__ComposedStructure59: BinaryAssociation = BinaryAssociation(
    name="assemblyContexts__ComposedStructure59",
    ends={
        Property(name="core_pc_av61", type=pcm_pc_av_composition_pc_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_av60", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredDelegationConnectors_ComposedStructure62: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredDelegationConnectors_ComposedStructure62",
    ends={
        Property(name="core_pc_av64", type=pcm_pc_av_composition_pc_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_av63", type=composition_pc_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventChannel__ComposedStructure65: BinaryAssociation = BinaryAssociation(
    name="eventChannel__ComposedStructure65",
    ends={
        Property(name="core_pc_av67", type=pcm_pc_av_composition_pc_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_av66", type=composition_pc_av_EventChannel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentStructure__Connector56: BinaryAssociation = BinaryAssociation(
    name="parentStructure__Connector56",
    ends={
        Property(name="core_pc_av58", type=pcm_pc_av_composition_pc_av_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_av57", type=composition_pc_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__EventChannelSinkConnector94: BinaryAssociation = BinaryAssociation(
    name="sinkRole__EventChannelSinkConnector94",
    ends={
        Property(name="SinkRole", type=pcm_pc_av_composition_pc_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_EventChannelSinkConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__EventChannelSinkConnector95: BinaryAssociation = BinaryAssociation(
    name="filterCondition__EventChannelSinkConnector95",
    ends={
        Property(name="core_pc_av96", type=pcm_pc_av_composition_pc_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext__EventChannelSinkConnector97: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSinkConnector97",
    ends={
        Property(name="composition_pc_av_AssemblyContext99", type=pcm_pc_av_composition_pc_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_EventChannelSinkConnector98", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSinkConnector100: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSinkConnector100",
    ends={
        Property(name="core_pc_av102", type=pcm_pc_av_composition_pc_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_av101", type=composition_pc_av_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
connectors__ComposedStructure68: BinaryAssociation = BinaryAssociation(
    name="connectors__ComposedStructure68",
    ends={
        Property(name="core_pc_av70", type=pcm_pc_av_composition_pc_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_av69", type=composition_pc_av_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerResourceRequiredRole_ResourceRequiredDelegationConnector71: BinaryAssociation = BinaryAssociation(
    name="innerResourceRequiredRole_ResourceRequiredDelegationConnector71",
    ends={
        Property(name="entity_pc_av_ResourceRequiredRole", type=pcm_pc_av_composition_pc_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_ResourceRequiredDelegationConnector", type=entity_pc_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerResourceRequiredRole_ResourceRequiredDelegationConnector72: BinaryAssociation = BinaryAssociation(
    name="outerResourceRequiredRole_ResourceRequiredDelegationConnector72",
    ends={
        Property(name="entity_pc_av_ResourceRequiredRole74", type=pcm_pc_av_composition_pc_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_ResourceRequiredDelegationConnector73", type=entity_pc_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure_ResourceRequiredDelegationConnector75: BinaryAssociation = BinaryAssociation(
    name="parentStructure_ResourceRequiredDelegationConnector75",
    ends={
        Property(name="core_pc_av77", type=pcm_pc_av_composition_pc_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_av76", type=composition_pc_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__EventChannel78: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventChannel78",
    ends={
        Property(name="EventGroup", type=pcm_pc_av_composition_pc_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_EventChannel", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSourceConnector__EventChannel79: BinaryAssociation = BinaryAssociation(
    name="eventChannelSourceConnector__EventChannel79",
    ends={
        Property(name="core_pc_av81", type=pcm_pc_av_composition_pc_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_av80", type=composition_pc_av_EventChannelSourceConnector, multiplicity=Multiplicity(0, 9999))
    }
)
eventChannelSinkConnector__EventChannel82: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__EventChannel82",
    ends={
        Property(name="core_pc_av84", type=pcm_pc_av_composition_pc_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_av83", type=composition_pc_av_EventChannelSinkConnector, multiplicity=Multiplicity(0, 9999))
    }
)
parentStructure__EventChannel85: BinaryAssociation = BinaryAssociation(
    name="parentStructure__EventChannel85",
    ends={
        Property(name="core_pc_av87", type=pcm_pc_av_composition_pc_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_av86", type=composition_pc_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EventChannelSourceRole88: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EventChannelSourceRole88",
    ends={
        Property(name="SourceRole", type=pcm_pc_av_composition_pc_av_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_EventChannelSourceConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__EventChannelSourceConnector89: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSourceConnector89",
    ends={
        Property(name="composition_pc_av_AssemblyContext", type=pcm_pc_av_composition_pc_av_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_EventChannelSourceConnector90", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSourceConnector91: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSourceConnector91",
    ends={
        Property(name="core_pc_av93", type=pcm_pc_av_composition_pc_av_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_av92", type=composition_pc_av_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole_RequiredDelegationConnector110: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole_RequiredDelegationConnector110",
    ends={
        Property(name="OperationRequiredRole", type=pcm_pc_av_composition_pc_av_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_RequiredDelegationConnector", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole_RequiredDelegationConnector111: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole_RequiredDelegationConnector111",
    ends={
        Property(name="OperationRequiredRole113", type=pcm_pc_av_composition_pc_av_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_RequiredDelegationConnector112", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_RequiredDelegationConnector114: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_RequiredDelegationConnector114",
    ends={
        Property(name="composition_pc_av_AssemblyContext116", type=pcm_pc_av_composition_pc_av_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_RequiredDelegationConnector115", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole_ProvidedDelegationConnector103: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole_ProvidedDelegationConnector103",
    ends={
        Property(name="OperationProvidedRole", type=pcm_pc_av_composition_pc_av_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_ProvidedDelegationConnector", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole_ProvidedDelegationConnector104: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole_ProvidedDelegationConnector104",
    ends={
        Property(name="OperationProvidedRole106", type=pcm_pc_av_composition_pc_av_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_ProvidedDelegationConnector105", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_ProvidedDelegationConnector107: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ProvidedDelegationConnector107",
    ends={
        Property(name="composition_pc_av_AssemblyContext109", type=pcm_pc_av_composition_pc_av_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_ProvidedDelegationConnector108", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__AssemblyEventConnector130: BinaryAssociation = BinaryAssociation(
    name="sourceRole__AssemblyEventConnector130",
    ends={
        Property(name="SourceRole132", type=pcm_pc_av_composition_pc_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyEventConnector131", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkAssemblyContext__AssemblyEventConnector133: BinaryAssociation = BinaryAssociation(
    name="sinkAssemblyContext__AssemblyEventConnector133",
    ends={
        Property(name="composition_pc_av_AssemblyContext135", type=pcm_pc_av_composition_pc_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyEventConnector134", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
sourceAssemblyContext__AssemblyEventConnector136: BinaryAssociation = BinaryAssociation(
    name="sourceAssemblyContext__AssemblyEventConnector136",
    ends={
        Property(name="composition_pc_av_AssemblyContext138", type=pcm_pc_av_composition_pc_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyEventConnector137", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__AssemblyEventConnector139: BinaryAssociation = BinaryAssociation(
    name="filterCondition__AssemblyEventConnector139",
    ends={
        Property(name="core_pc_av141", type=pcm_pc_av_composition_pc_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable140", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
innerSourceRole__SourceRole142: BinaryAssociation = BinaryAssociation(
    name="innerSourceRole__SourceRole142",
    ends={
        Property(name="SourceRole143", type=pcm_pc_av_composition_pc_av_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_SourceDelegationConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSourceRole__SourceRole144: BinaryAssociation = BinaryAssociation(
    name="outerSourceRole__SourceRole144",
    ends={
        Property(name="SourceRole146", type=pcm_pc_av_composition_pc_av_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_SourceDelegationConnector145", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SourceDelegationConnector147: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SourceDelegationConnector147",
    ends={
        Property(name="composition_pc_av_AssemblyContext149", type=pcm_pc_av_composition_pc_av_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_SourceDelegationConnector148", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext_AssemblyConnector117: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext_AssemblyConnector117",
    ends={
        Property(name="composition_pc_av_AssemblyContext118", type=pcm_pc_av_composition_pc_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyConnector", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext_AssemblyConnector119: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext_AssemblyConnector119",
    ends={
        Property(name="composition_pc_av_AssemblyContext121", type=pcm_pc_av_composition_pc_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyConnector120", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providedRole_AssemblyConnector122: BinaryAssociation = BinaryAssociation(
    name="providedRole_AssemblyConnector122",
    ends={
        Property(name="OperationProvidedRole124", type=pcm_pc_av_composition_pc_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyConnector123", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole_AssemblyConnector125: BinaryAssociation = BinaryAssociation(
    name="requiredRole_AssemblyConnector125",
    ends={
        Property(name="OperationRequiredRole127", type=pcm_pc_av_composition_pc_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyConnector126", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__AssemblyEventConnector128: BinaryAssociation = BinaryAssociation(
    name="sinkRole__AssemblyEventConnector128",
    ends={
        Property(name="SinkRole129", type=pcm_pc_av_composition_pc_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyEventConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole__RequiredResourceDelegationConnector185: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredResourceDelegationConnector185",
    ends={
        Property(name="entity_pc_av_ResourceRequiredRole187", type=pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector186", type=entity_pc_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredResourceDelegationConnector188: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredResourceDelegationConnector188",
    ends={
        Property(name="entity_pc_av_ResourceRequiredRole190", type=pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector189", type=entity_pc_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure__AssemblyContext191: BinaryAssociation = BinaryAssociation(
    name="parentStructure__AssemblyContext191",
    ends={
        Property(name="core_pc_av193", type=pcm_pc_av_composition_pc_av_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_av192", type=composition_pc_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
encapsulatedComponent__AssemblyContext194: BinaryAssociation = BinaryAssociation(
    name="encapsulatedComponent__AssemblyContext194",
    ends={
        Property(name="RepositoryComponent", type=pcm_pc_av_composition_pc_av_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyContext", type=RepositoryComponent, multiplicity=Multiplicity(0, 1))
    }
)
configParameterUsages__AssemblyContext195: BinaryAssociation = BinaryAssociation(
    name="configParameterUsages__AssemblyContext195",
    ends={
        Property(name="parameter_pc_av196", type=pcm_pc_av_composition_pc_av_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_Workload197: BinaryAssociation = BinaryAssociation(
    name="usageScenario_Workload197",
    ends={
        Property(name="usagemodel_pc_av198", type=pcm_pc_av_usagemodel_pc_av_Workload, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SinkDelegationConnector150: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SinkDelegationConnector150",
    ends={
        Property(name="composition_pc_av_AssemblyContext151", type=pcm_pc_av_composition_pc_av_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_SinkDelegationConnector", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerSinkRole__SinkRole152: BinaryAssociation = BinaryAssociation(
    name="innerSinkRole__SinkRole152",
    ends={
        Property(name="SinkRole154", type=pcm_pc_av_composition_pc_av_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_SinkDelegationConnector153", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSinkRole__SinkRole155: BinaryAssociation = BinaryAssociation(
    name="outerSinkRole__SinkRole155",
    ends={
        Property(name="SinkRole157", type=pcm_pc_av_composition_pc_av_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_SinkDelegationConnector156", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
providedRole__AssemblyInfrastructureConnector158: BinaryAssociation = BinaryAssociation(
    name="providedRole__AssemblyInfrastructureConnector158",
    ends={
        Property(name="InfrastructureProvidedRole", type=pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__AssemblyInfrastructureConnector159: BinaryAssociation = BinaryAssociation(
    name="requiredRole__AssemblyInfrastructureConnector159",
    ends={
        Property(name="InfrastructureRequiredRole", type=pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector160", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext__AssemblyInfrastructureConnector161: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext__AssemblyInfrastructureConnector161",
    ends={
        Property(name="composition_pc_av_AssemblyContext163", type=pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector162", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext__AssemblyInfrastructureConnector164: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext__AssemblyInfrastructureConnector164",
    ends={
        Property(name="composition_pc_av_AssemblyContext166", type=pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector165", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole__ProvidedInfrastructureDelegationConnector167: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole__ProvidedInfrastructureDelegationConnector167",
    ends={
        Property(name="InfrastructureProvidedRole168", type=pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole__ProvidedInfrastructureDelegationConnector169: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole__ProvidedInfrastructureDelegationConnector169",
    ends={
        Property(name="InfrastructureProvidedRole171", type=pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector170", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__ProvidedInfrastructureDelegationConnector172: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__ProvidedInfrastructureDelegationConnector172",
    ends={
        Property(name="composition_pc_av_AssemblyContext174", type=pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector173", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole__RequiredInfrastructureDelegationConnector175: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredInfrastructureDelegationConnector175",
    ends={
        Property(name="InfrastructureRequiredRole176", type=pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredInfrastructureDelegationConnector177: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredInfrastructureDelegationConnector177",
    ends={
        Property(name="InfrastructureRequiredRole179", type=pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector178", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredInfrastructureDelegationConnector180: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredInfrastructureDelegationConnector180",
    ends={
        Property(name="composition_pc_av_AssemblyContext182", type=pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector181", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredResourceDelegationConnector183: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredResourceDelegationConnector183",
    ends={
        Property(name="composition_pc_av_AssemblyContext184", type=pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providedRole_EntryLevelSystemCall218: BinaryAssociation = BinaryAssociation(
    name="providedRole_EntryLevelSystemCall218",
    ends={
        Property(name="OperationProvidedRole219", type=pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__EntryLevelSystemCall220: BinaryAssociation = BinaryAssociation(
    name="operationSignature__EntryLevelSystemCall220",
    ends={
        Property(name="OperationSignature", type=pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall221", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
outputParameterUsages_EntryLevelSystemCall222: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsages_EntryLevelSystemCall222",
    ends={
        Property(name="parameter_pc_av224", type=pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage223", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputParameterUsages_EntryLevelSystemCall225: BinaryAssociation = BinaryAssociation(
    name="inputParameterUsages_EntryLevelSystemCall225",
    ends={
        Property(name="parameter_pc_av227", type=pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage226", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageModel_UsageScenario199: BinaryAssociation = BinaryAssociation(
    name="usageModel_UsageScenario199",
    ends={
        Property(name="usagemodel_pc_av200", type=pcm_pc_av_usagemodel_pc_av_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageModel", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_UsageScenario201: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_UsageScenario201",
    ends={
        Property(name="usagemodel_pc_av202", type=pcm_pc_av_usagemodel_pc_av_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
workload_UsageScenario203: BinaryAssociation = BinaryAssociation(
    name="workload_UsageScenario203",
    ends={
        Property(name="usagemodel_pc_av204", type=pcm_pc_av_usagemodel_pc_av_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="Workload", type=Workload, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext_userData205: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_userData205",
    ends={
        Property(name="composition_pc_av_AssemblyContext206", type=pcm_pc_av_usagemodel_pc_av_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_usagemodel_pc_av_UserData", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UserData207: BinaryAssociation = BinaryAssociation(
    name="usageModel_UserData207",
    ends={
        Property(name="usagemodel_pc_av209", type=pcm_pc_av_usagemodel_pc_av_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageModel208", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
userDataParameterUsages_UserData210: BinaryAssociation = BinaryAssociation(
    name="userDataParameterUsages_UserData210",
    ends={
        Property(name="parameter_pc_av212", type=pcm_pc_av_usagemodel_pc_av_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage211", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_UsageModel213: BinaryAssociation = BinaryAssociation(
    name="usageScenario_UsageModel213",
    ends={
        Property(name="usagemodel_pc_av215", type=pcm_pc_av_usagemodel_pc_av_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageScenario214", type=UsageScenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_UsageModel216: BinaryAssociation = BinaryAssociation(
    name="userData_UsageModel216",
    ends={
        Property(name="usagemodel_pc_av217", type=pcm_pc_av_usagemodel_pc_av_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="UserData", type=UserData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_SenarioBehaviour236: BinaryAssociation = BinaryAssociation(
    name="usageScenario_SenarioBehaviour236",
    ends={
        Property(name="usagemodel_pc_av238", type=pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageScenario237", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
branchTransition_ScenarioBehaviour239: BinaryAssociation = BinaryAssociation(
    name="branchTransition_ScenarioBehaviour239",
    ends={
        Property(name="usagemodel_pc_av240", type=pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="BranchTransition", type=BranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
loop_ScenarioBehaviour241: BinaryAssociation = BinaryAssociation(
    name="loop_ScenarioBehaviour241",
    ends={
        Property(name="usagemodel_pc_av243", type=pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="Loop242", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
actions_ScenarioBehaviour244: BinaryAssociation = BinaryAssociation(
    name="actions_ScenarioBehaviour244",
    ends={
        Property(name="usagemodel_pc_av246", type=pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction245", type=AbstractUserAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branch_BranchTransition247: BinaryAssociation = BinaryAssociation(
    name="branch_BranchTransition247",
    ends={
        Property(name="usagemodel_pc_av248", type=pcm_pc_av_usagemodel_pc_av_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="Branch", type=Branch, multiplicity=Multiplicity(0, 1))
    }
)
successor228: BinaryAssociation = BinaryAssociation(
    name="successor228",
    ends={
        Property(name="usagemodel_pc_av229", type=pcm_pc_av_usagemodel_pc_av_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
predecessor230: BinaryAssociation = BinaryAssociation(
    name="predecessor230",
    ends={
        Property(name="usagemodel_pc_av232", type=pcm_pc_av_usagemodel_pc_av_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction231", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_AbstractUserAction233: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_AbstractUserAction233",
    ends={
        Property(name="usagemodel_pc_av235", type=pcm_pc_av_usagemodel_pc_av_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour234", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
branchedBehaviour_BranchTransition249: BinaryAssociation = BinaryAssociation(
    name="branchedBehaviour_BranchTransition249",
    ends={
        Property(name="usagemodel_pc_av251", type=pcm_pc_av_usagemodel_pc_av_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour250", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchTransitions_Branch252: BinaryAssociation = BinaryAssociation(
    name="branchTransitions_Branch252",
    ends={
        Property(name="usagemodel_pc_av254", type=pcm_pc_av_usagemodel_pc_av_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="BranchTransition253", type=BranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopIteration_Loop255: BinaryAssociation = BinaryAssociation(
    name="loopIteration_Loop255",
    ends={
        Property(name="core_pc_av257", type=pcm_pc_av_usagemodel_pc_av_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable256", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyBehaviour_Loop258: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop258",
    ends={
        Property(name="usagemodel_pc_av260", type=pcm_pc_av_usagemodel_pc_av_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour259", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capacity_PassiveResource270: BinaryAssociation = BinaryAssociation(
    name="capacity_PassiveResource270",
    ends={
        Property(name="core_pc_av272", type=pcm_pc_av_repository_pc_av_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable271", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicComponent_PassiveResource273: BinaryAssociation = BinaryAssociation(
    name="basicComponent_PassiveResource273",
    ends={
        Property(name="repository_pc_av274", type=pcm_pc_av_repository_pc_av_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="BasicComponent", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
resourceTimeoutFailureType__PassiveResource275: BinaryAssociation = BinaryAssociation(
    name="resourceTimeoutFailureType__PassiveResource275",
    ends={
        Property(name="reliability_pc_av", type=pcm_pc_av_repository_pc_av_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceTimeoutFailureType", type=ResourceTimeoutFailureType, multiplicity=Multiplicity(0, 1))
    }
)
interArrivalTime_OpenWorkload261: BinaryAssociation = BinaryAssociation(
    name="interArrivalTime_OpenWorkload261",
    ends={
        Property(name="core_pc_av263", type=pcm_pc_av_usagemodel_pc_av_OpenWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable262", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeSpecification_Delay264: BinaryAssociation = BinaryAssociation(
    name="timeSpecification_Delay264",
    ends={
        Property(name="core_pc_av266", type=pcm_pc_av_usagemodel_pc_av_Delay, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable265", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thinkTime_ClosedWorkload267: BinaryAssociation = BinaryAssociation(
    name="thinkTime_ClosedWorkload267",
    ends={
        Property(name="core_pc_av269", type=pcm_pc_av_usagemodel_pc_av_ClosedWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable268", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parentCompleteComponentTypes281: BinaryAssociation = BinaryAssociation(
    name="parentCompleteComponentTypes281",
    ends={
        Property(name="CompleteComponentType", type=pcm_pc_av_repository_pc_av_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_ImplementationComponentType", type=CompleteComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
serviceEffectSpecifications__BasicComponent276: BinaryAssociation = BinaryAssociation(
    name="serviceEffectSpecifications__BasicComponent276",
    ends={
        Property(name="seff_pc_av277", type=pcm_pc_av_repository_pc_av_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ServiceEffectSpecification", type=ServiceEffectSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveResource_BasicComponent278: BinaryAssociation = BinaryAssociation(
    name="passiveResource_BasicComponent278",
    ends={
        Property(name="repository_pc_av280", type=pcm_pc_av_repository_pc_av_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="PassiveResource279", type=PassiveResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceSignature__Parameter298: BinaryAssociation = BinaryAssociation(
    name="resourceSignature__Parameter298",
    ends={
        Property(name="resourcetype_pc_av", type=pcm_pc_av_repository_pc_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceSignature", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
repository__DataType299: BinaryAssociation = BinaryAssociation(
    name="repository__DataType299",
    ends={
        Property(name="repository_pc_av301", type=pcm_pc_av_repository_pc_av_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository300", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
componentParameterUsage_ImplementationComponentType282: BinaryAssociation = BinaryAssociation(
    name="componentParameterUsage_ImplementationComponentType282",
    ends={
        Property(name="VariableUsage284", type=pcm_pc_av_repository_pc_av_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_ImplementationComponentType283", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository__RepositoryComponent285: BinaryAssociation = BinaryAssociation(
    name="repository__RepositoryComponent285",
    ends={
        Property(name="repository_pc_av286", type=pcm_pc_av_repository_pc_av_RepositoryComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
providingEntity_ProvidedRole287: BinaryAssociation = BinaryAssociation(
    name="providingEntity_ProvidedRole287",
    ends={
        Property(name="core_pc_av289", type=pcm_pc_av_repository_pc_av_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_pc_av288", type=entity_pc_av_InterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
dataType__Parameter290: BinaryAssociation = BinaryAssociation(
    name="dataType__Parameter290",
    ends={
        Property(name="DataType", type=pcm_pc_av_repository_pc_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_Parameter", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureSignature__Parameter291: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignature__Parameter291",
    ends={
        Property(name="repository_pc_av292", type=pcm_pc_av_repository_pc_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="InfrastructureSignature", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__Parameter293: BinaryAssociation = BinaryAssociation(
    name="operationSignature__Parameter293",
    ends={
        Property(name="repository_pc_av295", type=pcm_pc_av_repository_pc_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationSignature294", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
eventType__Parameter296: BinaryAssociation = BinaryAssociation(
    name="eventType__Parameter296",
    ends={
        Property(name="repository_pc_av297", type=pcm_pc_av_repository_pc_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="EventType", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
protocols__Interface314: BinaryAssociation = BinaryAssociation(
    name="protocols__Interface314",
    ends={
        Property(name="Protocol", type=pcm_pc_av_repository_pc_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_Interface315", type=Protocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCharacterisations316: BinaryAssociation = BinaryAssociation(
    name="requiredCharacterisations316",
    ends={
        Property(name="repository_pc_av317", type=pcm_pc_av_repository_pc_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="RequiredCharacterisation", type=RequiredCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository__Interface318: BinaryAssociation = BinaryAssociation(
    name="repository__Interface318",
    ends={
        Property(name="repository_pc_av320", type=pcm_pc_av_repository_pc_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository319", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
parameter321: BinaryAssociation = BinaryAssociation(
    name="parameter321",
    ends={
        Property(name="Parameter", type=pcm_pc_av_repository_pc_av_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_RequiredCharacterisation", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
components__Repository302: BinaryAssociation = BinaryAssociation(
    name="components__Repository302",
    ends={
        Property(name="repository_pc_av304", type=pcm_pc_av_repository_pc_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="RepositoryComponent303", type=RepositoryComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaces__Repository305: BinaryAssociation = BinaryAssociation(
    name="interfaces__Repository305",
    ends={
        Property(name="repository_pc_av306", type=pcm_pc_av_repository_pc_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="Interface", type=Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureTypes__Repository307: BinaryAssociation = BinaryAssociation(
    name="failureTypes__Repository307",
    ends={
        Property(name="reliability_pc_av308", type=pcm_pc_av_repository_pc_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="FailureType", type=FailureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes__Repository309: BinaryAssociation = BinaryAssociation(
    name="dataTypes__Repository309",
    ends={
        Property(name="repository_pc_av311", type=pcm_pc_av_repository_pc_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="DataType310", type=DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentInterfaces__Interface312: BinaryAssociation = BinaryAssociation(
    name="parentInterfaces__Interface312",
    ends={
        Property(name="Interface313", type=pcm_pc_av_repository_pc_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_Interface", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
parameters__InfrastructureSignature338: BinaryAssociation = BinaryAssociation(
    name="parameters__InfrastructureSignature338",
    ends={
        Property(name="repository_pc_av340", type=pcm_pc_av_repository_pc_av_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter339", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureInterface__InfrastructureSignature341: BinaryAssociation = BinaryAssociation(
    name="infrastructureInterface__InfrastructureSignature341",
    ends={
        Property(name="repository_pc_av342", type=pcm_pc_av_repository_pc_av_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="InfrastructureInterface", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureSignatures__InfrastructureInterface343: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignatures__InfrastructureInterface343",
    ends={
        Property(name="repository_pc_av345", type=pcm_pc_av_repository_pc_av_InfrastructureInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="InfrastructureSignature344", type=InfrastructureSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterface__InfrastructureRequiredRole346: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__InfrastructureRequiredRole346",
    ends={
        Property(name="InfrastructureInterface347", type=pcm_pc_av_repository_pc_av_InfrastructureRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_InfrastructureRequiredRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
interface_RequiredCharacterisation322: BinaryAssociation = BinaryAssociation(
    name="interface_RequiredCharacterisation322",
    ends={
        Property(name="repository_pc_av324", type=pcm_pc_av_repository_pc_av_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="Interface323", type=Interface, multiplicity=Multiplicity(0, 1))
    }
)
eventTypes__EventGroup325: BinaryAssociation = BinaryAssociation(
    name="eventTypes__EventGroup325",
    ends={
        Property(name="repository_pc_av327", type=pcm_pc_av_repository_pc_av_EventGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="EventType326", type=EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter__EventType328: BinaryAssociation = BinaryAssociation(
    name="parameter__EventType328",
    ends={
        Property(name="repository_pc_av330", type=pcm_pc_av_repository_pc_av_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter329", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventGroup__EventType331: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventType331",
    ends={
        Property(name="repository_pc_av333", type=pcm_pc_av_repository_pc_av_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="EventGroup332", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
exceptions__Signature334: BinaryAssociation = BinaryAssociation(
    name="exceptions__Signature334",
    ends={
        Property(name="ExceptionType", type=pcm_pc_av_repository_pc_av_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_Signature", type=ExceptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureType335: BinaryAssociation = BinaryAssociation(
    name="failureType335",
    ends={
        Property(name="FailureType337", type=pcm_pc_av_repository_pc_av_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_Signature336", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
signatures__OperationInterface358: BinaryAssociation = BinaryAssociation(
    name="signatures__OperationInterface358",
    ends={
        Property(name="repository_pc_av360", type=pcm_pc_av_repository_pc_av_OperationInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationSignature359", type=OperationSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterface__OperationRequiredRole361: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__OperationRequiredRole361",
    ends={
        Property(name="OperationInterface362", type=pcm_pc_av_repository_pc_av_OperationRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_OperationRequiredRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SourceRole363: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SourceRole363",
    ends={
        Property(name="EventGroup364", type=pcm_pc_av_repository_pc_av_SourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_SourceRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SinkRole365: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SinkRole365",
    ends={
        Property(name="EventGroup366", type=pcm_pc_av_repository_pc_av_SinkRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_SinkRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
requiringEntity_RequiredRole348: BinaryAssociation = BinaryAssociation(
    name="requiringEntity_RequiredRole348",
    ends={
        Property(name="core_pc_av350", type=pcm_pc_av_repository_pc_av_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_pc_av349", type=entity_pc_av_InterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
interface__OperationSignature351: BinaryAssociation = BinaryAssociation(
    name="interface__OperationSignature351",
    ends={
        Property(name="repository_pc_av352", type=pcm_pc_av_repository_pc_av_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationInterface", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
parameters__OperationSignature353: BinaryAssociation = BinaryAssociation(
    name="parameters__OperationSignature353",
    ends={
        Property(name="repository_pc_av355", type=pcm_pc_av_repository_pc_av_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter354", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType__OperationSignature356: BinaryAssociation = BinaryAssociation(
    name="returnType__OperationSignature356",
    ends={
        Property(name="DataType357", type=pcm_pc_av_repository_pc_av_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_OperationSignature", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
parentProvidesComponentTypes371: BinaryAssociation = BinaryAssociation(
    name="parentProvidesComponentTypes371",
    ends={
        Property(name="ProvidesComponentType", type=pcm_pc_av_repository_pc_av_CompleteComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_CompleteComponentType", type=ProvidesComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
providedInterface__OperationProvidedRole367: BinaryAssociation = BinaryAssociation(
    name="providedInterface__OperationProvidedRole367",
    ends={
        Property(name="OperationInterface368", type=pcm_pc_av_repository_pc_av_OperationProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_OperationProvidedRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface__InfrastructureProvidedRole369: BinaryAssociation = BinaryAssociation(
    name="providedInterface__InfrastructureProvidedRole369",
    ends={
        Property(name="InfrastructureInterface370", type=pcm_pc_av_repository_pc_av_InfrastructureProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_InfrastructureProvidedRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
innerType_CollectionDataType372: BinaryAssociation = BinaryAssociation(
    name="innerType_CollectionDataType372",
    ends={
        Property(name="DataType373", type=pcm_pc_av_repository_pc_av_CollectionDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_CollectionDataType", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
parentType_CompositeDataType374: BinaryAssociation = BinaryAssociation(
    name="parentType_CompositeDataType374",
    ends={
        Property(name="CompositeDataType", type=pcm_pc_av_repository_pc_av_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 9999))
    }
)
innerDeclaration_CompositeDataType375: BinaryAssociation = BinaryAssociation(
    name="innerDeclaration_CompositeDataType375",
    ends={
        Property(name="repository_pc_av376", type=pcm_pc_av_repository_pc_av_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="InnerDeclaration", type=InnerDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hardwareInducedFailureType__ProcessingResourceType388: BinaryAssociation = BinaryAssociation(
    name="hardwareInducedFailureType__ProcessingResourceType388",
    ends={
        Property(name="reliability_pc_av389", type=pcm_pc_av_resourcetype_pc_av_ProcessingResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="HardwareInducedFailureType", type=HardwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
resourceRepository_ResourceType390: BinaryAssociation = BinaryAssociation(
    name="resourceRepository_ResourceType390",
    ends={
        Property(name="resourcetype_pc_av391", type=pcm_pc_av_resourcetype_pc_av_ResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaces__ResourceRepository392: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaces__ResourceRepository392",
    ends={
        Property(name="resourcetype_pc_av394", type=pcm_pc_av_resourcetype_pc_av_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceInterface393", type=ResourceInterface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schedulingPolicies__ResourceRepository395: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicies__ResourceRepository395",
    ends={
        Property(name="resourcetype_pc_av396", type=pcm_pc_av_resourcetype_pc_av_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="SchedulingPolicy", type=SchedulingPolicy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
availableResourceTypes_ResourceRepository397: BinaryAssociation = BinaryAssociation(
    name="availableResourceTypes_ResourceRepository397",
    ends={
        Property(name="resourcetype_pc_av398", type=pcm_pc_av_resourcetype_pc_av_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceType", type=ResourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype_InnerDeclaration377: BinaryAssociation = BinaryAssociation(
    name="datatype_InnerDeclaration377",
    ends={
        Property(name="DataType378", type=pcm_pc_av_repository_pc_av_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_InnerDeclaration", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
resourceRepository__SchedulingPolicy399: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__SchedulingPolicy399",
    ends={
        Property(name="resourcetype_pc_av401", type=pcm_pc_av_resourcetype_pc_av_SchedulingPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceRepository400", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
compositeDataType_InnerDeclaration379: BinaryAssociation = BinaryAssociation(
    name="compositeDataType_InnerDeclaration379",
    ends={
        Property(name="repository_pc_av381", type=pcm_pc_av_repository_pc_av_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="CompositeDataType380", type=CompositeDataType, multiplicity=Multiplicity(0, 1))
    }
)
networkInducedFailureType__CommunicationLinkResourceType402: BinaryAssociation = BinaryAssociation(
    name="networkInducedFailureType__CommunicationLinkResourceType402",
    ends={
        Property(name="reliability_pc_av403", type=pcm_pc_av_resourcetype_pc_av_CommunicationLinkResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="NetworkInducedFailureType", type=NetworkInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
resourceRepository__ResourceInterface404: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__ResourceInterface404",
    ends={
        Property(name="resourcetype_pc_av406", type=pcm_pc_av_resourcetype_pc_av_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceRepository405", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
parameter__ResourceSignature382: BinaryAssociation = BinaryAssociation(
    name="parameter__ResourceSignature382",
    ends={
        Property(name="repository_pc_av384", type=pcm_pc_av_resourcetype_pc_av_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter383", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceInterface__ResourceSignature385: BinaryAssociation = BinaryAssociation(
    name="resourceInterface__ResourceSignature385",
    ends={
        Property(name="resourcetype_pc_av387", type=pcm_pc_av_resourcetype_pc_av_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceInterface386", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
variableCharacterisation_VariableUsage410: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_VariableUsage410",
    ends={
        Property(name="parameter_pc_av412", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableCharacterisation411", type=VariableCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_VariableUsage413: BinaryAssociation = BinaryAssociation(
    name="userData_VariableUsage413",
    ends={
        Property(name="usagemodel_pc_av415", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="UserData414", type=UserData, multiplicity=Multiplicity(0, 1))
    }
)
callAction__VariableUsage416: BinaryAssociation = BinaryAssociation(
    name="callAction__VariableUsage416",
    ends={
        Property(name="seff_pc_av417", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="CallAction", type=CallAction, multiplicity=Multiplicity(0, 1))
    }
)
synchronisationPoint_VariableUsage418: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_VariableUsage418",
    ends={
        Property(name="seff_pc_av419", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
callReturnAction__VariableUsage420: BinaryAssociation = BinaryAssociation(
    name="callReturnAction__VariableUsage420",
    ends={
        Property(name="seff_pc_av421", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="CallReturnAction", type=CallReturnAction, multiplicity=Multiplicity(0, 1))
    }
)
setVariableAction_VariableUsage422: BinaryAssociation = BinaryAssociation(
    name="setVariableAction_VariableUsage422",
    ends={
        Property(name="seff_pc_av423", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="SetVariableAction", type=SetVariableAction, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage424: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage424",
    ends={
        Property(name="qosannotations_pc_av425", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="SpecifiedOutputParameterAbstraction", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__VariableUsage426: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__VariableUsage426",
    ends={
        Property(name="core_pc_av428", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_av427", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
resourceSignatures__ResourceInterface407: BinaryAssociation = BinaryAssociation(
    name="resourceSignatures__ResourceInterface407",
    ends={
        Property(name="resourcetype_pc_av409", type=pcm_pc_av_resourcetype_pc_av_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceSignature408", type=ResourceSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entryLevelSystemCall_InputParameterUsage429: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_InputParameterUsage429",
    ends={
        Property(name="usagemodel_pc_av430", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="EntryLevelSystemCall", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_OutputParameterUsage431: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_OutputParameterUsage431",
    ends={
        Property(name="usagemodel_pc_av433", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="EntryLevelSystemCall432", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
namedReference__VariableUsage434: BinaryAssociation = BinaryAssociation(
    name="namedReference__VariableUsage434",
    ends={
        Property(name="parameter_pc_av_pcm_pc_av_AbstractNamedReference", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_parameter_pc_av_VariableUsage", type=parameter_pc_av_pcm_pc_av_AbstractNamedReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification_VariableCharacterisation435: BinaryAssociation = BinaryAssociation(
    name="specification_VariableCharacterisation435",
    ends={
        Property(name="core_pc_av437", type=pcm_pc_av_parameter_pc_av_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable436", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableUsage_VariableCharacterisation438: BinaryAssociation = BinaryAssociation(
    name="variableUsage_VariableCharacterisation438",
    ends={
        Property(name="parameter_pc_av440", type=pcm_pc_av_parameter_pc_av_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage439", type=VariableUsage, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceType__HardwareInducedFailureType441: BinaryAssociation = BinaryAssociation(
    name="processingResourceType__HardwareInducedFailureType441",
    ends={
        Property(name="resourcetype_pc_av442", type=pcm_pc_av_reliability_pc_av_HardwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcessingResourceType", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
internalFailureOccurrenceDescriptions__SoftwareInducedFailureType443: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__SoftwareInducedFailureType443",
    ends={
        Property(name="reliability_pc_av444", type=pcm_pc_av_reliability_pc_av_SoftwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="InternalFailureOccurrenceDescription", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999))
    }
)
internalAction__InternalFailureOccurrenceDescription445: BinaryAssociation = BinaryAssociation(
    name="internalAction__InternalFailureOccurrenceDescription445",
    ends={
        Property(name="seff_pc_av446", type=pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="InternalAction", type=InternalAction, multiplicity=Multiplicity(0, 1))
    }
)
softwareInducedFailureType__InternalFailureOccurrenceDescription447: BinaryAssociation = BinaryAssociation(
    name="softwareInducedFailureType__InternalFailureOccurrenceDescription447",
    ends={
        Property(name="reliability_pc_av448", type=pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="SoftwareInducedFailureType", type=SoftwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription451: BinaryAssociation = BinaryAssociation(
    name="specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription451",
    ends={
        Property(name="qosannotations_pc_av452", type=pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="qos_reliability_pc_av", type=qos_reliability_pc_av_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(0, 1))
    }
)
failureType__ExternalFailureOccurrenceDescription453: BinaryAssociation = BinaryAssociation(
    name="failureType__ExternalFailureOccurrenceDescription453",
    ends={
        Property(name="FailureType454", type=pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription", type=FailureType, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource__ResourceTimeoutFailureType455: BinaryAssociation = BinaryAssociation(
    name="passiveResource__ResourceTimeoutFailureType455",
    ends={
        Property(name="repository_pc_av457", type=pcm_pc_av_reliability_pc_av_ResourceTimeoutFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="PassiveResource456", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
repository__FailureType458: BinaryAssociation = BinaryAssociation(
    name="repository__FailureType458",
    ends={
        Property(name="repository_pc_av460", type=pcm_pc_av_reliability_pc_av_FailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository459", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceType__NetworkInducedFailureType449: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType__NetworkInducedFailureType449",
    ends={
        Property(name="resourcetype_pc_av450", type=pcm_pc_av_reliability_pc_av_NetworkInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceType", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
resourceCall__Action467: BinaryAssociation = BinaryAssociation(
    name="resourceCall__Action467",
    ends={
        Property(name="seff_pc_av469", type=pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_pc_av468", type=seff_performance_pc_av_ResourceCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor_AbstractAction470: BinaryAssociation = BinaryAssociation(
    name="predecessor_AbstractAction470",
    ends={
        Property(name="seff_pc_av471", type=pcm_pc_av_seff_pc_av_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
successor_AbstractAction472: BinaryAssociation = BinaryAssociation(
    name="successor_AbstractAction472",
    ends={
        Property(name="seff_pc_av474", type=pcm_pc_av_seff_pc_av_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction473", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemandingBehaviour_AbstractAction475: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingBehaviour_AbstractAction475",
    ends={
        Property(name="seff_pc_av476", type=pcm_pc_av_seff_pc_av_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingBehaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
abstractLoopAction_ResourceDemandingBehaviour477: BinaryAssociation = BinaryAssociation(
    name="abstractLoopAction_ResourceDemandingBehaviour477",
    ends={
        Property(name="seff_pc_av478", type=pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractLoopAction", type=AbstractLoopAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemand_Action461: BinaryAssociation = BinaryAssociation(
    name="resourceDemand_Action461",
    ends={
        Property(name="seff_pc_av463", type=pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_pc_av462", type=seff_performance_pc_av_ParametricResourceDemand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureCall__Action464: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__Action464",
    ends={
        Property(name="seff_pc_av466", type=pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_pc_av465", type=seff_performance_pc_av_InfrastructureCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
steps_Behaviour481: BinaryAssociation = BinaryAssociation(
    name="steps_Behaviour481",
    ends={
        Property(name="AbstractAction482", type=AbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="seff_pc_av483", type=pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1))
    }
)
bodyBehaviour_Loop484: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop484",
    ends={
        Property(name="seff_pc_av486", type=pcm_pc_av_seff_pc_av_AbstractLoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingBehaviour485", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchAction_AbstractBranchTransition487: BinaryAssociation = BinaryAssociation(
    name="branchAction_AbstractBranchTransition487",
    ends={
        Property(name="seff_pc_av488", type=pcm_pc_av_seff_pc_av_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="BranchAction", type=BranchAction, multiplicity=Multiplicity(0, 1))
    }
)
branchBehaviour_BranchTransition489: BinaryAssociation = BinaryAssociation(
    name="branchBehaviour_BranchTransition489",
    ends={
        Property(name="seff_pc_av491", type=pcm_pc_av_seff_pc_av_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingBehaviour490", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branches_Branch492: BinaryAssociation = BinaryAssociation(
    name="branches_Branch492",
    ends={
        Property(name="seff_pc_av494", type=pcm_pc_av_seff_pc_av_BranchAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractBranchTransition493", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputVariableUsages__CallAction495: BinaryAssociation = BinaryAssociation(
    name="inputVariableUsages__CallAction495",
    ends={
        Property(name="parameter_pc_av497", type=pcm_pc_av_seff_pc_av_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage496", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abstractBranchTransition_ResourceDemandingBehaviour479: BinaryAssociation = BinaryAssociation(
    name="abstractBranchTransition_ResourceDemandingBehaviour479",
    ends={
        Property(name="seff_pc_av480", type=pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractBranchTransition", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
describedService__SEFF498: BinaryAssociation = BinaryAssociation(
    name="describedService__SEFF498",
    ends={
        Property(name="Signature", type=pcm_pc_av_seff_pc_av_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_pc_av_ServiceEffectSpecification", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
basicComponent_ServiceEffectSpecification499: BinaryAssociation = BinaryAssociation(
    name="basicComponent_ServiceEffectSpecification499",
    ends={
        Property(name="repository_pc_av501", type=pcm_pc_av_seff_pc_av_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BasicComponent500", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemandingInternalBehaviours502: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingInternalBehaviours502",
    ends={
        Property(name="seff_pc_av503", type=pcm_pc_av_seff_pc_av_ResourceDemandingSEFF, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingInternalBehaviour", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveResource_ReleaseAction506: BinaryAssociation = BinaryAssociation(
    name="passiveResource_ReleaseAction506",
    ends={
        Property(name="PassiveResource507", type=pcm_pc_av_seff_pc_av_ReleaseAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_pc_av_ReleaseAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
iterationCount_LoopAction508: BinaryAssociation = BinaryAssociation(
    name="iterationCount_LoopAction508",
    ends={
        Property(name="core_pc_av510", type=pcm_pc_av_seff_pc_av_LoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable509", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
asynchronousForkedBehaviours_ForkAction511: BinaryAssociation = BinaryAssociation(
    name="asynchronousForkedBehaviours_ForkAction511",
    ends={
        Property(name="seff_pc_av512", type=pcm_pc_av_seff_pc_av_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedBehaviour", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronisingBehaviours_ForkAction513: BinaryAssociation = BinaryAssociation(
    name="synchronisingBehaviours_ForkAction513",
    ends={
        Property(name="seff_pc_av515", type=pcm_pc_av_seff_pc_av_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="SynchronisationPoint514", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
synchronisationPoint_ForkedBehaviour516: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_ForkedBehaviour516",
    ends={
        Property(name="seff_pc_av518", type=pcm_pc_av_seff_pc_av_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="SynchronisationPoint517", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
forkAction_ForkedBehaivour519: BinaryAssociation = BinaryAssociation(
    name="forkAction_ForkedBehaivour519",
    ends={
        Property(name="seff_pc_av520", type=pcm_pc_av_seff_pc_av_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkAction", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
outputParameterUsage_SynchronisationPoint521: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsage_SynchronisationPoint521",
    ends={
        Property(name="parameter_pc_av523", type=pcm_pc_av_seff_pc_av_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage522", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forkAction_SynchronisationPoint524: BinaryAssociation = BinaryAssociation(
    name="forkAction_SynchronisationPoint524",
    ends={
        Property(name="seff_pc_av526", type=pcm_pc_av_seff_pc_av_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkAction525", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
synchronousForkedBehaviours_SynchronisationPoint527: BinaryAssociation = BinaryAssociation(
    name="synchronousForkedBehaviours_SynchronisationPoint527",
    ends={
        Property(name="seff_pc_av529", type=pcm_pc_av_seff_pc_av_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedBehaviour528", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceDemandingSEFF_ResourceDemandingInternalBehaviour504: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingSEFF_ResourceDemandingInternalBehaviour504",
    ends={
        Property(name="seff_pc_av505", type=pcm_pc_av_seff_pc_av_ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingSEFF", type=ResourceDemandingSEFF, multiplicity=Multiplicity(0, 1))
    }
)
parameter_CollectionIteratorAction540: BinaryAssociation = BinaryAssociation(
    name="parameter_CollectionIteratorAction540",
    ends={
        Property(name="Parameter541", type=pcm_pc_av_seff_pc_av_CollectionIteratorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_pc_av_CollectionIteratorAction", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
calledService_ExternalService530: BinaryAssociation = BinaryAssociation(
    name="calledService_ExternalService530",
    ends={
        Property(name="OperationSignature531", type=pcm_pc_av_seff_pc_av_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_pc_av_ExternalCallAction", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
role_ExternalService532: BinaryAssociation = BinaryAssociation(
    name="role_ExternalService532",
    ends={
        Property(name="OperationRequiredRole534", type=pcm_pc_av_seff_pc_av_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_pc_av_ExternalCallAction533", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
returnVariableUsage__CallReturnAction535: BinaryAssociation = BinaryAssociation(
    name="returnVariableUsage__CallReturnAction535",
    ends={
        Property(name="parameter_pc_av537", type=pcm_pc_av_seff_pc_av_CallReturnAction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage536", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveresource_AcquireAction538: BinaryAssociation = BinaryAssociation(
    name="passiveresource_AcquireAction538",
    ends={
        Property(name="PassiveResource539", type=pcm_pc_av_seff_pc_av_AcquireAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_pc_av_AcquireAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
eventType__EmitEventAction550: BinaryAssociation = BinaryAssociation(
    name="eventType__EmitEventAction550",
    ends={
        Property(name="EventType551", type=pcm_pc_av_seff_pc_av_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_pc_av_EmitEventAction", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EmitEventAction552: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EmitEventAction552",
    ends={
        Property(name="SourceRole554", type=pcm_pc_av_seff_pc_av_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_pc_av_EmitEventAction553", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
branchCondition_GuardedBranchTransition542: BinaryAssociation = BinaryAssociation(
    name="branchCondition_GuardedBranchTransition542",
    ends={
        Property(name="core_pc_av544", type=pcm_pc_av_seff_pc_av_GuardedBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable543", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localVariableUsages_SetVariableAction545: BinaryAssociation = BinaryAssociation(
    name="localVariableUsages_SetVariableAction545",
    ends={
        Property(name="parameter_pc_av547", type=pcm_pc_av_seff_pc_av_SetVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage546", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledResourceDemandingInternalBehaviour548: BinaryAssociation = BinaryAssociation(
    name="calledResourceDemandingInternalBehaviour548",
    ends={
        Property(name="ResourceDemandingInternalBehaviour549", type=pcm_pc_av_seff_pc_av_InternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_pc_av_InternalCallAction", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
internalFailureOccurrenceDescriptions__InternalAction555: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__InternalAction555",
    ends={
        Property(name="reliability_pc_av557", type=pcm_pc_av_seff_pc_av_InternalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="InternalFailureOccurrenceDescription556", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature__InfrastructureCall558: BinaryAssociation = BinaryAssociation(
    name="signature__InfrastructureCall558",
    ends={
        Property(name="InfrastructureSignature559", type=pcm_pc_av_seff_performance_pc_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_performance_pc_av_InfrastructureCall", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__InfrastructureCall560: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__InfrastructureCall560",
    ends={
        Property(name="core_pc_av562", type=pcm_pc_av_seff_performance_pc_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable561", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action__InfrastructureCall563: BinaryAssociation = BinaryAssociation(
    name="action__InfrastructureCall563",
    ends={
        Property(name="seff_pc_av564", type=pcm_pc_av_seff_performance_pc_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractInternalControlFlowAction", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__InfrastructureCall565: BinaryAssociation = BinaryAssociation(
    name="requiredRole__InfrastructureCall565",
    ends={
        Property(name="InfrastructureRequiredRole567", type=pcm_pc_av_seff_performance_pc_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_performance_pc_av_InfrastructureCall566", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
signature__ResourceCall573: BinaryAssociation = BinaryAssociation(
    name="signature__ResourceCall573",
    ends={
        Property(name="ResourceSignature575", type=pcm_pc_av_seff_performance_pc_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_performance_pc_av_ResourceCall574", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__ResourceCall576: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__ResourceCall576",
    ends={
        Property(name="core_pc_av578", type=pcm_pc_av_seff_performance_pc_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable577", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action__ResourceCall568: BinaryAssociation = BinaryAssociation(
    name="action__ResourceCall568",
    ends={
        Property(name="seff_pc_av570", type=pcm_pc_av_seff_performance_pc_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractInternalControlFlowAction569", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceRequiredRole__ResourceCall571: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRole__ResourceCall571",
    ends={
        Property(name="entity_pc_av_ResourceRequiredRole572", type=pcm_pc_av_seff_performance_pc_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_performance_pc_av_ResourceCall", type=entity_pc_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
specification_ParametericResourceDemand579: BinaryAssociation = BinaryAssociation(
    name="specification_ParametericResourceDemand579",
    ends={
        Property(name="core_pc_av581", type=pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable580", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredResource_ParametricResourceDemand582: BinaryAssociation = BinaryAssociation(
    name="requiredResource_ParametricResourceDemand582",
    ends={
        Property(name="ProcessingResourceType583", type=pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
action_ParametricResourceDemand584: BinaryAssociation = BinaryAssociation(
    name="action_ParametricResourceDemand584",
    ends={
        Property(name="seff_pc_av586", type=pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractInternalControlFlowAction585", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
primaryBehaviour__RecoveryAction590: BinaryAssociation = BinaryAssociation(
    name="primaryBehaviour__RecoveryAction590",
    ends={
        Property(name="seff_reliability_pc_av_RecoveryActionBehaviour591", type=pcm_pc_av_seff_reliability_pc_av_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_reliability_pc_av_RecoveryAction", type=seff_reliability_pc_av_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
recoveryActionBehaviours__RecoveryAction592: BinaryAssociation = BinaryAssociation(
    name="recoveryActionBehaviours__RecoveryAction592",
    ends={
        Property(name="seff_pc_av594", type=pcm_pc_av_seff_reliability_pc_av_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_reliability_pc_av593", type=seff_reliability_pc_av_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureTypes_FailureHandlingEntity595: BinaryAssociation = BinaryAssociation(
    name="failureTypes_FailureHandlingEntity595",
    ends={
        Property(name="FailureType596", type=pcm_pc_av_seff_reliability_pc_av_FailureHandlingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_reliability_pc_av_FailureHandlingEntity", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
failureHandlingAlternatives__RecoveryActionBehaviour587: BinaryAssociation = BinaryAssociation(
    name="failureHandlingAlternatives__RecoveryActionBehaviour587",
    ends={
        Property(name="seff_reliability_pc_av_RecoveryActionBehaviour", type=pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour", type=seff_reliability_pc_av_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999))
    }
)
recoveryAction__RecoveryActionBehaviour588: BinaryAssociation = BinaryAssociation(
    name="recoveryAction__RecoveryActionBehaviour588",
    ends={
        Property(name="seff_pc_av589", type=pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_reliability_pc_av", type=seff_reliability_pc_av_RecoveryAction, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstractions_QoSAnnotations603: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstractions_QoSAnnotations603",
    ends={
        Property(name="qosannotations_pc_av605", type=pcm_pc_av_qosannotations_pc_av_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="SpecifiedOutputParameterAbstraction604", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
system_QoSAnnotations606: BinaryAssociation = BinaryAssociation(
    name="system_QoSAnnotations606",
    ends={
        Property(name="system_pc_av", type=pcm_pc_av_qosannotations_pc_av_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="System", type=System, multiplicity=Multiplicity(0, 1))
    }
)
signature_SpecifiedQoSAnnation597: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedQoSAnnation597",
    ends={
        Property(name="Signature598", type=pcm_pc_av_qosannotations_pc_av_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_qosannotations_pc_av_SpecifiedQoSAnnotation", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedQoSAnnotation599: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedQoSAnnotation599",
    ends={
        Property(name="Role", type=pcm_pc_av_qosannotations_pc_av_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_qosannotations_pc_av_SpecifiedQoSAnnotation600", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
qosAnnotations_SpecifiedQoSAnnotation601: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedQoSAnnotation601",
    ends={
        Property(name="qosannotations_pc_av602", type=pcm_pc_av_qosannotations_pc_av_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
specification_SpecifiedExecutionTime620: BinaryAssociation = BinaryAssociation(
    name="specification_SpecifiedExecutionTime620",
    ends={
        Property(name="core_pc_av622", type=pcm_pc_av_qos_performance_pc_av_SpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable621", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specifiedQoSAnnotations_QoSAnnotations607: BinaryAssociation = BinaryAssociation(
    name="specifiedQoSAnnotations_QoSAnnotations607",
    ends={
        Property(name="qosannotations_pc_av608", type=pcm_pc_av_qosannotations_pc_av_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="SpecifiedQoSAnnotation", type=SpecifiedQoSAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature_SpecifiedOutputParameterAbstraction609: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedOutputParameterAbstraction609",
    ends={
        Property(name="Signature610", type=pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedOutputParameterAbstraction611: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedOutputParameterAbstraction611",
    ends={
        Property(name="Role613", type=pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction612", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
expectedExternalOutputs_SpecifiedOutputParameterAbstraction614: BinaryAssociation = BinaryAssociation(
    name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction614",
    ends={
        Property(name="parameter_pc_av616", type=pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage615", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qosAnnotations_SpecifiedOutputParameterAbstraction617: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedOutputParameterAbstraction617",
    ends={
        Property(name="qosannotations_pc_av619", type=pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="QoSAnnotations618", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation625: BinaryAssociation = BinaryAssociation(
    name="externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation625",
    ends={
        Property(name="reliability_pc_av626", type=pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ExternalFailureOccurrenceDescription", type=ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assemblyContext_ComponentSpecifiedExecutionTime623: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ComponentSpecifiedExecutionTime623",
    ends={
        Property(name="composition_pc_av_AssemblyContext624", type=pcm_pc_av_qos_performance_pc_av_ComponentSpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_qos_performance_pc_av_ComponentSpecifiedExecutionTime", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceSpecifications_ResourceContainer641: BinaryAssociation = BinaryAssociation(
    name="activeResourceSpecifications_ResourceContainer641",
    ends={
        Property(name="resourceenvironment_pc_av643", type=pcm_pc_av_resourceenvironment_pc_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcessingResourceSpecification642", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceEnvironment_ResourceContainer644: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_ResourceContainer644",
    ends={
        Property(name="resourceenvironment_pc_av646", type=pcm_pc_av_resourceenvironment_pc_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceEnvironment645", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
nestedResourceContainers__ResourceContainer647: BinaryAssociation = BinaryAssociation(
    name="nestedResourceContainers__ResourceContainer647",
    ends={
        Property(name="resourceenvironment_pc_av649", type=pcm_pc_av_resourceenvironment_pc_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer648", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentResourceContainer__ResourceContainer650: BinaryAssociation = BinaryAssociation(
    name="parentResourceContainer__ResourceContainer650",
    ends={
        Property(name="resourceenvironment_pc_av652", type=pcm_pc_av_resourceenvironment_pc_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer651", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
qosAnnotations_System627: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_System627",
    ends={
        Property(name="qosannotations_pc_av629", type=pcm_pc_av_system_pc_av_System, multiplicity=Multiplicity(1, 1)),
        Property(name="QoSAnnotations628", type=QoSAnnotations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkingResources__ResourceEnvironment630: BinaryAssociation = BinaryAssociation(
    name="linkingResources__ResourceEnvironment630",
    ends={
        Property(name="resourceenvironment_pc_av631", type=pcm_pc_av_resourceenvironment_pc_av_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="LinkingResource", type=LinkingResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_ResourceEnvironment632: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ResourceEnvironment632",
    ends={
        Property(name="resourceenvironment_pc_av633", type=pcm_pc_av_resourceenvironment_pc_av_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectedResourceContainers_LinkingResource634: BinaryAssociation = BinaryAssociation(
    name="connectedResourceContainers_LinkingResource634",
    ends={
        Property(name="ResourceContainer635", type=pcm_pc_av_resourceenvironment_pc_av_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_resourceenvironment_pc_av_LinkingResource", type=ResourceContainer, multiplicity=Multiplicity(0, 9999))
    }
)
communicationLinkResourceSpecifications_LinkingResource636: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifications_LinkingResource636",
    ends={
        Property(name="resourceenvironment_pc_av638", type=pcm_pc_av_resourceenvironment_pc_av_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceSpecification637", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceEnvironment_LinkingResource639: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_LinkingResource639",
    ends={
        Property(name="resourceenvironment_pc_av640", type=pcm_pc_av_resourceenvironment_pc_av_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceEnvironment", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
resourceContainer_AllocationContext675: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_AllocationContext675",
    ends={
        Property(name="ResourceContainer676", type=pcm_pc_av_allocation_pc_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_allocation_pc_av_AllocationContext", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_AllocationContext677: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_AllocationContext677",
    ends={
        Property(name="composition_pc_av_AssemblyContext679", type=pcm_pc_av_allocation_pc_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_allocation_pc_av_AllocationContext678", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
allocation_AllocationContext680: BinaryAssociation = BinaryAssociation(
    name="allocation_AllocationContext680",
    ends={
        Property(name="allocation_pc_av", type=pcm_pc_av_allocation_pc_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="Allocation", type=Allocation, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__AllocationContext681: BinaryAssociation = BinaryAssociation(
    name="eventChannel__AllocationContext681",
    ends={
        Property(name="composition_pc_av_EventChannel", type=pcm_pc_av_allocation_pc_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_allocation_pc_av_AllocationContext682", type=composition_pc_av_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
schedulingPolicy653: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicy653",
    ends={
        Property(name="SchedulingPolicy654", type=pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification", type=SchedulingPolicy, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceType_ActiveResourceSpecification655: BinaryAssociation = BinaryAssociation(
    name="activeResourceType_ActiveResourceSpecification655",
    ends={
        Property(name="ProcessingResourceType657", type=pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification656", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
processingRate_ProcessingResourceSpecification658: BinaryAssociation = BinaryAssociation(
    name="processingRate_ProcessingResourceSpecification658",
    ends={
        Property(name="core_pc_av660", type=pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable659", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceContainer_ProcessingResourceSpecification661: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ProcessingResourceSpecification661",
    ends={
        Property(name="resourceenvironment_pc_av663", type=pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer662", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
linkingResource_CommunicationLinkResourceSpecification664: BinaryAssociation = BinaryAssociation(
    name="linkingResource_CommunicationLinkResourceSpecification664",
    ends={
        Property(name="resourceenvironment_pc_av666", type=pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="LinkingResource665", type=LinkingResource, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceType_CommunicationLinkResourceSpecification667: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType_CommunicationLinkResourceSpecification667",
    ends={
        Property(name="CommunicationLinkResourceType668", type=pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
latency_CommunicationLinkResourceSpecification669: BinaryAssociation = BinaryAssociation(
    name="latency_CommunicationLinkResourceSpecification669",
    ends={
        Property(name="core_pc_av671", type=pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable670", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throughput_CommunicationLinkResourceSpecification672: BinaryAssociation = BinaryAssociation(
    name="throughput_CommunicationLinkResourceSpecification672",
    ends={
        Property(name="core_pc_av674", type=pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable673", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetResourceEnvironment_Allocation683: BinaryAssociation = BinaryAssociation(
    name="targetResourceEnvironment_Allocation683",
    ends={
        Property(name="ResourceEnvironment684", type=pcm_pc_av_allocation_pc_av_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_allocation_pc_av_Allocation", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
system_Allocation685: BinaryAssociation = BinaryAssociation(
    name="system_Allocation685",
    ends={
        Property(name="System687", type=pcm_pc_av_allocation_pc_av_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_allocation_pc_av_Allocation686", type=System, multiplicity=Multiplicity(0, 1))
    }
)
allocationContexts_Allocation688: BinaryAssociation = BinaryAssociation(
    name="allocationContexts_Allocation688",
    ends={
        Property(name="allocation_pc_av689", type=pcm_pc_av_allocation_pc_av_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="AllocationContext", type=AllocationContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
completions_CompletionRepository690: BinaryAssociation = BinaryAssociation(
    name="completions_CompletionRepository690",
    ends={
        Property(name="Completion", type=pcm_pc_av_completions_pc_av_CompletionRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_completions_pc_av_CompletionRepository", type=Completion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCommunicationLinkResource_ParametricResourceDemand691: BinaryAssociation = BinaryAssociation(
    name="requiredCommunicationLinkResource_ParametricResourceDemand691",
    ends={
        Property(name="CommunicationLinkResourceType692", type=pcm_pc_av_completions_pc_av_NetworkDemandParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_completions_pc_av_NetworkDemandParametricResourceDemand", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_pcm_pc_av_core_pc_av_PCMRandomVariable_RandomVariable = Generalization(general=RandomVariable, specific=pcm_pc_av_core_pc_av_PCMRandomVariable)
gen_pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingEntity)
gen_pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity_composition_pc_av_ComposedStructure = Generalization(general=composition_pc_av_ComposedStructure, specific=pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity)
gen_pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity_entity_pc_av_InterfaceProvidingRequiringEntity = Generalization(general=entity_pc_av_InterfaceProvidingRequiringEntity, specific=pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity)
gen_pcm_pc_av_entity_pc_av_ResourceProvidedRole_Role = Generalization(general=Role, specific=pcm_pc_av_entity_pc_av_ResourceProvidedRole)
gen_pcm_pc_av_entity_pc_av_InterfaceProvidingRequiringEntity_entity_pc_av_InterfaceProvidingEntity = Generalization(general=entity_pc_av_InterfaceProvidingEntity, specific=pcm_pc_av_entity_pc_av_InterfaceProvidingRequiringEntity)
gen_pcm_pc_av_entity_pc_av_InterfaceProvidingRequiringEntity_entity_pc_av_InterfaceRequiringEntity = Generalization(general=entity_pc_av_InterfaceRequiringEntity, specific=pcm_pc_av_entity_pc_av_InterfaceProvidingRequiringEntity)
gen_pcm_pc_av_entity_pc_av_InterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_pc_av_entity_pc_av_InterfaceProvidingEntity)
gen_pcm_pc_av_entity_pc_av_InterfaceRequiringEntity_entity_pc_av_Entity = Generalization(general=entity_pc_av_Entity, specific=pcm_pc_av_entity_pc_av_InterfaceRequiringEntity)
gen_pcm_pc_av_entity_pc_av_InterfaceRequiringEntity_entity_pc_av_ResourceInterfaceRequiringEntity = Generalization(general=entity_pc_av_ResourceInterfaceRequiringEntity, specific=pcm_pc_av_entity_pc_av_InterfaceRequiringEntity)
gen_pcm_pc_av_entity_pc_av_ResourceInterfaceRequiringEntity_Entity = Generalization(general=Entity, specific=pcm_pc_av_entity_pc_av_ResourceInterfaceRequiringEntity)
gen_pcm_pc_av_entity_pc_av_ResourceRequiredRole_Role = Generalization(general=Role, specific=pcm_pc_av_entity_pc_av_ResourceRequiredRole)
gen_pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingRequiringEntity_entity_pc_av_ResourceInterfaceRequiringEntity = Generalization(general=entity_pc_av_ResourceInterfaceRequiringEntity, specific=pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingRequiringEntity_entity_pc_av_ResourceInterfaceProvidingEntity = Generalization(general=entity_pc_av_ResourceInterfaceProvidingEntity, specific=pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_pc_av_entity_pc_av_Entity_Identifier = Generalization(general=Identifier, specific=pcm_pc_av_entity_pc_av_Entity)
gen_pcm_pc_av_entity_pc_av_Entity_entity_pc_av_NamedElement = Generalization(general=entity_pc_av_NamedElement, specific=pcm_pc_av_entity_pc_av_Entity)
gen_pcm_pc_av_composition_pc_av_DelegationConnector_Connector = Generalization(general=Connector, specific=pcm_pc_av_composition_pc_av_DelegationConnector)
gen_pcm_pc_av_composition_pc_av_Connector_Entity = Generalization(general=Entity, specific=pcm_pc_av_composition_pc_av_Connector)
gen_pcm_pc_av_composition_pc_av_ComposedStructure_Entity = Generalization(general=Entity, specific=pcm_pc_av_composition_pc_av_ComposedStructure)
gen_pcm_pc_av_composition_pc_av_ProvidedDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_av_composition_pc_av_ProvidedDelegationConnector)
gen_pcm_pc_av_composition_pc_av_EventChannel_Entity = Generalization(general=Entity, specific=pcm_pc_av_composition_pc_av_EventChannel)
gen_pcm_pc_av_composition_pc_av_EventChannelSourceConnector_Connector = Generalization(general=Connector, specific=pcm_pc_av_composition_pc_av_EventChannelSourceConnector)
gen_pcm_pc_av_composition_pc_av_EventChannelSinkConnector_Connector = Generalization(general=Connector, specific=pcm_pc_av_composition_pc_av_EventChannelSinkConnector)
gen_pcm_pc_av_composition_pc_av_AssemblyConnector_Connector = Generalization(general=Connector, specific=pcm_pc_av_composition_pc_av_AssemblyConnector)
gen_pcm_pc_av_composition_pc_av_RequiredDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_av_composition_pc_av_RequiredDelegationConnector)
gen_pcm_pc_av_composition_pc_av_SourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_av_composition_pc_av_SourceDelegationConnector)
gen_pcm_pc_av_composition_pc_av_SinkDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_av_composition_pc_av_SinkDelegationConnector)
gen_pcm_pc_av_composition_pc_av_AssemblyEventConnector_Connector = Generalization(general=Connector, specific=pcm_pc_av_composition_pc_av_AssemblyEventConnector)
gen_pcm_pc_av_composition_pc_av_AssemblyContext_Entity = Generalization(general=Entity, specific=pcm_pc_av_composition_pc_av_AssemblyContext)
gen_pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector_Connector = Generalization(general=Connector, specific=pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector)
gen_pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector)
gen_pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector)
gen_pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector)
gen_pcm_pc_av_usagemodel_pc_av_UsageScenario_Entity = Generalization(general=Entity, specific=pcm_pc_av_usagemodel_pc_av_UsageScenario)
gen_pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall)
gen_pcm_pc_av_usagemodel_pc_av_AbstractUserAction_Entity = Generalization(general=Entity, specific=pcm_pc_av_usagemodel_pc_av_AbstractUserAction)
gen_pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour_Entity = Generalization(general=Entity, specific=pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour)
gen_pcm_pc_av_usagemodel_pc_av_Start_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_av_usagemodel_pc_av_Start)
gen_pcm_pc_av_usagemodel_pc_av_OpenWorkload_Workload = Generalization(general=Workload, specific=pcm_pc_av_usagemodel_pc_av_OpenWorkload)
gen_pcm_pc_av_usagemodel_pc_av_Branch_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_av_usagemodel_pc_av_Branch)
gen_pcm_pc_av_usagemodel_pc_av_Loop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_av_usagemodel_pc_av_Loop)
gen_pcm_pc_av_usagemodel_pc_av_Stop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_av_usagemodel_pc_av_Stop)
gen_pcm_pc_av_repository_pc_av_PassiveResource_Entity = Generalization(general=Entity, specific=pcm_pc_av_repository_pc_av_PassiveResource)
gen_pcm_pc_av_repository_pc_av_BasicComponent_ImplementationComponentType = Generalization(general=ImplementationComponentType, specific=pcm_pc_av_repository_pc_av_BasicComponent)
gen_pcm_pc_av_usagemodel_pc_av_Delay_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_av_usagemodel_pc_av_Delay)
gen_pcm_pc_av_usagemodel_pc_av_ClosedWorkload_Workload = Generalization(general=Workload, specific=pcm_pc_av_usagemodel_pc_av_ClosedWorkload)
gen_pcm_pc_av_repository_pc_av_ImplementationComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_pc_av_repository_pc_av_ImplementationComponentType)
gen_pcm_pc_av_repository_pc_av_Repository_Entity = Generalization(general=Entity, specific=pcm_pc_av_repository_pc_av_Repository)
gen_pcm_pc_av_repository_pc_av_RepositoryComponent_InterfaceProvidingRequiringEntity = Generalization(general=InterfaceProvidingRequiringEntity, specific=pcm_pc_av_repository_pc_av_RepositoryComponent)
gen_pcm_pc_av_repository_pc_av_ProvidedRole_Role = Generalization(general=Role, specific=pcm_pc_av_repository_pc_av_ProvidedRole)
gen_pcm_pc_av_repository_pc_av_Interface_Entity = Generalization(general=Entity, specific=pcm_pc_av_repository_pc_av_Interface)
gen_pcm_pc_av_repository_pc_av_InfrastructureSignature_Signature = Generalization(general=Signature, specific=pcm_pc_av_repository_pc_av_InfrastructureSignature)
gen_pcm_pc_av_repository_pc_av_InfrastructureInterface_Interface = Generalization(general=Interface, specific=pcm_pc_av_repository_pc_av_InfrastructureInterface)
gen_pcm_pc_av_repository_pc_av_InfrastructureRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_pc_av_repository_pc_av_InfrastructureRequiredRole)
gen_pcm_pc_av_repository_pc_av_RequiredRole_Role = Generalization(general=Role, specific=pcm_pc_av_repository_pc_av_RequiredRole)
gen_pcm_pc_av_repository_pc_av_EventGroup_Interface = Generalization(general=Interface, specific=pcm_pc_av_repository_pc_av_EventGroup)
gen_pcm_pc_av_repository_pc_av_EventType_Signature = Generalization(general=Signature, specific=pcm_pc_av_repository_pc_av_EventType)
gen_pcm_pc_av_repository_pc_av_Signature_Entity = Generalization(general=Entity, specific=pcm_pc_av_repository_pc_av_Signature)
gen_pcm_pc_av_repository_pc_av_OperationRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_pc_av_repository_pc_av_OperationRequiredRole)
gen_pcm_pc_av_repository_pc_av_SourceRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_pc_av_repository_pc_av_SourceRole)
gen_pcm_pc_av_repository_pc_av_SinkRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_pc_av_repository_pc_av_SinkRole)
gen_pcm_pc_av_repository_pc_av_OperationSignature_Signature = Generalization(general=Signature, specific=pcm_pc_av_repository_pc_av_OperationSignature)
gen_pcm_pc_av_repository_pc_av_OperationInterface_Interface = Generalization(general=Interface, specific=pcm_pc_av_repository_pc_av_OperationInterface)
gen_pcm_pc_av_repository_pc_av_ProvidesComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_pc_av_repository_pc_av_ProvidesComponentType)
gen_pcm_pc_av_repository_pc_av_OperationProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_pc_av_repository_pc_av_OperationProvidedRole)
gen_pcm_pc_av_repository_pc_av_InfrastructureProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_pc_av_repository_pc_av_InfrastructureProvidedRole)
gen_pcm_pc_av_repository_pc_av_CompleteComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_pc_av_repository_pc_av_CompleteComponentType)
gen_pcm_pc_av_repository_pc_av_CollectionDataType_entity_pc_av_Entity = Generalization(general=entity_pc_av_Entity, specific=pcm_pc_av_repository_pc_av_CollectionDataType)
gen_pcm_pc_av_repository_pc_av_CollectionDataType_repository_pc_av_DataType = Generalization(general=repository_pc_av_DataType, specific=pcm_pc_av_repository_pc_av_CollectionDataType)
gen_pcm_pc_av_repository_pc_av_CompositeDataType_entity_pc_av_Entity = Generalization(general=entity_pc_av_Entity, specific=pcm_pc_av_repository_pc_av_CompositeDataType)
gen_pcm_pc_av_repository_pc_av_CompositeDataType_repository_pc_av_DataType = Generalization(general=repository_pc_av_DataType, specific=pcm_pc_av_repository_pc_av_CompositeDataType)
gen_pcm_pc_av_repository_pc_av_CompositeComponent_entity_pc_av_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_av_ComposedProvidingRequiringEntity, specific=pcm_pc_av_repository_pc_av_CompositeComponent)
gen_pcm_pc_av_repository_pc_av_CompositeComponent_repository_pc_av_ImplementationComponentType = Generalization(general=repository_pc_av_ImplementationComponentType, specific=pcm_pc_av_repository_pc_av_CompositeComponent)
gen_pcm_pc_av_repository_pc_av_PrimitiveDataType_DataType = Generalization(general=DataType, specific=pcm_pc_av_repository_pc_av_PrimitiveDataType)
gen_pcm_pc_av_resourcetype_pc_av_ResourceType_entity_pc_av_Entity = Generalization(general=entity_pc_av_Entity, specific=pcm_pc_av_resourcetype_pc_av_ResourceType)
gen_pcm_pc_av_resourcetype_pc_av_ResourceType_UnitCarryingElement = Generalization(general=UnitCarryingElement, specific=pcm_pc_av_resourcetype_pc_av_ResourceType)
gen_pcm_pc_av_resourcetype_pc_av_ResourceType_entity_pc_av_ResourceInterfaceProvidingEntity = Generalization(general=entity_pc_av_ResourceInterfaceProvidingEntity, specific=pcm_pc_av_resourcetype_pc_av_ResourceType)
gen_pcm_pc_av_repository_pc_av_InnerDeclaration_NamedElement = Generalization(general=NamedElement, specific=pcm_pc_av_repository_pc_av_InnerDeclaration)
gen_pcm_pc_av_resourcetype_pc_av_SchedulingPolicy_Entity = Generalization(general=Entity, specific=pcm_pc_av_resourcetype_pc_av_SchedulingPolicy)
gen_pcm_pc_av_resourcetype_pc_av_CommunicationLinkResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_pc_av_resourcetype_pc_av_CommunicationLinkResourceType)
gen_pcm_pc_av_repository_pc_av_Role_Entity = Generalization(general=Entity, specific=pcm_pc_av_repository_pc_av_Role)
gen_pcm_pc_av_resourcetype_pc_av_ResourceInterface_Entity = Generalization(general=Entity, specific=pcm_pc_av_resourcetype_pc_av_ResourceInterface)
gen_pcm_pc_av_resourcetype_pc_av_ResourceSignature_Entity = Generalization(general=Entity, specific=pcm_pc_av_resourcetype_pc_av_ResourceSignature)
gen_pcm_pc_av_resourcetype_pc_av_ProcessingResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_pc_av_resourcetype_pc_av_ProcessingResourceType)
gen_pcm_pc_av_parameter_pc_av_CharacterisedVariable_Variable = Generalization(general=Variable, specific=pcm_pc_av_parameter_pc_av_CharacterisedVariable)
gen_pcm_pc_av_reliability_pc_av_SoftwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_pc_av_reliability_pc_av_SoftwareInducedFailureType)
gen_pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription)
gen_pcm_pc_av_reliability_pc_av_NetworkInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_pc_av_reliability_pc_av_NetworkInducedFailureType)
gen_pcm_pc_av_reliability_pc_av_HardwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_pc_av_reliability_pc_av_HardwareInducedFailureType)
gen_pcm_pc_av_reliability_pc_av_ResourceTimeoutFailureType_SoftwareInducedFailureType = Generalization(general=SoftwareInducedFailureType, specific=pcm_pc_av_reliability_pc_av_ResourceTimeoutFailureType)
gen_pcm_pc_av_reliability_pc_av_FailureType_Entity = Generalization(general=Entity, specific=pcm_pc_av_reliability_pc_av_FailureType)
gen_pcm_pc_av_seff_pc_av_StopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_av_seff_pc_av_StopAction)
gen_pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction_AbstractAction = Generalization(general=AbstractAction, specific=pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction)
gen_pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription)
gen_pcm_pc_av_seff_pc_av_AbstractAction_Entity = Generalization(general=Entity, specific=pcm_pc_av_seff_pc_av_AbstractAction)
gen_pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour_Identifier = Generalization(general=Identifier, specific=pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour)
gen_pcm_pc_av_seff_pc_av_AbstractLoopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_av_seff_pc_av_AbstractLoopAction)
gen_pcm_pc_av_seff_pc_av_AbstractBranchTransition_Entity = Generalization(general=Entity, specific=pcm_pc_av_seff_pc_av_AbstractBranchTransition)
gen_pcm_pc_av_seff_pc_av_BranchAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_av_seff_pc_av_BranchAction)
gen_pcm_pc_av_seff_pc_av_StartAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_av_seff_pc_av_StartAction)
gen_pcm_pc_av_seff_pc_av_ResourceDemandingSEFF_Identifier = Generalization(general=Identifier, specific=pcm_pc_av_seff_pc_av_ResourceDemandingSEFF)
gen_pcm_pc_av_seff_pc_av_ResourceDemandingSEFF_seff_pc_av_ServiceEffectSpecification = Generalization(general=seff_pc_av_ServiceEffectSpecification, specific=pcm_pc_av_seff_pc_av_ResourceDemandingSEFF)
gen_pcm_pc_av_seff_pc_av_ResourceDemandingSEFF_seff_pc_av_ResourceDemandingBehaviour = Generalization(general=seff_pc_av_ResourceDemandingBehaviour, specific=pcm_pc_av_seff_pc_av_ResourceDemandingSEFF)
gen_pcm_pc_av_seff_pc_av_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_pc_av_seff_pc_av_ResourceDemandingInternalBehaviour)
gen_pcm_pc_av_seff_pc_av_LoopAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_pc_av_seff_pc_av_LoopAction)
gen_pcm_pc_av_seff_pc_av_ForkAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_av_seff_pc_av_ForkAction)
gen_pcm_pc_av_seff_pc_av_ForkedBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_pc_av_seff_pc_av_ForkedBehaviour)
gen_pcm_pc_av_seff_pc_av_ExternalCallAction_seff_pc_av_AbstractAction = Generalization(general=seff_pc_av_AbstractAction, specific=pcm_pc_av_seff_pc_av_ExternalCallAction)
gen_pcm_pc_av_seff_pc_av_ExternalCallAction_seff_pc_av_CallReturnAction = Generalization(general=seff_pc_av_CallReturnAction, specific=pcm_pc_av_seff_pc_av_ExternalCallAction)
gen_pcm_pc_av_seff_pc_av_ExternalCallAction_seff_reliability_pc_av_FailureHandlingEntity = Generalization(general=seff_reliability_pc_av_FailureHandlingEntity, specific=pcm_pc_av_seff_pc_av_ExternalCallAction)
gen_pcm_pc_av_seff_pc_av_ReleaseAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_av_seff_pc_av_ReleaseAction)
gen_pcm_pc_av_seff_pc_av_CollectionIteratorAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_pc_av_seff_pc_av_CollectionIteratorAction)
gen_pcm_pc_av_seff_pc_av_GuardedBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_pc_av_seff_pc_av_GuardedBranchTransition)
gen_pcm_pc_av_seff_pc_av_CallReturnAction_CallAction = Generalization(general=CallAction, specific=pcm_pc_av_seff_pc_av_CallReturnAction)
gen_pcm_pc_av_seff_pc_av_ProbabilisticBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_pc_av_seff_pc_av_ProbabilisticBranchTransition)
gen_pcm_pc_av_seff_pc_av_AcquireAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_av_seff_pc_av_AcquireAction)
gen_pcm_pc_av_seff_pc_av_InternalAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_av_seff_pc_av_InternalAction)
gen_pcm_pc_av_seff_pc_av_SetVariableAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_av_seff_pc_av_SetVariableAction)
gen_pcm_pc_av_seff_pc_av_InternalCallAction_seff_pc_av_CallAction = Generalization(general=seff_pc_av_CallAction, specific=pcm_pc_av_seff_pc_av_InternalCallAction)
gen_pcm_pc_av_seff_pc_av_InternalCallAction_seff_pc_av_AbstractInternalControlFlowAction = Generalization(general=seff_pc_av_AbstractInternalControlFlowAction, specific=pcm_pc_av_seff_pc_av_InternalCallAction)
gen_pcm_pc_av_seff_pc_av_EmitEventAction_seff_pc_av_AbstractAction = Generalization(general=seff_pc_av_AbstractAction, specific=pcm_pc_av_seff_pc_av_EmitEventAction)
gen_pcm_pc_av_seff_pc_av_EmitEventAction_seff_pc_av_CallAction = Generalization(general=seff_pc_av_CallAction, specific=pcm_pc_av_seff_pc_av_EmitEventAction)
gen_pcm_pc_av_seff_performance_pc_av_InfrastructureCall_CallAction = Generalization(general=CallAction, specific=pcm_pc_av_seff_performance_pc_av_InfrastructureCall)
gen_pcm_pc_av_seff_performance_pc_av_ResourceCall_CallAction = Generalization(general=CallAction, specific=pcm_pc_av_seff_performance_pc_av_ResourceCall)
gen_pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour_seff_reliability_pc_av_FailureHandlingEntity = Generalization(general=seff_reliability_pc_av_FailureHandlingEntity, specific=pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour)
gen_pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour_seff_pc_av_ResourceDemandingBehaviour = Generalization(general=seff_pc_av_ResourceDemandingBehaviour, specific=pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour)
gen_pcm_pc_av_seff_reliability_pc_av_FailureHandlingEntity_Entity = Generalization(general=Entity, specific=pcm_pc_av_seff_reliability_pc_av_FailureHandlingEntity)
gen_pcm_pc_av_seff_reliability_pc_av_RecoveryAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_av_seff_reliability_pc_av_RecoveryAction)
gen_pcm_pc_av_qosannotations_pc_av_QoSAnnotations_Entity = Generalization(general=Entity, specific=pcm_pc_av_qosannotations_pc_av_QoSAnnotations)
gen_pcm_pc_av_qos_performance_pc_av_SystemSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_pc_av_qos_performance_pc_av_SystemSpecifiedExecutionTime)
gen_pcm_pc_av_qos_performance_pc_av_SpecifiedExecutionTime_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_pc_av_qos_performance_pc_av_SpecifiedExecutionTime)
gen_pcm_pc_av_qos_performance_pc_av_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_pc_av_qos_performance_pc_av_ComponentSpecifiedExecutionTime)
gen_pcm_pc_av_system_pc_av_System_entity_pc_av_Entity = Generalization(general=entity_pc_av_Entity, specific=pcm_pc_av_system_pc_av_System)
gen_pcm_pc_av_system_pc_av_System_entity_pc_av_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_av_ComposedProvidingRequiringEntity, specific=pcm_pc_av_system_pc_av_System)
gen_pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation)
gen_pcm_pc_av_resourceenvironment_pc_av_ResourceContainer_Entity = Generalization(general=Entity, specific=pcm_pc_av_resourceenvironment_pc_av_ResourceContainer)
gen_pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification)
gen_pcm_pc_av_resourceenvironment_pc_av_ResourceEnvironment_NamedElement = Generalization(general=NamedElement, specific=pcm_pc_av_resourceenvironment_pc_av_ResourceEnvironment)
gen_pcm_pc_av_resourceenvironment_pc_av_LinkingResource_Entity = Generalization(general=Entity, specific=pcm_pc_av_resourceenvironment_pc_av_LinkingResource)
gen_pcm_pc_av_allocation_pc_av_AllocationContext_Entity = Generalization(general=Entity, specific=pcm_pc_av_allocation_pc_av_AllocationContext)
gen_pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification)
gen_pcm_pc_av_subsystem_pc_av_SubSystem_entity_pc_av_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_av_ComposedProvidingRequiringEntity, specific=pcm_pc_av_subsystem_pc_av_SubSystem)
gen_pcm_pc_av_subsystem_pc_av_SubSystem_repository_pc_av_RepositoryComponent = Generalization(general=repository_pc_av_RepositoryComponent, specific=pcm_pc_av_subsystem_pc_av_SubSystem)
gen_pcm_pc_av_completions_pc_av_Completion_entity_pc_av_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_av_ComposedProvidingRequiringEntity, specific=pcm_pc_av_completions_pc_av_Completion)
gen_pcm_pc_av_completions_pc_av_Completion_repository_pc_av_ImplementationComponentType = Generalization(general=repository_pc_av_ImplementationComponentType, specific=pcm_pc_av_completions_pc_av_Completion)
gen_pcm_pc_av_allocation_pc_av_Allocation_Entity = Generalization(general=Entity, specific=pcm_pc_av_allocation_pc_av_Allocation)
gen_pcm_pc_av_completions_pc_av_DelegatingExternalCallAction_ExternalCallAction = Generalization(general=ExternalCallAction, specific=pcm_pc_av_completions_pc_av_DelegatingExternalCallAction)
gen_pcm_pc_av_completions_pc_av_NetworkDemandParametricResourceDemand_ParametricResourceDemand = Generalization(general=ParametricResourceDemand, specific=pcm_pc_av_completions_pc_av_NetworkDemandParametricResourceDemand)

# Domain Model
domain_model = DomainModel(
    name="pcm_pc_av",
    types={pcm_pc_av_PerJoinPointScope, pcm_pc_av_core_pc_av_PCMRandomVariable, RandomVariable, pcm_pc_av_DummyClass, pcm_pc_av_Pointcut, pcm_pc_av_EObject, pcm_pc_av_Advice, pcm_pc_av_GlobalScope, Loop, OpenWorkload, Delay, CommunicationLinkResourceSpecification, ProcessingResourceSpecification, ClosedWorkload, PassiveResource, VariableCharacterisation, seff_performance_pc_av_InfrastructureCall, seff_performance_pc_av_ResourceCall, seff_performance_pc_av_ParametricResourceDemand, LoopAction, GuardedBranchTransition, qos_performance_pc_av_SpecifiedExecutionTime, composition_pc_av_EventChannelSinkConnector, composition_pc_av_AssemblyEventConnector, pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingEntity, entity_pc_av_ResourceProvidedRole, pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity, composition_pc_av_ComposedStructure, entity_pc_av_InterfaceProvidingRequiringEntity, pcm_pc_av_entity_pc_av_ResourceProvidedRole, Role, entity_pc_av_ResourceInterfaceProvidingEntity, ResourceInterface, pcm_pc_av_entity_pc_av_InterfaceProvidingRequiringEntity, entity_pc_av_InterfaceProvidingEntity, entity_pc_av_InterfaceRequiringEntity, pcm_pc_av_entity_pc_av_InterfaceProvidingEntity, Entity, ProvidedRole, pcm_pc_av_entity_pc_av_InterfaceRequiringEntity, entity_pc_av_Entity, entity_pc_av_ResourceInterfaceRequiringEntity, RequiredRole, pcm_pc_av_entity_pc_av_ResourceInterfaceRequiringEntity, entity_pc_av_ResourceRequiredRole, pcm_pc_av_entity_pc_av_ResourceRequiredRole, composition_pc_av_AssemblyContext, composition_pc_av_ResourceRequiredDelegationConnector, composition_pc_av_EventChannel, pcm_pc_av_entity_pc_av_NamedElement, pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingRequiringEntity, pcm_pc_av_entity_pc_av_Entity, Identifier, entity_pc_av_NamedElement, pcm_pc_av_composition_pc_av_DelegationConnector, Connector, pcm_pc_av_composition_pc_av_Connector, pcm_pc_av_composition_pc_av_ComposedStructure, SinkRole, PCMRandomVariable, pcm_pc_av_composition_pc_av_ProvidedDelegationConnector, DelegationConnector, composition_pc_av_Connector, pcm_pc_av_composition_pc_av_ResourceRequiredDelegationConnector, pcm_pc_av_composition_pc_av_EventChannel, EventGroup, composition_pc_av_EventChannelSourceConnector, pcm_pc_av_composition_pc_av_EventChannelSourceConnector, SourceRole, pcm_pc_av_composition_pc_av_EventChannelSinkConnector, OperationRequiredRole, pcm_pc_av_composition_pc_av_AssemblyConnector, OperationProvidedRole, pcm_pc_av_composition_pc_av_RequiredDelegationConnector, pcm_pc_av_composition_pc_av_SourceDelegationConnector, pcm_pc_av_composition_pc_av_SinkDelegationConnector, pcm_pc_av_composition_pc_av_AssemblyEventConnector, pcm_pc_av_composition_pc_av_AssemblyContext, RepositoryComponent, VariableUsage, pcm_pc_av_usagemodel_pc_av_Workload, UsageScenario, pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector, InfrastructureProvidedRole, InfrastructureRequiredRole, pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector, pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector, pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector, OperationSignature, pcm_pc_av_usagemodel_pc_av_UsageScenario, UsageModel, ScenarioBehaviour, Workload, pcm_pc_av_usagemodel_pc_av_UserData, pcm_pc_av_usagemodel_pc_av_UsageModel, UserData, pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall, AbstractUserAction, BranchTransition, pcm_pc_av_usagemodel_pc_av_BranchTransition, Branch, pcm_pc_av_usagemodel_pc_av_AbstractUserAction, pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour, pcm_pc_av_usagemodel_pc_av_Start, pcm_pc_av_usagemodel_pc_av_OpenWorkload, pcm_pc_av_usagemodel_pc_av_Branch, pcm_pc_av_usagemodel_pc_av_Loop, pcm_pc_av_usagemodel_pc_av_Stop, pcm_pc_av_repository_pc_av_PassiveResource, BasicComponent, ResourceTimeoutFailureType, pcm_pc_av_repository_pc_av_BasicComponent, ImplementationComponentType, pcm_pc_av_usagemodel_pc_av_Delay, pcm_pc_av_usagemodel_pc_av_ClosedWorkload, CompleteComponentType, ServiceEffectSpecification, pcm_pc_av_repository_pc_av_ImplementationComponentType, ResourceSignature, pcm_pc_av_repository_pc_av_DataType, pcm_pc_av_repository_pc_av_Repository, pcm_pc_av_repository_pc_av_RepositoryComponent, InterfaceProvidingRequiringEntity, Repository, pcm_pc_av_repository_pc_av_ProvidedRole, pcm_pc_av_repository_pc_av_Parameter, DataType, InfrastructureSignature, EventType, Protocol, RequiredCharacterisation, pcm_pc_av_repository_pc_av_RequiredCharacterisation, Parameter_, Interface, FailureType, pcm_pc_av_repository_pc_av_Interface, pcm_pc_av_repository_pc_av_InfrastructureSignature, InfrastructureInterface, pcm_pc_av_repository_pc_av_InfrastructureInterface, pcm_pc_av_repository_pc_av_InfrastructureRequiredRole, pcm_pc_av_repository_pc_av_RequiredRole, pcm_pc_av_repository_pc_av_EventGroup, pcm_pc_av_repository_pc_av_EventType, Signature, pcm_pc_av_repository_pc_av_Signature, ExceptionType, pcm_pc_av_repository_pc_av_ExceptionType, pcm_pc_av_repository_pc_av_OperationRequiredRole, pcm_pc_av_repository_pc_av_SourceRole, pcm_pc_av_repository_pc_av_SinkRole, pcm_pc_av_repository_pc_av_OperationSignature, OperationInterface, pcm_pc_av_repository_pc_av_OperationInterface, ProvidesComponentType, pcm_pc_av_repository_pc_av_ProvidesComponentType, pcm_pc_av_repository_pc_av_OperationProvidedRole, pcm_pc_av_repository_pc_av_InfrastructureProvidedRole, pcm_pc_av_repository_pc_av_CompleteComponentType, pcm_pc_av_repository_pc_av_CollectionDataType, repository_pc_av_DataType, pcm_pc_av_repository_pc_av_CompositeDataType, CompositeDataType, InnerDeclaration, pcm_pc_av_repository_pc_av_CompositeComponent, entity_pc_av_ComposedProvidingRequiringEntity, repository_pc_av_ImplementationComponentType, pcm_pc_av_repository_pc_av_PrimitiveDataType, HardwareInducedFailureType, pcm_pc_av_resourcetype_pc_av_ResourceType, UnitCarryingElement, ResourceRepository, pcm_pc_av_resourcetype_pc_av_ResourceRepository, SchedulingPolicy, pcm_pc_av_repository_pc_av_InnerDeclaration, NamedElement, pcm_pc_av_resourcetype_pc_av_SchedulingPolicy, pcm_pc_av_resourcetype_pc_av_CommunicationLinkResourceType, pcm_pc_av_repository_pc_av_Role, NetworkInducedFailureType, pcm_pc_av_resourcetype_pc_av_ResourceInterface, pcm_pc_av_resourcetype_pc_av_ResourceSignature, pcm_pc_av_resourcetype_pc_av_ProcessingResourceType, ResourceType, pcm_pc_av_protocol_pc_av_Protocol, pcm_pc_av_parameter_pc_av_VariableUsage, CallAction, SynchronisationPoint, CallReturnAction, SetVariableAction, SpecifiedOutputParameterAbstraction, parameter_pc_av_pcm_pc_av_AbstractNamedReference, pcm_pc_av_parameter_pc_av_VariableCharacterisation, pcm_pc_av_parameter_pc_av_CharacterisedVariable, Variable, pcm_pc_av_reliability_pc_av_FailureOccurrenceDescription, EntryLevelSystemCall, ProcessingResourceType, pcm_pc_av_reliability_pc_av_SoftwareInducedFailureType, InternalFailureOccurrenceDescription, pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription, FailureOccurrenceDescription, InternalAction, SoftwareInducedFailureType, pcm_pc_av_reliability_pc_av_NetworkInducedFailureType, CommunicationLinkResourceType, pcm_pc_av_reliability_pc_av_HardwareInducedFailureType, qos_reliability_pc_av_SpecifiedReliabilityAnnotation, pcm_pc_av_reliability_pc_av_ResourceTimeoutFailureType, pcm_pc_av_reliability_pc_av_FailureType, pcm_pc_av_seff_pc_av_StopAction, AbstractInternalControlFlowAction, pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction, AbstractAction, pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription, pcm_pc_av_seff_pc_av_AbstractAction, ResourceDemandingBehaviour, pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour, AbstractLoopAction, pcm_pc_av_seff_pc_av_AbstractLoopAction, pcm_pc_av_seff_pc_av_AbstractBranchTransition, BranchAction, pcm_pc_av_seff_pc_av_BranchAction, pcm_pc_av_seff_pc_av_CallAction, pcm_pc_av_seff_pc_av_StartAction, AbstractBranchTransition, pcm_pc_av_seff_pc_av_ServiceEffectSpecification, pcm_pc_av_seff_pc_av_ResourceDemandingSEFF, seff_pc_av_ServiceEffectSpecification, seff_pc_av_ResourceDemandingBehaviour, ResourceDemandingInternalBehaviour, pcm_pc_av_seff_pc_av_ResourceDemandingInternalBehaviour, pcm_pc_av_seff_pc_av_LoopAction, pcm_pc_av_seff_pc_av_ForkAction, ForkedBehaviour, pcm_pc_av_seff_pc_av_ForkedBehaviour, ForkAction, pcm_pc_av_seff_pc_av_SynchronisationPoint, pcm_pc_av_seff_pc_av_ExternalCallAction, seff_pc_av_AbstractAction, seff_pc_av_CallReturnAction, ResourceDemandingSEFF, seff_reliability_pc_av_FailureHandlingEntity, pcm_pc_av_seff_pc_av_ReleaseAction, pcm_pc_av_seff_pc_av_CollectionIteratorAction, pcm_pc_av_seff_pc_av_GuardedBranchTransition, pcm_pc_av_seff_pc_av_CallReturnAction, pcm_pc_av_seff_pc_av_ProbabilisticBranchTransition, pcm_pc_av_seff_pc_av_AcquireAction, pcm_pc_av_seff_pc_av_InternalAction, pcm_pc_av_seff_pc_av_SetVariableAction, pcm_pc_av_seff_pc_av_InternalCallAction, seff_pc_av_CallAction, seff_pc_av_AbstractInternalControlFlowAction, pcm_pc_av_seff_pc_av_EmitEventAction, pcm_pc_av_seff_performance_pc_av_InfrastructureCall, pcm_pc_av_seff_performance_pc_av_ResourceCall, pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand, pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour, pcm_pc_av_seff_reliability_pc_av_FailureHandlingEntity, pcm_pc_av_qosannotations_pc_av_SpecifiedQoSAnnotation, seff_reliability_pc_av_RecoveryActionBehaviour, seff_reliability_pc_av_RecoveryAction, pcm_pc_av_seff_reliability_pc_av_RecoveryAction, System, SpecifiedQoSAnnotation, QoSAnnotations, pcm_pc_av_qosannotations_pc_av_QoSAnnotations, pcm_pc_av_qos_performance_pc_av_SystemSpecifiedExecutionTime, SpecifiedExecutionTime, pcm_pc_av_qos_performance_pc_av_SpecifiedExecutionTime, pcm_pc_av_qos_performance_pc_av_ComponentSpecifiedExecutionTime, pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction, ExternalFailureOccurrenceDescription, pcm_pc_av_system_pc_av_System, pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation, pcm_pc_av_resourceenvironment_pc_av_ResourceContainer, pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification, pcm_pc_av_resourceenvironment_pc_av_ResourceEnvironment, LinkingResource, ResourceContainer, pcm_pc_av_resourceenvironment_pc_av_LinkingResource, ResourceEnvironment, pcm_pc_av_allocation_pc_av_AllocationContext, Allocation, pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification, AllocationContext, pcm_pc_av_subsystem_pc_av_SubSystem, repository_pc_av_RepositoryComponent, pcm_pc_av_completions_pc_av_Completion, pcm_pc_av_completions_pc_av_CompletionRepository, pcm_pc_av_allocation_pc_av_Allocation, Completion, pcm_pc_av_completions_pc_av_DelegatingExternalCallAction, ExternalCallAction, pcm_pc_av_completions_pc_av_NetworkDemandParametricResourceDemand, ParametricResourceDemand, ParameterModifier, ComponentType, PrimitiveTypeEnum, VariableCharacterisationType},
    associations={scopedObject5, children0, children1, scopedObject3, loop_LoopIteration26, openWorkload_PCMRandomVariable28, delay_TimeSpecification30, communicationLinkResourceSpecifcation_throughput_PCMRandomVariable32, processingResourceSpecification_processingRate_PCMRandomVariable33, communicationLinkResourceSpecification_latency_PCMRandomVariable35, closedWorkload_PCMRandomVariable7, passiveResource_capacity_PCMRandomVariable8, variableCharacterisation_Specification9, infrastructureCall__PCMRandomVariable10, resourceCall__PCMRandomVariable11, parametricResourceDemand_PCMRandomVariable14, loopAction_PCMRandomVariable17, guardedBranchTransition_PCMRandomVariable19, specifiedExecutionTime_PCMRandomVariable21, eventChannelSinkConnector__FilterCondition22, assemblyEventConnector__FilterCondition23, resourceProvidedRoles__ResourceInterfaceProvidingEntity53, resourceInterfaceProvidingEntity__ResourceProvidedRole38, providedResourceInterface__ResourceProvidedRole40, providedRoles_InterfaceProvidingEntity41, requiredRoles_InterfaceRequiringEntity43, resourceRequiredRoles__ResourceInterfaceRequiringEntity45, requiredResourceInterface__ResourceRequiredRole48, resourceInterfaceRequiringEntity__ResourceRequiredRole50, assemblyContexts__ComposedStructure59, resourceRequiredDelegationConnectors_ComposedStructure62, eventChannel__ComposedStructure65, parentStructure__Connector56, sinkRole__EventChannelSinkConnector94, filterCondition__EventChannelSinkConnector95, assemblyContext__EventChannelSinkConnector97, eventChannel__EventChannelSinkConnector100, connectors__ComposedStructure68, innerResourceRequiredRole_ResourceRequiredDelegationConnector71, outerResourceRequiredRole_ResourceRequiredDelegationConnector72, parentStructure_ResourceRequiredDelegationConnector75, eventGroup__EventChannel78, eventChannelSourceConnector__EventChannel79, eventChannelSinkConnector__EventChannel82, parentStructure__EventChannel85, sourceRole__EventChannelSourceRole88, assemblyContext__EventChannelSourceConnector89, eventChannel__EventChannelSourceConnector91, innerRequiredRole_RequiredDelegationConnector110, outerRequiredRole_RequiredDelegationConnector111, assemblyContext_RequiredDelegationConnector114, innerProvidedRole_ProvidedDelegationConnector103, outerProvidedRole_ProvidedDelegationConnector104, assemblyContext_ProvidedDelegationConnector107, sourceRole__AssemblyEventConnector130, sinkAssemblyContext__AssemblyEventConnector133, sourceAssemblyContext__AssemblyEventConnector136, filterCondition__AssemblyEventConnector139, innerSourceRole__SourceRole142, outerSourceRole__SourceRole144, assemblyContext__SourceDelegationConnector147, requiringAssemblyContext_AssemblyConnector117, providingAssemblyContext_AssemblyConnector119, providedRole_AssemblyConnector122, requiredRole_AssemblyConnector125, sinkRole__AssemblyEventConnector128, innerRequiredRole__RequiredResourceDelegationConnector185, outerRequiredRole__RequiredResourceDelegationConnector188, parentStructure__AssemblyContext191, encapsulatedComponent__AssemblyContext194, configParameterUsages__AssemblyContext195, usageScenario_Workload197, assemblyContext__SinkDelegationConnector150, innerSinkRole__SinkRole152, outerSinkRole__SinkRole155, providedRole__AssemblyInfrastructureConnector158, requiredRole__AssemblyInfrastructureConnector159, providingAssemblyContext__AssemblyInfrastructureConnector161, requiringAssemblyContext__AssemblyInfrastructureConnector164, innerProvidedRole__ProvidedInfrastructureDelegationConnector167, outerProvidedRole__ProvidedInfrastructureDelegationConnector169, assemblyContext__ProvidedInfrastructureDelegationConnector172, innerRequiredRole__RequiredInfrastructureDelegationConnector175, outerRequiredRole__RequiredInfrastructureDelegationConnector177, assemblyContext__RequiredInfrastructureDelegationConnector180, assemblyContext__RequiredResourceDelegationConnector183, providedRole_EntryLevelSystemCall218, operationSignature__EntryLevelSystemCall220, outputParameterUsages_EntryLevelSystemCall222, inputParameterUsages_EntryLevelSystemCall225, usageModel_UsageScenario199, scenarioBehaviour_UsageScenario201, workload_UsageScenario203, assemblyContext_userData205, usageModel_UserData207, userDataParameterUsages_UserData210, usageScenario_UsageModel213, userData_UsageModel216, usageScenario_SenarioBehaviour236, branchTransition_ScenarioBehaviour239, loop_ScenarioBehaviour241, actions_ScenarioBehaviour244, branch_BranchTransition247, successor228, predecessor230, scenarioBehaviour_AbstractUserAction233, branchedBehaviour_BranchTransition249, branchTransitions_Branch252, loopIteration_Loop255, bodyBehaviour_Loop258, capacity_PassiveResource270, basicComponent_PassiveResource273, resourceTimeoutFailureType__PassiveResource275, interArrivalTime_OpenWorkload261, timeSpecification_Delay264, thinkTime_ClosedWorkload267, parentCompleteComponentTypes281, serviceEffectSpecifications__BasicComponent276, passiveResource_BasicComponent278, resourceSignature__Parameter298, repository__DataType299, componentParameterUsage_ImplementationComponentType282, repository__RepositoryComponent285, providingEntity_ProvidedRole287, dataType__Parameter290, infrastructureSignature__Parameter291, operationSignature__Parameter293, eventType__Parameter296, protocols__Interface314, requiredCharacterisations316, repository__Interface318, parameter321, components__Repository302, interfaces__Repository305, failureTypes__Repository307, dataTypes__Repository309, parentInterfaces__Interface312, parameters__InfrastructureSignature338, infrastructureInterface__InfrastructureSignature341, infrastructureSignatures__InfrastructureInterface343, requiredInterface__InfrastructureRequiredRole346, interface_RequiredCharacterisation322, eventTypes__EventGroup325, parameter__EventType328, eventGroup__EventType331, exceptions__Signature334, failureType335, signatures__OperationInterface358, requiredInterface__OperationRequiredRole361, eventGroup__SourceRole363, eventGroup__SinkRole365, requiringEntity_RequiredRole348, interface__OperationSignature351, parameters__OperationSignature353, returnType__OperationSignature356, parentProvidesComponentTypes371, providedInterface__OperationProvidedRole367, providedInterface__InfrastructureProvidedRole369, innerType_CollectionDataType372, parentType_CompositeDataType374, innerDeclaration_CompositeDataType375, hardwareInducedFailureType__ProcessingResourceType388, resourceRepository_ResourceType390, resourceInterfaces__ResourceRepository392, schedulingPolicies__ResourceRepository395, availableResourceTypes_ResourceRepository397, datatype_InnerDeclaration377, resourceRepository__SchedulingPolicy399, compositeDataType_InnerDeclaration379, networkInducedFailureType__CommunicationLinkResourceType402, resourceRepository__ResourceInterface404, parameter__ResourceSignature382, resourceInterface__ResourceSignature385, variableCharacterisation_VariableUsage410, userData_VariableUsage413, callAction__VariableUsage416, synchronisationPoint_VariableUsage418, callReturnAction__VariableUsage420, setVariableAction_VariableUsage422, specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage424, assemblyContext__VariableUsage426, resourceSignatures__ResourceInterface407, entryLevelSystemCall_InputParameterUsage429, entryLevelSystemCall_OutputParameterUsage431, namedReference__VariableUsage434, specification_VariableCharacterisation435, variableUsage_VariableCharacterisation438, processingResourceType__HardwareInducedFailureType441, internalFailureOccurrenceDescriptions__SoftwareInducedFailureType443, internalAction__InternalFailureOccurrenceDescription445, softwareInducedFailureType__InternalFailureOccurrenceDescription447, specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription451, failureType__ExternalFailureOccurrenceDescription453, passiveResource__ResourceTimeoutFailureType455, repository__FailureType458, communicationLinkResourceType__NetworkInducedFailureType449, resourceCall__Action467, predecessor_AbstractAction470, successor_AbstractAction472, resourceDemandingBehaviour_AbstractAction475, abstractLoopAction_ResourceDemandingBehaviour477, resourceDemand_Action461, infrastructureCall__Action464, steps_Behaviour481, bodyBehaviour_Loop484, branchAction_AbstractBranchTransition487, branchBehaviour_BranchTransition489, branches_Branch492, inputVariableUsages__CallAction495, abstractBranchTransition_ResourceDemandingBehaviour479, describedService__SEFF498, basicComponent_ServiceEffectSpecification499, resourceDemandingInternalBehaviours502, passiveResource_ReleaseAction506, iterationCount_LoopAction508, asynchronousForkedBehaviours_ForkAction511, synchronisingBehaviours_ForkAction513, synchronisationPoint_ForkedBehaviour516, forkAction_ForkedBehaivour519, outputParameterUsage_SynchronisationPoint521, forkAction_SynchronisationPoint524, synchronousForkedBehaviours_SynchronisationPoint527, resourceDemandingSEFF_ResourceDemandingInternalBehaviour504, parameter_CollectionIteratorAction540, calledService_ExternalService530, role_ExternalService532, returnVariableUsage__CallReturnAction535, passiveresource_AcquireAction538, eventType__EmitEventAction550, sourceRole__EmitEventAction552, branchCondition_GuardedBranchTransition542, localVariableUsages_SetVariableAction545, calledResourceDemandingInternalBehaviour548, internalFailureOccurrenceDescriptions__InternalAction555, signature__InfrastructureCall558, numberOfCalls__InfrastructureCall560, action__InfrastructureCall563, requiredRole__InfrastructureCall565, signature__ResourceCall573, numberOfCalls__ResourceCall576, action__ResourceCall568, resourceRequiredRole__ResourceCall571, specification_ParametericResourceDemand579, requiredResource_ParametricResourceDemand582, action_ParametricResourceDemand584, primaryBehaviour__RecoveryAction590, recoveryActionBehaviours__RecoveryAction592, failureTypes_FailureHandlingEntity595, failureHandlingAlternatives__RecoveryActionBehaviour587, recoveryAction__RecoveryActionBehaviour588, specifiedOutputParameterAbstractions_QoSAnnotations603, system_QoSAnnotations606, signature_SpecifiedQoSAnnation597, role_SpecifiedQoSAnnotation599, qosAnnotations_SpecifiedQoSAnnotation601, specification_SpecifiedExecutionTime620, specifiedQoSAnnotations_QoSAnnotations607, signature_SpecifiedOutputParameterAbstraction609, role_SpecifiedOutputParameterAbstraction611, expectedExternalOutputs_SpecifiedOutputParameterAbstraction614, qosAnnotations_SpecifiedOutputParameterAbstraction617, externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation625, assemblyContext_ComponentSpecifiedExecutionTime623, activeResourceSpecifications_ResourceContainer641, resourceEnvironment_ResourceContainer644, nestedResourceContainers__ResourceContainer647, parentResourceContainer__ResourceContainer650, qosAnnotations_System627, linkingResources__ResourceEnvironment630, resourceContainer_ResourceEnvironment632, connectedResourceContainers_LinkingResource634, communicationLinkResourceSpecifications_LinkingResource636, resourceEnvironment_LinkingResource639, resourceContainer_AllocationContext675, assemblyContext_AllocationContext677, allocation_AllocationContext680, eventChannel__AllocationContext681, schedulingPolicy653, activeResourceType_ActiveResourceSpecification655, processingRate_ProcessingResourceSpecification658, resourceContainer_ProcessingResourceSpecification661, linkingResource_CommunicationLinkResourceSpecification664, communicationLinkResourceType_CommunicationLinkResourceSpecification667, latency_CommunicationLinkResourceSpecification669, throughput_CommunicationLinkResourceSpecification672, targetResourceEnvironment_Allocation683, system_Allocation685, allocationContexts_Allocation688, completions_CompletionRepository690, requiredCommunicationLinkResource_ParametricResourceDemand691},
    generalizations={gen_pcm_pc_av_core_pc_av_PCMRandomVariable_RandomVariable, gen_pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingEntity_Entity, gen_pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity_composition_pc_av_ComposedStructure, gen_pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity_entity_pc_av_InterfaceProvidingRequiringEntity, gen_pcm_pc_av_entity_pc_av_ResourceProvidedRole_Role, gen_pcm_pc_av_entity_pc_av_InterfaceProvidingRequiringEntity_entity_pc_av_InterfaceProvidingEntity, gen_pcm_pc_av_entity_pc_av_InterfaceProvidingRequiringEntity_entity_pc_av_InterfaceRequiringEntity, gen_pcm_pc_av_entity_pc_av_InterfaceProvidingEntity_Entity, gen_pcm_pc_av_entity_pc_av_InterfaceRequiringEntity_entity_pc_av_Entity, gen_pcm_pc_av_entity_pc_av_InterfaceRequiringEntity_entity_pc_av_ResourceInterfaceRequiringEntity, gen_pcm_pc_av_entity_pc_av_ResourceInterfaceRequiringEntity_Entity, gen_pcm_pc_av_entity_pc_av_ResourceRequiredRole_Role, gen_pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingRequiringEntity_entity_pc_av_ResourceInterfaceRequiringEntity, gen_pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingRequiringEntity_entity_pc_av_ResourceInterfaceProvidingEntity, gen_pcm_pc_av_entity_pc_av_Entity_Identifier, gen_pcm_pc_av_entity_pc_av_Entity_entity_pc_av_NamedElement, gen_pcm_pc_av_composition_pc_av_DelegationConnector_Connector, gen_pcm_pc_av_composition_pc_av_Connector_Entity, gen_pcm_pc_av_composition_pc_av_ComposedStructure_Entity, gen_pcm_pc_av_composition_pc_av_ProvidedDelegationConnector_DelegationConnector, gen_pcm_pc_av_composition_pc_av_EventChannel_Entity, gen_pcm_pc_av_composition_pc_av_EventChannelSourceConnector_Connector, gen_pcm_pc_av_composition_pc_av_EventChannelSinkConnector_Connector, gen_pcm_pc_av_composition_pc_av_AssemblyConnector_Connector, gen_pcm_pc_av_composition_pc_av_RequiredDelegationConnector_DelegationConnector, gen_pcm_pc_av_composition_pc_av_SourceDelegationConnector_DelegationConnector, gen_pcm_pc_av_composition_pc_av_SinkDelegationConnector_DelegationConnector, gen_pcm_pc_av_composition_pc_av_AssemblyEventConnector_Connector, gen_pcm_pc_av_composition_pc_av_AssemblyContext_Entity, gen_pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector_Connector, gen_pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector_DelegationConnector, gen_pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector_DelegationConnector, gen_pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector_DelegationConnector, gen_pcm_pc_av_usagemodel_pc_av_UsageScenario_Entity, gen_pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall_AbstractUserAction, gen_pcm_pc_av_usagemodel_pc_av_AbstractUserAction_Entity, gen_pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour_Entity, gen_pcm_pc_av_usagemodel_pc_av_Start_AbstractUserAction, gen_pcm_pc_av_usagemodel_pc_av_OpenWorkload_Workload, gen_pcm_pc_av_usagemodel_pc_av_Branch_AbstractUserAction, gen_pcm_pc_av_usagemodel_pc_av_Loop_AbstractUserAction, gen_pcm_pc_av_usagemodel_pc_av_Stop_AbstractUserAction, gen_pcm_pc_av_repository_pc_av_PassiveResource_Entity, gen_pcm_pc_av_repository_pc_av_BasicComponent_ImplementationComponentType, gen_pcm_pc_av_usagemodel_pc_av_Delay_AbstractUserAction, gen_pcm_pc_av_usagemodel_pc_av_ClosedWorkload_Workload, gen_pcm_pc_av_repository_pc_av_ImplementationComponentType_RepositoryComponent, gen_pcm_pc_av_repository_pc_av_Repository_Entity, gen_pcm_pc_av_repository_pc_av_RepositoryComponent_InterfaceProvidingRequiringEntity, gen_pcm_pc_av_repository_pc_av_ProvidedRole_Role, gen_pcm_pc_av_repository_pc_av_Interface_Entity, gen_pcm_pc_av_repository_pc_av_InfrastructureSignature_Signature, gen_pcm_pc_av_repository_pc_av_InfrastructureInterface_Interface, gen_pcm_pc_av_repository_pc_av_InfrastructureRequiredRole_RequiredRole, gen_pcm_pc_av_repository_pc_av_RequiredRole_Role, gen_pcm_pc_av_repository_pc_av_EventGroup_Interface, gen_pcm_pc_av_repository_pc_av_EventType_Signature, gen_pcm_pc_av_repository_pc_av_Signature_Entity, gen_pcm_pc_av_repository_pc_av_OperationRequiredRole_RequiredRole, gen_pcm_pc_av_repository_pc_av_SourceRole_RequiredRole, gen_pcm_pc_av_repository_pc_av_SinkRole_ProvidedRole, gen_pcm_pc_av_repository_pc_av_OperationSignature_Signature, gen_pcm_pc_av_repository_pc_av_OperationInterface_Interface, gen_pcm_pc_av_repository_pc_av_ProvidesComponentType_RepositoryComponent, gen_pcm_pc_av_repository_pc_av_OperationProvidedRole_ProvidedRole, gen_pcm_pc_av_repository_pc_av_InfrastructureProvidedRole_ProvidedRole, gen_pcm_pc_av_repository_pc_av_CompleteComponentType_RepositoryComponent, gen_pcm_pc_av_repository_pc_av_CollectionDataType_entity_pc_av_Entity, gen_pcm_pc_av_repository_pc_av_CollectionDataType_repository_pc_av_DataType, gen_pcm_pc_av_repository_pc_av_CompositeDataType_entity_pc_av_Entity, gen_pcm_pc_av_repository_pc_av_CompositeDataType_repository_pc_av_DataType, gen_pcm_pc_av_repository_pc_av_CompositeComponent_entity_pc_av_ComposedProvidingRequiringEntity, gen_pcm_pc_av_repository_pc_av_CompositeComponent_repository_pc_av_ImplementationComponentType, gen_pcm_pc_av_repository_pc_av_PrimitiveDataType_DataType, gen_pcm_pc_av_resourcetype_pc_av_ResourceType_entity_pc_av_Entity, gen_pcm_pc_av_resourcetype_pc_av_ResourceType_UnitCarryingElement, gen_pcm_pc_av_resourcetype_pc_av_ResourceType_entity_pc_av_ResourceInterfaceProvidingEntity, gen_pcm_pc_av_repository_pc_av_InnerDeclaration_NamedElement, gen_pcm_pc_av_resourcetype_pc_av_SchedulingPolicy_Entity, gen_pcm_pc_av_resourcetype_pc_av_CommunicationLinkResourceType_ResourceType, gen_pcm_pc_av_repository_pc_av_Role_Entity, gen_pcm_pc_av_resourcetype_pc_av_ResourceInterface_Entity, gen_pcm_pc_av_resourcetype_pc_av_ResourceSignature_Entity, gen_pcm_pc_av_resourcetype_pc_av_ProcessingResourceType_ResourceType, gen_pcm_pc_av_parameter_pc_av_CharacterisedVariable_Variable, gen_pcm_pc_av_reliability_pc_av_SoftwareInducedFailureType_FailureType, gen_pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_pc_av_reliability_pc_av_NetworkInducedFailureType_FailureType, gen_pcm_pc_av_reliability_pc_av_HardwareInducedFailureType_FailureType, gen_pcm_pc_av_reliability_pc_av_ResourceTimeoutFailureType_SoftwareInducedFailureType, gen_pcm_pc_av_reliability_pc_av_FailureType_Entity, gen_pcm_pc_av_seff_pc_av_StopAction_AbstractInternalControlFlowAction, gen_pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction_AbstractAction, gen_pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_pc_av_seff_pc_av_AbstractAction_Entity, gen_pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour_Identifier, gen_pcm_pc_av_seff_pc_av_AbstractLoopAction_AbstractInternalControlFlowAction, gen_pcm_pc_av_seff_pc_av_AbstractBranchTransition_Entity, gen_pcm_pc_av_seff_pc_av_BranchAction_AbstractInternalControlFlowAction, gen_pcm_pc_av_seff_pc_av_StartAction_AbstractInternalControlFlowAction, gen_pcm_pc_av_seff_pc_av_ResourceDemandingSEFF_Identifier, gen_pcm_pc_av_seff_pc_av_ResourceDemandingSEFF_seff_pc_av_ServiceEffectSpecification, gen_pcm_pc_av_seff_pc_av_ResourceDemandingSEFF_seff_pc_av_ResourceDemandingBehaviour, gen_pcm_pc_av_seff_pc_av_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour, gen_pcm_pc_av_seff_pc_av_LoopAction_AbstractLoopAction, gen_pcm_pc_av_seff_pc_av_ForkAction_AbstractInternalControlFlowAction, gen_pcm_pc_av_seff_pc_av_ForkedBehaviour_ResourceDemandingBehaviour, gen_pcm_pc_av_seff_pc_av_ExternalCallAction_seff_pc_av_AbstractAction, gen_pcm_pc_av_seff_pc_av_ExternalCallAction_seff_pc_av_CallReturnAction, gen_pcm_pc_av_seff_pc_av_ExternalCallAction_seff_reliability_pc_av_FailureHandlingEntity, gen_pcm_pc_av_seff_pc_av_ReleaseAction_AbstractInternalControlFlowAction, gen_pcm_pc_av_seff_pc_av_CollectionIteratorAction_AbstractLoopAction, gen_pcm_pc_av_seff_pc_av_GuardedBranchTransition_AbstractBranchTransition, gen_pcm_pc_av_seff_pc_av_CallReturnAction_CallAction, gen_pcm_pc_av_seff_pc_av_ProbabilisticBranchTransition_AbstractBranchTransition, gen_pcm_pc_av_seff_pc_av_AcquireAction_AbstractInternalControlFlowAction, gen_pcm_pc_av_seff_pc_av_InternalAction_AbstractInternalControlFlowAction, gen_pcm_pc_av_seff_pc_av_SetVariableAction_AbstractInternalControlFlowAction, gen_pcm_pc_av_seff_pc_av_InternalCallAction_seff_pc_av_CallAction, gen_pcm_pc_av_seff_pc_av_InternalCallAction_seff_pc_av_AbstractInternalControlFlowAction, gen_pcm_pc_av_seff_pc_av_EmitEventAction_seff_pc_av_AbstractAction, gen_pcm_pc_av_seff_pc_av_EmitEventAction_seff_pc_av_CallAction, gen_pcm_pc_av_seff_performance_pc_av_InfrastructureCall_CallAction, gen_pcm_pc_av_seff_performance_pc_av_ResourceCall_CallAction, gen_pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour_seff_reliability_pc_av_FailureHandlingEntity, gen_pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour_seff_pc_av_ResourceDemandingBehaviour, gen_pcm_pc_av_seff_reliability_pc_av_FailureHandlingEntity_Entity, gen_pcm_pc_av_seff_reliability_pc_av_RecoveryAction_AbstractInternalControlFlowAction, gen_pcm_pc_av_qosannotations_pc_av_QoSAnnotations_Entity, gen_pcm_pc_av_qos_performance_pc_av_SystemSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_pc_av_qos_performance_pc_av_SpecifiedExecutionTime_SpecifiedQoSAnnotation, gen_pcm_pc_av_qos_performance_pc_av_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_pc_av_system_pc_av_System_entity_pc_av_Entity, gen_pcm_pc_av_system_pc_av_System_entity_pc_av_ComposedProvidingRequiringEntity, gen_pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation, gen_pcm_pc_av_resourceenvironment_pc_av_ResourceContainer_Entity, gen_pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification_Identifier, gen_pcm_pc_av_resourceenvironment_pc_av_ResourceEnvironment_NamedElement, gen_pcm_pc_av_resourceenvironment_pc_av_LinkingResource_Entity, gen_pcm_pc_av_allocation_pc_av_AllocationContext_Entity, gen_pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification_Identifier, gen_pcm_pc_av_subsystem_pc_av_SubSystem_entity_pc_av_ComposedProvidingRequiringEntity, gen_pcm_pc_av_subsystem_pc_av_SubSystem_repository_pc_av_RepositoryComponent, gen_pcm_pc_av_completions_pc_av_Completion_entity_pc_av_ComposedProvidingRequiringEntity, gen_pcm_pc_av_completions_pc_av_Completion_repository_pc_av_ImplementationComponentType, gen_pcm_pc_av_allocation_pc_av_Allocation_Entity, gen_pcm_pc_av_completions_pc_av_DelegatingExternalCallAction_ExternalCallAction, gen_pcm_pc_av_completions_pc_av_NetworkDemandParametricResourceDemand_ParametricResourceDemand},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)