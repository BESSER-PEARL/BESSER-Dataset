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
			EnumerationLiteral(name="in_"),
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
pcm_pc_av_DummyClass = Class(name="pcm_pc_av_DummyClass")
pcm_pc_av_Pointcut = Class(name="pcm_pc_av_Pointcut")
pcm_pc_av_EObject = Class(name="pcm_pc_av_EObject")
pcm_pc_av_Advice = Class(name="pcm_pc_av_Advice")
pcm_pc_av_core_pc_av_PCMRandomVariable = Class(name="pcm_pc_av_core_pc_av_PCMRandomVariable")
RandomVariable = Class(name="RandomVariable")
ClosedWorkload = Class(name="ClosedWorkload")
PassiveResource = Class(name="PassiveResource")
VariableCharacterisation = Class(name="VariableCharacterisation")
seff_performance_pc_av_InfrastructureCall = Class(name="seff_performance_pc_av_InfrastructureCall")
pcm_pc_av_GlobalScope = Class(name="pcm_pc_av_GlobalScope")
pcm_pc_av_PerJoinPointScope = Class(name="pcm_pc_av_PerJoinPointScope")
GuardedBranchTransition = Class(name="GuardedBranchTransition")
qos_performance_pc_av_SpecifiedExecutionTime = Class(name="qos_performance_pc_av_SpecifiedExecutionTime")
composition_pc_av_EventChannelSinkConnector = Class(name="composition_pc_av_EventChannelSinkConnector")
composition_pc_av_AssemblyEventConnector = Class(name="composition_pc_av_AssemblyEventConnector")
Loop = Class(name="Loop")
OpenWorkload = Class(name="OpenWorkload")
Delay = Class(name="Delay")
seff_performance_pc_av_ResourceCall = Class(name="seff_performance_pc_av_ResourceCall")
seff_performance_pc_av_ParametricResourceDemand = Class(name="seff_performance_pc_av_ParametricResourceDemand")
LoopAction = Class(name="LoopAction")
ProcessingResourceSpecification = Class(name="ProcessingResourceSpecification")
pcm_pc_av_entity_pc_av_ResourceProvidedRole = Class(name="pcm_pc_av_entity_pc_av_ResourceProvidedRole")
Role = Class(name="Role")
entity_pc_av_ResourceInterfaceProvidingEntity = Class(name="entity_pc_av_ResourceInterfaceProvidingEntity")
ResourceInterface = Class(name="ResourceInterface")
pcm_pc_av_entity_pc_av_InterfaceProvidingRequiringEntity = Class(name="pcm_pc_av_entity_pc_av_InterfaceProvidingRequiringEntity")
entity_pc_av_InterfaceProvidingEntity = Class(name="entity_pc_av_InterfaceProvidingEntity")
entity_pc_av_InterfaceRequiringEntity = Class(name="entity_pc_av_InterfaceRequiringEntity")
pcm_pc_av_entity_pc_av_InterfaceProvidingEntity = Class(name="pcm_pc_av_entity_pc_av_InterfaceProvidingEntity")
Entity = Class(name="Entity")
ProvidedRole = Class(name="ProvidedRole")
pcm_pc_av_entity_pc_av_InterfaceRequiringEntity = Class(name="pcm_pc_av_entity_pc_av_InterfaceRequiringEntity")
entity_pc_av_Entity = Class(name="entity_pc_av_Entity")
entity_pc_av_ResourceInterfaceRequiringEntity = Class(name="entity_pc_av_ResourceInterfaceRequiringEntity")
RequiredRole = Class(name="RequiredRole")
pcm_pc_av_entity_pc_av_ResourceInterfaceRequiringEntity = Class(name="pcm_pc_av_entity_pc_av_ResourceInterfaceRequiringEntity")
entity_pc_av_ResourceRequiredRole = Class(name="entity_pc_av_ResourceRequiredRole")
pcm_pc_av_entity_pc_av_ResourceRequiredRole = Class(name="pcm_pc_av_entity_pc_av_ResourceRequiredRole")
CommunicationLinkResourceSpecification = Class(name="CommunicationLinkResourceSpecification")
pcm_pc_av_entity_pc_av_NamedElement = Class(name="pcm_pc_av_entity_pc_av_NamedElement")
pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingRequiringEntity = Class(name="pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingRequiringEntity")
pcm_pc_av_entity_pc_av_Entity = Class(name="pcm_pc_av_entity_pc_av_Entity")
Identifier = Class(name="Identifier")
entity_pc_av_NamedElement = Class(name="entity_pc_av_NamedElement")
pcm_pc_av_composition_pc_av_DelegationConnector = Class(name="pcm_pc_av_composition_pc_av_DelegationConnector")
Connector = Class(name="Connector")
pcm_pc_av_composition_pc_av_Connector = Class(name="pcm_pc_av_composition_pc_av_Connector")
pcm_pc_av_composition_pc_av_ComposedStructure = Class(name="pcm_pc_av_composition_pc_av_ComposedStructure")
pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingEntity = Class(name="pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingEntity")
entity_pc_av_ResourceProvidedRole = Class(name="entity_pc_av_ResourceProvidedRole")
pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity = Class(name="pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity")
composition_pc_av_ComposedStructure = Class(name="composition_pc_av_ComposedStructure")
entity_pc_av_InterfaceProvidingRequiringEntity = Class(name="entity_pc_av_InterfaceProvidingRequiringEntity")
composition_pc_av_AssemblyContext = Class(name="composition_pc_av_AssemblyContext")
composition_pc_av_ResourceRequiredDelegationConnector = Class(name="composition_pc_av_ResourceRequiredDelegationConnector")
composition_pc_av_EventChannel = Class(name="composition_pc_av_EventChannel")
composition_pc_av_Connector = Class(name="composition_pc_av_Connector")
pcm_pc_av_composition_pc_av_ResourceRequiredDelegationConnector = Class(name="pcm_pc_av_composition_pc_av_ResourceRequiredDelegationConnector")
pcm_pc_av_composition_pc_av_EventChannel = Class(name="pcm_pc_av_composition_pc_av_EventChannel")
EventGroup = Class(name="EventGroup")
composition_pc_av_EventChannelSourceConnector = Class(name="composition_pc_av_EventChannelSourceConnector")
pcm_pc_av_composition_pc_av_EventChannelSourceConnector = Class(name="pcm_pc_av_composition_pc_av_EventChannelSourceConnector")
SourceRole = Class(name="SourceRole")
PCMRandomVariable = Class(name="PCMRandomVariable")
pcm_pc_av_composition_pc_av_ProvidedDelegationConnector = Class(name="pcm_pc_av_composition_pc_av_ProvidedDelegationConnector")
DelegationConnector = Class(name="DelegationConnector")
OperationProvidedRole = Class(name="OperationProvidedRole")
pcm_pc_av_composition_pc_av_RequiredDelegationConnector = Class(name="pcm_pc_av_composition_pc_av_RequiredDelegationConnector")
pcm_pc_av_composition_pc_av_EventChannelSinkConnector = Class(name="pcm_pc_av_composition_pc_av_EventChannelSinkConnector")
SinkRole = Class(name="SinkRole")
OperationRequiredRole = Class(name="OperationRequiredRole")
pcm_pc_av_composition_pc_av_AssemblyConnector = Class(name="pcm_pc_av_composition_pc_av_AssemblyConnector")
pcm_pc_av_composition_pc_av_AssemblyEventConnector = Class(name="pcm_pc_av_composition_pc_av_AssemblyEventConnector")
pcm_pc_av_composition_pc_av_SourceDelegationConnector = Class(name="pcm_pc_av_composition_pc_av_SourceDelegationConnector")
pcm_pc_av_composition_pc_av_SinkDelegationConnector = Class(name="pcm_pc_av_composition_pc_av_SinkDelegationConnector")
pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector = Class(name="pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector")
pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector = Class(name="pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector")
pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector = Class(name="pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector")
pcm_pc_av_composition_pc_av_AssemblyContext = Class(name="pcm_pc_av_composition_pc_av_AssemblyContext")
RepositoryComponent = Class(name="RepositoryComponent")
VariableUsage = Class(name="VariableUsage")
pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector = Class(name="pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector")
InfrastructureProvidedRole = Class(name="InfrastructureProvidedRole")
InfrastructureRequiredRole = Class(name="InfrastructureRequiredRole")
UsageModel = Class(name="UsageModel")
ScenarioBehaviour = Class(name="ScenarioBehaviour")
pcm_pc_av_usagemodel_pc_av_AbstractUserAction = Class(name="pcm_pc_av_usagemodel_pc_av_AbstractUserAction")
Workload = Class(name="Workload")
pcm_pc_av_usagemodel_pc_av_UserData = Class(name="pcm_pc_av_usagemodel_pc_av_UserData")
pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour = Class(name="pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour")
pcm_pc_av_usagemodel_pc_av_UsageModel = Class(name="pcm_pc_av_usagemodel_pc_av_UsageModel")
UserData = Class(name="UserData")
pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall = Class(name="pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall")
AbstractUserAction = Class(name="AbstractUserAction")
pcm_pc_av_usagemodel_pc_av_Workload = Class(name="pcm_pc_av_usagemodel_pc_av_Workload")
OperationSignature = Class(name="OperationSignature")
UsageScenario = Class(name="UsageScenario")
pcm_pc_av_usagemodel_pc_av_UsageScenario = Class(name="pcm_pc_av_usagemodel_pc_av_UsageScenario")
pcm_pc_av_usagemodel_pc_av_BranchTransition = Class(name="pcm_pc_av_usagemodel_pc_av_BranchTransition")
Branch = Class(name="Branch")
pcm_pc_av_usagemodel_pc_av_Branch = Class(name="pcm_pc_av_usagemodel_pc_av_Branch")
BranchTransition = Class(name="BranchTransition")
pcm_pc_av_usagemodel_pc_av_OpenWorkload = Class(name="pcm_pc_av_usagemodel_pc_av_OpenWorkload")
pcm_pc_av_usagemodel_pc_av_Loop = Class(name="pcm_pc_av_usagemodel_pc_av_Loop")
pcm_pc_av_usagemodel_pc_av_Stop = Class(name="pcm_pc_av_usagemodel_pc_av_Stop")
pcm_pc_av_usagemodel_pc_av_Start = Class(name="pcm_pc_av_usagemodel_pc_av_Start")
BasicComponent = Class(name="BasicComponent")
ResourceTimeoutFailureType = Class(name="ResourceTimeoutFailureType")
pcm_pc_av_repository_pc_av_BasicComponent = Class(name="pcm_pc_av_repository_pc_av_BasicComponent")
ImplementationComponentType = Class(name="ImplementationComponentType")
pcm_pc_av_usagemodel_pc_av_Delay = Class(name="pcm_pc_av_usagemodel_pc_av_Delay")
pcm_pc_av_usagemodel_pc_av_ClosedWorkload = Class(name="pcm_pc_av_usagemodel_pc_av_ClosedWorkload")
pcm_pc_av_repository_pc_av_PassiveResource = Class(name="pcm_pc_av_repository_pc_av_PassiveResource")
CompleteComponentType = Class(name="CompleteComponentType")
ServiceEffectSpecification = Class(name="ServiceEffectSpecification")
pcm_pc_av_repository_pc_av_ImplementationComponentType = Class(name="pcm_pc_av_repository_pc_av_ImplementationComponentType")
ResourceSignature = Class(name="ResourceSignature")
pcm_pc_av_repository_pc_av_DataType = Class(name="pcm_pc_av_repository_pc_av_DataType")
pcm_pc_av_repository_pc_av_Repository = Class(name="pcm_pc_av_repository_pc_av_Repository")
Interface = Class(name="Interface")
pcm_pc_av_repository_pc_av_RepositoryComponent = Class(name="pcm_pc_av_repository_pc_av_RepositoryComponent")
InterfaceProvidingRequiringEntity = Class(name="InterfaceProvidingRequiringEntity")
Repository = Class(name="Repository")
pcm_pc_av_repository_pc_av_ProvidedRole = Class(name="pcm_pc_av_repository_pc_av_ProvidedRole")
pcm_pc_av_repository_pc_av_Parameter = Class(name="pcm_pc_av_repository_pc_av_Parameter")
DataType = Class(name="DataType")
InfrastructureSignature = Class(name="InfrastructureSignature")
EventType = Class(name="EventType")
RequiredCharacterisation = Class(name="RequiredCharacterisation")
pcm_pc_av_repository_pc_av_RequiredCharacterisation = Class(name="pcm_pc_av_repository_pc_av_RequiredCharacterisation")
Parameter_ = Class(name="Parameter")
pcm_pc_av_repository_pc_av_EventGroup = Class(name="pcm_pc_av_repository_pc_av_EventGroup")
FailureType = Class(name="FailureType")
pcm_pc_av_repository_pc_av_Interface = Class(name="pcm_pc_av_repository_pc_av_Interface")
Protocol = Class(name="Protocol")
pcm_pc_av_repository_pc_av_InfrastructureSignature = Class(name="pcm_pc_av_repository_pc_av_InfrastructureSignature")
InfrastructureInterface = Class(name="InfrastructureInterface")
pcm_pc_av_repository_pc_av_InfrastructureInterface = Class(name="pcm_pc_av_repository_pc_av_InfrastructureInterface")
pcm_pc_av_repository_pc_av_InfrastructureRequiredRole = Class(name="pcm_pc_av_repository_pc_av_InfrastructureRequiredRole")
pcm_pc_av_repository_pc_av_EventType = Class(name="pcm_pc_av_repository_pc_av_EventType")
Signature = Class(name="Signature")
pcm_pc_av_repository_pc_av_Signature = Class(name="pcm_pc_av_repository_pc_av_Signature")
ExceptionType = Class(name="ExceptionType")
pcm_pc_av_repository_pc_av_ExceptionType = Class(name="pcm_pc_av_repository_pc_av_ExceptionType")
pcm_pc_av_repository_pc_av_OperationRequiredRole = Class(name="pcm_pc_av_repository_pc_av_OperationRequiredRole")
pcm_pc_av_repository_pc_av_SourceRole = Class(name="pcm_pc_av_repository_pc_av_SourceRole")
pcm_pc_av_repository_pc_av_SinkRole = Class(name="pcm_pc_av_repository_pc_av_SinkRole")
pcm_pc_av_repository_pc_av_OperationProvidedRole = Class(name="pcm_pc_av_repository_pc_av_OperationProvidedRole")
pcm_pc_av_repository_pc_av_RequiredRole = Class(name="pcm_pc_av_repository_pc_av_RequiredRole")
pcm_pc_av_repository_pc_av_OperationSignature = Class(name="pcm_pc_av_repository_pc_av_OperationSignature")
OperationInterface = Class(name="OperationInterface")
pcm_pc_av_repository_pc_av_OperationInterface = Class(name="pcm_pc_av_repository_pc_av_OperationInterface")
ProvidesComponentType = Class(name="ProvidesComponentType")
pcm_pc_av_repository_pc_av_ProvidesComponentType = Class(name="pcm_pc_av_repository_pc_av_ProvidesComponentType")
pcm_pc_av_repository_pc_av_CompositeComponent = Class(name="pcm_pc_av_repository_pc_av_CompositeComponent")
entity_pc_av_ComposedProvidingRequiringEntity = Class(name="entity_pc_av_ComposedProvidingRequiringEntity")
repository_pc_av_ImplementationComponentType = Class(name="repository_pc_av_ImplementationComponentType")
pcm_pc_av_repository_pc_av_InfrastructureProvidedRole = Class(name="pcm_pc_av_repository_pc_av_InfrastructureProvidedRole")
pcm_pc_av_repository_pc_av_CompleteComponentType = Class(name="pcm_pc_av_repository_pc_av_CompleteComponentType")
pcm_pc_av_repository_pc_av_CompositeDataType = Class(name="pcm_pc_av_repository_pc_av_CompositeDataType")
CompositeDataType = Class(name="CompositeDataType")
InnerDeclaration = Class(name="InnerDeclaration")
pcm_pc_av_repository_pc_av_InnerDeclaration = Class(name="pcm_pc_av_repository_pc_av_InnerDeclaration")
NamedElement = Class(name="NamedElement")
pcm_pc_av_repository_pc_av_Role = Class(name="pcm_pc_av_repository_pc_av_Role")
pcm_pc_av_repository_pc_av_PrimitiveDataType = Class(name="pcm_pc_av_repository_pc_av_PrimitiveDataType")
pcm_pc_av_repository_pc_av_CollectionDataType = Class(name="pcm_pc_av_repository_pc_av_CollectionDataType")
repository_pc_av_DataType = Class(name="repository_pc_av_DataType")
SchedulingPolicy = Class(name="SchedulingPolicy")
pcm_pc_av_resourcetype_pc_av_SchedulingPolicy = Class(name="pcm_pc_av_resourcetype_pc_av_SchedulingPolicy")
pcm_pc_av_resourcetype_pc_av_CommunicationLinkResourceType = Class(name="pcm_pc_av_resourcetype_pc_av_CommunicationLinkResourceType")
NetworkInducedFailureType = Class(name="NetworkInducedFailureType")
pcm_pc_av_resourcetype_pc_av_ResourceInterface = Class(name="pcm_pc_av_resourcetype_pc_av_ResourceInterface")
pcm_pc_av_resourcetype_pc_av_ResourceSignature = Class(name="pcm_pc_av_resourcetype_pc_av_ResourceSignature")
pcm_pc_av_resourcetype_pc_av_ProcessingResourceType = Class(name="pcm_pc_av_resourcetype_pc_av_ProcessingResourceType")
ResourceType = Class(name="ResourceType")
HardwareInducedFailureType = Class(name="HardwareInducedFailureType")
pcm_pc_av_resourcetype_pc_av_ResourceType = Class(name="pcm_pc_av_resourcetype_pc_av_ResourceType")
UnitCarryingElement = Class(name="UnitCarryingElement")
ResourceRepository = Class(name="ResourceRepository")
pcm_pc_av_resourcetype_pc_av_ResourceRepository = Class(name="pcm_pc_av_resourcetype_pc_av_ResourceRepository")
EntryLevelSystemCall = Class(name="EntryLevelSystemCall")
parameter_pc_av_pcm_pc_av_AbstractNamedReference = Class(name="parameter_pc_av_pcm_pc_av_AbstractNamedReference")
pcm_pc_av_parameter_pc_av_VariableCharacterisation = Class(name="pcm_pc_av_parameter_pc_av_VariableCharacterisation")
pcm_pc_av_parameter_pc_av_CharacterisedVariable = Class(name="pcm_pc_av_parameter_pc_av_CharacterisedVariable")
Variable = Class(name="Variable")
pcm_pc_av_protocol_pc_av_Protocol = Class(name="pcm_pc_av_protocol_pc_av_Protocol")
pcm_pc_av_parameter_pc_av_VariableUsage = Class(name="pcm_pc_av_parameter_pc_av_VariableUsage")
CallAction = Class(name="CallAction")
SynchronisationPoint = Class(name="SynchronisationPoint")
CallReturnAction = Class(name="CallReturnAction")
SetVariableAction = Class(name="SetVariableAction")
SpecifiedOutputParameterAbstraction = Class(name="SpecifiedOutputParameterAbstraction")
ProcessingResourceType = Class(name="ProcessingResourceType")
pcm_pc_av_reliability_pc_av_SoftwareInducedFailureType = Class(name="pcm_pc_av_reliability_pc_av_SoftwareInducedFailureType")
InternalFailureOccurrenceDescription = Class(name="InternalFailureOccurrenceDescription")
pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription = Class(name="pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription")
FailureOccurrenceDescription = Class(name="FailureOccurrenceDescription")
InternalAction = Class(name="InternalAction")
pcm_pc_av_reliability_pc_av_FailureOccurrenceDescription = Class(name="pcm_pc_av_reliability_pc_av_FailureOccurrenceDescription")
pcm_pc_av_reliability_pc_av_HardwareInducedFailureType = Class(name="pcm_pc_av_reliability_pc_av_HardwareInducedFailureType")
pcm_pc_av_reliability_pc_av_ResourceTimeoutFailureType = Class(name="pcm_pc_av_reliability_pc_av_ResourceTimeoutFailureType")
pcm_pc_av_reliability_pc_av_FailureType = Class(name="pcm_pc_av_reliability_pc_av_FailureType")
pcm_pc_av_seff_pc_av_StopAction = Class(name="pcm_pc_av_seff_pc_av_StopAction")
AbstractInternalControlFlowAction = Class(name="AbstractInternalControlFlowAction")
SoftwareInducedFailureType = Class(name="SoftwareInducedFailureType")
pcm_pc_av_reliability_pc_av_NetworkInducedFailureType = Class(name="pcm_pc_av_reliability_pc_av_NetworkInducedFailureType")
CommunicationLinkResourceType = Class(name="CommunicationLinkResourceType")
pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription = Class(name="pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription")
qos_reliability_pc_av_SpecifiedReliabilityAnnotation = Class(name="qos_reliability_pc_av_SpecifiedReliabilityAnnotation")
AbstractLoopAction = Class(name="AbstractLoopAction")
AbstractBranchTransition = Class(name="AbstractBranchTransition")
pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction = Class(name="pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction")
AbstractAction = Class(name="AbstractAction")
pcm_pc_av_seff_pc_av_AbstractAction = Class(name="pcm_pc_av_seff_pc_av_AbstractAction")
ResourceDemandingBehaviour = Class(name="ResourceDemandingBehaviour")
pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour = Class(name="pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour")
pcm_pc_av_seff_pc_av_CallAction = Class(name="pcm_pc_av_seff_pc_av_CallAction")
pcm_pc_av_seff_pc_av_StartAction = Class(name="pcm_pc_av_seff_pc_av_StartAction")
pcm_pc_av_seff_pc_av_ServiceEffectSpecification = Class(name="pcm_pc_av_seff_pc_av_ServiceEffectSpecification")
pcm_pc_av_seff_pc_av_AbstractLoopAction = Class(name="pcm_pc_av_seff_pc_av_AbstractLoopAction")
pcm_pc_av_seff_pc_av_AbstractBranchTransition = Class(name="pcm_pc_av_seff_pc_av_AbstractBranchTransition")
BranchAction = Class(name="BranchAction")
pcm_pc_av_seff_pc_av_BranchAction = Class(name="pcm_pc_av_seff_pc_av_BranchAction")
pcm_pc_av_seff_pc_av_LoopAction = Class(name="pcm_pc_av_seff_pc_av_LoopAction")
pcm_pc_av_seff_pc_av_ForkAction = Class(name="pcm_pc_av_seff_pc_av_ForkAction")
ForkedBehaviour = Class(name="ForkedBehaviour")
pcm_pc_av_seff_pc_av_ForkedBehaviour = Class(name="pcm_pc_av_seff_pc_av_ForkedBehaviour")
ForkAction = Class(name="ForkAction")
pcm_pc_av_seff_pc_av_ResourceDemandingSEFF = Class(name="pcm_pc_av_seff_pc_av_ResourceDemandingSEFF")
seff_pc_av_ServiceEffectSpecification = Class(name="seff_pc_av_ServiceEffectSpecification")
seff_pc_av_ResourceDemandingBehaviour = Class(name="seff_pc_av_ResourceDemandingBehaviour")
ResourceDemandingInternalBehaviour = Class(name="ResourceDemandingInternalBehaviour")
pcm_pc_av_seff_pc_av_ResourceDemandingInternalBehaviour = Class(name="pcm_pc_av_seff_pc_av_ResourceDemandingInternalBehaviour")
ResourceDemandingSEFF = Class(name="ResourceDemandingSEFF")
pcm_pc_av_seff_pc_av_ReleaseAction = Class(name="pcm_pc_av_seff_pc_av_ReleaseAction")
pcm_pc_av_seff_pc_av_CallReturnAction = Class(name="pcm_pc_av_seff_pc_av_CallReturnAction")
pcm_pc_av_seff_pc_av_ProbabilisticBranchTransition = Class(name="pcm_pc_av_seff_pc_av_ProbabilisticBranchTransition")
pcm_pc_av_seff_pc_av_AcquireAction = Class(name="pcm_pc_av_seff_pc_av_AcquireAction")
pcm_pc_av_seff_pc_av_SynchronisationPoint = Class(name="pcm_pc_av_seff_pc_av_SynchronisationPoint")
pcm_pc_av_seff_pc_av_ExternalCallAction = Class(name="pcm_pc_av_seff_pc_av_ExternalCallAction")
seff_pc_av_AbstractAction = Class(name="seff_pc_av_AbstractAction")
seff_pc_av_CallReturnAction = Class(name="seff_pc_av_CallReturnAction")
seff_reliability_pc_av_FailureHandlingEntity = Class(name="seff_reliability_pc_av_FailureHandlingEntity")
pcm_pc_av_seff_pc_av_EmitEventAction = Class(name="pcm_pc_av_seff_pc_av_EmitEventAction")
pcm_pc_av_seff_pc_av_InternalAction = Class(name="pcm_pc_av_seff_pc_av_InternalAction")
pcm_pc_av_seff_pc_av_CollectionIteratorAction = Class(name="pcm_pc_av_seff_pc_av_CollectionIteratorAction")
pcm_pc_av_seff_pc_av_GuardedBranchTransition = Class(name="pcm_pc_av_seff_pc_av_GuardedBranchTransition")
pcm_pc_av_seff_pc_av_SetVariableAction = Class(name="pcm_pc_av_seff_pc_av_SetVariableAction")
pcm_pc_av_seff_pc_av_InternalCallAction = Class(name="pcm_pc_av_seff_pc_av_InternalCallAction")
seff_pc_av_CallAction = Class(name="seff_pc_av_CallAction")
seff_pc_av_AbstractInternalControlFlowAction = Class(name="seff_pc_av_AbstractInternalControlFlowAction")
pcm_pc_av_seff_performance_pc_av_InfrastructureCall = Class(name="pcm_pc_av_seff_performance_pc_av_InfrastructureCall")
pcm_pc_av_seff_performance_pc_av_ResourceCall = Class(name="pcm_pc_av_seff_performance_pc_av_ResourceCall")
pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour = Class(name="pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour")
pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand = Class(name="pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand")
pcm_pc_av_seff_reliability_pc_av_FailureHandlingEntity = Class(name="pcm_pc_av_seff_reliability_pc_av_FailureHandlingEntity")
pcm_pc_av_qosannotations_pc_av_SpecifiedQoSAnnotation = Class(name="pcm_pc_av_qosannotations_pc_av_SpecifiedQoSAnnotation")
seff_reliability_pc_av_RecoveryActionBehaviour = Class(name="seff_reliability_pc_av_RecoveryActionBehaviour")
seff_reliability_pc_av_RecoveryAction = Class(name="seff_reliability_pc_av_RecoveryAction")
pcm_pc_av_seff_reliability_pc_av_RecoveryAction = Class(name="pcm_pc_av_seff_reliability_pc_av_RecoveryAction")
System = Class(name="System")
SpecifiedQoSAnnotation = Class(name="SpecifiedQoSAnnotation")
pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction = Class(name="pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction")
QoSAnnotations = Class(name="QoSAnnotations")
pcm_pc_av_qosannotations_pc_av_QoSAnnotations = Class(name="pcm_pc_av_qosannotations_pc_av_QoSAnnotations")
ExternalFailureOccurrenceDescription = Class(name="ExternalFailureOccurrenceDescription")
pcm_pc_av_qos_performance_pc_av_SystemSpecifiedExecutionTime = Class(name="pcm_pc_av_qos_performance_pc_av_SystemSpecifiedExecutionTime")
SpecifiedExecutionTime = Class(name="SpecifiedExecutionTime")
pcm_pc_av_qos_performance_pc_av_SpecifiedExecutionTime = Class(name="pcm_pc_av_qos_performance_pc_av_SpecifiedExecutionTime")
pcm_pc_av_qos_performance_pc_av_ComponentSpecifiedExecutionTime = Class(name="pcm_pc_av_qos_performance_pc_av_ComponentSpecifiedExecutionTime")
pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation = Class(name="pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation")
ResourceEnvironment = Class(name="ResourceEnvironment")
pcm_pc_av_resourceenvironment_pc_av_ResourceContainer = Class(name="pcm_pc_av_resourceenvironment_pc_av_ResourceContainer")
pcm_pc_av_system_pc_av_System = Class(name="pcm_pc_av_system_pc_av_System")
pcm_pc_av_resourceenvironment_pc_av_ResourceEnvironment = Class(name="pcm_pc_av_resourceenvironment_pc_av_ResourceEnvironment")
LinkingResource = Class(name="LinkingResource")
ResourceContainer = Class(name="ResourceContainer")
pcm_pc_av_resourceenvironment_pc_av_LinkingResource = Class(name="pcm_pc_av_resourceenvironment_pc_av_LinkingResource")
pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification = Class(name="pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification")
pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification = Class(name="pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification")
Allocation = Class(name="Allocation")
pcm_pc_av_allocation_pc_av_Allocation = Class(name="pcm_pc_av_allocation_pc_av_Allocation")
pcm_pc_av_allocation_pc_av_AllocationContext = Class(name="pcm_pc_av_allocation_pc_av_AllocationContext")
pcm_pc_av_completions_pc_av_CompletionRepository = Class(name="pcm_pc_av_completions_pc_av_CompletionRepository")
Completion = Class(name="Completion")
pcm_pc_av_completions_pc_av_DelegatingExternalCallAction = Class(name="pcm_pc_av_completions_pc_av_DelegatingExternalCallAction")
ExternalCallAction = Class(name="ExternalCallAction")
pcm_pc_av_completions_pc_av_NetworkDemandParametricResourceDemand = Class(name="pcm_pc_av_completions_pc_av_NetworkDemandParametricResourceDemand")
ParametricResourceDemand = Class(name="ParametricResourceDemand")
AllocationContext = Class(name="AllocationContext")
pcm_pc_av_subsystem_pc_av_SubSystem = Class(name="pcm_pc_av_subsystem_pc_av_SubSystem")
repository_pc_av_RepositoryComponent = Class(name="repository_pc_av_RepositoryComponent")
pcm_pc_av_completions_pc_av_Completion = Class(name="pcm_pc_av_completions_pc_av_Completion")

# pcm_pc_av_DummyClass class attributes and methods

# pcm_pc_av_Pointcut class attributes and methods

# pcm_pc_av_EObject class attributes and methods

# pcm_pc_av_Advice class attributes and methods

# pcm_pc_av_core_pc_av_PCMRandomVariable class attributes and methods
pcm_pc_av_core_pc_av_PCMRandomVariable_m_SpecificationMustNotBeNULL: Method = Method(name="SpecificationMustNotBeNULL", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_core_pc_av_PCMRandomVariable.methods={pcm_pc_av_core_pc_av_PCMRandomVariable_m_SpecificationMustNotBeNULL}

# RandomVariable class attributes and methods

# ClosedWorkload class attributes and methods

# PassiveResource class attributes and methods

# VariableCharacterisation class attributes and methods

# seff_performance_pc_av_InfrastructureCall class attributes and methods

# pcm_pc_av_GlobalScope class attributes and methods

# pcm_pc_av_PerJoinPointScope class attributes and methods

# GuardedBranchTransition class attributes and methods

# qos_performance_pc_av_SpecifiedExecutionTime class attributes and methods

# composition_pc_av_EventChannelSinkConnector class attributes and methods

# composition_pc_av_AssemblyEventConnector class attributes and methods

# Loop class attributes and methods

# OpenWorkload class attributes and methods

# Delay class attributes and methods

# seff_performance_pc_av_ResourceCall class attributes and methods

# seff_performance_pc_av_ParametricResourceDemand class attributes and methods

# LoopAction class attributes and methods

# ProcessingResourceSpecification class attributes and methods

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

# CommunicationLinkResourceSpecification class attributes and methods

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
pcm_pc_av_composition_pc_av_ComposedStructure_m_MultipleConnectorsConstraint: Method = Method(name="MultipleConnectorsConstraint", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_composition_pc_av_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors: Method = Method(name="MultipleConnectorsConstraintForAssemblyConnectors", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_composition_pc_av_ComposedStructure.methods={pcm_pc_av_composition_pc_av_ComposedStructure_m_MultipleConnectorsConstraint, pcm_pc_av_composition_pc_av_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors}

# pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingEntity class attributes and methods

# entity_pc_av_ResourceProvidedRole class attributes and methods

# pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity class attributes and methods
pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound: Method = Method(name="ProvidedRolesMustBeBound", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity.methods={pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound}

# composition_pc_av_ComposedStructure class attributes and methods

# entity_pc_av_InterfaceProvidingRequiringEntity class attributes and methods

# composition_pc_av_AssemblyContext class attributes and methods

# composition_pc_av_ResourceRequiredDelegationConnector class attributes and methods

# composition_pc_av_EventChannel class attributes and methods

# composition_pc_av_Connector class attributes and methods

# pcm_pc_av_composition_pc_av_ResourceRequiredDelegationConnector class attributes and methods

# pcm_pc_av_composition_pc_av_EventChannel class attributes and methods

# EventGroup class attributes and methods

# composition_pc_av_EventChannelSourceConnector class attributes and methods

# pcm_pc_av_composition_pc_av_EventChannelSourceConnector class attributes and methods

# SourceRole class attributes and methods

# PCMRandomVariable class attributes and methods

# pcm_pc_av_composition_pc_av_ProvidedDelegationConnector class attributes and methods
pcm_pc_av_composition_pc_av_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_composition_pc_av_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_composition_pc_av_ProvidedDelegationConnector.methods={pcm_pc_av_composition_pc_av_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame, pcm_pc_av_composition_pc_av_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure}

# DelegationConnector class attributes and methods

# OperationProvidedRole class attributes and methods

# pcm_pc_av_composition_pc_av_RequiredDelegationConnector class attributes and methods
pcm_pc_av_composition_pc_av_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_composition_pc_av_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector: Method = Method(name="RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_composition_pc_av_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_composition_pc_av_RequiredDelegationConnector.methods={pcm_pc_av_composition_pc_av_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure, pcm_pc_av_composition_pc_av_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame, pcm_pc_av_composition_pc_av_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector}

# pcm_pc_av_composition_pc_av_EventChannelSinkConnector class attributes and methods

# SinkRole class attributes and methods

# OperationRequiredRole class attributes and methods

# pcm_pc_av_composition_pc_av_AssemblyConnector class attributes and methods
pcm_pc_av_composition_pc_av_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_composition_pc_av_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_composition_pc_av_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch: Method = Method(name="AssemblyConnectorsReferencedInterfacesMustMatch", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_composition_pc_av_AssemblyConnector.methods={pcm_pc_av_composition_pc_av_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch, pcm_pc_av_composition_pc_av_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch, pcm_pc_av_composition_pc_av_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch}

# pcm_pc_av_composition_pc_av_AssemblyEventConnector class attributes and methods

# pcm_pc_av_composition_pc_av_SourceDelegationConnector class attributes and methods

# pcm_pc_av_composition_pc_av_SinkDelegationConnector class attributes and methods

# pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector class attributes and methods

# pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector class attributes and methods

# pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector class attributes and methods

# pcm_pc_av_composition_pc_av_AssemblyContext class attributes and methods

# RepositoryComponent class attributes and methods

# VariableUsage class attributes and methods

# pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector class attributes and methods

# InfrastructureProvidedRole class attributes and methods

# InfrastructureRequiredRole class attributes and methods

# UsageModel class attributes and methods

# ScenarioBehaviour class attributes and methods

# pcm_pc_av_usagemodel_pc_av_AbstractUserAction class attributes and methods

# Workload class attributes and methods

# pcm_pc_av_usagemodel_pc_av_UserData class attributes and methods

# pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour class attributes and methods
pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour_m_Exactlyonestart: Method = Method(name="Exactlyonestart", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour_m_Exactlyonestop: Method = Method(name="Exactlyonestop", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor: Method = Method(name="EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour.methods={pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour_m_Exactlyonestop, pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor, pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour_m_Exactlyonestart}

# pcm_pc_av_usagemodel_pc_av_UsageModel class attributes and methods

# UserData class attributes and methods

# pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall class attributes and methods
pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall_priority: Property = Property(name="priority", type=IntegerType)
pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem: Method = Method(name="EntryLevelSystemCallMustReferenceProvidedRoleOfASystem", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole: Method = Method(name="EntryLevelSystemCallSignatureMustMatchItsProvidedRole", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall.attributes={pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall_priority}
pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall.methods={pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem, pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole}

# AbstractUserAction class attributes and methods

# pcm_pc_av_usagemodel_pc_av_Workload class attributes and methods

# OperationSignature class attributes and methods

# UsageScenario class attributes and methods

# pcm_pc_av_usagemodel_pc_av_UsageScenario class attributes and methods

# pcm_pc_av_usagemodel_pc_av_BranchTransition class attributes and methods
pcm_pc_av_usagemodel_pc_av_BranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_pc_av_usagemodel_pc_av_BranchTransition.attributes={pcm_pc_av_usagemodel_pc_av_BranchTransition_branchProbability}

# Branch class attributes and methods

# pcm_pc_av_usagemodel_pc_av_Branch class attributes and methods
pcm_pc_av_usagemodel_pc_av_Branch_m_AllBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_Branch.methods={pcm_pc_av_usagemodel_pc_av_Branch_m_AllBranchProbabilitiesMustSumUpTo1}

# BranchTransition class attributes and methods

# pcm_pc_av_usagemodel_pc_av_OpenWorkload class attributes and methods
pcm_pc_av_usagemodel_pc_av_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified: Method = Method(name="InterArrivalTimeInOpenWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_OpenWorkload.methods={pcm_pc_av_usagemodel_pc_av_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified}

# pcm_pc_av_usagemodel_pc_av_Loop class attributes and methods

# pcm_pc_av_usagemodel_pc_av_Stop class attributes and methods
pcm_pc_av_usagemodel_pc_av_Stop_m_StopHasNoSuccessor: Method = Method(name="StopHasNoSuccessor", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_Stop.methods={pcm_pc_av_usagemodel_pc_av_Stop_m_StopHasNoSuccessor}

# pcm_pc_av_usagemodel_pc_av_Start class attributes and methods
pcm_pc_av_usagemodel_pc_av_Start_m_StartHasNoPredecessor: Method = Method(name="StartHasNoPredecessor", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_Start.methods={pcm_pc_av_usagemodel_pc_av_Start_m_StartHasNoPredecessor}

# BasicComponent class attributes and methods

# ResourceTimeoutFailureType class attributes and methods

# pcm_pc_av_repository_pc_av_BasicComponent class attributes and methods
pcm_pc_av_repository_pc_av_BasicComponent_m_NoSeffTypeUsedTwice: Method = Method(name="NoSeffTypeUsedTwice", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_repository_pc_av_BasicComponent_m_ProvideSameInterfacesAsImplementationType: Method = Method(name="ProvideSameInterfacesAsImplementationType", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_repository_pc_av_BasicComponent_m_RequireSameInterfacesAsImplementationType: Method = Method(name="RequireSameInterfacesAsImplementationType", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_repository_pc_av_BasicComponent.methods={pcm_pc_av_repository_pc_av_BasicComponent_m_NoSeffTypeUsedTwice, pcm_pc_av_repository_pc_av_BasicComponent_m_RequireSameInterfacesAsImplementationType, pcm_pc_av_repository_pc_av_BasicComponent_m_ProvideSameInterfacesAsImplementationType}

# ImplementationComponentType class attributes and methods

# pcm_pc_av_usagemodel_pc_av_Delay class attributes and methods

# pcm_pc_av_usagemodel_pc_av_ClosedWorkload class attributes and methods
pcm_pc_av_usagemodel_pc_av_ClosedWorkload_population: Property = Property(name="population", type=IntegerType)
pcm_pc_av_usagemodel_pc_av_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified: Method = Method(name="PopulationInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified: Method = Method(name="ThinkTimeInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_usagemodel_pc_av_ClosedWorkload.attributes={pcm_pc_av_usagemodel_pc_av_ClosedWorkload_population}
pcm_pc_av_usagemodel_pc_av_ClosedWorkload.methods={pcm_pc_av_usagemodel_pc_av_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified, pcm_pc_av_usagemodel_pc_av_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified}

# pcm_pc_av_repository_pc_av_PassiveResource class attributes and methods

# CompleteComponentType class attributes and methods

# ServiceEffectSpecification class attributes and methods

# pcm_pc_av_repository_pc_av_ImplementationComponentType class attributes and methods
pcm_pc_av_repository_pc_av_ImplementationComponentType_componentType: Property = Property(name="componentType", type=StringType)
pcm_pc_av_repository_pc_av_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType: Method = Method(name="providedInterfacesHaveToConformToCompleteType", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_repository_pc_av_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType: Method = Method(name="ProvidedInterfaceHaveToConformToComponentType", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_repository_pc_av_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType: Method = Method(name="RequiredInterfacesHaveToConformToCompleteType", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_repository_pc_av_ImplementationComponentType.attributes={pcm_pc_av_repository_pc_av_ImplementationComponentType_componentType}
pcm_pc_av_repository_pc_av_ImplementationComponentType.methods={pcm_pc_av_repository_pc_av_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType, pcm_pc_av_repository_pc_av_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType, pcm_pc_av_repository_pc_av_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType}

# ResourceSignature class attributes and methods

# pcm_pc_av_repository_pc_av_DataType class attributes and methods

# pcm_pc_av_repository_pc_av_Repository class attributes and methods
pcm_pc_av_repository_pc_av_Repository_repositoryDescription: Property = Property(name="repositoryDescription", type=StringType)
pcm_pc_av_repository_pc_av_Repository.attributes={pcm_pc_av_repository_pc_av_Repository_repositoryDescription}

# Interface class attributes and methods

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

# RequiredCharacterisation class attributes and methods

# pcm_pc_av_repository_pc_av_RequiredCharacterisation class attributes and methods
pcm_pc_av_repository_pc_av_RequiredCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_pc_av_repository_pc_av_RequiredCharacterisation.attributes={pcm_pc_av_repository_pc_av_RequiredCharacterisation_type}

# Parameter class attributes and methods

# pcm_pc_av_repository_pc_av_EventGroup class attributes and methods

# FailureType class attributes and methods

# pcm_pc_av_repository_pc_av_Interface class attributes and methods
pcm_pc_av_repository_pc_av_Interface_m_NoProtocolTypeIDUsedTwice: Method = Method(name="NoProtocolTypeIDUsedTwice", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_repository_pc_av_Interface.methods={pcm_pc_av_repository_pc_av_Interface_m_NoProtocolTypeIDUsedTwice}

# Protocol class attributes and methods

# pcm_pc_av_repository_pc_av_InfrastructureSignature class attributes and methods

# InfrastructureInterface class attributes and methods

# pcm_pc_av_repository_pc_av_InfrastructureInterface class attributes and methods

# pcm_pc_av_repository_pc_av_InfrastructureRequiredRole class attributes and methods

# pcm_pc_av_repository_pc_av_EventType class attributes and methods

# Signature class attributes and methods

# pcm_pc_av_repository_pc_av_Signature class attributes and methods

# ExceptionType class attributes and methods

# pcm_pc_av_repository_pc_av_ExceptionType class attributes and methods
pcm_pc_av_repository_pc_av_ExceptionType_exceptionName: Property = Property(name="exceptionName", type=StringType)
pcm_pc_av_repository_pc_av_ExceptionType_exceptionMessage: Property = Property(name="exceptionMessage", type=StringType)
pcm_pc_av_repository_pc_av_ExceptionType.attributes={pcm_pc_av_repository_pc_av_ExceptionType_exceptionName, pcm_pc_av_repository_pc_av_ExceptionType_exceptionMessage}

# pcm_pc_av_repository_pc_av_OperationRequiredRole class attributes and methods

# pcm_pc_av_repository_pc_av_SourceRole class attributes and methods

# pcm_pc_av_repository_pc_av_SinkRole class attributes and methods

# pcm_pc_av_repository_pc_av_OperationProvidedRole class attributes and methods

# pcm_pc_av_repository_pc_av_RequiredRole class attributes and methods

# pcm_pc_av_repository_pc_av_OperationSignature class attributes and methods
pcm_pc_av_repository_pc_av_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature: Method = Method(name="ParameterNamesHaveToBeUniqueForASignature", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_repository_pc_av_OperationSignature.methods={pcm_pc_av_repository_pc_av_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature}

# OperationInterface class attributes and methods

# pcm_pc_av_repository_pc_av_OperationInterface class attributes and methods
pcm_pc_av_repository_pc_av_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface: Method = Method(name="SignaturesHaveToBeUniqueForAnInterface", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_repository_pc_av_OperationInterface.methods={pcm_pc_av_repository_pc_av_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface}

# ProvidesComponentType class attributes and methods

# pcm_pc_av_repository_pc_av_ProvidesComponentType class attributes and methods
pcm_pc_av_repository_pc_av_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_repository_pc_av_ProvidesComponentType.methods={pcm_pc_av_repository_pc_av_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType}

# pcm_pc_av_repository_pc_av_CompositeComponent class attributes and methods
pcm_pc_av_repository_pc_av_CompositeComponent_m_ProvideSameInterfaces: Method = Method(name="ProvideSameInterfaces", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_repository_pc_av_CompositeComponent_m_RequireSameInterfaces: Method = Method(name="RequireSameInterfaces", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_repository_pc_av_CompositeComponent.methods={pcm_pc_av_repository_pc_av_CompositeComponent_m_ProvideSameInterfaces, pcm_pc_av_repository_pc_av_CompositeComponent_m_RequireSameInterfaces}

# entity_pc_av_ComposedProvidingRequiringEntity class attributes and methods

# repository_pc_av_ImplementationComponentType class attributes and methods

# pcm_pc_av_repository_pc_av_InfrastructureProvidedRole class attributes and methods

# pcm_pc_av_repository_pc_av_CompleteComponentType class attributes and methods
pcm_pc_av_repository_pc_av_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_repository_pc_av_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2: Method = Method(name="providedInterfacesHaveToConformToProvidedType2", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_repository_pc_av_CompleteComponentType.methods={pcm_pc_av_repository_pc_av_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType, pcm_pc_av_repository_pc_av_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2}

# pcm_pc_av_repository_pc_av_CompositeDataType class attributes and methods

# CompositeDataType class attributes and methods

# InnerDeclaration class attributes and methods

# pcm_pc_av_repository_pc_av_InnerDeclaration class attributes and methods

# NamedElement class attributes and methods

# pcm_pc_av_repository_pc_av_Role class attributes and methods

# pcm_pc_av_repository_pc_av_PrimitiveDataType class attributes and methods
pcm_pc_av_repository_pc_av_PrimitiveDataType_type: Property = Property(name="type", type=StringType)
pcm_pc_av_repository_pc_av_PrimitiveDataType.attributes={pcm_pc_av_repository_pc_av_PrimitiveDataType_type}

# pcm_pc_av_repository_pc_av_CollectionDataType class attributes and methods

# repository_pc_av_DataType class attributes and methods

# SchedulingPolicy class attributes and methods

# pcm_pc_av_resourcetype_pc_av_SchedulingPolicy class attributes and methods

# pcm_pc_av_resourcetype_pc_av_CommunicationLinkResourceType class attributes and methods

# NetworkInducedFailureType class attributes and methods

# pcm_pc_av_resourcetype_pc_av_ResourceInterface class attributes and methods

# pcm_pc_av_resourcetype_pc_av_ResourceSignature class attributes and methods
pcm_pc_av_resourcetype_pc_av_ResourceSignature_resourceServiceId: Property = Property(name="resourceServiceId", type=IntegerType)
pcm_pc_av_resourcetype_pc_av_ResourceSignature.attributes={pcm_pc_av_resourcetype_pc_av_ResourceSignature_resourceServiceId}

# pcm_pc_av_resourcetype_pc_av_ProcessingResourceType class attributes and methods

# ResourceType class attributes and methods

# HardwareInducedFailureType class attributes and methods

# pcm_pc_av_resourcetype_pc_av_ResourceType class attributes and methods

# UnitCarryingElement class attributes and methods

# ResourceRepository class attributes and methods

# pcm_pc_av_resourcetype_pc_av_ResourceRepository class attributes and methods

# EntryLevelSystemCall class attributes and methods

# parameter_pc_av_pcm_pc_av_AbstractNamedReference class attributes and methods

# pcm_pc_av_parameter_pc_av_VariableCharacterisation class attributes and methods
pcm_pc_av_parameter_pc_av_VariableCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_pc_av_parameter_pc_av_VariableCharacterisation.attributes={pcm_pc_av_parameter_pc_av_VariableCharacterisation_type}

# pcm_pc_av_parameter_pc_av_CharacterisedVariable class attributes and methods
pcm_pc_av_parameter_pc_av_CharacterisedVariable_characterisationType: Property = Property(name="characterisationType", type=StringType)
pcm_pc_av_parameter_pc_av_CharacterisedVariable.attributes={pcm_pc_av_parameter_pc_av_CharacterisedVariable_characterisationType}

# Variable class attributes and methods

# pcm_pc_av_protocol_pc_av_Protocol class attributes and methods
pcm_pc_av_protocol_pc_av_Protocol_protocolTypeID: Property = Property(name="protocolTypeID", type=StringType)
pcm_pc_av_protocol_pc_av_Protocol.attributes={pcm_pc_av_protocol_pc_av_Protocol_protocolTypeID}

# pcm_pc_av_parameter_pc_av_VariableUsage class attributes and methods

# CallAction class attributes and methods

# SynchronisationPoint class attributes and methods

# CallReturnAction class attributes and methods

# SetVariableAction class attributes and methods

# SpecifiedOutputParameterAbstraction class attributes and methods

# ProcessingResourceType class attributes and methods

# pcm_pc_av_reliability_pc_av_SoftwareInducedFailureType class attributes and methods

# InternalFailureOccurrenceDescription class attributes and methods

# pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription class attributes and methods
pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription.methods={pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription}

# FailureOccurrenceDescription class attributes and methods

# InternalAction class attributes and methods

# pcm_pc_av_reliability_pc_av_FailureOccurrenceDescription class attributes and methods
pcm_pc_av_reliability_pc_av_FailureOccurrenceDescription_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_pc_av_reliability_pc_av_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange: Method = Method(name="EnsureValidFailureProbabilityRange", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_reliability_pc_av_FailureOccurrenceDescription.attributes={pcm_pc_av_reliability_pc_av_FailureOccurrenceDescription_failureProbability}
pcm_pc_av_reliability_pc_av_FailureOccurrenceDescription.methods={pcm_pc_av_reliability_pc_av_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange}

# pcm_pc_av_reliability_pc_av_HardwareInducedFailureType class attributes and methods
pcm_pc_av_reliability_pc_av_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType: Method = Method(name="HardwareInducedFailureTypeHasProcessingResourceType", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_reliability_pc_av_HardwareInducedFailureType.methods={pcm_pc_av_reliability_pc_av_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType}

# pcm_pc_av_reliability_pc_av_ResourceTimeoutFailureType class attributes and methods

# pcm_pc_av_reliability_pc_av_FailureType class attributes and methods

# pcm_pc_av_seff_pc_av_StopAction class attributes and methods
pcm_pc_av_seff_pc_av_StopAction_m_StopActionSuccessorMustNotBeDefined: Method = Method(name="StopActionSuccessorMustNotBeDefined", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_pc_av_StopAction.methods={pcm_pc_av_seff_pc_av_StopAction_m_StopActionSuccessorMustNotBeDefined}

# AbstractInternalControlFlowAction class attributes and methods

# SoftwareInducedFailureType class attributes and methods

# pcm_pc_av_reliability_pc_av_NetworkInducedFailureType class attributes and methods
pcm_pc_av_reliability_pc_av_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType: Method = Method(name="NetworkInducedFailureTypeHasCommunicationLinkResourceType", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_reliability_pc_av_NetworkInducedFailureType.methods={pcm_pc_av_reliability_pc_av_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType}

# CommunicationLinkResourceType class attributes and methods

# pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription class attributes and methods
pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription.methods={pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription}

# qos_reliability_pc_av_SpecifiedReliabilityAnnotation class attributes and methods

# AbstractLoopAction class attributes and methods

# AbstractBranchTransition class attributes and methods

# pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction class attributes and methods

# AbstractAction class attributes and methods

# pcm_pc_av_seff_pc_av_AbstractAction class attributes and methods

# ResourceDemandingBehaviour class attributes and methods

# pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour class attributes and methods
pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour_m_ExactlyOneStartAction: Method = Method(name="ExactlyOneStartAction", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor: Method = Method(name="EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour_m_ExactlyOneStopAction: Method = Method(name="ExactlyOneStopAction", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour.methods={pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour_m_ExactlyOneStopAction, pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour_m_ExactlyOneStartAction, pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor}

# pcm_pc_av_seff_pc_av_CallAction class attributes and methods

# pcm_pc_av_seff_pc_av_StartAction class attributes and methods
pcm_pc_av_seff_pc_av_StartAction_m_StartActionPredecessorMustNotBeDefined: Method = Method(name="StartActionPredecessorMustNotBeDefined", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_pc_av_StartAction.methods={pcm_pc_av_seff_pc_av_StartAction_m_StartActionPredecessorMustNotBeDefined}

# pcm_pc_av_seff_pc_av_ServiceEffectSpecification class attributes and methods
pcm_pc_av_seff_pc_av_ServiceEffectSpecification_seffTypeID: Property = Property(name="seffTypeID", type=StringType)
pcm_pc_av_seff_pc_av_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole: Method = Method(name="ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_pc_av_ServiceEffectSpecification.attributes={pcm_pc_av_seff_pc_av_ServiceEffectSpecification_seffTypeID}
pcm_pc_av_seff_pc_av_ServiceEffectSpecification.methods={pcm_pc_av_seff_pc_av_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole}

# pcm_pc_av_seff_pc_av_AbstractLoopAction class attributes and methods

# pcm_pc_av_seff_pc_av_AbstractBranchTransition class attributes and methods

# BranchAction class attributes and methods

# pcm_pc_av_seff_pc_av_BranchAction class attributes and methods
pcm_pc_av_seff_pc_av_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions: Method = Method(name="EitherGuardedBranchesOrProbabilisiticBranchTransitions", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_pc_av_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllProbabilisticBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_pc_av_BranchAction.methods={pcm_pc_av_seff_pc_av_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions, pcm_pc_av_seff_pc_av_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1}

# pcm_pc_av_seff_pc_av_LoopAction class attributes and methods

# pcm_pc_av_seff_pc_av_ForkAction class attributes and methods

# ForkedBehaviour class attributes and methods

# pcm_pc_av_seff_pc_av_ForkedBehaviour class attributes and methods

# ForkAction class attributes and methods

# pcm_pc_av_seff_pc_av_ResourceDemandingSEFF class attributes and methods

# seff_pc_av_ServiceEffectSpecification class attributes and methods

# seff_pc_av_ResourceDemandingBehaviour class attributes and methods

# ResourceDemandingInternalBehaviour class attributes and methods

# pcm_pc_av_seff_pc_av_ResourceDemandingInternalBehaviour class attributes and methods

# ResourceDemandingSEFF class attributes and methods

# pcm_pc_av_seff_pc_av_ReleaseAction class attributes and methods

# pcm_pc_av_seff_pc_av_CallReturnAction class attributes and methods

# pcm_pc_av_seff_pc_av_ProbabilisticBranchTransition class attributes and methods
pcm_pc_av_seff_pc_av_ProbabilisticBranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_pc_av_seff_pc_av_ProbabilisticBranchTransition.attributes={pcm_pc_av_seff_pc_av_ProbabilisticBranchTransition_branchProbability}

# pcm_pc_av_seff_pc_av_AcquireAction class attributes and methods
pcm_pc_av_seff_pc_av_AcquireAction_timeout: Property = Property(name="timeout", type=BooleanType)
pcm_pc_av_seff_pc_av_AcquireAction_timeoutValue: Property = Property(name="timeoutValue", type=FloatType)
pcm_pc_av_seff_pc_av_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative: Method = Method(name="TimeoutValueOfAcquireActionMustNotBeNegative", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_pc_av_AcquireAction.attributes={pcm_pc_av_seff_pc_av_AcquireAction_timeoutValue, pcm_pc_av_seff_pc_av_AcquireAction_timeout}
pcm_pc_av_seff_pc_av_AcquireAction.methods={pcm_pc_av_seff_pc_av_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative}

# pcm_pc_av_seff_pc_av_SynchronisationPoint class attributes and methods

# pcm_pc_av_seff_pc_av_ExternalCallAction class attributes and methods
pcm_pc_av_seff_pc_av_ExternalCallAction_retryCount: Property = Property(name="retryCount", type=IntegerType)
pcm_pc_av_seff_pc_av_ExternalCallAction_m_SignatureBelongsToRole: Method = Method(name="SignatureBelongsToRole", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_pc_av_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer: Method = Method(name="OperationRequiredRoleMustBeReferencedByContainer", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_pc_av_ExternalCallAction.attributes={pcm_pc_av_seff_pc_av_ExternalCallAction_retryCount}
pcm_pc_av_seff_pc_av_ExternalCallAction.methods={pcm_pc_av_seff_pc_av_ExternalCallAction_m_SignatureBelongsToRole, pcm_pc_av_seff_pc_av_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer}

# seff_pc_av_AbstractAction class attributes and methods

# seff_pc_av_CallReturnAction class attributes and methods

# seff_reliability_pc_av_FailureHandlingEntity class attributes and methods

# pcm_pc_av_seff_pc_av_EmitEventAction class attributes and methods

# pcm_pc_av_seff_pc_av_InternalAction class attributes and methods
pcm_pc_av_seff_pc_av_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_pc_av_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfInternalActionFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_pc_av_InternalAction.methods={pcm_pc_av_seff_pc_av_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed, pcm_pc_av_seff_pc_av_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1}

# pcm_pc_av_seff_pc_av_CollectionIteratorAction class attributes and methods

# pcm_pc_av_seff_pc_av_GuardedBranchTransition class attributes and methods

# pcm_pc_av_seff_pc_av_SetVariableAction class attributes and methods

# pcm_pc_av_seff_pc_av_InternalCallAction class attributes and methods

# seff_pc_av_CallAction class attributes and methods

# seff_pc_av_AbstractInternalControlFlowAction class attributes and methods

# pcm_pc_av_seff_performance_pc_av_InfrastructureCall class attributes and methods
pcm_pc_av_seff_performance_pc_av_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent: Method = Method(name="ReferencedRequiredRoleMustBeRequiredByComponent", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_performance_pc_av_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole: Method = Method(name="SignatureMustBelongToUsedRequiredRole", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_performance_pc_av_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_performance_pc_av_InfrastructureCall.methods={pcm_pc_av_seff_performance_pc_av_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole, pcm_pc_av_seff_performance_pc_av_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction, pcm_pc_av_seff_performance_pc_av_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent}

# pcm_pc_av_seff_performance_pc_av_ResourceCall class attributes and methods
pcm_pc_av_seff_performance_pc_av_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_performance_pc_av_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole: Method = Method(name="ResourceSignatureBelongsToResourceRequiredRole", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_performance_pc_av_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent: Method = Method(name="ResourceRequiredRoleMustBeReferencedByComponent", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_performance_pc_av_ResourceCall.methods={pcm_pc_av_seff_performance_pc_av_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent, pcm_pc_av_seff_performance_pc_av_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole, pcm_pc_av_seff_performance_pc_av_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction}

# pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour class attributes and methods
pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor: Method = Method(name="RecoveryActionBehaviourHasOnlyOnePredecessor", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself: Method = Method(name="RecoveryActionBehaviourIsNotSuccessorOfItself", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes: Method = Method(name="SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour.methods={pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself, pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor, pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes}

# pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand class attributes and methods
pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand.methods={pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction}

# pcm_pc_av_seff_reliability_pc_av_FailureHandlingEntity class attributes and methods

# pcm_pc_av_qosannotations_pc_av_SpecifiedQoSAnnotation class attributes and methods

# seff_reliability_pc_av_RecoveryActionBehaviour class attributes and methods

# seff_reliability_pc_av_RecoveryAction class attributes and methods

# pcm_pc_av_seff_reliability_pc_av_RecoveryAction class attributes and methods
pcm_pc_av_seff_reliability_pc_av_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet: Method = Method(name="PrimaryBehaviourOfRecoveryActionMustBeSet", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_seff_reliability_pc_av_RecoveryAction.methods={pcm_pc_av_seff_reliability_pc_av_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet}

# System class attributes and methods

# SpecifiedQoSAnnotation class attributes and methods

# pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction class attributes and methods

# QoSAnnotations class attributes and methods

# pcm_pc_av_qosannotations_pc_av_QoSAnnotations class attributes and methods
pcm_pc_av_qosannotations_pc_av_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed: Method = Method(name="MultipleReliabilityAnnotationsPerExternalCallNotAllowed", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_qosannotations_pc_av_QoSAnnotations.methods={pcm_pc_av_qosannotations_pc_av_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed}

# ExternalFailureOccurrenceDescription class attributes and methods

# pcm_pc_av_qos_performance_pc_av_SystemSpecifiedExecutionTime class attributes and methods
pcm_pc_av_qos_performance_pc_av_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem: Method = Method(name="SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_qos_performance_pc_av_SystemSpecifiedExecutionTime.methods={pcm_pc_av_qos_performance_pc_av_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem}

# SpecifiedExecutionTime class attributes and methods

# pcm_pc_av_qos_performance_pc_av_SpecifiedExecutionTime class attributes and methods

# pcm_pc_av_qos_performance_pc_av_ComponentSpecifiedExecutionTime class attributes and methods

# pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation class attributes and methods
pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem: Method = Method(name="SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation.methods={pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed, pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1, pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem}

# ResourceEnvironment class attributes and methods

# pcm_pc_av_resourceenvironment_pc_av_ResourceContainer class attributes and methods

# pcm_pc_av_system_pc_av_System class attributes and methods
pcm_pc_av_system_pc_av_System_m_SystemMustHaveAtLeastOneProvidedRole: Method = Method(name="SystemMustHaveAtLeastOneProvidedRole", parameters={Parameter(name='pcm_pc_av_diagnostics', type=StringType), Parameter(name='pcm_pc_av_context', type=StringType)}, type=BooleanType)
pcm_pc_av_system_pc_av_System.methods={pcm_pc_av_system_pc_av_System_m_SystemMustHaveAtLeastOneProvidedRole}

# pcm_pc_av_resourceenvironment_pc_av_ResourceEnvironment class attributes and methods

# LinkingResource class attributes and methods

# ResourceContainer class attributes and methods

# pcm_pc_av_resourceenvironment_pc_av_LinkingResource class attributes and methods

# pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification class attributes and methods
pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification.attributes={pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification_failureProbability}

# pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification class attributes and methods
pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification_requiredByContainer: Property = Property(name="requiredByContainer", type=BooleanType)
pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification_numberOfReplicas: Property = Property(name="numberOfReplicas", type=IntegerType)
pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification_MTTR: Property = Property(name="MTTR", type=FloatType)
pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification_MTTF: Property = Property(name="MTTF", type=FloatType)
pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification.attributes={pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification_MTTF, pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification_numberOfReplicas, pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification_MTTR, pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification_requiredByContainer}

# Allocation class attributes and methods

# pcm_pc_av_allocation_pc_av_Allocation class attributes and methods
pcm_pc_av_allocation_pc_av_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce: Method = Method(name="EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_allocation_pc_av_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource: Method = Method(name="CommunicatingServersHaveToBeConnectedByLinkingResource", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_allocation_pc_av_Allocation.methods={pcm_pc_av_allocation_pc_av_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce, pcm_pc_av_allocation_pc_av_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource}

# pcm_pc_av_allocation_pc_av_AllocationContext class attributes and methods
pcm_pc_av_allocation_pc_av_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred: Method = Method(name="OneAssemblyContextOrOneEventChannelShouldBeReferred", parameters={Parameter(name='pcm_pc_av_context', type=StringType), Parameter(name='pcm_pc_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_av_allocation_pc_av_AllocationContext.methods={pcm_pc_av_allocation_pc_av_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred}

# pcm_pc_av_completions_pc_av_CompletionRepository class attributes and methods

# Completion class attributes and methods

# pcm_pc_av_completions_pc_av_DelegatingExternalCallAction class attributes and methods

# ExternalCallAction class attributes and methods

# pcm_pc_av_completions_pc_av_NetworkDemandParametricResourceDemand class attributes and methods

# ParametricResourceDemand class attributes and methods

# AllocationContext class attributes and methods

# pcm_pc_av_subsystem_pc_av_SubSystem class attributes and methods

# repository_pc_av_RepositoryComponent class attributes and methods

# pcm_pc_av_completions_pc_av_Completion class attributes and methods

# Relationships
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="pcm_pc_av_EObject", type=pcm_pc_av_Pointcut, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_Pointcut", type=pcm_pc_av_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
closedWorkload_PCMRandomVariable7: BinaryAssociation = BinaryAssociation(
    name="closedWorkload_PCMRandomVariable7",
    ends={
        Property(name="ClosedWorkload", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="thinkTime_ClosedWorkload", type=ClosedWorkload, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_capacity_PCMRandomVariable8: BinaryAssociation = BinaryAssociation(
    name="passiveResource_capacity_PCMRandomVariable8",
    ends={
        Property(name="PassiveResource", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="capacity_PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
variableCharacterisation_Specification9: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_Specification9",
    ends={
        Property(name="VariableCharacterisation", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="specification_VariableCharacterisation", type=VariableCharacterisation, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureCall__PCMRandomVariable10: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__PCMRandomVariable10",
    ends={
        Property(name="InfrastructureCall", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="numberOfCalls__InfrastructureCall", type=seff_performance_pc_av_InfrastructureCall, multiplicity=Multiplicity(0, 1))
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
scopedObject5: BinaryAssociation = BinaryAssociation(
    name="scopedObject5",
    ends={
        Property(name="pcm_pc_av_EObject6", type=pcm_pc_av_PerJoinPointScope, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_PerJoinPointScope", type=pcm_pc_av_EObject, multiplicity=Multiplicity(1, 1))
    }
)
loopAction_PCMRandomVariable13: BinaryAssociation = BinaryAssociation(
    name="loopAction_PCMRandomVariable13",
    ends={
        Property(name="LoopAction", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="iterationCount_LoopAction", type=LoopAction, multiplicity=Multiplicity(0, 1))
    }
)
guardedBranchTransition_PCMRandomVariable14: BinaryAssociation = BinaryAssociation(
    name="guardedBranchTransition_PCMRandomVariable14",
    ends={
        Property(name="GuardedBranchTransition", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="branchCondition_GuardedBranchTransition", type=GuardedBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
specifiedExecutionTime_PCMRandomVariable15: BinaryAssociation = BinaryAssociation(
    name="specifiedExecutionTime_PCMRandomVariable15",
    ends={
        Property(name="SpecifiedExecutionTime", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="specification_SpecifiedExecutionTime", type=qos_performance_pc_av_SpecifiedExecutionTime, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSinkConnector__FilterCondition16: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__FilterCondition16",
    ends={
        Property(name="EventChannelSinkConnector", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="filterCondition__EventChannelSinkConnector", type=composition_pc_av_EventChannelSinkConnector, multiplicity=Multiplicity(0, 1))
    }
)
assemblyEventConnector__FilterCondition17: BinaryAssociation = BinaryAssociation(
    name="assemblyEventConnector__FilterCondition17",
    ends={
        Property(name="AssemblyEventConnector", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="filterCondition__AssemblyEventConnector", type=composition_pc_av_AssemblyEventConnector, multiplicity=Multiplicity(0, 1))
    }
)
loop_LoopIteration18: BinaryAssociation = BinaryAssociation(
    name="loop_LoopIteration18",
    ends={
        Property(name="Loop", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="loopIteration_Loop", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
openWorkload_PCMRandomVariable19: BinaryAssociation = BinaryAssociation(
    name="openWorkload_PCMRandomVariable19",
    ends={
        Property(name="OpenWorkload", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="interArrivalTime_OpenWorkload", type=OpenWorkload, multiplicity=Multiplicity(0, 1))
    }
)
resourceCall__PCMRandomVariable11: BinaryAssociation = BinaryAssociation(
    name="resourceCall__PCMRandomVariable11",
    ends={
        Property(name="ResourceCall", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="numberOfCalls__ResourceCall", type=seff_performance_pc_av_ResourceCall, multiplicity=Multiplicity(0, 1))
    }
)
parametricResourceDemand_PCMRandomVariable12: BinaryAssociation = BinaryAssociation(
    name="parametricResourceDemand_PCMRandomVariable12",
    ends={
        Property(name="ParametricResourceDemand", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="specification_ParametericResourceDemand", type=seff_performance_pc_av_ParametricResourceDemand, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceSpecification_processingRate_PCMRandomVariable22: BinaryAssociation = BinaryAssociation(
    name="processingResourceSpecification_processingRate_PCMRandomVariable22",
    ends={
        Property(name="ProcessingResourceSpecification", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="processingRate_ProcessingResourceSpecification", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecification_latency_PCMRandomVariable23: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecification_latency_PCMRandomVariable23",
    ends={
        Property(name="CommunicationLinkResourceSpecification24", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="latency_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaceProvidingEntity__ResourceProvidedRole25: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceProvidingEntity__ResourceProvidedRole25",
    ends={
        Property(name="ResourceInterfaceProvidingEntity", type=pcm_pc_av_entity_pc_av_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceProvidedRoles__ResourceInterfaceProvidingEntity", type=entity_pc_av_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
providedResourceInterface__ResourceProvidedRole26: BinaryAssociation = BinaryAssociation(
    name="providedResourceInterface__ResourceProvidedRole26",
    ends={
        Property(name="ResourceInterface", type=pcm_pc_av_entity_pc_av_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_entity_pc_av_ResourceProvidedRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedRoles_InterfaceProvidingEntity27: BinaryAssociation = BinaryAssociation(
    name="providedRoles_InterfaceProvidingEntity27",
    ends={
        Property(name="ProvidedRole", type=pcm_pc_av_entity_pc_av_InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="providingEntity_ProvidedRole", type=ProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredRoles_InterfaceRequiringEntity28: BinaryAssociation = BinaryAssociation(
    name="requiredRoles_InterfaceRequiringEntity28",
    ends={
        Property(name="RequiredRole", type=pcm_pc_av_entity_pc_av_InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="requiringEntity_RequiredRole", type=RequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredRoles__ResourceInterfaceRequiringEntity29: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRoles__ResourceInterfaceRequiringEntity29",
    ends={
        Property(name="ResourceRequiredRole", type=pcm_pc_av_entity_pc_av_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterfaceRequiringEntity__ResourceRequiredRole", type=entity_pc_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
delay_TimeSpecification20: BinaryAssociation = BinaryAssociation(
    name="delay_TimeSpecification20",
    ends={
        Property(name="Delay", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="timeSpecification_Delay", type=Delay, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecifcation_throughput_PCMRandomVariable21: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifcation_throughput_PCMRandomVariable21",
    ends={
        Property(name="CommunicationLinkResourceSpecification", type=pcm_pc_av_core_pc_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="throughput_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure__Connector34: BinaryAssociation = BinaryAssociation(
    name="parentStructure__Connector34",
    ends={
        Property(name="ComposedStructure", type=pcm_pc_av_composition_pc_av_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="connectors__ComposedStructure", type=composition_pc_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
requiredResourceInterface__ResourceRequiredRole30: BinaryAssociation = BinaryAssociation(
    name="requiredResourceInterface__ResourceRequiredRole30",
    ends={
        Property(name="ResourceInterface31", type=pcm_pc_av_entity_pc_av_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_entity_pc_av_ResourceRequiredRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaceRequiringEntity__ResourceRequiredRole32: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceRequiringEntity__ResourceRequiredRole32",
    ends={
        Property(name="ResourceInterfaceRequiringEntity", type=pcm_pc_av_entity_pc_av_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRequiredRoles__ResourceInterfaceRequiringEntity", type=entity_pc_av_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
resourceProvidedRoles__ResourceInterfaceProvidingEntity33: BinaryAssociation = BinaryAssociation(
    name="resourceProvidedRoles__ResourceInterfaceProvidingEntity33",
    ends={
        Property(name="ResourceProvidedRole", type=pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterfaceProvidingEntity__ResourceProvidedRole", type=entity_pc_av_ResourceProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assemblyContexts__ComposedStructure35: BinaryAssociation = BinaryAssociation(
    name="assemblyContexts__ComposedStructure35",
    ends={
        Property(name="AssemblyContext", type=pcm_pc_av_composition_pc_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure__AssemblyContext", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredDelegationConnectors_ComposedStructure36: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredDelegationConnectors_ComposedStructure36",
    ends={
        Property(name="ResourceRequiredDelegationConnector", type=pcm_pc_av_composition_pc_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure_ResourceRequiredDelegationConnector", type=composition_pc_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventChannel__ComposedStructure37: BinaryAssociation = BinaryAssociation(
    name="eventChannel__ComposedStructure37",
    ends={
        Property(name="EventChannel", type=pcm_pc_av_composition_pc_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure__EventChannel", type=composition_pc_av_EventChannel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectors__ComposedStructure38: BinaryAssociation = BinaryAssociation(
    name="connectors__ComposedStructure38",
    ends={
        Property(name="Connector", type=pcm_pc_av_composition_pc_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure__Connector", type=composition_pc_av_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerResourceRequiredRole_ResourceRequiredDelegationConnector39: BinaryAssociation = BinaryAssociation(
    name="innerResourceRequiredRole_ResourceRequiredDelegationConnector39",
    ends={
        Property(name="entity_pc_av_ResourceRequiredRole", type=pcm_pc_av_composition_pc_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_ResourceRequiredDelegationConnector", type=entity_pc_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerResourceRequiredRole_ResourceRequiredDelegationConnector40: BinaryAssociation = BinaryAssociation(
    name="outerResourceRequiredRole_ResourceRequiredDelegationConnector40",
    ends={
        Property(name="entity_pc_av_ResourceRequiredRole42", type=pcm_pc_av_composition_pc_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_ResourceRequiredDelegationConnector41", type=entity_pc_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure_ResourceRequiredDelegationConnector43: BinaryAssociation = BinaryAssociation(
    name="parentStructure_ResourceRequiredDelegationConnector43",
    ends={
        Property(name="ComposedStructure44", type=pcm_pc_av_composition_pc_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRequiredDelegationConnectors_ComposedStructure", type=composition_pc_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__EventChannel45: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventChannel45",
    ends={
        Property(name="EventGroup", type=pcm_pc_av_composition_pc_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_EventChannel", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSourceConnector__EventChannel46: BinaryAssociation = BinaryAssociation(
    name="eventChannelSourceConnector__EventChannel46",
    ends={
        Property(name="EventChannelSourceConnector", type=pcm_pc_av_composition_pc_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannel__EventChannelSourceConnector", type=composition_pc_av_EventChannelSourceConnector, multiplicity=Multiplicity(0, 9999))
    }
)
eventChannelSinkConnector__EventChannel47: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__EventChannel47",
    ends={
        Property(name="EventChannelSinkConnector48", type=pcm_pc_av_composition_pc_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannel__EventChannelSinkConnector", type=composition_pc_av_EventChannelSinkConnector, multiplicity=Multiplicity(0, 9999))
    }
)
parentStructure__EventChannel49: BinaryAssociation = BinaryAssociation(
    name="parentStructure__EventChannel49",
    ends={
        Property(name="ComposedStructure50", type=pcm_pc_av_composition_pc_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannel__ComposedStructure", type=composition_pc_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__EventChannelSinkConnector56: BinaryAssociation = BinaryAssociation(
    name="sinkRole__EventChannelSinkConnector56",
    ends={
        Property(name="SinkRole", type=pcm_pc_av_composition_pc_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_EventChannelSinkConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__EventChannelSinkConnector57: BinaryAssociation = BinaryAssociation(
    name="filterCondition__EventChannelSinkConnector57",
    ends={
        Property(name="PCMRandomVariable", type=pcm_pc_av_composition_pc_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannelSinkConnector__FilterCondition", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext__EventChannelSinkConnector58: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSinkConnector58",
    ends={
        Property(name="composition_pc_av_AssemblyContext60", type=pcm_pc_av_composition_pc_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_EventChannelSinkConnector59", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSinkConnector61: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSinkConnector61",
    ends={
        Property(name="EventChannel62", type=pcm_pc_av_composition_pc_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannelSinkConnector__EventChannel", type=composition_pc_av_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole_ProvidedDelegationConnector63: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole_ProvidedDelegationConnector63",
    ends={
        Property(name="OperationProvidedRole", type=pcm_pc_av_composition_pc_av_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_ProvidedDelegationConnector", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole_ProvidedDelegationConnector64: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole_ProvidedDelegationConnector64",
    ends={
        Property(name="OperationProvidedRole66", type=pcm_pc_av_composition_pc_av_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_ProvidedDelegationConnector65", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_ProvidedDelegationConnector67: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ProvidedDelegationConnector67",
    ends={
        Property(name="composition_pc_av_AssemblyContext69", type=pcm_pc_av_composition_pc_av_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_ProvidedDelegationConnector68", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EventChannelSourceRole51: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EventChannelSourceRole51",
    ends={
        Property(name="SourceRole", type=pcm_pc_av_composition_pc_av_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_EventChannelSourceConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__EventChannelSourceConnector52: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSourceConnector52",
    ends={
        Property(name="composition_pc_av_AssemblyContext", type=pcm_pc_av_composition_pc_av_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_EventChannelSourceConnector53", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSourceConnector54: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSourceConnector54",
    ends={
        Property(name="EventChannel55", type=pcm_pc_av_composition_pc_av_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannelSourceConnector__EventChannel", type=composition_pc_av_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole_RequiredDelegationConnector70: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole_RequiredDelegationConnector70",
    ends={
        Property(name="OperationRequiredRole", type=pcm_pc_av_composition_pc_av_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_RequiredDelegationConnector", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole_RequiredDelegationConnector71: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole_RequiredDelegationConnector71",
    ends={
        Property(name="OperationRequiredRole73", type=pcm_pc_av_composition_pc_av_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_RequiredDelegationConnector72", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_RequiredDelegationConnector74: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_RequiredDelegationConnector74",
    ends={
        Property(name="composition_pc_av_AssemblyContext76", type=pcm_pc_av_composition_pc_av_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_RequiredDelegationConnector75", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext_AssemblyConnector77: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext_AssemblyConnector77",
    ends={
        Property(name="composition_pc_av_AssemblyContext78", type=pcm_pc_av_composition_pc_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyConnector", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext_AssemblyConnector79: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext_AssemblyConnector79",
    ends={
        Property(name="composition_pc_av_AssemblyContext81", type=pcm_pc_av_composition_pc_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyConnector80", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providedRole_AssemblyConnector82: BinaryAssociation = BinaryAssociation(
    name="providedRole_AssemblyConnector82",
    ends={
        Property(name="OperationProvidedRole84", type=pcm_pc_av_composition_pc_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyConnector83", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole_AssemblyConnector85: BinaryAssociation = BinaryAssociation(
    name="requiredRole_AssemblyConnector85",
    ends={
        Property(name="OperationRequiredRole87", type=pcm_pc_av_composition_pc_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyConnector86", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__AssemblyEventConnector88: BinaryAssociation = BinaryAssociation(
    name="sinkRole__AssemblyEventConnector88",
    ends={
        Property(name="SinkRole89", type=pcm_pc_av_composition_pc_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyEventConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__AssemblyEventConnector90: BinaryAssociation = BinaryAssociation(
    name="sourceRole__AssemblyEventConnector90",
    ends={
        Property(name="SourceRole92", type=pcm_pc_av_composition_pc_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyEventConnector91", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkAssemblyContext__AssemblyEventConnector93: BinaryAssociation = BinaryAssociation(
    name="sinkAssemblyContext__AssemblyEventConnector93",
    ends={
        Property(name="composition_pc_av_AssemblyContext95", type=pcm_pc_av_composition_pc_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyEventConnector94", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
sourceAssemblyContext__AssemblyEventConnector96: BinaryAssociation = BinaryAssociation(
    name="sourceAssemblyContext__AssemblyEventConnector96",
    ends={
        Property(name="composition_pc_av_AssemblyContext98", type=pcm_pc_av_composition_pc_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyEventConnector97", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__AssemblyEventConnector99: BinaryAssociation = BinaryAssociation(
    name="filterCondition__AssemblyEventConnector99",
    ends={
        Property(name="PCMRandomVariable100", type=pcm_pc_av_composition_pc_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblyEventConnector__FilterCondition", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
innerSourceRole__SourceRole101: BinaryAssociation = BinaryAssociation(
    name="innerSourceRole__SourceRole101",
    ends={
        Property(name="SourceRole102", type=pcm_pc_av_composition_pc_av_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_SourceDelegationConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSourceRole__SourceRole103: BinaryAssociation = BinaryAssociation(
    name="outerSourceRole__SourceRole103",
    ends={
        Property(name="SourceRole105", type=pcm_pc_av_composition_pc_av_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_SourceDelegationConnector104", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SourceDelegationConnector106: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SourceDelegationConnector106",
    ends={
        Property(name="composition_pc_av_AssemblyContext108", type=pcm_pc_av_composition_pc_av_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_SourceDelegationConnector107", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SinkDelegationConnector109: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SinkDelegationConnector109",
    ends={
        Property(name="composition_pc_av_AssemblyContext110", type=pcm_pc_av_composition_pc_av_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_SinkDelegationConnector", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext__AssemblyInfrastructureConnector120: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext__AssemblyInfrastructureConnector120",
    ends={
        Property(name="composition_pc_av_AssemblyContext122", type=pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector121", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext__AssemblyInfrastructureConnector123: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext__AssemblyInfrastructureConnector123",
    ends={
        Property(name="composition_pc_av_AssemblyContext125", type=pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector124", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole__ProvidedInfrastructureDelegationConnector126: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole__ProvidedInfrastructureDelegationConnector126",
    ends={
        Property(name="InfrastructureProvidedRole127", type=pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole__ProvidedInfrastructureDelegationConnector128: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole__ProvidedInfrastructureDelegationConnector128",
    ends={
        Property(name="InfrastructureProvidedRole130", type=pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector129", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__ProvidedInfrastructureDelegationConnector131: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__ProvidedInfrastructureDelegationConnector131",
    ends={
        Property(name="composition_pc_av_AssemblyContext133", type=pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector132", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole__RequiredInfrastructureDelegationConnector134: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredInfrastructureDelegationConnector134",
    ends={
        Property(name="InfrastructureRequiredRole135", type=pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredInfrastructureDelegationConnector136: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredInfrastructureDelegationConnector136",
    ends={
        Property(name="InfrastructureRequiredRole138", type=pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector137", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredInfrastructureDelegationConnector139: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredInfrastructureDelegationConnector139",
    ends={
        Property(name="composition_pc_av_AssemblyContext141", type=pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector140", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredResourceDelegationConnector142: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredResourceDelegationConnector142",
    ends={
        Property(name="composition_pc_av_AssemblyContext143", type=pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole__RequiredResourceDelegationConnector144: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredResourceDelegationConnector144",
    ends={
        Property(name="entity_pc_av_ResourceRequiredRole146", type=pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector145", type=entity_pc_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredResourceDelegationConnector147: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredResourceDelegationConnector147",
    ends={
        Property(name="entity_pc_av_ResourceRequiredRole149", type=pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector148", type=entity_pc_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure__AssemblyContext150: BinaryAssociation = BinaryAssociation(
    name="parentStructure__AssemblyContext150",
    ends={
        Property(name="ComposedStructure151", type=pcm_pc_av_composition_pc_av_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblyContexts__ComposedStructure", type=composition_pc_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
encapsulatedComponent__AssemblyContext152: BinaryAssociation = BinaryAssociation(
    name="encapsulatedComponent__AssemblyContext152",
    ends={
        Property(name="RepositoryComponent", type=pcm_pc_av_composition_pc_av_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyContext", type=RepositoryComponent, multiplicity=Multiplicity(0, 1))
    }
)
configParameterUsages__AssemblyContext153: BinaryAssociation = BinaryAssociation(
    name="configParameterUsages__AssemblyContext153",
    ends={
        Property(name="VariableUsage", type=pcm_pc_av_composition_pc_av_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblyContext__VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerSinkRole__SinkRole111: BinaryAssociation = BinaryAssociation(
    name="innerSinkRole__SinkRole111",
    ends={
        Property(name="SinkRole113", type=pcm_pc_av_composition_pc_av_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_SinkDelegationConnector112", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSinkRole__SinkRole114: BinaryAssociation = BinaryAssociation(
    name="outerSinkRole__SinkRole114",
    ends={
        Property(name="SinkRole116", type=pcm_pc_av_composition_pc_av_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_SinkDelegationConnector115", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
providedRole__AssemblyInfrastructureConnector117: BinaryAssociation = BinaryAssociation(
    name="providedRole__AssemblyInfrastructureConnector117",
    ends={
        Property(name="InfrastructureProvidedRole", type=pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__AssemblyInfrastructureConnector118: BinaryAssociation = BinaryAssociation(
    name="requiredRole__AssemblyInfrastructureConnector118",
    ends={
        Property(name="InfrastructureRequiredRole", type=pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector119", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UsageScenario155: BinaryAssociation = BinaryAssociation(
    name="usageModel_UsageScenario155",
    ends={
        Property(name="UsageModel", type=pcm_pc_av_usagemodel_pc_av_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="usageScenario_UsageModel", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
inputParameterUsages_EntryLevelSystemCall173: BinaryAssociation = BinaryAssociation(
    name="inputParameterUsages_EntryLevelSystemCall173",
    ends={
        Property(name="VariableUsage174", type=pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="entryLevelSystemCall_InputParameterUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scenarioBehaviour_UsageScenario156: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_UsageScenario156",
    ends={
        Property(name="ScenarioBehaviour", type=pcm_pc_av_usagemodel_pc_av_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="usageScenario_SenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
workload_UsageScenario157: BinaryAssociation = BinaryAssociation(
    name="workload_UsageScenario157",
    ends={
        Property(name="Workload", type=pcm_pc_av_usagemodel_pc_av_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="usageScenario_Workload", type=Workload, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
successor175: BinaryAssociation = BinaryAssociation(
    name="successor175",
    ends={
        Property(name="AbstractUserAction", type=pcm_pc_av_usagemodel_pc_av_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
predecessor176: BinaryAssociation = BinaryAssociation(
    name="predecessor176",
    ends={
        Property(name="AbstractUserAction177", type=pcm_pc_av_usagemodel_pc_av_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_userData158: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_userData158",
    ends={
        Property(name="composition_pc_av_AssemblyContext159", type=pcm_pc_av_usagemodel_pc_av_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_usagemodel_pc_av_UserData", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_AbstractUserAction178: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_AbstractUserAction178",
    ends={
        Property(name="ScenarioBehaviour179", type=pcm_pc_av_usagemodel_pc_av_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UserData160: BinaryAssociation = BinaryAssociation(
    name="usageModel_UserData160",
    ends={
        Property(name="UsageModel161", type=pcm_pc_av_usagemodel_pc_av_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="userData_UsageModel", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
userDataParameterUsages_UserData162: BinaryAssociation = BinaryAssociation(
    name="userDataParameterUsages_UserData162",
    ends={
        Property(name="VariableUsage163", type=pcm_pc_av_usagemodel_pc_av_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="userData_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_UsageModel164: BinaryAssociation = BinaryAssociation(
    name="usageScenario_UsageModel164",
    ends={
        Property(name="UsageScenario165", type=pcm_pc_av_usagemodel_pc_av_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="usageModel_UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_UsageModel166: BinaryAssociation = BinaryAssociation(
    name="userData_UsageModel166",
    ends={
        Property(name="UserData", type=pcm_pc_av_usagemodel_pc_av_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="usageModel_UserData", type=UserData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedRole_EntryLevelSystemCall167: BinaryAssociation = BinaryAssociation(
    name="providedRole_EntryLevelSystemCall167",
    ends={
        Property(name="OperationProvidedRole168", type=pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__EntryLevelSystemCall169: BinaryAssociation = BinaryAssociation(
    name="operationSignature__EntryLevelSystemCall169",
    ends={
        Property(name="OperationSignature", type=pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall170", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
usageScenario_Workload154: BinaryAssociation = BinaryAssociation(
    name="usageScenario_Workload154",
    ends={
        Property(name="UsageScenario", type=pcm_pc_av_usagemodel_pc_av_Workload, multiplicity=Multiplicity(1, 1)),
        Property(name="workload_UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
outputParameterUsages_EntryLevelSystemCall171: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsages_EntryLevelSystemCall171",
    ends={
        Property(name="VariableUsage172", type=pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="entryLevelSystemCall_OutputParameterUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branch_BranchTransition187: BinaryAssociation = BinaryAssociation(
    name="branch_BranchTransition187",
    ends={
        Property(name="Branch", type=pcm_pc_av_usagemodel_pc_av_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="branchTransitions_Branch", type=Branch, multiplicity=Multiplicity(0, 1))
    }
)
branchedBehaviour_BranchTransition188: BinaryAssociation = BinaryAssociation(
    name="branchedBehaviour_BranchTransition188",
    ends={
        Property(name="ScenarioBehaviour189", type=pcm_pc_av_usagemodel_pc_av_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="branchTransition_ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
usageScenario_SenarioBehaviour180: BinaryAssociation = BinaryAssociation(
    name="usageScenario_SenarioBehaviour180",
    ends={
        Property(name="UsageScenario181", type=pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="scenarioBehaviour_UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
branchTransition_ScenarioBehaviour182: BinaryAssociation = BinaryAssociation(
    name="branchTransition_ScenarioBehaviour182",
    ends={
        Property(name="BranchTransition", type=pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="branchedBehaviour_BranchTransition", type=BranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
loop_ScenarioBehaviour183: BinaryAssociation = BinaryAssociation(
    name="loop_ScenarioBehaviour183",
    ends={
        Property(name="Loop184", type=pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyBehaviour_Loop", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
actions_ScenarioBehaviour185: BinaryAssociation = BinaryAssociation(
    name="actions_ScenarioBehaviour185",
    ends={
        Property(name="AbstractUserAction186", type=pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="scenarioBehaviour_AbstractUserAction", type=AbstractUserAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interArrivalTime_OpenWorkload196: BinaryAssociation = BinaryAssociation(
    name="interArrivalTime_OpenWorkload196",
    ends={
        Property(name="PCMRandomVariable197", type=pcm_pc_av_usagemodel_pc_av_OpenWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="openWorkload_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchTransitions_Branch190: BinaryAssociation = BinaryAssociation(
    name="branchTransitions_Branch190",
    ends={
        Property(name="BranchTransition191", type=pcm_pc_av_usagemodel_pc_av_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="branch_BranchTransition", type=BranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopIteration_Loop192: BinaryAssociation = BinaryAssociation(
    name="loopIteration_Loop192",
    ends={
        Property(name="PCMRandomVariable193", type=pcm_pc_av_usagemodel_pc_av_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="loop_LoopIteration", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyBehaviour_Loop194: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop194",
    ends={
        Property(name="ScenarioBehaviour195", type=pcm_pc_av_usagemodel_pc_av_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="loop_ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicComponent_PassiveResource204: BinaryAssociation = BinaryAssociation(
    name="basicComponent_PassiveResource204",
    ends={
        Property(name="BasicComponent", type=pcm_pc_av_repository_pc_av_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="passiveResource_BasicComponent", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
resourceTimeoutFailureType__PassiveResource205: BinaryAssociation = BinaryAssociation(
    name="resourceTimeoutFailureType__PassiveResource205",
    ends={
        Property(name="ResourceTimeoutFailureType", type=pcm_pc_av_repository_pc_av_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="passiveResource__ResourceTimeoutFailureType", type=ResourceTimeoutFailureType, multiplicity=Multiplicity(0, 1))
    }
)
timeSpecification_Delay198: BinaryAssociation = BinaryAssociation(
    name="timeSpecification_Delay198",
    ends={
        Property(name="PCMRandomVariable199", type=pcm_pc_av_usagemodel_pc_av_Delay, multiplicity=Multiplicity(1, 1)),
        Property(name="delay_TimeSpecification", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thinkTime_ClosedWorkload200: BinaryAssociation = BinaryAssociation(
    name="thinkTime_ClosedWorkload200",
    ends={
        Property(name="PCMRandomVariable201", type=pcm_pc_av_usagemodel_pc_av_ClosedWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="closedWorkload_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capacity_PassiveResource202: BinaryAssociation = BinaryAssociation(
    name="capacity_PassiveResource202",
    ends={
        Property(name="PCMRandomVariable203", type=pcm_pc_av_repository_pc_av_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="passiveResource_capacity_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serviceEffectSpecifications__BasicComponent206: BinaryAssociation = BinaryAssociation(
    name="serviceEffectSpecifications__BasicComponent206",
    ends={
        Property(name="ServiceEffectSpecification", type=pcm_pc_av_repository_pc_av_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="basicComponent_ServiceEffectSpecification", type=ServiceEffectSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveResource_BasicComponent207: BinaryAssociation = BinaryAssociation(
    name="passiveResource_BasicComponent207",
    ends={
        Property(name="PassiveResource208", type=pcm_pc_av_repository_pc_av_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="basicComponent_PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceSignature__Parameter220: BinaryAssociation = BinaryAssociation(
    name="resourceSignature__Parameter220",
    ends={
        Property(name="ResourceSignature", type=pcm_pc_av_repository_pc_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter__ResourceSignature", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
repository__DataType221: BinaryAssociation = BinaryAssociation(
    name="repository__DataType221",
    ends={
        Property(name="Repository222", type=pcm_pc_av_repository_pc_av_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="dataTypes__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
components__Repository223: BinaryAssociation = BinaryAssociation(
    name="components__Repository223",
    ends={
        Property(name="RepositoryComponent224", type=pcm_pc_av_repository_pc_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__RepositoryComponent", type=RepositoryComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentCompleteComponentTypes209: BinaryAssociation = BinaryAssociation(
    name="parentCompleteComponentTypes209",
    ends={
        Property(name="CompleteComponentType", type=pcm_pc_av_repository_pc_av_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_ImplementationComponentType", type=CompleteComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
componentParameterUsage_ImplementationComponentType210: BinaryAssociation = BinaryAssociation(
    name="componentParameterUsage_ImplementationComponentType210",
    ends={
        Property(name="VariableUsage212", type=pcm_pc_av_repository_pc_av_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_ImplementationComponentType211", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository__RepositoryComponent213: BinaryAssociation = BinaryAssociation(
    name="repository__RepositoryComponent213",
    ends={
        Property(name="Repository", type=pcm_pc_av_repository_pc_av_RepositoryComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="components__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
providingEntity_ProvidedRole214: BinaryAssociation = BinaryAssociation(
    name="providingEntity_ProvidedRole214",
    ends={
        Property(name="InterfaceProvidingEntity", type=pcm_pc_av_repository_pc_av_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="providedRoles_InterfaceProvidingEntity", type=entity_pc_av_InterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
dataType__Parameter215: BinaryAssociation = BinaryAssociation(
    name="dataType__Parameter215",
    ends={
        Property(name="DataType", type=pcm_pc_av_repository_pc_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_Parameter", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureSignature__Parameter216: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignature__Parameter216",
    ends={
        Property(name="InfrastructureSignature", type=pcm_pc_av_repository_pc_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters__InfrastructureSignature", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__Parameter217: BinaryAssociation = BinaryAssociation(
    name="operationSignature__Parameter217",
    ends={
        Property(name="OperationSignature218", type=pcm_pc_av_repository_pc_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters__OperationSignature", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
eventType__Parameter219: BinaryAssociation = BinaryAssociation(
    name="eventType__Parameter219",
    ends={
        Property(name="EventType", type=pcm_pc_av_repository_pc_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter__EventType", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
requiredCharacterisations233: BinaryAssociation = BinaryAssociation(
    name="requiredCharacterisations233",
    ends={
        Property(name="RequiredCharacterisation", type=pcm_pc_av_repository_pc_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface_RequiredCharacterisation", type=RequiredCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository__Interface234: BinaryAssociation = BinaryAssociation(
    name="repository__Interface234",
    ends={
        Property(name="Repository235", type=pcm_pc_av_repository_pc_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interfaces__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
parameter236: BinaryAssociation = BinaryAssociation(
    name="parameter236",
    ends={
        Property(name="Parameter", type=pcm_pc_av_repository_pc_av_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_RequiredCharacterisation", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
interface_RequiredCharacterisation237: BinaryAssociation = BinaryAssociation(
    name="interface_RequiredCharacterisation237",
    ends={
        Property(name="Interface238", type=pcm_pc_av_repository_pc_av_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredCharacterisations", type=Interface, multiplicity=Multiplicity(0, 1))
    }
)
interfaces__Repository225: BinaryAssociation = BinaryAssociation(
    name="interfaces__Repository225",
    ends={
        Property(name="Interface", type=pcm_pc_av_repository_pc_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__Interface", type=Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureTypes__Repository226: BinaryAssociation = BinaryAssociation(
    name="failureTypes__Repository226",
    ends={
        Property(name="FailureType", type=pcm_pc_av_repository_pc_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__FailureType", type=FailureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes__Repository227: BinaryAssociation = BinaryAssociation(
    name="dataTypes__Repository227",
    ends={
        Property(name="DataType228", type=pcm_pc_av_repository_pc_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__DataType", type=DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentInterfaces__Interface229: BinaryAssociation = BinaryAssociation(
    name="parentInterfaces__Interface229",
    ends={
        Property(name="Interface230", type=pcm_pc_av_repository_pc_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_Interface", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
protocols__Interface231: BinaryAssociation = BinaryAssociation(
    name="protocols__Interface231",
    ends={
        Property(name="Protocol", type=pcm_pc_av_repository_pc_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_Interface232", type=Protocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters__InfrastructureSignature249: BinaryAssociation = BinaryAssociation(
    name="parameters__InfrastructureSignature249",
    ends={
        Property(name="Parameter250", type=pcm_pc_av_repository_pc_av_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureSignature__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureInterface__InfrastructureSignature251: BinaryAssociation = BinaryAssociation(
    name="infrastructureInterface__InfrastructureSignature251",
    ends={
        Property(name="InfrastructureInterface", type=pcm_pc_av_repository_pc_av_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureSignatures__InfrastructureInterface", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureSignatures__InfrastructureInterface252: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignatures__InfrastructureInterface252",
    ends={
        Property(name="InfrastructureSignature253", type=pcm_pc_av_repository_pc_av_InfrastructureInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureInterface__InfrastructureSignature", type=InfrastructureSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventTypes__EventGroup239: BinaryAssociation = BinaryAssociation(
    name="eventTypes__EventGroup239",
    ends={
        Property(name="EventType240", type=pcm_pc_av_repository_pc_av_EventGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="eventGroup__EventType", type=EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter__EventType241: BinaryAssociation = BinaryAssociation(
    name="parameter__EventType241",
    ends={
        Property(name="Parameter242", type=pcm_pc_av_repository_pc_av_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="eventType__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventGroup__EventType243: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventType243",
    ends={
        Property(name="EventGroup244", type=pcm_pc_av_repository_pc_av_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="eventTypes__EventGroup", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
exceptions__Signature245: BinaryAssociation = BinaryAssociation(
    name="exceptions__Signature245",
    ends={
        Property(name="ExceptionType", type=pcm_pc_av_repository_pc_av_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_Signature", type=ExceptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureType246: BinaryAssociation = BinaryAssociation(
    name="failureType246",
    ends={
        Property(name="FailureType248", type=pcm_pc_av_repository_pc_av_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_Signature247", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
signatures__OperationInterface262: BinaryAssociation = BinaryAssociation(
    name="signatures__OperationInterface262",
    ends={
        Property(name="OperationSignature263", type=pcm_pc_av_repository_pc_av_OperationInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface__OperationSignature", type=OperationSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterface__OperationRequiredRole264: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__OperationRequiredRole264",
    ends={
        Property(name="OperationInterface265", type=pcm_pc_av_repository_pc_av_OperationRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_OperationRequiredRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SourceRole266: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SourceRole266",
    ends={
        Property(name="EventGroup267", type=pcm_pc_av_repository_pc_av_SourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_SourceRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SinkRole268: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SinkRole268",
    ends={
        Property(name="EventGroup269", type=pcm_pc_av_repository_pc_av_SinkRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_SinkRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
requiredInterface__InfrastructureRequiredRole254: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__InfrastructureRequiredRole254",
    ends={
        Property(name="InfrastructureInterface255", type=pcm_pc_av_repository_pc_av_InfrastructureRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_InfrastructureRequiredRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface__OperationProvidedRole270: BinaryAssociation = BinaryAssociation(
    name="providedInterface__OperationProvidedRole270",
    ends={
        Property(name="OperationInterface271", type=pcm_pc_av_repository_pc_av_OperationProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_OperationProvidedRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
requiringEntity_RequiredRole256: BinaryAssociation = BinaryAssociation(
    name="requiringEntity_RequiredRole256",
    ends={
        Property(name="InterfaceRequiringEntity", type=pcm_pc_av_repository_pc_av_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredRoles_InterfaceRequiringEntity", type=entity_pc_av_InterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
interface__OperationSignature257: BinaryAssociation = BinaryAssociation(
    name="interface__OperationSignature257",
    ends={
        Property(name="OperationInterface", type=pcm_pc_av_repository_pc_av_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signatures__OperationInterface", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
parameters__OperationSignature258: BinaryAssociation = BinaryAssociation(
    name="parameters__OperationSignature258",
    ends={
        Property(name="Parameter259", type=pcm_pc_av_repository_pc_av_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="operationSignature__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType__OperationSignature260: BinaryAssociation = BinaryAssociation(
    name="returnType__OperationSignature260",
    ends={
        Property(name="DataType261", type=pcm_pc_av_repository_pc_av_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_OperationSignature", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
parentProvidesComponentTypes274: BinaryAssociation = BinaryAssociation(
    name="parentProvidesComponentTypes274",
    ends={
        Property(name="ProvidesComponentType", type=pcm_pc_av_repository_pc_av_CompleteComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_CompleteComponentType", type=ProvidesComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
providedInterface__InfrastructureProvidedRole272: BinaryAssociation = BinaryAssociation(
    name="providedInterface__InfrastructureProvidedRole272",
    ends={
        Property(name="InfrastructureInterface273", type=pcm_pc_av_repository_pc_av_InfrastructureProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_InfrastructureProvidedRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
parentType_CompositeDataType277: BinaryAssociation = BinaryAssociation(
    name="parentType_CompositeDataType277",
    ends={
        Property(name="CompositeDataType", type=pcm_pc_av_repository_pc_av_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 9999))
    }
)
innerDeclaration_CompositeDataType278: BinaryAssociation = BinaryAssociation(
    name="innerDeclaration_CompositeDataType278",
    ends={
        Property(name="InnerDeclaration", type=pcm_pc_av_repository_pc_av_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeDataType_InnerDeclaration", type=InnerDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype_InnerDeclaration279: BinaryAssociation = BinaryAssociation(
    name="datatype_InnerDeclaration279",
    ends={
        Property(name="DataType280", type=pcm_pc_av_repository_pc_av_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_InnerDeclaration", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
compositeDataType_InnerDeclaration281: BinaryAssociation = BinaryAssociation(
    name="compositeDataType_InnerDeclaration281",
    ends={
        Property(name="CompositeDataType282", type=pcm_pc_av_repository_pc_av_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="innerDeclaration_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 1))
    }
)
innerType_CollectionDataType275: BinaryAssociation = BinaryAssociation(
    name="innerType_CollectionDataType275",
    ends={
        Property(name="DataType276", type=pcm_pc_av_repository_pc_av_CollectionDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_repository_pc_av_CollectionDataType", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaces__ResourceRepository289: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaces__ResourceRepository289",
    ends={
        Property(name="ResourceInterface290", type=pcm_pc_av_resourcetype_pc_av_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRepository__ResourceInterface", type=ResourceInterface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schedulingPolicies__ResourceRepository291: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicies__ResourceRepository291",
    ends={
        Property(name="SchedulingPolicy", type=pcm_pc_av_resourcetype_pc_av_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRepository__SchedulingPolicy", type=SchedulingPolicy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
availableResourceTypes_ResourceRepository292: BinaryAssociation = BinaryAssociation(
    name="availableResourceTypes_ResourceRepository292",
    ends={
        Property(name="ResourceType", type=pcm_pc_av_resourcetype_pc_av_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRepository_ResourceType", type=ResourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRepository__SchedulingPolicy293: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__SchedulingPolicy293",
    ends={
        Property(name="ResourceRepository294", type=pcm_pc_av_resourcetype_pc_av_SchedulingPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="schedulingPolicies__ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
networkInducedFailureType__CommunicationLinkResourceType295: BinaryAssociation = BinaryAssociation(
    name="networkInducedFailureType__CommunicationLinkResourceType295",
    ends={
        Property(name="NetworkInducedFailureType", type=pcm_pc_av_resourcetype_pc_av_CommunicationLinkResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceType__NetworkInducedFailureType", type=NetworkInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
resourceRepository__ResourceInterface296: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__ResourceInterface296",
    ends={
        Property(name="ResourceRepository297", type=pcm_pc_av_resourcetype_pc_av_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterfaces__ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
parameter__ResourceSignature283: BinaryAssociation = BinaryAssociation(
    name="parameter__ResourceSignature283",
    ends={
        Property(name="Parameter284", type=pcm_pc_av_resourcetype_pc_av_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceSignature__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceInterface__ResourceSignature285: BinaryAssociation = BinaryAssociation(
    name="resourceInterface__ResourceSignature285",
    ends={
        Property(name="ResourceInterface286", type=pcm_pc_av_resourcetype_pc_av_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceSignatures__ResourceInterface", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
hardwareInducedFailureType__ProcessingResourceType287: BinaryAssociation = BinaryAssociation(
    name="hardwareInducedFailureType__ProcessingResourceType287",
    ends={
        Property(name="HardwareInducedFailureType", type=pcm_pc_av_resourcetype_pc_av_ProcessingResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="processingResourceType__HardwareInducedFailureType", type=HardwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
resourceRepository_ResourceType288: BinaryAssociation = BinaryAssociation(
    name="resourceRepository_ResourceType288",
    ends={
        Property(name="ResourceRepository", type=pcm_pc_av_resourcetype_pc_av_ResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="availableResourceTypes_ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_InputParameterUsage311: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_InputParameterUsage311",
    ends={
        Property(name="EntryLevelSystemCall", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="inputParameterUsages_EntryLevelSystemCall", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_OutputParameterUsage312: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_OutputParameterUsage312",
    ends={
        Property(name="EntryLevelSystemCall313", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="outputParameterUsages_EntryLevelSystemCall", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
namedReference__VariableUsage314: BinaryAssociation = BinaryAssociation(
    name="namedReference__VariableUsage314",
    ends={
        Property(name="parameter_pc_av_pcm_pc_av_AbstractNamedReference", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_parameter_pc_av_VariableUsage", type=parameter_pc_av_pcm_pc_av_AbstractNamedReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification_VariableCharacterisation315: BinaryAssociation = BinaryAssociation(
    name="specification_VariableCharacterisation315",
    ends={
        Property(name="PCMRandomVariable316", type=pcm_pc_av_parameter_pc_av_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="variableCharacterisation_Specification", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableUsage_VariableCharacterisation317: BinaryAssociation = BinaryAssociation(
    name="variableUsage_VariableCharacterisation317",
    ends={
        Property(name="VariableUsage318", type=pcm_pc_av_parameter_pc_av_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="variableCharacterisation_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 1))
    }
)
resourceSignatures__ResourceInterface298: BinaryAssociation = BinaryAssociation(
    name="resourceSignatures__ResourceInterface298",
    ends={
        Property(name="ResourceSignature299", type=pcm_pc_av_resourcetype_pc_av_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterface__ResourceSignature", type=ResourceSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableCharacterisation_VariableUsage300: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_VariableUsage300",
    ends={
        Property(name="VariableCharacterisation301", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="variableUsage_VariableCharacterisation", type=VariableCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_VariableUsage302: BinaryAssociation = BinaryAssociation(
    name="userData_VariableUsage302",
    ends={
        Property(name="UserData303", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="userDataParameterUsages_UserData", type=UserData, multiplicity=Multiplicity(0, 1))
    }
)
callAction__VariableUsage304: BinaryAssociation = BinaryAssociation(
    name="callAction__VariableUsage304",
    ends={
        Property(name="CallAction", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="inputVariableUsages__CallAction", type=CallAction, multiplicity=Multiplicity(0, 1))
    }
)
synchronisationPoint_VariableUsage305: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_VariableUsage305",
    ends={
        Property(name="SynchronisationPoint", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="outputParameterUsage_SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
callReturnAction__VariableUsage306: BinaryAssociation = BinaryAssociation(
    name="callReturnAction__VariableUsage306",
    ends={
        Property(name="CallReturnAction", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="returnVariableUsage__CallReturnAction", type=CallReturnAction, multiplicity=Multiplicity(0, 1))
    }
)
setVariableAction_VariableUsage307: BinaryAssociation = BinaryAssociation(
    name="setVariableAction_VariableUsage307",
    ends={
        Property(name="SetVariableAction", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="localVariableUsages_SetVariableAction", type=SetVariableAction, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage308: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage308",
    ends={
        Property(name="SpecifiedOutputParameterAbstraction", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__VariableUsage309: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__VariableUsage309",
    ends={
        Property(name="AssemblyContext310", type=pcm_pc_av_parameter_pc_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="configParameterUsages__AssemblyContext", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceType__HardwareInducedFailureType319: BinaryAssociation = BinaryAssociation(
    name="processingResourceType__HardwareInducedFailureType319",
    ends={
        Property(name="ProcessingResourceType", type=pcm_pc_av_reliability_pc_av_HardwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="hardwareInducedFailureType__ProcessingResourceType", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
internalFailureOccurrenceDescriptions__SoftwareInducedFailureType320: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__SoftwareInducedFailureType320",
    ends={
        Property(name="InternalFailureOccurrenceDescription", type=pcm_pc_av_reliability_pc_av_SoftwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="softwareInducedFailureType__InternalFailureOccurrenceDescription", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999))
    }
)
passiveResource__ResourceTimeoutFailureType327: BinaryAssociation = BinaryAssociation(
    name="passiveResource__ResourceTimeoutFailureType327",
    ends={
        Property(name="PassiveResource328", type=pcm_pc_av_reliability_pc_av_ResourceTimeoutFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceTimeoutFailureType__PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
repository__FailureType329: BinaryAssociation = BinaryAssociation(
    name="repository__FailureType329",
    ends={
        Property(name="Repository330", type=pcm_pc_av_reliability_pc_av_FailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="failureTypes__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
internalAction__InternalFailureOccurrenceDescription321: BinaryAssociation = BinaryAssociation(
    name="internalAction__InternalFailureOccurrenceDescription321",
    ends={
        Property(name="InternalAction", type=pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="internalFailureOccurrenceDescriptions__InternalAction", type=InternalAction, multiplicity=Multiplicity(0, 1))
    }
)
softwareInducedFailureType__InternalFailureOccurrenceDescription322: BinaryAssociation = BinaryAssociation(
    name="softwareInducedFailureType__InternalFailureOccurrenceDescription322",
    ends={
        Property(name="SoftwareInducedFailureType", type=pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="internalFailureOccurrenceDescriptions__SoftwareInducedFailureType", type=SoftwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceType__NetworkInducedFailureType323: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType__NetworkInducedFailureType323",
    ends={
        Property(name="CommunicationLinkResourceType", type=pcm_pc_av_reliability_pc_av_NetworkInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="networkInducedFailureType__CommunicationLinkResourceType", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription324: BinaryAssociation = BinaryAssociation(
    name="specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription324",
    ends={
        Property(name="SpecifiedReliabilityAnnotation", type=pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation", type=qos_reliability_pc_av_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(0, 1))
    }
)
failureType__ExternalFailureOccurrenceDescription325: BinaryAssociation = BinaryAssociation(
    name="failureType__ExternalFailureOccurrenceDescription325",
    ends={
        Property(name="FailureType326", type=pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription", type=FailureType, multiplicity=Multiplicity(0, 1))
    }
)
abstractLoopAction_ResourceDemandingBehaviour341: BinaryAssociation = BinaryAssociation(
    name="abstractLoopAction_ResourceDemandingBehaviour341",
    ends={
        Property(name="AbstractLoopAction", type=pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyBehaviour_Loop342", type=AbstractLoopAction, multiplicity=Multiplicity(0, 1))
    }
)
abstractBranchTransition_ResourceDemandingBehaviour343: BinaryAssociation = BinaryAssociation(
    name="abstractBranchTransition_ResourceDemandingBehaviour343",
    ends={
        Property(name="AbstractBranchTransition", type=pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="branchBehaviour_BranchTransition", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
steps_Behaviour344: BinaryAssociation = BinaryAssociation(
    name="steps_Behaviour344",
    ends={
        Property(name="AbstractAction345", type=pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemandingBehaviour_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceDemand_Action331: BinaryAssociation = BinaryAssociation(
    name="resourceDemand_Action331",
    ends={
        Property(name="ParametricResourceDemand332", type=pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="action_ParametricResourceDemand", type=seff_performance_pc_av_ParametricResourceDemand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureCall__Action333: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__Action333",
    ends={
        Property(name="InfrastructureCall334", type=pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="action__InfrastructureCall", type=seff_performance_pc_av_InfrastructureCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceCall__Action335: BinaryAssociation = BinaryAssociation(
    name="resourceCall__Action335",
    ends={
        Property(name="ResourceCall336", type=pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="action__ResourceCall", type=seff_performance_pc_av_ResourceCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor_AbstractAction337: BinaryAssociation = BinaryAssociation(
    name="predecessor_AbstractAction337",
    ends={
        Property(name="AbstractAction", type=pcm_pc_av_seff_pc_av_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="successor_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
successor_AbstractAction338: BinaryAssociation = BinaryAssociation(
    name="successor_AbstractAction338",
    ends={
        Property(name="AbstractAction339", type=pcm_pc_av_seff_pc_av_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemandingBehaviour_AbstractAction340: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingBehaviour_AbstractAction340",
    ends={
        Property(name="ResourceDemandingBehaviour", type=pcm_pc_av_seff_pc_av_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="steps_Behaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
branches_Branch351: BinaryAssociation = BinaryAssociation(
    name="branches_Branch351",
    ends={
        Property(name="AbstractBranchTransition352", type=pcm_pc_av_seff_pc_av_BranchAction, multiplicity=Multiplicity(1, 1)),
        Property(name="branchAction_AbstractBranchTransition", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputVariableUsages__CallAction353: BinaryAssociation = BinaryAssociation(
    name="inputVariableUsages__CallAction353",
    ends={
        Property(name="VariableUsage354", type=pcm_pc_av_seff_pc_av_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="callAction__VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyBehaviour_Loop346: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop346",
    ends={
        Property(name="ResourceDemandingBehaviour347", type=pcm_pc_av_seff_pc_av_AbstractLoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractLoopAction_ResourceDemandingBehaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchAction_AbstractBranchTransition348: BinaryAssociation = BinaryAssociation(
    name="branchAction_AbstractBranchTransition348",
    ends={
        Property(name="BranchAction", type=pcm_pc_av_seff_pc_av_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="branches_Branch", type=BranchAction, multiplicity=Multiplicity(0, 1))
    }
)
branchBehaviour_BranchTransition349: BinaryAssociation = BinaryAssociation(
    name="branchBehaviour_BranchTransition349",
    ends={
        Property(name="ResourceDemandingBehaviour350", type=pcm_pc_av_seff_pc_av_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractBranchTransition_ResourceDemandingBehaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterationCount_LoopAction362: BinaryAssociation = BinaryAssociation(
    name="iterationCount_LoopAction362",
    ends={
        Property(name="PCMRandomVariable363", type=pcm_pc_av_seff_pc_av_LoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="loopAction_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
asynchronousForkedBehaviours_ForkAction364: BinaryAssociation = BinaryAssociation(
    name="asynchronousForkedBehaviours_ForkAction364",
    ends={
        Property(name="ForkedBehaviour", type=pcm_pc_av_seff_pc_av_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="forkAction_ForkedBehaivour", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronisingBehaviours_ForkAction365: BinaryAssociation = BinaryAssociation(
    name="synchronisingBehaviours_ForkAction365",
    ends={
        Property(name="SynchronisationPoint366", type=pcm_pc_av_seff_pc_av_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="forkAction_SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
synchronisationPoint_ForkedBehaviour367: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_ForkedBehaviour367",
    ends={
        Property(name="SynchronisationPoint368", type=pcm_pc_av_seff_pc_av_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronousForkedBehaviours_SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
forkAction_ForkedBehaivour369: BinaryAssociation = BinaryAssociation(
    name="forkAction_ForkedBehaivour369",
    ends={
        Property(name="ForkAction", type=pcm_pc_av_seff_pc_av_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="asynchronousForkedBehaviours_ForkAction", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
describedService__SEFF355: BinaryAssociation = BinaryAssociation(
    name="describedService__SEFF355",
    ends={
        Property(name="Signature", type=pcm_pc_av_seff_pc_av_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_pc_av_ServiceEffectSpecification", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
basicComponent_ServiceEffectSpecification356: BinaryAssociation = BinaryAssociation(
    name="basicComponent_ServiceEffectSpecification356",
    ends={
        Property(name="BasicComponent357", type=pcm_pc_av_seff_pc_av_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="serviceEffectSpecifications__BasicComponent", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemandingInternalBehaviours358: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingInternalBehaviours358",
    ends={
        Property(name="ResourceDemandingInternalBehaviour", type=pcm_pc_av_seff_pc_av_ResourceDemandingSEFF, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemandingSEFF_ResourceDemandingInternalBehaviour", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceDemandingSEFF_ResourceDemandingInternalBehaviour359: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingSEFF_ResourceDemandingInternalBehaviour359",
    ends={
        Property(name="ResourceDemandingSEFF", type=pcm_pc_av_seff_pc_av_ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemandingInternalBehaviours", type=ResourceDemandingSEFF, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_ReleaseAction360: BinaryAssociation = BinaryAssociation(
    name="passiveResource_ReleaseAction360",
    ends={
        Property(name="PassiveResource361", type=pcm_pc_av_seff_pc_av_ReleaseAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_pc_av_ReleaseAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
role_ExternalService378: BinaryAssociation = BinaryAssociation(
    name="role_ExternalService378",
    ends={
        Property(name="OperationRequiredRole380", type=pcm_pc_av_seff_pc_av_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_pc_av_ExternalCallAction379", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
returnVariableUsage__CallReturnAction381: BinaryAssociation = BinaryAssociation(
    name="returnVariableUsage__CallReturnAction381",
    ends={
        Property(name="VariableUsage382", type=pcm_pc_av_seff_pc_av_CallReturnAction, multiplicity=Multiplicity(1, 1)),
        Property(name="callReturnAction__VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputParameterUsage_SynchronisationPoint370: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsage_SynchronisationPoint370",
    ends={
        Property(name="VariableUsage371", type=pcm_pc_av_seff_pc_av_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronisationPoint_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forkAction_SynchronisationPoint372: BinaryAssociation = BinaryAssociation(
    name="forkAction_SynchronisationPoint372",
    ends={
        Property(name="ForkAction373", type=pcm_pc_av_seff_pc_av_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronisingBehaviours_ForkAction", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
synchronousForkedBehaviours_SynchronisationPoint374: BinaryAssociation = BinaryAssociation(
    name="synchronousForkedBehaviours_SynchronisationPoint374",
    ends={
        Property(name="ForkedBehaviour375", type=pcm_pc_av_seff_pc_av_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronisationPoint_ForkedBehaviour", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledService_ExternalService376: BinaryAssociation = BinaryAssociation(
    name="calledService_ExternalService376",
    ends={
        Property(name="OperationSignature377", type=pcm_pc_av_seff_pc_av_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_pc_av_ExternalCallAction", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
eventType__EmitEventAction393: BinaryAssociation = BinaryAssociation(
    name="eventType__EmitEventAction393",
    ends={
        Property(name="EventType394", type=pcm_pc_av_seff_pc_av_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_pc_av_EmitEventAction", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EmitEventAction395: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EmitEventAction395",
    ends={
        Property(name="SourceRole397", type=pcm_pc_av_seff_pc_av_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_pc_av_EmitEventAction396", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
passiveresource_AcquireAction383: BinaryAssociation = BinaryAssociation(
    name="passiveresource_AcquireAction383",
    ends={
        Property(name="PassiveResource384", type=pcm_pc_av_seff_pc_av_AcquireAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_pc_av_AcquireAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
parameter_CollectionIteratorAction385: BinaryAssociation = BinaryAssociation(
    name="parameter_CollectionIteratorAction385",
    ends={
        Property(name="Parameter386", type=pcm_pc_av_seff_pc_av_CollectionIteratorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_pc_av_CollectionIteratorAction", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
branchCondition_GuardedBranchTransition387: BinaryAssociation = BinaryAssociation(
    name="branchCondition_GuardedBranchTransition387",
    ends={
        Property(name="PCMRandomVariable388", type=pcm_pc_av_seff_pc_av_GuardedBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="guardedBranchTransition_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localVariableUsages_SetVariableAction389: BinaryAssociation = BinaryAssociation(
    name="localVariableUsages_SetVariableAction389",
    ends={
        Property(name="VariableUsage390", type=pcm_pc_av_seff_pc_av_SetVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="setVariableAction_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledResourceDemandingInternalBehaviour391: BinaryAssociation = BinaryAssociation(
    name="calledResourceDemandingInternalBehaviour391",
    ends={
        Property(name="ResourceDemandingInternalBehaviour392", type=pcm_pc_av_seff_pc_av_InternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_pc_av_InternalCallAction", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
internalFailureOccurrenceDescriptions__InternalAction398: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__InternalAction398",
    ends={
        Property(name="InternalFailureOccurrenceDescription399", type=pcm_pc_av_seff_pc_av_InternalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="internalAction__InternalFailureOccurrenceDescription", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action__ResourceCall408: BinaryAssociation = BinaryAssociation(
    name="action__ResourceCall408",
    ends={
        Property(name="AbstractInternalControlFlowAction409", type=pcm_pc_av_seff_performance_pc_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceCall__Action", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceRequiredRole__ResourceCall410: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRole__ResourceCall410",
    ends={
        Property(name="entity_pc_av_ResourceRequiredRole411", type=pcm_pc_av_seff_performance_pc_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_performance_pc_av_ResourceCall", type=entity_pc_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
signature__ResourceCall412: BinaryAssociation = BinaryAssociation(
    name="signature__ResourceCall412",
    ends={
        Property(name="ResourceSignature414", type=pcm_pc_av_seff_performance_pc_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_performance_pc_av_ResourceCall413", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
signature__InfrastructureCall400: BinaryAssociation = BinaryAssociation(
    name="signature__InfrastructureCall400",
    ends={
        Property(name="InfrastructureSignature401", type=pcm_pc_av_seff_performance_pc_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_performance_pc_av_InfrastructureCall", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__InfrastructureCall402: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__InfrastructureCall402",
    ends={
        Property(name="PCMRandomVariable403", type=pcm_pc_av_seff_performance_pc_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureCall__PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action__InfrastructureCall404: BinaryAssociation = BinaryAssociation(
    name="action__InfrastructureCall404",
    ends={
        Property(name="AbstractInternalControlFlowAction", type=pcm_pc_av_seff_performance_pc_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureCall__Action", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__InfrastructureCall405: BinaryAssociation = BinaryAssociation(
    name="requiredRole__InfrastructureCall405",
    ends={
        Property(name="InfrastructureRequiredRole407", type=pcm_pc_av_seff_performance_pc_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_performance_pc_av_InfrastructureCall406", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredResource_ParametricResourceDemand419: BinaryAssociation = BinaryAssociation(
    name="requiredResource_ParametricResourceDemand419",
    ends={
        Property(name="ProcessingResourceType420", type=pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
action_ParametricResourceDemand421: BinaryAssociation = BinaryAssociation(
    name="action_ParametricResourceDemand421",
    ends={
        Property(name="AbstractInternalControlFlowAction422", type=pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemand_Action", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__ResourceCall415: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__ResourceCall415",
    ends={
        Property(name="PCMRandomVariable416", type=pcm_pc_av_seff_performance_pc_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceCall__PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification_ParametericResourceDemand417: BinaryAssociation = BinaryAssociation(
    name="specification_ParametericResourceDemand417",
    ends={
        Property(name="PCMRandomVariable418", type=pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="parametricResourceDemand_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primaryBehaviour__RecoveryAction425: BinaryAssociation = BinaryAssociation(
    name="primaryBehaviour__RecoveryAction425",
    ends={
        Property(name="seff_reliability_pc_av_RecoveryActionBehaviour426", type=pcm_pc_av_seff_reliability_pc_av_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_reliability_pc_av_RecoveryAction", type=seff_reliability_pc_av_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
recoveryActionBehaviours__RecoveryAction427: BinaryAssociation = BinaryAssociation(
    name="recoveryActionBehaviours__RecoveryAction427",
    ends={
        Property(name="RecoveryActionBehaviour", type=pcm_pc_av_seff_reliability_pc_av_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="recoveryAction__RecoveryActionBehaviour", type=seff_reliability_pc_av_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureTypes_FailureHandlingEntity428: BinaryAssociation = BinaryAssociation(
    name="failureTypes_FailureHandlingEntity428",
    ends={
        Property(name="FailureType429", type=pcm_pc_av_seff_reliability_pc_av_FailureHandlingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_reliability_pc_av_FailureHandlingEntity", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
failureHandlingAlternatives__RecoveryActionBehaviour423: BinaryAssociation = BinaryAssociation(
    name="failureHandlingAlternatives__RecoveryActionBehaviour423",
    ends={
        Property(name="seff_reliability_pc_av_RecoveryActionBehaviour", type=pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour", type=seff_reliability_pc_av_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999))
    }
)
recoveryAction__RecoveryActionBehaviour424: BinaryAssociation = BinaryAssociation(
    name="recoveryAction__RecoveryActionBehaviour424",
    ends={
        Property(name="RecoveryAction", type=pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="recoveryActionBehaviours__RecoveryAction", type=seff_reliability_pc_av_RecoveryAction, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstractions_QoSAnnotations435: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstractions_QoSAnnotations435",
    ends={
        Property(name="SpecifiedOutputParameterAbstraction436", type=pcm_pc_av_qosannotations_pc_av_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="qosAnnotations_SpecifiedOutputParameterAbstraction", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
system_QoSAnnotations437: BinaryAssociation = BinaryAssociation(
    name="system_QoSAnnotations437",
    ends={
        Property(name="System", type=pcm_pc_av_qosannotations_pc_av_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="qosAnnotations_System", type=System, multiplicity=Multiplicity(0, 1))
    }
)
specifiedQoSAnnotations_QoSAnnotations438: BinaryAssociation = BinaryAssociation(
    name="specifiedQoSAnnotations_QoSAnnotations438",
    ends={
        Property(name="SpecifiedQoSAnnotation", type=pcm_pc_av_qosannotations_pc_av_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="qosAnnotations_SpecifiedQoSAnnotation", type=SpecifiedQoSAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature_SpecifiedOutputParameterAbstraction439: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedOutputParameterAbstraction439",
    ends={
        Property(name="Signature440", type=pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedOutputParameterAbstraction441: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedOutputParameterAbstraction441",
    ends={
        Property(name="Role443", type=pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction442", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
expectedExternalOutputs_SpecifiedOutputParameterAbstraction444: BinaryAssociation = BinaryAssociation(
    name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction444",
    ends={
        Property(name="VariableUsage445", type=pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qosAnnotations_SpecifiedOutputParameterAbstraction446: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedOutputParameterAbstraction446",
    ends={
        Property(name="QoSAnnotations447", type=pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedOutputParameterAbstractions_QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
signature_SpecifiedQoSAnnation430: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedQoSAnnation430",
    ends={
        Property(name="Signature431", type=pcm_pc_av_qosannotations_pc_av_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_qosannotations_pc_av_SpecifiedQoSAnnotation", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedQoSAnnotation432: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedQoSAnnotation432",
    ends={
        Property(name="Role", type=pcm_pc_av_qosannotations_pc_av_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_qosannotations_pc_av_SpecifiedQoSAnnotation433", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
qosAnnotations_SpecifiedQoSAnnotation434: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedQoSAnnotation434",
    ends={
        Property(name="QoSAnnotations", type=pcm_pc_av_qosannotations_pc_av_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedQoSAnnotations_QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation452: BinaryAssociation = BinaryAssociation(
    name="externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation452",
    ends={
        Property(name="ExternalFailureOccurrenceDescription", type=pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription", type=ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification_SpecifiedExecutionTime448: BinaryAssociation = BinaryAssociation(
    name="specification_SpecifiedExecutionTime448",
    ends={
        Property(name="PCMRandomVariable449", type=pcm_pc_av_qos_performance_pc_av_SpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedExecutionTime_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext_ComponentSpecifiedExecutionTime450: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ComponentSpecifiedExecutionTime450",
    ends={
        Property(name="composition_pc_av_AssemblyContext451", type=pcm_pc_av_qos_performance_pc_av_ComponentSpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_qos_performance_pc_av_ComponentSpecifiedExecutionTime", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecifications_LinkingResource459: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifications_LinkingResource459",
    ends={
        Property(name="CommunicationLinkResourceSpecification460", type=pcm_pc_av_resourceenvironment_pc_av_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="linkingResource_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceEnvironment_LinkingResource461: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_LinkingResource461",
    ends={
        Property(name="ResourceEnvironment", type=pcm_pc_av_resourceenvironment_pc_av_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="linkingResources__ResourceEnvironment", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceSpecifications_ResourceContainer462: BinaryAssociation = BinaryAssociation(
    name="activeResourceSpecifications_ResourceContainer462",
    ends={
        Property(name="ProcessingResourceSpecification463", type=pcm_pc_av_resourceenvironment_pc_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceContainer_ProcessingResourceSpecification", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qosAnnotations_System453: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_System453",
    ends={
        Property(name="QoSAnnotations454", type=pcm_pc_av_system_pc_av_System, multiplicity=Multiplicity(1, 1)),
        Property(name="system_QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkingResources__ResourceEnvironment455: BinaryAssociation = BinaryAssociation(
    name="linkingResources__ResourceEnvironment455",
    ends={
        Property(name="LinkingResource", type=pcm_pc_av_resourceenvironment_pc_av_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceEnvironment_LinkingResource", type=LinkingResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_ResourceEnvironment456: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ResourceEnvironment456",
    ends={
        Property(name="ResourceContainer", type=pcm_pc_av_resourceenvironment_pc_av_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceEnvironment_ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectedResourceContainers_LinkingResource457: BinaryAssociation = BinaryAssociation(
    name="connectedResourceContainers_LinkingResource457",
    ends={
        Property(name="ResourceContainer458", type=pcm_pc_av_resourceenvironment_pc_av_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_resourceenvironment_pc_av_LinkingResource", type=ResourceContainer, multiplicity=Multiplicity(0, 9999))
    }
)
schedulingPolicy470: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicy470",
    ends={
        Property(name="SchedulingPolicy471", type=pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification", type=SchedulingPolicy, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceType_ActiveResourceSpecification472: BinaryAssociation = BinaryAssociation(
    name="activeResourceType_ActiveResourceSpecification472",
    ends={
        Property(name="ProcessingResourceType474", type=pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification473", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
processingRate_ProcessingResourceSpecification475: BinaryAssociation = BinaryAssociation(
    name="processingRate_ProcessingResourceSpecification475",
    ends={
        Property(name="PCMRandomVariable476", type=pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="processingResourceSpecification_processingRate_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceContainer_ProcessingResourceSpecification477: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ProcessingResourceSpecification477",
    ends={
        Property(name="ResourceContainer478", type=pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="activeResourceSpecifications_ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
linkingResource_CommunicationLinkResourceSpecification479: BinaryAssociation = BinaryAssociation(
    name="linkingResource_CommunicationLinkResourceSpecification479",
    ends={
        Property(name="LinkingResource480", type=pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceSpecifications_LinkingResource", type=LinkingResource, multiplicity=Multiplicity(0, 1))
    }
)
resourceEnvironment_ResourceContainer464: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_ResourceContainer464",
    ends={
        Property(name="ResourceEnvironment465", type=pcm_pc_av_resourceenvironment_pc_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceContainer_ResourceEnvironment", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
nestedResourceContainers__ResourceContainer466: BinaryAssociation = BinaryAssociation(
    name="nestedResourceContainers__ResourceContainer466",
    ends={
        Property(name="ResourceContainer467", type=pcm_pc_av_resourceenvironment_pc_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="parentResourceContainer__ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentResourceContainer__ResourceContainer468: BinaryAssociation = BinaryAssociation(
    name="parentResourceContainer__ResourceContainer468",
    ends={
        Property(name="ResourceContainer469", type=pcm_pc_av_resourceenvironment_pc_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedResourceContainers__ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
resourceContainer_AllocationContext487: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_AllocationContext487",
    ends={
        Property(name="ResourceContainer488", type=pcm_pc_av_allocation_pc_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_allocation_pc_av_AllocationContext", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_AllocationContext489: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_AllocationContext489",
    ends={
        Property(name="composition_pc_av_AssemblyContext491", type=pcm_pc_av_allocation_pc_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_allocation_pc_av_AllocationContext490", type=composition_pc_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
allocation_AllocationContext492: BinaryAssociation = BinaryAssociation(
    name="allocation_AllocationContext492",
    ends={
        Property(name="Allocation", type=pcm_pc_av_allocation_pc_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="allocationContexts_Allocation", type=Allocation, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__AllocationContext493: BinaryAssociation = BinaryAssociation(
    name="eventChannel__AllocationContext493",
    ends={
        Property(name="composition_pc_av_EventChannel", type=pcm_pc_av_allocation_pc_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_allocation_pc_av_AllocationContext494", type=composition_pc_av_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceType_CommunicationLinkResourceSpecification481: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType_CommunicationLinkResourceSpecification481",
    ends={
        Property(name="CommunicationLinkResourceType482", type=pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
latency_CommunicationLinkResourceSpecification483: BinaryAssociation = BinaryAssociation(
    name="latency_CommunicationLinkResourceSpecification483",
    ends={
        Property(name="PCMRandomVariable484", type=pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceSpecification_latency_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throughput_CommunicationLinkResourceSpecification485: BinaryAssociation = BinaryAssociation(
    name="throughput_CommunicationLinkResourceSpecification485",
    ends={
        Property(name="PCMRandomVariable486", type=pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceSpecifcation_throughput_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
completions_CompletionRepository501: BinaryAssociation = BinaryAssociation(
    name="completions_CompletionRepository501",
    ends={
        Property(name="Completion", type=pcm_pc_av_completions_pc_av_CompletionRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_completions_pc_av_CompletionRepository", type=Completion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCommunicationLinkResource_ParametricResourceDemand502: BinaryAssociation = BinaryAssociation(
    name="requiredCommunicationLinkResource_ParametricResourceDemand502",
    ends={
        Property(name="CommunicationLinkResourceType503", type=pcm_pc_av_completions_pc_av_NetworkDemandParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_completions_pc_av_NetworkDemandParametricResourceDemand", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
targetResourceEnvironment_Allocation495: BinaryAssociation = BinaryAssociation(
    name="targetResourceEnvironment_Allocation495",
    ends={
        Property(name="ResourceEnvironment496", type=pcm_pc_av_allocation_pc_av_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_allocation_pc_av_Allocation", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
system_Allocation497: BinaryAssociation = BinaryAssociation(
    name="system_Allocation497",
    ends={
        Property(name="System499", type=pcm_pc_av_allocation_pc_av_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_av_allocation_pc_av_Allocation498", type=System, multiplicity=Multiplicity(0, 1))
    }
)
allocationContexts_Allocation500: BinaryAssociation = BinaryAssociation(
    name="allocationContexts_Allocation500",
    ends={
        Property(name="AllocationContext", type=pcm_pc_av_allocation_pc_av_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="allocation_AllocationContext", type=AllocationContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_pcm_pc_av_core_pc_av_PCMRandomVariable_RandomVariable = Generalization(general=RandomVariable, specific=pcm_pc_av_core_pc_av_PCMRandomVariable)
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
gen_pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingEntity)
gen_pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity_composition_pc_av_ComposedStructure = Generalization(general=composition_pc_av_ComposedStructure, specific=pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity)
gen_pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity_entity_pc_av_InterfaceProvidingRequiringEntity = Generalization(general=entity_pc_av_InterfaceProvidingRequiringEntity, specific=pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity)
gen_pcm_pc_av_composition_pc_av_EventChannel_Entity = Generalization(general=Entity, specific=pcm_pc_av_composition_pc_av_EventChannel)
gen_pcm_pc_av_composition_pc_av_EventChannelSourceConnector_Connector = Generalization(general=Connector, specific=pcm_pc_av_composition_pc_av_EventChannelSourceConnector)
gen_pcm_pc_av_composition_pc_av_ProvidedDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_av_composition_pc_av_ProvidedDelegationConnector)
gen_pcm_pc_av_composition_pc_av_RequiredDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_av_composition_pc_av_RequiredDelegationConnector)
gen_pcm_pc_av_composition_pc_av_EventChannelSinkConnector_Connector = Generalization(general=Connector, specific=pcm_pc_av_composition_pc_av_EventChannelSinkConnector)
gen_pcm_pc_av_composition_pc_av_AssemblyConnector_Connector = Generalization(general=Connector, specific=pcm_pc_av_composition_pc_av_AssemblyConnector)
gen_pcm_pc_av_composition_pc_av_AssemblyEventConnector_Connector = Generalization(general=Connector, specific=pcm_pc_av_composition_pc_av_AssemblyEventConnector)
gen_pcm_pc_av_composition_pc_av_SourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_av_composition_pc_av_SourceDelegationConnector)
gen_pcm_pc_av_composition_pc_av_SinkDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_av_composition_pc_av_SinkDelegationConnector)
gen_pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector)
gen_pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector)
gen_pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector)
gen_pcm_pc_av_composition_pc_av_AssemblyContext_Entity = Generalization(general=Entity, specific=pcm_pc_av_composition_pc_av_AssemblyContext)
gen_pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector_Connector = Generalization(general=Connector, specific=pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector)
gen_pcm_pc_av_usagemodel_pc_av_AbstractUserAction_Entity = Generalization(general=Entity, specific=pcm_pc_av_usagemodel_pc_av_AbstractUserAction)
gen_pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour_Entity = Generalization(general=Entity, specific=pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour)
gen_pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall)
gen_pcm_pc_av_usagemodel_pc_av_UsageScenario_Entity = Generalization(general=Entity, specific=pcm_pc_av_usagemodel_pc_av_UsageScenario)
gen_pcm_pc_av_usagemodel_pc_av_Branch_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_av_usagemodel_pc_av_Branch)
gen_pcm_pc_av_usagemodel_pc_av_OpenWorkload_Workload = Generalization(general=Workload, specific=pcm_pc_av_usagemodel_pc_av_OpenWorkload)
gen_pcm_pc_av_usagemodel_pc_av_Loop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_av_usagemodel_pc_av_Loop)
gen_pcm_pc_av_usagemodel_pc_av_Stop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_av_usagemodel_pc_av_Stop)
gen_pcm_pc_av_usagemodel_pc_av_Start_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_av_usagemodel_pc_av_Start)
gen_pcm_pc_av_repository_pc_av_BasicComponent_ImplementationComponentType = Generalization(general=ImplementationComponentType, specific=pcm_pc_av_repository_pc_av_BasicComponent)
gen_pcm_pc_av_usagemodel_pc_av_Delay_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_av_usagemodel_pc_av_Delay)
gen_pcm_pc_av_usagemodel_pc_av_ClosedWorkload_Workload = Generalization(general=Workload, specific=pcm_pc_av_usagemodel_pc_av_ClosedWorkload)
gen_pcm_pc_av_repository_pc_av_PassiveResource_Entity = Generalization(general=Entity, specific=pcm_pc_av_repository_pc_av_PassiveResource)
gen_pcm_pc_av_repository_pc_av_ImplementationComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_pc_av_repository_pc_av_ImplementationComponentType)
gen_pcm_pc_av_repository_pc_av_Repository_Entity = Generalization(general=Entity, specific=pcm_pc_av_repository_pc_av_Repository)
gen_pcm_pc_av_repository_pc_av_RepositoryComponent_InterfaceProvidingRequiringEntity = Generalization(general=InterfaceProvidingRequiringEntity, specific=pcm_pc_av_repository_pc_av_RepositoryComponent)
gen_pcm_pc_av_repository_pc_av_ProvidedRole_Role = Generalization(general=Role, specific=pcm_pc_av_repository_pc_av_ProvidedRole)
gen_pcm_pc_av_repository_pc_av_EventGroup_Interface = Generalization(general=Interface, specific=pcm_pc_av_repository_pc_av_EventGroup)
gen_pcm_pc_av_repository_pc_av_Interface_Entity = Generalization(general=Entity, specific=pcm_pc_av_repository_pc_av_Interface)
gen_pcm_pc_av_repository_pc_av_InfrastructureSignature_Signature = Generalization(general=Signature, specific=pcm_pc_av_repository_pc_av_InfrastructureSignature)
gen_pcm_pc_av_repository_pc_av_InfrastructureInterface_Interface = Generalization(general=Interface, specific=pcm_pc_av_repository_pc_av_InfrastructureInterface)
gen_pcm_pc_av_repository_pc_av_InfrastructureRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_pc_av_repository_pc_av_InfrastructureRequiredRole)
gen_pcm_pc_av_repository_pc_av_EventType_Signature = Generalization(general=Signature, specific=pcm_pc_av_repository_pc_av_EventType)
gen_pcm_pc_av_repository_pc_av_Signature_Entity = Generalization(general=Entity, specific=pcm_pc_av_repository_pc_av_Signature)
gen_pcm_pc_av_repository_pc_av_OperationRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_pc_av_repository_pc_av_OperationRequiredRole)
gen_pcm_pc_av_repository_pc_av_SourceRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_pc_av_repository_pc_av_SourceRole)
gen_pcm_pc_av_repository_pc_av_SinkRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_pc_av_repository_pc_av_SinkRole)
gen_pcm_pc_av_repository_pc_av_OperationProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_pc_av_repository_pc_av_OperationProvidedRole)
gen_pcm_pc_av_repository_pc_av_RequiredRole_Role = Generalization(general=Role, specific=pcm_pc_av_repository_pc_av_RequiredRole)
gen_pcm_pc_av_repository_pc_av_OperationSignature_Signature = Generalization(general=Signature, specific=pcm_pc_av_repository_pc_av_OperationSignature)
gen_pcm_pc_av_repository_pc_av_OperationInterface_Interface = Generalization(general=Interface, specific=pcm_pc_av_repository_pc_av_OperationInterface)
gen_pcm_pc_av_repository_pc_av_ProvidesComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_pc_av_repository_pc_av_ProvidesComponentType)
gen_pcm_pc_av_repository_pc_av_CompositeComponent_entity_pc_av_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_av_ComposedProvidingRequiringEntity, specific=pcm_pc_av_repository_pc_av_CompositeComponent)
gen_pcm_pc_av_repository_pc_av_CompositeComponent_repository_pc_av_ImplementationComponentType = Generalization(general=repository_pc_av_ImplementationComponentType, specific=pcm_pc_av_repository_pc_av_CompositeComponent)
gen_pcm_pc_av_repository_pc_av_InfrastructureProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_pc_av_repository_pc_av_InfrastructureProvidedRole)
gen_pcm_pc_av_repository_pc_av_CompleteComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_pc_av_repository_pc_av_CompleteComponentType)
gen_pcm_pc_av_repository_pc_av_CompositeDataType_entity_pc_av_Entity = Generalization(general=entity_pc_av_Entity, specific=pcm_pc_av_repository_pc_av_CompositeDataType)
gen_pcm_pc_av_repository_pc_av_CompositeDataType_repository_pc_av_DataType = Generalization(general=repository_pc_av_DataType, specific=pcm_pc_av_repository_pc_av_CompositeDataType)
gen_pcm_pc_av_repository_pc_av_InnerDeclaration_NamedElement = Generalization(general=NamedElement, specific=pcm_pc_av_repository_pc_av_InnerDeclaration)
gen_pcm_pc_av_repository_pc_av_Role_Entity = Generalization(general=Entity, specific=pcm_pc_av_repository_pc_av_Role)
gen_pcm_pc_av_repository_pc_av_PrimitiveDataType_DataType = Generalization(general=DataType, specific=pcm_pc_av_repository_pc_av_PrimitiveDataType)
gen_pcm_pc_av_repository_pc_av_CollectionDataType_entity_pc_av_Entity = Generalization(general=entity_pc_av_Entity, specific=pcm_pc_av_repository_pc_av_CollectionDataType)
gen_pcm_pc_av_repository_pc_av_CollectionDataType_repository_pc_av_DataType = Generalization(general=repository_pc_av_DataType, specific=pcm_pc_av_repository_pc_av_CollectionDataType)
gen_pcm_pc_av_resourcetype_pc_av_SchedulingPolicy_Entity = Generalization(general=Entity, specific=pcm_pc_av_resourcetype_pc_av_SchedulingPolicy)
gen_pcm_pc_av_resourcetype_pc_av_CommunicationLinkResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_pc_av_resourcetype_pc_av_CommunicationLinkResourceType)
gen_pcm_pc_av_resourcetype_pc_av_ResourceInterface_Entity = Generalization(general=Entity, specific=pcm_pc_av_resourcetype_pc_av_ResourceInterface)
gen_pcm_pc_av_resourcetype_pc_av_ResourceSignature_Entity = Generalization(general=Entity, specific=pcm_pc_av_resourcetype_pc_av_ResourceSignature)
gen_pcm_pc_av_resourcetype_pc_av_ProcessingResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_pc_av_resourcetype_pc_av_ProcessingResourceType)
gen_pcm_pc_av_resourcetype_pc_av_ResourceType_entity_pc_av_Entity = Generalization(general=entity_pc_av_Entity, specific=pcm_pc_av_resourcetype_pc_av_ResourceType)
gen_pcm_pc_av_resourcetype_pc_av_ResourceType_UnitCarryingElement = Generalization(general=UnitCarryingElement, specific=pcm_pc_av_resourcetype_pc_av_ResourceType)
gen_pcm_pc_av_resourcetype_pc_av_ResourceType_entity_pc_av_ResourceInterfaceProvidingEntity = Generalization(general=entity_pc_av_ResourceInterfaceProvidingEntity, specific=pcm_pc_av_resourcetype_pc_av_ResourceType)
gen_pcm_pc_av_parameter_pc_av_CharacterisedVariable_Variable = Generalization(general=Variable, specific=pcm_pc_av_parameter_pc_av_CharacterisedVariable)
gen_pcm_pc_av_reliability_pc_av_SoftwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_pc_av_reliability_pc_av_SoftwareInducedFailureType)
gen_pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription)
gen_pcm_pc_av_reliability_pc_av_HardwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_pc_av_reliability_pc_av_HardwareInducedFailureType)
gen_pcm_pc_av_reliability_pc_av_ResourceTimeoutFailureType_SoftwareInducedFailureType = Generalization(general=SoftwareInducedFailureType, specific=pcm_pc_av_reliability_pc_av_ResourceTimeoutFailureType)
gen_pcm_pc_av_reliability_pc_av_FailureType_Entity = Generalization(general=Entity, specific=pcm_pc_av_reliability_pc_av_FailureType)
gen_pcm_pc_av_seff_pc_av_StopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_av_seff_pc_av_StopAction)
gen_pcm_pc_av_reliability_pc_av_NetworkInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_pc_av_reliability_pc_av_NetworkInducedFailureType)
gen_pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription)
gen_pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction_AbstractAction = Generalization(general=AbstractAction, specific=pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction)
gen_pcm_pc_av_seff_pc_av_AbstractAction_Entity = Generalization(general=Entity, specific=pcm_pc_av_seff_pc_av_AbstractAction)
gen_pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour_Identifier = Generalization(general=Identifier, specific=pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour)
gen_pcm_pc_av_seff_pc_av_StartAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_av_seff_pc_av_StartAction)
gen_pcm_pc_av_seff_pc_av_AbstractLoopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_av_seff_pc_av_AbstractLoopAction)
gen_pcm_pc_av_seff_pc_av_AbstractBranchTransition_Entity = Generalization(general=Entity, specific=pcm_pc_av_seff_pc_av_AbstractBranchTransition)
gen_pcm_pc_av_seff_pc_av_BranchAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_av_seff_pc_av_BranchAction)
gen_pcm_pc_av_seff_pc_av_LoopAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_pc_av_seff_pc_av_LoopAction)
gen_pcm_pc_av_seff_pc_av_ForkAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_av_seff_pc_av_ForkAction)
gen_pcm_pc_av_seff_pc_av_ForkedBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_pc_av_seff_pc_av_ForkedBehaviour)
gen_pcm_pc_av_seff_pc_av_ResourceDemandingSEFF_Identifier = Generalization(general=Identifier, specific=pcm_pc_av_seff_pc_av_ResourceDemandingSEFF)
gen_pcm_pc_av_seff_pc_av_ResourceDemandingSEFF_seff_pc_av_ServiceEffectSpecification = Generalization(general=seff_pc_av_ServiceEffectSpecification, specific=pcm_pc_av_seff_pc_av_ResourceDemandingSEFF)
gen_pcm_pc_av_seff_pc_av_ResourceDemandingSEFF_seff_pc_av_ResourceDemandingBehaviour = Generalization(general=seff_pc_av_ResourceDemandingBehaviour, specific=pcm_pc_av_seff_pc_av_ResourceDemandingSEFF)
gen_pcm_pc_av_seff_pc_av_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_pc_av_seff_pc_av_ResourceDemandingInternalBehaviour)
gen_pcm_pc_av_seff_pc_av_ReleaseAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_av_seff_pc_av_ReleaseAction)
gen_pcm_pc_av_seff_pc_av_CallReturnAction_CallAction = Generalization(general=CallAction, specific=pcm_pc_av_seff_pc_av_CallReturnAction)
gen_pcm_pc_av_seff_pc_av_ProbabilisticBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_pc_av_seff_pc_av_ProbabilisticBranchTransition)
gen_pcm_pc_av_seff_pc_av_AcquireAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_av_seff_pc_av_AcquireAction)
gen_pcm_pc_av_seff_pc_av_ExternalCallAction_seff_pc_av_AbstractAction = Generalization(general=seff_pc_av_AbstractAction, specific=pcm_pc_av_seff_pc_av_ExternalCallAction)
gen_pcm_pc_av_seff_pc_av_ExternalCallAction_seff_pc_av_CallReturnAction = Generalization(general=seff_pc_av_CallReturnAction, specific=pcm_pc_av_seff_pc_av_ExternalCallAction)
gen_pcm_pc_av_seff_pc_av_ExternalCallAction_seff_reliability_pc_av_FailureHandlingEntity = Generalization(general=seff_reliability_pc_av_FailureHandlingEntity, specific=pcm_pc_av_seff_pc_av_ExternalCallAction)
gen_pcm_pc_av_seff_pc_av_EmitEventAction_seff_pc_av_AbstractAction = Generalization(general=seff_pc_av_AbstractAction, specific=pcm_pc_av_seff_pc_av_EmitEventAction)
gen_pcm_pc_av_seff_pc_av_EmitEventAction_seff_pc_av_CallAction = Generalization(general=seff_pc_av_CallAction, specific=pcm_pc_av_seff_pc_av_EmitEventAction)
gen_pcm_pc_av_seff_pc_av_InternalAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_av_seff_pc_av_InternalAction)
gen_pcm_pc_av_seff_pc_av_CollectionIteratorAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_pc_av_seff_pc_av_CollectionIteratorAction)
gen_pcm_pc_av_seff_pc_av_GuardedBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_pc_av_seff_pc_av_GuardedBranchTransition)
gen_pcm_pc_av_seff_pc_av_SetVariableAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_av_seff_pc_av_SetVariableAction)
gen_pcm_pc_av_seff_pc_av_InternalCallAction_seff_pc_av_CallAction = Generalization(general=seff_pc_av_CallAction, specific=pcm_pc_av_seff_pc_av_InternalCallAction)
gen_pcm_pc_av_seff_pc_av_InternalCallAction_seff_pc_av_AbstractInternalControlFlowAction = Generalization(general=seff_pc_av_AbstractInternalControlFlowAction, specific=pcm_pc_av_seff_pc_av_InternalCallAction)
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
gen_pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation)
gen_pcm_pc_av_resourceenvironment_pc_av_ResourceContainer_Entity = Generalization(general=Entity, specific=pcm_pc_av_resourceenvironment_pc_av_ResourceContainer)
gen_pcm_pc_av_system_pc_av_System_entity_pc_av_Entity = Generalization(general=entity_pc_av_Entity, specific=pcm_pc_av_system_pc_av_System)
gen_pcm_pc_av_system_pc_av_System_entity_pc_av_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_av_ComposedProvidingRequiringEntity, specific=pcm_pc_av_system_pc_av_System)
gen_pcm_pc_av_resourceenvironment_pc_av_ResourceEnvironment_NamedElement = Generalization(general=NamedElement, specific=pcm_pc_av_resourceenvironment_pc_av_ResourceEnvironment)
gen_pcm_pc_av_resourceenvironment_pc_av_LinkingResource_Entity = Generalization(general=Entity, specific=pcm_pc_av_resourceenvironment_pc_av_LinkingResource)
gen_pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification)
gen_pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification)
gen_pcm_pc_av_allocation_pc_av_AllocationContext_Entity = Generalization(general=Entity, specific=pcm_pc_av_allocation_pc_av_AllocationContext)
gen_pcm_pc_av_completions_pc_av_DelegatingExternalCallAction_ExternalCallAction = Generalization(general=ExternalCallAction, specific=pcm_pc_av_completions_pc_av_DelegatingExternalCallAction)
gen_pcm_pc_av_completions_pc_av_NetworkDemandParametricResourceDemand_ParametricResourceDemand = Generalization(general=ParametricResourceDemand, specific=pcm_pc_av_completions_pc_av_NetworkDemandParametricResourceDemand)
gen_pcm_pc_av_allocation_pc_av_Allocation_Entity = Generalization(general=Entity, specific=pcm_pc_av_allocation_pc_av_Allocation)
gen_pcm_pc_av_subsystem_pc_av_SubSystem_entity_pc_av_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_av_ComposedProvidingRequiringEntity, specific=pcm_pc_av_subsystem_pc_av_SubSystem)
gen_pcm_pc_av_subsystem_pc_av_SubSystem_repository_pc_av_RepositoryComponent = Generalization(general=repository_pc_av_RepositoryComponent, specific=pcm_pc_av_subsystem_pc_av_SubSystem)
gen_pcm_pc_av_completions_pc_av_Completion_entity_pc_av_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_av_ComposedProvidingRequiringEntity, specific=pcm_pc_av_completions_pc_av_Completion)
gen_pcm_pc_av_completions_pc_av_Completion_repository_pc_av_ImplementationComponentType = Generalization(general=repository_pc_av_ImplementationComponentType, specific=pcm_pc_av_completions_pc_av_Completion)

# Domain Model
domain_model = DomainModel(
    name="pcm_pc_av",
    types={pcm_pc_av_DummyClass, pcm_pc_av_Pointcut, pcm_pc_av_EObject, pcm_pc_av_Advice, pcm_pc_av_core_pc_av_PCMRandomVariable, RandomVariable, ClosedWorkload, PassiveResource, VariableCharacterisation, seff_performance_pc_av_InfrastructureCall, pcm_pc_av_GlobalScope, pcm_pc_av_PerJoinPointScope, GuardedBranchTransition, qos_performance_pc_av_SpecifiedExecutionTime, composition_pc_av_EventChannelSinkConnector, composition_pc_av_AssemblyEventConnector, Loop, OpenWorkload, Delay, seff_performance_pc_av_ResourceCall, seff_performance_pc_av_ParametricResourceDemand, LoopAction, ProcessingResourceSpecification, pcm_pc_av_entity_pc_av_ResourceProvidedRole, Role, entity_pc_av_ResourceInterfaceProvidingEntity, ResourceInterface, pcm_pc_av_entity_pc_av_InterfaceProvidingRequiringEntity, entity_pc_av_InterfaceProvidingEntity, entity_pc_av_InterfaceRequiringEntity, pcm_pc_av_entity_pc_av_InterfaceProvidingEntity, Entity, ProvidedRole, pcm_pc_av_entity_pc_av_InterfaceRequiringEntity, entity_pc_av_Entity, entity_pc_av_ResourceInterfaceRequiringEntity, RequiredRole, pcm_pc_av_entity_pc_av_ResourceInterfaceRequiringEntity, entity_pc_av_ResourceRequiredRole, pcm_pc_av_entity_pc_av_ResourceRequiredRole, CommunicationLinkResourceSpecification, pcm_pc_av_entity_pc_av_NamedElement, pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingRequiringEntity, pcm_pc_av_entity_pc_av_Entity, Identifier, entity_pc_av_NamedElement, pcm_pc_av_composition_pc_av_DelegationConnector, Connector, pcm_pc_av_composition_pc_av_Connector, pcm_pc_av_composition_pc_av_ComposedStructure, pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingEntity, entity_pc_av_ResourceProvidedRole, pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity, composition_pc_av_ComposedStructure, entity_pc_av_InterfaceProvidingRequiringEntity, composition_pc_av_AssemblyContext, composition_pc_av_ResourceRequiredDelegationConnector, composition_pc_av_EventChannel, composition_pc_av_Connector, pcm_pc_av_composition_pc_av_ResourceRequiredDelegationConnector, pcm_pc_av_composition_pc_av_EventChannel, EventGroup, composition_pc_av_EventChannelSourceConnector, pcm_pc_av_composition_pc_av_EventChannelSourceConnector, SourceRole, PCMRandomVariable, pcm_pc_av_composition_pc_av_ProvidedDelegationConnector, DelegationConnector, OperationProvidedRole, pcm_pc_av_composition_pc_av_RequiredDelegationConnector, pcm_pc_av_composition_pc_av_EventChannelSinkConnector, SinkRole, OperationRequiredRole, pcm_pc_av_composition_pc_av_AssemblyConnector, pcm_pc_av_composition_pc_av_AssemblyEventConnector, pcm_pc_av_composition_pc_av_SourceDelegationConnector, pcm_pc_av_composition_pc_av_SinkDelegationConnector, pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector, pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector, pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector, pcm_pc_av_composition_pc_av_AssemblyContext, RepositoryComponent, VariableUsage, pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector, InfrastructureProvidedRole, InfrastructureRequiredRole, UsageModel, ScenarioBehaviour, pcm_pc_av_usagemodel_pc_av_AbstractUserAction, Workload, pcm_pc_av_usagemodel_pc_av_UserData, pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour, pcm_pc_av_usagemodel_pc_av_UsageModel, UserData, pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall, AbstractUserAction, pcm_pc_av_usagemodel_pc_av_Workload, OperationSignature, UsageScenario, pcm_pc_av_usagemodel_pc_av_UsageScenario, pcm_pc_av_usagemodel_pc_av_BranchTransition, Branch, pcm_pc_av_usagemodel_pc_av_Branch, BranchTransition, pcm_pc_av_usagemodel_pc_av_OpenWorkload, pcm_pc_av_usagemodel_pc_av_Loop, pcm_pc_av_usagemodel_pc_av_Stop, pcm_pc_av_usagemodel_pc_av_Start, BasicComponent, ResourceTimeoutFailureType, pcm_pc_av_repository_pc_av_BasicComponent, ImplementationComponentType, pcm_pc_av_usagemodel_pc_av_Delay, pcm_pc_av_usagemodel_pc_av_ClosedWorkload, pcm_pc_av_repository_pc_av_PassiveResource, CompleteComponentType, ServiceEffectSpecification, pcm_pc_av_repository_pc_av_ImplementationComponentType, ResourceSignature, pcm_pc_av_repository_pc_av_DataType, pcm_pc_av_repository_pc_av_Repository, Interface, pcm_pc_av_repository_pc_av_RepositoryComponent, InterfaceProvidingRequiringEntity, Repository, pcm_pc_av_repository_pc_av_ProvidedRole, pcm_pc_av_repository_pc_av_Parameter, DataType, InfrastructureSignature, EventType, RequiredCharacterisation, pcm_pc_av_repository_pc_av_RequiredCharacterisation, Parameter_, pcm_pc_av_repository_pc_av_EventGroup, FailureType, pcm_pc_av_repository_pc_av_Interface, Protocol, pcm_pc_av_repository_pc_av_InfrastructureSignature, InfrastructureInterface, pcm_pc_av_repository_pc_av_InfrastructureInterface, pcm_pc_av_repository_pc_av_InfrastructureRequiredRole, pcm_pc_av_repository_pc_av_EventType, Signature, pcm_pc_av_repository_pc_av_Signature, ExceptionType, pcm_pc_av_repository_pc_av_ExceptionType, pcm_pc_av_repository_pc_av_OperationRequiredRole, pcm_pc_av_repository_pc_av_SourceRole, pcm_pc_av_repository_pc_av_SinkRole, pcm_pc_av_repository_pc_av_OperationProvidedRole, pcm_pc_av_repository_pc_av_RequiredRole, pcm_pc_av_repository_pc_av_OperationSignature, OperationInterface, pcm_pc_av_repository_pc_av_OperationInterface, ProvidesComponentType, pcm_pc_av_repository_pc_av_ProvidesComponentType, pcm_pc_av_repository_pc_av_CompositeComponent, entity_pc_av_ComposedProvidingRequiringEntity, repository_pc_av_ImplementationComponentType, pcm_pc_av_repository_pc_av_InfrastructureProvidedRole, pcm_pc_av_repository_pc_av_CompleteComponentType, pcm_pc_av_repository_pc_av_CompositeDataType, CompositeDataType, InnerDeclaration, pcm_pc_av_repository_pc_av_InnerDeclaration, NamedElement, pcm_pc_av_repository_pc_av_Role, pcm_pc_av_repository_pc_av_PrimitiveDataType, pcm_pc_av_repository_pc_av_CollectionDataType, repository_pc_av_DataType, SchedulingPolicy, pcm_pc_av_resourcetype_pc_av_SchedulingPolicy, pcm_pc_av_resourcetype_pc_av_CommunicationLinkResourceType, NetworkInducedFailureType, pcm_pc_av_resourcetype_pc_av_ResourceInterface, pcm_pc_av_resourcetype_pc_av_ResourceSignature, pcm_pc_av_resourcetype_pc_av_ProcessingResourceType, ResourceType, HardwareInducedFailureType, pcm_pc_av_resourcetype_pc_av_ResourceType, UnitCarryingElement, ResourceRepository, pcm_pc_av_resourcetype_pc_av_ResourceRepository, EntryLevelSystemCall, parameter_pc_av_pcm_pc_av_AbstractNamedReference, pcm_pc_av_parameter_pc_av_VariableCharacterisation, pcm_pc_av_parameter_pc_av_CharacterisedVariable, Variable, pcm_pc_av_protocol_pc_av_Protocol, pcm_pc_av_parameter_pc_av_VariableUsage, CallAction, SynchronisationPoint, CallReturnAction, SetVariableAction, SpecifiedOutputParameterAbstraction, ProcessingResourceType, pcm_pc_av_reliability_pc_av_SoftwareInducedFailureType, InternalFailureOccurrenceDescription, pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription, FailureOccurrenceDescription, InternalAction, pcm_pc_av_reliability_pc_av_FailureOccurrenceDescription, pcm_pc_av_reliability_pc_av_HardwareInducedFailureType, pcm_pc_av_reliability_pc_av_ResourceTimeoutFailureType, pcm_pc_av_reliability_pc_av_FailureType, pcm_pc_av_seff_pc_av_StopAction, AbstractInternalControlFlowAction, SoftwareInducedFailureType, pcm_pc_av_reliability_pc_av_NetworkInducedFailureType, CommunicationLinkResourceType, pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription, qos_reliability_pc_av_SpecifiedReliabilityAnnotation, AbstractLoopAction, AbstractBranchTransition, pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction, AbstractAction, pcm_pc_av_seff_pc_av_AbstractAction, ResourceDemandingBehaviour, pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour, pcm_pc_av_seff_pc_av_CallAction, pcm_pc_av_seff_pc_av_StartAction, pcm_pc_av_seff_pc_av_ServiceEffectSpecification, pcm_pc_av_seff_pc_av_AbstractLoopAction, pcm_pc_av_seff_pc_av_AbstractBranchTransition, BranchAction, pcm_pc_av_seff_pc_av_BranchAction, pcm_pc_av_seff_pc_av_LoopAction, pcm_pc_av_seff_pc_av_ForkAction, ForkedBehaviour, pcm_pc_av_seff_pc_av_ForkedBehaviour, ForkAction, pcm_pc_av_seff_pc_av_ResourceDemandingSEFF, seff_pc_av_ServiceEffectSpecification, seff_pc_av_ResourceDemandingBehaviour, ResourceDemandingInternalBehaviour, pcm_pc_av_seff_pc_av_ResourceDemandingInternalBehaviour, ResourceDemandingSEFF, pcm_pc_av_seff_pc_av_ReleaseAction, pcm_pc_av_seff_pc_av_CallReturnAction, pcm_pc_av_seff_pc_av_ProbabilisticBranchTransition, pcm_pc_av_seff_pc_av_AcquireAction, pcm_pc_av_seff_pc_av_SynchronisationPoint, pcm_pc_av_seff_pc_av_ExternalCallAction, seff_pc_av_AbstractAction, seff_pc_av_CallReturnAction, seff_reliability_pc_av_FailureHandlingEntity, pcm_pc_av_seff_pc_av_EmitEventAction, pcm_pc_av_seff_pc_av_InternalAction, pcm_pc_av_seff_pc_av_CollectionIteratorAction, pcm_pc_av_seff_pc_av_GuardedBranchTransition, pcm_pc_av_seff_pc_av_SetVariableAction, pcm_pc_av_seff_pc_av_InternalCallAction, seff_pc_av_CallAction, seff_pc_av_AbstractInternalControlFlowAction, pcm_pc_av_seff_performance_pc_av_InfrastructureCall, pcm_pc_av_seff_performance_pc_av_ResourceCall, pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour, pcm_pc_av_seff_performance_pc_av_ParametricResourceDemand, pcm_pc_av_seff_reliability_pc_av_FailureHandlingEntity, pcm_pc_av_qosannotations_pc_av_SpecifiedQoSAnnotation, seff_reliability_pc_av_RecoveryActionBehaviour, seff_reliability_pc_av_RecoveryAction, pcm_pc_av_seff_reliability_pc_av_RecoveryAction, System, SpecifiedQoSAnnotation, pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction, QoSAnnotations, pcm_pc_av_qosannotations_pc_av_QoSAnnotations, ExternalFailureOccurrenceDescription, pcm_pc_av_qos_performance_pc_av_SystemSpecifiedExecutionTime, SpecifiedExecutionTime, pcm_pc_av_qos_performance_pc_av_SpecifiedExecutionTime, pcm_pc_av_qos_performance_pc_av_ComponentSpecifiedExecutionTime, pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation, ResourceEnvironment, pcm_pc_av_resourceenvironment_pc_av_ResourceContainer, pcm_pc_av_system_pc_av_System, pcm_pc_av_resourceenvironment_pc_av_ResourceEnvironment, LinkingResource, ResourceContainer, pcm_pc_av_resourceenvironment_pc_av_LinkingResource, pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification, pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification, Allocation, pcm_pc_av_allocation_pc_av_Allocation, pcm_pc_av_allocation_pc_av_AllocationContext, pcm_pc_av_completions_pc_av_CompletionRepository, Completion, pcm_pc_av_completions_pc_av_DelegatingExternalCallAction, ExternalCallAction, pcm_pc_av_completions_pc_av_NetworkDemandParametricResourceDemand, ParametricResourceDemand, AllocationContext, pcm_pc_av_subsystem_pc_av_SubSystem, repository_pc_av_RepositoryComponent, pcm_pc_av_completions_pc_av_Completion, ComponentType, ParameterModifier, PrimitiveTypeEnum, VariableCharacterisationType},
    associations={children0, closedWorkload_PCMRandomVariable7, passiveResource_capacity_PCMRandomVariable8, variableCharacterisation_Specification9, infrastructureCall__PCMRandomVariable10, children1, scopedObject3, scopedObject5, loopAction_PCMRandomVariable13, guardedBranchTransition_PCMRandomVariable14, specifiedExecutionTime_PCMRandomVariable15, eventChannelSinkConnector__FilterCondition16, assemblyEventConnector__FilterCondition17, loop_LoopIteration18, openWorkload_PCMRandomVariable19, resourceCall__PCMRandomVariable11, parametricResourceDemand_PCMRandomVariable12, processingResourceSpecification_processingRate_PCMRandomVariable22, communicationLinkResourceSpecification_latency_PCMRandomVariable23, resourceInterfaceProvidingEntity__ResourceProvidedRole25, providedResourceInterface__ResourceProvidedRole26, providedRoles_InterfaceProvidingEntity27, requiredRoles_InterfaceRequiringEntity28, resourceRequiredRoles__ResourceInterfaceRequiringEntity29, delay_TimeSpecification20, communicationLinkResourceSpecifcation_throughput_PCMRandomVariable21, parentStructure__Connector34, requiredResourceInterface__ResourceRequiredRole30, resourceInterfaceRequiringEntity__ResourceRequiredRole32, resourceProvidedRoles__ResourceInterfaceProvidingEntity33, assemblyContexts__ComposedStructure35, resourceRequiredDelegationConnectors_ComposedStructure36, eventChannel__ComposedStructure37, connectors__ComposedStructure38, innerResourceRequiredRole_ResourceRequiredDelegationConnector39, outerResourceRequiredRole_ResourceRequiredDelegationConnector40, parentStructure_ResourceRequiredDelegationConnector43, eventGroup__EventChannel45, eventChannelSourceConnector__EventChannel46, eventChannelSinkConnector__EventChannel47, parentStructure__EventChannel49, sinkRole__EventChannelSinkConnector56, filterCondition__EventChannelSinkConnector57, assemblyContext__EventChannelSinkConnector58, eventChannel__EventChannelSinkConnector61, innerProvidedRole_ProvidedDelegationConnector63, outerProvidedRole_ProvidedDelegationConnector64, assemblyContext_ProvidedDelegationConnector67, sourceRole__EventChannelSourceRole51, assemblyContext__EventChannelSourceConnector52, eventChannel__EventChannelSourceConnector54, innerRequiredRole_RequiredDelegationConnector70, outerRequiredRole_RequiredDelegationConnector71, assemblyContext_RequiredDelegationConnector74, requiringAssemblyContext_AssemblyConnector77, providingAssemblyContext_AssemblyConnector79, providedRole_AssemblyConnector82, requiredRole_AssemblyConnector85, sinkRole__AssemblyEventConnector88, sourceRole__AssemblyEventConnector90, sinkAssemblyContext__AssemblyEventConnector93, sourceAssemblyContext__AssemblyEventConnector96, filterCondition__AssemblyEventConnector99, innerSourceRole__SourceRole101, outerSourceRole__SourceRole103, assemblyContext__SourceDelegationConnector106, assemblyContext__SinkDelegationConnector109, providingAssemblyContext__AssemblyInfrastructureConnector120, requiringAssemblyContext__AssemblyInfrastructureConnector123, innerProvidedRole__ProvidedInfrastructureDelegationConnector126, outerProvidedRole__ProvidedInfrastructureDelegationConnector128, assemblyContext__ProvidedInfrastructureDelegationConnector131, innerRequiredRole__RequiredInfrastructureDelegationConnector134, outerRequiredRole__RequiredInfrastructureDelegationConnector136, assemblyContext__RequiredInfrastructureDelegationConnector139, assemblyContext__RequiredResourceDelegationConnector142, innerRequiredRole__RequiredResourceDelegationConnector144, outerRequiredRole__RequiredResourceDelegationConnector147, parentStructure__AssemblyContext150, encapsulatedComponent__AssemblyContext152, configParameterUsages__AssemblyContext153, innerSinkRole__SinkRole111, outerSinkRole__SinkRole114, providedRole__AssemblyInfrastructureConnector117, requiredRole__AssemblyInfrastructureConnector118, usageModel_UsageScenario155, inputParameterUsages_EntryLevelSystemCall173, scenarioBehaviour_UsageScenario156, workload_UsageScenario157, successor175, predecessor176, assemblyContext_userData158, scenarioBehaviour_AbstractUserAction178, usageModel_UserData160, userDataParameterUsages_UserData162, usageScenario_UsageModel164, userData_UsageModel166, providedRole_EntryLevelSystemCall167, operationSignature__EntryLevelSystemCall169, usageScenario_Workload154, outputParameterUsages_EntryLevelSystemCall171, branch_BranchTransition187, branchedBehaviour_BranchTransition188, usageScenario_SenarioBehaviour180, branchTransition_ScenarioBehaviour182, loop_ScenarioBehaviour183, actions_ScenarioBehaviour185, interArrivalTime_OpenWorkload196, branchTransitions_Branch190, loopIteration_Loop192, bodyBehaviour_Loop194, basicComponent_PassiveResource204, resourceTimeoutFailureType__PassiveResource205, timeSpecification_Delay198, thinkTime_ClosedWorkload200, capacity_PassiveResource202, serviceEffectSpecifications__BasicComponent206, passiveResource_BasicComponent207, resourceSignature__Parameter220, repository__DataType221, components__Repository223, parentCompleteComponentTypes209, componentParameterUsage_ImplementationComponentType210, repository__RepositoryComponent213, providingEntity_ProvidedRole214, dataType__Parameter215, infrastructureSignature__Parameter216, operationSignature__Parameter217, eventType__Parameter219, requiredCharacterisations233, repository__Interface234, parameter236, interface_RequiredCharacterisation237, interfaces__Repository225, failureTypes__Repository226, dataTypes__Repository227, parentInterfaces__Interface229, protocols__Interface231, parameters__InfrastructureSignature249, infrastructureInterface__InfrastructureSignature251, infrastructureSignatures__InfrastructureInterface252, eventTypes__EventGroup239, parameter__EventType241, eventGroup__EventType243, exceptions__Signature245, failureType246, signatures__OperationInterface262, requiredInterface__OperationRequiredRole264, eventGroup__SourceRole266, eventGroup__SinkRole268, requiredInterface__InfrastructureRequiredRole254, providedInterface__OperationProvidedRole270, requiringEntity_RequiredRole256, interface__OperationSignature257, parameters__OperationSignature258, returnType__OperationSignature260, parentProvidesComponentTypes274, providedInterface__InfrastructureProvidedRole272, parentType_CompositeDataType277, innerDeclaration_CompositeDataType278, datatype_InnerDeclaration279, compositeDataType_InnerDeclaration281, innerType_CollectionDataType275, resourceInterfaces__ResourceRepository289, schedulingPolicies__ResourceRepository291, availableResourceTypes_ResourceRepository292, resourceRepository__SchedulingPolicy293, networkInducedFailureType__CommunicationLinkResourceType295, resourceRepository__ResourceInterface296, parameter__ResourceSignature283, resourceInterface__ResourceSignature285, hardwareInducedFailureType__ProcessingResourceType287, resourceRepository_ResourceType288, entryLevelSystemCall_InputParameterUsage311, entryLevelSystemCall_OutputParameterUsage312, namedReference__VariableUsage314, specification_VariableCharacterisation315, variableUsage_VariableCharacterisation317, resourceSignatures__ResourceInterface298, variableCharacterisation_VariableUsage300, userData_VariableUsage302, callAction__VariableUsage304, synchronisationPoint_VariableUsage305, callReturnAction__VariableUsage306, setVariableAction_VariableUsage307, specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage308, assemblyContext__VariableUsage309, processingResourceType__HardwareInducedFailureType319, internalFailureOccurrenceDescriptions__SoftwareInducedFailureType320, passiveResource__ResourceTimeoutFailureType327, repository__FailureType329, internalAction__InternalFailureOccurrenceDescription321, softwareInducedFailureType__InternalFailureOccurrenceDescription322, communicationLinkResourceType__NetworkInducedFailureType323, specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription324, failureType__ExternalFailureOccurrenceDescription325, abstractLoopAction_ResourceDemandingBehaviour341, abstractBranchTransition_ResourceDemandingBehaviour343, steps_Behaviour344, resourceDemand_Action331, infrastructureCall__Action333, resourceCall__Action335, predecessor_AbstractAction337, successor_AbstractAction338, resourceDemandingBehaviour_AbstractAction340, branches_Branch351, inputVariableUsages__CallAction353, bodyBehaviour_Loop346, branchAction_AbstractBranchTransition348, branchBehaviour_BranchTransition349, iterationCount_LoopAction362, asynchronousForkedBehaviours_ForkAction364, synchronisingBehaviours_ForkAction365, synchronisationPoint_ForkedBehaviour367, forkAction_ForkedBehaivour369, describedService__SEFF355, basicComponent_ServiceEffectSpecification356, resourceDemandingInternalBehaviours358, resourceDemandingSEFF_ResourceDemandingInternalBehaviour359, passiveResource_ReleaseAction360, role_ExternalService378, returnVariableUsage__CallReturnAction381, outputParameterUsage_SynchronisationPoint370, forkAction_SynchronisationPoint372, synchronousForkedBehaviours_SynchronisationPoint374, calledService_ExternalService376, eventType__EmitEventAction393, sourceRole__EmitEventAction395, passiveresource_AcquireAction383, parameter_CollectionIteratorAction385, branchCondition_GuardedBranchTransition387, localVariableUsages_SetVariableAction389, calledResourceDemandingInternalBehaviour391, internalFailureOccurrenceDescriptions__InternalAction398, action__ResourceCall408, resourceRequiredRole__ResourceCall410, signature__ResourceCall412, signature__InfrastructureCall400, numberOfCalls__InfrastructureCall402, action__InfrastructureCall404, requiredRole__InfrastructureCall405, requiredResource_ParametricResourceDemand419, action_ParametricResourceDemand421, numberOfCalls__ResourceCall415, specification_ParametericResourceDemand417, primaryBehaviour__RecoveryAction425, recoveryActionBehaviours__RecoveryAction427, failureTypes_FailureHandlingEntity428, failureHandlingAlternatives__RecoveryActionBehaviour423, recoveryAction__RecoveryActionBehaviour424, specifiedOutputParameterAbstractions_QoSAnnotations435, system_QoSAnnotations437, specifiedQoSAnnotations_QoSAnnotations438, signature_SpecifiedOutputParameterAbstraction439, role_SpecifiedOutputParameterAbstraction441, expectedExternalOutputs_SpecifiedOutputParameterAbstraction444, qosAnnotations_SpecifiedOutputParameterAbstraction446, signature_SpecifiedQoSAnnation430, role_SpecifiedQoSAnnotation432, qosAnnotations_SpecifiedQoSAnnotation434, externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation452, specification_SpecifiedExecutionTime448, assemblyContext_ComponentSpecifiedExecutionTime450, communicationLinkResourceSpecifications_LinkingResource459, resourceEnvironment_LinkingResource461, activeResourceSpecifications_ResourceContainer462, qosAnnotations_System453, linkingResources__ResourceEnvironment455, resourceContainer_ResourceEnvironment456, connectedResourceContainers_LinkingResource457, schedulingPolicy470, activeResourceType_ActiveResourceSpecification472, processingRate_ProcessingResourceSpecification475, resourceContainer_ProcessingResourceSpecification477, linkingResource_CommunicationLinkResourceSpecification479, resourceEnvironment_ResourceContainer464, nestedResourceContainers__ResourceContainer466, parentResourceContainer__ResourceContainer468, resourceContainer_AllocationContext487, assemblyContext_AllocationContext489, allocation_AllocationContext492, eventChannel__AllocationContext493, communicationLinkResourceType_CommunicationLinkResourceSpecification481, latency_CommunicationLinkResourceSpecification483, throughput_CommunicationLinkResourceSpecification485, completions_CompletionRepository501, requiredCommunicationLinkResource_ParametricResourceDemand502, targetResourceEnvironment_Allocation495, system_Allocation497, allocationContexts_Allocation500},
    generalizations={gen_pcm_pc_av_core_pc_av_PCMRandomVariable_RandomVariable, gen_pcm_pc_av_entity_pc_av_ResourceProvidedRole_Role, gen_pcm_pc_av_entity_pc_av_InterfaceProvidingRequiringEntity_entity_pc_av_InterfaceProvidingEntity, gen_pcm_pc_av_entity_pc_av_InterfaceProvidingRequiringEntity_entity_pc_av_InterfaceRequiringEntity, gen_pcm_pc_av_entity_pc_av_InterfaceProvidingEntity_Entity, gen_pcm_pc_av_entity_pc_av_InterfaceRequiringEntity_entity_pc_av_Entity, gen_pcm_pc_av_entity_pc_av_InterfaceRequiringEntity_entity_pc_av_ResourceInterfaceRequiringEntity, gen_pcm_pc_av_entity_pc_av_ResourceInterfaceRequiringEntity_Entity, gen_pcm_pc_av_entity_pc_av_ResourceRequiredRole_Role, gen_pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingRequiringEntity_entity_pc_av_ResourceInterfaceRequiringEntity, gen_pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingRequiringEntity_entity_pc_av_ResourceInterfaceProvidingEntity, gen_pcm_pc_av_entity_pc_av_Entity_Identifier, gen_pcm_pc_av_entity_pc_av_Entity_entity_pc_av_NamedElement, gen_pcm_pc_av_composition_pc_av_DelegationConnector_Connector, gen_pcm_pc_av_composition_pc_av_Connector_Entity, gen_pcm_pc_av_composition_pc_av_ComposedStructure_Entity, gen_pcm_pc_av_entity_pc_av_ResourceInterfaceProvidingEntity_Entity, gen_pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity_composition_pc_av_ComposedStructure, gen_pcm_pc_av_entity_pc_av_ComposedProvidingRequiringEntity_entity_pc_av_InterfaceProvidingRequiringEntity, gen_pcm_pc_av_composition_pc_av_EventChannel_Entity, gen_pcm_pc_av_composition_pc_av_EventChannelSourceConnector_Connector, gen_pcm_pc_av_composition_pc_av_ProvidedDelegationConnector_DelegationConnector, gen_pcm_pc_av_composition_pc_av_RequiredDelegationConnector_DelegationConnector, gen_pcm_pc_av_composition_pc_av_EventChannelSinkConnector_Connector, gen_pcm_pc_av_composition_pc_av_AssemblyConnector_Connector, gen_pcm_pc_av_composition_pc_av_AssemblyEventConnector_Connector, gen_pcm_pc_av_composition_pc_av_SourceDelegationConnector_DelegationConnector, gen_pcm_pc_av_composition_pc_av_SinkDelegationConnector_DelegationConnector, gen_pcm_pc_av_composition_pc_av_ProvidedInfrastructureDelegationConnector_DelegationConnector, gen_pcm_pc_av_composition_pc_av_RequiredInfrastructureDelegationConnector_DelegationConnector, gen_pcm_pc_av_composition_pc_av_RequiredResourceDelegationConnector_DelegationConnector, gen_pcm_pc_av_composition_pc_av_AssemblyContext_Entity, gen_pcm_pc_av_composition_pc_av_AssemblyInfrastructureConnector_Connector, gen_pcm_pc_av_usagemodel_pc_av_AbstractUserAction_Entity, gen_pcm_pc_av_usagemodel_pc_av_ScenarioBehaviour_Entity, gen_pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall_AbstractUserAction, gen_pcm_pc_av_usagemodel_pc_av_UsageScenario_Entity, gen_pcm_pc_av_usagemodel_pc_av_Branch_AbstractUserAction, gen_pcm_pc_av_usagemodel_pc_av_OpenWorkload_Workload, gen_pcm_pc_av_usagemodel_pc_av_Loop_AbstractUserAction, gen_pcm_pc_av_usagemodel_pc_av_Stop_AbstractUserAction, gen_pcm_pc_av_usagemodel_pc_av_Start_AbstractUserAction, gen_pcm_pc_av_repository_pc_av_BasicComponent_ImplementationComponentType, gen_pcm_pc_av_usagemodel_pc_av_Delay_AbstractUserAction, gen_pcm_pc_av_usagemodel_pc_av_ClosedWorkload_Workload, gen_pcm_pc_av_repository_pc_av_PassiveResource_Entity, gen_pcm_pc_av_repository_pc_av_ImplementationComponentType_RepositoryComponent, gen_pcm_pc_av_repository_pc_av_Repository_Entity, gen_pcm_pc_av_repository_pc_av_RepositoryComponent_InterfaceProvidingRequiringEntity, gen_pcm_pc_av_repository_pc_av_ProvidedRole_Role, gen_pcm_pc_av_repository_pc_av_EventGroup_Interface, gen_pcm_pc_av_repository_pc_av_Interface_Entity, gen_pcm_pc_av_repository_pc_av_InfrastructureSignature_Signature, gen_pcm_pc_av_repository_pc_av_InfrastructureInterface_Interface, gen_pcm_pc_av_repository_pc_av_InfrastructureRequiredRole_RequiredRole, gen_pcm_pc_av_repository_pc_av_EventType_Signature, gen_pcm_pc_av_repository_pc_av_Signature_Entity, gen_pcm_pc_av_repository_pc_av_OperationRequiredRole_RequiredRole, gen_pcm_pc_av_repository_pc_av_SourceRole_RequiredRole, gen_pcm_pc_av_repository_pc_av_SinkRole_ProvidedRole, gen_pcm_pc_av_repository_pc_av_OperationProvidedRole_ProvidedRole, gen_pcm_pc_av_repository_pc_av_RequiredRole_Role, gen_pcm_pc_av_repository_pc_av_OperationSignature_Signature, gen_pcm_pc_av_repository_pc_av_OperationInterface_Interface, gen_pcm_pc_av_repository_pc_av_ProvidesComponentType_RepositoryComponent, gen_pcm_pc_av_repository_pc_av_CompositeComponent_entity_pc_av_ComposedProvidingRequiringEntity, gen_pcm_pc_av_repository_pc_av_CompositeComponent_repository_pc_av_ImplementationComponentType, gen_pcm_pc_av_repository_pc_av_InfrastructureProvidedRole_ProvidedRole, gen_pcm_pc_av_repository_pc_av_CompleteComponentType_RepositoryComponent, gen_pcm_pc_av_repository_pc_av_CompositeDataType_entity_pc_av_Entity, gen_pcm_pc_av_repository_pc_av_CompositeDataType_repository_pc_av_DataType, gen_pcm_pc_av_repository_pc_av_InnerDeclaration_NamedElement, gen_pcm_pc_av_repository_pc_av_Role_Entity, gen_pcm_pc_av_repository_pc_av_PrimitiveDataType_DataType, gen_pcm_pc_av_repository_pc_av_CollectionDataType_entity_pc_av_Entity, gen_pcm_pc_av_repository_pc_av_CollectionDataType_repository_pc_av_DataType, gen_pcm_pc_av_resourcetype_pc_av_SchedulingPolicy_Entity, gen_pcm_pc_av_resourcetype_pc_av_CommunicationLinkResourceType_ResourceType, gen_pcm_pc_av_resourcetype_pc_av_ResourceInterface_Entity, gen_pcm_pc_av_resourcetype_pc_av_ResourceSignature_Entity, gen_pcm_pc_av_resourcetype_pc_av_ProcessingResourceType_ResourceType, gen_pcm_pc_av_resourcetype_pc_av_ResourceType_entity_pc_av_Entity, gen_pcm_pc_av_resourcetype_pc_av_ResourceType_UnitCarryingElement, gen_pcm_pc_av_resourcetype_pc_av_ResourceType_entity_pc_av_ResourceInterfaceProvidingEntity, gen_pcm_pc_av_parameter_pc_av_CharacterisedVariable_Variable, gen_pcm_pc_av_reliability_pc_av_SoftwareInducedFailureType_FailureType, gen_pcm_pc_av_reliability_pc_av_InternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_pc_av_reliability_pc_av_HardwareInducedFailureType_FailureType, gen_pcm_pc_av_reliability_pc_av_ResourceTimeoutFailureType_SoftwareInducedFailureType, gen_pcm_pc_av_reliability_pc_av_FailureType_Entity, gen_pcm_pc_av_seff_pc_av_StopAction_AbstractInternalControlFlowAction, gen_pcm_pc_av_reliability_pc_av_NetworkInducedFailureType_FailureType, gen_pcm_pc_av_reliability_pc_av_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_pc_av_seff_pc_av_AbstractInternalControlFlowAction_AbstractAction, gen_pcm_pc_av_seff_pc_av_AbstractAction_Entity, gen_pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour_Identifier, gen_pcm_pc_av_seff_pc_av_StartAction_AbstractInternalControlFlowAction, gen_pcm_pc_av_seff_pc_av_AbstractLoopAction_AbstractInternalControlFlowAction, gen_pcm_pc_av_seff_pc_av_AbstractBranchTransition_Entity, gen_pcm_pc_av_seff_pc_av_BranchAction_AbstractInternalControlFlowAction, gen_pcm_pc_av_seff_pc_av_LoopAction_AbstractLoopAction, gen_pcm_pc_av_seff_pc_av_ForkAction_AbstractInternalControlFlowAction, gen_pcm_pc_av_seff_pc_av_ForkedBehaviour_ResourceDemandingBehaviour, gen_pcm_pc_av_seff_pc_av_ResourceDemandingSEFF_Identifier, gen_pcm_pc_av_seff_pc_av_ResourceDemandingSEFF_seff_pc_av_ServiceEffectSpecification, gen_pcm_pc_av_seff_pc_av_ResourceDemandingSEFF_seff_pc_av_ResourceDemandingBehaviour, gen_pcm_pc_av_seff_pc_av_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour, gen_pcm_pc_av_seff_pc_av_ReleaseAction_AbstractInternalControlFlowAction, gen_pcm_pc_av_seff_pc_av_CallReturnAction_CallAction, gen_pcm_pc_av_seff_pc_av_ProbabilisticBranchTransition_AbstractBranchTransition, gen_pcm_pc_av_seff_pc_av_AcquireAction_AbstractInternalControlFlowAction, gen_pcm_pc_av_seff_pc_av_ExternalCallAction_seff_pc_av_AbstractAction, gen_pcm_pc_av_seff_pc_av_ExternalCallAction_seff_pc_av_CallReturnAction, gen_pcm_pc_av_seff_pc_av_ExternalCallAction_seff_reliability_pc_av_FailureHandlingEntity, gen_pcm_pc_av_seff_pc_av_EmitEventAction_seff_pc_av_AbstractAction, gen_pcm_pc_av_seff_pc_av_EmitEventAction_seff_pc_av_CallAction, gen_pcm_pc_av_seff_pc_av_InternalAction_AbstractInternalControlFlowAction, gen_pcm_pc_av_seff_pc_av_CollectionIteratorAction_AbstractLoopAction, gen_pcm_pc_av_seff_pc_av_GuardedBranchTransition_AbstractBranchTransition, gen_pcm_pc_av_seff_pc_av_SetVariableAction_AbstractInternalControlFlowAction, gen_pcm_pc_av_seff_pc_av_InternalCallAction_seff_pc_av_CallAction, gen_pcm_pc_av_seff_pc_av_InternalCallAction_seff_pc_av_AbstractInternalControlFlowAction, gen_pcm_pc_av_seff_performance_pc_av_InfrastructureCall_CallAction, gen_pcm_pc_av_seff_performance_pc_av_ResourceCall_CallAction, gen_pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour_seff_reliability_pc_av_FailureHandlingEntity, gen_pcm_pc_av_seff_reliability_pc_av_RecoveryActionBehaviour_seff_pc_av_ResourceDemandingBehaviour, gen_pcm_pc_av_seff_reliability_pc_av_FailureHandlingEntity_Entity, gen_pcm_pc_av_seff_reliability_pc_av_RecoveryAction_AbstractInternalControlFlowAction, gen_pcm_pc_av_qosannotations_pc_av_QoSAnnotations_Entity, gen_pcm_pc_av_qos_performance_pc_av_SystemSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_pc_av_qos_performance_pc_av_SpecifiedExecutionTime_SpecifiedQoSAnnotation, gen_pcm_pc_av_qos_performance_pc_av_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_pc_av_qos_reliability_pc_av_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation, gen_pcm_pc_av_resourceenvironment_pc_av_ResourceContainer_Entity, gen_pcm_pc_av_system_pc_av_System_entity_pc_av_Entity, gen_pcm_pc_av_system_pc_av_System_entity_pc_av_ComposedProvidingRequiringEntity, gen_pcm_pc_av_resourceenvironment_pc_av_ResourceEnvironment_NamedElement, gen_pcm_pc_av_resourceenvironment_pc_av_LinkingResource_Entity, gen_pcm_pc_av_resourceenvironment_pc_av_CommunicationLinkResourceSpecification_Identifier, gen_pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification_Identifier, gen_pcm_pc_av_allocation_pc_av_AllocationContext_Entity, gen_pcm_pc_av_completions_pc_av_DelegatingExternalCallAction_ExternalCallAction, gen_pcm_pc_av_completions_pc_av_NetworkDemandParametricResourceDemand_ParametricResourceDemand, gen_pcm_pc_av_allocation_pc_av_Allocation_Entity, gen_pcm_pc_av_subsystem_pc_av_SubSystem_entity_pc_av_ComposedProvidingRequiringEntity, gen_pcm_pc_av_subsystem_pc_av_SubSystem_repository_pc_av_RepositoryComponent, gen_pcm_pc_av_completions_pc_av_Completion_entity_pc_av_ComposedProvidingRequiringEntity, gen_pcm_pc_av_completions_pc_av_Completion_repository_pc_av_ImplementationComponentType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)