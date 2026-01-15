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
ComponentType: Enumeration = Enumeration(
    name="ComponentType",
    literals={
            EnumerationLiteral(name="BUSINESS_COMPONENT"),
			EnumerationLiteral(name="INFRASTRUCTURE_COMPONENT")
    }
)

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
pcm_pc_pc_DummyClass = Class(name="pcm::pc::pc::DummyClass")
pcm_pc_pc_PointcutPointcut = Class(name="pcm::pc::pc::PointcutPointcut")
pcm_pc_pc_EObject = Class(name="pcm::pc::pc::EObject")
pcm_pc_pc_Pointcut = Class(name="pcm::pc::pc::Pointcut")
seff_performance_pc_pc_ResourceCall = Class(name="seff::performance::pc::pc::ResourceCall")
seff_performance_pc_pc_ParametricResourceDemand = Class(name="seff::performance::pc::pc::ParametricResourceDemand")
LoopAction = Class(name="LoopAction")
GuardedBranchTransition = Class(name="GuardedBranchTransition")
qos_performance_pc_pc_SpecifiedExecutionTime = Class(name="qos::performance::pc::pc::SpecifiedExecutionTime")
composition_pc_pc_EventChannelSinkConnector = Class(name="composition::pc::pc::EventChannelSinkConnector")
composition_pc_pc_AssemblyEventConnector = Class(name="composition::pc::pc::AssemblyEventConnector")
pcm_pc_pc_core_pc_pc_PCMRandomVariable = Class(name="pcm::pc::pc::core::pc::pc::PCMRandomVariable")
RandomVariable = Class(name="RandomVariable")
ClosedWorkload = Class(name="ClosedWorkload")
PassiveResource = Class(name="PassiveResource")
VariableCharacterisation = Class(name="VariableCharacterisation")
seff_performance_pc_pc_InfrastructureCall = Class(name="seff::performance::pc::pc::InfrastructureCall")
pcm_pc_pc_entity_pc_pc_InterfaceProvidingEntity = Class(name="pcm::pc::pc::entity::pc::pc::InterfaceProvidingEntity")
Entity = Class(name="Entity")
ProvidedRole = Class(name="ProvidedRole")
pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity = Class(name="pcm::pc::pc::entity::pc::pc::InterfaceRequiringEntity")
entity_pc_pc_Entity = Class(name="entity::pc::pc::Entity")
entity_pc_pc_ResourceInterfaceRequiringEntity = Class(name="entity::pc::pc::ResourceInterfaceRequiringEntity")
RequiredRole = Class(name="RequiredRole")
pcm_pc_pc_entity_pc_pc_ResourceInterfaceRequiringEntity = Class(name="pcm::pc::pc::entity::pc::pc::ResourceInterfaceRequiringEntity")
entity_pc_pc_ResourceRequiredRole = Class(name="entity::pc::pc::ResourceRequiredRole")
pcm_pc_pc_entity_pc_pc_ResourceRequiredRole = Class(name="pcm::pc::pc::entity::pc::pc::ResourceRequiredRole")
Loop = Class(name="Loop")
OpenWorkload = Class(name="OpenWorkload")
Delay = Class(name="Delay")
CommunicationLinkResourceSpecification = Class(name="CommunicationLinkResourceSpecification")
ProcessingResourceSpecification = Class(name="ProcessingResourceSpecification")
pcm_pc_pc_entity_pc_pc_ResourceProvidedRole = Class(name="pcm::pc::pc::entity::pc::pc::ResourceProvidedRole")
Role = Class(name="Role")
entity_pc_pc_ResourceInterfaceProvidingEntity = Class(name="entity::pc::pc::ResourceInterfaceProvidingEntity")
ResourceInterface = Class(name="ResourceInterface")
pcm_pc_pc_entity_pc_pc_InterfaceProvidingRequiringEntity = Class(name="pcm::pc::pc::entity::pc::pc::InterfaceProvidingRequiringEntity")
entity_pc_pc_InterfaceProvidingEntity = Class(name="entity::pc::pc::InterfaceProvidingEntity")
entity_pc_pc_InterfaceRequiringEntity = Class(name="entity::pc::pc::InterfaceRequiringEntity")
pcm_pc_pc_composition_pc_pc_DelegationConnector = Class(name="pcm::pc::pc::composition::pc::pc::DelegationConnector")
Connector = Class(name="Connector")
pcm_pc_pc_composition_pc_pc_Connector = Class(name="pcm::pc::pc::composition::pc::pc::Connector")
pcm_pc_pc_composition_pc_pc_ComposedStructure = Class(name="pcm::pc::pc::composition::pc::pc::ComposedStructure")
pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingEntity = Class(name="pcm::pc::pc::entity::pc::pc::ResourceInterfaceProvidingEntity")
entity_pc_pc_ResourceProvidedRole = Class(name="entity::pc::pc::ResourceProvidedRole")
pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity = Class(name="pcm::pc::pc::entity::pc::pc::ComposedProvidingRequiringEntity")
composition_pc_pc_ComposedStructure = Class(name="composition::pc::pc::ComposedStructure")
entity_pc_pc_InterfaceProvidingRequiringEntity = Class(name="entity::pc::pc::InterfaceProvidingRequiringEntity")
pcm_pc_pc_entity_pc_pc_NamedElement = Class(name="pcm::pc::pc::entity::pc::pc::NamedElement")
pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingRequiringEntity = Class(name="pcm::pc::pc::entity::pc::pc::ResourceInterfaceProvidingRequiringEntity")
pcm_pc_pc_entity_pc_pc_Entity = Class(name="pcm::pc::pc::entity::pc::pc::Entity")
Identifier = Class(name="Identifier")
entity_pc_pc_NamedElement = Class(name="entity::pc::pc::NamedElement")
pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector = Class(name="pcm::pc::pc::composition::pc::pc::EventChannelSourceConnector")
SourceRole = Class(name="SourceRole")
pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector = Class(name="pcm::pc::pc::composition::pc::pc::EventChannelSinkConnector")
SinkRole = Class(name="SinkRole")
PCMRandomVariable = Class(name="PCMRandomVariable")
composition_pc_pc_AssemblyContext = Class(name="composition::pc::pc::AssemblyContext")
composition_pc_pc_ResourceRequiredDelegationConnector = Class(name="composition::pc::pc::ResourceRequiredDelegationConnector")
composition_pc_pc_EventChannel = Class(name="composition::pc::pc::EventChannel")
composition_pc_pc_Connector = Class(name="composition::pc::pc::Connector")
pcm_pc_pc_composition_pc_pc_ResourceRequiredDelegationConnector = Class(name="pcm::pc::pc::composition::pc::pc::ResourceRequiredDelegationConnector")
pcm_pc_pc_composition_pc_pc_EventChannel = Class(name="pcm::pc::pc::composition::pc::pc::EventChannel")
EventGroup = Class(name="EventGroup")
composition_pc_pc_EventChannelSourceConnector = Class(name="composition::pc::pc::EventChannelSourceConnector")
OperationRequiredRole = Class(name="OperationRequiredRole")
pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector = Class(name="pcm::pc::pc::composition::pc::pc::ProvidedDelegationConnector")
DelegationConnector = Class(name="DelegationConnector")
OperationProvidedRole = Class(name="OperationProvidedRole")
pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector = Class(name="pcm::pc::pc::composition::pc::pc::RequiredDelegationConnector")
pcm_pc_pc_composition_pc_pc_AssemblyConnector = Class(name="pcm::pc::pc::composition::pc::pc::AssemblyConnector")
pcm_pc_pc_composition_pc_pc_AssemblyEventConnector = Class(name="pcm::pc::pc::composition::pc::pc::AssemblyEventConnector")
pcm_pc_pc_composition_pc_pc_SourceDelegationConnector = Class(name="pcm::pc::pc::composition::pc::pc::SourceDelegationConnector")
pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector = Class(name="pcm::pc::pc::composition::pc::pc::RequiredInfrastructureDelegationConnector")
pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector = Class(name="pcm::pc::pc::composition::pc::pc::RequiredResourceDelegationConnector")
pcm_pc_pc_composition_pc_pc_AssemblyContext = Class(name="pcm::pc::pc::composition::pc::pc::AssemblyContext")
pcm_pc_pc_composition_pc_pc_SinkDelegationConnector = Class(name="pcm::pc::pc::composition::pc::pc::SinkDelegationConnector")
pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector = Class(name="pcm::pc::pc::composition::pc::pc::AssemblyInfrastructureConnector")
InfrastructureProvidedRole = Class(name="InfrastructureProvidedRole")
InfrastructureRequiredRole = Class(name="InfrastructureRequiredRole")
pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector = Class(name="pcm::pc::pc::composition::pc::pc::ProvidedInfrastructureDelegationConnector")
pcm_pc_pc_usagemodel_pc_pc_UsageModel = Class(name="pcm::pc::pc::usagemodel::pc::pc::UsageModel")
UserData = Class(name="UserData")
pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall = Class(name="pcm::pc::pc::usagemodel::pc::pc::EntryLevelSystemCall")
AbstractUserAction = Class(name="AbstractUserAction")
RepositoryComponent = Class(name="RepositoryComponent")
VariableUsage = Class(name="VariableUsage")
pcm_pc_pc_usagemodel_pc_pc_Workload = Class(name="pcm::pc::pc::usagemodel::pc::pc::Workload")
UsageScenario = Class(name="UsageScenario")
pcm_pc_pc_usagemodel_pc_pc_UsageScenario = Class(name="pcm::pc::pc::usagemodel::pc::pc::UsageScenario")
UsageModel = Class(name="UsageModel")
ScenarioBehaviour = Class(name="ScenarioBehaviour")
Workload = Class(name="Workload")
pcm_pc_pc_usagemodel_pc_pc_UserData = Class(name="pcm::pc::pc::usagemodel::pc::pc::UserData")
BranchTransition = Class(name="BranchTransition")
OperationSignature = Class(name="OperationSignature")
pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction = Class(name="pcm::pc::pc::usagemodel::pc::pc::AbstractUserAction")
pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour = Class(name="pcm::pc::pc::usagemodel::pc::pc::ScenarioBehaviour")
pcm_pc_pc_usagemodel_pc_pc_Stop = Class(name="pcm::pc::pc::usagemodel::pc::pc::Stop")
pcm_pc_pc_usagemodel_pc_pc_Start = Class(name="pcm::pc::pc::usagemodel::pc::pc::Start")
pcm_pc_pc_usagemodel_pc_pc_OpenWorkload = Class(name="pcm::pc::pc::usagemodel::pc::pc::OpenWorkload")
pcm_pc_pc_usagemodel_pc_pc_BranchTransition = Class(name="pcm::pc::pc::usagemodel::pc::pc::BranchTransition")
Branch = Class(name="Branch")
pcm_pc_pc_usagemodel_pc_pc_Branch = Class(name="pcm::pc::pc::usagemodel::pc::pc::Branch")
pcm_pc_pc_usagemodel_pc_pc_Loop = Class(name="pcm::pc::pc::usagemodel::pc::pc::Loop")
pcm_pc_pc_repository_pc_pc_PassiveResource = Class(name="pcm::pc::pc::repository::pc::pc::PassiveResource")
BasicComponent = Class(name="BasicComponent")
ResourceTimeoutFailureType = Class(name="ResourceTimeoutFailureType")
pcm_pc_pc_repository_pc_pc_BasicComponent = Class(name="pcm::pc::pc::repository::pc::pc::BasicComponent")
ImplementationComponentType = Class(name="ImplementationComponentType")
pcm_pc_pc_usagemodel_pc_pc_Delay = Class(name="pcm::pc::pc::usagemodel::pc::pc::Delay")
pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload = Class(name="pcm::pc::pc::usagemodel::pc::pc::ClosedWorkload")
CompleteComponentType = Class(name="CompleteComponentType")
ServiceEffectSpecification = Class(name="ServiceEffectSpecification")
pcm_pc_pc_repository_pc_pc_ImplementationComponentType = Class(name="pcm::pc::pc::repository::pc::pc::ImplementationComponentType")
ResourceSignature = Class(name="ResourceSignature")
pcm_pc_pc_repository_pc_pc_DataType = Class(name="pcm::pc::pc::repository::pc::pc::DataType")
pcm_pc_pc_repository_pc_pc_Repository = Class(name="pcm::pc::pc::repository::pc::pc::Repository")
Interface = Class(name="Interface")
pcm_pc_pc_repository_pc_pc_RepositoryComponent = Class(name="pcm::pc::pc::repository::pc::pc::RepositoryComponent")
InterfaceProvidingRequiringEntity = Class(name="InterfaceProvidingRequiringEntity")
Repository = Class(name="Repository")
pcm_pc_pc_repository_pc_pc_ProvidedRole = Class(name="pcm::pc::pc::repository::pc::pc::ProvidedRole")
pcm_pc_pc_repository_pc_pc_Parameter = Class(name="pcm::pc::pc::repository::pc::pc::Parameter")
DataType = Class(name="DataType")
InfrastructureSignature = Class(name="InfrastructureSignature")
EventType = Class(name="EventType")
pcm_pc_pc_repository_pc_pc_RequiredCharacterisation = Class(name="pcm::pc::pc::repository::pc::pc::RequiredCharacterisation")
Parameter_ = Class(name="Parameter")
pcm_pc_pc_repository_pc_pc_EventGroup = Class(name="pcm::pc::pc::repository::pc::pc::EventGroup")
pcm_pc_pc_repository_pc_pc_EventType = Class(name="pcm::pc::pc::repository::pc::pc::EventType")
Signature = Class(name="Signature")
FailureType = Class(name="FailureType")
pcm_pc_pc_repository_pc_pc_Interface = Class(name="pcm::pc::pc::repository::pc::pc::Interface")
Protocol = Class(name="Protocol")
RequiredCharacterisation = Class(name="RequiredCharacterisation")
pcm_pc_pc_repository_pc_pc_RequiredRole = Class(name="pcm::pc::pc::repository::pc::pc::RequiredRole")
pcm_pc_pc_repository_pc_pc_OperationSignature = Class(name="pcm::pc::pc::repository::pc::pc::OperationSignature")
OperationInterface = Class(name="OperationInterface")
pcm_pc_pc_repository_pc_pc_Signature = Class(name="pcm::pc::pc::repository::pc::pc::Signature")
ExceptionType = Class(name="ExceptionType")
pcm_pc_pc_repository_pc_pc_ExceptionType = Class(name="pcm::pc::pc::repository::pc::pc::ExceptionType")
pcm_pc_pc_repository_pc_pc_InfrastructureSignature = Class(name="pcm::pc::pc::repository::pc::pc::InfrastructureSignature")
InfrastructureInterface = Class(name="InfrastructureInterface")
pcm_pc_pc_repository_pc_pc_InfrastructureInterface = Class(name="pcm::pc::pc::repository::pc::pc::InfrastructureInterface")
pcm_pc_pc_repository_pc_pc_InfrastructureRequiredRole = Class(name="pcm::pc::pc::repository::pc::pc::InfrastructureRequiredRole")
pcm_pc_pc_repository_pc_pc_SourceRole = Class(name="pcm::pc::pc::repository::pc::pc::SourceRole")
pcm_pc_pc_repository_pc_pc_SinkRole = Class(name="pcm::pc::pc::repository::pc::pc::SinkRole")
pcm_pc_pc_repository_pc_pc_OperationProvidedRole = Class(name="pcm::pc::pc::repository::pc::pc::OperationProvidedRole")
pcm_pc_pc_repository_pc_pc_InfrastructureProvidedRole = Class(name="pcm::pc::pc::repository::pc::pc::InfrastructureProvidedRole")
pcm_pc_pc_repository_pc_pc_OperationInterface = Class(name="pcm::pc::pc::repository::pc::pc::OperationInterface")
pcm_pc_pc_repository_pc_pc_OperationRequiredRole = Class(name="pcm::pc::pc::repository::pc::pc::OperationRequiredRole")
pcm_pc_pc_repository_pc_pc_ProvidesComponentType = Class(name="pcm::pc::pc::repository::pc::pc::ProvidesComponentType")
pcm_pc_pc_repository_pc_pc_CompositeComponent = Class(name="pcm::pc::pc::repository::pc::pc::CompositeComponent")
entity_pc_pc_ComposedProvidingRequiringEntity = Class(name="entity::pc::pc::ComposedProvidingRequiringEntity")
repository_pc_pc_ImplementationComponentType = Class(name="repository::pc::pc::ImplementationComponentType")
pcm_pc_pc_repository_pc_pc_CompleteComponentType = Class(name="pcm::pc::pc::repository::pc::pc::CompleteComponentType")
ProvidesComponentType = Class(name="ProvidesComponentType")
InnerDeclaration = Class(name="InnerDeclaration")
pcm_pc_pc_repository_pc_pc_InnerDeclaration = Class(name="pcm::pc::pc::repository::pc::pc::InnerDeclaration")
NamedElement = Class(name="NamedElement")
pcm_pc_pc_repository_pc_pc_Role = Class(name="pcm::pc::pc::repository::pc::pc::Role")
pcm_pc_pc_resourcetype_pc_pc_ResourceSignature = Class(name="pcm::pc::pc::resourcetype::pc::pc::ResourceSignature")
pcm_pc_pc_repository_pc_pc_PrimitiveDataType = Class(name="pcm::pc::pc::repository::pc::pc::PrimitiveDataType")
pcm_pc_pc_repository_pc_pc_CollectionDataType = Class(name="pcm::pc::pc::repository::pc::pc::CollectionDataType")
repository_pc_pc_DataType = Class(name="repository::pc::pc::DataType")
pcm_pc_pc_repository_pc_pc_CompositeDataType = Class(name="pcm::pc::pc::repository::pc::pc::CompositeDataType")
CompositeDataType = Class(name="CompositeDataType")
pcm_pc_pc_resourcetype_pc_pc_CommunicationLinkResourceType = Class(name="pcm::pc::pc::resourcetype::pc::pc::CommunicationLinkResourceType")
NetworkInducedFailureType = Class(name="NetworkInducedFailureType")
pcm_pc_pc_resourcetype_pc_pc_ResourceInterface = Class(name="pcm::pc::pc::resourcetype::pc::pc::ResourceInterface")
pcm_pc_pc_protocol_pc_pc_Protocol = Class(name="pcm::pc::pc::protocol::pc::pc::Protocol")
pcm_pc_pc_parameter_pc_pc_VariableUsage = Class(name="pcm::pc::pc::parameter::pc::pc::VariableUsage")
pcm_pc_pc_resourcetype_pc_pc_ProcessingResourceType = Class(name="pcm::pc::pc::resourcetype::pc::pc::ProcessingResourceType")
ResourceType = Class(name="ResourceType")
HardwareInducedFailureType = Class(name="HardwareInducedFailureType")
pcm_pc_pc_resourcetype_pc_pc_ResourceType = Class(name="pcm::pc::pc::resourcetype::pc::pc::ResourceType")
UnitCarryingElement = Class(name="UnitCarryingElement")
ResourceRepository = Class(name="ResourceRepository")
pcm_pc_pc_resourcetype_pc_pc_ResourceRepository = Class(name="pcm::pc::pc::resourcetype::pc::pc::ResourceRepository")
SchedulingPolicy = Class(name="SchedulingPolicy")
pcm_pc_pc_resourcetype_pc_pc_SchedulingPolicy = Class(name="pcm::pc::pc::resourcetype::pc::pc::SchedulingPolicy")
pcm_pc_pc_parameter_pc_pc_VariableCharacterisation = Class(name="pcm::pc::pc::parameter::pc::pc::VariableCharacterisation")
pcm_pc_pc_parameter_pc_pc_CharacterisedVariable = Class(name="pcm::pc::pc::parameter::pc::pc::CharacterisedVariable")
Variable = Class(name="Variable")
CallAction = Class(name="CallAction")
SynchronisationPoint = Class(name="SynchronisationPoint")
CallReturnAction = Class(name="CallReturnAction")
SetVariableAction = Class(name="SetVariableAction")
SpecifiedOutputParameterAbstraction = Class(name="SpecifiedOutputParameterAbstraction")
EntryLevelSystemCall = Class(name="EntryLevelSystemCall")
parameter_pc_pc_pcm_pc_pc_AbstractNamedReference = Class(name="parameter::pc::pc::pcm::pc::pc::AbstractNamedReference")
ProcessingResourceType = Class(name="ProcessingResourceType")
pcm_pc_pc_reliability_pc_pc_SoftwareInducedFailureType = Class(name="pcm::pc::pc::reliability::pc::pc::SoftwareInducedFailureType")
InternalFailureOccurrenceDescription = Class(name="InternalFailureOccurrenceDescription")
pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription = Class(name="pcm::pc::pc::reliability::pc::pc::InternalFailureOccurrenceDescription")
FailureOccurrenceDescription = Class(name="FailureOccurrenceDescription")
pcm_pc_pc_reliability_pc_pc_FailureOccurrenceDescription = Class(name="pcm::pc::pc::reliability::pc::pc::FailureOccurrenceDescription")
pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType = Class(name="pcm::pc::pc::reliability::pc::pc::HardwareInducedFailureType")
CommunicationLinkResourceType = Class(name="CommunicationLinkResourceType")
pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription = Class(name="pcm::pc::pc::reliability::pc::pc::ExternalFailureOccurrenceDescription")
qos_reliability_pc_pc_SpecifiedReliabilityAnnotation = Class(name="qos::reliability::pc::pc::SpecifiedReliabilityAnnotation")
pcm_pc_pc_reliability_pc_pc_ResourceTimeoutFailureType = Class(name="pcm::pc::pc::reliability::pc::pc::ResourceTimeoutFailureType")
InternalAction = Class(name="InternalAction")
SoftwareInducedFailureType = Class(name="SoftwareInducedFailureType")
pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType = Class(name="pcm::pc::pc::reliability::pc::pc::NetworkInducedFailureType")
pcm_pc_pc_seff_pc_pc_AbstractAction = Class(name="pcm::pc::pc::seff::pc::pc::AbstractAction")
ResourceDemandingBehaviour = Class(name="ResourceDemandingBehaviour")
pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour = Class(name="pcm::pc::pc::seff::pc::pc::ResourceDemandingBehaviour")
pcm_pc_pc_reliability_pc_pc_FailureType = Class(name="pcm::pc::pc::reliability::pc::pc::FailureType")
pcm_pc_pc_seff_pc_pc_StopAction = Class(name="pcm::pc::pc::seff::pc::pc::StopAction")
AbstractInternalControlFlowAction = Class(name="AbstractInternalControlFlowAction")
pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction = Class(name="pcm::pc::pc::seff::pc::pc::AbstractInternalControlFlowAction")
AbstractAction = Class(name="AbstractAction")
BranchAction = Class(name="BranchAction")
pcm_pc_pc_seff_pc_pc_BranchAction = Class(name="pcm::pc::pc::seff::pc::pc::BranchAction")
pcm_pc_pc_seff_pc_pc_CallAction = Class(name="pcm::pc::pc::seff::pc::pc::CallAction")
AbstractLoopAction = Class(name="AbstractLoopAction")
AbstractBranchTransition = Class(name="AbstractBranchTransition")
pcm_pc_pc_seff_pc_pc_AbstractLoopAction = Class(name="pcm::pc::pc::seff::pc::pc::AbstractLoopAction")
pcm_pc_pc_seff_pc_pc_AbstractBranchTransition = Class(name="pcm::pc::pc::seff::pc::pc::AbstractBranchTransition")
pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF = Class(name="pcm::pc::pc::seff::pc::pc::ResourceDemandingSEFF")
seff_pc_pc_ServiceEffectSpecification = Class(name="seff::pc::pc::ServiceEffectSpecification")
seff_pc_pc_ResourceDemandingBehaviour = Class(name="seff::pc::pc::ResourceDemandingBehaviour")
ResourceDemandingInternalBehaviour = Class(name="ResourceDemandingInternalBehaviour")
pcm_pc_pc_seff_pc_pc_ResourceDemandingInternalBehaviour = Class(name="pcm::pc::pc::seff::pc::pc::ResourceDemandingInternalBehaviour")
ResourceDemandingSEFF = Class(name="ResourceDemandingSEFF")
pcm_pc_pc_seff_pc_pc_ReleaseAction = Class(name="pcm::pc::pc::seff::pc::pc::ReleaseAction")
pcm_pc_pc_seff_pc_pc_LoopAction = Class(name="pcm::pc::pc::seff::pc::pc::LoopAction")
pcm_pc_pc_seff_pc_pc_StartAction = Class(name="pcm::pc::pc::seff::pc::pc::StartAction")
pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification = Class(name="pcm::pc::pc::seff::pc::pc::ServiceEffectSpecification")
pcm_pc_pc_seff_pc_pc_ExternalCallAction = Class(name="pcm::pc::pc::seff::pc::pc::ExternalCallAction")
seff_pc_pc_AbstractAction = Class(name="seff::pc::pc::AbstractAction")
seff_pc_pc_CallReturnAction = Class(name="seff::pc::pc::CallReturnAction")
seff_reliability_pc_pc_FailureHandlingEntity = Class(name="seff::reliability::pc::pc::FailureHandlingEntity")
pcm_pc_pc_seff_pc_pc_ForkAction = Class(name="pcm::pc::pc::seff::pc::pc::ForkAction")
ForkedBehaviour = Class(name="ForkedBehaviour")
pcm_pc_pc_seff_pc_pc_ForkedBehaviour = Class(name="pcm::pc::pc::seff::pc::pc::ForkedBehaviour")
ForkAction = Class(name="ForkAction")
pcm_pc_pc_seff_pc_pc_SynchronisationPoint = Class(name="pcm::pc::pc::seff::pc::pc::SynchronisationPoint")
pcm_pc_pc_seff_pc_pc_CollectionIteratorAction = Class(name="pcm::pc::pc::seff::pc::pc::CollectionIteratorAction")
pcm_pc_pc_seff_pc_pc_GuardedBranchTransition = Class(name="pcm::pc::pc::seff::pc::pc::GuardedBranchTransition")
pcm_pc_pc_seff_pc_pc_SetVariableAction = Class(name="pcm::pc::pc::seff::pc::pc::SetVariableAction")
pcm_pc_pc_seff_pc_pc_CallReturnAction = Class(name="pcm::pc::pc::seff::pc::pc::CallReturnAction")
pcm_pc_pc_seff_pc_pc_ProbabilisticBranchTransition = Class(name="pcm::pc::pc::seff::pc::pc::ProbabilisticBranchTransition")
pcm_pc_pc_seff_pc_pc_AcquireAction = Class(name="pcm::pc::pc::seff::pc::pc::AcquireAction")
pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall = Class(name="pcm::pc::pc::seff::performance::pc::pc::InfrastructureCall")
pcm_pc_pc_seff_pc_pc_InternalCallAction = Class(name="pcm::pc::pc::seff::pc::pc::InternalCallAction")
seff_pc_pc_CallAction = Class(name="seff::pc::pc::CallAction")
seff_pc_pc_AbstractInternalControlFlowAction = Class(name="seff::pc::pc::AbstractInternalControlFlowAction")
pcm_pc_pc_seff_pc_pc_EmitEventAction = Class(name="pcm::pc::pc::seff::pc::pc::EmitEventAction")
pcm_pc_pc_seff_pc_pc_InternalAction = Class(name="pcm::pc::pc::seff::pc::pc::InternalAction")
pcm_pc_pc_seff_performance_pc_pc_ResourceCall = Class(name="pcm::pc::pc::seff::performance::pc::pc::ResourceCall")
pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour = Class(name="pcm::pc::pc::seff::reliability::pc::pc::RecoveryActionBehaviour")
seff_reliability_pc_pc_RecoveryActionBehaviour = Class(name="seff::reliability::pc::pc::RecoveryActionBehaviour")
pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand = Class(name="pcm::pc::pc::seff::performance::pc::pc::ParametricResourceDemand")
pcm_pc_pc_qosannotations_pc_pc_SpecifiedQoSAnnotation = Class(name="pcm::pc::pc::qosannotations::pc::pc::SpecifiedQoSAnnotation")
QoSAnnotations = Class(name="QoSAnnotations")
pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations = Class(name="pcm::pc::pc::qosannotations::pc::pc::QoSAnnotations")
seff_reliability_pc_pc_RecoveryAction = Class(name="seff::reliability::pc::pc::RecoveryAction")
pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction = Class(name="pcm::pc::pc::seff::reliability::pc::pc::RecoveryAction")
pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity = Class(name="pcm::pc::pc::seff::reliability::pc::pc::FailureHandlingEntity")
pcm_pc_pc_qos_performance_pc_pc_SpecifiedExecutionTime = Class(name="pcm::pc::pc::qos::performance::pc::pc::SpecifiedExecutionTime")
pcm_pc_pc_qos_performance_pc_pc_ComponentSpecifiedExecutionTime = Class(name="pcm::pc::pc::qos::performance::pc::pc::ComponentSpecifiedExecutionTime")
pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation = Class(name="pcm::pc::pc::qos::reliability::pc::pc::SpecifiedReliabilityAnnotation")
System = Class(name="System")
SpecifiedQoSAnnotation = Class(name="SpecifiedQoSAnnotation")
pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction = Class(name="pcm::pc::pc::qosannotations::pc::pc::SpecifiedOutputParameterAbstraction")
pcm_pc_pc_qos_performance_pc_pc_SystemSpecifiedExecutionTime = Class(name="pcm::pc::pc::qos::performance::pc::pc::SystemSpecifiedExecutionTime")
SpecifiedExecutionTime = Class(name="SpecifiedExecutionTime")
ExternalFailureOccurrenceDescription = Class(name="ExternalFailureOccurrenceDescription")
pcm_pc_pc_system_pc_pc_System = Class(name="pcm::pc::pc::system::pc::pc::System")
pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification = Class(name="pcm::pc::pc::resourceenvironment::pc::pc::ProcessingResourceSpecification")
pcm_pc_pc_resourceenvironment_pc_pc_ResourceEnvironment = Class(name="pcm::pc::pc::resourceenvironment::pc::pc::ResourceEnvironment")
LinkingResource = Class(name="LinkingResource")
ResourceContainer = Class(name="ResourceContainer")
pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource = Class(name="pcm::pc::pc::resourceenvironment::pc::pc::LinkingResource")
ResourceEnvironment = Class(name="ResourceEnvironment")
pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer = Class(name="pcm::pc::pc::resourceenvironment::pc::pc::ResourceContainer")
pcm_pc_pc_allocation_pc_pc_AllocationContext = Class(name="pcm::pc::pc::allocation::pc::pc::AllocationContext")
Allocation = Class(name="Allocation")
pcm_pc_pc_allocation_pc_pc_Allocation = Class(name="pcm::pc::pc::allocation::pc::pc::Allocation")
pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification = Class(name="pcm::pc::pc::resourceenvironment::pc::pc::CommunicationLinkResourceSpecification")
pcm_pc_pc_subsystem_pc_pc_SubSystem = Class(name="pcm::pc::pc::subsystem::pc::pc::SubSystem")
repository_pc_pc_RepositoryComponent = Class(name="repository::pc::pc::RepositoryComponent")
pcm_pc_pc_completions_pc_pc_Completion = Class(name="pcm::pc::pc::completions::pc::pc::Completion")
pcm_pc_pc_completions_pc_pc_CompletionRepository = Class(name="pcm::pc::pc::completions::pc::pc::CompletionRepository")
Completion = Class(name="Completion")
pcm_pc_pc_completions_pc_pc_DelegatingExternalCallAction = Class(name="pcm::pc::pc::completions::pc::pc::DelegatingExternalCallAction")
ExternalCallAction = Class(name="ExternalCallAction")
pcm_pc_pc_completions_pc_pc_NetworkDemandParametricResourceDemand = Class(name="pcm::pc::pc::completions::pc::pc::NetworkDemandParametricResourceDemand")
ParametricResourceDemand = Class(name="ParametricResourceDemand")
AllocationContext = Class(name="AllocationContext")

# pcm_pc_pc_DummyClass class attributes and methods

# pcm_pc_pc_PointcutPointcut class attributes and methods

# pcm_pc_pc_EObject class attributes and methods

# pcm_pc_pc_Pointcut class attributes and methods

# seff_performance_pc_pc_ResourceCall class attributes and methods

# seff_performance_pc_pc_ParametricResourceDemand class attributes and methods

# LoopAction class attributes and methods

# GuardedBranchTransition class attributes and methods

# qos_performance_pc_pc_SpecifiedExecutionTime class attributes and methods

# composition_pc_pc_EventChannelSinkConnector class attributes and methods

# composition_pc_pc_AssemblyEventConnector class attributes and methods

# pcm_pc_pc_core_pc_pc_PCMRandomVariable class attributes and methods
pcm_pc_pc_core_pc_pc_PCMRandomVariable_m_SpecificationMustNotBeNULL: Method = Method(name="SpecificationMustNotBeNULL", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_core_pc_pc_PCMRandomVariable.methods={pcm_pc_pc_core_pc_pc_PCMRandomVariable_m_SpecificationMustNotBeNULL}

# RandomVariable class attributes and methods

# ClosedWorkload class attributes and methods

# PassiveResource class attributes and methods

# VariableCharacterisation class attributes and methods

# seff_performance_pc_pc_InfrastructureCall class attributes and methods

# pcm_pc_pc_entity_pc_pc_InterfaceProvidingEntity class attributes and methods

# Entity class attributes and methods

# ProvidedRole class attributes and methods

# pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity class attributes and methods

# entity_pc_pc_Entity class attributes and methods

# entity_pc_pc_ResourceInterfaceRequiringEntity class attributes and methods

# RequiredRole class attributes and methods

# pcm_pc_pc_entity_pc_pc_ResourceInterfaceRequiringEntity class attributes and methods

# entity_pc_pc_ResourceRequiredRole class attributes and methods

# pcm_pc_pc_entity_pc_pc_ResourceRequiredRole class attributes and methods

# Loop class attributes and methods

# OpenWorkload class attributes and methods

# Delay class attributes and methods

# CommunicationLinkResourceSpecification class attributes and methods

# ProcessingResourceSpecification class attributes and methods

# pcm_pc_pc_entity_pc_pc_ResourceProvidedRole class attributes and methods

# Role class attributes and methods

# entity_pc_pc_ResourceInterfaceProvidingEntity class attributes and methods

# ResourceInterface class attributes and methods

# pcm_pc_pc_entity_pc_pc_InterfaceProvidingRequiringEntity class attributes and methods

# entity_pc_pc_InterfaceProvidingEntity class attributes and methods

# entity_pc_pc_InterfaceRequiringEntity class attributes and methods

# pcm_pc_pc_composition_pc_pc_DelegationConnector class attributes and methods

# Connector class attributes and methods

# pcm_pc_pc_composition_pc_pc_Connector class attributes and methods

# pcm_pc_pc_composition_pc_pc_ComposedStructure class attributes and methods
pcm_pc_pc_composition_pc_pc_ComposedStructure_m_MultipleConnectorsConstraint: Method = Method(name="MultipleConnectorsConstraint", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_composition_pc_pc_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors: Method = Method(name="MultipleConnectorsConstraintForAssemblyConnectors", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_composition_pc_pc_ComposedStructure.methods={pcm_pc_pc_composition_pc_pc_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors, pcm_pc_pc_composition_pc_pc_ComposedStructure_m_MultipleConnectorsConstraint}

# pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingEntity class attributes and methods

# entity_pc_pc_ResourceProvidedRole class attributes and methods

# pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity class attributes and methods
pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound: Method = Method(name="ProvidedRolesMustBeBound", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity.methods={pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound}

# composition_pc_pc_ComposedStructure class attributes and methods

# entity_pc_pc_InterfaceProvidingRequiringEntity class attributes and methods

# pcm_pc_pc_entity_pc_pc_NamedElement class attributes and methods
pcm_pc_pc_entity_pc_pc_NamedElement_entityName: Property = Property(name="entityName", type=StringType)
pcm_pc_pc_entity_pc_pc_NamedElement.attributes={pcm_pc_pc_entity_pc_pc_NamedElement_entityName}

# pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingRequiringEntity class attributes and methods

# pcm_pc_pc_entity_pc_pc_Entity class attributes and methods

# Identifier class attributes and methods

# entity_pc_pc_NamedElement class attributes and methods

# pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector class attributes and methods

# SourceRole class attributes and methods

# pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector class attributes and methods

# SinkRole class attributes and methods

# PCMRandomVariable class attributes and methods

# composition_pc_pc_AssemblyContext class attributes and methods

# composition_pc_pc_ResourceRequiredDelegationConnector class attributes and methods

# composition_pc_pc_EventChannel class attributes and methods

# composition_pc_pc_Connector class attributes and methods

# pcm_pc_pc_composition_pc_pc_ResourceRequiredDelegationConnector class attributes and methods

# pcm_pc_pc_composition_pc_pc_EventChannel class attributes and methods

# EventGroup class attributes and methods

# composition_pc_pc_EventChannelSourceConnector class attributes and methods

# OperationRequiredRole class attributes and methods

# pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector class attributes and methods
pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector.methods={pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure, pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame}

# DelegationConnector class attributes and methods

# OperationProvidedRole class attributes and methods

# pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector class attributes and methods
pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector: Method = Method(name="RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector.methods={pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure, pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame, pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector}

# pcm_pc_pc_composition_pc_pc_AssemblyConnector class attributes and methods
pcm_pc_pc_composition_pc_pc_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_composition_pc_pc_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch: Method = Method(name="AssemblyConnectorsReferencedInterfacesMustMatch", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_composition_pc_pc_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_composition_pc_pc_AssemblyConnector.methods={pcm_pc_pc_composition_pc_pc_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch, pcm_pc_pc_composition_pc_pc_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch, pcm_pc_pc_composition_pc_pc_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch}

# pcm_pc_pc_composition_pc_pc_AssemblyEventConnector class attributes and methods

# pcm_pc_pc_composition_pc_pc_SourceDelegationConnector class attributes and methods

# pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector class attributes and methods

# pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector class attributes and methods

# pcm_pc_pc_composition_pc_pc_AssemblyContext class attributes and methods

# pcm_pc_pc_composition_pc_pc_SinkDelegationConnector class attributes and methods

# pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector class attributes and methods

# InfrastructureProvidedRole class attributes and methods

# InfrastructureRequiredRole class attributes and methods

# pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector class attributes and methods

# pcm_pc_pc_usagemodel_pc_pc_UsageModel class attributes and methods

# UserData class attributes and methods

# pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall class attributes and methods
pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall_priority: Property = Property(name="priority", type=IntegerType)
pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem: Method = Method(name="EntryLevelSystemCallMustReferenceProvidedRoleOfASystem", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole: Method = Method(name="EntryLevelSystemCallSignatureMustMatchItsProvidedRole", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall.attributes={pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall_priority}
pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall.methods={pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole, pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem}

# AbstractUserAction class attributes and methods

# RepositoryComponent class attributes and methods

# VariableUsage class attributes and methods

# pcm_pc_pc_usagemodel_pc_pc_Workload class attributes and methods

# UsageScenario class attributes and methods

# pcm_pc_pc_usagemodel_pc_pc_UsageScenario class attributes and methods

# UsageModel class attributes and methods

# ScenarioBehaviour class attributes and methods

# Workload class attributes and methods

# pcm_pc_pc_usagemodel_pc_pc_UserData class attributes and methods

# BranchTransition class attributes and methods

# OperationSignature class attributes and methods

# pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction class attributes and methods

# pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour class attributes and methods
pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour_m_Exactlyonestop: Method = Method(name="Exactlyonestop", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor: Method = Method(name="EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour_m_Exactlyonestart: Method = Method(name="Exactlyonestart", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour.methods={pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor, pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour_m_Exactlyonestart, pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour_m_Exactlyonestop}

# pcm_pc_pc_usagemodel_pc_pc_Stop class attributes and methods
pcm_pc_pc_usagemodel_pc_pc_Stop_m_StopHasNoSuccessor: Method = Method(name="StopHasNoSuccessor", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_Stop.methods={pcm_pc_pc_usagemodel_pc_pc_Stop_m_StopHasNoSuccessor}

# pcm_pc_pc_usagemodel_pc_pc_Start class attributes and methods
pcm_pc_pc_usagemodel_pc_pc_Start_m_StartHasNoPredecessor: Method = Method(name="StartHasNoPredecessor", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_Start.methods={pcm_pc_pc_usagemodel_pc_pc_Start_m_StartHasNoPredecessor}

# pcm_pc_pc_usagemodel_pc_pc_OpenWorkload class attributes and methods
pcm_pc_pc_usagemodel_pc_pc_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified: Method = Method(name="InterArrivalTimeInOpenWorkloadNeedsToBeSpecified", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_OpenWorkload.methods={pcm_pc_pc_usagemodel_pc_pc_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified}

# pcm_pc_pc_usagemodel_pc_pc_BranchTransition class attributes and methods
pcm_pc_pc_usagemodel_pc_pc_BranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_pc_pc_usagemodel_pc_pc_BranchTransition.attributes={pcm_pc_pc_usagemodel_pc_pc_BranchTransition_branchProbability}

# Branch class attributes and methods

# pcm_pc_pc_usagemodel_pc_pc_Branch class attributes and methods
pcm_pc_pc_usagemodel_pc_pc_Branch_m_AllBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_Branch.methods={pcm_pc_pc_usagemodel_pc_pc_Branch_m_AllBranchProbabilitiesMustSumUpTo1}

# pcm_pc_pc_usagemodel_pc_pc_Loop class attributes and methods

# pcm_pc_pc_repository_pc_pc_PassiveResource class attributes and methods

# BasicComponent class attributes and methods

# ResourceTimeoutFailureType class attributes and methods

# pcm_pc_pc_repository_pc_pc_BasicComponent class attributes and methods
pcm_pc_pc_repository_pc_pc_BasicComponent_m_NoSeffTypeUsedTwice: Method = Method(name="NoSeffTypeUsedTwice", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_BasicComponent_m_ProvideSameInterfacesAsImplementationType: Method = Method(name="ProvideSameInterfacesAsImplementationType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_BasicComponent_m_RequireSameInterfacesAsImplementationType: Method = Method(name="RequireSameInterfacesAsImplementationType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_BasicComponent.methods={pcm_pc_pc_repository_pc_pc_BasicComponent_m_ProvideSameInterfacesAsImplementationType, pcm_pc_pc_repository_pc_pc_BasicComponent_m_NoSeffTypeUsedTwice, pcm_pc_pc_repository_pc_pc_BasicComponent_m_RequireSameInterfacesAsImplementationType}

# ImplementationComponentType class attributes and methods

# pcm_pc_pc_usagemodel_pc_pc_Delay class attributes and methods

# pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload class attributes and methods
pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload_population: Property = Property(name="population", type=IntegerType)
pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified: Method = Method(name="PopulationInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified: Method = Method(name="ThinkTimeInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload.attributes={pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload_population}
pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload.methods={pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified, pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified}

# CompleteComponentType class attributes and methods

# ServiceEffectSpecification class attributes and methods

# pcm_pc_pc_repository_pc_pc_ImplementationComponentType class attributes and methods
pcm_pc_pc_repository_pc_pc_ImplementationComponentType_componentType: Property = Property(name="componentType", type=StringType)
pcm_pc_pc_repository_pc_pc_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType: Method = Method(name="providedInterfacesHaveToConformToCompleteType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType: Method = Method(name="ProvidedInterfaceHaveToConformToComponentType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType: Method = Method(name="RequiredInterfacesHaveToConformToCompleteType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_ImplementationComponentType.attributes={pcm_pc_pc_repository_pc_pc_ImplementationComponentType_componentType}
pcm_pc_pc_repository_pc_pc_ImplementationComponentType.methods={pcm_pc_pc_repository_pc_pc_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType, pcm_pc_pc_repository_pc_pc_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType, pcm_pc_pc_repository_pc_pc_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType}

# ResourceSignature class attributes and methods

# pcm_pc_pc_repository_pc_pc_DataType class attributes and methods

# pcm_pc_pc_repository_pc_pc_Repository class attributes and methods
pcm_pc_pc_repository_pc_pc_Repository_repositoryDescription: Property = Property(name="repositoryDescription", type=StringType)
pcm_pc_pc_repository_pc_pc_Repository.attributes={pcm_pc_pc_repository_pc_pc_Repository_repositoryDescription}

# Interface class attributes and methods

# pcm_pc_pc_repository_pc_pc_RepositoryComponent class attributes and methods

# InterfaceProvidingRequiringEntity class attributes and methods

# Repository class attributes and methods

# pcm_pc_pc_repository_pc_pc_ProvidedRole class attributes and methods

# pcm_pc_pc_repository_pc_pc_Parameter class attributes and methods
pcm_pc_pc_repository_pc_pc_Parameter_modifier__Parameter: Property = Property(name="modifier__Parameter", type=StringType)
pcm_pc_pc_repository_pc_pc_Parameter_parameterName: Property = Property(name="parameterName", type=StringType)
pcm_pc_pc_repository_pc_pc_Parameter.attributes={pcm_pc_pc_repository_pc_pc_Parameter_parameterName, pcm_pc_pc_repository_pc_pc_Parameter_modifier__Parameter}

# DataType class attributes and methods

# InfrastructureSignature class attributes and methods

# EventType class attributes and methods

# pcm_pc_pc_repository_pc_pc_RequiredCharacterisation class attributes and methods
pcm_pc_pc_repository_pc_pc_RequiredCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_pc_pc_repository_pc_pc_RequiredCharacterisation.attributes={pcm_pc_pc_repository_pc_pc_RequiredCharacterisation_type}

# Parameter class attributes and methods

# pcm_pc_pc_repository_pc_pc_EventGroup class attributes and methods

# pcm_pc_pc_repository_pc_pc_EventType class attributes and methods

# Signature class attributes and methods

# FailureType class attributes and methods

# pcm_pc_pc_repository_pc_pc_Interface class attributes and methods
pcm_pc_pc_repository_pc_pc_Interface_m_NoProtocolTypeIDUsedTwice: Method = Method(name="NoProtocolTypeIDUsedTwice", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_Interface.methods={pcm_pc_pc_repository_pc_pc_Interface_m_NoProtocolTypeIDUsedTwice}

# Protocol class attributes and methods

# RequiredCharacterisation class attributes and methods

# pcm_pc_pc_repository_pc_pc_RequiredRole class attributes and methods

# pcm_pc_pc_repository_pc_pc_OperationSignature class attributes and methods
pcm_pc_pc_repository_pc_pc_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature: Method = Method(name="ParameterNamesHaveToBeUniqueForASignature", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_OperationSignature.methods={pcm_pc_pc_repository_pc_pc_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature}

# OperationInterface class attributes and methods

# pcm_pc_pc_repository_pc_pc_Signature class attributes and methods

# ExceptionType class attributes and methods

# pcm_pc_pc_repository_pc_pc_ExceptionType class attributes and methods
pcm_pc_pc_repository_pc_pc_ExceptionType_exceptionName: Property = Property(name="exceptionName", type=StringType)
pcm_pc_pc_repository_pc_pc_ExceptionType_exceptionMessage: Property = Property(name="exceptionMessage", type=StringType)
pcm_pc_pc_repository_pc_pc_ExceptionType.attributes={pcm_pc_pc_repository_pc_pc_ExceptionType_exceptionMessage, pcm_pc_pc_repository_pc_pc_ExceptionType_exceptionName}

# pcm_pc_pc_repository_pc_pc_InfrastructureSignature class attributes and methods

# InfrastructureInterface class attributes and methods

# pcm_pc_pc_repository_pc_pc_InfrastructureInterface class attributes and methods

# pcm_pc_pc_repository_pc_pc_InfrastructureRequiredRole class attributes and methods

# pcm_pc_pc_repository_pc_pc_SourceRole class attributes and methods

# pcm_pc_pc_repository_pc_pc_SinkRole class attributes and methods

# pcm_pc_pc_repository_pc_pc_OperationProvidedRole class attributes and methods

# pcm_pc_pc_repository_pc_pc_InfrastructureProvidedRole class attributes and methods

# pcm_pc_pc_repository_pc_pc_OperationInterface class attributes and methods
pcm_pc_pc_repository_pc_pc_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface: Method = Method(name="SignaturesHaveToBeUniqueForAnInterface", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_OperationInterface.methods={pcm_pc_pc_repository_pc_pc_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface}

# pcm_pc_pc_repository_pc_pc_OperationRequiredRole class attributes and methods

# pcm_pc_pc_repository_pc_pc_ProvidesComponentType class attributes and methods
pcm_pc_pc_repository_pc_pc_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_ProvidesComponentType.methods={pcm_pc_pc_repository_pc_pc_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType}

# pcm_pc_pc_repository_pc_pc_CompositeComponent class attributes and methods
pcm_pc_pc_repository_pc_pc_CompositeComponent_m_ProvideSameInterfaces: Method = Method(name="ProvideSameInterfaces", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_CompositeComponent_m_RequireSameInterfaces: Method = Method(name="RequireSameInterfaces", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_CompositeComponent.methods={pcm_pc_pc_repository_pc_pc_CompositeComponent_m_RequireSameInterfaces, pcm_pc_pc_repository_pc_pc_CompositeComponent_m_ProvideSameInterfaces}

# entity_pc_pc_ComposedProvidingRequiringEntity class attributes and methods

# repository_pc_pc_ImplementationComponentType class attributes and methods

# pcm_pc_pc_repository_pc_pc_CompleteComponentType class attributes and methods
pcm_pc_pc_repository_pc_pc_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2: Method = Method(name="providedInterfacesHaveToConformToProvidedType2", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_CompleteComponentType.methods={pcm_pc_pc_repository_pc_pc_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2, pcm_pc_pc_repository_pc_pc_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType}

# ProvidesComponentType class attributes and methods

# InnerDeclaration class attributes and methods

# pcm_pc_pc_repository_pc_pc_InnerDeclaration class attributes and methods

# NamedElement class attributes and methods

# pcm_pc_pc_repository_pc_pc_Role class attributes and methods

# pcm_pc_pc_resourcetype_pc_pc_ResourceSignature class attributes and methods
pcm_pc_pc_resourcetype_pc_pc_ResourceSignature_resourceServiceId: Property = Property(name="resourceServiceId", type=IntegerType)
pcm_pc_pc_resourcetype_pc_pc_ResourceSignature.attributes={pcm_pc_pc_resourcetype_pc_pc_ResourceSignature_resourceServiceId}

# pcm_pc_pc_repository_pc_pc_PrimitiveDataType class attributes and methods
pcm_pc_pc_repository_pc_pc_PrimitiveDataType_type: Property = Property(name="type", type=StringType)
pcm_pc_pc_repository_pc_pc_PrimitiveDataType.attributes={pcm_pc_pc_repository_pc_pc_PrimitiveDataType_type}

# pcm_pc_pc_repository_pc_pc_CollectionDataType class attributes and methods

# repository_pc_pc_DataType class attributes and methods

# pcm_pc_pc_repository_pc_pc_CompositeDataType class attributes and methods

# CompositeDataType class attributes and methods

# pcm_pc_pc_resourcetype_pc_pc_CommunicationLinkResourceType class attributes and methods

# NetworkInducedFailureType class attributes and methods

# pcm_pc_pc_resourcetype_pc_pc_ResourceInterface class attributes and methods

# pcm_pc_pc_protocol_pc_pc_Protocol class attributes and methods
pcm_pc_pc_protocol_pc_pc_Protocol_protocolTypeID: Property = Property(name="protocolTypeID", type=StringType)
pcm_pc_pc_protocol_pc_pc_Protocol.attributes={pcm_pc_pc_protocol_pc_pc_Protocol_protocolTypeID}

# pcm_pc_pc_parameter_pc_pc_VariableUsage class attributes and methods

# pcm_pc_pc_resourcetype_pc_pc_ProcessingResourceType class attributes and methods

# ResourceType class attributes and methods

# HardwareInducedFailureType class attributes and methods

# pcm_pc_pc_resourcetype_pc_pc_ResourceType class attributes and methods

# UnitCarryingElement class attributes and methods

# ResourceRepository class attributes and methods

# pcm_pc_pc_resourcetype_pc_pc_ResourceRepository class attributes and methods

# SchedulingPolicy class attributes and methods

# pcm_pc_pc_resourcetype_pc_pc_SchedulingPolicy class attributes and methods

# pcm_pc_pc_parameter_pc_pc_VariableCharacterisation class attributes and methods
pcm_pc_pc_parameter_pc_pc_VariableCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_pc_pc_parameter_pc_pc_VariableCharacterisation.attributes={pcm_pc_pc_parameter_pc_pc_VariableCharacterisation_type}

# pcm_pc_pc_parameter_pc_pc_CharacterisedVariable class attributes and methods
pcm_pc_pc_parameter_pc_pc_CharacterisedVariable_characterisationType: Property = Property(name="characterisationType", type=StringType)
pcm_pc_pc_parameter_pc_pc_CharacterisedVariable.attributes={pcm_pc_pc_parameter_pc_pc_CharacterisedVariable_characterisationType}

# Variable class attributes and methods

# CallAction class attributes and methods

# SynchronisationPoint class attributes and methods

# CallReturnAction class attributes and methods

# SetVariableAction class attributes and methods

# SpecifiedOutputParameterAbstraction class attributes and methods

# EntryLevelSystemCall class attributes and methods

# parameter_pc_pc_pcm_pc_pc_AbstractNamedReference class attributes and methods

# ProcessingResourceType class attributes and methods

# pcm_pc_pc_reliability_pc_pc_SoftwareInducedFailureType class attributes and methods

# InternalFailureOccurrenceDescription class attributes and methods

# pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription class attributes and methods
pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription.methods={pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription}

# FailureOccurrenceDescription class attributes and methods

# pcm_pc_pc_reliability_pc_pc_FailureOccurrenceDescription class attributes and methods
pcm_pc_pc_reliability_pc_pc_FailureOccurrenceDescription_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_pc_pc_reliability_pc_pc_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange: Method = Method(name="EnsureValidFailureProbabilityRange", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_reliability_pc_pc_FailureOccurrenceDescription.attributes={pcm_pc_pc_reliability_pc_pc_FailureOccurrenceDescription_failureProbability}
pcm_pc_pc_reliability_pc_pc_FailureOccurrenceDescription.methods={pcm_pc_pc_reliability_pc_pc_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange}

# pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType class attributes and methods
pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType: Method = Method(name="HardwareInducedFailureTypeHasProcessingResourceType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType.methods={pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType}

# CommunicationLinkResourceType class attributes and methods

# pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription class attributes and methods
pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription.methods={pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription}

# qos_reliability_pc_pc_SpecifiedReliabilityAnnotation class attributes and methods

# pcm_pc_pc_reliability_pc_pc_ResourceTimeoutFailureType class attributes and methods

# InternalAction class attributes and methods

# SoftwareInducedFailureType class attributes and methods

# pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType class attributes and methods
pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType: Method = Method(name="NetworkInducedFailureTypeHasCommunicationLinkResourceType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType.methods={pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType}

# pcm_pc_pc_seff_pc_pc_AbstractAction class attributes and methods

# ResourceDemandingBehaviour class attributes and methods

# pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour class attributes and methods
pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour_m_ExactlyOneStopAction: Method = Method(name="ExactlyOneStopAction", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour_m_ExactlyOneStartAction: Method = Method(name="ExactlyOneStartAction", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor: Method = Method(name="EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour.methods={pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour_m_ExactlyOneStopAction, pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour_m_ExactlyOneStartAction, pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor}

# pcm_pc_pc_reliability_pc_pc_FailureType class attributes and methods

# pcm_pc_pc_seff_pc_pc_StopAction class attributes and methods
pcm_pc_pc_seff_pc_pc_StopAction_m_StopActionSuccessorMustNotBeDefined: Method = Method(name="StopActionSuccessorMustNotBeDefined", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_StopAction.methods={pcm_pc_pc_seff_pc_pc_StopAction_m_StopActionSuccessorMustNotBeDefined}

# AbstractInternalControlFlowAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction class attributes and methods

# AbstractAction class attributes and methods

# BranchAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_BranchAction class attributes and methods
pcm_pc_pc_seff_pc_pc_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions: Method = Method(name="EitherGuardedBranchesOrProbabilisiticBranchTransitions", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllProbabilisticBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_BranchAction.methods={pcm_pc_pc_seff_pc_pc_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions, pcm_pc_pc_seff_pc_pc_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1}

# pcm_pc_pc_seff_pc_pc_CallAction class attributes and methods

# AbstractLoopAction class attributes and methods

# AbstractBranchTransition class attributes and methods

# pcm_pc_pc_seff_pc_pc_AbstractLoopAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_AbstractBranchTransition class attributes and methods

# pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF class attributes and methods

# seff_pc_pc_ServiceEffectSpecification class attributes and methods

# seff_pc_pc_ResourceDemandingBehaviour class attributes and methods

# ResourceDemandingInternalBehaviour class attributes and methods

# pcm_pc_pc_seff_pc_pc_ResourceDemandingInternalBehaviour class attributes and methods

# ResourceDemandingSEFF class attributes and methods

# pcm_pc_pc_seff_pc_pc_ReleaseAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_LoopAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_StartAction class attributes and methods
pcm_pc_pc_seff_pc_pc_StartAction_m_StartActionPredecessorMustNotBeDefined: Method = Method(name="StartActionPredecessorMustNotBeDefined", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_StartAction.methods={pcm_pc_pc_seff_pc_pc_StartAction_m_StartActionPredecessorMustNotBeDefined}

# pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification class attributes and methods
pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification_seffTypeID: Property = Property(name="seffTypeID", type=StringType)
pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole: Method = Method(name="ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification.attributes={pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification_seffTypeID}
pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification.methods={pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole}

# pcm_pc_pc_seff_pc_pc_ExternalCallAction class attributes and methods
pcm_pc_pc_seff_pc_pc_ExternalCallAction_retryCount: Property = Property(name="retryCount", type=IntegerType)
pcm_pc_pc_seff_pc_pc_ExternalCallAction_m_SignatureBelongsToRole: Method = Method(name="SignatureBelongsToRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer: Method = Method(name="OperationRequiredRoleMustBeReferencedByContainer", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_ExternalCallAction.attributes={pcm_pc_pc_seff_pc_pc_ExternalCallAction_retryCount}
pcm_pc_pc_seff_pc_pc_ExternalCallAction.methods={pcm_pc_pc_seff_pc_pc_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer, pcm_pc_pc_seff_pc_pc_ExternalCallAction_m_SignatureBelongsToRole}

# seff_pc_pc_AbstractAction class attributes and methods

# seff_pc_pc_CallReturnAction class attributes and methods

# seff_reliability_pc_pc_FailureHandlingEntity class attributes and methods

# pcm_pc_pc_seff_pc_pc_ForkAction class attributes and methods

# ForkedBehaviour class attributes and methods

# pcm_pc_pc_seff_pc_pc_ForkedBehaviour class attributes and methods

# ForkAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_SynchronisationPoint class attributes and methods

# pcm_pc_pc_seff_pc_pc_CollectionIteratorAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_GuardedBranchTransition class attributes and methods

# pcm_pc_pc_seff_pc_pc_SetVariableAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_CallReturnAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_ProbabilisticBranchTransition class attributes and methods
pcm_pc_pc_seff_pc_pc_ProbabilisticBranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_pc_pc_seff_pc_pc_ProbabilisticBranchTransition.attributes={pcm_pc_pc_seff_pc_pc_ProbabilisticBranchTransition_branchProbability}

# pcm_pc_pc_seff_pc_pc_AcquireAction class attributes and methods
pcm_pc_pc_seff_pc_pc_AcquireAction_timeout: Property = Property(name="timeout", type=BooleanType)
pcm_pc_pc_seff_pc_pc_AcquireAction_timeoutValue: Property = Property(name="timeoutValue", type=FloatType)
pcm_pc_pc_seff_pc_pc_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative: Method = Method(name="TimeoutValueOfAcquireActionMustNotBeNegative", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_AcquireAction.attributes={pcm_pc_pc_seff_pc_pc_AcquireAction_timeout, pcm_pc_pc_seff_pc_pc_AcquireAction_timeoutValue}
pcm_pc_pc_seff_pc_pc_AcquireAction.methods={pcm_pc_pc_seff_pc_pc_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative}

# pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall class attributes and methods
pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole: Method = Method(name="SignatureMustBelongToUsedRequiredRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent: Method = Method(name="ReferencedRequiredRoleMustBeRequiredByComponent", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall.methods={pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole, pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction, pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent}

# pcm_pc_pc_seff_pc_pc_InternalCallAction class attributes and methods

# seff_pc_pc_CallAction class attributes and methods

# seff_pc_pc_AbstractInternalControlFlowAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_EmitEventAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_InternalAction class attributes and methods
pcm_pc_pc_seff_pc_pc_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfInternalActionFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_InternalAction.methods={pcm_pc_pc_seff_pc_pc_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed, pcm_pc_pc_seff_pc_pc_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1}

# pcm_pc_pc_seff_performance_pc_pc_ResourceCall class attributes and methods
pcm_pc_pc_seff_performance_pc_pc_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole: Method = Method(name="ResourceSignatureBelongsToResourceRequiredRole", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_seff_performance_pc_pc_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent: Method = Method(name="ResourceRequiredRoleMustBeReferencedByComponent", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_seff_performance_pc_pc_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_seff_performance_pc_pc_ResourceCall.methods={pcm_pc_pc_seff_performance_pc_pc_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole, pcm_pc_pc_seff_performance_pc_pc_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent, pcm_pc_pc_seff_performance_pc_pc_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction}

# pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour class attributes and methods
pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor: Method = Method(name="RecoveryActionBehaviourHasOnlyOnePredecessor", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself: Method = Method(name="RecoveryActionBehaviourIsNotSuccessorOfItself", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes: Method = Method(name="SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour.methods={pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes, pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor, pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself}

# seff_reliability_pc_pc_RecoveryActionBehaviour class attributes and methods

# pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand class attributes and methods
pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand.methods={pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction}

# pcm_pc_pc_qosannotations_pc_pc_SpecifiedQoSAnnotation class attributes and methods

# QoSAnnotations class attributes and methods

# pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations class attributes and methods
pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed: Method = Method(name="MultipleReliabilityAnnotationsPerExternalCallNotAllowed", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations.methods={pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed}

# seff_reliability_pc_pc_RecoveryAction class attributes and methods

# pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction class attributes and methods
pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet: Method = Method(name="PrimaryBehaviourOfRecoveryActionMustBeSet", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction.methods={pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet}

# pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity class attributes and methods

# pcm_pc_pc_qos_performance_pc_pc_SpecifiedExecutionTime class attributes and methods

# pcm_pc_pc_qos_performance_pc_pc_ComponentSpecifiedExecutionTime class attributes and methods

# pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation class attributes and methods
pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem: Method = Method(name="SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation.methods={pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed, pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1, pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem}

# System class attributes and methods

# SpecifiedQoSAnnotation class attributes and methods

# pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction class attributes and methods

# pcm_pc_pc_qos_performance_pc_pc_SystemSpecifiedExecutionTime class attributes and methods
pcm_pc_pc_qos_performance_pc_pc_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem: Method = Method(name="SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_qos_performance_pc_pc_SystemSpecifiedExecutionTime.methods={pcm_pc_pc_qos_performance_pc_pc_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem}

# SpecifiedExecutionTime class attributes and methods

# ExternalFailureOccurrenceDescription class attributes and methods

# pcm_pc_pc_system_pc_pc_System class attributes and methods
pcm_pc_pc_system_pc_pc_System_m_SystemMustHaveAtLeastOneProvidedRole: Method = Method(name="SystemMustHaveAtLeastOneProvidedRole", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_system_pc_pc_System.methods={pcm_pc_pc_system_pc_pc_System_m_SystemMustHaveAtLeastOneProvidedRole}

# pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification class attributes and methods
pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification_MTTR: Property = Property(name="MTTR", type=FloatType)
pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification_MTTF: Property = Property(name="MTTF", type=FloatType)
pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification_requiredByContainer: Property = Property(name="requiredByContainer", type=BooleanType)
pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification_numberOfReplicas: Property = Property(name="numberOfReplicas", type=IntegerType)
pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification.attributes={pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification_requiredByContainer, pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification_MTTF, pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification_MTTR, pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification_numberOfReplicas}

# pcm_pc_pc_resourceenvironment_pc_pc_ResourceEnvironment class attributes and methods

# LinkingResource class attributes and methods

# ResourceContainer class attributes and methods

# pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource class attributes and methods

# ResourceEnvironment class attributes and methods

# pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer class attributes and methods

# pcm_pc_pc_allocation_pc_pc_AllocationContext class attributes and methods
pcm_pc_pc_allocation_pc_pc_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred: Method = Method(name="OneAssemblyContextOrOneEventChannelShouldBeReferred", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_pc_pc_allocation_pc_pc_AllocationContext.methods={pcm_pc_pc_allocation_pc_pc_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred}

# Allocation class attributes and methods

# pcm_pc_pc_allocation_pc_pc_Allocation class attributes and methods
pcm_pc_pc_allocation_pc_pc_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce: Method = Method(name="EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_allocation_pc_pc_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource: Method = Method(name="CommunicatingServersHaveToBeConnectedByLinkingResource", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_pc_pc_allocation_pc_pc_Allocation.methods={pcm_pc_pc_allocation_pc_pc_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce, pcm_pc_pc_allocation_pc_pc_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource}

# pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification class attributes and methods
pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification.attributes={pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification_failureProbability}

# pcm_pc_pc_subsystem_pc_pc_SubSystem class attributes and methods

# repository_pc_pc_RepositoryComponent class attributes and methods

# pcm_pc_pc_completions_pc_pc_Completion class attributes and methods

# pcm_pc_pc_completions_pc_pc_CompletionRepository class attributes and methods

# Completion class attributes and methods

# pcm_pc_pc_completions_pc_pc_DelegatingExternalCallAction class attributes and methods

# ExternalCallAction class attributes and methods

# pcm_pc_pc_completions_pc_pc_NetworkDemandParametricResourceDemand class attributes and methods

# ParametricResourceDemand class attributes and methods

# AllocationContext class attributes and methods

# Relationships
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="pcm_pc_pc_EObject", type=pcm_pc_pc_PointcutPointcut, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_PointcutPointcut", type=pcm_pc_pc_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceCall__PCMRandomVariable7: BinaryAssociation = BinaryAssociation(
    name="resourceCall__PCMRandomVariable7",
    ends={
        Property(name="seff_pc_pc9", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_pc_pc8", type=seff_performance_pc_pc_ResourceCall, multiplicity=Multiplicity(0, 1))
    }
)
parametricResourceDemand_PCMRandomVariable10: BinaryAssociation = BinaryAssociation(
    name="parametricResourceDemand_PCMRandomVariable10",
    ends={
        Property(name="seff_pc_pc12", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_pc_pc11", type=seff_performance_pc_pc_ParametricResourceDemand, multiplicity=Multiplicity(0, 1))
    }
)
loopAction_PCMRandomVariable13: BinaryAssociation = BinaryAssociation(
    name="loopAction_PCMRandomVariable13",
    ends={
        Property(name="seff_pc_pc14", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="LoopAction", type=LoopAction, multiplicity=Multiplicity(0, 1))
    }
)
guardedBranchTransition_PCMRandomVariable15: BinaryAssociation = BinaryAssociation(
    name="guardedBranchTransition_PCMRandomVariable15",
    ends={
        Property(name="seff_pc_pc16", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="GuardedBranchTransition", type=GuardedBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
specifiedExecutionTime_PCMRandomVariable17: BinaryAssociation = BinaryAssociation(
    name="specifiedExecutionTime_PCMRandomVariable17",
    ends={
        Property(name="qosannotations_pc_pc", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="qos_performance_pc_pc", type=qos_performance_pc_pc_SpecifiedExecutionTime, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSinkConnector__FilterCondition18: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__FilterCondition18",
    ends={
        Property(name="core_pc_pc", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_pc", type=composition_pc_pc_EventChannelSinkConnector, multiplicity=Multiplicity(0, 1))
    }
)
assemblyEventConnector__FilterCondition19: BinaryAssociation = BinaryAssociation(
    name="assemblyEventConnector__FilterCondition19",
    ends={
        Property(name="core_pc_pc21", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_pc20", type=composition_pc_pc_AssemblyEventConnector, multiplicity=Multiplicity(0, 1))
    }
)
children1: BinaryAssociation = BinaryAssociation(
    name="children1",
    ends={
        Property(name="pcm_pc_pc_EObject2", type=pcm_pc_pc_Pointcut, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_Pointcut", type=pcm_pc_pc_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
closedWorkload_PCMRandomVariable3: BinaryAssociation = BinaryAssociation(
    name="closedWorkload_PCMRandomVariable3",
    ends={
        Property(name="usagemodel_pc_pc", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ClosedWorkload", type=ClosedWorkload, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_capacity_PCMRandomVariable4: BinaryAssociation = BinaryAssociation(
    name="passiveResource_capacity_PCMRandomVariable4",
    ends={
        Property(name="repository_pc_pc", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
variableCharacterisation_Specification5: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_Specification5",
    ends={
        Property(name="parameter_pc_pc", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableCharacterisation", type=VariableCharacterisation, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureCall__PCMRandomVariable6: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__PCMRandomVariable6",
    ends={
        Property(name="seff_pc_pc", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_pc_pc", type=seff_performance_pc_pc_InfrastructureCall, multiplicity=Multiplicity(0, 1))
    }
)
providedRoles_InterfaceProvidingEntity37: BinaryAssociation = BinaryAssociation(
    name="providedRoles_InterfaceProvidingEntity37",
    ends={
        Property(name="repository_pc_pc38", type=pcm_pc_pc_entity_pc_pc_InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="ProvidedRole", type=ProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredRoles_InterfaceRequiringEntity39: BinaryAssociation = BinaryAssociation(
    name="requiredRoles_InterfaceRequiringEntity39",
    ends={
        Property(name="repository_pc_pc40", type=pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="RequiredRole", type=RequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredRoles__ResourceInterfaceRequiringEntity41: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRoles__ResourceInterfaceRequiringEntity41",
    ends={
        Property(name="core_pc_pc43", type=pcm_pc_pc_entity_pc_pc_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_pc_pc42", type=entity_pc_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loop_LoopIteration22: BinaryAssociation = BinaryAssociation(
    name="loop_LoopIteration22",
    ends={
        Property(name="usagemodel_pc_pc23", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Loop", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
openWorkload_PCMRandomVariable24: BinaryAssociation = BinaryAssociation(
    name="openWorkload_PCMRandomVariable24",
    ends={
        Property(name="usagemodel_pc_pc25", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="OpenWorkload", type=OpenWorkload, multiplicity=Multiplicity(0, 1))
    }
)
delay_TimeSpecification26: BinaryAssociation = BinaryAssociation(
    name="delay_TimeSpecification26",
    ends={
        Property(name="usagemodel_pc_pc27", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Delay", type=Delay, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecifcation_throughput_PCMRandomVariable28: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifcation_throughput_PCMRandomVariable28",
    ends={
        Property(name="resourceenvironment_pc_pc", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceSpecification_processingRate_PCMRandomVariable29: BinaryAssociation = BinaryAssociation(
    name="processingResourceSpecification_processingRate_PCMRandomVariable29",
    ends={
        Property(name="resourceenvironment_pc_pc30", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcessingResourceSpecification", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecification_latency_PCMRandomVariable31: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecification_latency_PCMRandomVariable31",
    ends={
        Property(name="resourceenvironment_pc_pc33", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceSpecification32", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaceProvidingEntity__ResourceProvidedRole34: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceProvidingEntity__ResourceProvidedRole34",
    ends={
        Property(name="core_pc_pc35", type=pcm_pc_pc_entity_pc_pc_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_pc_pc", type=entity_pc_pc_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
providedResourceInterface__ResourceProvidedRole36: BinaryAssociation = BinaryAssociation(
    name="providedResourceInterface__ResourceProvidedRole36",
    ends={
        Property(name="ResourceInterface", type=pcm_pc_pc_entity_pc_pc_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_entity_pc_pc_ResourceProvidedRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure__Connector52: BinaryAssociation = BinaryAssociation(
    name="parentStructure__Connector52",
    ends={
        Property(name="core_pc_pc54", type=pcm_pc_pc_composition_pc_pc_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_pc53", type=composition_pc_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
requiredResourceInterface__ResourceRequiredRole44: BinaryAssociation = BinaryAssociation(
    name="requiredResourceInterface__ResourceRequiredRole44",
    ends={
        Property(name="ResourceInterface45", type=pcm_pc_pc_entity_pc_pc_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_entity_pc_pc_ResourceRequiredRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaceRequiringEntity__ResourceRequiredRole46: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceRequiringEntity__ResourceRequiredRole46",
    ends={
        Property(name="core_pc_pc48", type=pcm_pc_pc_entity_pc_pc_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_pc_pc47", type=entity_pc_pc_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
resourceProvidedRoles__ResourceInterfaceProvidingEntity49: BinaryAssociation = BinaryAssociation(
    name="resourceProvidedRoles__ResourceInterfaceProvidingEntity49",
    ends={
        Property(name="core_pc_pc51", type=pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_pc_pc50", type=entity_pc_pc_ResourceProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentStructure__EventChannel81: BinaryAssociation = BinaryAssociation(
    name="parentStructure__EventChannel81",
    ends={
        Property(name="core_pc_pc83", type=pcm_pc_pc_composition_pc_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_pc82", type=composition_pc_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EventChannelSourceRole84: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EventChannelSourceRole84",
    ends={
        Property(name="SourceRole", type=pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__EventChannelSourceConnector85: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSourceConnector85",
    ends={
        Property(name="composition_pc_pc_AssemblyContext", type=pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector86", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSourceConnector87: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSourceConnector87",
    ends={
        Property(name="core_pc_pc89", type=pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_pc88", type=composition_pc_pc_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__EventChannelSinkConnector90: BinaryAssociation = BinaryAssociation(
    name="sinkRole__EventChannelSinkConnector90",
    ends={
        Property(name="SinkRole", type=pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__EventChannelSinkConnector91: BinaryAssociation = BinaryAssociation(
    name="filterCondition__EventChannelSinkConnector91",
    ends={
        Property(name="core_pc_pc92", type=pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext__EventChannelSinkConnector93: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSinkConnector93",
    ends={
        Property(name="composition_pc_pc_AssemblyContext95", type=pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector94", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSinkConnector96: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSinkConnector96",
    ends={
        Property(name="core_pc_pc98", type=pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_pc97", type=composition_pc_pc_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContexts__ComposedStructure55: BinaryAssociation = BinaryAssociation(
    name="assemblyContexts__ComposedStructure55",
    ends={
        Property(name="core_pc_pc57", type=pcm_pc_pc_composition_pc_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_pc56", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredDelegationConnectors_ComposedStructure58: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredDelegationConnectors_ComposedStructure58",
    ends={
        Property(name="core_pc_pc60", type=pcm_pc_pc_composition_pc_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_pc59", type=composition_pc_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventChannel__ComposedStructure61: BinaryAssociation = BinaryAssociation(
    name="eventChannel__ComposedStructure61",
    ends={
        Property(name="core_pc_pc63", type=pcm_pc_pc_composition_pc_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_pc62", type=composition_pc_pc_EventChannel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectors__ComposedStructure64: BinaryAssociation = BinaryAssociation(
    name="connectors__ComposedStructure64",
    ends={
        Property(name="core_pc_pc66", type=pcm_pc_pc_composition_pc_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_pc65", type=composition_pc_pc_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerResourceRequiredRole_ResourceRequiredDelegationConnector67: BinaryAssociation = BinaryAssociation(
    name="innerResourceRequiredRole_ResourceRequiredDelegationConnector67",
    ends={
        Property(name="entity_pc_pc_ResourceRequiredRole", type=pcm_pc_pc_composition_pc_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_ResourceRequiredDelegationConnector", type=entity_pc_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerResourceRequiredRole_ResourceRequiredDelegationConnector68: BinaryAssociation = BinaryAssociation(
    name="outerResourceRequiredRole_ResourceRequiredDelegationConnector68",
    ends={
        Property(name="entity_pc_pc_ResourceRequiredRole70", type=pcm_pc_pc_composition_pc_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_ResourceRequiredDelegationConnector69", type=entity_pc_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure_ResourceRequiredDelegationConnector71: BinaryAssociation = BinaryAssociation(
    name="parentStructure_ResourceRequiredDelegationConnector71",
    ends={
        Property(name="core_pc_pc73", type=pcm_pc_pc_composition_pc_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_pc72", type=composition_pc_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__EventChannel74: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventChannel74",
    ends={
        Property(name="EventGroup", type=pcm_pc_pc_composition_pc_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_EventChannel", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSourceConnector__EventChannel75: BinaryAssociation = BinaryAssociation(
    name="eventChannelSourceConnector__EventChannel75",
    ends={
        Property(name="core_pc_pc77", type=pcm_pc_pc_composition_pc_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_pc76", type=composition_pc_pc_EventChannelSourceConnector, multiplicity=Multiplicity(0, 9999))
    }
)
eventChannelSinkConnector__EventChannel78: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__EventChannel78",
    ends={
        Property(name="core_pc_pc80", type=pcm_pc_pc_composition_pc_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_pc79", type=composition_pc_pc_EventChannelSinkConnector, multiplicity=Multiplicity(0, 9999))
    }
)
innerRequiredRole_RequiredDelegationConnector106: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole_RequiredDelegationConnector106",
    ends={
        Property(name="OperationRequiredRole", type=pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole_RequiredDelegationConnector107: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole_RequiredDelegationConnector107",
    ends={
        Property(name="OperationRequiredRole109", type=pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector108", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole_ProvidedDelegationConnector99: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole_ProvidedDelegationConnector99",
    ends={
        Property(name="OperationProvidedRole", type=pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole_ProvidedDelegationConnector100: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole_ProvidedDelegationConnector100",
    ends={
        Property(name="OperationProvidedRole102", type=pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector101", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_ProvidedDelegationConnector103: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ProvidedDelegationConnector103",
    ends={
        Property(name="composition_pc_pc_AssemblyContext105", type=pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector104", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_RequiredDelegationConnector110: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_RequiredDelegationConnector110",
    ends={
        Property(name="composition_pc_pc_AssemblyContext112", type=pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector111", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole_AssemblyConnector121: BinaryAssociation = BinaryAssociation(
    name="requiredRole_AssemblyConnector121",
    ends={
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyConnector122", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1)),
        Property(name="OperationRequiredRole123", type=pcm_pc_pc_composition_pc_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1))
    }
)
sinkRole__AssemblyEventConnector124: BinaryAssociation = BinaryAssociation(
    name="sinkRole__AssemblyEventConnector124",
    ends={
        Property(name="SinkRole125", type=pcm_pc_pc_composition_pc_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyEventConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__AssemblyEventConnector126: BinaryAssociation = BinaryAssociation(
    name="sourceRole__AssemblyEventConnector126",
    ends={
        Property(name="SourceRole128", type=pcm_pc_pc_composition_pc_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyEventConnector127", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkAssemblyContext__AssemblyEventConnector129: BinaryAssociation = BinaryAssociation(
    name="sinkAssemblyContext__AssemblyEventConnector129",
    ends={
        Property(name="composition_pc_pc_AssemblyContext131", type=pcm_pc_pc_composition_pc_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyEventConnector130", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
sourceAssemblyContext__AssemblyEventConnector132: BinaryAssociation = BinaryAssociation(
    name="sourceAssemblyContext__AssemblyEventConnector132",
    ends={
        Property(name="composition_pc_pc_AssemblyContext134", type=pcm_pc_pc_composition_pc_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyEventConnector133", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__AssemblyEventConnector135: BinaryAssociation = BinaryAssociation(
    name="filterCondition__AssemblyEventConnector135",
    ends={
        Property(name="core_pc_pc137", type=pcm_pc_pc_composition_pc_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable136", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
innerSourceRole__SourceRole138: BinaryAssociation = BinaryAssociation(
    name="innerSourceRole__SourceRole138",
    ends={
        Property(name="SourceRole139", type=pcm_pc_pc_composition_pc_pc_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_SourceDelegationConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSourceRole__SourceRole140: BinaryAssociation = BinaryAssociation(
    name="outerSourceRole__SourceRole140",
    ends={
        Property(name="SourceRole142", type=pcm_pc_pc_composition_pc_pc_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_SourceDelegationConnector141", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext_AssemblyConnector113: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext_AssemblyConnector113",
    ends={
        Property(name="composition_pc_pc_AssemblyContext114", type=pcm_pc_pc_composition_pc_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyConnector", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext_AssemblyConnector115: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext_AssemblyConnector115",
    ends={
        Property(name="composition_pc_pc_AssemblyContext117", type=pcm_pc_pc_composition_pc_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyConnector116", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providedRole_AssemblyConnector118: BinaryAssociation = BinaryAssociation(
    name="providedRole_AssemblyConnector118",
    ends={
        Property(name="OperationProvidedRole120", type=pcm_pc_pc_composition_pc_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyConnector119", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__ProvidedInfrastructureDelegationConnector168: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__ProvidedInfrastructureDelegationConnector168",
    ends={
        Property(name="composition_pc_pc_AssemblyContext170", type=pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector169", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole__RequiredInfrastructureDelegationConnector171: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredInfrastructureDelegationConnector171",
    ends={
        Property(name="InfrastructureRequiredRole172", type=pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredInfrastructureDelegationConnector173: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredInfrastructureDelegationConnector173",
    ends={
        Property(name="InfrastructureRequiredRole175", type=pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector174", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredInfrastructureDelegationConnector176: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredInfrastructureDelegationConnector176",
    ends={
        Property(name="composition_pc_pc_AssemblyContext178", type=pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector177", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredResourceDelegationConnector179: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredResourceDelegationConnector179",
    ends={
        Property(name="composition_pc_pc_AssemblyContext180", type=pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole__RequiredResourceDelegationConnector181: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredResourceDelegationConnector181",
    ends={
        Property(name="entity_pc_pc_ResourceRequiredRole183", type=pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector182", type=entity_pc_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredResourceDelegationConnector184: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredResourceDelegationConnector184",
    ends={
        Property(name="entity_pc_pc_ResourceRequiredRole186", type=pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector185", type=entity_pc_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SourceDelegationConnector143: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SourceDelegationConnector143",
    ends={
        Property(name="composition_pc_pc_AssemblyContext145", type=pcm_pc_pc_composition_pc_pc_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_SourceDelegationConnector144", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SinkDelegationConnector146: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SinkDelegationConnector146",
    ends={
        Property(name="composition_pc_pc_AssemblyContext147", type=pcm_pc_pc_composition_pc_pc_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_SinkDelegationConnector", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerSinkRole__SinkRole148: BinaryAssociation = BinaryAssociation(
    name="innerSinkRole__SinkRole148",
    ends={
        Property(name="SinkRole150", type=pcm_pc_pc_composition_pc_pc_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_SinkDelegationConnector149", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSinkRole__SinkRole151: BinaryAssociation = BinaryAssociation(
    name="outerSinkRole__SinkRole151",
    ends={
        Property(name="SinkRole153", type=pcm_pc_pc_composition_pc_pc_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_SinkDelegationConnector152", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
providedRole__AssemblyInfrastructureConnector154: BinaryAssociation = BinaryAssociation(
    name="providedRole__AssemblyInfrastructureConnector154",
    ends={
        Property(name="InfrastructureProvidedRole", type=pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__AssemblyInfrastructureConnector155: BinaryAssociation = BinaryAssociation(
    name="requiredRole__AssemblyInfrastructureConnector155",
    ends={
        Property(name="InfrastructureRequiredRole", type=pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector156", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext__AssemblyInfrastructureConnector157: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext__AssemblyInfrastructureConnector157",
    ends={
        Property(name="composition_pc_pc_AssemblyContext159", type=pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector158", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext__AssemblyInfrastructureConnector160: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext__AssemblyInfrastructureConnector160",
    ends={
        Property(name="composition_pc_pc_AssemblyContext162", type=pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector161", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole__ProvidedInfrastructureDelegationConnector163: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole__ProvidedInfrastructureDelegationConnector163",
    ends={
        Property(name="InfrastructureProvidedRole164", type=pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole__ProvidedInfrastructureDelegationConnector165: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole__ProvidedInfrastructureDelegationConnector165",
    ends={
        Property(name="InfrastructureProvidedRole167", type=pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector166", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
userDataParameterUsages_UserData206: BinaryAssociation = BinaryAssociation(
    name="userDataParameterUsages_UserData206",
    ends={
        Property(name="parameter_pc_pc208", type=pcm_pc_pc_usagemodel_pc_pc_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage207", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_UsageModel209: BinaryAssociation = BinaryAssociation(
    name="usageScenario_UsageModel209",
    ends={
        Property(name="usagemodel_pc_pc211", type=pcm_pc_pc_usagemodel_pc_pc_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageScenario210", type=UsageScenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_UsageModel212: BinaryAssociation = BinaryAssociation(
    name="userData_UsageModel212",
    ends={
        Property(name="usagemodel_pc_pc213", type=pcm_pc_pc_usagemodel_pc_pc_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="UserData", type=UserData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentStructure__AssemblyContext187: BinaryAssociation = BinaryAssociation(
    name="parentStructure__AssemblyContext187",
    ends={
        Property(name="core_pc_pc189", type=pcm_pc_pc_composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_pc188", type=composition_pc_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
encapsulatedComponent__AssemblyContext190: BinaryAssociation = BinaryAssociation(
    name="encapsulatedComponent__AssemblyContext190",
    ends={
        Property(name="RepositoryComponent", type=pcm_pc_pc_composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyContext", type=RepositoryComponent, multiplicity=Multiplicity(0, 1))
    }
)
configParameterUsages__AssemblyContext191: BinaryAssociation = BinaryAssociation(
    name="configParameterUsages__AssemblyContext191",
    ends={
        Property(name="parameter_pc_pc192", type=pcm_pc_pc_composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_Workload193: BinaryAssociation = BinaryAssociation(
    name="usageScenario_Workload193",
    ends={
        Property(name="usagemodel_pc_pc194", type=pcm_pc_pc_usagemodel_pc_pc_Workload, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UsageScenario195: BinaryAssociation = BinaryAssociation(
    name="usageModel_UsageScenario195",
    ends={
        Property(name="usagemodel_pc_pc196", type=pcm_pc_pc_usagemodel_pc_pc_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageModel", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_UsageScenario197: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_UsageScenario197",
    ends={
        Property(name="usagemodel_pc_pc198", type=pcm_pc_pc_usagemodel_pc_pc_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
workload_UsageScenario199: BinaryAssociation = BinaryAssociation(
    name="workload_UsageScenario199",
    ends={
        Property(name="usagemodel_pc_pc200", type=pcm_pc_pc_usagemodel_pc_pc_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="Workload", type=Workload, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext_userData201: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_userData201",
    ends={
        Property(name="composition_pc_pc_AssemblyContext202", type=pcm_pc_pc_usagemodel_pc_pc_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_usagemodel_pc_pc_UserData", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UserData203: BinaryAssociation = BinaryAssociation(
    name="usageModel_UserData203",
    ends={
        Property(name="usagemodel_pc_pc205", type=pcm_pc_pc_usagemodel_pc_pc_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageModel204", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
usageScenario_SenarioBehaviour232: BinaryAssociation = BinaryAssociation(
    name="usageScenario_SenarioBehaviour232",
    ends={
        Property(name="usagemodel_pc_pc234", type=pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="UsageScenario233", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
branchTransition_ScenarioBehaviour235: BinaryAssociation = BinaryAssociation(
    name="branchTransition_ScenarioBehaviour235",
    ends={
        Property(name="usagemodel_pc_pc236", type=pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="BranchTransition", type=BranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
providedRole_EntryLevelSystemCall214: BinaryAssociation = BinaryAssociation(
    name="providedRole_EntryLevelSystemCall214",
    ends={
        Property(name="OperationProvidedRole215", type=pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__EntryLevelSystemCall216: BinaryAssociation = BinaryAssociation(
    name="operationSignature__EntryLevelSystemCall216",
    ends={
        Property(name="OperationSignature", type=pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall217", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
outputParameterUsages_EntryLevelSystemCall218: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsages_EntryLevelSystemCall218",
    ends={
        Property(name="parameter_pc_pc220", type=pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage219", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputParameterUsages_EntryLevelSystemCall221: BinaryAssociation = BinaryAssociation(
    name="inputParameterUsages_EntryLevelSystemCall221",
    ends={
        Property(name="parameter_pc_pc223", type=pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage222", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
successor224: BinaryAssociation = BinaryAssociation(
    name="successor224",
    ends={
        Property(name="usagemodel_pc_pc225", type=pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
predecessor226: BinaryAssociation = BinaryAssociation(
    name="predecessor226",
    ends={
        Property(name="usagemodel_pc_pc228", type=pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction227", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_AbstractUserAction229: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_AbstractUserAction229",
    ends={
        Property(name="usagemodel_pc_pc231", type=pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour230", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
loop_ScenarioBehaviour237: BinaryAssociation = BinaryAssociation(
    name="loop_ScenarioBehaviour237",
    ends={
        Property(name="usagemodel_pc_pc239", type=pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="Loop238", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
actions_ScenarioBehaviour240: BinaryAssociation = BinaryAssociation(
    name="actions_ScenarioBehaviour240",
    ends={
        Property(name="usagemodel_pc_pc242", type=pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction241", type=AbstractUserAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branch_BranchTransition243: BinaryAssociation = BinaryAssociation(
    name="branch_BranchTransition243",
    ends={
        Property(name="usagemodel_pc_pc244", type=pcm_pc_pc_usagemodel_pc_pc_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="Branch", type=Branch, multiplicity=Multiplicity(0, 1))
    }
)
branchedBehaviour_BranchTransition245: BinaryAssociation = BinaryAssociation(
    name="branchedBehaviour_BranchTransition245",
    ends={
        Property(name="usagemodel_pc_pc247", type=pcm_pc_pc_usagemodel_pc_pc_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour246", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchTransitions_Branch248: BinaryAssociation = BinaryAssociation(
    name="branchTransitions_Branch248",
    ends={
        Property(name="usagemodel_pc_pc250", type=pcm_pc_pc_usagemodel_pc_pc_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="BranchTransition249", type=BranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopIteration_Loop251: BinaryAssociation = BinaryAssociation(
    name="loopIteration_Loop251",
    ends={
        Property(name="core_pc_pc253", type=pcm_pc_pc_usagemodel_pc_pc_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable252", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyBehaviour_Loop254: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop254",
    ends={
        Property(name="usagemodel_pc_pc256", type=pcm_pc_pc_usagemodel_pc_pc_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="ScenarioBehaviour255", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thinkTime_ClosedWorkload263: BinaryAssociation = BinaryAssociation(
    name="thinkTime_ClosedWorkload263",
    ends={
        Property(name="core_pc_pc265", type=pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable264", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capacity_PassiveResource266: BinaryAssociation = BinaryAssociation(
    name="capacity_PassiveResource266",
    ends={
        Property(name="core_pc_pc268", type=pcm_pc_pc_repository_pc_pc_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable267", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicComponent_PassiveResource269: BinaryAssociation = BinaryAssociation(
    name="basicComponent_PassiveResource269",
    ends={
        Property(name="repository_pc_pc270", type=pcm_pc_pc_repository_pc_pc_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="BasicComponent", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
resourceTimeoutFailureType__PassiveResource271: BinaryAssociation = BinaryAssociation(
    name="resourceTimeoutFailureType__PassiveResource271",
    ends={
        Property(name="reliability_pc_pc", type=pcm_pc_pc_repository_pc_pc_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceTimeoutFailureType", type=ResourceTimeoutFailureType, multiplicity=Multiplicity(0, 1))
    }
)
interArrivalTime_OpenWorkload257: BinaryAssociation = BinaryAssociation(
    name="interArrivalTime_OpenWorkload257",
    ends={
        Property(name="core_pc_pc259", type=pcm_pc_pc_usagemodel_pc_pc_OpenWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable258", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeSpecification_Delay260: BinaryAssociation = BinaryAssociation(
    name="timeSpecification_Delay260",
    ends={
        Property(name="core_pc_pc262", type=pcm_pc_pc_usagemodel_pc_pc_Delay, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable261", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parentCompleteComponentTypes277: BinaryAssociation = BinaryAssociation(
    name="parentCompleteComponentTypes277",
    ends={
        Property(name="CompleteComponentType", type=pcm_pc_pc_repository_pc_pc_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_ImplementationComponentType", type=CompleteComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
serviceEffectSpecifications__BasicComponent272: BinaryAssociation = BinaryAssociation(
    name="serviceEffectSpecifications__BasicComponent272",
    ends={
        Property(name="seff_pc_pc273", type=pcm_pc_pc_repository_pc_pc_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ServiceEffectSpecification", type=ServiceEffectSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveResource_BasicComponent274: BinaryAssociation = BinaryAssociation(
    name="passiveResource_BasicComponent274",
    ends={
        Property(name="repository_pc_pc276", type=pcm_pc_pc_repository_pc_pc_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="PassiveResource275", type=PassiveResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceSignature__Parameter294: BinaryAssociation = BinaryAssociation(
    name="resourceSignature__Parameter294",
    ends={
        Property(name="resourcetype_pc_pc", type=pcm_pc_pc_repository_pc_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceSignature", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
repository__DataType295: BinaryAssociation = BinaryAssociation(
    name="repository__DataType295",
    ends={
        Property(name="repository_pc_pc297", type=pcm_pc_pc_repository_pc_pc_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository296", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
components__Repository298: BinaryAssociation = BinaryAssociation(
    name="components__Repository298",
    ends={
        Property(name="repository_pc_pc300", type=pcm_pc_pc_repository_pc_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="RepositoryComponent299", type=RepositoryComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaces__Repository301: BinaryAssociation = BinaryAssociation(
    name="interfaces__Repository301",
    ends={
        Property(name="repository_pc_pc302", type=pcm_pc_pc_repository_pc_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="Interface", type=Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentParameterUsage_ImplementationComponentType278: BinaryAssociation = BinaryAssociation(
    name="componentParameterUsage_ImplementationComponentType278",
    ends={
        Property(name="VariableUsage280", type=pcm_pc_pc_repository_pc_pc_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_ImplementationComponentType279", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository__RepositoryComponent281: BinaryAssociation = BinaryAssociation(
    name="repository__RepositoryComponent281",
    ends={
        Property(name="repository_pc_pc282", type=pcm_pc_pc_repository_pc_pc_RepositoryComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
providingEntity_ProvidedRole283: BinaryAssociation = BinaryAssociation(
    name="providingEntity_ProvidedRole283",
    ends={
        Property(name="core_pc_pc285", type=pcm_pc_pc_repository_pc_pc_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_pc_pc284", type=entity_pc_pc_InterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
dataType__Parameter286: BinaryAssociation = BinaryAssociation(
    name="dataType__Parameter286",
    ends={
        Property(name="DataType", type=pcm_pc_pc_repository_pc_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_Parameter", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureSignature__Parameter287: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignature__Parameter287",
    ends={
        Property(name="repository_pc_pc288", type=pcm_pc_pc_repository_pc_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="InfrastructureSignature", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__Parameter289: BinaryAssociation = BinaryAssociation(
    name="operationSignature__Parameter289",
    ends={
        Property(name="repository_pc_pc291", type=pcm_pc_pc_repository_pc_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationSignature290", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
eventType__Parameter292: BinaryAssociation = BinaryAssociation(
    name="eventType__Parameter292",
    ends={
        Property(name="repository_pc_pc293", type=pcm_pc_pc_repository_pc_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="EventType", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
repository__Interface314: BinaryAssociation = BinaryAssociation(
    name="repository__Interface314",
    ends={
        Property(name="Repository315", type=Repository, multiplicity=Multiplicity(0, 1)),
        Property(name="repository_pc_pc316", type=pcm_pc_pc_repository_pc_pc_Interface, multiplicity=Multiplicity(1, 1))
    }
)
parameter317: BinaryAssociation = BinaryAssociation(
    name="parameter317",
    ends={
        Property(name="Parameter", type=pcm_pc_pc_repository_pc_pc_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_RequiredCharacterisation", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
interface_RequiredCharacterisation318: BinaryAssociation = BinaryAssociation(
    name="interface_RequiredCharacterisation318",
    ends={
        Property(name="repository_pc_pc320", type=pcm_pc_pc_repository_pc_pc_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="Interface319", type=Interface, multiplicity=Multiplicity(0, 1))
    }
)
eventTypes__EventGroup321: BinaryAssociation = BinaryAssociation(
    name="eventTypes__EventGroup321",
    ends={
        Property(name="repository_pc_pc323", type=pcm_pc_pc_repository_pc_pc_EventGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="EventType322", type=EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter__EventType324: BinaryAssociation = BinaryAssociation(
    name="parameter__EventType324",
    ends={
        Property(name="repository_pc_pc326", type=pcm_pc_pc_repository_pc_pc_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter325", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventGroup__EventType327: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventType327",
    ends={
        Property(name="repository_pc_pc329", type=pcm_pc_pc_repository_pc_pc_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="EventGroup328", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
failureTypes__Repository303: BinaryAssociation = BinaryAssociation(
    name="failureTypes__Repository303",
    ends={
        Property(name="reliability_pc_pc304", type=pcm_pc_pc_repository_pc_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="FailureType", type=FailureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes__Repository305: BinaryAssociation = BinaryAssociation(
    name="dataTypes__Repository305",
    ends={
        Property(name="repository_pc_pc307", type=pcm_pc_pc_repository_pc_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="DataType306", type=DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentInterfaces__Interface308: BinaryAssociation = BinaryAssociation(
    name="parentInterfaces__Interface308",
    ends={
        Property(name="Interface309", type=pcm_pc_pc_repository_pc_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_Interface", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
protocols__Interface310: BinaryAssociation = BinaryAssociation(
    name="protocols__Interface310",
    ends={
        Property(name="Protocol", type=pcm_pc_pc_repository_pc_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_Interface311", type=Protocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCharacterisations312: BinaryAssociation = BinaryAssociation(
    name="requiredCharacterisations312",
    ends={
        Property(name="repository_pc_pc313", type=pcm_pc_pc_repository_pc_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="RequiredCharacterisation", type=RequiredCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiringEntity_RequiredRole344: BinaryAssociation = BinaryAssociation(
    name="requiringEntity_RequiredRole344",
    ends={
        Property(name="core_pc_pc346", type=pcm_pc_pc_repository_pc_pc_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_pc_pc345", type=entity_pc_pc_InterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
interface__OperationSignature347: BinaryAssociation = BinaryAssociation(
    name="interface__OperationSignature347",
    ends={
        Property(name="repository_pc_pc348", type=pcm_pc_pc_repository_pc_pc_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationInterface", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
parameters__OperationSignature349: BinaryAssociation = BinaryAssociation(
    name="parameters__OperationSignature349",
    ends={
        Property(name="repository_pc_pc351", type=pcm_pc_pc_repository_pc_pc_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter350", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptions__Signature330: BinaryAssociation = BinaryAssociation(
    name="exceptions__Signature330",
    ends={
        Property(name="ExceptionType", type=pcm_pc_pc_repository_pc_pc_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_Signature", type=ExceptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureType331: BinaryAssociation = BinaryAssociation(
    name="failureType331",
    ends={
        Property(name="FailureType333", type=pcm_pc_pc_repository_pc_pc_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_Signature332", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
parameters__InfrastructureSignature334: BinaryAssociation = BinaryAssociation(
    name="parameters__InfrastructureSignature334",
    ends={
        Property(name="repository_pc_pc336", type=pcm_pc_pc_repository_pc_pc_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter335", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureInterface__InfrastructureSignature337: BinaryAssociation = BinaryAssociation(
    name="infrastructureInterface__InfrastructureSignature337",
    ends={
        Property(name="repository_pc_pc338", type=pcm_pc_pc_repository_pc_pc_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="InfrastructureInterface", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureSignatures__InfrastructureInterface339: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignatures__InfrastructureInterface339",
    ends={
        Property(name="repository_pc_pc341", type=pcm_pc_pc_repository_pc_pc_InfrastructureInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="InfrastructureSignature340", type=InfrastructureSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterface__InfrastructureRequiredRole342: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__InfrastructureRequiredRole342",
    ends={
        Property(name="InfrastructureInterface343", type=pcm_pc_pc_repository_pc_pc_InfrastructureRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_InfrastructureRequiredRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SourceRole359: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SourceRole359",
    ends={
        Property(name="EventGroup360", type=pcm_pc_pc_repository_pc_pc_SourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_SourceRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SinkRole361: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SinkRole361",
    ends={
        Property(name="EventGroup362", type=pcm_pc_pc_repository_pc_pc_SinkRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_SinkRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface__OperationProvidedRole363: BinaryAssociation = BinaryAssociation(
    name="providedInterface__OperationProvidedRole363",
    ends={
        Property(name="OperationInterface364", type=pcm_pc_pc_repository_pc_pc_OperationProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_OperationProvidedRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
returnType__OperationSignature352: BinaryAssociation = BinaryAssociation(
    name="returnType__OperationSignature352",
    ends={
        Property(name="DataType353", type=pcm_pc_pc_repository_pc_pc_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_OperationSignature", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
signatures__OperationInterface354: BinaryAssociation = BinaryAssociation(
    name="signatures__OperationInterface354",
    ends={
        Property(name="repository_pc_pc356", type=pcm_pc_pc_repository_pc_pc_OperationInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="OperationSignature355", type=OperationSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterface__OperationRequiredRole357: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__OperationRequiredRole357",
    ends={
        Property(name="OperationInterface358", type=pcm_pc_pc_repository_pc_pc_OperationRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_OperationRequiredRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface__InfrastructureProvidedRole365: BinaryAssociation = BinaryAssociation(
    name="providedInterface__InfrastructureProvidedRole365",
    ends={
        Property(name="InfrastructureInterface366", type=pcm_pc_pc_repository_pc_pc_InfrastructureProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_InfrastructureProvidedRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
parentProvidesComponentTypes367: BinaryAssociation = BinaryAssociation(
    name="parentProvidesComponentTypes367",
    ends={
        Property(name="ProvidesComponentType", type=pcm_pc_pc_repository_pc_pc_CompleteComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_CompleteComponentType", type=ProvidesComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
innerDeclaration_CompositeDataType371: BinaryAssociation = BinaryAssociation(
    name="innerDeclaration_CompositeDataType371",
    ends={
        Property(name="repository_pc_pc372", type=pcm_pc_pc_repository_pc_pc_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="InnerDeclaration", type=InnerDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype_InnerDeclaration373: BinaryAssociation = BinaryAssociation(
    name="datatype_InnerDeclaration373",
    ends={
        Property(name="DataType374", type=pcm_pc_pc_repository_pc_pc_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_InnerDeclaration", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
compositeDataType_InnerDeclaration375: BinaryAssociation = BinaryAssociation(
    name="compositeDataType_InnerDeclaration375",
    ends={
        Property(name="repository_pc_pc377", type=pcm_pc_pc_repository_pc_pc_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="CompositeDataType376", type=CompositeDataType, multiplicity=Multiplicity(0, 1))
    }
)
innerType_CollectionDataType368: BinaryAssociation = BinaryAssociation(
    name="innerType_CollectionDataType368",
    ends={
        Property(name="DataType369", type=pcm_pc_pc_repository_pc_pc_CollectionDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_CollectionDataType", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
parentType_CompositeDataType370: BinaryAssociation = BinaryAssociation(
    name="parentType_CompositeDataType370",
    ends={
        Property(name="CompositeDataType", type=pcm_pc_pc_repository_pc_pc_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 9999))
    }
)
networkInducedFailureType__CommunicationLinkResourceType398: BinaryAssociation = BinaryAssociation(
    name="networkInducedFailureType__CommunicationLinkResourceType398",
    ends={
        Property(name="reliability_pc_pc399", type=pcm_pc_pc_resourcetype_pc_pc_CommunicationLinkResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="NetworkInducedFailureType", type=NetworkInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
resourceRepository__ResourceInterface400: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__ResourceInterface400",
    ends={
        Property(name="resourcetype_pc_pc402", type=pcm_pc_pc_resourcetype_pc_pc_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceRepository401", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
resourceSignatures__ResourceInterface403: BinaryAssociation = BinaryAssociation(
    name="resourceSignatures__ResourceInterface403",
    ends={
        Property(name="resourcetype_pc_pc405", type=pcm_pc_pc_resourcetype_pc_pc_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceSignature404", type=ResourceSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter__ResourceSignature378: BinaryAssociation = BinaryAssociation(
    name="parameter__ResourceSignature378",
    ends={
        Property(name="repository_pc_pc380", type=pcm_pc_pc_resourcetype_pc_pc_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter379", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceInterface__ResourceSignature381: BinaryAssociation = BinaryAssociation(
    name="resourceInterface__ResourceSignature381",
    ends={
        Property(name="resourcetype_pc_pc383", type=pcm_pc_pc_resourcetype_pc_pc_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceInterface382", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
hardwareInducedFailureType__ProcessingResourceType384: BinaryAssociation = BinaryAssociation(
    name="hardwareInducedFailureType__ProcessingResourceType384",
    ends={
        Property(name="reliability_pc_pc385", type=pcm_pc_pc_resourcetype_pc_pc_ProcessingResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="HardwareInducedFailureType", type=HardwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
resourceRepository_ResourceType386: BinaryAssociation = BinaryAssociation(
    name="resourceRepository_ResourceType386",
    ends={
        Property(name="resourcetype_pc_pc387", type=pcm_pc_pc_resourcetype_pc_pc_ResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaces__ResourceRepository388: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaces__ResourceRepository388",
    ends={
        Property(name="resourcetype_pc_pc390", type=pcm_pc_pc_resourcetype_pc_pc_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceInterface389", type=ResourceInterface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schedulingPolicies__ResourceRepository391: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicies__ResourceRepository391",
    ends={
        Property(name="resourcetype_pc_pc392", type=pcm_pc_pc_resourcetype_pc_pc_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="SchedulingPolicy", type=SchedulingPolicy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
availableResourceTypes_ResourceRepository393: BinaryAssociation = BinaryAssociation(
    name="availableResourceTypes_ResourceRepository393",
    ends={
        Property(name="resourcetype_pc_pc394", type=pcm_pc_pc_resourcetype_pc_pc_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceType", type=ResourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRepository__SchedulingPolicy395: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__SchedulingPolicy395",
    ends={
        Property(name="resourcetype_pc_pc397", type=pcm_pc_pc_resourcetype_pc_pc_SchedulingPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceRepository396", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
namedReference__VariableUsage430: BinaryAssociation = BinaryAssociation(
    name="namedReference__VariableUsage430",
    ends={
        Property(name="parameter_pc_pc_pcm_pc_pc_AbstractNamedReference", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_parameter_pc_pc_VariableUsage", type=parameter_pc_pc_pcm_pc_pc_AbstractNamedReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification_VariableCharacterisation431: BinaryAssociation = BinaryAssociation(
    name="specification_VariableCharacterisation431",
    ends={
        Property(name="core_pc_pc433", type=pcm_pc_pc_parameter_pc_pc_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable432", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableUsage_VariableCharacterisation434: BinaryAssociation = BinaryAssociation(
    name="variableUsage_VariableCharacterisation434",
    ends={
        Property(name="parameter_pc_pc436", type=pcm_pc_pc_parameter_pc_pc_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage435", type=VariableUsage, multiplicity=Multiplicity(0, 1))
    }
)
variableCharacterisation_VariableUsage406: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_VariableUsage406",
    ends={
        Property(name="parameter_pc_pc408", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableCharacterisation407", type=VariableCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_VariableUsage409: BinaryAssociation = BinaryAssociation(
    name="userData_VariableUsage409",
    ends={
        Property(name="usagemodel_pc_pc411", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="UserData410", type=UserData, multiplicity=Multiplicity(0, 1))
    }
)
callAction__VariableUsage412: BinaryAssociation = BinaryAssociation(
    name="callAction__VariableUsage412",
    ends={
        Property(name="seff_pc_pc413", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="CallAction", type=CallAction, multiplicity=Multiplicity(0, 1))
    }
)
synchronisationPoint_VariableUsage414: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_VariableUsage414",
    ends={
        Property(name="seff_pc_pc415", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
callReturnAction__VariableUsage416: BinaryAssociation = BinaryAssociation(
    name="callReturnAction__VariableUsage416",
    ends={
        Property(name="seff_pc_pc417", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="CallReturnAction", type=CallReturnAction, multiplicity=Multiplicity(0, 1))
    }
)
setVariableAction_VariableUsage418: BinaryAssociation = BinaryAssociation(
    name="setVariableAction_VariableUsage418",
    ends={
        Property(name="seff_pc_pc419", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="SetVariableAction", type=SetVariableAction, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage420: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage420",
    ends={
        Property(name="qosannotations_pc_pc421", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="SpecifiedOutputParameterAbstraction", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__VariableUsage422: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__VariableUsage422",
    ends={
        Property(name="core_pc_pc424", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="composition_pc_pc423", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_InputParameterUsage425: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_InputParameterUsage425",
    ends={
        Property(name="usagemodel_pc_pc426", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="EntryLevelSystemCall", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_OutputParameterUsage427: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_OutputParameterUsage427",
    ends={
        Property(name="usagemodel_pc_pc429", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="EntryLevelSystemCall428", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceType__HardwareInducedFailureType437: BinaryAssociation = BinaryAssociation(
    name="processingResourceType__HardwareInducedFailureType437",
    ends={
        Property(name="resourcetype_pc_pc438", type=pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcessingResourceType", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
internalFailureOccurrenceDescriptions__SoftwareInducedFailureType439: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__SoftwareInducedFailureType439",
    ends={
        Property(name="reliability_pc_pc440", type=pcm_pc_pc_reliability_pc_pc_SoftwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="InternalFailureOccurrenceDescription", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999))
    }
)
communicationLinkResourceType__NetworkInducedFailureType445: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType__NetworkInducedFailureType445",
    ends={
        Property(name="resourcetype_pc_pc446", type=pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceType", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription447: BinaryAssociation = BinaryAssociation(
    name="specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription447",
    ends={
        Property(name="qosannotations_pc_pc448", type=pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="qos_reliability_pc_pc", type=qos_reliability_pc_pc_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(0, 1))
    }
)
failureType__ExternalFailureOccurrenceDescription449: BinaryAssociation = BinaryAssociation(
    name="failureType__ExternalFailureOccurrenceDescription449",
    ends={
        Property(name="FailureType450", type=pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription", type=FailureType, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource__ResourceTimeoutFailureType451: BinaryAssociation = BinaryAssociation(
    name="passiveResource__ResourceTimeoutFailureType451",
    ends={
        Property(name="repository_pc_pc453", type=pcm_pc_pc_reliability_pc_pc_ResourceTimeoutFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="PassiveResource452", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
internalAction__InternalFailureOccurrenceDescription441: BinaryAssociation = BinaryAssociation(
    name="internalAction__InternalFailureOccurrenceDescription441",
    ends={
        Property(name="seff_pc_pc442", type=pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="InternalAction", type=InternalAction, multiplicity=Multiplicity(0, 1))
    }
)
softwareInducedFailureType__InternalFailureOccurrenceDescription443: BinaryAssociation = BinaryAssociation(
    name="softwareInducedFailureType__InternalFailureOccurrenceDescription443",
    ends={
        Property(name="reliability_pc_pc444", type=pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="SoftwareInducedFailureType", type=SoftwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
resourceCall__Action463: BinaryAssociation = BinaryAssociation(
    name="resourceCall__Action463",
    ends={
        Property(name="seff_pc_pc465", type=pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_pc_pc464", type=seff_performance_pc_pc_ResourceCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor_AbstractAction466: BinaryAssociation = BinaryAssociation(
    name="predecessor_AbstractAction466",
    ends={
        Property(name="seff_pc_pc467", type=pcm_pc_pc_seff_pc_pc_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
successor_AbstractAction468: BinaryAssociation = BinaryAssociation(
    name="successor_AbstractAction468",
    ends={
        Property(name="seff_pc_pc470", type=pcm_pc_pc_seff_pc_pc_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction469", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemandingBehaviour_AbstractAction471: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingBehaviour_AbstractAction471",
    ends={
        Property(name="seff_pc_pc472", type=pcm_pc_pc_seff_pc_pc_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingBehaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
repository__FailureType454: BinaryAssociation = BinaryAssociation(
    name="repository__FailureType454",
    ends={
        Property(name="repository_pc_pc456", type=pcm_pc_pc_reliability_pc_pc_FailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository455", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemand_Action457: BinaryAssociation = BinaryAssociation(
    name="resourceDemand_Action457",
    ends={
        Property(name="seff_pc_pc459", type=pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_pc_pc458", type=seff_performance_pc_pc_ParametricResourceDemand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureCall__Action460: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__Action460",
    ends={
        Property(name="seff_pc_pc462", type=pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_performance_pc_pc461", type=seff_performance_pc_pc_InfrastructureCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branchAction_AbstractBranchTransition483: BinaryAssociation = BinaryAssociation(
    name="branchAction_AbstractBranchTransition483",
    ends={
        Property(name="seff_pc_pc484", type=pcm_pc_pc_seff_pc_pc_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="BranchAction", type=BranchAction, multiplicity=Multiplicity(0, 1))
    }
)
branchBehaviour_BranchTransition485: BinaryAssociation = BinaryAssociation(
    name="branchBehaviour_BranchTransition485",
    ends={
        Property(name="seff_pc_pc487", type=pcm_pc_pc_seff_pc_pc_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingBehaviour486", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branches_Branch488: BinaryAssociation = BinaryAssociation(
    name="branches_Branch488",
    ends={
        Property(name="seff_pc_pc490", type=pcm_pc_pc_seff_pc_pc_BranchAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractBranchTransition489", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abstractLoopAction_ResourceDemandingBehaviour473: BinaryAssociation = BinaryAssociation(
    name="abstractLoopAction_ResourceDemandingBehaviour473",
    ends={
        Property(name="seff_pc_pc474", type=pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractLoopAction", type=AbstractLoopAction, multiplicity=Multiplicity(0, 1))
    }
)
abstractBranchTransition_ResourceDemandingBehaviour475: BinaryAssociation = BinaryAssociation(
    name="abstractBranchTransition_ResourceDemandingBehaviour475",
    ends={
        Property(name="seff_pc_pc476", type=pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractBranchTransition", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
steps_Behaviour477: BinaryAssociation = BinaryAssociation(
    name="steps_Behaviour477",
    ends={
        Property(name="seff_pc_pc479", type=pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction478", type=AbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyBehaviour_Loop480: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop480",
    ends={
        Property(name="seff_pc_pc482", type=pcm_pc_pc_seff_pc_pc_AbstractLoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingBehaviour481", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
describedService__SEFF494: BinaryAssociation = BinaryAssociation(
    name="describedService__SEFF494",
    ends={
        Property(name="Signature", type=pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
basicComponent_ServiceEffectSpecification495: BinaryAssociation = BinaryAssociation(
    name="basicComponent_ServiceEffectSpecification495",
    ends={
        Property(name="repository_pc_pc497", type=pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BasicComponent496", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemandingInternalBehaviours498: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingInternalBehaviours498",
    ends={
        Property(name="seff_pc_pc499", type=pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingInternalBehaviour", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceDemandingSEFF_ResourceDemandingInternalBehaviour500: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingSEFF_ResourceDemandingInternalBehaviour500",
    ends={
        Property(name="seff_pc_pc501", type=pcm_pc_pc_seff_pc_pc_ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceDemandingSEFF", type=ResourceDemandingSEFF, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_ReleaseAction502: BinaryAssociation = BinaryAssociation(
    name="passiveResource_ReleaseAction502",
    ends={
        Property(name="PassiveResource503", type=pcm_pc_pc_seff_pc_pc_ReleaseAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_pc_pc_ReleaseAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
inputVariableUsages__CallAction491: BinaryAssociation = BinaryAssociation(
    name="inputVariableUsages__CallAction491",
    ends={
        Property(name="parameter_pc_pc493", type=pcm_pc_pc_seff_pc_pc_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage492", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputParameterUsage_SynchronisationPoint517: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsage_SynchronisationPoint517",
    ends={
        Property(name="parameter_pc_pc519", type=pcm_pc_pc_seff_pc_pc_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage518", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forkAction_SynchronisationPoint520: BinaryAssociation = BinaryAssociation(
    name="forkAction_SynchronisationPoint520",
    ends={
        Property(name="seff_pc_pc522", type=pcm_pc_pc_seff_pc_pc_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkAction521", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
synchronousForkedBehaviours_SynchronisationPoint523: BinaryAssociation = BinaryAssociation(
    name="synchronousForkedBehaviours_SynchronisationPoint523",
    ends={
        Property(name="seff_pc_pc525", type=pcm_pc_pc_seff_pc_pc_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedBehaviour524", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledService_ExternalService526: BinaryAssociation = BinaryAssociation(
    name="calledService_ExternalService526",
    ends={
        Property(name="OperationSignature527", type=pcm_pc_pc_seff_pc_pc_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_pc_pc_ExternalCallAction", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
iterationCount_LoopAction504: BinaryAssociation = BinaryAssociation(
    name="iterationCount_LoopAction504",
    ends={
        Property(name="core_pc_pc506", type=pcm_pc_pc_seff_pc_pc_LoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable505", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
asynchronousForkedBehaviours_ForkAction507: BinaryAssociation = BinaryAssociation(
    name="asynchronousForkedBehaviours_ForkAction507",
    ends={
        Property(name="seff_pc_pc508", type=pcm_pc_pc_seff_pc_pc_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedBehaviour", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronisingBehaviours_ForkAction509: BinaryAssociation = BinaryAssociation(
    name="synchronisingBehaviours_ForkAction509",
    ends={
        Property(name="seff_pc_pc511", type=pcm_pc_pc_seff_pc_pc_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="SynchronisationPoint510", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
synchronisationPoint_ForkedBehaviour512: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_ForkedBehaviour512",
    ends={
        Property(name="seff_pc_pc514", type=pcm_pc_pc_seff_pc_pc_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="SynchronisationPoint513", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
forkAction_ForkedBehaivour515: BinaryAssociation = BinaryAssociation(
    name="forkAction_ForkedBehaivour515",
    ends={
        Property(name="seff_pc_pc516", type=pcm_pc_pc_seff_pc_pc_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkAction", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
passiveresource_AcquireAction534: BinaryAssociation = BinaryAssociation(
    name="passiveresource_AcquireAction534",
    ends={
        Property(name="PassiveResource535", type=pcm_pc_pc_seff_pc_pc_AcquireAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_pc_pc_AcquireAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
parameter_CollectionIteratorAction536: BinaryAssociation = BinaryAssociation(
    name="parameter_CollectionIteratorAction536",
    ends={
        Property(name="Parameter537", type=pcm_pc_pc_seff_pc_pc_CollectionIteratorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_pc_pc_CollectionIteratorAction", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
branchCondition_GuardedBranchTransition538: BinaryAssociation = BinaryAssociation(
    name="branchCondition_GuardedBranchTransition538",
    ends={
        Property(name="core_pc_pc540", type=pcm_pc_pc_seff_pc_pc_GuardedBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable539", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
role_ExternalService528: BinaryAssociation = BinaryAssociation(
    name="role_ExternalService528",
    ends={
        Property(name="OperationRequiredRole530", type=pcm_pc_pc_seff_pc_pc_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_pc_pc_ExternalCallAction529", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
returnVariableUsage__CallReturnAction531: BinaryAssociation = BinaryAssociation(
    name="returnVariableUsage__CallReturnAction531",
    ends={
        Property(name="parameter_pc_pc533", type=pcm_pc_pc_seff_pc_pc_CallReturnAction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage532", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
internalFailureOccurrenceDescriptions__InternalAction551: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__InternalAction551",
    ends={
        Property(name="reliability_pc_pc553", type=pcm_pc_pc_seff_pc_pc_InternalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="InternalFailureOccurrenceDescription552", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localVariableUsages_SetVariableAction541: BinaryAssociation = BinaryAssociation(
    name="localVariableUsages_SetVariableAction541",
    ends={
        Property(name="parameter_pc_pc543", type=pcm_pc_pc_seff_pc_pc_SetVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage542", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledResourceDemandingInternalBehaviour544: BinaryAssociation = BinaryAssociation(
    name="calledResourceDemandingInternalBehaviour544",
    ends={
        Property(name="ResourceDemandingInternalBehaviour545", type=pcm_pc_pc_seff_pc_pc_InternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_pc_pc_InternalCallAction", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
eventType__EmitEventAction546: BinaryAssociation = BinaryAssociation(
    name="eventType__EmitEventAction546",
    ends={
        Property(name="EventType547", type=pcm_pc_pc_seff_pc_pc_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_pc_pc_EmitEventAction", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EmitEventAction548: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EmitEventAction548",
    ends={
        Property(name="SourceRole550", type=pcm_pc_pc_seff_pc_pc_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_pc_pc_EmitEventAction549", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__InfrastructureCall561: BinaryAssociation = BinaryAssociation(
    name="requiredRole__InfrastructureCall561",
    ends={
        Property(name="InfrastructureRequiredRole563", type=pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall562", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
signature__InfrastructureCall554: BinaryAssociation = BinaryAssociation(
    name="signature__InfrastructureCall554",
    ends={
        Property(name="InfrastructureSignature555", type=pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__InfrastructureCall556: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__InfrastructureCall556",
    ends={
        Property(name="core_pc_pc558", type=pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable557", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action__InfrastructureCall559: BinaryAssociation = BinaryAssociation(
    name="action__InfrastructureCall559",
    ends={
        Property(name="seff_pc_pc560", type=pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractInternalControlFlowAction", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
failureHandlingAlternatives__RecoveryActionBehaviour583: BinaryAssociation = BinaryAssociation(
    name="failureHandlingAlternatives__RecoveryActionBehaviour583",
    ends={
        Property(name="seff_reliability_pc_pc_RecoveryActionBehaviour", type=pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour", type=seff_reliability_pc_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999))
    }
)
action__ResourceCall564: BinaryAssociation = BinaryAssociation(
    name="action__ResourceCall564",
    ends={
        Property(name="seff_pc_pc566", type=pcm_pc_pc_seff_performance_pc_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractInternalControlFlowAction565", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceRequiredRole__ResourceCall567: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRole__ResourceCall567",
    ends={
        Property(name="entity_pc_pc_ResourceRequiredRole568", type=pcm_pc_pc_seff_performance_pc_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_performance_pc_pc_ResourceCall", type=entity_pc_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
signature__ResourceCall569: BinaryAssociation = BinaryAssociation(
    name="signature__ResourceCall569",
    ends={
        Property(name="ResourceSignature571", type=pcm_pc_pc_seff_performance_pc_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_performance_pc_pc_ResourceCall570", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__ResourceCall572: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__ResourceCall572",
    ends={
        Property(name="core_pc_pc574", type=pcm_pc_pc_seff_performance_pc_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable573", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification_ParametericResourceDemand575: BinaryAssociation = BinaryAssociation(
    name="specification_ParametericResourceDemand575",
    ends={
        Property(name="core_pc_pc577", type=pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable576", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredResource_ParametricResourceDemand578: BinaryAssociation = BinaryAssociation(
    name="requiredResource_ParametricResourceDemand578",
    ends={
        Property(name="ProcessingResourceType579", type=pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
action_ParametricResourceDemand580: BinaryAssociation = BinaryAssociation(
    name="action_ParametricResourceDemand580",
    ends={
        Property(name="seff_pc_pc582", type=pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractInternalControlFlowAction581", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
failureTypes_FailureHandlingEntity591: BinaryAssociation = BinaryAssociation(
    name="failureTypes_FailureHandlingEntity591",
    ends={
        Property(name="FailureType592", type=pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
signature_SpecifiedQoSAnnation593: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedQoSAnnation593",
    ends={
        Property(name="Signature594", type=pcm_pc_pc_qosannotations_pc_pc_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_qosannotations_pc_pc_SpecifiedQoSAnnotation", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedQoSAnnotation595: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedQoSAnnotation595",
    ends={
        Property(name="Role", type=pcm_pc_pc_qosannotations_pc_pc_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_qosannotations_pc_pc_SpecifiedQoSAnnotation596", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
qosAnnotations_SpecifiedQoSAnnotation597: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedQoSAnnotation597",
    ends={
        Property(name="qosannotations_pc_pc598", type=pcm_pc_pc_qosannotations_pc_pc_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstractions_QoSAnnotations599: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstractions_QoSAnnotations599",
    ends={
        Property(name="qosannotations_pc_pc601", type=pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="SpecifiedOutputParameterAbstraction600", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
recoveryAction__RecoveryActionBehaviour584: BinaryAssociation = BinaryAssociation(
    name="recoveryAction__RecoveryActionBehaviour584",
    ends={
        Property(name="seff_pc_pc585", type=pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_reliability_pc_pc", type=seff_reliability_pc_pc_RecoveryAction, multiplicity=Multiplicity(0, 1))
    }
)
primaryBehaviour__RecoveryAction586: BinaryAssociation = BinaryAssociation(
    name="primaryBehaviour__RecoveryAction586",
    ends={
        Property(name="seff_reliability_pc_pc_RecoveryActionBehaviour587", type=pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction", type=seff_reliability_pc_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
recoveryActionBehaviours__RecoveryAction588: BinaryAssociation = BinaryAssociation(
    name="recoveryActionBehaviours__RecoveryAction588",
    ends={
        Property(name="seff_pc_pc590", type=pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="seff_reliability_pc_pc589", type=seff_reliability_pc_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification_SpecifiedExecutionTime616: BinaryAssociation = BinaryAssociation(
    name="specification_SpecifiedExecutionTime616",
    ends={
        Property(name="core_pc_pc618", type=pcm_pc_pc_qos_performance_pc_pc_SpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable617", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext_ComponentSpecifiedExecutionTime619: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ComponentSpecifiedExecutionTime619",
    ends={
        Property(name="composition_pc_pc_AssemblyContext620", type=pcm_pc_pc_qos_performance_pc_pc_ComponentSpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_qos_performance_pc_pc_ComponentSpecifiedExecutionTime", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
system_QoSAnnotations602: BinaryAssociation = BinaryAssociation(
    name="system_QoSAnnotations602",
    ends={
        Property(name="system_pc_pc", type=pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="System", type=System, multiplicity=Multiplicity(0, 1))
    }
)
specifiedQoSAnnotations_QoSAnnotations603: BinaryAssociation = BinaryAssociation(
    name="specifiedQoSAnnotations_QoSAnnotations603",
    ends={
        Property(name="qosannotations_pc_pc604", type=pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="SpecifiedQoSAnnotation", type=SpecifiedQoSAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature_SpecifiedOutputParameterAbstraction605: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedOutputParameterAbstraction605",
    ends={
        Property(name="Signature606", type=pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedOutputParameterAbstraction607: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedOutputParameterAbstraction607",
    ends={
        Property(name="Role609", type=pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction608", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
expectedExternalOutputs_SpecifiedOutputParameterAbstraction610: BinaryAssociation = BinaryAssociation(
    name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction610",
    ends={
        Property(name="parameter_pc_pc612", type=pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableUsage611", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qosAnnotations_SpecifiedOutputParameterAbstraction613: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedOutputParameterAbstraction613",
    ends={
        Property(name="qosannotations_pc_pc615", type=pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="QoSAnnotations614", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation621: BinaryAssociation = BinaryAssociation(
    name="externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation621",
    ends={
        Property(name="reliability_pc_pc622", type=pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ExternalFailureOccurrenceDescription", type=ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qosAnnotations_System623: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_System623",
    ends={
        Property(name="qosannotations_pc_pc625", type=pcm_pc_pc_system_pc_pc_System, multiplicity=Multiplicity(1, 1)),
        Property(name="QoSAnnotations624", type=QoSAnnotations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activeResourceSpecifications_ResourceContainer637: BinaryAssociation = BinaryAssociation(
    name="activeResourceSpecifications_ResourceContainer637",
    ends={
        Property(name="resourceenvironment_pc_pc639", type=pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcessingResourceSpecification638", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceEnvironment_ResourceContainer640: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_ResourceContainer640",
    ends={
        Property(name="resourceenvironment_pc_pc642", type=pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceEnvironment641", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
nestedResourceContainers__ResourceContainer643: BinaryAssociation = BinaryAssociation(
    name="nestedResourceContainers__ResourceContainer643",
    ends={
        Property(name="resourceenvironment_pc_pc645", type=pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer644", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentResourceContainer__ResourceContainer646: BinaryAssociation = BinaryAssociation(
    name="parentResourceContainer__ResourceContainer646",
    ends={
        Property(name="resourceenvironment_pc_pc648", type=pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer647", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
schedulingPolicy649: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicy649",
    ends={
        Property(name="SchedulingPolicy650", type=pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification", type=SchedulingPolicy, multiplicity=Multiplicity(0, 1))
    }
)
linkingResources__ResourceEnvironment626: BinaryAssociation = BinaryAssociation(
    name="linkingResources__ResourceEnvironment626",
    ends={
        Property(name="resourceenvironment_pc_pc627", type=pcm_pc_pc_resourceenvironment_pc_pc_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="LinkingResource", type=LinkingResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_ResourceEnvironment628: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ResourceEnvironment628",
    ends={
        Property(name="resourceenvironment_pc_pc629", type=pcm_pc_pc_resourceenvironment_pc_pc_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectedResourceContainers_LinkingResource630: BinaryAssociation = BinaryAssociation(
    name="connectedResourceContainers_LinkingResource630",
    ends={
        Property(name="ResourceContainer631", type=pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource", type=ResourceContainer, multiplicity=Multiplicity(0, 9999))
    }
)
communicationLinkResourceSpecifications_LinkingResource632: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifications_LinkingResource632",
    ends={
        Property(name="resourceenvironment_pc_pc634", type=pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="CommunicationLinkResourceSpecification633", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceEnvironment_LinkingResource635: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_LinkingResource635",
    ends={
        Property(name="resourceenvironment_pc_pc636", type=pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceEnvironment", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
resourceContainer_AllocationContext671: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_AllocationContext671",
    ends={
        Property(name="ResourceContainer672", type=pcm_pc_pc_allocation_pc_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_allocation_pc_pc_AllocationContext", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_AllocationContext673: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_AllocationContext673",
    ends={
        Property(name="composition_pc_pc_AssemblyContext675", type=pcm_pc_pc_allocation_pc_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_allocation_pc_pc_AllocationContext674", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
allocation_AllocationContext676: BinaryAssociation = BinaryAssociation(
    name="allocation_AllocationContext676",
    ends={
        Property(name="allocation_pc_pc", type=pcm_pc_pc_allocation_pc_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="Allocation", type=Allocation, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__AllocationContext677: BinaryAssociation = BinaryAssociation(
    name="eventChannel__AllocationContext677",
    ends={
        Property(name="composition_pc_pc_EventChannel", type=pcm_pc_pc_allocation_pc_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_allocation_pc_pc_AllocationContext678", type=composition_pc_pc_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceType_ActiveResourceSpecification651: BinaryAssociation = BinaryAssociation(
    name="activeResourceType_ActiveResourceSpecification651",
    ends={
        Property(name="ProcessingResourceType653", type=pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification652", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
processingRate_ProcessingResourceSpecification654: BinaryAssociation = BinaryAssociation(
    name="processingRate_ProcessingResourceSpecification654",
    ends={
        Property(name="core_pc_pc656", type=pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable655", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceContainer_ProcessingResourceSpecification657: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ProcessingResourceSpecification657",
    ends={
        Property(name="resourceenvironment_pc_pc659", type=pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceContainer658", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
linkingResource_CommunicationLinkResourceSpecification660: BinaryAssociation = BinaryAssociation(
    name="linkingResource_CommunicationLinkResourceSpecification660",
    ends={
        Property(name="resourceenvironment_pc_pc662", type=pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="LinkingResource661", type=LinkingResource, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceType_CommunicationLinkResourceSpecification663: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType_CommunicationLinkResourceSpecification663",
    ends={
        Property(name="CommunicationLinkResourceType664", type=pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
latency_CommunicationLinkResourceSpecification665: BinaryAssociation = BinaryAssociation(
    name="latency_CommunicationLinkResourceSpecification665",
    ends={
        Property(name="core_pc_pc667", type=pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable666", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throughput_CommunicationLinkResourceSpecification668: BinaryAssociation = BinaryAssociation(
    name="throughput_CommunicationLinkResourceSpecification668",
    ends={
        Property(name="core_pc_pc670", type=pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="PCMRandomVariable669", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
completions_CompletionRepository686: BinaryAssociation = BinaryAssociation(
    name="completions_CompletionRepository686",
    ends={
        Property(name="Completion", type=pcm_pc_pc_completions_pc_pc_CompletionRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_completions_pc_pc_CompletionRepository", type=Completion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCommunicationLinkResource_ParametricResourceDemand687: BinaryAssociation = BinaryAssociation(
    name="requiredCommunicationLinkResource_ParametricResourceDemand687",
    ends={
        Property(name="CommunicationLinkResourceType688", type=pcm_pc_pc_completions_pc_pc_NetworkDemandParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_completions_pc_pc_NetworkDemandParametricResourceDemand", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
targetResourceEnvironment_Allocation679: BinaryAssociation = BinaryAssociation(
    name="targetResourceEnvironment_Allocation679",
    ends={
        Property(name="ResourceEnvironment680", type=pcm_pc_pc_allocation_pc_pc_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_allocation_pc_pc_Allocation", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
system_Allocation681: BinaryAssociation = BinaryAssociation(
    name="system_Allocation681",
    ends={
        Property(name="System683", type=pcm_pc_pc_allocation_pc_pc_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_allocation_pc_pc_Allocation682", type=System, multiplicity=Multiplicity(0, 1))
    }
)
allocationContexts_Allocation684: BinaryAssociation = BinaryAssociation(
    name="allocationContexts_Allocation684",
    ends={
        Property(name="allocation_pc_pc685", type=pcm_pc_pc_allocation_pc_pc_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="AllocationContext", type=AllocationContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_pcm_pc_pc_core_pc_pc_PCMRandomVariable_RandomVariable = Generalization(general=RandomVariable, specific=pcm_pc_pc_core_pc_pc_PCMRandomVariable)
gen_pcm_pc_pc_entity_pc_pc_InterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_pc_pc_entity_pc_pc_InterfaceProvidingEntity)
gen_pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity_entity_pc_pc_Entity = Generalization(general=entity_pc_pc_Entity, specific=pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity)
gen_pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity_entity_pc_pc_ResourceInterfaceRequiringEntity = Generalization(general=entity_pc_pc_ResourceInterfaceRequiringEntity, specific=pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity)
gen_pcm_pc_pc_entity_pc_pc_ResourceInterfaceRequiringEntity_Entity = Generalization(general=Entity, specific=pcm_pc_pc_entity_pc_pc_ResourceInterfaceRequiringEntity)
gen_pcm_pc_pc_entity_pc_pc_ResourceRequiredRole_Role = Generalization(general=Role, specific=pcm_pc_pc_entity_pc_pc_ResourceRequiredRole)
gen_pcm_pc_pc_entity_pc_pc_ResourceProvidedRole_Role = Generalization(general=Role, specific=pcm_pc_pc_entity_pc_pc_ResourceProvidedRole)
gen_pcm_pc_pc_entity_pc_pc_InterfaceProvidingRequiringEntity_entity_pc_pc_InterfaceProvidingEntity = Generalization(general=entity_pc_pc_InterfaceProvidingEntity, specific=pcm_pc_pc_entity_pc_pc_InterfaceProvidingRequiringEntity)
gen_pcm_pc_pc_entity_pc_pc_InterfaceProvidingRequiringEntity_entity_pc_pc_InterfaceRequiringEntity = Generalization(general=entity_pc_pc_InterfaceRequiringEntity, specific=pcm_pc_pc_entity_pc_pc_InterfaceProvidingRequiringEntity)
gen_pcm_pc_pc_composition_pc_pc_DelegationConnector_Connector = Generalization(general=Connector, specific=pcm_pc_pc_composition_pc_pc_DelegationConnector)
gen_pcm_pc_pc_composition_pc_pc_Connector_Entity = Generalization(general=Entity, specific=pcm_pc_pc_composition_pc_pc_Connector)
gen_pcm_pc_pc_composition_pc_pc_ComposedStructure_Entity = Generalization(general=Entity, specific=pcm_pc_pc_composition_pc_pc_ComposedStructure)
gen_pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingEntity)
gen_pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity_composition_pc_pc_ComposedStructure = Generalization(general=composition_pc_pc_ComposedStructure, specific=pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity)
gen_pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity_entity_pc_pc_InterfaceProvidingRequiringEntity = Generalization(general=entity_pc_pc_InterfaceProvidingRequiringEntity, specific=pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity)
gen_pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingRequiringEntity_entity_pc_pc_ResourceInterfaceRequiringEntity = Generalization(general=entity_pc_pc_ResourceInterfaceRequiringEntity, specific=pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingRequiringEntity_entity_pc_pc_ResourceInterfaceProvidingEntity = Generalization(general=entity_pc_pc_ResourceInterfaceProvidingEntity, specific=pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_pc_pc_entity_pc_pc_Entity_Identifier = Generalization(general=Identifier, specific=pcm_pc_pc_entity_pc_pc_Entity)
gen_pcm_pc_pc_entity_pc_pc_Entity_entity_pc_pc_NamedElement = Generalization(general=entity_pc_pc_NamedElement, specific=pcm_pc_pc_entity_pc_pc_Entity)
gen_pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector_Connector = Generalization(general=Connector, specific=pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector)
gen_pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector_Connector = Generalization(general=Connector, specific=pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector)
gen_pcm_pc_pc_composition_pc_pc_EventChannel_Entity = Generalization(general=Entity, specific=pcm_pc_pc_composition_pc_pc_EventChannel)
gen_pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector)
gen_pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector)
gen_pcm_pc_pc_composition_pc_pc_AssemblyConnector_Connector = Generalization(general=Connector, specific=pcm_pc_pc_composition_pc_pc_AssemblyConnector)
gen_pcm_pc_pc_composition_pc_pc_AssemblyEventConnector_Connector = Generalization(general=Connector, specific=pcm_pc_pc_composition_pc_pc_AssemblyEventConnector)
gen_pcm_pc_pc_composition_pc_pc_SourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_pc_composition_pc_pc_SourceDelegationConnector)
gen_pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector)
gen_pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector)
gen_pcm_pc_pc_composition_pc_pc_AssemblyContext_Entity = Generalization(general=Entity, specific=pcm_pc_pc_composition_pc_pc_AssemblyContext)
gen_pcm_pc_pc_composition_pc_pc_SinkDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_pc_composition_pc_pc_SinkDelegationConnector)
gen_pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector_Connector = Generalization(general=Connector, specific=pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector)
gen_pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector)
gen_pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall)
gen_pcm_pc_pc_usagemodel_pc_pc_UsageScenario_Entity = Generalization(general=Entity, specific=pcm_pc_pc_usagemodel_pc_pc_UsageScenario)
gen_pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction_Entity = Generalization(general=Entity, specific=pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction)
gen_pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour_Entity = Generalization(general=Entity, specific=pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour)
gen_pcm_pc_pc_usagemodel_pc_pc_Stop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_pc_usagemodel_pc_pc_Stop)
gen_pcm_pc_pc_usagemodel_pc_pc_Start_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_pc_usagemodel_pc_pc_Start)
gen_pcm_pc_pc_usagemodel_pc_pc_OpenWorkload_Workload = Generalization(general=Workload, specific=pcm_pc_pc_usagemodel_pc_pc_OpenWorkload)
gen_pcm_pc_pc_usagemodel_pc_pc_Branch_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_pc_usagemodel_pc_pc_Branch)
gen_pcm_pc_pc_usagemodel_pc_pc_Loop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_pc_usagemodel_pc_pc_Loop)
gen_pcm_pc_pc_repository_pc_pc_PassiveResource_Entity = Generalization(general=Entity, specific=pcm_pc_pc_repository_pc_pc_PassiveResource)
gen_pcm_pc_pc_repository_pc_pc_BasicComponent_ImplementationComponentType = Generalization(general=ImplementationComponentType, specific=pcm_pc_pc_repository_pc_pc_BasicComponent)
gen_pcm_pc_pc_usagemodel_pc_pc_Delay_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_pc_usagemodel_pc_pc_Delay)
gen_pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload_Workload = Generalization(general=Workload, specific=pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload)
gen_pcm_pc_pc_repository_pc_pc_ImplementationComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_pc_pc_repository_pc_pc_ImplementationComponentType)
gen_pcm_pc_pc_repository_pc_pc_Repository_Entity = Generalization(general=Entity, specific=pcm_pc_pc_repository_pc_pc_Repository)
gen_pcm_pc_pc_repository_pc_pc_RepositoryComponent_InterfaceProvidingRequiringEntity = Generalization(general=InterfaceProvidingRequiringEntity, specific=pcm_pc_pc_repository_pc_pc_RepositoryComponent)
gen_pcm_pc_pc_repository_pc_pc_ProvidedRole_Role = Generalization(general=Role, specific=pcm_pc_pc_repository_pc_pc_ProvidedRole)
gen_pcm_pc_pc_repository_pc_pc_EventGroup_Interface = Generalization(general=Interface, specific=pcm_pc_pc_repository_pc_pc_EventGroup)
gen_pcm_pc_pc_repository_pc_pc_EventType_Signature = Generalization(general=Signature, specific=pcm_pc_pc_repository_pc_pc_EventType)
gen_pcm_pc_pc_repository_pc_pc_Interface_Entity = Generalization(general=Entity, specific=pcm_pc_pc_repository_pc_pc_Interface)
gen_pcm_pc_pc_repository_pc_pc_RequiredRole_Role = Generalization(general=Role, specific=pcm_pc_pc_repository_pc_pc_RequiredRole)
gen_pcm_pc_pc_repository_pc_pc_OperationSignature_Signature = Generalization(general=Signature, specific=pcm_pc_pc_repository_pc_pc_OperationSignature)
gen_pcm_pc_pc_repository_pc_pc_Signature_Entity = Generalization(general=Entity, specific=pcm_pc_pc_repository_pc_pc_Signature)
gen_pcm_pc_pc_repository_pc_pc_InfrastructureSignature_Signature = Generalization(general=Signature, specific=pcm_pc_pc_repository_pc_pc_InfrastructureSignature)
gen_pcm_pc_pc_repository_pc_pc_InfrastructureInterface_Interface = Generalization(general=Interface, specific=pcm_pc_pc_repository_pc_pc_InfrastructureInterface)
gen_pcm_pc_pc_repository_pc_pc_InfrastructureRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_pc_pc_repository_pc_pc_InfrastructureRequiredRole)
gen_pcm_pc_pc_repository_pc_pc_SourceRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_pc_pc_repository_pc_pc_SourceRole)
gen_pcm_pc_pc_repository_pc_pc_SinkRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_pc_pc_repository_pc_pc_SinkRole)
gen_pcm_pc_pc_repository_pc_pc_OperationProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_pc_pc_repository_pc_pc_OperationProvidedRole)
gen_pcm_pc_pc_repository_pc_pc_InfrastructureProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_pc_pc_repository_pc_pc_InfrastructureProvidedRole)
gen_pcm_pc_pc_repository_pc_pc_OperationInterface_Interface = Generalization(general=Interface, specific=pcm_pc_pc_repository_pc_pc_OperationInterface)
gen_pcm_pc_pc_repository_pc_pc_OperationRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_pc_pc_repository_pc_pc_OperationRequiredRole)
gen_pcm_pc_pc_repository_pc_pc_ProvidesComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_pc_pc_repository_pc_pc_ProvidesComponentType)
gen_pcm_pc_pc_repository_pc_pc_CompositeComponent_entity_pc_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_pc_ComposedProvidingRequiringEntity, specific=pcm_pc_pc_repository_pc_pc_CompositeComponent)
gen_pcm_pc_pc_repository_pc_pc_CompositeComponent_repository_pc_pc_ImplementationComponentType = Generalization(general=repository_pc_pc_ImplementationComponentType, specific=pcm_pc_pc_repository_pc_pc_CompositeComponent)
gen_pcm_pc_pc_repository_pc_pc_CompleteComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_pc_pc_repository_pc_pc_CompleteComponentType)
gen_pcm_pc_pc_repository_pc_pc_InnerDeclaration_NamedElement = Generalization(general=NamedElement, specific=pcm_pc_pc_repository_pc_pc_InnerDeclaration)
gen_pcm_pc_pc_repository_pc_pc_Role_Entity = Generalization(general=Entity, specific=pcm_pc_pc_repository_pc_pc_Role)
gen_pcm_pc_pc_resourcetype_pc_pc_ResourceSignature_Entity = Generalization(general=Entity, specific=pcm_pc_pc_resourcetype_pc_pc_ResourceSignature)
gen_pcm_pc_pc_repository_pc_pc_PrimitiveDataType_DataType = Generalization(general=DataType, specific=pcm_pc_pc_repository_pc_pc_PrimitiveDataType)
gen_pcm_pc_pc_repository_pc_pc_CollectionDataType_entity_pc_pc_Entity = Generalization(general=entity_pc_pc_Entity, specific=pcm_pc_pc_repository_pc_pc_CollectionDataType)
gen_pcm_pc_pc_repository_pc_pc_CollectionDataType_repository_pc_pc_DataType = Generalization(general=repository_pc_pc_DataType, specific=pcm_pc_pc_repository_pc_pc_CollectionDataType)
gen_pcm_pc_pc_repository_pc_pc_CompositeDataType_entity_pc_pc_Entity = Generalization(general=entity_pc_pc_Entity, specific=pcm_pc_pc_repository_pc_pc_CompositeDataType)
gen_pcm_pc_pc_repository_pc_pc_CompositeDataType_repository_pc_pc_DataType = Generalization(general=repository_pc_pc_DataType, specific=pcm_pc_pc_repository_pc_pc_CompositeDataType)
gen_pcm_pc_pc_resourcetype_pc_pc_CommunicationLinkResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_pc_pc_resourcetype_pc_pc_CommunicationLinkResourceType)
gen_pcm_pc_pc_resourcetype_pc_pc_ResourceInterface_Entity = Generalization(general=Entity, specific=pcm_pc_pc_resourcetype_pc_pc_ResourceInterface)
gen_pcm_pc_pc_resourcetype_pc_pc_ProcessingResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_pc_pc_resourcetype_pc_pc_ProcessingResourceType)
gen_pcm_pc_pc_resourcetype_pc_pc_ResourceType_entity_pc_pc_Entity = Generalization(general=entity_pc_pc_Entity, specific=pcm_pc_pc_resourcetype_pc_pc_ResourceType)
gen_pcm_pc_pc_resourcetype_pc_pc_ResourceType_UnitCarryingElement = Generalization(general=UnitCarryingElement, specific=pcm_pc_pc_resourcetype_pc_pc_ResourceType)
gen_pcm_pc_pc_resourcetype_pc_pc_ResourceType_entity_pc_pc_ResourceInterfaceProvidingEntity = Generalization(general=entity_pc_pc_ResourceInterfaceProvidingEntity, specific=pcm_pc_pc_resourcetype_pc_pc_ResourceType)
gen_pcm_pc_pc_resourcetype_pc_pc_SchedulingPolicy_Entity = Generalization(general=Entity, specific=pcm_pc_pc_resourcetype_pc_pc_SchedulingPolicy)
gen_pcm_pc_pc_parameter_pc_pc_CharacterisedVariable_Variable = Generalization(general=Variable, specific=pcm_pc_pc_parameter_pc_pc_CharacterisedVariable)
gen_pcm_pc_pc_reliability_pc_pc_SoftwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_pc_pc_reliability_pc_pc_SoftwareInducedFailureType)
gen_pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription)
gen_pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType)
gen_pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription)
gen_pcm_pc_pc_reliability_pc_pc_ResourceTimeoutFailureType_SoftwareInducedFailureType = Generalization(general=SoftwareInducedFailureType, specific=pcm_pc_pc_reliability_pc_pc_ResourceTimeoutFailureType)
gen_pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType)
gen_pcm_pc_pc_seff_pc_pc_AbstractAction_Entity = Generalization(general=Entity, specific=pcm_pc_pc_seff_pc_pc_AbstractAction)
gen_pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour_Identifier = Generalization(general=Identifier, specific=pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour)
gen_pcm_pc_pc_reliability_pc_pc_FailureType_Entity = Generalization(general=Entity, specific=pcm_pc_pc_reliability_pc_pc_FailureType)
gen_pcm_pc_pc_seff_pc_pc_StopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_pc_pc_StopAction)
gen_pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction_AbstractAction = Generalization(general=AbstractAction, specific=pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction)
gen_pcm_pc_pc_seff_pc_pc_BranchAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_pc_pc_BranchAction)
gen_pcm_pc_pc_seff_pc_pc_AbstractLoopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_pc_pc_AbstractLoopAction)
gen_pcm_pc_pc_seff_pc_pc_AbstractBranchTransition_Entity = Generalization(general=Entity, specific=pcm_pc_pc_seff_pc_pc_AbstractBranchTransition)
gen_pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF_Identifier = Generalization(general=Identifier, specific=pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF)
gen_pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF_seff_pc_pc_ServiceEffectSpecification = Generalization(general=seff_pc_pc_ServiceEffectSpecification, specific=pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF)
gen_pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF_seff_pc_pc_ResourceDemandingBehaviour = Generalization(general=seff_pc_pc_ResourceDemandingBehaviour, specific=pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF)
gen_pcm_pc_pc_seff_pc_pc_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_pc_pc_seff_pc_pc_ResourceDemandingInternalBehaviour)
gen_pcm_pc_pc_seff_pc_pc_ReleaseAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_pc_pc_ReleaseAction)
gen_pcm_pc_pc_seff_pc_pc_LoopAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_pc_pc_seff_pc_pc_LoopAction)
gen_pcm_pc_pc_seff_pc_pc_StartAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_pc_pc_StartAction)
gen_pcm_pc_pc_seff_pc_pc_ExternalCallAction_seff_pc_pc_AbstractAction = Generalization(general=seff_pc_pc_AbstractAction, specific=pcm_pc_pc_seff_pc_pc_ExternalCallAction)
gen_pcm_pc_pc_seff_pc_pc_ExternalCallAction_seff_pc_pc_CallReturnAction = Generalization(general=seff_pc_pc_CallReturnAction, specific=pcm_pc_pc_seff_pc_pc_ExternalCallAction)
gen_pcm_pc_pc_seff_pc_pc_ExternalCallAction_seff_reliability_pc_pc_FailureHandlingEntity = Generalization(general=seff_reliability_pc_pc_FailureHandlingEntity, specific=pcm_pc_pc_seff_pc_pc_ExternalCallAction)
gen_pcm_pc_pc_seff_pc_pc_ForkAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_pc_pc_ForkAction)
gen_pcm_pc_pc_seff_pc_pc_ForkedBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_pc_pc_seff_pc_pc_ForkedBehaviour)
gen_pcm_pc_pc_seff_pc_pc_CollectionIteratorAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_pc_pc_seff_pc_pc_CollectionIteratorAction)
gen_pcm_pc_pc_seff_pc_pc_GuardedBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_pc_pc_seff_pc_pc_GuardedBranchTransition)
gen_pcm_pc_pc_seff_pc_pc_SetVariableAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_pc_pc_SetVariableAction)
gen_pcm_pc_pc_seff_pc_pc_CallReturnAction_CallAction = Generalization(general=CallAction, specific=pcm_pc_pc_seff_pc_pc_CallReturnAction)
gen_pcm_pc_pc_seff_pc_pc_ProbabilisticBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_pc_pc_seff_pc_pc_ProbabilisticBranchTransition)
gen_pcm_pc_pc_seff_pc_pc_AcquireAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_pc_pc_AcquireAction)
gen_pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall_CallAction = Generalization(general=CallAction, specific=pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall)
gen_pcm_pc_pc_seff_pc_pc_InternalCallAction_seff_pc_pc_CallAction = Generalization(general=seff_pc_pc_CallAction, specific=pcm_pc_pc_seff_pc_pc_InternalCallAction)
gen_pcm_pc_pc_seff_pc_pc_InternalCallAction_seff_pc_pc_AbstractInternalControlFlowAction = Generalization(general=seff_pc_pc_AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_pc_pc_InternalCallAction)
gen_pcm_pc_pc_seff_pc_pc_EmitEventAction_seff_pc_pc_AbstractAction = Generalization(general=seff_pc_pc_AbstractAction, specific=pcm_pc_pc_seff_pc_pc_EmitEventAction)
gen_pcm_pc_pc_seff_pc_pc_EmitEventAction_seff_pc_pc_CallAction = Generalization(general=seff_pc_pc_CallAction, specific=pcm_pc_pc_seff_pc_pc_EmitEventAction)
gen_pcm_pc_pc_seff_pc_pc_InternalAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_pc_pc_InternalAction)
gen_pcm_pc_pc_seff_performance_pc_pc_ResourceCall_CallAction = Generalization(general=CallAction, specific=pcm_pc_pc_seff_performance_pc_pc_ResourceCall)
gen_pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour_seff_reliability_pc_pc_FailureHandlingEntity = Generalization(general=seff_reliability_pc_pc_FailureHandlingEntity, specific=pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour)
gen_pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour_seff_pc_pc_ResourceDemandingBehaviour = Generalization(general=seff_pc_pc_ResourceDemandingBehaviour, specific=pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour)
gen_pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations_Entity = Generalization(general=Entity, specific=pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations)
gen_pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction)
gen_pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity_Entity = Generalization(general=Entity, specific=pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity)
gen_pcm_pc_pc_qos_performance_pc_pc_SpecifiedExecutionTime_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_pc_pc_qos_performance_pc_pc_SpecifiedExecutionTime)
gen_pcm_pc_pc_qos_performance_pc_pc_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_pc_pc_qos_performance_pc_pc_ComponentSpecifiedExecutionTime)
gen_pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation)
gen_pcm_pc_pc_qos_performance_pc_pc_SystemSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_pc_pc_qos_performance_pc_pc_SystemSpecifiedExecutionTime)
gen_pcm_pc_pc_system_pc_pc_System_entity_pc_pc_Entity = Generalization(general=entity_pc_pc_Entity, specific=pcm_pc_pc_system_pc_pc_System)
gen_pcm_pc_pc_system_pc_pc_System_entity_pc_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_pc_ComposedProvidingRequiringEntity, specific=pcm_pc_pc_system_pc_pc_System)
gen_pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification)
gen_pcm_pc_pc_resourceenvironment_pc_pc_ResourceEnvironment_NamedElement = Generalization(general=NamedElement, specific=pcm_pc_pc_resourceenvironment_pc_pc_ResourceEnvironment)
gen_pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource_Entity = Generalization(general=Entity, specific=pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource)
gen_pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer_Entity = Generalization(general=Entity, specific=pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer)
gen_pcm_pc_pc_allocation_pc_pc_AllocationContext_Entity = Generalization(general=Entity, specific=pcm_pc_pc_allocation_pc_pc_AllocationContext)
gen_pcm_pc_pc_allocation_pc_pc_Allocation_Entity = Generalization(general=Entity, specific=pcm_pc_pc_allocation_pc_pc_Allocation)
gen_pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification)
gen_pcm_pc_pc_subsystem_pc_pc_SubSystem_entity_pc_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_pc_ComposedProvidingRequiringEntity, specific=pcm_pc_pc_subsystem_pc_pc_SubSystem)
gen_pcm_pc_pc_subsystem_pc_pc_SubSystem_repository_pc_pc_RepositoryComponent = Generalization(general=repository_pc_pc_RepositoryComponent, specific=pcm_pc_pc_subsystem_pc_pc_SubSystem)
gen_pcm_pc_pc_completions_pc_pc_Completion_entity_pc_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_pc_ComposedProvidingRequiringEntity, specific=pcm_pc_pc_completions_pc_pc_Completion)
gen_pcm_pc_pc_completions_pc_pc_Completion_repository_pc_pc_ImplementationComponentType = Generalization(general=repository_pc_pc_ImplementationComponentType, specific=pcm_pc_pc_completions_pc_pc_Completion)
gen_pcm_pc_pc_completions_pc_pc_DelegatingExternalCallAction_ExternalCallAction = Generalization(general=ExternalCallAction, specific=pcm_pc_pc_completions_pc_pc_DelegatingExternalCallAction)
gen_pcm_pc_pc_completions_pc_pc_NetworkDemandParametricResourceDemand_ParametricResourceDemand = Generalization(general=ParametricResourceDemand, specific=pcm_pc_pc_completions_pc_pc_NetworkDemandParametricResourceDemand)

# Domain Model
domain_model = DomainModel(
    name="pcm_pc_pc",
    types={pcm_pc_pc_DummyClass, pcm_pc_pc_PointcutPointcut, pcm_pc_pc_EObject, pcm_pc_pc_Pointcut, seff_performance_pc_pc_ResourceCall, seff_performance_pc_pc_ParametricResourceDemand, LoopAction, GuardedBranchTransition, qos_performance_pc_pc_SpecifiedExecutionTime, composition_pc_pc_EventChannelSinkConnector, composition_pc_pc_AssemblyEventConnector, pcm_pc_pc_core_pc_pc_PCMRandomVariable, RandomVariable, ClosedWorkload, PassiveResource, VariableCharacterisation, seff_performance_pc_pc_InfrastructureCall, pcm_pc_pc_entity_pc_pc_InterfaceProvidingEntity, Entity, ProvidedRole, pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity, entity_pc_pc_Entity, entity_pc_pc_ResourceInterfaceRequiringEntity, RequiredRole, pcm_pc_pc_entity_pc_pc_ResourceInterfaceRequiringEntity, entity_pc_pc_ResourceRequiredRole, pcm_pc_pc_entity_pc_pc_ResourceRequiredRole, Loop, OpenWorkload, Delay, CommunicationLinkResourceSpecification, ProcessingResourceSpecification, pcm_pc_pc_entity_pc_pc_ResourceProvidedRole, Role, entity_pc_pc_ResourceInterfaceProvidingEntity, ResourceInterface, pcm_pc_pc_entity_pc_pc_InterfaceProvidingRequiringEntity, entity_pc_pc_InterfaceProvidingEntity, entity_pc_pc_InterfaceRequiringEntity, pcm_pc_pc_composition_pc_pc_DelegationConnector, Connector, pcm_pc_pc_composition_pc_pc_Connector, pcm_pc_pc_composition_pc_pc_ComposedStructure, pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingEntity, entity_pc_pc_ResourceProvidedRole, pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity, composition_pc_pc_ComposedStructure, entity_pc_pc_InterfaceProvidingRequiringEntity, pcm_pc_pc_entity_pc_pc_NamedElement, pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingRequiringEntity, pcm_pc_pc_entity_pc_pc_Entity, Identifier, entity_pc_pc_NamedElement, pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector, SourceRole, pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector, SinkRole, PCMRandomVariable, composition_pc_pc_AssemblyContext, composition_pc_pc_ResourceRequiredDelegationConnector, composition_pc_pc_EventChannel, composition_pc_pc_Connector, pcm_pc_pc_composition_pc_pc_ResourceRequiredDelegationConnector, pcm_pc_pc_composition_pc_pc_EventChannel, EventGroup, composition_pc_pc_EventChannelSourceConnector, OperationRequiredRole, pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector, DelegationConnector, OperationProvidedRole, pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector, pcm_pc_pc_composition_pc_pc_AssemblyConnector, pcm_pc_pc_composition_pc_pc_AssemblyEventConnector, pcm_pc_pc_composition_pc_pc_SourceDelegationConnector, pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector, pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector, pcm_pc_pc_composition_pc_pc_AssemblyContext, pcm_pc_pc_composition_pc_pc_SinkDelegationConnector, pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector, InfrastructureProvidedRole, InfrastructureRequiredRole, pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector, pcm_pc_pc_usagemodel_pc_pc_UsageModel, UserData, pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall, AbstractUserAction, RepositoryComponent, VariableUsage, pcm_pc_pc_usagemodel_pc_pc_Workload, UsageScenario, pcm_pc_pc_usagemodel_pc_pc_UsageScenario, UsageModel, ScenarioBehaviour, Workload, pcm_pc_pc_usagemodel_pc_pc_UserData, BranchTransition, OperationSignature, pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction, pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour, pcm_pc_pc_usagemodel_pc_pc_Stop, pcm_pc_pc_usagemodel_pc_pc_Start, pcm_pc_pc_usagemodel_pc_pc_OpenWorkload, pcm_pc_pc_usagemodel_pc_pc_BranchTransition, Branch, pcm_pc_pc_usagemodel_pc_pc_Branch, pcm_pc_pc_usagemodel_pc_pc_Loop, pcm_pc_pc_repository_pc_pc_PassiveResource, BasicComponent, ResourceTimeoutFailureType, pcm_pc_pc_repository_pc_pc_BasicComponent, ImplementationComponentType, pcm_pc_pc_usagemodel_pc_pc_Delay, pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload, CompleteComponentType, ServiceEffectSpecification, pcm_pc_pc_repository_pc_pc_ImplementationComponentType, ResourceSignature, pcm_pc_pc_repository_pc_pc_DataType, pcm_pc_pc_repository_pc_pc_Repository, Interface, pcm_pc_pc_repository_pc_pc_RepositoryComponent, InterfaceProvidingRequiringEntity, Repository, pcm_pc_pc_repository_pc_pc_ProvidedRole, pcm_pc_pc_repository_pc_pc_Parameter, DataType, InfrastructureSignature, EventType, pcm_pc_pc_repository_pc_pc_RequiredCharacterisation, Parameter_, pcm_pc_pc_repository_pc_pc_EventGroup, pcm_pc_pc_repository_pc_pc_EventType, Signature, FailureType, pcm_pc_pc_repository_pc_pc_Interface, Protocol, RequiredCharacterisation, pcm_pc_pc_repository_pc_pc_RequiredRole, pcm_pc_pc_repository_pc_pc_OperationSignature, OperationInterface, pcm_pc_pc_repository_pc_pc_Signature, ExceptionType, pcm_pc_pc_repository_pc_pc_ExceptionType, pcm_pc_pc_repository_pc_pc_InfrastructureSignature, InfrastructureInterface, pcm_pc_pc_repository_pc_pc_InfrastructureInterface, pcm_pc_pc_repository_pc_pc_InfrastructureRequiredRole, pcm_pc_pc_repository_pc_pc_SourceRole, pcm_pc_pc_repository_pc_pc_SinkRole, pcm_pc_pc_repository_pc_pc_OperationProvidedRole, pcm_pc_pc_repository_pc_pc_InfrastructureProvidedRole, pcm_pc_pc_repository_pc_pc_OperationInterface, pcm_pc_pc_repository_pc_pc_OperationRequiredRole, pcm_pc_pc_repository_pc_pc_ProvidesComponentType, pcm_pc_pc_repository_pc_pc_CompositeComponent, entity_pc_pc_ComposedProvidingRequiringEntity, repository_pc_pc_ImplementationComponentType, pcm_pc_pc_repository_pc_pc_CompleteComponentType, ProvidesComponentType, InnerDeclaration, pcm_pc_pc_repository_pc_pc_InnerDeclaration, NamedElement, pcm_pc_pc_repository_pc_pc_Role, pcm_pc_pc_resourcetype_pc_pc_ResourceSignature, pcm_pc_pc_repository_pc_pc_PrimitiveDataType, pcm_pc_pc_repository_pc_pc_CollectionDataType, repository_pc_pc_DataType, pcm_pc_pc_repository_pc_pc_CompositeDataType, CompositeDataType, pcm_pc_pc_resourcetype_pc_pc_CommunicationLinkResourceType, NetworkInducedFailureType, pcm_pc_pc_resourcetype_pc_pc_ResourceInterface, pcm_pc_pc_protocol_pc_pc_Protocol, pcm_pc_pc_parameter_pc_pc_VariableUsage, pcm_pc_pc_resourcetype_pc_pc_ProcessingResourceType, ResourceType, HardwareInducedFailureType, pcm_pc_pc_resourcetype_pc_pc_ResourceType, UnitCarryingElement, ResourceRepository, pcm_pc_pc_resourcetype_pc_pc_ResourceRepository, SchedulingPolicy, pcm_pc_pc_resourcetype_pc_pc_SchedulingPolicy, pcm_pc_pc_parameter_pc_pc_VariableCharacterisation, pcm_pc_pc_parameter_pc_pc_CharacterisedVariable, Variable, CallAction, SynchronisationPoint, CallReturnAction, SetVariableAction, SpecifiedOutputParameterAbstraction, EntryLevelSystemCall, parameter_pc_pc_pcm_pc_pc_AbstractNamedReference, ProcessingResourceType, pcm_pc_pc_reliability_pc_pc_SoftwareInducedFailureType, InternalFailureOccurrenceDescription, pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription, FailureOccurrenceDescription, pcm_pc_pc_reliability_pc_pc_FailureOccurrenceDescription, pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType, CommunicationLinkResourceType, pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription, qos_reliability_pc_pc_SpecifiedReliabilityAnnotation, pcm_pc_pc_reliability_pc_pc_ResourceTimeoutFailureType, InternalAction, SoftwareInducedFailureType, pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType, pcm_pc_pc_seff_pc_pc_AbstractAction, ResourceDemandingBehaviour, pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour, pcm_pc_pc_reliability_pc_pc_FailureType, pcm_pc_pc_seff_pc_pc_StopAction, AbstractInternalControlFlowAction, pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction, AbstractAction, BranchAction, pcm_pc_pc_seff_pc_pc_BranchAction, pcm_pc_pc_seff_pc_pc_CallAction, AbstractLoopAction, AbstractBranchTransition, pcm_pc_pc_seff_pc_pc_AbstractLoopAction, pcm_pc_pc_seff_pc_pc_AbstractBranchTransition, pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF, seff_pc_pc_ServiceEffectSpecification, seff_pc_pc_ResourceDemandingBehaviour, ResourceDemandingInternalBehaviour, pcm_pc_pc_seff_pc_pc_ResourceDemandingInternalBehaviour, ResourceDemandingSEFF, pcm_pc_pc_seff_pc_pc_ReleaseAction, pcm_pc_pc_seff_pc_pc_LoopAction, pcm_pc_pc_seff_pc_pc_StartAction, pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification, pcm_pc_pc_seff_pc_pc_ExternalCallAction, seff_pc_pc_AbstractAction, seff_pc_pc_CallReturnAction, seff_reliability_pc_pc_FailureHandlingEntity, pcm_pc_pc_seff_pc_pc_ForkAction, ForkedBehaviour, pcm_pc_pc_seff_pc_pc_ForkedBehaviour, ForkAction, pcm_pc_pc_seff_pc_pc_SynchronisationPoint, pcm_pc_pc_seff_pc_pc_CollectionIteratorAction, pcm_pc_pc_seff_pc_pc_GuardedBranchTransition, pcm_pc_pc_seff_pc_pc_SetVariableAction, pcm_pc_pc_seff_pc_pc_CallReturnAction, pcm_pc_pc_seff_pc_pc_ProbabilisticBranchTransition, pcm_pc_pc_seff_pc_pc_AcquireAction, pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall, pcm_pc_pc_seff_pc_pc_InternalCallAction, seff_pc_pc_CallAction, seff_pc_pc_AbstractInternalControlFlowAction, pcm_pc_pc_seff_pc_pc_EmitEventAction, pcm_pc_pc_seff_pc_pc_InternalAction, pcm_pc_pc_seff_performance_pc_pc_ResourceCall, pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour, seff_reliability_pc_pc_RecoveryActionBehaviour, pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand, pcm_pc_pc_qosannotations_pc_pc_SpecifiedQoSAnnotation, QoSAnnotations, pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations, seff_reliability_pc_pc_RecoveryAction, pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction, pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity, pcm_pc_pc_qos_performance_pc_pc_SpecifiedExecutionTime, pcm_pc_pc_qos_performance_pc_pc_ComponentSpecifiedExecutionTime, pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation, System, SpecifiedQoSAnnotation, pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction, pcm_pc_pc_qos_performance_pc_pc_SystemSpecifiedExecutionTime, SpecifiedExecutionTime, ExternalFailureOccurrenceDescription, pcm_pc_pc_system_pc_pc_System, pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification, pcm_pc_pc_resourceenvironment_pc_pc_ResourceEnvironment, LinkingResource, ResourceContainer, pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource, ResourceEnvironment, pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer, pcm_pc_pc_allocation_pc_pc_AllocationContext, Allocation, pcm_pc_pc_allocation_pc_pc_Allocation, pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification, pcm_pc_pc_subsystem_pc_pc_SubSystem, repository_pc_pc_RepositoryComponent, pcm_pc_pc_completions_pc_pc_Completion, pcm_pc_pc_completions_pc_pc_CompletionRepository, Completion, pcm_pc_pc_completions_pc_pc_DelegatingExternalCallAction, ExternalCallAction, pcm_pc_pc_completions_pc_pc_NetworkDemandParametricResourceDemand, ParametricResourceDemand, AllocationContext, ComponentType, ParameterModifier, PrimitiveTypeEnum, VariableCharacterisationType},
    associations={children0, resourceCall__PCMRandomVariable7, parametricResourceDemand_PCMRandomVariable10, loopAction_PCMRandomVariable13, guardedBranchTransition_PCMRandomVariable15, specifiedExecutionTime_PCMRandomVariable17, eventChannelSinkConnector__FilterCondition18, assemblyEventConnector__FilterCondition19, children1, closedWorkload_PCMRandomVariable3, passiveResource_capacity_PCMRandomVariable4, variableCharacterisation_Specification5, infrastructureCall__PCMRandomVariable6, providedRoles_InterfaceProvidingEntity37, requiredRoles_InterfaceRequiringEntity39, resourceRequiredRoles__ResourceInterfaceRequiringEntity41, loop_LoopIteration22, openWorkload_PCMRandomVariable24, delay_TimeSpecification26, communicationLinkResourceSpecifcation_throughput_PCMRandomVariable28, processingResourceSpecification_processingRate_PCMRandomVariable29, communicationLinkResourceSpecification_latency_PCMRandomVariable31, resourceInterfaceProvidingEntity__ResourceProvidedRole34, providedResourceInterface__ResourceProvidedRole36, parentStructure__Connector52, requiredResourceInterface__ResourceRequiredRole44, resourceInterfaceRequiringEntity__ResourceRequiredRole46, resourceProvidedRoles__ResourceInterfaceProvidingEntity49, parentStructure__EventChannel81, sourceRole__EventChannelSourceRole84, assemblyContext__EventChannelSourceConnector85, eventChannel__EventChannelSourceConnector87, sinkRole__EventChannelSinkConnector90, filterCondition__EventChannelSinkConnector91, assemblyContext__EventChannelSinkConnector93, eventChannel__EventChannelSinkConnector96, assemblyContexts__ComposedStructure55, resourceRequiredDelegationConnectors_ComposedStructure58, eventChannel__ComposedStructure61, connectors__ComposedStructure64, innerResourceRequiredRole_ResourceRequiredDelegationConnector67, outerResourceRequiredRole_ResourceRequiredDelegationConnector68, parentStructure_ResourceRequiredDelegationConnector71, eventGroup__EventChannel74, eventChannelSourceConnector__EventChannel75, eventChannelSinkConnector__EventChannel78, innerRequiredRole_RequiredDelegationConnector106, outerRequiredRole_RequiredDelegationConnector107, innerProvidedRole_ProvidedDelegationConnector99, outerProvidedRole_ProvidedDelegationConnector100, assemblyContext_ProvidedDelegationConnector103, assemblyContext_RequiredDelegationConnector110, requiredRole_AssemblyConnector121, sinkRole__AssemblyEventConnector124, sourceRole__AssemblyEventConnector126, sinkAssemblyContext__AssemblyEventConnector129, sourceAssemblyContext__AssemblyEventConnector132, filterCondition__AssemblyEventConnector135, innerSourceRole__SourceRole138, outerSourceRole__SourceRole140, requiringAssemblyContext_AssemblyConnector113, providingAssemblyContext_AssemblyConnector115, providedRole_AssemblyConnector118, assemblyContext__ProvidedInfrastructureDelegationConnector168, innerRequiredRole__RequiredInfrastructureDelegationConnector171, outerRequiredRole__RequiredInfrastructureDelegationConnector173, assemblyContext__RequiredInfrastructureDelegationConnector176, assemblyContext__RequiredResourceDelegationConnector179, innerRequiredRole__RequiredResourceDelegationConnector181, outerRequiredRole__RequiredResourceDelegationConnector184, assemblyContext__SourceDelegationConnector143, assemblyContext__SinkDelegationConnector146, innerSinkRole__SinkRole148, outerSinkRole__SinkRole151, providedRole__AssemblyInfrastructureConnector154, requiredRole__AssemblyInfrastructureConnector155, providingAssemblyContext__AssemblyInfrastructureConnector157, requiringAssemblyContext__AssemblyInfrastructureConnector160, innerProvidedRole__ProvidedInfrastructureDelegationConnector163, outerProvidedRole__ProvidedInfrastructureDelegationConnector165, userDataParameterUsages_UserData206, usageScenario_UsageModel209, userData_UsageModel212, parentStructure__AssemblyContext187, encapsulatedComponent__AssemblyContext190, configParameterUsages__AssemblyContext191, usageScenario_Workload193, usageModel_UsageScenario195, scenarioBehaviour_UsageScenario197, workload_UsageScenario199, assemblyContext_userData201, usageModel_UserData203, usageScenario_SenarioBehaviour232, branchTransition_ScenarioBehaviour235, providedRole_EntryLevelSystemCall214, operationSignature__EntryLevelSystemCall216, outputParameterUsages_EntryLevelSystemCall218, inputParameterUsages_EntryLevelSystemCall221, successor224, predecessor226, scenarioBehaviour_AbstractUserAction229, loop_ScenarioBehaviour237, actions_ScenarioBehaviour240, branch_BranchTransition243, branchedBehaviour_BranchTransition245, branchTransitions_Branch248, loopIteration_Loop251, bodyBehaviour_Loop254, thinkTime_ClosedWorkload263, capacity_PassiveResource266, basicComponent_PassiveResource269, resourceTimeoutFailureType__PassiveResource271, interArrivalTime_OpenWorkload257, timeSpecification_Delay260, parentCompleteComponentTypes277, serviceEffectSpecifications__BasicComponent272, passiveResource_BasicComponent274, resourceSignature__Parameter294, repository__DataType295, components__Repository298, interfaces__Repository301, componentParameterUsage_ImplementationComponentType278, repository__RepositoryComponent281, providingEntity_ProvidedRole283, dataType__Parameter286, infrastructureSignature__Parameter287, operationSignature__Parameter289, eventType__Parameter292, repository__Interface314, parameter317, interface_RequiredCharacterisation318, eventTypes__EventGroup321, parameter__EventType324, eventGroup__EventType327, failureTypes__Repository303, dataTypes__Repository305, parentInterfaces__Interface308, protocols__Interface310, requiredCharacterisations312, requiringEntity_RequiredRole344, interface__OperationSignature347, parameters__OperationSignature349, exceptions__Signature330, failureType331, parameters__InfrastructureSignature334, infrastructureInterface__InfrastructureSignature337, infrastructureSignatures__InfrastructureInterface339, requiredInterface__InfrastructureRequiredRole342, eventGroup__SourceRole359, eventGroup__SinkRole361, providedInterface__OperationProvidedRole363, returnType__OperationSignature352, signatures__OperationInterface354, requiredInterface__OperationRequiredRole357, providedInterface__InfrastructureProvidedRole365, parentProvidesComponentTypes367, innerDeclaration_CompositeDataType371, datatype_InnerDeclaration373, compositeDataType_InnerDeclaration375, innerType_CollectionDataType368, parentType_CompositeDataType370, networkInducedFailureType__CommunicationLinkResourceType398, resourceRepository__ResourceInterface400, resourceSignatures__ResourceInterface403, parameter__ResourceSignature378, resourceInterface__ResourceSignature381, hardwareInducedFailureType__ProcessingResourceType384, resourceRepository_ResourceType386, resourceInterfaces__ResourceRepository388, schedulingPolicies__ResourceRepository391, availableResourceTypes_ResourceRepository393, resourceRepository__SchedulingPolicy395, namedReference__VariableUsage430, specification_VariableCharacterisation431, variableUsage_VariableCharacterisation434, variableCharacterisation_VariableUsage406, userData_VariableUsage409, callAction__VariableUsage412, synchronisationPoint_VariableUsage414, callReturnAction__VariableUsage416, setVariableAction_VariableUsage418, specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage420, assemblyContext__VariableUsage422, entryLevelSystemCall_InputParameterUsage425, entryLevelSystemCall_OutputParameterUsage427, processingResourceType__HardwareInducedFailureType437, internalFailureOccurrenceDescriptions__SoftwareInducedFailureType439, communicationLinkResourceType__NetworkInducedFailureType445, specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription447, failureType__ExternalFailureOccurrenceDescription449, passiveResource__ResourceTimeoutFailureType451, internalAction__InternalFailureOccurrenceDescription441, softwareInducedFailureType__InternalFailureOccurrenceDescription443, resourceCall__Action463, predecessor_AbstractAction466, successor_AbstractAction468, resourceDemandingBehaviour_AbstractAction471, repository__FailureType454, resourceDemand_Action457, infrastructureCall__Action460, branchAction_AbstractBranchTransition483, branchBehaviour_BranchTransition485, branches_Branch488, abstractLoopAction_ResourceDemandingBehaviour473, abstractBranchTransition_ResourceDemandingBehaviour475, steps_Behaviour477, bodyBehaviour_Loop480, describedService__SEFF494, basicComponent_ServiceEffectSpecification495, resourceDemandingInternalBehaviours498, resourceDemandingSEFF_ResourceDemandingInternalBehaviour500, passiveResource_ReleaseAction502, inputVariableUsages__CallAction491, outputParameterUsage_SynchronisationPoint517, forkAction_SynchronisationPoint520, synchronousForkedBehaviours_SynchronisationPoint523, calledService_ExternalService526, iterationCount_LoopAction504, asynchronousForkedBehaviours_ForkAction507, synchronisingBehaviours_ForkAction509, synchronisationPoint_ForkedBehaviour512, forkAction_ForkedBehaivour515, passiveresource_AcquireAction534, parameter_CollectionIteratorAction536, branchCondition_GuardedBranchTransition538, role_ExternalService528, returnVariableUsage__CallReturnAction531, internalFailureOccurrenceDescriptions__InternalAction551, localVariableUsages_SetVariableAction541, calledResourceDemandingInternalBehaviour544, eventType__EmitEventAction546, sourceRole__EmitEventAction548, requiredRole__InfrastructureCall561, signature__InfrastructureCall554, numberOfCalls__InfrastructureCall556, action__InfrastructureCall559, failureHandlingAlternatives__RecoveryActionBehaviour583, action__ResourceCall564, resourceRequiredRole__ResourceCall567, signature__ResourceCall569, numberOfCalls__ResourceCall572, specification_ParametericResourceDemand575, requiredResource_ParametricResourceDemand578, action_ParametricResourceDemand580, failureTypes_FailureHandlingEntity591, signature_SpecifiedQoSAnnation593, role_SpecifiedQoSAnnotation595, qosAnnotations_SpecifiedQoSAnnotation597, specifiedOutputParameterAbstractions_QoSAnnotations599, recoveryAction__RecoveryActionBehaviour584, primaryBehaviour__RecoveryAction586, recoveryActionBehaviours__RecoveryAction588, specification_SpecifiedExecutionTime616, assemblyContext_ComponentSpecifiedExecutionTime619, system_QoSAnnotations602, specifiedQoSAnnotations_QoSAnnotations603, signature_SpecifiedOutputParameterAbstraction605, role_SpecifiedOutputParameterAbstraction607, expectedExternalOutputs_SpecifiedOutputParameterAbstraction610, qosAnnotations_SpecifiedOutputParameterAbstraction613, externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation621, qosAnnotations_System623, activeResourceSpecifications_ResourceContainer637, resourceEnvironment_ResourceContainer640, nestedResourceContainers__ResourceContainer643, parentResourceContainer__ResourceContainer646, schedulingPolicy649, linkingResources__ResourceEnvironment626, resourceContainer_ResourceEnvironment628, connectedResourceContainers_LinkingResource630, communicationLinkResourceSpecifications_LinkingResource632, resourceEnvironment_LinkingResource635, resourceContainer_AllocationContext671, assemblyContext_AllocationContext673, allocation_AllocationContext676, eventChannel__AllocationContext677, activeResourceType_ActiveResourceSpecification651, processingRate_ProcessingResourceSpecification654, resourceContainer_ProcessingResourceSpecification657, linkingResource_CommunicationLinkResourceSpecification660, communicationLinkResourceType_CommunicationLinkResourceSpecification663, latency_CommunicationLinkResourceSpecification665, throughput_CommunicationLinkResourceSpecification668, completions_CompletionRepository686, requiredCommunicationLinkResource_ParametricResourceDemand687, targetResourceEnvironment_Allocation679, system_Allocation681, allocationContexts_Allocation684},
    generalizations={gen_pcm_pc_pc_core_pc_pc_PCMRandomVariable_RandomVariable, gen_pcm_pc_pc_entity_pc_pc_InterfaceProvidingEntity_Entity, gen_pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity_entity_pc_pc_Entity, gen_pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity_entity_pc_pc_ResourceInterfaceRequiringEntity, gen_pcm_pc_pc_entity_pc_pc_ResourceInterfaceRequiringEntity_Entity, gen_pcm_pc_pc_entity_pc_pc_ResourceRequiredRole_Role, gen_pcm_pc_pc_entity_pc_pc_ResourceProvidedRole_Role, gen_pcm_pc_pc_entity_pc_pc_InterfaceProvidingRequiringEntity_entity_pc_pc_InterfaceProvidingEntity, gen_pcm_pc_pc_entity_pc_pc_InterfaceProvidingRequiringEntity_entity_pc_pc_InterfaceRequiringEntity, gen_pcm_pc_pc_composition_pc_pc_DelegationConnector_Connector, gen_pcm_pc_pc_composition_pc_pc_Connector_Entity, gen_pcm_pc_pc_composition_pc_pc_ComposedStructure_Entity, gen_pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingEntity_Entity, gen_pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity_composition_pc_pc_ComposedStructure, gen_pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity_entity_pc_pc_InterfaceProvidingRequiringEntity, gen_pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingRequiringEntity_entity_pc_pc_ResourceInterfaceRequiringEntity, gen_pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingRequiringEntity_entity_pc_pc_ResourceInterfaceProvidingEntity, gen_pcm_pc_pc_entity_pc_pc_Entity_Identifier, gen_pcm_pc_pc_entity_pc_pc_Entity_entity_pc_pc_NamedElement, gen_pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector_Connector, gen_pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector_Connector, gen_pcm_pc_pc_composition_pc_pc_EventChannel_Entity, gen_pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector_DelegationConnector, gen_pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector_DelegationConnector, gen_pcm_pc_pc_composition_pc_pc_AssemblyConnector_Connector, gen_pcm_pc_pc_composition_pc_pc_AssemblyEventConnector_Connector, gen_pcm_pc_pc_composition_pc_pc_SourceDelegationConnector_DelegationConnector, gen_pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector_DelegationConnector, gen_pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector_DelegationConnector, gen_pcm_pc_pc_composition_pc_pc_AssemblyContext_Entity, gen_pcm_pc_pc_composition_pc_pc_SinkDelegationConnector_DelegationConnector, gen_pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector_Connector, gen_pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector_DelegationConnector, gen_pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall_AbstractUserAction, gen_pcm_pc_pc_usagemodel_pc_pc_UsageScenario_Entity, gen_pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction_Entity, gen_pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour_Entity, gen_pcm_pc_pc_usagemodel_pc_pc_Stop_AbstractUserAction, gen_pcm_pc_pc_usagemodel_pc_pc_Start_AbstractUserAction, gen_pcm_pc_pc_usagemodel_pc_pc_OpenWorkload_Workload, gen_pcm_pc_pc_usagemodel_pc_pc_Branch_AbstractUserAction, gen_pcm_pc_pc_usagemodel_pc_pc_Loop_AbstractUserAction, gen_pcm_pc_pc_repository_pc_pc_PassiveResource_Entity, gen_pcm_pc_pc_repository_pc_pc_BasicComponent_ImplementationComponentType, gen_pcm_pc_pc_usagemodel_pc_pc_Delay_AbstractUserAction, gen_pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload_Workload, gen_pcm_pc_pc_repository_pc_pc_ImplementationComponentType_RepositoryComponent, gen_pcm_pc_pc_repository_pc_pc_Repository_Entity, gen_pcm_pc_pc_repository_pc_pc_RepositoryComponent_InterfaceProvidingRequiringEntity, gen_pcm_pc_pc_repository_pc_pc_ProvidedRole_Role, gen_pcm_pc_pc_repository_pc_pc_EventGroup_Interface, gen_pcm_pc_pc_repository_pc_pc_EventType_Signature, gen_pcm_pc_pc_repository_pc_pc_Interface_Entity, gen_pcm_pc_pc_repository_pc_pc_RequiredRole_Role, gen_pcm_pc_pc_repository_pc_pc_OperationSignature_Signature, gen_pcm_pc_pc_repository_pc_pc_Signature_Entity, gen_pcm_pc_pc_repository_pc_pc_InfrastructureSignature_Signature, gen_pcm_pc_pc_repository_pc_pc_InfrastructureInterface_Interface, gen_pcm_pc_pc_repository_pc_pc_InfrastructureRequiredRole_RequiredRole, gen_pcm_pc_pc_repository_pc_pc_SourceRole_RequiredRole, gen_pcm_pc_pc_repository_pc_pc_SinkRole_ProvidedRole, gen_pcm_pc_pc_repository_pc_pc_OperationProvidedRole_ProvidedRole, gen_pcm_pc_pc_repository_pc_pc_InfrastructureProvidedRole_ProvidedRole, gen_pcm_pc_pc_repository_pc_pc_OperationInterface_Interface, gen_pcm_pc_pc_repository_pc_pc_OperationRequiredRole_RequiredRole, gen_pcm_pc_pc_repository_pc_pc_ProvidesComponentType_RepositoryComponent, gen_pcm_pc_pc_repository_pc_pc_CompositeComponent_entity_pc_pc_ComposedProvidingRequiringEntity, gen_pcm_pc_pc_repository_pc_pc_CompositeComponent_repository_pc_pc_ImplementationComponentType, gen_pcm_pc_pc_repository_pc_pc_CompleteComponentType_RepositoryComponent, gen_pcm_pc_pc_repository_pc_pc_InnerDeclaration_NamedElement, gen_pcm_pc_pc_repository_pc_pc_Role_Entity, gen_pcm_pc_pc_resourcetype_pc_pc_ResourceSignature_Entity, gen_pcm_pc_pc_repository_pc_pc_PrimitiveDataType_DataType, gen_pcm_pc_pc_repository_pc_pc_CollectionDataType_entity_pc_pc_Entity, gen_pcm_pc_pc_repository_pc_pc_CollectionDataType_repository_pc_pc_DataType, gen_pcm_pc_pc_repository_pc_pc_CompositeDataType_entity_pc_pc_Entity, gen_pcm_pc_pc_repository_pc_pc_CompositeDataType_repository_pc_pc_DataType, gen_pcm_pc_pc_resourcetype_pc_pc_CommunicationLinkResourceType_ResourceType, gen_pcm_pc_pc_resourcetype_pc_pc_ResourceInterface_Entity, gen_pcm_pc_pc_resourcetype_pc_pc_ProcessingResourceType_ResourceType, gen_pcm_pc_pc_resourcetype_pc_pc_ResourceType_entity_pc_pc_Entity, gen_pcm_pc_pc_resourcetype_pc_pc_ResourceType_UnitCarryingElement, gen_pcm_pc_pc_resourcetype_pc_pc_ResourceType_entity_pc_pc_ResourceInterfaceProvidingEntity, gen_pcm_pc_pc_resourcetype_pc_pc_SchedulingPolicy_Entity, gen_pcm_pc_pc_parameter_pc_pc_CharacterisedVariable_Variable, gen_pcm_pc_pc_reliability_pc_pc_SoftwareInducedFailureType_FailureType, gen_pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType_FailureType, gen_pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_pc_pc_reliability_pc_pc_ResourceTimeoutFailureType_SoftwareInducedFailureType, gen_pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType_FailureType, gen_pcm_pc_pc_seff_pc_pc_AbstractAction_Entity, gen_pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour_Identifier, gen_pcm_pc_pc_reliability_pc_pc_FailureType_Entity, gen_pcm_pc_pc_seff_pc_pc_StopAction_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction_AbstractAction, gen_pcm_pc_pc_seff_pc_pc_BranchAction_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_pc_pc_AbstractLoopAction_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_pc_pc_AbstractBranchTransition_Entity, gen_pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF_Identifier, gen_pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF_seff_pc_pc_ServiceEffectSpecification, gen_pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF_seff_pc_pc_ResourceDemandingBehaviour, gen_pcm_pc_pc_seff_pc_pc_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour, gen_pcm_pc_pc_seff_pc_pc_ReleaseAction_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_pc_pc_LoopAction_AbstractLoopAction, gen_pcm_pc_pc_seff_pc_pc_StartAction_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_pc_pc_ExternalCallAction_seff_pc_pc_AbstractAction, gen_pcm_pc_pc_seff_pc_pc_ExternalCallAction_seff_pc_pc_CallReturnAction, gen_pcm_pc_pc_seff_pc_pc_ExternalCallAction_seff_reliability_pc_pc_FailureHandlingEntity, gen_pcm_pc_pc_seff_pc_pc_ForkAction_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_pc_pc_ForkedBehaviour_ResourceDemandingBehaviour, gen_pcm_pc_pc_seff_pc_pc_CollectionIteratorAction_AbstractLoopAction, gen_pcm_pc_pc_seff_pc_pc_GuardedBranchTransition_AbstractBranchTransition, gen_pcm_pc_pc_seff_pc_pc_SetVariableAction_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_pc_pc_CallReturnAction_CallAction, gen_pcm_pc_pc_seff_pc_pc_ProbabilisticBranchTransition_AbstractBranchTransition, gen_pcm_pc_pc_seff_pc_pc_AcquireAction_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall_CallAction, gen_pcm_pc_pc_seff_pc_pc_InternalCallAction_seff_pc_pc_CallAction, gen_pcm_pc_pc_seff_pc_pc_InternalCallAction_seff_pc_pc_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_pc_pc_EmitEventAction_seff_pc_pc_AbstractAction, gen_pcm_pc_pc_seff_pc_pc_EmitEventAction_seff_pc_pc_CallAction, gen_pcm_pc_pc_seff_pc_pc_InternalAction_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_performance_pc_pc_ResourceCall_CallAction, gen_pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour_seff_reliability_pc_pc_FailureHandlingEntity, gen_pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour_seff_pc_pc_ResourceDemandingBehaviour, gen_pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations_Entity, gen_pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity_Entity, gen_pcm_pc_pc_qos_performance_pc_pc_SpecifiedExecutionTime_SpecifiedQoSAnnotation, gen_pcm_pc_pc_qos_performance_pc_pc_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation, gen_pcm_pc_pc_qos_performance_pc_pc_SystemSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_pc_pc_system_pc_pc_System_entity_pc_pc_Entity, gen_pcm_pc_pc_system_pc_pc_System_entity_pc_pc_ComposedProvidingRequiringEntity, gen_pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification_Identifier, gen_pcm_pc_pc_resourceenvironment_pc_pc_ResourceEnvironment_NamedElement, gen_pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource_Entity, gen_pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer_Entity, gen_pcm_pc_pc_allocation_pc_pc_AllocationContext_Entity, gen_pcm_pc_pc_allocation_pc_pc_Allocation_Entity, gen_pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification_Identifier, gen_pcm_pc_pc_subsystem_pc_pc_SubSystem_entity_pc_pc_ComposedProvidingRequiringEntity, gen_pcm_pc_pc_subsystem_pc_pc_SubSystem_repository_pc_pc_RepositoryComponent, gen_pcm_pc_pc_completions_pc_pc_Completion_entity_pc_pc_ComposedProvidingRequiringEntity, gen_pcm_pc_pc_completions_pc_pc_Completion_repository_pc_pc_ImplementationComponentType, gen_pcm_pc_pc_completions_pc_pc_DelegatingExternalCallAction_ExternalCallAction, gen_pcm_pc_pc_completions_pc_pc_NetworkDemandParametricResourceDemand_ParametricResourceDemand},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)